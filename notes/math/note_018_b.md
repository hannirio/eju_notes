# 《EJU 教材全解与备课讲义》数学 018（下）（P256–P270）

> **对应源文件**：`work_math/ocr_md/ocr_018_p256-270.md`（種々の数列、漸化式と数列）
> **视觉核对参考图**：`work_math/ref_imgs/page_0262.jpg` – `page_0270.jpg`
> **本册范围**：逐题深度解析（**演習問題 3 (1)–(7)** 与 **演習問題 4 (1)–(2)**）；知识点梳理、考纲对比、日文词汇表与 **演習問題 1–2** 见上册 `note_018_a.md`。

---

## 三、逐题深度解析（下：演習問題 3 & 演習問題 4）

---

### 演習問題 3（種々の数列）

#### 演習問題 3-(1)[1]
- **【原题重现与翻译】**
  - 原题：次の和を求めよ。
    [1] $\displaystyle\sum_{k=1}^{n} (3k^2 - k + 2)$
  - 中文：求 $\displaystyle\sum_{k=1}^{n} (3k^2 - k + 2)$ 的和。
- **【考点定位】**
  - $\sum$ 的线性性质与自然数幂和公式（$\sum k^2,\; \sum k,\; \sum c$）的因式分解化简。
- **【分步标准解答】**
  $$\sum_{k=1}^{n} (3k^2 - k + 2) = 3\sum_{k=1}^{n} k^2 - \sum_{k=1}^{n} k + \sum_{k=1}^{n} 2$$
  $$= 3 \cdot \frac{1}{6}n(n+1)(2n+1) - \frac{1}{2}n(n+1) + 2n$$
  > 💡 讲师批注：常数项 $\sum_{k=1}^{n} 2 = 2n$，初学者极易误写成 $2$！

  $$= \frac{1}{2}n\big\{(n+1)(2n+1) - (n+1) + 4\big\}$$
  > 💡 讲师批注：**日本考场黄金法则**：先提取公因式 $\frac{1}{2}n$，千万不要急着展开！提取后再化简大括号内，计算量减半且不易出错。

  $$= \frac{1}{2}n\big\{(2n^2 + 3n + 1) - n - 1 + 4\big\} = \frac{1}{2}n(2n^2 + 2n + 4) = n(n^2 + n + 2)$$
  > 💡 讲师批注：代入 $n = 1, 2$ 验算：$n=1$ 时原式 $= 3 - 1 + 2 = 4$，结果 $= 1(1+1+2) = 4$；$n=2$ 时原式 $= 4 + (12 - 2 + 2) = 16$，结果 $= 2(4+2+2) = 16$。正确！
- **【最终答案】**
  **$n(n^2 + n + 2)$**

---

#### 演習問題 3-(1)[2]
- **【原题重现与翻译】**
  - 原题：[2] $\displaystyle\sum_{k=1}^{n} (2k+1)(4k^2 - 2k + 1)$
  - 中文：求 $\displaystyle\sum_{k=1}^{n} (2k+1)(4k^2 - 2k + 1)$ 的和。
- **【考点定位】**
  - 立方和公式展开与 $\sum k^3$ 公式的综合应用。
- **【分步标准解答】**
  $(2k+1)(4k^2 - 2k + 1) = (2k)^3 + 1^3 = 8k^3 + 1$ であるから
  > 💡 讲师批注：一眼识破立方和公式 $(a+b)(a^2 - ab + b^2) = a^3 + b^3$，可省去大量展开合并的步骤！

  $$\sum_{k=1}^{n} (2k+1)(4k^2 - 2k + 1) = \sum_{k=1}^{n} (8k^3 + 1) = 8\sum_{k=1}^{n} k^3 + \sum_{k=1}^{n} 1$$
  $$= 8\left\{\frac{1}{2}n(n+1)\right\}^2 + n = 2n^2(n+1)^2 + n$$
  $$= n\big\{2n(n^2 + 2n + 1) + 1\big\} = n(2n^3 + 4n^2 + 2n + 1)$$
  > 💡 讲师批注：代入 $n=1$ 验算：原式 $= 3 \times 3 = 9$，结果 $= 1(2+4+2+1) = 9$；代入 $n=2$ 验算：原式 $= 9 + 5 \times 13 = 74$，结果 $= 2(16+16+4+1) = 74$。完全一致！
- **【最终答案】**
  **$n(2n^3 + 4n^2 + 2n + 1)$**

---

#### 演習問題 3-(1)[3]
- **【原题重现与翻译】**
  - 原题：[3] $\displaystyle\sum_{k=11}^{20} (6k - 1)$
  - 中文：求 $\displaystyle\sum_{k=11}^{20} (6k - 1)$ 的和。
- **【考点定位】**
  - 非 $1$ 起点的 $\sum$ 求和（拆分法或等差数列求和法）。
- **【分步标准解答】**
  **【解法 1：$\sum$ の差で表す】**
  $$\sum_{k=11}^{20} (6k - 1) = \sum_{k=1}^{20} (6k - 1) - \sum_{k=1}^{10} (6k - 1)$$
  ここで、$\displaystyle\sum_{k=1}^{n} (6k - 1) = 6 \cdot \frac{1}{2}n(n+1) - n = 3n^2 + 2n = n(3n + 2)$ であるから
  $$\sum_{k=11}^{20} (6k - 1) = 20 \cdot (3 \cdot 20 + 2) - 10 \cdot (3 \cdot 10 + 2) = 20 \cdot 62 - 10 \cdot 32 = 1240 - 320 = 920$$
  > 💡 讲师批注：注意减掉的是 $\sum_{k=1}^{\mathbf{10}}$ 而不是 $\sum_{k=1}^{11}$！因为第 $11$ 项要保留。

  **【解法 2：等差数列の和として求める（推奨）】**
  $6k - 1$ は $k$ の $1$ 次式（等差数列）であるから、初項（$k=11$）は $6 \cdot 11 - 1 = 65$、末項（$k=20$）は $6 \cdot 20 - 1 = 119$、項数は $20 - 11 + 1 = 10$ である。よって
  $$\sum_{k=11}^{20} (6k - 1) = \frac{1}{2} \cdot 10 \cdot (65 + 119) = 5 \cdot 184 = 920$$
  > 💡 讲师批注：通项是一次式时，直接套等差数列求和公式「$\frac{1}{2} \times \text{项数} \times (\text{首项}+\text{末项})$」最快最稳！
- **【最终答案】**
  **$920$**

---

#### 演習問題 3-(2)[1]
- **【原题重现与翻译】**
  - 原题：次の数列の初項から第 $n$ 項までの和を求めよ。
    [1] $1^2,\; 3^2,\; 5^2,\; \dots$
  - 中文：求数列 $1^2,\; 3^2,\; 5^2,\; \dots$ 从初项到第 $n$ 项的和。
- **【考点定位】**
  - 先归纳第 $k$ 项通项，再转化为 $\sum$ 求和。
