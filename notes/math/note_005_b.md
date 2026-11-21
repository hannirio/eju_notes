# 《EJU 教材全解与备课讲义》数学 005-B（P68–P75）

> **对应源文件**：`work_math/ocr_md/ocr_005_p61-75.md`（下篇：第三章 演習問題 5-(1)～(10) 及 第四章《指数関数と対数関数》演習問題 1-(1)～(3)；知识点与词汇总览、上篇习题见 [note_005_a.md](file:///Users/baohan/Desktop/EJU/notes_math/note_005_a.md)）
> **视觉核对参考图**：`work_math/ref_imgs/page_0068.jpg` – `page_0075.jpg`

---

## 三、逐题深度解析（不可跳步）— Part B（P68–P75）

---

### 第三章 演習問題 5（二次不等式・絶対値・最大最小・実数解の個数）

#### 演習問題 5-(1)
- **【原题重现与翻译】**
  - 原题：$-3x^2 + 8x - 6 > 0$（次の不等式を解け）
  - 中文：解不等式 $-3x^2 + 8x - 6 > 0$。
- **【考点定位】**
  - 二次项系数为负且判别式 $D < 0$ 的二次不等式。
- **【分步标准解答】**
  両辺に $-1$ を掛けて、$x^2$ の係数を正にすると（不等号の向きが変わる）：
  $$3x^2 - 8x + 6 < 0$$
  > 💡 讲师批注：解二次不等式的第一铁律——**先把 $x^2$ 系数化为正数**，同时牢记乘以负数必须反转不等号！

  2 次方程式 $3x^2 - 8x + 6 = 0$ の判別式を $D$ とすると：
  $$\frac{D}{4} = (-4)^2 - 3 \cdot 6 = 16 - 18 = -2 < 0$$
  $3 > 0$ かつ $D < 0$ であるから、すべての実数 $x$ に対して $3x^2 - 8x + 6 > 0$ が成り立つ。
  よって、$3x^2 - 8x + 6 < 0$ を満たす実数 $x$ は存在しない。
  > 💡 讲师批注：配方验算：$3x^2 - 8x + 6 = 3\left(x - \dfrac{4}{3}\right)^2 + \dfrac{2}{3} \ge \dfrac{2}{3} > 0$，恒正，故严格小于 $0$ 无解。
- **【最终答案】**
  **解はない（解なし）**

---

#### 演習問題 5-(2)
- **【原题重现与翻译】**
  - 原题：$2 - 3x - 2x^2 \le 4x - 2 < x^2$（次の不等式を解け）
  - 中文：解连不等式 $2 - 3x - 2x^2 \le 4x - 2 < x^2$。
- **【考点定位】**
  - 连不等式拆分（$A \le B < C \iff A \le B \text{ かつ } B < C$）+ 联立二次不等式 + 无理数端点大小比较。
- **【图解辅助（SVG 矢量图）】**

<svg viewBox="0 0 560 155" width="560" height="155" xmlns="http://www.w3.org/2000/svg" style="background:#fafafa;border:1px solid #e0e0e0;border-radius:6px;">
  <style>
    .title { font: bold 12px sans-serif; fill: #2c3e50; }
    .lbl { font: 11px sans-serif; fill: #333; text-anchor: middle; }
    .axis { stroke: #333; stroke-width: 1.4; }
    .r1 { stroke: #2980b9; stroke-width: 2; fill: none; }
    .r2 { stroke: #c0392b; stroke-width: 2; fill: none; }
    .sh { fill: #27ae60; fill-opacity: 0.25; }
  </style>
  <text x="15" y="20" class="title">連立二次不等式の共通範囲（数直線）</text>
  <!-- Number line y=120 -->
  <line x1="25" y1="120" x2="535" y2="120" class="axis"/>
  <polygon points="535,120 528,116 528,124" fill="#333"/>
  <text x="530" y="138" class="lbl" font-style="italic">x</text>
  <!-- Positions: -4 -> 115, 1/2 -> 240, 2-sqrt(2)~0.586 -> 310 (stretched for clarity), 2+sqrt(2)~3.414 -> 445 -->
  <!-- Shaded overlaps -->
  <rect x="30" y="96" width="85" height="24" class="sh"/>
  <rect x="240" y="96" width="70" height="24" class="sh"/>
  <rect x="445" y="96" width="80" height="24" class="sh"/>
  <!-- Range ① (blue, height 96): x <= -4, x >= 1/2 -->
  <polyline points="30,96 115,96 115,120" class="r1"/>
  <polyline points="240,120 240,96 525,96" class="r1"/>
  <circle cx="115" cy="120" r="3.5" fill="#2980b9"/>
  <circle cx="240" cy="120" r="3.5" fill="#2980b9"/>
  <text x="45" y="90" class="lbl" fill="#2980b9">①</text>
  <text x="505" y="90" class="lbl" fill="#2980b9">①</text>
  <!-- Range ② (red, height 68): x < 2-sqrt(2), x > 2+sqrt(2) -->
  <polyline points="30,68 310,68 310,120" class="r2"/>
  <polyline points="445,120 445,68 525,68" class="r2"/>
  <circle cx="310" cy="120" r="3.5" fill="#fff" stroke="#c0392b" stroke-width="1.8"/>
  <circle cx="445" cy="120" r="3.5" fill="#fff" stroke="#c0392b" stroke-width="1.8"/>
  <text x="190" y="62" class="lbl" fill="#c0392b">②</text>
  <text x="490" y="62" class="lbl" fill="#c0392b">②</text>
  <!-- Tick labels -->
  <text x="115" y="138" class="lbl">-4</text>
  <text x="240" y="138" class="lbl">1/2</text>
  <text x="315" y="138" class="lbl">2-√2</text>
  <text x="445" y="138" class="lbl">2+√2</text>
  <text x="315" y="150" class="lbl" font-size="10" fill="#7f8c8d">(≈0.586)</text>
  <text x="445" y="150" class="lbl" font-size="10" fill="#7f8c8d">(≈3.414)</text>
</svg>

- **【分步标准解答】**
  与えられた連不等式は次の連立不等式と同値である：
  $$\begin{cases} 2 - 3x - 2x^2 \le 4x - 2 & \cdots ① \\ 4x - 2 < x^2 & \cdots ② \end{cases}$$

  - **① を解く**：
    右辺に移項して整理すると：
    $$2x^2 + 7x - 4 \ge 0$$
    たすき掛けにより因数分解すると：
    $$(2x - 1)(x + 4) \ge 0$$
    ゆえに：
    $$x \le -4,\qquad \frac{1}{2} \le x \quad \cdots ①'$$

  - **② を解く**：
    右辺に移項して整理すると：
    $$x^2 - 4x + 2 > 0$$
    $x^2 - 4x + 2 = 0$ を解の公式で解くと $x = 2 \pm \sqrt{4 - 2} = 2 \pm \sqrt{2}$。
    ゆえに：
    $$x < 2 - \sqrt{2},\qquad 2 + \sqrt{2} < x \quad \cdots ②'$$

  - **大小関係の比較と共通範囲**：
    $\dfrac{1}{2}$ と $2 - \sqrt{2}$ の大小を比べる：
    $$(2 - \sqrt{2}) - \frac{1}{2} = \frac{3}{2} - \sqrt{2} = \sqrt{\frac{9}{4}} - \sqrt{2} > 0$$
    > 💡 讲师批注：**必考细节！** $\dfrac{1}{2} = 0.5$ 与 $2 - \sqrt{2} \approx 0.586$ 非常接近，必须通过平方比较（$\frac{9}{4} > 2$）严谨确认 $\dfrac{1}{2} < 2 - \sqrt{2}$，否则会漏掉中间解区间 $\dfrac{1}{2} \le x < 2 - \sqrt{2}$！

    よって $-4 < \dfrac{1}{2} < 2 - \sqrt{2} < 2 + \sqrt{2}$ であり、①' と ②' の共通範囲（上の数直線）を求めると：
    $$x \le -4,\qquad \frac{1}{2} \le x < 2 - \sqrt{2},\qquad 2 + \sqrt{2} < x$$
- **【最终答案】**
  **$x \le -4,\quad \dfrac{1}{2} \le x < 2 - \sqrt{2},\quad 2 + \sqrt{2} < x$**

---

#### 演習問題 5-(3)
- **【原题重现与翻译】**
  - 原题：$|x^2 - 2x - 3| \ge 3 - x$（次の不等式を解け）
  - 中文：解含绝对值的不等式 $|x^2 - 2x - 3| \ge 3 - x$。
- **【考点定位】**
  - 含绝对值的二次不等式（分段去绝对值法）。
- **【分步标准解答】**
  絶対値の中身を因数分解すると：
  $$x^2 - 2x - 3 = (x - 3)(x + 1)$$
  したがって、$x^2 - 2x - 3$ の符号によって次の 2 つの場合に分ける。

  - **[1] $x^2 - 2x - 3 \ge 0$、すなわち $x \le -1,\; 3 \le x$ のとき**：
    $|x^2 - 2x - 3| = x^2 - 2x - 3$ より、不等式は：
    $$x^2 - 2x - 3 \ge 3 - x$$
    $$x^2 - x - 6 \ge 0$$
    $$(x - 3)(x + 2) \ge 0$$
    $$x \le -2,\qquad 3 \le x$$
    これと場合分けの条件（$x \le -1,\; 3 \le x$）との共通範囲は：
    $$x \le -2,\qquad 3 \le x \quad \cdots ①$$

  - **[2] $x^2 - 2x - 3 < 0$、すなわち $-1 < x < 3$ のとき**：
    $|x^2 - 2x - 3| = -(x^2 - 2x - 3)$ より、不等式は：
    $$-(x^2 - 2x - 3) \ge 3 - x$$
    $$-x^2 + 2x + 3 \ge 3 - x$$
    $$x^2 - 3x \le 0 \implies x(x - 3) \le 0$$
    $$0 \le x \le 3$$
    これと場合分けの条件（$-1 < x < 3$）との共通範囲は：
    $$0 \le x < 3 \quad \cdots ②$$

  - **① と ② を合わせる（和集合）**：
    $0 \le x < 3$ と $3 \le x$ は $x = 3$ でつながるため、合わせて $0 \le x$ となる。
    > 💡 讲师批注：切记最后合并分类结果时要检查边界是否无缝衔接！$0 \le x < 3$ 与 $3 \le x$ 合并后务必化简为 **$0 \le x$**，不要分开写。
    > 💡 讲师批注（验算）：取 $x = -2$（左 $5 \ge$ 右 $5$，成立）；$x = -1$（左 $0 <$ 右 $4$，不成立）；$x = 0$（左 $3 \ge$ 右 $3$，成立）；$x = 3$（左 $0 \ge$ 右 $0$，成立）。100% 准确！
- **【最终答案】**
  **$x \le -2,\quad 0 \le x$**

---

#### 演習問題 5-(4)
- **【原题重现与翻译】**
  - 原题：$x$ についての不等式 $x^2 - (a+1)x + a < 0,\; 3x^2 + 2x - 1 > 0$ を同時に満たす整数 $x$ がちょうど 3 つ存在するような定数 $a$ の値の範囲を求めよ。
  - 中文：求常数 $a$ 的取值范围，使得同时满足关于 $x$ 的不等式 $x^2 - (a+1)x + a < 0$ 与 $3x^2 + 2x - 1 > 0$ 的整数 $x$ 恰好有 3 个。
- **【考点定位】**
  - 含参联立二次不等式的整数解个数问题（数轴法 + 端点等号检验）。
- **【图解辅助（SVG 矢量图）】**

<svg viewBox="0 0 560 190" width="560" height="190" xmlns="http://www.w3.org/2000/svg" style="background:#fafafa;border:1px solid #e0e0e0;border-radius:6px;">
  <style>
    .title { font: bold 12px sans-serif; fill: #2c3e50; }
    .lbl { font: 11px sans-serif; fill: #333; text-anchor: middle; }
    .axis { stroke: #333; stroke-width: 1.4; }
    .fixed { stroke: #2980b9; stroke-width: 2; fill: none; }
    .param { stroke: #c0392b; stroke-width: 2; fill: none; }
    .intdot { fill: #27ae60; }
  </style>
  <text x="15" y="20" class="title">整数解がちょうど3つになる定数 a の範囲（左：a &lt; 1，右：a &gt; 1）</text>
  <!-- Number line y=130, ticks from -6 to 6, center 0 at x=280, step=40 -->
  <line x1="20" y1="130" x2="540" y2="130" class="axis"/>
  <polygon points="540,130 533,126 533,134" fill="#333"/>
  <!-- Fixed range ②: x < -1 (x=240) and x > 1/3 (x=293) -->
  <polyline points="25,92 240,92 240,130" class="fixed"/>
  <polyline points="293,130 293,92 530,92" class="fixed"/>
  <circle cx="240" cy="130" r="3.5" fill="#fff" stroke="#2980b9" stroke-width="1.8"/>
  <circle cx="293" cy="130" r="3.5" fill="#fff" stroke="#2980b9" stroke-width="1.8"/>
  <text x="150" y="86" class="lbl" fill="#2980b9">② x &lt; -1</text>
  <text x="420" y="86" class="lbl" fill="#2980b9">② x &gt; 1/3</text>
  <!-- Case (ii) a > 1: (1, a) with 1 at x=320, a between 4(440) and 5(480), say 465 -->
  <polyline points="320,130 320,58 465,58 465,130" class="param"/>
  <circle cx="320" cy="130" r="3.5" fill="#fff" stroke="#c0392b" stroke-width="1.8"/>
  <circle cx="465" cy="130" r="3.5" fill="#fff" stroke="#c0392b" stroke-width="1.8"/>
  <text x="465" y="48" class="lbl" fill="#c0392b">a (4 &lt; a ≤ 5)</text>
  <!-- Case (iii) a < 1: (a, 1) with a between -5(80) and -4(120), say 95 -->
  <polyline points="95,130 95,58 320,58 320,130" class="param" stroke-dasharray="5,3"/>
  <circle cx="95" cy="130" r="3.5" fill="#fff" stroke="#c0392b" stroke-width="1.8"/>
  <text x="95" y="48" class="lbl" fill="#c0392b">a (-5 ≤ a &lt; -4)</text>
  <!-- Integer ticks & highlights -->
  <!-- -5:80, -4:120, -3:160, -2:200, -1:240, 0:280, 1:320, 2:360, 3:400, 4:440, 5:480 -->
  <text x="80" y="148" class="lbl">-5</text>
  <text x="120" y="148" class="lbl">-4</text>
  <text x="160" y="148" class="lbl">-3</text>
  <text x="200" y="148" class="lbl">-2</text>
  <text x="240" y="148" class="lbl">-1</text>
  <text x="280" y="148" class="lbl">0</text>
  <text x="293" y="162" class="lbl" fill="#2980b9" font-size="10">1/3</text>
  <text x="320" y="148" class="lbl">1</text>
  <text x="360" y="148" class="lbl">2</text>
  <text x="400" y="148" class="lbl">3</text>
  <text x="440" y="148" class="lbl">4</text>
  <text x="480" y="148" class="lbl">5</text>
  <!-- Highlighted 3 integer solutions on left (-4,-3,-2) and right (2,3,4) -->
  <circle cx="120" cy="130" r="4" class="intdot"/>
  <circle cx="160" cy="130" r="4" class="intdot"/>
  <circle cx="200" cy="130" r="4" class="intdot"/>
  <circle cx="360" cy="130" r="4" class="intdot"/>
  <circle cx="400" cy="130" r="4" class="intdot"/>
  <circle cx="440" cy="130" r="4" class="intdot"/>
  <text x="160" y="176" class="lbl" fill="#27ae60">左側の整数解：-4, -3, -2</text>
  <text x="400" y="176" class="lbl" fill="#27ae60">右側の整数解：2, 3, 4</text>
</svg>

- **【分步标准解答】**
  2 つの不等式をそれぞれ ①，② とおく：
  $$x^2 - (a+1)x + a < 0 \implies (x - 1)(x - a) < 0 \quad \cdots ①$$
  $$3x^2 + 2x - 1 > 0 \implies (3x - 1)(x + 1) > 0 \implies x < -1,\quad \frac{1}{3} < x \quad \cdots ②$$
  ① の解は $a$ と $1$ の大小関係によって決まるため、次のように場合分けする。

  - **[1] $a = 1$ のとき**：
    ① は $(x - 1)^2 < 0$ となり、解はない（不適）。

  - **[2] $a > 1$ のとき**：
    ① の解は $1 < x < a$。
    $1 > \dfrac{1}{3}$ より、① と ② の共通範囲はそのまま $1 < x < a$ である。
    この範囲に含まれる整数は小さい方から $2, 3, 4, \dots$ であるから、整数 $x$ がちょうど 3 つ（$2, 3, 4$）存在するための条件は：
    $$4 < a \le 5$$
    > 💡 讲师批注：**端点等号检验口诀「代进去看数够不够」**：
    > - 若 $a = 4$，则 $1 < x < 4$，整数只有 $2, 3$（仅 2 个）→ **不能取等号**；
    > - 若 $a = 5$，则 $1 < x < 5$，整数为 $2, 3, 4$（恰好 3 个）→ **可以取等号**！

  - **[3] $a < 1$ のとき**：
    ① の解は $a < x < 1$。
    これと ②（$x < -1$ または $\dfrac{1}{3} < x$）の共通範囲を考える。
    区間 $\dfrac{1}{3} < x < 1$ には**整数が含まれない**ため、整数解はすべて $a < x < -1$ の部分から出る必要がある。
    この範囲に含まれる整数は大きい方から $-2, -3, -4, \dots$ であるから、ちょうど 3 つ（$-2, -3, -4$）存在するための条件は：
    $$-5 \le a < -4$$
    > 💡 讲师批注：同样用代入法检验边界：
    > - 若 $a = -4$，则 $-4 < x < -1$，整数只有 $-3, -2$（仅 2 个）→ **不能取等号**；
    > - 若 $a = -5$，则 $-5 < x < -1$，整数为 $-4, -3, -2$（恰好 3 个）→ **可以取等号**！

  以上 [1]～[3] より、求める $a$ の値の範囲は $-5 \le a < -4,\quad 4 < a \le 5$。
- **【最终答案】**
  **$-5 \le a < -4,\quad 4 < a \le 5$**

---

#### 演習問題 5-(5)
- **【原题重现与翻译】**
  - 原题：$0 \le x \le 8$ のすべての $x$ の値に対して、不等式 $x^2 - 2mx + m + 6 > 0$ が成り立つような定数 $m$ の値の範囲を求めよ。
  - 中文：求常数 $m$ 的取值范围，使得对于 $0 \le x \le 8$ 内的所有 $x$，不等式 $x^2 - 2mx + m + 6 > 0$ 恒成立。
- **【考点定位】**
  - 闭区间上的二次不等式恒成立问题 $\iff$ **区间最小值 $> 0$**（动轴定区间分类讨论）。
- **【分步标准解答】**
  $f(x) = x^2 - 2mx + m + 6$ とおくと、平方完成して：
  $$f(x) = (x - m)^2 - m^2 + m + 6$$
  グラフは下に凸の放物線で、軸は直線 $x = m$ である。
  $0 \le x \le 8$ のすべての $x$ に対して $f(x) > 0$ が成り立つための必要十分条件は、**$0 \le x \le 8$ における $f(x)$ の最小値が正である**ことである。
  軸 $x = m$ の位置によって 3 つの場合に分ける：

  - **[1] $m < 0$ のとき**：
    $f(x)$ は $x = 0$ で最小値 $f(0) = m + 6$ をとる。
    $$f(0) > 0 \implies m + 6 > 0 \implies m > -6$$
    $m < 0$ との共通範囲は：$-6 < m < 0$。

  - **[2] $0 \le m \le 8$ のとき**：
    $f(x)$ は頂点 $x = m$ で最小値 $f(m) = -m^2 + m + 6$ をとる。
    $$f(m) > 0 \implies -m^2 + m + 6 > 0 \implies m^2 - m - 6 < 0$$
    $$(m - 3)(m + 2) < 0 \implies -2 < m < 3$$
    $0 \le m \le 8$ との共通範囲は：$0 \le m < 3$。

  - **[3] $m > 8$ のとき**：
    $f(x)$ は $x = 8$ で最小値 $f(8) = 64 - 16m + m + 6 = 70 - 15m$ をとる。
    $$f(8) > 0 \implies 70 - 15m > 0 \implies m < \frac{14}{3}$$
    $m > 8$ と $m < \dfrac{14}{3}\;(\approx 4.67)$ には共通範囲がない（解なし）。

  [1]～[3] の結果を合わせると（$-6 < m < 0$ と $0 \le m < 3$ が $m = 0$ でつながる）：
  $$-6 < m < 3$$
  > 💡 讲师批注：本题与 5-(7) 形成鲜明对比！开口向上时：
  > - 求「恒 $> 0$」看**最小值**（需按轴的位置分 3 类）；
  > - 求「恒 $\le 0$」看**最大值**（只需看两端点，见 5-(7)）。
- **【最终答案】**
  **$-6 < m < 3$**

---

#### 演習問題 5-(6)
- **【原题重现与翻译】**
  - 原题：2 つの 2 次関数 $f(x) = x^2 + 2ax + 25,\; g(x) = -x^2 + 4ax - 25$ がある。次の条件が成り立つような定数 $a$ の値の範囲を求めよ。
    - [1] 全ての実数に対して $f(x) > g(x)$ が成り立つ。
    - [2] ある実数に対して $f(x) < g(x)$ が成り立つ。
  - 中文：已知两个二次函数 $f(x) = x^2 + 2ax + 25,\; g(x) = -x^2 + 4ax - 25$。求满足下列条件时常数 $a$ 的取值范围。
    - [1] 对所有实数 $x$，都有 $f(x) > g(x)$ 成立。
    - [2] 存在某个实数 $x$，使得 $f(x) < g(x)$ 成立。
- **【考点定位】**
  - 全称量词（全ての実数）vs. 存在量词（ある実数）的二次不等式转化。
- **【分步标准解答】**
  $h(x) = f(x) - g(x)$ とおくと：
  $$h(x) = (x^2 + 2ax + 25) - (-x^2 + 4ax - 25) = 2x^2 - 2ax + 50 = 2(x^2 - ax + 25)$$
  $y = x^2 - ax + 25$ は下に凸の放物線であり、方程式 $x^2 - ax + 25 = 0$ の判別式を $D$ とすると：
  $$D = (-a)^2 - 4 \cdot 1 \cdot 25 = a^2 - 100 = (a + 10)(a - 10)$$

  - **[1] 全ての実数 $x$ に対して $f(x) > g(x)$**：
    すなわち、全ての実数 $x$ に対して $x^2 - ax + 25 > 0$ が成り立つことと同値である。
    放物線が常に $x$ 軸より上側にあればよいから、条件は $D < 0$：
    $$(a + 10)(a - 10) < 0 \implies -10 < a < 10$$

  - **[2] ある実数 $x$ に対して $f(x) < g(x)$**：
    すなわち、$x^2 - ax + 25 < 0$ を満たす実数 $x$ が**少なくとも 1 つ存在する**ことと同値である。
    下に凸の放物線が $x$ 軸より下側の部分を少しでも持てばよいから、条件は $D > 0$：
    $$(a + 10)(a - 10) > 0 \implies a < -10,\quad 10 < a$$
    > 💡 讲师批注：注意区分 [1] 与 [2] 并非严格互补！当 $a = \pm 10$ 时，$h(x) = 2(x \mp 5)^2 \ge 0$，在 $x = \pm 5$ 处 $f(x) = g(x)$，既不满足「恒大于」，也不满足「存在小于」，因此两端均**不含等号**。
- **【最终答案】**
  **[1] $-10 < a < 10$　　[2] $a < -10,\quad 10 < a$**

---

#### 演習問題 5-(7)
- **【原题重现与翻译】**
  - 原题：$0 \le x \le 1$ のすべての $x$ の値に対して、不等式 $x(x - 2m) \le m^2$ が成り立つような定数 $m$ の値の範囲を求めよ。
  - 中文：求常数 $m$ 的取值范围，使得对于 $0 \le x \le 1$ 内的所有 $x$，不等式 $x(x - 2m) \le m^2$ 恒成立。
- **【考点定位】**
  - 下凸二次函数在闭区间上恒 $\le 0$ 的端点判定定理（无需按轴分类讨论！）。
- **【分步标准解答】**
  移項して整理すると：
  $$x^2 - 2mx - m^2 \le 0$$
  $f(x) = x^2 - 2mx - m^2$ とおくと、$y = f(x)$ のグラフは**下に凸**の放物線である。
  下に凸の放物線が閉区間 $0 \le x \le 1$ で常に $f(x) \le 0$ となるための必要十分条件は、**両端点での値がともに $0$ 以下である**ことである：
  $$\begin{cases} f(0) \le 0 \\ f(1) \le 0 \end{cases}$$
  > 💡 讲师批注：**必背秒杀技巧！** 下凸函数在闭区间 $[p, q]$ 上的最大值一定只在端点 $x=p$ 或 $x=q$ 处取得，所以「$\forall x \in [p, q],\; f(x) \le 0 \iff f(p) \le 0 \text{ かつ } f(q) \le 0$」，完全省去了按对称轴分类讨论的麻烦！

  それぞれ計算すると：
  - $f(0) = -m^2 \le 0$：これは**すべての実数 $m$** に対して成り立つ。
  - $f(1) = 1 - 2m - m^2 \le 0 \iff m^2 + 2m - 1 \ge 0$。
    $m^2 + 2m - 1 = 0$ の解は $m = -1 \pm \sqrt{1 + 1} = -1 \pm \sqrt{2}$ より：
    $$m \le -1 - \sqrt{2},\qquad -1 + \sqrt{2} \le m$$
  > 💡 讲师批注：代入特值验算：$m = 0$ 时 $x^2 \le 0$ 在 $x=1$ 不成立（$0$ 确实不在解集内）；$m = 1$ 时 $x^2 - 2x - 1 \le 0$ 在 $[0, 1]$ 上最大值为 $f(0) = -1 \le 0$，成立！
- **【最终答案】**
  **$m \le -1 - \sqrt{2},\quad -1 + \sqrt{2} \le m$**

---

#### 演習問題 5-(8)
- **【原题重现与翻译】**
  - 原题：$x, y$ が $x^2 + 2y^2 = 1$ を満たすとき、$\dfrac{1}{2}x + y^2$ の最大値と最小値、及びそのときの $x, y$ の値を求めよ。
  - 中文：当实数 $x, y$ 满足 $x^2 + 2y^2 = 1$ 时，求 $\dfrac{1}{2}x + y^2$ 的最大值与最小值，以及取得最值时的 $x, y$ 的值。
- **【考点定位】**
  - 条件最值问题（消元法 + **挖掘隐含定义域 $y^2 \ge 0$**）。
- **【分步标准解答】**
  条件式 $x^2 + 2y^2 = 1$ より：
  $$y^2 = \frac{1 - x^2}{2} \quad \cdots ①$$
  ここで $y$ は実数なので $y^2 \ge 0$ である。よって：
  $$\frac{1 - x^2}{2} \ge 0 \implies x^2 \le 1 \implies -1 \le x \le 1 \quad \cdots ②$$
  > 💡 讲师批注：**EJU 最高频失分点！** 消去 $y^2$ 时，必须立刻写下隐含条件 $y^2 \ge 0 \implies -1 \le x \le 1$！如果漏掉这个定义域，不仅求不出最小值，还会错以为没有最小值！

  ① を与式 $z = \dfrac{1}{2}x + y^2$ に代入すると：
  $$z = \frac{1}{2}x + \frac{1 - x^2}{2} = -\frac{1}{2}x^2 + \frac{1}{2}x + \frac{1}{2}$$
  平方完成すると：
  $$z = -\frac{1}{2}\left(x^2 - x\right) + \frac{1}{2} = -\frac{1}{2}\left(x - \frac{1}{2}\right)^2 + \frac{1}{8} + \frac{1}{2} = -\frac{1}{2}\left(x - \frac{1}{2}\right)^2 + \frac{5}{8}$$
  グラフは**上に凸**の放物線で、軸は $x = \dfrac{1}{2}$ である。定義域 $-1 \le x \le 1$ において：
  - **最大値**：頂点 $x = \dfrac{1}{2}$ で最大値 $\dfrac{5}{8}$ をとる。
    このとき ① より $y^2 = \dfrac{1 - \frac{1}{4}}{2} = \dfrac{3}{8} \implies y = \pm \sqrt{\dfrac{3}{8}} = \pm \dfrac{\sqrt{6}}{4}$。
  - **最小値**：軸 $x = \dfrac{1}{2}$ から最も遠い端点 $x = -1$ で最小値をとる：
    $$z = -\frac{1}{2}(-1)^2 + \frac{1}{2}(-1) + \frac{1}{2} = -\frac{1}{2}$$
    このとき ① より $y^2 = \dfrac{1 - 1}{2} = 0 \implies y = 0$。
  > 💡 讲师批注：求 $y$ 时别忘了正负号 $\pm \dfrac{\sqrt{6}}{4}$ 并做好分母有理化！
- **【最终答案】**
  **$x = \dfrac{1}{2},\; y = \pm\dfrac{\sqrt{6}}{4}$ のとき最大値 $\dfrac{5}{8}$；$x = -1,\; y = 0$ のとき最小値 $-\dfrac{1}{2}$**

---

#### 演習問題 5-(9)
- **【原题重现与翻译】**
  - 原题：$f(x) = |x^2 - 1| - x$ の $-1 \le x \le 2$ における最大値と最小値を求めよ。
  - 中文：求函数 $f(x) = |x^2 - 1| - x$ 在区间 $-1 \le x \le 2$ 上的最大值与最小值。
- **【考点定位】**
  - 含绝对值的分段二次函数图像与闭区间最值。
- **【图解辅助（SVG 矢量图）】**

<svg viewBox="0 0 460 220" width="460" height="220" xmlns="http://www.w3.org/2000/svg" style="background:#fafafa;border:1px solid #e0e0e0;border-radius:6px;">
  <style>
    .title { font: bold 12px sans-serif; fill: #2c3e50; }
    .lbl { font: 11px sans-serif; fill: #333; }
    .math { font: italic 12px serif; fill: #2c3e50; }
    .axis { stroke: #444; stroke-width: 1.2; }
    .seg1 { fill: none; stroke: #2980b9; stroke-width: 2.3; }
    .seg2 { fill: none; stroke: #c0392b; stroke-width: 2.3; }
    .dash { stroke: #7f8c8d; stroke-width: 1; stroke-dasharray: 3,3; }
  </style>
  <text x="15" y="20" class="title">y = |x² - 1| - x（-1 ≤ x ≤ 2）のグラフ</text>
  <!-- O=(180, 125), scaleX=80, scaleY=50 -->
  <line x1="50" y1="125" x2="410" y2="125" class="axis"/>
  <polygon points="410,125 403,121 403,129" fill="#444"/>
  <line x1="180" y1="205" x2="180" y2="35" class="axis"/>
  <polygon points="180,35 176,42 184,42" fill="#444"/>
  <text x="404" y="140" class="math">x</text>
  <text x="188" y="45" class="math">y</text>
  <text x="167" y="140" class="lbl">O</text>
  <!-- Exact Seg1: y=-x^2-x+1 from x=-1 to x=1: P0(100,75), P1(180,25), P2(260,175) -->
  <path d="M 100,75 Q 180,25 260,175" class="seg1"/>
  <!-- Exact Seg2: y=x^2-x-1 from x=1 to x=2: P0=(1,-1)=(260,175), P2=(2,1)=(340,75).
       Slope at x=1 is 2(1)-1=1. Tangent from (1,-1) to x=1.5 gives y=-0.5 -> P1=(300,150). Exact! -->
  <path d="M 260,175 Q 300,150 340,75" class="seg2"/>
  <!-- Key points -->
  <circle cx="100" cy="75" r="3.5" fill="#2980b9"/>
  <circle cx="140" cy="62.5" r="4" fill="#27ae60"/>
  <circle cx="260" cy="175" r="4" fill="#c0392b"/>
  <circle cx="340" cy="75" r="3.5" fill="#c0392b"/>
  <!-- Dashed guides -->
  <line x1="100" y1="75" x2="100" y2="125" class="dash"/>
  <line x1="140" y1="62.5" x2="140" y2="125" class="dash"/>
  <line x1="140" y1="62.5" x2="180" y2="62.5" class="dash"/>
  <line x1="260" y1="125" x2="260" y2="175" class="dash"/>
  <line x1="180" y1="175" x2="260" y2="175" class="dash"/>
  <line x1="340" y1="75" x2="340" y2="125" class="dash"/>
  <!-- Labels -->
  <text x="92" y="140" class="lbl">-1</text>
  <text x="126" y="140" class="lbl">-1/2</text>
  <text x="257" y="120" class="lbl">1</text>
  <text x="337" y="140" class="lbl">2</text>
  <text x="186" y="65" class="lbl" fill="#27ae60" font-weight="bold">5/4 (最大)</text>
  <text x="163" y="179" class="lbl">-1</text>
  <text x="268" y="180" class="lbl" fill="#c0392b" font-weight="bold">最小値 -1</text>
  <text x="346" y="75" class="lbl">(2, 1)</text>
</svg>

- **【分步标准解答】**
  定義域 $-1 \le x \le 2$ において、$x^2 - 1 = (x+1)(x-1)$ の符号により場合分けする：

  - **[1] $-1 \le x \le 1$ のとき**（$x^2 - 1 \le 0$）：
    $$f(x) = -(x^2 - 1) - x = -x^2 - x + 1 = -\left(x + \frac{1}{2}\right)^2 + \frac{5}{4}$$
    - $x = -\dfrac{1}{2}$ のとき最大値 $\dfrac{5}{4}$；
    - 端点の値は $f(-1) = 1,\; f(1) = -1$。

  - **[2] $1 \le x \le 2$ のとき**（$x^2 - 1 \ge 0$）：
    $$f(x) = (x^2 - 1) - x = x^2 - x - 1 = \left(x - \frac{1}{2}\right)^2 - \frac{5}{4}$$
    軸 $x = \dfrac{1}{2}$ は区間 $[1, 2]$ より左側にあるため、この区間では単調増加である：
    - $f(1) = -1$，$f(2) = 4 - 2 - 1 = 1$。

  [1]，[2] のグラフ（上図）より、区間 $-1 \le x \le 2$ 全体での最大値と最小値は次の通りである：
  - **最大値**：$\dfrac{5}{4}$（$x = -\dfrac{1}{2}$ のとき）
  - **最小値**：$-1$（$x = 1$ のとき）
  > 💡 讲师批注：分段函数求最值时，务必在衔接点 $x = 1$ 处验证两段函数值是否相等（均为 $-1$），这既是连续性检验，也是防算错的极佳自查手段！
- **【最终答案】**
  **最大値 $\dfrac{5}{4}$（$x = -\dfrac{1}{2}$ のとき）、最小値 $-1$（$x = 1$ のとき）**

---

#### 演習問題 5-(10)
- **【原题重现与翻译】**
  - 原题：$k$ は定数とする、方程式 $|x^2 - x - 2| = 2x + k$ の異なる実数解の個数を調べよ。
  - 中文：设 $k$ 为常数，讨论方程 $|x^2 - x - 2| = 2x + k$ 的不同实数解的个数。
- **【考点定位】**
  - 含绝对值二次方程的实根个数讨论（**图像平移法**：折返抛物线 $y = |x^2-x-2|$ 与动直线 $y = 2x+k$ 的交点个数）。
- **【图解辅助（SVG 矢量图）】**

<svg viewBox="0 0 540 270" width="540" height="270" xmlns="http://www.w3.org/2000/svg" style="background:#fafafa;border:1px solid #e0e0e0;border-radius:6px;">
  <style>
    .title { font: bold 12px sans-serif; fill: #2c3e50; }
    .lbl { font: 11px sans-serif; fill: #333; }
    .math { font: italic 12px serif; fill: #2c3e50; }
    .axis { stroke: #444; stroke-width: 1.2; }
    .parab { fill: none; stroke: #2c3e50; stroke-width: 2.2; }
    .l1 { stroke: #e67e22; stroke-width: 1.6; stroke-dasharray: 5,3; }
    .l2 { stroke: #2980b9; stroke-width: 1.6; stroke-dasharray: 5,3; }
    .l3 { stroke: #c0392b; stroke-width: 1.8; }
  </style>
  <text x="15" y="20" class="title">y = |x² - x - 2| と 直線 y = 2x + k の共有点の個数</text>
  <!-- O=(210, 215), scaleX=55, scaleY=30 -->
  <line x1="30" y1="215" x2="495" y2="215" class="axis"/>
  <polygon points="495,215 488,211 488,219" fill="#444"/>
  <line x1="210" y1="255" x2="210" y2="35" class="axis"/>
  <polygon points="210,35 206,42 214,42" fill="#444"/>
  <text x="488" y="230" class="math">x</text>
  <text x="218" y="45" class="math">y</text>
  <text x="197" y="230" class="lbl">O</text>
  <!-- Left branch x<=-1: (-2.2, 5.04)->(89, 63.8) to (-1, 0)->(155, 215) -->
  <!-- Exact quadratic bezier from x=-2.2 to x=-1:
       P0=(-2.2, 5.04), P2=(-1,0), slope at -1 is -3. Tangent from (-1,0) to x=-1.6 gives y=1.8 -> P1=(122, 161) -->
  <path d="M 89,64 Q 122,161 155,215" class="parab"/>
  <!-- Middle folded arch -1<=x<=2: y=-x^2+x+2. (-1,0)->(155,215), (0.5,2.25)->(237.5,147.5), (2,0)->(320,215).
       Slope at -1 is +3 -> P1=(0.5, 4.5) -> (237.5, 80) -->
  <path d="M 155,215 Q 237.5,80 320,215" class="parab"/>
  <!-- Right branch x>=2: (2,0)->(320,215) to (3.5, 6.75)->(402.5, 12.5) Wait clamp to y=5.5 (x=3.29):
       Use x=3.2: y=5.04 -> (386, 63.8). Slope at 2 is +3. P1 at x=2.6: y=1.8 -> (353, 161) -->
  <path d="M 320,215 Q 353,161 386,64" class="parab"/>
  <!-- Critical lines y = 2x + k (slope=2 -> in screen dx=55, dy=-60) -->
  <!-- Line 1: k = -4, passes B(2,0)=(320,215). From (1.3,-1.4)->(281,257) to (4.2,4.4)->(441,83) -->
  <line x1="285" y1="253" x2="435" y2="90" class="l1"/>
  <text x="438" y="95" class="lbl" fill="#e67e22">k = -4 (1個)</text>
  <!-- Line 2: k = 2, passes A(-1,0)=(155,215) and (0,2)=(210,155) and (2,6)=(320,35) -->
  <line x1="125" y1="248" x2="315" y2="40" class="l2"/>
  <text x="318" y="45" class="lbl" fill="#2980b9">k = 2 (3個)</text>
  <!-- Line 3: k = 9/4 = 2.25, tangent at (-0.5, 1.25)=(182.5, 177.5) -->
  <line x1="115" y1="244" x2="300" y2="42" class="l3"/>
  <text x="120" y="55" class="lbl" fill="#c0392b" font-weight="bold">k = 9/4 (接線・3個)</text>
  <line x1="165" y1="60" x2="182" y2="173" stroke="#c0392b" stroke-width="1" stroke-dasharray="2,2"/>
  <!-- Key points -->
  <circle cx="155" cy="215" r="3.5" fill="#2980b9"/>
  <circle cx="320" cy="215" r="3.5" fill="#e67e22"/>
  <circle cx="182.5" cy="177.5" r="4" fill="#c0392b"/>
  <text x="148" y="232" class="lbl">-1</text>
  <text x="318" y="232" class="lbl">2</text>
  <text x="216" y="160" class="lbl">2</text>
</svg>

- **【分步标准解答】**
  方程式の異なる実数解の個数は、曲線 $y = |x^2 - x - 2|$ と直線 $y = 2x + k$ の共有点の個数に一致する。
  $x^2 - x - 2 = (x + 1)(x - 2)$ より、曲線 $y = |x^2 - x - 2|$ は次のように表される：
  - $x \le -1,\; x \ge 2$ のとき：$y = x^2 - x - 2 \quad \cdots ①$
  - $-1 < x < 2$ のとき：$y = -x^2 + x + 2 \quad \cdots ②$

  傾き $2$ の直線 $y = 2x + k$ を上下に動かして、重要な境界となる $k$ の値を求める：
  1. **点 $(2, 0)$ を通るとき**：
     $0 = 2(2) + k \implies k = -4$。
     > 💡 讲师批注：检查直线能否与 ① 相切：联立 $x^2 - x - 2 = 2x + k \implies x^2 - 3x - (2+k) = 0$，切点横坐标为 $x = \dfrac{3}{2}$。因为 $\dfrac{3}{2} \in (-1, 2)$ 不在 ① 的定义域内，所以直线与 ① 的有效部分**绝不相切**！当 $k < -4$ 时直线完全在折返抛物线下方，无交点。

  2. **点 $(-1, 0)$ を通るとき**：
     $0 = 2(-1) + k \implies k = 2$。
     このとき、$x = -1$ のほか、$-1 < x < 2$ で $x = 0$、$x \ge 2$ で $x = 4$ にも交わるため、共有点は **3 個**。

  3. **② の部分（$-1 < x < 2$）と接するとき**：
     $-x^2 + x + 2 = 2x + k \implies x^2 + x + (k - 2) = 0$ の判別式 $D = 0$ より：
     $$D = 1^2 - 4(k - 2) = 9 - 4k = 0 \implies k = \frac{9}{4}$$
     このときの接点の $x$ 座標は $x = -\dfrac{1}{2}$ であり、確かに $-1 < -\dfrac{1}{2} < 2$ を満たす（有効）。
     このとき、接点のほかに $x \le -1$ と $x \ge 2$ の枝でそれぞれ 1 個ずつ交わるため、共有点は合計 **3 個**。

  以上の境界値と上のグラフより、$k$ の値に応じた共有点（＝異なる実数解）の個数をまとめると：
  - $k < -4$ のとき：**0 個**
  - $k = -4$ のとき：**1 個**
  - $-4 < k < 2,\quad k > \dfrac{9}{4}$ のとき：**2 個**
  - $k = 2,\quad k = \dfrac{9}{4}$ のとき：**3 個**
  - $2 < k < \dfrac{9}{4}$ のとき：**4 個**
  > 💡 讲师批注：这类压轴题极易漏掉「$k > \dfrac{9}{4}$ 时与左右两支仍有 **2 个**交点」，或者忘记验证切点 $x = -\dfrac{1}{2}$ 是否落在 $(-1, 2)$ 内。记住按 $k$ 从小到大扫过每个临界点，并用特值（如 $k = 2.1,\; k = 3$）抽检，万无一失！
- **【最终答案】**
  **$k < -4$ のとき 0 個；$k = -4$ のとき 1 個；$-4 < k < 2,\; k > \dfrac{9}{4}$ のとき 2 個；$k = 2,\; k = \dfrac{9}{4}$ のとき 3 個；$2 < k < \dfrac{9}{4}$ のとき 4 個**

---

### 第四章 演習問題 1（指数方程式・指数不等式・指数関数の最大最小）

#### 演習問題 1-(1)
- **【原题重现与翻译】**
  - 原题：$4^{x+2} - 2^{x+2} - 32 = 0$（次の方程式を解け）
  - 中文：解指数方程 $4^{x+2} - 2^{x+2} - 32 = 0$。
- **【考点定位】**
  - 换元法（$t = 2^x > 0$）化指数方程为一元二次方程。
- **【分步标准解答】**
  指数法則より $4^{x+2} = 4^2 \cdot 4^x = 16 \cdot (2^x)^2$、$2^{x+2} = 2^2 \cdot 2^x = 4 \cdot 2^x$ であるから、方程式は：
  $$16 \cdot (2^x)^2 - 4 \cdot 2^x - 32 = 0$$
  両辺を $4$ で割ると：
  $$4 \cdot (2^x)^2 - 2^x - 8 = 0$$
  ここで $t = 2^x$ とおくと **$t > 0$** であり、方程式は：
  $$4t^2 - t - 8 = 0$$
  解の公式より：
  $$t = \frac{1 \pm \sqrt{(-1)^2 - 4 \cdot 4 \cdot (-8)}}{2 \cdot 4} = \frac{1 \pm \sqrt{129}}{8}$$
  $t > 0$ かつ $\sqrt{129} > 1$ より、$t = \dfrac{1 - \sqrt{129}}{8} < 0$ は不適である。
  したがって：
  $$2^x = \frac{1 + \sqrt{129}}{8}$$
  対数の定義を用いて $x$ を表すと：
  $$x = \log_2 \frac{1 + \sqrt{129}}{8} = \log_2(1 + \sqrt{129}) - 3$$
  > ⚠️ **教材勘误提示**：原教材第 74 页（`page_0075.jpg`）此时尚未讲授对数函数，却印作 $4^{x+2} - 2^{x+2} - 32 = 0$（解出无理根需用对数表示）。极大概率为原题 **$4^x - 2^{x+2} - 32 = 0$** 误印多加了「$+2$」。若按 $4^x - 2^{x+2} - 32 = 0$ 计算：
  > $$t^2 - 4t - 32 = 0 \implies (t - 8)(t + 4) = 0$$
  > $t > 0$ より $t = 8 \implies 2^x = 2^3 \implies x = 3$。备课时建议同时向学生说明原题严格解与勘误版整数解！
- **【最终答案】**
  **原题严格解：$x = \log_2(1 + \sqrt{129}) - 3$**（若原题系 $4^x - 2^{x+2} - 32 = 0$ 误印，则 **$x = 3$**）

---

#### 演習問題 1-(2)
- **【原题重现与翻译】**
  - 原题：$2 \cdot 4^x - 17 \cdot 2^x + 8 < 0$（次の不等式を解け）
  - 中文：解指数不等式 $2 \cdot 4^x - 17 \cdot 2^x + 8 < 0$。
- **【考点定位】**
  - 换元法（$t = 2^x > 0$）+ 十字相乘法（たすき掛け）+ 指数函数单调性。
- **【分步标准解答】**
  $4^x = (2^2)^x = (2^x)^2$ より、$t = 2^x$ とおくと **$t > 0$** であり、不等式は：
  $$2t^2 - 17t + 8 < 0$$
  たすき掛けにより因数分解すると：
  $$(2t - 1)(t - 8) < 0$$
  $$\frac{1}{2} < t < 8$$
  これは $t > 0$ を満たしている。$t = 2^x$ に戻すと：
  $$2^{-1} < 2^x < 2^3$$
  底 $2$ は $1$ より大きいから（単調増加、不等号の向きはそのまま）：
  $$-1 < x < 3$$
  > 💡 讲师批注：务必写出「**底 $2$ は $1$ より大きいから**」这一核心理由句！若底数在 $0$ 与 $1$ 之间（如 $\frac{1}{2}$），去掉底数时不等号必须反转。验算：$x = 0$ 时 $2 - 17 + 8 = -7 < 0$，成立！
- **【最终答案】**
  **$-1 < x < 3$**

---

#### 演習問題 1-(3)
- **【原题重现与翻译】**
  - 原题：関数 $y = 4^x - 2^{x+2} + 2\;(x \le 2)$ の最大値と最小値を求めよ。
  - 中文：求函数 $y = 4^x - 2^{x+2} + 2\;(x \le 2)$ 的最大值与最小值。
- **【考点定位】**
  - 指数函数换元转化为二次函数求最值（**换元后半开区间 $0 < t \le 4$ 的边界判定**）。
- **【图解辅助（SVG 矢量图）】**

<svg viewBox="0 0 440 210" width="440" height="210" xmlns="http://www.w3.org/2000/svg" style="background:#fafafa;border:1px solid #e0e0e0;border-radius:6px;">
  <style>
    .title { font: bold 12px sans-serif; fill: #2c3e50; }
    .lbl { font: 11px sans-serif; fill: #333; }
    .math { font: italic 12px serif; fill: #2c3e50; }
    .axis { stroke: #444; stroke-width: 1.2; }
    .parab { fill: none; stroke: #2980b9; stroke-width: 2.3; }
    .dash { stroke: #7f8c8d; stroke-width: 1; stroke-dasharray: 3,3; }
  </style>
  <text x="15" y="20" class="title">y = (t - 2)² - 2（0 &lt; t ≤ 4）のグラフ</text>
  <!-- O=(95, 115), scaleT=60, scaleY=30 -->
  <line x1="45" y1="115" x2="395" y2="115" class="axis"/>
  <polygon points="395,115 388,111 388,119" fill="#444"/>
  <line x1="95" y1="195" x2="95" y2="35" class="axis"/>
  <polygon points="95,35 91,42 99,42" fill="#444"/>
  <text x="388" y="130" class="math">t</text>
  <text x="103" y="45" class="math">y</text>
  <text x="82" y="130" class="lbl">O</text>
  <!-- Exact quadratic bezier from t=0 (95,55) to t=4 (335,55), vertex at (2, -2) -> (215, 175).
       Control point P1: midpoint of (95,55) and (335,55) is (215,55). For vertex y=175: 0.5*55+0.5*y1=175 => y1=295 -->
  <path d="M 95,55 Q 215,295 335,55" class="parab"/>
  <!-- Left open circle at (0, 2) = (95, 55) -->
  <circle cx="95" cy="55" r="4.5" fill="#fff" stroke="#2980b9" stroke-width="2"/>
  <!-- Right closed circle at (4, 2) = (335, 55) -->
  <circle cx="335" cy="55" r="4.5" fill="#c0392b"/>
  <!-- Vertex closed circle at (2, -2) = (215, 175) -->
  <circle cx="215" cy="175" r="4.5" fill="#27ae60"/>
  <!-- Guides -->
  <line x1="215" y1="115" x2="215" y2="175" class="dash"/>
  <line x1="95" y1="175" x2="215" y2="175" class="dash"/>
  <line x1="335" y1="55" x2="335" y2="115" class="dash"/>
  <line x1="95" y1="55" x2="335" y2="55" class="dash"/>
  <!-- Labels -->
  <text x="212" y="108" class="lbl">2</text>
  <text x="332" y="130" class="lbl">4</text>
  <text x="80" y="59" class="lbl">2</text>
  <text x="76" y="179" class="lbl">-2</text>
  <text x="105" y="48" class="lbl" fill="#7f8c8d">t=0 は含まない(白丸)</text>
  <text x="295" y="45" class="lbl" fill="#c0392b" font-weight="bold">最大値 2 (t=4)</text>
  <text x="225" y="180" class="lbl" fill="#27ae60" font-weight="bold">最小値 -2 (t=2)</text>
</svg>

- **【分步标准解答】**
  $y = (2^x)^2 - 4 \cdot 2^x + 2$ において、$t = 2^x$ とおく。
  $x \le 2$ であり、底 $2 > 1$ より $2^x$ は単調増加かつ常に正であるから、$t$ の値の範囲は：
  $$0 < t \le 2^2 \implies 0 < t \le 4$$
  > 💡 讲师批注：**极易漏掉左边界 $0 < t$！** 当 $x \to -\infty$ 时 $2^x$ 无限趋近于 $0$ 但永远大于 $0$，所以 $t$ 的取值范围是左开右闭区间 **$0 < t \le 4$**。

  $y$ を $t$ の式で表し平方完成すると：
  $$y = t^2 - 4t + 2 = (t - 2)^2 - 2 \qquad (0 < t \le 4)$$
  グラフ（上図）は下に凸の放物線で、軸は $t = 2$ である。
  - **最大値**：$t = 0$（白丸・含まない）と $t = 4$（黒丸・含む）は軸 $t = 2$ に関して対称であり、$t = 4$ でのみ値 $2$ をとる。
    $t = 4$ のとき $2^x = 4 \implies x = 2$、最大値は **$2$**。
  - **最小値**：頂点 $t = 2$ で最小値 $-2$ をとる。
    $t = 2$ のとき $2^x = 2 \implies x = 1$、最小値は **$-2$**。
  > 💡 讲师批注：如果题目给的是 $x < 2$（开区间 $0 < t < 4$），那么本题就会变成「最大値なし」！本题因为是 $x \le 2$，右端点 $t = 4$ 闭区间能取到，所以最大值 $2$ 存在且唯一在 $x = 2$ 处取得！
- **【最终答案】**
  **$x = 2$ のとき最大値 $2$、$x = 1$ のとき最小値 $-2$**
