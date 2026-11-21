# 《EJU 教材全解与备课讲义》数学 028-a（P406–P410）

> **对应源文件**：`work_math/ocr_md/ocr_028_p406-420.md`（前半部分：第十一章《微分積分》之「定積分の応用・面積」演習問題 17 (13)–(23)；后半部分 P411–P420 见 `note_028_b.md`）
> **视觉核对参考图**：`work_math/ref_imgs/page_0406.jpg` – `page_0410.jpg`（对应教材印制页码 P405–P409）

---

## 一、国内高中基础知识点唤醒与 EJU 考纲差异对比

本讲义对应日本高中 **数学Ⅱ・数学Ⅲ（積分法の応用：面積）** 的高阶综合题型，涵盖 **对称隐函数曲线面积、参数方程面积、面积二等分与等积条件、含参面积最值、三次/四次函数切线面积、含绝对值定积分最值、以 $y$ 为积分变量的面积计算** 七大核心模块。

### 1.1 定积分求面积的 5 大核心公式与技巧

1. **普通直角坐标（对 $x$ 积分）**：在区间 $[a, b]$ 上，曲线 $y = f(x)$ 与 $y = g(x)$ 围成的面积为
   $$S = \int_a^b |f(x) - g(x)|\,dx$$
2. **以 $y$ 为积分变量（对 $y$ 积分）**：在区间 $[c, d]$ 上，曲线 $x = f(y)$ 与 $x = g(y)$ 围成的面积为（右减左）
   $$S = \int_c^d |f(y) - g(y)|\,dy$$
3. **参数方程（媒介変数表示）面积**：若 $x = x(t),\; y = y(t)$，当 $t$ 从 $\alpha$ 变到 $\beta$ 时 $x$ 从 $a$ 单调变到 $b$ 且 $y \ge 0$，则
   $$S = \int_a^b y\,dx = \int_\alpha^\beta y(t)\,x'(t)\,dt$$
   > 注意上下限必须严格对应 $x$ 的起点 $a$ 与终点 $b$，切勿随意颠倒导致符号出错！
4. **EJU 考场必背「面积速算公式」（$\frac{1}{6}$・$\frac{1}{12}$・$\frac{1}{30}$ 公式）**：
   - **$\frac{1}{6}$ 公式（二次函数与直线 / 两二次函数）**：
     $$\int_\alpha^\beta (x - \alpha)(x - \beta)\,dx = -\frac{1}{6}(\beta - \alpha)^3 \quad (\alpha < \beta)$$
   - **$\frac{1}{30}$ 公式（四次函数与二重切线）**：
     $$\int_\alpha^\beta (x - \alpha)^2(x - \beta)^2\,dx = \frac{1}{30}(\beta - \alpha)^5 \quad (\alpha < \beta)$$
5. **两区域面积相等的充要条件（定积分抵消法）**：
   若曲线 $y = f(x)$ 与 $y = g(x)$ 依次交于 $x = \alpha < \beta < \gamma$，则两块封闭区域面积相等 $\iff$
   $$\int_\alpha^\gamma \{f(x) - g(x)\}\,dx = 0$$
   特别地，对三次函数与直线所围两块区域，面积相等 $\iff$ **中间交点恰好为三次函数的拐点（変曲点）**！

### 1.2 国内高中 vs. 日本 EJU 考纲差异对比

| 对比维度 | 国内高中习惯 | 日本 EJU 习惯 | 备课/应试提醒 |
| :--- | :--- | :--- | :--- |
| **定积分考纲地位** | 新高考已大幅删减微积分（不再考定积分求面积） | **理系数学（コース2）压轴大题核心** | 国内学生普遍缺乏熟练的积分变形与作图训练，需重点补强 |
| **参数方程求面积** | 几乎不涉及 | **高频常规考点**（如椭圆、摆线、利萨如曲线） | 牢记 $dx = x'(t)\,dt$ 及上下限替换时的方向（$x$ 从小到大） |
| **$\frac{1}{6}$ / $\frac{1}{30}$ 速算公式** | 仅作选学技巧 | **EJU 填空题提速神技** | 解答题中可用换元法 $t = x - \alpha$ 规范推导，填空题可直接套用 |
| **对 $y$ 积分（横切）** | 较少强调 | **常考题型**（如 $x = y^2 - 3y$ 型抛物线） | 遇到「$x$ 是 $y$ 的二次函数」时，立刻切换为 $\int_c^d (x_{\text{右}} - x_{\text{左}})\,dy$ |
| **含绝对值积分最值** | 几乎不考 | **经典压轴题**（如 $\int_0^1 |x^2 - tx|\,dx$） | 按零点 $x = t$ 与积分区间 $[0, 1]$ 的位置关系分 3 类讨论 |

---

## 二、日文核心词汇与公式假名注音

### 2.1 本部分日文核心词汇

- 面積（めんせき / menseki） — 面积
- 媒介変数（ばいかいへんすう / baikai hensuu） — 参数（媒介变量）
- 2等分する（にとうぶんする / nitoubun suru） — 二等分
- 分割する（ぶんかつする / bunkatsu suru） — 分割
- 接線（せっせん / sessen） — 切线
- 接する（せっする / sessuru） — 相切
- 最小値（さいしょうち / saishouchi） — 最小值
- 最大値（さいだいち / saidaichi） — 最大值
- 囲まれた図形（かこまれたずけい / kakomareta zukei） — 所围成的图形
- 対称性（たいしょうせい / taishousei） — 对称性

### 2.2 核心公式的日本课堂口语读法

1. **参数方程面积公式** $S = \displaystyle\int_a^b y\,dx = \int_\alpha^\beta y(t)\,\frac{dx}{dt}\,dt$
   - 课堂读法：**エス イコール インテグラル エーから ビーまでの ワイ ディーエックス イコール インテグラル アルファから ベータまでの ワイ ティー、ディーエックス ディーティー、ディーティー**
2. **$\frac{1}{6}$ 面积公式** $\displaystyle\int_\alpha^\beta (x-\alpha)(x-\beta)\,dx = -\frac{1}{6}(\beta-\alpha)^3$
   - 课堂读法：**インテグラル アルファから ベータまでの、エックス ひく アルファ かける エックス ひく ベータ ディーエックス イコール マイナス ろくぶんのいち かっこ ベータ ひく アルファ かっことじ の さんじょう**（俗称 **ろくぶんのいち公式 / $\frac{1}{6}$ 公式**）
3. **以 $y$ 为积分变量的面积** $S = \displaystyle\int_c^d x\,dy$
   - 课堂读法：**エス イコール インテグラル シーから ディーまでの エックス ディーワイ**

---

## 三、逐题深度解析（不可跳步）

---

### 演習問題 17（定積分の応用：面積）

#### 演習問題 17-(13)
- **【原题重现与翻译】**
  - 原题：曲線 $(x^2 - 2)^2 + y^2 = 4$ で囲まれる部分の面積 $S$ を求めよ。
  - 中文：求曲线 $(x^2 - 2)^2 + y^2 = 4$ 所围成部分的面积 $S$。
- **【考点定位】**
  - 隐函数曲线的对称性分析 + 换元积分法（置換積分法）。
- **【图解辅助（SVG 矢量图）】**
  曲线呈水平「8 字形（双叶闭曲线）」，关于 $x$ 轴、$y$ 轴均对称，四个象限面积完全相等：

