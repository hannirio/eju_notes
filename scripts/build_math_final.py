#!/usr/bin/env python3
"""
Compile all EJU Mathematics lecture notes (glossary.md + note_001..note_031) into:
  1. ./eju_math_solutions.md
  2. ./eju_math_solutions.html  (iPad-friendly, collapsible sidebar TOC, KaTeX math, responsive SVG)
"""

import glob
import html
import os
import re

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NOTES_DIR = os.path.join(BASE_DIR, "notes", "math")
GLOSSARY_PATH = os.path.join(NOTES_DIR, "glossary.md")
OUT_MD = os.path.join(BASE_DIR, "eju_math_solutions.md")
OUT_HTML = os.path.join(BASE_DIR, "eju_math_solutions.html")


def natural_note_key(path: str):
    name = os.path.basename(path)
    m = re.match(r"note_(\d+)(?:_([a-z]))?\.md$", name)
    if not m:
        return (9999, "")
    return (int(m.group(1)), m.group(2) or "")


def collect_note_files():
    files = glob.glob(os.path.join(NOTES_DIR, "note_*.md"))
    files.sort(key=natural_note_key)
    return files


class MarkdownToHTML:
    """Zero-dependency Markdown -> HTML converter that strictly protects LaTeX and inline SVG."""

    def __init__(self):
        self.toc = []  # list of dicts: {level, id, text, section_idx}
        self.heading_counter = 0

    def _new_id(self, prefix="sec"):
        self.heading_counter += 1
        return f"{prefix}-{self.heading_counter}"

    def convert_document(self, md_text: str, section_idx: int) -> str:
        # 1. Extract and protect <svg ...>...</svg> blocks
        svg_store = []

        def repl_svg(m):
            idx = len(svg_store)
            svg_store.append(m.group(0))
            return f"\n\n@@SVG_BLOCK_{idx}@@\n\n"

        text = re.sub(r"<svg\b[^>]*>.*?</svg>", repl_svg, md_text, flags=re.DOTALL | re.IGNORECASE)

        # 2. Extract and protect fenced code blocks
        code_store = []

        def repl_code(m):
            idx = len(code_store)
            lang = (m.group(1) or "").strip()
            body = html.escape(m.group(2))
            code_store.append(f'<pre><code class="lang-{html.escape(lang)}">{body}</code></pre>')
            return f"\n\n@@CODE_BLOCK_{idx}@@\n\n"

        text = re.sub(r"```([^\n]*)\n(.*?)```", repl_code, text, flags=re.DOTALL)

        # 3. Extract and protect display math $$...$$ and \[...\]
        dmath_store = []

        def repl_dmath(m):
            idx = len(dmath_store)
            # Keep raw LaTeX inside a div/span so HTML escaping preserves <, >, & safely for KaTeX
            raw = m.group(0)
            escaped = raw.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
            dmath_store.append(f'<div class="math-display">{escaped}</div>')
            return f"\n@@DMATH_{idx}@@\n"

        text = re.sub(r"\$\$.*?\$\$", repl_dmath, text, flags=re.DOTALL)
        text = re.sub(r"\\\[.*?\\\]", repl_dmath, text, flags=re.DOTALL)

        # 4. Line-by-line block parser
        lines = text.splitlines()
        out = []
        i = 0
        n = len(lines)

        def render_inline(s: str) -> str:
            # Protect inline code `...`
            icodes = []

            def r_ic(m):
                k = len(icodes)
                icodes.append(f"<code>{html.escape(m.group(1))}</code>")
                return f"@@IC_{k}@@"

            s = re.sub(r"`([^`\n]+)`", r_ic, s)

            # Protect inline math $...$ and \(...\)
            imaths = []

            def r_im(m):
                k = len(imaths)
                raw = m.group(0)
                escaped = raw.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
                imaths.append(f'<span class="math-inline">{escaped}</span>')
                return f"@@IM_{k}@@"

            # Match $...$ (non-greedy, not starting/ending with space unless single char, no newline)
            s = re.sub(r"(?<!\\)\$(?!\$)(.+?)(?<!\\)\$", r_im, s)
            s = re.sub(r"\\\(.+?\\\)", r_im, s)

            # Escape remaining HTML (except our @@ placeholders)
            s = html.escape(s)

            # Markdown links [text](url)
            s = re.sub(
                r"\[([^\]]+)\]\(([^)]+)\)",
                lambda m: f'<a href="{m.group(2)}" target="_blank" rel="noopener">{m.group(1)}</a>',
                s,
            )

            # Bold **...**
            s = re.sub(r"\*\*([^*]+?)\*\*", r"<strong>\1</strong>", s)
            # Italic *...* (avoid breaking already-processed tags)
            s = re.sub(r"(?<!\*)\*([^*\n]+?)\*(?!\*)", r"<em>\1</em>", s)

            # Restore inline math & inline code
            for k, val in enumerate(imaths):
                s = s.replace(f"@@IM_{k}@@", val)
            for k, val in enumerate(icodes):
                s = s.replace(f"@@IC_{k}@@", val)

            # Also restore any inline DMATH / SVG / CODE placeholders if embedded on same line
            s = re.sub(r"@@DMATH_(\d+)@@", lambda m: dmath_store[int(m.group(1))], s)
            s = re.sub(r"@@SVG_BLOCK_(\d+)@@", lambda m: f'<div class="svg-wrapper">{svg_store[int(m.group(1))]}</div>', s)
            s = re.sub(r"@@CODE_BLOCK_(\d+)@@", lambda m: code_store[int(m.group(1))], s)
            return s

        while i < n:
            line = lines[i]
            stripped = line.strip()

            # Blank line
            if not stripped:
                i += 1
                continue

            # Protected SVG block
            m_svg = re.match(r"^@@SVG_BLOCK_(\d+)@@$", stripped)
            if m_svg:
                out.append(f'<div class="svg-wrapper">{svg_store[int(m_svg.group(1))]}</div>')
                i += 1
                continue

            # Protected Code block
            m_code = re.match(r"^@@CODE_BLOCK_(\d+)@@$", stripped)
            if m_code:
                out.append(code_store[int(m_code.group(1))])
                i += 1
                continue

            # Protected Display Math block
            m_dm = re.match(r"^@@DMATH_(\d+)@@$", stripped)
            if m_dm:
                out.append(dmath_store[int(m_dm.group(1))])
                i += 1
                continue

            # Horizontal rule
            if re.match(r"^([-*_])\1{2,}$", stripped):
                out.append("<hr>")
                i += 1
                continue

            # Headings (# .. ####)
            m_h = re.match(r"^(#{1,6})\s+(.*)$", stripped)
            if m_h:
                level = len(m_h.group(1))
                raw_title = m_h.group(2).strip()
                hid = self._new_id(f"s{section_idx}-h{level}")
                rendered_title = render_inline(raw_title)
                out.append(f'<h{level} id="{hid}">{rendered_title}</h{level}>')
                if level <= 3:
                    # Clean plain-ish text for TOC (strip markdown bold/code markers)
                    toc_label = re.sub(r"\*\*(.*?)\*\*", r"\1", raw_title)
                    toc_label = re.sub(r"`(.*?)`", r"\1", toc_label)
                    self.toc.append({
                        "level": level,
                        "id": hid,
                        "text": toc_label,
                        "section_idx": section_idx,
                    })
                i += 1
                continue

            # Blockquote (including 💡 讲师批注 and ⚠️ 教材勘误提示)
            if stripped.startswith(">"):
                bq_lines = []
                while i < n and lines[i].strip().startswith(">"):
                    bq_lines.append(re.sub(r"^>\s?", "", lines[i].strip()))
                    i += 1
                bq_raw = "\n".join(bq_lines)
                css_cls = "callout"
                if "💡" in bq_raw or "讲师批注" in bq_raw:
                    css_cls = "callout callout-tip"
                elif "⚠️" in bq_raw or "勘误" in bq_raw:
                    css_cls = "callout callout-warn"
                bq_html = "<br>".join(render_inline(l) for l in bq_lines if l.strip())
                out.append(f'<blockquote class="{css_cls}">{bq_html}</blockquote>')
                continue

            # Markdown Table
            if "|" in stripped and i + 1 < n and re.match(r"^\s*\|?[\s:\-|]+\|[\s:\-|]*$", lines[i + 1].strip()):
                table_lines = [stripped]
                i += 1
                # skip separator
                i += 1
                while i < n and "|" in lines[i].strip() and lines[i].strip():
                    table_lines.append(lines[i].strip())
                    i += 1

                def split_row(r):
                    r = r.strip()
                    if r.startswith("|"):
                        r = r[1:]
                    if r.endswith("|"):
                        r = r[:-1]
                    # Do not split pipes inside $...$ (e.g. |x| or \mid)
                    cells = []
                    buf = []
                    in_math = False
                    for ch in r:
                        if ch == "$":
                            in_math = not in_math
                            buf.append(ch)
                        elif ch == "|" and not in_math:
                            cells.append("".join(buf).strip())
                            buf = []
                        else:
                            buf.append(ch)
                    cells.append("".join(buf).strip())
                    return cells

                header_cells = split_row(table_lines[0])
                t_html = ['<div class="table-wrap"><table><thead><tr>']
                for c in header_cells:
                    t_html.append(f"<th>{render_inline(c)}</th>")
                t_html.append("</tr></thead><tbody>")
                for row_str in table_lines[1:]:
                    cells = split_row(row_str)
                    t_html.append("<tr>")
                    for c in cells:
                        t_html.append(f"<td>{render_inline(c)}</td>")
                    t_html.append("</tr>")
                t_html.append("</tbody></table></div>")
                out.append("".join(t_html))
                continue

            # Unordered / Ordered Lists (supports indented continuations, blockquotes, math inside list items)
            m_ul = re.match(r"^(\s*)([-*+])\s+(.*)$", line)
            m_ol = re.match(r"^(\s*)(\d+)\.\s+(.*)$", line)
            if m_ul or m_ol:
                is_ol = bool(m_ol)
                tag = "ol" if is_ol else "ul"
                base_indent = len((m_ol or m_ul).group(1))
                out.append(f"<{tag}>")
                while i < n:
                    cur = lines[i]
                    cur_s = cur.strip()
                    if not cur_s:
                        # Look ahead: if next non-empty line is another list item at same indent, continue list
                        j = i + 1
                        while j < n and not lines[j].strip():
                            j += 1
                        if j < n:
                            nxt = lines[j]
                            if (is_ol and re.match(rf"^\s{{{base_indent}}}\d+\.\s+", nxt)) or (
                                not is_ol and re.match(rf"^\s{{{base_indent}}}[-*+]\s+", nxt)
                            ):
                                i = j
                                continue
                            # Or indented continuation belonging to current list item
                            if len(nxt) - len(nxt.lstrip()) > base_indent and not nxt.strip().startswith("#"):
                                i = j
                                continue
                        break

                    m_item = (
                        re.match(rf"^(\s{{{base_indent}}})\d+\.\s+(.*)$", cur)
                        if is_ol
                        else re.match(rf"^(\s{{{base_indent}}})[-*+]\s+(.*)$", cur)
                    )
                    if not m_item:
                        break

                    item_parts = [render_inline(m_item.group(2))]
                    i += 1
                    # Consume indented continuation lines for this list item
                    while i < n:
                        nxt = lines[i]
                        nxt_s = nxt.strip()
                        if not nxt_s:
                            # check if indented content follows blank line
                            j = i + 1
                            while j < n and not lines[j].strip():
                                j += 1
                            if j < n and (len(lines[j]) - len(lines[j].lstrip()) > base_indent):
                                nxt_j = lines[j].strip()
                                if not nxt_j.startswith("#") and not re.match(r"^([-*_])\1{2,}$", nxt_j):
                                    i = j
                                    continue
                            break
                        nxt_indent = len(nxt) - len(nxt.lstrip())
                        if nxt_indent <= base_indent:
                            break
                        if re.match(r"^@@SVG_BLOCK_(\d+)@@$", nxt_s):
                            idx_s = int(re.match(r"^@@SVG_BLOCK_(\d+)@@$", nxt_s).group(1))
                            item_parts.append(f'<div class="svg-wrapper">{svg_store[idx_s]}</div>')
                            i += 1
                        elif re.match(r"^@@DMATH_(\d+)@@$", nxt_s):
                            idx_d = int(re.match(r"^@@DMATH_(\d+)@@$", nxt_s).group(1))
                            item_parts.append(dmath_store[idx_d])
                            i += 1
                        elif nxt_s.startswith(">"):
                            bq_sub = []
                            while i < n and lines[i].strip().startswith(">"):
                                bq_sub.append(re.sub(r"^>\s?", "", lines[i].strip()))
                                i += 1
                            bq_raw = "\n".join(bq_sub)
                            css_cls = "callout"
                            if "💡" in bq_raw or "讲师批注" in bq_raw:
                                css_cls = "callout callout-tip"
                            elif "⚠️" in bq_raw or "勘误" in bq_raw:
                                css_cls = "callout callout-warn"
                            bq_h = "<br>".join(render_inline(l) for l in bq_sub if l.strip())
                            item_parts.append(f'<blockquote class="{css_cls}">{bq_h}</blockquote>')
                        elif re.match(r"^[-*+]\s+", nxt_s):
                            # Sub-bullet
                            sub_items = []
                            while i < n and (len(lines[i]) - len(lines[i].lstrip()) > base_indent) and re.match(r"^[-*+]\s+", lines[i].strip()):
                                sub_txt = re.sub(r"^[-*+]\s+", "", lines[i].strip())
                                sub_items.append(f"<li>{render_inline(sub_txt)}</li>")
                                i += 1
                            item_parts.append("<ul>" + "".join(sub_items) + "</ul>")
                        else:
                            item_parts.append(f"<p>{render_inline(nxt_s)}</p>")
                            i += 1

                    out.append(f"<li>{''.join(item_parts)}</li>")
                out.append(f"</{tag}>")
                continue

            # Regular paragraph
            para_lines = [stripped]
            i += 1
            while i < n:
                nxt_s = lines[i].strip()
                if (
                    not nxt_s
                    or nxt_s.startswith("#")
                    or nxt_s.startswith(">")
                    or re.match(r"^@@(SVG_BLOCK|CODE_BLOCK|DMATH)_\d+@@$", nxt_s)
                    or re.match(r"^([-*_])\1{2,}$", nxt_s)
                    or re.match(r"^[-*+]\s+", nxt_s)
                    or re.match(r"^\d+\.\s+", nxt_s)
                ):
                    break
                para_lines.append(nxt_s)
                i += 1
            out.append(f"<p>{'<br>'.join(render_inline(l) for l in para_lines)}</p>")

        result = "\n".join(out)
        # Final safety restore for any placeholders that appeared inside nested contexts
        result = re.sub(r"@@SVG_BLOCK_(\d+)@@", lambda m: f'<div class="svg-wrapper">{svg_store[int(m.group(1))]}</div>', result)
        result = re.sub(r"@@CODE_BLOCK_(\d+)@@", lambda m: code_store[int(m.group(1))], result)
        result = re.sub(r"@@DMATH_(\d+)@@", lambda m: dmath_store[int(m.group(1))], result)
        return result


