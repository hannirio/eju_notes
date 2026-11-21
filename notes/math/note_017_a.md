# 《EJU 教材全解与备课讲义》数学 017-A（P241–P249）

> **对应源文件**：`work_math/ocr_md/ocr_017_p241-255.md`（第九章《複素数平面》之「複素数の相等（演習1-(2)）」「複素数平面」「複素数の極形式と乗法、除法」）
> **视觉核对参考图**：`work_math/ref_imgs/page_0241.jpg`、`page_0242.jpg`、`page_0244.jpg`、`page_0245.jpg`、`page_0246.jpg`、`page_0247.jpg`、`page_0248.jpg`、`page_0249.jpg`
> **本切片分册说明**：本切片涵盖第九章《複素数平面》与第十章《数列》开篇，题量丰富。为保证推导完整不跳步，拆分为 `note_017_a.md`（P241–P249：复数平面与极形式）与 `note_017_b.md`（P250–P255：棣莫弗定理、单位根与等差/调和数列）。

---

## 一、国内高中基础知识点唤醒与 EJU 考纲差异对比

本分册对应日本高中理系核心课程 **数学Ⅲ（新课纲：数学C）《複素数平面》** 的前半部分，是 EJU 理系数学**高频必考大题模块**，核心在于将复数代数运算与平面几何变换（平移、对称、伸缩、旋转）完全打通。

### 1.1 复数平面与基本运算的几何意义（複素数平面）

- **复数平面（複素数平面 / ガウス平面）**：
  - 将复数 $\alpha = a + bi$（$a, b \in \mathbb{R}$）对应于坐标平面上的点 $A(a, b)$，横轴称为**实轴（実軸）**，纵轴称为**虚轴（虚軸）**。
  - 实轴上的点表示实数；虚轴上除原点 $O$ 外的点表示**纯虚数（純虚数）** $bi\ (b \neq 0)$。
- **复数的实数倍（共线条件）**：
  $$\alpha \neq 0 \text{ のとき，} 3\text{点 } 0, \alpha, \beta \text{ が一直線上にある} \iff \beta = k\alpha \quad (k \text{ は実数})$$
- **复数加减法的几何意义**：
  - 加法 $C(\alpha + \beta)$：将点 $A(\alpha)$ 沿原点 $O \to B(\beta)$ 的方向平移所得的点（以 $OA, OB$ 为邻边的平行四边形的第四个顶点）。
  - 减法 $D(\alpha - \beta)$：将点 $A(\alpha)$ 沿 $B(\beta) \to O(0)$ 的方向平移所得的点。
- **共轭复数（共役な複素数）的性质**（设 $\alpha, \beta \in \mathbb{C}$）：
  1. 实数与纯虚数判定：
     $$\alpha \text{ が実数} \iff \overline{\alpha} = \alpha, \qquad \alpha \text{ が純虚数} \iff \overline{\alpha} = -\alpha \text{ かつ } \alpha \neq 0$$
  2. 几何对称性：$\overline{\alpha}$ 与 $\alpha$ 关于**实轴对称**；$-\alpha$ 与 $\alpha$ 关于**原点对称**；$-\overline{\alpha}$ 与 $\alpha$ 关于**虚轴对称**。
  3. 运算封闭性（可穿透四则运算与自然数次幂）：
     $$\alpha + \overline{\alpha} \in \mathbb{R}, \quad \overline{\alpha \pm \beta} = \overline{\alpha} \pm \overline{\beta}, \quad \overline{\alpha\beta} = \overline{\alpha}\,\overline{\beta}, \quad \overline{\left(\frac{\alpha}{\beta}\right)} = \frac{\overline{\alpha}}{\overline{\beta}}\ (\beta \neq 0), \quad \overline{\overline{\alpha}} = \alpha, \quad \overline{\alpha^n} = (\overline{\alpha})^n$$
- **绝对值（模长）与两点间距离**：
  - 定义：$|\alpha| = |a + bi| = \sqrt{a^2 + b^2}$。
  - 核心性质：
    $$|z| = 0 \iff z = 0, \quad |z| = |-z| = |\overline{z}|, \quad z\overline{z} = |z|^2, \quad |\alpha\beta| = |\alpha||\beta|, \quad \left|\frac{\alpha}{\beta}\right| = \frac{|\alpha|}{|\beta|}\ (\beta \neq 0)$$
  - 两点 $\alpha, \beta$ 之间的距离为 $|\beta - \alpha|$。

### 1.2 复数的极形式与乘除法、旋转（極形式と乗法・除法・回転）

- **极形式（極形式）**：
  - 对非零复数 $z = a + bi$，记 $r = |z| > 0$，射线 $OP$ 与实轴正方向所成角（辐角）为 $\theta = \arg z$，则：
    $$z = r(\cos\theta + i\sin\theta) \qquad (r > 0)$$
  - 注：$z = 0$ 时辐角不确定，不定义极形式；辐角相差 $2\pi$ 的整数倍表示同一复数，通常限定主值范围为 $0 \le \theta < 2\pi$ 或 $-\pi \le \theta < \pi$。
- **乘除法的极形式法则**：
  设 $z_1 = r_1(\cos\theta_1 + i\sin\theta_1),\ z_2 = r_2(\cos\theta_2 + i\sin\theta_2)$（$r_1, r_2 > 0$），则：
  $$z_1 z_2 = r_1 r_2 \{\cos(\theta_1 + \theta_2) + i\sin(\theta_1 + \theta_2)\}, \qquad \arg(z_1 z_2) = \arg z_1 + \arg z_2$$
  $$\frac{z_1}{z_2} = \frac{r_1}{r_2}\{\cos(\theta_1 - \theta_2) + i\sin(\theta_1 - \theta_2)\}, \qquad \arg\left(\frac{z_1}{z_2}\right) = \arg z_1 - \arg z_2 \quad (z_2 \neq 0)$$
- **复数乘法的几何意义（旋转与伸缩）**：
  - 绕**原点 $O$** 旋转角 $\theta$ 并伸缩 $r$ 倍：$z' = r(\cos\theta + i\sin\theta) \cdot z$。
  - 绕**定点 $Q(\alpha)$** 旋转角 $\theta$ 并伸缩 $r$ 倍：
    $$z' - \alpha = r(\cos\theta + i\sin\theta)(z - \alpha) \iff z' = r(\cos\theta + i\sin\theta)(z - \alpha) + \alpha$$
  - 特例：乘以 $i$ 等价于绕原点逆时针旋转 $\dfrac{\pi}{2}$；乘以 $-i$ 等价于绕原点顺时针旋转 $\dfrac{\pi}{2}$。

### 1.3 国内高中 vs. 日本 EJU 考纲差异对比

| 对比维度 | 国内高中习惯 | 日本 EJU 习惯 | 备课/应试提醒 |
| :--- | :--- | :--- | :--- |
| **考核深度** | 新高考仅考复数基本四则运算与模长，**三角形式/旋转极少深入考** | **理系数学核心大题**，高频考查极形式、旋转变换、几何图形判定与轨迹 | 国内学生普遍在此模块薄弱，必须系统补强「复数几何化」思维 |
| **术语称呼** | 称「复数的模」「辐角」「三角形式」 | 称 **絶対値（ぜったいち）**、**偏角（へんかく）**、**極形式（きょくけいしき）** | 题干说「絶対値」即指模长 $|z|$，说「偏角」即指 $\arg z$ |
| **辐角主值范围** | 国内教材多约定 $[0, 2\pi)$ | EJU 题目会**明确指定** $0 \le \theta < 2\pi$ 或 $-\pi < \theta \le \pi$ | 务必读清题干对 $\theta$ 范围的限定，避免填错负角或超范围角 |
| **旋转方向陷阱** | 几何题常给图形方向 | 仅给 $\angle BAC = \dfrac{\pi}{3}$ 时**未限定顺/逆时针**，必须分 $+\dfrac{\pi}{3}$ 和 $-\dfrac{\pi}{3}$ 双解！ | 如本讲义演習問題 3-(8)，漏解是最高频失分点 |

---

## 二、日文核心词汇与公式假名注音

### 2.1 本分册日文核心词汇

