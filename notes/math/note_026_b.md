# 《EJU 教材全解与备课讲义》数学 026（P376–P390，下篇）

> **对应源文件**：`work_math/ocr_md/ocr_026_p376-390.md`（第七章《微分積分》之「定積分で表された関数（演習問題 15）」「定積分と和の極限、不等式（[18.1]–[18.2]・[18.1]解説(1)）」）
> **视觉核对参考图**：`work_math/ref_imgs/page_0385.jpg` – `page_0390.jpg`（逐页逐符号视觉核对）
> **衔接说明**：本篇承接 [`note_026_a.md`](./note_026_a.md)（知识点总览、国内 vs. EJU 考纲对比、日文核心词汇与公式口语读法、演習問題 14 全 27 题详解），完整覆盖本切片剩余的 **演習問題 15 全 11 题** 及 **[18.1] 区分求积法例题与 [18.2] 定积分不等式图解**。

---

## 三、逐题深度解析（不可跳步）— 下篇：演習問題 15 与区分求积法例题

---

### 演習問題 15-(1)

#### 演習問題 15-(1) [1]
- **【原题重现与翻译】**
  - 原题：次の等式を満たす関数 $f(x)$ を求めよ。
    $$f(x) = 6x^2 - x + \int_{-1}^1 f(t)\,dx \quad \text{（※ 教材原印为 } dx \text{）}$$
  - 中文：求满足等式 $f(x) = 6x^2 - x + \displaystyle\int_{-1}^1 f(t)\,dt$ 的函数 $f(x)$。
  > ⚠️ **教材勘误提示**：原教材第 385 页（`page_0386.jpg`）将积分微元误印为 $dx$，结合被积函数变量 $t$ 及本节主题，应修正为 $dt$。以下按修正后的 $dt$ 解答。
- **【考点定位】**
  - **积分方程（定积分常量型）**：利用「上下限均为常数的定积分是一个常数」设为 $A$，代回求解。
- **【分步标准解答】**
  $\displaystyle\int_{-1}^1 f(t)\,dt$ は定数であるから，これを $A$ とおくと，
  $$A = \int_{-1}^1 f(t)\,dt \quad \cdots \text{①}$$
  与式より，
  $$f(x) = 6x^2 - x + A \quad \cdots \text{②}$$
  > 💡 讲师批注：看到积分上下限都是具体数字（$-1$ 和 $1$），立刻把整个定积分设成大写字母 $A$，这是最标准的得分第一步！

  ② より $f(t) = 6t^2 - t + A$ であるから，これを ① に代入すると，
  $$A = \int_{-1}^1 (6t^2 - t + A)\,dt$$
  積分区間 $[-1, 1]$ は原点に関して対称であり，$6t^2 + A$ は偶関数，$-t$ は奇関数であるから，
  $$A = 2\int_0^1 (6t^2 + A)\,dt = 2\Bigl[2t^3 + At\Bigr]_0^1 = 2(2 + A) = 4 + 2A$$
  > 💡 讲师批注：利用对称区间 $[-1, 1]$ 上的奇偶性，直接砍掉奇函数项 $-t$，计算量减半且极不易算错符号！

  これを解くと，$A = -4$。
  ② に代入して，
  $$f(x) = 6x^2 - x - 4$$
  > 💡 讲师批注：口算验算：$\int_{-1}^1 (6t^2 - t - 4)\,dt = 2[2t^3 - 4t]_0^1 = 2(2 - 4) = -4 = A$，完全正确！
- **【最终答案】**
  **$f(x) = 6x^2 - x - 4$**

---

#### 演習問題 15-(1) [2]
- **【原题重现与翻译】**
  - 原题：次の等式を満たす関数 $f(x)$ を求めよ。
    $$f(x) = \int_0^1 x f(t)\,dt + \int_0^1 t f(t)\,dt + 1$$
  - 中文：求满足等式 $f(x) = \displaystyle\int_0^1 x f(t)\,dt + \int_0^1 t f(t)\,dt + 1$ 的函数 $f(x)$。
- **【考点定位】**
  - **双常数型积分方程**：先将与积分变量 $t$ 无关的 $x$ 提到积分号外，再设两个独立常数 $A, B$ 列二元一次方程组。
- **【分步标准解答】**
  第 1 項において，変数 $x$ は積分変数 $t$ に無関係であるから積分の外に出すことができる：
  $$f(x) = x\int_0^1 f(t)\,dt + \int_0^1 t f(t)\,dt + 1$$
  ここで，2 つの定積分はともに定数であるから，
  $$A = \int_0^1 f(t)\,dt \quad \cdots \text{①}, \qquad B = \int_0^1 t f(t)\,dt \quad \cdots \text{②}$$
  とおくと，与式は
  $$f(x) = Ax + B + 1 \quad \cdots \text{③}$$
  > 💡 讲师批注：**千万不要把 $x$ 留在 $\int_0^1 x f(t)\,dt$ 里面直接设为常数！** 必须先提出来写成 $x\int_0^1 f(t)\,dt$，剩下纯关于 $t$ 的定积分才是常数。

  ③ より $f(t) = At + B + 1$ であるから，これを ① に代入すると，
  $$A = \int_0^1 (At + B + 1)\,dt = \left[\frac{A}{2}t^2 + (B + 1)t\right]_0^1 = \frac{A}{2} + B + 1$$
  両辺に $2$ を掛けて整理すると，
  $$A - 2B = 2 \quad \cdots \text{④}$$

  次に，③ を ② に代入すると，
  $$B = \int_0^1 t(At + B + 1)\,dt = \int_0^1 \bigl(At^2 + (B + 1)t\bigr)\,dt = \left[\frac{A}{3}t^3 + \frac{B + 1}{2}t^2\right]_0^1 = \frac{A}{3} + \frac{B + 1}{2}$$
  両辺に $6$ を掛けて整理すると，
  $$6B = 2A + 3B + 3 \iff 2A - 3B = -3 \quad \cdots \text{⑤}$$

  ④ より $A = 2B + 2$ を ⑤ に代入すると，
  $$2(2B + 2) - 3B = -3 \iff B + 4 = -3 \iff B = -7$$
  よって，$A = 2(-7) + 2 = -12$。
  これらを ③ に代入すると，
  $$f(x) = -12x + (-7) + 1 = -12x - 6$$
  > 💡 讲师批注：代回检验：$A = \int_0^1 (-12t-6)\,dt = [-6t^2-6t]_0^1 = -12$，$B = \int_0^1 (-12t^2-6t)\,dt = [-4t^3-3t^2]_0^1 = -7$，完全吻合！
- **【最终答案】**
  **$f(x) = -12x - 6$**

---

### 演習問題 15-(2)