- **【分步标准解答】**
  この数列の第 $k$ 項は $(2k - 1)^2$ であるから、求める和 $S_n$ は
  $$S_n = \sum_{k=1}^{n} (2k - 1)^2 = \sum_{k=1}^{n} (4k^2 - 4k + 1)$$
  $$= 4 \cdot \frac{1}{6}n(n+1)(2n+1) - 4 \cdot \frac{1}{2}n(n+1) + n$$
  $$= \frac{1}{3}n\big\{2(n+1)(2n+1) - 6(n+1) + 3\big\}$$
  $$= \frac{1}{3}n\big\{(4n^2 + 6n + 2) - 6n - 6 + 3\big\} = \frac{1}{3}n(4n^2 - 1) = \frac{1}{3}n(2n - 1)(2n + 1)$$
  > 💡 讲师批注：验算 $n=1, 2, 3$：$n=1 \Rightarrow \frac{1}{3}(1)(1)(3) = 1 = 1^2$；$n=2 \Rightarrow \frac{1}{3}(2)(3)(5) = 10 = 1^2+3^2$；$n=3 \Rightarrow \frac{1}{3}(3)(5)(7) = 35 = 1^2+3^2+5^2$。非常漂亮！
- **【最终答案】**
  **$\dfrac{1}{3}n(2n - 1)(2n + 1)$**

---

#### 演習問題 3-(2)[2]
- **【原题重现与翻译】**
  - 原题：[2] $1,\; 1+2,\; 1+2+2^2,\; \dots$
  - 中文：求数列 $1,\; 1+2,\; 1+2+2^2,\; \dots$ 从初项到第 $n$ 项的和。
- **【考点定位】**
  - 通项本身为等比数列之和的双重求和问题。
- **【分步标准解答】**
  この数列の第 $k$ 項 $a_k$ は、初項 $1$、公比 $2$、項数 $k$ の等比数列の和であるから
  $$a_k = 1 + 2 + 2^2 + \dots + 2^{k-1} = \frac{1 \cdot (2^k - 1)}{2 - 1} = 2^k - 1$$
  > 💡 讲师批注：此类「每一项都是一个和式」的数列，**第一步必须先把第 $k$ 项 $a_k$ 化简成封闭公式**，绝不可直接把所有项加在一起乱凑。

  よって、初項から第 $n$ 項までの和 $S_n$ は
  $$S_n = \sum_{k=1}^{n} (2^k - 1) = \sum_{k=1}^{n} 2^k - \sum_{k=1}^{n} 1$$
  ここで、$\displaystyle\sum_{k=1}^{n} 2^k = 2 + 2^2 + \dots + 2^n$ は初項 $2$、公比 $2$、項数 $n$ の等比数列の和であるから
  $$S_n = \frac{2(2^n - 1)}{2 - 1} - n = 2^{n+1} - n - 2$$
  > 💡 讲师批注：注意 $\sum_{k=1}^{n} 2^k$ 的初项是 $2^1 = 2$（不是 $1$）！验算 $n=1 \Rightarrow 4-1-2=1$；$n=2 \Rightarrow 8-2-2=4 = 1+3$；$n=3 \Rightarrow 16-3-2=11 = 1+3+7$。完全正确！
- **【最终答案】**
  **$2^{n+1} - n - 2$**

---

#### 演習問題 3-(3)[1]
- **【原题重现与翻译】**
  - 原题：次の数列の和を求めよ。
    [1] $1\cdot(n+1),\; 2\cdot n,\; 3\cdot(n-1),\; \dots,\; (n-1)\cdot 3,\; n\cdot 2$
  - 中文：求数列 $1\cdot(n+1),\; 2\cdot n,\; 3\cdot(n-1),\; \dots,\; (n-1)\cdot 3,\; n\cdot 2$ 的和。
- **【考点定位】**
  - 含参数 $n$ 的 $\sum$ 求和（区分求和指标 $k$ 与常数 $n$）。
- **【分步标准解答】**
  この数列の項数は $n$ であり、第 $k$ 項（$k = 1, 2, \dots, n$）は、前の因数が $k$、後ろの因数が $(n + 2) - k$ である。
  > 💡 讲师批注：找第 $k$ 项的秘诀：观察「前因数 $+$ 后因数」的和是否恒定！$1+(n+1) = n+2$，$2+n = n+2$，$n+2 = n+2$，所以后因数必为 $n + 2 - k$！

  したがって、求める和 $S$ は
  $$S = \sum_{k=1}^{n} k(n + 2 - k) = \sum_{k=1}^{n} \big\{(n + 2)k - k^2\big\}$$
  $n + 2$ は $k$ に無関係な定数であるから
  $$S = (n + 2)\sum_{k=1}^{n} k - \sum_{k=1}^{n} k^2$$
  $$= (n + 2) \cdot \frac{1}{2}n(n+1) - \frac{1}{6}n(n+1)(2n+1)$$
  $$= \frac{1}{6}n(n+1)\big\{3(n+2) - (2n+1)\big\} = \frac{1}{6}n(n+1)(n+5)$$
  > 💡 讲师批注：验算 $n=1$: $1\cdot 2 = 2$，公式 $\frac{1}{6}(1)(2)(6)=2$；$n=2$: $1\cdot 3 + 2\cdot 2 = 7$，公式 $\frac{1}{6}(2)(3)(7)=7$。正确！
- **【最终答案】**
  **$\dfrac{1}{6}n(n+1)(n+5)$**

---

#### 演習問題 3-(3)[2]
- **【原题重现与翻译】**
  - 原题：[2] $1\cdot 1,\; 3\cdot 3,\; 5\cdot 3^2,\; \dots,\; (2n-1)\cdot 3^{n-1}$
  - 中文：求数列 $1\cdot 1,\; 3\cdot 3,\; 5\cdot 3^2,\; \dots,\; (2n-1)\cdot 3^{n-1}$ 的和。
- **【考点定位】**
  - 「等差 $\times$ 等比」型数列求和——错位相减法（$S - rS$ 法）。