- 複素数（ふくそすう / fukusosuu） — 复数
- 複素数平面（ふくそすうへいめん / fukusosuu heimen） — 复平面（亦称 複素平面 / ガウス平面）
- 実部（じつぶ / jitsubu） — 实部
- 虚部（きょぶ / kyobu） — 虚部
- 虚数単位（きょすうたんい / kyosuu tan'i） — 虚数单位（$i$）
- 実軸（じつじく / jitsujiku） — 实轴
- 虚軸（きょじく / kyojiku） — 虚轴
- 純虚数（じゅんきょすう / junkyosuu） — 纯虚数
- 実数倍（じっすうばい / jissuubai） — 实数倍（数乘）
- 共役な複素数（きょうやくなふくそすう / kyouyaku na fukusosuu） — 共轭复数（旧词复现）
- 絶対値（ぜったいち / zettaichi） — 绝对值、复数的模（旧词复现）
- 極形式（きょくけいしき / kyokukeishiki） — 极形式（复数的三角形式）
- 偏角（へんかく / henkaku） — 辐角（$\arg z$）
- 回転（かいてん / kaiten） — 旋转

### 2.2 核心公式的日本课堂口语读法

1. **共轭复数** $\overline{\alpha}$
   - 课堂读法：**アルファ バー**（alpha bar）
   - 备注：上划线在数学中统一读作 **バー（bar）**，如 $\overline{z}$ 读作「ゼット バー」。
2. **复数模的平方性质** $z\overline{z} = |z|^2$
   - 课堂读法：**ゼット かける ゼットバー イコール ぜったいち ゼット の にじょう**
3. **极形式** $z = r(\cos\theta + i\sin\theta)$
   - 课堂读法：**ゼット イコール アール かっこ コサイン シータ たす アイ サイン シータ かっことじ**
4. **辐角乘法公式** $\arg(z_1 z_2) = \arg z_1 + \arg z_2$
   - 课堂读法：**アーギュメント ゼットワン ゼットツー イコール アーギュメント ゼットワン たす アーギュメント ゼットツー**
   - 备注：$\arg$ 源自英文 argument，日本课堂常简读为 **アーグ（aagu）** 或 **アーギュメント（aagyumento）**。

---

## 三、逐题深度解析（不可跳步）

---

### 演習問題 1（複素数の相等・P241）

#### 演習問題 1-(2)
- **【原题重现与翻译】**
  - 原题：次の等式を満たす実数 $x, y$ の値を、それぞれ求めよ。
    - [1] $(4 + 2i)x + (1 + 4i)y + 7 = 0$
    - [2] $(x + 2yi)(1 + i) = 3 - 2i$
  - 中文：分别求满足下列等式的实数 $x, y$ 的值。
    - [1] $(4 + 2i)x + (1 + 4i)y + 7 = 0$
    - [2] $(x + 2yi)(1 + i) = 3 - 2i$
- **【考点定位】**
  - 复数相等的充要条件：当 $a, b, c, d \in \mathbb{R}$ 时，$a + bi = c + di \iff a = c \text{ 且 } b = d$（特别地，$a + bi = 0 \iff a = 0 \text{ 且 } b = 0$）。
- **【分步标准解答】**
  - **[1]** 左辺を実部と虚部に整理すると、
    $$(4x + y + 7) + (2x + 4y)i = 0$$
    > 💡 讲师批注：解复数相等题的第一步永远是**按实部与虚部分离合并**，写成 $(\text{実部}) + (\text{虚部})i = 0$ 的标准形式。

    $x, y$ は実数であるから、$4x + y + 7$、$2x + 4y$ も実数である。
    > 💡 讲师批注：**日本考场极其看重这一句声明！** 只有确认实部与虚部均为实数，才能令两者分别等于 $0$；若在記述式考试中漏写此句会被扣过程分。

    よって、
    $$\begin{cases} 4x + y + 7 = 0 & \cdots ① \\ 2x + 4y = 0 & \cdots ② \end{cases}$$
    ② より $x = -2y$。これを ① に代入すると、
    $$4(-2y) + y + 7 = 0 \implies -7y = -7 \implies y = 1$$
    よって $x = -2 \cdot 1 = -2$。
    > 💡 讲师批注：代入原式验算：$(4+2i)(-2) + (1+4i)(1) + 7 = (-8-4i) + (1+4i) + 7 = 0$，无误。

  - **[2]** 左辺を展開して整理すると、
    $$x + xi + 2yi + 2yi^2 = 3 - 2i$$
    $i^2 = -1$ であるから、
    $$(x - 2y) + (x + 2y)i = 3 - 2i$$
    > 💡 讲师批注：展开时务必留心 $2yi \cdot i = 2yi^2 = -2y$ 的负号，这是初学者最易算错的地方。

    $x, y$ は実数であるから、$x - 2y$、$x + 2y$ も実数である。よって、
    $$\begin{cases} x - 2y = 3 & \cdots ① \\ x + 2y = -2 & \cdots ② \end{cases}$$
    $① + ②$ より $2x = 1 \implies x = \dfrac{1}{2}$。
    $② - ①$ より $4y = -5 \implies y = -\dfrac{5}{4}$。
    > 💡 讲师批注：代入验算：$\left(\dfrac{1}{2} - \dfrac{5}{2}i\right)(1+i) = \dfrac{1}{2}(1-5i)(1+i) = \dfrac{1}{2}(6-4i) = 3-2i$，完全正确。

- **【最终答案】**
  - **[1] $x = -2,\quad y = 1$**
  - **[2] $x = \dfrac{1}{2},\quad y = -\dfrac{5}{4}$**

---

### 演習問題 2（複素数平面・共役複素数・絶対値・P244–P245）

#### 演習問題 2-(1)
- **【原题重现与翻译】**
  - 原题：$\alpha = a + 2i,\ \beta = -2 - 4i,\ r = 3 + bi$ とする。4 点 $0, \alpha, \beta, r$ が一直線上にあるとき、実数 $a, b$ の値を求めよ。
  - 中文：设 $\alpha = a + 2i,\ \beta = -2 - 4i,\ r = 3 + bi$。当 4 点 $0, \alpha, \beta, r$ 在同一直线上时，求实数 $a, b$ 的值。
  > 💡 讲师注：原教材此处将第三个复数印作拉丁字母 $r$（常规教材多写作希腊字母 $\gamma$），讲义忠实于原教材符号。
- **【考点定位】**
  - 复数平面上过原点的共线充要条件：$\beta \neq 0$ 时，$0, \alpha, \beta$ 共线 $\iff \alpha = k\beta\ (k \in \mathbb{R})$。
- **【图解辅助（SVG 矢量图）】**

<svg viewBox="0 0 360 280" width="360" height="280" xmlns="http://www.w3.org/2000/svg" style="background:#fafafa;border:1px solid #e0e0e0;border-radius:6px;">
  <defs>
    <marker id="arr1" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto">
      <path d="M0,0 L0,6 L7,3 z" fill="#333"/>
    </marker>
  </defs>
  <!-- 坐标轴 -->
  <line x1="30" y1="160" x2="330" y2="160" stroke="#333" stroke-width="1.5" marker-end="url(#arr1)"/>
  <line x1="150" y1="265" x2="150" y2="20" stroke="#333" stroke-width="1.5" marker-end="url(#arr1)"/>
  <text x="333" y="164" font-size="13" fill="#333">実軸</text>
  <text x="157" y="25" font-size="13" fill="#333">虚軸</text>
  <text x="135" y="176" font-size="13" fill="#333">O</text>
  <!-- 过原点直线 y = 2x (1单位=20px, 中心(150,160)) -->
  <!-- β(-2,-4) -> (110, 240); α(1,2) -> (170, 120); r(3,6) -> (210, 40) -->
  <line x1="95" y1="270" x2="225" y2="10" stroke="#1e88e5" stroke-width="2" stroke-dasharray="5,3"/>
  <!-- 关键点 -->
  <circle cx="150" cy="160" r="3.5" fill="#333"/>
  <circle cx="110" cy="240" r="4.5" fill="#e53935"/>
  <text x="48" y="245" font-size="13" fill="#e53935" font-weight="bold">β(-2-4i)</text>
  <circle cx="170" cy="120" r="4.5" fill="#2e7d32"/>
  <text x="178" y="124" font-size="13" fill="#2e7d32" font-weight="bold">α(1+2i)</text>
  <circle cx="210" cy="40" r="4.5" fill="#6a1b9a"/>
  <text x="218" y="44" font-size="13" fill="#6a1b9a" font-weight="bold">r(3+6i)</text>
  <text x="235" y="100" font-size="12" fill="#1e88e5">直線 y = 2x</text>
