# 《EJU 教材全解与备课讲义》数学 024-B（P353–P360）

> **对应源文件**：`work_math/ocr_md/ocr_024_p346-360.md`（后半部分：第 14 节「不定積分とその基本性質」、第 15 节「不定積分の求め方」、基本公式总结及演習問題 13）
> **视觉核对参考图**：`work_math/ref_imgs/page_0353.jpg` – `page_0360.jpg`（逐页逐式全量核对）
> **同切片上篇**：[`note_024_a.md`](./note_024_a.md)（P346–P352：渐近线、图像概形、公切线、微分在方程与不等式中的应用）

---

## 一、国内高中基础知识点唤醒与 EJU 考纲差异对比

从第 353 页起，教材正式进入 **数学Ⅲ《积分法（積分法）》** 的开篇——**不定积分（不定積分）**。不定积分本质上是微分的逆运算，也是后续定积分计算、面积体积求解的绝对核心基本功。

### 1.1 不定积分的定义与线性性质（[14.1]・[14.2]）

1. **定义**：若函数 $F(x)$ 的导数为 $f(x)$（即 $F'(x) = f(x)$），则称 $F(x)$ 为 $f(x)$ 的**原函数（原始関数）**，记作：
   $$\int f(x)\,dx = F(x) + C \qquad (C \text{ は積分定数})$$
   - $f(x)$ 称为**被积函数（被積分関数）**，$x$ 称为**积分变量（積分変数）**，$C$ 称为**积分常数（積分定数）**。
   > ⚠️ **教材勘误提示**：原教材第 352 页（`page_0353.jpg`）将「被積分関数」误印为「被積分**定数**」（第 354 页解说中已正确写作「被積分関数」），授课时请提醒学生更正。

   <svg viewBox="0 0 460 120" width="80%" xmlns="http://www.w3.org/2000/svg" style="background:#fafafa;border:1px solid #e5e7eb;border-radius:8px;">
     <defs>
       <marker id="arrowR" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto">
         <path d="M 0 0 L 10 5 L 0 10 z" fill="#2563eb"/>
       </marker>
       <marker id="arrowL" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto">
         <path d="M 0 0 L 10 5 L 0 10 z" fill="#dc2626"/>
       </marker>
     </defs>
     <!-- 左右方框 -->
     <rect x="45" y="38" width="115" height="44" rx="8" fill="#eff6ff" stroke="#2563eb" stroke-width="1.5"/>
     <text x="102" y="57" font-size="14" font-weight="bold" fill="#1e40af" text-anchor="middle">F(x) + C</text>
     <text x="102" y="74" font-size="10" fill="#475569" text-anchor="middle">原始関数（不定積分）</text>

     <rect x="300" y="38" width="115" height="44" rx="8" fill="#fef2f2" stroke="#dc2626" stroke-width="1.5"/>
     <text x="357" y="57" font-size="14" font-weight="bold" fill="#991b1b" text-anchor="middle">f(x)</text>
     <text x="357" y="74" font-size="10" fill="#475569" text-anchor="middle">導関数（被積分関数）</text>

     <!-- 上箭头：微分 -->
     <path d="M 165 48 Q 230 22 292 48" fill="none" stroke="#2563eb" stroke-width="1.8" marker-end="url(#arrowR)"/>
     <text x="230" y="25" font-size="11" font-weight="bold" fill="#2563eb" text-anchor="middle">微分する：d/dx</text>

     <!-- 下箭头：積分 -->
     <path d="M 295 72 Q 230 98 168 72" fill="none" stroke="#dc2626" stroke-width="1.8" marker-end="url(#arrowL)"/>
     <text x="230" y="106" font-size="11" font-weight="bold" fill="#dc2626" text-anchor="middle">積分する：∫ f(x) dx</text>
   </svg>

2. **线性性质**（$k, l$ 为常数）：
   $$\int \{k f(x) + l g(x)\}\,dx = k\int f(x)\,dx + l\int g(x)\,dx$$
   - 注意：$\int 1\,dx$ 常省略 $1$ 写作 $\int dx = x + C$；多个不定积分合并时，积分常数统一在末尾只写**一个 $C$**。

### 1.2 基本初等函数的不定积分公式（[14.3]・[14.4]・P357 总结）

