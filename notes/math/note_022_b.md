# 《EJU 教材全解与备课讲义》数学 022-B（P325–P330）

> **对应源文件**：`work_math/ocr_md/ocr_022_p316-330.md`（后半部分 P325–P330：接線と法線、演習問題 9、関数の増減と値の変化）
> **视觉核对参考图**：`work_math/ref_imgs/page_0325.jpg` – `page_0330.jpg`
> **前篇说明**：本切片前半部分（P316–P324，共 37 小题）见 `note_022_a.md`；本篇覆盖 P325–P330 全部知识点与演習問題 9 共 11 道核心大题。

---

## 一、国内高中基础知识点唤醒与 EJU 考纲差异对比

本部分对应日本高中 **数学Ⅱ・数学Ⅲ（微分の応用：接線と法線、関数の増減・極値）** 的核心内容，是 EJU 理系数学压轴题的绝对高频考点。

### 1.1 切线与法线方程（接線と法線，P325）

设曲线 $y = f(x)$ 在点 $A(a, f(a))$ 处可微：
1. **切线方程（接線の方程式）**：
   $$y - f(a) = f'(a)(x - a)$$
2. **法线方程（法線の方程式）**（过切点 $A$ 且与切线垂直的直线）：
   - 当 $f'(a) \neq 0$ 时：
     $$y - f(a) = -\frac{1}{f'(a)}(x - a)$$
   - 当 $f'(a) = 0$ 时，切线水平，法线为竖直线 $x = a$。
3. **隐函数与参数曲线的切线**：
   - 曲线由 $F(x, y) = 0$ 或参数方程 $x = f(t),\; y = g(t)$ 给出时，过曲线上一点 $(x_1, y_1)$ 的切线方程为 $y - y_1 = m(x - x_1)$，其中 $m$ 为 $\dfrac{dy}{dx}$ 在该点处的值。
   > ⚠️ **教材勘误提示**：原教材 P325（`page_0325.jpg`）[10.2] 中将参数方程误印为「$t$ を媒介変数として $x = f(x),\; y = g(x)$」，应修正为 **$x = f(t),\; y = g(t)$**。

**EJU 切线题五大必考题型口诀**：
- **「在」点求切线**：直接代入切点 $(a, f(a))$ 与斜率 $f'(a)$。
- **「过」点引切线（点在曲线外或未知）**：**必须先设切点坐标 $(t, f(t))$**，写出切线方程后再代入已知点坐标解 $t$！
- **两曲线公切线（共通接線）**：
  - *同点相切（2曲線が接する）*：$f(t) = g(t)$ 且 $f'(t) = g'(t)$；
  - *异点公切线（共通接線）*：分别设切点 $s, t$，写出两条切线后令斜率与截距分别相等（或写出一条切线后与另一二次曲线联立令判别式 $D = 0$）。
- **四次函数的二重切线（複接線）**：设切线 $y = mx + n$，直接利用恒等式 $f(x) - (mx + n) = (x - \alpha)^2(x - \beta)^2$ 比较系数秒杀！
- **切线条数问题（接線の本数）**：转化为关于切点横坐标 $t$ 的方程的**不同实数解个数**（注意：三次曲线的切点与切线是一一对应的！）。

### 1.2 函数的增减、极值与最值（関数の増減と値の変化，P330）

设函数 $f(x)$ 在闭区间 $[a, b]$ 上连续，在开区间 $(a, b)$ 上可微：
1. **单调性判定（関数の増加と減少）**：
   - 在 $(a, b)$ 内恒有 $f'(x) > 0 \implies f(x)$ 在 $[a, b]$ 上**单调递增（単調に増加）**；
   - 在 $(a, b)$ 内恒有 $f'(x) < 0 \implies f(x)$ 在 $[a, b]$ 上**单调递减（単調に減少）**；
   - 在 $(a, b)$ 内恒有 $f'(x) = 0 \implies f(x)$ 在 $[a, b]$ 上为常数。
2. **极值判定（極大・極小）**：
   - 必要条件：若 $f(x)$ 在 $x = a$ 可微且取极值，则必有 $f'(a) = 0$（**逆命题不成立！** 如 $f(x) = x^3$ 在 $x = 0$ 处 $f'(0) = 0$ 但无极值）。
   - 充分条件（符号变号判定）：
     - $f'(x)$ 在 $x = a$ 前后由 **$+$ 变为 $-$** $\implies f(a)$ 为**极大值（極大値）**；
     - $f'(x)$ 在 $x = a$ 前后由 **$-$ 变为 $+$** $\implies f(a)$ 为**极小值（極小値）**。
3. **增减表（増減表）**：日本高中解题标准规范必须画 3 行表格（$x$、$f'(x)$、$f(x)$），用斜箭头 $\nearrow$、$\searrow$ 标示增减。
4. **闭区间最值（最大と最小）**：比较区间内所有**极值**与区间**两端点值 $f(a), f(b)$**，最大者为最大值，最小者为最小值。

### 1.3 国内高中 vs. 日本 EJU 考纲差异对比

| 对比维度 | 国内高中习惯 | 日本 EJU 习惯 | 备课/应试提醒 |
| :--- | :--- | :--- | :--- |
| **法线方程** | 高考几乎不提「法线」 | **数学Ⅲ常规考点**，常与切线围成三角形面积结合考 | 牢记法线斜率 $= -\dfrac{1}{f'(a)}$，注意单独检查 $f'(a) = 0$ 的竖直法线 |
| **「在某点」vs「过某点」** | 「在点 $P$ 处的切线」vs「过点 $P$ 的切线」 | **点 $P$ における接線**（$P$ 为切点）vs **点 $P$ から引いた接線 / 点 $P$ を通る接線**（$P$ 不一定是切点！） | 读题死盯助词：**における** 直接代，**から引いた / を通る** 必须先设切点 $t$！ |
| **增减表画法** | 常用表格写「递增 / 递减」 | 必须用斜箭头 **$\nearrow$（増加）**、**$\searrow$（減少）** | 熟悉日本教科书标准增减表格式，快速定位极值与图像草图 |

---

## 二、日文核心词汇与公式假名注音

### 2.1 本部分新增日文核心词汇（P325–P330）

- 単調に増加する（たんちょうにぞうかする / tanchou ni zouka suru） — 单调递增
- 単調に減少する（たんちょうにげんしょうする / tanchou ni genshou suru） — 单调递减
- 極大（きょくだい / kyokudai） — 极大
- 極小（きょくしょう / kyokushou） — 极小
- 極大値（きょくだいち / kyokudaichi） — 极大值
- 極小値（きょくしょうち / kyokushouchi） — 极小值
- 極値（きょくち / kyokuchi） — 极值（极大值与极小值的统称）
- 増減表（ぞうげんひょう / zougenhyou） — 增减表
- 変曲点（へんきょくてん / henkyokuten） — 拐点

### 2.2 核心公式的日本课堂口语读法

1. **切线方程** $y - f(a) = f'(a)(x - a)$
   - 课堂读法：**ワイ ひく エフ エー イコール エフダッシュ エー、かっこ エックス ひく エー かっことじ**
2. **法线方程** $y - f(a) = -\dfrac{1}{f'(a)}(x - a)$
   - 课堂读法：**ワイ ひく エフ エー イコール マイナス エフダッシュ エー ぶんの いち、かっこ エックス ひく エー かっことじ**
3. **增减判定** $f'(x) > 0 \implies$ 単調に増加
   - 课堂读法：**エフダッシュ エックス だなり ゼロ ならば、エフ エックス は たんちょうに ぞうかする**

---

## 三、逐题深度解析（不可跳步）

---

### 演習問題 9（接線と法線）

#### 演習問題 9-(1)
- **【原题重现与翻译】**
  - 原题：曲線 $y = \dfrac{3}{x}$ 上の点 $(1, 3)$ における接線の方程式を求めよ。
  - 中文：求曲线 $y = \dfrac{3}{x}$ 上的点 $(1, 3)$ 处的切线方程。
- **【考点定位】**
  - 已知切点（「における」）求切线方程。
- **【分步标准解答】**
  $y = 3x^{-1}$ を $x$ で微分すると、
  $$y' = -3x^{-2} = -\frac{3}{x^2}$$
  点 $(1, 3)$ における接線の傾きは、$x = 1$ を代入して、
  $$y'\big|_{x=1} = -\frac{3}{1^2} = -3$$
  よって、求める接線の方程式は、
  $$y - 3 = -3(x - 1)$$
  $$y = -3x + 6$$
  > 💡 讲师批注：验算——联立 $\dfrac{3}{x} = -3x + 6 \Rightarrow 3x^2 - 6x + 3 = 3(x - 1)^2 = 0$，恰在 $x = 1$ 处有重根，验证无误！
- **【最终答案】**
  **$y = -3x + 6$**

---

#### 演習問題 9-(2)
- **【原题重现与翻译】**
  - 原题：曲線 $y = \sqrt{25 - x^2}$ に接し、傾きが $-\dfrac{3}{4}$ である直線の方程式を求めよ。
  - 中文：求与曲线 $y = \sqrt{25 - x^2}$ 相切且斜率为 $-\dfrac{3}{4}$ 的直线方程。
- **【考点定位】**
  - 已知斜率求切线方程、半圆曲线的符号限定（防增根！）。
- **【图解辅助（SVG 矢量图）】**

<svg viewBox="0 0 380 210" width="380" height="210" xmlns="http://www.w3.org/2000/svg" style="background:#fafbfc;border:1px solid #e1e4e8;border-radius:6px;">
  <defs>
    <marker id="arr92" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#333"/>
    </marker>
  </defs>
  <!-- 坐标轴 -->
  <line x1="30" y1="175" x2="355" y2="175" stroke="#333" stroke-width="1.3" marker-end="url(#arr92)"/>
  <line x1="170" y1="198" x2="170" y2="18" stroke="#333" stroke-width="1.3" marker-end="url(#arr92)"/>
  <text x="360" y="179" font-size="13" font-style="italic" fill="#333">x</text>
  <text x="176" y="23" font-size="13" font-style="italic" fill="#333">y</text>
  <text x="157" y="190" font-size="12" fill="#333">O</text>
  <!-- 上半圆 r = 5 (1 unit = 20px, center (170,175), r=100) -->
  <path d="M 70 175 A 100 100 0 0 1 270 175" fill="none" stroke="#1f77b4" stroke-width="2.4"/>
  <text x="64" y="191" font-size="11.5" fill="#333">-5</text>
  <text x="266" y="191" font-size="11.5" fill="#333">5</text>
  <text x="155" y="73" font-size="11.5" fill="#333">5</text>
  <text x="58" y="88" font-size="12" fill="#1f77b4" font-weight="bold">y = √(25 - x²)</text>
  <!-- 切点 (3, 4) -> (170+60, 175-80) = (230, 95) -->
  <circle cx="230" cy="95" r="4" fill="#d62728"/>
  <text x="238" y="88" font-size="12" fill="#d62728" font-weight="bold">P(3, 4)</text>
  <!-- 半径 OP -->
  <line x1="170" y1="175" x2="230" y2="95" stroke="#888" stroke-width="1.2" stroke-dasharray="4,3"/>
  <!-- 切线 y = -3/4 x + 25/4: x=0 -> y=6.25 (170, 50); x=8.33 -> y=0 (336.6, 175) -->
  <line x1="120" y1="12.5" x2="345" y2="181.25" stroke="#d62728" stroke-width="2"/>
  <text x="242" y="128" font-size="11.5" fill="#d62728">y = -(3/4)x + 25/4</text>
</svg>

- **【分步标准解答】**
  曲線 $y = \sqrt{25 - x^2}$ は $-5 \le x \le 5,\; y \ge 0$ の上半円である。
  $-5 < x < 5$ で微分すると、
  $$y' = \frac{-2x}{2\sqrt{25 - x^2}} = -\frac{x}{\sqrt{25 - x^2}}$$
  接点の $x$ 座標を $t$（$-5 < t < 5$）とおくと、傾きが $-\dfrac{3}{4}$ であるから、
  $$-\frac{t}{\sqrt{25 - t^2}} = -\frac{3}{4} \iff \frac{t}{\sqrt{25 - t^2}} = \frac{3}{4}$$
  > 💡 讲师批注：**极易漏检的符号条件！** 右边 $\dfrac{3}{4} > 0$，分母 $\sqrt{25 - t^2} > 0$，因此**必有 $t > 0$**！若直接平方而不记 $t > 0$，会错把增根 $t = -3$（对应斜率 $+\frac{3}{4}$）也算进去！

  両辺を 2 乗すると（ただし $t > 0$）、
  $$\frac{t^2}{25 - t^2} = \frac{9}{16} \implies 16t^2 = 9(25 - t^2) \implies 25t^2 = 225 \implies t^2 = 9$$
  $t > 0$ より $t = 3$。
  このとき $y = \sqrt{25 - 3^2} = 4$ であるから、接点は $(3, 4)$。
  よって、求める接線の方程式は、
  $$y - 4 = -\frac{3}{4}(x - 3) \implies y = -\frac{3}{4}x + \frac{25}{4}$$
- **【最终答案】**
  **$y = -\dfrac{3}{4}x + \dfrac{25}{4}$**（或 $3x + 4y = 25$）

---

#### 演習問題 9-(3)
- **【原题重现与翻译】**
  - 原题：点 $(2, -2)$ から、曲線 $y = \dfrac{1}{3}x^3 - x$ に引いた接線の方程式を求めよ。
  - 中文：从点 $(2, -2)$ 向曲线 $y = \dfrac{1}{3}x^3 - x$ 引切线，求切线方程。
- **【考点定位】**
  - 过曲线外一点（「から引いた」）引切线：设切点法。
- **【分步标准解答】**
  まず点 $(2, -2)$ が曲線上にあるか確認すると、$\dfrac{1}{3} \cdot 2^3 - 2 = \dfrac{2}{3} \neq -2$ より曲線外の点である。
  $f(x) = \dfrac{1}{3}x^3 - x$ とおくと、$f'(x) = x^2 - 1$。
  接点の座標を $\left(t,\; \dfrac{1}{3}t^3 - t\right)$ とおくと、接線の方程式は、
  $$y - \left(\frac{1}{3}t^3 - t\right) = (t^2 - 1)(x - t)$$
  $$y = (t^2 - 1)x - \frac{2}{3}t^3 \qquad \cdots \text{①}$$
  > 💡 讲师批注：把常数项合并整理成 $y = (t^2 - 1)x - \frac{2}{3}t^3$，代入点和最后回代求切线都清爽无比！

  この接線が点 $(2, -2)$ を通るから、$x = 2,\; y = -2$ を代入すると、
  $$-2 = 2(t^2 - 1) - \frac{2}{3}t^3$$
  $$-2 = 2t^2 - 2 - \frac{2}{3}t^3 \implies \frac{2}{3}t^3 - 2t^2 = 0 \implies t^2(t - 3) = 0$$
  よって $t = 0,\; 3$。
  - $t = 0$ のとき、①より $y = -x$。
  - $t = 3$ のとき、①より $y = (9 - 1)x - \dfrac{2}{3} \cdot 27 = 8x - 18$。
  > 💡 讲师批注：注意 $t = 0$ 是重根！几何上意味着 $(0, 0)$ 恰是三次函数的**拐点（変曲点）**，$y = -x$ 既是切线又穿过曲线。
- **【最终答案】**
  **$y = -x$，$y = 8x - 18$**

---

#### 演習問題 9-(4)
- **【原题重现与翻译】**
  - 原题：原点から曲線 $y = \log x - 1$ に引いた接線の方程式を求めよ。
  - 中文：从原点向曲线 $y = \log x - 1$ 引切线，求切线方程。
- **【考点定位】**
  - 过曲线外一点向对数曲线引切线。
- **【分步标准解答】**
  $f(x) = \log x - 1$（$x > 0$）とおくと、$f'(x) = \dfrac{1}{x}$。
  接点の座標を $(t,\; \log t - 1)$（$t > 0$）とおくと、接線の方程式は、
  $$y - (\log t - 1) = \frac{1}{t}(x - t)$$
  $$y = \frac{1}{t}x + \log t - 2$$
  この接線が原点 $(0, 0)$ を通るから、$x = 0,\; y = 0$ を代入すると、
  $$0 = \log t - 2 \implies \log t = 2 \implies t = e^2$$
  これは $t > 0$ を満たす。よって、求める接線の方程式は、
  $$y = \frac{1}{e^2}x$$
  > 💡 讲师批注：高频秒杀结论——原点向 $y = \log x$ 引的切线是 $y = \frac{1}{e}x$（切点 $(e, 1)$）；向下平移 $1$ 个单位变成 $y = \log x - 1$ 后，切点变为 $(e^2, 1)$，切线斜率为 $\frac{1}{e^2}$。
- **【最终答案】**
  **$y = \dfrac{1}{e^2}x$**

---

#### 演習問題 9-(5)
- **【原题重现与翻译】**
  - 原题：二つ放物線 $y = -x^2$，$y = x^2 - 2x + 5$ の共通接線の方程式を求めよ。
  - 中文：求两条抛物线 $y = -x^2$ 与 $y = x^2 - 2x + 5$ 的公切线方程。
- **【考点定位】**
  - 两抛物线的公切线（共通接線）：一侧设切点 + 另一侧联立判别式 $D = 0$。
- **【图解辅助（SVG 矢量图）】**

<svg viewBox="0 0 380 230" width="380" height="230" xmlns="http://www.w3.org/2000/svg" style="background:#fafbfc;border:1px solid #e1e4e8;border-radius:6px;">
  <defs>
    <marker id="arr95" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#333"/>
    </marker>
  </defs>
  <!-- 坐标轴：原点 (170, 145)，scale: x=28px, y=13px -->
  <line x1="25" y1="145" x2="355" y2="145" stroke="#333" stroke-width="1.2" marker-end="url(#arr95)"/>
  <line x1="170" y1="220" x2="170" y2="15" stroke="#333" stroke-width="1.2" marker-end="url(#arr95)"/>
  <text x="360" y="149" font-size="12" font-style="italic" fill="#333">x</text>
  <text x="176" y="20" font-size="12" font-style="italic" fill="#333">y</text>
  <text x="157" y="159" font-size="11" fill="#333">O</text>
  <!-- y = -x^2: x=-2.4 -> (103, 220), x=0 -> (170,145), x=2.4 -> (237, 220) -->
  <path d="M 103 220 Q 170 70 237 220" fill="none" stroke="#1f77b4" stroke-width="2.2"/>
  <text x="242" y="210" font-size="11.5" fill="#1f77b4" font-weight="bold">y = -x²</text>
  <!-- y = x^2 - 2x + 5 = (x-1)^2 + 4: vertex (1,4)->(198,93), x=-1.5 -> (128,12), x=3.5 -> (268,12) -->
  <path d="M 128 12 Q 198 174 268 12" fill="none" stroke="#2e7d32" stroke-width="2.2"/>
  <text x="255" y="34" font-size="11.5" fill="#2e7d32" font-weight="bold">y = x²-2x+5</text>
  <!-- 公切线 1: y = 2x + 1: x=-2.5 -> (100,197), x=3.5 -> (268,41) -->
  <line x1="92" y1="205" x2="295" y2="16" stroke="#d62728" stroke-width="1.8" stroke-dasharray="6,3"/>
  <text x="275" y="75" font-size="11" fill="#d62728" font-weight="bold">y = 2x + 1</text>
  <!-- 公切线 2: y = -4x + 4: x=-1.3 -> (134, 25), x=2.6 -> (243, 228) -->
  <line x1="128" y1="15" x2="240" y2="223" stroke="#e65100" stroke-width="1.8" stroke-dasharray="6,3"/>
  <text x="36" y="55" font-size="11" fill="#e65100" font-weight="bold">y = -4x + 4</text>
  <!-- 切点标记 -->
  <circle cx="142" cy="158" r="3" fill="#d62728"/>
  <circle cx="226" cy="80" r="3" fill="#d62728"/>
  <circle cx="226" cy="197" r="3" fill="#e65100"/>
  <circle cx="142" cy="41" r="3" fill="#e65100"/>
</svg>

- **【分步标准解答】**
  放物線 $C_1: y = -x^2$ において $y' = -2x$ である。
  $C_1$ 上の点 $(t, -t^2)$ における接線の方程式は、
  $$y - (-t^2) = -2t(x - t) \implies y = -2tx + t^2 \qquad \cdots \text{①}$$
  この直線が放物線 $C_2: y = x^2 - 2x + 5$ にも接するための条件は、両式から $y$ を消去した 2 次方程式
  $$x^2 - 2x + 5 = -2tx + t^2$$
  $$x^2 + 2(t - 1)x + (5 - t^2) = 0$$
  が重解をもつことである。判別式を $D$ とすると、
  $$\frac{D}{4} = (t - 1)^2 - (5 - t^2) = 0$$
  $$2t^2 - 2t - 4 = 0 \implies t^2 - t - 2 = 0 \implies (t - 2)(t + 1) = 0$$
  よって $t = -1,\; 2$。
  ① に代入すると、
  - $t = -1$ のとき：$y = 2x + 1$
  - $t = 2$ のとき：$y = -4x + 4$
  > 💡 讲师批注：当另一条曲线是**二次函数（抛物线）**时，用判别式 $D = 0$ 只需设一个未知数 $t$，比设两个切点 $s, t$ 快得多！
- **【最终答案】**
  **$y = 2x + 1$，$y = -4x + 4$**

---

#### 演習問題 9-(6)
- **【原题重现与翻译】**
  - 原题：$k > 0$ とする。曲線 $y = k\sqrt{x}$ 上にない点 $(0, 2)$ からこの曲線に引いた接線の方程式が $y = 8x + 2$ であるとき、定数 $k$ の値と接点の座標を求めよ。
  - 中文：设 $k > 0$。从不在曲线 $y = k\sqrt{x}$ 上的点 $(0, 2)$ 向该曲线引出的切线方程为 $y = 8x + 2$，求常数 $k$ 的值与切点坐标。
- **【考点定位】**
  - 由已知切线方程反求函数参数 $k$ 与切点坐标。
- **【分步标准解答】**
  $y = k\sqrt{x} = kx^{\frac{1}{2}}$ を $x$ で微分すると（$x > 0$）、
  $$y' = \frac{k}{2\sqrt{x}}$$
  接点の座標を $(t,\; k\sqrt{t})$（$t > 0$）とおくと、この点における接線の方程式は、
  $$y - k\sqrt{t} = \frac{k}{2\sqrt{t}}(x - t)$$
  $$y = \frac{k}{2\sqrt{t}}x + \frac{k\sqrt{t}}{2}$$
  これが直線 $y = 8x + 2$ と一致するから、傾きと $y$ 切片を比較して、
  $$\frac{k}{2\sqrt{t}} = 8 \quad \cdots \text{①}, \qquad \frac{k\sqrt{t}}{2} = 2 \quad \cdots \text{②}$$
  ① $\times$ ② より $\sqrt{t}$ を消去すると、
  $$\frac{k^2}{4} = 16 \implies k^2 = 64$$
  $k > 0$ より $k = 8$。
  > 💡 讲师批注：① 与 ② 两式直接相乘瞬间消去 $\sqrt{t}$，无需开方化简，一步出 $k$！

  これを ② に代入すると、
  $$\frac{8\sqrt{t}}{2} = 2 \implies 4\sqrt{t} = 2 \implies \sqrt{t} = \frac{1}{2} \implies t = \frac{1}{4}$$
  このとき接点の $y$ 座標は $k\sqrt{t} = 8 \cdot \dfrac{1}{2} = 4$ となる。
- **【最终答案】**
  **$k = 8$，接点の座標は $\left(\dfrac{1}{4},\; 4\right)$**

---

#### 演習問題 9-(7)
- **【原题重现与翻译】**
  - 原题：二つ曲線 $y = -x^2$，$y = \dfrac{1}{x}$ に同時に接する直線の方程式を求めよ。
  - 中文：求同时与两条曲线 $y = -x^2$ 和 $y = \dfrac{1}{x}$ 相切的直线方程。
- **【考点定位】**
  - 一般两曲线的公切线（双切点设元比较系数法）。
- **【分步标准解答】**
  曲線 $C_1: y = -x^2$ 上の点 $(s, -s^2)$ における接線の方程式は、$y' = -2x$ より、
  $$y - (-s^2) = -2s(x - s) \implies y = -2sx + s^2 \qquad \cdots \text{①}$$
  曲線 $C_2: y = \dfrac{1}{x}$ 上の点 $\left(t, \dfrac{1}{t}\right)$（$t \neq 0$）における接線の方程式は、$y' = -\dfrac{1}{x^2}$ より、
  $$y - \frac{1}{t} = -\frac{1}{t^2}(x - t) \implies y = -\frac{1}{t^2}x + \frac{2}{t} \qquad \cdots \text{②}$$
  ① と ② が同じ直線を表すための条件は、傾きと $y$ 切片がそれぞれ等しいことであるから、
  $$-2s = -\frac{1}{t^2} \quad \cdots \text{③}, \qquad s^2 = \frac{2}{t} \quad \cdots \text{④}$$
  ③ より $s = \dfrac{1}{2t^2}$ を ④ に代入すると、
  $$\left(\frac{1}{2t^2}\right)^2 = \frac{2}{t} \implies \frac{1}{4t^4} = \frac{2}{t} \implies 8t^3 = 1 \implies t^3 = \frac{1}{8}$$
  $t$ は実数であるから $t = \dfrac{1}{2}$（$t \neq 0$ を満たす）。
  このとき $s = \dfrac{1}{2 \cdot \left(\frac{1}{2}\right)^2} = 2$。
  ① に代入すると、求める接線の方程式は、
  $$y = -4x + 4$$
  > 💡 讲师批注：别解——也可把 ① 代入 $y = \frac{1}{x}$ 得 $-2sx^2 + s^2 x - 1 = 0$，令判别式 $D = s^4 - 8s = s(s^3 - 8) = 0$。因 $s = 0$ 时直线为 $y = 0$（渐近线，不相切），故 $s = 2$，立刻得 $y = -4x + 4$！两种方法互为验算。
- **【最终答案】**
  **$y = -4x + 4$**

---

#### 演習問題 9-(8)
- **【原题重现与翻译】**
  - 原题：$0 < x < \pi$ のとき、曲線 $C_1: y = 2\sin x$ と曲線 $C_2: y = k - \cos 2x$ が共有点 $P$ で共通の接線 $l$ をもつ。定数 $k$ の値と点 $P$ の座標を求めよ。
  - 中文：当 $0 < x < \pi$ 时，曲线 $C_1: y = 2\sin x$ 与曲线 $C_2: y = k - \cos 2x$ 在公共点 $P$ 处有公共切线 $l$，求常数 $k$ 的值及点 $P$ 的坐标。
- **【考点定位】**
  - 两三角函数曲线在公共点处相切（$f(t) = g(t)$ 且 $f'(t) = g'(t)$）、三角方程防漏解！
- **【图解辅助（SVG 矢量图）】**

<svg viewBox="0 0 420 215" width="420" height="215" xmlns="http://www.w3.org/2000/svg" style="background:#fafbfc;border:1px solid #e1e4e8;border-radius:6px;">
  <defs>
    <marker id="arr98" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#333"/>
    </marker>
  </defs>
  <!-- 坐标轴：x=0 at 45, x=π at 359 (100px/rad), y=0 at 175 (55px/unit) -->
  <line x1="25" y1="175" x2="395" y2="175" stroke="#333" stroke-width="1.2" marker-end="url(#arr98)"/>
  <line x1="45" y1="200" x2="45" y2="18" stroke="#333" stroke-width="1.2" marker-end="url(#arr98)"/>
  <text x="400" y="179" font-size="12" font-style="italic" fill="#333">x</text>
  <text x="51" y="23" font-size="12" font-style="italic" fill="#333">y</text>
  <text x="33" y="190" font-size="11" fill="#333">O</text>
  <!-- 刻度 -->
  <text x="196" y="191" font-size="11" fill="#333">π/2</text>
  <text x="355" y="191" font-size="11" fill="#333">π</text>
  <text x="30" y="69" font-size="11" fill="#333">2</text>
  <text x="30" y="124" font-size="11" fill="#333">1</text>
  <!-- C1: y = 2 sin x -->
  <path d="M 45 175 C 100 65, 145 65, 202 65 C 259 65, 304 65, 359 175" fill="none" stroke="#1f77b4" stroke-width="2.4"/>
  <text x="64" y="95" font-size="11.5" fill="#1f77b4" font-weight="bold">C₁: y = 2sin x</text>
  <!-- C2 (k = 1): y = 1 - cos 2x = 2 sin^2 x -->
  <path d="M 45 175 C 110 175, 145 65, 202 65 C 259 65, 294 175, 359 175" fill="none" stroke="#d62728" stroke-width="2" stroke-dasharray="5,3"/>
  <text x="275" y="55" font-size="11" fill="#d62728">k = 1: P(π/2, 2)</text>
  <!-- C2 (k = 3/2): y = 1.5 - cos 2x -->
  <path d="M 45 147.5 C 110 147.5, 145 37.5, 202 37.5 C 259 37.5, 294 147.5, 359 147.5" fill="none" stroke="#2e7d32" stroke-width="2" stroke-dasharray="3,2"/>
  <text x="260" y="28" font-size="11" fill="#2e7d32">k = 3/2: P(π/6, 1), (5π/6, 1)</text>
  <!-- 切点 -->
  <circle cx="202" cy="65" r="4" fill="#d62728"/>
  <circle cx="97" cy="120" r="4" fill="#2e7d32"/>
  <circle cx="307" cy="120" r="4" fill="#2e7d32"/>
</svg>

- **【分步标准解答】**
  $f(x) = 2\sin x$，$g(x) = k - \cos 2x$ とおくと、
  $$f'(x) = 2\cos x, \qquad g'(x) = 2\sin 2x = 4\sin x \cos x$$
  点 $P$ の $x$ 座標を $t$（$0 < t < \pi$）とおく。$C_1$ と $C_2$ が点 $P$ で共通の接線をもつ条件は、
  $$f(t) = g(t) \quad \text{かつ} \quad f'(t) = g'(t)$$
  まず $f'(t) = g'(t)$ より、
  $$2\cos t = 4\sin t \cos t$$
  $$2\cos t(1 - 2\sin t) = 0$$
  > 💡 讲师批注：**严禁两边直接约去 $\cos t$！** 约去 $\cos t$ 会直接丢掉 $\cos t = 0$（即 $t = \frac{\pi}{2}$、两曲线在顶点水平相切）的解！必须移项提公因式！

  よって、$\cos t = 0$ または $\sin t = \dfrac{1}{2}$。
  $0 < t < \pi$ の範囲でこれを解くと、
  - **[1] $\cos t = 0$ のとき**：$t = \dfrac{\pi}{2}$。
    $f\left(\dfrac{\pi}{2}\right) = g\left(\dfrac{\pi}{2}\right)$ より、
    $$2\sin\frac{\pi}{2} = k - \cos\pi \implies 2 = k - (-1) \implies k = 1$$
    このとき $P$ の座標は $\left(\dfrac{\pi}{2},\; 2\right)$。
  - **[2] $\sin t = \dfrac{1}{2}$ のとき**：$t = \dfrac{\pi}{6},\; \dfrac{5\pi}{6}$。
    - $t = \dfrac{\pi}{6}$ のとき：$2\sin\dfrac{\pi}{6} = k - \cos\dfrac{\pi}{3} \implies 1 = k - \dfrac{1}{2} \implies k = \dfrac{3}{2}$。点 $P\left(\dfrac{\pi}{6},\; 1\right)$。
    - $t = \dfrac{5\pi}{6}$ のとき：$2\sin\dfrac{5\pi}{6} = k - \cos\dfrac{5\pi}{3} \implies 1 = k - \dfrac{1}{2} \implies k = \dfrac{3}{2}$。点 $P\left(\dfrac{5\pi}{6},\; 1\right)$。
- **【最终答案】**
  - **$k = 1$ のとき、$P\left(\dfrac{\pi}{2},\; 2\right)$**
  - **$k = \dfrac{3}{2}$ のとき、$P\left(\dfrac{\pi}{6},\; 1\right)$ または $P\left(\dfrac{5\pi}{6},\; 1\right)$**

---

#### 演習問題 9-(9)
- **【原题重现与翻译】**
  - 原题：2 曲線 $y = x^3 - 2x + 1$ と $y = x^2 + 2ax + 1$ が接するとき、定数 $a$ の値を求めよ。また、その接点における共通接線の方程式を求めよ。
  - 中文：两曲线 $y = x^3 - 2x + 1$ 与 $y = x^2 + 2ax + 1$ 相切时，求常数 $a$ 的值，并求在该切点处的公切线方程。
- **【考点定位】**
  - 两多项式曲线相切的条件（$f(t) = g(t)$ 且 $f'(t) = g'(t)$）与消参法。
- **【分步标准解答】**
  $f(x) = x^3 - 2x + 1$，$g(x) = x^2 + 2ax + 1$ とおくと、
  $$f'(x) = 3x^2 - 2, \qquad g'(x) = 2x + 2a$$
  接点の $x$ 座標を $t$ とおくと、2 曲線が接する条件より、
  $$f(t) = g(t) \implies t^3 - 2t + 1 = t^2 + 2at + 1 \implies t^3 - t^2 - 2(a + 1)t = 0 \qquad \cdots \text{①}$$
  $$f'(t) = g'(t) \implies 3t^2 - 2 = 2t + 2a \implies 2a = 3t^2 - 2t - 2 \qquad \cdots \text{②}$$
  ② を ① に代入して $a$ を消去すると、
  $$t^3 - t^2 - (3t^2 - 2t)t = 0$$
  $$-2t^3 + t^2 = 0 \implies t^2(1 - 2t) = 0$$
  よって $t = 0,\; \dfrac{1}{2}$。
  > 💡 讲师批注：把参数 $a$ 用 $t$ 表示后代入另一式消去 $a$，是解含参相切方程组的标准套路！

  - **[1] $t = 0$ のとき**：
    ② より $2a = -2 \implies a = -1$。
    接点は $(0,\; f(0)) = (0, 1)$、傾きは $f'(0) = -2$ であるから、共通接線の方程式は、
    $$y - 1 = -2(x - 0) \implies y = -2x + 1$$
  - **[2] $t = \dfrac{1}{2}$ のとき**：
    ② より $2a = 3 \cdot \dfrac{1}{4} - 2 \cdot \dfrac{1}{2} - 2 = -\dfrac{9}{4} \implies a = -\dfrac{9}{8}$。
    接点の $y$ 座標は $f\left(\dfrac{1}{2}\right) = \dfrac{1}{8} - 1 + 1 = \dfrac{1}{8}$、傾きは $f'\left(\dfrac{1}{2}\right) = \dfrac{3}{4} - 2 = -\dfrac{5}{4}$ であるから、共通接線の方程式は、
    $$y - \frac{1}{8} = -\frac{5}{4}\left(x - \frac{1}{2}\right) \implies y = -\frac{5}{4}x + \frac{3}{4}$$
- **【最终答案】**
  - **$a = -1$ のとき、共通接線：$y = -2x + 1$**
  - **$a = -\dfrac{9}{8}$ のとき、共通接線：$y = -\dfrac{5}{4}x + \dfrac{3}{4}$**

---

#### 演習問題 9-(10)
- **【原题重现与翻译】**
  - 原题：関数 $y = x^3(x - 4)$ のグラフと異なる 2 点で接する直線の方程式を求めよ。
  - 中文：求与函数 $y = x^3(x - 4)$ 的图像在两个不同点相切的直线方程。
- **【考点定位】**
  - **四次函数的二重切线（複接線）**：恒等式比较系数法（超级提速技巧！）。
- **【图解辅助（SVG 矢量图）】**

<svg viewBox="0 0 380 215" width="380" height="215" xmlns="http://www.w3.org/2000/svg" style="background:#fafbfc;border:1px solid #e1e4e8;border-radius:6px;">
  <defs>
    <marker id="arr910" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#333"/>
    </marker>
  </defs>
  <!-- 坐标轴：原点 (120, 70), x scale = 42px, y scale = 4.5px -->
  <line x1="25" y1="70" x2="355" y2="70" stroke="#333" stroke-width="1.2" marker-end="url(#arr910)"/>
  <line x1="120" y1="205" x2="120" y2="15" stroke="#333" stroke-width="1.2" marker-end="url(#arr910)"/>
  <text x="360" y="74" font-size="12" font-style="italic" fill="#333">x</text>
  <text x="126" y="20" font-size="12" font-style="italic" fill="#333">y</text>
  <text x="107" y="84" font-size="11" fill="#333">O</text>
  <text x="285" y="84" font-size="11" fill="#333">4</text>
  <!-- y = x^4 - 4x^3:
       x=-1.1 -> y=6.8 (74, 39)
       x=-0.732 (1-√3) -> y=1.856 (89, 61.6)
       x=0 -> y=0 (120, 70)
       x=1 -> y=-3 (162, 83.5)
       x=2 -> y=-16 (204, 142)
       x=2.732 (1+√3) -> y=-25.856 (235, 186.4)
       x=3 -> y=-27 (246, 191.5)
       x=4 -> y=0 (288, 70)
       x=4.2 -> y=14.8 (296, 3) -->
  <path d="M 70 25 C 82 62, 102 70, 120 70 C 155 70, 200 185, 246 191.5 C 272 191.5, 282 110, 294 20" fill="none" stroke="#1f77b4" stroke-width="2.3"/>
  <text x="148" y="38" font-size="12" fill="#1f77b4" font-weight="bold">y = x³(x - 4)</text>
  <!-- 二重切线 y = -8x - 4:
       x=-1.2 -> y=5.6 (70, 44.8)
       x=3.0 -> y=-28 (246, 196) -->
  <line x1="65" y1="40" x2="256" y2="204" stroke="#d62728" stroke-width="2"/>
  <text x="242" y="160" font-size="11.5" fill="#d62728" font-weight="bold">y = -8x - 4</text>
  <!-- 两个切点 -->
  <circle cx="89" cy="61.6" r="4" fill="#d62728"/>
  <text x="32" y="90" font-size="10.5" fill="#d62728">x = 1 - √3</text>
  <circle cx="235" cy="186.4" r="4" fill="#d62728"/>
  <text x="145" y="198" font-size="10.5" fill="#d62728">x = 1 + √3</text>
</svg>

- **【分步标准解答】**
  求める直線の方程式を $y = mx + n$ とし、この直線が曲線 $y = x^4 - 4x^3$ と異なる 2 点 $x = \alpha,\; \beta$（$\alpha \neq \beta$）で接するとする。
  このとき、方程式 $x^4 - 4x^3 - (mx + n) = 0$ は $\alpha,\; \beta$ をそれぞれ重解にもつから、次の恒等式が成り立つ：
  $$x^4 - 4x^3 - mx - n = (x - \alpha)^2(x - \beta)^2$$
  > 💡 讲师批注：**满分神技！** 如果老老实实设两个切点联立求导，计算量巨大；利用「在两点相切 $\Leftrightarrow$ 差函数有两个二重根」直接写成完全平方式，4 行秒杀！

  ここで $\alpha + \beta = p$，$\alpha\beta = q$ とおくと、右辺は次のように展開できる：
  $$(x^2 - px + q)^2 = x^4 - 2px^3 + (p^2 + 2q)x^2 - 2pqx + q^2$$
  両辺の係数を比較すると、
  - $x^3$ の係数：$-2p = -4 \implies p = 2$
  - $x^2$ の係数：$p^2 + 2q = 0 \implies 4 + 2q = 0 \implies q = -2$
  - $x$ の係数：$-m = -2pq = -2(2)(-2) = 8 \implies m = -8$
  - 定数項：$-n = q^2 = (-2)^2 = 4 \implies n = -4$

  ここで、$\alpha, \beta$ は 2 次方程式 $t^2 - 2t - 2 = 0$ の 2 解であり、判別式 $D/4 = 1^2 - (-2) = 3 > 0$ より、確かに**異なる 2 つの実数** $\alpha, \beta = 1 \pm \sqrt{3}$ が存在する。
  > 💡 讲师批注：最后一步检验 $\alpha, \beta$ 确实是不同实数（判别式 $> 0$），在严谨证明中不可或缺！

  よって、求める直線の方程式は $y = -8x - 4$ である。
- **【最终答案】**
  **$y = -8x - 4$**

---

#### 演習問題 9-(11)
- **【原题重现与翻译】**
  - 原题：曲線 $C: y = x^3 + 3x^2 + x$ と点 $A(1, a)$ がある。$A$ を通って $C$ に 3 本の接線が引けるとき、定数 $a$ の値の範囲を求めよ。
  - 中文：已知曲线 $C: y = x^3 + 3x^2 + x$ 与点 $A(1, a)$。当过点 $A$ 可以向曲线 $C$ 引出 3 条切线时，求常数 $a$ 的取值范围。
- **【考点定位】**
  - 三次函数的切线条数问题 $\Leftrightarrow$ 参变分离转化为三次函数极值与水平直线交点数问题（EJU 绝对王牌压轴题型！）。
- **【图解辅助（SVG 矢量图）】**

<svg viewBox="0 0 420 220" width="420" height="220" xmlns="http://www.w3.org/2000/svg" style="background:#fafbfc;border:1px solid #e1e4e8;border-radius:6px;">
  <defs>
    <marker id="arr911" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#333"/>
    </marker>
  </defs>
  <!-- 坐标轴：原点 (200, 118)，t scale = 55px, y scale = 14px -->
  <line x1="25" y1="118" x2="385" y2="118" stroke="#333" stroke-width="1.2" marker-end="url(#arr911)"/>
  <line x1="200" y1="208" x2="200" y2="15" stroke="#333" stroke-width="1.2" marker-end="url(#arr911)"/>
  <text x="390" y="122" font-size="12" font-style="italic" fill="#333">t</text>
  <text x="206" y="20" font-size="12" font-style="italic" fill="#333">y</text>
  <text x="188" y="132" font-size="11" fill="#333">O</text>
  <!-- 3交点区域阴影 (-3 < y < 5 -> y_svg from 48 to 160) -->
  <rect x="35" y="48" width="335" height="112" fill="#e8f5e9" opacity="0.65"/>
  <!-- g(t) = -2t^3 + 6t + 1:
       t=-2 -> y=5 (90, 48)
       t=-1 -> y=-3 (145, 160) 极小
       t=0 -> y=1 (200, 104)
       t=1 -> y=5 (255, 48) 极大
       t=2 -> y=-3 (310, 160)
       t=2.2 -> y=-7.1 (321, 200) -->
  <path d="M 80 18 C 102 105, 125 160, 145 160 C 172 160, 228 48, 255 48 C 275 48, 298 105, 320 198" fill="none" stroke="#1f77b4" stroke-width="2.4"/>
  <text x="275" y="34" font-size="11.5" fill="#1f77b4" font-weight="bold">y = g(t) = -2t³ + 6t + 1</text>
  <!-- 极值点虚线与水平线 y = a -->
  <line x1="35" y1="48" x2="370" y2="48" stroke="#d62728" stroke-width="1.2" stroke-dasharray="4,3"/>
  <line x1="35" y1="160" x2="370" y2="160" stroke="#d62728" stroke-width="1.2" stroke-dasharray="4,3"/>
  <line x1="35" y1="90" x2="370" y2="90" stroke="#2e7d32" stroke-width="1.8"/>
  <text x="325" y="85" font-size="11.5" fill="#2e7d32" font-weight="bold">y = a (3交点)</text>
  <!-- 关键点标注 -->
  <circle cx="145" cy="160" r="3.5" fill="#d62728"/>
  <text x="128" y="176" font-size="11" fill="#d62728">(-1, -3) 极小</text>
  <circle cx="255" cy="48" r="3.5" fill="#d62728"/>
  <text x="228" y="42" font-size="11" fill="#d62728">(1, 5) 极大</text>
  <text x="204" y="44" font-size="11" fill="#333">5</text>
  <text x="204" y="173" font-size="11" fill="#333">-3</text>
</svg>

- **【分步标准解答】**
  $f(x) = x^3 + 3x^2 + x$ とおくと、$f'(x) = 3x^2 + 6x + 1$。
  曲線 $C$ 上の点 $(t,\; t^3 + 3t^2 + t)$ における接線の方程式は、
  $$y - (t^3 + 3t^2 + t) = (3t^2 + 6t + 1)(x - t)$$
  この接線が点 $A(1, a)$ を通るから、$x = 1,\; y = a$ を代入すると、
  $$a - (t^3 + 3t^2 + t) = (3t^2 + 6t + 1)(1 - t)$$
  $$a = (t^3 + 3t^2 + t) + (3t^2 + 6t + 1 - 3t^3 - 6t^2 - t)$$
  $$a = -2t^3 + 6t + 1 \qquad \cdots \text{①}$$
  > 💡 讲师批注：整理时注意 $3t^2 + 3t^2 - 6t^2 = 0$，二次项恰好消去！这种简洁结果是正确计算的强力信号。

  ここで、3 次曲線 $C$ においては**異なる接点 $t$ に対して必ず異なる接線が 1 対 1 に対応する**（3 次曲線には 2 点以上で同時に接する二重接線は存在しないため）。
  したがって、点 $A$ から $C$ に 3 本の接線が引けるための必要十分条件は、$t$ に関する方程式 ① が**異なる 3 つの実数解をもつ**ことである。
  > 💡 讲师批注：**大学笔试扣分重灾区！** 必须明确写出一句「接点 $t$ 与切线一一对应（3次曲线无二重切线）」，否则在記述式考试中会被扣掉逻辑分！

  $g(t) = -2t^3 + 6t + 1$ とおくと、
  $$g'(t) = -6t^2 + 6 = -6(t + 1)(t - 1)$$
  $g'(t) = 0$ を解くと $t = -1,\; 1$。$g(t)$ の増減表は次のようになる：

  | $t$ | $\cdots$ | $-1$ | $\cdots$ | $1$ | $\cdots$ |
  | :---: | :---: | :---: | :---: | :---: | :---: |
  | $g'(t)$ | $-$ | $0$ | $+$ | $0$ | $-$ |
  | $g(t)$ | $\searrow$ | $-3$（極小） | $\nearrow$ | $5$（極大） | $\searrow$ |

  - 極小値：$g(-1) = -2(-1)^3 + 6(-1) + 1 = 2 - 6 + 1 = -3$
  - 極大値：$g(1) = -2(1)^3 + 6(1) + 1 = -2 + 6 + 1 = 5$

  直線 $y = a$ と曲線 $y = g(t)$ が異なる 3 つの共有点をもつための条件は、$a$ が極小値と極大値の間にあることだから、
  $$-3 < a < 5$$
- **【最终答案】**
  **$-3 < a < 5$**