</svg>

- **【分步标准解答】**
  $\beta = -2 - 4i \neq 0$ である。
  4 点 $0, \alpha, \beta, r$ が一直線上にあるための条件は、実数 $k, l$ を用いて
  $$\alpha = k\beta,\qquad r = l\beta$$
  と表されることである。
  > 💡 讲师批注：由于 $\beta = -2-4i$ 已经完全已知且非零，所以选 $\beta$ 作为基准向量（基准复数）最方便，直接令 $\alpha = k\beta,\ r = l\beta$ 即可。

  まず $\alpha = k\beta$ より、
  $$a + 2i = k(-2 - 4i) = -2k - 4ki$$
  $a, k$ は実数であるから、実部と虚部を比較して、
  $$\begin{cases} a = -2k \\ 2 = -4k \end{cases} \implies k = -\frac{1}{2},\quad a = -2\left(-\frac{1}{2}\right) = 1$$

  次に $r = l\beta$ より、
  $$3 + bi = l(-2 - 4i) = -2l - 4li$$
  $b, l$ は実数であるから、実部と虚部を比較して、
  $$\begin{cases} 3 = -2l \\ b = -4l \end{cases} \implies l = -\frac{3}{2},\quad b = -4\left(-\frac{3}{2}\right) = 6$$
  > 💡 讲师批注：快速验算技巧：过原点的直线满足「虚部 / 实部 = 常数」。由 $\beta = -2-4i$ 知 $\dfrac{\text{虚部}}{\text{实部}} = \dfrac{-4}{-2} = 2$，因此 $\dfrac{2}{a} = 2 \implies a = 1$，$\dfrac{b}{3} = 2 \implies b = 6$，一步秒杀验算！

- **【最终答案】**
  **$a = 1,\quad b = 6$**

---

#### 演習問題 2-(2)
- **【原题重现与翻译】**
  - 原题：$a, b, c\ (a \neq 0)$ は実数とする。5 次方程式 $ax^5 + bx^2 + c = 0$ が虚数解 $\alpha$ をもつとき、$\overline{\alpha}$ もこの方程式の解であることを示せ。
  - 中文：设 $a, b, c\ (a \neq 0)$ 为实数。证明：当 5 次方程 $ax^5 + bx^2 + c = 0$ 有虚数解 $\alpha$ 时，$\overline{\alpha}$ 也是该方程的解。
- **【考点定位】**
  - 实系数高次方程的虚根成对共轭定理；共轭复数的四则运算与乘幂性质。
- **【分步标准解答】**
  $\alpha$ は方程式 $ax^5 + bx^2 + c = 0$ の解であるから、
  $$a\alpha^5 + b\alpha^2 + c = 0$$
  が成り立つ。両辺の共役な複素数をとると、
  $$\overline{a\alpha^5 + b\alpha^2 + c} = \overline{0}$$
  > 💡 讲师批注：证明「$\overline{\alpha}$ 也是解」的标准套路是**将 $\alpha$ 代入方程 $\to$ 等式两边同时取共轭 $\to$ 利用共轭运算性质将上划线逐层拆开 $\to$ 利用实系数 $\overline{a}=a$ 去掉系数上的共轭号**。

  共役な複素数の性質より、
  $$\overline{a\alpha^5} + \overline{b\alpha^2} + \overline{c} = 0$$
  $$\overline{a}\,(\overline{\alpha})^5 + \overline{b}\,(\overline{\alpha})^2 + \overline{c} = 0$$
  ここで、$a, b, c$ は実数であるから、$\overline{a} = a,\ \overline{b} = b,\ \overline{c} = c$ である。
  > 💡 讲师批注：**核心得分点！** 必须明确写出「因为 $a, b, c$ 是实数，所以 $\overline{a}=a,\ \overline{b}=b,\ \overline{c}=c$」。若方程为虚系数方程，此结论不成立。

  したがって、
  $$a(\overline{\alpha})^5 + b(\overline{\alpha})^2 + c = 0$$
  よって、$\overline{\alpha}$ も方程式 $ax^5 + bx^2 + c = 0$ の解である。（証明終）
- **【最终答案】**
  **証明完了（如上所示，$\overline{\alpha}$ 满足 $a(\overline{\alpha})^5 + b(\overline{\alpha})^2 + c = 0$，故亦为方程的解）**

---

#### 演習問題 2-(3)
- **【原题重现与翻译】**
  - 原题：$z = 1 + i$ のとき、$\left|z + \dfrac{1}{\overline{z}}\right|$ の値を求めよ。
  - 中文：当 $z = 1 + i$ 时，求 $\left|z + \dfrac{1}{\overline{z}}\right|$ 的值。
- **【考点定位】**
  - 共轭复数、分母实数化与复数模长的计算；性质 $z\overline{z} = |z|^2$ 的灵活运用。
- **【分步标准解答】**
  - **解法一（直接代入化简）**：
    $z = 1 + i$ より、$\overline{z} = 1 - i$ である。よって、
    $$\frac{1}{\overline{z}} = \frac{1}{1 - i} = \frac{1 + i}{(1 - i)(1 + i)} = \frac{1 + i}{1 - i^2} = \frac{1 + i}{2}$$
    したがって、
    $$z + \frac{1}{\overline{z}} = (1 + i) + \frac{1 + i}{2} = \frac{3}{2}(1 + i)$$
    よって、求める値は
    $$\left|z + \frac{1}{\overline{z}}\right| = \left|\frac{3}{2}(1 + i)\right| = \frac{3}{2}|1 + i| = \frac{3}{2}\sqrt{1^2 + 1^2} = \frac{3\sqrt{2}}{2}$$
  - **解法二（巧用 $|z|^2 = z\overline{z}$，推荐！）**：
    $|z|^2 = 1^2 + 1^2 = 2$ であり、$z\overline{z} = |z|^2 = 2$ より $\dfrac{1}{\overline{z}} = \dfrac{z}{2}$ である。
    > 💡 讲师批注：在复数计算中，遇到 $\dfrac{1}{\overline{z}}$ 时立刻联想到 $\dfrac{1}{\overline{z}} = \dfrac{z}{|z|^2}$，往往能一步消去分母，避免繁琐的分母有理化！

    よって、
    $$\left|z + \frac{1}{\overline{z}}\right| = \left|z + \frac{z}{2}\right| = \left|\frac{3}{2}z\right| = \frac{3}{2}|z| = \frac{3\sqrt{2}}{2}$$
- **【最终答案】**
  **$\dfrac{3\sqrt{2}}{2}$**

---

#### 演習問題 2-(4)
- **【原题重现与翻译】**
  - 原题：2 点 $A(-1 + 5i),\ B(3 + 2i)$ の間の距離は $\square$ である。また、この 2 点から等距離にある虚軸上の点 $C$ を表す複素数は $\square$ である。
  - 中文：两点 $A(-1 + 5i),\ B(3 + 2i)$ 之间的距离为 $\square$。另外，虚轴上与这两点等距离的点 $C$ 所表示的复数为 $\square$。
- **【考点定位】**
  - 复数平面上两点间距离公式 $AB = |\beta - \alpha|$；虚轴上点的设法（$z = yi,\ y \in \mathbb{R}$）。
- **【图解辅助（SVG 矢量图）】**