CHAPTER_DEFS = [
    (1, "第一章　数与式、集合と命題", "P1–P30"),
    (2, "第二章　整数性質", "P31–P45"),
    (3, "第三章　二次関数", "P46–P75"),
    (4, "第四章　指数関数と対数関数", "P76–P82"),
    (5, "第五章　幾何基礎", "P82–P120"),
    (6, "第六章　三角関数", "P121–P150"),
    (7, "第七章　解析幾何", "P151–P210"),
    (8, "第八章　ベクトル（向量）", "P211–P240"),
    (9, "第九章　複素数", "P241–P255"),
    (10, "第十章　数列", "P256–P285"),
    (11, "第十一章　微分積分", "P286–P420"),
    (12, "第十二章　確率と統計推測", "P421–P465"),
]

# filename -> (chapter_no, page_range, unit_theme)
UNIT_META = {
    "note_001.md":   (1, "P1–P15",   "整式の加減乗・因数分解・整式の除法・分数式"),
    "note_002_a.md": (1, "P16–P23",  "分数式・実数と絶対値・一次不等式・相加相乗平均"),
    "note_002_b.md": (1, "P24–P30",  "集合と命題・約数と倍数（第二章導入）"),
    "note_003_a.md": (2, "P31–P37",  "約数と倍数・整数の割り算・互除法（上）"),
    "note_003_b.md": (2, "P38–P45",  "ユークリッドの互除法・1次不定方程式・n進法（下）"),
    "note_004_a.md": (3, "P46–P53",  "n進法（続）・二次関数のグラフと平行/対称移動"),
    "note_004_b.md": (3, "P54–P60",  "二次関数の最大最小・二次方程式と判別式"),
    "note_005_a.md": (3, "P61–P67",  "グラフと二次方程式・二次不等式・指数の拡張"),
    "note_005_b.md": (3, "P68–P75",  "二次不等式演習（続）・指数関数（第四章導入）"),
    "note_006_a.md": (4, "P76–P82",  "指数関数・対数とその性質・対数関数"),
    "note_006_b.md": (5, "P82–P90",  "平面図形と三角比・三角比の拡張"),
    "note_007.md":   (5, "P91–P105", "正弦/余弦定理・図形の計量・五心・チェバ/メネラウス"),
    "note_008.md":   (5, "P106–P120","円と直線・空間図形・一般角と弧度法（第六章導入）"),
    "note_009_a.md": (6, "P121–P129","三角関数のグラフと性質・三角関数の応用"),
    "note_009_b.md": (6, "P130–P135","加法定理とその応用（2倍角・半角・3倍角）"),
    "note_010.md":   (6, "P136–P150","和積公式・三角関数の合成・直線の方程式（第七章導入）"),
    "note_011_a.md": (7, "P151–P159","直線束・点と直線の距離・円の方程式と接線"),
    "note_011_b.md": (7, "P160–P165","極線・2つの円の位置関係・円束・軌跡と方程式"),
    "note_012_a.md": (7, "P166–P170","不等式の表す領域・二次曲線（知識梳理）"),
    "note_012_b.md": (7, "P171–P180","放物線・楕円・双曲線・2次曲線と直線"),
    "note_013_a.md": (7, "P181–P187","2次曲線の接線・離心率と準線・領域（上）"),
    "note_013_b.md": (7, "P188–P195","2次曲線の性質・媒介変数表示（下）"),
    "note_014.md":   (7, "P196–P210","極座標と極方程式・平面ベクトル（第八章導入）"),
    "note_015_a.md": (8, "P211–P215","平面ベクトルの内積応用・位置ベクトルと図形"),
    "note_015_b.md": (8, "P216–P225","ベクトル方程式・空間ベクトル（導入）"),
    "note_016.md":   (8, "P226–P240","空間ベクトルの内積・空間図形・複素数（第九章導入）"),
    "note_017_a.md": (9, "P241–P249","複素数平面・極形式と乗法/除法"),
    "note_017_b.md": (9, "P250–P255","ド・モアブルの定理・1のn乗根・等差数列（第十章導入）"),
    "note_018_a.md": (10,"P256–P261","等差数列の和・共通項・等比数列（上）"),
    "note_018_b.md": (10,"P262–P270","種々の数列（Σ・群数列）・漸化式と数列（下）"),
    "note_019.md":   (10,"P271–P285","種々の漸化式・数学的帰納法・数列の極限（第十一章導入）"),
    "note_020_a.md": (11,"P286–P290","数列の極限・極限総覧（上）"),
    "note_020_b.md": (11,"P290–P300","無限級数・関数の極限（下）"),
    "note_021_a.md": (11,"P301–P305","関数の極限（演習問題 3）"),
    "note_021_b.md": (11,"P306–P315","関数の連続性・導関数・三角/対数/指数関数の微分"),
    "note_022_a.md": (11,"P316–P324","高次導関数・陰関数/媒介変数の微分・ロピタルの定理"),
    "note_022_b.md": (11,"P325–P330","接線と法線・関数の増減と値の変化"),
    "note_023_a.md": (11,"P331–P337","関数の増減・凹凸・変曲点・漸近線（上）"),
    "note_023_b.md": (11,"P338–P345","関数の増減とグラフ概形（演習問題 10–11 下）"),
    "note_024_a.md": (11,"P346–P352","漸近線・共通接線・方程式/不等式への微分応用"),
    "note_024_b.md": (11,"P353–P360","不定積分とその基本性質・不定積分の求め方"),
    "note_025_a.md": (11,"P361–P366","不定積分演習（前半）・定積分の基本性質"),
    "note_025_b.md": (11,"P367–P375","不定積分演習（後半：演習問題 13）"),
    "note_026_a.md": (11,"P376–P384","定積分とその基本性質（演習問題 14）"),
    "note_026_b.md": (11,"P385–P390","定積分で表された関数・定積分と和の極限"),
    "note_027_a.md": (11,"P391–P401","区分求積法・定積分と不等式・面積（上）"),
    "note_027_b.md": (11,"P402–P405","定積分の応用：面積（演習問題 17 後半）"),
    "note_028_a.md": (11,"P406–P410","定積分の応用：面積（演習問題 17 続）"),
    "note_028_b.md": (11,"P411–P420","体積・曲線の長さ・順列（第十二章導入）"),
    "note_029_a.md": (12,"P421–P429","円順列・組合せ・重複組合せ・確率の基本"),
    "note_029_b.md": (12,"P430–P435","確率の定義・独立試行・反復試行・条件付き確率"),
    "note_030.md":   (12,"P436–P450","確率変数と期待値/分散・二項分布・正規分布"),
    "note_031.md":   (12,"P451–P465","二項分布の正規近似・標本分布・母平均/母比率の推定"),
}