#### 演習問題 15-(2) [1]
- **【原题重现与翻译】**
  - 原题：次の等式を満たす関数 $f(x)$ 及び定数 $a$ の値を求めよ。
    $$\int_a^x f(t)\,dt = x^2 - 3x - 4$$
  - 中文：求满足等式 $\displaystyle\int_a^x f(t)\,dt = x^2 - 3x - 4$ 的函数 $f(x)$ 及常数 $a$ 的值。
- **【考点定位】**
  - **变限积分方程标准模板**：① 两边对 $x$ 求导求 $f(x)$；② 令 $x = a$（使上下限相等）求常数 $a$。
- **【分步标准解答】**
  与式の両辺を $x$ で微分すると，$\dfrac{d}{dx}\displaystyle\int_a^x f(t)\,dt = f(x)$ より，
  $$f(x) = (x^2 - 3x - 4)' = 2x - 3$$
  また，与式に $x = a$ を代入すると，左辺は $\displaystyle\int_a^a f(t)\,dt = 0$ となるから，
  $$0 = a^2 - 3a - 4$$
  $$(a - 4)(a + 1) = 0 \implies a = -1,\; 4$$
  > 💡 讲师批注：EJU 必考的「**一导一代**」双步法！注意 $a$ 有两个解 $-1$ 和 $4$，因为题目没有对 $a$ 加正负限制，两个解都要保留。
- **【最终答案】**
  **$f(x) = 2x - 3,\qquad a = -1,\; 4$**

---

#### 演習問題 15-(2) [2]
- **【原题重现与翻译】**
  - 原题：次の等式を満たす関数 $f(x)$ 及び定数 $a$ の値を求めよ。
    $$\int_x^a f(t)\,dt = x^3 - 3x$$
  - 中文：求满足等式 $\displaystyle\int_x^a f(t)\,dt = x^3 - 3x$ 的函数 $f(x)$ 及常数 $a$ 的值。
- **【考点定位】**
  - 积分下限为变量 $x$ 时的求导（别忘负号！）+ 令 $x = a$ 求常数 $a$。
- **【分步标准解答】**
  左辺は $\displaystyle\int_x^a f(t)\,dt = -\int_a^x f(t)\,dt$ であるから，与式の両辺を $x$ で微分すると，
  $$-f(x) = (x^3 - 3x)' = 3x^2 - 3$$
  したがって，
  $$f(x) = -3x^2 + 3$$
  > 💡 讲师批注：**高频失分陷阱**！本题变量 $x$ 在积分**下限**而不是上限，求导必须带负号：$\frac{d}{dx}\int_x^a f(t)\,dt = -f(x)$。养成先改写成 $-\int_a^x$ 的习惯，彻底杜绝符号失误！

  また，与式に $x = a$ を代入すると，左辺は $\displaystyle\int_a^a f(t)\,dt = 0$ であるから，
  $$0 = a^3 - 3a \iff a(a^2 - 3) = 0 \iff a = 0,\; \pm\sqrt{3}$$
- **【最终答案】**
  **$f(x) = -3x^2 + 3,\qquad a = 0,\; \pm\sqrt{3}$**

---

### 演習問題 15-(3)

#### 演習問題 15-(3) [1]
- **【原题重现与翻译】**
  - 原题：次の関数を微分せよ。
    $$f(x) = \int_0^x (t - x)\sin t\,dt$$
  - 中文：对函数 $f(x) = \displaystyle\int_0^x (t - x)\sin t\,dt$ 求导。
- **【考点定位】**
  - **被积函数含参变量 $x$ 的变限积分求导**：先展开把 $x$ 提到积分号外，再用乘法求导法则。
- **【分步标准解答】**
  被積分関数を展開し，積分変数 $t$ に無関係な $x$ を積分の外に出すと，
  $$f(x) = \int_0^x t\sin t\,dt - x\int_0^x \sin t\,dt$$
  > 💡 讲师批注：**严禁直接把 $t$ 换成 $x$ 得到 $(x-x)\sin x = 0$！** 那是新手最常犯的致命错误。只要被积函数里出现了 $x$，就必须先把 $x$ 分离到积分号外面！

  両辺を $x$ で微分する（第 2 項は積の微分法を用いる）：
  $$f'(x) = x\sin x - \left(1\cdot\int_0^x \sin t\,dt + x\cdot\sin x\right)$$
  $$= x\sin x - \int_0^x \sin t\,dt - x\sin x = -\int_0^x \sin t\,dt$$
  > 💡 讲师批注：$x\sin x$ 与 $-x\sin x$ 恰好相互抵消！这正是含 $(x-t)g(t)$ 或 $(t-x)g(t)$ 卷积型积分求导的经典特征。

  残った定積分を計算すると，
  $$f'(x) = -\Bigl[-\cos t\Bigr]_0^x = \Bigl[\cos t\Bigr]_0^x = \cos x - \cos 0 = \cos x - 1$$
- **【最终答案】**
  **$f'(x) = \cos x - 1$**

---

#### 演習問題 15-(3) [2]
- **【原题重现与翻译】**
  - 原题：次の関数を微分せよ。
    $$f(x) = \int_{x^2}^{x^3} \frac{1}{\log t}\,dx \quad (x > 0) \quad \text{（※ 教材原印为 } dx \text{）}$$
  - 中文：对函数 $f(x) = \displaystyle\int_{x^2}^{x^3} \frac{1}{\log t}\,dt \quad (x > 0,\; x \neq 1)$ 求导。
  > ⚠️ **教材勘误提示**：原教材第 386 页（`page_0387.jpg`）存在两处疏漏：① 积分微元误印为 $dx$，应修正为 $dt$；② 被积函数 $\dfrac{1}{\log t}$ 在 $t = 1$ 处发散（分母为零），为使定积分有定义，需在 $x > 0$ 基础上附加条件 $x \neq 1$（即 $0 < x < 1$ 或 $x > 1$）。
- **【考点定位】**
  - 上下限均为 $x$ 的函数时的变限积分求导公式（[17.2] ②）：$\dfrac{d}{dx}\displaystyle\int_{h(x)}^{g(x)} \varphi(t)\,dt = \varphi(g(x))g'(x) - \varphi(h(x))h'(x)$。
- **【分步标准解答】**
  公式 $\dfrac{d}{dx}\displaystyle\int_{h(x)}^{g(x)} \varphi(t)\,dt = \varphi(g(x))g'(x) - \varphi(h(x))h'(x)$ を用いると，
  $$f'(x) = \frac{1}{\log(x^3)}\cdot (x^3)' - \frac{1}{\log(x^2)}\cdot (x^2)'$$
  $$= \frac{1}{3\log x}\cdot 3x^2 - \frac{1}{2\log x}\cdot 2x$$
  > 💡 讲师批注：千万别忘记乘上各自上下限的导数 $(x^3)' = 3x^2$ 与 $(x^2)' = 2x$！同时利用对数性质 $\log(x^3) = 3\log x$，$\log(x^2) = 2\log x$（因 $x > 0$），系数 $3$ 和 $2$ 完美约去！

  $$= \frac{x^2}{\log x} - \frac{x}{\log x} = \frac{x^2 - x}{\log x}$$
