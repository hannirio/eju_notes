#!/usr/bin/env python3
"""
Apply Optimizations 1, 2, and 3A:
  1. Unify visual design system across Math, Physics, and Chemistry HTMLs
     (shared light/warm/dark theme variables, unified 320px sidebar, unified typography,
      blockquote, code, table styles, and unified topbar with Home / TOC / A- / A+ / Theme).
  2. Eliminate mobile 390px horizontal overflow (long inline KaTeX wrapping/scrolling + overflow-x: clip).
  3. Add tailored 【讲师批注】 to the 9 Math problems that lacked it (both HTML and notes/math/*.md).
"""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# ---------------------------------------------------------------------------
# 1. Unified Theme CSS (appended at end of <style> to unify all 3 subjects)
# ---------------------------------------------------------------------------
UNIFIED_CSS = """
    /* === Unified EJU 3-Subject Design System === */
    :root {
      --bg: #f8fafc;
      --surface: #ffffff;
      --bg-sidebar: #ffffff;
      --sidebar-bg: #ffffff;
      --sidebar-text: #1e293b;
      --sidebar-hover: #f1f5f9;
      --text: #1e293b;
      --muted: #64748b;
      --border: #e2e8f0;
      --accent: #2563eb;
      --primary: #2563eb;
      --primary-light: #eff6ff;
      --h2-color: #1e3a8a;
      --h3-color: #2563eb;
      --tip-bg: #eff6ff;
      --tip-border: #3b82f6;
      --warn-bg: #fffbeb;
      --warn-border: #f59e0b;
      --code-bg: #f1f5f9;
      --code-color: #be123c;
      --table-th-bg: #f1f5f9;
      --font-size: 16px;
      --sidebar-w: 320px;
      --topbar-h: 52px;
    }
    [data-theme="warm"] {
      --bg: #f5f0e1;
      --surface: #fbf8ef;
      --bg-sidebar: #efe9d5;
      --sidebar-bg: #efe9d5;
      --sidebar-text: #2c261e;
      --sidebar-hover: #e5dec7;
      --text: #2c261e;
      --muted: #6b5e4c;
      --border: #dfd6be;
      --accent: #1d4ed8;
      --primary: #1d4ed8;
      --primary-light: #e8eefc;
      --h2-color: #1e3a8a;
      --h3-color: #1d4ed8;
      --tip-bg: #edf2fb;
      --tip-border: #3b82f6;
      --warn-bg: #f9f0d8;
      --warn-border: #d97706;
      --code-bg: #ebe4d0;
      --code-color: #9f1239;
      --table-th-bg: #ebe4d0;
    }
    [data-theme="dark"] {
      --bg: #0f172a;
      --surface: #1e293b;
      --bg-sidebar: #161f33;
      --sidebar-bg: #161f33;
      --sidebar-text: #e2e8f0;
      --sidebar-hover: #1e293b;
      --text: #e2e8f0;
      --muted: #94a3b8;
      --border: #334155;
      --accent: #60a5fa;
      --primary: #60a5fa;
      --primary-light: #172554;
      --h2-color: #93c5fd;
      --h3-color: #60a5fa;
      --tip-bg: #172554;
      --tip-border: #3b82f6;
      --warn-bg: #3b260b;
      --warn-border: #f59e0b;
      --code-bg: #0b1220;
      --code-color: #fda4af;
      --table-th-bg: #1e293b;
    }

    html {
      font-size: 16px;
      max-width: 100%;
      overflow-x: clip;
    }
    body {
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "Hiragino Sans", "PingFang SC", "Noto Sans CJK SC", "Microsoft YaHei", sans-serif !important;
      font-size: var(--font-size) !important;
      line-height: 1.75 !important;
      background: var(--bg) !important;
      color: var(--text) !important;
      max-width: 100%;
      overflow-x: clip;
    }

    /* Unified Topbar */
    .eju-topbar, header.topbar {
      position: fixed !important;
      top: 0; left: 0; right: 0;
      height: var(--topbar-h) !important;
      background: var(--surface) !important;
      color: var(--text) !important;
      border-bottom: 1px solid var(--border) !important;
      display: flex !important;
      align-items: center;
      justify-content: space-between;
      padding: 0 14px !important;
      z-index: 1200 !important;
      gap: 10px;
      box-shadow: 0 1px 4px rgba(15, 23, 42, 0.05);
    }
    .eju-topbar .topbar-left, header.topbar .topbar-left {
      display: flex; align-items: center; gap: 10px; min-width: 0;
    }
    .eju-topbar .topbar-title, header.topbar .topbar-title {
      font-weight: 700; font-size: 15px; color: var(--text);
      white-space: nowrap; overflow: hidden; text-overflow: ellipsis;
    }
    .eju-topbar .topbar-controls, header.topbar .topbar-controls {
      display: flex; align-items: center; gap: 6px; flex-shrink: 0;
    }
    .eju-topbar .btn, header.topbar .btn, .eju-home-link {
      appearance: none;
      border: 1px solid var(--border) !important;
      background: var(--surface) !important;
      color: var(--text) !important;
      border-radius: 6px !important;
      padding: 5px 10px !important;
      font-size: 13px !important;
      font-weight: 600;
      cursor: pointer;
      text-decoration: none;
      line-height: 1.2;
      white-space: nowrap;
      display: inline-flex;
      align-items: center;
    }
    .eju-topbar .btn:hover, header.topbar .btn:hover, .eju-home-link:hover {
      border-color: var(--accent) !important;
      color: var(--accent) !important;
    }
    #menu-toggle { display: none !important; }

    /* Unified Sidebar */
    aside#sidebar, aside.sidebar {
      position: fixed !important;
      top: var(--topbar-h) !important;
      left: 0 !important;
      bottom: 0 !important;
      width: var(--sidebar-w) !important;
      background: var(--sidebar-bg) !important;
      color: var(--sidebar-text) !important;
      border-right: 1px solid var(--border) !important;
      z-index: 1050 !important;
      transition: transform 0.2s ease !important;
    }
    body.sidebar-hidden aside#sidebar,
    body.sidebar-hidden aside.sidebar {
      transform: translateX(-100%) !important;
    }
    aside#sidebar .brand, aside#sidebar .sidebar-header, aside.sidebar .sidebar-brand {
      background: var(--sidebar-bg) !important;
      color: var(--text) !important;
      border-bottom: 1px solid var(--border) !important;
    }
    aside#sidebar .brand h2, aside#sidebar .sidebar-header h1, aside.sidebar .sidebar-brand h2 {
      color: var(--text) !important;
      font-size: 15px !important;
    }
    aside#sidebar .brand p, aside#sidebar .sidebar-stats, aside.sidebar .sidebar-brand p {
      color: var(--muted) !important;
    }
    aside#sidebar a, aside.sidebar a {
      color: var(--sidebar-text) !important;
    }
    aside#sidebar a:hover, aside.sidebar a:hover {
      background: var(--sidebar-hover) !important;
      color: var(--accent) !important;
    }
    aside#sidebar input[type="search"], aside#sidebar input[type="text"], aside.sidebar input[type="search"] {
      background: var(--bg) !important;
      color: var(--text) !important;
      border: 1px solid var(--border) !important;
    }
    aside#sidebar .nav-part-label, aside.sidebar .nav-part-label {
      color: var(--muted) !important;
    }
    aside#sidebar summary, aside.sidebar summary {
      color: var(--text) !important;
    }

    /* Unified Main Container */
    main, #main, .main, .content {
      margin-left: var(--sidebar-w) !important;
      margin-top: var(--topbar-h) !important;
      max-width: 1120px !important;
      padding: 32px 36px 80px !important;
      background: transparent !important;
      min-width: 0 !important;
      overflow-x: clip !important;
      box-sizing: border-box !important;
      transition: margin-left 0.2s ease;
    }
    body.sidebar-hidden main,
    body.sidebar-hidden #main,
    body.sidebar-hidden .main {
      margin-left: auto !important;
      margin-right: auto !important;
    }
    .chapter-section, .doc-section, .section-card, .hero {
      background: var(--surface) !important;
      color: var(--text) !important;
      border-color: var(--border) !important;
      overflow-x: clip !important;
      max-width: 100% !important;
    }

    /* Unified Headings, Blockquote, Code, Table */
    main h2, #main h2, .content h2 {
      color: var(--h2-color) !important;
      background: transparent !important;
      border-bottom: 2px solid var(--border) !important;
      padding: 8px 0 6px !important;
      font-size: 1.25em !important;
    }
    main h3, #main h3, .content h3 {
      color: var(--h3-color) !important;
      font-size: 1.12em !important;
    }
    blockquote {
      background: var(--tip-bg) !important;
      border-left: 4px solid var(--tip-border) !important;
      color: var(--text) !important;
      padding: 12px 16px !important;
      border-radius: 0 8px 8px 0 !important;
    }
    code {
      font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace !important;
      font-size: 0.875em !important;
      background: var(--code-bg) !important;
      color: var(--code-color) !important;
      padding: 2px 5px !important;
      border-radius: 4px !important;
    }
    pre {
      background: var(--code-bg) !important;
      color: var(--text) !important;
      border: 1px solid var(--border) !important;
      max-width: 100%;
      overflow-x: auto;
    }
    pre code {
      background: transparent !important;
      color: inherit !important;
      padding: 0 !important;
    }
    table {
      display: block;
      max-width: 100%;
      overflow-x: auto;
      -webkit-overflow-scrolling: touch;
      border-color: var(--border) !important;
    }
    table th {
      background: var(--table-th-bg) !important;
      color: var(--text) !important;
      font-size: 14px !important;
      border-color: var(--border) !important;
    }
    table td {
      border-color: var(--border) !important;
      color: var(--text) !important;
    }
    [data-theme="dark"] svg {
      background: #f8fafc;
      border-radius: 8px;
      padding: 4px;
    }

    /* Mobile & iPad Zero-Overflow Protection */
    .katex-display {
      max-width: 100%;
      overflow-x: auto;
      overflow-y: hidden;
      padding: 4px 0;
      -webkit-overflow-scrolling: touch;
    }
    @media (max-width: 960px) {
      aside#sidebar, aside.sidebar {
        transform: translateX(-100%) !important;
      }
      body.sidebar-open aside#sidebar,
      body.sidebar-open aside.sidebar,
      aside#sidebar.open {
        transform: translateX(0) !important;
        box-shadow: 4px 0 24px rgba(15, 23, 42, 0.25);
      }
      main, #main, .main, .content {
        margin-left: 0 !important;
        padding: 20px 16px 60px !important;
        max-width: 100% !important;
      }
      .eju-topbar .topbar-title, header.topbar .topbar-title {
        font-size: 13.5px;
      }
    }
    @media (max-width: 768px) {
      p, li, blockquote, td {
        overflow-wrap: break-word;
        word-break: break-word;
      }
      .katex {
        max-width: 100% !important;
        overflow-x: auto !important;
        overflow-y: hidden !important;
        display: inline-block !important;
        vertical-align: middle !important;
        -webkit-overflow-scrolling: touch;
      }
    }
"""

