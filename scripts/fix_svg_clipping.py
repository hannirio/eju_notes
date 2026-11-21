#!/usr/bin/env python3
"""
Fix SVG clipping and global CSS style collisions in EJU solution HTML files.

Root causes addressed:
1. Inline <style> tags inside <svg> elements are global in HTML5. When multiple SVGs
   define the same class names (.title, .lbl, .note, .axis, .math, etc.), later SVGs
   overwrite earlier ones (e.g. forcing text-anchor: middle on x=16 left-aligned labels,
   clipping the left half of text outside the viewBox).
   Fix: Scope every <svg>'s inline <style> rules with svg[data-svg-scope="sN"].
2. Any SVG whose actual rendered content (measured via Chrome getBBox()) extends beyond
   its viewBox gets its viewBox (and matching width/height aspect ratio) expanded with
   clean padding so 100% of every diagram is visible without clipping.
"""

import re
import sys
import threading
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parent.parent
TARGET_FILES = [
    ROOT / "eju_math_solutions.html",
    ROOT / "eju_physics_solutions.html",
    ROOT / "eju_chemistry_solutions.html",
]


class QuietHandler(SimpleHTTPRequestHandler):
    def log_message(self, *args):
        pass


def scope_css(css_text: str, scope_attr: str) -> str:
    """Prefix every CSS selector in css_text with svg[data-svg-scope="<scope_attr>"]."""
    prefix = f'svg[data-svg-scope="{scope_attr}"]'
    # Strip CSS comments
    cleaned = re.sub(r"/\*.*?\*/", "", css_text, flags=re.S)

    def repl_rule(m):
        sel_block = m.group(1)
        body = m.group(2)
        selectors = [s.strip() for s in sel_block.split(",") if s.strip()]
        scoped = []
        for sel in selectors:
            if sel.startswith("svg[data-svg-scope="):
                scoped.append(sel)
            elif sel == "svg":
                scoped.append(prefix)
            elif sel.startswith("svg.") or sel.startswith("svg#") or sel.startswith("svg:"):
                scoped.append(f"{prefix}{sel[3:]}")
            else:
                scoped.append(f"{prefix} {sel}")
        return f"{', '.join(scoped)} {{{body}}}"

    return re.sub(r"([^{}]+)\{([^{}]*)\}", repl_rule, cleaned)


def scope_svg_styles_in_html(html: str) -> tuple[str, int]:
    """Scope all <style> blocks inside <svg> tags."""
    scoped_count = 0
    svg_idx = 0

    def repl_svg(m):
        nonlocal scoped_count, svg_idx
        svg_str = m.group(0)
        idx = svg_idx
        svg_idx += 1

        if "<style" not in svg_str.lower():
            return svg_str

        scope_id = f"s{idx}"
        # Add data-svg-scope to <svg ...> opening tag if not present
        open_tag_m = re.match(r"<svg\b[^>]*>", svg_str, flags=re.I)
        if not open_tag_m:
            return svg_str
        open_tag = open_tag_m.group(0)
        if "data-svg-scope=" in open_tag:
            existing = re.search(r'data-svg-scope="([^"]+)"', open_tag)
            if existing:
                scope_id = existing.group(1)
        else:
            new_open_tag = open_tag[:-1] + f' data-svg-scope="{scope_id}">'
            svg_str = new_open_tag + svg_str[len(open_tag):]

        def repl_style(sm):
            style_open = sm.group(1)
            style_body = sm.group(2)
            style_close = sm.group(3)
            return style_open + scope_css(style_body, scope_id) + style_close

        svg_str = re.sub(
            r"(<style\b[^>]*>)(.*?)(</style>)",
            repl_style,
            svg_str,
            flags=re.S | re.I,
        )
        scoped_count += 1
        return svg_str

    new_html = re.sub(r"<svg\b[^>]*>.*?</svg>", repl_svg, html, flags=re.S | re.I)
    return new_html, scoped_count


MEASURE_JS = """() => {
    const svgs = Array.from(document.querySelectorAll('svg')).filter(s => !s.closest('.katex'));
    const out = [];
    svgs.forEach((svg, idx) => {
        const sr = svg.getBoundingClientRect();
        if (sr.width === 0 || sr.height === 0) return;

        let vbAttr = svg.getAttribute('viewBox');
        let vb = vbAttr ? vbAttr.trim().split(/[\\s,]+/).map(Number) : null;
        if (!vb || vb.length !== 4 || vb.some(isNaN)) {
            const w = parseFloat(svg.getAttribute('width')) || sr.width;
            const h = parseFloat(svg.getAttribute('height')) || sr.height;
            vb = [0, 0, w, h];
        }

        let bbox;
        try {
            bbox = svg.getBBox();
        } catch (e) {
            return;
        }
        if (!bbox || (bbox.width === 0 && bbox.height === 0)) return;

        // Also check individual text elements in case getBBox misses anything or for diagnostics
        const vbX = vb[0], vbY = vb[1], vbW = vb[2], vbH = vb[3];
        const minX = bbox.x;
        const minY = bbox.y;
        const maxX = bbox.x + bbox.width;
        const maxY = bbox.y + bbox.height;

        const overflowLeft = Math.max(0, vbX - minX);
        const overflowTop = Math.max(0, vbY - minY);
        const overflowRight = Math.max(0, maxX - (vbX + vbW));
        const overflowBottom = Math.max(0, maxY - (vbY + vbH));

        if (overflowLeft > 1 || overflowTop > 1 || overflowRight > 1 || overflowBottom > 1 || !vbAttr) {
            out.push({
                idx,
                hasViewBox: !!vbAttr,
                vb,
                bbox: [minX, minY, bbox.width, bbox.height],
                overflow: [overflowLeft, overflowTop, overflowRight, overflowBottom],
                widthAttr: svg.getAttribute('width'),
                heightAttr: svg.getAttribute('height'),
            });
        }
    });
    return { total: svgs.length, clipped: out };
}"""


