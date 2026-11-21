# 《EJU 教材全解与备课讲义》数学 026（P376–P390，上篇）

> **对应源文件**：`work_math/ocr_md/ocr_026_p376-390.md`（第七章《微分積分》之「定積分とその基本性質（[16.3]–[16.7]解説・演習問題14）」「定積分で表された関数（[17.1]–[17.2]・演習問題15）」「定積分と和の極限、不等式（[18.1]–[18.2]）」）
> **视觉核对参考图**：`work_math/ref_imgs/page_0376.jpg` – `page_0390.jpg`（全 15 页逐符号视觉核对）
> **分篇说明**：本切片含 38 道独立习题与三大核心知识板块，为保证每步推导完整不省略，拆分为 `note_026_a.md`（知识点总览、词汇注音、演習問題 14 全解）与 `note_026_b.md`（演習問題 15 全解、区分求积法例题详解）。

---

## 一、国内高中基础知识点唤醒与 EJU 考纲差异对比

本切片是 **数学Ⅲ（積分法）** 与 **数学Ⅱ（積分法）** 的核心计算与应用枢纽，涵盖 **定积分的计算技巧与渐化式**、**用定积分表示的函数（积分方程与变限积分求导）**、**区分求积法（黎曼和极限）与定积分不等式** 三大模块。

### 1.1 定积分的核心计算法则与递推（[16.3]–[16.7]）

1. **含绝对值函数的定积分（絶対値のついた関数の定積分）**：
   - 核心原则：**先找零点，分段去绝对值**，再利用区间可加性 $\int_a^b = \int_a^c + \int_c^b$ 分段积分。
2. **定积分的换元积分法（定積分の置換積分法）**：
   - 设 $x = g(t)$，当 $x: a \to b$ 时 $t: \alpha \to \beta$，则：
     $$\int_a^b f(x)\,dx = \int_\alpha^\beta f(g(t))\,g'(t)\,dt$$
   - **铁律**：换元后**必须同步更换积分上下限**，且不需要再回代原变量 $x$。
   - **EJU 两大高频三角换元**：
     - 含 $\sqrt{a^2 - x^2}$（$a>0$）$\implies$ 令 $x = a\sin\theta$（$-\dfrac{\pi}{2} \le \theta \le \dfrac{\pi}{2}$）。
     - 含 $\dfrac{1}{x^2 + a^2}$（$a>0$）$\implies$ 令 $x = a\tan\theta$（$-\dfrac{\pi}{2} < \theta < \dfrac{\pi}{2}$）。
3. **偶函数与奇函数在对称区间 $[-a, a]$ 上的积分**：
   - 偶函数（$f(-x) = f(x)$，$y$ 轴对称）：$\displaystyle \int_{-a}^a f(x)\,dx = 2\int_0^a f(x)\,dx$。
   - 奇函数（$f(-x) = -f(x)$，原点对称）：$\displaystyle \int_{-a}^a f(x)\,dx = 0$。
4. **定积分的分部积分法（定積分の部分積分法）**：
   $$\int_a^b f(x)g'(x)\,dx = \Bigl[f(x)g(x)\Bigr]_a^b - \int_a^b f'(x)g(x)\,dx$$
   - 特例（$g(x)=x$）：$\displaystyle \int_a^b f(x)\,dx = \Bigl[x f(x)\Bigr]_a^b - \int_a^b x f'(x)\,dx$（常用于 $\log x$ 等函数的积分）。
5. **定积分与渐化式（定積分と漸化式）**：
   - 例 1：$I_n = \displaystyle\int_0^1 x^n e^{-x}\,dx$（$n \ge 0$）满足 $I_n = n I_{n-1} - \dfrac{1}{e}$（$n \ge 1$），结合 $I_0 = 1 - \dfrac{1}{e}$ 可逐项递推。
   - 例 2：$I_{m,n} = \displaystyle\int_0^1 x^m(1-x)^n\,dx$（$m, n \ge 0$）满足 $I_{m,n} = \dfrac{n}{m+1}I_{m+1, n-1}$，递推可得著名结论：
     $$I_{m,n} = \frac{m!\,n!}{(m+n+1)!}$$
   - 拓展：二元函数 $B(p, q) = \displaystyle\int_0^1 x^{p-1}(1-x)^{q-1}\,dx$（$p>0, q>0$）称为**贝塔函数（ベータ関数）**。
6. **1/6 公式（$\dfrac{1}{6}$ 公式）**：
   $$\int_\alpha^\beta (x-\alpha)(x-\beta)\,dx = -\frac{1}{6}(\beta-\alpha)^3$$
   - EJU 速度提分利器，求抛物线与直线围成的面积时可一步出答案。

### 1.2 用定积分表示的函数（[17.1]–[17.2]）

设 $a, b$ 为常数，$x$ 为与积分变量 $t$ 无关的变量：
1. **定积分常量型（积分上下限均为常数）**：
   - $\displaystyle \int_a^b f(t)\,dt$ 是一个**与 $t$ 无关的常数**。
   - 解题通法（**积分方程常量替换法**）：令 $A = \displaystyle\int_a^b f(t)\,dt$，代入原方程得 $f(x)$ 的显式表达式，再代回 $A$ 的定义式解出常数 $A$。
2. **变限积分求导公式（微积分基本定理推论）**：
   - 上限为 $x$：$\displaystyle \frac{d}{dx}\int_a^x f(t)\,dt = f(x)$
   - 上下限均为 $x$ 的函数（结合链式法则）：
     $$\frac{d}{dx}\int_{h(x)}^{g(x)} f(t)\,dt = f(g(x))\,g'(x) - f(h(x))\,h'(x)$$
   - **易错铁律**：若被积函数同时含有 $x$ 与 $t$（如 $\int_a^x (x-t)f(t)\,dt$），**必须先把 $x$ 提到积分号外面**，再对 $x$ 使用乘法求导法则！同时别忘了令 $x = a$ 利用 $\int_a^a = 0$ 确定未知常数 $a$。

### 1.3 区分求积法与定积分不等式（[18.1]–[18.2]）

1. **区分求积法（定積分と和の極限）**：
   - 设 $f(x)$ 在闭区间 $[a, b]$ 上连续，将 $[a, b]$ $n$ 等分，$\Delta x = \dfrac{b-a}{n}$，$x_k = a + k\Delta x$，则：
     $$\int_a^b f(x)\,dx = \lim_{n\to\infty}\sum_{k=0}^{n-1} f(x_k)\Delta x = \lim_{n\to\infty}\sum_{k=1}^n f(x_k)\Delta x$$
   - **最常用标准形（$a=0, b=1$）**：
     $$\int_0^1 f(x)\,dx = \lim_{n\to\infty}\frac{1}{n}\sum_{k=0}^{n-1} f\!\left(\frac{k}{n}\right) = \lim_{n\to\infty}\frac{1}{n}\sum_{k=1}^n f\!\left(\frac{k}{n}\right)$$
2. **定积分不等式（定積分と不等式）**：
   - 在闭区间 $[a, b]$（$a < b$）上，若连续函数满足 $f(x) \ge 0$，则 $\displaystyle\int_a^b f(x)\,dx \ge 0$（等号当且仅当在 $[a, b]$ 上恒有 $f(x) = 0$ 时成立）。
   - 若 $f(x) \ge g(x)$，则 $\displaystyle\int_a^b f(x)\,dx \ge \int_a^b g(x)\,dx$（等号当且仅当恒有 $f(x)=g(x)$ 时成立）。

### 1.4 国内高中 vs. 日本 EJU 考纲差异与符号习惯

| 对比维度 | 国内高中习惯 | 日本 EJU 习惯 | 备课/应试提醒 |
| :--- | :--- | :--- | :--- |
| **自然对数记号** | $\ln x$ | $\log x$（省略底数 $e$） | EJU 中出现 $\log x$ 一律默认以 $e$ 为底，切勿误当常用对数 $\log_{10} x$ |
| **变限积分与积分方程** | 高考基本不考，属于大学高数内容 | **EJU 数学Ⅱ・Ⅲ 绝对核心必考点** | 必须熟练掌握「设常数 $A$」与「两边求导 + 令上下限相等」两大模板 |
| **三角换元积分** | 大学高数内容，高中不考 | **数学Ⅲ 必考计算题** | 牢记 $\sqrt{a^2-x^2} \to a\sin\theta$ 与 $\dfrac{1}{x^2+a^2} \to a\tan\theta$，并习惯画对应表 |
| **区分求积法** | 仅作定积分概念引入，不考计算 | **数学Ⅲ 高频压轴题型** | 务必练熟将 $\sum$ 中的 $\dfrac{1}{n}$ 变为 $dx$、$\dfrac{k}{n}$ 变为 $x$ 的机械转化 |
| **1/6 公式** | 竞赛或拓展技巧 | 日本高中生人手必备的**标准解题公式** | 填空题可直接秒杀，解答题建议视分值快速推导或直接引用 |
| **换元对应表** | 一般用文字写「当 $x=a$ 时 $t=\alpha$」 | 习惯画两行对应表 $\begin{array}{c\|c} x & a \to b \\ \hline t & \alpha \to \beta \end{array}$ | 清晰不易写反上下限，强烈推荐考场使用 |

---

## 二、日文核心词汇与公式假名注音

### 2.1 本切片日文核心词汇

- ベータ関数（べーたかんすう / beeta kansuu） — 贝塔函数（Beta 函数）
- 2変数関数（にへんすうかんすう / nihensuu kansuu） — 二元函数（二变量函数）
- 1/6公式（ろくぶんのいちこうしき / rokubun no ichi koushiki） — 1/6 公式
- 広義積分（こうぎせきぶん / kougi sekibun） — 广义积分（反常积分、瑕积分）
- 定積分で表された関数（ていせきぶんであらわされたかんすう / tei sekibun de arawasareta kansuu） — 用定积分表示的函数（含参/变限积分函数）
- 積分方程式（せきぶんほうていしき / sekibun houteishiki） — 积分方程
- 区分求積法（くぶんきゅうせきほう / kubun kyuusekihou） — 区分求积法
- 等分（とうぶん / toubun） — 等分（如 $n$ 等分 = エヌとうぶん）
- 積分値（せきぶんち / sekibunchi） — 积分值
- 無関係（むかんけい / mukankei） — 无关（如 $t$ に無関係 = 与 $t$ 无关）

*(注：定積分、置換積分法、部分積分法、偶関数、奇関数、漸化式、逆関数、閉区間、分点 等高频词已收录于总表 `glossary_all.md`。)*

### 2.2 核心公式的日本课堂口语读法

