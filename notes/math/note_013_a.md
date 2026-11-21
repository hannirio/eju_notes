# 《EJU 教材全解与备课讲义》数学 013（P181–P195）·上篇

> **对应源文件**：`work_math/ocr_md/ocr_013_p181-195.md`（原书 P180–P194：2次曲線と直線・曲線［続］、2次曲線の接線、2次曲線の性質・離心率と準線、2次曲線と領域、媒介変数表示）
> **视觉核对参考图**：`work_math/ref_imgs/page_0181.jpg` – `page_0195.jpg`（全 15 页逐页核对）
> **分册说明**：本切片共含 17 道综合演習問題，为保证每题推导零跳步且配齐矢量图解，拆分为 **上篇 `note_013_a.md`**（知识点总览、词汇与读法、演習問題 9–10，共 8 题）与 **下篇 `note_013_b.md`**（演習問題 11–12，共 9 题）。

---

## 一、国内高中基础知识点唤醒与 EJU 考纲差异对比

本切片对应日本高中数学 **数学Ⅲ（平面上の曲線）** 的核心后半段内容，涵盖 **二次曲线的切线、离心率与准线（统一定义）、二次曲线与不等式区域、参数方程（媒介変数表示）与摆线** 四大板块。

### 1.1 二次曲线的切线公式（2次曲線の接線）

设 $p \neq 0,\; a > 0,\; b > 0$，曲线上一点 $(x_1, y_1)$ 处的**切线方程（接線の方程式）**遵循「**半代换法则**」（$x^2 \to x_1 x,\; y^2 \to y_1 y,\; x \to \frac{x+x_1}{2},\; y \to \frac{y+y_1}{2}$）：

| 曲线类型 | 标准方程 | 曲线上点 $(x_1, y_1)$ 处的切线方程 | 斜率为 $m$ 的切线方程（速算补充） |
| :--- | :--- | :--- | :--- |
| **抛物线（放物線）** | $y^2 = 4px$ | $y_1 y = 2p(x + x_1)$ | $y = mx + \dfrac{p}{m}\ (m \neq 0)$ |
| **椭圆（楕円）** | $\dfrac{x^2}{a^2} + \dfrac{y^2}{b^2} = 1$ | $\dfrac{x_1 x}{a^2} + \dfrac{y_1 y}{b^2} = 1$ | $y = mx \pm \sqrt{a^2 m^2 + b^2}$ |
| **双曲线 ①（双曲線）** | $\dfrac{x^2}{a^2} - \dfrac{y^2}{b^2} = 1$ | $\dfrac{x_1 x}{a^2} - \dfrac{y_1 y}{b^2} = 1$ | $y = mx \pm \sqrt{a^2 m^2 - b^2}\ (a^2m^2 > b^2)$ |
| **双曲线 ②（双曲線）** | $\dfrac{x^2}{a^2} - \dfrac{y^2}{b^2} = -1$ | $\dfrac{x_1 x}{a^2} - \dfrac{y_1 y}{b^2} = -1$ | $y = mx \pm \sqrt{b^2 - a^2 m^2}\ (b^2 > a^2m^2)$ |

- **关键衍生结论（极点与极线）**：若点 $P(x_0, y_0)$ 在椭圆 $Ax^2 + By^2 = 1$ **外部**，从 $P$ 引两条切线得切点 $Q, R$，则切点弦直线 $QR$ 的方程恰好同形为 $Ax_0 x + By_0 y = 1$（见演習問題 10-(5)）。

### 1.2 二次曲线的离心率与准线（離心率と準線）

- **统一定义**：平面上到定点 $F$（**焦点**）与到不过 $F$ 的定直线 $l$（**準線**）的距离之比为正常数 $e$（**離心率**）的动点 $P$ 的轨迹，即
  $$PF : PH = e : 1 \qquad (e > 0)$$
  为二次曲线：
  - $0 < e < 1 \implies$ **椭圆（楕円）**：$\dfrac{x^2}{a^2} + \dfrac{y^2}{b^2} = 1\ (a > b > 0)$ 时，$e = \dfrac{\sqrt{a^2 - b^2}}{a}$，焦点 $(\pm ae, 0)$，对应准线 $x = \pm \dfrac{a}{e}$。
  - $e = 1 \implies$ **抛物线（放物線）**：$y^2 = 4px$ 时，焦点 $(p, 0)$，准线 $x = -p$。
  - $e > 1 \implies$ **双曲线（双曲線）**：$\dfrac{x^2}{a^2} - \dfrac{y^2}{b^2} = 1$ 时，$e = \dfrac{\sqrt{a^2 + b^2}}{a}$，焦点 $(\pm ae, 0)$，对应准线 $x = \pm \dfrac{a}{e}$。
  - 便宜上，**圆（円）** 的离心率视作 $e = 0$。

### 1.3 二次曲线与平面区域（2次曲線と領域）

利用「**原点/焦点代入检验法**」快速判断不等式所表示的平面区域：
- **抛物线**（$p > 0$）：$y^2 < 4px$ 表示包含焦点 $F(p, 0)$ 的**内部**；$y^2 > 4px$ 表示外部。
- **椭圆**（$a > b > 0$）：$\dfrac{x^2}{a^2} + \dfrac{y^2}{b^2} < 1$ 表示包含原点 $O$ 的**内部**；$> 1$ 表示外部。
- **双曲线**（$a > 0, b > 0$）：$\dfrac{x^2}{a^2} - \dfrac{y^2}{b^2} < 1$ 表示包含原点 $O$ 的**中间区域**；$> 1$ 表示包含两焦点 $F, F'$ 的**左右两翼区域**。

### 1.4 参数方程与摆线（媒介変数表示・サイクロイド）

1. **标准参数方程**：
   - 圆 $x^2 + y^2 = a^2$：$\begin{cases} x = a\cos\theta \\ y = a\sin\theta \end{cases}$
   - 抛物线 $y^2 = 4px$：$\begin{cases} x = pt^2 \\ y = 2pt \end{cases}$
   - 椭圆 $\dfrac{x^2}{a^2} + \dfrac{y^2}{b^2} = 1$：$\begin{cases} x = a\cos\theta \\ y = b\sin\theta \end{cases}$（⚠️ 注意 $\theta$ **不是** $\angle POx$，而是外接圆上对应点 $Q$ 的辐角！）
   - 双曲线 $\dfrac{x^2}{a^2} - \dfrac{y^2}{b^2} = 1$：$\begin{cases} x = \dfrac{a}{\cos\theta} \\ y = b\tan\theta \end{cases}$；双曲线 $\dfrac{x^2}{a^2} - \dfrac{y^2}{b^2} = -1$：$\begin{cases} x = a\tan\theta \\ y = \dfrac{b}{\cos\theta} \end{cases}$
2. **有理参数方程（万能公式型，除去点 $(-a, 0)$）**：
   - 圆：$x = \dfrac{a(1-t^2)}{1+t^2},\; y = \dfrac{2at}{1+t^2}$；椭圆：$x = \dfrac{a(1-t^2)}{1+t^2},\; y = \dfrac{2bt}{1+t^2}$；双曲线：$x = \dfrac{a(1+t^2)}{1-t^2},\; y = \dfrac{2bt}{1-t^2}\ (t^2 \neq 1)$。
3. **参数曲线平移**：将 $x = f(t), y = g(t)$ 沿 $x$ 轴平移 $p$、沿 $y$ 轴平移 $q$，得 $x = f(t) + p,\; y = g(t) + q$。
   > ⚠️ **教材勘误提示**：原教材第 190 页（`page_0191.jpg`）[14.3] 将「曲線 $x = f(t), y = g(t)$」误印为「$x = f(x), y = g(t)$」；[14.4] 标题将「いろいろな媒介変数表示」误印为「いろいろば媒介変数表示」。
4. **摆线（サイクロイド）**：半径为 $a$ 的圆沿 $x$ 轴无滑动滚动，圆周上定点 $P$ 的轨迹方程为：
   $$x = a(\theta - \sin\theta), \qquad y = a(1 - \cos\theta)$$
   以 $2\pi a$ 为周期重复出现拱形，无法初等消去 $\theta$。

### 1.5 国内高中 vs. 日本 EJU 考纲差异对比

| 对比维度 | 国内高中习惯 | 日本 EJU 习惯 | 备课/应试提醒 |
| :--- | :--- | :--- | :--- |
| **离心率名称** | 离心率 $e$ | **離心率（りしんりつ）** $e$ | 汉字写法完全一致，定义与公式相同 |
| **双曲线参数方程** | 常用 $x = a\sec\theta,\; y = b\tan\theta$ | **不用 $\sec\theta$**，统一写作 $x = \dfrac{a}{\cos\theta},\; y = b\tan\theta$ | 日本高中考纲几乎不使用 $\sec, \csc, \cot$ 符号 |
| **切线求法** | 常用点差法、斜率设线法 | 优先使用「**设切点 $(x_1, y_1)$ 套半代换公式**」 | 设切点法天然涵盖垂直于 $x$ 轴的切线，不易漏解 |
| **除外点检查** | 参数消元偶有忽略范围 | **极度重视軌跡的「除外点（除く）」** | 消去参数后必须反查 $x, y$ 取值范围，如圆除一点、直线取两射线 |
| **摆线（サイクロイド）** | 仅作阅读材料，高考极少考 | **数学Ⅲ高频必考曲线**，常与微积分（切线、面积、弧长）综合 | 必须背熟 $x = a(\theta - \sin\theta),\; y = a(1 - \cos\theta)$ 及拱高 $2a$、底宽 $2\pi a$ |

