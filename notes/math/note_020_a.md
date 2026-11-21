# 《EJU 教材全解与备课讲义》数学 020-A（P286–P300 上篇：知识点总览 & 数列极限）

> **对应源文件**：`work_math/ocr_md/ocr_020_p286-300.md`（数学Ⅲ《極限》之「数列の極限」「無限級数」「関数の極限」）
> **视觉核对参考图**：`work_math/ref_imgs/page_0286.jpg` – `page_0300.jpg`（其中 `page_0287.jpg`、`page_0293.jpg` 为教材留白页）
> **分篇说明**：本切片题量较大（共 34 道小题），为确保推导绝不跳步，拆分为 `note_020_a.md`（全切片知识梳理 + 词汇读法 + 演習問題 1 全 20 小题）与 `note_020_b.md`（演習問題 2 全 10 题 + 演習問題 3 全 4 小题）。

---

## 一、国内高中基础知识点唤醒与 EJU 考纲差异对比

本切片对应日本高中 **数学Ⅲ《極限》** 的全部核心框架，涵盖 **数列极限（数列の極限）**、**无穷级数（無限級数）** 与 **函数极限（関数の極限）** 三大板块。国内新课标高中已删去大部分极限与无穷级数内容（移至大学高等数学），而 EJU 理系数学将本部分列为**绝对高频必考模块**，务必从零系统建立规范意识。

### 1.1 数列的极限与等比数列 $\{r^n\}$ 的收敛条件

- **夹逼定理（はさみうちの原理）**：
  - 若对所有 $n$ 有 $a_n \le c_n \le b_n$，且 $\lim_{n\to\infty} a_n = \lim_{n\to\infty} b_n = \alpha$，则 $\lim_{n\to\infty} c_n = \alpha$。
  - 常用推论：由 $-|a_n| \le a_n \le |a_n|$，若 $\lim_{n\to\infty} |a_n| = 0$，则 $\lim_{n\to\infty} a_n = 0$。
- **等比数列 $\{r^n\}$ 的极限与收敛条件**：
  - $r > 1$ 时：$\lim_{n\to\infty} r^n = \infty$（正无穷大发散）
  - $r = 1$ 时：$\lim_{n\to\infty} r^n = 1$（收敛于 $1$）
  - $-1 < r < 1$ 时：$\lim_{n\to\infty} r^n = 0$（收敛于 $0$）
  - $r \le -1$ 时：震荡发散（振動する・極限なし）
  - **核心结论**：数列 $\{r^n\}$ 收敛的**必要充分条件**是 **$-1 < r \le 1$**（特别注意右侧包含等号 $r = 1$！）。

<svg viewBox="0 0 520 115" width="520" height="115" xmlns="http://www.w3.org/2000/svg">
  <rect x="0" y="0" width="520" height="115" fill="#f8fafc" rx="8"/>
  <text x="20" y="24" font-size="13" font-weight="bold" fill="#1e293b">数列 {rⁿ} 的收敛与发散区间（-1 &lt; r ≤ 1）</text>
  <!-- 数轴 -->
  <line x1="40" y1="75" x2="480" y2="75" stroke="#334155" stroke-width="2"/>
  <polygon points="480,75 472,71 472,79" fill="#334155"/>
  <text x="488" y="80" font-size="13" font-style="italic" fill="#334155">r</text>
  <!-- 区间高亮 -->
  <line x1="40" y1="55" x2="180" y2="55" stroke="#ef4444" stroke-width="3" stroke-dasharray="5,3"/>
  <line x1="180" y1="55" x2="340" y2="55" stroke="#10b981" stroke-width="4"/>
  <line x1="340" y1="55" x2="465" y2="55" stroke="#f59e0b" stroke-width="3"/>
  <!-- 端点垂线与实心/空心点 -->
  <line x1="180" y1="55" x2="180" y2="75" stroke="#64748b" stroke-width="1" stroke-dasharray="3,2"/>
  <line x1="340" y1="55" x2="340" y2="75" stroke="#64748b" stroke-width="1" stroke-dasharray="3,2"/>
  <!-- r = -1 空心点（不收敛） -->
  <circle cx="180" cy="55" r="5" fill="#ffffff" stroke="#10b981" stroke-width="2.5"/>
  <circle cx="180" cy="75" r="3" fill="#334155"/>
  <text x="172" y="96" font-size="13" fill="#1e293b">-1</text>
  <!-- r = 1 实心点（收敛于1） -->
  <circle cx="340" cy="55" r="5" fill="#10b981" stroke="#047857" stroke-width="2"/>
  <circle cx="340" cy="75" r="3" fill="#334155"/>
  <text x="336" y="96" font-size="13" fill="#1e293b">1</text>
  <!-- 文字标签 -->
  <text x="72" y="45" font-size="12" fill="#dc2626" font-weight="bold">振動発散 (r ≤ -1)</text>
  <text x="208" y="45" font-size="12" fill="#059669" font-weight="bold">収束 (-1 &lt; r ≤ 1)</text>
  <text x="362" y="45" font-size="12" fill="#d97706" font-weight="bold">発散 +∞ (r &gt; 1)</text>
  <text x="315" y="109" font-size="11" fill="#059669">r=1 时极限为 1</text>
</svg>

### 1.2 无穷级数与无穷等比级数（無限級数）

- **定义**：对于无穷数列 $\{a_n\}$，称 $\sum_{n=1}^{\infty} a_n = a_1 + a_2 + \dots + a_n + \dots$ 为无穷级数；称前 $n$ 项和 $S_n = \sum_{k=1}^{n} a_k$ 为**第 $n$ 项部分和（部分和）**。
  - 若 $\lim_{n\to\infty} S_n = S$（有限值），则称无穷级数收敛，和为 $S$；若 $\{S_n\}$ 发散，则无穷级数发散。
- **收敛的必要条件（发散判定法）**：
  1. 無限級数 $\sum_{n=1}^{\infty} a_n$ が収束する $\implies \lim_{n\to\infty} a_n = 0$（注意：**逆命题不成立！**经典反例：调和级数 $\sum_{n=1}^{\infty} \frac{1}{n}$ 满足 $\lim \frac{1}{n} = 0$，但级数发散至 $\infty$）。
  2. 逆否命题（対偶）：$\lim_{n\to\infty} a_n \neq 0$（或极限不存在）$\implies$ 無限級数 $\sum_{n=1}^{\infty} a_n$ は発散する。
- **无穷等比级数 $\sum_{n=1}^{\infty} ar^{n-1} = a + ar + ar^2 + \dots$ 的收敛条件与求和**：
  - **$a = 0$ 时**：恒收敛，和为 $0$。
  - **$a \neq 0$ 时**：
    - $|r| < 1$（即 $-1 < r < 1$）$\implies$ **收敛**，和为 $S = \dfrac{a}{1-r}$。
    - $|r| \ge 1$（即 $r \le -1$ 或 $r \ge 1$）$\implies$ **发散**。
  - **合并收敛条件**：**$a = 0$ または $-1 < r < 1$**（注意：与数列 $\{r^n\}$ 不同，级数在 $r = 1$ 且 $a \neq 0$ 时部分和 $S_n = na \to \pm\infty$ 是**发散**的！）。
- **线性性质**：若 $\sum_{n=1}^{\infty} a_n = S$、$\sum_{n=1}^{\infty} b_n = T$ 均收敛，则对任意常数 $k, l$，
  $$\sum_{n=1}^{\infty} (ka_n + lb_n) = kS + lT$$

### 1.3 函数的极限与重要极限公式（関数の極限）

- **单侧极限（片側極限）**：
  - 右极限：$\lim_{x \to a+0} f(x)$（$x > a$ 趋近 $a$）；左极限：$\lim_{x \to a-0} f(x)$（$x < a$ 趋近 $a$）。
  - $\lim_{x \to a} f(x) = \alpha \iff \lim_{x \to a+0} f(x) = \lim_{x \to a-0} f(x) = \alpha$。
  > ⚠️ **教材勘误提示（P295 / `page_0296.jpg` [3.3]）**：原教材「左側極限」一行的公式误印为 $\lim_{x \to a+0} f(x)$，正确应为 **$\lim_{x \to a-0} f(x)$**。