- **【分步标准解答】**
  求める和を $S$ とおくと
  $$S = 1\cdot 1 + 3\cdot 3 + 5\cdot 3^2 + \dots + (2n-1)\cdot 3^{n-1} \qquad \cdots \text{①}$$
  両辺に等比数列部分の公比 $3$ を掛けると
  $$3S = \phantom{1\cdot 1 +} 1\cdot 3 + 3\cdot 3^2 + \dots + (2n-3)\cdot 3^{n-1} + (2n-1)\cdot 3^n \qquad \cdots \text{②}$$
  ① $-$ ② より（$n \ge 2$ のとき）
  $$-2S = 1 + 2\cdot 3 + 2\cdot 3^2 + \dots + 2\cdot 3^{n-1} - (2n-1)\cdot 3^n$$
  $$= 1 + 2(3 + 3^2 + \dots + 3^{n-1}) - (2n-1)\cdot 3^n$$
  > 💡 讲师批注：**两大易错点**：① 中间等比数列 $3 + 3^2 + \dots + 3^{n-1}$ 的初项是 $3$、项数是 **$n - 1$**（不是 $n$！）；② 末尾项是被减去的，前面必须是**负号** $-(2n-1)\cdot 3^n$！

  $$= 1 + 2 \cdot \frac{3(3^{n-1} - 1)}{3 - 1} - (2n-1)\cdot 3^n$$
  $$= 1 + (3^n - 3) - (2n-1)\cdot 3^n = (2 - 2n)\cdot 3^n - 2 = -2(n - 1)\cdot 3^n - 2$$
  両辺を $-2$ で割ると
  $$S = (n - 1)\cdot 3^n + 1$$
  この式は $n = 1$ のとき $(1 - 1)\cdot 3^1 + 1 = 1 = 1\cdot 1$ となり成り立つ。
  > 💡 讲师批注：验算 $n=2$: $1 + 9 = 10$，公式 $(2-1)3^2+1 = 10$；$n=3$: $10 + 5\cdot 9 = 55$，公式 $(3-1)3^3+1 = 55$。100% 准确！
- **【最终答案】**
  **$(n - 1)\cdot 3^n + 1$**

---

#### 演習問題 3-(4)[1]
- **【原题重现与翻译】**
  - 原题：次の数列の一般項を求めよ。
    [1] $2,\; 7,\; 18,\; 35,\; 58,\; \dots$
  - 中文：求数列 $2,\; 7,\; 18,\; 35,\; 58,\; \dots$ 的通项公式。
- **【考点定位】**
  - 阶差数列（階差数列）求通项公式。
- **【分步标准解答】**
  与えられた数列を $\{a_n\}$ とし、その階差数列を $\{b_n\}$ とすると、$\{b_n\}$ は
  $$5,\; 11,\; 17,\; 23,\; \dots$$
  これは初項 $5$、公差 $6$ の等差数列であるから
  $$b_n = 5 + (n - 1)\cdot 6 = 6n - 1$$
  よって、$n \ge 2$ のとき
  $$a_n = a_1 + \sum_{k=1}^{n-1} b_k = 2 + \sum_{k=1}^{n-1} (6k - 1)$$
  $$= 2 + 6 \cdot \frac{1}{2}(n - 1)n - (n - 1)$$
  > 💡 讲师批注：求和上限是 **$n - 1$**，把公式中的 $n$ 全部替换为 $n - 1$：$\sum_{k=1}^{n-1} k = \frac{1}{2}(n-1)n$，$\sum_{k=1}^{n-1} 1 = n - 1$。

  $$= 2 + 3n^2 - 3n - n + 1 = 3n^2 - 4n + 3$$
  $n = 1$ のとき、この式は $3\cdot 1^2 - 4\cdot 1 + 3 = 2 = a_1$ となり成り立つ。
  したがって、すべての自然数 $n$ に対して $a_n = 3n^2 - 4n + 3$ である。
- **【最终答案】**
  **$a_n = 3n^2 - 4n + 3$**

---

#### 演習問題 3-(4)[2]
- **【原题重现与翻译】**
  - 原题：[2] $6,\; 24,\; 60,\; 120,\; 210,\; 336,\; 504,\; \dots$
  - 中文：求数列 $6,\; 24,\; 60,\; 120,\; 210,\; 336,\; 504,\; \dots$ 的通项公式。
- **【考点定位】**
  - 二阶阶差数列（2階の階差数列）求通项公式。
- **【图解辅助（SVG 矢量图）】**

<svg viewBox="0 0 540 148" width="100%" xmlns="http://www.w3.org/2000/svg" style="max-width:540px;background:#fafbfc;border:1px solid #e1e4e8;border-radius:6px;">
  <text x="20" y="34" font-size="12" fill="#1e293b" font-weight="bold">{aₙ}:</text>
  <text x="80" y="34" text-anchor="middle" font-size="13" fill="#0f172a" font-weight="bold">6</text>
  <text x="150" y="34" text-anchor="middle" font-size="13" fill="#0f172a" font-weight="bold">24</text>
  <text x="220" y="34" text-anchor="middle" font-size="13" fill="#0f172a" font-weight="bold">60</text>
  <text x="290" y="34" text-anchor="middle" font-size="13" fill="#0f172a" font-weight="bold">120</text>
  <text x="360" y="34" text-anchor="middle" font-size="13" fill="#0f172a" font-weight="bold">210</text>
  <text x="430" y="34" text-anchor="middle" font-size="13" fill="#0f172a" font-weight="bold">336</text>
  <text x="500" y="34" text-anchor="middle" font-size="13" fill="#0f172a" font-weight="bold">504</text>

  <polyline points="85,42 115,62 145,42" fill="none" stroke="#94a3b8" stroke-width="1.2"/>
  <polyline points="155,42 185,62 215,42" fill="none" stroke="#94a3b8" stroke-width="1.2"/>
  <polyline points="225,42 255,62 285,42" fill="none" stroke="#94a3b8" stroke-width="1.2"/>
  <polyline points="295,42 325,62 355,42" fill="none" stroke="#94a3b8" stroke-width="1.2"/>
  <polyline points="365,42 395,62 425,42" fill="none" stroke="#94a3b8" stroke-width="1.2"/>
  <polyline points="435,42 465,62 495,42" fill="none" stroke="#94a3b8" stroke-width="1.2"/>

  <text x="20" y="80" font-size="12" fill="#2563eb" font-weight="bold">{bₙ}:</text>
  <text x="115" y="80" text-anchor="middle" font-size="13" fill="#2563eb" font-weight="bold">18</text>
  <text x="185" y="80" text-anchor="middle" font-size="13" fill="#2563eb" font-weight="bold">36</text>
  <text x="255" y="80" text-anchor="middle" font-size="13" fill="#2563eb" font-weight="bold">60</text>
  <text x="325" y="80" text-anchor="middle" font-size="13" fill="#2563eb" font-weight="bold">90</text>
  <text x="395" y="80" text-anchor="middle" font-size="13" fill="#2563eb" font-weight="bold">126</text>
  <text x="465" y="80" text-anchor="middle" font-size="13" fill="#2563eb" font-weight="bold">168</text>

  <polyline points="120,88 150,108 180,88" fill="none" stroke="#93c5fd" stroke-width="1.2"/>
  <polyline points="190,88 220,108 250,88" fill="none" stroke="#93c5fd" stroke-width="1.2"/>
  <polyline points="260,88 290,108 320,88" fill="none" stroke="#93c5fd" stroke-width="1.2"/>
  <polyline points="330,88 360,108 390,88" fill="none" stroke="#93c5fd" stroke-width="1.2"/>
  <polyline points="400,88 430,108 460,88" fill="none" stroke="#93c5fd" stroke-width="1.2"/>

  <text x="20" y="128" font-size="12" fill="#dc2626" font-weight="bold">{cₙ}:</text>
  <text x="150" y="128" text-anchor="middle" font-size="13" fill="#dc2626" font-weight="bold">18</text>
  <text x="220" y="128" text-anchor="middle" font-size="13" fill="#dc2626" font-weight="bold">24</text>
  <text x="290" y="128" text-anchor="middle" font-size="13" fill="#dc2626" font-weight="bold">30</text>
  <text x="360" y="128" text-anchor="middle" font-size="13" fill="#dc2626" font-weight="bold">36</text>
  <text x="430" y="128" text-anchor="middle" font-size="13" fill="#dc2626" font-weight="bold">42</text>
  <text x="495" y="128" text-anchor="middle" font-size="11" fill="#dc2626">(公差 6)</text>
