# 《EJU 教材全解与备课讲义》数学 021-A（P301–P305）

> **对应源文件**：`work_math/ocr_md/ocr_021_p301-315.md`（前半部：関数の極限・演習問題 3-(3)～(10)）
> **视觉核对参考图**：`work_math/ref_imgs/page_0301.jpg` – `page_0305.jpg`
> **拆卷说明**：本切片（P301–P315）包含 36 道小题及「関数の連続性」「微分係数と導関数」「導関数の計算」「三角・対数・指数関数の微分」四大核心理论板块。为保证推导完整、绝不跳步，按知识模块拆分为 `note_021_a.md`（P301–P305：函数极限综合演练）与 `note_021_b.md`（P306–P315：连续性与微分法基础）。

---

## 一、国内高中基础知识点唤醒与 EJU 考纲差异对比

本部分（P301–P305）对应日本高中 **数学Ⅲ（極限：関数の極限）** 的核心计算演练，涵盖 **单侧极限（片側極限）、不定形（$\frac{\infty}{\infty}$、$\infty-\infty$、$\frac{0}{0}$、$1^\infty$）解消、夹逼定理（はさみうちの原理）、三角函数极限、自然对数底 $e$ 相关极限** 五大题型。

### 1.1 单侧极限与极限的存在性（片側極限と極限の存在）

- **右极限（右側極限）**：$x$ 从大于 $a$ 的一侧无限趋近于 $a$，记作 $\displaystyle\lim_{x \to a+0} f(x)$（$a=0$ 时常简记为 $\displaystyle\lim_{x \to +0} f(x)$）。
- **左极限（左側極限）**：$x$ 从小于 $a$ 的一侧无限趋近于 $a$，记作 $\displaystyle\lim_{x \to a-0} f(x)$（$a=0$ 时常简记为 $\displaystyle\lim_{x \to -0} f(x)$）。
- **极限存在的充要条件**：
  $$\lim_{x \to a} f(x) = \alpha \iff \lim_{x \to a+0} f(x) = \lim_{x \to a-0} f(x) = \alpha$$
  - 若左右极限不相等，或其中至少一个发散，则 $\displaystyle\lim_{x \to a} f(x)$ **不存在**。

### 1.2 四大常见不定形（不定形）的标准解消策略

| 不定形类型 | 典型结构 | 标准解消手段 |
| :--- | :--- | :--- |
| **$\dfrac{\infty}{\infty}$ 型** | 多项式分式、指数分式 | 分子分母同除以**最高次幂**或**增长最快的底数幂**（注意 $x \to -\infty$ 时谁最大！） |
| **$\infty - \infty$ 型** | 含根号相减（如 $\sqrt{x^2-x}-x$） | **分子有理化**；若 $x \to -\infty$，强烈建议先换元 $t = -x \to \infty$ 防止 $\sqrt{x^2} = |x| = -x$ 符号出错 |
| **$\dfrac{0}{0}$ 型** | 三角函数、对数、指数分式 | 凑基本极限公式 $\displaystyle\lim_{x\to 0}\frac{\sin x}{x}=1$、$\displaystyle\lim_{x\to 0}\frac{e^x-1}{x}=1$、$\displaystyle\lim_{x\to 0}\frac{\log(1+x)}{x}=1$ |
| **$1^\infty$ 型** | $(1+\text{无穷小})^{\text{无穷大}}$ | 凑自然对数底 $e$ 的定义式 $\displaystyle\lim_{t\to 0}(1+t)^{\frac{1}{t}}=e$ 或 $\displaystyle\lim_{t\to \pm\infty}\left(1+\frac{1}{t}\right)^t=e$ |

### 1.3 三角函数与自然对数底 $e$ 的核心极限公式

1. **三角函数基本极限（弧度制限定！）**：
   $$\lim_{x \to 0} \frac{\sin x}{x} = 1, \qquad \lim_{x \to 0} \frac{\tan x}{x} = 1, \qquad \lim_{x \to 0} \frac{1 - \cos x}{x^2} = \frac{1}{2}$$
2. **自然对数底 $e$ 的定义与衍生公式**：
   $$e = \lim_{x \to \pm\infty} \left(1 + \frac{1}{x}\right)^x = \lim_{h \to 0} (1 + h)^{\frac{1}{h}} \approx 2.71828\cdots$$
   $$\lim_{x \to 0} \frac{\log(1+x)}{x} = 1, \qquad \lim_{x \to 0} \frac{e^x - 1}{x} = 1$$
3. **夹逼定理（はさみうちの原理）**：
   若在 $x \to a$（或 $x \to \infty$）的附近恒有 $g(x) \le f(x) \le h(x)$，且 $\displaystyle\lim g(x) = \lim h(x) = \alpha$，则 $\displaystyle\lim f(x) = \alpha$。

### 1.4 国内高中 vs. 日本 EJU 考纲差异与符号习惯

| 对比维度 | 国内高中 / 大学高数习惯 | 日本 EJU（数学Ⅲ）习惯 | 备课/应试提醒 |
| :--- | :--- | :--- | :--- |
| **极限考察定位** | 高中课标已弱化/删去，主要在大学高数学习 | **EJU 理系数学必考核心板块** | 国内学生普遍缺乏系统训练，需补足不定形解消与换元技巧 |
| **自然对数记法** | $\ln x$（以 $e$ 为底），$\lg x$（以 $10$ 为底） | **$\log x$ 默认表示自然对数 $\log_e x$**（省略底数 $e$） | **最高频坑点！** 数学Ⅲ中看到无底数的 $\log x$ 一律按 $\ln x$ 处理 |
| **左右极限记法** | $x \to a^+$、$x \to a^-$ | **$x \to a+0$、$x \to a-0$**（$a=0$ 时写 $x \to +0$、$x \to -0$） | 书写与读题务必习惯 $+0$、$-0$ 记号 |
| **正无穷记法** | 常写 $+\infty$ | 多简记为 **$\infty$**（与 $-\infty$ 相对） | 看到 $x \to \infty$ 意即 $x \to +\infty$ |
| **洛必达法则** | 大学高数常用 | **日本高中考纲不收录**（大题不可直接用，选择题/填空题可用于快速验算） | 讲义中标准解答严格按日本考纲变形，批注中可辅以洛必达验算 |

---

## 二、日文核心词汇与公式假名注音

### 2.1 本切片（前半部）日文核心词汇