- **指数函数与对数函数的极限**：
  - $y = a^x$：
    - $a > 1$ 时：$\lim_{x\to\infty} a^x = \infty,\quad \lim_{x\to -\infty} a^x = 0$
    - $0 < a < 1$ 时：$\lim_{x\to\infty} a^x = 0,\quad \lim_{x\to -\infty} a^x = \infty$
  - $y = \log_a x$：
    - $a > 1$ 时：$\lim_{x\to\infty} \log_a x = \infty,\quad \lim_{x\to +0} \log_a x = -\infty$
    - $0 < a < 1$ 时：$\lim_{x\to\infty} \log_a x = -\infty,\quad \lim_{x\to +0} \log_a x = \infty$
  > ⚠️ **教材勘误提示（P295 / `page_0296.jpg` [3.4]）**：原教材连续出现三处严重漏印/错印：
  > 1. $a>1$ 时右侧误印为 $\lim_{x\to\infty} a^x = 0$，应为 $\lim_{x\to -\infty} a^x = 0$；
  > 2. $0<a<1$ 时右侧误印为 $\lim_{x\to\infty} a^x = \infty$，应为 $\lim_{x\to -\infty} a^x = \infty$；
  > 3. $0<a<1$ 时右侧误印为 $\lim_{x\to -0} \log_a x = \infty$，因对数定义域为 $x>0$，正确应为 $\lim_{x\to +0} \log_a x = \infty$。

<svg viewBox="0 0 600 175" width="600" height="175" xmlns="http://www.w3.org/2000/svg">
  <rect x="0" y="0" width="600" height="175" fill="#f8fafc" rx="8"/>
  <!-- 图1: y=a^x (a>1) -->
  <g transform="translate(15,15)">
    <text x="35" y="14" font-size="11" font-weight="bold" fill="#1e293b">y = aˣ (a &gt; 1)</text>
    <line x1="10" y1="115" x2="125" y2="115" stroke="#475569" stroke-width="1.5"/>
    <line x1="65" y1="135" x2="65" y2="25" stroke="#475569" stroke-width="1.5"/>
    <path d="M 15 112 Q 55 110 75 90 T 110 28" fill="none" stroke="#2563eb" stroke-width="2.2"/>
    <circle cx="65" cy="98" r="2.5" fill="#2563eb"/>
    <text x="53" y="96" font-size="10" fill="#1e293b">1</text>
    <text x="12" y="128" font-size="9" fill="#64748b">x→-∞: y→0</text>
    <text x="72" y="38" font-size="9" fill="#2563eb">x→∞: y→∞</text>
  </g>
  <!-- 图2: y=a^x (0<a<1) -->
  <g transform="translate(160,15)">
    <text x="25" y="14" font-size="11" font-weight="bold" fill="#1e293b">y = aˣ (0 &lt; a &lt; 1)</text>
    <line x1="10" y1="115" x2="125" y2="115" stroke="#475569" stroke-width="1.5"/>
    <line x1="65" y1="135" x2="65" y2="25" stroke="#475569" stroke-width="1.5"/>
    <path d="M 20 28 Q 55 90 75 106 T 120 113" fill="none" stroke="#dc2626" stroke-width="2.2"/>
    <circle cx="65" cy="98" r="2.5" fill="#dc2626"/>
    <text x="70" y="96" font-size="10" fill="#1e293b">1</text>
    <text x="72" y="128" font-size="9" fill="#64748b">x→∞: y→0</text>
    <text x="10" y="38" font-size="9" fill="#dc2626">x→-∞: y→∞</text>
  </g>
  <!-- 图3: y=log_a x (a>1) -->
  <g transform="translate(305,15)">
    <text x="25" y="14" font-size="11" font-weight="bold" fill="#1e293b">y = logₐx (a &gt; 1)</text>
    <line x1="10" y1="80" x2="125" y2="80" stroke="#475569" stroke-width="1.5"/>
    <line x1="35" y1="140" x2="35" y2="25" stroke="#475569" stroke-width="1.5"/>
    <path d="M 38 138 Q 42 85 58 80 T 120 42" fill="none" stroke="#059669" stroke-width="2.2"/>
    <circle cx="58" cy="80" r="2.5" fill="#059669"/>
    <text x="56" y="94" font-size="10" fill="#1e293b">1</text>
    <text x="42" y="138" font-size="9" fill="#059669">x→+0: y→-∞</text>
    <text x="70" y="38" font-size="9" fill="#059669">x→∞: y→∞</text>
  </g>
  <!-- 图4: y=log_a x (0<a<1) -->
  <g transform="translate(450,15)">
    <text x="15" y="14" font-size="11" font-weight="bold" fill="#1e293b">y = logₐx (0 &lt; a &lt; 1)</text>
    <line x1="10" y1="80" x2="125" y2="80" stroke="#475569" stroke-width="1.5"/>
    <line x1="35" y1="140" x2="35" y2="25" stroke="#475569" stroke-width="1.5"/>
    <path d="M 38 25 Q 42 75 58 80 T 120 118" fill="none" stroke="#7c3aed" stroke-width="2.2"/>
    <circle cx="58" cy="80" r="2.5" fill="#7c3aed"/>
    <text x="56" y="72" font-size="10" fill="#1e293b">1</text>
    <text x="42" y="34" font-size="9" fill="#7c3aed">x→+0: y→∞</text>
    <text x="65" y="133" font-size="9" fill="#7c3aed">x→∞: y→-∞</text>
  </g>
</svg>

- **三角函数极限核心定理（弧度制 / 弧度法）**：
  $$\lim_{x \to 0} \frac{\sin x}{x} = 1, \qquad \lim_{x \to 0} \frac{x}{\sin x} = 1, \qquad \lim_{x \to 0} \frac{\tan x}{x} = 1$$
  - **几何证明核心**（$0 < x < \frac{\pi}{2}$）：由单位圆中 $\triangle \mathrm{OAB} < \text{扇形 }\mathrm{OAB} < \triangle \mathrm{OAT}$，得 $\frac{1}{2}\sin x < \frac{1}{2}x < \frac{1}{2}\tan x \implies \cos x < \frac{\sin x}{x} < 1$，由夹逼定理得证。