</svg>

- **【分步标准解答】**
  与えられた数列を $\{a_n\}$、その階差数列を $\{b_n\}$、さらに $\{b_n\}$ の階差数列を $\{c_n\}$ とする。
  - $\{b_n\}$：$18,\; 36,\; 60,\; 90,\; 126,\; 168,\; \dots$
  - $\{c_n\}$：$18,\; 24,\; 30,\; 36,\; 42,\; \dots$

  $\{c_n\}$ は初項 $18$、公差 $6$ の等差数列であるから
  $$c_n = 18 + (n - 1)\cdot 6 = 6n + 12$$
  よって、$n \ge 2$ のとき
  $$b_n = b_1 + \sum_{k=1}^{n-1} c_k = 18 + \sum_{k=1}^{n-1} (6k + 12)$$
  $$= 18 + 6 \cdot \frac{1}{2}(n - 1)n + 12(n - 1) = 18 + 3n^2 - 3n + 12n - 12 = 3n^2 + 9n + 6$$
  これは $n = 1$ のとき $3 + 9 + 6 = 18 = b_1$ となり成り立つ。

  さらに、$n \ge 2$ のとき
  $$a_n = a_1 + \sum_{k=1}^{n-1} b_k = 6 + \sum_{k=1}^{n-1} (3k^2 + 9k + 6)$$
  $$= 6 + 3 \cdot \frac{1}{6}(n - 1)n(2n - 1) + 9 \cdot \frac{1}{2}(n - 1)n + 6(n - 1)$$
  $$= 6n + \frac{1}{2}n(n - 1)\big\{(2n - 1) + 9\big\} = 6n + \frac{1}{2}n(n - 1)(2n + 8)$$
  $$= 6n + n(n - 1)(n + 4) = n(6 + n^2 + 3n - 4) = n(n^2 + 3n + 2) = n(n + 1)(n + 2)$$
  これは $n = 1$ のとき $1\cdot 2\cdot 3 = 6 = a_1$ となり成り立つ。
  > 💡 讲师批注：直觉洞察：$6 = 1\cdot 2\cdot 3$，$24 = 2\cdot 3\cdot 4$，$60 = 3\cdot 4\cdot 5$，$120 = 4\cdot 5\cdot 6$！二阶阶差数列得到的是 $3$ 次多项式 $n(n+1)(n+2)$。
- **【最终答案】**
  **$a_n = n(n + 1)(n + 2)$**（展開形 $n^3 + 3n^2 + 2n$ も可）

---

#### 演習問題 3-(5)
- **【原题重现与翻译】**
  - 原题：初項から第 $n$ 項までの和 $S_n$ が $S_n = 2n^2 - n$ となる数列 $\{a_n\}$ について
    [1] 一般項 $a_n$ を求めよ。　　[2] 和 $a_1 + a_3 + a_5 + \dots + a_{2n-1}$ を求めよ。
  - 中文：已知数列 $\{a_n\}$ 的前 $n$ 项和为 $S_n = 2n^2 - n$，求：[1] 通项 $a_n$；[2] 和 $a_1 + a_3 + a_5 + \dots + a_{2n-1}$。
- **【考点定位】**
  - 由 $S_n$ 求 $a_n$（$a_1 = S_1$ 与 $a_n = S_n - S_{n-1}$）；奇数项子数列求和。
- **【分步标准解答】**
  - **[1] 一般項 $a_n$**：
    $n = 1$ のとき
    $$a_1 = S_1 = 2\cdot 1^2 - 1 = 1$$
    $n \ge 2$ のとき
    $$a_n = S_n - S_{n-1} = (2n^2 - n) - \big\{2(n - 1)^2 - (n - 1)\big\}$$
    $$= (2n^2 - n) - (2n^2 - 4n + 2 - n + 1) = (2n^2 - n) - (2n^2 - 5n + 3) = 4n - 3$$
    ここで $n = 1$ のとき、$4\cdot 1 - 3 = 1 = a_1$ となり成り立つ。
    よって、すべての自然数 $n$ に対して
    $$a_n = 4n - 3$$
    > 💡 讲师批注：当 $S_n = An^2 + Bn$（**无常数项**）时，$\{a_n\}$ 必为等差数列（且 $n=1$ 自动成立）；若 $S_n$ 含非零常数项，则 $a_1$ 必须分段单写！

  - **[2] 和 $a_1 + a_3 + a_5 + \dots + a_{2n-1}$**：
    $a_{2k-1} = 4(2k - 1) - 3 = 8k - 7$ であるから、求める和は
    $$\sum_{k=1}^{n} a_{2k-1} = \sum_{k=1}^{n} (8k - 7) = 8 \cdot \frac{1}{2}n(n + 1) - 7n = 4n^2 + 4n - 7n = 4n^2 - 3n = n(4n - 3)$$
    > 💡 讲师批注：验算 $n=1$: $a_1 = 1$，公式 $1(1)=1$；$n=2$: $a_1 + a_3 = 1 + 9 = 10$，公式 $2(5)=10$。正确！
- **【最终答案】**
  **[1] $a_n = 4n - 3$　　[2] $n(4n - 3)$**（または $4n^2 - 3n$）

---

#### 演習問題 3-(6)[1]
- **【原题重现与翻译】**
  - 原题：次の数列の和を求めよ。
    [1] $\dfrac{1}{1\cdot 3},\; \dfrac{1}{3\cdot 5},\; \dfrac{1}{5\cdot 7},\; \dots,\; \dfrac{1}{(2n-1)(2n+1)}$
  - 中文：求数列 $\dfrac{1}{1\cdot 3},\; \dfrac{1}{3\cdot 5},\; \dots,\; \dfrac{1}{(2n-1)(2n+1)}$ 的和。
- **【考点定位】**
  - 部分分式分解（裂项相消法）：$\dfrac{1}{AB} = \dfrac{1}{B - A}\left(\dfrac{1}{A} - \dfrac{1}{B}\right)$。