<svg viewBox="0 0 360 270" width="360" height="270" xmlns="http://www.w3.org/2000/svg" style="background:#fafafa;border:1px solid #e0e0e0;border-radius:6px;">
  <defs>
    <marker id="arr2" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto">
      <path d="M0,0 L0,6 L7,3 z" fill="#333"/>
    </marker>
  </defs>
  <!-- 坐标轴: O(120, 230), 1单位=35px -->
  <line x1="30" y1="230" x2="330" y2="230" stroke="#333" stroke-width="1.5" marker-end="url(#arr2)"/>
  <line x1="120" y1="255" x2="120" y2="20" stroke="#333" stroke-width="1.5" marker-end="url(#arr2)"/>
  <text x="333" y="234" font-size="13" fill="#333">実軸</text>
  <text x="126" y="25" font-size="13" fill="#333">虚軸</text>
  <text x="104" y="245" font-size="13" fill="#333">O</text>
  <!-- A(-1,5) -> (85, 55); B(3,2) -> (225, 160); C(0, 13/6≈2.167) -> (120, 154.2) -->
  <!-- 线段 AB, CA, CB -->
  <line x1="85" y1="55" x2="225" y2="160" stroke="#1e88e5" stroke-width="2"/>
  <line x1="120" y1="154" x2="85" y2="55" stroke="#e53935" stroke-width="1.8" stroke-dasharray="4,3"/>
  <line x1="120" y1="154" x2="225" y2="160" stroke="#e53935" stroke-width="1.8" stroke-dasharray="4,3"/>
  <!-- 标注 -->
  <circle cx="85" cy="55" r="4.5" fill="#1e88e5"/>
  <text x="12" y="50" font-size="12.5" fill="#1e88e5" font-weight="bold">A(-1+5i)</text>
  <circle cx="225" cy="160" r="4.5" fill="#1e88e5"/>
  <text x="232" y="164" font-size="12.5" fill="#1e88e5" font-weight="bold">B(3+2i)</text>
  <circle cx="120" cy="154" r="4.5" fill="#e53935"/>
  <text x="126" y="146" font-size="12.5" fill="#e53935" font-weight="bold">C(13/6 i)</text>
  <text x="162" y="100" font-size="12" fill="#1e88e5">AB = 5</text>
  <text x="58" y="116" font-size="11.5" fill="#e53935">CA = CB</text>
</svg>

- **【分步标准解答】**
  2 点 $A(-1 + 5i),\ B(3 + 2i)$ の間の距離 $AB$ は、
  $$AB = |(3 + 2i) - (-1 + 5i)| = |4 - 3i| = \sqrt{4^2 + (-3)^2} = \sqrt{16 + 9} = 5$$
  > 💡 讲师批注：看到实部差 $4$、虚部差 $-3$，直接识别出「3-4-5」勾股数，秒得距离 $5$。

  次に、点 $C$ は虚軸上の点であるから、実数 $y$ を用いて $C(yi)$ とおくことができる。
  > 💡 讲师批注：虚轴上的点包含原点 $0 = 0i$，所以设成 $yi\ (y \in \mathbb{R})$ 即可完整覆盖整条虚轴（无需先假设 $y \neq 0$）。

  $AC = BC$ より $AC^2 = BC^2$ であるから、
  $$|yi - (-1 + 5i)|^2 = |yi - (3 + 2i)|^2$$
  $$|1 + (y - 5)i|^2 = |-3 + (y - 2)i|^2$$
  $$1^2 + (y - 5)^2 = (-3)^2 + (y - 2)^2$$
  展開して整理すると、
  $$1 + y^2 - 10y + 25 = 9 + y^2 - 4y + 4$$
  $$26 - 10y = 13 - 4y \implies 6y = 13 \implies y = \frac{13}{6}$$
  よって、点 $C$ を表す複素数は $\dfrac{13}{6}i$ である。
  > 💡 讲师批注：验算 $AC^2 = 1 + \left(\dfrac{13}{6}-5\right)^2 = 1 + \dfrac{289}{36} = \dfrac{325}{36}$，$BC^2 = 9 + \left(\dfrac{13}{6}-2\right)^2 = 9 + \dfrac{1}{36} = \dfrac{325}{36}$，相等！

- **【最终答案】**
  **距離：$5$，点 $C$ を表す複素数：$\dfrac{13}{6}i$**

---

#### 演習問題 2-(5)
- **【原题重现与翻译】**
  - 原题：$z, \alpha, \beta$ を複素数とする。
    - [1] $|z - 3| = |z + 3i|$ のとき、等式 $z + i\overline{z} = 0$ が成り立つことを示せ。
    - [2] $|\alpha| = |\beta| = |\alpha - \beta| = 2$ のとき、$|\alpha + \beta|$ の値を求めよ。
  - 中文：设 $z, \alpha, \beta$ 为复数。
    - [1] 当 $|z - 3| = |z + 3i|$ 时，证明等式 $z + i\overline{z} = 0$ 成立。
    - [2] 当 $|\alpha| = |\beta| = |\alpha - \beta| = 2$ 时，求 $|\alpha + \beta|$ 的值。
- **【考点定位】**
  - 复数绝对值平方展开技巧 $|w|^2 = w\overline{w}$；垂直平分线方程与平行四边形恒等式的复数表示。
- **【图解辅助（SVG 矢量图，针对 [2] 的几何直观）】**

<svg viewBox="0 0 360 240" width="360" height="240" xmlns="http://www.w3.org/2000/svg" style="background:#fafafa;border:1px solid #e0e0e0;border-radius:6px;">
  <!-- O(60, 180), A(α)=(180, 180) [长120代表2], B(β)=(120, 76) [60度], C(α+β)=(240, 76) -->
  <!-- 平行四边形 OACB -->
  <polygon points="60,180 180,180 240,76 120,76" fill="#e3f2fd" fill-opacity="0.55" stroke="#1e88e5" stroke-width="2"/>
  <!-- 对角线 AB (|α-β|=2) 与 OC (|α+β|=2√3) -->
  <line x1="180" y1="180" x2="120" y2="76" stroke="#2e7d32" stroke-width="1.8" stroke-dasharray="5,3"/>
  <line x1="60" y1="180" x2="240" y2="76" stroke="#e53935" stroke-width="2.2"/>
  <!-- 60度角弧 -->
  <path d="M 90,180 A 30,30 0 0,0 75,154" fill="none" stroke="#333" stroke-width="1.3"/>
  <text x="93" y="168" font-size="12" fill="#333">60°</text>
  <!-- 顶点标注 -->
  <circle cx="60" cy="180" r="4" fill="#333"/>
  <text x="42" y="196" font-size="13" fill="#333" font-weight="bold">O(0)</text>
  <circle cx="180" cy="180" r="4" fill="#1e88e5"/>
  <text x="176" y="198" font-size="13" fill="#1e88e5" font-weight="bold">A(α)</text>
  <circle cx="120" cy="76" r="4" fill="#1e88e5"/>
  <text x="96" y="65" font-size="13" fill="#1e88e5" font-weight="bold">B(β)</text>
  <circle cx="240" cy="76" r="4" fill="#e53935"/>
  <text x="246" y="72" font-size="13" fill="#e53935" font-weight="bold">C(α+β)</text>
  <!-- 长度标注 -->
  <text x="112" y="196" font-size="12" fill="#1e88e5">|α| = 2</text>
  <text x="58" y="122" font-size="12" fill="#1e88e5">|β| = 2</text>
  <text x="164" y="114" font-size="12" fill="#e53935" font-weight="bold">OC = |α+β| = 2√3</text>
  <text x="134" y="150" font-size="11.5" fill="#2e7d32">|α-β|=2</text>
</svg>

