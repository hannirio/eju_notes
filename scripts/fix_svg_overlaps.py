#!/usr/bin/env python3
"""
Geometry-guided SVG <text> overlap resolver using Playwright + Chrome.
For each diagram <svg> in Math, Physics, and Chemistry HTMLs:
  1. Measures exact rendered bounding boxes of all <text> elements via Chrome.
  2. Removes exact duplicate overlaid <text> labels (same text + >85% overlap).
  3. Nudges overlapping <text> labels minimally along X (for same-row annotations)
     or Y (for stacked labels) in viewBox coordinates, expanding viewBox if needed.
  4. Re-verifies in Chrome up to 4 passes until 0 overlaps remain.
"""

import re
import threading
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parent.parent
FILES = [
    ("math", ROOT / "eju_math_solutions.html"),
    ("physics", ROOT / "eju_physics_solutions.html"),
    ("chemistry", ROOT / "eju_chemistry_solutions.html"),
]


class QuietHandler(SimpleHTTPRequestHandler):
    def log_message(self, *a):
        pass


DETECT_JS = """() => {
    const svgs = Array.from(document.querySelectorAll('svg')).filter(s => !s.closest('.katex'));
    const results = [];
    svgs.forEach((svg, sIdx) => {
        const sr = svg.getBoundingClientRect();
        if (sr.width === 0 || sr.height === 0) return;
        const vb = (svg.getAttribute('viewBox') || '').trim().split(/[\\s,]+/).map(Number);
        const vbW = vb.length === 4 ? vb[2] : sr.width;
        const vbH = vb.length === 4 ? vb[3] : sr.height;
        const scaleX = vbW / sr.width;
        const scaleY = vbH / sr.height;

        const textEls = Array.from(svg.querySelectorAll('text'));
        const items = textEls.map((el, tIdx) => ({
            tIdx,
            txt: el.textContent.trim(),
            rect: el.getBoundingClientRect(),
            xAttr: el.getAttribute('x'),
            yAttr: el.getAttribute('y'),
            anchor: el.getAttribute('text-anchor') || 'start',
        })).filter(it => it.txt.length > 0 && it.rect.width > 2 && it.rect.height > 2);

        const overlaps = [];
        for (let i = 0; i < items.length; i++) {
            for (let j = i + 1; j < items.length; j++) {
                const a = items[i], b = items[j];
                const ix = Math.max(0, Math.min(a.rect.right, b.rect.right) - Math.max(a.rect.left, b.rect.left));
                const iy = Math.max(0, Math.min(a.rect.bottom, b.rect.bottom) - Math.max(a.rect.top, b.rect.top));
                const inter = ix * iy;
                const minA = Math.min(a.rect.width * a.rect.height, b.rect.width * b.rect.height);
                if (ix > 4 && iy > 4 && minA > 0 && (inter / minA) > 0.25) {
                    overlaps.push({
                        iIdx: a.tIdx, jIdx: b.tIdx,
                        iTxt: a.txt, jTxt: b.txt,
                        ratio: inter / minA,
                        ix, iy,
                        aRect: { l: a.rect.left, r: a.rect.right, t: a.rect.top, b: a.rect.bottom, w: a.rect.width, h: a.rect.height },
                        bRect: { l: b.rect.left, r: b.rect.right, t: b.rect.top, b: b.rect.bottom, w: b.rect.width, h: b.rect.height },
                    });
                }
            }
        }
        if (overlaps.length > 0) {
            results.push({ sIdx, vb, scaleX, scaleY, overlaps });
        }
    });
    return results;
}"""


def parse_num(val, default=0.0):
    if val is None:
        return default
    m = re.match(r"\s*([+-]?\d+(?:\.\d+)?)", str(val))
    return float(m.group(1)) if m else default


