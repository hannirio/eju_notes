# 《EJU 教材全解与备课讲义》数学 023（下：P338–P345）

> **对应源文件**：`work_math/ocr_md/ocr_023_p331-345.md`（下册：承接 [`note_023_a.md`](file:///Users/baohan/Desktop/EJU/notes_math/note_023_a.md) 之知识点综述与核心词汇，完整解析 **演習問題 10 (12)–(21)** 与 **演習問題 11 (1)**）
> **视觉核对参考图**：`work_math/ref_imgs/page_0338.jpg` – `page_0345.jpg`

---

## 三、逐题深度解析（下：演習問題 10 (12)–(21) & 演習問題 11 (1)）

---

### 演習問題 10 (12)

- **【原题重现与翻译】**
  - 原题：関数 $f(x) = x^3 - 6x^2 + 3ax - 4$ の極大値と極小値の差が $4$ となるとき、定数 $a$ の値を求めよ。
  - 中文：当函数 $f(x) = x^3 - 6x^2 + 3ax - 4$ 的极大值与极小值之差为 $4$ 时，求常数 $a$ 的值。
  > ⚠️ **教材勘误提示**：原教材第 337 页（`page_0338.jpg`）题干将「極大値と極小値の差」误印为「**極小値**と極小値の差」，备课与授课时务必修正。
- **【考点定位】**
  - 三次函数极值之差（降次法 + 韦达定理；亦可用积分 $1/6$ 公式验算）。
- **【分步标准解答】**
  1. 微分する：
     $$f'(x) = 3x^2 - 12x + 3a = 3(x^2 - 4x + a)$$
  2. 極大値と極小値をもつための条件は、$x^2 - 4x + a = 0$ が異なる 2 つの実数解をもつことである：
     $$\frac{D}{4} = (-2)^2 - a = 4 - a > 0 \implies a < 4 \quad \cdots\text{①}$$
  3. 2 解を $\alpha, \beta$（$\alpha < \beta$）とすると、$x = \alpha$ で極大、$x = \beta$ で極小をとる。解と係数の関係より：
     $$\alpha + \beta = 4, \qquad \alpha\beta = a$$
     よって $\beta - \alpha > 0$ より：
     $$\beta - \alpha = \sqrt{(\alpha + \beta)^2 - 4\alpha\beta} = \sqrt{16 - 4a} = 2\sqrt{4 - a}$$
  4. $f(x)$ を $f'(x) = 3x^2 - 12x + 3a$ で割って次数下げを行う：
     $$f(x) = \left(\frac{1}{3}x - \frac{2}{3}\right) f'(x) + (2a - 8)x + (2a - 4)$$
     > 💡 讲师批注：多项式除法验算：$(\frac{1}{3}x - \frac{2}{3})(3x^2 - 12x + 3a) = x^3 - 6x^2 + (a+8)x - 2a$，用原式减去它得 $(2a-8)x + (2a-4)$，无误！
  5. $f'(\alpha) = f'(\beta) = 0$ を用いて極大値と極小値の差を計算する：
     $$\begin{aligned}
     f(\alpha) - f(\beta) &= (2a - 8)(\alpha - \beta) \\
     &= (8 - 2a)(\beta - \alpha) \\
     &= 2(4 - a) \cdot 2\sqrt{4 - a} = 4(4 - a)^{\frac{3}{2}}
     \end{aligned}$$
     > 💡 讲师批注：**EJU 秒杀公式（积分 $1/6$ 公式法）**：对三次函数 $f(x) = Ax^3 + \cdots$（极值点 $\alpha < \beta$），极值差恒等于 $\dfrac{|A|}{2}(\beta - \alpha)^3$！本题 $A=1$，故差 $= \dfrac{1}{2}(2\sqrt{4-a})^3 = 4(4-a)^{\frac{3}{2}}$，一步到位！
  6. 条件より $4(4 - a)^{\frac{3}{2}} = 4 \implies (4 - a)^{\frac{3}{2}} = 1 \implies 4 - a = 1 \implies a = 3$。
     これは ①（$a < 4$）を満たす。
     > 💡 讲师批注：回代验算：$a=3$ 时 $f(x)=x^3-6x^2+9x-4$，$f'(x)=3(x-1)(x-3)$，$f(1)=0,\; f(3)=-4$，极值差 $0-(-4)=4$，100% 正确！
- **【最终答案】**
  **$a = 3$**

---

### 演習問題 10 (13)

- **【原题重现与翻译】**
  - 原题：関数 $f(x) = x^4 - 8x^3 + 18kx^2$ が極大値を持たないとき、定数 $k$ の値の範囲を求めよ。
  - 中文：当函数 $f(x) = x^4 - 8x^3 + 18kx^2$ 没有极大值时，求常数 $k$ 的取值范围。
- **【考点定位】**
  - 四次函数无极大值的充要条件（**高频陷阱：切勿漏掉 $f'(x)$ 因子间产生重根的情况！**）。
- **【图解辅助（SVG 矢量图）】**

<svg viewBox="0 0 430 165" xmlns="http://www.w3.org/2000/svg" style="max-width:430px;display:block;margin:10px auto;background:#fafafa;border:1px solid #e0e0e0;border-radius:6px;">
  <!-- Case A: 3 distinct roots (has local max -> NG) -->
  <text x="18" y="20" font-size="11" font-weight="bold" fill="#d32f2f">× NG: 3个不同实根</text>
  <path d="M 22,40 C 35,125 45,130 56,130 C 68,130 74,90 85,90 C 96,90 102,135 114,135 C 125,135 135,95 144,40" fill="none" stroke="#d32f2f" stroke-width="2"/>
  <circle cx="85" cy="90" r="3.5" fill="#d32f2f"/>
  <text x="64" y="82" font-size="10" fill="#d32f2f">有极大值!</text>

  <line x1="152" y1="12" x2="152" y2="152" stroke="#ccc" stroke-dasharray="3,3"/>

  <!-- Case B: D<=0 (k>=1 -> OK) -->
  <text x="165" y="20" font-size="11" font-weight="bold" fill="#2e7d32">○ OK: k ≥ 1 (D ≤ 0)</text>
  <path d="M 172,38 C 190,120 205,135 222,135 C 242,135 262,100 280,38" fill="none" stroke="#2e7d32" stroke-width="2.2"/>
  <circle cx="222" cy="135" r="3.5" fill="#2e7d32"/>
  <text x="195" y="152" font-size="10" fill="#2e7d32">仅 x=0 极小</text>

  <line x1="292" y1="12" x2="292" y2="152" stroke="#ccc" stroke-dasharray="3,3"/>

  <!-- Case C: k=0 (x=0 is double root -> OK!) -->
  <text x="304" y="20" font-size="11" font-weight="bold" fill="#1565c0">○ OK: k = 0 (x=0 重根)</text>
  <path d="M 308,38 C 318,75 326,82 338,82 C 352,82 364,135 382,135 C 398,135 410,95 420,38" fill="none" stroke="#1565c0" stroke-width="2.2"/>
  <circle cx="338" cy="82" r="3.5" fill="#1565c0"/>
  <circle cx="382" cy="135" r="3.5" fill="#1565c0"/>
  <text x="308" y="98" font-size="10" fill="#1565c0">x=0 拐点</text>
  <text x="366" y="152" font-size="10" fill="#1565c0">x=6 极小</text>
</svg>

- **【分步标准解答】**
  1. 微分して因数分解する：
     $$f'(x) = 4x^3 - 24x^2 + 36kx = 4x(x^2 - 6x + 9k)$$
  2. 4 次関数 $f(x)$ は $x^4$ の係数が正（$1 > 0$）であるため、$f'(x) = 0$ が異なる 3 つの実数解をもつと増減は $\searrow \nearrow \searrow \nearrow$ となり必ず極大値をもつ。
     したがって、$f(x)$ が**極大値をもたないための必要十分条件**は、3 次方程式 $f'(x) = 0$ の異なる実数解の個数が **2 個以下**（すなわち 1 個または重解を含む 2 個）であることである。
  3. 2 次方程式 $x^2 - 6x + 9k = 0 \;\cdots\text{①}$ について、次の 2 つの場合に分けて調べる：
     - **場合 1：方程式 ① が実数解を 1 個以下（重解または虚数解）もつとき**
       判別式を $D$ とすると：
       $$\frac{D}{4} = (-3)^2 - 9k = 9 - 9k \le 0 \implies k \ge 1$$
       このとき $x^2 - 6x + 9k \ge 0$ となるため、$f'(x)$ の符号は $x = 0$ の前後でのみ負から正に変わり、極大値は存在しない。
     - **場合 2：方程式 ① が異なる 2 つの実数解をもち、そのうちの 1 つが $x = 0$ であるとき**
       ① に $x = 0$ を代入すると $9k = 0 \implies k = 0$。
       逆に $k = 0$ のとき、$f'(x) = 4x^2(x - 6)$ となり、$x = 0$ の前後では符号が変わらず（負のまま）、$x = 6$ の前後でのみ負から正に変わるため、極小値のみをもち極大値をもたない。
     > 💡 讲师批注：**全场最易失分陷阱！** 90% 的学生只做情况 1（判别式 $D \le 0$）得出 $k \ge 1$，完全忘记 $x=0$ 可以作为二次方程 ① 的根合并成重根 $x^2$，从而漏掉孤立解 **$k = 0$**！
  4. 以上をまとめて、$k = 0$ または $k \ge 1$。
- **【最终答案】**
  **$k = 0$ または $k \ge 1$**

---

### 演習問題 10 (14)

- **【原题重现与翻译】**
  - 原题：次の関数の最大値と最小値を求めよ。また、その時の $x$ の値を求めよ。
    $[1]\; y = x^3 - 6x^2 + 10 \quad (-2 \le x \le 3) \qquad [2]\; y = 3x^4 - 4x^3 - 12x^2 \quad (-1 \le x \le 3)$
  - 中文：求下列函数在给定闭区间上的最大值和最小值，以及取得最值时的 $x$ 值。
- **【考点定位】**
  - 闭区间上三次函数与四次函数的最大・最小值（增减表 + 端点值比较）。

#### $[1]\; y = x^3 - 6x^2 + 10 \quad (-2 \le x \le 3)$
- **【分步标准解答】**
  1. 微分する：
     $$y' = 3x^2 - 12x = 3x(x - 4)$$
  2. 区間 $-2 \le x \le 3$ において $y' = 0$ となるのは $x = 0$ のみ（$x = 4$ は区間外）。
  3. 端点および極値の計算：
     - $x = -2$：$y = (-2)^3 - 6(-2)^2 + 10 = -8 - 24 + 10 = -22$
     - $x = 0$：$y = 10$
     - $x = 3$：$y = 27 - 54 + 10 = -17$
  4. 増減表（$-2 \le x \le 3$）：

     | $x$ | $-2$ | $\cdots$ | $0$ | $\cdots$ | $3$ |
     | :---: | :---: | :---: | :---: | :---: | :---: |
     | $y'$ |  | $+$ | $0$ | $-$ |  |
     | $y$ | $-22$ | $\nearrow$ | $10$ | $\searrow$ | $-17$ |

     > 💡 讲师批注：最小值在两个端点 $-22$ 与 $-17$ 中比较得出，切勿只看一端。
- **【最终答案】**
  - **最大値：$10$（$x = 0$ のとき）、最小値：$-22$（$x = -2$ のとき）**

#### $[2]\; y = 3x^4 - 4x^3 - 12x^2 \quad (-1 \le x \le 3)$
- **【分步标准解答】**
  1. 微分して因数分解する：
     $$y' = 12x^3 - 12x^2 - 24x = 12x(x^2 - x - 2) = 12x(x + 1)(x - 2)$$
  2. 区間 $-1 \le x \le 3$ において $y' = 0$ となるのは $x = -1,\; 0,\; 2$。
  3. 各点の値を計算する：
     - $x = -1$：$y = 3(1) - 4(-1) - 12(1) = 3 + 4 - 12 = -5$
     - $x = 0$：$y = 0$
     - $x = 2$：$y = 3(16) - 4(8) - 12(4) = 48 - 32 - 48 = -32$
     - $x = 3$：$y = 3(81) - 4(27) - 12(9) = 243 - 108 - 108 = 27$
  4. 増減表（$-1 \le x \le 3$）：

     | $x$ | $-1$ | $\cdots$ | $0$ | $\cdots$ | $2$ | $\cdots$ | $3$ |
     | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
     | $y'$ | $0$ | $+$ | $0$ | $-$ | $0$ | $+$ |  |
     | $y$ | $-5$ | $\nearrow$ | $0$ | $\searrow$ | $-32$ | $\nearrow$ | $27$ |

     > 💡 讲师批注：比较所有候选值 $\{-5,\; 0,\; -32,\; 27\}$，最大值 $27$ 在右端点 $x=3$ 取得，最小值 $-32$ 在极小点 $x=2$ 取得。
- **【最终答案】**
  - **最大値：$27$（$x = 3$ のとき）、最小値：$-32$（$x = 2$ のとき）**

---

### 演習問題 10 (15)

- **【原题重现与翻译】**
  - 原题：$a$ を正の定数とする。3 次関数 $f(x) = x^3 - 2ax^2 + a^2 x$ の $0 \le x \le 1$ における最大値 $M(a)$ を求めよ。
  - 中文：设 $a$ 为正常数，求三次函数 $f(x) = x^3 - 2ax^2 + a^2 x$ 在 $0 \le x \le 1$ 上的最大值 $M(a)$。
- **【考点定位】**
  - **定区间、动函数（含参三次函数）**的最值分类讨论（关键：求出与极大值等高的右侧点 $\dfrac{4}{3}a$）。
- **【图解辅助（SVG 矢量图）】**

<svg viewBox="0 0 420 220" xmlns="http://www.w3.org/2000/svg" style="max-width:420px;display:block;margin:10px auto;background:#fafafa;border:1px solid #e0e0e0;border-radius:6px;">
  <defs>
    <marker id="arr15" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0,0 L0,6 L6,3 z" fill="#333"/></marker>
  </defs>
  <line x1="30" y1="170" x2="395" y2="170" stroke="#333" stroke-width="1.4" marker-end="url(#arr15)"/>
  <line x1="65" y1="200" x2="65" y2="20" stroke="#333" stroke-width="1.4" marker-end="url(#arr15)"/>
  <text x="398" y="174" font-size="12" font-style="italic" fill="#333">x</text>
  <text x="71" y="25" font-size="12" font-style="italic" fill="#333">y</text>
  <text x="52" y="185" font-size="12" fill="#333">O</text>
  <!-- Cubic y=x(x-a)^2: O=(65,170), a/3=(135,75), a=(275,170), 4a/3=(345,75) -->
  <path d="M 65,170 C 90,115 110,75 135,75 C 185,75 230,170 275,170 C 305,170 328,118 345,75 C 354,52 360,35 365,20" fill="none" stroke="#1565c0" stroke-width="2.4"/>
  <!-- Equal height horizontal line -->
  <line x1="65" y1="75" x2="345" y2="75" stroke="#d32f2f" stroke-width="1.2" stroke-dasharray="4,3"/>
  <line x1="135" y1="75" x2="135" y2="170" stroke="#888" stroke-dasharray="3,3"/>
  <line x1="345" y1="75" x2="345" y2="170" stroke="#888" stroke-dasharray="3,3"/>
  <circle cx="135" cy="75" r="4" fill="#d32f2f"/>
  <circle cx="275" cy="170" r="3.5" fill="#1565c0"/>
  <circle cx="345" cy="75" r="4" fill="#d32f2f"/>
  <text x="126" y="186" font-size="12" fill="#333">a/3</text>
  <text x="271" y="186" font-size="12" fill="#333">a</text>
  <text x="332" y="186" font-size="12" fill="#333">4a/3</text>
  <text x="14" y="79" font-size="11" fill="#d32f2f">4a³/27</text>
  <!-- Region annotations for x=1 -->
  <text x="72" y="208" font-size="10.5" fill="#2e7d32">① 1 ≤ a/3 → f(1)</text>
  <text x="172" y="208" font-size="10.5" fill="#d32f2f">② a/3 &lt; 1 &lt; 4a/3 → f(a/3)</text>
  <text x="312" y="208" font-size="10.5" fill="#2e7d32">③ 1 ≥ 4a/3 → f(1)</text>
</svg>

- **【分步标准解答】**
  1. 微分して増減を調べる：
     $$f'(x) = 3x^2 - 4ax + a^2 = (3x - a)(x - a)$$
     $a > 0$ より $0 < \dfrac{a}{3} < a$ である。$x \ge 0$ における増減表は次の通り：

     | $x$ | $0$ | $\cdots$ | $\dfrac{a}{3}$ | $\cdots$ | $a$ | $\cdots$ |
     | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
     | $f'(x)$ |  | $+$ | $0$ | $-$ | $0$ | $+$ |
     | $f(x)$ | $0$ | $\nearrow$ | $\dfrac{4}{27}a^3$（極大） | $\searrow$ | $0$（極小） | $\nearrow$ |

     （ここで $f(x) = x(x-a)^2$ より $f\left(\dfrac{a}{3}\right) = \dfrac{a}{3}\left(-\dfrac{2a}{3}\right)^2 = \dfrac{4}{27}a^3$。）
  2. **極大値と同じ高さになる右側の点**を求める：
     $$f(x) - f\left(\frac{a}{3}\right) = x^3 - 2ax^2 + a^2 x - \frac{4}{27}a^3 = \left(x - \frac{a}{3}\right)^2 \left(x - \frac{4}{3}a\right) = 0$$
     よって $x = \dfrac{4}{3}a$ のとき $f\left(\dfrac{4}{3}a\right) = \dfrac{4}{27}a^3$ となる。
     > 💡 讲师批注：**三次函数黄金比例性质**：极大值点 $x=\frac{a}{3}$、极小值点 $x=a$、与极大值等高的右侧点 $x=\frac{4}{3}a$，两段水平距离之比恒为 $2 : 1$（即 $\left(a - \frac{a}{3}\right) : \left(\frac{4}{3}a - a\right) = \frac{2}{3}a : \frac{1}{3}a = 2:1$），秒杀因式分解！
  3. 区間 $0 \le x \le 1$ の右端点 $x = 1$ の位置によって場合分けする（なお $f(1) = 1 - 2a + a^2 = (a - 1)^2$）：
     - **(i) $1 \le \dfrac{a}{3}$ すなわち $a \ge 3$ のとき**：
       区間 $[0, 1]$ で単調増加。よって $x = 1$ で最大値 $M(a) = f(1) = a^2 - 2a + 1$。
     - **(ii) $\dfrac{a}{3} < 1 < \dfrac{4}{3}a$ すなわち $\dfrac{3}{4} < a < 3$ のとき**：
       $x = \dfrac{a}{3}$ が区間内にあり、かつ $f(1) < f\left(\dfrac{a}{3}\right)$。よって $x = \dfrac{a}{3}$ で最大値 $M(a) = \dfrac{4}{27}a^3$。
     - **(iii) $1 \ge \dfrac{4}{3}a$ すなわち $0 < a \le \dfrac{3}{4}$ のとき**：
       $f(1) \ge f\left(\dfrac{a}{3}\right)$ となるため、$x = 1$ で最大値 $M(a) = f(1) = a^2 - 2a + 1$。
     > 💡 讲师批注：边界连续性验算：$a = \frac{3}{4}$ 时 $(a-1)^2 = \frac{1}{16} = \frac{4}{27}(\frac{3}{4})^3$；$a = 3$ 时 $(a-1)^2 = 4 = \frac{4}{27}\cdot 27$。两处边界无缝衔接，100% 正确！
- **【最终答案】**
  **$$M(a) = \begin{cases} a^2 - 2a + 1 & \left(0 < a \le \dfrac{3}{4},\; a \ge 3\right) \\[6pt] \dfrac{4}{27}a^3 & \left(\dfrac{3}{4} < a < 3\right) \end{cases}$$**

---

### 演習問題 10 (16)

- **【原题重现与翻译】**
  - 原题：$f(x) = x^3 - 6x^2 + 9x$ とする。区間 $a \le x \le a + 1$ における $f(x)$ の最大値 $M(a)$ を求めよ。
  - 中文：设 $f(x) = x^3 - 6x^2 + 9x$，求函数在区间 $a \le x \le a + 1$ 上的最大值 $M(a)$。
- **【考点定位】**
  - **定函数、动区间（滑动窗口）**在三次函数上的最大值分类讨论（关键：极小值点在窗口内时比较两端的函数值 $f(a)$ 与 $f(a+1)$）。
- **【图解辅助（SVG 矢量图）】**

<svg viewBox="0 0 430 225" xmlns="http://www.w3.org/2000/svg" style="max-width:430px;display:block;margin:10px auto;background:#fafafa;border:1px solid #e0e0e0;border-radius:6px;">
  <defs>
    <marker id="arr16" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0,0 L0,6 L6,3 z" fill="#333"/></marker>
  </defs>
  <!-- O=(65,165), x scale 70px/unit: 1->135, 3->275, 4->345; y=4 -> 60 -->
  <line x1="25" y1="165" x2="405" y2="165" stroke="#333" stroke-width="1.4" marker-end="url(#arr16)"/>
  <line x1="65" y1="205" x2="65" y2="18" stroke="#333" stroke-width="1.4" marker-end="url(#arr16)"/>
  <text x="408" y="169" font-size="12" font-style="italic" fill="#333">x</text>
  <text x="71" y="24" font-size="12" font-style="italic" fill="#333">y</text>
  <text x="52" y="180" font-size="12" fill="#333">O</text>
  <!-- Curve y=x(x-3)^2 -->
  <path d="M 48,205 C 55,188 60,176 65,165 C 90,108 110,60 135,60 C 185,60 230,165 275,165 C 305,165 328,108 345,60 C 352,40 356,28 360,18" fill="none" stroke="#1565c0" stroke-width="2.4"/>
  <!-- Highlight equal height window [a0, a0+1] around x=3: a0 ≈ 2.46 -> X=237, a0+1=3.46 -> X=307 -->
  <rect x="237" y="142" width="70" height="23" fill="#ff9800" fill-opacity="0.22" stroke="#ef6c00" stroke-width="1.2"/>
  <line x1="237" y1="142" x2="307" y2="142" stroke="#ef6c00" stroke-width="1.4" stroke-dasharray="3,2"/>
  <circle cx="135" cy="60" r="4" fill="#d32f2f"/>
  <circle cx="275" cy="165" r="3.5" fill="#1565c0"/>
  <circle cx="237" cy="142" r="3.5" fill="#ef6c00"/>
  <circle cx="307" cy="142" r="3.5" fill="#ef6c00"/>
  <line x1="135" y1="60" x2="135" y2="165" stroke="#888" stroke-dasharray="3,3"/>
  <text x="131" y="180" font-size="12" fill="#333">1</text>
  <text x="271" y="180" font-size="12" fill="#333">3</text>
  <text x="341" y="180" font-size="12" fill="#333">4</text>
  <text x="115" y="48" font-size="11.5" fill="#d32f2f" font-weight="bold">極大 (1, 4)</text>
  <text x="218" y="132" font-size="10.5" fill="#ef6c00" font-weight="bold">f(a)=f(a+1) の境目</text>
  <text x="180" y="205" font-size="11" fill="#ef6c00">a = (9+√33)/6 ≈ 2.46</text>
</svg>

- **【分步标准解答】**
  1. 微分して全体の増減を調べる：
     $$f'(x) = 3x^2 - 12x + 9 = 3(x - 1)(x - 3)$$
     $x \le 1$ で増加、$1 \le x \le 3$ で減少、$x \ge 3$ で増加。
     - 極大値：$f(1) = 4$；極小値：$f(3) = 0$。
  2. 区間 $[a,\; a + 1]$（幅 $1$）の位置で場合分けする（なお $f(a+1) = (a+1)(a-2)^2 = a^3 - 3a^2 + 4$）：
     - **(i) $a + 1 < 1$ すなわち $a < 0$ のとき**：
       区間は $(-\infty, 1)$ 内にあり単調増加。最大値は $f(a + 1) = a^3 - 3a^2 + 4$。
     - **(ii) $a \le 1 \le a + 1$ すなわち $0 \le a \le 1$ のとき**：
       極大点 $x = 1$ が区間内に含まれる。また右端点 $a + 1 \le 2 < 3$ より、$x = 1$ で最大値 $f(1) = 4$。
     - **(iii) $1 < a$ かつ $a + 1 \le 3$ すなわち $1 < a \le 2$ のとき**：
       区間は $[1, 3]$ 内にあり単調減少。最大値は左端点の $f(a) = a^3 - 6a^2 + 9a$。
     - **(iv) $2 < a < 3$ のとき（極小点 $x = 3$ が区間内に入る）**：
       最大値は $f(a)$ と $f(a + 1)$ の大きい方となるため、その差を調べる：
       $$f(a + 1) - f(a) = (a^3 - 3a^2 + 4) - (a^3 - 6a^2 + 9a) = 3a^2 - 9a + 4$$
       $3a^2 - 9a + 4 = 0$ を解くと $a = \dfrac{9 \pm \sqrt{81 - 48}}{6} = \dfrac{9 \pm \sqrt{33}}{6}$。
       ここで $5 < \sqrt{33} < 6$ より：
       $$\frac{9 - \sqrt{33}}{6} < 1, \qquad 2 < \frac{9 + \sqrt{33}}{6} < 3$$
       > 💡 讲师批注：精确估值检验：$5.7^2 = 32.49 < 33 < 33.64 = 5.8^2$，故 $\frac{9+\sqrt{33}}{6} \approx \frac{14.74}{6} \approx 2.46$，稳稳落在 $(2, 3)$ 内！
       よって $2 < a < 3$ において：
       - $2 < a < \dfrac{9 + \sqrt{33}}{6}$ のとき $f(a+1) < f(a) \implies$ 最大値は $f(a) = a^3 - 6a^2 + 9a$；
       - $\dfrac{9 + \sqrt{33}}{6} \le a < 3$ のとき $f(a+1) \ge f(a) \implies$ 最大値は $f(a+1) = a^3 - 3a^2 + 4$。
     - **(v) $a \ge 3$ のとき**：
       区間は $[3, \infty)$ 内にあり単調増加。最大値は $f(a + 1) = a^3 - 3a^2 + 4$。
  3. 同じ式となる範囲を統合してまとめる。
- **【最终答案】**
  **$$M(a) = \begin{cases} a^3 - 3a^2 + 4 & \left(a < 0,\; a \ge \dfrac{9 + \sqrt{33}}{6}\right) \\[6pt] 4 & (0 \le a \le 1) \\[4pt] a^3 - 6a^2 + 9a & \left(1 < a < \dfrac{9 + \sqrt{33}}{6}\right) \end{cases}$$**

---

### 演習問題 10 (17)

- **【原题重现与翻译】**
  - 原题：$0 \le x < 2\pi$ のとき、関数 $y = 2\sin x \sin 2x - \cos x + 2$ の最大値と最小値、及びそのときの $x$ の値を求めよ。
  - 中文：当 $0 \le x < 2\pi$ 时，求函数 $y = 2\sin x \sin 2x - \cos x + 2$ 的最大值、最小值及对应的 $x$ 值。
- **【考点定位】**
  - 三角函数化为关于 $\cos x$ 的三次多项式（换元法 $t = \cos x$ + 闭区间 $[-1, 1]$ 最值）。
- **【分步标准解答】**
  1. 2 倍角の公式 $\sin 2x = 2\sin x \cos x$ と $\sin^2 x = 1 - \cos^2 x$ を用いて $\cos x$ のみの式に直す：
     $$\begin{aligned}
     y &= 2\sin x (2\sin x \cos x) - \cos x + 2 \\
       &= 4\sin^2 x \cos x - \cos x + 2 \\
       &= 4(1 - \cos^2 x)\cos x - \cos x + 2 \\
       &= -4\cos^3 x + 3\cos x + 2
     \end{aligned}$$
  2. $t = \cos x$ とおくと、$0 \le x < 2\pi$ より $t$ の変域は $-1 \le t \le 1$ である。
     $g(t) = -4t^3 + 3t + 2$（$-1 \le t \le 1$）とおき、微分する：
     $$g'(t) = -12t^2 + 3 = -3(4t^2 - 1) = -3(2t + 1)(2t - 1)$$
  3. $g'(t) = 0 \implies t = -\dfrac{1}{2},\; \dfrac{1}{2}$。増減表をかく：

     | $t$ | $-1$ | $\cdots$ | $-\dfrac{1}{2}$ | $\cdots$ | $\dfrac{1}{2}$ | $\cdots$ | $1$ |
     | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
     | $g'(t)$ |  | $-$ | $0$ | $+$ | $0$ | $-$ |  |
     | $g(t)$ | $3$ | $\searrow$ | $1$ | $\nearrow$ | $3$ | $\searrow$ | $1$ |

     > 💡 讲师批注：注意最大值 $3$ 在 $t=-1$ 与 $t=\frac{1}{2}$ **两处同时取得**，最小值 $1$ 在 $t=-\frac{1}{2}$ 与 $t=1$ **两处同时取得**！千万别漏写任何一处对应的 $x$！
  4. $0 \le x < 2\pi$ における各 $t$ に対応する $x$ の値を求める：
     - 最大値 $3$：$t = \cos x = -1 \implies x = \pi$；$t = \cos x = \dfrac{1}{2} \implies x = \dfrac{\pi}{3},\; \dfrac{5\pi}{3}$。
     - 最小値 $1$：$t = \cos x = 1 \implies x = 0$；$t = \cos x = -\dfrac{1}{2} \implies x = \dfrac{2\pi}{3},\; \dfrac{4\pi}{3}$。
     > 💡 讲师批注：**神级验算法（三倍角公式）**：一眼看出 $-4\cos^3 x + 3\cos x = -\cos 3x$！原函数就是 $y = 2 - \cos 3x$（$0 \le 3x < 6\pi$）！最大值 $3$ 当 $\cos 3x = -1 \iff 3x = \pi, 3\pi, 5\pi$；最小值 $1$ 当 $\cos 3x = 1 \iff 3x = 0, 2\pi, 4\pi$。与换元求导的结果分毫不差！
- **【最终答案】**
  - **最大値：$3$（$x = \dfrac{\pi}{3},\; \pi,\; \dfrac{5\pi}{3}$ のとき）**
  - **最小値：$1$（$x = 0,\; \dfrac{2\pi}{3},\; \dfrac{4\pi}{3}$ のとき）**

---

### 演習問題 10 (18)

- **【原题重现与翻译】**
  - 原题：関数 $y = 8^x - 3\cdot 2^x$ の最小値と、その時の $x$ の値を求めよ。
  - 中文：求函数 $y = 8^x - 3\cdot 2^x$ 的最小值，以及取得最小值时的 $x$ 值。
- **【考点定位】**
  - 指数函数换元（$t = 2^x > 0$）转化为开区间上的三次函数求最小值。
- **【分步标准解答】**
  1. $t = 2^x$ とおくと、すべての実数 $x$ に対して $t > 0$ である。また $8^x = (2^3)^x = (2^x)^3 = t^3$ より：
     $$y = t^3 - 3t \qquad (t > 0)$$
  2. $g(t) = t^3 - 3t$（$t > 0$）とおき、微分する：
     $$g'(t) = 3t^2 - 3 = 3(t + 1)(t - 1)$$
  3. $t > 0$ の範囲で $g'(t) = 0 \implies t = 1$。増減表（$t > 0$）：

     | $t$ | $(0)$ | $\cdots$ | $1$ | $\cdots$ |
     | :---: | :---: | :---: | :---: | :---: |
     | $g'(t)$ |  | $-$ | $0$ | $+$ |
     | $g(t)$ |  | $\searrow$ | $-2$（極小） | $\nearrow$ |

     > 💡 讲师批注：在开区间 $t > 0$ 上，先减后增且只有一个极小值点 $t=1$，故极小值即全局最小值。
  4. よって $t = 1$ すなわち $2^x = 1 \implies x = 0$ のとき、最小値 $-2$ をとる。
- **【最终答案】**
  **最小値：$-2$（$x = 0$ のとき）**

---

### 演習問題 10 (19)

- **【原题重现与翻译】**
  - 原题：関数 $y = \log_3 x + 2\log_3(6 - x)$ の最大値と、その時の $x$ の値を求めよ。
  - 中文：求函数 $y = \log_3 x + 2\log_3(6 - x)$ 的最大值，以及取得最大值时的 $x$ 值。
- **【考点定位】**
  - 对数函数真数条件（定义域）+ 对数运算性质 + 三次函数求最大值。
- **【分步标准解答】**
  1. **真数条件**より $x > 0$ かつ $6 - x > 0 \implies 0 < x < 6$。
     > 💡 讲师批注：任何对数函数题，**第一步必须写真数条件**，确定 $x$ 的取值范围！
  2. 対数の性質より変形する：
     $$y = \log_3 x + \log_3(6 - x)^2 = \log_3 \{x(6 - x)^2\}$$
  3. 底 $3 > 1$ より対数関数 $\log_3 u$ は単調増加であるから、真数 $g(x) = x(6 - x)^2$（$0 < x < 6$）が最大となるとき $y$ も最大となる。
  4. $g(x) = x(36 - 12x + x^2) = x^3 - 12x^2 + 36x$ を微分する：
     $$g'(x) = 3x^2 - 24x + 36 = 3(x^2 - 8x + 12) = 3(x - 2)(x - 6)$$
  5. $0 < x < 6$ において $g'(x) = 0 \implies x = 2$。増減表：

     | $x$ | $(0)$ | $\cdots$ | $2$ | $\cdots$ | $(6)$ |
     | :---: | :---: | :---: | :---: | :---: | :---: |
     | $g'(x)$ |  | $+$ | $0$ | $-$ |  |
     | $g(x)$ |  | $\nearrow$ | $32$（極大） | $\searrow$ |  |

     （ここで $g(2) = 2 \cdot (6 - 2)^2 = 2 \cdot 16 = 32$。）
  6. したがって $x = 2$ のとき $y$ は最大値 $\log_3 32 = \log_3 2^5 = 5\log_3 2$ をとる。
     > 💡 讲师批注：三元均值不等式秒验：$2x \cdot (6-x) \cdot (6-x) \le \left(\frac{2x + (6-x) + (6-x)}{3}\right)^3 = 4^3 = 64 \implies x(6-x)^2 \le 32$，当 $2x = 6-x \iff x=2$ 时取等，完全吻合！
- **【最终答案】**
  **最大値：$5\log_3 2$（或 $\log_3 32$，$x = 2$ のとき）**

---

### 演習問題 10 (20)

- **【原题重现与翻译】**
  - 原题：$0 < a < 3$ とする。関数 $f(x) = 2x^3 - 3ax^2 + b$（$0 \le x \le 3$）の最大値が $10$、最小値が $-18$ のとき、定数 $a, b$ の値を求めよ。
  - 中文：设 $0 < a < 3$。当函数 $f(x) = 2x^3 - 3ax^2 + b$（$0 \le x \le 3$）的最大值为 $10$、最小值为 $-18$ 时，求常数 $a, b$ 的值。
- **【考点定位】**
  - 含双参数三次函数闭区间最值反求参数（需按两端点大小关系分类讨论，并**严格检验参数范围**）。
- **【分步标准解答】**
  1. 微分する：
     $$f'(x) = 6x^2 - 6ax = 6x(x - a)$$
  2. $0 < a < 3$ より、区間 $0 \le x \le 3$ における増減表は次の通り：

     | $x$ | $0$ | $\cdots$ | $a$ | $\cdots$ | $3$ |
     | :---: | :---: | :---: | :---: | :---: | :---: |
     | $f'(x)$ | $0$ | $-$ | $0$ | $+$ |  |
     | $f(x)$ | $b$ | $\searrow$ | $-a^3 + b$ | $\nearrow$ | $54 - 27a + b$ |

  3. **最小値の条件**：増減表より最小値は必ず $x = a$ でとるため：
     $$f(a) = -a^3 + b = -18 \implies b = a^3 - 18 \quad \cdots\text{①}$$
  4. **最大値の条件**：最大値は $f(0) = b$ または $f(3) = 54 - 27a + b$ の大きい方である。
     両者の差を調べると：
     $$f(3) - f(0) = 54 - 27a = 27(2 - a)$$
     よって $a = 2$ を境に場合分けする：
     - **場合 1：$0 < a \le 2$ のとき**（$f(3) \ge f(0)$ より最大値は $f(3)$）
       $$f(3) = 54 - 27a + b = 10 \quad \cdots\text{②}$$
       ① を ② に代入すると：
       $$54 - 27a + (a^3 - 18) = 10 \implies a^3 - 27a + 26 = 0$$
       $a = 1$ が解であることから因数分解すると：
       $$(a - 1)(a^2 + a - 26) = 0 \implies a = 1,\quad \frac{-1 \pm \sqrt{105}}{2}$$
       ここで $10 < \sqrt{105} < 11$ より $\dfrac{-1 + \sqrt{105}}{2} > 4.5$、$\dfrac{-1 - \sqrt{105}}{2} < 0$ であり、いずれも $0 < a \le 2$ を満たさない。
       よって $a = 1$。① より $b = 1^3 - 18 = -17$。
     - **場合 2：$2 < a < 3$ のとき**（$f(0) > f(3)$ より最大値は $f(0)$）
       $$f(0) = b = 10$$
       これを ① に代入すると $-a^3 + 10 = -18 \implies a^3 = 28$。
       ところが $2 < a < 3 \iff 8 < a^3 < 27$ であるため、$a^3 = 28$ は **$2 < a < 3$ を満たさない（不適）**！
       > 💡 讲师批注：**极易中招的隐蔽陷阱！** $28$ 仅仅比 $3^3 = 27$ 大 $1$，如果心算粗心把 $\sqrt[3]{28}$ 当成小于 $3$，就会多出一个错解 $(a=\sqrt[3]{28}, b=10)$！务必比较立方数 $28 > 27$！
  5. 以上より、求める定数は $a = 1,\; b = -17$。
- **【最终答案】**
  **$a = 1,\quad b = -17$**

---

### 演習問題 10 (21)

- **【原题重现与翻译】**
  - 原题：すべての正の数 $x$ に対して、不等式 $kx^2 \ge \log x$ が成り立つような定数 $k$ のうちで最小のものを求めよ。
  - 中文：求满足「对所有正数 $x$，不等式 $kx^2 \ge \log x$ 恒成立」的常数 $k$ 中的最小值。（注：$\log x$ 为自然对数 $\ln x$。）
- **【考点定位】**
  - 参数分离法（定数分離）+ 利用导数求对数分式函数的最大值。
- **【图解辅助（SVG 矢量图）】**

<svg viewBox="0 0 380 210" xmlns="http://www.w3.org/2000/svg" style="max-width:380px;display:block;margin:10px auto;background:#fafafa;border:1px solid #e0e0e0;border-radius:6px;">
  <defs>
    <marker id="arr21" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0,0 L0,6 L6,3 z" fill="#333"/></marker>
  </defs>
  <!-- O=(65, 130), x=1->(125,130), x=sqrt(e)≈1.65->(165,65) max 1/(2e) -->
  <line x1="30" y1="130" x2="360" y2="130" stroke="#333" stroke-width="1.4" marker-end="url(#arr21)"/>
  <line x1="65" y1="195" x2="65" y2="18" stroke="#333" stroke-width="1.4" marker-end="url(#arr21)"/>
  <text x="363" y="134" font-size="12" font-style="italic" fill="#333">x</text>
  <text x="71" y="24" font-size="12" font-style="italic" fill="#333">y</text>
  <text x="52" y="145" font-size="12" fill="#333">O</text>
  <!-- Curve y = (log x)/x^2 -->
  <path d="M 92,195 C 102,165 112,145 125,130 C 138,100 148,65 165,65 C 195,65 240,108 350,124" fill="none" stroke="#1565c0" stroke-width="2.4"/>
  <!-- Line y = k >= 1/(2e) -->
  <line x1="65" y1="65" x2="355" y2="65" stroke="#d32f2f" stroke-width="1.6" stroke-dasharray="5,3"/>
  <line x1="165" y1="65" x2="165" y2="130" stroke="#888" stroke-dasharray="3,3"/>
  <circle cx="165" cy="65" r="4" fill="#d32f2f"/>
  <circle cx="125" cy="130" r="3" fill="#1565c0"/>
  <text x="121" y="146" font-size="12" fill="#333">1</text>
  <text x="155" y="146" font-size="12" fill="#333">√e</text>
  <text x="30" y="69" font-size="11.5" fill="#d32f2f" font-weight="bold">1/(2e)</text>
  <text x="225" y="55" font-size="11.5" fill="#d32f2f" font-weight="bold">y = k（最小値 k = 1/(2e)）</text>
  <text x="235" y="102" font-size="11.5" fill="#1565c0">y = (log x) / x²</text>
</svg>

- **【分步标准解答】**
  1. $x > 0$ より $x^2 > 0$ であるから、与えられた不等式の両辺を $x^2$ で割って定数 $k$ を分離する：
     $$kx^2 \ge \log x \iff k \ge \frac{\log x}{x^2}$$
     > 💡 讲师批注：不等式恒成立求参数最值，首选**参变分离（定数分離）**！由于 $x^2 > 0$，直接除过去不用讨论符号。
  2. $f(x) = \dfrac{\log x}{x^2}$（$x > 0$）とおき、商の微分法により微分する：
     $$f'(x) = \frac{\dfrac{1}{x} \cdot x^2 - (\log x) \cdot 2x}{x^4} = \frac{x(1 - 2\log x)}{x^4} = \frac{1 - 2\log x}{x^3}$$
  3. $x > 0$ において $f'(x) = 0$ を解くと：
     $$1 - 2\log x = 0 \implies \log x = \frac{1}{2} \implies x = e^{\frac{1}{2}} = \sqrt{e}$$
  4. $x > 0$ における増減表：

     | $x$ | $(0)$ | $\cdots$ | $\sqrt{e}$ | $\cdots$ |
     | :---: | :---: | :---: | :---: | :---: |
     | $f'(x)$ |  | $+$ | $0$ | $-$ |
     | $f(x)$ |  | $\nearrow$ | $\dfrac{1}{2e}$（極大） | $\searrow$ |

     （ここで $f(\sqrt{e}) = \dfrac{\log e^{\frac{1}{2}}}{(\sqrt{e})^2} = \dfrac{\frac{1}{2}}{e} = \dfrac{1}{2e}$。）
  5. 増減表より、$f(x)$ は $x = \sqrt{e}$ で最大値 $\dfrac{1}{2e}$ をとる。
     したがって、すべての $x > 0$ で $k \ge f(x)$ が成り立つための必要十分条件は $k \ge \dfrac{1}{2e}$ であり、最小の定数 $k$ は $\dfrac{1}{2e}$ である。
- **【最终答案】**
  **$k = \dfrac{1}{2e}$**

---

### 演習問題 11 (1)

- **【原题重现与翻译】**
  - 原题：曲線 $y = \dfrac{x}{x^2 + 1}$ の凹凸を調べ、変曲点を求めよ。
  - 中文：讨论曲线 $y = \dfrac{x}{x^2 + 1}$ 的凹凸性，并求其拐点（变曲点）。
- **【考点定位】**
  - 数学Ⅲ核心：二阶导数 $y''$ 的计算、凹凸性区间判定与変曲点（拐点）坐标求解。
- **【图解辅助（SVG 矢量图）】**

<svg viewBox="0 0 430 230" xmlns="http://www.w3.org/2000/svg" style="max-width:430px;display:block;margin:10px auto;background:#fafafa;border:1px solid #e0e0e0;border-radius:6px;">
  <defs>
    <marker id="arr11" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0,0 L0,6 L6,3 z" fill="#333"/></marker>
  </defs>
  <!-- O=(215, 115), x scale 55px/unit: ±1 -> ±55, ±sqrt3(1.73) -> ±95; y scale 130px/unit: ±0.5 -> ±65, ±sqrt3/4(0.433) -> ±56 -->
  <line x1="25" y1="115" x2="405" y2="115" stroke="#333" stroke-width="1.4" marker-end="url(#arr11)"/>
  <line x1="215" y1="215" x2="215" y2="18" stroke="#333" stroke-width="1.4" marker-end="url(#arr11)"/>
  <text x="408" y="119" font-size="12" font-style="italic" fill="#333">x</text>
  <text x="221" y="24" font-size="12" font-style="italic" fill="#333">y</text>
  <!-- Curve y = x/(x^2+1): odd function -->
  <path d="M 35,134 C 75,142 100,160 120,171 C 138,180 150,180 160,180 C 180,180 198,145 215,115 C 232,85 250,50 270,50 C 280,50 292,50 310,59 C 330,70 355,88 395,96" fill="none" stroke="#1565c0" stroke-width="2.5"/>
  <!-- Inflection points: (-sqrt3, -sqrt3/4)->(120,171), (0,0)->(215,115), (sqrt3, sqrt3/4)->(310,59) -->
  <line x1="120" y1="115" x2="120" y2="171" stroke="#888" stroke-dasharray="3,3"/>
  <line x1="310" y1="59" x2="310" y2="115" stroke="#888" stroke-dasharray="3,3"/>
  <circle cx="120" cy="171" r="4.5" fill="#d32f2f"/>
  <circle cx="215" cy="115" r="4.5" fill="#d32f2f"/>
  <circle cx="310" cy="59" r="4.5" fill="#d32f2f"/>
  <text x="106" y="106" font-size="11.5" fill="#333">-√3</text>
  <text x="303" y="130" font-size="11.5" fill="#333">√3</text>
  <text x="222" y="130" font-size="11.5" fill="#d32f2f" font-weight="bold">O(0,0)</text>
  <text x="296" y="46" font-size="11" fill="#d32f2f" font-weight="bold">変曲点 (√3, √3/4)</text>
  <text x="36" y="190" font-size="11" fill="#d32f2f" font-weight="bold">変曲点 (-√3, -√3/4)</text>
  <!-- Concavity labels -->
  <text x="40" y="156" font-size="10.5" fill="#2e7d32">上に凸</text>
  <text x="150" y="198" font-size="10.5" fill="#1565c0">下に凸</text>
  <text x="242" y="40" font-size="10.5" fill="#2e7d32">上に凸</text>
  <text x="342" y="78" font-size="10.5" fill="#1565c0">下に凸</text>
</svg>

- **【分步标准解答】**
  1. 第 1 次導関数 $y'$ を求める（定義域はすべての実数）：
     $$y' = \frac{1\cdot(x^2 + 1) - x \cdot 2x}{(x^2 + 1)^2} = \frac{1 - x^2}{(x^2 + 1)^2}$$
  2. さらに微分して第 2 次導関数 $y''$ を求める：
     $$\begin{aligned}
     y'' &= \frac{(-2x)(x^2 + 1)^2 - (1 - x^2) \cdot 2(x^2 + 1) \cdot 2x}{(x^2 + 1)^4} \\
         &= \frac{-2x(x^2 + 1) - 4x(1 - x^2)}{(x^2 + 1)^3} \\
         &= \frac{-2x^3 - 2x - 4x + 4x^3}{(x^2 + 1)^3} \\
         &= \frac{2x^3 - 6x}{(x^2 + 1)^3} = \frac{2x(x + \sqrt{3})(x - \sqrt{3})}{(x^2 + 1)^3}
     \end{aligned}$$
     > 💡 讲师批注：求二阶导数时，**先约掉分子分母的公因式 $(x^2+1)$** 再展开分子，千万不要傻傻展开 $(x^2+1)^2$，能省一半计算量且极难出错！
  3. すべての実数 $x$ で $(x^2 + 1)^3 > 0$ であるから、$y'' = 0$ の解は $x = -\sqrt{3},\; 0,\; \sqrt{3}$。
     各点における $y$ の値を求める：
     - $x = -\sqrt{3}$ のとき：$y = \dfrac{-\sqrt{3}}{3 + 1} = -\dfrac{\sqrt{3}}{4}$
     - $x = 0$ のとき：$y = 0$
     - $x = \sqrt{3}$ のとき：$y = \dfrac{\sqrt{3}}{3 + 1} = \dfrac{\sqrt{3}}{4}$
  4. $y''$ の符号表（凹凸表）：

     | $x$ | $\cdots$ | $-\sqrt{3}$ | $\cdots$ | $0$ | $\cdots$ | $\sqrt{3}$ | $\cdots$ |
     | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
     | $y''$ | $-$ | $0$ | $+$ | $0$ | $-$ | $0$ | $+$ |
     | $y$ の凹凸 | 上に凸 | 変曲点 | 下に凸 | 変曲点 | 上に凸 | 変曲点 | 下に凸 |

     > 💡 讲师批注：三个零点前后 $y''$ 均发生变号，故全部为変曲点！且原函数是奇函数（$f(-x)=-f(x)$），因此三个拐点关于原点对称，完美自检！
- **【最终答案】**
  - **凹凸**：
    - **$-\sqrt{3} < x < 0,\; x > \sqrt{3}$ で下に凸（下凸）**
    - **$x < -\sqrt{3},\; 0 < x < \sqrt{3}$ で上に凸（上凸）**
  - **変曲点**：**$\left(-\sqrt{3},\; -\dfrac{\sqrt{3}}{4}\right),\quad (0,\; 0),\quad \left(\sqrt{3},\; \dfrac{\sqrt{3}}{4}\right)$**