<svg viewBox="0 0 540 190" width="540" height="190" xmlns="http://www.w3.org/2000/svg">
  <rect x="0" y="0" width="540" height="190" fill="#f8fafc" rx="8"/>
  <!-- 左侧：单位圆面积夹逼图 -->
  <g transform="translate(20,15)">
    <text x="10" y="14" font-size="12" font-weight="bold" fill="#1e293b">① 面积夹逼：△OAB &lt; 扇形OAB &lt; △OAT</text>
    <!-- 坐标原点 O(30,145), 半径 R=120, A(150,145), 角 x=38° -->
    <!-- B: x=30+120*cos38=124.6, y=145-120*sin38=71.1 -->
    <!-- H(124.6,145), T(150, 145-120*tan38=51.2) -->
    <!-- 阴影：△OAB -->
    <polygon points="30,145 150,145 124.6,71.1" fill="#dbeafe" opacity="0.7"/>
    <!-- 扇形弧 AB -->
    <path d="M 150,145 A 120,120 0 0,0 124.6,71.1" fill="none" stroke="#2563eb" stroke-width="2.5"/>
    <!-- △OAT 边 -->
    <line x1="30" y1="145" x2="150" y2="145" stroke="#1e293b" stroke-width="2"/>
    <line x1="30" y1="145" x2="150" y2="51.2" stroke="#1e293b" stroke-width="1.8"/>
    <line x1="150" y1="145" x2="150" y2="51.2" stroke="#dc2626" stroke-width="2"/>
    <!-- 弦 AB 与垂线 BH -->
    <line x1="124.6" y1="71.1" x2="150" y2="145" stroke="#2563eb" stroke-width="1.5"/>
    <line x1="124.6" y1="71.1" x2="124.6" y2="145" stroke="#059669" stroke-width="1.8" stroke-dasharray="4,2"/>
    <!-- 直角标记 -->
    <polyline points="118.6,145 118.6,139 124.6,139" fill="none" stroke="#059669" stroke-width="1.2"/>
    <polyline points="144,145 144,139 150,139" fill="none" stroke="#dc2626" stroke-width="1.2"/>
    <!-- 角度弧 x -->
    <path d="M 55,145 A 25,25 0 0,0 49.7,129.6" fill="none" stroke="#1e293b" stroke-width="1.2"/>
    <text x="58" y="138" font-size="11" font-style="italic" fill="#1e293b">x</text>
    <!-- 顶点标注 -->
    <text x="16" y="152" font-size="12" font-weight="bold" fill="#1e293b">O</text>
    <text x="154" y="152" font-size="12" font-weight="bold" fill="#1e293b">A</text>
    <text x="115" y="64" font-size="12" font-weight="bold" fill="#2563eb">B</text>
    <text x="154" y="54" font-size="12" font-weight="bold" fill="#dc2626">T</text>
    <text x="120" y="159" font-size="11" fill="#059669">H</text>
    <!-- 长度标注 -->
    <text x="86" y="160" font-size="11" fill="#475569">1</text>
    <text x="95" y="114" font-size="11" fill="#059669" font-weight="bold">sin x</text>
    <text x="155" y="102" font-size="11" fill="#dc2626" font-weight="bold">tan x</text>
  </g>
  <!-- 右侧：y=sin x, y=x, y=tan x 图像对比 -->
  <g transform="translate(290,15)">
    <text x="10" y="14" font-size="12" font-weight="bold" fill="#1e293b">② 0 &lt; x &lt; π/2 时：sin x &lt; x &lt; tan x</text>
    <line x1="20" y1="145" x2="210" y2="145" stroke="#475569" stroke-width="1.5"/>
    <line x1="40" y1="160" x2="40" y2="28" stroke="#475569" stroke-width="1.5"/>
    <!-- 渐近线 x = pi/2 (x=115) -->
    <line x1="115" y1="145" x2="115" y2="28" stroke="#94a3b8" stroke-width="1.2" stroke-dasharray="4,3"/>
    <text x="105" y="160" font-size="11" fill="#475569">π/2</text>
    <text x="184" y="160" font-size="11" fill="#475569">π</text>
    <!-- y = x -->
    <line x1="25" y1="160" x2="155" y2="30" stroke="#1e293b" stroke-width="1.8"/>
    <text x="156" y="42" font-size="11" fill="#1e293b">y = x</text>
    <!-- y = sin x (弧度 1 ≈ 47.7px，所以 pi/2=75px, 1=47.7px, 顶点(115, 97.3), 零点(190,145)) -->
    <path d="M 40,145 Q 78,97.3 115,97.3 Q 152,97.3 190,145" fill="none" stroke="#2563eb" stroke-width="2.2"/>
    <text x="152" y="102" font-size="11" fill="#2563eb" font-weight="bold">y = sin x</text>
    <!-- y = tan x -->
    <path d="M 40,145 Q 88,110 108,30" fill="none" stroke="#dc2626" stroke-width="2.2"/>
    <text x="68" y="38" font-size="11" fill="#dc2626" font-weight="bold">y = tan x</text>
    <text x="27" y="158" font-size="11" fill="#475569">O</text>
  </g>
</svg>

- **极限定理与重要公式总表（修正原教材 P298 / `page_0299.jpg` 错误）**：
  1. $\lim_{x \to 0} \dfrac{e^x - 1}{x} = 1$
  2. $\lim_{x \to 0} \dfrac{\log(1+x)}{x} = 1$（日本数学Ⅲ中自然对数省略底数 $e$，写作 $\log x$ 即国内 $\ln x$）
  3. $\lim_{x \to 0} \dfrac{\sin x}{x} = 1$
  4. $\lim_{x \to 0} \dfrac{1 - \cos x}{x} = 0$，以及 $\lim_{x \to 0} \dfrac{1 - \cos x}{x^2} = \dfrac{1}{2}$
  5. $\lim_{x \to \infty} \left(1 + \dfrac{1}{x}\right)^x = e$（等价形式：$\lim_{t \to 0} (1+t)^{\frac{1}{t}} = e$）
  > ⚠️ **教材勘误提示（P298 / `page_0299.jpg` 極限の重要公式まとめ）**：原教材存在三处严重印刷错误，备课授课时务必当堂纠正！
  > - **(1)** 分子排错成 $e^{x-1}$，正确应为 **$e^x - 1$**；
  > - **(2)** 分子将真数错排为上标 $\log^{(1+x)}$，正确应为 **$\log(1+x)$**；
  > - **(4)** 原教材误印为 $\lim_{x \to 0} \dfrac{1 - \cos x}{x} = 1$（**完全错误！**），正确应为 **$\lim_{x \to 0} \dfrac{1 - \cos x}{x} = 0$** 以及 **$\lim_{x \to 0} \dfrac{1 - \cos x}{x^2} = \dfrac{1}{2}$**。

### 1.4 国内高中 vs. 日本 EJU 考纲差异与符号习惯

| 对比维度 | 国内高中 / 大学习惯 | 日本 EJU 习惯 | 备课/应试提醒 |
| :--- | :--- | :--- | :--- |
| **左右极限记号** | $\lim_{x \to a^+} f(x)$，$\lim_{x \to a^-} f(x)$ | **$\lim_{x \to a+0} f(x)$**、**$\lim_{x \to a-0} f(x)$**（$a=0$ 时写 $x\to +0, x\to -0$） | **最高频记号差异！** 日本考场一律写 $+0$ 与 $-0$ |
| **自然对数记号** | $\ln x$ | **$\log x$**（数学Ⅲ默认底数为 $e$，省略底数） | 看到无底数 $\log$ 切勿当成常用对数 $\lg$！ |
| **「極限がある」vs「極限値がある」** | 统一称极限存在（发散至 $\infty$ 称极限不存在） | 教材中 $\pm\infty$ 算「極限がある（有极限趋势）」但**「極限値がない（无极限值）」** | 问「極限を求めよ」可答 $\infty$；问「極限値を求めよ」必为有限实数 |
| **无穷级数与数列收敛对比** | 高中不考，大一高数学习 | **EJU 数学Ⅲ 核心必考点**，必考含参等比级数收敛范围 | 死记：数列 $\{r^n\}$ 是 $-1 < r \le 1$；级数 $\sum ar^{n-1}$ 是 $a=0$ 或 $-1 < r < 1$ |
| **洛必达法则** | 竞赛/大学常用 | **日本高中课纲外内容**，解答题禁止直接使用 | 选填题可用洛必达快速验算，但标准解法须掌握因式分解、有理化与重要极限变形 |

---

## 二、日文核心词汇与公式假名注音

### 2.1 本切片日文核心词汇