- **【最终答案】**
  **$f'(x) = \dfrac{x^2 - x}{\log x}$**（亦可写作 **$\dfrac{x(x - 1)}{\log x}$**）

---

### 演習問題 15-(4)

#### 演習問題 15-(4) [1]
- **【原题重现与翻译】**
  - 原题：次の等式を満たす関数 $f(x)$ を求めよ。
    $$f(x) = 3x + \int_0^\pi f(t)\sin t\,dt$$
  - 中文：求满足等式 $f(x) = 3x + \displaystyle\int_0^\pi f(t)\sin t\,dt$ 的函数 $f(x)$。
- **【考点定位】**
  - 积分方程（定积分常量型）+ 分部积分法（$\int_0^\pi t\sin t\,dt$）。
- **【分步标准解答】**
  $\displaystyle\int_0^\pi f(t)\sin t\,dt$ は定数であるから，これを $A$ とおくと，
  $$A = \int_0^\pi f(t)\sin t\,dt \quad \cdots \text{①}$$
  与式より，
  $$f(x) = 3x + A \quad \cdots \text{②}$$
  ② より $f(t) = 3t + A$ を ① に代入すると，
  $$A = \int_0^\pi (3t + A)\sin t\,dt = 3\int_0^\pi t\sin t\,dt + A\int_0^\pi \sin t\,dt$$
  ここで，2 つの定積分をそれぞれ計算する：
  - 第 1 項（部分積分法，$\sin t = (-\cos t)'$）：
    $$\int_0^\pi t\sin t\,dt = \Bigl[-t\cos t\Bigr]_0^\pi - \int_0^\pi 1\cdot(-\cos t)\,dt = \bigl(-\pi(-1) - 0\bigr) + \Bigl[\sin t\Bigr]_0^\pi = \pi + (0 - 0) = \pi$$
  - 第 2 項：
    $$\int_0^\pi \sin t\,dt = \Bigl[-\cos t\Bigr]_0^\pi = -(-1) - (-1) = 2$$
  > 💡 讲师批注：小结论建议熟记：$\int_0^\pi \sin t\,dt = 2$（正弦波半个拱的面积恒为 $2$），$\int_0^\pi t\sin t\,dt = \pi$（可用前一篇 14-(14) 的 King's Property 秒杀：$\frac{\pi}{2}\int_0^\pi \sin t\,dt = \frac{\pi}{2}\cdot 2 = \pi$！）。

  これらを代入すると，
  $$A = 3\pi + 2A \implies A = -3\pi$$
  よって ② より，
  $$f(x) = 3x - 3\pi$$
- **【最终答案】**
  **$f(x) = 3x - 3\pi$**

---

#### 演習問題 15-(4) [2]
- **【原题重现与翻译】**
  - 原题：次の等式を満たす関数 $f(x)$ を求めよ。[2] では，定数 $a$ の値も求めよ。
    $$\int_a^x (x - t)f(t)\,dt = \log x - x + 1$$
  - 中文：求满足等式 $\displaystyle\int_a^x (x - t)f(t)\,dt = \log x - x + 1$ 的函数 $f(x)$ 及常数 $a$ 的值。
- **【考点定位】**
  - **含 $(x-t)f(t)$ 的二阶积分方程**：分离变量 $x$ 后**连续求导两次**求 $f(x)$，并令 $x = a$ 求常数 $a$（且需检验原式与一阶导数式均成立）。
- **【分步标准解答】**
  右辺の対数の真数条件より $x > 0$（したがって定数 $a > 0$）。
  左辺を展開して $x$ を積分の外に出すと，
  $$x\int_a^x f(t)\,dt - \int_a^x t f(t)\,dt = \log x - x + 1 \quad \cdots \text{①}$$
  ① の両辺を $x$ で微分する（第 1 項は積の微分法を用いる）：
  $$1\cdot\int_a^x f(t)\,dt + x f(x) - x f(x) = \frac{1}{x} - 1$$
  整理すると，
  $$\int_a^x f(t)\,dt = \frac{1}{x} - 1 \quad \cdots \text{②}$$
  > 💡 讲师批注：记住规律！$\displaystyle\frac{d}{dx}\int_a^x (x - t)f(t)\,dt = \int_a^x f(t)\,dt$，再求一次导就是 $f(x)$。但在考场上务必写出展开与抵消 $xf(x)-xf(x)$ 的完整步骤，不要直接跳步！

  さらに ② の両辺を $x$ で微分すると，
  $$f(x) = \left(\frac{1}{x} - 1\right)' = -\frac{1}{x^2}$$
  また，② に $x = a$ を代入すると，左辺は $0$ となるから，
  $$0 = \frac{1}{a} - 1 \implies a = 1$$
  念のため，$a = 1$ のとき ① の両辺に $x = 1$ を代入すると，
  左辺 $= 0$，右辺 $= \log 1 - 1 + 1 = 0$ となり，確かに ① を満たす。
  > 💡 讲师批注：二阶积分方程中有**两个**初始条件（① 在 $x=a$ 为 $0$，② 在 $x=a$ 也为 $0$），从 ② 解出 $a=1$ 后，一定要代回 ① 验证 $x=a$ 时右边也为 $0$，这是严谨性的满分细节！
- **【最终答案】**
  **$f(x) = -\dfrac{1}{x^2},\qquad a = 1$**

---

### 演習問題 15-(5)
- **【原题重现与翻译】**
  - 原题：$-2 \le x \le 2$ のとき，関数 $f(x) = \displaystyle\int_0^x (1 - t^2)e^t\,dt$ の最大値・最小値と，その時の $x$ の値を求めよ。
  - 中文：当 $-2 \le x \le 2$ 时，求函数 $f(x) = \displaystyle\int_0^x (1 - t^2)e^t\,dt$ 的最大值、最小值及取最值时的 $x$ 的值。
- **【考点定位】**
  - 变限积分求导判断单调性与极值 + 分部积分法求原函数 + 闭区间最值比较（含无理数 $e$ 的大小比较）。
- **【图解辅助（SVG 矢量图）】**
  $f(x) = 1 - (x - 1)^2 e^x$ 在闭区间 $[-2, 2]$ 上的单调性与关键点示意图：