- **【分步标准解答】**
  - **[1]** $|z - 3| = |z + 3i|$ の両辺を 2 乗すると、
    $$|z - 3|^2 = |z + 3i|^2$$
    $|w|^2 = w\overline{w}$ を用いて展開すると、
    $$(z - 3)\overline{(z - 3)} = (z + 3i)\overline{(z + 3i)}$$
    $$(z - 3)(\overline{z} - 3) = (z + 3i)(\overline{z} - 3i)$$
    > 💡 讲师批注：展开 $\overline{z + 3i} = \overline{z} - 3i$ 时，千万别忘了给 $+3i$ 变号！

    $$z\overline{z} - 3z - 3\overline{z} + 9 = z\overline{z} - 3iz + 3i\overline{z} + 9$$
    両辺から $z\overline{z} + 9$ を引き、移項して整理すると、
    $$(3i - 3)z - (3 + 3i)\overline{z} = 0$$
    両辺を $3$ で割ると、
    $$(i - 1)z - (1 + i)\overline{z} = 0$$
    ここで $-(1 + i) = i(i - 1)$ であることに注意すると、
    $$(i - 1)(z + i\overline{z}) = 0$$
    > 💡 讲师批注：也可以两边直接除以 $(i-1)$：$\dfrac{-(1+i)}{i-1} = \dfrac{-(1+i)(-i-1)}{2} = \dfrac{(1+i)^2}{2} = i$。或者用**代数坐标法**验证：$|z-3|=|z+3i|$ 是 $(3,0)$ 与 $(0,-3)$ 的垂直平分线 $y = -x$，代入 $z = x - xi$ 立刻得 $z + i\overline{z} = (x-xi) + i(x+xi) = 0$。

    $i - 1 \neq 0$ であるから、$z + i\overline{z} = 0$ が成り立つ。（証明終）

  - **[2]** $|\alpha - \beta| = 2$ の両辺を 2 乗すると、
    $$|\alpha - \beta|^2 = 4$$
    $$(\alpha - \beta)(\overline{\alpha} - \overline{\beta}) = 4$$
    $$|\alpha|^2 - \alpha\overline{\beta} - \overline{\alpha}\beta + |\beta|^2 = 4$$
    $|\alpha| = |\beta| = 2$ より $|\alpha|^2 = |\beta|^2 = 4$ であるから、
    $$4 - (\alpha\overline{\beta} + \overline{\alpha}\beta) + 4 = 4 \implies \alpha\overline{\beta} + \overline{\alpha}\beta = 4$$
    > 💡 讲师批注：这是复数计算中的**黄金恒等式（平行四边形法则）**：$|\alpha+\beta|^2 + |\alpha-\beta|^2 = 2(|\alpha|^2 + |\beta|^2)$！考场若直接记住它，可瞬间算出 $|\alpha+\beta|^2 = 2(4+4) - 4 = 12$，再用展开式写出完整步骤。

    これを用いて $|\alpha + \beta|^2$ を計算すると、
    $$|\alpha + \beta|^2 = (\alpha + \beta)(\overline{\alpha} + \overline{\beta}) = |\alpha|^2 + (\alpha\overline{\beta} + \overline{\alpha}\beta) + |\beta|^2 = 4 + 4 + 4 = 12$$
    $|\alpha + \beta| \ge 0$ であるから、
    $$|\alpha + \beta| = \sqrt{12} = 2\sqrt{3}$$
    > 💡 讲师批注：几何验证如上图：$\triangle OAB$ 是边长为 $2$ 的正三角形，平行四边形 $OACB$ 是内角 $60^\circ$ 的菱形，长对角线 $OC = 2 \times 2\cos 30^\circ = 2\sqrt{3}$。

- **【最终答案】**
  - **[1] 証明完了（$z + i\overline{z} = 0$）**
  - **[2] $|\alpha + \beta| = 2\sqrt{3}$**

---

### 演習問題 3（極形式・乗法と除法・回転・P247–P249）

#### 演習問題 3-(1)
- **【原题重现与翻译】**
  - 原题：次の複素数を極形式で表せ。ただし、偏角 $\theta$ は $0 \le \theta < 2\pi$ とする。
    - [1] $-1 + \sqrt{3}i$
    - [2] $-2i$
    - [3] $z = \cos\dfrac{\pi}{5} + i\sin\dfrac{\pi}{5}$ のとき $2\overline{z}$
  - 中文：将下列复数化为极形式（其中辐角 $\theta$ 满足 $0 \le \theta < 2\pi$）。
    - [1] $-1 + \sqrt{3}i$
    - [2] $-2i$
    - [3] 当 $z = \cos\dfrac{\pi}{5} + i\sin\dfrac{\pi}{5}$ 时，求 $2\overline{z}$ 的极形式。
- **【考点定位】**
  - 复数的极形式转化，以及利用诱导公式将负角调整至 $[0, 2\pi)$ 范围内。
- **【分步标准解答】**
  - **[1]** 絶対値は $r = \sqrt{(-1)^2 + (\sqrt{3})^2} = 2$。
    $$-1 + \sqrt{3}i = 2\left(-\frac{1}{2} + \frac{\sqrt{3}}{2}i\right)$$
    $\cos\theta = -\dfrac{1}{2},\ \sin\theta = \dfrac{\sqrt{3}}{2}$ かつ $0 \le \theta < 2\pi$ より、$\theta = \dfrac{2}{3}\pi$。
    よって、$-1 + \sqrt{3}i = 2\left(\cos\dfrac{2}{3}\pi + i\sin\dfrac{2}{3}\pi\right)$。
  - **[2]** 絶対値は $r = |-2i| = 2$。
    $$-2i = 2(0 - i)$$
    $\cos\theta = 0,\ \sin\theta = -1$ かつ $0 \le \theta < 2\pi$ より、$\theta = \dfrac{3}{2}\pi$。
    よって、$-2i = 2\left(\cos\dfrac{3}{2}\pi + i\sin\dfrac{3}{2}\pi\right)$。
  - **[3]** $z = \cos\dfrac{\pi}{5} + i\sin\dfrac{\pi}{5}$ より、
    $$2\overline{z} = 2\left(\cos\frac{\pi}{5} - i\sin\frac{\pi}{5}\right)$$
    > 💡 讲师批注：**极形式绝对不能中间是减号！** 必须把 $\cos\theta - i\sin\theta$ 转化为 $\cos(-\theta) + i\sin(-\theta)$，再加 $2\pi$ 调整进 $0 \le \theta < 2\pi$。

    ここで $\cos(-\alpha) = \cos\alpha,\ \sin(-\alpha) = -\sin\alpha$ より、
    $$2\overline{z} = 2\left\{\cos\left(-\frac{\pi}{5}\right) + i\sin\left(-\frac{\pi}{5}\right)\right\} = 2\left\{\cos\left(2\pi - \frac{\pi}{5}\right) + i\sin\left(2\pi - \frac{\pi}{5}\right)\right\} = 2\left(\cos\frac{9}{5}\pi + i\sin\frac{9}{5}\pi\right)$$
- **【最终答案】**
  - **[1] $2\left(\cos\dfrac{2}{3}\pi + i\sin\dfrac{2}{3}\pi\right)$**
  - **[2] $2\left(\cos\dfrac{3}{2}\pi + i\sin\dfrac{3}{2}\pi\right)$**
  - **[3] $2\left(\cos\dfrac{9}{5}\pi + i\sin\dfrac{9}{5}\pi\right)$**

---

#### 演習問題 3-(2)
- **【原题重现与翻译】**
  - 原题：$\alpha = 2 + 2i,\ \beta = 1 - \sqrt{3}i$ のとき、$\alpha\beta,\ \dfrac{\alpha}{\beta}$ をそれぞれ極形式で表せ。ただし、偏角 $\theta$ は $0 \le \theta < 2\pi$ とする。
  - 中文：当 $\alpha = 2 + 2i,\ \beta = 1 - \sqrt{3}i$ 时，将 $\alpha\beta,\ \dfrac{\alpha}{\beta}$ 分别化为极形式（其中辐角 $\theta$ 满足 $0 \le \theta < 2\pi$）。
- **【考点定位】**
  - 极形式下复数的乘法（模相乘、辐角相加）与除法（模相除、辐角相减）。