UNIFIED_TOOLBAR_JS = """
<script id="eju-unified-controls">
(function() {
  const body = document.body;
  const sidebar = document.querySelector('aside#sidebar, aside.sidebar');
  const toggleBtn = document.getElementById('ejuToggleSidebar');
  if (toggleBtn && sidebar) {
    toggleBtn.addEventListener('click', () => {
      if (window.innerWidth <= 960) {
        body.classList.toggle('sidebar-open');
        sidebar.classList.toggle('open');
      } else {
        body.classList.toggle('sidebar-hidden');
      }
    });
    sidebar.addEventListener('click', (e) => {
      if (e.target.closest('a') && window.innerWidth <= 960) {
        body.classList.remove('sidebar-open');
        sidebar.classList.remove('open');
      }
    });
  }
  let allExpanded = false;
  const expandBtn = document.getElementById('ejuExpandAll');
  if (expandBtn) {
    expandBtn.addEventListener('click', () => {
      allExpanded = !allExpanded;
      document.querySelectorAll('aside details').forEach(d => d.open = allExpanded);
      expandBtn.textContent = allExpanded ? '折叠目录' : '展开目录';
    });
  }
  let fontSize = 16;
  const decBtn = document.getElementById('fontDec');
  const incBtn = document.getElementById('fontInc');
  if (decBtn) decBtn.addEventListener('click', () => {
    fontSize = Math.max(13, fontSize - 1);
    document.documentElement.style.setProperty('--font-size', fontSize + 'px');
  });
  if (incBtn) incBtn.addEventListener('click', () => {
    fontSize = Math.min(22, fontSize + 1);
    document.documentElement.style.setProperty('--font-size', fontSize + 'px');
  });
  const themes = ['', 'warm', 'dark'];
  const labels = ['护眼', '深色', '浅色'];
  let tIdx = 0;
  const themeBtn = document.getElementById('themeBtn');
  if (themeBtn) themeBtn.addEventListener('click', () => {
    tIdx = (tIdx + 1) % themes.length;
    if (themes[tIdx]) document.documentElement.setAttribute('data-theme', themes[tIdx]);
    else document.documentElement.removeAttribute('data-theme');
    themeBtn.textContent = labels[tIdx];
  });
})();
</script>
"""