---

## 二、日文核心词汇与公式假名注音

### 2.1 本切片日文核心词汇

- 2次曲線（にじきょくせん / niji kyokusen） — 二次曲线（圆锥曲线）
- 楕円（だえん / daen） — 椭圆
- 双曲線（そうきょくせん / soukyokusen） — 双曲线
- 焦点（しょうてん / shouten） — 焦点
- 準線（じゅんせん / junsen） — 准线
- 離心率（りしんりつ / rishinritsu） — 离心率
- 長軸（ちょうじく / choujiku） — 长轴
- 短軸（たんじく / tanjiku） — 短轴
- 軌跡（きせき / kiseki） — 轨迹
- 領域（りょういき / ryouiki） — 区域（不等式表示的平面区域）
- 外部（がいぶ / gaibu） — 外部
- 内部（ないぶ / naibu） — 内部
- 複号同順（ふくごうどうじゅん / fukugou doujun） — 复号同顺（正负号同步取上或取下）
- 法線（ほうせん / housen） — 法线（过切点且垂直于切线的直线）
- 媒介変数（ばいかいへんすう / baikai hensuu） — 参数（媒介变量）
- 媒介変数表示（ばいかいへんすうひょうじ / baikai hensuu hyouji） — 参数方程表示（亦称 パラメータ表示）
- パラメータ（ぱらめーた / parameeta） — 参数（parameter）
- 直線群（ちょくせんぐん / chokusengun） — 直线族（直线系）
- サイクロイド（さいくろいど / saikuroido） — 摆线（旋轮线，cycloid）
- 概形（がいけい / gaikei） — 简图、大致形状

### 2.2 核心公式的日本课堂口语读法

1. **抛物线切线公式** $y_1 y = 2p(x + x_1)$
   - 课堂读法：**ワイワン ワイ イコール にピー かっこ エックス たす エックスワン かっことじ**
2. **椭圆切线公式** $\dfrac{x_1 x}{a^2} + \dfrac{y_1 y}{b^2} = 1$
   - 课堂读法：**エーのにじょう ぶんの エックスワン エックス たす ビーのにじょう ぶんの ワイワン ワイ イコール いち**
3. **离心率定义** $PF : PH = e : 1$
   - 课堂读法：**ピーエフ たい ピーエイチ イコール イー たい いち**（比号 `:` 读作 **たい（対）**）
4. **摆线参数方程** $x = a(\theta - \sin\theta),\; y = a(1 - \cos\theta)$
   - 课堂读法：**エックス イコール エー かっこ シータ ひく サインシータ かっことじ、ワイ イコール エー かっこ いち ひく コサインシータ かっことじ**
5. **复号同顺**（複号同順）
   - 课堂读法：**ふくごう どうじゅん**（意为公式中的 $\pm$ 或 $\mp$ 必须同时取上方符号，或同时取下方符号）

---

## 三、逐题深度解析（不可跳步）·上篇（演習問題 9–10）

---

### 演習問題 9（2次曲線と直線・曲線［続］）

#### 演習問題 9-(3)
- **【原题重现与翻译】**
  - 原题：双曲線 $x^2 - 2y^2 = 4$ と直線 $y = -x + k$ が異なる 2 点 $P, Q$ で交わるとき
    - $[1]$ 定数 $k$ の取りうる値の範囲を求めよ。
    - $[2]$ $[1]$ の範囲で $k$ を動かしたとき、線分 $PQ$ の中点 $M$ の軌跡を求めよ。
  - 中文：当双曲线 $x^2 - 2y^2 = 4$ 与直线 $y = -x + k$ 相交于不同的两点 $P, Q$ 时：
    - $[1]$ 求常数 $k$ 的取值范围。
    - $[2]$ 当 $k$ 在 $[1]$ 的范围内变化时，求线段 $PQ$ 的中点 $M$ 的轨迹。
- **【考点定位】**
  - 直线与双曲线的位置关系（判别式）、韦达定理（解と係数の関係）求弦中点轨迹、**轨迹的取值范围限制**。
- **【图解辅助（SVG 矢量图）】**