- **【分步标准解答】**
  第 $k$ 項を部分分数に分解すると
  $$\frac{1}{(2k - 1)(2k + 1)} = \frac{1}{2}\left(\frac{1}{2k - 1} - \frac{1}{2k + 1}\right)$$
  > 💡 讲师批注：分母两因数之差 $(2k+1)-(2k-1) = 2$，所以前面必须乘系数 $\dfrac{1}{2}$，切勿遗漏！

  よって、求める和 $S_n$ は
  $$S_n = \sum_{k=1}^{n} \frac{1}{2}\left(\frac{1}{2k - 1} - \frac{1}{2k + 1}\right)$$
  $$= \frac{1}{2}\left\{\left(1 - \frac{1}{3}\right) + \left(\frac{1}{3} - \frac{1}{5}\right) + \left(\frac{1}{5} - \frac{1}{7}\right) + \dots + \left(\frac{1}{2n - 1} - \frac{1}{2n + 1}\right)\right\}$$
  $$= \frac{1}{2}\left(1 - \frac{1}{2n + 1}\right) = \frac{1}{2} \cdot \frac{2n}{2n + 1} = \frac{n}{2n + 1}$$
  > 💡 讲师批注：代入 $n=1 \Rightarrow \frac{1}{3}$，$n=2 \Rightarrow \frac{2}{5} = \frac{1}{3} + \frac{1}{15}$ 验算通过。
- **【最终答案】**
  **$\dfrac{n}{2n + 1}$**

---

#### 演習問題 3-(6)[2]
- **【原题重现与翻译】**
  - 原题：[2] $\dfrac{1}{1\cdot 2\cdot 3},\; \dfrac{1}{2\cdot 3\cdot 4},\; \dfrac{1}{3\cdot 4\cdot 5},\; \dots,\; \dfrac{1}{n(n+1)(n+2)}$
  - 中文：求数列 $\dfrac{1}{1\cdot 2\cdot 3},\; \dfrac{1}{2\cdot 3\cdot 4},\; \dots,\; \dfrac{1}{n(n+1)(n+2)}$ 的和。
- **【考点定位】**
  - 三因数分母的裂项相消法：$\dfrac{1}{k(k+1)(k+2)} = \dfrac{1}{2}\left\{\dfrac{1}{k(k+1)} - \dfrac{1}{(k+1)(k+2)}\right\}$。
- **【分步标准解答】**
  第 $k$ 項を変形すると
  $$\frac{1}{k(k+1)(k+2)} = \frac{1}{2}\left\{\frac{1}{k(k+1)} - \frac{1}{(k+1)(k+2)}\right\}$$
  > 💡 讲师批注：三连积裂项口诀：「**去尾减除头，除以尾减头**」——最大因数 $(k+2)$ 与最小因数 $k$ 之差为 $2$，因此系数为 $\frac{1}{2}$。反向通分验证：$\frac{(k+2) - k}{2k(k+1)(k+2)} = \frac{1}{k(k+1)(k+2)}$，完全一致！

  よって、求める和 $S_n$ は
  $$S_n = \frac{1}{2}\left\{\left(\frac{1}{1\cdot 2} - \frac{1}{2\cdot 3}\right) + \left(\frac{1}{2\cdot 3} - \frac{1}{3\cdot 4}\right) + \dots + \left(\frac{1}{n(n+1)} - \frac{1}{(n+1)(n+2)}\right)\right\}$$
  $$= \frac{1}{2}\left\{\frac{1}{2} - \frac{1}{(n+1)(n+2)}\right\} = \frac{1}{2} \cdot \frac{(n+1)(n+2) - 2}{2(n+1)(n+2)}$$
  $$= \frac{n^2 + 3n}{4(n+1)(n+2)} = \frac{n(n + 3)}{4(n+1)(n+2)}$$
  > 💡 讲师批注：验算 $n=1$: $\frac{1\cdot 4}{4\cdot 2\cdot 3} = \frac{1}{6}$；$n=2$: $\frac{2\cdot 5}{4\cdot 3\cdot 4} = \frac{5}{24} = \frac{1}{6} + \frac{1}{24}$。正确！
- **【最终答案】**
  **$\dfrac{n(n + 3)}{4(n + 1)(n + 2)}$**

---

#### 演習問題 3-(6)[3]
- **【原题重现与翻译】**
  - 原题：[3] $\dfrac{1}{1+\sqrt{3}},\; \dfrac{1}{\sqrt{2}+\sqrt{4}},\; \dfrac{1}{\sqrt{3}+\sqrt{5}},\; \dots,\; \dfrac{1}{\sqrt{n}+\sqrt{n+2}}$
  - 中文：求数列 $\dfrac{1}{1+\sqrt{3}},\; \dfrac{1}{\sqrt{2}+\sqrt{4}},\; \dots,\; \dfrac{1}{\sqrt{n}+\sqrt{n+2}}$ 的和。
- **【考点定位】**
  - 分母有理化后的**隔项相消**求和（差 $2$ 抵消，首尾各留 $2$ 项）。
- **【图解辅助（SVG 矢量图）】**

<svg viewBox="0 0 540 120" width="100%" xmlns="http://www.w3.org/2000/svg" style="max-width:540px;background:#fafbfc;border:1px solid #e1e4e8;border-radius:6px;">
  <text x="18" y="34" font-size="12" fill="#334155" font-weight="bold">2Sₙ =</text>
  <text x="64" y="34" font-size="12" fill="#475569">(</text>
  <text x="72" y="34" font-size="12" fill="#94a3b8" text-decoration="line-through">√3</text>
  <text x="92" y="34" font-size="12" fill="#dc2626" font-weight="bold">- √1</text>
  <text x="118" y="34" font-size="12" fill="#475569">) + (</text>
  <text x="145" y="34" font-size="12" fill="#94a3b8" text-decoration="line-through">√4</text>
  <text x="165" y="34" font-size="12" fill="#dc2626" font-weight="bold">- √2</text>
  <text x="191" y="34" font-size="12" fill="#475569">) + (</text>
  <text x="218" y="34" font-size="12" fill="#94a3b8" text-decoration="line-through">√5</text>
  <text x="238" y="34" font-size="12" fill="#94a3b8" text-decoration="line-through">- √3</text>
  <text x="265" y="34" font-size="12" fill="#475569">) + ... + (</text>
  <text x="322" y="34" font-size="12" fill="#2563eb" font-weight="bold">√(n+1)</text>
  <text x="366" y="34" font-size="12" fill="#94a3b8" text-decoration="line-through">- √(n-1)</text>
  <text x="415" y="34" font-size="12" fill="#475569">) + (</text>
  <text x="442" y="34" font-size="12" fill="#2563eb" font-weight="bold">√(n+2)</text>
  <text x="486" y="34" font-size="12" fill="#94a3b8" text-decoration="line-through">- √n</text>
  <text x="515" y="34" font-size="12" fill="#475569">)</text>

  <path d="M 79 42 Q 165 78 250 42" fill="none" stroke="#94a3b8" stroke-width="1.3" stroke-dasharray="3,2"/>
  <text x="165" y="72" text-anchor="middle" font-size="10" fill="#64748b">隔 1 项抵消 (√3 与 -√3)</text>

  <rect x="65" y="84" width="410" height="26" rx="5" fill="#eff6ff" stroke="#3b82f6" stroke-width="1.2"/>
  <text x="270" y="101" text-anchor="middle" font-size="12" fill="#1e3a8a" font-weight="bold">保留项：前留 2 个负项 (-1, -√2)，后留 2 个正项 (+√(n+1), +√(n+2))</text>