- 極限（きょくげん / kyokugen） — 极限
- 極限値（きょくげんち / kyokugenchi） — 极限值（有限收敛值）
- 収束（しゅうそく / shuusoku） — 收敛（動詞：収束する）
- 発散（はっさん / hassan） — 发散（動詞：発散する）
- 振動（しんどう / shindou） — 震荡（動詞：振動する）
- 無限大（むげんだい / mugendai） — 无穷大（$\infty$）
- 収束条件（しゅうそくじょうけん / shuusoku jouken） — 收敛条件
- はさみうちの原理（はさみうちのげんり / hasamiuchi no genri） — 夹逼定理（亦作 挟み撃ちの原理）
- 漸化式（ぜんかしき / zenkashiki） — 递推公式
- 無限数列（むげんすうれつ / mugen suuretsu） — 无穷数列
- 無限級数（むげんきゅうすう / mugen kyuusuu） — 无穷级数
- 部分和（ぶぶんわ / bubunwa） — 部分和（前 $n$ 项和 $S_n$）
- 無限等比級数（むげんとうひきゅうすう / mugen touhi kyuusuu） — 无穷等比级数
- 関数の極限（かんすうのきょくげん / kansuu no kyokugen） — 函数的极限
- 片側極限（かたがわきょくげん / katagawa kyokugen） — 单侧极限
- 右側極限（みぎがわきょくげん / migigawa kyokugen） — 右极限（$x \to a+0$）
- 左側極限（ひだりがわきょくげん / hidarigawa kyokugen） — 左极限（$x \to a-0$）
- 不定形（ふていけい / futeikei） — 不定型（如 $\frac{0}{0}, \frac{\infty}{\infty}, \infty-\infty$）
- 自然対数の底（しぜんたいすうのてい / shizen taisuu no tei） — 自然对数的底数 $e$
- 近似（きんじ / kinji） — 近似（如 $\sin x \fallingdotseq x$）

### 2.2 核心公式的日本课堂口语读法

1. **数列极限** $\lim_{n \to \infty} a_n = \alpha$
   - 课堂读法：**リミット エヌ やじるし むげんだい の エーエヌ イコール アルファ**（口语常说：**エヌを むげんだいに したときの エーエヌの きょくげんは アルファ**）。
2. **无穷级数** $\sum_{n=1}^{\infty} a_n$
   - 课堂读法：**シグマ エヌ イコール いち から むげんだい までの エーエヌ**。
3. **无穷等比级数求和** $S = \dfrac{a}{1-r}$
   - 课堂读法：**エス イコール いち ひく アール ぶんの エー**（记住口诀：「$1 -$ 公比 分の 初項」）。
4. **右极限与左极限** $\lim_{x \to a+0} f(x)$，$\lim_{x \to a-0} f(x)$
   - 课堂读法：**リミット エックス やじるし エー プラス ゼロ の エフエックス** / **リミット エックス やじるし エー マイナス ゼロ の エフエックス**。
5. **三角函数重要极限** $\lim_{x \to 0} \dfrac{\sin x}{x} = 1$
   - 课堂读法：**リミット エックス やじるし ゼロ の エックス ぶんの サインエックス イコール いち**。
6. **自然对数底数定义** $\lim_{x \to \infty} \left(1 + \dfrac{1}{x}\right)^x = e$
   - 课堂读法：**リミット エックス やじるし むげんだい の かっこ いち たす エックス ぶんの いち かっことじ の エックスじょう イコール イー**。

---

## 三、逐题深度解析（不可跳步）— 演習問題 1（数列の極限）

---

### 演習問題 1-(1)（P286 / 原书 P285）

> **大题干**：第 $n$ 項が次の式で表される数列の極限を求めよ。（求第 $n$ 项由下列各式表示的数列的极限。）

---

#### 演習問題 1-(1)-[1]
- **【原题重现与翻译】**
  - 原题：$1 - \dfrac{1}{2n^3}$
  - 中文：求数列 $a_n = 1 - \dfrac{1}{2n^3}$ 的极限。
- **【考点定位】**
  - 基本极限 $\lim_{n\to\infty} \dfrac{1}{n^k} = 0\;(k>0)$ 与极限的线性运算。
- **【分步标准解答】**
  $$\lim_{n\to\infty} \left(1 - \frac{1}{2n^3}\right) = 1 - \frac{1}{2} \lim_{n\to\infty} \frac{1}{n^3}$$
  > 💡 讲师批注：当 $n \to \infty$ 时，$n^3 \to \infty$，故 $\dfrac{1}{n^3} \to 0$。

  $$= 1 - \frac{1}{2} \cdot 0 = 1$$
- **【最终答案】**
  **$1$**

---

#### 演習問題 1-(1)-[2]
- **【原题重现与翻译】**
  - 原题：$3n - n^2$
  - 中文：求数列 $a_n = 3n - n^2$ 的极限。
- **【考点定位】**
  - $\infty - \infty$ 型不定式：提取最高次幂 $n^2$。
- **【分步标准解答】**
  $$3n - n^2 = n^2\left(\frac{3}{n} - 1\right)$$
  > 💡 讲师批注：直接代入会出现 $\infty - \infty$ 型不定式，不可直接相减！标准做法是提出最高次项 $n^2$。

  $n \to \infty$ のとき，$n^2 \to \infty$，$\dfrac{3}{n} - 1 \to 0 - 1 = -1$ であるから，
  $$\lim_{n\to\infty} (3n - n^2) = \lim_{n\to\infty} n^2\left(\frac{3}{n} - 1\right) = -\infty$$
  > 💡 讲师批注：「正无穷大 $\times$ 负常数 $(-1)$」趋于 $-\infty$。注意在 EJU 中，负无穷大发散须明确写明 $-\infty$（不能只写「発散」）。
- **【最终答案】**
  **$-\infty$（負の無限大に発散する）**

---

#### 演習問題 1-(1)-[3]
- **【原题重现与翻译】**
  - 原题：$\dfrac{2n^2 - 3}{n^2 + 1}$
  - 中文：求数列 $a_n = \dfrac{2n^2 - 3}{n^2 + 1}$ 的极限。
- **【考点定位】**
  - $\dfrac{\infty}{\infty}$ 型分式不定式：分子分母同除以分母最高次幂 $n^2$。
- **【分步标准解答】**
  分母・分子を $n^2$ で割ると，
  $$\frac{2n^2 - 3}{n^2 + 1} = \frac{2 - \dfrac{3}{n^2}}{1 + \dfrac{1}{n^2}}$$
  > 💡 讲师批注：分子分母同除以最高次幂 $n^2$，将所有发散项转化为收敛于 $0$ 的分式。

  よって，
  $$\lim_{n\to\infty} \frac{2n^2 - 3}{n^2 + 1} = \lim_{n\to\infty} \frac{2 - \dfrac{3}{n^2}}{1 + \dfrac{1}{n^2}} = \frac{2 - 0}{1 + 0} = 2$$
  > 💡 讲师批注：口算验算技巧——分子分母同为 $n$ 的 $2$ 次式，极限即最高次项系数之比 $\dfrac{2}{1} = 2$。
- **【最终答案】**
  **$2$**

---

#### 演習問題 1-(1)-[4]
- **【原题重现与翻译】**
  - 原题：$\dfrac{4n}{\sqrt{n^2 + 2n} + n}$
  - 中文：求数列 $a_n = \dfrac{4n}{\sqrt{n^2 + 2n} + n}$ 的极限。
- **【考点定位】**
  - 含根号的 $\dfrac{\infty}{\infty}$ 型不定式：分子分母同除以 $n$（$n > 0$ 时 $n = \sqrt{n^2}$）。
- **【分步标准解答】**
  $n > 0$ であるから，分母・分子を $n$ で割ると，
  $$\frac{4n}{\sqrt{n^2 + 2n} + n} = \frac{4}{\dfrac{\sqrt{n^2 + 2n}}{n} + 1} = \frac{4}{\sqrt{1 + \dfrac{2}{n}} + 1}$$
  > 💡 讲师批注：由于 $n$ 是自然数（$n > 0$），可将 $n$ 直接以 $\sqrt{n^2}$ 的形式放入根号内。若在函数极限中遇到 $x \to -\infty$，则须特别小心 $x = -\sqrt{x^2}$！

  よって，
  $$\lim_{n\to\infty} \frac{4n}{\sqrt{n^2 + 2n} + n} = \lim_{n\to\infty} \frac{4}{\sqrt{1 + \dfrac{2}{n}} + 1} = \frac{4}{\sqrt{1 + 0} + 1} = \frac{4}{2} = 2$$
- **【最终答案】**
  **$2$**

---

#### 演習問題 1-(1)-[5]
- **【原题重现与翻译】**
  - 原题：$\dfrac{1}{\sqrt{2n + 1} - \sqrt{2n}}$
  - 中文：求数列 $a_n = \dfrac{1}{\sqrt{2n + 1} - \sqrt{2n}}$ 的极限。