<svg viewBox="0 0 460 240" width="460" height="240" xmlns="http://www.w3.org/2000/svg" style="background:#fafafa;border:1px solid #e0e0e0;border-radius:6px;">
  <style>
    .axis { stroke: #333; stroke-width: 1.4; }
    .curve { fill: #d6eaf8; fill-opacity: 0.6; stroke: #2471a3; stroke-width: 2.2; }
    .q1 { fill: #f9e79f; fill-opacity: 0.75; stroke: #d35400; stroke-width: 2.2; }
    .lbl { font: 12px sans-serif; fill: #2c3e50; }
    .math { font: italic 12px serif; fill: #2c3e50; }
  </style>
  <!-- Axes -->
  <line x1="40" y1="120" x2="420" y2="120" class="axis"/>
  <polygon points="420,120 412,116 412,124" fill="#333"/>
  <line x1="230" y1="225" x2="230" y2="15" class="axis"/>
  <polygon points="230,15 226,23 234,23" fill="#333"/>
  <!-- Left & Right loops: x in [-2,2] mapped to [100,360] (scale 65px/unit), y in [-2,2] (scale 40px/unit) -->
  <!-- Full figure-8 path approximated smoothly -->
  <path d="M 230,120 C 260,70 310,40 340,60 C 365,78 365,162 340,180 C 310,200 260,170 230,120 C 200,70 150,40 120,60 C 95,78 95,162 120,180 C 150,200 200,170 230,120 Z" class="curve"/>
  <!-- Highlight Q1 (1/4 area) -->
  <path d="M 230,120 C 260,70 310,40 340,60 C 355,70 360,95 360,120 L 230,120 Z" class="q1"/>
  <!-- Ticks & labels -->
  <circle cx="230" cy="120" r="3" fill="#2c3e50"/>
  <circle cx="360" cy="120" r="3" fill="#c0392b"/>
  <circle cx="100" cy="120" r="3" fill="#2471a3"/>
  <text x="415" y="138" class="math">x</text>
  <text x="238" y="25" class="math">y</text>
  <text x="216" y="136" class="lbl">O</text>
  <text x="364" y="136" class="lbl">2</text>
  <text x="84" y="136" class="lbl">-2</text>
  <text x="290" y="96" class="lbl" fill="#a04000" font-weight="bold">S/4</text>
  <text x="265" y="38" class="math">y = x√(4 - x²)</text>
  <text x="16" y="24" class="lbl" font-weight="bold">(x² - 2)² + y² = 4（关于两坐标轴对称）</text>
</svg>

- **【分步标准解答】**
  1. **対称性と定義域の確認**：
     方程式 $(x^2 - 2)^2 + y^2 = 4$ において、$x$ を $-x$ に、また $y$ を $-y$ に置き換えても式は変わらない。
     よって、この曲線は $x$ 軸および $y$ 軸に関して対称である。
     > 💡 讲师批注：凡是方程中只含 $x^2$ 与 $y^2$ 的曲线，必同时关于 $x$ 轴、$y$ 轴、原点对称！只需算第一象限面积再乘以 $4$，可极大简化计算并避免绝对值分情况讨论。

  2. **第一象限（$x \ge 0,\; y \ge 0$）での陽関数表示**：
     $$y^2 = 4 - (x^2 - 2)^2 = 4 - (x^4 - 4x^2 + 4) = 4x^2 - x^4 = x^2(4 - x^2)$$
     $y^2 \ge 0$ より $4 - x^2 \ge 0$、すなわち $-2 \le x \le 2$。
     特に $x \ge 0,\; y \ge 0$ のとき、
     $$y = x\sqrt{4 - x^2} \qquad (0 \le x \le 2)$$
     > 💡 讲师批注：展开 $4 - (x^2-2)^2$ 时常数项 $4$ 恰好抵消，留下 $x^2(4-x^2)$。因 $x \ge 0$，开根号直接得到 $x\sqrt{4-x^2}$（无需加绝对值）。

  3. **置換積分による面積計算**：
     対称性より、
     $$S = 4 \int_0^2 x\sqrt{4 - x^2}\,dx$$
     ここで $u = 4 - x^2$ とおくと、$du = -2x\,dx$ より $x\,dx = -\dfrac{1}{2}\,du$。
     また、$x : 0 \to 2$ のとき $u : 4 \to 0$ であるから、
     $$S = 4 \int_4^0 \sqrt{u}\left(-\frac{1}{2}\right)du = 2 \int_0^4 u^{\frac{1}{2}}\,du$$
     > 💡 讲师批注：换元后利用负号把积分上下限 $4 \to 0$ 翻转为 $0 \to 4$，更不易算错符号。

     $$= 2 \left[\frac{2}{3} u^{\frac{3}{2}}\right]_0^4 = \frac{4}{3} \cdot 4^{\frac{3}{2}} = \frac{4}{3} \cdot 8 = \frac{32}{3}$$
- **【最终答案】**
  **$S = \dfrac{32}{3}$**

---

#### 演習問題 17-(14)
- **【原题重现与翻译】**
  - 原题：媒介変数 $t$ によって、$x = 4\cos t,\; y = \sin 2t \;\left(0 \le t \le \dfrac{\pi}{2}\right)$ と表される曲線と $x$ 軸で囲まれた部分の面積 $S$ を求めよ。
  - 中文：求由参数 $t$ 表示的曲线 $x = 4\cos t,\; y = \sin 2t \;\left(0 \le t \le \dfrac{\pi}{2}\right)$ 与 $x$ 轴所围成部分的面积 $S$。
- **【考点定位】**
  - 参数方程（媒介変数表示）的定积分求面积 + 二倍角公式 + 凑微分法。
- **【图解辅助（SVG 矢量图）】**
  当 $t$ 从 $0$ 增至 $\frac{\pi}{2}$ 时，点 $(x, y)$ 从 $(4, 0)$ 出发，经最高点 $(2\sqrt{2}, 1)$（$t = \frac{\pi}{4}$），回到原点 $(0, 0)$：

<svg viewBox="0 0 420 200" width="420" height="200" xmlns="http://www.w3.org/2000/svg" style="background:#fafafa;border:1px solid #e0e0e0;border-radius:6px;">
  <style>
    .axis { stroke: #333; stroke-width: 1.4; }
    .area { fill: #d5f5e3; stroke: #1e8449; stroke-width: 2.2; }
    .lbl { font: 12px sans-serif; fill: #2c3e50; }
    .math { font: italic 12px serif; fill: #2c3e50; }
  </style>
  <line x1="40" y1="160" x2="390" y2="160" class="axis"/>
  <polygon points="390,160 382,156 382,164" fill="#333"/>
  <line x1="70" y1="185" x2="70" y2="20" class="axis"/>
  <polygon points="70,20 66,28 74,28" fill="#333"/>
  <!-- Curve: x in [0,4] -> [70, 350] (70px/unit), y in [0,1] -> [160, 60] (100px/unit) -->
  <!-- Peak at t=pi/4: x=2.828 -> 268, y=1 -> 60 -->
  <path d="M 70,160 C 120,90 210,60 268,60 C 315,60 345,105 350,160 Z" class="area"/>
  <!-- Peak marker -->
  <line x1="268" y1="60" x2="268" y2="160" stroke="#7f8c8d" stroke-dasharray="4,3"/>
  <circle cx="268" cy="60" r="3.5" fill="#1e8449"/>
  <circle cx="350" cy="160" r="3.5" fill="#c0392b"/>
  <circle cx="70" cy="160" r="3.5" fill="#c0392b"/>
  <text x="385" y="178" class="math">x</text>
  <text x="78" y="28" class="math">y</text>
  <text x="55" y="176" class="lbl">O</text>
  <text x="346" y="176" class="lbl">4</text>
  <text x="252" y="176" class="lbl">2√2</text>
  <text x="275" y="55" class="lbl">(2√2, 1) [t = π/4]</text>
  <text x="322" y="148" class="lbl" fill="#c0392b">t = 0</text>
  <text x="78" y="148" class="lbl" fill="#c0392b">t = π/2</text>
  <text x="195" y="128" class="lbl" font-weight="bold" fill="#196f3d">S</text>
</svg>

- **【分步标准解答】**
  1. **$x, y$ の増減と範囲の確認**：
     $0 \le t \le \dfrac{\pi}{2}$ において、
     - $\dfrac{dx}{dt} = -4\sin t \le 0$ より、$x = 4\cos t$ は $t = 0$ のとき $4$ から $t = \dfrac{\pi}{2}$ のとき $0$ まで単調に減少する。
     - $0 \le 2t \le \pi$ より、$y = \sin 2t \ge 0$ である。
     > 💡 讲师批注：用参数方程算面积前，务必确认两点：① $y$ 的符号（恒 $\ge 0$）；② $x$ 随 $t$ 的单调性及端点对应关系（$x=0 \leftrightarrow t=\frac{\pi}{2}$，$x=4 \leftrightarrow t=0$）。

  2. **定積分の立式と置換計算**：
     $$S = \int_0^4 y\,dx = \int_{\frac{\pi}{2}}^0 \sin 2t \cdot \frac{dx}{dt}\,dt = \int_{\frac{\pi}{2}}^0 \sin 2t \cdot (-4\sin t)\,dt$$
     > 💡 讲师批注：特别注意下限 $x=0$ 对应 $t=\frac{\pi}{2}$，上限 $x=4$ 对应 $t=0$！切勿错写成 $\int_0^{\pi/2}$ 导致面积变负。

     $$= 4 \int_0^{\frac{\pi}{2}} \sin 2t \sin t\,dt$$
     2倍角の公式 $\sin 2t = 2\sin t \cos t$ を用いると、
     $$S = 4 \int_0^{\frac{\pi}{2}} (2\sin t \cos t)\sin t\,dt = 8 \int_0^{\frac{\pi}{2}} \sin^2 t \cos t\,dt$$
     ここで $u = \sin t$ とおくと $du = \cos t\,dt$、$t : 0 \to \dfrac{\pi}{2}$ のとき $u : 0 \to 1$ であるから、
     $$S = 8 \int_0^1 u^2\,du = 8 \left[\frac{1}{3}u^3\right]_0^1 = \frac{8}{3}$$
- **【最终答案】**
  **$S = \dfrac{8}{3}$**

---

#### 演習問題 17-(15)
- **【原题重现与翻译】**
  - 原题：放物線 $y = -x(x - 2)$ と $x$ 軸で囲まれた図形の面積が、直線 $y = ax$ によって $2$ 等分されるとき、定数 $a$ の値を求めよ。ただし、$0 < a < 2$ とする。
  - 中文：当抛物线 $y = -x(x - 2)$ 与 $x$ 轴所围成图形的面积被直线 $y = ax$ 二等分时，求常数 $a$ 的值。其中 $0 < a < 2$。
- **【考点定位】**
  - 二次函数与直线的面积二等分问题 + $\frac{1}{6}$ 面积速算公式。
- **【图解辅助（SVG 矢量图）】**

<svg viewBox="0 0 380 210" width="380" height="210" xmlns="http://www.w3.org/2000/svg" style="background:#fafafa;border:1px solid #e0e0e0;border-radius:6px;">
  <style>
    .axis { stroke: #333; stroke-width: 1.4; }
    .par { fill: none; stroke: #2471a3; stroke-width: 2.2; }
    .lin { stroke: #c0392b; stroke-width: 2; }
    .top-a { fill: #fadbd8; fill-opacity: 0.7; }
    .bot-a { fill: #d6eaf8; fill-opacity: 0.6; }
    .lbl { font: 12px sans-serif; fill: #2c3e50; }
    .math { font: italic 12px serif; fill: #2c3e50; }
  </style>
  <line x1="40" y1="165" x2="350" y2="165" class="axis"/>
  <polygon points="350,165 342,161 342,169" fill="#333"/>
  <line x1="80" y1="190" x2="80" y2="20" class="axis"/>
  <polygon points="80,20 76,28 84,28" fill="#333"/>
  <!-- x in [0,2] -> [80, 300] (110px/unit), y in [0,1] -> [165, 55] (110px/unit) -->
  <!-- Parabola y = -x^2 + 2x: (0,0)->(80,165), (1,1)->(190,55), (2,0)->(300,165) -->
  <!-- Quadratic Bezier control point for exact parabola: (190, -55) -->
  <!-- Line y = ax with a = 2 - cbrt(4) ≈ 0.4126, intersect at x = 2-a ≈ 1.5874 -> px=254.6, y = 0.655 -> py=93 -->
  <path d="M 80,165 Q 190,-55 300,165 Z" class="bot-a"/>
  <path d="M 80,165 Q 167,10 254.6,93 L 80,165 Z" class="top-a"/>
  <path d="M 80,165 Q 190,-55 300,165" class="par"/>
  <line x1="60" y1="173" x2="310" y2="70" class="lin"/>
  <line x1="254.6" y1="93" x2="254.6" y2="165" stroke="#7f8c8d" stroke-dasharray="4,3"/>
  <circle cx="254.6" cy="93" r="3.5" fill="#c0392b"/>
  <text x="345" y="182" class="math">x</text>
  <text x="88" y="28" class="math">y</text>
  <text x="65" y="181" class="lbl">O</text>
  <text x="296" y="181" class="lbl">2</text>
  <text x="242" y="181" class="math">2 - a</text>
  <text x="155" y="95" class="lbl" fill="#922b21" font-weight="bold">S₁ = S/2</text>
  <text x="195" y="145" class="lbl" fill="#1b4f72" font-weight="bold">S/2</text>
  <text x="278" y="65" class="math" fill="#c0392b">y = ax</text>
  <text x="160" y="42" class="math" fill="#2471a3">y = -x(x-2)</text>
</svg>

- **【分步标准解答】**
  1. **全体の面積 $S$ を求める**：
     放物線 $y = -x(x - 2) = -x^2 + 2x$ と $x$ 軸の交点は $x = 0,\; 2$ である。
     $0 \le x \le 2$ で $y \ge 0$ より、全体の面積 $S$ は、
     $$S = \int_0^2 (-x^2 + 2x)\,dx = -\int_0^2 x(x - 2)\,dx = \frac{1}{6}(2 - 0)^3 = \frac{4}{3}$$
     > 💡 讲师批注：直接套用 $\frac{1}{6}$ 公式，无需展开成 $\left[-\frac{x^3}{3} + x^2\right]_0^2$（当然展开算也能得到 $-\frac{8}{3} + 4 = \frac{4}{3}$ 作为验算）。

  2. **放物線と直線 $y = ax$ の交点と上部の面積 $S_1$**：
     $-x(x - 2) = ax$ を解くと、
     $$x^2 - (2 - a)x = 0 \implies x\{x - (2 - a)\} = 0 \implies x = 0,\; 2 - a$$
     条件 $0 < a < 2$ より $0 < 2 - a < 2$ であるから、直線 $y = ax$ は確かに図形を $2$ つの部分に分ける。
     放物線と直線で囲まれた上部の面積を $S_1$ とすると、
     $$S_1 = \int_0^{2-a} \{(-x^2 + 2x) - ax\}\,dx = -\int_0^{2-a} x\{x - (2 - a)\}\,dx = \frac{1}{6}(2 - a)^3$$
     > 💡 讲师批注：把「上部的弓形面积」$S_1$ 作为研究对象最巧妙，因为它恰好又是抛物线与直线围成的区域，能**第二次直接套用 $\frac{1}{6}$ 公式**！千万别去算下面那块需要分段积分的区域。

  3. **面積 $2$ 等分の条件から $a$ を求める**：
     $S_1 = \dfrac{1}{2} S$ より、
     $$\frac{1}{6}(2 - a)^3 = \frac{1}{2} \cdot \frac{1}{6} \cdot 2^3$$
     両辺に $6$ を掛けて、
     $$(2 - a)^3 = 4$$
     $2 - a$ は実数であるから、
     $$2 - a = \sqrt[3]{4} \implies a = 2 - \sqrt[3]{4}$$
     ここで $1^3 < 4 < 2^3$ すなわち $1 < \sqrt[3]{4} < 2$ より、$0 < 2 - \sqrt[3]{4} < 1 < 2$ となり、条件 $0 < a < 2$ を満たす。
     > 💡 讲师批注：EJU 中遇到三次方程 $(2-a)^3 = 4$，一定要在最后验证结果是否满足题目给定的参数范围 $0 < a < 2$！
- **【最终答案】**
  **$a = 2 - \sqrt[3]{4}$**

---

#### 演習問題 17-(16)
- **【原题重现与翻译】**
  - 原题：曲線 $y = \cos x \;\left(-\dfrac{\pi}{2} \le x \le \dfrac{\pi}{2}\right)$ と $x$ 軸で囲まれた図形を $E$ とする。曲線上の点 $(t, \cos t)$ を通る傾きが $1$ の直線 $l$ で $E$ を分割する。こうして得られた $2$ つの図形の面積が等しくなるとき、$\cos t$ の値を求めよ。
  - 中文：设曲线 $y = \cos x \;\left(-\dfrac{\pi}{2} \le x \le \dfrac{\pi}{2}\right)$ 与 $x$ 轴所围成的图形为 $E$。用过曲线上一点 $(t, \cos t)$ 且斜率为 $1$ 的直线 $l$ 将 $E$ 分割。当所得到的两个图形面积相等时，求 $\cos t$ 的值。
- **【考点定位】**
  - 三角函数定积分 + 凸性与切线斜率位置判定 + 等腰直角三角形几何面积巧算。
- **【图解辅助（SVG 矢量图）】**
  因为曲线斜率 $y' = -\sin x < 1$（$x > -\frac{\pi}{2}$），故过 $P(t, \cos t)$ 斜率为 $1$ 的直线 $l$ 必从 $P$ 左下方穿过 $E$ 交 $x$ 轴于 $Q(t - \cos t, 0)$，形成等腰直角三角形 $\triangle PQH$：

<svg viewBox="0 0 440 220" width="440" height="220" xmlns="http://www.w3.org/2000/svg" style="background:#fafafa;border:1px solid #e0e0e0;border-radius:6px;">
  <style>
    .axis { stroke: #333; stroke-width: 1.4; }
    .curve { fill: none; stroke: #2471a3; stroke-width: 2.2; }
    .lin { stroke: #c0392b; stroke-width: 2; }
    .left-a { fill: #d6eaf8; fill-opacity: 0.7; }
    .tri { fill: #fadbd8; fill-opacity: 0.7; stroke: #c0392b; stroke-width: 1.2; stroke-dasharray: 4,2; }
    .lbl { font: 12px sans-serif; fill: #2c3e50; }
    .math { font: italic 12px serif; fill: #2c3e50; }
  </style>
  <line x1="30" y1="175" x2="410" y2="175" class="axis"/>
  <polygon points="410,175 402,171 402,179" fill="#333"/>
  <line x1="220" y1="200" x2="220" y2="20" class="axis"/>
  <polygon points="220,20 216,28 224,28" fill="#333"/>
  <!-- x in [-pi/2, pi/2] -> [80, 360] (scale ~89.1px/unit), y in [0,1] -> [175, 55] (120px/unit) -->
  <!-- cos x curve: (-pi/2,0)=(80,175), (0,1)=(220,55), (pi/2,0)=(360,175) -->
  <!-- P at t ≈ 0.427 (sin t = sqrt(2)-1, cos t ≈ 0.910): px = 220 + 0.427*89.1 = 258, py = 175 - 0.910*120 = 66 -->
  <!-- Q at x0 = t - cos t ≈ -0.483: qx = 220 - 0.483*89.1 = 177, qy = 175 -->
  <!-- Shade left area E_L -->
  <path d="M 80,175 C 125,95 170,55 220,55 C 235,55 248,59 258,66 L 177,175 Z" class="left-a"/>
  <!-- Triangle PQH -->
  <polygon points="258,66 177,175 258,175" class="tri"/>
  <!-- Full cosine curve -->
  <path d="M 80,175 C 125,95 170,55 220,55 C 270,55 315,95 360,175" class="curve"/>
  <!-- Line l -->
  <line x1="158" y1="200" x2="290" y2="23" class="lin"/>
  <!-- Points -->
  <circle cx="258" cy="66" r="3.5" fill="#c0392b"/>
  <circle cx="177" cy="175" r="3.5" fill="#c0392b"/>
  <circle cx="258" cy="175" r="3" fill="#2c3e50"/>
  <!-- Right angle mark -->
  <polyline points="248,175 248,165 258,165" fill="none" stroke="#555" stroke-width="1"/>
  <text x="405" y="192" class="math">x</text>
  <text x="228" y="28" class="math">y</text>
  <text x="70" y="192" class="lbl">-π/2</text>
  <text x="352" y="192" class="lbl">π/2</text>
  <text x="208" y="191" class="lbl">O</text>
  <text x="150" y="193" class="math" fill="#c0392b">Q(t-cos t, 0)</text>
  <text x="253" y="192" class="math">H(t,0)</text>
  <text x="266" y="64" class="math" fill="#c0392b">P(t, cos t)</text>
  <text x="285" y="36" class="math" fill="#c0392b">l（傾き1）</text>
  <text x="148" y="128" class="lbl" font-weight="bold" fill="#1b4f72">左側 S₁ = 1</text>
  <text x="225" y="150" class="lbl" fill="#922b21">½cos²t</text>
</svg>

- **【分步标准解答】**
  1. **図形 $E$ の総面積 $S$**：
     $$S = \int_{-\frac{\pi}{2}}^{\frac{\pi}{2}} \cos x\,dx = [\sin x]_{-\frac{\pi}{2}}^{\frac{\pi}{2}} = 1 - (-1) = 2$$
     よって、$2$ 等分された各部分の面積は $1$ である。

  2. **直線 $l$ の方程式と $E$ との位置関係**：
     点 $P(t, \cos t)$ を通り傾きが $1$ の直線 $l$ の方程式は、
     $$y - \cos t = 1 \cdot (x - t) \implies y = x - t + \cos t$$
     ここで $g(x) = \cos x - (x - t + \cos t)$ とおくと、
     $$g'(x) = -\sin x - 1 \le 0 \qquad \left(-\frac{\pi}{2} \le x \le \frac{\pi}{2}\right)$$
     であり、等号は $x = -\dfrac{\pi}{2}$ のみで成り立つから、$g(x)$ は区間 $\left[-\dfrac{\pi}{2}, \dfrac{\pi}{2}\right]$ で単調に減少する。
     $g(t) = 0$ であるから、$-\dfrac{\pi}{2} \le x < t$ では $g(x) > 0$（曲線が直線より上）、$t < x \le \dfrac{\pi}{2}$ では $g(x) < 0$（直線が曲線より上）となる。
     また、直線 $l$ と $x$ 軸の交点 $Q$ の $x$ 座標は $x = t - \cos t$ であり、
     $$g\left(-\frac{\pi}{2}\right) = \frac{\pi}{2} + t - \cos t > 0 \implies -\frac{\pi}{2} < t - \cos t \le t$$
     > 💡 讲师批注：这一步「证明直线 $l$ 不会与 $y = \cos x$ 再次相交，且交点 $Q$ 必落在线段 $\left(-\frac{\pi}{2}, t\right]$ 内」是日本考场拿满分的严密关键！因为 $y = \cos x$ 在 $[-\frac{\pi}{2}, \frac{\pi}{2}]$ 的最大切线斜率是 $1$（仅在左端点取得），所以斜率为 $1$ 的直线必然一穿而过。

  3. **左側の面積 $S_1$ の立式と方程式の解法**：
     点 $P(t, \cos t)$ から $x$ 軸に下ろした垂線の足を $H(t, 0)$ とすると、$\triangle PQH$ は $QH = t - (t - \cos t) = \cos t$、$PH = \cos t$ の直角二等辺三角形である。
     よって、直線 $l$ より左側の図形の面積 $S_1$ は、
     $$S_1 = \int_{-\frac{\pi}{2}}^t \cos x\,dx - \triangle PQH = [\sin x]_{-\frac{\pi}{2}}^t - \frac{1}{2}\cos^2 t = (\sin t + 1) - \frac{1}{2}\cos^2 t$$
     > 💡 讲师批注：把「积分区域减去等腰直角三角形」这一步看出来，能省去对直线 $l$ 的繁琐积分！直角边 $QH = t - (t - \cos t) = \cos t$，面积直接是 $\frac{1}{2}\cos^2 t$。

     条件 $S_1 = 1$ より、
     $$\sin t + 1 - \frac{1}{2}\cos^2 t = 1 \implies \sin t = \frac{1}{2}\cos^2 t \quad \cdots ①$$
     $\cos^2 t = 1 - \sin^2 t$ を代入すると、
     $$2\sin t = 1 - \sin^2 t \implies \sin^2 t + 2\sin t - 1 = 0$$
     これを解くと $\sin t = -1 \pm \sqrt{2}$。
     $-1 \le \sin t \le 1$ であるから、
     $$\sin t = \sqrt{2} - 1$$
     ① より $\cos^2 t = 2\sin t = 2(\sqrt{2} - 1) = 2\sqrt{2} - 2$。
     $-\dfrac{\pi}{2} \le t \le \dfrac{\pi}{2}$ より $\cos t \ge 0$ であるから、
     $$\cos t = \sqrt{2\sqrt{2} - 2}$$
- **【最终答案】**
  **$\cos t = \sqrt{2\sqrt{2} - 2}$**

---

#### 演習問題 17-(17)
- **【原题重现与翻译】**
  - 原题（原文照录）：点 $(1, 2)$ を通る直線 $y = x^2$ で囲まれた図形の面積を $S$ とする。$S$ の最大値を求めよ。
  > ⚠️ **教材勘误提示**：原教材第 407 页（`page_0408.jpg`）存在两处明显印刷错误：
  > 1. 题干漏印了「と放物線」，应为「点 $(1, 2)$ を通る直線**と放物線** $y = x^2$ で囲まれた図形の面積を $S$ とする。」
  > 2. 极值方向印反！点 $(1, 2)$ 位于抛物线 $y = x^2$ 内部（$2 > 1^2$），过该点的任意非竖直线与抛物线围成的面积 $S \to +\infty$（当斜率 $|m| \to \infty$ 时），**不存在最大值**，而是存在**最小值（最小値）**！故应修正为「$S$ の**最小値**を求めよ。」
  - 中文（修正后）：设过点 $(1, 2)$ 的直线与抛物线 $y = x^2$ 所围成图形的面积为 $S$。求 $S$ 的最小值。
- **【考点定位】**
  - 直线与抛物线联立 + 韦达定理（解と係数の関係）+ $\frac{1}{6}$ 面积公式 + 二次函数配方求最值。
- **【图解辅助（SVG 矢量图）】**

<svg viewBox="0 0 360 220" width="360" height="220" xmlns="http://www.w3.org/2000/svg" style="background:#fafafa;border:1px solid #e0e0e0;border-radius:6px;">
  <style>
    .axis { stroke: #333; stroke-width: 1.4; }
    .par { fill: none; stroke: #2471a3; stroke-width: 2.2; }
    .lin { stroke: #c0392b; stroke-width: 2; }
    .area { fill: #fadbd8; fill-opacity: 0.65; }
    .lbl { font: 12px sans-serif; fill: #2c3e50; }
    .math { font: italic 12px serif; fill: #2c3e50; }
  </style>
  <line x1="30" y1="185" x2="330" y2="185" class="axis"/>
  <polygon points="330,185 322,181 322,189" fill="#333"/>
  <line x1="150" y1="205" x2="150" y2="15" class="axis"/>
  <polygon points="150,15 146,23 154,23" fill="#333"/>
  <!-- Origin (150, 185), scale x: 45px/unit, y: 26px/unit -->
  <!-- y = x^2: (-2,4)=(60,81), (0,0)=(150,185), (1,1)=(195,159), (2.414, 5.83)=(258.6, 33.4) -->
  <!-- Min area line m=2: y = 2x, passes (1,2)=(195,133), intersects at x=0 and x=2 -> (150,185) and (240,81) -->
  <!-- Area between y=2x and y=x^2 from x=0 to x=2 -->
  <path d="M 150,185 Q 195,185 240,81 L 150,185 Z" class="area"/>
  <!-- Full parabola x in [-2.2, 2.5]: using Q Bezier -->
  <path d="M 51,59 Q 150,311 262.5,22.5" class="par"/>
  <!-- Optimal line y = 2x -->
  <line x1="120" y1="220" x2="265" y2="52" class="lin"/>
  <circle cx="195" cy="133" r="4" fill="#c0392b"/>
  <circle cx="150" cy="185" r="3" fill="#2c3e50"/>
  <circle cx="240" cy="81" r="3.5" fill="#2471a3"/>
  <text x="322" y="200" class="math">x</text>
  <text x="158" y="25" class="math">y</text>
  <text x="136" y="200" class="lbl">O</text>
  <text x="202" y="138" class="lbl" fill="#c0392b" font-weight="bold">P(1, 2)</text>
  <text x="246" y="82" class="lbl">(2, 4)</text>
  <text x="65" y="45" class="math" fill="#2471a3">y = x²</text>
  <text x="240" y="45" class="math" fill="#c0392b">y = 2x (m=2)</text>
  <text x="180" y="160" class="lbl" fill="#922b21" font-weight="bold">S_min</text>
</svg>

- **【分步标准解答】**
  1. **直線の方程式と交点の $x$ 座標**：
     点 $(1, 2)$ を通る直線が放物線 $y = x^2$ と図形を囲むためには、$y$ 軸に平行ではないから、傾きを $m$ として
     $$y - 2 = m(x - 1) \implies y = mx - m + 2$$
     と表せる。放物線 $y = x^2$ と連立すると、
     $$x^2 = mx - m + 2 \implies x^2 - mx + m - 2 = 0 \quad \cdots ①$$
     判別式を $D$ とすると、
     $$D = (-m)^2 - 4(m - 2) = m^2 - 4m + 8 = (m - 2)^2 + 4 > 0$$
     よって、すべての実数 $m$ に対して①は異なる $2$ つの実数解 $\alpha,\; \beta$（$\alpha < \beta$）をもつ。
     > 💡 讲师批注：由于点 $(1, 2)$ 严格在抛物线内部，任何非竖直线必与抛物线交于两点，因此判别式 $D = (m-2)^2 + 4$ 恒正。

  2. **面積 $S$ を $m$ で表して最小値を求める**：
     解の公式（または解と係数の関係 $\alpha + \beta = m,\; \alpha\beta = m - 2$）より、
     $$\beta - \alpha = \sqrt{(\alpha + \beta)^2 - 4\alpha\beta} = \sqrt{D} = \sqrt{(m - 2)^2 + 4}$$
     $\dfrac{1}{6}$ 公式より、
     $$S = \int_\alpha^\beta \{(mx - m + 2) - x^2\}\,dx = \frac{1}{6}(\beta - \alpha)^3 = \frac{1}{6}\left\{(m - 2)^2 + 4\right\}^{\frac{3}{2}}$$
     $(m - 2)^2 \ge 0$ であるから、$m = 2$ のとき $S$ は最小値
     $$S_{\min} = \frac{1}{6} \cdot 4^{\frac{3}{2}} = \frac{1}{6} \cdot 8 = \frac{4}{3}$$
     をとる。
     > 💡 讲师批注：**经典几何规律**：过抛物线内部定点 $P(x_0, y_0)$ 截抛物线所得面积最小，当且仅当该直线与**横坐标相同的抛物线切线平行**（即 $m = f'(x_0) = 2x_0 = 2$）！记住此结论可用于考场秒杀验算。
- **【最终答案】**
  **最小値 $\dfrac{4}{3}$（$m = 2$，即直线 $y = 2x$ 时取得）**

---

#### 演習問題 17-(18)
- **【原题重现与翻译】**
  - 原题：$y = \sin x \;(0 \le x \le \pi)$ で表された曲線を $C$ とする。
    - [1] 曲線 $C$ 上の点 $P(a, b)$ における接線 $l$ の方程式を求めよ。
    - [2] $0 < a < \pi$ とするとき、曲線 $C$ と接線 $l$ 及び直線 $x = \pi$ と $y$ 軸で囲まれる部分の面積 $S(a)$（$2$ 部分の和）を求めよ。
    - [3] 面積 $S(a)$ の最小値とそのときの $a$ の値を求めよ。
  - 中文：设由 $y = \sin x \;(0 \le x \le \pi)$ 表示的曲线为 $C$。
    - [1] 求曲线 $C$ 上点 $P(a, b)$ 处的切线 $l$ 的方程。
    - [2] 当 $0 < a < \pi$ 时，求由曲线 $C$、切线 $l$、直线 $x = \pi$ 与 $y$ 轴所围成部分的面积 $S(a)$（两部分之和）。
    - [3] 求面积 $S(a)$ 的最小值以及取得最小值时 $a$ 的值。
- **【考点定位】**
  - 三角函数切线方程 + 曲线凸性与面积积分 + 导数求最值（増減表）。
- **【图解辅助（SVG 矢量图）】**
  $y = \sin x$ 在 $[0, \pi]$ 上严格上凸，切线 $l$ 恒在曲线上方（仅在切点 $P$ 相切）：

<svg viewBox="0 0 420 210" width="420" height="210" xmlns="http://www.w3.org/2000/svg" style="background:#fafafa;border:1px solid #e0e0e0;border-radius:6px;">
  <style>
    .axis { stroke: #333; stroke-width: 1.4; }
    .curve { fill: none; stroke: #2471a3; stroke-width: 2.2; }
    .lin { stroke: #c0392b; stroke-width: 2; }
    .area { fill: #fdebd0; fill-opacity: 0.75; }
    .lbl { font: 12px sans-serif; fill: #2c3e50; }
    .math { font: italic 12px serif; fill: #2c3e50; }
  </style>
  <line x1="40" y1="175" x2="390" y2="175" class="axis"/>
  <polygon points="390,175 382,171 382,179" fill="#333"/>
  <line x1="70" y1="195" x2="70" y2="20" class="axis"/>
  <polygon points="70,20 66,28 74,28" fill="#333"/>
  <!-- x in [0, pi] -> [70, 350] (89.1px/unit), y in [0, 1] -> [175, 65] (110px/unit) -->
  <!-- Take a = pi/3 (1.047 -> px=163.3, y=0.866 -> py=79.7), slope = 0.5 -->
  <!-- Tangent at x=0: y = 0.866 - 0.5236 = 0.342 -> py=137.4; at x=pi: y = 0.342 + 1.571 = 1.913 -> clamped/scaled -->
  <!-- Use a = 1.25 (px=181, sin=0.949->py=70.6, cos=0.315): at x=0 y=0.555 (py=114), at x=pi y=1.545 (py=5) -> slightly adjust scale y: 80px/unit -->
  <!-- Let y scale = 80px/unit: y=0->175, y=1->95, y=1.545->51 -->
  <!-- Shaded area between tangent l and sin x from x=0 (70) to x=pi (350) -->
  <path d="M 70,131 L 350,51 L 350,175 C 305,120 260,95 210,95 C 160,95 115,120 70,175 Z" class="area"/>
  <!-- Sine curve -->
  <path d="M 70,175 C 115,120 160,95 210,95 C 260,95 305,120 350,175" class="curve"/>
  <!-- Vertical line x = pi -->
  <line x1="350" y1="30" x2="350" y2="175" stroke="#555" stroke-dasharray="4,3"/>
  <!-- Tangent line l -->
  <line x1="55" y1="135" x2="365" y2="47" class="lin"/>
  <!-- Tangent point P -->
  <line x1="181" y1="99" x2="181" y2="175" stroke="#7f8c8d" stroke-dasharray="3,3"/>
  <circle cx="181" cy="99" r="3.5" fill="#c0392b"/>
  <text x="385" y="191" class="math">x</text>
  <text x="78" y="28" class="math">y</text>
  <text x="56" y="190" class="lbl">O</text>
  <text x="177" y="190" class="math">a</text>
  <text x="346" y="190" class="lbl">π</text>
  <text x="355" y="42" class="math">x = π</text>
  <text x="165" y="88" class="math" fill="#c0392b">P(a, b)</text>
  <text x="278" y="60" class="math" fill="#c0392b">l</text>
  <text x="100" y="145" class="lbl" fill="#9c640c" font-weight="bold">S₁</text>
  <text x="295" y="110" class="lbl" fill="#9c640c" font-weight="bold">S₂</text>
</svg>

- **【分步标准解答】**
  - **[1] 接線 $l$ の方程式**：
    $y = \sin x$ より $y' = \cos x$。
    点 $P(a, b)$ は曲線 $C$ 上にあるから $b = \sin a$ である。
    よって、点 $P(a, \sin a)$ における接線 $l$ の方程式は、
    $$y - \sin a = \cos a \cdot (x - a)$$
    すなわち
    $$y = (\cos a) x - a\cos a + \sin a$$
    > 💡 讲师批注：把点斜式保留为 $y = (\cos a)(x - a) + \sin a$ 在下一步积分时会超级好算，最终答案写展开形式 $y = x\cos a - a\cos a + \sin a$ 更符合日本考场规范。

  - **[2] 面積 $S(a)$ の計算**：
    $0 \le x \le \pi$ において $y'' = -\sin x \le 0$ より、曲線 $C$ は上に凸である。
    したがって、接線 $l$ は常に曲線 $C$ の上側（接点 $P$ のみで共有）にあるから、
    $$S(a) = \int_0^\pi \left\{(\cos a)(x - a) + \sin a - \sin x\right\}\,dx$$
    $$= \left[\frac{1}{2}(\cos a)(x - a)^2 + (\sin a) x + \cos x\right]_0^\pi$$
    > 💡 讲师批注：直接把 $(x - a)$ 当作整体积分得 $\frac{1}{2}(x - a)^2$，比拆开 $x\cos a - a\cos a$ 分别积分简洁得多！

    $$= \left\{\frac{1}{2}(\cos a)(\pi - a)^2 + \pi\sin a + \cos\pi\right\} - \left\{\frac{1}{2}(\cos a)(-a)^2 + 0 + \cos 0\right\}$$
    $$= \frac{1}{2}(\cos a)\{(\pi - a)^2 - a^2\} + \pi\sin a - 2$$
    $$= \frac{1}{2}(\cos a)(\pi^2 - 2\pi a) + \pi\sin a - 2$$
    $$= \pi\left(\frac{\pi}{2} - a\right)\cos a + \pi\sin a - 2$$

  - **[3] $S(a)$ の最小値**：
    $S(a)$ を $a$ で微分すると、積の微分法より、
    $$S'(a) = \pi\left\{(-1)\cos a + \left(\frac{\pi}{2} - a\right)(-\sin a)\right\} + \pi\cos a$$
    $$= -\pi\cos a - \pi\left(\frac{\pi}{2} - a\right)\sin a + \pi\cos a = \pi\left(a - \frac{\pi}{2}\right)\sin a$$
    > 💡 讲师批注：$-\pi\cos a$ 与 $+\pi\cos a$ 完美抵消！这是判断 [2] 计算无误的最佳自检信号。

    $0 < a < \pi$ では $\sin a > 0$ であるから、$S'(a) = 0$ となるのは $a = \dfrac{\pi}{2}$ のみである。
    増減表は次のようになる：

    | $a$ | $0$ | $\cdots$ | $\dfrac{\pi}{2}$ | $\cdots$ | $\pi$ |
    | :---: | :---: | :---: | :---: | :---: | :---: |
    | $S'(a)$ | | $-$ | $0$ | $+$ | |
    | $S(a)$ | | $\searrow$ | 極小（$\pi - 2$） | $\nearrow$ | |

    よって、$S(a)$ は $a = \dfrac{\pi}{2}$ のとき最小値
    $$S\left(\frac{\pi}{2}\right) = \pi \cdot 0 \cdot 0 + \pi \cdot 1 - 2 = \pi - 2$$
    をとる。
- **【最终答案】**
  - **[1] $y = x\cos a - a\cos a + \sin a$**
  - **[2] $S(a) = \pi\left(\dfrac{\pi}{2} - a\right)\cos a + \pi\sin a - 2$**
  - **[3] $a = \dfrac{\pi}{2}$ のとき、最小値 $\pi - 2$**

---

#### 演習問題 17-(19)
- **【原题重现与翻译】**
  - 原题：曲線 $y = x^3 - 6x^2 + 9x$ と直線 $y = mx$ で囲まれた $2$ つの図形の面積が等しくなるような定数 $m$ を求めよ。ただし、$0 < m < 9$ とする。
  - 中文：求使得曲线 $y = x^3 - 6x^2 + 9x$ 与直线 $y = mx$ 所围成的两个图形面积相等的常数 $m$。其中 $0 < m < 9$。
- **【考点定位】**
  - 三次函数与直线的等积条件（$\int_0^\beta \{f(x) - g(x)\}\,dx = 0$）+ 拐点对称性验算。
- **【图解辅助（SVG 矢量图）】**

<svg viewBox="0 0 380 220" width="380" height="220" xmlns="http://www.w3.org/2000/svg" style="background:#fafafa;border:1px solid #e0e0e0;border-radius:6px;">
  <style>
    .axis { stroke: #333; stroke-width: 1.4; }
    .curve { fill: none; stroke: #2471a3; stroke-width: 2.2; }
    .lin { stroke: #c0392b; stroke-width: 2; }
    .a1 { fill: #d6eaf8; fill-opacity: 0.7; }
    .a2 { fill: #fadbd8; fill-opacity: 0.7; }
    .lbl { font: 12px sans-serif; fill: #2c3e50; }
    .math { font: italic 12px serif; fill: #2c3e50; }
  </style>
  <line x1="35" y1="185" x2="355" y2="185" class="axis"/>
  <polygon points="355,185 347,181 347,189" fill="#333"/>
  <line x1="70" y1="205" x2="70" y2="15" class="axis"/>
  <polygon points="70,15 66,23 74,23" fill="#333"/>
  <!-- x in [0, 4.5] -> [70, 340] (60px/unit), y in [0, 5] -> [185, 35] (30px/unit) -->
  <!-- y = x^3 - 6x^2 + 9x: (0,0)=(70,185), (1,4)=(130,65), (2,2)=(190,125), (3,0)=(250,185), (4,4)=(310,65) -->
  <!-- Line y = x (m=1): (0,0)->(70,185), (2,2)->(190,125), (4,4)->(310,65) -->
  <path d="M 70,185 C 100,95 115,65 130,65 C 150,65 170,100 190,125 L 70,185 Z" class="a1"/>
  <path d="M 190,125 C 210,150 230,185 250,185 C 275,185 295,120 310,65 L 190,125 Z" class="a2"/>
  <path d="M 70,185 C 100,95 115,65 130,65 C 150,65 170,100 190,125 C 210,150 230,185 250,185 C 275,185 295,120 315,40" class="curve"/>
  <line x1="55" y1="192.5" x2="335" y2="52.5" class="lin"/>
  <circle cx="190" cy="125" r="4" fill="#c0392b"/>
  <circle cx="310" cy="65" r="3.5" fill="#c0392b"/>
  <text x="350" y="201" class="math">x</text>
  <text x="78" y="25" class="math">y</text>
  <text x="56" y="200" class="lbl">O</text>
  <text x="184" y="201" class="math">α (=2)</text>
  <text x="303" y="201" class="math">β (=4)</text>
  <text x="198" y="135" class="lbl" fill="#c0392b">変曲点 (2, 2)</text>
  <text x="118" y="118" class="lbl" fill="#1b4f72" font-weight="bold">S₁</text>
  <text x="242" y="145" class="lbl" fill="#922b21" font-weight="bold">S₂</text>
  <text x="320" y="48" class="math" fill="#c0392b">y = mx</text>
</svg>

- **【分步标准解答】**
  1. **交点の $x$ 座標の確認**：
     $x^3 - 6x^2 + 9x = mx$ より、
     $$x\{x^2 - 6x + (9 - m)\} = 0$$
     二次方程式 $x^2 - 6x + (9 - m) = 0$ の判別式を $D$ とすると、
     $$\frac{D}{4} = (-3)^2 - (9 - m) = m$$
     条件 $0 < m < 9$ より $D > 0$、さらに $2$ 解の和 $= 6 > 0$、積 $= 9 - m > 0$ であるから、$2$ つの正の異なる実数解 $\alpha,\; \beta$（$0 < \alpha < \beta$）をもつ。
     具体的には $\alpha = 3 - \sqrt{m},\; \beta = 3 + \sqrt{m}$ である。

  2. **面積が等しい条件（定積分の相殺）**：
     区間 $[0, \alpha]$ では曲線が直線の上側、区間 $[\alpha, \beta]$ では直線が曲線の上側にあるから、$2$ つの図形の面積が等しいための必要十分条件は、
     $$\int_0^\beta \{(x^3 - 6x^2 + 9x) - mx\}\,dx = 0$$
     > 💡 讲师批注：千万不要把两块面积分别求出来再令它们相等（含根号 $\sqrt{m}$ 会算到崩溃）！直接用「总定积分为 $0$」把中间交点 $\alpha$ 完美消掉！

     左辺を計算すると、
     $$\int_0^\beta \{x^3 - 6x^2 + (9 - m)x\}\,dx = \left[\frac{1}{4}x^4 - 2x^3 + \frac{9 - m}{2}x^2\right]_0^\beta = \frac{\beta^2}{4}\left\{\beta^2 - 8\beta + 2(9 - m)\right\} = 0$$
     $\beta > 0$ より、
     $$\beta^2 - 8\beta + 2(9 - m) = 0 \quad \cdots ①$$

  3. **交点の関係式を用いて $\beta$ と $m$ を決定する**：
     $\beta$ は $x^2 - 6x + (9 - m) = 0$ の解であるから、$9 - m = 6\beta - \beta^2$。
     これを①に代入すると、
     $$\beta^2 - 8\beta + 2(6\beta - \beta^2) = 0 \implies -\beta^2 + 4\beta = 0 \implies \beta(\beta - 4) = 0$$
     $\beta > 0$ より $\beta = 4$。
     よって、$9 - m = 6 \cdot 4 - 4^2 = 24 - 16 = 8$ より、
     $$m = 1$$
     これは $0 < m < 9$ を満たす。
     > 💡 讲师批注：**拐点秒杀验算**：$f(x) = x^3 - 6x^2 + 9x$ 的拐点由 $f''(x) = 6x - 12 = 0 \implies x = 2$ 给出，拐点为 $(2, 2)$。直线 $y = mx$ 过拐点 $(2, 2)$ 时 $2 = 2m \implies m = 1$！1 秒验算完毕！
- **【最终答案】**
  **$m = 1$**

---

#### 演習問題 17-(20)
- **【原题重现与翻译】**
  - 原题：曲線 $y = x^4 + 2x^3 - 3x^2$ を $C$、直線 $y = 4x - 4$ を $l$ とする。
    - [1] 曲線 $C$ と直線 $l$ は異なる $2$ 点で接することを示せ。
    - [2] 曲線 $C$ と直線 $l$ で囲まれた図形の面積を求めよ。
  - 中文：设曲线 $y = x^4 + 2x^3 - 3x^2$ 为 $C$，直线 $y = 4x - 4$ 为 $l$。
    - [1] 证明曲线 $C$ 与直线 $l$ 在不同的两点处相切。
    - [2] 求曲线 $C$ 与直线 $l$ 所围成图形的面积。
- **【考点定位】**
  - 四次函数与二重切线（複接線）的判定 + $\frac{1}{30}$ 面积公式（平移换元推导）。
- **【图解辅助（SVG 矢量图）】**

<svg viewBox="0 0 380 220" width="380" height="220" xmlns="http://www.w3.org/2000/svg" style="background:#fafafa;border:1px solid #e0e0e0;border-radius:6px;">
  <style>
    .axis { stroke: #333; stroke-width: 1.4; }
    .curve { fill: none; stroke: #2471a3; stroke-width: 2.2; }
    .lin { stroke: #c0392b; stroke-width: 2; }
    .area { fill: #d6eaf8; fill-opacity: 0.7; }
    .lbl { font: 12px sans-serif; fill: #2c3e50; }
    .math { font: italic 12px serif; fill: #2c3e50; }
  </style>
  <line x1="30" y1="75" x2="355" y2="75" class="axis"/>
  <polygon points="355,75 347,71 347,79" fill="#333"/>
  <line x1="210" y1="210" x2="210" y2="15" class="axis"/>
  <polygon points="210,15 206,23 214,23" fill="#333"/>
  <!-- Origin (210, 75), x scale: 55px/unit, y scale: 9px/unit -->
  <!-- Key points on C: (-2, -12)=(100, 183), (0,0)=(210,75), (1,0)=(265,75), (-0.5, -0.94)=(182.5, 83.5) -->
  <!-- Tangent l: y = 4x - 4 passes (-2, -12)=(100,183) and (1, 0)=(265,75) -->
  <path d="M 100,183 C 145,155 180,75 210,75 C 235,75 245,95 265,75 L 100,183 Z" class="area"/>
  <!-- Full W-shaped quartic C -->
  <path d="M 65,40 C 78,135 88,188 100,183 C 145,155 180,75 210,75 C 235,75 245,95 265,75 C 282,58 292,35 300,18" class="curve"/>
  <!-- Double tangent line l -->
  <line x1="65" y1="206" x2="315" y2="42" class="lin"/>
  <circle cx="100" cy="183" r="3.5" fill="#c0392b"/>
  <circle cx="265" cy="75" r="3.5" fill="#c0392b"/>
  <text x="348" y="90" class="math">x</text>
  <text x="218" y="25" class="math">y</text>
  <text x="196" y="90" class="lbl">O</text>
  <text x="262" y="92" class="lbl">1</text>
  <text x="90" y="200" class="lbl" fill="#c0392b">(-2, -12)</text>
  <text x="268" y="64" class="lbl" fill="#c0392b">(1, 0)</text>
  <text x="180" y="112" class="lbl" fill="#1b4f72" font-weight="bold">S = 81/10</text>
  <text x="295" y="42" class="math" fill="#c0392b">l: y = 4x-4</text>
</svg>

- **【分步标准解答】**
  - **[1] 異なる $2$ 点で接することの証明**：
    $f(x) = x^4 + 2x^3 - 3x^2$、$g(x) = 4x - 4$ とおく。
    連立方程式 $f(x) - g(x) = 0$ を整理すると、
    $$x^4 + 2x^3 - 3x^2 - 4x + 4 = 0$$
    左辺を因数分解する。$x = 1$ を代入すると $1 + 2 - 3 - 4 + 4 = 0$、$x = -2$ を代入すると $16 - 16 - 12 + 8 + 4 = 0$ であるから、組立除法（または係数比較）により、
    $$x^4 + 2x^3 - 3x^2 - 4x + 4 = (x - 1)^2(x + 2)^2$$
    > 💡 讲师批注：展开验算 $(x-1)^2(x+2)^2 = (x^2 - 2x + 1)(x^2 + 4x + 4) = x^4 + 2x^3 - 3x^2 - 4x + 4$，完全一致！

    したがって、$f(x) - g(x) = (x - 1)^2(x + 2)^2$ は $x = -2$ および $x = 1$ をそれぞれ重解にもつ。
    （確認：$f'(x) = 4x^3 + 6x^2 - 6x$ より $f'(-2) = -32 + 24 + 12 = 4$、$f'(1) = 4 + 6 - 6 = 4$ であり、接点の座標も $f(-2) = -12 = g(-2)$、$f(1) = 0 = g(1)$ で一致する。）
    よって、曲線 $C$ と直線 $l$ は異なる $2$ 点 $(-2, -12)$、$(1, 0)$ において接する。 $\blacksquare$

  - **[2] 囲まれた図形の面積 $S$**：
    すべての実数 $x$ に対して $f(x) - g(x) = (x - 1)^2(x + 2)^2 \ge 0$ であるから、区間 $[-2, 1]$ で曲線 $C$ は直線 $l$ の上側にある。
    よって、
    $$S = \int_{-2}^1 (x - 1)^2(x + 2)^2\,dx$$
    ここで $t = x + 2$ とおくと、$x - 1 = t - 3$、$dx = dt$、$x : -2 \to 1$ のとき $t : 0 \to 3$ であるから、
    $$S = \int_0^3 (t - 3)^2 t^2\,dt = \int_0^3 (t^4 - 6t^3 + 9t^2)\,dt$$
    > 💡 讲师批注：用平移换元 $t = x + 2$ 把积分下限变成 $0$，代入上下限时下限全为 $0$，计算量直降一半！

    $$= \left[\frac{1}{5}t^5 - \frac{3}{2}t^4 + 3t^3\right]_0^3 = \frac{243}{5} - \frac{243}{2} + 81$$
    $$= \frac{486 - 1215 + 810}{10} = \frac{81}{10}$$
    > 💡 讲师批注：**$\frac{1}{30}$ 公式速算验算**：$S = \dfrac{1}{30}\{1 - (-2)\}^5 = \dfrac{3^5}{30} = \dfrac{243}{30} = \dfrac{81}{10}$，分毫不差！
- **【最终答案】**
  - **[1] 証明完了（接点は $(-2, -12)$ と $(1, 0)$）**
  - **[2] $\dfrac{81}{10}$**

---

#### 演習問題 17-(21)
- **【原题重现与翻译】**
  - 原题：$f(t) = \displaystyle\int_0^1 |x^2 - tx|\,dx$ とする。$f(t)$ の最小値と、最小値を与える $t$ の値を求めよ。
  - 中文：设 $f(t) = \displaystyle\int_0^1 |x^2 - tx|\,dx$。求 $f(t)$ 的最小值以及使它取得最小值的 $t$ 的值。
- **【考点定位】**
  - 含参数绝对值的定积分分类讨论（場合分け）+ 分段函数的单调性与最小值。
- **【图解辅助（SVG 矢量图）】**
  当 $0 < t < 1$ 时，$x = t$ 将积分区间 $[0, 1]$ 分为两段：左侧 $tx \ge x^2$，右侧 $x^2 \ge tx$：

<svg viewBox="0 0 420 200" width="420" height="200" xmlns="http://www.w3.org/2000/svg" style="background:#fafafa;border:1px solid #e0e0e0;border-radius:6px;">
  <style>
    .axis { stroke: #333; stroke-width: 1.4; }
    .par { fill: none; stroke: #2471a3; stroke-width: 2.2; }
    .lin { stroke: #c0392b; stroke-width: 2; }
    .a1 { fill: #fadbd8; fill-opacity: 0.7; }
    .a2 { fill: #d6eaf8; fill-opacity: 0.7; }
    .lbl { font: 12px sans-serif; fill: #2c3e50; }
    .math { font: italic 12px serif; fill: #2c3e50; }
  </style>
  <!-- Left: Graph of y=x^2 and y=tx -->
  <line x1="25" y1="165" x2="220" y2="165" class="axis"/>
  <polygon points="220,165 212,161 212,169" fill="#333"/>
  <line x1="45" y1="185" x2="45" y2="20" class="axis"/>
  <polygon points="45,20 41,28 49,28" fill="#333"/>
  <!-- x in [0,1] -> [45, 185] (140px), y in [0,1] -> [165, 35] (130px) -->
  <!-- t = 0.707 -> px = 144, y = 0.5 -> py = 100 -->
  <path d="M 45,165 Q 94.5,165 144,100 L 45,165 Z" class="a1"/>
  <path d="M 144,100 Q 164.5,73 185,35 L 185,73 L 144,100 Z" class="a2"/>
  <path d="M 45,165 Q 115,165 185,35" class="par"/>
  <line x1="45" y1="165" x2="205" y2="60" class="lin"/>
  <line x1="144" y1="100" x2="144" y2="165" stroke="#7f8c8d" stroke-dasharray="3,3"/>
  <line x1="185" y1="35" x2="185" y2="165" stroke="#555" stroke-dasharray="3,3"/>
  <text x="215" y="180" class="math">x</text>
  <text x="52" y="28" class="math">y</text>
  <text x="34" y="180" class="lbl">O</text>
  <text x="140" y="180" class="math">t</text>
  <text x="181" y="180" class="lbl">1</text>
  <text x="148" y="34" class="math" fill="#2471a3">y = x²</text>
  <text x="188" y="55" class="math" fill="#c0392b">y = tx</text>
  <!-- Right: Number line for 3 cases of t -->
  <text x="245" y="45" class="lbl" font-weight="bold">場合分け（t の位置）</text>
  <line x1="245" y1="95" x2="405" y2="95" class="axis"/>
  <polygon points="405,95 397,91 397,99" fill="#333"/>
  <circle cx="290" cy="95" r="3.5" fill="#2c3e50"/>
  <circle cx="355" cy="95" r="3.5" fill="#2c3e50"/>
  <text x="286" y="114" class="lbl">0</text>
  <text x="351" y="114" class="lbl">1</text>
  <text x="402" y="112" class="math">t</text>
  <text x="248" y="82" class="lbl" fill="#2471a3">(i) t≤0</text>
  <text x="300" y="82" class="lbl" fill="#c0392b">(ii) 0&lt;t&lt;1</text>
  <text x="364" y="82" class="lbl" fill="#1e8449">(iii) t≥1</text>
  <text x="248" y="140" class="lbl">・(i) 単調減少</text>
  <text x="248" y="158" class="lbl" fill="#c0392b" font-weight="bold">・(ii) t=√2/2 で最小</text>
  <text x="248" y="176" class="lbl">・(iii) 単調増加</text>
</svg>

- **【分步标准解答】**
  被積分関数 $|x^2 - tx| = x|x - t|$（$0 \le x \le 1$ なので $x \ge 0$）の絶対値を外すため、$t$ の値によって $3$ つに場合分けする。

  1. **(i) $t \le 0$ のとき**：
     $0 \le x \le 1$ で常に $x - t \ge 0$ より $|x^2 - tx| = x^2 - tx$。
     $$f(t) = \int_0^1 (x^2 - tx)\,dx = \left[\frac{1}{3}x^3 - \frac{t}{2}x^2\right]_0^1 = -\frac{1}{2}t + \frac{1}{3}$$
     これは $t \le 0$ で単調に減少する（$f(0) = \dfrac{1}{3}$）。

  2. **(ii) $0 < t < 1$ のとき**：
     $0 \le x \le t$ では $x^2 - tx \le 0$、$t \le x \le 1$ では $x^2 - tx \ge 0$ であるから、
     $$f(t) = \int_0^t (tx - x^2)\,dx + \int_t^1 (x^2 - tx)\,dx$$
     $$= \left[\frac{t}{2}x^2 - \frac{1}{3}x^3\right]_0^t + \left[\frac{1}{3}x^3 - \frac{t}{2}x^2\right]_t^1$$
     $$= \left(\frac{1}{2}t^3 - \frac{1}{3}t^3\right) + \left(\frac{1}{3} - \frac{1}{2}t\right) - \left(\frac{1}{3}t^3 - \frac{1}{2}t^3\right)$$
     $$= \frac{1}{3}t^3 - \frac{1}{2}t + \frac{1}{3}$$
     > 💡 讲师批注：自检技巧——将 $t = 0$ 代入得 $\frac{1}{3}$（与 (i) 连续），将 $t = 1$ 代入得 $\frac{1}{3} - \frac{1}{2} + \frac{1}{3} = \frac{1}{6}$（与 (iii) 连续）！边界连续性检验能 100% 防错。

     $f'(t) = t^2 - \dfrac{1}{2}$ より、$0 < t < 1$ で $f'(t) = 0$ となるのは $t = \dfrac{1}{\sqrt{2}} = \dfrac{\sqrt{2}}{2}$。
     - $0 < t < \dfrac{\sqrt{2}}{2}$ のとき $f'(t) < 0$（減少）
     - $\dfrac{\sqrt{2}}{2} < t < 1$ のとき $f'(t) > 0$（増加）

  3. **(iii) $t \ge 1$ のとき**：
     $0 \le x \le 1$ で常に $x - t \le 0$ より $|x^2 - tx| = tx - x^2$。
     $$f(t) = \int_0^1 (tx - x^2)\,dx = \frac{1}{2}t - \frac{1}{3}$$
     これは $t \ge 1$ で単調に増加する（$f(1) = \dfrac{1}{6}$）。

  4. **全体での最小値の決定**：
     $f(t)$ はすべての実数 $t$ で連続であり、(i)〜(iii) を合わせると、$t \le \dfrac{\sqrt{2}}{2}$ で単調減少、$t \ge \dfrac{\sqrt{2}}{2}$ で単調増加する。
     よって、$t = \dfrac{\sqrt{2}}{2}$ のとき最小値
     $$f\left(\frac{\sqrt{2}}{2}\right) = \frac{1}{3}\left(\frac{\sqrt{2}}{2}\right)^3 - \frac{1}{2}\left(\frac{\sqrt{2}}{2}\right) + \frac{1}{3} = \frac{\sqrt{2}}{12} - \frac{\sqrt{2}}{4} + \frac{1}{3} = \frac{2 - \sqrt{2}}{6}$$
     をとる。
- **【最终答案】**
  **$t = \dfrac{\sqrt{2}}{2}$ のとき、最小値 $\dfrac{2 - \sqrt{2}}{6}$**

---

#### 演習問題 17-(22)
- **【原题重现与翻译】**
  - 原题：曲線 $x = -y^2 + 2y - 2,\; y$ 軸，$2$ 直線 $y = 1,\; y = 2$ で囲まれた図形の面積 $S$ を求めよ。
  - 中文：求由曲线 $x = -y^2 + 2y - 2$、$y$ 轴以及两条直线 $y = 1,\; y = 2$ 所围成图形的面积 $S$。
- **【考点定位】**
  - 以 $y$ 为积分变量的定积分面积计算（$y$ 軸方向への積分）。
- **【图解辅助（SVG 矢量图）】**

<svg viewBox="0 0 360 210" width="360" height="210" xmlns="http://www.w3.org/2000/svg" style="background:#fafafa;border:1px solid #e0e0e0;border-radius:6px;">
  <style>
    .axis { stroke: #333; stroke-width: 1.4; }
    .curve { fill: none; stroke: #2471a3; stroke-width: 2.2; }
    .area { fill: #d6eaf8; fill-opacity: 0.75; }
    .lbl { font: 12px sans-serif; fill: #2c3e50; }
    .math { font: italic 12px serif; fill: #2c3e50; }
  </style>
  <line x1="30" y1="175" x2="330" y2="175" class="axis"/>
  <polygon points="330,175 322,171 322,179" fill="#333"/>
  <line x1="270" y1="195" x2="270" y2="15" class="axis"/>
  <polygon points="270,15 266,23 274,23" fill="#333"/>
  <!-- Origin (270, 175), x scale: 65px/unit, y scale: 60px/unit -->
  <!-- x = -(y-1)^2 - 1: vertex (-1, 1) -> (205, 115); at y=2: (-2, 2) -> (140, 55); at y=0: (-2, 0) -> (140, 175) -->
  <!-- Shaded area between x = -y^2+2y-2 and x = 0 from y=1 (115) to y=2 (55) -->
  <path d="M 270,115 L 205,115 Q 205,85 140,55 L 270,55 Z" class="area"/>
  <!-- Full parabola -->
  <path d="M 105,195 Q 305,115 105,35" class="curve"/>
  <line x1="120" y1="115" x2="295" y2="115" stroke="#c0392b" stroke-dasharray="4,3"/>
  <line x1="120" y1="55" x2="295" y2="55" stroke="#c0392b" stroke-dasharray="4,3"/>
  <circle cx="205" cy="115" r="3.5" fill="#2471a3"/>
  <text x="322" y="191" class="math">x</text>
  <text x="278" y="25" class="math">y</text>
  <text x="276" y="191" class="lbl">O</text>
  <text x="276" y="112" class="lbl" fill="#c0392b">y = 1</text>
  <text x="276" y="52" class="lbl" fill="#c0392b">y = 2</text>
  <text x="155" y="132" class="lbl">頂点 (-1, 1)</text>
  <text x="220" y="88" class="lbl" fill="#1b4f72" font-weight="bold">S = 4/3</text>
  <text x="32" y="38" class="math" fill="#2471a3">x = -y² + 2y - 2</text>
</svg>

- **【分步标准解答】**
  1. **曲線と $y$ 軸の位置関係（左右の判定）**：
     平方完成すると、
     $$x = -(y - 1)^2 - 1$$
     よって、すべての実数 $y$ に対して $x \le -1 < 0$ であり、この曲線は常に $y$ 軸（$x = 0$）の左側にある。
     > 💡 讲师批注：对 $y$ 积分求面积的口诀是「**右减左**」（$x_{\text{右}} - x_{\text{左}}$）！此处 $y$ 轴（$x = 0$）在右，抛物线在左，故被积函数是 $0 - (-y^2 + 2y - 2)$，切勿漏掉负号导致面积为负。

  2. **$y$ についての定積分**：
     $$S = \int_1^2 \{0 - (-y^2 + 2y - 2)\}\,dy = \int_1^2 (y^2 - 2y + 2)\,dy$$
     $$= \left[\frac{1}{3}y^3 - y^2 + 2y\right]_1^2 = \left(\frac{8}{3} - 4 + 4\right) - \left(\frac{1}{3} - 1 + 2\right) = \frac{8}{3} - \frac{4}{3} = \frac{4}{3}$$
- **【最终答案】**
  **$S = \dfrac{4}{3}$**

---

#### 演習問題 17-(23)
- **【原题重现与翻译】**
  - 原题：曲線 $x = y^2 - 3y$ と直線 $y = x$ で囲まれた図形の面積 $S$ を求めよ。
  - 中文：求由曲线 $x = y^2 - 3y$ 与直线 $y = x$ 所围成图形的面积 $S$。
- **【考点定位】**
  - 以 $y$ 为积分变量求面积 + $\frac{1}{6}$ 面积公式。
- **【图解辅助（SVG 矢量图）】**

<svg viewBox="0 0 360 220" width="360" height="220" xmlns="http://www.w3.org/2000/svg" style="background:#fafafa;border:1px solid #e0e0e0;border-radius:6px;">
  <style>
    .axis { stroke: #333; stroke-width: 1.4; }
    .curve { fill: none; stroke: #2471a3; stroke-width: 2.2; }
    .lin { stroke: #c0392b; stroke-width: 2; }
    .area { fill: #d5f5e3; fill-opacity: 0.7; }
    .lbl { font: 12px sans-serif; fill: #2c3e50; }
    .math { font: italic 12px serif; fill: #2c3e50; }
  </style>
  <line x1="30" y1="175" x2="335" y2="175" class="axis"/>
  <polygon points="335,175 327,171 327,179" fill="#333"/>
  <line x1="145" y1="205" x2="145" y2="15" class="axis"/>
  <polygon points="145,15 141,23 149,23" fill="#333"/>
  <!-- Origin (145, 175), scale x: 35px/unit, y: 35px/unit -->
  <!-- x = y^2 - 3y: (0,0)=(145,175), vertex (-2.25, 1.5)=(66.25, 122.5), (0,3)=(145,70), (4,4)=(285,35) -->
  <!-- Line x = y: (0,0)=(145,175) to (4,4)=(285,35) -->
  <path d="M 145,175 Q 25,105 285,35 L 145,175 Z" class="area"/>
  <path d="M 205,195 Q -15,122.5 310,20" class="curve"/>
  <line x1="115" y1="205" x2="310" y2="10" class="lin"/>
  <circle cx="145" cy="175" r="3.5" fill="#c0392b"/>
  <circle cx="285" cy="35" r="3.5" fill="#c0392b"/>
  <text x="328" y="191" class="math">x</text>
  <text x="153" y="25" class="math">y</text>
  <text x="128" y="191" class="lbl">O</text>
  <text x="292" y="38" class="lbl" fill="#c0392b">(4, 4)</text>
  <text x="148" y="110" class="lbl" fill="#196f3d" font-weight="bold">S = 32/3</text>
  <text x="200" y="160" class="math" fill="#2471a3">x = y² - 3y</text>
  <text x="242" y="95" class="math" fill="#c0392b">x = y</text>
</svg>

- **【分步标准解答】**
  1. **交点の $y$ 座標を求める**：
     $x = y^2 - 3y$ と $x = y$ を連立すると、
     $$y^2 - 3y = y \implies y^2 - 4y = 0 \implies y(y - 4) = 0 \implies y = 0,\; 4$$
     （交点は $(0, 0)$ と $(4, 4)$ である。）

  2. **$y$ についての定積分で面積を計算する**：
     $0 \le y \le 4$ において、$y - (y^2 - 3y) = -y(y - 4) \ge 0$ より、直線 $x = y$ が曲線 $x = y^2 - 3y$ の右側にある。
     よって、$\dfrac{1}{6}$ 公式を用いると、
     $$S = \int_0^4 \{y - (y^2 - 3y)\}\,dy = -\int_0^4 y(y - 4)\,dy = \frac{1}{6}(4 - 0)^3 = \frac{64}{6} = \frac{32}{3}$$
     > 💡 讲师批注：把 $y$ 当作自变量，不仅无需解二次方程去拆成上下两支根式，还能直接套用 $\frac{1}{6}$ 公式 2 行出答案！
- **【最终答案】**
  **$S = \dfrac{32}{3}$**