def inject_unified_css(html_text: str) -> str:
    if "Unified EJU 3-Subject Design System" in html_text:
        return html_text
    idx = html_text.rfind("</style>")
    assert idx != -1, "No </style> found"
    return html_text[:idx] + UNIFIED_CSS + "\n  </style>" + html_text[idx + len("</style>"):]


def inject_topbar(html_text: str, title: str) -> str:
    if 'class="eju-topbar"' in html_text:
        return html_text
    topbar_html = f"""<header class="eju-topbar">
  <div class="topbar-left">
    <button class="btn" id="ejuToggleSidebar" title="展开/收起目录">☰ 目录</button>
    <a class="eju-home-link" href="index.html" title="返回三科导航首页">🏠 首页</a>
    <span class="topbar-title">{title}</span>
  </div>
  <div class="topbar-controls">
    <button class="btn" id="ejuExpandAll" title="展开/折叠全部目录">展开目录</button>
    <button class="btn" id="fontDec" title="缩小字号">A-</button>
    <button class="btn" id="fontInc" title="放大字号">A+</button>
    <button class="btn" id="themeBtn" title="切换浅色/护眼/深色主题">护眼</button>
  </div>
</header>
"""
    html_text = re.sub(r"(<body[^>]*>)", r"\1\n" + topbar_html, html_text, count=1)
    if 'id="eju-unified-controls"' not in html_text:
        html_text = html_text.replace("</body>", UNIFIED_TOOLBAR_JS + "\n</body>", 1)
    return html_text