</svg>

- **【分步标准解答】**
  第 $k$ 項の分母を有理化すると
  $$\frac{1}{\sqrt{k} + \sqrt{k+2}} = \frac{\sqrt{k+2} - \sqrt{k}}{(\sqrt{k+2} + \sqrt{k})(\sqrt{k+2} - \sqrt{k})} = \frac{\sqrt{k+2} - \sqrt{k}}{(k+2) - k} = \frac{1}{2}\left(\sqrt{k+2} - \sqrt{k}\right)$$
  よって、$n \ge 2$ のとき求める和 $S_n$ は
  $$S_n = \frac{1}{2}\Big\{(\sqrt{3} - \sqrt{1}) + (\sqrt{4} - \sqrt{2}) + (\sqrt{5} - \sqrt{3}) + \dots + (\sqrt{n+1} - \sqrt{n-1}) + (\sqrt{n+2} - \sqrt{n})\Big\}$$
  $$= \frac{1}{2}\left(\sqrt{n+1} + \sqrt{n+2} - 1 - \sqrt{2}\right)$$
  $n = 1$ のとき、この式は $\dfrac{1}{2}(\sqrt{2} + \sqrt{3} - 1 - \sqrt{2}) = \dfrac{\sqrt{3} - 1}{2} = \dfrac{1}{1 + \sqrt{3}}$ となり成り立つ。
  > 💡 讲师批注：**最高频失分点**：因为下标相差 $2$（$k+2$ 与 $k$），抵消时是**隔项相消**，必须**首尾各留 $2$ 项**！切忌惯性地只留首尾各 $1$ 项！另外，$n=1$ 时虽然写不出两项，但最终公式依然成立，务必补一句验证。
- **【最终答案】**
  **$\dfrac{1}{2}\left(\sqrt{n+1} + \sqrt{n+2} - 1 - \sqrt{2}\right)$**

---

#### 演習問題 3-(7)
- **【原题重现与翻译】**
  - 原题：奇数の数列を $1 \mid 3, 5 \mid 7, 9, 11 \mid 13, 15, 17, 19 \mid 21, \dots$ のように、第 $n$ 群が $n$ 個の数を含むように分けるとき
    [1] 第 $n$ 群の最初の奇数を求めよ。
    [2] 第 $n$ 群の総和を求めよ。
    [3] $301$ は第何群の何番目に並ぶ数か。
  - 中文：将奇数列按 $1 \mid 3, 5 \mid 7, 9, 11 \mid 13, 15, 17, 19 \mid 21, \dots$ 的方式分组，使得第 $n$ 群包含 $n$ 个数，求：
    [1] 第 $n$ 群的第一个奇数；[2] 第 $n$ 群的总和；[3] $301$ 排在第几群的第几个位置？
- **【考点定位】**
  - 群数列（群数列）的标准三连问：首项定位、群内求和、反查位置。
- **【图解辅助（SVG 矢量图）】**

<svg viewBox="0 0 540 128" width="100%" xmlns="http://www.w3.org/2000/svg" style="max-width:540px;background:#fafbfc;border:1px solid #e1e4e8;border-radius:6px;">
  <rect x="16" y="32" width="44" height="36" rx="5" fill="#eff6ff" stroke="#3b82f6"/>
  <text x="38" y="24" text-anchor="middle" font-size="10" fill="#1d4ed8">第1群(1個)</text>
  <text x="38" y="55" text-anchor="middle" font-size="12" fill="#0f172a" font-weight="bold">1</text>

  <rect x="72" y="32" width="76" height="36" rx="5" fill="#eff6ff" stroke="#3b82f6"/>
  <text x="110" y="24" text-anchor="middle" font-size="10" fill="#1d4ed8">第2群(2個)</text>
  <text x="110" y="55" text-anchor="middle" font-size="12" fill="#0f172a" font-weight="bold">3, 5</text>

  <rect x="160" y="32" width="102" height="36" rx="5" fill="#eff6ff" stroke="#3b82f6"/>
  <text x="211" y="24" text-anchor="middle" font-size="10" fill="#1d4ed8">第3群(3個)</text>
  <text x="211" y="55" text-anchor="middle" font-size="12" fill="#0f172a" font-weight="bold">7, 9, 11</text>

  <text x="285" y="55" text-anchor="middle" font-size="14" fill="#64748b">…</text>

  <rect x="308" y="32" width="214" height="36" rx="5" fill="#fef2f2" stroke="#dc2626" stroke-width="1.5"/>
  <text x="415" y="24" text-anchor="middle" font-size="10" fill="#dc2626" font-weight="bold">第 n 群 (n個)</text>
  <text x="415" y="55" text-anchor="middle" font-size="12" fill="#991b1b" font-weight="bold">n²-n+1,  n²-n+3,  …,  n²+n-1</text>

  <path d="M 16 78 L 16 86 L 298 86 L 298 78" fill="none" stroke="#475569" stroke-width="1.3"/>
  <text x="157" y="106" text-anchor="middle" font-size="11" fill="#334155">前 n-1 群総項数 = 1 + 2 + … + (n-1) = n(n-1)/2</text>
  <text x="415" y="106" text-anchor="middle" font-size="11" fill="#dc2626" font-weight="bold">第 n 群の和 = n³</text>
</svg>

