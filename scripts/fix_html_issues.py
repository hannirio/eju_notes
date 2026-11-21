#!/usr/bin/env python3
"""
Surgical auto-fixer for verified issues in EJU Math, Physics, and Chemistry HTML solutions:
1. Math: fix KaTeX ParseError (`\\begin{array}{c\\|c}` -> `c|c`) and unclosed `$` typo.
2. Chemistry: remove `<br>` tags inside `$$...$$` blocks so KaTeX renders aligned equations.
3. Math & Chemistry: deduplicate duplicate internal SVG element IDs (e.g., `<marker id="arr1">`).
4. All 3 HTMLs: inject responsive overflow-protection CSS so tables, display math, and SVGs
   never overflow Desktop (1440px), iPad (768px), or Mobile (390px) viewports.
"""

import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def dedupe_svg_ids(html_text: str) -> tuple[str, int]:
    """Ensure every id inside <svg>...</svg> is globally unique, updating url(#id) & href=#id within that SVG."""
    seen = Counter()
    renamed = 0

    def repl_svg(match):
        nonlocal renamed
        svg = match.group(0)
        ids = re.findall(r'\bid="([^"]+)"', svg)
        if not ids:
            return svg
        local_map = {}
        for oid in ids:
            seen[oid] += 1
            if seen[oid] > 1:
                nid = f"{oid}-u{seen[oid]}"
                local_map[oid] = nid
                renamed += 1
        if not local_map:
            return svg
        for oid, nid in local_map.items():
            svg = re.sub(rf'\bid="{re.escape(oid)}"', f'id="{nid}"', svg)
            svg = re.sub(rf'url\(#{re.escape(oid)}\)', f'url(#{nid})', svg)
            svg = re.sub(rf'(xlink:)?href="#{re.escape(oid)}"', rf'\1href="#{nid}"', svg)
        return svg

    new_html = re.sub(r"<svg\b[^>]*>.*?</svg>", repl_svg, html_text, flags=re.S | re.I)
    return new_html, renamed


RESPONSIVE_FIX_CSS = """
    /* === QA Auto-Fix: Responsive Overflow Protection (Desktop / iPad / Mobile) === */
    html, body { max-width: 100%; overflow-x: hidden; }
    main, #main, .main, .content, .chapter-section, .doc-section, .section-card {
      min-width: 0;
      max-width: 100%;
      box-sizing: border-box;
    }
    .katex-display {
      max-width: 100%;
      overflow-x: auto;
      overflow-y: hidden;
      padding: 4px 0;
      -webkit-overflow-scrolling: touch;
    }
    .svg-wrap, .svg-container, .svg-wrapper {
      max-width: 100%;
      overflow-x: auto;
      -webkit-overflow-scrolling: touch;
    }
    .svg-wrap svg, .svg-container svg, .svg-wrapper svg, main svg, #main svg {
      max-width: 100% !important;
      height: auto !important;
    }
    pre {
      max-width: 100%;
      overflow-x: auto;
    }
    table {
      display: block;
      max-width: 100%;
      overflow-x: auto;
      -webkit-overflow-scrolling: touch;
    }
"""


def inject_responsive_css(html_text: str) -> tuple[str, bool]:
    if "QA Auto-Fix: Responsive Overflow Protection" in html_text:
        return html_text, False
    idx = html_text.rfind("</style>")
    if idx == -1:
        return html_text, False
    return html_text[:idx] + RESPONSIVE_FIX_CSS + "\n  </style>" + html_text[idx + len("</style>"):], True


def fix_math():
    p = ROOT / "eju_math_solutions.html"
    txt = p.read_text(encoding="utf-8")
    changes = []

    # 1. Fix KaTeX ParseError: \begin{array}{c\|c} -> \begin{array}{c|c}
    if r"\begin{array}{c\|c}" in txt:
        txt = txt.replace(r"\begin{array}{c\|c}", r"\begin{array}{c|c}")
        changes.append("Fixed KaTeX ParseError: \\begin{array}{c\\|c} -> c|c")

    # 2. Fix unclosed $ typo
    bad_str = '<span class="math-inline">$**から引いた / を通る** 必须先设切点 $</span>t$！'
    good_str = '<strong>から引いた / を通る</strong> 必须先设切点 <span class="math-inline">$t$</span>！'
    if bad_str in txt:
        txt = txt.replace(bad_str, good_str)
        changes.append("Fixed unclosed $ typo around から引いた / を通る")

    # Also fix the source note markdown if present
    for md in (ROOT / "notes" / "math").glob("*.md"):
        mtxt = md.read_text(encoding="utf-8")
        if "$**から引いた / を通る** 必须先设切点 $t$" in mtxt:
            md.write_text(
                mtxt.replace("$**から引いた / を通る** 必须先设切点 $t$", "**から引いた / を通る** 必须先设切点 $t$"),
                encoding="utf-8",
            )
            changes.append(f"Fixed source typo in {md.relative_to(ROOT)}")

    # 3. Deduplicate SVG IDs
    txt, renamed = dedupe_svg_ids(txt)
    if renamed:
        changes.append(f"Deduplicated {renamed} SVG internal IDs")

    # 4. Inject responsive overflow CSS
    txt, injected = inject_responsive_css(txt)
    if injected:
        changes.append("Injected responsive overflow-protection CSS")

    p.write_text(txt, encoding="utf-8")
    print("[MATH]", "; ".join(changes) if changes else "No changes needed")


def fix_physics():
    p = ROOT / "eju_physics_solutions.html"
    txt = p.read_text(encoding="utf-8")
    changes = []

    txt, renamed = dedupe_svg_ids(txt)
    if renamed:
        changes.append(f"Deduplicated {renamed} SVG internal IDs")

    txt, injected = inject_responsive_css(txt)
    if injected:
        changes.append("Injected responsive overflow-protection CSS")

    p.write_text(txt, encoding="utf-8")
    print("[PHYSICS]", "; ".join(changes) if changes else "No changes needed")


def fix_chemistry():
    p = ROOT / "eju_chemistry_solutions.html"
    txt = p.read_text(encoding="utf-8")
    changes = []

    # 1. Fix <br> inside $$...$$ display math blocks
    fixed_blocks = 0

    def repl_dmath(m):
        nonlocal fixed_blocks
        block = m.group(0)
        if "<br" in block:
            fixed_blocks += 1
            return re.sub(r"<br\s*/?>", "\n", block)
        return block

    txt = re.sub(r"\$\$.*?\$\$", repl_dmath, txt, flags=re.S)
    if fixed_blocks:
        changes.append(f"Removed <br> inside {fixed_blocks} $$...$$ display math blocks")

    # 2. Deduplicate SVG IDs
    txt, renamed = dedupe_svg_ids(txt)
    if renamed:
        changes.append(f"Deduplicated {renamed} SVG internal IDs")

    # 3. Inject responsive overflow CSS
    txt, injected = inject_responsive_css(txt)
    if injected:
        changes.append("Injected responsive overflow-protection CSS")

    p.write_text(txt, encoding="utf-8")
    print("[CHEMISTRY]", "; ".join(changes) if changes else "No changes needed")


if __name__ == "__main__":
    fix_math()
    fix_physics()
    fix_chemistry()