# glossary H2 key (note_XXX) -> (sort_order, page_range, theme)
GLOSSARY_META = {
    "note_001": (1,  "P1–P15",   "整式の加減乗・因数分解・整式の除法・分数式"),
    "note_002": (2,  "P16–P30",  "実数・一次不等式・集合と命題・約数と倍数"),
    "note_003": (3,  "P31–P45",  "整数の性質・互除法・1次不定方程式・n進法"),
    "note_004": (4,  "P46–P60",  "二次関数のグラフ・最大最小・二次方程式"),
    "note_005": (5,  "P61–P75",  "二次不等式・指数の拡張・指数関数"),
    "note_006": (6,  "P76–P90",  "対数関数・平面図形と三角比"),
    "note_007": (7,  "P91–P105", "正弦/余弦定理・五心・チェバ/メネラウス"),
    "note_008": (8,  "P106–P120","円と直線・空間図形・一般角と弧度法"),
    "note_009": (9,  "P121–P135","三角関数のグラフ・加法定理と倍角/半角"),
    "note_010": (10, "P136–P150","和積公式・三角関数の合成・直線の方程式"),
    "note_011": (11, "P151–P165","円の方程式・接線・2円の位置関係・軌跡"),
    "note_012": (12, "P166–P180","不等式の領域・放物線/楕円/双曲線"),
    "note_013": (13, "P181–P195","2次曲線の接線・離心率・媒介変数表示"),
    "note_014": (14, "P196–P210","極座標と極方程式・平面ベクトル基礎"),
    "note_015": (15, "P211–P225","平面ベクトル応用・位置ベクトル・空間座標"),
    "note_016": (16, "P226–P240","空間ベクトル・空間図形・複素数導入"),
    "note_017": (17, "P241–P255","複素数平面・極形式・ド・モアブル・等差数列"),
    "note_018": (18, "P256–P270","等差/等比数列・種々の数列・漸化式"),
    "note_019": (19, "P271–P285","種々の漸化式・数学的帰納法・数列の極限"),
    "note_020": (20, "P286–P300","数列の極限・無限級数・関数の極限"),
    "note_021": (21, "P301–P315","関数の連続性・導関数・初等関数の微分"),
    "note_022": (22, "P316–P330","高次導関数・ロピタルの定理・接線と法線"),
    "note_023": (23, "P331–P345","関数の増減・凹凸・変曲点・漸近線"),
    "note_024": (24, "P346–P360","微分の方程式/不等式応用・不定積分"),
    "note_025": (25, "P361–P375","不定積分の計算・定積分の基本性質"),
    "note_026": (26, "P376–P390","定積分で表された関数・定積分と和の極限"),
    "note_027": (27, "P391–P405","区分求積法・定積分と不等式・面積（上）"),
    "note_028": (28, "P406–P420","面積（下）・体積・曲線の長さ・順列導入"),
    "note_029": (29, "P421–P435","順列/組合せ・確率の基本・独立/条件付き確率"),
    "note_030": (30, "P436–P450","確率変数・期待値/分散・二項分布・正規分布"),
    "note_031": (31, "P451–P465","正規近似・標本分布・母平均/母比率の推定"),
}