- **【分步标准解答】**
  $\alpha, \beta$ をそれぞれ極形式で表すと、
  $$\alpha = 2 + 2i = 2\sqrt{2}\left(\frac{1}{\sqrt{2}} + \frac{1}{\sqrt{2}}i\right) = 2\sqrt{2}\left(\cos\frac{\pi}{4} + i\sin\frac{\pi}{4}\right)$$
  $$\beta = 1 - \sqrt{3}i = 2\left(\frac{1}{2} - \frac{\sqrt{3}}{2}i\right) = 2\left(\cos\frac{5}{3}\pi + i\sin\frac{5}{3}\pi\right)$$
  よって、
  $$\alpha\beta = (2\sqrt{2} \cdot 2)\left\{\cos\left(\frac{\pi}{4} + \frac{5}{3}\pi\right) + i\sin\left(\frac{\pi}{4} + \frac{5}{3}\pi\right)\right\} = 4\sqrt{2}\left(\cos\frac{23}{12}\pi + i\sin\frac{23}{12}\pi\right)$$
  $$\frac{\alpha}{\beta} = \frac{2\sqrt{2}}{2}\left\{\cos\left(\frac{\pi}{4} - \frac{5}{3}\pi\right) + i\sin\left(\frac{\pi}{4} - \frac{5}{3}\pi\right)\right\} = \sqrt{2}\left\{\cos\left(-\frac{17}{12}\pi\right) + i\sin\left(-\frac{17}{12}\pi\right)\right\}$$
  $0 \le \theta < 2\pi$ の範囲に直すと、$-\dfrac{17}{12}\pi + 2\pi = \dfrac{7}{12}\pi$ より、
  $$\frac{\alpha}{\beta} = \sqrt{2}\left(\cos\frac{7}{12}\pi + i\sin\frac{7}{12}\pi\right)$$
  > 💡 讲师批注：若把 $\beta$ 先写成 $2\left\{\cos\left(-\dfrac{\pi}{3}\right) + i\sin\left(-\dfrac{\pi}{3}\right)\right\}$ 计算商，则 $\dfrac{\pi}{4} - \left(-\dfrac{\pi}{3}\right) = \dfrac{7}{12}\pi$，一步就落在 $[0, 2\pi)$ 内，能减少一次加 $2\pi$ 的计算失误风险！

- **【最终答案】**
  **$\alpha\beta = 4\sqrt{2}\left(\cos\dfrac{23}{12}\pi + i\sin\dfrac{23}{12}\pi\right),\qquad \dfrac{\alpha}{\beta} = \sqrt{2}\left(\cos\dfrac{7}{12}\pi + i\sin\dfrac{7}{12}\pi\right)$**

---

#### 演習問題 3-(3)
- **【原题重现与翻译】**
  - 原题：$1 + \sqrt{3}i,\ 1 + i$ を極形式で表すことにより、$\cos\dfrac{\pi}{12},\ \sin\dfrac{\pi}{12}$ の値をそれぞれ求めよ。
  - 中文：通过将 $1 + \sqrt{3}i,\ 1 + i$ 表示为极形式，分别求 $\cos\dfrac{\pi}{12},\ \sin\dfrac{\pi}{12}$ 的值。
- **【考点定位】**
  - 复数商的两种表示法（极形式法 vs. 代数有理化法）对比实部虚部求特殊角三角函数值。
- **【分步标准解答】**
  $1 + \sqrt{3}i,\ 1 + i$ を極形式で表すと、
  $$1 + \sqrt{3}i = 2\left(\cos\frac{\pi}{3} + i\sin\frac{\pi}{3}\right),\qquad 1 + i = \sqrt{2}\left(\cos\frac{\pi}{4} + i\sin\frac{\pi}{4}\right)$$
  $\dfrac{\pi}{3} - \dfrac{\pi}{4} = \dfrac{\pi}{12}$ に注目し、商 $\dfrac{1 + \sqrt{3}i}{1 + i}$ を極形式で計算すると、
  $$\frac{1 + \sqrt{3}i}{1 + i} = \frac{2}{\sqrt{2}}\left\{\cos\left(\frac{\pi}{3} - \frac{\pi}{4}\right) + i\sin\left(\frac{\pi}{3} - \frac{\pi}{4}\right)\right\} = \sqrt{2}\left(\cos\frac{\pi}{12} + i\sin\frac{\pi}{12}\right) \quad \cdots ①$$
  一方、通常の複素数の除法で計算すると、
  $$\frac{1 + \sqrt{3}i}{1 + i} = \frac{(1 + \sqrt{3}i)(1 - i)}{(1 + i)(1 - i)} = \frac{1 - i + \sqrt{3}i - \sqrt{3}i^2}{2} = \frac{(\sqrt{3} + 1) + (\sqrt{3} - 1)i}{2} \quad \cdots ②$$
  > 💡 讲师批注：同一个复数用「极形式」和「代数形式」各算一遍再对比实部虚部，是 EJU 数学Ⅲ中求非特殊角（如 $\dfrac{\pi}{12},\ \dfrac{5\pi}{12},\ \dfrac{\pi}{8}$）三角函数值的经典压轴套路！

  ①、② の実部と虚部をそれぞれ比較して、
  $$\sqrt{2}\cos\frac{\pi}{12} = \frac{\sqrt{3} + 1}{2} \implies \cos\frac{\pi}{12} = \frac{\sqrt{3} + 1}{2\sqrt{2}} = \frac{\sqrt{6} + \sqrt{2}}{4}$$
  $$\sqrt{2}\sin\frac{\pi}{12} = \frac{\sqrt{3} - 1}{2} \implies \sin\frac{\pi}{12} = \frac{\sqrt{3} - 1}{2\sqrt{2}} = \frac{\sqrt{6} - \sqrt{2}}{4}$$
  > 💡 讲师批注：验算：$\cos^2\dfrac{\pi}{12} + \sin^2\dfrac{\pi}{12} = \dfrac{(6+2+4\sqrt{3}) + (6+2-4\sqrt{3})}{16} = 1$，且 $\cos 15^\circ > \sin 15^\circ > 0$，无误。

- **【最终答案】**
  **$\cos\dfrac{\pi}{12} = \dfrac{\sqrt{6} + \sqrt{2}}{4},\qquad \sin\dfrac{\pi}{12} = \dfrac{\sqrt{6} - \sqrt{2}}{4}$**

---

#### 演習問題 3-(4) & (5)
- **【原题重现与翻译】**
  - 原题：
    - (4) $\alpha = \dfrac{1}{\sqrt{2}}(1 + i)$ とするとき、$\alpha + i$ の絶対値と偏角 $\theta\ (0 \le \theta < 2\pi)$ を求めよ。
    - (5) (4) の結果を利用して、$\cos\dfrac{\pi}{8}$ の値を求めよ。
  - 中文：
    - (4) 设 $\alpha = \dfrac{1}{\sqrt{2}}(1 + i)$，求 $\alpha + i$ 的绝对值与辐角 $\theta\ (0 \le \theta < 2\pi)$。
    - (5) 利用 (4) 的结果，求 $\cos\dfrac{\pi}{8}$ 的值。
- **【考点定位】**
  - 单位圆上两复数相加的**菱形对角线几何法**（求辐角为两辐角平均值）；利用极形式与代数形式对比求半角三角函数值。
- **【图解辅助（SVG 矢量图）】**

<svg viewBox="0 0 340 270" width="340" height="270" xmlns="http://www.w3.org/2000/svg" style="background:#fafafa;border:1px solid #e0e0e0;border-radius:6px;">
  <defs>
    <marker id="arr3" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto">
      <path d="M0,0 L0,6 L7,3 z" fill="#333"/>
    </marker>
  </defs>
  <!-- 原点 O(100, 230), 半径 R=100 -->
  <line x1="40" y1="230" x2="300" y2="230" stroke="#333" stroke-width="1.5" marker-end="url(#arr3)"/>
  <line x1="100" y1="255" x2="100" y2="15" stroke="#333" stroke-width="1.5" marker-end="url(#arr3)"/>
  <text x="303" y="234" font-size="13" fill="#333">実軸</text>
  <text x="106" y="22" font-size="13" fill="#333">虚軸</text>
  <text x="84" y="245" font-size="13" fill="#333">O</text>
  <!-- 单位圆第一象限弧 -->
  <path d="M 200,230 A 100,100 0 0,0 100,130" fill="none" stroke="#bdbdbd" stroke-width="1.4" stroke-dasharray="4,3"/>
  <!-- A(α): 45° -> (100+70.7, 230-70.7) = (170.7, 159.3) -->
  <!-- B(i): 90° -> (100, 130) -->
  <!-- C(α+i): (170.7, 59.3) -->
  <polygon points="100,230 170.7,159.3 170.7,59.3 100,130" fill="#e8f5e9" fill-opacity="0.6" stroke="#2e7d32" stroke-width="2"/>
  <line x1="100" y1="230" x2="170.7" y2="59.3" stroke="#e53935" stroke-width="2.2"/>
  <!-- 角度弧 -->
  <path d="M 135,230 A 35,35 0 0,0 124.7,205.3" fill="none" stroke="#1e88e5" stroke-width="1.4"/>
  <text x="138" y="220" font-size="11.5" fill="#1e88e5">π/4</text>
  <path d="M 155,230 A 55,55 0 0,0 121.0,179.2" fill="none" stroke="#e53935" stroke-width="1.5"/>
  <text x="148" y="196" font-size="11.5" fill="#e53935" font-weight="bold">θ = 3π/8</text>
  <!-- 顶点标注 -->
  <circle cx="170.7" cy="159.3" r="4" fill="#2e7d32"/>
  <text x="178" y="164" font-size="12.5" fill="#2e7d32" font-weight="bold">A(α), |α|=1</text>
  <circle cx="100" cy="130" r="4" fill="#2e7d32"/>
  <text x="64" y="134" font-size="12.5" fill="#2e7d32" font-weight="bold">B(i)</text>
  <circle cx="170.7" cy="59.3" r="4.5" fill="#e53935"/>
  <text x="178" y="58" font-size="12.5" fill="#e53935" font-weight="bold">C(α+i)</text>
  <text x="178" y="75" font-size="11.5" fill="#555">ひし形 OACB の対角線</text>