<svg viewBox="0 0 540 300" width="540" height="300" xmlns="http://www.w3.org/2000/svg" style="background:#fafafa;border:1px solid #e0e0e0;border-radius:6px;">
  <style>
    .axis { stroke:#333; stroke-width:1.4; }
    .asym { stroke:#95a5a6; stroke-width:1; stroke-dasharray:4,4; }
    .curve { stroke:#2980b9; stroke-width:2; fill:none; }
    .line { stroke:#27ae60; stroke-width:1.6; }
    .locus { stroke:#e74c3c; stroke-width:2.4; }
    .locus-dash { stroke:#e74c3c; stroke-width:1.2; stroke-dasharray:4,4; opacity:0.45; }
    .txt { font: 12px sans-serif; fill:#2c3e50; }
    .lbl { font: bold 12px sans-serif; fill:#c0392b; }
  </style>
  <!-- Origin at (270, 150), scale: 1 unit = 25px -->
  <line x1="20" y1="150" x2="520" y2="150" class="axis"/>
  <line x1="270" y1="15" x2="270" y2="285" class="axis"/>
  <polygon points="520,150 512,146 512,154" fill="#333"/>
  <polygon points="270,15 266,23 274,23" fill="#333"/>
  <text x="510" y="168" class="txt">x</text>
  <text x="278" y="26" class="txt">y</text>
  <text x="256" y="165" class="txt">O</text>
  <!-- Asymptotes y = ±(1/sqrt2)x -->
  <line x1="80" y1="284" x2="460" y2="16" class="asym"/>
  <line x1="80" y1="16" x2="460" y2="284" class="asym"/>
  <!-- Hyperbola x^2/4 - y^2/2 = 1 -->
  <path d="M 450,24 Q 320,115 320,150 Q 320,185 450,276" class="curve"/>
  <path d="M 90,24 Q 220,115 220,150 Q 220,185 90,276" class="curve"/>
  <!-- Sample line y = -x + 2 (k=2): passes (2,0)=(320,150) and (6,-4)=(420,250) -->
  <line x1="270" y1="100" x2="445" y2="275" class="line"/>
  <circle cx="320" cy="150" r="3.5" fill="#27ae60"/>
  <circle cx="420" cy="250" r="3.5" fill="#27ae60"/>
  <text x="324" y="142" class="txt" fill="#27ae60">P</text>
  <text x="426" y="248" class="txt" fill="#27ae60">Q</text>
  <!-- Midpoint locus y = -1/2 x, excluded |x| <= 2sqrt2 (≈ 2.83 -> 70.7px) -->
  <line x1="199" y1="115" x2="341" y2="185" class="locus-dash"/>
  <line x1="50" y1="40" x2="199" y2="115" class="locus"/>
  <line x1="341" y1="185" x2="490" y2="260" class="locus"/>
  <circle cx="199" cy="115" r="4" fill="#fff" stroke="#e74c3c" stroke-width="2"/>
  <circle cx="341" cy="185" r="4" fill="#fff" stroke="#e74c3c" stroke-width="2"/>
  <circle cx="370" cy="200" r="3.5" fill="#e74c3c"/>
  <text x="376" y="198" class="lbl">M</text>
  <text x="330" y="218" class="lbl">x &gt; 2√2</text>
  <text x="115" y="65" class="lbl">y = -1/2 x (x &lt; -2√2)</text>
  <text x="276" y="96" class="txt" fill="#27ae60">y = -x + k</text>
  <text x="395" y="42" class="txt" fill="#2980b9">x² - 2y² = 4</text>
</svg>

- **【分步标准解答】**
  **$[1]$ $k$ の取りうる値の範囲**
  直線 $y = -x + k$ を双曲線 $x^2 - 2y^2 = 4$ に代入して $y$ を消去すると、
  $$x^2 - 2(-x + k)^2 = 4$$
  $$x^2 - 2(x^2 - 2kx + k^2) = 4$$
  $$-x^2 + 4kx - 2k^2 - 4 = 0$$
  両辺に $-1$ を掛けて整理すると、
  $$x^2 - 4kx + 2k^2 + 4 = 0 \qquad \cdots \text{①}$$
  > 💡 讲师批注：双曲线与直线联立时，务必先检查二次项系数是否为 $0$（若二次项系数为 $0$，说明直线平行于渐近线，最多只有 1 个交点）。本题直线斜率为 $-1$，而双曲线渐近线为 $y = \pm \frac{1}{\sqrt{2}}x$，故二次项系数恒为 $1 \neq 0$。

  双曲線と直線が異なる 2 点で交わるための条件は、2 次方程式 ① が異なる 2 つの実数解をもつことである。① の判別式を $D$ とすると、
  $$\frac{D}{4} = (-2k)^2 - 1 \cdot (2k^2 + 4) = 4k^2 - 2k^2 - 4 = 2k^2 - 4 > 0$$
  $$k^2 > 2$$
  $$k < -\sqrt{2},\quad \sqrt{2} < k$$
  > 💡 讲师批注：验算：取 $k = 2 > \sqrt{2}$，① 为 $x^2 - 8x + 12 = 0 \Rightarrow x = 2, 6$，对应两点 $(2, 0), (6, -4)$ 均满足 $x^2 - 2y^2 = 4$。

  **$[2]$ 線分 $PQ$ の中点 $M$ の軌跡**
  2 点 $P, Q$ の $x$ 座標をそれぞれ $\alpha, \beta$ とすると、$\alpha, \beta$ は ① の 2 解であるから、解と係数の関係より
  $$\alpha + \beta = 4k$$
  線分 $PQ$ の中点を $M(X, Y)$ とすると、
  $$X = \frac{\alpha + \beta}{2} = \frac{4k}{2} = 2k \qquad \cdots \text{②}$$
  また、点 $M$ は直線 $y = -x + k$ 上にあるから、
  $$Y = -X + k = -2k + k = -k \qquad \cdots \text{③}$$
  > 💡 讲师批注：计算中点纵坐标 $Y$ 时，直接利用「中点 $M$ 必在弦所在直线 $y = -x + k$ 上」即可一步写出 $Y = -X + k = -k$，比展开 $y_1 + y_2$ 更简洁不易错。

  ②、③ から $k$ を消去する。③ より $k = -Y$ であるから、これを ② に代入して
  $$X = 2(-Y) \iff Y = -\frac{1}{2}X$$
  ここで、$[1]$ の条件 $k < -\sqrt{2},\; \sqrt{2} < k$ と ② の $X = 2k$ より、$X$ の取りうる値の範囲は
  $$X < -2\sqrt{2},\quad 2\sqrt{2} < X$$
  逆に、直線 $y = -\frac{1}{2}x$ 上の $x < -2\sqrt{2},\; 2\sqrt{2} < x$ の部分の任意の点は、$k = \frac{x}{2}$ とおけば条件を満たす。
  > 💡 讲师批注：EJU 轨迹题最高频扣分点就是**漏写范围限制**！因为 $k$ 只能在 $(-\infty, -\sqrt{2}) \cup (\sqrt{2}, +\infty)$ 内变动，所以中点 $M$ 只能覆盖直线 $y = -\frac{1}{2}x$ 位于双曲线内部以外的两条开射线（不含端点）。

- **【最终答案】**
  - **$[1]\; k < -\sqrt{2},\; \sqrt{2} < k$**
  - **$[2]$ 直線 $y = -\dfrac{1}{2}x$ のうち、$x < -2\sqrt{2},\; 2\sqrt{2} < x$ の部分**

---

#### 演習問題 9-(4)
- **【原题重现与翻译】**
  - 原题：放物線 $y^2 = 4px\ (p > 0)$ の焦点 $F$ を通る直線と放物線との交点を $P, Q$ とするとき、線分 $PQ$ が点 $F$ で $1 : 2$ に内分されるように直線 $PQ$ の傾きを定めよ。
  - 中文：过抛物线 $y^2 = 4px\ (p > 0)$ 的焦点 $F$ 的直线与抛物线交于 $P, Q$ 两点，确定直线 $PQ$ 的斜率，使得线段 $PQ$ 被点 $F$ 内分为 $1 : 2$。
- **【考点定位】**
  - 抛物线的焦点弦性质、内分点公式、韦达定理（以 $y$ 为主元联立简化计算）。
- **【图解辅助（SVG 矢量图）】**

<svg viewBox="0 0 460 280" width="460" height="280" xmlns="http://www.w3.org/2000/svg" style="background:#fafafa;border:1px solid #e0e0e0;border-radius:6px;">
  <style>
    .axis { stroke:#333; stroke-width:1.4; }
    .curve { stroke:#2980b9; stroke-width:2.2; fill:none; }
    .line { stroke:#e74c3c; stroke-width:1.8; }
    .dash { stroke:#7f8c8d; stroke-width:1; stroke-dasharray:4,3; }
    .txt { font: 12px sans-serif; fill:#2c3e50; }
    .lbl { font: bold 12px sans-serif; fill:#c0392b; }
  </style>
  <!-- Origin at (100, 140), scale: p=1 -> 60px, so x=p at 160, x=2p at 220 -->
  <line x1="40" y1="140" x2="430" y2="140" class="axis"/>
  <line x1="100" y1="20" x2="100" y2="260" class="axis"/>
  <polygon points="430,140 422,136 422,144" fill="#333"/>
  <polygon points="100,20 96,28 104,28" fill="#333"/>
  <text x="418" y="158" class="txt">x</text>
  <text x="108" y="30" class="txt">y</text>
  <text x="84" y="156" class="txt">O</text>
  <!-- Parabola y^2 = 4px: (x, y) -> (100+60x, 140-60y) -->
  <!-- x=0: (100,140), x=1: y=±2 (160, 20/260), x=2: y=±2.83 -->
  <path d="M 244,24 Q 100,82 100,140 Q 100,198 244,256" class="curve"/>
  <!-- Focus F(p, 0) = (160, 140) -->
  <!-- Line m = 2sqrt2: P(0.5p, -sqrt2 p) = (130, 225), Q(2p, 2sqrt2 p) = (220, -30) -> rescale y by 0.65: -->
  <!-- Let's use scale_x = 60, scale_y = 35: -->
  <!-- Re-path parabola with scale_x=60, scale_y=35: at x=3(280), y=±3.46(±121 -> 19, 261) -->
  <rect x="40" y="15" width="390" height="250" fill="#fafafa"/>
  <line x1="40" y1="140" x2="430" y2="140" class="axis"/>
  <line x1="100" y1="20" x2="100" y2="260" class="axis"/>
  <polygon points="430,140 422,136 422,144" fill="#333"/>
  <polygon points="100,20 96,28 104,28" fill="#333"/>
  <text x="418" y="158" class="txt">x</text>
  <text x="108" y="30" class="txt">y</text>
  <text x="84" y="156" class="txt">O</text>
  <!-- Accurate parabola y^2=4x with sx=60, sy=35:
       x=0->(100,140), x=0.5->(130, 140±49.5), x=1->(160, 140±70), x=2->(220, 140±99), x=3->(280, 140±121) -->
  <path d="M 280,19 Q 100,80 100,140 Q 100,200 280,261" class="curve"/>
  <!-- P(0.5, -1.414) = (130, 189.5), F(1, 0) = (160, 140), Q(2, 2.828) = (220, 41) -->
  <line x1="112" y1="219" x2="235" y2="16" class="line"/>
  <circle cx="160" cy="140" r="4" fill="#2c3e50"/>
  <circle cx="130" cy="189.5" r="4" fill="#e74c3c"/>
  <circle cx="220" cy="41" r="4" fill="#e74c3c"/>
  <line x1="130" y1="189.5" x2="100" y2="189.5" class="dash"/>
  <line x1="220" y1="41" x2="100" y2="41" class="dash"/>
  <text x="167" y="155" class="txt">F(p, 0)</text>
  <text x="136" y="198" class="lbl">P(x₁, y₁)</text>
  <text x="228" y="45" class="lbl">Q(x₂, y₂)</text>
  <text x="132" y="164" class="lbl">1</text>
  <text x="180" y="92" class="lbl">2</text>
  <text x="72" y="194" class="txt">y₁</text>
  <text x="72" y="46" class="txt">y₂</text>
  <text x="290" y="34" class="txt" fill="#2980b9">y² = 4px</text>
</svg>

- **【分步标准解答】**
  放物線 $y^2 = 4px\ (p > 0)$ の焦点は $F(p, 0)$ である。
  直線 $PQ$ が $x$ 軸に垂直（$x = p$）であるとき、交点は $(p, \pm 2p)$ となり、点 $F$ は線分 $PQ$ を $1 : 1$ に内分するため不適。
  また、直線 $PQ$ が $x$ 軸に平行（傾き $0$）であるとき、放物線とは 1 点でしか交わらないため不適。
  > 💡 讲师批注：在设直线斜率为 $m$ 之前，必须先排除「垂直于 $x$ 轴（斜率不存在）」与「平行于 $x$ 轴（$m=0$）」两种特殊情形，这是日本数学大题的标准严谨格式。

  したがって、直線 $PQ$ の傾き $m$ は存在し、$m \neq 0$ である。直線 $PQ$ の方程式は
  $$y = m(x - p) \iff x = \frac{1}{m}y + p \qquad \cdots \text{①}$$
  ① を放物線 $y^2 = 4px$ に代入して $x$ を消去すると、
  $$y^2 = 4p\left(\frac{1}{m}y + p\right) \iff y^2 - \frac{4p}{m}y - 4p^2 = 0 \qquad \cdots \text{②}$$
  > 💡 讲师批注：**核心降维技巧**：处理抛物线 $y^2 = 4px$ 的焦点弦时，千万不要消去 $y$ 留 $x$，而应**消去 $x$ 留 $y$**！因为关于 $y$ 的二次方程 ② 首项系数为 $1$，且常数项 $-4p^2 < 0$，判别式恒大于 $0$，韦达定理极为清爽。

  交点を $P(x_1, y_1),\; Q(x_2, y_2)$ とすると、$y_1, y_2$ は ② の 2 解であるから、解と係数の関係より
  $$y_1 + y_2 = \frac{4p}{m} \quad \cdots \text{③}, \qquad y_1 y_2 = -4p^2 \quad \cdots \text{④}$$
  線分 $PQ$ が点 $F(p, 0)$ で $1 : 2$ に内分されるから、$y$ 座標について内分点の公式より
  $$\frac{2y_1 + 1 \cdot y_2}{1 + 2} = 0 \iff y_2 = -2y_1 \qquad \cdots \text{⑤}$$
  > 💡 讲师批注：由于 $y_1 y_2 = -4p^2 < 0$，$P, Q$ 必然分居 $x$ 轴两侧，利用纵坐标的内分关系 $\frac{2y_1 + y_2}{3} = 0$ 直接得到 $y_2 = -2y_1$，省去求横坐标和距离公式的繁琐计算！

  ⑤ を ④ に代入すると、
  $$y_1(-2y_1) = -4p^2 \iff y_1^2 = 2p^2 \implies y_1 = \pm \sqrt{2}\,p$$
  また、⑤ を ③ に代入すると、
  $$y_1 + (-2y_1) = \frac{4p}{m} \iff -y_1 = \frac{4p}{m} \iff m = -\frac{4p}{y_1}$$
  よって、$y_1 = \pm \sqrt{2}\,p$ を代入して
  $$m = -\frac{4p}{\pm \sqrt{2}\,p} = \mp \frac{4}{\sqrt{2}} = \mp 2\sqrt{2}$$
  すなわち、$m = \pm 2\sqrt{2}$。
  > 💡 讲师批注：注意 $P, Q$ 位于 $x$ 轴上下方的对称性：当 $P$ 在下方、$Q$ 在上方时 $m = 2\sqrt{2}$；当 $P$ 在上方、$Q$ 在下方时 $m = -2\sqrt{2}$。两者均满足题意。

- **【最终答案】**
  **$\pm 2\sqrt{2}$**

---

#### 演習問題 9-(5)
- **【原题重现与翻译】**
  - 原题：楕円 $x^2 + 2y^2 = 1$ と放物線 $4y = 2x^2 + a$ が異なる 4 点で交わるための、定数 $a$ の値の範囲を求めよ。
  - 中文：求常数 $a$ 的取值范围，使得椭圆 $x^2 + 2y^2 = 1$ 与抛物线 $4y = 2x^2 + a$ 相交于不同的 4 个点。
- **【考点定位】**
  - 二次曲线交点个数问题、消元后的**二次方程根的分布（解の配置）**。
- **【图解辅助（SVG 矢量图）】**

<svg viewBox="0 0 460 280" width="460" height="280" xmlns="http://www.w3.org/2000/svg" style="background:#fafafa;border:1px solid #e0e0e0;border-radius:6px;">
  <style>
    .axis { stroke:#333; stroke-width:1.4; }
    .ell { stroke:#2980b9; stroke-width:2.2; fill:none; }
    .par { stroke:#e74c3c; stroke-width:2; fill:none; }
    .par-lim { stroke:#95a5a6; stroke-width:1.2; stroke-dasharray:4,3; fill:none; }
    .txt { font: 12px sans-serif; fill:#2c3e50; }
    .lbl { font: bold 12px sans-serif; fill:#c0392b; }
  </style>
  <!-- Origin (230, 140), scale = 120px per unit -->
  <!-- Ellipse: rx=120 (a=1), ry=85 (b=1/sqrt2 ≈ 0.707) -->
  <line x1="40" y1="140" x2="420" y2="140" class="axis"/>
  <line x1="230" y1="20" x2="230" y2="265" class="axis"/>
  <polygon points="420,140 412,136 412,144" fill="#333"/>
  <polygon points="230,20 226,28 234,28" fill="#333"/>
  <text x="408" y="158" class="txt">x</text>
  <text x="238" y="30" class="txt">y</text>
  <text x="215" y="156" class="txt">O</text>
  <ellipse cx="230" cy="140" rx="120" ry="85" class="ell"/>
  <text x="355" y="135" class="txt">1</text>
  <text x="95" y="135" class="txt">-1</text>
  <text x="236" y="50" class="txt">1/√2</text>
  <text x="236" y="240" class="txt">-1/√2</text>
  <!-- Parabola y = 0.5 x^2 + a/4.
       When a = -2.9: vertex y = -0.725 (py = 140 + 87 = 227)
       At x = ±1 (110, 350): y = 0.5 - 0.725 = -0.225 (py = 167)
       At x = ±1.4 (62, 398): y = 0.98 - 0.725 = 0.255 (py = 109) -->
  <path d="M 62,109 Q 230,345 398,109" class="par"/>
  <!-- Limit a = -3 (tangent): vertex y = -0.75 (py = 230) -->
  <path d="M 62,115 Q 230,351 398,115" class="par-lim"/>
  <!-- Highlight 4 intersections roughly -->
  <circle cx="144" cy="200" r="3.5" fill="#e74c3c"/>
  <circle cx="316" cy="200" r="3.5" fill="#e74c3c"/>
  <circle cx="184" cy="219" r="3.5" fill="#e74c3c"/>
  <circle cx="276" cy="219" r="3.5" fill="#e74c3c"/>
  <text x="315" y="70" class="txt" fill="#2980b9">x² + 2y² = 1</text>
  <text x="325" y="102" class="lbl">4y = 2x² + a</text>
  <text x="50" y="255" class="txt">4交点条件: -3 &lt; a &lt; -2√2</text>
</svg>

- **【分步标准解答】**
  放物線の方程式 $4y = 2x^2 + a$ より、
  $$x^2 = 2y - \frac{a}{2} \qquad \cdots \text{①}$$
  ① を楕円の方程式 $x^2 + 2y^2 = 1$ に代入して $x^2$ を消去すると、
  $$\left(2y - \frac{a}{2}\right) + 2y^2 = 1$$
  両辺に $2$ を掛けて整理すると、
  $$4y^2 + 4y - a - 2 = 0 \qquad \cdots \text{②}$$
  > 💡 讲师批注：由于两个方程都只含 $x^2$ 而不含 $x$ 的一次项，曲线均关于 $y$ 轴对称。因此，每一个使 $x^2 > 0$ 的 $y$ 值都恰好对应**两个互为相反数的实数 $x$**；若 $x^2 = 0$ 则只对应 1 个交点 $(0, y)$；若 $x^2 < 0$ 则无实数交点！

  ここで、楕円の方程式より $x^2 = 1 - 2y^2$ であるから、1 つの $y$ の値に対して異なる 2 つの実数 $x$ が存在する条件は
  $$x^2 = 1 - 2y^2 > 0 \iff y^2 < \frac{1}{2} \iff -\frac{1}{\sqrt{2}} < y < \frac{1}{\sqrt{2}}$$
  したがって、2 つの曲線が異なる 4 点で交わるための必要十分条件は、2 次方程式 ② が区間 $-\dfrac{1}{\sqrt{2}} < y < \dfrac{1}{\sqrt{2}}$ の範囲に**異なる 2 つの実数解**をもつことである。
  > 💡 讲师批注：用 $1 - 2y^2 > 0$ 来刻画 $x^2 > 0$ 比用 $2y - \frac{a}{2} > 0$ 更妙！因为区间端点 $\pm\frac{1}{\sqrt{2}}$ 是不含参数 $a$ 的定值，根的分布分析极为简便。

  $f(y) = 4y^2 + 4y - a - 2$ とおくと、平方完成して
  $$f(y) = 4\left(y + \frac{1}{2}\right)^2 - a - 3$$
  放物線 $z = f(y)$ は下に凸であり、その軸 $y = -\dfrac{1}{2}$ は、$-\dfrac{1}{\sqrt{2}} \approx -0.707 < -\dfrac{1}{2} < \dfrac{1}{\sqrt{2}}$ より、常に区間 $\left(-\dfrac{1}{\sqrt{2}}, \dfrac{1}{\sqrt{2}}\right)$ の内部にある。
  よって、求める条件は以下 3 つを同時に満たすことである：
  1. 判別式 $D > 0$（頂点の $z$ 座標 $< 0$）：
     $$-a - 3 < 0 \iff a > -3$$
  2. $f\left(-\dfrac{1}{\sqrt{2}}\right) > 0$：
     $$4\left(-\frac{1}{\sqrt{2}}\right)^2 + 4\left(-\frac{1}{\sqrt{2}}\right) - a - 2 = 2 - 2\sqrt{2} - a - 2 = -2\sqrt{2} - a > 0 \iff a < -2\sqrt{2}$$
  3. $f\left(\dfrac{1}{\sqrt{2}}\right) > 0$：
     $$4\left(\frac{1}{\sqrt{2}}\right)^2 + 4\left(\frac{1}{\sqrt{2}}\right) - a - 2 = 2 + 2\sqrt{2} - a - 2 = 2\sqrt{2} - a > 0 \iff a < 2\sqrt{2}$$

  1, 2, 3 の共通範囲をとると、
  $$-3 < a < -2\sqrt{2}$$
  > 💡 讲师批注：边界几何意义核对：当 $a = -3$ 时，抛物线与椭圆相切于对称两点（2 个交点）；当 $a = -2\sqrt{2}$ 时，抛物线顶点恰好落在椭圆下顶点 $\left(0, -\frac{1}{\sqrt{2}}\right)$（3 个交点）。因此 $-3 < a < -2\sqrt{2}$ 区间虽窄（$-3 < a < -2.828\dots$），但完全精确！

- **【最终答案】**
  **$-3 < a < -2\sqrt{2}$**

---

### 演習問題 10（2次曲線の接線）

#### 演習問題 10-(1)
- **【原题重现与翻译】**
  - 原题：点 $(-1, 3)$ から楕円 $\dfrac{x^2}{12} + \dfrac{y^2}{4} = 1$ に引いた接線の方程式を求めよ。
  - 中文：求过点 $(-1, 3)$ 向椭圆 $\dfrac{x^2}{12} + \dfrac{y^2}{4} = 1$ 所引切线的方程。
- **【考点定位】**
  - 过**曲线外一点**求椭圆切线（设切点法）。
- **【分步标准解答】**
  点 $(-1, 3)$ について $\dfrac{(-1)^2}{12} + \dfrac{3^2}{4} = \dfrac{28}{12} > 1$ より、この点は楕円の外部にある。
  接点の座標を $(x_1, y_1)$ とすると、接点は楕円上にあるから
  $$\frac{x_1^2}{12} + \frac{y_1^2}{4} = 1 \iff x_1^2 + 3y_1^2 = 12 \qquad \cdots \text{①}$$
  また、点 $(x_1, y_1)$ における楕円の接線の方程式は
  $$\frac{x_1 x}{12} + \frac{y_1 y}{4} = 1 \iff x_1 x + 3y_1 y = 12 \qquad \cdots \text{②}$$
  > 💡 讲师批注：**严禁把点 $(-1, 3)$ 直接代入切线公式当成 $(x_1, y_1)$！** 切线公式中的 $(x_1, y_1)$ 必须是**曲线上的切点**，而定点 $(-1, 3)$ 是切线经过的点，应代入 $(x, y)$！

  直線 ② が点 $(-1, 3)$ を通るから、$x = -1,\; y = 3$ を代入して
  $$-x_1 + 9y_1 = 12 \iff x_1 = 9y_1 - 12 \qquad \cdots \text{③}$$
  ③ を ① に代入すると、
  $$(9y_1 - 12)^2 + 3y_1^2 = 12$$
  $$81y_1^2 - 216y_1 + 144 + 3y_1^2 - 12 = 0$$
  $$84y_1^2 - 216y_1 + 132 = 0$$
  両辺を $12$ で割ると、
  $$7y_1^2 - 18y_1 + 11 = 0$$
  $$(7y_1 - 11)(y_1 - 1) = 0$$
  よって、$y_1 = 1,\; \dfrac{11}{7}$。
  - $y_1 = 1$ のとき、③ より $x_1 = 9 \cdot 1 - 12 = -3$。
    ② に代入して、$-3x + 3y = 12 \iff x - y + 4 = 0$（すなわち $y = x + 4$）。
  - $y_1 = \dfrac{11}{7}$ のとき、③ より $x_1 = 9 \cdot \dfrac{11}{7} - 12 = \dfrac{99 - 84}{7} = \dfrac{15}{7}$。
    ② に代入して、$\dfrac{15}{7}x + \dfrac{33}{7}y = 12$。両辺に $\dfrac{7}{3}$ を掛けて、$5x + 11y = 28$（すなわち $y = -\dfrac{5}{11}x + \dfrac{28}{11}$）。
  > 💡 讲师批注：验算：将 $(-1, 3)$ 分别代入两条切线：$-1 - 3 + 4 = 0$，$-5 + 33 = 28$，均成立；再将两切点 $(-3, 1)$ 与 $\left(\frac{15}{7}, \frac{11}{7}\right)$ 代入 $x^2 + 3y^2 = 12$：$9+3=12$，$\frac{225+363}{49} = \frac{588}{49} = 12$，100% 准确！

- **【最终答案】**
  **$x - y + 4 = 0,\quad 5x + 11y - 28 = 0$**（或 $y = x + 4,\quad y = -\dfrac{5}{11}x + \dfrac{28}{11}$）

---

#### 演習問題 10-(2)
- **【原题重现与翻译】**
  - 原题：放物線 $y^2 = 4px\ (p > 0)$ 上の点 $P(x_1, y_1)$ における接線と $x$ 軸との交点を $T$、放物線の焦点を $F$ とすると、$\angle PTF = \angle TPF$ であることを証明せよ。ただし、$x_1 > 0,\; y_1 > 0$ とする。
    > ⚠️ **教材勘误提示**：原教材第 183 页（`page_0184.jpg`）将「$x$ 軸との交点」漏印为「$x$ 軸と交点」，且「$x_1 > 0,\; y_1 > 0$」间漏了逗号，此处已修正。
  - 中文：设抛物线 $y^2 = 4px\ (p > 0)$ 上一点 $P(x_1, y_1)$（$x_1 > 0,\; y_1 > 0$）处的切线与 $x$ 轴的交点为 $T$，抛物线的焦点为 $F$，证明 $\angle PTF = \angle TPF$。
- **【考点定位】**
  - 抛物线的切线方程、抛物线的几何性质（光学反射性质的核心引理）。
- **【图解辅助（SVG 矢量图）】**

<svg viewBox="0 0 460 250" width="460" height="250" xmlns="http://www.w3.org/2000/svg" style="background:#fafafa;border:1px solid #e0e0e0;border-radius:6px;">
  <style>
    .axis { stroke:#333; stroke-width:1.4; }
    .curve { stroke:#2980b9; stroke-width:2.2; fill:none; }
    .tan { stroke:#e74c3c; stroke-width:1.8; }
    .seg { stroke:#27ae60; stroke-width:1.8; }
    .dash { stroke:#7f8c8d; stroke-width:1.2; stroke-dasharray:4,3; }
    .txt { font: 12px sans-serif; fill:#2c3e50; }
    .lbl { font: bold 12px sans-serif; fill:#c0392b; }
  </style>
  <!-- Origin (200, 140), scale: 1 unit = 45px, p=1 -> F=(245, 140), x1=2 -> P=(290, 140-2.83*45=13)? Wait use sy=35:
       x1=2 -> y1=2.83 -> py = 140 - 99 = 41; T=(-2,0) = (110, 140) -->
  <line x1="30" y1="140" x2="430" y2="140" class="axis"/>
  <line x1="200" y1="15" x2="200" y2="235" class="axis"/>
  <polygon points="430,140 422,136 422,144" fill="#333"/>
  <polygon points="200,15 196,23 204,23" fill="#333"/>
  <text x="418" y="158" class="txt">x</text>
  <text x="208" y="26" class="txt">y</text>
  <text x="184" y="156" class="txt">O</text>
  <!-- Directrix x = -p = (155) -->
  <line x1="155" y1="20" x2="155" y2="230" class="dash"/>
  <text x="135" y="225" class="txt">x=-p</text>
  <!-- Parabola y^2 = 4px (sx=45, sy=35): x=3->(335, 19/261) -->
  <path d="M 335,19 Q 200,79 200,140 Q 200,201 335,261" class="curve"/>
  <!-- T(-2,0)=(110,140), P(2,2.83)=(290,41), F(1,0)=(245,140) -->
  <line x1="65" y1="164.8" x2="344" y2="11.3" class="tan"/>
  <line x1="290" y1="41" x2="245" y2="140" class="seg"/>
  <line x1="110" y1="140" x2="245" y2="140" class="seg"/>
  <line x1="290" y1="41" x2="155" y2="41" class="dash"/>
  <!-- Equal tick marks on TF and PF -->
  <circle cx="110" cy="140" r="3.5" fill="#e74c3c"/>
  <circle cx="245" cy="140" r="3.5" fill="#2c3e50"/>
  <circle cx="290" cy="41" r="3.5" fill="#e74c3c"/>
  <text x="92" y="160" class="lbl">T(-x₁, 0)</text>
  <text x="242" y="158" class="txt">F(p, 0)</text>
  <text x="298" y="42" class="lbl">P(x₁, y₁)</text>
  <text x="172" y="132" class="txt" fill="#27ae60">TF = x₁ + p</text>
  <text x="276" y="102" class="txt" fill="#27ae60">PF = x₁ + p</text>
  <text x="342" y="34" class="txt" fill="#2980b9">y² = 4px</text>
</svg>

- **【分步标准解答】**
  **［証明］**
  放物線 $y^2 = 4px\ (p > 0)$ 上の点 $P(x_1, y_1)$ における接線の方程式は
  $$y_1 y = 2p(x + x_1)$$
  点 $T$ はこの接線と $x$ 軸との交点であるから、$y = 0$ を代入して
  $$0 = 2p(x + x_1)$$
  $p > 0$ より $x = -x_1$。よって、点 $T$ の座標は $T(-x_1, 0)$ である。
  > 💡 讲师批注：记住这个超实用的几何性质——抛物线 $y^2 = 4px$ 上点 $(x_1, y_1)$ 处切线的 $x$ 截距恰好是 $-x_1$，即原点 $O$ 永远是点 $T$ 与点 $P$ 在 $x$ 轴上射影的中点！

  また、放物線の焦点は $F(p, 0)$ であり、$x_1 > 0,\; p > 0$ であるから、線分 $TF$ の長さは
  $$TF = p - (-x_1) = x_1 + p$$
  一方、点 $P(x_1, y_1)$ は放物線 $y^2 = 4px$ 上にあるから $y_1^2 = 4px_1$ を満たす。よって、線分 $PF$ の長さは
  $$PF = \sqrt{(x_1 - p)^2 + y_1^2} = \sqrt{(x_1 - p)^2 + 4px_1} = \sqrt{x_1^2 + 2px_1 + p^2} = \sqrt{(x_1 + p)^2}$$
  $x_1 + p > 0$ であるから、
  $$PF = x_1 + p$$
  > 💡 讲师批注：也可以直接利用抛物线定义「$PF = P$ 到准线 $x = -p$ 的距离 $= x_1 - (-p) = x_1 + p$」，一步到位！

  以上より $TF = PF$ である。さらに $y_1 > 0$ より点 $P$ は $x$ 軸上にないので、$\triangle PTF$ は $FT = FP$ の二等辺三角形となる。
  したがって、底角が等しいことから
  $$\angle PTF = \angle TPF \qquad \text{（証明終）}$$
  > 💡 讲师批注：由此立即推得抛物线的**光学反射性质**：平行于对称轴入射的光线，经抛物面反射后必汇聚于焦点 $F$（卫星天线、车灯反光罩的原理）。

- **【最终答案】**
  **$\triangle PTF$ において $TF = PF = x_1 + p$ より二等辺三角形となるため、$\angle PTF = \angle TPF$（証明完了）**

---

#### 演習問題 10-(3)
- **【原题重现与翻译】**
  - 原题：双曲線 $x^2 - 4y^2 = 4$ 上の点 $(a, b)$ における接線の傾きが $m$ のとき、次の問いに答えよ。ただし、$b \neq 0$ とする。
    - $[1]$ $a, b, m$ の間の関係式を求めよ。
    - $[2]$ この曲線上の点と直線 $y = 2x$ の間の距離を $d$ とする。$d$ の最小値を求めよ。また、$d$ の最小値を与える曲線上の点の座標を求めよ。
    > ⚠️ **教材勘误提示**：原教材第 184 页（`page_0185.jpg`）将「与える」误印为「与えられる」，此处已按自然日语修正。
  - 中文：双曲线 $x^2 - 4y^2 = 4$ 上一点 $(a, b)$（$b \neq 0$）处切线的斜率为 $m$，回答下列问题：
    - $[1]$ 求 $a, b, m$ 之间的关系式。
    - $[2]$ 设该曲线上的点到直线 $y = 2x$ 的距离为 $d$，求 $d$ 的最小值以及取得最小值的曲线上点的坐标。
- **【考点定位】**
  - 双曲线的切线公式、利用**平行切线**求曲线上点到定直线的最短距离。
- **【图解辅助（SVG 矢量图）】**

<svg viewBox="0 0 460 280" width="460" height="280" xmlns="http://www.w3.org/2000/svg" style="background:#fafafa;border:1px solid #e0e0e0;border-radius:6px;">
  <style>
    .axis { stroke:#333; stroke-width:1.4; }
    .asym { stroke:#bdc3c7; stroke-width:1; stroke-dasharray:4,4; }
    .curve { stroke:#2980b9; stroke-width:2.2; fill:none; }
    .l0 { stroke:#2c3e50; stroke-width:1.8; }
    .tan { stroke:#e74c3c; stroke-width:1.6; stroke-dasharray:5,3; }
    .txt { font: 12px sans-serif; fill:#2c3e50; }
    .lbl { font: bold 12px sans-serif; fill:#c0392b; }
  </style>
  <!-- Origin (230, 140), scale: 1 unit = 40px -->
  <!-- Hyperbola x^2/4 - y^2/1 = 1: vertices (±2,0) = (150,140), (310,140); asym y = ±0.5x -->
  <line x1="30" y1="140" x2="430" y2="140" class="axis"/>
  <line x1="230" y1="15" x2="230" y2="265" class="axis"/>
  <polygon points="430,140 422,136 422,144" fill="#333"/>
  <polygon points="230,15 226,23 234,23" fill="#333"/>
  <text x="418" y="158" class="txt">x</text>
  <text x="238" y="26" class="txt">y</text>
  <text x="215" y="156" class="txt">O</text>
  <!-- Asymptotes y = ±0.5x -->
  <line x1="40" y1="235" x2="420" y2="45" class="asym"/>
  <line x1="40" y1="45" x2="420" y2="235" class="asym"/>
  <!-- Hyperbola -->
  <path d="M 420,56 Q 310,104 310,140 Q 310,176 420,224" class="curve"/>
  <path d="M 40,56 Q 150,104 150,140 Q 150,176 40,224" class="curve"/>
  <!-- Line y = 2x: passes (230,140), slope 2 -> (290, 20) to (170, 260) -->
  <line x1="170" y1="260" x2="290" y2="20" class="l0"/>
  <!-- Tangent points (±2.065, ±0.258) -> (312.6, 129.7) and (147.4, 150.3) -->
  <line x1="255" y1="245" x2="365" y2="25" class="tan"/>
  <line x1="95" y1="255" x2="205" y2="35" class="tan"/>
  <circle cx="312.6" cy="129.7" r="4" fill="#e74c3c"/>
  <circle cx="147.4" cy="150.3" r="4" fill="#e74c3c"/>
  <text x="294" y="34" class="txt">y = 2x</text>
  <text x="320" y="128" class="lbl">P₁(8√15/15, √15/15)</text>
  <text x="18" y="168" class="lbl">P₂(-8√15/15, -√15/15)</text>
  <text x="355" y="218" class="txt" fill="#2980b9">x² - 4y² = 4</text>
</svg>

- **【分步标准解答】**
  **$[1]$ $a, b, m$ の間の関係式**
  双曲線 $x^2 - 4y^2 = 4$（すなわち $\dfrac{x^2}{4} - \dfrac{y^2}{1} = 1$）上の点 $(a, b)$ における接線の方程式は
  $$ax - 4by = 4$$
  $b \neq 0$ であるから、$y$ について解くと
  $$y = \frac{a}{4b}x - \frac{1}{b}$$
  この接線の傾きが $m$ であるから、
  $$m = \frac{a}{4b} \qquad \text{（すなわち } a = 4bm \text{）}$$
  > 💡 讲师批注：本题题干已给出 $b \neq 0$，因此可以直接除以 $4b$ 得到 $m = \frac{a}{4b}$。

  **$[2]$ 距離 $d$ の最小値とそのときの点の座標**
  双曲線 $x^2 - 4y^2 = 4$ の漸近線は $y = \pm \dfrac{1}{2}x$ であり、直線 $y = 2x$ の傾きは $2 > \dfrac{1}{2}$ であるから、直線 $y = 2x$ はこの双曲線と共有点をもたない。
  よって、双曲線上の点と直線 $y = 2x$ の距離 $d$ が最小となるのは、その点における双曲線の接線が直線 $y = 2x$ と平行（傾き $m = 2$）になるときである。
  > 💡 讲师批注：务必先确认直线 $y = 2x$ 与双曲线不相交！若直线斜率在 $\left(-\frac{1}{2}, \frac{1}{2}\right)$ 之间，直线会与双曲线相交，最小距离就成了 $0$。

  $[1]$ の関係式に $m = 2$ を代入すると、
  $$a = 4b \cdot 2 = 8b \qquad \cdots \text{①}$$
  また、点 $(a, b)$ は双曲線 $x^2 - 4y^2 = 4$ 上にあるから、
  $$a^2 - 4b^2 = 4 \qquad \cdots \text{②}$$
  ① を ② に代入して、
  $$(8b)^2 - 4b^2 = 4 \iff 60b^2 = 4 \iff b^2 = \frac{1}{15}$$
  よって、$b = \pm \dfrac{1}{\sqrt{15}} = \pm \dfrac{\sqrt{15}}{15}$。
  ① より、$a = 8b = \pm \dfrac{8\sqrt{15}}{15}$（複号同順）。
  したがって、求める点の座標は
  $$\left(\frac{8\sqrt{15}}{15},\; \frac{\sqrt{15}}{15}\right),\quad \left(-\frac{8\sqrt{15}}{15},\; -\frac{\sqrt{15}}{15}\right)$$
  このとき、点 $(a, b)$ と直線 $2x - y = 0$ の距離 $d$ は、点と直線の距離の公式より
  $$d = \frac{|2a - b|}{\sqrt{2^2 + (-1)^2}} = \frac{\left|\pm \dfrac{16\sqrt{15}}{15} \mp \dfrac{\sqrt{15}}{15}\right|}{\sqrt{5}} = \frac{\dfrac{15\sqrt{15}}{15}}{\sqrt{5}} = \frac{\sqrt{15}}{\sqrt{5}} = \sqrt{3}$$
  > 💡 讲师批注：双曲线关于原点对称，直线 $y = 2x$ 也过原点，所以必有两个关于原点对称的最近点，切勿漏写负号那一组！另外，也可用「联立 $y = 2x + k$ 与双曲线，由 $D \ge 0 \implies |k| \ge \sqrt{15} \implies d = \frac{|k|}{\sqrt{5}} \ge \sqrt{3}$」完成双重验算。

- **【最终答案】**
  - **$[1]\; m = \dfrac{a}{4b}$（または $a = 4bm$）**
  - **$[2]$ 最小値 $\sqrt{3}$、点の座標 $\left(\dfrac{8\sqrt{15}}{15},\; \dfrac{\sqrt{15}}{15}\right),\; \left(-\dfrac{8\sqrt{15}}{15},\; -\dfrac{\sqrt{15}}{15}\right)$**

---

#### 演習問題 10-(4)
- **【原题重现与翻译】**
  - 原题：楕円 $x^2 + 4y^2 = 4$ について、楕円の外部の点 $P(a, b)$ から、この楕円に引いた 2 本の接線が直交するような点 $P$ の軌跡を求めよ。
  - 中文：对于椭圆 $x^2 + 4y^2 = 4$，求椭圆外部一点 $P(a, b)$ 的轨迹，使得从点 $P$ 向该椭圆所引的两条切线互相垂直。
- **【考点定位】**
  - 椭圆的**蒙日圆（準円 / モンジュの円）**、切线斜率的二次方程与韦达定理、**垂直切线特殊情形的分类讨论**。
- **【图解辅助（SVG 矢量图）】**

<svg viewBox="0 0 460 280" width="460" height="280" xmlns="http://www.w3.org/2000/svg" style="background:#fafafa;border:1px solid #e0e0e0;border-radius:6px;">
  <style>
    .axis { stroke:#333; stroke-width:1.4; }
    .ell { stroke:#2980b9; stroke-width:2.2; fill:none; }
    .cir { stroke:#e74c3c; stroke-width:2; fill:none; }
    .tan { stroke:#27ae60; stroke-width:1.5; }
    .box { stroke:#95a5a6; stroke-width:1.1; stroke-dasharray:4,3; fill:none; }
    .txt { font: 12px sans-serif; fill:#2c3e50; }
    .lbl { font: bold 12px sans-serif; fill:#c0392b; }
  </style>
  <!-- Origin (230, 140), scale: 1 unit = 45px -->
  <!-- Ellipse: rx=90 (2), ry=45 (1) -->
  <!-- Monge Circle: r = sqrt5 ≈ 2.236 -> 100.6px -->
  <line x1="50" y1="140" x2="410" y2="140" class="axis"/>
  <line x1="230" y1="15" x2="230" y2="265" class="axis"/>
  <polygon points="410,140 402,136 402,144" fill="#333"/>
  <polygon points="230,15 226,23 234,23" fill="#333"/>
  <text x="398" y="158" class="txt">x</text>
  <text x="238" y="26" class="txt">y</text>
  <text x="215" y="156" class="txt">O</text>
  <!-- Bounding rectangle (±2, ±1) for special case -->
  <rect x="140" y="95" width="180" height="90" class="box"/>
  <ellipse cx="230" cy="140" rx="90" ry="45" class="ell"/>
  <circle cx="230" cy="140" r="100.6" class="cir"/>
  <!-- Special point (2,1) = (320, 95) -->
  <circle cx="320" cy="95" r="3.5" fill="#95a5a6"/>
  <text x="326" y="92" class="txt">(2, 1)</text>
  <!-- General point P(1, 2) = (275, 50)? Check: 1^2+2^2=5 -> on circle!
       Tangents from (1,2): (1-4)m^2 - 4m + (4-1)=0 -> -3m^2-4m+3=0 -> m = (-2±sqrt13)/3 ≈ 0.535, -1.868 -->
  <!-- Draw tangents from P(1,2) = (275, 50) -->
  <line x1="150" y1="117" x2="310" y2="31" class="tan"/>
  <line x1="255" y1="13" x2="345" y2="181" class="tan"/>
  <circle cx="275" cy="50" r="4" fill="#e74c3c"/>
  <text x="282" y="46" class="lbl">P(a, b)</text>
  <text x="258" y="70" class="txt" fill="#27ae60">90°</text>
  <text x="68" y="62" class="lbl">軌跡: x² + y² = 5</text>
  <text x="68" y="218" class="txt" fill="#2980b9">楕円: x² + 4y² = 4</text>
</svg>

- **【分步标准解答】**
  楕円の方程式は $\dfrac{x^2}{4} + \dfrac{y^2}{1} = 1$ である。点 $P(a, b)$ が楕円の外部にあることから、
  $$a^2 + 4b^2 > 4 \qquad \cdots \text{①}$$
  2 本の接線が $x$ 軸に垂直な直線を含むかどうかで場合分けを行う。

  **（i）2 本の接線がいずれも $x$ 軸に垂直でないとき（すなわち $a \neq \pm 2$）**
  点 $P(a, b)$ を通り傾き $m$ の直線の方程式は
  $$y = m(x - a) + b = mx + (b - ma) \qquad \cdots \text{②}$$
  ② を楕円 $x^2 + 4y^2 = 4$ に代入して $y$ を消去すると、
  $$x^2 + 4\{mx + (b - ma)\}^2 = 4$$
  $$(4m^2 + 1)x^2 + 8m(b - ma)x + 4(b - ma)^2 - 4 = 0$$
  直線 ② が楕円に接するための条件は、この $x$ についての 2 次方程式の判別式を $D$ として $D = 0$ であるから、
  $$\frac{D}{4} = 16m^2(b - ma)^2 - (4m^2 + 1)\{4(b - ma)^2 - 4\} = 0$$
  両辺を $4$ で割って整理すると、
  $$4m^2(b - ma)^2 - (4m^2 + 1)(b - ma)^2 + (4m^2 + 1) = 0$$
  $$-(b - ma)^2 + 4m^2 + 1 = 0$$
  $$(a^2 - 4)m^2 - 2abm + (b^2 - 1) = 0 \qquad \cdots \text{③}$$
  > 💡 讲师批注：若熟记椭圆切线截距公式 $n^2 = a_0^2 m^2 + b_0^2$（教材 P182 的式 ⑦），直接将 $n = b - ma,\; a_0^2 = 4,\; b_0^2 = 1$ 代入 $(b - ma)^2 = 4m^2 + 1$，一秒即可得到 ③！

  $a \neq \pm 2$ より $a^2 - 4 \neq 0$ であるから、③ は $m$ についての 2 次方程式であり、その 2 解 $m_1, m_2$ が 2 本の接線の傾きとなる。
  2 本の接線が直交するための条件は $m_1 m_2 = -1$ であるから、解と係数の関係より
  $$\frac{b^2 - 1}{a^2 - 4} = -1 \iff b^2 - 1 = 4 - a^2 \iff a^2 + b^2 = 5$$
  このとき、③ の判別式 $D_m$ は
  $$\frac{D_m}{4} = (-ab)^2 - (a^2 - 4)(b^2 - 1) = a^2 + 4b^2 - 4 > 0 \quad (\text{① より})$$
  となり、③ は確かに異なる 2 つの実数解をもつ。

  **（ii）2 本の接線のうち 1 本が $x$ 軸に垂直であるとき（すなわち $a = \pm 2$）**
  $x$ 軸に垂直な楕円の接線は $x = \pm 2$ であり、これと直交する接線は $x$ 軸に平行な接線 $y = \pm 1$ である。
  よって、交点 $P$ は $(\pm 2, \pm 1)$（複号任意、計 4 点）となるが、これらはいずれも
  $$a^2 + b^2 = (\pm 2)^2 + (\pm 1)^2 = 5$$
  を満たす。
  > 💡 讲师批注：**必考严谨步！** 绝不能漏掉情况 (ii)！如果只算情况 (i)，就会留下 4 个待确认的空心点 $(\pm 2, \pm 1)$，必须显式验证这 4 点恰好补全了圆 $x^2 + y^2 = 5$。

  **（i）（ii）のまとめ（逆の確認）**
  円 $x^2 + y^2 = 5$ 上の任意の点 $(x, y)$ は $x^2 + 4y^2 = (x^2 + y^2) + 3y^2 = 5 + 3y^2 \ge 5 > 4$ を満たすため、すべて楕円の外部にある。
  したがって、求める点 $P$ の軌跡は円 $x^2 + y^2 = 5$ 全体である。

- **【最终答案】**
  **円 $x^2 + y^2 = 5$**（一般结论速记：椭圆 $\dfrac{x^2}{a^2} + \dfrac{y^2}{b^2} = 1$ 的蒙日圆恒为 $x^2 + y^2 = a^2 + b^2$）

---

#### 演習問題 10-(5)
- **【原题重现与翻译】**
  - 原题：楕円 $Ax^2 + By^2 = 1$ に、この楕円の外部にある点 $P(x_0, y_0)$ から引いた 2 つの接線を考え、その接点を $Q, R$ とする。次のことを示せ。
    - $[1]$ 直線 $QR$ の方程式は $Ax_0 x + By_0 y = 1$ である。
    - $[2]$ 楕円 $Ax^2 + By^2 = 1$ の外部にあって、直線 $QR$ 上にある点 $S$ からこの楕円に引いた 2 本の接線の 2 つの接点を通る直線 $l$ は、点 $P$ を通る。
    > ⚠️ **教材勘误提示**：原教材第 185 页（`page_0186.jpg`）[1] 误印为「直線 $QR$ のほう方程式は $Ax_0 x + By_0 y = 1$ にある。」，多印了「ほう」且「である」误作「にある」，此处已修正。
  - 中文：从椭圆 $Ax^2 + By^2 = 1$ 外部一点 $P(x_0, y_0)$ 向该椭圆引两条切线，切点为 $Q, R$。证明以下结论：
    - $[1]$ 直线 $QR$ 的方程为 $Ax_0 x + By_0 y = 1$。
    - $[2]$ 从位于椭圆外部且在直线 $QR$ 上的点 $S$ 向椭圆引两条切线，过这两条切线的切点的直线 $l$ 必经过点 $P$。
- **【考点定位】**
  - 椭圆的**切点弦（極線 / 极线）**方程、射影几何中的**配极定理**（以对称代入法巧妙证明）。
- **【图解辅助（SVG 矢量图）】**

<svg viewBox="0 0 460 270" width="460" height="270" xmlns="http://www.w3.org/2000/svg" style="background:#fafafa;border:1px solid #e0e0e0;border-radius:6px;">
  <style>
    .ell { stroke:#2980b9; stroke-width:2.2; fill:none; }
    .tanP { stroke:#27ae60; stroke-width:1.4; }
    .qr { stroke:#e74c3c; stroke-width:2; }
    .tanS { stroke:#8e44ad; stroke-width:1.4; stroke-dasharray:4,3; }
    .lineL { stroke:#d35400; stroke-width:2; }
    .txt { font: 12px sans-serif; fill:#2c3e50; }
    .lbl { font: bold 12px sans-serif; fill:#c0392b; }
  </style>
  <!-- Center (210, 145), rx=100, ry=65 -->
  <ellipse cx="210" cy="145" rx="100" ry="65" class="ell"/>
  <!-- P outside on right: P(370, 125) -->
  <!-- Approximate tangents from P(370, 125) to ellipse -->
  <line x1="370" y1="125" x2="225" y2="62" class="tanP"/>
  <line x1="370" y1="125" x2="245" y2="218" class="tanP"/>
  <!-- Tangent points Q(268, 92) and R(278, 192) roughly on ellipse:
       Check (268-210)/100 = 0.58, (92-145)/65 = -0.815 -> 0.336+0.664 = 1.00!
       Check (278-210)/100 = 0.68, (192-145)/65 = 0.723 -> 0.462+0.523 ≈ 0.99! -->
  <circle cx="268" cy="92" r="3.5" fill="#e74c3c"/>
  <circle cx="278" cy="192" r="3.5" fill="#e74c3c"/>
  <!-- Line QR extended up to S(258, 22) -->
  <line x1="255" y1="12" x2="286" y2="255" class="qr"/>
  <circle cx="258" cy="28" r="4" fill="#8e44ad"/>
  <!-- Tangents from S(258, 28) to ellipse: touch around U(146, 95) and V(304, 123) -->
  <!-- Wait: line UV must pass through P(370, 125)!
       Check U(146, 95): (-64/100)^2 + (-50/65)^2 = 0.41 + 0.59 = 1.00!
       Line from U(146, 95) to P(370, 125): slope = 30/224 = 0.134.
       Intersects ellipse again at V(306, 116.4): (96/100)^2 + (-28.6/65)^2 = 0.92 + 0.19 ≈ 1.11, close enough:
       Use U(142, 97), V(304, 121) -> passes right near P(370, 125) -->
  <line x1="258" y1="28" x2="115" y2="115" class="tanS"/>
  <line x1="258" y1="28" x2="322" y2="155" class="tanS"/>
  <line x1="120" y1="92" x2="395" y2="128" class="lineL"/>
  <circle cx="144" cy="95" r="3.5" fill="#d35400"/>
  <circle cx="305" cy="116" r="3.5" fill="#d35400"/>
  <circle cx="370" cy="125" r="4.5" fill="#27ae60"/>
  <text x="378" y="128" class="txt" fill="#27ae60" font-weight="bold">P(x₀, y₀)</text>
  <text x="275" y="88" class="lbl">Q</text>
  <text x="285" y="198" class="lbl">R</text>
  <text x="266" y="28" class="txt" fill="#8e44ad" font-weight="bold">S(x₃, y₃)</text>
  <text x="160" y="228" class="txt" fill="#2980b9">楕円 Ax² + By² = 1</text>
  <text x="325" y="148" class="txt" fill="#d35400" font-weight="bold">直線 l</text>
  <text x="290" y="246" class="lbl">直線 QR</text>
</svg>

- **【分步标准解答】**
  **$[1]$ 直線 $QR$ の方程式**
  2 つの接点の座標を $Q(x_1, y_1),\; R(x_2, y_2)$ とする。
  楕円 $Ax^2 + By^2 = 1$（すなわち $\dfrac{x^2}{1/A} + \dfrac{y^2}{1/B} = 1$、$A > 0, B > 0$）上の点 $Q, R$ における接線の方程式はそれぞれ
  $$Ax_1 x + By_1 y = 1, \qquad Ax_2 x + By_2 y = 1$$
  これら 2 本の接線はともに点 $P(x_0, y_0)$ を通るから、$(x, y) = (x_0, y_0)$ を代入して
  $$Ax_1 x_0 + By_1 y_0 = 1 \iff Ax_0 x_1 + By_0 y_1 = 1 \qquad \cdots \text{①}$$
  $$Ax_2 x_0 + By_2 y_0 = 1 \iff Ax_0 x_2 + By_0 y_2 = 1 \qquad \cdots \text{②}$$
  > 💡 讲师批注：**神级「逆向视角」思维！** 不要去硬解 $Q, R$ 的坐标！只需把 ①、② 看成是**关于 $(x, y)$ 的一次方程 $Ax_0 x + By_0 y = 1$ 分别在 $(x_1, y_1)$ 和 $(x_2, y_2)$ 处成立**！

  点 $P(x_0, y_0)$ は楕円の外部にあるから $(x_0, y_0) \neq (0, 0)$ であり、$Ax_0 x + By_0 y = 1$ は直線を表す。
  ①、② より、異なる 2 点 $Q(x_1, y_1),\; R(x_2, y_2)$ はともに直線 $Ax_0 x + By_0 y = 1$ 上にある。
  異なる 2 点を通る直線はただ 1 つに定まるから、直線 $QR$ の方程式は
  $$Ax_0 x + By_0 y = 1 \qquad \text{（証明終）}$$

  **$[2]$ 直線 $l$ が点 $P$ を通ることの証明**
  点 $S$ の座標を $(x_3, y_3)$ とする。
  点 $S$ は直線 $QR$ 上にあるから、$[1]$ より
  $$Ax_0 x_3 + By_0 y_3 = 1 \qquad \cdots \text{③}$$
  また、点 $S(x_3, y_3)$ は楕円の外部にあるから、$[1]$ の結果をそのまま点 $S$ に適用すると、点 $S$ から楕円に引いた 2 本の接線の 2 つの接点を通る直線 $l$ の方程式は
  $$Ax_3 x + By_3 y = 1 \qquad \cdots \text{④}$$
  ③ を書き直すと $Ax_3 x_0 + By_3 y_0 = 1$ となり、これは点 $P(x_0, y_0)$ が直線 ④ の方程式を満たすことを示している。
  したがって、直線 $l$ は点 $P$ を通る。　（証明終）
  > 💡 讲师批注：本题展示了极点与极线的**对偶对称性（対称性）**：$S$ 在 $P$ 的极线上 $\iff P$ 在 $S$ 的极线上。整个证明不求任何交点坐标，行云流水，是日本国公立大学二次试验的经典压轴思维！

- **【最终答案】**
  **$[1][2]$ 均按上述同构代入法严格证明完毕。**

---
> ➡️ **接续下篇**：演習問題 11（4 题）与 演習問題 12（5 题）详见 [`note_013_b.md`](./note_013_b.md)。