def clean_toc_label(text: str) -> str:
    """Strip raw LaTeX dollar signs and simple TeX commands so sidebar labels read cleanly."""
    s = re.sub(r"\$([^$]+)\$", r"\1", text)
    s = s.replace("\\", "")
    s = re.sub(r"([A-Za-z])_\{?n\}?", r"\1ₙ", s)
    s = re.sub(r"\s+", " ", s).strip()
    return s


def build_toc_html(toc_entries, section_meta):
    """Build two-level chapter -> unit collapsible sidebar TOC (referencing EJU Physics & Chemistry)."""
    groups = {}
    for entry in toc_entries:
        groups.setdefault(entry["section_idx"], []).append(entry)

    # Map chapter_no -> list of section indices
    chapter_sections = {ch[0]: [] for ch in CHAPTER_DEFS}
    glossary_idx = None
    for idx, meta in enumerate(section_meta):
        if meta["kind"] == "glossary":
            glossary_idx = idx
        else:
            chapter_sections[meta["chapter"]].append(idx)

    parts = ['<div class="nav-part-label">理系数学（全十二章）</div>']

    for ch_no, ch_title, ch_pages in CHAPTER_DEFS:
        sec_indices = chapter_sections.get(ch_no, [])
        if not sec_indices:
            continue
        first_entries = groups.get(sec_indices[0], [])
        ch_anchor = first_entries[0]["id"] if first_entries else ""
        open_attr = " open" if ch_no == 1 else ""
        parts.append(f'<details class="toc-chapter"{open_attr} data-ch="{ch_no}">')
        parts.append(
            f'<summary class="toc-ch-summary">'
            f'<a href="#{ch_anchor}" class="toc-ch-link">{html.escape(ch_title)}</a>'
            f'<span class="toc-pages">{html.escape(ch_pages)}</span>'
            f'</summary>'
        )
        parts.append('<div class="toc-units">')
        for idx in sec_indices:
            meta = section_meta[idx]
            entries = groups.get(idx, [])
            if not entries:
                continue
            top_id = entries[0]["id"]
            sub_entries = [e for e in entries[1:] if e["level"] in (2, 3)]
            parts.append(f'<details class="toc-unit" data-sec="{idx}">')
            parts.append(
                f'<summary class="toc-unit-summary">'
                f'<a href="#{top_id}" class="toc-unit-link">'
                f'<span class="pg">{html.escape(meta["pages"])}</span>'
                f'<span class="tx">{html.escape(meta["theme"])}</span>'
                f'</a></summary>'
            )
            if sub_entries:
                parts.append('<ul class="toc-sub">')
                for e in sub_entries:
                    cls = "toc-h2" if e["level"] == 2 else "toc-h3"
                    lbl = clean_toc_label(e["text"])
                    parts.append(
                        f'<li class="{cls}"><a href="#{e["id"]}">{html.escape(lbl)}</a></li>'
                    )
                parts.append("</ul>")
            parts.append("</details>")
        parts.append("</div>")
        parts.append("</details>")

    # Appendix: Glossary at bottom (consistent with Physics & Chemistry)
    if glossary_idx is not None:
        g_entries = groups.get(glossary_idx, [])
        if g_entries:
            g_top_id = g_entries[0]["id"]
            g_subs = [e for e in g_entries[1:] if e["level"] == 2]
            # Sort glossary sub-items by note number (fixes note_026 out of order)
            def glossary_sort_key(e):
                m = re.match(r"(note_\d+)", e["text"].strip())
                if m and m.group(1) in GLOSSARY_META:
                    return GLOSSARY_META[m.group(1)][0]
                return 999

            g_subs_sorted = sorted(g_subs, key=glossary_sort_key)
            parts.append('<div class="nav-part-label">附录</div>')
            parts.append(f'<details class="toc-chapter toc-glossary" data-sec="{glossary_idx}">')
            parts.append(
                f'<summary class="toc-ch-summary">'
                f'<a href="#{g_top_id}" class="toc-ch-link">📖 日文核心术语总表（Glossary）</a>'
                f'<span class="toc-pages">{len(g_subs_sorted)} 单元</span>'
                f'</summary>'
            )
            parts.append('<ul class="toc-glossary-list">')
            for e in g_subs_sorted:
                m = re.match(r"(note_\d+)", e["text"].strip())
                if m and m.group(1) in GLOSSARY_META:
                    _, pg, theme = GLOSSARY_META[m.group(1)]
                else:
                    pg, theme = "", clean_toc_label(e["text"])
                parts.append(
                    f'<li><a href="#{e["id"]}" class="toc-glossary-link">'
                    f'<span class="pg">{html.escape(pg)}</span>'
                    f'<span class="tx">{html.escape(theme)}</span>'
                    f'</a></li>'
                )
            parts.append("</ul>")
            parts.append("</details>")

    return "\n".join(parts)