1. **变限积分求导公式** $\displaystyle\frac{d}{dx}\int_a^x f(t)\,dt = f(x)$
   - 课堂读法：**ディー ディーエックス、インテグラル エーから エックスまでの エフティー ディーティー イコール エフエックス**
   - 备注：$\dfrac{d}{dx}$ 读作「ディー・ディーエックス」或「エックスで びぶんする」。
2. **1/6 公式** $\displaystyle\int_\alpha^\beta (x-\alpha)(x-\beta)\,dx = -\frac{1}{6}(\beta-\alpha)^3$
   - 课堂读法：**インテグラル アルファから ベータまでの かっこ エックス ひく アルファ かっことじ かっこ エックス ひく ベータ かっことじ ディーエックス イコール マイナス ろくぶんのいち かっこ ベータ ひく アルファ かっことじ の さんじょう**
3. **区分求积法标准形** $\displaystyle\lim_{n\to\infty}\frac{1}{n}\sum_{k=1}^n f\!\left(\frac{k}{n}\right) = \int_0^1 f(x)\,dx$
   - 课堂读法：**リミット エヌが むげんだいに ちかづくときの エヌぶんのいち、シグマ ケー イコール いちから エヌまでの エフ かっこ エヌぶんのケー かっことじ イコール インテグラル ゼロから いちまでの エフエックス ディーエックス**

---

## 三、逐题深度解析（不可跳步）— 上篇：演習問題 14

---

### 演習問題 14-(1)

#### 演習問題 14-(1) [1]
- **【原题重现与翻译】**
  - 原题：次の定積分を求めよ。$\displaystyle\int_0^2 (3t - 1)(t + 1)\,dx$（※ 教材原印为 $dx$）
  - 中文：求定积分 $\displaystyle\int_0^2 (3t - 1)(t + 1)\,dt$。
  > ⚠️ **教材勘误提示**：原教材第 376 页（`page_0377.jpg`）将积分微元误印为 $dx$，结合被积函数变量 $t$，显然应修正为 $dt$。以下按修正后的 $dt$ 给出解答。
- **【考点定位】**
  - 多项式展开与基本幂函数定积分。
- **【分步标准解答】**
  $$\int_0^2 (3t - 1)(t + 1)\,dt = \int_0^2 (3t^2 + 2t - 1)\,dt$$
  > 💡 讲师批注：先将乘积展开为多项式，再逐项积分。

  $$= \Bigl[t^3 + t^2 - t\Bigr]_0^2$$
  > 💡 讲师批注：$\int 3t^2\,dt = t^3$，$\int 2t\,dt = t^2$，$\int (-1)\,dt = -t$；微分回代检查：$3t^2+2t-1$ 无误。

  $$= (2^3 + 2^2 - 2) - 0 = 8 + 4 - 2 = 10$$
- **【最终答案】**
  **$10$**

---

#### 演習問題 14-(1) [2]
- **【原题重现与翻译】**
  - 原题：次の定積分を求めよ。$\displaystyle\int_0^1 (3x - 1)^4\,dx$
  - 中文：求定积分 $\displaystyle\int_0^1 (3x - 1)^4\,dx$。
- **【考点定位】**
  - 一次线性复合函数 $(ax+b)^n$ 的直接积分公式：$\displaystyle\int (ax+b)^n\,dx = \frac{1}{a(n+1)}(ax+b)^{n+1} + C$。
- **【分步标准解答】**
  $$\int_0^1 (3x - 1)^4\,dx = \left[\frac{1}{3} \cdot \frac{1}{5}(3x - 1)^5\right]_0^1 = \frac{1}{15}\Bigl[(3x - 1)^5\Bigr]_0^1$$
  > 💡 讲师批注：切忌展开成 5 项硬算！直接把 $(3x-1)$ 看成整体积分，**千万不要漏掉内层导数的倒数 $\dfrac{1}{3}$**。

  $$= \frac{1}{15}\bigl\{(3\cdot 1 - 1)^5 - (3\cdot 0 - 1)^5\bigr\} = \frac{1}{15}\bigl\{2^5 - (-1)^5\bigr\}$$
  $$= \frac{1}{15}\bigl(32 - (-1)\bigr) = \frac{33}{15} = \frac{11}{5}$$
  > 💡 讲师批注：注意下限 $x=0$ 代入后 $(-1)^5 = -1$，减去 $-1$ 变成 $+1$，避免符号失误。
- **【最终答案】**
  **$\dfrac{11}{5}$**

---

### 演習問題 14-(2)
- **【原题重现与翻译】**
  - 原题：等式 $\displaystyle\int_\alpha^\beta (x - \alpha)(x - \beta)\,dx = -\frac{1}{6}(\beta - \alpha)^3$ を証明せよ。
  - 中文：证明等式 $\displaystyle\int_\alpha^\beta (x - \alpha)(x - \beta)\,dx = -\frac{1}{6}(\beta - \alpha)^3$。
- **【考点定位】**
  - **1/6 公式**的恒等变形与标准证明。
- **【图解辅助（SVG 矢量图）】**
  当 $\alpha < \beta$ 时，抛物线 $y=(x-\alpha)(x-\beta)$ 在区间 $(\alpha, \beta)$ 位于 $x$ 轴下方，定积分的值等于其围成面积的相反数 $-\dfrac{1}{6}(\beta-\alpha)^3$：