</svg>

- **【分步标准解答】**
  - **(4)** まず、$\alpha + i$ を $a + bi$ の形に整理して絶対値を求める。
    $$\alpha + i = \frac{1}{\sqrt{2}} + \left(\frac{1}{\sqrt{2}} + 1\right)i$$
    よって、
    $$|\alpha + i| = \sqrt{\left(\frac{1}{\sqrt{2}}\right)^2 + \left(\frac{1}{\sqrt{2}} + 1\right)^2} = \sqrt{\frac{1}{2} + \left(\frac{1}{2} + \sqrt{2} + 1\right)} = \sqrt{2 + \sqrt{2}}$$
    > 💡 讲师批注：不要急着化简双重根号，$\sqrt{2+\sqrt{2}}$ 本身就是最简形式！

    次に偏角 $\theta$ を求める。複素数平面上で、点 $A(\alpha),\ B(i),\ C(\alpha + i)$ をとると、
    $$OA = |\alpha| = \frac{1}{\sqrt{2}}\sqrt{1^2 + 1^2} = 1,\qquad OB = |i| = 1$$
    より、四角形 $OACB$ は $OA = OB = 1$ である**ひし形（菱形）**になる。
    また、$\alpha = \cos\dfrac{\pi}{4} + i\sin\dfrac{\pi}{4}$、$i = \cos\dfrac{\pi}{2} + i\sin\dfrac{\pi}{2}$ より、$\arg\alpha = \dfrac{\pi}{4},\ \arg i = \dfrac{\pi}{2}$ である。
    ひし形の対角線 $OC$ は $\angle AOB$ を二等分するから、
    $$\theta = \arg(\alpha + i) = \frac{1}{2}\left(\frac{\pi}{4} + \frac{\pi}{2}\right) = \frac{3}{8}\pi$$
    （$0 \le \dfrac{3}{8}\pi < 2\pi$ を満たす。）
    > 💡 讲师批注：**备用代数法（和差化积）**：若不借助菱形，也可用和差化积直接推导出极形式：
    > $\alpha + i = \left(\cos\dfrac{\pi}{4}+\cos\dfrac{\pi}{2}\right) + i\left(\sin\dfrac{\pi}{4}+\sin\dfrac{\pi}{2}\right) = 2\cos\dfrac{\pi}{8}\left(\cos\dfrac{3}{8}\pi + i\sin\dfrac{3}{8}\pi\right)$。两种方法殊途同归！

  - **(5)** (4) の結果より、$\alpha + i$ の極形式は
    $$\alpha + i = \sqrt{2 + \sqrt{2}}\left(\cos\frac{3}{8}\pi + i\sin\frac{3}{8}\pi\right)$$
    一方、$\alpha + i = \dfrac{1}{\sqrt{2}} + \left(\dfrac{1}{\sqrt{2}} + 1\right)i$ であるから、虚部を比較すると、
    $$\sqrt{2 + \sqrt{2}}\sin\frac{3}{8}\pi = \frac{1}{\sqrt{2}} + 1 = \frac{2 + \sqrt{2}}{2}$$
    ここで、$\sin\dfrac{3}{8}\pi = \sin\left(\dfrac{\pi}{2} - \dfrac{\pi}{8}\right) = \cos\dfrac{\pi}{8}$ であるから、
    $$\sqrt{2 + \sqrt{2}}\cos\frac{\pi}{8} = \frac{2 + \sqrt{2}}{2}$$
    よって、
    $$\cos\frac{\pi}{8} = \frac{2 + \sqrt{2}}{2\sqrt{2 + \sqrt{2}}} = \frac{\sqrt{2 + \sqrt{2}}}{2}$$
    > 💡 讲师批注：妙用 $\dfrac{A}{\sqrt{A}} = \sqrt{A}$（此处 $A = 2 + \sqrt{2}$），一步完成分母有理化！用半角公式验算：$\cos\dfrac{\pi}{8} = \sqrt{\dfrac{1+\cos\frac{\pi}{4}}{2}} = \sqrt{\dfrac{2+\sqrt{2}}{4}} = \dfrac{\sqrt{2+\sqrt{2}}}{2}$，100% 一致！

- **【最终答案】**
  - **(4) 絶対値：$\sqrt{2 + \sqrt{2}}$，偏角：$\theta = \dfrac{3}{8}\pi$**
  - **(5) $\cos\dfrac{\pi}{8} = \dfrac{\sqrt{2 + \sqrt{2}}}{2}$**

---

#### 演習問題 3-(6)
- **【原题重现与翻译】**
  - 原题：$z = 2 - 6i$ とする。点 $z$ を、原点を中心として次の角だけ回転した点を表す複素数を求めよ。
    - [1] $\dfrac{\pi}{6}$
    - [2] $-\dfrac{\pi}{2}$
  - 中文：设 $z = 2 - 6i$。求将点 $z$ 绕原点旋转下列角度后的点所表示的复数。
    - [1] $\dfrac{\pi}{6}$
    - [2] $-\dfrac{\pi}{2}$
- **【考点定位】**
  - 绕原点旋转公式：$z' = (\cos\theta + i\sin\theta)z$。
- **【分步标准解答】**
  - **[1]** 原点を中心として $\dfrac{\pi}{6}$ だけ回転した点は、
    $$\left(\cos\frac{\pi}{6} + i\sin\frac{\pi}{6}\right)(2 - 6i) = \left(\frac{\sqrt{3}}{2} + \frac{1}{2}i\right)(2 - 6i)$$
    $$= (\sqrt{3} + i)(1 - 3i) = \sqrt{3} - 3\sqrt{3}i + i - 3i^2 = (3 + \sqrt{3}) + (1 - 3\sqrt{3})i$$
    > 💡 讲师批注：提取分母的 $\dfrac{1}{2}$ 与 $(2-6i)$ 约分为 $(1-3i)$ 再展开，可大幅减少分数运算失误！验算模长平方：$(3+\sqrt{3})^2 + (1-3\sqrt{3})^2 = 12+6\sqrt{3} + 28-6\sqrt{3} = 40 = |2-6i|^2$，旋转保模长，正确！

  - **[2]** 原点を中心として $-\dfrac{\pi}{2}$ だけ回転した点は、
    $$\left\{\cos\left(-\frac{\pi}{2}\right) + i\sin\left(-\frac{\pi}{2}\right)\right\}(2 - 6i) = (-i)(2 - 6i) = -2i + 6i^2 = -6 - 2i$$
    > 💡 讲师批注：熟记结论：绕原点逆时针转 $90^\circ$ 乘 $i$，顺时针转 $90^\circ$（即 $-\dfrac{\pi}{2}$）乘 $-i$。

- **【最终答案】**
  - **[1] $(3 + \sqrt{3}) + (1 - 3\sqrt{3})i$**
  - **[2] $-6 - 2i$**

---

#### 演習問題 3-(7)
- **【原题重现与翻译】**
  - 原题：点 $(1 - i)z$ は、点 $z$ をどのように移動した点であるか。
  - 中文：点 $(1 - i)z$ 是点 $z$ 经过怎样的变换移动得到的点？
- **【考点定位】**
  - 复数乘法 $w \cdot z$ 的几何意义（将系数 $w$ 化为极形式 $r(\cos\theta + i\sin\theta)$，读出伸缩倍数 $r$ 与旋转角 $\theta$）。