- 極限（きょくげん / kyokugen） — 极限
- 極限値（きょくげんち / kyokugenchi） — 极限值
- 片側極限（かたがわきょくげん / katagawa kyokugen） — 单侧极限
- 右側極限（みぎがわきょくげん / migigawa kyokugen） — 右极限（亦作 右極限）
- 左側極限（ひだりがわきょくげん / hidarigawa kyokugen） — 左极限（亦作 左極限）
- 不定形（ふていけい / futeikei） — 不定形（未定式）
- はさみうちの原理（はさみうちのげんり / hasamiuchi no genri） — 夹逼定理
- 自然対数（しぜんたいすう / shizen taisuu） — 自然对数（$\log x = \log_e x$）
- 自然対数の底（しぜんたいすうのてい / shizen taisuu no tei） — 自然对数的底数 $e$

### 2.2 核心公式的日本课堂口语读法

1. **右极限** $\displaystyle\lim_{x \to 1+0} f(x)$
   - 课堂读法：**リミット、エックス やじるし いち プラス ゼロ の エフ・エックス**（口语亦说「エックスを みぎがわから いちに ちかづける」）
2. **三角函数基本极限** $\displaystyle\lim_{x \to 0} \frac{\sin x}{x} = 1$
   - 课堂读法：**リミット、エックス やじるし ゼロ、エックス ぶんの サイン・エックス イコール いち**
3. **自然对数底 $e$** $\displaystyle\lim_{x \to \infty} \left(1 + \frac{1}{x}\right)^x = e$
   - 课堂读法：**リミット、エックス やじるし むげんだい、かっこ いち たす エックス ぶんの いち かっことじ の エックスじょう イコール イー**
   - 备注：$\infty$ 读作 **むげんだい（無限大）**，$-\infty$ 读作 **マイナス むげんだい**。

---

## 三、逐题深度解析（不可跳步）

---

### 演習問題 3（関数の極限）

#### 演習問題 3-(3)
- **【原题重现与翻译】**
  - 原题：$\displaystyle\lim_{x \to 1+0} \frac{x-2}{x-1}\ ,\ \lim_{x \to 1-0} \frac{x-2}{x-1}$ を求めよ。（注：此题在 OCR 中漏识，已对照 `page_0301.jpg` 补全）
  - 中文：求 $\displaystyle\lim_{x \to 1+0} \frac{x-2}{x-1}$ 与 $\displaystyle\lim_{x \to 1-0} \frac{x-2}{x-1}$。
- **【考点定位】**
  - 分式函数在分母为零处的左右极限（$\frac{\text{非零常数}}{\pm 0}$ 型发散判定）。
- **【图解辅助（SVG 矢量图）】**
  将 $\dfrac{x-2}{x-1} = 1 - \dfrac{1}{x-1}$ 绘出草图，直观观察 $x=1$ 两侧函数值的趋向：