<svg viewBox="0 0 460 220" width="460" height="220" xmlns="http://www.w3.org/2000/svg" style="background:#fafafa;border:1px solid #e0e0e0;border-radius:6px;">
  <style>
    .axis { stroke: #333; stroke-width: 1.5; }
    .curve { fill: none; stroke: #2980b9; stroke-width: 2.2; }
    .area { fill: rgba(231, 76, 60, 0.18); stroke: none; }
    .lbl { font: 13px sans-serif; fill: #2c3e50; }
    .math { font: italic 14px serif; fill: #2c3e50; }
    .note { font: bold 13px sans-serif; fill: #c0392b; text-anchor: middle; }
  </style>
  <!-- Axes -->
  <line x1="30" y1="80" x2="430" y2="80" class="axis"/>
  <polygon points="430,80 422,76 422,84" fill="#333"/>
  <text x="435" y="84" class="math">x</text>
  <line x1="70" y1="200" x2="70" y2="20" class="axis"/>
  <polygon points="70,20 66,28 74,28" fill="#333"/>
  <text x="54" y="26" class="math">y</text>
  <text x="56" y="96" class="lbl">O</text>
  <!-- Shaded area under x-axis between x=130 (alpha) and x=330 (beta) -->
  <!-- Parabola: y_math = (x-130)(x-330)/125 => at x=230, y_math = -80 => y_svg = 80 + 80 = 160 -->
  <path d="M 130 80 Q 230 240 330 80 Z" class="area"/>
  <!-- Parabola curve -->
  <path d="M 95 29 Q 230 291 365 29" class="curve"/>
  <!-- Intercept dots -->
  <circle cx="130" cy="80" r="3.5" fill="#c0392b"/>
  <circle cx="330" cy="80" r="3.5" fill="#c0392b"/>
  <text x="122" y="70" class="math">α</text>
  <text x="334" y="70" class="math">β</text>
  <!-- Annotations -->
  <text x="330" y="34" class="math">y = (x - α)(x - β)</text>
  <text x="230" y="130" class="note">定積分 = -1/6 (β - α)³</text>
  <text x="230" y="150" class="lbl" text-anchor="middle" fill="#7f8c8d">(x軸より下側なので負)</text>
</svg>

- **【分步标准解答】**
  $$(x - \alpha)(x - \beta) = (x - \alpha)\bigl\{(x - \alpha) - (\beta - \alpha)\bigr\} = (x - \alpha)^2 - (\beta - \alpha)(x - \alpha)$$
  > 💡 讲师批注：这是证明 1/6 公式**最优雅的技巧**！将 $x-\beta$ 改写为 $(x-\alpha)-(\beta-\alpha)$，这样积分后下限 $x=\alpha$ 代入时**所有项同时归零**，避免繁琐的 $\beta^3-\alpha^3$ 因式分解。

  したがって，
  $$\int_\alpha^\beta (x - \alpha)(x - \beta)\,dx = \int_\alpha^\beta \bigl\{(x - \alpha)^2 - (\beta - \alpha)(x - \alpha)\bigr\}\,dx$$
  $$= \left[\frac{1}{3}(x - \alpha)^3 - \frac{1}{2}(\beta - \alpha)(x - \alpha)^2\right]_\alpha^\beta$$
  > 💡 讲师批注：注意 $(\beta-\alpha)$ 对积分变量 $x$ 而言是常数，直接保留在前面。

  $$= \left\{\frac{1}{3}(\beta - \alpha)^3 - \frac{1}{2}(\beta - \alpha)^3\right\} - 0$$
  $$= \left(\frac{1}{3} - \frac{1}{2}\right)(\beta - \alpha)^3 = -\frac{1}{6}(\beta - \alpha)^3 \quad \text{（証明終わり）}$$
- **【最终答案】**
  **証明完了（如上所示）**

---

### 演習問題 14-(3)

#### 演習問題 14-(3) [1]
- **【原题重现与翻译】**
  - 原题：次の定積分を求めよ。$\displaystyle\int_2^3 (x - 2)(x - 3)\,dx$
  - 中文：求定积分 $\displaystyle\int_2^3 (x - 2)(x - 3)\,dx$。
- **【考点定位】**
  - 1/6 公式的直接应用。
- **【分步标准解答】**
  (2) の公式 $\displaystyle\int_\alpha^\beta (x-\alpha)(x-\beta)\,dx = -\frac{1}{6}(\beta-\alpha)^3$ に $\alpha = 2,\; \beta = 3$ を代入すると，
  $$\int_2^3 (x - 2)(x - 3)\,dx = -\frac{1}{6}(3 - 2)^3 = -\frac{1}{6}$$
  > 💡 讲师批注：直接验算展开法：$\int_2^3 (x^2-5x+6)\,dx = \left[\frac{x^3}{3}-\frac{5}{2}x^2+6x\right]_2^3 = (9-\frac{45}{2}+18)-(\frac{8}{3}-10+12) = \frac{9}{2}-\frac{14}{3} = -\frac{1}{6}$，完全一致。
- **【最终答案】**
  **$-\dfrac{1}{6}$**

---

#### 演習問題 14-(3) [2]
- **【原题重现与翻译】**
  - 原题：次の定積分を求めよ。$\displaystyle\int_{1-\sqrt{2}}^{1+\sqrt{2}} (x^2 - 2x - 1)\,dx$
  - 中文：求定积分 $\displaystyle\int_{1-\sqrt{2}}^{1+\sqrt{2}} (x^2 - 2x - 1)\,dx$。
- **【考点定位】**
  - 识别积分上下限为被积二次式的两根，套用 1/6 公式。
- **【分步标准解答】**
  2 次方程式 $x^2 - 2x - 1 = 0$ を解くと，
  $$x = 1 \pm \sqrt{1 - (-1)} = 1 \pm \sqrt{2}$$
  > 💡 讲师批注：看到上下限出现无理数 $1-\sqrt{2}$ 与 $1+\sqrt{2}$ 时，**千万不要硬算三次方**！先检查它们是不是被积函数等于 0 的两个根。

  よって，$x^2 - 2x - 1 = \bigl\{x - (1 - \sqrt{2})\bigr\}\bigl\{x - (1 + \sqrt{2})\bigr\}$ であるから，1/6 公式より，
  $$\int_{1-\sqrt{2}}^{1+\sqrt{2}} (x^2 - 2x - 1)\,dx = -\frac{1}{6}\Bigl\{(1 + \sqrt{2}) - (1 - \sqrt{2})\Bigr\}^3$$
  $$= -\frac{1}{6}(2\sqrt{2})^3 = -\frac{1}{6} \cdot 16\sqrt{2} = -\frac{8\sqrt{2}}{3}$$
  > 💡 讲师批注：$(2\sqrt{2})^3 = 2^3 \cdot (\sqrt{2})^3 = 8 \cdot 2\sqrt{2} = 16\sqrt{2}$，约分得 $-\dfrac{8\sqrt{2}}{3}$。
- **【最终答案】**
  **$-\dfrac{8\sqrt{2}}{3}$**

---

### 演習問題 14-(4)
- **【原题重现与翻译】**
  - 原题：どんな 2 次関数 $f(x)$ に対しても $\displaystyle\int_\alpha^\beta f(x)\,dx = \frac{1}{2}\{f(\alpha) + f(\beta)\}$ が成り立つ（※ 原印「成り立つする」）ような定数 $\alpha, \beta$（$\alpha < \beta$）の値を求めよ。
  - 中文：求常数 $\alpha, \beta$（$\alpha < \beta$），使得对任意二次函数 $f(x)$，等式 $\displaystyle\int_\alpha^\beta f(x)\,dx = \frac{1}{2}\{f(\alpha) + f(\beta)\}$ 恒成立。
  > ⚠️ **教材勘误提示（重大排版错误）**：
  > 1. 原教材第 378 页（`page_0379.jpg`）题干日文多印一字「成り立つ**す**るような」，应为「成り立つような」。
  > 2. **更关键的数学勘误**：原印刷版积分上下限写作 $\displaystyle\int_\alpha^\beta f(x)\,dx$，经严格推导该方程在 $\alpha < \beta$ 时**无解**（证明见下文「情况 A」）。本题实为日本高中数学经典名题（**两点高斯求积公式**），原题积分上下限应为 **$\displaystyle\int_0^1 f(x)\,dx = \frac{1}{2}\{f(\alpha) + f(\beta)\}$**！以下分别给出原印刷版的无解证明与修正版的完整标准解答。
- **【考点定位】**
  - 多项式恒等式与系数比较法（对任意二次函数恒成立 $\iff$ 对 $a, b, c$ 恒成立）。
- **【分步标准解答】**
  **【情况 A：按教材原印刷版 $\displaystyle\int_\alpha^\beta f(x)\,dx = \frac{1}{2}\{f(\alpha)+f(\beta)\}$ 检验】**
  任意の 2 次関数 $f(x) = ax^2 + bx + c$（$a \neq 0$）に対して成り立つとする。
  - 左辺：$a\dfrac{\beta^3 - \alpha^3}{3} + b\dfrac{\beta^2 - \alpha^2}{2} + c(\beta - \alpha)$
  - 右辺：$a\dfrac{\alpha^2 + \beta^2}{2} + b\dfrac{\alpha + \beta}{2} + c$

  これが任意の $a\neq 0,\; b,\; c$ について恒等的に成り立つためには，各係数が一致しなければならない：
  - $c$ の係数比較：$\beta - \alpha = 1$
  - $a$ の係数比較：$\dfrac{\beta^3 - \alpha^3}{3} = \dfrac{\alpha^2 + \beta^2}{2}$

  $\beta - \alpha = 1$ を第 2 式に代入すると，
  $$\frac{1}{3}(\alpha^2 + \alpha\beta + \beta^2) = \frac{1}{2}(\alpha^2 + \beta^2) \iff 2\alpha^2 + 2\alpha\beta + 2\beta^2 = 3\alpha^2 + 3\beta^2 \iff (\beta - \alpha)^2 = 0$$
  これは $\alpha < \beta$ に矛盾するため，**原印刷版は解なし（無解）**。

  ---

  **【情况 B：修正为正确原题 $\displaystyle\int_0^1 f(x)\,dx = \frac{1}{2}\{f(\alpha) + f(\beta)\}$ 的标准解答】**
  任意の 2 次関数を $f(x) = ax^2 + bx + c$（$a \neq 0$）とおく。
  $$\text{（左辺）} = \int_0^1 (ax^2 + bx + c)\,dx = \left[\frac{a}{3}x^3 + \frac{b}{2}x^2 + cx\right]_0^1 = \frac{1}{3}a + \frac{1}{2}b + c$$
  $$\text{（右辺）} = \frac{1}{2}\bigl\{(a\alpha^2 + b\alpha + c) + (a\beta^2 + b\beta + c)\bigr\} = \frac{\alpha^2 + \beta^2}{2}a + \frac{\alpha + \beta}{2}b + c$$
  > 💡 讲师批注：将左右两边都整理成关于 $a, b, c$ 的线性组合，使之对任意 $a \neq 0$ 和任意实数 $b, c$ 恒成立。

  これらが $a, b, c$ の値によらず常に等しいためには，係数を比較して，
  $$\frac{\alpha^2 + \beta^2}{2} = \frac{1}{3}, \qquad \frac{\alpha + \beta}{2} = \frac{1}{2}$$
  すなわち，
  $$\alpha + \beta = 1 \quad \cdots \text{①}, \qquad \alpha^2 + \beta^2 = \frac{2}{3} \quad \cdots \text{②}$$
  ①，② より，
  $$\alpha\beta = \frac{(\alpha + \beta)^2 - (\alpha^2 + \beta^2)}{2} = \frac{1^2 - \frac{2}{3}}{2} = \frac{1}{6}$$
  > 💡 讲师批注：已知两数和与两数积，直接构造一元二次方程（韦达定理逆用），避免代入消元走弯路。

  よって，$\alpha, \beta$ は 2 次方程式 $t^2 - t + \dfrac{1}{6} = 0$（すなわち $6t^2 - 6t + 1 = 0$）の 2 つの実数解である。
  $$t = \frac{3 \pm \sqrt{9 - 6}}{6} = \frac{3 \pm \sqrt{3}}{6}$$
  $\alpha < \beta$ であるから，
  $$\alpha = \frac{3 - \sqrt{3}}{6}, \qquad \beta = \frac{3 + \sqrt{3}}{6}$$
  > 💡 讲师批注：顺便一提，这两个点不仅对所有 2 次函数精确成立，连所有 **3 次函数**也精确成立（因为 $(t-\frac{1}{2})^3$ 关于 $t=\frac{1}{2}$ 奇对称）！这就是数值分析中大名鼎鼎的 2 点高斯-勒让德求积节点。
- **【最终答案】**
  - **原印刷版**：**解なし（无解）**
  - **修正原题（$\int_0^1$）**：**$\alpha = \dfrac{3 - \sqrt{3}}{6},\quad \beta = \dfrac{3 + \sqrt{3}}{6}$**

---

### 演習問題 14-(5)

#### 演習問題 14-(5) [1]
- **【原题重现与翻译】**
  - 原题：次の定積分を求めよ。$\displaystyle\int_a^{\frac{a}{2}} \sqrt{a^2 - x^2}\,dx$
  - 中文：求定积分 $\displaystyle\int_a^{\frac{a}{2}} \sqrt{a^2 - x^2}\,dx$。
- **【考点定位】**
  - 无理函数 $\sqrt{a^2 - x^2}$ 的三角换元积分法（$x = a\sin\theta$）与参数 $a$ 的正负号讨论。
- **【分步标准解答】**
  $x = a\sin\theta$（$-\dfrac{\pi}{2} \le \theta \le \dfrac{\pi}{2}$）とおくと，$dx = a\cos\theta\,d\theta$ である。
  $x$ と $\theta$ の対応は次のようになる：

  | $x$ | $a \longrightarrow \dfrac{a}{2}$ |
  | :---: | :---: |
  | $\theta$ | $\dfrac{\pi}{2} \longrightarrow \dfrac{\pi}{6}$ |

  > 💡 讲师批注：$\cos\theta \ge 0$ 在 $\left[\frac{\pi}{6}, \frac{\pi}{2}\right]$ 上恒成立，因此 $\sqrt{a^2 - a^2\sin^2\theta} = \sqrt{a^2\cos^2\theta} = |a|\cos\theta$。**原题未注明 $a>0$，最严谨的做法是保留 $|a|$**。

  したがって，
  $$\int_a^{\frac{a}{2}} \sqrt{a^2 - x^2}\,dx = \int_{\frac{\pi}{2}}^{\frac{\pi}{6}} |a|\cos\theta \cdot a\cos\theta\,d\theta = -a|a|\int_{\frac{\pi}{6}}^{\frac{\pi}{2}} \cos^2\theta\,d\theta$$
  半角の公式 $\cos^2\theta = \dfrac{1 + \cos 2\theta}{2}$ を用いると，
  $$= -a|a|\int_{\frac{\pi}{6}}^{\frac{\pi}{2}} \frac{1 + \cos 2\theta}{2}\,d\theta = -\frac{a|a|}{2}\left[\theta + \frac{1}{2}\sin 2\theta\right]_{\frac{\pi}{6}}^{\frac{\pi}{2}}$$
  $$= -\frac{a|a|}{2}\left\{\left(\frac{\pi}{2} + 0\right) - \left(\frac{\pi}{6} + \frac{\sqrt{3}}{4}\right)\right\} = -\frac{a|a|}{2}\left(\frac{\pi}{3} - \frac{\sqrt{3}}{4}\right)$$
  $$= \frac{3\sqrt{3} - 4\pi}{24}a|a|$$
  > 💡 讲师批注：
  > - 若按日本教材惯例默认 $a > 0$，则 $a|a| = a^2$，结果为 $\dfrac{3\sqrt{3}-4\pi}{24}a^2 = -a^2\left(\dfrac{\pi}{6} - \dfrac{\sqrt{3}}{8}\right)$（因为下限 $a >$ 上限 $\frac{a}{2}$ 且被积函数非负，结果必为负！）。
  > - 若 $a < 0$，则 $a|a| = -a^2$，结果为 $\dfrac{4\pi - 3\sqrt{3}}{24}a^2 > 0$；若 $a = 0$，结果为 $0$。
- **【最终答案】**
  **$\dfrac{3\sqrt{3} - 4\pi}{24}a|a|$**（当 $a > 0$ 时为 **$-\left(\dfrac{\pi}{6} - \dfrac{\sqrt{3}}{8}\right)a^2$**）

---

#### 演習問題 14-(5) [2]
- **【原题重现与翻译】**
  - 原题：次の定積分を求めよ。$\displaystyle\int_0^{\sqrt{2}} \frac{dx}{\sqrt{4 - x^2}}$
  - 中文：求定积分 $\displaystyle\int_0^{\sqrt{2}} \frac{dx}{\sqrt{4 - x^2}}$。
- **【考点定位】**
  - $\dfrac{1}{\sqrt{a^2 - x^2}}$ 型三角换元积分（$x = a\sin\theta$）。
- **【分步标准解答】**
  $x = 2\sin\theta$（$-\dfrac{\pi}{2} \le \theta \le \dfrac{\pi}{2}$）とおくと，$dx = 2\cos\theta\,d\theta$。
  $x$ と $\theta$ の対応は次のようになる：

  | $x$ | $0 \longrightarrow \sqrt{2}$ |
  | :---: | :---: |
  | $\theta$ | $0 \longrightarrow \dfrac{\pi}{4}$ |

  区間 $0 \le \theta \le \dfrac{\pi}{4}$ で $\cos\theta > 0$ であるから，$\sqrt{4 - x^2} = 2\cos\theta$。よって，
  $$\int_0^{\sqrt{2}} \frac{dx}{\sqrt{4 - x^2}} = \int_0^{\frac{\pi}{4}} \frac{2\cos\theta}{2\cos\theta}\,d\theta = \int_0^{\frac{\pi}{4}} 1\,d\theta = \Bigl[\theta\Bigr]_0^{\frac{\pi}{4}} = \frac{\pi}{4}$$
  > 💡 讲师批注：熟记反三角导数 $\left(\arcsin\frac{x}{2}\right)' = \frac{1}{\sqrt{4-x^2}}$ 也可瞬间心算验算：$\arcsin\frac{\sqrt{2}}{2} - \arcsin 0 = \frac{\pi}{4}$。
- **【最终答案】**
  **$\dfrac{\pi}{4}$**

---

### 演習問題 14-(6)

#### 演習問題 14-(6) [1]
- **【原题重现与翻译】**
  - 原题：次の定積分を求めよ。$\displaystyle\int_1^{\sqrt{3}} \frac{dx}{x^2 + 3}$
  - 中文：求定积分 $\displaystyle\int_1^{\sqrt{3}} \frac{dx}{x^2 + 3}$。
- **【考点定位】**
  - $\dfrac{1}{x^2 + a^2}$ 型三角换元积分（$x = a\tan\theta$）。
- **【分步标准解答】**
  $x = \sqrt{3}\tan\theta$（$-\dfrac{\pi}{2} < \theta < \dfrac{\pi}{2}$）とおくと，$dx = \dfrac{\sqrt{3}}{\cos^2\theta}\,d\theta$。
  また，$x^2 + 3 = 3(\tan^2\theta + 1) = \dfrac{3}{\cos^2\theta}$。
  $x$ と $\theta$ の対応は次のようになる：

  | $x$ | $1 \longrightarrow \sqrt{3}$ |
  | :---: | :---: |
  | $\theta$ | $\dfrac{\pi}{6} \longrightarrow \dfrac{\pi}{4}$ |

  > 💡 讲师批注：当 $x=1$ 时 $\tan\theta = \frac{1}{\sqrt{3}} \implies \theta = \frac{\pi}{6}$；当 $x=\sqrt{3}$ 时 $\tan\theta = 1 \implies \theta = \frac{\pi}{4}$。

  したがって，
  $$\int_1^{\sqrt{3}} \frac{dx}{x^2 + 3} = \int_{\frac{\pi}{6}}^{\frac{\pi}{4}} \frac{\cos^2\theta}{3} \cdot \frac{\sqrt{3}}{\cos^2\theta}\,d\theta = \frac{\sqrt{3}}{3}\int_{\frac{\pi}{6}}^{\frac{\pi}{4}} d\theta = \frac{\sqrt{3}}{3}\left(\frac{\pi}{4} - \frac{\pi}{6}\right) = \frac{\sqrt{3}}{3} \cdot \frac{\pi}{12} = \frac{\sqrt{3}\pi}{36}$$
- **【最终答案】**
  **$\dfrac{\sqrt{3}\pi}{36}$**

---

#### 演習問題 14-(6) [2]
- **【原题重现与翻译】**
  - 原题：次の定積分を求めよ。$\displaystyle\int_{-1}^1 \frac{dx}{x^2 + 2x + 5}$
  - 中文：求定积分 $\displaystyle\int_{-1}^1 \frac{dx}{x^2 + 2x + 5}$。
- **【考点定位】**
  - 分母配方（平方完成）+ 正切三角换元积分。
- **【分步标准解答】**
  分母を平方完成すると，$x^2 + 2x + 5 = (x + 1)^2 + 4$。
  ここで，$x + 1 = 2\tan\theta$（$-\dfrac{\pi}{2} < \theta < \dfrac{\pi}{2}$）とおくと，$dx = \dfrac{2}{\cos^2\theta}\,d\theta$ であり，
  $$(x + 1)^2 + 4 = 4(\tan^2\theta + 1) = \frac{4}{\cos^2\theta}$$
  $x$ と $\theta$ の対応は次のようになる：

  | $x$ | $-1 \longrightarrow 1$ |
  | :---: | :---: |
  | $\theta$ | $0 \longrightarrow \dfrac{\pi}{4}$ |

  > 💡 讲师批注：遇到分母是判别式 $D < 0$ 的二次三项式，标准动作永远是**先配方成 $(x-p)^2 + q^2$，再令 $x-p = q\tan\theta$**。

  よって，
  $$\int_{-1}^1 \frac{dx}{(x + 1)^2 + 4} = \int_0^{\frac{\pi}{4}} \frac{\cos^2\theta}{4} \cdot \frac{2}{\cos^2\theta}\,d\theta = \frac{1}{2}\int_0^{\frac{\pi}{4}} d\theta = \frac{1}{2} \cdot \frac{\pi}{4} = \frac{\pi}{8}$$
- **【最终答案】**
  **$\dfrac{\pi}{8}$**

---

### 演習問題 14-(7)

#### 演習問題 14-(7) [1]
- **【原题重现与翻译】**
  - 原题：次の定積分を求めよ。$\displaystyle\int_0^{\sqrt{3}} \frac{3 - x}{(x + 1)(x^2 + 1)}\,dx$
  - 中文：求定积分 $\displaystyle\int_0^{\sqrt{3}} \frac{3 - x}{(x + 1)(x^2 + 1)}\,dx$。
- **【考点定位】**
  - 有理函数的部分分式分解（部分分数分解）+ 对数型与 $\arctan$ 型综合积分。
- **【分步标准解答】**
  まず，部分分数分解を行う。
  $$\frac{3 - x}{(x + 1)(x^2 + 1)} = \frac{A}{x + 1} + \frac{Bx + C}{x^2 + 1}$$
  とおいて両辺に $(x+1)(x^2+1)$ を掛けると，
  $$3 - x = A(x^2 + 1) + (Bx + C)(x + 1) = (A + B)x^2 + (B + C)x + (A + C)$$
  > 💡 讲师批注：注意二次不可约因子 $x^2+1$ 对应的分子必须设为**一次式 $Bx+C$**，不可漏掉 $Bx$。

  係数を比較すると，
  $$A + B = 0, \qquad B + C = -1, \qquad A + C = 3$$
  これを解くと（あるいは $x = -1$ を代入して $2A = 4 \implies A = 2$ より），$A = 2,\; B = -2,\; C = 1$ を得る。したがって，
  $$\int_0^{\sqrt{3}} \frac{3 - x}{(x + 1)(x^2 + 1)}\,dx = \int_0^{\sqrt{3}} \left(\frac{2}{x + 1} - \frac{2x}{x^2 + 1} + \frac{1}{x^2 + 1}\right)dx$$
  > 💡 讲师批注：把 $\dfrac{-2x+1}{x^2+1}$ 拆成 $-\dfrac{2x}{x^2+1} + \dfrac{1}{x^2+1}$ 是关键！前者正好是 $-\dfrac{(x^2+1)'}{x^2+1}$，直接积出 $-\log(x^2+1)$；后者用 $x=\tan\theta$。

  前半 2 項の積分は，
  $$\int_0^{\sqrt{3}} \left(\frac{2}{x + 1} - \frac{2x}{x^2 + 1}\right)dx = \Bigl[2\log(x + 1) - \log(x^2 + 1)\Bigr]_0^{\sqrt{3}} = \left[\log\frac{(x + 1)^2}{x^2 + 1}\right]_0^{\sqrt{3}}$$
  $$= \log\frac{(\sqrt{3} + 1)^2}{3 + 1} - \log 1 = \log\frac{4 + 2\sqrt{3}}{4} = \log\frac{2 + \sqrt{3}}{2}$$
  後半の積分は，$x = \tan\theta$（$x: 0 \to \sqrt{3}$ のとき $\theta: 0 \to \dfrac{\pi}{3}$）とおくと，
  $$\int_0^{\sqrt{3}} \frac{1}{x^2 + 1}\,dx = \int_0^{\frac{\pi}{3}} d\theta = \frac{\pi}{3}$$
  以上より，求める定積分は $\log\dfrac{2 + \sqrt{3}}{2} + \dfrac{\pi}{3}$。
- **【最终答案】**
  **$\log\dfrac{2 + \sqrt{3}}{2} + \dfrac{\pi}{3}$**

---

#### 演習問題 14-(7) [2]
- **【原题重现与翻译】**
  - 原题：次の定積分を求めよ。$\displaystyle\int_{-1}^2 x^2\sqrt{2 - x}\,dx$
  - 中文：求定积分 $\displaystyle\int_{-1}^2 x^2\sqrt{2 - x}\,dx$。
- **【考点定位】**
  - 无理根式整体换元法（令 $t = \sqrt{2 - x}$ 去根号）。
- **【分步标准解答】**
  $t = \sqrt{2 - x}$ とおくと，$t^2 = 2 - x$ より $x = 2 - t^2$，両辺を微分して $dx = -2t\,dt$。
  $x$ と $t$ の対応は次のようになる：

  | $x$ | $-1 \longrightarrow 2$ |
  | :---: | :---: |
  | $t$ | $\sqrt{3} \longrightarrow 0$ |

  > 💡 讲师批注：令根号整体等于 $t$，可以把无理积分彻底转化为多项式积分，是最稳妥的做法。

  したがって，
  $$\int_{-1}^2 x^2\sqrt{2 - x}\,dx = \int_{\sqrt{3}}^0 (2 - t^2)^2 \cdot t \cdot (-2t)\,dt$$
  $$= 2\int_0^{\sqrt{3}} (4 - 4t^2 + t^4)t^2\,dt = 2\int_0^{\sqrt{3}} (4t^2 - 4t^4 + t^6)\,dt$$
  $$= 2\left[\frac{4}{3}t^3 - \frac{4}{5}t^5 + \frac{1}{7}t^7\right]_0^{\sqrt{3}}$$
  $$= 2\left(\frac{4}{3}\cdot 3\sqrt{3} - \frac{4}{5}\cdot 9\sqrt{3} + \frac{1}{7}\cdot 27\sqrt{3}\right)$$
  $$= 6\sqrt{3}\left(\frac{4}{3} - \frac{12}{5} + \frac{9}{7}\right) = 6\sqrt{3}\cdot\frac{140 - 252 + 135}{105} = 6\sqrt{3}\cdot\frac{23}{105} = \frac{46\sqrt{3}}{35}$$
  > 💡 讲师批注：提取公因子 $3\sqrt{3}$ 后再通分，可以把分子分母数值压小，大幅降低算错概率。
- **【最终答案】**
  **$\dfrac{46\sqrt{3}}{35}$**

---

### 演習問題 14-(8)

#### 演習問題 14-(8) [1]
- **【原题重现与翻译】**
  - 原题：次の定積分を求めよ。$\displaystyle\int_0^{\frac{\pi}{2}} \frac{\sin x}{1 + \cos x}\,dx$
  - 中文：求定积分 $\displaystyle\int_0^{\frac{\pi}{2}} \frac{\sin x}{1 + \cos x}\,dx$。
- **【考点定位】**
  - $\displaystyle\int \frac{f'(x)}{f(x)}\,dx = \log|f(x)| + C$ 型凑微分积分。
- **【分步标准解答】**
  $(1 + \cos x)' = -\sin x$ であることに着目すると，
  $$\int_0^{\frac{\pi}{2}} \frac{\sin x}{1 + \cos x}\,dx = -\int_0^{\frac{\pi}{2}} \frac{(1 + \cos x)'}{1 + \cos x}\,dx = \Bigl[-\log(1 + \cos x)\Bigr]_0^{\frac{\pi}{2}}$$
  > 💡 讲师批注：在 $[0, \frac{\pi}{2}]$ 上 $1 + \cos x \ge 1 > 0$，绝对值符号可直接省略。也可以令 $t = 1 + \cos x$ 换元，结果完全相同。

  $$= -\log(1 + 0) - \bigl\{-\log(1 + 1)\bigr\} = 0 + \log 2 = \log 2$$
- **【最终答案】**
  **$\log 2$**

---

#### 演習問題 14-(8) [2]
- **【原题重现与翻译】**
  - 原题：次の定積分を求めよ。$\displaystyle\int_{-\frac{\pi}{4}}^{\frac{\pi}{4}} \cos^2 x\,dx$
  - 中文：求定积分 $\displaystyle\int_{-\frac{\pi}{4}}^{\frac{\pi}{4}} \cos^2 x\,dx$。
- **【考点定位】**
  - 偶函数对称性 + 半角公式（降幂公式）。
- **【分步标准解答】**
  $\cos^2 x$ は偶関数であるから，
  $$\int_{-\frac{\pi}{4}}^{\frac{\pi}{4}} \cos^2 x\,dx = 2\int_0^{\frac{\pi}{4}} \cos^2 x\,dx = 2\int_0^{\frac{\pi}{4}} \frac{1 + \cos 2x}{2}\,dx = \int_0^{\frac{\pi}{4}} (1 + \cos 2x)\,dx$$
  > 💡 讲师批注：利用偶函数先将区间减半为 $[0, \frac{\pi}{4}]$，下限变为 $0$，计算极省事！

  $$= \left[x + \frac{1}{2}\sin 2x\right]_0^{\frac{\pi}{4}} = \left(\frac{\pi}{4} + \frac{1}{2}\sin\frac{\pi}{2}\right) - 0 = \frac{\pi}{4} + \frac{1}{2}$$
- **【最终答案】**
  **$\dfrac{\pi}{4} + \dfrac{1}{2}$**

---

### 演習問題 14-(9)

#### 演習問題 14-(9) [1]
- **【原题重现与翻译】**
  - 原题：次の定積分を求めよ。$\displaystyle\int_{-a}^a \frac{x^3}{\sqrt{a^2 + x^2}}\,dx$
  - 中文：求定积分 $\displaystyle\int_{-a}^a \frac{x^3}{\sqrt{a^2 + x^2}}\,dx$。
- **【考点定位】**
  - 奇函数在对称区间 $[-a, a]$ 上的定积分性质。
- **【图解辅助（SVG 矢量图）】**
  对称区间 $[-a, a]$ 上偶函数与奇函数的定积分几何意义对比：

<svg viewBox="0 0 540 190" width="540" height="190" xmlns="http://www.w3.org/2000/svg" style="background:#fafafa;border:1px solid #e0e0e0;border-radius:6px;">
  <style>
    .axis { stroke: #444; stroke-width: 1.3; }
    .curve { fill: none; stroke: #2980b9; stroke-width: 2; }
    .pos { fill: rgba(46, 204, 113, 0.25); }
    .neg { fill: rgba(231, 76, 60, 0.25); }
    .title { font: bold 13px sans-serif; fill: #2c3e50; text-anchor: middle; }
    .lbl { font: 12px sans-serif; fill: #333; }
    .math { font: italic 13px serif; fill: #2c3e50; }
  </style>
  <!-- Left: Even function -->
  <text x="135" y="22" class="title">偶関数：f(-x) = f(x)（y軸対称）</text>
  <line x1="25" y1="140" x2="245" y2="140" class="axis"/>
  <line x1="135" y1="165" x2="135" y2="38" class="axis"/>
  <path d="M 65 140 L 65 65 Q 135 125 205 65 L 205 140 Z" class="pos"/>
  <path d="M 55 55 Q 135 135 215 55" class="curve"/>
  <line x1="65" y1="65" x2="65" y2="140" stroke="#7f8c8d" stroke-dasharray="3,2"/>
  <line x1="205" y1="65" x2="205" y2="140" stroke="#7f8c8d" stroke-dasharray="3,2"/>
  <text x="58" y="155" class="math">-a</text>
  <text x="138" y="155" class="lbl">O</text>
  <text x="201" y="155" class="math">a</text>
  <text x="100" y="122" class="lbl" fill="#27ae60" font-weight="bold">S</text>
  <text x="165" y="122" class="lbl" fill="#27ae60" font-weight="bold">S</text>
  <text x="135" y="178" class="lbl" text-anchor="middle">∫₋ₐᵃ f(x)dx = 2 ∫₀ᵃ f(x)dx</text>

  <!-- Divider -->
  <line x1="270" y1="15" x2="270" y2="178" stroke="#dcdcdc" stroke-dasharray="4,3"/>

  <!-- Right: Odd function -->
  <text x="405" y="22" class="title">奇関数：f(-x) = -f(x)（原点対称）</text>
  <line x1="295" y1="105" x2="515" y2="105" class="axis"/>
  <line x1="405" y1="165" x2="405" y2="38" class="axis"/>
  <path d="M 335 105 L 335 145 Q 370 155 405 105 Z" class="neg"/>
  <path d="M 405 105 Q 440 55 475 65 L 475 105 Z" class="pos"/>
  <path d="M 325 142 Q 370 160 405 105 Q 440 50 485 68" class="curve"/>
  <line x1="335" y1="105" x2="335" y2="145" stroke="#7f8c8d" stroke-dasharray="3,2"/>
  <line x1="475" y1="65" x2="475" y2="105" stroke="#7f8c8d" stroke-dasharray="3,2"/>
  <text x="328" y="98" class="math">-a</text>
  <text x="409" y="120" class="lbl">O</text>
  <text x="472" y="120" class="math">a</text>
  <text x="362" y="132" class="lbl" fill="#c0392b" font-weight="bold">-S</text>
  <text x="435" y="92" class="lbl" fill="#27ae60" font-weight="bold">+S</text>
  <text x="405" y="178" class="lbl" text-anchor="middle">∫₋ₐᵃ f(x)dx = (-S) + (+S) = 0</text>
</svg>

- **【分步标准解答】**
  $a = 0$ のときは積分区間が $[0, 0]$ より $0$（または極限としても $0$）。
  $a \neq 0$ のとき，被積分関数を $f(x) = \dfrac{x^3}{\sqrt{a^2 + x^2}}$ とおくと，
  $$f(-x) = \frac{(-x)^3}{\sqrt{a^2 + (-x)^2}} = -\frac{x^3}{\sqrt{a^2 + x^2}} = -f(x)$$
  ゆえに，$f(x)$ は奇関数である。積分区間 $[-a, a]$ は原点に関して対称であるから，
  $$\int_{-a}^a \frac{x^3}{\sqrt{a^2 + x^2}}\,dx = 0$$
  > 💡 讲师批注：**看到对称积分区间 $[-a, a]$，第一反应永远是先判断奇偶性！** 切勿傻傻去凑微分或换元。
- **【最终答案】**
  **$0$**

---

#### 演習問題 14-(9) [2]
- **【原题重现与翻译】**
  - 原题：次の定積分を求めよ。$\displaystyle\int_{-\frac{\pi}{2}}^{\frac{\pi}{2}} (2\sin x + \cos x)^3\,dx$
  - 中文：求定积分 $\displaystyle\int_{-\frac{\pi}{2}}^{\frac{\pi}{2}} (2\sin x + \cos x)^3\,dx$。
- **【考点定位】**
  - 展开后利用奇偶性消去奇函数项 + 凑微分（$t = \sin x$）。
- **【分步标准解答】**
  被積分関数を展開すると，
  $$(2\sin x + \cos x)^3 = 8\sin^3 x + 12\sin^2 x\cos x + 6\sin x\cos^2 x + \cos^3 x$$
  ここで，$\sin x$ は奇関数，$\cos x$ は偶関数であるから，
  - 奇関数：$8\sin^3 x,\; 6\sin x\cos^2 x$（$[-\frac{\pi}{2}, \frac{\pi}{2}]$ での積分は $0$）
  - 偶関数：$12\sin^2 x\cos x,\; \cos^3 x$
  > 💡 讲师批注：展开后四项中直接砍掉两项奇函数，剩下两项都恰好含有一个 $\cos x$ 因子，简直是为换元 $t = \sin x$ 量身定制的！

  したがって，
  $$\int_{-\frac{\pi}{2}}^{\frac{\pi}{2}} (2\sin x + \cos x)^3\,dx = 2\int_0^{\frac{\pi}{2}} (12\sin^2 x\cos x + \cos^3 x)\,dx$$
  $$= 2\int_0^{\frac{\pi}{2}} \bigl(12\sin^2 x + 1 - \sin^2 x\bigr)\cos x\,dx = 2\int_0^{\frac{\pi}{2}} (1 + 11\sin^2 x)\cos x\,dx$$
  $t = \sin x$ とおくと，$dt = \cos x\,dx$ であり，$x: 0 \to \dfrac{\pi}{2}$ のとき $t: 0 \to 1$。よって，
  $$= 2\int_0^1 (1 + 11t^2)\,dt = 2\left[t + \frac{11}{3}t^3\right]_0^1 = 2\left(1 + \frac{11}{3}\right) = \frac{28}{3}$$
- **【最终答案】**
  **$\dfrac{28}{3}$**

---

### 演習問題 14-(10)

#### 演習問題 14-(10) [1]
- **【原题重现与翻译】**
  - 原题：次の定積分を求めよ。$\displaystyle\int_0^{\frac{\pi}{2}} x\sin x\,dx$
  - 中文：求定积分 $\displaystyle\int_0^{\frac{\pi}{2}} x\sin x\,dx$。
- **【考点定位】**
  - 定积分的分部积分法（多项式 × 三角函数）。
- **【分步标准解答】**
  $(\cos x)' = -\sin x$ より $\sin x = (-\cos x)'$ を用いて部分積分を行うと，
  $$\int_0^{\frac{\pi}{2}} x\sin x\,dx = \int_0^{\frac{\pi}{2}} x(-\cos x)'\,dx$$
  $$= \Bigl[-x\cos x\Bigr]_0^{\frac{\pi}{2}} - \int_0^{\frac{\pi}{2}} 1\cdot (-\cos x)\,dx$$
  > 💡 讲师批注：分部积分口诀「**反对幂三指**（谁在后面谁先凑进导数里）」：$x$（幂）求导降次，$\sin x$（三）凑导数。

  $$= \left(-\frac{\pi}{2}\cos\frac{\pi}{2} + 0\right) + \Bigl[\sin x\Bigr]_0^{\frac{\pi}{2}} = 0 + (1 - 0) = 1$$
- **【最终答案】**
  **$1$**

---

#### 演習問題 14-(10) [2]
- **【原题重现与翻译】**
  - 原题：次の定積分を求めよ。$\displaystyle\int_1^e \log x\,dx$
  - 中文：求定积分 $\displaystyle\int_1^e \log x\,dx$。
- **【考点定位】**
  - 对数函数的分部积分法（补乘 $1 = (x)'$）。
- **【分步标准解答】**
  $\log x = (x)'\log x$ とみて部分積分を行うと，
  $$\int_1^e \log x\,dx = \Bigl[x\log x\Bigr]_1^e - \int_1^e x \cdot \frac{1}{x}\,dx$$
  $$= (e\log e - 1\cdot\log 1) - \int_1^e 1\,dx = (e - 0) - \Bigl[x\Bigr]_1^e$$
  $$= e - (e - 1) = 1$$
  > 💡 讲师批注：$\int \log x\,dx = x\log x - x + C$ 建议直接背诵，在 EJU 考试中出现频率极高。
- **【最终答案】**
  **$1$**

---

### 演習問題 14-(11)

#### 演習問題 14-(11) [1]
- **【原题重现与翻译】**
  - 原题：次の定積分を求めよ。$\displaystyle\int_{-2}^2 |x^2 - 4|\,dx$
  - 中文：求定积分 $\displaystyle\int_{-2}^2 |x^2 - 4|\,dx$。
- **【考点定位】**
  - 含绝对值函数的定积分 + 偶函数对称性（或 1/6 公式）。
- **【图解辅助（SVG 矢量图）】**
  在区间 $[-2, 2]$ 内 $x^2 - 4 \le 0$，故 $|x^2 - 4| = 4 - x^2$：

<svg viewBox="0 0 420 200" width="420" height="200" xmlns="http://www.w3.org/2000/svg" style="background:#fafafa;border:1px solid #e0e0e0;border-radius:6px;">
  <style>
    .axis { stroke: #333; stroke-width: 1.4; }
    .curve { fill: none; stroke: #2980b9; stroke-width: 2.2; }
    .dash { fill: none; stroke: #95a5a6; stroke-width: 1.3; stroke-dasharray: 4,3; }
    .area { fill: rgba(52, 152, 219, 0.22); }
    .lbl { font: 12px sans-serif; fill: #2c3e50; }
    .math { font: italic 13px serif; fill: #2c3e50; }
  </style>
  <!-- Axes -->
  <line x1="30" y1="150" x2="390" y2="150" class="axis"/>
  <polygon points="390,150 382,146 382,154" fill="#333"/>
  <text x="396" y="154" class="math">x</text>
  <line x1="210" y1="185" x2="210" y2="18" class="axis"/>
  <polygon points="210,18 206,26 214,26" fill="#333"/>
  <text x="195" y="24" class="math">y</text>
  <!-- Shaded arch y = 4 - x^2 on [-2, 2]: scale x: 50px=1, y: 25px=1 -->
  <!-- x=-2 -> 110, x=2 -> 310, vertex (0,4) -> (210, 50) => quad control y = 150 - 2*100 = -50 -->
  <path d="M 110 150 Q 210 -50 310 150 Z" class="area"/>
  <!-- y = |x^2 - 4| curve -->
  <path d="M 85 87.5 L 110 150" class="curve"/>
  <path d="M 110 150 Q 210 -50 310 150" class="curve"/>
  <path d="M 310 150 L 335 87.5" class="curve"/>
  <!-- Dashed original below x-axis -->
  <path d="M 110 150 Q 210 210 310 150" class="dash"/>
  <text x="102" y="168" class="lbl">-2</text>
  <text x="215" y="168" class="lbl">O</text>
  <text x="307" y="168" class="lbl">2</text>
  <text x="216" y="48" class="lbl">4</text>
  <text x="295" y="65" class="math">y = |x² - 4|</text>
  <text x="210" y="115" class="lbl" text-anchor="middle" fill="#2980b9" font-weight="bold">y = 4 - x²</text>
</svg>

- **【分步标准解答】**
  区間 $-2 \le x \le 2$ において $x^2 - 4 \le 0$ であるから，$|x^2 - 4| = 4 - x^2$。
  また，$4 - x^2$ は偶関数であるから，
  $$\int_{-2}^2 |x^2 - 4|\,dx = \int_{-2}^2 (4 - x^2)\,dx = 2\int_0^2 (4 - x^2)\,dx$$
  $$= 2\left[4x - \frac{1}{3}x^3\right]_0^2 = 2\left(8 - \frac{8}{3}\right) = 2 \cdot \frac{16}{3} = \frac{32}{3}$$
  > 💡 讲师批注：也可直接套用 1/6 公式：$-\int_{-2}^2 (x+2)(x-2)\,dx = \dfrac{1}{6}\{2 - (-2)\}^3 = \dfrac{64}{6} = \dfrac{32}{3}$，一秒秒杀！
- **【最终答案】**
  **$\dfrac{32}{3}$**

---

#### 演習問題 14-(11) [2]
- **【原题重现与翻译】**
  - 原题：次の定積分を求めよ。$\displaystyle\int_0^4 \frac{1}{\sqrt{|x(x - 2)|}}\,dx$
  - 中文：求定积分 $\displaystyle\int_0^4 \frac{1}{\sqrt{|x(x - 2)|}}\,dx$。
- **【考点定位】**
  - 分段去绝对值 + 广义积分（広義積分）+ 配方后的三角换元与无理换元（欧拉代换）。
- **【分步标准解答】**
  積分区間 $[0, 4]$ を $x = 2$ で分ける（被積分関数は $x = 0, 2$ で発散するため，厳密には広義積分として極限をとる）。
  $$I = \int_0^4 \frac{dx}{\sqrt{|x(x - 2)|}} = \underbrace{\int_0^2 \frac{dx}{\sqrt{2x - x^2}}}_{I_1} + \underbrace{\int_2^4 \frac{dx}{\sqrt{x^2 - 2x}}}_{I_2}$$
  > 💡 讲师批注：这是一道极具挑战性的好题！区间 $(0,2)$ 上 $x(x-2) < 0$，绝对值变成 $2x-x^2 = 1-(x-1)^2$；区间 $(2,4)$ 上 $x(x-2) > 0$，绝对值变成 $x^2-2x = (x-1)^2-1$。

  **① $I_1$ の計算**：$2x - x^2 = 1 - (x - 1)^2$ であるから，$x - 1 = \sin\theta$（$-\dfrac{\pi}{2} < \theta < \dfrac{\pi}{2}$）とおくと，$dx = \cos\theta\,d\theta$，$\sqrt{1 - (x-1)^2} = \cos\theta$。
  $x: 0^+ \to 2^-$ のとき $\theta: -\dfrac{\pi}{2} \to \dfrac{\pi}{2}$ となるので，
  $$I_1 = \lim_{\varepsilon_1\to +0,\,\varepsilon_2\to +0}\int_{\varepsilon_1}^{2-\varepsilon_2}\frac{dx}{\sqrt{1-(x-1)^2}} = \int_{-\frac{\pi}{2}}^{\frac{\pi}{2}} \frac{\cos\theta}{\cos\theta}\,d\theta = \Bigl[\theta\Bigr]_{-\frac{\pi}{2}}^{\frac{\pi}{2}} = \pi$$

  **② $I_2$ の計算**：$x^2 - 2x = (x - 1)^2 - 1$ である。ここで $u = x - 1$ とおくと $u: 1 \to 3$ であり，
  $$I_2 = \int_1^3 \frac{du}{\sqrt{u^2 - 1}}$$
  さらに $t = u + \sqrt{u^2 - 1}$ とおくと，$\dfrac{dt}{du} = 1 + \dfrac{u}{\sqrt{u^2 - 1}} = \dfrac{u + \sqrt{u^2 - 1}}{\sqrt{u^2 - 1}} = \dfrac{t}{\sqrt{u^2 - 1}}$，すなわち $\dfrac{du}{\sqrt{u^2 - 1}} = \dfrac{dt}{t}$ となる。
  > 💡 讲师批注：对于 $\displaystyle\int \frac{du}{\sqrt{u^2 \pm a^2}}$，记住万能换元 $t = u + \sqrt{u^2 \pm a^2}$，立刻化为 $\displaystyle\int \frac{dt}{t} = \log|t|$！

  $u: 1^+ \to 3$ のとき $t: 1^+ \to 3 + \sqrt{8} = 3 + 2\sqrt{2}$ であるから，
  $$I_2 = \lim_{\varepsilon\to +0}\int_{1+\varepsilon}^{3+2\sqrt{2}} \frac{dt}{t} = \Bigl[\log t\Bigr]_1^{3+2\sqrt{2}} = \log(3 + 2\sqrt{2}) = 2\log(1 + \sqrt{2})$$
  > 💡 讲师批注：注意到 $3 + 2\sqrt{2} = (1 + \sqrt{2})^2$，故 $\log(3 + 2\sqrt{2}) = 2\log(1 + \sqrt{2})$，两种写法均完全等价。

  以上より，
  $$I = I_1 + I_2 = \pi + \log(3 + 2\sqrt{2}) \quad \bigl(= \pi + 2\log(1 + \sqrt{2})\bigr)$$
- **【最终答案】**
  **$\pi + \log(3 + 2\sqrt{2})$**（亦可写作 **$\pi + 2\log(1 + \sqrt{2})$**）

---

### 演習問題 14-(12)

#### 演習問題 14-(12) [1]
- **【原题重现与翻译】**
  - 原题：次の定積分を求めよ。$\displaystyle\int_1^2 \frac{\log x}{x}\,dx$
  - 中文：求定积分 $\displaystyle\int_1^2 \frac{\log x}{x}\,dx$。
- **【考点定位】**
  - 换元积分法（令 $t = \log x$）。
- **【分步标准解答】**
  $t = \log x$ とおくと，$dt = \dfrac{1}{x}\,dx$。
  $x: 1 \to 2$ のとき $t: 0 \to \log 2$ であるから，
  $$\int_1^2 \frac{\log x}{x}\,dx = \int_0^{\log 2} t\,dt = \left[\frac{1}{2}t^2\right]_0^{\log 2} = \frac{1}{2}(\log 2)^2$$
  > 💡 讲师批注：注意 $(\log 2)^2$ **不能**写成 $\log 2^2 = 2\log 2$，括号万万不可省略！
- **【最终答案】**
  **$\dfrac{1}{2}(\log 2)^2$**

---

#### 演習問題 14-(12) [2]
- **【原题重现与翻译】**
  - 原题：次の定積分を求めよ。$\displaystyle\int_0^{2\pi} x^2 |\sin x|\,dx$
  - 中文：求定积分 $\displaystyle\int_0^{2\pi} x^2 |\sin x|\,dx$。
- **【考点定位】**
  - 分段去绝对值 + 连续两次分部积分法。
- **【分步标准解答】**
  区間 $[0, \pi]$ で $\sin x \ge 0$，区間 $[\pi, 2\pi]$ で $\sin x \le 0$ であるから，
  $$\int_0^{2\pi} x^2 |\sin x|\,dx = \int_0^\pi x^2\sin x\,dx - \int_\pi^{2\pi} x^2\sin x\,dx$$
  > 💡 讲师批注：先统一求出 $x^2\sin x$ 的一个原函数 $F(x)$，再代入端点 $0, \pi, 2\pi$，比分别做两次分部积分更简洁、不易出错！

  ここで，$\displaystyle\int x^2\sin x\,dx$ を部分積分法を 2 回用いて求める：
  $$\int x^2\sin x\,dx = \int x^2(-\cos x)'\,dx = -x^2\cos x + 2\int x\cos x\,dx$$
  $$= -x^2\cos x + 2\int x(\sin x)'\,dx = -x^2\cos x + 2\left(x\sin x - \int \sin x\,dx\right)$$
  $$= -x^2\cos x + 2x\sin x + 2\cos x + C = (2 - x^2)\cos x + 2x\sin x + C$$
  > 💡 讲师批注：求完立即求导验算：$-2x\cos x - (2-x^2)\sin x + 2\sin x + 2x\cos x = x^2\sin x$，100% 正确！

  $F(x) = (2 - x^2)\cos x + 2x\sin x$ とおくと，
  - $F(0) = 2\cdot 1 + 0 = 2$
  - $F(\pi) = (2 - \pi^2)(-1) + 0 = \pi^2 - 2$
  - $F(2\pi) = (2 - 4\pi^2)\cdot 1 + 0 = 2 - 4\pi^2$

  したがって，
  $$\int_0^{2\pi} x^2|\sin x|\,dx = \bigl\{F(\pi) - F(0)\bigr\} - \bigl\{F(2\pi) - F(\pi)\bigr\} = 2F(\pi) - F(0) - F(2\pi)$$
  $$= 2(\pi^2 - 2) - 2 - (2 - 4\pi^2) = 2\pi^2 - 4 - 2 - 2 + 4\pi^2 = 6\pi^2 - 8$$
- **【最终答案】**
  **$6\pi^2 - 8$**

---

### 演習問題 14-(13)
- **【原题重现与翻译】**
  - 原题：$a$ は $0$ でない定数とし，$A = \displaystyle\int_0^\pi e^{-ax}\sin 2x\,dx,\; B = \displaystyle\int_0^\pi e^{-ax}\cos 2x\,dx$ とする。このとき，$A, B$ の値をそれぞれ求めよ。
  - 中文：设 $a$ 为非零常数，$A = \displaystyle\int_0^\pi e^{-ax}\sin 2x\,dx$，$B = \displaystyle\int_0^\pi e^{-ax}\cos 2x\,dx$。求 $A, B$ 的值。
- **【考点定位】**
  - 指数函数 × 三角函数的**循环分部积分法**（建立关于 $A, B$ 的二元一次方程组）。
- **【分步标准解答】**
  $A$ に対して，$\sin 2x = \left(-\dfrac{1}{2}\cos 2x\right)'$ を用いて部分積分を行うと，
  $$A = \left[-\frac{1}{2}e^{-ax}\cos 2x\right]_0^\pi - \int_0^\pi (-a e^{-ax})\left(-\frac{1}{2}\cos 2x\right)dx$$
  $$= \left(-\frac{1}{2}e^{-a\pi}\cdot 1\right) - \left(-\frac{1}{2}\cdot 1\cdot 1\right) - \frac{a}{2}B = \frac{1 - e^{-a\pi}}{2} - \frac{a}{2}B$$
  整理すると，
  $$2A + aB = 1 - e^{-a\pi} \quad \cdots \text{①}$$
  > 💡 讲师批注：也可以把 $e^{-ax} = \left(-\frac{1}{a}e^{-ax}\right)'$ 凑进导数，但注意把三角函数凑进导数可以避免分母出现 $a$（甚至在 $a=0$ 时也无分母为零之忧），计算更干净！

  同様に，$B$ に対して $\cos 2x = \left(\dfrac{1}{2}\sin 2x\right)'$ を用いて部分積分を行うと，
  $$B = \left[\frac{1}{2}e^{-ax}\sin 2x\right]_0^\pi - \int_0^\pi (-a e^{-ax})\left(\frac{1}{2}\sin 2x\right)dx$$
  $$= (0 - 0) + \frac{a}{2}A = \frac{a}{2}A \quad \cdots \text{②}$$
  ② を ① に代入すると，
  $$2A + \frac{a^2}{2}A = 1 - e^{-a\pi} \iff \frac{a^2 + 4}{2}A = 1 - e^{-a\pi}$$
  $a^2 + 4 > 0$ であるから，
  $$A = \frac{2(1 - e^{-a\pi})}{a^2 + 4}$$
  ② より，
  $$B = \frac{a}{2}A = \frac{a(1 - e^{-a\pi})}{a^2 + 4}$$
  > 💡 讲师批注：因为 $a \neq 0$，两式结果清晰且分母 $a^2+4 > 0$ 恒不为零。可代入特值（如 $a \to 0$ 时 $A \to 0, B \to 0$，正好符合 $\int_0^\pi \sin 2x\,dx = 0$ 与 $\int_0^\pi \cos 2x\,dx = 0$）快速检验！
- **【最终答案】**
  **$A = \dfrac{2(1 - e^{-a\pi})}{a^2 + 4},\qquad B = \dfrac{a(1 - e^{-a\pi})}{a^2 + 4}$**

---

### 演習問題 14-(14)
- **【原题重现与翻译】**
  - 原题：連続な関数 $f(x)$ について，等式 $\displaystyle\int_0^\pi x f(\sin x)\,dx = \frac{\pi}{2}\int_0^\pi f(\sin x)\,dx$ を示せ。
  - 中文：对连续函数 $f(x)$，证明等式 $\displaystyle\int_0^\pi x f(\sin x)\,dx = \frac{\pi}{2}\int_0^\pi f(\sin x)\,dx$。
- **【考点定位】**
  - **King's Property（对称区间换元法）**：$x = \pi - t$。
- **【分步标准解答】**
  $I = \displaystyle\int_0^\pi x f(\sin x)\,dx$ とおく。
  $x = \pi - t$ とおくと，$dx = -dt$ であり，$x: 0 \to \pi$ のとき $t: \pi \to 0$。
  また，$\sin(\pi - t) = \sin t$ であるから，
  $$I = \int_\pi^0 (\pi - t)f(\sin(\pi - t))(-dt) = \int_0^\pi (\pi - t)f(\sin t)\,dt$$
  > 💡 讲师批注：定积分的值与积分变量的字母无关（哑变量），将 $t$ 改写回 $x$ 即可与原式 $I$ 合并！

  $$= \pi\int_0^\pi f(\sin t)\,dt - \int_0^\pi t f(\sin t)\,dt = \pi\int_0^\pi f(\sin x)\,dx - I$$
  よって，
  $$2I = \pi\int_0^\pi f(\sin x)\,dx \implies I = \frac{\pi}{2}\int_0^\pi f(\sin x)\,dx \quad \text{（証明終わり）}$$
  > 💡 讲师批注：这是 EJU 数学Ⅲ 超级经典的一条性质！遇到 $\int_0^\pi x\cdot(\text{只含 }\sin x\text{ 的式子})\,dx$，直接用 $x = \pi - t$ 就能把讨厌的因子 $x$ 消掉！
- **【最终答案】**
  **証明完了（如上所示）**

---

### 演習問題 14-(15)
- **【原题重现与翻译】**
  - 原题：(14) の等式を利用して，定積分 $\displaystyle\int_0^\pi \frac{x\sin x}{3 + \sin^2 x}\,dx$ を求めよ。
  - 中文：利用 (14) 的等式，求定积分 $\displaystyle\int_0^\pi \frac{x\sin x}{3 + \sin^2 x}\,dx$。
- **【考点定位】**
  - 应用 (14) 消去因子 $x$ + 换元 $t = \cos x$ + 部分分式分解。
- **【分步标准解答】**
  (14) の等式において $f(u) = \dfrac{u}{3 + u^2}$ とおくと，
  $$\int_0^\pi \frac{x\sin x}{3 + \sin^2 x}\,dx = \frac{\pi}{2}\int_0^\pi \frac{\sin x}{3 + \sin^2 x}\,dx$$
  分母に $\sin^2 x = 1 - \cos^2 x$ を代入すると，
  $$= \frac{\pi}{2}\int_0^\pi \frac{\sin x}{4 - \cos^2 x}\,dx$$
  > 💡 讲师批注：分子有 $\sin x\,dx = -d(\cos x)$，把分母全部改写成 $\cos x$ 就能立即换元！

  ここで，$t = \cos x$ とおくと，$dt = -\sin x\,dx$ であり，$x: 0 \to \pi$ のとき $t: 1 \to -1$。よって，
  $$= \frac{\pi}{2}\int_1^{-1} \frac{-dt}{4 - t^2} = \frac{\pi}{2}\int_{-1}^1 \frac{dt}{4 - t^2}$$
  $\dfrac{1}{4 - t^2}$ は偶関数であり，$\dfrac{1}{4 - t^2} = \dfrac{1}{(2 - t)(2 + t)} = \dfrac{1}{4}\left(\dfrac{1}{2 - t} + \dfrac{1}{2 + t}\right)$ であるから，
  $$= \frac{\pi}{2} \cdot 2\int_0^1 \frac{dt}{4 - t^2} = \frac{\pi}{4}\int_0^1 \left(\frac{1}{2 - t} + \frac{1}{2 + t}\right)dt$$
  $$= \frac{\pi}{4}\Bigl[-\log(2 - t) + \log(2 + t)\Bigr]_0^1 = \frac{\pi}{4}\left[\log\frac{2 + t}{2 - t}\right]_0^1$$
  $$= \frac{\pi}{4}\left(\log\frac{3}{1} - \log\frac{2}{2}\right) = \frac{\pi}{4}\log 3$$
  > 💡 讲师批注：特别注意 $\displaystyle\int \frac{dt}{2-t} = -\log|2-t|$，前面的负号千万不要漏掉！
- **【最终答案】**
  **$\dfrac{\pi}{4}\log 3$**

---

### 演習問題 14-(16)
- **【原题重现与翻译】**
  - 原题：$f(x) = \dfrac{e^x}{e^x + 1}$ のとき，$y = f(x)$ の逆関数 $y = g(x)$ を求めよ。
  - 中文：当 $f(x) = \dfrac{e^x}{e^x + 1}$ 时，求 $y = f(x)$ 的反函数 $y = g(x)$。
- **【考点定位】**
  - 反函数的求法与定义域（原函数的值域）的确定。
- **【分步标准解答】**
  $y = \dfrac{e^x}{e^x + 1} = 1 - \dfrac{1}{e^x + 1}$ と変形できる。
  $e^x > 0$ より $e^x + 1 > 1$ であるから，$0 < \dfrac{1}{e^x + 1} < 1$，したがって原関数の値域は，
  $$0 < y < 1$$
  > 💡 讲师批注：**求反函数必须同时写出定义域！** 原函数的值域就是反函数的定义域。

  次に，$y = \dfrac{e^x}{e^x + 1}$ を $x$ について解く：
  $$y(e^x + 1) = e^x \iff (1 - y)e^x = y \iff e^x = \frac{y}{1 - y}$$
  両辺の自然対数をとると，$x = \log\dfrac{y}{1 - y}$。
  $x$ と $y$ を入れ替えて，求める逆関数は，
  $$y = g(x) = \log\frac{x}{1 - x} \qquad (0 < x < 1)$$
- **【最终答案】**
  **$g(x) = \log\dfrac{x}{1 - x} \quad (0 < x < 1)$**

---

### 演習問題 14-(17)
- **【原题重现与翻译】**
  - 原题：(16) の $f(x), g(x)$ に対し，次の等式が成り立つことを示せ。
    $$\int_a^b f(x)\,dx + \int_{f(a)}^{f(b)} g(x)\,dx = b f(b) - a f(a)$$
  - 中文：对 (16) 中的 $f(x), g(x)$，证明下列等式成立：
    $$\int_a^b f(x)\,dx + \int_{f(a)}^{f(b)} g(x)\,dx = b f(b) - a f(a)$$
- **【考点定位】**
  - 反函数定积分恒等式（换元积分法 + 分部积分法；几何意义为大矩形减去小矩形）。
- **【图解辅助（SVG 矢量图）】**
  当 $0 < a < b$ 且 $f$ 单调递增时，两项定积分恰好拼成 L 形区域（大矩形面积 $b f(b)$ 减去小矩形面积 $a f(a)$）：

<svg viewBox="0 0 420 240" width="420" height="240" xmlns="http://www.w3.org/2000/svg" style="background:#fafafa;border:1px solid #e0e0e0;border-radius:6px;">
  <style>
    .axis { stroke: #333; stroke-width: 1.4; }
    .curve { fill: none; stroke: #2c3e50; stroke-width: 2.3; }
    .area1 { fill: rgba(52, 152, 219, 0.25); }
    .area2 { fill: rgba(230, 126, 34, 0.25); }
    .smallrect { fill: rgba(189, 195, 199, 0.35); stroke: #7f8c8d; stroke-dasharray: 3,2; }
    .dash { stroke: #7f8c8d; stroke-width: 1; stroke-dasharray: 3,2; }
    .lbl { font: 12px sans-serif; fill: #2c3e50; }
    .math { font: italic 13px serif; fill: #2c3e50; }
  </style>
  <!-- Origin at (70, 200) -->
  <!-- a=150, b=330; f(a)=145 (height 55), f(b)=55 (height 145) -->
  <!-- Small rectangle a*f(a) -->
  <rect x="70" y="145" width="80" height="55" class="smallrect"/>
  <!-- Area 1: integral_a^b f(x) dx -->
  <path d="M 150 200 L 150 145 C 205 130, 250 75, 330 55 L 330 200 Z" class="area1"/>
  <!-- Area 2: integral_{f(a)}^{f(b)} g(y) dy -->
  <path d="M 70 145 L 150 145 C 205 130, 250 75, 330 55 L 70 55 Z" class="area2"/>
  <!-- Axes -->
  <line x1="40" y1="200" x2="395" y2="200" class="axis"/>
  <polygon points="395,200 387,196 387,204" fill="#333"/>
  <text x="400" y="204" class="math">x</text>
  <line x1="70" y1="225" x2="70" y2="20" class="axis"/>
  <polygon points="70,20 66,28 74,28" fill="#333"/>
  <text x="55" y="26" class="math">y</text>
  <!-- Dashed bounding lines -->
  <line x1="150" y1="145" x2="150" y2="200" class="dash"/>
  <line x1="330" y1="55" x2="330" y2="200" class="dash"/>
  <line x1="70" y1="145" x2="150" y2="145" class="dash"/>
  <line x1="70" y1="55" x2="330" y2="55" class="dash"/>
  <!-- Curve y = f(x) -->
  <path d="M 100 162 C 160 148, 240 75, 365 46" class="curve"/>
  <!-- Labels -->
  <text x="55" y="214" class="lbl">O</text>
  <text x="147" y="216" class="math">a</text>
  <text x="327" y="216" class="math">b</text>
  <text x="36" y="149" class="math">f(a)</text>
  <text x="36" y="59" class="math">f(b)</text>
  <text x="355" y="38" class="math">y = f(x)</text>
  <text x="110" y="177" class="lbl" text-anchor="middle" fill="#7f8c8d">a·f(a)</text>
  <text x="255" y="160" class="lbl" text-anchor="middle" fill="#2980b9" font-weight="bold">∫ₐᵇ f(x)dx</text>
  <text x="158" y="95" class="lbl" text-anchor="middle" fill="#d35400" font-weight="bold">∫f(a)f(b) g(y)dy</text>
</svg>

- **【分步标准解答】**
  (16) より，$f(x)$ は微分可能で $g(f(t)) = t$ を満たす。
  左辺の第 2 項 $\displaystyle\int_{f(a)}^{f(b)} g(x)\,dx$ において，$x = f(t)$ と置換すると，$dx = f'(t)\,dt$ であり，
  $x: f(a) \to f(b)$ のとき $t: a \to b$ となる（$f$ は単調増加なので $1$ 対 $1$ に対応）。
  したがって，
  $$\int_{f(a)}^{f(b)} g(x)\,dx = \int_a^b g(f(t))\,f'(t)\,dt = \int_a^b t\,f'(t)\,dt$$
  > 💡 讲师批注：切忌把 $f(x)=\frac{e^x}{e^x+1}$ 和 $g(x)=\log\frac{x}{1-x}$ 具体表达式硬代入积分！利用反函数本质关系 $g(f(t)) = t$ 一步换元，再用分部积分，对**任意可微单调反函数对**普遍成立！

  さらに部分積分法を用いると，
  $$\int_a^b t\,f'(t)\,dt = \Bigl[t\,f(t)\Bigr]_a^b - \int_a^b 1\cdot f(t)\,dt = b f(b) - a f(a) - \int_a^b f(x)\,dx$$
  右辺の定積分を左辺に移項すると，
  $$\int_a^b f(x)\,dx + \int_{f(a)}^{f(b)} g(x)\,dx = b f(b) - a f(a) \quad \text{（証明終わり）}$$
- **【最终答案】**
  **証明完了（如上所示）**

---

> 👉 **下篇请继续阅读**：[`note_026_b.md`](./note_026_b.md)（演習問題 15 全 11 题深度解析 + 区分求积法例题与 SVG 图解）