- **【分步标准解答】**
  もとの奇数の数列は、第 $m$ 項が $2m - 1$ で表される。

  - **[1] 第 $n$ 群の最初の奇数**：
    $n \ge 2$ のとき、第 $1$ 群から第 $(n - 1)$ 群までに含まれる数の総数は
    $$1 + 2 + 3 + \dots + (n - 1) = \frac{1}{2}(n - 1)n$$
    したがって、第 $n$ 群の最初の数は、もとの数列の最初から数えて $\left\{\dfrac{1}{2}n(n - 1) + 1\right\}$ 番目の奇数である。
    よって、求める数は
    $$2\left\{\frac{1}{2}n(n - 1) + 1\right\} - 1 = n(n - 1) + 2 - 1 = n^2 - n + 1$$
    これは $n = 1$ のとき $1^2 - 1 + 1 = 1$ となり、第 $1$ 群の最初の数 $1$ と一致する。
    > 💡 讲师批注：**群数列万能两步模板**：① 算前 $n-1$ 群的总项数；② 加 $1$ 得到第 $n$ 群首项在原数列中的「总序号」，再代入原数列通项公式！

  - **[2] 第 $n$ 群の総和**：
    第 $n$ 群は、初項 $n^2 - n + 1$、公差 $2$、項数 $n$ の等差数列であるから、その総和 $S_n$ は
    $$S_n = \frac{1}{2}n\big\{2(n^2 - n + 1) + (n - 1)\cdot 2\big\} = \frac{1}{2}n(2n^2 - 2n + 2 + 2n - 2) = \frac{1}{2}n \cdot 2n^2 = n^3$$
    > 💡 讲师批注：极其优美的结论！第 $1$ 群和 $1=1^3$，第 $2$ 群和 $3+5=8=2^3$，第 $3$ 群和 $7+9+11=27=3^3$，第 $4$ 群和 $13+15+17+19=64=4^3$。

  - **[3] $301$ の位置**：
    $301$ がもとの奇数の数列の第 $m$ 項であるとすると
    $$2m - 1 = 301 \implies m = 151$$
    $301$（第 $151$ 番目の数）が第 $n$ 群に含まれる条件は、第 $(n - 1)$ 群までの総数より大きく、第 $n$ 群までの総数以下であること、すなわち
    $$\frac{1}{2}(n - 1)n < 151 \le \frac{1}{2}n(n + 1) \iff (n - 1)n < 302 \le n(n + 1)$$
    ここで、$16 \cdot 17 = 272$、$17 \cdot 18 = 306$ であるから、不等式を満たす自然数 $n$ は $n = 17$ である。
    第 $16$ 群までに含まれる数の総数は $\dfrac{1}{2} \cdot 16 \cdot 17 = 136$ 個であるから、第 $17$ 群での順番は
    $$151 - 136 = 15 \text{ 番目}$$
    > 💡 讲师批注：验算：第 $17$ 群首项 $= 17^2 - 17 + 1 = 273$，第 $15$ 个数 $= 273 + (15 - 1) \times 2 = 273 + 28 = 301$。分毫不差！
- **【最终答案】**
  **[1] $n^2 - n + 1$　　[2] $n^3$　　[3] 第 $17$ 群の $15$ 番目**

---

### 演習問題 4（漸化式と数列）

#### 演習問題 4-(1)[1]
- **【原题重现与翻译】**
  - 原题：次の条件によって定められる数列 $\{a_n\}$ の一般項を求めよ。
    [1] $a_1 = -3,\; a_{n+1} = a_n + 4$
  - 中文：求由 $a_1 = -3,\; a_{n+1} = a_n + 4$ 确定的数列 $\{a_n\}$ 的通项公式。
- **【考点定位】**
  - 等差数列型递推公式：$a_{n+1} - a_n = d$。
- **【分步标准解答】**
  漸化式より $a_{n+1} - a_n = 4$ であるから、数列 $\{a_n\}$ は初項 $a_1 = -3$、公差 $4$ の等差数列である。
  よって
  $$a_n = -3 + (n - 1)\cdot 4 = 4n - 7$$
  > 💡 讲师批注：验算：$a_1 = 4 - 7 = -3$，$a_2 = 1 = -3 + 4$。正确！
- **【最终答案】**
  **$a_n = 4n - 7$**

---

#### 演習問題 4-(1)[2]
- **【原题重现与翻译】**
  - 原题：[2] $a_1 = 4,\; 2a_{n+1} + 3a_n = 0$
  - 中文：求由 $a_1 = 4,\; 2a_{n+1} + 3a_n = 0$ 确定的数列 $\{a_n\}$ 的通项公式。
- **【考点定位】**
  - 等比数列型递推公式：$a_{n+1} = r a_n$。
- **【分步标准解答】**
  漸化式を変形すると
  $$a_{n+1} = -\frac{3}{2}a_n$$
  よって、数列 $\{a_n\}$ は初項 $a_1 = 4$、公比 $-\dfrac{3}{2}$ の等比数列であるから
  $$a_n = 4\left(-\frac{3}{2}\right)^{n-1}$$
  > 💡 讲师批注：注意移项时的负号！验算 $a_1 = 4$，$a_2 = -6$，代入 $2(-6) + 3(4) = 0$ 成立。
- **【最终答案】**
  **$a_n = 4\left(-\dfrac{3}{2}\right)^{n-1}$**

---

#### 演習問題 4-(1)[3]
- **【原题重现与翻译】**
  - 原题：[3] $a_1 = 1,\; a_{n+1} = a_n + 2^n - 3n + 1$
  - 中文：求由 $a_1 = 1,\; a_{n+1} = a_n + 2^n - 3n + 1$ 确定的数列 $\{a_n\}$ 的通项公式。
- **【考点定位】**
  - 阶差数列型递推公式：$a_{n+1} - a_n = f(n)$（混合指数项与一次项的 $\sum$ 求和）。
- **【分步标准解答】**
  漸化式より $a_{n+1} - a_n = 2^n - 3n + 1$ であるから、数列 $\{a_n\}$ の階差数列の一般項は $b_n = 2^n - 3n + 1$ である。
  よって、$n \ge 2$ のとき
  $$a_n = a_1 + \sum_{k=1}^{n-1} (2^k - 3k + 1)$$
  $$= 1 + \sum_{k=1}^{n-1} 2^k - 3\sum_{k=1}^{n-1} k + \sum_{k=1}^{n-1} 1$$
  $$= 1 + \frac{2(2^{n-1} - 1)}{2 - 1} - 3 \cdot \frac{1}{2}(n - 1)n + (n - 1)$$
  > 💡 讲师批注：再次提醒：$\sum_{k=1}^{n-1} 2^k$ 是初项 $2$、公比 $2$、项数 **$n - 1$** 的等比数列求和，结果是 $2(2^{n-1} - 1) = 2^n - 2$！

  $$= 1 + (2^n - 2) - \frac{3}{2}n^2 + \frac{3}{2}n + n - 1 = 2^n - \frac{3}{2}n^2 + \frac{5}{2}n - 2$$
  $n = 1$ のとき、この式は $2^1 - \dfrac{3}{2} + \dfrac{5}{2} - 2 = 1 = a_1$ となり成り立つ。
  > 💡 讲师批注：强烈建议用递推式手算 $a_2, a_3$ 验算！递推得 $a_2 = 1 + 2 - 3 + 1 = 1$，$a_3 = 1 + 4 - 6 + 1 = 0$。代入通项：$n=2 \Rightarrow 4 - 6 + 5 - 2 = 1$；$n=3 \Rightarrow 8 - \frac{27}{2} + \frac{15}{2} - 2 = 0$。完全吻合！
- **【最终答案】**
  **$a_n = 2^n - \dfrac{3}{2}n^2 + \dfrac{5}{2}n - 2$**

---

#### 演習問題 4-(2)[1]
- **【原题重现与翻译】**
  - 原题：次の条件によって定められる数列 $\{a_n\}$ の一般項を求めよ。
    [1] $a_1 = 6,\; a_{n+1} = 4a_n - 3$
  - 中文：求由 $a_1 = 6,\; a_{n+1} = 4a_n - 3$ 确定的数列 $\{a_n\}$ 的通项公式。
- **【考点定位】**
  - 线性常数型递推公式 $a_{n+1} = pa_n + q$（特性方程式法）。