def main():
    note_files = collect_note_files()
    print(f"Found {len(note_files)} note files + glossary.md")

    # 1. Build merged Markdown
    md_parts = []
    section_docs = []  # (meta_dict, md_content)

    with open(GLOSSARY_PATH, "r", encoding="utf-8") as f:
        glossary_md = f.read().strip()
    md_parts.append(glossary_md)
    section_docs.append(
        ({"kind": "glossary", "title": "📖 日文核心术语总表（Glossary）"}, glossary_md)
    )

    for nf in note_files:
        fname = os.path.basename(nf)
        with open(nf, "r", encoding="utf-8") as f:
            txt = f.read().strip()
        md_parts.append(txt)
        if fname in UNIT_META:
            ch_no, pages, theme = UNIT_META[fname]
        else:
            m_h1 = re.search(r"^#\s+(.+)$", txt, flags=re.MULTILINE)
            fallback = m_h1.group(1).strip() if m_h1 else fname
            ch_no, pages, theme = 12, "", fallback
        section_docs.append(
            ({"kind": "unit", "file": fname, "chapter": ch_no, "pages": pages, "theme": theme}, txt)
        )

    merged_md = "\n\n---\n\n".join(md_parts) + "\n"
    with open(OUT_MD, "w", encoding="utf-8") as f:
        f.write(merged_md)
    print(f"Wrote merged Markdown: {OUT_MD} ({len(merged_md):,} chars)")

    # 2. Build iPad-friendly HTML
    converter = MarkdownToHTML()
    body_sections = []
    section_meta = [m for m, _ in section_docs]
    for idx, (meta, md_content) in enumerate(section_docs):
        sec_html = converter.convert_document(md_content, idx)
        body_sections.append(f'<section class="chapter-section" data-sec="{idx}">\n{sec_html}\n</section>')

    toc_html = build_toc_html(converter.toc, section_meta)
    all_body_html = "\n".join(body_sections)

    html_doc = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