- **【考点定位】**
  - 分母有理化消除 $\infty - \infty$ 不定形。
- **【分步标准解答】**
  分母を有理化すると，
  $$\frac{1}{\sqrt{2n + 1} - \sqrt{2n}} = \frac{\sqrt{2n + 1} + \sqrt{2n}}{(\sqrt{2n + 1} - \sqrt{2n})(\sqrt{2n + 1} + \sqrt{2n})}$$
  $$= \frac{\sqrt{2n + 1} + \sqrt{2n}}{(2n + 1) - 2n} = \sqrt{2n + 1} + \sqrt{2n}$$
  > 💡 讲师批注：利用平方差公式 $(a-b)(a+b)=a^2-b^2$，分母化简为常数 $1$，瞬间消除不定形！

  よって，
  $$\lim_{n\to\infty} \frac{1}{\sqrt{2n + 1} - \sqrt{2n}} = \lim_{n\to\infty} (\sqrt{2n + 1} + \sqrt{2n}) = \infty$$
- **【最终答案】**
  **$\infty$（正の無限大に発散する）**

---

#### 演習問題 1-(1)-[6]
- **【原题重现与翻译】**
  - 原题：$\log_2 \sqrt[n]{3}$
  - 中文：求数列 $a_n = \log_2 \sqrt[n]{3}$ 的极限。
- **【考点定位】**
  - 分数指数幂与对数运算性质：$\log_a b^p = p\log_a b$。
- **【分步标准解答】**
  $$\log_2 \sqrt[n]{3} = \log_2 3^{\frac{1}{n}} = \frac{1}{n} \log_2 3$$
  > 💡 讲师批注：把 $n$ 次方根写成 $\frac{1}{n}$ 次幂并提到对数前面，分离出常数 $\log_2 3$ 与变量 $\frac{1}{n}$。

  $\log_2 3$ は定数で，$\lim_{n\to\infty} \dfrac{1}{n} = 0$ であるから，
  $$\lim_{n\to\infty} \log_2 \sqrt[n]{3} = \lim_{n\to\infty} \left(\frac{1}{n} \log_2 3\right) = 0 \cdot \log_2 3 = 0$$
  > 💡 讲师批注：也可直接由 $\lim_{n\to\infty} \sqrt[n]{3} = 1$ 及对数函数连续性得出 $\log_2 1 = 0$。
- **【最终答案】**
  **$0$**

---

#### 演習問題 1-(1)-[7]
- **【原题重现与翻译】**
  - 原题：$\cos n\pi$
  - 中文：求数列 $a_n = \cos n\pi$ 的极限。
- **【考点定位】**
  - 震荡发散数列的判定（$\cos n\pi = (-1)^n$）。
- **【分步标准解答】**
  $n = 1, 2, 3, 4, \dots$ に対して，$\cos n\pi = (-1)^n$ より，数列の各項は
  $$-1,\; 1,\; -1,\; 1,\; \dots$$
  と交互に $-1$ と $1$ を繰り返す。
  > 💡 讲师批注：记住高频恒等式 $\cos n\pi = (-1)^n$（$n$ 为整数）。

  したがって，この数列は**振動する（発散する・極限はない）**。
- **【最终答案】**
  **振動する（発散する、極限はない）**

---

#### 演習問題 1-(1)-[8]
- **【原题重现与翻译】**
  - 原题：$\sqrt{n^2 + n} - \sqrt{n^2 - n}$
  - 中文：求数列 $a_n = \sqrt{n^2 + n} - \sqrt{n^2 - n}$ 的极限。
- **【考点定位】**
  - 根式 $\infty - \infty$ 型不定式：分子有理化 + 同除以最高次幂 $n$。
- **【分步标准解答】**
  分子を有理化すると，
  $$\sqrt{n^2 + n} - \sqrt{n^2 - n} = \frac{(\sqrt{n^2 + n} - \sqrt{n^2 - n})(\sqrt{n^2 + n} + \sqrt{n^2 - n})}{\sqrt{n^2 + n} + \sqrt{n^2 - n}}$$
  $$= \frac{(n^2 + n) - (n^2 - n)}{\sqrt{n^2 + n} + \sqrt{n^2 - n}} = \frac{2n}{\sqrt{n^2 + n} + \sqrt{n^2 - n}}$$
  > 💡 讲师批注：分子展开时注意去括号变号：$-(n^2 - n) = -n^2 + n$，所以分子是 $2n$ 而非 $0$！

  $n > 0$ より，分母・分子を $n$ で割ると，
  $$= \frac{2}{\sqrt{1 + \dfrac{1}{n}} + \sqrt{1 - \dfrac{1}{n}}}$$
  よって，
  $$\lim_{n\to\infty} (\sqrt{n^2 + n} - \sqrt{n^2 - n}) = \frac{2}{\sqrt{1 + 0} + \sqrt{1 - 0}} = \frac{2}{1 + 1} = 1$$
  > 💡 讲师批注：快速验算（配方近似法）：$\sqrt{n^2+n} \approx n + \frac{1}{2}$，$\sqrt{n^2-n} \approx n - \frac{1}{2}$，两者相减约等于 $1$！
- **【最终答案】**
  **$1$**

---

#### 演習問題 1-(1)-[9]
- **【原题重现与翻译】**
  - 原题：$2\left(-\dfrac{3}{4}\right)^{n-1}$
  - 中文：求数列 $a_n = 2\left(-\dfrac{3}{4}\right)^{n-1}$ 的极限。
- **【考点定位】**
  - 等比数列 $\{r^n\}$ 在 $|r| < 1$ 时的极限。
- **【分步标准解答】**
  公比 $r = -\dfrac{3}{4}$ は $-1 < r < 1$ を満たすので，$\lim_{n\to\infty} \left(-\dfrac{3}{4}\right)^{n-1} = 0$。
  > 💡 讲师批注：负公比但绝对值严格小于 $1$ 时，数列正负交替衰减，最终收敛于 $0$（不震荡发散）。

  よって，
  $$\lim_{n\to\infty} 2\left(-\frac{3}{4}\right)^{n-1} = 2 \cdot 0 = 0$$
- **【最终答案】**
  **$0$**

---

#### 演習問題 1-(1)-[10]
- **【原题重现与翻译】**
  - 原题：$5^n - (-4)^n$
  - 中文：求数列 $a_n = 5^n - (-4)^n$ 的极限。
- **【考点定位】**
  - 指数型不定式：提取底数绝对值最大的项 $5^n$。
- **【分步标准解答】**
  底の絶対値が最大の $5^n$ でくくると，
  $$5^n - (-4)^n = 5^n\left\{1 - \left(-\frac{4}{5}\right)^n\right\}$$
  > 💡 讲师批注：铁律——遇到 $a^n \pm b^n$，一律提出底数绝对值最大的那一项！

  $\left|-\dfrac{4}{5}\right| < 1$ であるから $\lim_{n\to\infty} \left(-\dfrac{4}{5}\right)^n = 0$。また $\lim_{n\to\infty} 5^n = \infty$ であるから，
  $$\lim_{n\to\infty} \{5^n - (-4)^n\} = \lim_{n\to\infty} 5^n\left\{1 - \left(-\frac{4}{5}\right)^n\right\} = \infty$$
- **【最终答案】**
  **$\infty$（正の無限大に発散する）**

---

#### 演習問題 1-(1)-[11]
- **【原题重现与翻译】**
  - 原题：$\dfrac{3^{n+1} - 2^n}{3^n + 2^n}$
  - 中文：求数列 $a_n = \dfrac{3^{n+1} - 2^n}{3^n + 2^n}$ 的极限。
- **【考点定位】**
  - 指数分式型不定式：分子分母同除以分母中底数绝对值最大的项 $3^n$。