# ---------------------------------------------------------------------------
# 2. Tailored 【讲师批注】 for the 9 Math problems
# ---------------------------------------------------------------------------
MATH_COMMENTARIES = {
    "s7-h4-222": (
        "判别式 $D = b^2 - 4ac$ 仅适用于**实系数**二次方程；EJU 填空题中常把常数项换成含参表达式，看到「実数解の個数」第一时间写出 $D$（若 $b$ 为偶数优先用 $D/4$ 降低计算出错率）。"
    ),
    "s9-h4-260": (
        "指数方程换元 $t = 2^x$ 时，**必须在换元句后紧跟 $t > 0$ 的范围限制**！日本考场评分标准对「正の解のみ適する（只取正根）」的舍根依据非常严格，漏写 $t > 0$ 会直接扣分。"
    ),
    "s20-h3-505": (
        "双曲线标准方程右侧为 $+1$ 时焦点在 $x$ 轴上、为 $-1$ 时焦点在 $y$ 轴上，务必先将常数项化为 $\\pm 1$ 再读 $a, b$；渐近线统一用「把右侧 $\\pm 1$ 改成 $0$」口诀速写，既快又不容易颠倒斜率 $b/a$ 与 $a/b$。"
    ),
    "s35-h4-868": (
        "多项式逐项求导是微积分送分题，唯一易错点是**常数项求导为 $0$** 以及负号与幂次系数相乘时的符号遗漏，算完建议快速检查每一项的次数是否都恰好降了 1 次。"
    ),
    "s36-h4-897": (
        "复合指数函数 $(e^{kx})' = k e^{kx}$ 切忌漏掉内层导数因子 $k$！在 EJU 积分逆运算中也要养成条件反射：见到 $e^{2x}$ 的原函数立刻除以 $2$。"
    ),
    "s36-h4-900": (
        "带根号的函数求导一律先改写为分数指数幂 $x^{m/n}$，套用 $(x^\\alpha)' = \\alpha x^{\\alpha - 1}$ 后再还原为根式；同时注意 $x = 0$ 处导数不存在，定义域须注明 $x > 0$。"
    ),
    "s36-h4-905": (
        "高阶导数只需逐层求导，$n$ 次多项式求导 $n$ 次后变为常数、$n+1$ 次起恒为 $0$；考试中求二阶导 $y''$ 最常用于后续判断曲线凹凸性与変曲点（拐点）。"
    ),
    "s36-h4-918": (
        "考场上看到极限题**第一步永远是先直接代入极限点**，确认是否为 $\\frac{0}{0}$ 或 $\\frac{\\infty}{\\infty}$ 不定型，切忌不看条件就盲目套用洛必达法则！若为 $x \\to \\infty$，记住核心阶数口诀「指数增长 $\\gg$ 多项式 $\\gg$ 对数」。"
    ),
    "s46-h4-1197": (
        "直线与抛物线围成的面积是 EJU 必考高频模型：求出两交点横坐标 $\\alpha < \\beta$ 后，直接套用 $\\frac{1}{6}$ 公式 $S = \\frac{|a|}{6}(\\beta - \\alpha)^3$ 可比展开定积分节省一半以上时间，且大幅降低符号出错率。"
    ),
}