<title>EJU 理系数学教材全解与备课讲义（全 465 页终稿）</title>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.css">
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.js"></script>
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/contrib/auto-render.min.js"
  onload="renderMathInElement(document.getElementById('content'), {{
    delimiters: [
      {{left: '$$', right: '$$', display: true}},
      {{left: '\\\\[', right: '\\\\]', display: true}},
      {{left: '$', right: '$', display: false}},
      {{left: '\\\\(', right: '\\\\)', display: false}}
    ],
    throwOnError: false,
    strict: false
  }});"></script>
<style>
  :root {{
    --bg: #ffffff;
    --bg-sidebar: #f6f8fa;
    --text: #1f2937;
    --muted: #6b7280;
    --border: #e5e7eb;
    --accent: #2563eb;
    --tip-bg: #eff6ff;
    --tip-border: #3b82f6;
    --warn-bg: #fffbeb;
    --warn-border: #f59e0b;
    --code-bg: #f3f4f6;
    --font-size: 16px;
    --sidebar-w: 348px;
  }}
  [data-theme="warm"] {{
    --bg: #fbf7ef;
    --bg-sidebar: #f3ecdf;
    --text: #2c241b;
    --muted: #6e6255;
    --border: #e4d9c6;
    --accent: #b45309;
    --tip-bg: #f5efe2;
    --tip-border: #d97706;
    --warn-bg: #fef3c7;
    --warn-border: #d97706;
    --code-bg: #efe7d8;
  }}
  [data-theme="dark"] {{
    --bg: #111827;
    --bg-sidebar: #1f2937;
    --text: #e5e7eb;
    --muted: #9ca3af;
    --border: #374151;
    --accent: #60a5fa;
    --tip-bg: #1e293b;
    --tip-border: #60a5fa;
    --warn-bg: #292524;
    --warn-border: #f59e0b;
    --code-bg: #1f2937;
  }}
  * {{ box-sizing: border-box; }}
  html {{ scroll-behavior: smooth; }}
  body {{
    margin: 0;
    font-family: -apple-system, BlinkMacSystemFont, "Hiragino Sans", "PingFang SC", "Noto Sans CJK SC", "Microsoft YaHei", sans-serif;
    font-size: var(--font-size);
    line-height: 1.75;
    color: var(--text);
    background: var(--bg);
  }}
  /* Top toolbar (especially handy on iPad split-screen) */
  .topbar {{
    position: fixed;
    top: 0; left: 0; right: 0;
    height: 48px;
    background: var(--bg-sidebar);
    border-bottom: 1px solid var(--border);
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0 14px;
    z-index: 1000;
    gap: 10px;
  }}
  .topbar-left {{ display: flex; align-items: center; gap: 10px; min-width: 0; }}
  .topbar-title {{
    font-weight: 700; font-size: 15px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;
  }}
  .topbar-controls {{ display: flex; align-items: center; gap: 6px; flex-shrink: 0; }}
  .btn {{
    background: var(--bg);
    color: var(--text);
    border: 1px solid var(--border);
    border-radius: 6px;
    padding: 4px 10px;
    font-size: 13px;
    cursor: pointer;
    user-select: none;
  }}
  .btn:hover {{ border-color: var(--accent); color: var(--accent); }}
  /* Sidebar TOC */
  .sidebar {{
    position: fixed;
    top: 48px; left: 0; bottom: 0;
    width: var(--sidebar-w);
    background: var(--bg-sidebar);
    border-right: 1px solid var(--border);
    display: flex;
    flex-direction: column;
    z-index: 900;
    transition: transform 0.22s ease;
  }}
  body.sidebar-hidden .sidebar {{ transform: translateX(-100%); }}
  .sidebar-brand {{
    padding: 12px 14px 10px;
    border-bottom: 1px solid var(--border);
  }}
  .sidebar-brand h2 {{
    margin: 0;
    padding: 0;
    border: none;
    font-size: 15px;
    font-weight: 700;
    color: var(--text);
  }}
  .sidebar-brand p {{
    margin: 3px 0 0;
    font-size: 11.5px;
    color: var(--muted);
    line-height: 1.4;
  }}
  .toc-search-wrap {{ padding: 8px 10px; border-bottom: 1px solid var(--border); }}
  .toc-search {{
    width: 100%;
    padding: 7px 10px;
    border: 1px solid var(--border);
    border-radius: 6px;
    background: var(--bg);
    color: var(--text);
    font-size: 13px;
  }}
  .toc-scroll {{
    flex: 1;
    overflow-y: auto;
    padding: 6px 8px 44px;
    -webkit-overflow-scrolling: touch;
  }}
  .nav-part-label {{
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 0.04em;
    color: var(--muted);
    padding: 10px 8px 4px;
    text-transform: uppercase;
  }}
  .toc-chapter {{ margin-bottom: 4px; }}
  .toc-ch-summary {{
    list-style: none;
    cursor: pointer;
    display: flex;
    align-items: baseline;
    gap: 6px;
    padding: 6px 8px;
    border-radius: 6px;
    font-weight: 700;
    font-size: 13.5px;
    line-height: 1.35;
    user-select: none;
  }}
  .toc-ch-summary::-webkit-details-marker {{ display: none; }}
  .toc-ch-summary::before {{
    content: "▸";
    display: inline-block;
    width: 12px;
    flex-shrink: 0;
    font-size: 11px;
    color: var(--muted);
    transition: transform 0.16s ease;
  }}
  .toc-chapter[open] > .toc-ch-summary::before {{
    transform: rotate(90deg);
    color: var(--accent);
  }}
  .toc-ch-summary:hover {{ background: rgba(37, 99, 235, 0.08); }}
  .toc-ch-link {{
    color: var(--text);
    text-decoration: none;
    flex: 1;
    min-width: 0;
  }}
  .toc-ch-link:hover {{ color: var(--accent); }}
  .toc-pages {{
    font-size: 11px;
    font-weight: 600;
    font-family: ui-monospace, SFMono-Regular, Menlo, monospace;
    color: var(--accent);
    background: rgba(37, 99, 235, 0.09);
    padding: 1px 6px;
    border-radius: 999px;
    flex-shrink: 0;
    white-space: nowrap;
  }}
  .toc-units {{
    margin: 2px 0 6px 10px;
    padding-left: 8px;
    border-left: 1.5px solid var(--border);
  }}
  .toc-unit {{ margin: 2px 0; }}
  .toc-unit-summary {{
    list-style: none;
    cursor: pointer;
    display: flex;
    align-items: baseline;
    gap: 4px;
    padding: 4px 6px;
    border-radius: 5px;
    user-select: none;
  }}
  .toc-unit-summary::-webkit-details-marker {{ display: none; }}
  .toc-unit-summary::before {{
    content: "▸";
    display: inline-block;
    width: 10px;
    flex-shrink: 0;
    font-size: 10px;
    color: var(--muted);
    transition: transform 0.16s ease;
  }}
  .toc-unit[open] > .toc-unit-summary::before {{
    transform: rotate(90deg);
    color: var(--accent);
  }}
  .toc-unit-summary:hover {{ background: rgba(37, 99, 235, 0.07); }}
  .toc-unit-link, .toc-glossary-link {{
    display: flex;
    align-items: baseline;
    gap: 7px;
    text-decoration: none;
    flex: 1;
    min-width: 0;
    line-height: 1.38;
  }}
  .toc-unit-link .pg, .toc-glossary-link .pg {{
    font-family: ui-monospace, SFMono-Regular, Menlo, monospace;
    font-size: 11px;
    font-weight: 600;
    color: var(--accent);
    flex-shrink: 0;
    min-width: 58px;
  }}
  .toc-unit-link .tx, .toc-glossary-link .tx {{
    font-size: 12.5px;
    font-weight: 600;
    color: var(--text);
    flex: 1;
    min-width: 0;
  }}
  .toc-glossary-link .tx {{ font-weight: 500; font-size: 12px; color: var(--muted); }}
  .toc-unit-link:hover .tx, .toc-unit-link.active .tx,
  .toc-glossary-link:hover .tx, .toc-glossary-link.active .tx {{ color: var(--accent); }}
  .toc-glossary-list {{
    list-style: none;
    margin: 2px 0 6px 10px;
    padding: 0 0 0 8px;
    border-left: 1.5px solid var(--border);
  }}
  .toc-glossary-list li {{ margin: 1px 0; }}
  .toc-glossary-link {{
    padding: 3px 6px;
    border-radius: 4px;
  }}
  .toc-glossary-link:hover, .toc-glossary-link.active {{ background: rgba(37, 99, 235, 0.08); }}
  .toc-sub {{ list-style: none; margin: 2px 0 4px 14px; padding: 0; border-left: 1px solid var(--border); }}
  .toc-sub li {{ margin: 1px 0; }}
  .toc-sub a {{
    display: block;
    text-decoration: none;
    color: var(--muted);
    font-size: 12px;
    padding: 2px 8px;
    border-radius: 4px;
    line-height: 1.38;
  }}
  .toc-sub li.toc-h2 a {{ font-weight: 600; color: var(--text); opacity: 0.85; }}
  .toc-sub li.toc-h3 a {{ padding-left: 16px; font-size: 11.5px; }}
  .toc-sub a:hover, .toc-sub a.active {{ color: var(--accent); background: rgba(37, 99, 235, 0.08); opacity: 1; }}
  /* Main content */
  .main {{
    margin-top: 48px;
    margin-left: var(--sidebar-w);
    padding: 28px 36px 80px;
    max-width: calc(960px + var(--sidebar-w));
    transition: margin-left 0.22s ease;
  }}
  body.sidebar-hidden .main {{ margin-left: 0; margin-right: auto; margin-left: auto; max-width: 960px; }}
  .chapter-section {{
    padding-bottom: 36px;
    margin-bottom: 42px;
    border-bottom: 2px dashed var(--border);
  }}
  h1 {{
    font-size: 1.75em;
    border-bottom: 2px solid var(--accent);
    padding-bottom: 8px;
    margin-top: 10px;
    scroll-margin-top: 64px;
  }}
  h2 {{
    font-size: 1.38em;
    margin-top: 28px;
    padding-left: 10px;
    border-left: 4px solid var(--accent);
    scroll-margin-top: 64px;
  }}
  h3 {{
    font-size: 1.15em;
    margin-top: 22px;
    color: var(--accent);
    scroll-margin-top: 64px;
  }}
  h4 {{
    font-size: 1.05em;
    margin-top: 18px;
    background: var(--bg-sidebar);
    padding: 6px 12px;
    border-radius: 6px;
    scroll-margin-top: 64px;
  }}
  hr {{ border: none; border-top: 1px solid var(--border); margin: 22px 0; }}
  p {{ margin: 10px 0; }}
  ul, ol {{ padding-left: 24px; margin: 8px 0; }}
  li {{ margin: 5px 0; }}
  code {{
    background: var(--code-bg);
    padding: 2px 5px;
    border-radius: 4px;
    font-size: 0.9em;
    font-family: ui-monospace, SFMono-Regular, Menlo, monospace;
  }}
  pre {{
    background: var(--code-bg);
    padding: 12px 16px;
    border-radius: 8px;
    overflow-x: auto;
  }}
  pre code {{ background: none; padding: 0; }}
  /* Callouts */
  .callout {{
    margin: 12px 0;
    padding: 10px 14px;
    border-left: 4px solid var(--border);
    background: var(--bg-sidebar);
    border-radius: 0 6px 6px 0;
    font-size: 0.95em;
  }}
  .callout-tip {{
    border-left-color: var(--tip-border);
    background: var(--tip-bg);
  }}
  .callout-warn {{
    border-left-color: var(--warn-border);
    background: var(--warn-bg);
  }}
  /* Tables */
  .table-wrap {{ overflow-x: auto; margin: 14px 0; -webkit-overflow-scrolling: touch; }}
  table {{
    width: 100%;
    border-collapse: collapse;
    font-size: 0.93em;
  }}
  th, td {{
    border: 1px solid var(--border);
    padding: 8px 10px;
    text-align: left;
    vertical-align: top;
  }}
  th {{ background: var(--bg-sidebar); font-weight: 700; }}
  /* Math display */
  .math-display {{
    overflow-x: auto;
    overflow-y: hidden;
    padding: 6px 2px;
    margin: 8px 0;
    -webkit-overflow-scrolling: touch;
  }}
  /* SVG centered & responsive */
  .svg-wrapper {{
    display: flex;
    justify-content: center;
    align-items: center;
    margin: 16px auto;
    padding: 10px;
    background: #ffffff;
    border: 1px solid var(--border);
    border-radius: 8px;
    overflow-x: auto;
  }}
  .svg-wrapper svg {{
    max-width: 100%;
    height: auto !important;
    display: block;
  }}
  /* iPad / narrow split-screen responsiveness */
  @media (max-width: 960px) {{
    .sidebar {{
      box-shadow: 4px 0 20px rgba(0,0,0,0.18);
    }}
    .main {{
      margin-left: 0;
      padding: 20px 18px 70px;
    }}
  }}
  @media print {{
    .topbar, .sidebar {{ display: none !important; }}
    .main {{ margin: 0 !important; padding: 0 !important; max-width: 100% !important; }}
  }}
