# 《EJU 教材全解与备课讲义》数学 003（下：P38–P45）

> **对应源文件**：`work_math/ocr_md/ocr_003_p31-45.md`（承接 [`note_003_a.md`](note_003_a.md)，本篇覆盖 P38–P45：**数学 A《整数の性質》**之「ユークリッドの互除法と 1 次不定方程式」「分数と小数、$n$ 進法」逐题深度解析）
> **视觉核对参考图**：`work_math/ref_imgs/page_0038.jpg` – `page_0045.jpg`

---

## 本篇核心图解回顾（欧几里得互除法的几何直观与日式笔算）

参考原教材第 40 页（`page_0040.jpg`，教材页码 39），用「$270 \times 396$ 长方形剪最大正方形铺满」直观理解为何 $\gcd(396, 270) = \gcd(270, 126) = \gcd(126, 18) = 18$：

<svg viewBox="0 0 600 215" width="600" height="215" xmlns="http://www.w3.org/2000/svg" style="background:#fafafa;border:1px solid #e0e0e0;border-radius:6px;">
  <style>
    .t { font: bold 13px sans-serif; fill: #2c3e50; }
    .sub { font: 11px sans-serif; fill: #555; }
    .num { font: bold 11px monospace; fill: #2c3e50; text-anchor: middle; }
    .sq1 { fill: #d6eaf8; stroke: #2980b9; stroke-width: 1.5; }
    .sq2 { fill: #d5f5e3; stroke: #27ae60; stroke-width: 1.5; }
    .sq3 { fill: #fdebd0; stroke: #e67e22; stroke-width: 1.4; }
    .rem { fill: #fadbd8; stroke: #c0392b; stroke-width: 1.5; }
  </style>
  <text x="16" y="22" class="t">ユークリッドの互除法の幾何学的意味（縦 270 × 横 396 の長方形の敷き詰め）</text>
  <!-- Main rectangle 396 x 270 scaled by 0.52 -> 206 x 140 -->
  <g transform="translate(24, 48)">
    <!-- 270x270 square: 140 x 140 -->
    <rect x="0" y="0" width="140" height="140" class="sq1"/>
    <text x="70" y="74" class="num">270 × 270</text>
    <text x="70" y="90" class="sub" text-anchor="middle">① 1個切り取る</text>
    <!-- Remaining 126x270: 66 x 140 -->
    <!-- Two 126x126 squares: 66 x 66 each -->
    <rect x="140" y="0" width="66" height="66" class="sq2"/>
    <text x="173" y="37" class="num">126×126</text>
    <rect x="140" y="66" width="66" height="66" class="sq2"/>
    <text x="173" y="103" class="num">126×126</text>
    <!-- Remaining 126x18 strip: 66 x 8 -->
    <rect x="140" y="132" width="66" height="8" class="rem"/>
    <!-- Dimensions -->
    <text x="103" y="-8" class="num">横 396</text>
    <text x="-12" y="74" class="num" transform="rotate(-90,-12,74)">縦 270</text>
    <text x="70" y="156" class="sub" text-anchor="middle">270</text>
    <text x="173" y="156" class="sub" text-anchor="middle">126</text>
  </g>
  <!-- Arrow and zoomed strip -->
  <line x1="242" y1="184" x2="295" y2="184" stroke="#c0392b" stroke-width="1.5" stroke-dasharray="4,2"/>
  <text x="305" y="66" class="t" fill="#2980b9">① 396 = 270 × 1 + 126</text>
  <text x="320" y="84" class="sub">⇒ gcd(396, 270) = gcd(270, 126)</text>
  <text x="305" y="112" class="t" fill="#27ae60">② 270 = 126 × 2 + 18</text>
  <text x="320" y="130" class="sub">⇒ gcd(270, 126) = gcd(126, 18)</text>
  <text x="305" y="158" class="t" fill="#c0392b">③ 126 = 18 × 7 + 0（割り切れ！）</text>
  <text x="320" y="176" class="sub">⇒ 最大公約数 ＝ 18（18×18 が7個並ぶ）</text>
  <!-- 7 small squares -->
  <g transform="translate(305, 184)">
    <rect x="0" y="0" width="18" height="18" class="sq3"/>
    <rect x="18" y="0" width="18" height="18" class="sq3"/>
    <rect x="36" y="0" width="18" height="18" class="sq3"/>
    <rect x="54" y="0" width="18" height="18" class="sq3"/>
    <rect x="72" y="0" width="18" height="18" class="sq3"/>
    <rect x="90" y="0" width="18" height="18" class="sq3"/>
    <rect x="108" y="0" width="18" height="18" class="sq3"/>
    <text x="136" y="13" class="sub">18 × 126（7個ぴったり）</text>
  </g>
</svg>

---

## 三、逐题深度解析（下：演習問題 3 & 演習問題 4，不可跳步）

---

### 演習問題 3（ユークリッドの互除法と 1 次不定方程式）

#### 演習問題 3-(1)
- **【原题重现与翻译】**
  - 原题：次の 2 つの整数の最大公約数を、互除法を用いて求めよ。
    - `[1]` $323,\; 884$　　`[2]` $943,\; 1058$　　`[3]` $1829,\; 2077$
  - 中文：利用辗转相除法，求下列各组两个整数的最大公约数。
- **【考点定位】**
  - 欧几里得辗转相除法（ユークリッドの互除法）标准步骤。
- **【分步标准解答】**
  **`[1]` $323,\; 884$**
  $$884 = 323 \times 2 + 238$$
  $$323 = 238 \times 1 + 85$$
  $$238 = 85 \times 2 + 68$$
  $$85 = 68 \times 1 + 17$$
  $$68 = 17 \times 4 + 0$$
  > 💡 讲师批注：最后一次整除时的除数（即最后一个非零余数）为 $17$。反向验算：$323 = 17 \times 19$，$884 = 17 \times 52$，且 $19$ 与 $52$ 互素，100% 正确！

  よって、$323$ と $884$ の最大公約数は **$17$**。

  **`[2]` $943,\; 1058$**
  $$1058 = 943 \times 1 + 115$$
  $$943 = 115 \times 8 + 23$$
  $$115 = 23 \times 5 + 0$$
  > 💡 讲师批注：反向验算：$943 = 23 \times 41$，$1058 = 23 \times 46$，$41$ 与 $46$ 互素，仅需 3 步即得结果！

  よって、$943$ と $1058$ の最大公約数は **$23$**。

  **`[3]` $1829,\; 2077$**
  $$2077 = 1829 \times 1 + 248$$
  $$1829 = 248 \times 7 + 93$$
  $$248 = 93 \times 2 + 62$$
  $$93 = 62 \times 1 + 31$$
  $$62 = 31 \times 2 + 0$$
  > 💡 讲师批注：注意第 2 步计算 $248 \times 7 = 1736$，$1829 - 1736 = 93$。反向验算：$1829 = 31 \times 59$，$2077 = 31 \times 67$，$59$ 与 $67$ 均为素数，互素！若用试除法找 $31 \times 59$ 会非常痛苦，这正是互除法的威力所在。

  よって、$1829$ と $2077$ の最大公約数は **$31$**。
- **【最终答案】**
  **`[1]` $17$　　`[2]` $23$　　`[3]` $31$**

---

#### 演習問題 3-(2)
- **【原题重现与翻译】**
  - 原题：2 つの整数 $m, n$ の最大公約数と $3m + 4n,\; 2m + 3n$ の最大公約数は一致することを示せ。
  - 中文：证明：两个整数 $m, n$ 的最大公约数与 $3m+4n,\; 2m+3n$ 的最大公约数相等。
- **【考点定位】**
  - 互除法定理 $(a, b) = (b, r)$ 对含字母整式的灵活运用。
- **【分步标准解答】**
  2 つの整数 $a, b$ の最大公約数を $(a, b)$ と表す。$a = bq + r$ のとき $(a, b) = (b, r)$ が成り立つ（$r$ の符号・大小を問わない）ことを繰り返し用いる。
  1. $3m + 4n = (2m + 3n) \cdot 1 + (m + n)$ より、
     $$(3m + 4n,\; 2m + 3n) = (2m + 3n,\; m + n)$$
  2. $2m + 3n = (m + n) \cdot 2 + n$ より、
     $$(2m + 3n,\; m + n) = (m + n,\; n)$$
  3. $m + n = n \cdot 1 + m$ より、
     $$(m + n,\; n) = (n,\; m) = (m,\; n)$$
  > 💡 讲师批注：每一步都把系数变小（$3,4 \to 2,3 \to 1,1 \to 1,0$），就像给矩阵做初等行变换！从线性代数视角看，变换矩阵 $\begin{pmatrix} 3 & 4 \\ 2 & 3 \end{pmatrix}$ 的行列式为 $3 \times 3 - 4 \times 2 = 1$（幺模矩阵），因此 $m, n$ 也可反解为 $m = 3(3m+4n) - 4(2m+3n)$、$n = -2(3m+4n) + 3(2m+3n)$，故双向整除，最大公约数必然相等！

  以上より、$(3m + 4n,\; 2m + 3n) = (m,\; n)$ が成り立ち、両者の最大公約数は一致する。$\blacksquare$
- **【最终答案】**
  **証明完了（互除法の原理を 3 回適用し $(3m+4n, 2m+3n) = (m, n)$ を導出）**

---

#### 演習問題 3-(3)
- **【原题重现与翻译】**
  - 原题：$7n + 4$ と $8n + 5$ が互いに素になるような $100$ 以下の自然数 $n$ は全部でいくつあるか。
  - 中文：使 $7n+4$ 与 $8n+5$ 互素的不超过 $100$ 的自然数 $n$ 一共有多少个？
- **【考点定位】**
  - 互除法降维化简 $\gcd(8n+5, 7n+4)$ + 补集计数。
- **【分步标准解答】**
  2 つの整数 $a, b$ の最大公約数を $(a, b)$ と表す。互除法の原理を適用して $n$ を消去する。
  1. $8n + 5 = (7n + 4) \cdot 1 + (n + 1)$ より、
     $$(8n + 5,\; 7n + 4) = (7n + 4,\; n + 1)$$
  2. $7n + 4 = (n + 1) \cdot 7 - 3$（または $7(n+1) = (7n+4) \cdot 1 + 3$）より、
     $$(7n + 4,\; n + 1) = (n + 1,\; 3)$$
  > 💡 讲师批注：参考教材第 39 页（`page_0039.jpg`）明确说明：**使用定理 $(a, b) = (b, r)$ 时，不必拘泥于 $0 \le r < b$**！所以写出 $7n+4 = 7(n+1) - 3$ 后直接得出 $(7n+4, n+1) = (n+1, -3) = (n+1, 3)$，省去繁琐讨论！

  よって、$7n + 4$ と $8n + 5$ が互いに素であるための必要十分条件は、
  $$(n + 1,\; 3) = 1 \iff n + 1 \text{ が } 3 \text{ の倍数でないこと}$$
  である。
  $n$ は $1 \le n \le 100$ の自然数であるから、$2 \le n + 1 \le 101$ である。
  この範囲にある $3$ の倍数は、
  $$3 \times 1,\; 3 \times 2,\; \dots,\; 3 \times 33 \quad (\text{計 } 33 \text{ 個})$$
  である（$3 \times 33 = 99 \le 101 < 102 = 3 \times 34$）。
  > 💡 讲师批注：切勿漏看范围下界是 $2$（不是 $1$）！因为 $3 \times 1 = 3 \ge 2$，所以 $3$ 的倍数确实从 $3 \times 1$ 开始到 $3 \times 33 = 99$，共 $33$ 个。如果题目条件变成「$n+1$ 是 $2$ 的倍数」，范围 $2 \le n+1 \le 101$ 中就包含 $2 \times 1 = 2$。务必写清范围不等式再数！

  したがって、求める $n$ の個数は、全体 $100$ 個から $n + 1$ が $3$ の倍数となる $33$ 個を除いて、
  $$100 - 33 = 67 \text{（個）}$$
- **【最终答案】**
  **$67$ 個**

---

#### 演習問題 3-(4)
- **【原题重现与翻译】**
  - 原题：次の方程式の整数解をすべて求めよ。
    - `[1]` $7x + 6y = 40$　　`[2]` $37x - 90y = 4$
  - 中文：求下列一次不定方程的所有整数解。
- **【考点定位】**
  - 一次不定方程 $ax + by = c$ 的通解求法（目测特解 / 欧几里得互除法逆推特解）。
- **【分步标准解答】**
  **`[1]` $7x + 6y = 40$ …… ①**
  整数解の 1 組を見つけると、$x = 4,\; y = 2$ が成り立つ（$7 \cdot 4 + 6 \cdot 2 = 28 + 12 = 40$）。
  $$7 \cdot 4 + 6 \cdot 2 = 40 \qquad \cdots \text{②}$$
  ① $-$ ② より、
  $$7(x - 4) + 6(y - 2) = 0 \implies 7(x - 4) = -6(y - 2) \qquad \cdots \text{③}$$
  > 💡 讲师批注：即使一眼看不出 $(4, 2)$，也可以先看 $7(1) + 6(-1) = 1$，两边乘 $40$ 得特解 $(40, -40)$；再将 $x$ 减 $6 \times 6 = 36$、$y$ 加 $7 \times 6 = 42$，即可化简为小数字特解 $(4, 2)$！

  $7$ と $6$ は互いに素であるから、$x - 4$ は $6$ の倍数である。
  よって、整数 $k$ を用いて $x - 4 = 6k$ すなわち $x = 6k + 4$ と表される。
  これを ③ に代入すると、$7(6k) = -6(y - 2) \implies y - 2 = -7k \implies y = -7k + 2$。
  したがって、すべての整数解は、
  $$x = 6k + 4, \qquad y = -7k + 2 \qquad (k \text{ は整数})$$

  **`[2]` $37x - 90y = 4$ …… ①**
  係数が大きいため、$90$ と $37$ に対してユークリッドの互除法を用い、$37p - 90q = 1$ の解を求める。
  $$\begin{aligned}
  90 &= 37 \times 2 + 16 &\implies 16 &= 90 - 37 \times 2 \quad \cdots \text{(A)} \\
  37 &= 16 \times 2 + 5  &\implies 5  &= 37 - 16 \times 2 \quad \cdots \text{(B)} \\
  16 &= 5 \times 3 + 1   &\implies 1  &= 16 - 5 \times 3  \quad \cdots \text{(C)}
  \end{aligned}$$
  (C) に (B), (A) を順に代入して逆算する（$37$ と $90$ は掛け算を実行せず文字のように残すのがコツ）：
  $$\begin{aligned}
  1 &= 16 - (37 - 16 \times 2) \times 3 \\
    &= 16 \times 7 - 37 \times 3 \\
    &= (90 - 37 \times 2) \times 7 - 37 \times 3 \\
    &= 90 \times 7 - 37 \times 17
  \end{aligned}$$
  > 💡 讲师批注：逆推回代时**绝对不要把 $37 \times 2$ 算成 $74$**！把 $37, 90, 16, 5$ 当作字母合并同类项（例如 $16 + 16 \times 6 = 16 \times 7$），最后立刻验算：$90 \times 7 - 37 \times 17 = 630 - 629 = 1$，一气呵成！

  すなわち、$37 \cdot (-17) - 90 \cdot (-7) = 1$。両辺を $4$ 倍すると、
  $$37 \cdot (-68) - 90 \cdot (-28) = 4$$
  より小さい正の特解にするため、$-68 + 90 = 22,\; -28 + 37 = 9$ を用いると（$37 \cdot 22 - 90 \cdot 9 = 814 - 810 = 4$）、
  $$37 \cdot 22 - 90 \cdot 9 = 4 \qquad \cdots \text{②}$$
  ① $-$ ② より、
  $$37(x - 22) - 90(y - 9) = 0 \implies 37(x - 22) = 90(y - 9) \qquad \cdots \text{③}$$
  $37$ と $90$ は互いに素であるから、整数 $k$ を用いて $x - 22 = 90k \implies x = 90k + 22$。
  ③ に代入して $y - 9 = 37k \implies y = 37k + 9$。
  > 💡 讲师批注：直接用特解 $(-68, -28)$ 写出 $x = 90k - 68,\; y = 37k - 28$ 也是完全等价的正确答案（令 $k = k' + 1$ 即重合）。考场上如果题目要求「$x$ 为最小正整数」，则 $(22, 9)$ 直接命中！
- **【最终答案】**
  **`[1]` $x = 6k + 4,\; y = -7k + 2$（$k$ は整数）**
  **`[2]` $x = 90k + 22,\; y = 37k + 9$（$k$ は整数）**（※ $x = 90k - 68,\; y = 37k - 28$ とも同値）

---

#### 演習問題 3-(5)
- **【原题重现与翻译】**
  - 原题：$3$ で割ると $2$ 余り、$5$ で割ると $3$ 余り、$7$ で割ると $4$ 余るような自然数 $n$ で最小のものを求めよ。
  - 中文：求除以 $3$ 余 $2$、除以 $5$ 余 $3$、除以 $7$ 余 $4$ 的最小自然数 $n$。
- **【考点定位】**
  - 中国剩余定理（孫子の定理）背景下的连立一次不定方程求解。
- **【分步标准解答】**
  条件より、整数 $a, b, c$ を用いて
  $$n = 7a + 4 = 5b + 3 = 3c + 2$$
  と表せる。まず、係数の大きい $7a + 4 = 5b + 3$ を解く。
  $$7a - 5b = -1$$
  特解として $a = 2,\; b = 3$ がある（$7 \cdot 2 - 5 \cdot 3 = -1$）。辺々引いて、
  $$7(a - 2) = 5(b - 3)$$
  $7$ と $5$ は互いに素であるから、整数 $k$ を用いて $a - 2 = 5k \implies a = 5k + 2$。
  よって、
  $$n = 7(5k + 2) + 4 = 35k + 18$$
  > 💡 讲师批注：**策略提速**：解三个余数条件时，务必先联立模数最大的两个（$7$ 和 $5$），这样得到 $35k + 18$ 后，只需把 $k = 0, 1, 2$ 代入检验除以 $3$ 是否余 $2$，最多试 3 次必出答案！

  次に、$n = 35k + 18$ が「$3$ で割ると $2$ 余る」条件を満たす $k$ を求める。
  $$35k + 18 = 3(11k + 6) + 2k$$
  これが $3$ で割って $2$ 余るためには、$2k$ を $3$ で割った余りが $2$ であればよい。
  $k$ を $3$ で割った余りで調べると、
  - $k \equiv 0 \pmod 3 \implies 2k \equiv 0$
  - $k \equiv 1 \pmod 3 \implies 2k \equiv 2$（適！）
  - $k \equiv 2 \pmod 3 \implies 2k \equiv 1$
  よって、$k = 3m + 1$（$m$ は整数）であり、
  $$n = 35(3m + 1) + 18 = 105m + 53$$
  $n$ が最小の自然数となるのは $m = 0$ のときで、$n = 53$。
  > 💡 讲师批注：逐条验算：$53 = 3 \times 17 + 2$ ✓，$53 = 5 \times 10 + 3$ ✓，$53 = 7 \times 7 + 4$ ✓！而且 $53 < 105$，确为最小自然数。
- **【最终答案】**
  **$n = 53$**

---

#### 演習問題 3-(6)
- **【原题重现与翻译】**
  - 原题：どのような負でない 2 つの整数 $m$ と $n$ を用いても $x = 3m + 5n$ とは表すことができない正の整数 $x$ をすべて求めよ。
  - 中文：求所有不能用任意两个非负整数 $m, n$ 表示成 $x = 3m + 5n$ 的正整数 $x$。
- **【考点定位】**
  - 非负整数线性组合的可表示性（Frobenius 硬币问题 / 模 $3$ 剩余类分类法）。
- **【图解辅助（SVG 矢量图）】**
  按除以 $3$ 的余数将所有正整数排成 3 行，直观看到每行从「首次被 $5n$ 命中」起向右（加 $3m$）全部可表示，被截断在左侧的即为无法表示的数：

<svg viewBox="0 0 580 165" width="580" height="165" xmlns="http://www.w3.org/2000/svg" style="background:#fafafa;border:1px solid #e0e0e0;border-radius:6px;">
  <style>
    .t { font: bold 13px sans-serif; fill: #2c3e50; }
    .rlbl { font: bold 11px sans-serif; fill: #555; }
    .bad { fill: #fadbd8; stroke: #c0392b; stroke-width: 1.5; rx: 4; }
    .ok { fill: #d5f5e3; stroke: #27ae60; stroke-width: 1.2; rx: 4; }
    .start { fill: #a9dfbf; stroke: #1e8449; stroke-width: 2; rx: 4; }
    .num { font: bold 12px monospace; fill: #2c3e50; text-anchor: middle; }
    .num-b { font: bold 12px monospace; fill: #c0392b; text-anchor: middle; }
    .note { font: 11px sans-serif; fill: #555; }
  </style>
  <text x="16" y="22" class="t">x = 3m + 5n（m, n ≥ 0）の 3 の余り別マップ（赤＝表せない、緑＝すべて表せる）</text>
  <!-- Row 0: 3k -->
  <text x="16" y="56" class="rlbl">3の倍数 (n=0)</text>
  <rect x="125" y="38" width="44" height="26" class="start"/><text x="147" y="56" class="num">3</text>
  <rect x="180" y="38" width="44" height="26" class="ok"/><text x="202" y="56" class="num">6</text>
  <rect x="235" y="38" width="44" height="26" class="ok"/><text x="257" y="56" class="num">9</text>
  <rect x="290" y="38" width="44" height="26" class="ok"/><text x="312" y="56" class="num">12</text>
  <rect x="345" y="38" width="44" height="26" class="ok"/><text x="367" y="56" class="num">15</text>
  <text x="405" y="56" class="note">⋯ すべて表せる (3m+5·0)</text>
  <!-- Row 2: 3k+2 -->
  <text x="16" y="96" class="rlbl">余り 2 (n=1)</text>
  <rect x="125" y="78" width="44" height="26" class="bad"/><text x="147" y="96" class="num-b">2 ×</text>
  <rect x="180" y="78" width="44" height="26" class="start"/><text x="202" y="96" class="num">5</text>
  <rect x="235" y="78" width="44" height="26" class="ok"/><text x="257" y="96" class="num">8</text>
  <rect x="290" y="78" width="44" height="26" class="ok"/><text x="312" y="96" class="num">11</text>
  <rect x="345" y="78" width="44" height="26" class="ok"/><text x="367" y="96" class="num">14</text>
  <text x="405" y="96" class="note">⋯ 5以上はすべて表せる (3m+5·1)</text>
  <!-- Row 1: 3k+1 -->
  <text x="16" y="136" class="rlbl">余り 1 (n=2)</text>
  <rect x="125" y="118" width="44" height="26" class="bad"/><text x="147" y="136" class="num-b">1 ×</text>
  <rect x="180" y="118" width="44" height="26" class="bad"/><text x="202" y="136" class="num-b">4 ×</text>
  <rect x="235" y="118" width="44" height="26" class="bad"/><text x="257" y="136" class="num-b">7 ×</text>
  <rect x="290" y="118" width="44" height="26" class="start"/><text x="312" y="136" class="num">10</text>
  <rect x="345" y="118" width="44" height="26" class="ok"/><text x="367" y="136" class="num">13</text>
  <text x="405" y="136" class="note">⋯ 10以上はすべて表せる (3m+5·2)</text>
</svg>

- **【分步标准解答】**
  正の整数 $x$ を $3$ で割った余りによって分類し、$x = 3m + 5n$（$m, n$ は $0$ 以上の整数）と表せるかどうかを調べる。
  1. **$x$ が $3$ の倍数のとき（$x = 3, 6, 9, \dots$）**：
     $n = 0$、$m = 1, 2, 3, \dots$ とすることで、$x = 3m + 5 \cdot 0$ と**すべて表せる**。
  2. **$x$ を $3$ で割った余りが $2$ のとき（$x = 2, 5, 8, 11, \dots$）**：
     $x = 3m + 5n$ の両辺を $3$ で割った余りを考えると、$5n = 3n + 2n$ より $2n \equiv 2 \pmod 3 \implies n \equiv 1 \pmod 3$。
     $n \ge 0$ なので最小の $n$ は $n = 1$（$5n = 5$）。
     よって、$x \ge 5$ ならば $x = 3m + 5 \cdot 1$（$m \ge 0$）として**すべて表せる**が、$x = 2$ は $5n \ge 5$ となり得ないため**表せない**。
  3. **$x$ を $3$ で割った余りが $1$ のとき（$x = 1, 4, 7, 10, 13, \dots$）**：
     同様に $2n \equiv 1 \pmod 3 \implies n \equiv 2 \pmod 3$。
     $n \ge 0$ なので最小の $n$ は $n = 2$（$5n = 10$）。
     よって、$x \ge 10$ ならば $x = 3m + 5 \cdot 2$（$m \ge 0$）として**すべて表せる**が、$x = 1, 4, 7$ は $5n \ge 10$ となり得ないため**表せない**。
  > 💡 讲师批注：**EJU 实用秒杀结论（鸡块定理 / Frobenius 公式）**：若正整数 $a, b$ 互素，则不能表示为 $am + bn$（$m, n \ge 0$）的最大正整数是 **$ab - a - b$**，且无法表示的正整数总个数为 **$\dfrac{(a-1)(b-1)}{2}$**！代入 $a=3, b=5$：最大不可表示数 $= 15 - 3 - 5 = 7$，总个数 $= \dfrac{2 \times 4}{2} = 4$ 个（即 $1, 2, 4, 7$），瞬间验算无误！

  以上より、表すことができない正の整数 $x$ は $1, 2, 4, 7$ である。
- **【最终答案】**
  **$x = 1,\; 2,\; 4,\; 7$**

---

### 演習問題 4（分数と小数、$n$ 進法）

#### 演習問題 4-(1)
- **【原题重现与翻译】**
  - 原题：$10$ 進数 $78$ を $2$ 進法で表すと $\square$、$5$ 進法で表すと $\square$ である。
  - 中文：将 $10$ 进制数 $78$ 用 $2$ 进制表示为 $\square$，用 $5$ 进制表示为 $\square$。
- **【考点定位】**
  - $10$ 进制整数转 $n$ 进制整数（除基取余短除法 / 連除法）。
- **【图解辅助（SVG 矢量图）】**
  直观展示将 $78$ 分别用 $2$ 和 $5$ 连续作短除法、并「**从下往上逆序读取余数**」的标准操作：

<svg viewBox="0 0 560 225" width="560" height="225" xmlns="http://www.w3.org/2000/svg" style="background:#fafafa;border:1px solid #e0e0e0;border-radius:6px;">
  <style>
    .t { font: bold 13px sans-serif; fill: #2c3e50; }
    .div { font: bold 13px monospace; fill: #2c3e50; text-anchor: end; }
    .rem { font: bold 13px monospace; fill: #c0392b; }
    .ln { stroke: #34495e; stroke-width: 1.4; }
    .arr { stroke: #c0392b; stroke-width: 1.8; fill: none; }
    .note { font: 11px sans-serif; fill: #c0392b; }
  </style>
  <text x="16" y="22" class="t">10進数 78 の連除法（余りを下から上へ逆順に並べる）</text>
  <!-- Left: base 2 -->
  <g transform="translate(20, 40)">
    <text x="0" y="10" class="t" fill="#2980b9">① 2進法への変換</text>
    <text x="26" y="34" class="div">2</text><line x1="34" y1="20" x2="34" y2="39" class="ln"/><line x1="34" y1="39" x2="90" y2="39" class="ln"/><text x="76" y="34" class="div">78</text><text x="102" y="34" class="rem">… 0</text>
    <text x="26" y="56" class="div">2</text><line x1="34" y1="42" x2="34" y2="61" class="ln"/><line x1="34" y1="61" x2="90" y2="61" class="ln"/><text x="76" y="56" class="div">39</text><text x="102" y="56" class="rem">… 1</text>
    <text x="26" y="78" class="div">2</text><line x1="34" y1="64" x2="34" y2="83" class="ln"/><line x1="34" y1="83" x2="90" y2="83" class="ln"/><text x="76" y="78" class="div">19</text><text x="102" y="78" class="rem">… 1</text>
    <text x="26" y="100" class="div">2</text><line x1="34" y1="86" x2="34" y2="105" class="ln"/><line x1="34" y1="105" x2="90" y2="105" class="ln"/><text x="76" y="100" class="div">9</text><text x="102" y="100" class="rem">… 1</text>
    <text x="26" y="122" class="div">2</text><line x1="34" y1="108" x2="34" y2="127" class="ln"/><line x1="34" y1="127" x2="90" y2="127" class="ln"/><text x="76" y="122" class="div">4</text><text x="102" y="122" class="rem">… 0</text>
    <text x="26" y="144" class="div">2</text><line x1="34" y1="130" x2="34" y2="149" class="ln"/><line x1="34" y1="149" x2="90" y2="149" class="ln"/><text x="76" y="144" class="div">2</text><text x="102" y="144" class="rem">… 0</text>
    <text x="76" y="166" class="rem" text-anchor="end">1</text>
    <!-- Upward arrow -->
    <path d="M 86 164 L 145 164 L 145 28" class="arr"/>
    <polygon points="145,22 140,32 150,32" fill="#c0392b"/>
    <text x="155" y="96" class="note">下から順に読む</text>
    <text x="155" y="116" class="rem">1001110₍₂₎</text>
  </g>
  <!-- Right: base 5 -->
  <g transform="translate(320, 40)">
    <text x="0" y="10" class="t" fill="#27ae60">② 5進法への変換</text>
    <text x="26" y="34" class="div">5</text><line x1="34" y1="20" x2="34" y2="39" class="ln"/><line x1="34" y1="39" x2="90" y2="39" class="ln"/><text x="76" y="34" class="div">78</text><text x="102" y="34" class="rem">… 3</text>
    <text x="26" y="56" class="div">5</text><line x1="34" y1="42" x2="34" y2="61" class="ln"/><line x1="34" y1="61" x2="90" y2="61" class="ln"/><text x="76" y="56" class="div">15</text><text x="102" y="56" class="rem">… 0</text>
    <text x="76" y="78" class="rem" text-anchor="end">3</text>
    <path d="M 86 76 L 145 76 L 145 28" class="arr"/>
    <polygon points="145,22 140,32 150,32" fill="#c0392b"/>
    <text x="155" y="56" class="note">下から順に読む</text>
    <text x="155" y="76" class="rem">303₍₅₎</text>
  </g>
</svg>

- **【分步标准解答】**
  1. **$2$ 進法**：$78$ を $2$ で順次割って余りを求める。
     $$\begin{aligned}
     78 &= 2 \times 39 + 0 \\
     39 &= 2 \times 19 + 1 \\
     19 &= 2 \times 9 + 1 \\
     9  &= 2 \times 4 + 1 \\
     4  &= 2 \times 2 + 0 \\
     2  &= 2 \times 1 + 0
     \end{aligned}$$
     最後の商 $1$ と余りを下から順に並べて、$1001110_{(2)}$。
     > 💡 讲师批注：反向展开验算：$2^6 + 2^3 + 2^2 + 2^1 = 64 + 8 + 4 + 2 = 78$ ✓！熟练记下 $2$ 的幂（$1, 2, 4, 8, 16, 32, 64$）后，也可以直接拆解 $78 = 64 + 8 + 4 + 2$ 秒写二进制。

  2. **$5$ 進法**：$78$ を $5$ で順次割る。
     $$\begin{aligned}
     78 &= 5 \times 15 + 3 \\
     15 &= 5 \times 3 + 0
     \end{aligned}$$
     最後の商 $3$ と余りを下から順に並べて、$303_{(5)}$。
     > 💡 讲师批注：反向展开验算：$3 \times 5^2 + 0 \times 5^1 + 3 \times 5^0 = 75 + 0 + 3 = 78$ ✓！
- **【最终答案】**
  **$2$ 進法：$1001110_{(2)}$、$5$ 進法：$303_{(5)}$**

---

#### 演習問題 4-(2)
- **【原题重现与翻译】**
  - 原题：$n$ は $3$ 以上の整数とする。$10$ 進法で $(n + 1)^2$ と表される数を $n$ 進法で表せ。
  - 中文：设 $n$ 为不小于 $3$ 的整数。将 $10$ 进制下表示为 $(n+1)^2$ 的数用 $n$ 进制表示。
- **【考点定位】**
  - $n$ 进制的位值展开定义与各位数字上限 $0 \le a_i \le n - 1$ 的检验。
- **【分步标准解答】**
  $(n + 1)^2$ を展開すると、
  $$(n + 1)^2 = n^2 + 2n + 1 = 1 \cdot n^2 + 2 \cdot n^1 + 1 \cdot n^0$$
  ここで、$n \ge 3$ より $n - 1 \ge 2$ であるから、各位の係数 $1, 2, 1$ はすべて $0$ 以上 $n - 1$ 以下の整数であり、繰り上がりは起こらない。
  > 💡 讲师批注：一定要理解为什么题干强调「$n \ge 3$」！如果 $n = 2$，那么数字 $2$ 超过了二进制各位最大允许值 $n - 1 = 1$，会发生进位：$(2+1)^2 = 9 = 1 \cdot 2^3 + 0 \cdot 2^2 + 0 \cdot 2^1 + 1 \cdot 2^0 = 1001_{(2)}$，而不是 $121_{(2)}$！

  したがって、$n$ 進法で表すと $121_{(n)}$ となる。
- **【最终答案】**
  **$121_{(n)}$**

---

#### 演習問題 4-(3)
- **【原题重现与翻译】**
  - 原题：$110111_{(2)},\; 120201_{(3)}$ をそれぞれ $10$ 進数で表せ。
  - 中文：将 $110111_{(2)}$ 与 $120201_{(3)}$ 分别用 $10$ 进制数表示。
- **【考点定位】**
  - $n$ 进制整数转 $10$ 进制（按权展开求和）。
- **【分步标准解答】**
  1. **$110111_{(2)}$**：
     $$110111_{(2)} = 1 \cdot 2^5 + 1 \cdot 2^4 + 0 \cdot 2^3 + 1 \cdot 2^2 + 1 \cdot 2^1 + 1 \cdot 2^0$$
     $$= 32 + 16 + 0 + 4 + 2 + 1 = 55$$
     > 💡 讲师批注：数位数时最容易把最高位指数多算 $1$！6 位数最高位是 $n^5$（$6 - 1 = 5$），建议从右向左标出 $0, 1, 2, 3, 4, 5$ 再展开。

  2. **$120201_{(3)}$**：
     $$120201_{(3)} = 1 \cdot 3^5 + 2 \cdot 3^4 + 0 \cdot 3^3 + 2 \cdot 3^2 + 0 \cdot 3^1 + 1 \cdot 3^0$$
     $$= 243 + 2 \times 81 + 0 + 2 \times 9 + 0 + 1$$
     $$= 243 + 162 + 18 + 1 = 424$$
     > 💡 讲师批注：核对 3 的幂次：$3^0=1, 3^1=3, 3^2=9, 3^3=27, 3^4=81, 3^5=243$。求和：$243+162=405$，$405+18+1=424$，无误！
- **【最终答案】**
  **$110111_{(2)} = 55$、$120201_{(3)} = 424$**

---

#### 演習問題 4-(4)
- **【原题重现与翻译】**
  - 原题：$0.111_{(2)}$ を $10$ 進法の小数で表せ。
  - 中文：将 $0.111_{(2)}$ 用 $10$ 进制小数表示。
- **【考点定位】**
  - $n$ 进制小数转 $10$ 进制小数（按负权 $\dfrac{1}{n^1}, \dfrac{1}{n^2}, \dfrac{1}{n^3}, \dots$ 展开）。
- **【分步标准解答】**
  $2$ 進法の小数点以下の位は、左から順に $\dfrac{1}{2^1},\; \dfrac{1}{2^2},\; \dfrac{1}{2^3}$ の位であるから、
  $$0.111_{(2)} = 1 \cdot \frac{1}{2} + 1 \cdot \frac{1}{2^2} + 1 \cdot \frac{1}{2^3} = \frac{1}{2} + \frac{1}{4} + \frac{1}{8} = \frac{4 + 2 + 1}{8} = \frac{7}{8}$$
  小数に直すと、
  $$\frac{7}{8} = 0.875$$
  > 💡 讲师批注：熟记 $\dfrac{1}{8} = 0.125$、$\dfrac{3}{8} = 0.375$、$\dfrac{5}{8} = 0.625$、$\dfrac{7}{8} = 0.875$ 可大幅提升 $2$ 进制小数互化速度！
- **【最终答案】**
  **$0.875$**

---

#### 演習問題 4-(5)
- **【原题重现与翻译】**
  - 原题：$10$ 進数 $0.375$ を $2$ 進法で表すと $\square$、$5$ 進法で表すと $\square$ である。
  - 中文：将 $10$ 进制数 $0.375$ 用 $2$ 进制表示为 $\square$，用 $5$ 进制表示为 $\square$。
- **【考点定位】**
  - $10$ 进制小数转 $n$ 进制小数（乘基取整法）与不同进制下「有限小数 vs. 循环小数」的转化陷阱。
- **【图解辅助（SVG 矢量图）】**
  直观对比 $0.375$ 在 $2$ 进制（有限结束）与 $5$ 进制（进入循环）中的「乘基取整」流程：

<svg viewBox="0 0 580 185" width="580" height="185" xmlns="http://www.w3.org/2000/svg" style="background:#fafafa;border:1px solid #e0e0e0;border-radius:6px;">
  <style>
    .t { font: bold 13px sans-serif; fill: #2c3e50; }
    .eq { font: 12px monospace; fill: #2c3e50; }
    .dig { font: bold 13px monospace; fill: #c0392b; }
    .box { fill: #fff; stroke: #bdc3c7; stroke-width: 1.2; rx: 5; }
    .loop { stroke: #e67e22; stroke-width: 1.6; fill: none; }
    .note { font: bold 11px sans-serif; fill: #e67e22; }
  </style>
  <text x="16" y="22" class="t">10進小数 0.375 の変換（基数を掛けて整数部を上から順に並べる）</text>
  <!-- Left: base 2 -->
  <rect x="16" y="36" width="258" height="134" class="box"/>
  <text x="28" y="56" class="t" fill="#2980b9">① 2進法（×2 を繰り返す）</text>
  <text x="28" y="80" class="eq">0.375 × 2 = </text><text x="114" y="80" class="dig">0</text><text x="124" y="80" class="eq">.75</text>
  <text x="28" y="102" class="eq">0.75  × 2 = </text><text x="114" y="102" class="dig">1</text><text x="124" y="102" class="eq">.5</text>
  <text x="28" y="124" class="eq">0.5   × 2 = </text><text x="114" y="124" class="dig">1</text><text x="124" y="124" class="eq">.0（終了！）</text>
  <text x="28" y="152" class="dig">▶ 0.011₍₂₎（有限小数）</text>
  <!-- Right: base 5 -->
  <rect x="292" y="36" width="272" height="134" class="box"/>
  <text x="304" y="56" class="t" fill="#e67e22">② 5進法（×5 を繰り返す）</text>
  <text x="304" y="80" class="eq">0.375 × 5 = </text><text x="390" y="80" class="dig">1</text><text x="400" y="80" class="eq">.875</text>
  <text x="304" y="102" class="eq">0.875 × 5 = </text><text x="390" y="102" class="dig">4</text><text x="400" y="102" class="eq">.375</text>
  <text x="304" y="124" class="eq">0.375 × 5 = </text><text x="390" y="124" class="dig">1</text><text x="400" y="124" class="eq">.875 …</text>
  <path d="M 438 100 C 468 100, 468 76, 438 76" class="loop"/>
  <polygon points="434,76 442,72 442,80" fill="#e67e22"/>
  <text x="466" y="92" class="note">0.375 に戻る！</text>
  <text x="304" y="152" class="dig">▶ 0.1̇4̇₍₅₎（循環小数 0.1414⋯₍₅₎）</text>
</svg>

- **【分步标准解答】**
  $10$ 進小数を $n$ 進法に直すには、小数部分に $n$ を掛け続け、出てきた整数部分を上から順に小数第 1 位、第 2 位、……と並べる。

  1. **$2$ 進法**（小数部分に $2$ を掛ける）：
     $$\begin{aligned}
     0.375 \times 2 &= \mathbf{0}.75 \\
     0.75 \times 2  &= \mathbf{1}.5 \\
     0.5 \times 2   &= \mathbf{1}.0 \quad (\text{小数部が } 0 \text{ で終了})
     \end{aligned}$$
     よって、$0.011_{(2)}$。
     > 💡 讲师批注：分数巧解：$0.375 = \dfrac{3}{8} = \dfrac{0}{2} + \dfrac{1}{4} + \dfrac{1}{8} = 0.011_{(2)}$，一眼秒杀！

  2. **$5$ 進法**（小数部分に $5$ を掛ける）：
     $$\begin{aligned}
     0.375 \times 5 &= \mathbf{1}.875 \\
     0.875 \times 5 &= \mathbf{4}.375 \\
     0.375 \times 5 &= \mathbf{1}.875 \quad (\text{以後 } 1, 4 \text{ を無限に繰り返す})
     \end{aligned}$$
     よって、$0.141414\cdots_{(5)} = 0.\dot{1}\dot{4}_{(5)}$。
     > 💡 讲师批注：**极易踩坑的高级亮点**！为什么 $10$ 进制下的有限小数 $0.375$ 在 $5$ 进制下变成了**无限循环小数**？因为 $0.375 = \dfrac{3}{8} = \dfrac{3}{2^3}$，分母含素因数 $2$（不是 $5$ 的约数），所以在 $5$ 进制下无法化为有限小数！
     > 反向验算（等比数列求和）：
     > $$0.\dot{1}\dot{4}_{(5)} = \left(\frac{1}{5} + \frac{4}{5^2}\right) + \left(\frac{1}{5^3} + \frac{4}{5^4}\right) + \cdots = \frac{\frac{9}{25}}{1 - \frac{1}{25}} = \frac{9}{24} = \frac{3}{8} = 0.375 \quad \checkmark$$
- **【最终答案】**
  **$2$ 進法：$0.011_{(2)}$、$5$ 進法：$0.\dot{1}\dot{4}_{(5)}$（すなわち $0.1414\cdots_{(5)}$）**