def add_math_commentaries(html_text: str) -> tuple[str, int]:
    added = 0
    for hid, comment in MATH_COMMENTARIES.items():
        # Find heading with id=hid, then locate the next 【最终答案】 block before the next h3/h4
        m_h = re.search(rf'<h([34])\s+id="{re.escape(hid)}"[^>]*>.*?</h\1>', html_text, re.S)
        if not m_h:
            print(f"  WARN: Heading {hid} not found")
            continue
        start = m_h.end()
        # Find next heading of same/higher level
        m_next = re.search(r'<h[1-4]\b', html_text[start:])
        end = start + m_next.start() if m_next else len(html_text)
        section = html_text[start:end]
        if "讲师批注" in section:
            continue
        # Wrap inline $...$ inside comment into <span class="math-inline">$...$</span> and **...** into <strong>
        rendered_comment = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", comment)
        rendered_comment = re.sub(r"\$([^$]+)\$", r'<span class="math-inline">$\1$</span>', rendered_comment)
        callout = f'\n<blockquote class="callout-tip"><p><strong>💡 讲师批注</strong>：{rendered_comment}</p></blockquote>\n'
        # Insert right before the end of this problem section
        html_text = html_text[:end] + callout + html_text[end:]
        added += 1
    return html_text, added


def process_all():
    # 1. Math
    p_math = ROOT / "eju_math_solutions.html"
    txt_math = p_math.read_text(encoding="utf-8")
    txt_math = inject_unified_css(txt_math)
    # Add Home link into Math's existing topbar if missing
    if 'href="index.html"' not in txt_math:
        txt_math = txt_math.replace(
            '<button class="btn" id="toggleSidebar" title="展开/收起目录">☰ 目录</button>',
            '<button class="btn" id="toggleSidebar" title="展开/收起目录">☰ 目录</button>\n    <a class="eju-home-link" href="index.html" title="返回三科导航首页">🏠 首页</a>',
            1,
        )
    # Fix Math's mobile sidebar toggle to also toggle sidebar-open
    txt_math = txt_math.replace(
        "body.classList.toggle('sidebar-hidden');",
        "if (window.innerWidth <= 960) { body.classList.toggle('sidebar-open'); } else { body.classList.toggle('sidebar-hidden'); }",
    )
    txt_math, added = add_math_commentaries(txt_math)
    p_math.write_text(txt_math, encoding="utf-8")
    print(f"[MATH] Unified theme/CSS + Home link + added {added}/9 讲师批注")

    # 2. Physics
    p_phys = ROOT / "eju_physics_solutions.html"
    txt_phys = p_phys.read_text(encoding="utf-8")
    txt_phys = inject_unified_css(txt_phys)
    txt_phys = inject_topbar(txt_phys, "EJU 物理教材全解终稿（力学・热力学・波动・电磁学・原子物理）")
    p_phys.write_text(txt_phys, encoding="utf-8")
    print("[PHYSICS] Unified theme/CSS + Topbar (Home / TOC / A- / A+ / Theme)")

    # 3. Chemistry
    p_chem = ROOT / "eju_chemistry_solutions.html"
    txt_chem = p_chem.read_text(encoding="utf-8")
    txt_chem = inject_unified_css(txt_chem)
    txt_chem = inject_topbar(txt_chem, "EJU 化学教材全解终稿（格致学苑・13 切片全解 + 全局术语表）")
    p_chem.write_text(txt_chem, encoding="utf-8")
    print("[CHEMISTRY] Unified theme/CSS + Topbar (Home / TOC / A- / A+ / Theme)")


if __name__ == "__main__":
    process_all()