<svg viewBox="0 0 460 260" width="460" height="260" xmlns="http://www.w3.org/2000/svg" style="background:#fafafa;border:1px solid #e0e0e0;border-radius:6px;">
  <style>
    .axis { stroke: #333; stroke-width: 1.4; }
    .asym { stroke: #e67e22; stroke-width: 1.4; stroke-dasharray: 5,4; }
    .curve { fill: none; stroke: #2980b9; stroke-width: 2.2; }
    .lbl { font: 12px sans-serif; fill: #333; }
    .hl { font: bold 12px sans-serif; fill: #c0392b; }
    .note { font: 11px sans-serif; fill: #d35400; }
  </style>
  <!-- Axes -->
  <line x1="30" y1="150" x2="430" y2="150" class="axis"/>
  <polygon points="430,150 422,146 422,154" fill="#333"/>
  <line x1="170" y1="245" x2="170" y2="18" class="axis"/>
  <polygon points="170,18 166,26 174,26" fill="#333"/>
  <text x="422" y="168" class="lbl">x</text>
  <text x="155" y="28" class="lbl">y</text>
  <text x="156" y="165" class="lbl">O</text>
  <!-- Asymptotes x=1 (x=220), y=1 (y=105) -->
  <line x1="220" y1="25" x2="220" y2="245" class="asym"/>
  <line x1="30" y1="105" x2="425" y2="105" class="asym"/>
  <text x="224" y="165" class="note">x = 1</text>
  <text x="142" y="102" class="note">y = 1</text>
  <!-- Left branch: y = 1 - 1/(x-1) for x<1 -->
  <path d="M 40,95 Q 160,88 195,55 Q 208,40 213,22" class="curve"/>
  <!-- Right branch: y = 1 - 1/(x-1) for x>1 -->
  <path d="M 227,242 Q 235,175 265,138 Q 310,115 415,111" class="curve"/>
  <!-- Annotations -->
  <text x="242" y="226" class="hl">x → 1+0 で y → −∞</text>
  <text x="234" y="42" class="hl">x → 1−0 で y → +∞</text>
  <text x="285" y="95" class="lbl" fill="#2980b9">y = (x−2)/(x−1) = 1 − 1/(x−1)</text>
</svg>

- **【分步标准解答】**
  1. $x \to 1+0$ のとき：
     分子 $x - 2 \to 1 - 2 = -1 < 0$ であり、分母 $x - 1 > 0$ を保ちながら $x - 1 \to +0$ となる。
     > 💡 讲师批注：判断 $\frac{c}{0}$ 型极限的符号时，只需看**分子极限的正负**与**分母趋于 $0$ 的方向（$+0$ 还是 $-0$）**。此处为 $\frac{-1}{+0}$，异号得 $-\infty$。

     よって、
     $$\lim_{x \to 1+0} \frac{x-2}{x-1} = -\infty$$

  2. $x \to 1-0$ のとき：
     分子 $x - 2 \to -1 < 0$ であり、分母 $x - 1 < 0$ を保ちながら $x - 1 \to -0$ となる。
     > 💡 讲师批注：此处为 $\frac{-1}{-0}$，负负得正，趋向 $+\infty$（日本教材习惯记作 $\infty$）。代入验算：$x = 0.99$ 时 $\frac{-1.01}{-0.01} = 101$，确认无误。

     よって、
     $$\lim_{x \to 1-0} \frac{x-2}{x-1} = \infty$$
- **【最终答案】**
  **$\displaystyle\lim_{x \to 1+0} \frac{x-2}{x-1} = -\infty$，$\displaystyle\lim_{x \to 1-0} \frac{x-2}{x-1} = \infty$**

---

#### 演習問題 3-(4)
- **【原题重现与翻译】**
  - 原题：$x \to 0$ のとき、関数 $\dfrac{x^2-x}{|x|}$ の極限は存在するかどうかを調べよ。
  - 中文：判断当 $x \to 0$ 时，函数 $\dfrac{x^2-x}{|x|}$ 的极限是否存在。
- **【考点定位】**
  - 含绝对值函数的分情况讨论 + 左右极限是否相等的判定。
- **【图解辅助（SVG 矢量图）】**
  画出 $f(x) = \dfrac{x^2-x}{|x|}$ 在 $x=0$ 附近的图像，清晰可见跳跃间断（右极限 $-1$，左极限 $1$）：

<svg viewBox="0 0 420 220" width="420" height="220" xmlns="http://www.w3.org/2000/svg" style="background:#fafafa;border:1px solid #e0e0e0;border-radius:6px;">
  <style>
    .axis { stroke: #333; stroke-width: 1.4; }
    .line { stroke: #2980b9; stroke-width: 2.4; }
    .lbl { font: 12px sans-serif; fill: #333; }
    .hl { font: bold 12px sans-serif; fill: #c0392b; }
  </style>
  <!-- Axes -->
  <line x1="40" y1="110" x2="380" y2="110" class="axis"/>
  <polygon points="380,110 372,106 372,114" fill="#333"/>
  <line x1="210" y1="205" x2="210" y2="18" class="axis"/>
  <polygon points="210,18 206,26 214,26" fill="#333"/>
  <text x="372" y="128" class="lbl">x</text>
  <text x="195" y="28" class="lbl">y</text>
  <text x="196" y="126" class="lbl">O</text>
  <!-- x < 0: y = 1 - x (at x=0, y=1 -> svg y=60; at x=-2, y=3 -> svg x=110, y=20? Let scale: 50px = 1 unit) -->
  <!-- Scale: origin (210,110), 1 unit = 50px -->
  <!-- x < 0: from x=-1.6 (130, 110-2.6*50=-20) -> from x=-1.4 (140, 110-2.4*50=-10) -> let 1 unit = 40px -->
  <!-- Origin (210,110), 1 unit = 40px. y=1 -> 70, y=-1 -> 150 -->
  <!-- Left ray: x<0, y=1-x: at x=-2 (130), y=3 (y=-10) -> at x=-1.5 (150), y=2.5 (y=10) to (210,70) -->
  <line x1="150" y1="10" x2="210" y2="70" class="line"/>
  <!-- Right ray: x>0, y=x-1: from (210,150) to x=3 (330), y=2 (y=30) -->
  <line x1="210" y1="150" x2="330" y2="30" class="line"/>
  <!-- Open circles at (0,1) and (0,-1) -->
  <circle cx="210" cy="70" r="4.5" fill="#fff" stroke="#c0392b" stroke-width="2"/>
  <circle cx="210" cy="150" r="4.5" fill="#fff" stroke="#c0392b" stroke-width="2"/>
  <!-- Ticks & labels -->
  <text x="220" y="74" class="hl">1 (左極限)</text>
  <text x="220" y="155" class="hl">−1 (右極限)</text>
  <text x="72" y="45" class="lbl" fill="#2980b9">y = 1 − x (x &lt; 0)</text>
  <text x="292" y="95" class="lbl" fill="#2980b9">y = x − 1 (x &gt; 0)</text>
</svg>

- **【分步标准解答】**
  $f(x) = \dfrac{x^2-x}{|x|}$ とおく。絶対値記号を外すため、$x$ の符号で場合分けする。
  > 💡 讲师批注：遇到绝对值 $|x|$ 在 $x \to 0$ 处的极限，**必须**分 $x > 0$（右极限）和 $x < 0$（左极限）讨论。

  1. $x > 0$ のとき、$|x| = x$ であるから、
     $$f(x) = \frac{x(x-1)}{x} = x - 1$$
     よって、右側極限は
     $$\lim_{x \to +0} f(x) = \lim_{x \to +0} (x - 1) = -1$$

  2. $x < 0$ のとき、$|x| = -x$ であるから、
     $$f(x) = \frac{x(x-1)}{-x} = -(x - 1) = 1 - x$$
     よって、左側極限は
     $$\lim_{x \to -0} f(x) = \lim_{x \to -0} (1 - x) = 1$$

  以上より、$\displaystyle\lim_{x \to +0} f(x) \neq \lim_{x \to -0} f(x)$ であるから、$x \to 0$ のとき関数 $\dfrac{x^2-x}{|x|}$ の極限は存在しない。
  > 💡 讲师批注：即使左右极限各自存在，只要两者不相等（$-1 \neq 1$），该点极限就不存在。
- **【最终答案】**
  **極限は存在しない（极限不存在）**

---

#### 演習問題 3-(5)-[1]
- **【原题重现与翻译】**
  - 原题：$\displaystyle\lim_{x \to \infty} (x^3 - 3x^2 + 5)$（次の極限値を求めよ。）
  - 中文：求 $\displaystyle\lim_{x \to \infty} (x^3 - 3x^2 + 5)$。
- **【考点定位】**
  - 多项式函数在 $x \to \infty$ 时的极限（$\infty - \infty$ 型不定形，提取最高次项）。
- **【分步标准解答】**
  $$\lim_{x \to \infty} (x^3 - 3x^2 + 5) = \lim_{x \to \infty} x^3 \left(1 - \frac{3}{x} + \frac{5}{x^3}\right)$$
  > 💡 讲师批注：切忌直接写成 $\infty - \infty + 5$！标准规范写法是**提取最高次项 $x^3$**，将不定形转化为「$\infty \times \text{正数}$」。

  ここで、$x \to \infty$ のとき $x^3 \to \infty$ であり、$1 - \dfrac{3}{x} + \dfrac{5}{x^3} \to 1 - 0 + 0 = 1$ であるから、
  $$\lim_{x \to \infty} (x^3 - 3x^2 + 5) = \infty$$
- **【最终答案】**
  **$\infty$**

---

#### 演習問題 3-(5)-[2]
- **【原题重现与翻译】**
  - 原题：$\displaystyle\lim_{x \to -\infty} \frac{3x^2 + 4x - 1}{2x^2 - 3}$
  - 中文：求 $\displaystyle\lim_{x \to -\infty} \frac{3x^2 + 4x - 1}{2x^2 - 3}$。
- **【考点定位】**
  - 有理分式在 $x \to -\infty$ 时的极限（$\frac{\infty}{\infty}$ 型，同除分母最高次项）。
- **【分步标准解答】**
  分母・分子を $x^2$ で割ると、
  $$\lim_{x \to -\infty} \frac{3x^2 + 4x - 1}{2x^2 - 3} = \lim_{x \to -\infty} \frac{3 + \dfrac{4}{x} - \dfrac{1}{x^2}}{2 - \dfrac{3}{x^2}}$$
  > 💡 讲师批注：无论是 $x \to \infty$ 还是 $x \to -\infty$，只要 $k > 0$，均有 $\dfrac{1}{x^k} \to 0$。

  $$= \frac{3 + 0 - 0}{2 - 0} = \frac{3}{2}$$
- **【最终答案】**
  **$\dfrac{3}{2}$**

---

#### 演習問題 3-(5)-[3]
- **【原题重现与翻译】**
  - 原题：$\displaystyle\lim_{x \to \infty} (\sqrt{x^2 - x} - x)$
  - 中文：求 $\displaystyle\lim_{x \to \infty} (\sqrt{x^2 - x} - x)$。
- **【考点定位】**
  - 无理函数的 $\infty - \infty$ 型极限（分子有理化）。
- **【分步标准解答】**
  分子を有理化すると、
  $$\lim_{x \to \infty} (\sqrt{x^2 - x} - x) = \lim_{x \to \infty} \frac{(\sqrt{x^2 - x} - x)(\sqrt{x^2 - x} + x)}{\sqrt{x^2 - x} + x}$$
  $$= \lim_{x \to \infty} \frac{(x^2 - x) - x^2}{\sqrt{x^2 - x} + x} = \lim_{x \to \infty} \frac{-x}{\sqrt{x^2 - x} + x}$$
  > 💡 讲师批注：有理化后从 $\infty - \infty$ 型转化为 $\frac{\infty}{\infty}$ 型。下一步除以 $x$ 时，由于 $x \to \infty$（$x > 0$），可将 $x$ 直接作为 $\sqrt{x^2}$ 放入根号内。

  $x > 0$ であるから、分母・分子を $x$（$=\sqrt{x^2}$）で割ると、
  $$= \lim_{x \to \infty} \frac{-1}{\sqrt{1 - \dfrac{1}{x}} + 1} = \frac{-1}{\sqrt{1 - 0} + 1} = -\frac{1}{2}$$
  > 💡 讲师批注：快速验算技巧：$\sqrt{x^2-x} = \sqrt{(x-\frac{1}{2})^2 - \frac{1}{4}} \approx x - \frac{1}{2}$，减去 $x$ 即得 $-\frac{1}{2}$。
- **【最终答案】**
  **$-\dfrac{1}{2}$**

---

#### 演習問題 3-(5)-[4]
- **【原题重现与翻译】**
  - 原题：$\displaystyle\lim_{x \to -\infty} \frac{4^x}{3^x + 2^x}$
  - 中文：求 $\displaystyle\lim_{x \to -\infty} \frac{4^x}{3^x + 2^x}$。
- **【考点定位】**
  - 指数分式在 $x \to -\infty$ 时的极限（$\frac{0}{0}$ 型，同除**最小底数**的幂或换元 $t=-x$）。
- **【分步标准解答】**
  $t = -x$ とおくと、$x \to -\infty$ のとき $t \to \infty$ である。
  > 💡 讲师批注：**高频易错点！** 当 $x \to -\infty$ 时，$4^x, 3^x, 2^x$ 全部趋近于 $0$，且**底数越小反而越大**（$2^x > 3^x > 4^x$）！强烈推荐换元 $t = -x \to \infty$，把负无穷变成熟悉的正无穷。

  $$\lim_{x \to -\infty} \frac{4^x}{3^x + 2^x} = \lim_{t \to \infty} \frac{4^{-t}}{3^{-t} + 2^{-t}} = \lim_{t \to \infty} \frac{\left(\dfrac{1}{4}\right)^t}{\left(\dfrac{1}{3}\right)^t + \left(\dfrac{1}{2}\right)^t}$$
  分母・分子を $\left(\dfrac{1}{2}\right)^t$（最大項）で割ると、
  $$= \lim_{t \to \infty} \frac{\left(\dfrac{1}{2}\right)^t}{\left(\dfrac{2}{3}\right)^t + 1} = \frac{0}{0 + 1} = 0$$
  > 💡 讲师批注：因为 $0 < \frac{1}{2} < 1$ 且 $0 < \frac{2}{3} < 1$，当 $t \to \infty$ 时两者的 $t$ 次幂均趋于 $0$。如果不换元，直接分子分母同除以 $2^x$ 也可一步得 $\lim_{x\to-\infty}\frac{2^x}{(3/2)^x+1} = \frac{0}{0+1} = 0$。
- **【最终答案】**
  **$0$**

---

#### 演習問題 3-(6)-[1]
- **【原题重现与翻译】**
  - 原题：$\displaystyle\lim_{x \to \infty} \left\{\frac{1}{2}\log_3 x + \log_3(\sqrt{3x+1} - \sqrt{3x-1})\right\}$
  - 中文：求 $\displaystyle\lim_{x \to \infty} \left\{\frac{1}{2}\log_3 x + \log_3(\sqrt{3x+1} - \sqrt{3x-1})\right\}$。
- **【考点定位】**
  - 对数运算法则 + 分子有理化 + 对数函数的连续性。
- **【分步标准解答】**
  対数の性質 $\dfrac{1}{2}\log_3 x = \log_3 \sqrt{x}$ および $\log_3 M + \log_3 N = \log_3 (MN)$ を用いてまとめる。
  $$\frac{1}{2}\log_3 x + \log_3(\sqrt{3x+1} - \sqrt{3x-1}) = \log_3 \left\{\sqrt{x}(\sqrt{3x+1} - \sqrt{3x-1})\right\}$$
  > 💡 讲师批注：先利用对数法则合并成一个 $\log_3(\cdots)$，再单独求真数部分的极限。

  ここで、真数部分を有理化すると、
  $$\sqrt{x}(\sqrt{3x+1} - \sqrt{3x-1}) = \sqrt{x} \cdot \frac{(3x+1) - (3x-1)}{\sqrt{3x+1} + \sqrt{3x-1}} = \frac{2\sqrt{x}}{\sqrt{3x+1} + \sqrt{3x-1}}$$
  分母・分子を $\sqrt{x}$ で割ると、
  $$= \frac{2}{\sqrt{3 + \dfrac{1}{x}} + \sqrt{3 - \dfrac{1}{x}}}$$
  $x \to \infty$ のとき、真数部分の極限は
  $$\lim_{x \to \infty} \frac{2}{\sqrt{3 + \dfrac{1}{x}} + \sqrt{3 - \dfrac{1}{x}}} = \frac{2}{\sqrt{3} + \sqrt{3}} = \frac{1}{\sqrt{3}} = 3^{-\frac{1}{2}}$$
  よって、対数関数の連続性より、
  $$\lim_{x \to \infty} \left\{\frac{1}{2}\log_3 x + \log_3(\sqrt{3x+1} - \sqrt{3x-1})\right\} = \log_3 3^{-\frac{1}{2}} = -\frac{1}{2}$$
- **【最终答案】**
  **$-\dfrac{1}{2}$**

---

#### 演習問題 3-(6)-[2]
- **【原题重现与翻译】**
  - 原题：$\displaystyle\lim_{x \to -\infty} (\sqrt{x^2 + 3x} + x)$
  - 中文：求 $\displaystyle\lim_{x \to -\infty} (\sqrt{x^2 + 3x} + x)$。
- **【考点定位】**
  - $x \to -\infty$ 时的无理函数 $\infty - \infty$ 型极限（**必用换元 $t = -x$ 防符号陷阱**）。
- **【分步标准解答】**
  $t = -x$ とおくと、$x = -t$ であり、$x \to -\infty$ のとき $t \to \infty$ である。
  > 💡 讲师批注：**EJU 最高频失分点！** 很多学生不换元直接有理化，然后在除以 $x$ 时误以为 $\frac{\sqrt{x^2+3x}}{x} = \sqrt{1+\frac{3}{x}}$，忘记了 $x < 0$ 时 $\sqrt{x^2} = -x$，导致正负号完全相反！养成**见 $x \to -\infty$ 先令 $t = -x \to \infty$** 的铁律可 100% 免疫此陷阱。

  $$\lim_{x \to -\infty} (\sqrt{x^2 + 3x} + x) = \lim_{t \to \infty} (\sqrt{t^2 - 3t} - t)$$
  分子を有理化すると、
  $$= \lim_{t \to \infty} \frac{(t^2 - 3t) - t^2}{\sqrt{t^2 - 3t} + t} = \lim_{t \to \infty} \frac{-3t}{\sqrt{t^2 - 3t} + t}$$
  $t > 0$ であるから、分母・分子を $t$（$=\sqrt{t^2}$）で割ると、
  $$= \lim_{t \to \infty} \frac{-3}{\sqrt{1 - \dfrac{3}{t}} + 1} = \frac{-3}{\sqrt{1 - 0} + 1} = -\frac{3}{2}$$
- **【最终答案】**
  **$-\dfrac{3}{2}$**

---

#### 演習問題 3-(6)-[3]
- **【原题重现与翻译】**
  - 原题：$\displaystyle\lim_{x \to \infty} (3^x + 5^x)^{\frac{1}{x}}$
  - 中文：求 $\displaystyle\lim_{x \to \infty} (3^x + 5^x)^{\frac{1}{x}}$。
- **【考点定位】**
  - 指数和的 $\frac{1}{x}$ 次幂极限（**夹逼定理 / はさみうちの原理** 经典应用）。
- **【图解辅助（SVG 矢量图）】**
  夹逼定理（はさみうちの原理）结构示意：$5 < (3^x+5^x)^{1/x} < 5 \cdot 2^{1/x}$：

<svg viewBox="0 0 460 190" width="460" height="190" xmlns="http://www.w3.org/2000/svg" style="background:#fafafa;border:1px solid #e0e0e0;border-radius:6px;">
  <style>
    .axis { stroke: #333; stroke-width: 1.3; }
    .upper { fill: none; stroke: #e67e22; stroke-width: 2; stroke-dasharray: 6,3; }
    .mid { fill: none; stroke: #2980b9; stroke-width: 2.5; }
    .lower { stroke: #27ae60; stroke-width: 2; }
    .lbl { font: 12px sans-serif; fill: #333; }
  </style>
  <!-- Axes -->
  <line x1="40" y1="160" x2="430" y2="160" class="axis"/>
  <polygon points="430,160 422,156 422,164" fill="#333"/>
  <line x1="60" y1="175" x2="60" y2="18" class="axis"/>
  <polygon points="60,18 56,26 64,26" fill="#333"/>
  <text x="420" y="176" class="lbl">x</text>
  <text x="45" y="28" class="lbl">y</text>
  <text x="45" y="174" class="lbl">O</text>
  <!-- Lower bound y = 5 (svg y = 110) -->
  <line x1="60" y1="110" x2="415" y2="110" class="lower"/>
  <text x="42" y="114" class="lbl" fill="#27ae60" font-weight="bold">5</text>
  <text x="305" y="130" class="lbl" fill="#27ae60">下界: y = 5</text>
  <!-- Upper bound y = 5 * 2^(1/x) -->
  <path d="M 85,22 Q 130,80 220,97 Q 310,104 415,107" class="upper"/>
  <text x="155" y="42" class="lbl" fill="#d35400">上界: y = 5 · 2^(1/x) → 5</text>
  <!-- Middle curve y = (3^x + 5^x)^(1/x) -->
  <path d="M 85,55 Q 140,95 230,105 Q 320,108 415,109" class="mid"/>
  <text x="200" y="75" class="lbl" fill="#2980b9" font-weight="bold">y = (3ˣ + 5ˣ)^(1/x) → 5</text>
</svg>

- **【分步标准解答】**
  $x > 0$ のとき、$0 < 3^x < 5^x$ であるから、
  $$5^x < 3^x + 5^x < 5^x + 5^x = 2 \cdot 5^x$$
  > 💡 讲师批注：核心放缩技巧——将较小项 $3^x$ 向下放缩为 $0$、向上放缩为最大项 $5^x$。

  各辺は正であるから、$\dfrac{1}{x}$ 乗すると（$\dfrac{1}{x} > 0$ より不等号の向きは変わらない）、
  $$5 < (3^x + 5^x)^{\frac{1}{x}} < 2^{\frac{1}{x}} \cdot 5$$
  ここで、$x \to \infty$ のとき $\dfrac{1}{x} \to 0$ であるから、
  $$\lim_{x \to \infty} \left(2^{\frac{1}{x}} \cdot 5\right) = 2^0 \cdot 5 = 5$$
  よって、はさみうちの原理より、
  $$\lim_{x \to \infty} (3^x + 5^x)^{\frac{1}{x}} = 5$$
  > 💡 讲师批注：另解（直接提取最大底数）：$(3^x+5^x)^{\frac{1}{x}} = 5\left\{1 + \left(\frac{3}{5}\right)^x\right\}^{\frac{1}{x}} \to 5 \cdot 1^0 = 5$。两种方法均可，但日本教材标准答案偏爱夹逼定理。
- **【最终答案】**
  **$5$**

---

#### 演習問題 3-(7)-[1]
- **【原题重现与翻译】**
  - 原题：$\displaystyle\lim_{x \to 0} \frac{\sin 3x}{x}$
  - 中文：求 $\displaystyle\lim_{x \to 0} \frac{\sin 3x}{x}$。
- **【考点定位】**
  - 三角函数基本极限 $\displaystyle\lim_{\theta \to 0} \frac{\sin\theta}{\theta} = 1$ 的配系数变形。
- **【分步标准解答】**
  $$\lim_{x \to 0} \frac{\sin 3x}{x} = \lim_{x \to 0} \left(\frac{\sin 3x}{3x} \cdot 3\right)$$
  > 💡 讲师批注：核心原则——**$\sin(\text{框})$ 下面的分母必须和「框」完全一致**，因此分母配 $3$，同时乘 $3$ 保持值不变。

  $x \to 0$ のとき $3x \to 0$ であり、$\displaystyle\lim_{3x \to 0} \frac{\sin 3x}{3x} = 1$ であるから、
  $$= 1 \cdot 3 = 3$$
- **【最终答案】**
  **$3$**

---

#### 演習問題 3-(7)-[2]
- **【原题重现与翻译】**
  - 原题：$\displaystyle\lim_{x \to 0} \frac{\tan x^\circ}{x}$
  - 中文：求 $\displaystyle\lim_{x \to 0} \frac{\tan x^\circ}{x}$。
- **【考点定位】**
  - 角度制（度数法）与弧度制（弧度法）的换算 + 三角函数极限。
- **【分步标准解答】**
  角の大きさを弧度法で表すと、$x^\circ = \dfrac{\pi}{180} x$（ラジアン）である。
  > 💡 讲师批注：**经典陷阱题！** 公式 $\displaystyle\lim_{\theta\to 0}\frac{\sin\theta}{\theta}=1$ 与 $\displaystyle\lim_{\theta\to 0}\frac{\tan\theta}{\theta}=1$ **仅在弧度制下成立**！看到度数符号 $^\circ$，第一步必须转化为 $\dfrac{\pi}{180}x$。

  よって、
  $$\lim_{x \to 0} \frac{\tan x^\circ}{x} = \lim_{x \to 0} \frac{\tan\left(\dfrac{\pi}{180} x\right)}{x} = \lim_{x \to 0} \left\{\frac{\sin\left(\dfrac{\pi}{180} x\right)}{\dfrac{\pi}{180} x} \cdot \frac{1}{\cos\left(\dfrac{\pi}{180} x\right)} \cdot \frac{\pi}{180}\right\}$$
  $x \to 0$ のとき $\dfrac{\pi}{180} x \to 0$ であるから、
  $$= 1 \cdot \frac{1}{1} \cdot \frac{\pi}{180} = \frac{\pi}{180}$$
- **【最终答案】**
  **$\dfrac{\pi}{180}$**

---

#### 演習問題 3-(7)-[3]
- **【原题重现与翻译】**
  - 原题：$\displaystyle\lim_{x \to 0} \frac{x^2}{1 - \cos x}$
  - 中文：求 $\displaystyle\lim_{x \to 0} \frac{x^2}{1 - \cos x}$。
- **【考点定位】**
  - $1 - \cos x$ 型三角函数极限（共轭相乘法或半角公式法）。
- **【分步标准解答】**
  分母・分子に $1 + \cos x$ を掛けると、$1 - \cos^2 x = \sin^2 x$ であるから、
  $$\lim_{x \to 0} \frac{x^2}{1 - \cos x} = \lim_{x \to 0} \frac{x^2(1 + \cos x)}{1 - \cos^2 x} = \lim_{x \to 0} \frac{x^2(1 + \cos x)}{\sin^2 x}$$
  $$= \lim_{x \to 0} \left\{\left(\frac{x}{\sin x}\right)^2 (1 + \cos x)\right\}$$
  > 💡 讲师批注：因为 $\displaystyle\lim_{x \to 0}\frac{\sin x}{x} = 1$，其倒数极限 $\displaystyle\lim_{x \to 0}\frac{x}{\sin x} = 1$ 同样成立。也可利用半角公式 $1 - \cos x = 2\sin^2\frac{x}{2}$ 求解。

  $$= 1^2 \cdot (1 + 1) = 2$$
- **【最终答案】**
  **$2$**

---

#### 演習問題 3-(7)-[4]
- **【原题重现与翻译】**
  - 原题：$\displaystyle\lim_{x \to \frac{\pi}{2}} \frac{\cos x}{2x - \pi}$
  - 中文：求 $\displaystyle\lim_{x \to \frac{\pi}{2}} \frac{\cos x}{2x - \pi}$。
- **【考点定位】**
  - 非零点处的三角函数 $\frac{0}{0}$ 型极限（平移换元 $t = x - \frac{\pi}{2}$）。
- **【分步标准解答】**
  $t = x - \dfrac{\pi}{2}$ とおくと、$x = t + \dfrac{\pi}{2}$ であり、$x \to \dfrac{\pi}{2}$ のとき $t \to 0$ である。
  また、$2x - \pi = 2t$、$\cos\left(t + \dfrac{\pi}{2}\right) = -\sin t$ であるから、
  > 💡 讲师批注：凡是 $x \to a$（$a \neq 0$）的三角极限，第一时间令 $t = x - a \to 0$，再利用诱导公式化为 $\sin t$ 或 $\cos t$。

  $$\lim_{x \to \frac{\pi}{2}} \frac{\cos x}{2x - \pi} = \lim_{t \to 0} \frac{-\sin t}{2t} = -\frac{1}{2} \lim_{t \to 0} \frac{\sin t}{t} = -\frac{1}{2} \cdot 1 = -\frac{1}{2}$$
  > 💡 讲师批注：诱导公式 $\cos(t + \frac{\pi}{2}) = -\sin t$ 切勿漏掉负号！可用特值 $t = \frac{\pi}{6}$ 检验：$\cos\frac{2\pi}{3} = -\frac{1}{2} = -\sin\frac{\pi}{6}$。
- **【最终答案】**
  **$-\dfrac{1}{2}$**

---

#### 演習問題 3-(7)-[5]
- **【原题重现与翻译】**
  - 原题：$\displaystyle\lim_{x \to \infty} x \sin \frac{1}{x}$
  - 中文：求 $\displaystyle\lim_{x \to \infty} x \sin \frac{1}{x}$。
- **【考点定位】**
  - 倒数换元 $t = \frac{1}{x}$ 转化为 $\frac{\sin t}{t}$ 型基本极限。
- **【分步标准解答】**
  $t = \dfrac{1}{x}$ とおくと、$x = \dfrac{1}{t}$ であり、$x \to \infty$ のとき $t \to +0$ である。
  $$\lim_{x \to \infty} x \sin \frac{1}{x} = \lim_{t \to +0} \frac{\sin t}{t} = 1$$
  > 💡 讲师批注：因为 $\displaystyle\lim_{t \to 0} \frac{\sin t}{t} = 1$，所以其右极限 $\displaystyle\lim_{t \to +0} \frac{\sin t}{t}$ 同样等于 $1$。
- **【最终答案】**
  **$1$**

---

#### 演習問題 3-(7)-[6]
- **【原题重现与翻译】**
  - 原题：$\displaystyle\lim_{x \to 0} x^2 \sin \frac{1}{x}$
  - 中文：求 $\displaystyle\lim_{x \to 0} x^2 \sin \frac{1}{x}$。
- **【考点定位】**
  - 无穷小量 $\times$ 有界振荡函数（**夹逼定理 / はさみうちの原理**）。
- **【图解辅助（SVG 矢量图）】**
  $y = x^2 \sin\dfrac{1}{x}$ 被包络线 $y = x^2$ 与 $y = -x^2$ 夹紧至原点 $(0, 0)$：

<svg viewBox="0 0 420 210" width="420" height="210" xmlns="http://www.w3.org/2000/svg" style="background:#fafafa;border:1px solid #e0e0e0;border-radius:6px;">
  <style>
    .axis { stroke: #333; stroke-width: 1.3; }
    .env { fill: none; stroke: #e67e22; stroke-width: 1.6; stroke-dasharray: 5,3; }
    .osc { fill: none; stroke: #2980b9; stroke-width: 1.8; }
    .lbl { font: 12px sans-serif; fill: #333; }
  </style>
  <!-- Axes -->
  <line x1="30" y1="105" x2="390" y2="105" class="axis"/>
  <polygon points="390,105 382,101 382,109" fill="#333"/>
  <line x1="210" y1="195" x2="210" y2="15" class="axis"/>
  <polygon points="210,15 206,23 214,23" fill="#333"/>
  <text x="382" y="122" class="lbl">x</text>
  <text x="195" y="25" class="lbl">y</text>
  <text x="196" y="120" class="lbl">O</text>
  <!-- Envelopes y = x^2 and y = -x^2 -->
  <path d="M 60,25 Q 210,185 360,25" class="env"/>
  <path d="M 60,185 Q 210,25 360,185" class="env"/>
  <!-- Oscillating curve y = x^2 sin(1/x) schematic -->
  <path d="M 70,55 C 100,155 125,65 148,132 C 165,86 178,120 188,96 C 196,112 203,101 210,105 C 217,109 224,98 232,114 C 242,90 255,124 272,78 C 295,145 320,55 350,155" class="osc"/>
  <!-- Labels -->
  <text x="295" y="34" class="lbl" fill="#d35400">y = x²</text>
  <text x="295" y="185" class="lbl" fill="#d35400">y = −x²</text>
  <text x="48" y="20" class="lbl" fill="#2980b9" font-weight="bold">y = x² sin(1/x) → 0</text>
</svg>

- **【分步标准解答】**
  $x \neq 0$ のとき、$-1 \le \sin\dfrac{1}{x} \le 1$ である。
  各辺に $x^2 > 0$ を掛けると、
  $$-x^2 \le x^2 \sin\frac{1}{x} \le x^2$$
  > 💡 讲师批注：当 $x \to 0$ 时 $\sin\frac{1}{x}$ 在 $[-1, 1]$ 之间剧烈振荡、极限不存在，因此**绝对不能**拆成 $\lim x^2 \cdot \lim \sin\frac{1}{x}$！必须使用夹逼定理。

  ここで、$\displaystyle\lim_{x \to 0} (-x^2) = 0$、$\displaystyle\lim_{x \to 0} x^2 = 0$ であるから、はさみうちの原理より、
  $$\lim_{x \to 0} x^2 \sin\frac{1}{x} = 0$$
- **【最终答案】**
  **$0$**

---

#### 演習問題 3-(8)-(1)
- **【原题重现与翻译】**
  - 原题：$\displaystyle\lim_{x \to \infty} \left(1 - \frac{1}{x}\right)^x$
  - 中文：求 $\displaystyle\lim_{x \to \infty} \left(1 - \frac{1}{x}\right)^x$。
- **【考点定位】**
  - 自然对数底 $e$ 的极限公式 $\displaystyle\lim_{t \to \pm\infty} \left(1 + \frac{1}{t}\right)^t = e$。
- **【分步标准解答】**
  $t = -x$ とおくと、$x = -t$ であり、$x \to \infty$ のとき $t \to -\infty$ である。
  > 💡 讲师批注：把括号内凑成标准的 $1 + \dfrac{1}{t}$ 形式，注意同时把指数 $x$ 写成 $-t$。

  $$\lim_{x \to \infty} \left(1 - \frac{1}{x}\right)^x = \lim_{t \to -\infty} \left(1 + \frac{1}{t}\right)^{-t} = \lim_{t \to -\infty} \left\{\left(1 + \frac{1}{t}\right)^t\right\}^{-1}$$
  $\displaystyle\lim_{t \to -\infty} \left(1 + \frac{1}{t}\right)^t = e$ であるから、
  $$= e^{-1} = \frac{1}{e}$$
- **【最终答案】**
  **$\dfrac{1}{e}$**

---

#### 演習問題 3-(8)-(2)
- **【原题重现与翻译】**
  - 原题：$\displaystyle\lim_{x \to 0} \frac{e^x - 1}{x}$
  - 中文：求 $\displaystyle\lim_{x \to 0} \frac{e^x - 1}{x}$。
- **【考点定位】**
  - 指数函数基本极限公式的推导（换元 $t = e^x - 1$ 结合 $e$ 的定义）。
- **【分步标准解答】**
  $e^x - 1 = t$ とおくと、$e^x = 1 + t$ より $x = \log(1 + t)$ である。また、$x \to 0$ のとき $t \to 0$ である。
  > 💡 讲师批注：这是指数函数求导的核心前置极限。注意日本数学Ⅲ中 $\log$ 默认以 $e$ 为底。

  よって、
  $$\lim_{x \to 0} \frac{e^x - 1}{x} = \lim_{t \to 0} \frac{t}{\log(1 + t)} = \lim_{t \to 0} \frac{1}{\dfrac{1}{t}\log(1 + t)} = \lim_{t \to 0} \frac{1}{\log(1 + t)^{\frac{1}{t}}}$$
  ここで、$\displaystyle\lim_{t \to 0} (1 + t)^{\frac{1}{t}} = e$ であるから、対数関数の連続性より、
  $$= \frac{1}{\log e} = \frac{1}{1} = 1$$
- **【最终答案】**
  **$1$**

---

#### 演習問題 3-(9)-(1)
- **【原题重现与翻译】**
  - 原题：$\displaystyle\lim_{x \to 0} \frac{\log(1 + x)}{x}$
  - 中文：求 $\displaystyle\lim_{x \to 0} \frac{\log(1 + x)}{x}$。
  > ⚠️ **教材勘误提示**：原教材 P304（`page_0305.jpg`）将本题及下一题的对数真数误排为上标（印作 $\log^{(1+x)}$ 与 $\log^{(a+2x)} - \log^{(a)}$），授课时务必提示学生正确写法为 $\log(1+x)$ 与 $\log(a+2x) - \log a$（其中 $a > 0$）。
- **【考点定位】**
  - 对数函数基本极限公式的推导（利用 $e = \lim_{x\to 0}(1+x)^{\frac{1}{x}}$）。
- **【分步标准解答】**
  $$\lim_{x \to 0} \frac{\log(1 + x)}{x} = \lim_{x \to 0} \left\{\frac{1}{x} \log(1 + x)\right\} = \lim_{x \to 0} \log(1 + x)^{\frac{1}{x}}$$
  > 💡 讲师批注：把系数 $\frac{1}{x}$ 放到真数的指数位置，即出现 $e$ 的定义式 $(1+x)^{\frac{1}{x}}$。

  $\displaystyle\lim_{x \to 0} (1 + x)^{\frac{1}{x}} = e$ であり、対数関数の連続性より、
  $$= \log e = 1$$
- **【最终答案】**
  **$1$**

---

#### 演習問題 3-(9)-(2)
- **【原题重现与翻译】**
  - 原题：$\displaystyle\lim_{x \to 0} \frac{\log(a + 2x) - \log a}{x}$ （ただし $a > 0$）
  - 中文：求 $\displaystyle\lim_{x \to 0} \frac{\log(a + 2x) - \log a}{x}$（其中 $a > 0$）。
- **【考点定位】**
  - 对数减法合并 + 换元转化为 $\displaystyle\lim_{t\to 0}\frac{\log(1+t)}{t} = 1$。
- **【分步标准解答】**
  対数の性質より、
  $$\lim_{x \to 0} \frac{\log(a + 2x) - \log a}{x} = \lim_{x \to 0} \frac{1}{x} \log\frac{a + 2x}{a} = \lim_{x \to 0} \frac{1}{x} \log\left(1 + \frac{2x}{a}\right)$$
  ここで、$t = \dfrac{2x}{a}$ とおくと、$x = \dfrac{a}{2} t$ であり、$x \to 0$ のとき $t \to 0$ である。
  > 💡 讲师批注：配凑 $\log(1 + \text{框})$ 与分母的「框」一致即可。也可用导数定义直觉验算：原式为 $2 \cdot \left.\frac{d}{du}\log u\right|_{u=a} = \frac{2}{a}$。

  よって、
  $$= \lim_{t \to 0} \frac{2}{a} \cdot \frac{\log(1 + t)}{t} = \frac{2}{a} \cdot 1 = \frac{2}{a}$$
- **【最终答案】**
  **$\dfrac{2}{a}$**

---

#### 演習問題 3-(10)
- **【原题重现与翻译】**
  - 原题：$\displaystyle\lim_{x \to 0} (1 + x + x^2)^{\frac{1}{x}}$ を求めよ。
  - 中文：求 $\displaystyle\lim_{x \to 0} (1 + x + x^2)^{\frac{1}{x}}$。
- **【考点定位】**
  - $1^\infty$ 型不定形（将 $x + x^2$ 整体视作无穷小量 $u$，凑 $(1+u)^{\frac{1}{u}}$ 结构）。
- **【分步标准解答】**
  $u = x + x^2 = x(1 + x)$ とおく。$x \to 0$ のとき $u \to 0$ である（$x = 0$ の十分近くで $x \neq 0$ ならば $1 + x \neq 0$ より $u \neq 0$）。
  > 💡 讲师批注：把括号内除 $1$ 以外的整体记作 $u = x+x^2$，指数 $\frac{1}{x}$ 改写为 $\frac{1}{u} \cdot \frac{u}{x} = \frac{1}{u} \cdot (1+x)$，这是解决所有 $1^\infty$ 型极限的万能模板！

  $$(1 + x + x^2)^{\frac{1}{x}} = (1 + u)^{\frac{1}{u} \cdot \frac{u}{x}} = \left\{(1 + u)^{\frac{1}{u}}\right\}^{1 + x}$$
  ここで、$x \to 0$ のとき $u \to 0$ であるから $\displaystyle\lim_{u \to 0} (1 + u)^{\frac{1}{u}} = e$、かつ $\displaystyle\lim_{x \to 0} (1 + x) = 1$ である。
  よって、
  $$\lim_{x \to 0} (1 + x + x^2)^{\frac{1}{x}} = e^1 = e$$
- **【最终答案】**
  **$e$**