设 $C$ 为积分常数：
1. **幂函数与倒数**：
   $$\int x^\alpha\,dx = \frac{x^{\alpha+1}}{\alpha+1} + C \quad (\alpha \neq -1), \qquad \int \frac{1}{x}\,dx = \log|x| + C$$
2. **三角函数**：
   $$\int \sin x\,dx = -\cos x + C, \qquad \int \cos x\,dx = \sin x + C$$
   $$\int \frac{1}{\cos^2 x}\,dx = \tan x + C, \qquad \int \frac{1}{\sin^2 x}\,dx = -\frac{1}{\tan x} + C \quad (= -\cot x + C)$$
3. **指数函数**：
   $$\int e^x\,dx = e^x + C, \qquad \int a^x\,dx = \frac{a^x}{\log a} + C \quad (a > 0,\; a \neq 1)$$
4. **一次复合型 $f(ax + b)$ 的不定积分（[14.4]）**：若 $F'(x) = f(x)$ 且 $a \neq 0$，则
   $$\int f(ax + b)\,dx = \frac{1}{a}F(ax + b) + C$$
   - 口诀：**「照常积分，再除以一次项系数 $a$」**。
5. **大学拓展型补充公式（教材 P357 总结表）**：
   $$\int \frac{1}{\sqrt{1 - x^2}}\,dx = \sin^{-1}x + C, \qquad \int \frac{1}{1 + x^2}\,dx = \tan^{-1}x + C$$
   $$\int \frac{1}{\sqrt{x^2 + 1}}\,dx = \log\left(x + \sqrt{x^2 + 1}\right) + C, \qquad \int \frac{1}{\sqrt{x^2 - 1}}\,dx = \log\left|x + \sqrt{x^2 - 1}\right| + C$$
   $$\int \frac{1}{1 - x^2}\,dx = \frac{1}{2}\log\left|\frac{1 + x}{1 - x}\right| + C \quad (|x| < 1\text{ 时为 }\tanh^{-1}x + C = \frac{1}{2}\log\frac{1 + x}{1 - x} + C)$$

> ⚠️ **教材勘误提示（P353 & P357 多处印刷错误）**：
> 1. 原教材第 353 页（`page_0354.jpg`）将 $\int \dfrac{dx}{\cos^2 x}$ 与 $\int \dfrac{dx}{\sin^2 x}$ 重复印成了 $\int \dfrac{dx}{\cos^2 x}\,dx$ 和 $\int \dfrac{dx}{\sin^2 x}\,dx$（多了一个 $dx$）；且「指数関数」编号误印为 `[2]`（应为 `[3]`）；`[14.4]` 中「$a \neq 0$ とすとき」漏印「る」（应为「とするとき」）。
> 2. **严重符号错误！** 原教材第 357 页（`page_0358.jpg`）右侧第 6 行将 $\int \dfrac{1}{1 - x^2}\,dx$ 误印为 $\dfrac{1}{2}\log\dfrac{1 - x}{1 + x} + C$（分子分母写反，求导后差一个负号！）。正确结果应为 **$\dfrac{1}{2}\log\dfrac{1 + x}{1 - x} + C$**（$|x| < 1$）。
> 3. 原教材第 357 页 $\int x^a\,dx = \dfrac{x^{a+1}}{a+1} + C$ 漏注 $a \neq -1$ 条件，且混用了 $\ln$ 与 $\log$。

### 1.3 换元积分法与分部积分法（[14.5]・[14.6]）

1. **换元积分法（置換積分法）**：
   - 第一换元（令 $x = g(t)$）：$\displaystyle\int f(x)\,dx = \int f(g(t))\,g'(t)\,dt$
   - 第二换元（凑微分，令 $u = g(x)$）：$\displaystyle\int f(g(x))\,g'(x)\,dx = \int f(u)\,du$
   - 高频特例：
     $$\int \{g(x)\}^\alpha g'(x)\,dx = \frac{\{g(x)\}^{\alpha+1}}{\alpha+1} + C \quad (\alpha \neq -1), \qquad \int \frac{g'(x)}{g(x)}\,dx = \log|g(x)| + C$$