- **【分步标准解答】**
  分母・分子を $3^n$ で割ると，
  $$\frac{3^{n+1} - 2^n}{3^n + 2^n} = \frac{3 \cdot 3^n - 2^n}{3^n + 2^n} = \frac{3 - \left(\dfrac{2}{3}\right)^n}{1 + \left(\dfrac{2}{3}\right)^n}$$
  > 💡 讲师批注：先将 $3^{n+1}$ 拆成 $3 \cdot 3^n$，再同除以 $3^n$，避免指数漏乘系数 $3$。

  $\left|\dfrac{2}{3}\right| < 1$ より $\lim_{n\to\infty} \left(\dfrac{2}{3}\right)^n = 0$ であるから，
  $$\lim_{n\to\infty} \frac{3^{n+1} - 2^n}{3^n + 2^n} = \frac{3 - 0}{1 + 0} = 3$$
- **【最终答案】**
  **$3$**

---

#### 演習問題 1-(1)-[12]
- **【原题重现与翻译】**
  - 原题：$\dfrac{r^n}{2 + r^{n+1}} \quad (r > -1)$
  - 中文：求数列 $a_n = \dfrac{r^n}{2 + r^{n+1}}\;(r > -1)$ 的极限。
- **【考点定位】**
  - 含参数等比数列极限的分类讨论（場合分け）：按 $-1 < r < 1$、$r = 1$、$r > 1$ 三段讨论。
- **【分步标准解答】**
  $r > -1$ の範囲で，次のように場合分けする。
  > 💡 讲师批注：因为题干已限定 $r > -1$，故无需讨论 $r = -1$ 与 $r < -1$；临界点只有 $r = 1$，分为三段：$-1 < r < 1$、$r = 1$、$r > 1$。

  - **[i] $-1 < r < 1$ のとき**：
    $\lim_{n\to\infty} r^n = 0$，$\lim_{n\to\infty} r^{n+1} = 0$ であるから，
    $$\lim_{n\to\infty} \frac{r^n}{2 + r^{n+1}} = \frac{0}{2 + 0} = 0$$

  - **[ii] $r = 1$ のとき**：
    $r^n = 1$，$r^{n+1} = 1$ であるから，
    $$\lim_{n\to\infty} \frac{r^n}{2 + r^{n+1}} = \lim_{n\to\infty} \frac{1}{2 + 1} = \frac{1}{3}$$

  - **[iii] $r > 1$ のとき**：
    分母・分子を $r^n$ で割ると，$\dfrac{r^n}{2 + r^{n+1}} = \dfrac{1}{\dfrac{2}{r^n} + r}$。
    $r > 1$ より $\left|\dfrac{1}{r}\right| < 1$ であるから $\lim_{n\to\infty} \dfrac{1}{r^n} = 0$。よって，
    $$\lim_{n\to\infty} \frac{r^n}{2 + r^{n+1}} = \lim_{n\to\infty} \frac{1}{\dfrac{2}{r^n} + r} = \frac{1}{0 + r} = \frac{1}{r}$$
    > 💡 讲师批注：特值验算：$r = 2$ 时原式 $= \frac{2^n}{2 + 2\cdot 2^n} \to \frac{1}{2} = \frac{1}{r}$，完全吻合！
- **【最终答案】**
  **$-1 < r < 1$ のとき $0$；$r = 1$ のとき $\dfrac{1}{3}$；$r > 1$ のとき $\dfrac{1}{r}$**

---

### 演習問題 1-(2)（P288 / 原书 P287）

> **大题干**：次の極限を求めよ。（求下列极限。）

---

#### 演習問題 1-(2)-[1]
- **【原题重现与翻译】**
  - 原题：$\lim_{n\to\infty} \dfrac{3 + 7 + 11 + \dots + (4n - 1)}{3 + 5 + 7 + \dots + (2n + 1)}$
  - 中文：求极限 $\lim_{n\to\infty} \dfrac{3 + 7 + 11 + \dots + (4n - 1)}{3 + 5 + 7 + \dots + (2n + 1)}$。
- **【考点定位】**
  - 先用等差数列求和公式化简分子分母，再求 $\dfrac{\infty}{\infty}$ 型极限。
- **【分步标准解答】**
  分子は初項 $3$，末項 $4n - 1$，項数 $n$ の等差数列の和であるから，
  $$3 + 7 + 11 + \dots + (4n - 1) = \frac{1}{2}n\{3 + (4n - 1)\} = \frac{1}{2}n(4n + 2) = 2n^2 + n$$
  分母は初項 $3$，末項 $2n + 1$，項数 $n$ の等差数列の和であるから，
  $$3 + 5 + 7 + \dots + (2n + 1) = \frac{1}{2}n\{3 + (2n + 1)\} = \frac{1}{2}n(2n + 4) = n^2 + 2n$$
  > 💡 讲师批注：**切忌漏数项数！** 检验项数的方法：把 $n=1, 2$ 代入末项与求和式——分子 $n=1$ 得 $3$、$n=2$ 得 $3+7=10$，而 $2(2)^2+2 = 10$；分母 $n=1$ 得 $3$、$n=2$ 得 $3+5=8$，而 $2^2+2(2)=8$，完全无误！

  したがって，
  $$\lim_{n\to\infty} \frac{2n^2 + n}{n^2 + 2n} = \lim_{n\to\infty} \frac{2 + \dfrac{1}{n}}{1 + \dfrac{2}{n}} = \frac{2 + 0}{1 + 0} = 2$$
- **【最终答案】**
  **$2$**

---

#### 演習問題 1-(2)-[2]
- **【原题重现与翻译】**
  - 原题：$\lim_{n\to\infty} \{\log_3(1^2 + 2^2 + \dots + n^2) - \log_3 n^3\}$
  - 中文：求极限 $\lim_{n\to\infty} \{\log_3(1^2 + 2^2 + \dots + n^2) - \log_3 n^3\}$。
- **【考点定位】**
  - 平方和公式 $\sum_{k=1}^n k^2 = \dfrac{1}{6}n(n+1)(2n+1)$ 与对数减法法则。
- **【分步标准解答】**
  $1^2 + 2^2 + \dots + n^2 = \dfrac{1}{6}n(n+1)(2n+1)$ であるから，対数の性質より，
  $$\log_3(1^2 + 2^2 + \dots + n^2) - \log_3 n^3 = \log_3 \frac{n(n+1)(2n+1)}{6n^3}$$
  > 💡 讲师批注：直接求极限会出现 $\infty - \infty$ 不定形，先利用 $\log_a M - \log_a N = \log_a \dfrac{M}{N}$ 合并为一个对数！

  真数部分を整理すると，
  $$\frac{n(n+1)(2n+1)}{6n^3} = \frac{1}{6} \cdot \frac{n+1}{n} \cdot \frac{2n+1}{n} = \frac{1}{6}\left(1 + \frac{1}{n}\right)\left(2 + \frac{1}{n}\right)$$
  $n \to \infty$ のとき，真数は $\dfrac{1}{6} \cdot 1 \cdot 2 = \dfrac{1}{3}$ に収束するから，
  $$\lim_{n\to\infty} \{\log_3(1^2 + 2^2 + \dots + n^2) - \log_3 n^3\} = \log_3 \frac{1}{3} = -1$$
- **【最终答案】**
  **$-1$**

---

### 演習問題 1-(3)（P288 / 原书 P287）
- **【原题重现与翻译】**
  - 原题：極限 $\lim_{n\to\infty} \dfrac{\cos n\pi}{n}$ を求めよ。
  - 中文：求极限 $\lim_{n\to\infty} \dfrac{\cos n\pi}{n}$。
- **【考点定位】**
  - 夹逼定理（はさみうちの原理）处理有界震荡数列除以无穷大。