</style>
</head>
<body>
<header class="topbar">
  <div class="topbar-left">
    <button class="btn" id="toggleSidebar" title="展开/收起目录">☰ 目录</button>
    <span class="topbar-title">EJU 理系数学教材全解与备课讲义（P1–P465 终稿）</span>
  </div>
  <div class="topbar-controls">
    <button class="btn" id="expandAll" title="展开/折叠全部目录">展开目录</button>
    <button class="btn" id="fontDec">A-</button>
    <button class="btn" id="fontInc">A+</button>
    <button class="btn" id="themeBtn">护眼</button>
  </div>
</header>

<aside class="sidebar" id="sidebar">
  <div class="sidebar-brand">
    <h2>EJU 理系数学全解讲义</h2>
    <p>格致学苑《EJU数学対策》全十二章 · 原书 P1–P465</p>
  </div>
  <div class="toc-search-wrap">
    <input type="search" id="tocSearch" class="toc-search" placeholder="筛选章节 / 单元主题 / 演习题 / 页码...">
  </div>
  <div class="toc-scroll" id="tocScroll">
    {toc_html}
  </div>
</aside>

<main class="main" id="content">
  {all_body_html}
</main>

<script>
  const body = document.body;
  // Auto-collapse sidebar on narrow iPad split-screen
  if (window.innerWidth <= 960) {{
    body.classList.add('sidebar-hidden');
  }}
  document.getElementById('toggleSidebar').addEventListener('click', () => {{
    body.classList.toggle('sidebar-hidden');
  }});
  // Highlight active TOC link & close sidebar on narrow screens
  document.getElementById('tocScroll').addEventListener('click', (e) => {{
    const link = e.target.closest('a');
    if (!link) return;
    document.querySelectorAll('#tocScroll a.active').forEach(a => a.classList.remove('active'));
    link.classList.add('active');
    if (window.innerWidth <= 960) {{
      body.classList.add('sidebar-hidden');
    }}
  }});
  // Expand / collapse all chapters (and collapse units when folding)
  let allExpanded = false;
  document.getElementById('expandAll').addEventListener('click', (e) => {{
    allExpanded = !allExpanded;
    document.querySelectorAll('.toc-chapter').forEach(d => d.open = allExpanded);
    if (!allExpanded) {{
      document.querySelectorAll('.toc-unit').forEach(d => d.open = false);
    }}
    e.target.textContent = allExpanded ? '折叠目录' : '展开目录';
  }});
  // Search TOC across chapters, units (pages + themes), and sub-items
  document.getElementById('tocSearch').addEventListener('input', (e) => {{
    const q = e.target.value.trim().toLowerCase();
    document.querySelectorAll('.toc-chapter').forEach(ch => {{
      if (!q) {{
        ch.style.display = '';
        ch.querySelectorAll('.toc-unit').forEach(u => {{
          u.style.display = '';
          u.querySelectorAll('li').forEach(li => li.style.display = '');
        }});
        ch.querySelectorAll('.toc-glossary-list li').forEach(li => li.style.display = '');
        return;
      }}
      const chText = ch.querySelector('.toc-ch-summary').textContent.toLowerCase();
      const chDirectMatch = chText.includes(q);
      let anyMatch = chDirectMatch;

      ch.querySelectorAll('.toc-unit').forEach(u => {{
        const uText = u.querySelector('.toc-unit-summary').textContent.toLowerCase();
        const uDirectMatch = chDirectMatch || uText.includes(q);
        let uSubMatch = false;
        u.querySelectorAll('li').forEach(li => {{
          const m = uDirectMatch || li.textContent.toLowerCase().includes(q);
          li.style.display = m ? '' : 'none';
          if (m && !uDirectMatch) uSubMatch = true;
        }});
        const showUnit = uDirectMatch || uSubMatch;
        u.style.display = showUnit ? '' : 'none';
        if (uSubMatch) u.open = true;
        if (showUnit) anyMatch = true;
      }});

      ch.querySelectorAll('.toc-glossary-list li').forEach(li => {{
        const m = chDirectMatch || li.textContent.toLowerCase().includes(q);
        li.style.display = m ? '' : 'none';
        if (m) anyMatch = true;
      }});

      ch.style.display = anyMatch ? '' : 'none';
      if (anyMatch) ch.open = true;
    }});
  }});
  // Font size controls
  let fontSize = 16;
  document.getElementById('fontDec').addEventListener('click', () => {{
    fontSize = Math.max(13, fontSize - 1);
    document.documentElement.style.setProperty('--font-size', fontSize + 'px');
  }});
  document.getElementById('fontInc').addEventListener('click', () => {{
    fontSize = Math.min(22, fontSize + 1);
    document.documentElement.style.setProperty('--font-size', fontSize + 'px');
  }});
  // Theme switcher: light -> warm -> dark
  const themes = ['', 'warm', 'dark'];
  const labels = ['护眼', '深色', '浅色'];
  let tIdx = 0;
  document.getElementById('themeBtn').addEventListener('click', (e) => {{
    tIdx = (tIdx + 1) % themes.length;
    if (themes[tIdx]) document.documentElement.setAttribute('data-theme', themes[tIdx]);
    else document.documentElement.removeAttribute('data-theme');
    e.target.textContent = labels[tIdx];
  }});
</script>
</body>
</html>
"""
    with open(OUT_HTML, "w", encoding="utf-8") as f:
        f.write(html_doc)
    print(f"Wrote self-contained HTML: {OUT_HTML} ({len(html_doc):,} chars, {len(converter.toc)} TOC entries)")


if __name__ == "__main__":
    main()