def expand_clipped_viewboxes(html: str, clipped_items: list, pad: float = 10.0) -> tuple[str, int]:
    """Expand viewBox (and proportionally adjust width/height) for clipped SVGs."""
    svg_matches = list(re.finditer(r"<svg\b[^>]*>.*?</svg>", html, flags=re.S | re.I))
    replacements = {}

    for item in clipped_items:
        idx = item["idx"]
        if idx >= len(svg_matches):
            continue
        svg_str = svg_matches[idx].group(0)
        open_m = re.match(r"<svg\b[^>]*>", svg_str, flags=re.I)
        if not open_m:
            continue
        open_tag = open_m.group(0)

        vbX, vbY, vbW, vbH = item["vb"]
        bx, by, bw, bh = item["bbox"]

        new_x = min(vbX, bx - pad)
        new_y = min(vbY, by - pad)
        new_r = max(vbX + vbW, bx + bw + pad)
        new_b = max(vbY + vbH, by + bh + pad)
        new_w = new_r - new_x
        new_h = new_b - new_y

        new_vb = f"{new_x:.1f} {new_y:.1f} {new_w:.1f} {new_h:.1f}"
        new_open = open_tag
        if re.search(r'\bviewBox="[^"]*"', new_open, flags=re.I):
            new_open = re.sub(r'\bviewBox="[^"]*"', f'viewBox="{new_vb}"', new_open, count=1, flags=re.I)
        else:
            new_open = new_open[:-1] + f' viewBox="{new_vb}">'

        # Update width/height attributes proportionally if present so aspect ratio stays 1:1
        if re.search(r'\bwidth="[^"]*"', new_open, flags=re.I) and vbW > 0:
            w_m = re.search(r'\bwidth="([0-9.]+)(px)?"', new_open, flags=re.I)
            if w_m:
                old_w = float(w_m.group(1))
                scaled_w = round(old_w * (new_w / vbW))
                unit = w_m.group(2) or ""
                new_open = re.sub(r'\bwidth="[^"]*"', f'width="{scaled_w}{unit}"', new_open, count=1, flags=re.I)
        if re.search(r'\bheight="[^"]*"', new_open, flags=re.I) and vbH > 0:
            h_m = re.search(r'\bheight="([0-9.]+)(px)?"', new_open, flags=re.I)
            if h_m:
                old_h = float(h_m.group(1))
                scaled_h = round(old_h * (new_h / vbH))
                unit = h_m.group(2) or ""
                new_open = re.sub(r'\bheight="[^"]*"', f'height="{scaled_h}{unit}"', new_open, count=1, flags=re.I)

        replacements[idx] = new_open + svg_str[len(open_tag):]

    if not replacements:
        return html, 0

    parts = []
    last = 0
    for idx, m in enumerate(svg_matches):
        if idx in replacements:
            parts.append(html[last:m.start()])
            parts.append(replacements[idx])
            last = m.end()
    parts.append(html[last:])
    return "".join(parts), len(replacements)


def main():
    # Step 1: Scope inline SVG <style> tags
    for path in TARGET_FILES:
        if not path.exists():
            continue
        raw = path.read_text(encoding="utf-8")
        new_html, scoped = scope_svg_styles_in_html(raw)
        if scoped > 0 and new_html != raw:
            path.write_text(new_html, encoding="utf-8")
            print(f"[{path.name}] Scoped inline <style> in {scoped} SVGs.")
        else:
            print(f"[{path.name}] No unscoped inline SVG <style> tags found.")

    # Step 2: Measure all SVGs in Chrome via Playwright and expand clipped viewBoxes
    handler = partial(QuietHandler, directory=str(ROOT))
    server = ThreadingHTTPServer(("127.0.0.1", 0), handler)
    port = server.server_address[1]
    t = threading.Thread(target=server.serve_forever, daemon=True)
    t.start()

    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(channel="chrome", headless=True)
            page = browser.new_page(viewport={"width": 1400, "height": 900})

            for path in TARGET_FILES:
                if not path.exists():
                    continue
                url = f"http://127.0.0.1:{port}/{path.name}"
                page.goto(url, wait_until="load", timeout=60000)
                page.wait_for_timeout(500)

                res = page.evaluate(MEASURE_JS)
                clipped = res["clipped"]
                print(f"[{path.name}] Total SVGs: {res['total']}, Clipped/overflowing: {len(clipped)}")
                for item in clipped[:15]:
                    ov = [round(v, 1) for v in item["overflow"]]
                    print(f"   SVG #{item['idx']}: vb={item['vb']} overflow(L,T,R,B)={ov}")

                if clipped:
                    raw = path.read_text(encoding="utf-8")
                    fixed_html, count = expand_clipped_viewboxes(raw, clipped, pad=10.0)
                    if count > 0:
                        path.write_text(fixed_html, encoding="utf-8")
                        print(f"[{path.name}] Expanded viewBox on {count} SVGs.")

                    # Re-verify in Chrome
                    page.goto(url, wait_until="load", timeout=60000)
                    page.wait_for_timeout(500)
                    res2 = page.evaluate(MEASURE_JS)
                    print(f"[{path.name}] After fix — Clipped/overflowing remaining: {len(res2['clipped'])}")

            browser.close()
    finally:
        server.shutdown()


if __name__ == "__main__":
    main()