- **【图解辅助（SVG 矢量图）】**

<svg viewBox="0 0 540 105" width="100%" xmlns="http://www.w3.org/2000/svg" style="max-width:540px;background:#fafbfc;border:1px solid #e1e4e8;border-radius:6px;">
  <defs>
    <marker id="arr-g" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#2563eb"/>
    </marker>
  </defs>
  <rect x="14" y="28" width="138" height="48" rx="6" fill="#fff7ed" stroke="#ea580c" stroke-width="1.5"/>
  <text x="83" y="48" text-anchor="middle" font-size="11" fill="#9a3412" font-weight="bold">原漸化式</text>
  <text x="83" y="66" text-anchor="middle" font-size="12" fill="#c2410c">aₙ₊₁ = 4aₙ - 3</text>

  <line x1="154" y1="52" x2="188" y2="52" stroke="#2563eb" stroke-width="1.6" marker-end="url(#arr-g)"/>
  <text x="171" y="42" text-anchor="middle" font-size="9" fill="#1d4ed8">α=4α-3</text>
  <text x="171" y="68" text-anchor="middle" font-size="9" fill="#1d4ed8">⇒ α=1</text>

  <rect x="192" y="28" width="154" height="48" rx="6" fill="#eff6ff" stroke="#2563eb" stroke-width="1.5"/>
  <text x="269" y="48" text-anchor="middle" font-size="11" fill="#1e40af" font-weight="bold">等比数列型へ帰着</text>
  <text x="269" y="66" text-anchor="middle" font-size="12" fill="#1d4ed8">aₙ₊₁ - 1 = 4(aₙ - 1)</text>

  <line x1="348" y1="52" x2="380" y2="52" stroke="#2563eb" stroke-width="1.6" marker-end="url(#arr-g)"/>

  <rect x="384" y="28" width="142" height="48" rx="6" fill="#ecfdf5" stroke="#059669" stroke-width="1.5"/>
  <text x="455" y="48" text-anchor="middle" font-size="11" fill="#065f46" font-weight="bold">一般項</text>
  <text x="455" y="66" text-anchor="middle" font-size="12" fill="#047857" font-weight="bold">aₙ = 5 · 4ⁿ⁻¹ + 1</text>
</svg>

- **【分步标准解答】**
  特性方程式 $\alpha = 4\alpha - 3$ を解くと $\alpha = 1$ である。
  よって、与えられた漸化式を変形すると
  $$a_{n+1} - 1 = 4(a_n - 1)$$
  > 💡 讲师批注：把原式写开验算：$a_{n+1} - 1 = 4a_n - 4 \iff a_{n+1} = 4a_n - 3$，完全等价。

  したがって、数列 $\{a_n - 1\}$ は初項 $a_1 - 1 = 6 - 1 = 5$、公比 $4$ の等比数列であるから
  $$a_n - 1 = 5 \cdot 4^{n-1}$$
  ゆえに
  $$a_n = 5 \cdot 4^{n-1} + 1$$
  > 💡 讲师批注：验算：$a_1 = 5 + 1 = 6$；$a_2 = 20 + 1 = 21 = 4(6) - 3$；$a_3 = 80 + 1 = 81 = 4(21) - 3$。准确无误！
- **【最终答案】**
  **$a_n = 5 \cdot 4^{n-1} + 1$**

---

#### 演習問題 4-(2)[2]
- **【原题重现与翻译】**
  - 原题：[2] $a_1 = 1,\; a_{n+1} = 3a_n + 4n$
  - 中文：求由 $a_1 = 1,\; a_{n+1} = 3a_n + 4n$ 确定的数列 $\{a_n\}$ 的通项公式。
- **【考点定位】**
  - 线性一次式型递推公式 $a_{n+1} = pa_n + f(n)$（待定系数法构造等比数列 / 阶差数列法）。
- **【分步标准解答】**
  **【解法 1：$a_n - g(n)$ を利用して等比数列に帰着する（推奨）】**
  与えられた漸化式を、定数 $p, q$ を用いて
  $$a_{n+1} + p(n + 1) + q = 3(a_n + pn + q)$$
  の形に変形することを考える。展開して整理すると
  $$a_{n+1} = 3a_n + 2pn + (2q - p)$$
  これをもとの漸化式 $a_{n+1} = 3a_n + 4n$ と係数比較すると
  $$\begin{cases} 2p = 4 \\ 2q - p = 0 \end{cases} \implies p = 2,\; q = 1$$
  > 💡 讲师批注：待定系数法的优势在于**一步归结为等比数列，完全不需要计算阶差数列求和**，计算量小且零出错率！

  したがって、漸化式は
  $$a_{n+1} + 2(n + 1) + 1 = 3(a_n + 2n + 1)$$
  と変形できる。よって、数列 $\{a_n + 2n + 1\}$ は初項 $a_1 + 2\cdot 1 + 1 = 1 + 3 = 4$、公比 $3$ の等比数列であるから
  $$a_n + 2n + 1 = 4 \cdot 3^{n-1}$$
  ゆえに
  $$a_n = 4 \cdot 3^{n-1} - 2n - 1$$

  **【解法 2：階差数列を利用する（別解）】**
  $a_{n+1} = 3a_n + 4n \cdots$ ① において $n$ を $n + 1$ に置き換えると
  $$a_{n+2} = 3a_{n+1} + 4(n + 1) \qquad \cdots \text{②}$$
  ② $-$ ① より
  $$a_{n+2} - a_{n+1} = 3(a_{n+1} - a_n) + 4$$
  ここで $b_n = a_{n+1} - a_n$ とおくと、$a_2 = 3\cdot 1 + 4\cdot 1 = 7$ より $b_1 = a_2 - a_1 = 6$ であり、漸化式は $b_{n+1} = 3b_n + 4$ となる。
  変形して $b_{n+1} + 2 = 3(b_n + 2)$。初項 $b_1 + 2 = 8$、公比 $3$ より
  $$b_n + 2 = 8 \cdot 3^{n-1} \implies b_n = 8 \cdot 3^{n-1} - 2$$
  よって $n \ge 2$ のとき
  $$a_n = a_1 + \sum_{k=1}^{n-1} (8 \cdot 3^{k-1} - 2) = 1 + 8 \cdot \frac{3^{n-1} - 1}{3 - 1} - 2(n - 1) = 4 \cdot 3^{n-1} - 2n - 1$$
  これは $n = 1$ のとき $4 - 2 - 1 = 1 = a_1$ となり成り立つ。
  > 💡 讲师批注：两种解法得到完全一致的答案！再代入 $n=1, 2, 3$ 验算：$a_1 = 1$，$a_2 = 12 - 4 - 1 = 7 = 3(1) + 4(1)$，$a_3 = 36 - 6 - 1 = 29 = 3(7) + 4(2)$。完美！
- **【最终答案】**
  **$a_n = 4 \cdot 3^{n-1} - 2n - 1$**