<svg viewBox="0 0 460 230" width="460" height="230" xmlns="http://www.w3.org/2000/svg" style="background:#fafafa;border:1px solid #e0e0e0;border-radius:6px;">
  <style>
    .axis { stroke: #333; stroke-width: 1.4; }
    .curve { fill: none; stroke: #2980b9; stroke-width: 2.3; }
    .dash { stroke: #95a5a6; stroke-width: 1; stroke-dasharray: 3,3; }
    .pt { fill: #e74c3c; stroke: #fff; stroke-width: 1.5; }
    .pt-max { fill: #27ae60; stroke: #fff; stroke-width: 1.5; }
    .lbl { font: 12px sans-serif; fill: #2c3e50; }
    .math { font: italic 13px serif; fill: #2c3e50; }
    .note { font: bold 11px sans-serif; }
  </style>
  <!-- Origin O at (220, 75), x scale: 80px=1, y scale: 18px=1 -->
  <!-- x=-2 -> 60, y = 1 - 9/e^2 ≈ -0.22 -> 75 + 4 = 79 -->
  <!-- x=-1 -> 140, y = 1 - 4/e ≈ -0.47 -> 75 + 8.5 = 83.5 -->
  <!-- x=0 -> 220, y = 0 -> 75 -->
  <!-- x=1 -> 300, y = 1 -> 57 -->
  <!-- x=2 -> 380, y = 1 - e^2 ≈ -6.39 -> 75 + 115 = 190 -->
  <!-- Axes -->
  <line x1="25" y1="75" x2="430" y2="75" class="axis"/>
  <polygon points="430,75 422,71 422,79" fill="#333"/>
  <text x="436" y="79" class="math">x</text>
  <line x1="220" y1="215" x2="220" y2="18" class="axis"/>
  <polygon points="220,18 216,26 224,26" fill="#333"/>
  <text x="205" y="24" class="math">y</text>

  <!-- Dashed guides -->
  <line x1="60" y1="75" x2="60" y2="79" class="dash"/>
  <line x1="140" y1="75" x2="140" y2="84" class="dash"/>
  <line x1="300" y1="75" x2="300" y2="57" class="dash"/>
  <line x1="220" y1="57" x2="300" y2="57" class="dash"/>
  <line x1="380" y1="75" x2="380" y2="190" class="dash"/>
  <line x1="220" y1="190" x2="380" y2="190" class="dash"/>

  <!-- Curve y = 1 - (x-1)^2 e^x -->
  <path d="M 60 79 C 90 83, 120 84, 140 84 C 175 84, 200 79, 220 75 C 255 68, 280 57, 300 57 C 330 57, 355 110, 380 190" class="curve"/>

  <!-- Key points -->
  <circle cx="60" cy="79" r="4" fill="#2980b9"/>
  <circle cx="140" cy="84" r="4" fill="#e67e22"/>
  <circle cx="220" cy="75" r="3" fill="#333"/>
  <circle cx="300" cy="57" r="5" class="pt-max"/>
  <circle cx="380" cy="190" r="5" class="pt"/>

  <!-- X-axis ticks & labels -->
  <text x="52" y="68" class="lbl">-2</text>
  <text x="132" y="68" class="lbl">-1</text>
  <text x="206" y="90" class="lbl">O</text>
  <text x="296" y="90" class="lbl">1</text>
  <text x="376" y="68" class="lbl">2</text>

  <!-- Point annotations -->
  <text x="42" y="102" class="lbl" font-size="11">f(-2)≈-0.22</text>
  <text x="112" y="106" class="lbl" font-size="11" fill="#d35400">極小 f(-1)=1-4/e</text>
  <text x="275" y="42" class="note" fill="#27ae60">最大値 f(1) = 1</text>
  <text x="260" y="205" class="note" fill="#c0392b">最小値 f(2) = 1 - e² ≈ -6.39</text>
  <text x="205" y="61" class="lbl">1</text>
</svg>

- **【分步标准解答】**
  $f(x)$ を $x$ で微分すると，
  $$f'(x) = (1 - x^2)e^x = -(x + 1)(x - 1)e^x$$
  $e^x > 0$ であるから，$f'(x) = 0$ となるのは $x = -1, 1$ のとき。
  $-2 \le x \le 2$ における $f(x)$ の増減表は次のようになる：

  | $x$ | $-2$ | $\cdots$ | $-1$ | $\cdots$ | $1$ | $\cdots$ | $2$ |
  | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
  | $f'(x)$ | | $-$ | $0$ | $+$ | $0$ | $-$ | |
  | $f(x)$ | $f(-2)$ | $\searrow$ | 極小 $f(-1)$ | $\nearrow$ | 極大 $f(1)$ | $\searrow$ | $f(2)$ |

  > 💡 讲师批注：求最值不需要逐个区间重新积分！先用分部积分把 $f(x)$ 的显式表达式算出来，再代入 4 个候选点 $-2, -1, 1, 2$ 即可。

  ここで，部分積分法を用いて $f(x)$ を計算する：
  $$f(x) = \int_0^x (1 - t^2)(e^t)'\,dt = \Bigl[(1 - t^2)e^t\Bigr]_0^x - \int_0^x (-2t)e^t\,dt$$
  $$= (1 - x^2)e^x - 1 + 2\int_0^x t(e^t)'\,dt$$
  $$= (1 - x^2)e^x - 1 + 2\left\{\Bigl[t e^t\Bigr]_0^x - \int_0^x e^t\,dt\right\}$$
  $$= (1 - x^2)e^x - 1 + 2\Bigl\{x e^x - (e^x - 1)\Bigr\}$$
  $$= (-x^2 + 2x - 1)e^x + 1 = 1 - (x - 1)^2 e^x$$
  > 💡 讲师批注：求导验证一下：$\bigl(1 - (x-1)^2 e^x\bigr)' = -\bigl(2(x-1) + (x-1)^2\bigr)e^x = -(x-1)(x+1)e^x = (1-x^2)e^x$，且 $f(0) = 1 - 1 = 0$，100% 精准！

  これより各点の値を求める：
  - $f(-2) = 1 - (-3)^2 e^{-2} = 1 - \dfrac{9}{e^2}$
  - $f(-1) = 1 - (-2)^2 e^{-1} = 1 - \dfrac{4}{e}$
  - $f(1) = 1 - 0 = 1$
  - $f(2) = 1 - 1^2 e^2 = 1 - e^2$

  **① 最大値の比較**：$f(-2) = 1 - \dfrac{9}{e^2} < 1 = f(1)$ であるから，最大値は **$x = 1$ のとき $1$**。
  **② 最小値の比較**：$f(-1)$ と $f(2)$ の大小を比較する。
  $$f(-1) - f(2) = \left(1 - \frac{4}{e}\right) - (1 - e^2) = e^2 - \frac{4}{e} = \frac{e^3 - 4}{e}$$
  ここで $e > 2$ より $e^3 > 8 > 4$ であるから，$f(-1) - f(2) > 0$，すなわち $f(2) < f(-1)$。
  ゆえに，最小値は **$x = 2$ のとき $1 - e^2$**。
- **【最终答案】**
  **最大値：$1$（$x = 1$ のとき），最小値：$1 - e^2$（$x = 2$ のとき）**

---

### 演習問題 15-(6)
- **【原题重现与翻译】**
  - 原题：定積分 $I(a) = \displaystyle\int_0^1 \left(\sin\frac{\pi}{2}x - ax\right)^2 dx$ を求めよ、また $I(a)$ の値を最小にする $a$ の値 $I$ を求め、その時の積分値を求めよ。
  - 中文：求定积分 $I(a) = \displaystyle\int_0^1 \left(\sin\frac{\pi}{2}x - ax\right)^2 dx$；再求使 $I(a)$ 取得最小值的 $a$ 的值，以及此时的积分值。
  > ⚠️ **教材勘误提示**：原教材第 387 页（`page_0388.jpg`）题干中「$a$ の値 $I$ を求め」中的字符「$I$」为多余印刷错误，应为「$a$ の値を求め」。
- **【考点定位】**
  - 含参定积分展开为参数 $a$ 的二次函数 + 倍角公式降次积分 + 分部积分法 + 配方求二次函数最小值（最小二乘法思想）。
- **【分步标准解答】**
  被積分関数を展開して $a$ の多項式として整理する：
  $$I(a) = \int_0^1 \left(\sin^2\frac{\pi}{2}x - 2ax\sin\frac{\pi}{2}x + a^2 x^2\right)dx$$
  $$= a^2\int_0^1 x^2\,dx - 2a\int_0^1 x\sin\frac{\pi}{2}x\,dx + \int_0^1 \sin^2\frac{\pi}{2}x\,dx$$
  > 💡 讲师批注：把与积分变量 $x$ 无关的参数 $a^2, -2a$ 提到积分号外，3 个定积分全是纯数字，思路瞬间清晰！

  それぞれの定積分を計算する：
  1. $\displaystyle\int_0^1 x^2\,dx = \left[\frac{1}{3}x^3\right]_0^1 = \frac{1}{3}$
  2. $\displaystyle\int_0^1 x\sin\frac{\pi}{2}x\,dx$（部分積分法，$\sin\dfrac{\pi}{2}x = \left(-\dfrac{2}{\pi}\cos\dfrac{\pi}{2}x\right)'$）：
     $$\int_0^1 x\sin\frac{\pi}{2}x\,dx = \left[-\frac{2}{\pi}x\cos\frac{\pi}{2}x\right]_0^1 - \int_0^1 1\cdot\left(-\frac{2}{\pi}\cos\frac{\pi}{2}x\right)dx$$
     $$= (0 - 0) + \frac{2}{\pi}\left[\frac{2}{\pi}\sin\frac{\pi}{2}x\right]_0^1 = \frac{4}{\pi^2}(1 - 0) = \frac{4}{\pi^2}$$
  3. $\displaystyle\int_0^1 \sin^2\frac{\pi}{2}x\,dx$（半角の公式 $\sin^2\theta = \dfrac{1 - \cos 2\theta}{2}$）：
     $$\int_0^1 \sin^2\frac{\pi}{2}x\,dx = \int_0^1 \frac{1 - \cos\pi x}{2}\,dx = \left[\frac{1}{2}x - \frac{1}{2\pi}\sin\pi x\right]_0^1 = \frac{1}{2} - 0 = \frac{1}{2}$$

  これらを代入すると，
  $$I(a) = \frac{1}{3}a^2 - \frac{8}{\pi^2}a + \frac{1}{2}$$
  次に，$a$ について平方完成すると，
  $$I(a) = \frac{1}{3}\left(a^2 - \frac{24}{\pi^2}a\right) + \frac{1}{2} = \frac{1}{3}\left(a - \frac{12}{\pi^2}\right)^2 - \frac{1}{3}\cdot\frac{144}{\pi^4} + \frac{1}{2}$$
  $$= \frac{1}{3}\left(a - \frac{12}{\pi^2}\right)^2 + \frac{1}{2} - \frac{48}{\pi^4}$$
  > 💡 讲师批注：验算合理性！原积分被积函数是平方形式，最小值必大于 $0$。因为 $\pi^4 \approx 97.4$，所以 $\frac{1}{2} - \frac{48}{\pi^4} \approx 0.5 - 0.493 = 0.007 > 0$，数值极其合理（说明直线 $y = \frac{12}{\pi^2}x$ 极度逼近曲线 $y = \sin\frac{\pi}{2}x$）！

  したがって，$I(a)$ は $a = \dfrac{12}{\pi^2}$ のとき最小となり，その最小値は $\dfrac{1}{2} - \dfrac{48}{\pi^4}$ である。
- **【最终答案】**
  **$I(a) = \dfrac{1}{3}a^2 - \dfrac{8}{\pi^2}a + \dfrac{1}{2}$**；**$a = \dfrac{12}{\pi^2}$ のとき最小値 $\dfrac{1}{2} - \dfrac{48}{\pi^4}$**

---

### 演習問題 15-(7)
- **【原题重现与翻译】**
  - 原题：実数 $t$ が $1 \le t \le e$ の範囲を動くとき，$S(t) = \displaystyle\int_0^1 |e^x - t|\,dx$ の最大値・最小値を求めよ。
  - 中文：当实数 $t$ 在 $1 \le t \le e$ 范围内变动时，求 $S(t) = \displaystyle\int_0^1 |e^x - t|\,dx$ 的最大值与最小值。
- **【考点定位】**
  - **含参数绝对值定积分的最值**：找零点 $x = \log t$ 分段去绝对值 $\to$ 算出 $S(t)$ $\to$ 对 $t$ 求导列表求闭区间最值。
- **【图解辅助（SVG 矢量图）】**
  $S(t) = \displaystyle\int_0^1 |e^x - t|\,dx$ 表示曲线 $y = e^x$ 与水平直线 $y = t$（$1 \le t \le e$）在 $[0, 1]$ 上围成的两块阴影面积之和：

<svg viewBox="0 0 430 245" width="430" height="245" xmlns="http://www.w3.org/2000/svg" style="background:#fafafa;border:1px solid #e0e0e0;border-radius:6px;">
  <style>
    .axis { stroke: #333; stroke-width: 1.4; }
    .curve { fill: none; stroke: #2c3e50; stroke-width: 2.3; }
    .hline { stroke: #e74c3c; stroke-width: 1.8; }
    .dash { stroke: #7f8c8d; stroke-width: 1.1; stroke-dasharray: 4,3; }
    .areaL { fill: rgba(52, 152, 219, 0.28); }
    .areaR { fill: rgba(230, 126, 34, 0.28); }
    .lbl { font: 12px sans-serif; fill: #2c3e50; }
    .math { font: italic 13px serif; fill: #2c3e50; }
  </style>
  <!-- Origin at (70, 205), x scale: 260px=1 (x=1 at 330), y scale: 58px=1 (y=1 at 147, y=e=2.718 at 47.3) -->
  <!-- Take t = 1.65 (sqrt(e)): y_t = 205 - 95.7 = 109.3, x = log t = 0.5 -> 200 -->
  <!-- Left shaded area: between y=t (109.3) and y=e^x from x=0 (70,147) to x=0.5 (200,109.3) -->
  <path d="M 70 109.3 L 200 109.3 Q 135 132 70 147 Z" class="areaL"/>
  <!-- Right shaded area: between y=e^x and y=t (109.3) from x=0.5 (200,109.3) to x=1 (330,47.3) -->
  <path d="M 200 109.3 Q 270 84 330 47.3 L 330 109.3 Z" class="areaR"/>

  <!-- Axes -->
  <line x1="35" y1="205" x2="395" y2="205" class="axis"/>
  <polygon points="395,205 387,201 387,209" fill="#333"/>
  <text x="401" y="209" class="math">x</text>
  <line x1="70" y1="225" x2="70" y2="18" class="axis"/>
  <polygon points="70,18 66,26 74,26" fill="#333"/>
  <text x="55" y="24" class="math">y</text>

  <!-- Vertical line x=1 and x=log t -->
  <line x1="330" y1="47.3" x2="330" y2="205" class="dash"/>
  <line x1="200" y1="109.3" x2="200" y2="205" class="dash"/>
  <line x1="70" y1="47.3" x2="330" y2="47.3" class="dash"/>

  <!-- Horizontal line y = t -->
  <line x1="55" y1="109.3" x2="365" y2="109.3" class="hline"/>
  <text x="370" y="113" class="math" fill="#c0392b">y = t</text>

  <!-- Curve y = e^x -->
  <path d="M 55 151 L 70 147 Q 135 132 200 109.3 Q 270 84 330 47.3 L 348 34" class="curve"/>
  <text x="352" y="34" class="math">y = eˣ</text>

  <!-- Intersection dot -->
  <circle cx="200" cy="109.3" r="4" fill="#c0392b"/>

  <!-- Axis labels -->
  <text x="54" y="220" class="lbl">O</text>
  <text x="187" y="222" class="math">log t</text>
  <text x="326" y="222" class="lbl">1</text>
  <text x="56" y="151" class="lbl">1</text>
  <text x="56" y="113" class="math" fill="#c0392b">t</text>
  <text x="56" y="51" class="math">e</text>

  <!-- Region labels -->
  <text x="115" y="125" class="lbl" fill="#2980b9" font-weight="bold">t - eˣ</text>
  <text x="282" y="96" class="lbl" fill="#d35400" font-weight="bold">eˣ - t</text>
</svg>

- **【分步标准解答】**
  $0 \le x \le 1$ において $e^x$ は単調増加であり，$1 \le e^x \le e$ を満たす。
  条件 $1 \le t \le e$ より，$e^x = t$ を満たす $x$ は $x = \log t$ であり，$0 \le \log t \le 1$ である。
  したがって，
  - $0 \le x \le \log t$ のとき：$e^x \le t$ より $|e^x - t| = t - e^x$
  - $\log t \le x \le 1$ のとき：$e^x \ge t$ より $|e^x - t| = e^x - t$

  よって，積分区間を $x = \log t$ で分けて計算すると，
  $$S(t) = \int_0^{\log t} (t - e^x)\,dx + \int_{\log t}^1 (e^x - t)\,dx$$
  $$= \Bigl[tx - e^x\Bigr]_0^{\log t} + \Bigl[e^x - tx\Bigr]_{\log t}^1$$
  > 💡 讲师批注：注意本题积分变量是 $x$，而 $t$ 是常数！积分时 $t$ 的原函数是 $tx$，千万不要误写成 $\frac{1}{2}t^2$！

  $$= \bigl(t\log t - e^{\log t}\bigr) - (0 - e^0) + (e^1 - t) - \bigl(e^{\log t} - t\log t\bigr)$$
  $e^{\log t} = t$ を用いて整理すると，
  $$S(t) = (t\log t - t) + 1 + (e - t) - (t - t\log t) = 2t\log t - 3t + e + 1$$
  > 💡 讲师批注：端点快速验算：$t=1$ 时原式 $\int_0^1 (e^x-1)\,dx = e-2$，公式 $S(1) = -3+e+1 = e-2$；$t=e$ 时原式 $\int_0^1 (e-e^x)\,dx = 1$，公式 $S(e) = 2e-3e+e+1 = 1$，完全正确！

  $S(t)$ を $t$ で微分すると，
  $$S'(t) = 2\left(1\cdot\log t + t\cdot\frac{1}{t}\right) - 3 = 2\log t + 2 - 3 = 2\log t - 1$$
  $S'(t) = 0$ を解くと，$\log t = \dfrac{1}{2} \iff t = \sqrt{e}$（$1 < \sqrt{e} < e$）。
  $1 \le t \le e$ における $S(t)$ の増減表は次の通り：

  | $t$ | $1$ | $\cdots$ | $\sqrt{e}$ | $\cdots$ | $e$ |
  | :---: | :---: | :---: | :---: | :---: | :---: |
  | $S'(t)$ | | $-$ | $0$ | $+$ | |
  | $S(t)$ | $e - 2$ | $\searrow$ | 極小 $(\sqrt{e}-1)^2$ | $\nearrow$ | $1$ |

  - **最小値**：$t = \sqrt{e}$ のとき，
    $$S(\sqrt{e}) = 2\sqrt{e}\cdot\frac{1}{2} - 3\sqrt{e} + e + 1 = e - 2\sqrt{e} + 1 = (\sqrt{e} - 1)^2$$
  - **最大値**：両端の値 $S(1) = e - 2$ と $S(e) = 1$ を比較する。
    $e < 3$（$e \fallingdotseq 2.718$）より $e - 2 < 1$ であるから，最大値は $t = e$ のとき $S(e) = 1$。
  > 💡 讲师批注：有一个非常优美的几何结论值得记住——当水平线 $y=t$ 将区间 $[0, 1]$ **恰好平分**（即交点横坐标 $\log t = \frac{1}{2} \implies t = \sqrt{e}$）时，上下两块面积之和 $S(t)$ 一定取得**最小值**！这是因为 $S'(t) = \log t - (1 - \log t)$。
- **【最终答案】**
  **最大値：$1$（$t = e$ のとき），最小値：$e - 2\sqrt{e} + 1$（$= (\sqrt{e} - 1)^2$，$t = \sqrt{e}$ のとき）**

---

### [18.2] 定積分と不等式（几何直观图解）

在闭区间 $[a, b]$（$a < b$）上，若连续函数满足 $f(x) \ge g(x)$，则：
$$\int_a^b f(x)\,dx \ge \int_a^b g(x)\,dx$$
等号当且仅当在 $[a, b]$ 上恒有 $f(x) = g(x)$ 时成立。

- **【图解辅助（SVG 矢量图）】**
  当 $f(x) \ge g(x) \ge 0$ 时，上方曲线 $y = f(x)$ 下的面积不小于下方曲线 $y = g(x)$ 下的面积：

<svg viewBox="0 0 380 210" width="380" height="210" xmlns="http://www.w3.org/2000/svg" style="background:#fafafa;border:1px solid #e0e0e0;border-radius:6px;">
  <style>
    .axis { stroke: #333; stroke-width: 1.4; }
    .curveF { fill: none; stroke: #2980b9; stroke-width: 2.2; }
    .curveG { fill: none; stroke: #e67e22; stroke-width: 2.2; }
    .areaF { fill: rgba(52, 152, 219, 0.16); }
    .areaG { fill: rgba(230, 126, 34, 0.28); }
    .dash { stroke: #555; stroke-width: 1.1; }
    .lbl { font: 12px sans-serif; fill: #2c3e50; }
    .math { font: italic 13px serif; fill: #2c3e50; }
  </style>
  <!-- Area under f(x) -->
  <path d="M 110 175 L 110 70 Q 200 32 290 50 L 290 175 Z" class="areaF"/>
  <!-- Area under g(x) -->
  <path d="M 110 175 L 110 142 Q 205 140 290 102 L 290 175 Z" class="areaG"/>
  <!-- Axes -->
  <line x1="30" y1="175" x2="355" y2="175" class="axis"/>
  <polygon points="355,175 347,171 347,179" fill="#333"/>
  <text x="360" y="179" class="math">x</text>
  <line x1="65" y1="198" x2="65" y2="16" class="axis"/>
  <polygon points="65,16 61,24 69,24" fill="#333"/>
  <text x="50" y="22" class="math">y</text>
  <!-- Vertical bounds -->
  <line x1="110" y1="70" x2="110" y2="175" class="dash"/>
  <line x1="290" y1="50" x2="290" y2="175" class="dash"/>
  <!-- Curves -->
  <path d="M 80 86 Q 190 30 330 56" class="curveF"/>
  <path d="M 80 144 Q 205 144 330 78" class="curveG"/>
  <!-- Labels -->
  <text x="50" y="191" class="lbl">O</text>
  <text x="106" y="192" class="math">a</text>
  <text x="286" y="192" class="math">b</text>
  <text x="200" y="34" class="math" fill="#2980b9">y = f(x)</text>
  <text x="180" y="118" class="math" fill="#d35400">y = g(x)</text>
  <text x="200" y="160" class="lbl" text-anchor="middle" fill="#d35400">∫ₐᵇ g(x)dx</text>
  <text x="200" y="88" class="lbl" text-anchor="middle" fill="#2980b9">∫ₐᵇ {f(x)-g(x)}dx ≥ 0</text>
</svg>

---

### [18.1] 解説(1) [例]（区分求积法经典例题）
- **【原题重现与翻译】**
  - 原题：定積分 $\displaystyle\int_0^1 x^2\,dx$ について，区間 $[0, 1]$ を $n$ 等分した長方形の面積の和 $S_n$（左端点和）と $T_n$（右端点和）を求め，極限から $\displaystyle\int_0^1 x^2\,dx = \lim_{n\to\infty} S_n = \lim_{n\to\infty} T_n = \frac{1}{3}$ であることを確かめよ。
  - 中文：对于定积分 $\displaystyle\int_0^1 x^2\,dx$，将区间 $[0, 1]$ $n$ 等分，求内接矩形面积和 $S_n$（左端点和）与外接矩形面积和 $T_n$（右端点和），并取极限验证 $\displaystyle\int_0^1 x^2\,dx = \lim_{n\to\infty} S_n = \lim_{n\to\infty} T_n = \frac{1}{3}$。
- **【考点定位】**
  - **区分求积法（定积分的黎曼和定义）** + 自然数平方和公式 $\displaystyle\sum_{k=1}^m k^2 = \frac{1}{6}m(m+1)(2m+1)$ + 夹逼思想。
- **【图解辅助（SVG 矢量图）】**
  将区间 $[0, 1]$ $n$ 等分后，蓝色内接矩形和 $S_n$ 与红色外接矩形和 $T_n$ 在 $n \to \infty$ 时共同逼近曲边梯形面积 $\displaystyle\int_0^1 x^2\,dx = \frac{1}{3}$：

<svg viewBox="0 0 540 220" width="540" height="220" xmlns="http://www.w3.org/2000/svg" style="background:#fafafa;border:1px solid #e0e0e0;border-radius:6px;">
  <style>
    .axis { stroke: #333; stroke-width: 1.4; }
    .curve { fill: none; stroke: #2c3e50; stroke-width: 2.2; }
    .inner { fill: rgba(52, 152, 219, 0.35); stroke: #2980b9; stroke-width: 1; }
    .outer { fill: rgba(231, 76, 60, 0.22); stroke: #c0392b; stroke-width: 1; stroke-dasharray: 2,2; }
    .exact { fill: rgba(52, 152, 219, 0.3); }
    .lbl { font: 11px sans-serif; fill: #2c3e50; }
    .math { font: italic 13px serif; fill: #2c3e50; }
    .title { font: bold 12px sans-serif; fill: #2c3e50; text-anchor: middle; }
  </style>
  <!-- Left panel: n=4 subdivision of y=x^2 on [0,1] -->
  <!-- Origin (50, 180), x: 160px=1 (step 40), y: 130px=1 -->
  <text x="130" y="20" class="title">区間 [0, 1] を n 等分（Sₙ &lt; 面積 &lt; Tₙ）</text>
  <!-- Outer (upper) rectangles T_n: k=1..4, height (k/4)^2 * 130 -->
  <!-- k=1: h=8.125; k=2: h=32.5; k=3: h=73.125; k=4: h=130 -->
  <rect x="50" y="171.9" width="40" height="8.1" class="outer"/>
  <rect x="90" y="147.5" width="40" height="32.5" class="outer"/>
  <rect x="130" y="106.9" width="40" height="73.1" class="outer"/>
  <rect x="170" y="50" width="40" height="130" class="outer"/>
  <!-- Inner (lower) rectangles S_n: k=0..3 -->
  <rect x="90" y="171.9" width="40" height="8.1" class="inner"/>
  <rect x="130" y="147.5" width="40" height="32.5" class="inner"/>
  <rect x="170" y="106.9" width="40" height="73.1" class="inner"/>

  <!-- Left Axes -->
  <line x1="25" y1="180" x2="240" y2="180" class="axis"/>
  <polygon points="240,180 232,176 232,184" fill="#333"/>
  <text x="244" y="184" class="math">x</text>
  <line x1="50" y1="202" x2="50" y2="32" class="axis"/>
  <polygon points="50,32 46,40 54,40" fill="#333"/>
  <text x="36" y="38" class="math">y</text>

  <!-- Curve y=x^2: M 50 180 Q 130 180 210 50 -->
  <path d="M 50 180 Q 130 180 210 50 L 220 33" class="curve"/>
  <text x="195" y="38" class="math">y = x²</text>
  <text x="36" y="194" class="lbl">O</text>
  <text x="83" y="196" class="lbl">1/n</text>
  <text x="123" y="196" class="lbl">2/n</text>
  <text x="160" y="196" class="lbl">…</text>
  <text x="206" y="196" class="lbl">1</text>
  <text x="36" y="54" class="lbl">1</text>

  <!-- Arrow n -> infinity -->
  <line x1="262" y1="115" x2="312" y2="115" stroke="#2c3e50" stroke-width="2"/>
  <polygon points="315,115 305,110 305,120" fill="#2c3e50"/>
  <text x="288" y="106" class="math" text-anchor="middle">n → ∞</text>

  <!-- Right panel: exact integral -->
  <text x="425" y="20" class="title">極限＝定積分 ∫₀¹ x²dx = 1/3</text>
  <!-- Shaded area under y=x^2 from x=350 to 490 (width 140), y=180 to 50 -->
  <path d="M 350 180 Q 420 180 490 50 L 490 180 Z" class="exact"/>
  <line x1="325" y1="180" x2="520" y2="180" class="axis"/>
  <polygon points="520,180 512,176 512,184" fill="#333"/>
  <text x="524" y="184" class="math">x</text>
  <line x1="350" y1="202" x2="350" y2="32" class="axis"/>
  <polygon points="350,32 346,40 354,40" fill="#333"/>
  <text x="336" y="38" class="math">y</text>
  <path d="M 350 180 Q 420 180 490 50 L 498 35" class="curve"/>
  <line x1="490" y1="50" x2="490" y2="180" stroke="#555" stroke-dasharray="3,2"/>
  <text x="480" y="38" class="math">y = x²</text>
  <text x="336" y="194" class="lbl">O</text>
  <text x="487" y="196" class="lbl">1</text>
  <text x="336" y="54" class="lbl">1</text>
  <text x="448" y="156" class="lbl" fill="#2980b9" font-weight="bold">面積 = 1/3</text>
</svg>

- **【分步标准解答】**
  区間 $[0, 1]$ を $n$ 等分すると，各小区間の幅は $\dfrac{1}{n}$，分点は $\dfrac{k}{n}$（$k = 0, 1, \dots, n$）となる。

  **① 青い内接長方形（左端点和）の面積の和 $S_n$**：
  各長方形の面積は $\left(\dfrac{1}{n}\right)\cdot\left(\dfrac{k}{n}\right)^2$（$k = 0, 1, \dots, n - 1$）であるから，
  $$S_n = \sum_{k=0}^{n-1} \frac{1}{n}\cdot\left(\frac{k}{n}\right)^2 = \frac{1}{n^3}\sum_{k=1}^{n-1} k^2$$
  自然数の平方和の公式 $\displaystyle\sum_{k=1}^{m} k^2 = \frac{1}{6}m(m+1)(2m+1)$ に $m = n - 1$ を適用すると，
  $$S_n = \frac{1}{n^3}\cdot\frac{1}{6}(n - 1)n(2n - 1) = \frac{1}{6}\left(1 - \frac{1}{n}\right)\left(2 - \frac{1}{n}\right) \quad \cdots \text{Ⓐ}$$

  **② 赤い外接長方形（右端点和）の面積の和 $T_n$**：
  各長方形の面積は $\left(\dfrac{1}{n}\right)\cdot\left(\dfrac{k}{n}\right)^2$（$k = 1, 2, \dots, n$）であるから，
  $$T_n = \sum_{k=1}^{n} \frac{1}{n}\cdot\left(\frac{k}{n}\right)^2 = \frac{1}{n^3}\sum_{k=1}^{n} k^2$$
  $$= \frac{1}{n^3}\cdot\frac{1}{6}n(n + 1)(2n + 1) = \frac{1}{6}\left(1 + \frac{1}{n}\right)\left(2 + \frac{1}{n}\right) \quad \cdots \text{Ⓑ}$$
  > 💡 讲师批注：注意 $S_n$ 和 $T_n$ 只差了一个最右端的高为 $1$、宽为 $\frac{1}{n}$ 的细长矩形（即 $T_n - S_n = \frac{1}{n}$）。当 $n \to \infty$ 时，这个误差 $\frac{1}{n} \to 0$，于是内接和与外接和夹逼到同一个定积分值！

  **③ 定積分の値との一致**：
  曲線 $y = x^2$ と $x$ 軸，直線 $x = 1$ で囲まれた部分の面積は，
  $$\int_0^1 x^2\,dx = \left[\frac{x^3}{3}\right]_0^1 = \frac{1}{3}$$
  また，Ⓐ，Ⓑ において $n \to \infty$ の極限をとると，
  $$\lim_{n\to\infty} S_n = \frac{1}{6}(1 - 0)(2 - 0) = \frac{1}{3}, \qquad \lim_{n\to\infty} T_n = \frac{1}{6}(1 + 0)(2 + 0) = \frac{1}{3}$$
  よって，
  $$\int_0^1 x^2\,dx = \lim_{n\to\infty} S_n = \lim_{n\to\infty} T_n = \frac{1}{3}$$
- **【最终答案】**
  **$S_n = \dfrac{1}{6}\left(1 - \dfrac{1}{n}\right)\left(2 - \dfrac{1}{n}\right),\; T_n = \dfrac{1}{6}\left(1 + \dfrac{1}{n}\right)\left(2 + \dfrac{1}{n}\right)$；$\displaystyle\int_0^1 x^2\,dx = \lim_{n\to\infty} S_n = \lim_{n\to\infty} T_n = \dfrac{1}{3}$**

---

> 👉 **本切片（P376–P390）已全部完结**：上篇 [`note_026_a.md`](./note_026_a.md)（演習問題 14 全 27 题）+ 下篇 `note_026_b.md`（演習問題 15 全 11 题 + 区分求积法例题）。下一讲义 [`note_027.md`](./note_027.md) 将继续深入区分求积法实战习题与定积分求面积专题。
