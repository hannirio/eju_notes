#!/usr/bin/env python3
"""
Automated QA & Rendering Inspection for EJU Math, Physics, and Chemistry HTML Solutions.
Combines static HTML/regex analysis with live headless Chrome (Playwright) rendering checks.
Outputs a structured JSON report and prints a concise summary.
"""

import json
import os
import re
import sys
import threading
from collections import Counter
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parent.parent
FILES = {
    "math": ROOT / "eju_math_solutions.html",
    "physics": ROOT / "eju_physics_solutions.html",
    "chemistry": ROOT / "eju_chemistry_solutions.html",
}

REPORT_JSON = ROOT / "scripts" / "qa_report.json"


class QuietHandler(SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        pass


def start_local_server(directory: Path):
    handler = partial(QuietHandler, directory=str(directory))
    server = ThreadingHTTPServer(("127.0.0.1", 0), handler)
    port = server.server_address[1]
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    return server, port


def static_check(subject: str, path: Path) -> dict:
    raw = path.read_text(encoding="utf-8")
    soup = BeautifulSoup(raw, "lxml")

    res = {
        "file": path.name,
        "size_bytes": len(raw.encode("utf-8")),
        "latex_static": {},
        "svg_static": {},
        "modules": {},
        "anchors": {},
    }

    # --- 1. Static LaTeX & Chem Check ---
    # Check raw unclosed $$ or $ inside main content text nodes (excluding script, style, code, pre, svg)
    unclosed_dollar_snippets = []
    chem_garble_snippets = []
    # Strip script/style/svg/code/pre for text inspection
    body = soup.body
    if body:
        # Walk leaf text nodes in main content (avoid sidebar)
        main_el = body.find("main") or body.find(id="main") or body.find(class_=re.compile("main|content")) or body
        # Check paragraph/li/td/blockquote/div blocks
        for el in main_el.find_all(["p", "li", "td", "th", "blockquote", "h1", "h2", "h3", "h4"]):
            if el.find(["p", "li", "td", "blockquote"]):
                continue
            if el.find_parent(["svg", "pre", "code", "script", "style", "aside", "nav"]):
                continue
            txt = el.get_text(" ", strip=True)
            if not txt:
                continue
            # Remove escaped \$ and currency like $100
            cleaned = re.sub(r"\\\$", "", txt)
            # Check $$ parity
            dd_count = len(re.findall(r"\$\$", cleaned))
            if dd_count % 2 != 0:
                unclosed_dollar_snippets.append({"type": "unclosed_$$", "text": txt[:140]})
            # Remove $$...$$ pairs then check single $ parity
            no_dd = re.sub(r"\$\$.*?\$\$", "", cleaned, flags=re.S)
            single_d = len(re.findall(r"(?<!\$)\$(?!\$)", no_dd))
            if single_d % 2 != 0:
                unclosed_dollar_snippets.append({"type": "unclosed_$", "text": txt[:140]})

            # Check chemical formula garble outside $...$ (e.g. H_2O, SO_4^{2-}, \ce{)
            # Exclude <code> elements which may contain literal OCR quotes
            el_clone = BeautifulSoup(str(el), "lxml")
            for c in el_clone.find_all("code"):
                c.decompose()
            txt_nocode = el_clone.get_text(" ", strip=True)
            no_math = re.sub(r"\$\$.*?\$\$", "", re.sub(r"\\\$", "", txt_nocode), flags=re.S)
            no_math = re.sub(r"\$[^$\n]+?\$", "", no_math)
            no_math = re.sub(r"\\\(.*?\\\)", "", no_math, flags=re.S)
            no_math = re.sub(r"\\\[.*?\\\]", "", no_math, flags=re.S)
            if re.search(r"\\(?:frac|sqrt|ce|text|mathrm|rightarrow|rightleftharpoons|Delta|sum|int)\b", no_math):
                chem_garble_snippets.append({"type": "raw_latex_outside_math", "text": txt[:160]})
            elif subject == "chemistry" and re.search(r"\b(?:H_2O|CO_2|SO_4|NH_3|Na_2|Ca\(OH\)_2|CH_3|C_2H_5|Fe_2O_3)\b", no_math):
                chem_garble_snippets.append({"type": "unrendered_chem_sub", "text": txt[:160]})

    res["latex_static"] = {
        "unclosed_dollar_count": len(unclosed_dollar_snippets),
        "unclosed_dollar_samples": unclosed_dollar_snippets[:15],
        "raw_latex_or_chem_garble_count": len(chem_garble_snippets),
        "raw_latex_or_chem_garble_samples": chem_garble_snippets[:15],
    }

    # --- 2. Static SVG Check ---
    svg_open_count = len(re.findall(r"<svg\b", raw, re.I))
    svg_close_count = len(re.findall(r"</svg>", raw, re.I))
    svgs = soup.find_all("svg")
    missing_viewbox = []
    for idx, svg in enumerate(svgs, 1):
        vb = svg.get("viewbox") or svg.get("viewBox")
        if not vb:
            missing_viewbox.append({"svg_index": idx, "attrs": dict(svg.attrs)})
    res["svg_static"] = {
        "open_tags": svg_open_count,
        "close_tags": svg_close_count,
        "tag_balanced": svg_open_count == svg_close_count,
        "parsed_svg_count": len(svgs),
        "missing_viewbox_count": len(missing_viewbox),
        "missing_viewbox_samples": missing_viewbox[:10],
    }

    # --- 3. Teaching Modules & Anti-Laziness Check ---
    # Find problem headings depending on subject structure
    problem_heading_re = re.compile(
        r"^(?:\d+(?:\.\d+)*\s+)?(?:演習問題|例[題题]|練習問題|練習|基本問題|発展問題|確認問題|問題|問\s*\d+|演[习習][题題]|Exercise|Problem|【例[題题]|【演習)",
        re.I,
    )
    problems = []
    main_el = soup.find("main") or soup.find(id="main") or soup.find(class_=re.compile("main|content")) or soup.body
    if main_el:
        headings = main_el.find_all(["h3", "h4"])
        for h in headings:
            htxt = h.get_text(" ", strip=True)
            if not problem_heading_re.search(htxt):
                continue
            # Avoid matching sub-module headers like "【原题重现与翻译】"
            if htxt.startswith("【") and any(k in htxt for k in ["原题", "考点", "解答", "答案", "图解"]):
                continue
            level = int(h.name[1])
            # Collect sibling text until next heading of same or higher level
            chunks = []
            sib = h.find_next_sibling()
            while sib is not None:
                if sib.name in ("h1", "h2", "h3", "h4") and int(sib.name[1]) <= level:
                    break
                chunks.append(sib.get_text(" ", strip=True))
                sib = sib.find_next_sibling()
            block_txt = "\n".join(chunks)
            if len(block_txt) < 30:
                continue

            has_orig_trans = bool(re.search(r"原[题題]|翻[译譯]", block_txt))
            has_topic = bool(re.search(r"考[点點]|思路|模型定位", block_txt))
            has_steps = bool(re.search(r"分步|解答|解[析答]|推[导導]|Step\s*1|解：", block_txt))
            has_comment = bool(re.search(r"[讲講][师師]批注|批注|避坑|易[错錯]|注意|提醒", block_txt))
            has_answer = bool(re.search(r"最[终終]答案|答案[：:]|答[：:]", block_txt))

            missing = []
            if not has_orig_trans: missing.append("原题与翻译")
            if not has_topic: missing.append("考点定位")
            if not has_steps: missing.append("分步解答")
            if not has_comment: missing.append("讲师批注")
            if not has_answer: missing.append("最终答案")

            # Laziness detection (carefully avoiding legit terms like 省略记号, 略图, 攻略, 策略, 略去乘号)
            lazy_hits = []
            lazy_patterns = [
                (r"(?:计算|证明|推导|过程|解法|步骤|其余|以下|这里|此处)[均皆]?[从]?略(?![图圖])", "过程略"),
                (r"（\s*略\s*）|\(\s*略\s*\)|【\s*略\s*】", "（略）"),
                (r"同上(?![述所])", "同上"),
                (r"自行(?:计算|完成|推导|验证|练习)", "自行计算/推导"),
                (r"读者自证|留作练习|不再赘述", "读者自证/不再赘述"),
            ]
            for pat, label in lazy_patterns:
                for m in re.finditer(pat, block_txt):
                    start = max(0, m.start() - 18)
                    end = min(len(block_txt), m.end() + 18)
                    lazy_hits.append({"label": label, "context": block_txt[start:end]})

            problems.append({
                "title": htxt[:80],
                "id": h.get("id", ""),
                "missing": missing,
                "lazy_hits": lazy_hits,
            })

    incomplete_problems = [p for p in problems if p["missing"]]
    lazy_problems = [p for p in problems if p["lazy_hits"]]
    missing_counter = Counter()
    for p in incomplete_problems:
        for m in p["missing"]:
            missing_counter[m] += 1

    # Hiragana reading check across document
    hiragana_paren_matches = re.findall(r"[（(][ぁ-んー・\s]{2,}[）)]", raw)
    ruby_count = len(soup.find_all("ruby"))

    res["modules"] = {
        "total_problems_detected": len(problems),
        "complete_problems": len(problems) - len(incomplete_problems),
        "incomplete_problems_count": len(incomplete_problems),
        "missing_breakdown": dict(missing_counter),
        "incomplete_samples": incomplete_problems[:15],
        "lazy_problems_count": len(lazy_problems),
        "lazy_samples": lazy_problems[:15],
        "hiragana_reading_annotations": len(hiragana_paren_matches),
        "ruby_tag_count": ruby_count,
    }

    # --- 4. Sidebar TOC Anchors & Duplicate IDs ---
    all_ids = [el.get("id") for el in soup.find_all(id=True)]
    id_counts = Counter(all_ids)
    dup_ids = {k: v for k, v in id_counts.items() if v > 1}
    id_set = set(all_ids)

    sidebar = soup.find("aside") or soup.find("nav") or soup.find(id=re.compile("sidebar|toc", re.I))
    toc_links = sidebar.find_all("a", href=True) if sidebar else []
    hash_links = [a for a in toc_links if a["href"].startswith("#")]
    dead_links = []
    for a in hash_links:
        target = a["href"][1:]
        if not target or target not in id_set:
            dead_links.append({"href": a["href"], "text": a.get_text(" ", strip=True)[:60]})

    res["anchors"] = {
        "total_ids": len(all_ids),
        "duplicate_ids_count": len(dup_ids),
        "duplicate_ids_samples": list(dup_ids.items())[:15],
        "sidebar_hash_links_total": len(hash_links),
        "dead_links_count": len(dead_links),
        "dead_links_samples": dead_links[:15],
    }

    return res


def playwright_check(subject: str, url: str, browser) -> dict:
    res = {
        "console_errors": [],
        "failed_requests": [],
        "katex": {},
        "svg_runtime": {},
        "styles": {},
        "responsive": {},
        "toc_runtime": {},
    }

    context = browser.new_context(viewport={"width": 1440, "height": 900})
    page = context.new_page()

    page.on("console", lambda msg: res["console_errors"].append(msg.text) if msg.type == "error" else None)
    page.on("requestfailed", lambda req: res["failed_requests"].append({"url": req.url, "error": str(req.failure)}))

    page.goto(url, wait_until="networkidle", timeout=60000)
    # Wait a moment for KaTeX auto-render to finish on large documents
    page.wait_for_timeout(2000)

    # 1. KaTeX runtime inspection
    katex_info = page.evaluate("""() => {
        const katexCount = document.querySelectorAll('.katex').length;
        const errors = Array.from(document.querySelectorAll('.katex-error')).map(el => ({
            text: el.textContent.trim().slice(0, 120),
            title: el.getAttribute('title') || '',
            parentText: (el.parentElement ? el.parentElement.textContent.trim().slice(0, 140) : '')
        }));

        // Check leftover unrendered $...$ or $$...$$ in visible text nodes outside .katex, code, pre, script, style, svg
        const unrendered = [];
        const main = document.querySelector('main, #main, .main, .content') || document.body;
        const walker = document.createTreeWalker(main, NodeFilter.SHOW_TEXT);
        let node;
        while ((node = walker.nextNode())) {
            const p = node.parentElement;
            if (!p) continue;
            if (p.closest('.katex, .katex-display, script, style, code, pre, svg, aside, nav')) continue;
            const txt = node.nodeValue || '';
            if (txt.includes('$$') || /\\$(?:[^$\\n]{1,80})\\$/.test(txt) || /\\\\(?:frac|sqrt|ce|sum|int|rightarrow)\\b/.test(txt)) {
                unrendered.push(txt.trim().slice(0, 140));
            }
        }
        return {
            katex_rendered_count: katexCount,
            katex_error_count: errors.length,
            katex_error_samples: errors.slice(0, 20),
            unrendered_text_nodes_count: unrendered.length,
            unrendered_samples: unrendered.slice(0, 20),
        };
    }""")
    res["katex"] = katex_info

    # 2. SVG runtime inspection (Desktop 1440px, iPad 768px, Mobile 390px)
    def inspect_svgs_at_viewport(w, h):
        page.set_viewport_size({"width": w, "height": h})
        page.wait_for_timeout(300)
        return page.evaluate("""() => {
            const vw = window.innerWidth;
            const docOverflow = document.documentElement.scrollWidth > vw + 2;
            const svgs = Array.from(document.querySelectorAll('svg'));
            let zeroSize = 0;
            const overflowSvgs = [];
            const overlapSvgs = [];

            svgs.forEach((svg, idx) => {
                const r = svg.getBoundingClientRect();
                if (r.width === 0 || r.height === 0) {
                    zeroSize++;
                    return;
                }
                const parent = svg.parentElement;
                const pr = parent ? parent.getBoundingClientRect() : { width: vw };
                if (r.width > vw + 2 || (pr.width > 0 && r.width > pr.width + 4 && getComputedStyle(parent).overflowX !== 'auto' && getComputedStyle(parent).overflowX !== 'scroll')) {
                    overflowSvgs.push({
                        svg_index: idx + 1,
                        svg_w: Math.round(r.width),
                        parent_w: Math.round(pr.width),
                        vw: vw,
                        viewBox: svg.getAttribute('viewBox') || ''
                    });
                }

                // Check pairwise <text> overlap inside this SVG (only at Desktop to avoid duplicate counting)
                if (vw === 1440) {
                    const texts = Array.from(svg.querySelectorAll('text')).map(t => ({
                        txt: t.textContent.trim().slice(0, 30),
                        rect: t.getBoundingClientRect()
                    })).filter(x => x.txt.length > 0 && x.rect.width > 2 && x.rect.height > 2);

                    let pairs = [];
                    for (let i = 0; i < texts.length; i++) {
                        for (let j = i + 1; j < texts.length; j++) {
                            const a = texts[i].rect, b = texts[j].rect;
                            const ix = Math.max(0, Math.min(a.right, b.right) - Math.max(a.left, b.left));
                            const iy = Math.max(0, Math.min(a.bottom, b.bottom) - Math.max(a.top, b.top));
                            const interArea = ix * iy;
                            const minArea = Math.min(a.width * a.height, b.width * b.height);
                            // Flag significant overlap (> 25% of smaller text box AND > 4px in both axes)
                            if (ix > 4 && iy > 4 && minArea > 0 && (interArea / minArea) > 0.25) {
                                pairs.push([texts[i].txt, texts[j].txt, Math.round(interArea / minArea * 100) + '%']);
                            }
                        }
                    }
                    if (pairs.length > 0) {
                        overlapSvgs.push({
                            svg_index: idx + 1,
                            overlap_pairs_count: pairs.length,
                            sample_pairs: pairs.slice(0, 3)
                        });
                    }
                }
            });

            const sidebar = document.querySelector('aside, #sidebar, .sidebar');
            const sidebarRect = sidebar ? sidebar.getBoundingClientRect() : null;
            const sidebarStyle = sidebar ? getComputedStyle(sidebar) : null;

            return {
                viewport: { w: vw, h: window.innerHeight },
                doc_scroll_width: document.documentElement.scrollWidth,
                doc_horizontal_overflow: docOverflow,
                total_svgs: svgs.length,
                zero_size_svgs: zeroSize,
                overflow_svgs_count: overflowSvgs.length,
                overflow_svgs_samples: overflowSvgs.slice(0, 8),
                overlap_svgs_count: overlapSvgs.length,
                overlap_svgs_samples: overlapSvgs.slice(0, 10),
                sidebar_visible_width: sidebarRect ? Math.round(sidebarRect.width) : 0,
                sidebar_transform: sidebarStyle ? sidebarStyle.transform : null,
                sidebar_display: sidebarStyle ? sidebarStyle.display : null,
            };
        }""")

    res["responsive"]["desktop_1440"] = inspect_svgs_at_viewport(1440, 900)
    res["responsive"]["ipad_768"] = inspect_svgs_at_viewport(768, 1024)
    res["responsive"]["mobile_390"] = inspect_svgs_at_viewport(390, 844)

    # Restore Desktop for style & TOC checks
    page.set_viewport_size({"width": 1440, "height": 900})
    page.wait_for_timeout(200)

    # 3. Computed styles for Cross-Subject Consistency Comparison
    res["styles"] = page.evaluate("""() => {
        const pick = (sel, props) => {
            const el = document.querySelector(sel);
            if (!el) return null;
            const cs = getComputedStyle(el);
            const out = {};
            props.forEach(p => out[p] = cs[p]);
            return out;
        };
        return {
            body: pick('body', ['fontFamily', 'fontSize', 'lineHeight', 'color', 'backgroundColor']),
            sidebar: pick('aside, #sidebar, .sidebar', ['width', 'backgroundColor', 'color', 'borderRightColor']),
            main: pick('main, #main, .main, .content', ['maxWidth', 'paddingLeft', 'paddingRight', 'backgroundColor']),
            h1: pick('main h1, .content h1, h1', ['fontSize', 'color', 'fontWeight']),
            h2: pick('main h2, .content h2, h2', ['fontSize', 'color', 'borderBottomColor']),
            h3: pick('main h3, .content h3, h3', ['fontSize', 'color']),
            blockquote: pick('blockquote', ['backgroundColor', 'borderLeftColor', 'borderLeftWidth', 'paddingLeft', 'borderRadius']),
            code: pick('code', ['fontFamily', 'fontSize', 'backgroundColor', 'color']),
            table_th: pick('table th', ['backgroundColor', 'color', 'fontSize']),
            has_theme_toggle: !!document.querySelector('#themeBtn, [data-theme-toggle], .theme-btn'),
            has_font_controls: !!document.querySelector('#fontInc, #fontDec, .font-btn'),
            has_toc_search: !!document.querySelector('#tocSearch, .toc-search, input[type="search"], .sidebar-search input'),
        };
    }""")

    # 4. TOC runtime check (verify all hash links resolve to visible/existing targets)
    res["toc_runtime"] = page.evaluate("""() => {
        const sidebar = document.querySelector('aside, #sidebar, .sidebar, nav');
        if (!sidebar) return { found_sidebar: false };
        const links = Array.from(sidebar.querySelectorAll('a[href^="#"]'));
        let ok = 0, broken = [];
        for (const a of links) {
            const id = decodeURIComponent(a.getAttribute('href').slice(1));
            const target = document.getElementById(id);
            if (target) ok++;
            else broken.push({ href: a.getAttribute('href'), text: a.textContent.trim().slice(0, 50) });
        }
        return {
            found_sidebar: true,
            total_links: links.length,
            resolved_ok: ok,
            broken_count: broken.length,
            broken_samples: broken.slice(0, 10),
        };
    }""")

    context.close()
    return res


def main():
    server, port = start_local_server(ROOT)
    print(f"Started local HTTP server on http://127.0.0.1:{port}", flush=True)
    report = {}

    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(channel="chrome", headless=True)
            for subject, path in FILES.items():
                print(f"\n>>> Checking [{subject}] {path.name} ...", flush=True)
                s_res = static_check(subject, path)
                url = f"http://127.0.0.1:{port}/{path.name}"
                p_res = playwright_check(subject, url, browser)
                report[subject] = {"static": s_res, "playwright": p_res}
                print(
                    f"    KaTeX rendered: {p_res['katex']['katex_rendered_count']}, "
                    f"KaTeX errors: {p_res['katex']['katex_error_count']}, "
                    f"Unrendered nodes: {p_res['katex']['unrendered_text_nodes_count']}",
                    flush=True,
                )
                print(
                    f"    SVGs: {s_res['svg_static']['parsed_svg_count']} "
                    f"(missing viewBox: {s_res['svg_static']['missing_viewbox_count']}, "
                    f"mobile overflow: {p_res['responsive']['mobile_390']['overflow_svgs_count']}, "
                    f"text overlaps: {p_res['responsive']['desktop_1440']['overlap_svgs_count']})",
                    flush=True,
                )
                print(
                    f"    Problems: {s_res['modules']['total_problems_detected']} "
                    f"(complete: {s_res['modules']['complete_problems']}, "
                    f"incomplete: {s_res['modules']['incomplete_problems_count']}, "
                    f"lazy hits: {s_res['modules']['lazy_problems_count']})",
                    flush=True,
                )
                print(
                    f"    TOC links: {p_res['toc_runtime'].get('total_links', 0)} "
                    f"(broken: {p_res['toc_runtime'].get('broken_count', 0)}, "
                    f"dup IDs: {s_res['anchors']['duplicate_ids_count']})",
                    flush=True,
                )
            browser.close()
    finally:
        server.shutdown()

    REPORT_JSON.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"\nSaved full QA report to {REPORT_JSON}")


if __name__ == "__main__":
    main()