- **【分步标准解答】**
  すべての自然数 $n$ に対して，$-1 \le \cos n\pi \le 1$ が成り立つ。
  各辺を $n\; (> 0)$ で割ると，
  $$-\frac{1}{n} \le \frac{\cos n\pi}{n} \le \frac{1}{n}$$
  > 💡 讲师批注：虽然 $\cos n\pi$ 自身震荡不收敛，但它是**有界量**（始终在 $[-1, 1]$ 之间），乘以趋于 $0$ 的 $\frac{1}{n}$ 必被夹逼至 $0$。

  ここで，$\lim_{n\to\infty} \left(-\dfrac{1}{n}\right) = 0$，$\lim_{n\to\infty} \dfrac{1}{n} = 0$ であるから，はさみうちの原理により，
  $$\lim_{n\to\infty} \frac{\cos n\pi}{n} = 0$$
- **【最终答案】**
  **$0$**

---

### 演習問題 1-(4)（P288 / 原书 P287）
- **【原题重现与翻译】**
  - 原题：$a_n = \dfrac{1}{n^2 + 1} + \dfrac{1}{n^2 + 2} + \dots + \dfrac{1}{n^2 + n}$ とするとき，$\lim_{n\to\infty} a_n$ を求めよ。
  - 中文：设 $a_n = \dfrac{1}{n^2 + 1} + \dfrac{1}{n^2 + 2} + \dots + \dfrac{1}{n^2 + n}$，求 $\lim_{n\to\infty} a_n$。
- **【考点定位】**
  - 放缩法 + 夹逼定理（はさみうちの原理）：将 $n$ 项和放大为「$n \times$ 最大项」、缩小为「$n \times$ 最小项」。
- **【分步标准解答】**
  $a_n$ の各項はすべて正で，項数は $n$ 個である。その中で最大の項は $\dfrac{1}{n^2 + 1}$，最小の項は $\dfrac{1}{n^2 + n}$ であるから，
  $$\underbrace{\frac{1}{n^2 + n} + \dots + \frac{1}{n^2 + n}}_{n\text{ 個}} \le a_n \le \underbrace{\frac{1}{n^2 + 1} + \dots + \frac{1}{n^2 + 1}}_{n\text{ 個}}$$
  すなわち，
  $$\frac{n}{n^2 + n} \le a_n \le \frac{n}{n^2 + 1}$$
  > 💡 讲师批注：**极易踩坑点！** 绝对不能认为「每一项都趋于 $0$，所以 $n$ 项之和就趋于 $0$」——因为项数 $n$ 也在趋于 $\infty$（属于 $0 \times \infty$ 不定形，如 $\sum_{k=1}^n \frac{1}{n+k} \to \ln 2 \neq 0$）！必须严格用夹逼放缩证明。

  ここで，左辺と右辺の極限をそれぞれ求めると，
  $$\lim_{n\to\infty} \frac{n}{n^2 + n} = \lim_{n\to\infty} \frac{1}{n + 1} = 0$$
  $$\lim_{n\to\infty} \frac{n}{n^2 + 1} = \lim_{n\to\infty} \frac{\dfrac{1}{n}}{1 + \dfrac{1}{n^2}} = \frac{0}{1 + 0} = 0$$
  よって，はさみうちの原理により，
  $$\lim_{n\to\infty} a_n = 0$$
- **【最终答案】**
  **$0$**

---

### 演習問題 1-(5)（P289 / 原书 P288）
- **【原题重现与翻译】**
  - 原题：数列 $\left\{\left(\dfrac{2x}{x^2 + 1}\right)^n\right\}$ が収束するように，実数 $x$ の値の範囲を定めよ。また，そのときの数列の極限値を求めよ。
  - 中文：求使数列 $\left\{\left(\dfrac{2x}{x^2 + 1}\right)^n\right\}$ 收敛的实数 $x$ 的取值范围，并求此时该数列的极限值。
- **【考点定位】**
  - 等比数列 $\{r^n\}$ 的收敛条件 $-1 < r \le 1$ 与一元二次不等式求解。
- **【图解辅助（SVG 矢量图）】**

<svg viewBox="0 0 460 155" width="460" height="155" xmlns="http://www.w3.org/2000/svg">
  <rect x="0" y="0" width="460" height="155" fill="#f8fafc" rx="8"/>
  <text x="16" y="20" font-size="12" font-weight="bold" fill="#1e293b">函数 r(x) = 2x / (x² + 1) 的值域与收敛点分布</text>
  <!-- 坐标轴 -->
  <line x1="30" y1="88" x2="430" y2="88" stroke="#475569" stroke-width="1.5"/>
  <line x1="230" y1="145" x2="230" y2="28" stroke="#475569" stroke-width="1.5"/>
  <text x="434" y="92" font-size="12" font-style="italic" fill="#334155">x</text>
  <text x="236" y="34" font-size="12" font-style="italic" fill="#334155">r</text>
  <!-- 水平虚线 r=1 (y=43), r=-1 (y=133) -->
  <line x1="40" y1="43" x2="420" y2="43" stroke="#10b981" stroke-width="1" stroke-dasharray="4,3"/>
  <line x1="40" y1="133" x2="420" y2="133" stroke="#ef4444" stroke-width="1" stroke-dasharray="4,3"/>
  <text x="215" y="47" font-size="11" fill="#059669">1</text>
  <text x="210" y="137" font-size="11" fill="#dc2626">-1</text>
  <!-- 曲线 r = 2x/(x^2+1), 比例: x 1单位=50px, r 1单位=45px -->
  <path d="M 40,104 C 95,112 145,133 180,133 C 205,133 218,110 230,88 C 242,66 255,43 280,43 C 315,43 365,64 420,72" fill="none" stroke="#2563eb" stroke-width="2.4"/>
  <!-- x = -1 空心点 (180, 133) -->
  <circle cx="180" cy="133" r="5" fill="#ffffff" stroke="#dc2626" stroke-width="2.2"/>
  <line x1="180" y1="88" x2="180" y2="133" stroke="#94a3b8" stroke-width="1" stroke-dasharray="3,2"/>
  <text x="172" y="82" font-size="11" fill="#dc2626">-1</text>
  <text x="65" y="146" font-size="10.5" fill="#dc2626">x = -1 时 r = -1（发散，剔除）</text>
  <!-- x = 1 实心点 (280, 43) -->
  <circle cx="280" cy="43" r="5" fill="#10b981" stroke="#047857" stroke-width="2"/>
  <line x1="280" y1="43" x2="280" y2="88" stroke="#94a3b8" stroke-width="1" stroke-dasharray="3,2"/>
  <text x="277" y="102" font-size="11" fill="#059669">1</text>
  <text x="290" y="38" font-size="10.5" fill="#059669">x = 1 时 r = 1（极限为 1）</text>
</svg>

- **【分步标准解答】**
  公比を $r = \dfrac{2x}{x^2 + 1}$ とおく。数列 $\{r^n\}$ が収束するための必要十分条件は，
  $$-1 < \frac{2x}{x^2 + 1} \le 1$$
  すべての実数 $x$ に対して $x^2 + 1 > 0$ であるから，各辺に $x^2 + 1$ を掛けても不等号の向きは変わらない：
  $$-(x^2 + 1) < 2x \le x^2 + 1$$
  これを 2 つの不等式に分けて解く。
  1. 左側の不等式：$-x^2 - 1 < 2x \iff x^2 + 2x + 1 > 0 \iff (x + 1)^2 > 0$
     よって，$x \neq -1$。
  2. 右側の不等式：$2x \le x^2 + 1 \iff x^2 - 2x + 1 \ge 0 \iff (x - 1)^2 \ge 0$
     これはすべての実数 $x$ について成り立つ（等号成立は $x = 1$ のとき）。
  > 💡 讲师批注：不等式 $(x+1)^2 > 0$ 的解不是「所有实数」，必须**挖去 $x = -1$**！而 $(x-1)^2 \ge 0$ 对所有实数恒成立，且等号在 $x=1$ 处取到，这决定了极限值必须分 $x=1$ 与 $x \neq \pm 1$ 两种情况讨论。

  以上より，求める実数 $x$ の範囲は **$x \neq -1$** である。
  また，このときの極限値は：
  - $x = 1$ のとき：$r = \dfrac{2 \cdot 1}{1^2 + 1} = 1$ より，$\lim_{n\to\infty} 1^n = 1$。
  - $x \neq \pm 1$ のとき：$-1 < r < 1$ より，$\lim_{n\to\infty} r^n = 0$。