- **【分步标准解答】**
  $1 - i$ を極形式で表すと、$|1 - i| = \sqrt{1^2 + (-1)^2} = \sqrt{2}$ より、
  $$1 - i = \sqrt{2}\left(\frac{1}{\sqrt{2}} - \frac{1}{\sqrt{2}}i\right) = \sqrt{2}\left\{\cos\left(-\frac{\pi}{4}\right) + i\sin\left(-\frac{\pi}{4}\right)\right\}$$
  （偏角を $0 \le \theta < 2\pi$ とすれば $\dfrac{7}{4}\pi$。）
  > 💡 讲师批注：回答「どのように移動した点であるか（怎样移动的点）」时，必须答全三大要素：**① 旋转中心（原点を中心として）② 旋转角（角 $-\dfrac{\pi}{4}$ だけ回転し）③ 距离伸缩倍数（原点からの距離を $\sqrt{2}$ 倍した点）**，缺一不可！

- **【最终答案】**
  **点 $z$ を、原点を中心として角 $-\dfrac{\pi}{4}$（または $\dfrac{7}{4}\pi$）だけ回転し、原点からの距離を $\sqrt{2}$ 倍した点である。**（将点 $z$ 绕原点旋转 $-\dfrac{\pi}{4}$（或 $\dfrac{7}{4}\pi$），并将到原点的距离扩大为 $\sqrt{2}$ 倍所得到的点。）

---

#### 演習問題 3-(8)
- **【原题重现与翻译】**
  - 原题：複素数平面上の 3 点 $A(1 + i),\ B(3 + 4i),\ C$ について、$AB = AC,\ \angle BAC = \dfrac{\pi}{3}$ であるとき、点 $C$ を表す複素数 $z$ を求めよ。
  - 中文：复数平面上三点 $A(1 + i),\ B(3 + 4i),\ C$ 满足 $AB = AC,\ \angle BAC = \dfrac{\pi}{3}$，求点 $C$ 表示的复数 $z$。
- **【考点定位】**
  - 绕非原点定点 $A(\alpha)$ 旋转的复数公式：$z - \alpha = (\cos\theta + i\sin\theta)(\beta - \alpha)$；**正负双旋转方向讨论**。
- **【图解辅助（SVG 矢量图）】**

<svg viewBox="0 0 360 270" width="360" height="270" xmlns="http://www.w3.org/2000/svg" style="background:#fafafa;border:1px solid #e0e0e0;border-radius:6px;">
  <defs>
    <marker id="arr4" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto">
      <path d="M0,0 L0,6 L7,3 z" fill="#333"/>
    </marker>
  </defs>
  <!-- 原点 O(90, 230), 1单位=35px -->
  <line x1="25" y1="230" x2="335" y2="230" stroke="#333" stroke-width="1.5" marker-end="url(#arr4)"/>
  <line x1="90" y1="255" x2="90" y2="15" stroke="#333" stroke-width="1.5" marker-end="url(#arr4)"/>
  <text x="338" y="234" font-size="12" fill="#333">実軸</text>
  <text x="96" y="22" font-size="12" fill="#333">虚軸</text>
  <text x="76" y="245" font-size="12" fill="#333">O</text>
  <!-- A(1,1) -> (125, 195); B(3,4) -> (195, 90) -->
  <!-- C1(-0.598, 4.232) -> (69.1, 81.9); C2(4.598, 0.768) -> (250.9, 203.1) -->
  <!-- 两个等边三角形 -->
  <polygon points="125,195 195,90 69.1,81.9" fill="#e3f2fd" fill-opacity="0.45" stroke="#1e88e5" stroke-width="1.6"/>
  <polygon points="125,195 195,90 250.9,203.1" fill="#fce4ec" fill-opacity="0.45" stroke="#d81b60" stroke-width="1.6"/>
  <line x1="125" y1="195" x2="195" y2="90" stroke="#333" stroke-width="2"/>
  <!-- 旋转箭头标注 -->
  <text x="116" y="138" font-size="11.5" fill="#1e88e5" font-weight="bold">+π/3</text>
  <text x="168" y="176" font-size="11.5" fill="#d81b60" font-weight="bold">-π/3</text>
  <!-- 顶点 -->
  <circle cx="125" cy="195" r="4" fill="#333"/>
  <text x="108" y="213" font-size="12.5" fill="#333" font-weight="bold">A(1+i)</text>
  <circle cx="195" cy="90" r="4" fill="#333"/>
  <text x="202" y="88" font-size="12.5" fill="#333" font-weight="bold">B(3+4i)</text>
  <circle cx="69.1" cy="81.9" r="4.5" fill="#1e88e5"/>
  <text x="14" y="74" font-size="12" fill="#1e88e5" font-weight="bold">C₁ (逆時針)</text>
  <circle cx="250.9" cy="203.1" r="4.5" fill="#d81b60"/>
  <text x="256" y="206" font-size="12" fill="#d81b60" font-weight="bold">C₂ (順時針)</text>
</svg>

- **【分步标准解答】**
  $\alpha = 1 + i,\ \beta = 3 + 4i$ とおく。
  $AB = AC,\ \angle BAC = \dfrac{\pi}{3}$ であるから、点 $C(z)$ は、点 $B(\beta)$ を点 $A(\alpha)$ を中心として **$\dfrac{\pi}{3}$ または $-\dfrac{\pi}{3}$ だけ回転した点**である。
  > 💡 讲师批注：**最高频易错警报！** 题干只说几何角 $\angle BAC = \dfrac{\pi}{3}$，没有指定点 $A, B, C$ 的顺逆时针顺序，所以必须同时考虑 $+\dfrac{\pi}{3}$ 和 $-\dfrac{\pi}{3}$ 两种情况！

  したがって、
  $$z - \alpha = \left\{\cos\left(\pm\frac{\pi}{3}\right) + i\sin\left(\pm\frac{\pi}{3}\right)\right\}(\beta - \alpha) \quad (\text{複号同順})$$
  ここで、$\beta - \alpha = (3 + 4i) - (1 + i) = 2 + 3i$ であるから、
  $$z = (1 + i) + \left(\frac{1}{2} \pm \frac{\sqrt{3}}{2}i\right)(2 + 3i)$$
  - **[1] 回転角が $+\dfrac{\pi}{3}$ のとき**：
    $$z = (1 + i) + \left(\frac{1}{2} + \frac{\sqrt{3}}{2}i\right)(2 + 3i) = (1 + i) + \left(1 + \frac{3}{2}i + \sqrt{3}i - \frac{3\sqrt{3}}{2}\right)$$
    $$= \left(2 - \frac{3\sqrt{3}}{2}\right) + \left(\frac{5}{2} + \sqrt{3}\right)i = \frac{4 - 3\sqrt{3}}{2} + \frac{5 + 2\sqrt{3}}{2}i$$
  - **[2] 回転角が $-\dfrac{\pi}{3}$ のとき**：
    $$z = (1 + i) + \left(\frac{1}{2} - \frac{\sqrt{3}}{2}i\right)(2 + 3i) = (1 + i) + \left(1 + \frac{3}{2}i - \sqrt{3}i + \frac{3\sqrt{3}}{2}\right)$$
    $$= \left(2 + \frac{3\sqrt{3}}{2}\right) + \left(\frac{5}{2} - \sqrt{3}\right)i = \frac{4 + 3\sqrt{3}}{2} + \frac{5 - 2\sqrt{3}}{2}i$$
  > 💡 讲师批注：验算 $AC^2 = |z - \alpha|^2 = \left(1 \mp \dfrac{3\sqrt{3}}{2}\right)^2 + \left(\dfrac{3}{2} \pm \sqrt{3}\right)^2 = 1 + \dfrac{27}{4} + \dfrac{9}{4} + 3 = 13 = 2^2 + 3^2 = AB^2$，双解均准确！

- **【最终答案】**
  **$z = \dfrac{4 - 3\sqrt{3}}{2} + \dfrac{5 + 2\sqrt{3}}{2}i,\qquad \dfrac{4 + 3\sqrt{3}}{2} + \dfrac{5 - 2\sqrt{3}}{2}i$**