def apply_adjustments(path: Path, issues: list) -> tuple[int, int]:
    """Apply minimal coordinate shifts or duplicate removal to diagram SVGs in HTML."""
    raw = path.read_text(encoding="utf-8")
    # Extract all <svg ...>...</svg> blocks from raw HTML (only inline diagram SVGs exist in static HTML)
    svg_matches = list(re.finditer(r"<svg\b[^>]*>.*?</svg>", raw, flags=re.S | re.I))

    removed_dups = 0
    nudged = 0
    replacements = {}

    for iss in issues:
        sIdx = iss["sIdx"]
        if sIdx >= len(svg_matches):
            continue
        svg_str = svg_matches[sIdx].group(0)
        soup = BeautifulSoup(svg_str, "xml")
        svg_el = soup.find("svg")
        if not svg_el:
            continue
        text_els = svg_el.find_all("text")
        scaleX = iss["scaleX"]
        scaleY = iss["scaleY"]
        vb = iss["vb"]  # [minX, minY, vbW, vbH]

        moved_indices = set()
        to_remove = set()

        for ov in iss["overlaps"]:
            iIdx, jIdx = ov["iIdx"], ov["jIdx"]
            if iIdx in to_remove or jIdx in to_remove:
                continue
            if iIdx >= len(text_els) or jIdx >= len(text_els):
                continue

            # Case 1: Exact duplicate label overlaid on itself
            if ov["iTxt"] == ov["jTxt"] and ov["ratio"] > 0.80:
                to_remove.add(jIdx)
                removed_dups += 1
                continue

            # Only move jIdx once per pass to avoid oscillation
            target_idx = jIdx if jIdx not in moved_indices else (iIdx if iIdx not in moved_indices else None)
            if target_idx is None:
                continue
            moved_indices.add(target_idx)

            t_el = text_els[target_idx]
            aR, bR = ov["aRect"], ov["bRect"]
            same_row = abs((aR["t"] + aR["b"]) / 2 - (bR["t"] + bR["b"]) / 2) < min(aR["h"], bR["h"]) * 0.55

            # Prefer horizontal shift for right-hand annotations (arrows, comments) on the same row
            if same_row and target_idx == jIdx and (bR["l"] >= aR["l"] - 2 or "←" in ov["jTxt"] or "⋯" in ov["jTxt"]):
                dx = (aR["r"] - bR["l"] + 8.0) * scaleX
                cur_x = parse_num(t_el.get("x"), 0.0)
                new_x = round(cur_x + dx, 1)
                t_el["x"] = str(new_x)
                # Expand viewBox width if text might clip right edge
                if len(vb) == 4:
                    est_right = new_x + bR["w"] * scaleX + 12
                    if est_right > vb[0] + vb[2]:
                        vb[2] = round(est_right - vb[0], 1)
                        svg_el["viewBox"] = " ".join(str(v) for v in vb)
                nudged += 1
            else:
                # Vertical nudge: move lower/second label down (or upper label up if near top)
                dy = (ov["iy"] + 6.0) * scaleY
                cur_y = parse_num(t_el.get("y"), 0.0)
                if bR["t"] < aR["t"] and cur_y - dy > (vb[1] + 12 if len(vb) == 4 else 12):
                    new_y = round(cur_y - dy, 1)
                else:
                    new_y = round(cur_y + dy, 1)
                t_el["y"] = str(new_y)
                if len(vb) == 4 and new_y + 10 > vb[1] + vb[3]:
                    vb[3] = round(new_y + 12 - vb[1], 1)
                    svg_el["viewBox"] = " ".join(str(v) for v in vb)
                nudged += 1

        for idx in sorted(to_remove, reverse=True):
            text_els[idx].decompose()

        # Serialize back cleanly without <?xml ...?> header
        fixed_svg = str(svg_el)
        replacements[sIdx] = fixed_svg

    if not replacements:
        return 0, 0

    # Rebuild HTML string from back to front so offsets stay valid
    parts = []
    last = 0
    for idx, m in enumerate(svg_matches):
        if idx in replacements:
            parts.append(raw[last:m.start()])
            parts.append(replacements[idx])
            last = m.end()
    parts.append(raw[last:])
    path.write_text("".join(parts), encoding="utf-8")
    return removed_dups, nudged


def main():
    server = ThreadingHTTPServer(("127.0.0.1", 0), partial(QuietHandler, directory=str(ROOT)))
    port = server.server_address[1]
    threading.Thread(target=server.serve_forever, daemon=True).start()

    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(channel="chrome", headless=True)
            for subj, path in FILES:
                url = f"http://127.0.0.1:{port}/{path.name}"
                page = browser.new_page(viewport={"width": 1440, "height": 900})
                for pass_num in range(1, 5):
                    page.goto(url, wait_until="networkidle", timeout=60000)
                    page.wait_for_timeout(800)
                    issues = page.evaluate(DETECT_JS)
                    if not issues:
                        print(f"[{subj.upper()}] Pass {pass_num}: 0 SVG text overlaps remaining!", flush=True)
                        break
                    dups, nudged = apply_adjustments(path, issues)
                    print(
                        f"[{subj.upper()}] Pass {pass_num}: found {len(issues)} SVGs with overlaps "
                        f"-> removed {dups} duplicates, nudged {nudged} labels",
                        flush=True,
                    )
                else:
                    page.goto(url, wait_until="networkidle", timeout=60000)
                    page.wait_for_timeout(800)
                    rem = page.evaluate(DETECT_JS)
                    print(f"[{subj.upper()}] Final remaining SVG overlaps: {len(rem)}", flush=True)
                page.close()
            browser.close()
    finally:
        server.shutdown()


if __name__ == "__main__":
    main()