- **【最终答案】**
  **$x$ の範囲：$x \neq -1$（$-1$ 以外のすべての実数）**
  **極限値：$x = 1$ のとき $1$；$x \neq \pm 1$ のとき $0$**

---

### 演習問題 1-(6)（P289 / 原书 P288）

> **大题干**：次の条件によって定められる数列 $\{a_n\}$ の極限を求めよ。（求由下列条件确定的数列 $\{a_n\}$ 的极限。）

---

#### 演習問題 1-(6)-[1]
- **【原题重现与翻译】**
  - 原题：$a_1 = 1,\; a_{n+1} = \dfrac{1}{2}a_n + 1$
  - 中文：已知 $a_1 = 1,\; a_{n+1} = \dfrac{1}{2}a_n + 1$，求 $\lim_{n\to\infty} a_n$。
- **【考点定位】**
  - 一阶线性递推式 $a_{n+1} = pa_n + q$（特性方程式法）求通项后再求极限。
- **【分步标准解答】**
  特性方程式 $\alpha = \dfrac{1}{2}\alpha + 1$ を解くと，$\alpha = 2$。
  > 💡 讲师批注：**注意规范！** 不可直接令 $\lim a_n = \alpha$ 代入递推式就得出 $\alpha = 2$，因为尚未证明数列 $\{a_n\}$ 收敛（参见下题 [2]，不收敛的数列也有特征根！）。必须先求出通项公式 $a_n$，再取极限。

  漸化式を変形すると，
  $$a_{n+1} - 2 = \frac{1}{2}(a_n - 2)$$
  よって，数列 $\{a_n - 2\}$ は初項 $a_1 - 2 = 1 - 2 = -1$，公比 $\dfrac{1}{2}$ の等比数列であるから，
  $$a_n - 2 = -1 \cdot \left(\frac{1}{2}\right)^{n-1} \implies a_n = 2 - \left(\frac{1}{2}\right)^{n-1}$$
  > 💡 讲师批注：验算前两项：$a_1 = 2 - 1 = 1$，$a_2 = 2 - \frac{1}{2} = \frac{3}{2} = \frac{1}{2}(1)+1$，正确！

  $\left|\dfrac{1}{2}\right| < 1$ より $\lim_{n\to\infty} \left(\dfrac{1}{2}\right)^{n-1} = 0$ であるから，
  $$\lim_{n\to\infty} a_n = \lim_{n\to\infty} \left\{2 - \left(\frac{1}{2}\right)^{n-1}\right\} = 2 - 0 = 2$$
- **【最终答案】**
  **$2$**

---

#### 演習問題 1-(6)-[2]
- **【原题重现与翻译】**
  - 原题：$a_1 = 5,\; a_{n+1} = 2a_n - 4$
  - 中文：已知 $a_1 = 5,\; a_{n+1} = 2a_n - 4$，求 $\lim_{n\to\infty} a_n$。
- **【考点定位】**
  - 一阶线性递推式（公比 $|p| > 1$ 时发散的典型警示题）。
- **【分步标准解答】**
  特性方程式 $\alpha = 2\alpha - 4$ を解くと，$\alpha = 4$。
  漸化式を変形すると，
  $$a_{n+1} - 4 = 2(a_n - 4)$$
  よって，数列 $\{a_n - 4\}$ は初項 $a_1 - 4 = 5 - 4 = 1$，公比 $2$ の等比数列であるから，
  $$a_n - 4 = 1 \cdot 2^{n-1} \implies a_n = 4 + 2^{n-1}$$
  > 💡 讲师批注：这就是为什么**严禁直接假设极限存在而套特征根**！如果直接套 $\alpha = 2\alpha - 4$ 得到 $\alpha = 4$，就会掉进大坑！因为首项 $a_1 = 5 \neq 4$ 且公比 $2 > 1$，数列其实是发散至 $+\infty$ 的！

  $2 > 1$ より $\lim_{n\to\infty} 2^{n-1} = \infty$ であるから，
  $$\lim_{n\to\infty} a_n = \lim_{n\to\infty} (4 + 2^{n-1}) = \infty$$
- **【最终答案】**
  **$\infty$（正の無限大に発散する）**

---

#### 演習問題 1-(6)-[3]
- **【原题重现与翻译】**
  - 原题：$a_1 = 0,\; a_2 = 1,\; a_{n+2} = \dfrac{1}{4}(a_{n+1} + 3a_n)$
  - 中文：已知 $a_1 = 0,\; a_2 = 1,\; a_{n+2} = \dfrac{1}{4}(a_{n+1} + 3a_n)$，求 $\lim_{n\to\infty} a_n$。
- **【考点定位】**
  - 相邻三项递推式（隣接3項間漸化式）：二阶特征方程求解 + 构造双等比数列消元。
- **【分步标准解答】**
  漸化式 $4a_{n+2} - a_{n+1} - 3a_n = 0$ の特性方程式
  $$4t^2 - t - 3 = 0 \iff (t - 1)(4t + 3) = 0$$
  を解くと，$t = 1,\; -\dfrac{3}{4}$。
  > 💡 讲师批注：特性方程两根为 $\alpha = 1,\; \beta = -\frac{3}{4}$，利用 $a_{n+2} - \alpha a_{n+1} = \beta(a_{n+1} - \alpha a_n)$ 构造两个等比递推式。

  これより，漸化式は次の 2 通りに変形できる：
  $$a_{n+2} - a_{n+1} = -\frac{3}{4}(a_{n+1} - a_n) \quad \cdots \text{①}$$
  $$a_{n+2} + \frac{3}{4}a_{n+1} = 1 \cdot \left(a_{n+1} + \frac{3}{4}a_n\right) \quad \cdots \text{②}$$

  - ① より，数列 $\{a_{n+1} - a_n\}$ は初項 $a_2 - a_1 = 1 - 0 = 1$，公比 $-\dfrac{3}{4}$ の等比数列であるから，
    $$a_{n+1} - a_n = \left(-\frac{3}{4}\right)^{n-1} \quad \cdots \text{①}'$$
  - ② より，数列 $\left\{a_{n+1} + \dfrac{3}{4}a_n\right\}$ は定数列（公比 $1$）であるから，
    $$a_{n+1} + \frac{3}{4}a_n = a_2 + \frac{3}{4}a_1 = 1 + \frac{3}{4} \cdot 0 = 1 \quad \cdots \text{②}'$$

  $\text{②}' - \text{①}'$ より $a_{n+1}$ を消去すると，
  $$\frac{7}{4}a_n = 1 - \left(-\frac{3}{4}\right)^{n-1}$$
  $$a_n = \frac{4}{7}\left\{1 - \left(-\frac{3}{4}\right)^{n-1}\right\}$$
  > 💡 讲师批注：验算前三项：$n=1 \implies \frac{4}{7}(1-1)=0$；$n=2 \implies \frac{4}{7}(1+\frac{3}{4})=1$；$n=3 \implies \frac{4}{7}(1-\frac{9}{16})=\frac{1}{4}$，而原递推式 $a_3 = \frac{1}{4}(1+0) = \frac{1}{4}$，100% 精准！

  $\left|-\dfrac{3}{4}\right| < 1$ より $\lim_{n\to\infty} \left(-\dfrac{3}{4}\right)^{n-1} = 0$ であるから，
  $$\lim_{n\to\infty} a_n = \frac{4}{7}(1 - 0) = \frac{4}{7}$$
- **【最终答案】**
  **$\dfrac{4}{7}$**

---
> **下篇衔接**：无穷级数（演習問題 2 全 10 题）与函数极限（演習問題 3 全 4 小题）的逐题深度解析，详见同目录 [`note_020_b.md`](note_020_b.md)。