2. **分部积分法（部分積分法）**：
   $$\int f(x)g'(x)\,dx = f(x)g(x) - \int f'(x)g(x)\,dx$$
   - 特别地，取 $g(x) = x$（即把 $1$ 看作 $x'$）：$\displaystyle\int f(x)\,dx = x f(x) - \int x f'(x)\,dx$。
   - **必背黄金结论**：$\displaystyle\int \log x\,dx = x\log x - x + C$。

### 1.4 五大类函数的积分策略总览（[15.1]–[15.5]）

| 函数类型 | 核心变形 / 换元策略 | 典型例子 |
| :--- | :--- | :--- |
| **[15.1] 分式函数（分数関数）** | ① 观察 $\dfrac{g'(x)}{g(x)}$ 型；② 假分式先降次（帯分数化）；③ 部分分式分解（裂项）；④ 含 $(ax+b)^n$ 令 $ax+b=t$ | $\dfrac{x^2+1}{x-1} = x + 1 + \dfrac{2}{x-1}$ |
| **[15.2] 无理函数（無理関数）** | ① 分母有理化；② 含 $\sqrt[n]{ax+b}$ 令 $\sqrt[n]{ax+b}=t$；③ $g'(x)\sqrt{g(x)}$ 令 $g(x)=t$；④ $\sqrt{x^2+A}$ 令 $x+\sqrt{x^2+A}=t$ | $\int \dfrac{x}{\sqrt{x+1}}\,dx$ 令 $\sqrt{x+1}=t$ |
| **[15.3] 三角函数（三角関数）** | ① 凑 $f(\sin x)\cos x$ 或 $g(\cos x)\sin x$；② 用倍角/三倍角/积化和差降次为 1 次；③ 分部积分；④ 递推式 | $\cos^2 2x = \dfrac{1+\cos 4x}{2}$ |
| **[15.4] 指数・对数函数** | ① 找 $f(a^x)(a^x)'$；② 分部积分（熟记 $\int \log x\,dx = x\log x - x + C$）；③ 递推式 | $\int x e^x\,dx$、$\int x\log x\,dx$ |
| **[15.5] 指数 $\times$ 三角函数** | 连续两次分部积分，出现**同形循环（同形出現）**后移项解方程 | $\int e^x \sin x\,dx$ |

### 1.5 国内高中 vs. 日本 EJU 考纲差异对比

| 对比维度 | 国内高中（新高考）习惯 | 日本 EJU（数学Ⅲ）习惯 | 备课/应试提醒 |
| :--- | :--- | :--- | :--- |
| **微积分考查深度** | 新高考已**大幅删减定积分与不定积分**，仅保留极少量选学 | **数学Ⅲ 核心大题！** 换元积分、分部积分、分式/三角/无理积分全覆盖 | 国内普高生在此章几乎是零基础，必须从头系统训练积分基本功 |
| **$\int \frac{1}{x}\,dx$ 的绝对值** | 部分学生易忘写绝对值符号 | **严格要求写 $\log|x| + C$**（除非题干已限定 $x>0$） | 漏写绝对值在描述题中会扣分，务必养成习惯 |
| **积分常数 $C$** | 有时默认省略 | **必须在答案末尾注明「（$C$ は積分定数）」** | 不定积分不写 $+C$ 会直接判错 |
| **$\sec, \csc, \cot$ 与反三角** | 大学高数内容 | EJU 考纲**不直接考** $\sec, \csc, \sin^{-1}x, \sinh^{-1}x$（教材 P357 仅作拓展参考） | EJU 标准写法一律用 $\dfrac{1}{\cos x},\; \dfrac{1}{\tan x}$ 表示 |

---

## 二、日文核心词汇与公式假名注音

### 2.1 本部分日文核心词汇

- 不定積分（ふていせきぶん / futei sekibun） — 不定积分
- 原始関数（げんしかんすう / genshi kansuu） — 原函数（原始函数）
- 積分する（せきぶんする / sekibun suru） — 求积分、积分
- 積分定数（せきぶんていすう / sekibun teisuu） — 积分常数（$C$）
- 被積分関数（ひせきぶんかんすう / hisekibun kansuu） — 被积函数
- 積分変数（せきぶんへんすう / sekibun hensuu） — 积分变量
- 置換積分法（ちかんせきぶんほう / chikan sekibunhou） — 换元积分法（置换积分法）
- 部分積分法（ぶぶんせきぶんほう / bubun sekibunhou） — 分部积分法
- 分数関数（ぶんすうかんすう / bunsuu kansuu） — 分式函数（有理函数）
- 無理関数（むりかんすう / muri kansuu） — 无理函数（根式函数）
- 逆三角関数（ぎゃくさんかくかんすう / gyaku sankaku kansuu） — 反三角函数（$\sin^{-1}x, \tan^{-1}x$ 等）
- 双曲線関数（そうきょくせんかんすう / soukyokusen kansuu） — 双曲函数（$\sinh x, \cosh x, \tanh x$）

### 2.2 核心公式的日本课堂口语读法

1. **不定积分定义** $\displaystyle\int f(x)\,dx = F(x) + C$
   - 课堂读法：**インテグラル エフ エックス ディーエックス イコール ラージエフ エックス たす シー**
   - 备注：积分号 $\int$ 读作 **インテグラル（integral）**；大写 $F$ 读作 **ラージエフ（large F）** 以区分小写 $f$。
2. **倒数积分** $\displaystyle\int \frac{1}{x}\,dx = \log|x| + C$
   - 课堂读法：**インテグラル エックス ぶんの いち ディーエックス イコール ログ ぜったいち エックス たす シー**
3. **一次复合积分** $\displaystyle\int f(ax + b)\,dx = \frac{1}{a}F(ax + b) + C$
   - 课堂读法：**インテグラル エフ かっこ エーエックス たす ビー かっことじ ディーエックス イコール エーぶんのいち ラージエフ かっこ エーエックス たす ビー かっことじ たす シー**

---

## 三、逐题深度解析（不可跳步）

> 注：以下所有不定积分答案中，$C$ 均表示**積分定数（积分常数）**。每道题完成后都必须用**「对答案求导，看是否还原为被积函数」**进行 100% 反向验算！

---

### 演習問題 13（不定積分の基本計算）

#### 演習問題 13-(1)
- **【原题重现与翻译】**
  - 原题：次の不定積分を求めよ。
    [1] $\displaystyle\int (x - 1)^3\,dx - \int (x + 1)^3\,dx$
    [2] $\displaystyle\int (t - x)(2t + x)\,dx$
  - 中文：求下列不定积分。
    [1] $\displaystyle\int (x - 1)^3\,dx - \int (x + 1)^3\,dx$
    [2] $\displaystyle\int (t - x)(2t + x)\,dx$
- **【考点定位】**
  - 不定积分的线性合并（先合再积，大幅简化计算）；区分积分变量 $x$ 与常数参数 $t$。
- **【分步标准解答】**
  **[1]** 不定積分の線形性により、1 つの積分にまとめてから展開する：
  $$\begin{aligned}
  \int (x - 1)^3\,dx - \int (x + 1)^3\,dx &= \int \left\{(x - 1)^3 - (x + 1)^3\right\} dx \\
  &= \int \left\{(x^3 - 3x^2 + 3x - 1) - (x^3 + 3x^2 + 3x + 1)\right\} dx \\
  &= \int (-6x^2 - 2)\,dx \\
  &= -6 \cdot \frac{x^3}{3} - 2x + C \\
  &= -2x^3 - 2x + C \quad (C \text{ は積分定数})
  \end{aligned}$$
  > 💡 讲师批注：不要分别积分 $\frac{1}{4}(x-1)^4 - \frac{1}{4}(x+1)^4$ 再展开！先利用线性性质合并被积函数，奇次项 $x^3$ 与 $3x$ 瞬间抵消，计算量减半！反向求导验算：$(-2x^3 - 2x)' = -6x^2 - 2$，无误！

  **[2]** 積分変数は $x$ であり、$t$ は定数として扱う。展開してから項別に積分する：
  $$\begin{aligned}
  \int (t - x)(2t + x)\,dx &= \int (2t^2 - tx - x^2)\,dx \\
  &= 2t^2 x - t \cdot \frac{x^2}{2} - \frac{x^3}{3} + C \\
  &= -\frac{1}{3}x^3 - \frac{1}{2}tx^2 + 2t^2 x + C \quad (C \text{ は積分定数})
  \end{aligned}$$
  > 💡 讲师批注：**经典陷阱题！** 一定要看清末尾的 **$dx$**——$x$ 才是积分变量，$t$ 只是普通常数（所以 $\int 2t^2\,dx = 2t^2 x$，千万别积成 $\frac{2}{3}t^3$！）。反向对 $x$ 求导得 $-x^2 - tx + 2t^2 = (t-x)(2t+x)$，无误！
- **【最终答案】**
  **[1] $-2x^3 - 2x + C$（$C$ 为积分常数）**
  **[2] $-\dfrac{1}{3}x^3 - \dfrac{1}{2}tx^2 + 2t^2 x + C$（$C$ 为积分常数）**

---

#### 演習問題 13-(2)
- **【原题重现与翻译】**
  - 原题：次の不定積分を求めよ。
    [1] $\displaystyle\int \frac{(\sqrt{x} - 2)^2}{\sqrt{x}}\,dx$
    [2] $\displaystyle\int \frac{x - \cos^2 x}{x\cos^2 x}\,dx$
  - 中文：求下列不定积分。
    [1] $\displaystyle\int \frac{(\sqrt{x} - 2)^2}{\sqrt{x}}\,dx$
    [2] $\displaystyle\int \frac{x - \cos^2 x}{x\cos^2 x}\,dx$
- **【考点定位】**
  - 单项分母拆项法（化为幂函数 $x^\alpha$ 与基本公式之和）。
- **【分步标准解答】**
  **[1]** 分子を展開し、分母の $\sqrt{x} = x^{\frac{1}{2}}$ で各項を割ってべき乗の和にする：
  $$\begin{aligned}
  \int \frac{(\sqrt{x} - 2)^2}{\sqrt{x}}\,dx &= \int \frac{x - 4\sqrt{x} + 4}{\sqrt{x}}\,dx \\
  &= \int \left(x^{\frac{1}{2}} - 4 + 4x^{-\frac{1}{2}}\right) dx \\
  &= \frac{x^{\frac{3}{2}}}{\frac{3}{2}} - 4x + 4 \cdot \frac{x^{\frac{1}{2}}}{\frac{1}{2}} + C \\
  &= \frac{2}{3}x\sqrt{x} - 4x + 8\sqrt{x} + C \quad (C \text{ は積分定数})
  \end{aligned}$$
  > 💡 讲师批注：把根式改写为分数指数 $x^{\frac{1}{2}}, x^{-\frac{1}{2}}$ 套用 $\int x^\alpha\,dx = \frac{x^{\alpha+1}}{\alpha+1} + C$ 最不容易出错；最后结果再写回根号形式 $x\sqrt{x},\; \sqrt{x}$ 更美观。反向求导验算：$\sqrt{x} - 4 + \frac{4}{\sqrt{x}} = \frac{x - 4\sqrt{x} + 4}{\sqrt{x}}$，完全正确！

  **[2]** 分子の引き算ごとに分数を 2 つに分解する：
  $$\begin{aligned}
  \int \frac{x - \cos^2 x}{x\cos^2 x}\,dx &= \int \left(\frac{x}{x\cos^2 x} - \frac{\cos^2 x}{x\cos^2 x}\right) dx \\
  &= \int \left(\frac{1}{\cos^2 x} - \frac{1}{x}\right) dx \\
  &= \tan x - \log|x| + C \quad (C \text{ は積分定数})
  \end{aligned}$$
  > 💡 讲师批注：拆项后立刻变为两个最基本公式！务必记得 $\int \frac{1}{x}\,dx = \log|x| + C$ 带有**绝对值符号**。反向求导验算：$\frac{1}{\cos^2 x} - \frac{1}{x} = \frac{x - \cos^2 x}{x\cos^2 x}$，完全正确！
- **【最终答案】**
  **[1] $\dfrac{2}{3}x\sqrt{x} - 4x + 8\sqrt{x} + C$（$C$ 为积分常数）**
  **[2] $\tan x - \log|x| + C$（$C$ 为积分常数）**

---

#### 演習問題 13-(3)
- **【原题重现与翻译】**
  - 原题：次の不定積分を求めよ。
    [1] $\displaystyle\int \frac{1}{\tan^2 x}\,dx$
    [2] $\displaystyle\int (2e^t - 3 \cdot 2^t)\,dt$（原书误印为 $dx$，见下方勘误）
  - 中文：求下列不定积分。
    [1] $\displaystyle\int \frac{1}{\tan^2 x}\,dx$
    [2] $\displaystyle\int (2e^t - 3 \cdot 2^t)\,dt$
  > ⚠️ **教材勘误提示**：原教材第 359 页（`page_0360.jpg`）将 [2] 印作 $\int (2e^t - 3 \cdot 2^t)\,dx$（被积函数变量为 $t$，微分符号却印成了 $dx$）。若按字面 $dx$ 计算则结果为 $(2e^t - 3\cdot 2^t)x + C$，显然违背本题考察指数函数积分的命题意图；此处按正确题意 $dt$（或变量全为 $x$）给出标准解答。
- **【考点定位】**
  - 三角恒等式 $1 + \dfrac{1}{\tan^2 x} = \dfrac{1}{\sin^2 x}$ 变形积分；指数函数 $e^t$ 与 $a^t$ 的基本积分公式。
- **【分步标准解答】**
  **[1]** 三角関数の相互関係 $1 + \dfrac{1}{\tan^2 x} = \dfrac{1}{\sin^2 x}$ より、$\dfrac{1}{\tan^2 x} = \dfrac{1}{\sin^2 x} - 1$ と変形する：
  $$\begin{aligned}
  \int \frac{1}{\tan^2 x}\,dx &= \int \left(\frac{1}{\sin^2 x} - 1\right) dx \\
  &= -\frac{1}{\tan x} - x + C \quad (C \text{ は積分定数})
  \end{aligned}$$
  > 💡 讲师批注：与 $\int \tan^2 x\,dx = \int \left(\frac{1}{\cos^2 x} - 1\right)dx = \tan x - x + C$ 是一对**黄金姐妹题**！牢记把 $\tan^2 x$ 换成 $\frac{1}{\cos^2 x} - 1$、把 $\frac{1}{\tan^2 x}$ 换成 $\frac{1}{\sin^2 x} - 1$。反向求导验算：$\left(-\frac{1}{\tan x} - x\right)' = \frac{1}{\sin^2 x} - 1 = \frac{1 - \sin^2 x}{\sin^2 x} = \frac{\cos^2 x}{\sin^2 x} = \frac{1}{\tan^2 x}$，完全正确！

  **[2]** 指数関数の不定積分公式 $\int e^t\,dt = e^t + C$、$\int a^t\,dt = \dfrac{a^t}{\log a} + C$ を用いる：
  $$\begin{aligned}
  \int (2e^t - 3 \cdot 2^t)\,dt &= 2\int e^t\,dt - 3\int 2^t\,dt \\
  &= 2e^t - 3 \cdot \frac{2^t}{\log 2} + C \\
  &= 2e^t - \frac{3 \cdot 2^t}{\log 2} + C \quad (C \text{ は積分定数})
  \end{aligned}$$
  > 💡 讲师批注：区分求导与积分时 $\log a$ 的位置——求导是**乘以** $\log a$（$(2^t)' = 2^t \log 2$），积分是**除以** $\log a$（$\int 2^t\,dt = \frac{2^t}{\log 2} + C$）！
- **【最终答案】**
  **[1] $-\dfrac{1}{\tan x} - x + C$（$C$ 为积分常数）**
  **[2] $2e^t - \dfrac{3 \cdot 2^t}{\log 2} + C$（$C$ 为积分常数，按 $dt$ 修正）**

---

#### 演習問題 13-(4)
- **【原题重现与翻译】**
  - 原题：次の不定積分を求めよ。
    [1] $\displaystyle\int \sqrt{2x - 3}\,dx$
    [2] $\displaystyle\int \cos\left(\frac{2}{3}x - 1\right)\,dx$
    [3] $\displaystyle\int \frac{1}{4x + 5}\,dx$（原书印作 $\int \frac{dx}{4x+5}\,dx$，重复多印了一个 $dx$）
    [4] $\displaystyle\int 2^{-3x + 1}\,dx$
  - 中文：求下列不定积分。
    [1] $\displaystyle\int \sqrt{2x - 3}\,dx$
    [2] $\displaystyle\int \cos\left(\frac{2}{3}x - 1\right)\,dx$
    [3] $\displaystyle\int \frac{1}{4x + 5}\,dx$
    [4] $\displaystyle\int 2^{-3x + 1}\,dx$
  > ⚠️ **教材勘误提示**：原教材第 359 页（`page_0360.jpg`）[3] 题印作 $\int \dfrac{dx}{4x + 5}\,dx$，重复印了两次 $dx$，正确应为 $\int \dfrac{1}{4x + 5}\,dx$ 或 $\int \dfrac{dx}{4x + 5}$。
- **【考点定位】**
  - 公式 [14.4]「一次复合型 $\displaystyle\int f(ax + b)\,dx = \frac{1}{a}F(ax + b) + C$」的专项熟练度训练。
- **【分步标准解答】**
  **[1]** $\sqrt{2x - 3} = (2x - 3)^{\frac{1}{2}}$ であり、一次の係数 $a = 2$ より：
  $$\begin{aligned}
  \int \sqrt{2x - 3}\,dx &= \int (2x - 3)^{\frac{1}{2}}\,dx \\
  &= \frac{1}{2} \cdot \frac{(2x - 3)^{\frac{3}{2}}}{\frac{3}{2}} + C \\
  &= \frac{1}{3}(2x - 3)\sqrt{2x - 3} + C \quad (C \text{ は積分定数})
  \end{aligned}$$
  > 💡 讲师批注：$\frac{1}{2} \cdot \frac{2}{3} = \frac{1}{3}$。反向求导验算：$\frac{1}{3}\cdot\frac{3}{2}(2x-3)^{\frac{1}{2}}\cdot 2 = \sqrt{2x-3}$，完全正确！

  **[2]** 一次の係数 $a = \dfrac{2}{3}$ より、$\dfrac{1}{a} = \dfrac{3}{2}$：
  $$\begin{aligned}
  \int \cos\left(\frac{2}{3}x - 1\right)\,dx &= \frac{1}{\frac{2}{3}}\sin\left(\frac{2}{3}x - 1\right) + C \\
  &= \frac{3}{2}\sin\left(\frac{2}{3}x - 1\right) + C \quad (C \text{ は積分定数})
  \end{aligned}$$
  > 💡 讲师批注：$\cos$ 积分是 $+\sin$（不是 $-\sin$！）。反向求导验算：$\frac{3}{2}\cdot\frac{2}{3}\cos\left(\frac{2}{3}x-1\right) = \cos\left(\frac{2}{3}x-1\right)$，完全正确！

  **[3]** 一次の係数 $a = 4$ より：
  $$\int \frac{1}{4x + 5}\,dx = \frac{1}{4}\log|4x + 5| + C \quad (C \text{ は積分定数})$$
  > 💡 讲师批注：千万别漏掉分母 $4$ 和绝对值 $|4x+5|$！反向求导验算：$\frac{1}{4}\cdot\frac{4}{4x+5} = \frac{1}{4x+5}$，完全正确！

  **[4]** 一次の係数 $a = -3$ より：
  $$\begin{aligned}
  \int 2^{-3x + 1}\,dx &= \frac{1}{-3} \cdot \frac{2^{-3x + 1}}{\log 2} + C \\
  &= -\frac{2^{-3x + 1}}{3\log 2} + C \quad (C \text{ は積分定数})
  \end{aligned}$$
  > 💡 讲师批注：也可先拆成 $2\cdot (2^{-3})^x = 2\cdot \left(\frac{1}{8}\right)^x$，积分得 $2\cdot\frac{(1/8)^x}{\log(1/8)} + C = \frac{2^{-3x+1}}{-3\log 2} + C$，结果完全一致！反向求导验算：$-\frac{1}{3\log 2}\cdot 2^{-3x+1}(\log 2)(-3) = 2^{-3x+1}$，无误！
- **【最终答案】**
  **[1] $\dfrac{1}{3}(2x - 3)\sqrt{2x - 3} + C$**
  **[2] $\dfrac{3}{2}\sin\left(\dfrac{2}{3}x - 1\right) + C$**
  **[3] $\dfrac{1}{4}\log|4x + 5| + C$**
  **[4] $-\dfrac{2^{-3x + 1}}{3\log 2} + C$**
  **（以上 $C$ 均为积分常数）**
