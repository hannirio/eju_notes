# 《EJU 教材全解与备课讲义》数学 010（P136–P150）

> **对应源文件**：`work_math/ocr_md/ocr_010_p136-150.md`（第六章《三角関数》之「万能公式・和と積の公式・三角関数の合成・演習問題 4(8) & 5」；第七章《解析幾何》之「直線上の点、平面上の点・直線の方程式、2直線の関係・演習問題 1 & 2」）
> **视觉核对参考图**：`work_math/ref_imgs/page_0136.jpg` – `page_0150.jpg`（全 15 页逐符号核对）

---

## 一、国内高中基础知识点唤醒与 EJU 考纲差异对比

本切片横跨日本高中 **数学Ⅱ** 的两大核心模块：**「三角関数」收官（积化和差、和差化积、辅助角合成）** 与 **「図形と方程式（解析幾何）」开篇（定比分点、两点距离、重心、点对称、直线方程与两直线位置关系）**。

### 1.1 万能公式（$t = \tan\frac{\theta}{2}$ 的有理表示）

设 $t = \tan\dfrac{\theta}{2}$（$\cos\dfrac{\theta}{2} \neq 0$），则：
$$\sin\theta = \frac{2t}{1+t^2}, \qquad \cos\theta = \frac{1-t^2}{1+t^2}, \qquad \tan\theta = \frac{2t}{1-t^2}\;\; (t \neq \pm 1)$$

### 1.2 三角函数的积化和差与和差化积公式（三角関数の和と積公式）

- **積→和の公式（积化和差）**：直接由加法定理两式相加或相减得到：
  1. $\sin\alpha\cos\beta = \dfrac{1}{2}\{\sin(\alpha+\beta) + \sin(\alpha-\beta)\}$
  2. $\cos\alpha\sin\beta = \dfrac{1}{2}\{\sin(\alpha+\beta) - \sin(\alpha-\beta)\}$
  3. $\cos\alpha\cos\beta = \dfrac{1}{2}\{\cos(\alpha+\beta) + \cos(\alpha-\beta)\}$
  4. $\sin\alpha\sin\beta = -\dfrac{1}{2}\{\cos(\alpha+\beta) - \cos(\alpha-\beta)\}$
- **和→積の公式（和差化积）**：令 $\alpha+\beta=A,\; \alpha-\beta=B$，即 $\alpha=\dfrac{A+B}{2},\; \beta=\dfrac{A-B}{2}$ 代入上四式得到：
  5. $\sin A + \sin B = 2\sin\dfrac{A+B}{2}\cos\dfrac{A-B}{2}$
  6. $\sin A - \sin B = 2\cos\dfrac{A+B}{2}\sin\dfrac{A-B}{2}$
  7. $\cos A + \cos B = 2\cos\dfrac{A+B}{2}\cos\dfrac{A-B}{2}$
  8. $\cos A - \cos B = -2\sin\dfrac{A+B}{2}\sin\dfrac{A-B}{2}$

> 💡 **记忆防错诀窍**：不要死记 8 条公式！只需牢记加法定理，考场 10 秒内现场推导；尤其注意第 ④、⑧ 条前方的**负号**（$\cos(\alpha+\beta) - \cos(\alpha-\beta) = -2\sin\alpha\sin\beta$）。

### 1.3 三角函数的合成（三角関数の合成 / 辅助角公式）

$$a\sin\theta + b\cos\theta = \sqrt{a^2+b^2}\,\sin(\theta + \alpha)$$
其中辅助角 $\alpha$ 由坐标平面上的点 $P(a, b)$ 确定（$OP = r = \sqrt{a^2+b^2}$，$\alpha$ 为射线 $OP$ 与 $x$ 轴正方向的夹角）：
$$\cos\alpha = \frac{a}{\sqrt{a^2+b^2}}, \qquad \sin\alpha = \frac{b}{\sqrt{a^2+b^2}}, \qquad \tan\alpha = \frac{b}{a}\;\;(a\neq 0)$$
- $\alpha$ 通常取 $-\pi < \alpha \le \pi$ 或 $0 \le \alpha < 2\pi$。
- **日本教材独门画点法**：把 $\sin\theta$ 的系数 $a$ 作为**横坐标**，把 $\cos\theta$ 的系数 $b$ 作为**纵坐标**，在 $xy$ 平面上描出点 $P(a,b)$，一眼读出半径 $r$ 与角 $\alpha$！

### 1.4 直线与平面上的点（直線上の点、平面上の点）

1. **数轴上的内分点・外分点**：$A(a),\; B(b)$，$m>0,\; n>0$：
   - 内分点 $P$（$m:n$）：$x = \dfrac{na + mb}{m+n}$；中点：$x = \dfrac{a+b}{2}$。
   - 外分点 $Q$（$m:n,\; m\neq n$）：$x = \dfrac{-na + mb}{m-n}$（把内分公式中的 $n$ 换成 $-n$ 即可！）。
2. **坐标平面上两点距离**：$A(x_1,y_1),\; B(x_2,y_2)$：
   $$AB = \sqrt{(x_2-x_1)^2 + (y_2-y_1)^2}, \qquad OA = \sqrt{x_1^2 + y_1^2}$$
3. **坐标平面上的内分点・外分点・重心・对称点**：
   - 内分点 $P\left(\dfrac{nx_1+mx_2}{m+n},\; \dfrac{ny_1+my_2}{m+n}\right)$，中点 $M\left(\dfrac{x_1+x_2}{2},\; \dfrac{y_1+y_2}{2}\right)$，外分点 $Q\left(\dfrac{-nx_1+mx_2}{m-n},\; \dfrac{-ny_1+my_2}{m-n}\right)$。
   - $\triangle ABC$ 重心：$G\left(\dfrac{x_1+x_2+x_3}{3},\; \dfrac{y_1+y_2+y_3}{3}\right)$。
     > ⚠️ **教材勘误提示**：原教材第 143 页（`page_0144.jpg`）将重心 $G$ 的纵坐标误印为 $\dfrac{y_1+y_2+y_2}{3}$，应修正为 $\dfrac{y_1+y_2+y_3}{3}$；此外同页下方「点に関して対称な点」小节号重复印为 `[1.4]`（应为 `[1.5]`），框内「中心の座標」应为「中点の座標」。
   - 关于点 $A(a,b)$ 对称的两点 $P(x_1,y_1),\; Q(x_2,y_2)$ 满足：$a = \dfrac{x_1+x_2}{2},\; b = \dfrac{y_1+y_2}{2}$（即 $x_2 = 2a-x_1,\; y_2 = 2b-y_1$）。

### 1.5 直线方程与两直线的位置关系（直線の方程式、2直線の関係）

| 方程形式 | 公式 | 适用范围 / 备注 |
| :--- | :--- | :--- |
| **斜截式** | $y = mx + n$ | 斜率 $m$，$y$ 截距 $n$（不含垂直 $x$ 轴的直线） |
| **点斜式** | $y - y_1 = m(x - x_1)$ | 过 $(x_1, y_1)$，斜率 $m$；垂直 $x$ 轴时为 $x = x_1$ |
| **两点式** | $y - y_1 = \dfrac{y_2-y_1}{x_2-x_1}(x - x_1)$ | $x_1 \neq x_2$；统一形式：$(y_2-y_1)(x-x_1)-(x_2-x_1)(y-y_1)=0$ |
| **截距式** | $\dfrac{x}{a} + \dfrac{y}{b} = 1$ | 过 $(a,0),\; (0,b)$（$a \neq 0,\; b \neq 0$） |
| **一般式** | $ax + by + c = 0$ | $a \neq 0$ 或 $b \neq 0$，可表示平面内**任意**直线 |

- **两直线平行・垂直条件**：
  - 斜截式 $y = m_1x + n_1,\; y = m_2x + n_2$：
    - 平行（本教材含重合）：$m_1 = m_2$
    - 垂直：$m_1 m_2 = -1$
  - 一般式 $a_1x + b_1y + c_1 = 0,\; a_2x + b_2y + c_2 = 0$：
    - 平行（含重合）：$a_1 b_2 - a_2 b_1 = 0$
    - 垂直：$a_1 a_2 + b_1 b_2 = 0$（无需分类讨论斜率是否存在，**强烈推荐**！）

### 1.6 国内高中 vs. 日本 EJU 考纲差异与符号习惯

| 对比维度 | 国内高中习惯 | 日本 EJU 习惯 | 备课/应试提醒 |
| :--- | :--- | :--- | :--- |
| **三角函数合成** | 称「辅助角公式」，常凭代数硬提 $\sqrt{a^2+b^2}$ | 称 **三角関数の合成**，习惯用点 $P(a,b)$ 的几何坐标图定角 $\alpha$ | 画 $P(a,b)$ 极快且极难出错，尤其适合含负系数题（如 $-\frac{\sqrt{3}}{2}\sin\theta - \frac{1}{2}\cos\theta$） |
| **积化和差 / 和差化积** | 新课标已弱化为选学/拓展公式 | **EJU 数学Ⅱ・Ⅲ 必会工具**，常出现在三角方程与微积分大题中 | 必须会由加法定理 10 秒反推，不能只靠死记 |
| **斜截式字母** | $y = kx + b$ | **$y = mx + n$**（斜率用 $m$，$y$ 截距用 $n$） | 读题时看到「傾き $m$」切勿与直线斜率脱节 |
| **平行条件的定义** | 严格区分「平行」与「重合」（平行要求 $b_1 \neq b_2$） | 日本教科书常约定**平行条件包含一致（重合）**，若要排除重合会明确写「平行で異なる」 | 审题时务必看清「平行」是否注明「一致する場合を除く / 異なる」 |
| **外分点记忆** | 较少单独考定比分点公式，多用向量 | **高频直接考点**，交叉相乘 $\frac{-na+mb}{m-n}$ | 记住口诀：**内分「加交叉」，外分「把 $n$ 变 $-n$」** |

---

## 二、日文核心词汇与公式假名注音

### 2.1 本切片日文核心词汇

- 積和の公式（せきわのこうしき / sekiwa no koushiki） — 积化和差公式（本教材亦作 積→和の公式 / 積化和差）
- 和積の公式（わせきのこうしき / waseki no koushiki） — 和差化积公式（本教材亦作 和→積の公式 / 和差化積）
- 三角関数の合成（さんかくかんすうのごうせい / sankaku kansuu no gousei） — 三角函数的合成（辅助角公式）
- 解析幾何（かいせききか / kaiseki kika） — 解析几何（日本高中课纲称「図形と方程式」）
- 内分点（ないぶんてん / naibunten） — 内分点
- 外分点（がいぶんてん / gaibunten） — 外分点
- 座標平面（ざひょうへいめん / zahyou heimen） — 坐标平面（$xy$ 平面）
- 対称な点（たいしょうなてん / taishou na ten） — 对称点
- 直線の方程式（ちょくせんのほうていしき / chokusen no houteishiki） — 直线方程
- $x$ 切片（エックスせっぺん / ekkusu seppen） — $x$ 截距（横截距）
- $y$ 切片（ワイせっぺん / wai seppen） — $y$ 截距（纵截距）
- 平行条件（へいこうじょうけん / heikou jouken） — 平行条件
- 垂直条件（すいちょくじょうけん / suichoku jouken） — 垂直条件
- 一致する（いっちする / itchi suru） — 重合、一致
- 交点（こうてん / kouten） — 交点
- 無数の解（むすうのかい / musuu no kai） — 无穷多解

### 2.2 核心公式的日本课堂口语读法

1. **三角函数的合成** $a\sin\theta + b\cos\theta = \sqrt{a^2+b^2}\sin(\theta+\alpha)$
   - 课堂读法：**エー サイン シータ たす ビー コサイン シータ イコール ルート エーのにじょう たす ビーのにじょう、サイン かっこ シータ たす アルファ かっことじ**
2. **数轴内分点・外分点公式** $x = \dfrac{na+mb}{m+n},\; x = \dfrac{-na+mb}{m-n}$
   - 课堂读法：**エム たす エヌ ぶんの エヌ エー たす エム ビー**；外分点：**エム ひく エヌ ぶんの マイナス エヌ エー たす エム ビー**
3. **直线的点斜式** $y - y_1 = m(x - x_1)$
   - 课堂读法：**ワイ ひく ワイワン イコール エム かっこ エックス ひく エックスワン かっことじ**
4. **两直线垂直条件** $m_1 m_2 = -1$ / $a_1 a_2 + b_1 b_2 = 0$
   - 课堂读法：**エムワン エムツー イコール マイナスいち** / **エーワン エーツー たす ビーワン ビーツー イコール ゼロ**
5. **直线的截距式** $\dfrac{x}{a} + \dfrac{y}{b} = 1$
   - 课堂读法：**エー ぶんの エックス たす ビー ぶんの ワイ イコール いち**

---

## 三、逐题深度解析（不可跳步）

---

### 第六章 演習問題 4-(8)（万能公式の証明）

#### 演習問題 4-(8)
- **【原题重现与翻译】**
  - 原题：$t = \tan\dfrac{\theta}{2}$ のとき、次の等式が成り立つことを証明せよ。
    - [1] $\sin\theta = \dfrac{2t}{1+t^2}$
    - [2] $\cos\theta = \dfrac{1-t^2}{1+t^2}$
    - [3] $\tan\theta = \dfrac{2t}{1-t^2}$
  > ⚠️ **教材勘误提示**：原教材第 135 页（`page_0136.jpg`）题干误将「次の**等式**」印作「次の**不等式**」，显然应为「等式」。
  - 中文：当 $t = \tan\dfrac{\theta}{2}$ 时，证明下列等式成立：[1] $\sin\theta = \dfrac{2t}{1+t^2}$；[2] $\cos\theta = \dfrac{1-t^2}{1+t^2}$；[3] $\tan\theta = \dfrac{2t}{1-t^2}$。
- **【考点定位】**
  - 二倍角公式 + 齐次化（利用 $1 = \cos^2\frac{\theta}{2} + \sin^2\frac{\theta}{2}$ 分子分母同除 $\cos^2\frac{\theta}{2}$）。
- **【分步标准解答】**
  $t = \tan\dfrac{\theta}{2}$ が定義されるから、$\cos\dfrac{\theta}{2} \neq 0$ である。
  > 💡 讲师批注：证明前先交代 $\cos\frac{\theta}{2} \neq 0$，这样后续分子分母同除以 $\cos^2\frac{\theta}{2}$ 才完全严谨。

  **[1] $\sin\theta = \dfrac{2t}{1+t^2}$ の証明**
  $$\sin\theta = 2\sin\frac{\theta}{2}\cos\frac{\theta}{2} = \frac{2\sin\frac{\theta}{2}\cos\frac{\theta}{2}}{\cos^2\frac{\theta}{2} + \sin^2\frac{\theta}{2}}$$
  > 💡 讲师批注：把分母 $1$ 写成 $\cos^2\frac{\theta}{2} + \sin^2\frac{\theta}{2}$，使分子分母变为关于 $\sin\frac{\theta}{2},\; \cos\frac{\theta}{2}$ 的二次齐次式。

  分母・分子を $\cos^2\dfrac{\theta}{2}\;(\neq 0)$ で割ると、
  $$\sin\theta = \frac{2\tan\frac{\theta}{2}}{1 + \tan^2\frac{\theta}{2}} = \frac{2t}{1+t^2}$$

  **[2] $\cos\theta = \dfrac{1-t^2}{1+t^2}$ の証明**
  $$\cos\theta = \cos^2\frac{\theta}{2} - \sin^2\frac{\theta}{2} = \frac{\cos^2\frac{\theta}{2} - \sin^2\frac{\theta}{2}}{\cos^2\frac{\theta}{2} + \sin^2\frac{\theta}{2}}$$
  分母・分子を $\cos^2\dfrac{\theta}{2}\;(\neq 0)$ で割ると、
  $$\cos\theta = \frac{1 - \tan^2\frac{\theta}{2}}{1 + \tan^2\frac{\theta}{2}} = \frac{1-t^2}{1+t^2}$$
  > 💡 讲师批注：特值验算：取 $\theta = 60^\circ$，则 $t = \tan 30^\circ = \frac{1}{\sqrt{3}}$，代入得 $\sin 60^\circ = \frac{2/\sqrt{3}}{4/3} = \frac{\sqrt{3}}{2}$，$\cos 60^\circ = \frac{2/3}{4/3} = \frac{1}{2}$，完全吻合。

  **[3] $\tan\theta = \dfrac{2t}{1-t^2}$ の証明**
  $\cos\theta \neq 0$（すなわち $t \neq \pm 1$）のとき、[1], [2] より
  $$\tan\theta = \frac{\sin\theta}{\cos\theta} = \frac{\dfrac{2t}{1+t^2}}{\dfrac{1-t^2}{1+t^2}} = \frac{2t}{1-t^2}$$
  > 💡 讲师批注：也可以直接对 $\theta = 2 \cdot \frac{\theta}{2}$ 应用 $\tan$ 的二倍角公式 $\tan\theta = \dfrac{2\tan\frac{\theta}{2}}{1-\tan^2\frac{\theta}{2}} = \dfrac{2t}{1-t^2}$，一步到位！
- **【最终答案】**
  **証明終わり（Q.E.D.）**

---

### 第六章 教材例题（三角関数の合成，P138）

#### 例題（三角関数の合成）
- **【原题重现与翻译】**
  - 原题：$\sqrt{3}\sin\theta + \cos\theta$ を $r\sin(\theta+\alpha)$ の形に変形する。
  - 中文：将 $\sqrt{3}\sin\theta + \cos\theta$ 变形为 $r\sin(\theta+\alpha)$ 的形式。
- **【考点定位】**
  - 三角函数合成的几何作图法：$P(a, b) \Rightarrow r = OP,\; \alpha = \angle xOP$。
- **【图解辅助（SVG 矢量图）】**
  参考教材第 137 页（`page_0138.jpg`），用点 $P(\sqrt{3}, 1)$ 定位 $r=2$ 与 $\alpha = \frac{\pi}{6}$：

<svg viewBox="0 0 460 220" width="460" height="220" xmlns="http://www.w3.org/2000/svg" style="background:#fafafa;border:1px solid #e0e0e0;border-radius:6px;">
  <style>
    .axis { stroke: #34495e; stroke-width: 1.5; }
    .tri { fill: #eaf4fc; stroke: #2980b9; stroke-width: 2; }
    .dash { stroke: #7f8c8d; stroke-width: 1.2; stroke-dasharray: 4 3; }
    .lbl { font: 13px sans-serif; fill: #2c3e50; }
    .hl { font: bold 13px sans-serif; fill: #c0392b; }
    .note { font: 12px sans-serif; fill: #555; }
  </style>
  <defs>
    <marker id="arr10a" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#34495e"/>
    </marker>
  </defs>
  <!-- Axes -->
  <line x1="40" y1="175" x2="290" y2="175" class="axis" marker-end="url(#arr10a)"/>
  <line x1="80" y1="200" x2="80" y2="25" class="axis" marker-end="url(#arr10a)"/>
  <text x="296" y="179" class="lbl">x</text>
  <text x="74" y="18" class="lbl">y</text>
  <text x="64" y="191" class="lbl">O</text>
  <!-- Triangle O-H-P: scale 1 unit = 90px => sqrt(3) ~ 156px, 1 = 90px -->
  <polygon points="80,175 236,175 236,85" class="tri"/>
  <!-- Right angle mark -->
  <polyline points="224,175 224,163 236,163" fill="none" stroke="#2980b9" stroke-width="1.3"/>
  <!-- Angle arc -->
  <path d="M 122 175 A 42 42 0 0 0 116 154" fill="none" stroke="#c0392b" stroke-width="1.8"/>
  <text x="128" y="168" class="hl">α = π/6</text>
  <!-- Point P -->
  <circle cx="236" cy="85" r="4" fill="#c0392b"/>
  <text x="242" y="78" class="hl">P(√3, 1)</text>
  <!-- Side labels -->
  <text x="150" y="193" class="lbl">a = √3</text>
  <text x="244" y="135" class="lbl">b = 1</text>
  <text x="132" y="118" class="hl">r = 2</text>
  <!-- Right explanation box -->
  <rect x="308" y="42" width="140" height="126" rx="6" fill="#fff" stroke="#dcdcdc"/>
  <text x="318" y="66" class="hl">合成ステップ</text>
  <text x="318" y="90" class="note">① sin係数 a = √3</text>
  <text x="318" y="110" class="note">② cos係数 b = 1</text>
  <text x="318" y="130" class="note">③ r = √(3+1) = 2</text>
  <text x="318" y="150" class="note">④ α = π/6 (30°)</text>
</svg>

- **【分步标准解答】**
  点 $P(\sqrt{3},\; 1)$ をとると、
  $$OP = \sqrt{(\sqrt{3})^2 + 1^2} = \sqrt{4} = 2$$
  線分 $OP$ が $x$ 軸の正の向きとなす角は $\alpha = \dfrac{\pi}{6}$ であるから、
  $$\sqrt{3}\sin\theta + \cos\theta = 2\left(\frac{\sqrt{3}}{2}\sin\theta + \frac{1}{2}\cos\theta\right) = 2\left(\sin\theta\cos\frac{\pi}{6} + \cos\theta\sin\frac{\pi}{6}\right) = 2\sin\left(\theta + \frac{\pi}{6}\right)$$
  > 💡 讲师批注：切记横坐标对应 $\sin\theta$ 的系数，纵坐标对应 $\cos\theta$ 的系数！切勿看反。
- **【最终答案】**
  **$2\sin\left(\theta + \dfrac{\pi}{6}\right)$**

---

### 第六章 演習問題 5（和積公式・合成の総合演習）

#### 演習問題 5-(1)
- **【原题重现与翻译】**
  - 原题：積化和差、和差化積の公式を用いて、次の値を求めよ。
    - [1] $\sin 75^\circ \cos 15^\circ$　　[2] $\sin 75^\circ + \sin 15^\circ$　　[3] $\cos 20^\circ \cos 40^\circ \cos 80^\circ$
    - [4] $\sin 75^\circ \cos 45^\circ$　　[5] $\cos 105^\circ - \cos 15^\circ$　　[6] $\sin 20^\circ \sin 40^\circ \sin 80^\circ$
  - 中文：利用积化和差、和差化积公式，求下列各式的值。
- **【考点定位】**
  - 积化和差与和差化积公式的直接计算与连乘技巧。
- **【分步标准解答】**

  **[1] $\sin 75^\circ \cos 15^\circ$**
  $$\sin 75^\circ \cos 15^\circ = \frac{1}{2}\left\{\sin(75^\circ + 15^\circ) + \sin(75^\circ - 15^\circ)\right\}$$
  $$= \frac{1}{2}(\sin 90^\circ + \sin 60^\circ) = \frac{1}{2}\left(1 + \frac{\sqrt{3}}{2}\right) = \frac{2 + \sqrt{3}}{4}$$
  > 💡 讲师批注：套用 $\sin\alpha\cos\beta = \frac{1}{2}\{\sin(\alpha+\beta)+\sin(\alpha-\beta)\}$，把非特殊角 $75^\circ, 15^\circ$ 转化为特殊角 $90^\circ, 60^\circ$。

  **[2] $\sin 75^\circ + \sin 15^\circ$**
  $$\sin 75^\circ + \sin 15^\circ = 2\sin\frac{75^\circ + 15^\circ}{2}\cos\frac{75^\circ - 15^\circ}{2}$$
  $$= 2\sin 45^\circ \cos 30^\circ = 2 \cdot \frac{\sqrt{2}}{2} \cdot \frac{\sqrt{3}}{2} = \frac{\sqrt{6}}{2}$$

  **[3] $\cos 20^\circ \cos 40^\circ \cos 80^\circ$**
  $$\cos 20^\circ \cos 40^\circ \cos 80^\circ = \cos 20^\circ \cdot \frac{1}{2}\left\{\cos(80^\circ + 40^\circ) + \cos(80^\circ - 40^\circ)\right\}$$
  > 💡 讲师批注：先结合 $40^\circ$ 与 $80^\circ$，因为 $80^\circ + 40^\circ = 120^\circ$ 是特殊角！
  $$= \frac{1}{2}\cos 20^\circ (\cos 120^\circ + \cos 40^\circ) = \frac{1}{2}\cos 20^\circ\left(-\frac{1}{2} + \cos 40^\circ\right)$$
  $$= -\frac{1}{4}\cos 20^\circ + \frac{1}{2}\cos 40^\circ \cos 20^\circ$$
  $$= -\frac{1}{4}\cos 20^\circ + \frac{1}{2} \cdot \frac{1}{2}(\cos 60^\circ + \cos 20^\circ)$$
  $$= -\frac{1}{4}\cos 20^\circ + \frac{1}{4}\cos 60^\circ + \frac{1}{4}\cos 20^\circ = \frac{1}{4} \cdot \frac{1}{2} = \frac{1}{8}$$
  > 💡 讲师批注：**经典验算（二倍角连乘法）**：分子分母同乘 $8\sin 20^\circ$，得 $\dfrac{8\sin 20^\circ\cos 20^\circ\cos 40^\circ\cos 80^\circ}{8\sin 20^\circ} = \dfrac{\sin 160^\circ}{8\sin 20^\circ} = \dfrac{1}{8}$，结果完全一致！

  **[4] $\sin 75^\circ \cos 45^\circ$**
  $$\sin 75^\circ \cos 45^\circ = \frac{1}{2}\left\{\sin(75^\circ + 45^\circ) + \sin(75^\circ - 45^\circ)\right\}$$
  $$= \frac{1}{2}(\sin 120^\circ + \sin 30^\circ) = \frac{1}{2}\left(\frac{\sqrt{3}}{2} + \frac{1}{2}\right) = \frac{\sqrt{3} + 1}{4}$$

  **[5] $\cos 105^\circ - \cos 15^\circ$**
  $$\cos 105^\circ - \cos 15^\circ = -2\sin\frac{105^\circ + 15^\circ}{2}\sin\frac{105^\circ - 15^\circ}{2}$$
  $$= -2\sin 60^\circ \sin 45^\circ = -2 \cdot \frac{\sqrt{3}}{2} \cdot \frac{\sqrt{2}}{2} = -\frac{\sqrt{6}}{2}$$
  > 💡 讲师批注：务必检查符号！$\cos 105^\circ < 0$，$\cos 15^\circ > 0$，故差必为负数，切勿漏掉公式前方的负号。

  **[6] $\sin 20^\circ \sin 40^\circ \sin 80^\circ$**
  $$\sin 20^\circ \sin 40^\circ \sin 80^\circ = \sin 20^\circ \cdot \left(-\frac{1}{2}\right)\left\{\cos(80^\circ + 40^\circ) - \cos(80^\circ - 40^\circ)\right\}$$
  $$= -\frac{1}{2}\sin 20^\circ (\cos 120^\circ - \cos 40^\circ) = -\frac{1}{2}\sin 20^\circ \left(-\frac{1}{2} - \cos 40^\circ\right)$$
  $$= \frac{1}{4}\sin 20^\circ + \frac{1}{2}\cos 40^\circ \sin 20^\circ$$
  $$= \frac{1}{4}\sin 20^\circ + \frac{1}{2} \cdot \frac{1}{2}\left\{\sin(40^\circ + 20^\circ) - \sin(40^\circ - 20^\circ)\right\}$$
  $$= \frac{1}{4}\sin 20^\circ + \frac{1}{4}\sin 60^\circ - \frac{1}{4}\sin 20^\circ = \frac{1}{4} \cdot \frac{\sqrt{3}}{2} = \frac{\sqrt{3}}{8}$$
  > 💡 讲师批注：注意 $\sin 20^\circ$ 与 $-\frac{1}{4}\sin 20^\circ$ 再次完美抵消！记住一组高频结论：$\cos 20^\circ\cos 40^\circ\cos 80^\circ = \frac{1}{8}$，$\sin 20^\circ\sin 40^\circ\sin 80^\circ = \frac{\sqrt{3}}{8}$，$\tan 20^\circ\tan 40^\circ\tan 80^\circ = \sqrt{3}$。
- **【最终答案】**
  **[1] $\dfrac{2+\sqrt{3}}{4}$　[2] $\dfrac{\sqrt{6}}{2}$　[3] $\dfrac{1}{8}$　[4] $\dfrac{\sqrt{3}+1}{4}$　[5] $-\dfrac{\sqrt{6}}{2}$　[6] $\dfrac{\sqrt{3}}{8}$**

---

#### 演習問題 5-(2)
- **【原题重现与翻译】**
  - 原题：次の関数の最大値と最小値を求めよ。また、その時の $\theta$ の値を求めよ。ただし、$0 \le \theta \le \pi$ とする。
    - [1] $y = \cos\theta - \sin\theta$
    - [2] $y = \sin\left(\theta + \dfrac{5}{6}\pi\right) - \cos\theta$
  - 中文：求下列函数的最大值与最小值，并求取最值时的 $\theta$ 值。其中 $0 \le \theta \le \pi$。
- **【考点定位】**
  - 加法定理展开 + 三角函数的合成 + 单位圆区间求最值。
- **【图解辅助（SVG 矢量图）】**
  在单位圆上分别标出 [1] 中 $\phi_1 = \theta + \frac{3}{4}\pi \in [\frac{3}{4}\pi, \frac{7}{4}\pi]$ 与 [2] 中 $\phi_2 = \theta - \frac{5}{6}\pi \in [-\frac{5}{6}\pi, \frac{\pi}{6}]$ 的动径扫过弧段（粗蓝弧），一眼锁定纵坐标 $\sin\phi$ 的最大・最小值：

<svg viewBox="0 0 560 230" width="560" height="230" xmlns="http://www.w3.org/2000/svg" style="background:#fafafa;border:1px solid #e0e0e0;border-radius:6px;">
  <style>
    .ttl { font: bold 13px sans-serif; fill: #2c3e50; }
    .ax { stroke: #95a5a6; stroke-width: 1.2; }
    .circ { fill: none; stroke: #bdc3c7; stroke-width: 1.5; }
    .arc { fill: none; stroke: #2980b9; stroke-width: 4; stroke-linecap: round; }
    .pt-max { fill: #e74c3c; }
    .pt-min { fill: #27ae60; }
    .lbl { font: 11px sans-serif; fill: #2c3e50; }
    .hl-r { font: bold 11px sans-serif; fill: #c0392b; }
    .hl-g { font: bold 11px sans-serif; fill: #1e8449; }
  </style>
  <!-- Left: [1] -->
  <text x="16" y="22" class="ttl">[1] φ₁ = θ + 3π/4 ∈ [3π/4, 7π/4]</text>
  <line x1="40" y1="125" x2="230" y2="125" class="ax"/>
  <line x1="135" y1="210" x2="135" y2="38" class="ax"/>
  <circle cx="135" cy="125" r="68" class="circ"/>
  <!-- Arc from 3pi/4 (135-48, 125-48)=(87,77) counterclockwise to 7pi/4 (135+48, 125+48)=(183,173) -->
  <path d="M 87 77 A 68 68 0 0 0 183 173" class="arc"/>
  <!-- Max at 3pi/4 -->
  <circle cx="87" cy="77" r="4.5" class="pt-max"/>
  <text x="14" y="72" class="hl-r">Max: φ₁=3π/4</text>
  <text x="14" y="86" class="lbl">(sin = √2/2)</text>
  <!-- Min at 3pi/2 -->
  <circle cx="135" cy="193" r="4.5" class="pt-min"/>
  <text x="90" y="212" class="hl-g">Min: φ₁=3π/2 (sin = -1)</text>
  <!-- Endpoint 7pi/4 -->
  <circle cx="183" cy="173" r="3.5" fill="#2980b9"/>
  <text x="190" y="178" class="lbl">7π/4</text>

  <!-- Divider -->
  <line x1="280" y1="15" x2="280" y2="215" stroke="#e0e0e0" stroke-dasharray="4 4"/>

  <!-- Right: [2] -->
  <text x="296" y="22" class="ttl">[2] φ₂ = θ - 5π/6 ∈ [-5π/6, π/6]</text>
  <line x1="320" y1="125" x2="510" y2="125" class="ax"/>
  <line x1="415" y1="210" x2="415" y2="38" class="ax"/>
  <circle cx="415" cy="125" r="68" class="circ"/>
  <!-- Arc from -5pi/6 (415-58.9, 125+34)=(356,159) counterclockwise to pi/6 (415+58.9, 125-34)=(474,91) -->
  <path d="M 356 159 A 68 68 0 0 0 474 91" class="arc"/>
  <!-- Max at pi/6 -->
  <circle cx="474" cy="91" r="4.5" class="pt-max"/>
  <text x="452" y="72" class="hl-r">Max: φ₂=π/6</text>
  <text x="460" y="85" class="lbl">(sin = 1/2)</text>
  <!-- Min at -pi/2 -->
  <circle cx="415" cy="193" r="4.5" class="pt-min"/>
  <text x="366" y="212" class="hl-g">Min: φ₂=-π/2 (sin = -1)</text>
  <!-- Endpoint -5pi/6 -->
  <circle cx="356" cy="159" r="3.5" fill="#2980b9"/>
  <text x="304" y="164" class="lbl">-5π/6</text>
</svg>

- **【分步标准解答】**

  **[1] $y = \cos\theta - \sin\theta$**
  $$y = -\sin\theta + \cos\theta$$
  点 $P(-1, 1)$ は $OP = \sqrt{(-1)^2 + 1^2} = \sqrt{2}$、$x$ 軸の正の向きとなす角が $\dfrac{3}{4}\pi$ であるから、
  $$y = \sqrt{2}\sin\left(\theta + \frac{3}{4}\pi\right)$$
  > 💡 讲师批注：务必先把 $\sin\theta$ 写在前面（$-\sin\theta + \cos\theta$），再读取点 $P(-1, 1)$！最常见错误是直接按原序看成 $P(1, -1)$。

  $0 \le \theta \le \pi$ より、$\dfrac{3}{4}\pi \le \theta + \dfrac{3}{4}\pi \le \dfrac{7}{4}\pi$。
  単位円より、この範囲で $\sin\left(\theta + \dfrac{3}{4}\pi\right)$ は：
  - $\theta + \dfrac{3}{4}\pi = \dfrac{3}{4}\pi$、すなわち $\theta = 0$ のとき最大値 $\dfrac{\sqrt{2}}{2}$ をとる。よって $y$ の最大値は $\sqrt{2} \cdot \dfrac{\sqrt{2}}{2} = 1$。
  - $\theta + \dfrac{3}{4}\pi = \dfrac{3}{2}\pi$、すなわち $\theta = \dfrac{3}{4}\pi$ のとき最小値 $-1$ をとる。よって $y$ の最小値は $\sqrt{2} \cdot (-1) = -\sqrt{2}$。

  **[2] $y = \sin\left(\theta + \dfrac{5}{6}\pi\right) - \cos\theta$**
  加法定理を用いて展開すると、
  $$y = \sin\theta\cos\frac{5}{6}\pi + \cos\theta\sin\frac{5}{6}\pi - \cos\theta$$
  $$= -\frac{\sqrt{3}}{2}\sin\theta + \frac{1}{2}\cos\theta - \cos\theta = -\frac{\sqrt{3}}{2}\sin\theta - \frac{1}{2}\cos\theta$$
  点 $P\left(-\dfrac{\sqrt{3}}{2},\; -\dfrac{1}{2}\right)$ は $OP = \sqrt{\left(-\dfrac{\sqrt{3}}{2}\right)^2 + \left(-\dfrac{1}{2}\right)^2} = 1$、$x$ 軸の正の向きとなす角が $-\dfrac{5}{6}\pi$ であるから、
  $$y = \sin\left(\theta - \frac{5}{6}\pi\right)$$
  $0 \le \theta \le \pi$ より、$-\dfrac{5}{6}\pi \le \theta - \dfrac{5}{6}\pi \le \dfrac{\pi}{6}$。
  単位円より、この範囲で $\sin\left(\theta - \dfrac{5}{6}\pi\right)$ は：
  - $\theta - \dfrac{5}{6}\pi = \dfrac{\pi}{6}$、すなわち $\theta = \pi$ のとき最大値 $\sin\dfrac{\pi}{6} = \dfrac{1}{2}$。
  - $\theta - \dfrac{5}{6}\pi = -\dfrac{\pi}{2}$、すなわち $\theta = \dfrac{\pi}{3}$ のとき最小値 $\sin\left(-\dfrac{\pi}{2}\right) = -1$。
  > 💡 讲师批注：代入验算：$\theta = \pi$ 时 $\sin\frac{11}{6}\pi - \cos\pi = -\frac{1}{2} - (-1) = \frac{1}{2}$；$\theta = \frac{\pi}{3}$ 时 $\sin\frac{7}{6}\pi - \cos\frac{\pi}{3} = -\frac{1}{2} - \frac{1}{2} = -1$，100% 准确！
- **【最终答案】**
  - **[1] 最大値 $1$（$\theta = 0$ のとき），最小値 $-\sqrt{2}$（$\theta = \dfrac{3}{4}\pi$ のとき）**
  - **[2] 最大値 $\dfrac{1}{2}$（$\theta = \pi$ のとき），最小値 $-1$（$\theta = \dfrac{\pi}{3}$ のとき）**

---

#### 演習問題 5-(3)
- **【原题重现与翻译】**
  - 原题：$\triangle ABC$ において、次の等式が成り立つことを証明せよ。
    - [1] $\sin A + \sin B + \sin C = 4\cos\dfrac{A}{2}\cos\dfrac{B}{2}\cos\dfrac{C}{2}$
    - [2] $\cos A + \cos B - \cos C = 4\cos\dfrac{A}{2}\cos\dfrac{B}{2}\sin\dfrac{C}{2} - 1$
  - 中文：在 $\triangle ABC$ 中，证明下列等式成立。
- **【考点定位】**
  - 三角形内角和关系 $A+B+C = \pi$（$\dfrac{A+B}{2} = \dfrac{\pi}{2} - \dfrac{C}{2}$）与和差化积・二倍角公式的综合证明。
- **【分步标准解答】**
  $\triangle ABC$ において $A + B + C = \pi$ より、$\dfrac{A+B}{2} = \dfrac{\pi}{2} - \dfrac{C}{2}$ であるから、
  $$\sin\frac{A+B}{2} = \cos\frac{C}{2}, \qquad \cos\frac{A+B}{2} = \sin\frac{C}{2}$$
  > 💡 讲师批注：这两条诱导公式是三角形恒等式证明的「黄金桥梁」，先写在开头，后面提取公因式水到渠成。

  **[1] $\sin A + \sin B + \sin C = 4\cos\dfrac{A}{2}\cos\dfrac{B}{2}\cos\dfrac{C}{2}$ の証明**
  $$(\text{左辺}) = (\sin A + \sin B) + \sin C$$
  $$= 2\sin\frac{A+B}{2}\cos\frac{A-B}{2} + 2\sin\frac{C}{2}\cos\frac{C}{2}$$
  > 💡 讲师批注：前两项用和差化积，第三项 $\sin C$ 用二倍角公式拆成半角 $\frac{C}{2}$。
  $$= 2\cos\frac{C}{2}\cos\frac{A-B}{2} + 2\cos\frac{A+B}{2}\cos\frac{C}{2}$$
  $$= 2\cos\frac{C}{2}\left(\cos\frac{A-B}{2} + \cos\frac{A+B}{2}\right)$$
  $$= 2\cos\frac{C}{2} \cdot 2\cos\frac{A}{2}\cos\frac{B}{2} = 4\cos\frac{A}{2}\cos\frac{B}{2}\cos\frac{C}{2} = (\text{右辺})$$

  **[2] $\cos A + \cos B - \cos C = 4\cos\dfrac{A}{2}\cos\dfrac{B}{2}\sin\dfrac{C}{2} - 1$ の証明**
  $$(\text{左辺}) = (\cos A + \cos B) - \cos C$$
  $$= 2\cos\frac{A+B}{2}\cos\frac{A-B}{2} - \left(1 - 2\sin^2\frac{C}{2}\right)$$
  > 💡 讲师批注：右侧出现了 $-1$ 和 $\sin\frac{C}{2}$，因此将 $\cos C$ 展开为 $1 - 2\sin^2\frac{C}{2}$，既凑出 $-1$ 又凑出公因式 $2\sin\frac{C}{2}$！
  $$= 2\sin\frac{C}{2}\cos\frac{A-B}{2} + 2\sin^2\frac{C}{2} - 1$$
  $$= 2\sin\frac{C}{2}\left(\cos\frac{A-B}{2} + \sin\frac{C}{2}\right) - 1$$
  $$= 2\sin\frac{C}{2}\left(\cos\frac{A-B}{2} + \cos\frac{A+B}{2}\right) - 1$$
  $$= 2\sin\frac{C}{2} \cdot 2\cos\frac{A}{2}\cos\frac{B}{2} - 1 = 4\cos\frac{A}{2}\cos\frac{B}{2}\sin\frac{C}{2} - 1 = (\text{右辺})$$
- **【最终答案】**
  **証明終わり（Q.E.D.）**

---

#### 演習問題 5-(4)
- **【原题重现与翻译】**
  - 原题：$0 \le \theta \le \pi$ のとき、次の方程式、不等式を解け。
    - [1] $\sin 2\theta + \sin 3\theta + \sin 4\theta = 0$
    - [2] $\cos\theta + \sqrt{3}\sin\theta + 1 = 0$
    - [3] $\cos 2\theta + \sin 2\theta + 1 > 0$
  - 中文：当 $0 \le \theta \le \pi$ 时，解下列方程与不等式。
- **【考点定位】**
  - 和差化积因式分解解三角方程、三角函数合成解三角方程与不等式。
- **【图解辅助（SVG 矢量图）】**
  针对最易漏解/错边界的 [3] $\sin\left(2\theta + \frac{\pi}{4}\right) > -\frac{1}{\sqrt{2}}$（$\frac{\pi}{4} \le 2\theta + \frac{\pi}{4} \le \frac{9}{4}\pi$），用单位圆清晰标出满足条件的弧段：

<svg viewBox="0 0 460 220" width="460" height="220" xmlns="http://www.w3.org/2000/svg" style="background:#fafafa;border:1px solid #e0e0e0;border-radius:6px;">
  <style>
    .ttl { font: bold 13px sans-serif; fill: #2c3e50; }
    .ax { stroke: #95a5a6; stroke-width: 1.2; }
    .circ { fill: none; stroke: #bdc3c7; stroke-width: 1.5; }
    .arc-ok { fill: none; stroke: #2980b9; stroke-width: 4; }
    .cut { stroke: #e74c3c; stroke-width: 1.5; stroke-dasharray: 5 3; }
    .lbl { font: 11px sans-serif; fill: #2c3e50; }
    .hl { font: bold 11px sans-serif; fill: #c0392b; }
  </style>
  <text x="16" y="22" class="ttl">[3] φ = 2θ + π/4 ∈ [π/4, 9π/4] で sin φ > -1/√2</text>
  <line x1="40" y1="115" x2="250" y2="115" class="ax"/>
  <line x1="145" y1="205" x2="145" y2="32" class="ax"/>
  <circle cx="145" cy="115" r="68" class="circ"/>
  <!-- Line y = -1/sqrt(2) => y = 115 + 48 = 163 -->
  <line x1="55" y1="163" x2="235" y2="163" class="cut"/>
  <text x="238" y="167" class="hl">y = -1/√2</text>
  <!-- Valid arc 1: pi/4 (193,67) CCW to 5pi/4 (97,163) -->
  <path d="M 193 67 A 68 68 0 0 0 97 163" class="arc-ok"/>
  <!-- Valid arc 2: 7pi/4 (193,163) CCW to 9pi/4 (193,67) -->
  <path d="M 193 163 A 68 68 0 0 0 193 67" class="arc-ok"/>
  <!-- Points -->
  <circle cx="193" cy="67" r="4" fill="#2980b9"/>
  <text x="200" y="64" class="lbl">π/4 (9π/4) ●</text>
  <circle cx="97" cy="163" r="4" fill="#fff" stroke="#e74c3c" stroke-width="2"/>
  <text x="58" y="179" class="hl">5π/4 ○</text>
  <circle cx="193" cy="163" r="4" fill="#fff" stroke="#e74c3c" stroke-width="2"/>
  <text x="196" y="182" class="hl">7π/4 ○</text>
  <!-- Summary box -->
  <rect x="295" y="48" width="152" height="122" rx="6" fill="#fff" stroke="#dcdcdc"/>
  <text x="305" y="70" class="ttl">解の範囲（2区間）</text>
  <text x="305" y="96" class="lbl">① π/4 ≤ φ &lt; 5π/4</text>
  <text x="315" y="114" class="hl">⇒ 0 ≤ θ &lt; π/2</text>
  <text x="305" y="140" class="lbl">② 7π/4 &lt; φ ≤ 9π/4</text>
  <text x="315" y="158" class="hl">⇒ 3π/4 &lt; θ ≤ π</text>
</svg>

- **【分步标准解答】**

  **[1] $\sin 2\theta + \sin 3\theta + \sin 4\theta = 0$**
  $\sin 4\theta$ と $\sin 2\theta$ を組み合わせて和→積の公式を適用すると、
  $$(\sin 4\theta + \sin 2\theta) + \sin 3\theta = 0$$
  $$2\sin 3\theta \cos\theta + \sin 3\theta = 0$$
  $$\sin 3\theta (2\cos\theta + 1) = 0$$
  > 💡 讲师批注：把平均角为 $3\theta$ 的两项 $4\theta$ 与 $2\theta$ 配对，立刻提取出公因式 $\sin 3\theta$！
  よって、$\sin 3\theta = 0$ または $\cos\theta = -\dfrac{1}{2}$。
  $0 \le \theta \le \pi$ の範囲で解くと：
  - $\sin 3\theta = 0$（$0 \le 3\theta \le 3\pi$）より、$3\theta = 0,\; \pi,\; 2\pi,\; 3\pi \implies \theta = 0,\; \dfrac{\pi}{3},\; \dfrac{2}{3}\pi,\; \pi$。
  - $\cos\theta = -\dfrac{1}{2}$ より、$\theta = \dfrac{2}{3}\pi$（上と重複）。
  したがって、$\theta = 0,\; \dfrac{\pi}{3},\; \dfrac{2}{3}\pi,\; \pi$。

  **[2] $\cos\theta + \sqrt{3}\sin\theta + 1 = 0$**
  $$\sqrt{3}\sin\theta + \cos\theta = -1$$
  左辺を合成すると、
  $$2\sin\left(\theta + \frac{\pi}{6}\right) = -1 \iff \sin\left(\theta + \frac{\pi}{6}\right) = -\frac{1}{2}$$
  $0 \le \theta \le \pi$ より、$\dfrac{\pi}{6} \le \theta + \dfrac{\pi}{6} \le \dfrac{7}{6}\pi$。
  この範囲で $\sin\left(\theta + \dfrac{\pi}{6}\right) = -\dfrac{1}{2}$ を満たすのは、
  $$\theta + \frac{\pi}{6} = \frac{7}{6}\pi \implies \theta = \pi$$
  > 💡 讲师批注：千万注意区间上界是 $\frac{7}{6}\pi$（闭区间），恰好包含端点解 $\theta = \pi$，而 $\frac{11}{6}\pi$ 超出范围应舍去。

  **[3] $\cos 2\theta + \sin 2\theta + 1 > 0$**
  $$\sin 2\theta + \cos 2\theta > -1$$
  左辺を合成すると、
  $$\sqrt{2}\sin\left(2\theta + \frac{\pi}{4}\right) > -1 \iff \sin\left(2\theta + \frac{\pi}{4}\right) > -\frac{1}{\sqrt{2}}$$
  $0 \le \theta \le \pi$ より、$\dfrac{\pi}{4} \le 2\theta + \dfrac{\pi}{4} \le \dfrac{9}{4}\pi$。
  単位円より、この範囲で不等式を満たすのは、
  $$\frac{\pi}{4} \le 2\theta + \frac{\pi}{4} < \frac{5}{4}\pi \quad \text{または} \quad \frac{7}{4}\pi < 2\theta + \frac{\pi}{4} \le \frac{9}{4}\pi$$
  各辺から $\dfrac{\pi}{4}$ を引き、$2$ で割ると、
  $$0 \le \theta < \frac{\pi}{2}, \qquad \frac{3}{4}\pi < \theta \le \pi$$
- **【最终答案】**
  - **[1] $\theta = 0,\; \dfrac{\pi}{3},\; \dfrac{2}{3}\pi,\; \pi$**
  - **[2] $\theta = \pi$**
  - **[3] $0 \le \theta < \dfrac{\pi}{2},\; \dfrac{3}{4}\pi < \theta \le \pi$**

---

#### 演習問題 5-(5)
- **【原题重现与翻译】**
  - 原题：$f(\theta) = \sin 2\theta + 2(\sin\theta + \cos\theta) - 1$ を考える。ただし、$0 \le \theta < 2\pi$ とする。
    - [1] $t = \sin\theta + \cos\theta$ と置くとき、$f(\theta)$ を $t$ の式で表せ。
    - [2] $t$ の取りうる値の範囲を求めよ。
    - [3] $f(\theta)$ の最大値と最小値を求め、その時の $\theta$ の値を求めよ。
  - 中文：考虑函数 $f(\theta) = \sin 2\theta + 2(\sin\theta + \cos\theta) - 1$（$0 \le \theta < 2\pi$）。
    - [1] 令 $t = \sin\theta + \cos\theta$，用 $t$ 表示 $f(\theta)$。
    - [2] 求 $t$ 的取值范围。
    - [3] 求 $f(\theta)$ 的最大值与最小值，以及取最值时的 $\theta$ 值。
- **【考点定位】**
  - EJU 最高频压轴模板题：**「和积换元法」**（$t = \sin\theta + \cos\theta \implies \sin 2\theta = t^2 - 1$）+ 三角函数合成定定义域 + 闭区间二次函数最值。
- **【图解辅助（SVG 矢量图）】**
  抛物线 $g(t) = (t+1)^2 - 3$ 在闭区间 $[-\sqrt{2},\; \sqrt{2}]$ 上的最值分布：

<svg viewBox="0 0 460 220" width="460" height="220" xmlns="http://www.w3.org/2000/svg" style="background:#fafafa;border:1px solid #e0e0e0;border-radius:6px;">
  <style>
    .ttl { font: bold 13px sans-serif; fill: #2c3e50; }
    .ax { stroke: #7f8c8d; stroke-width: 1.3; }
    .dash { stroke: #95a5a6; stroke-width: 1.2; stroke-dasharray: 4 3; }
    .curve-bg { fill: none; stroke: #bdc3c7; stroke-width: 1.5; stroke-dasharray: 4 3; }
    .curve-ok { fill: none; stroke: #2980b9; stroke-width: 3; }
    .lbl { font: 11px sans-serif; fill: #2c3e50; }
    .hl-r { font: bold 11px sans-serif; fill: #c0392b; }
    .hl-g { font: bold 11px sans-serif; fill: #1e8449; }
  </style>
  <text x="16" y="22" class="ttl">g(t) = (t + 1)² - 3　(-√2 ≤ t ≤ √2)</text>
  <!-- Coordinate system: origin at (210, 120), x-scale 65px/unit, y-scale 24px/unit -->
  <line x1="60" y1="120" x2="365" y2="120" class="ax"/>
  <line x1="210" y1="208" x2="210" y2="34" class="ax"/>
  <text x="370" y="124" class="lbl">t</text>
  <text x="215" y="42" class="lbl">g(t)</text>
  <text x="214" y="133" class="lbl">O</text>
  <line x1="145" y1="42" x2="145" y2="202" class="dash"/>
  <line x1="302" y1="52" x2="302" y2="120" class="dash"/>
  <line x1="118" y1="120" x2="118" y2="188" class="dash"/>
  <path d="M 118 188 Q 210 216 302 52" class="curve-ok"/>
  <!-- Max point (sqrt(2), 2sqrt(2)) -->
  <circle cx="302" cy="52" r="4.5" fill="#e74c3c"/>
  <text x="310" y="50" class="hl-r">Max = 2√2</text>
  <text x="310" y="64" class="lbl">(t = √2)</text>
  <text x="295" y="134" class="lbl">√2</text>
  <!-- Min point (-1, -3) -->
  <circle cx="145" cy="192" r="4.5" fill="#27ae60"/>
  <text x="154" y="205" class="hl-g">Min = -3 (t = -1)</text>
  <text x="137" y="114" class="lbl">-1</text>
  <!-- Left endpoint (-sqrt(2), -2sqrt(2)) -->
  <circle cx="118" cy="188" r="3.5" fill="#2980b9"/>
  <text x="95" y="114" class="lbl">-√2</text>
  <text x="64" y="192" class="lbl">-2√2</text>
</svg>

- **【分步标准解答】**

  **[1] $f(\theta)$ を $t$ の式で表す**
  $t = \sin\theta + \cos\theta$ の両辺を 2 乗すると、
  $$t^2 = (\sin\theta + \cos\theta)^2 = \sin^2\theta + 2\sin\theta\cos\theta + \cos^2\theta = 1 + \sin 2\theta$$
  よって、$\sin 2\theta = t^2 - 1$。これを $f(\theta)$ に代入すると、
  $$f(\theta) = (t^2 - 1) + 2t - 1 = t^2 + 2t - 2$$
  > 💡 讲师批注：不要漏掉原式末尾的 $-1$！结果是 $t^2 + 2t - 2$（而不是 $t^2 + 2t - 1$）。

  **[2] $t$ の取りうる値の範囲**
  三角関数の合成により、
  $$t = \sin\theta + \cos\theta = \sqrt{2}\sin\left(\theta + \frac{\pi}{4}\right)$$
  $0 \le \theta < 2\pi$ より、$\dfrac{\pi}{4} \le \theta + \dfrac{\pi}{4} < \dfrac{9}{4}\pi$（ちょうど 1 周分）であるから、
  $$-1 \le \sin\left(\theta + \frac{\pi}{4}\right) \le 1$$
  したがって、
  $$-\sqrt{2} \le t \le \sqrt{2}$$

  **[3] $f(\theta)$ の最大値・最小値とそのときの $\theta$**
  $g(t) = t^2 + 2t - 2 = (t + 1)^2 - 3$（$-\sqrt{2} \le t \le \sqrt{2}$）とおく。
  軸 $t = -1$ は区間 $[-\sqrt{2},\; \sqrt{2}]$ の内部にある下に凸の放物線であるから：
  - **最大値**：軸から最も遠い端点 $t = \sqrt{2}$ のとき、
    $$g(\sqrt{2}) = (\sqrt{2})^2 + 2\sqrt{2} - 2 = 2\sqrt{2}$$
    このとき $\sqrt{2}\sin\left(\theta + \dfrac{\pi}{4}\right) = \sqrt{2} \iff \sin\left(\theta + \dfrac{\pi}{4}\right) = 1$。
    $\dfrac{\pi}{4} \le \theta + \dfrac{\pi}{4} < \dfrac{9}{4}\pi$ より、$\theta + \dfrac{\pi}{4} = \dfrac{\pi}{2} \implies \theta = \dfrac{\pi}{4}$。
  - **最小値**：頂点 $t = -1$ のとき、
    $$g(-1) = -3$$
    このとき $\sqrt{2}\sin\left(\theta + \dfrac{\pi}{4}\right) = -1 \iff \sin\left(\theta + \dfrac{\pi}{4}\right) = -\dfrac{1}{\sqrt{2}}$。
    $\dfrac{\pi}{4} \le \theta + \dfrac{\pi}{4} < \dfrac{9}{4}\pi$ より、
    $$\theta + \frac{\pi}{4} = \frac{5}{4}\pi,\; \frac{7}{4}\pi \implies \theta = \pi,\; \frac{3}{2}\pi$$
  > 💡 讲师批注：最小值对应的 $\theta$ 有**两个解**（$\pi$ 与 $\frac{3}{2}\pi$），EJU 填空题若漏写一个就会扣分！代回原式验算：$\theta = \pi$ 时 $\sin 2\pi + 2(-1) - 1 = -3$；$\theta = \frac{3}{2}\pi$ 时 $\sin 3\pi + 2(-1) - 1 = -3$，均正确。
- **【最终答案】**
  - **[1] $f(\theta) = t^2 + 2t - 2$**
  - **[2] $-\sqrt{2} \le t \le \sqrt{2}$**
  - **[3] 最大値 $2\sqrt{2}$（$\theta = \dfrac{\pi}{4}$ のとき），最小値 $-3$（$\theta = \pi,\; \dfrac{3}{2}\pi$ のとき）**

---

#### 演習問題 5-(6)
- **【原题重现与翻译】**
  - 原题：$0 \le \theta \le \dfrac{\pi}{2}$ のとき、関数 $y = \sqrt{3}\sin\theta\cos\theta + \cos^2\theta$ の最大値と最小値を求めよ。また、その時の $\theta$ の値を求めよ。
  - 中文：当 $0 \le \theta \le \dfrac{\pi}{2}$ 时，求函数 $y = \sqrt{3}\sin\theta\cos\theta + \cos^2\theta$ 的最大值与最小值，并求取最值时的 $\theta$ 值。
- **【考点定位】**
  - 二倍角公式降幂（$\sin\theta\cos\theta = \frac{1}{2}\sin 2\theta,\; \cos^2\theta = \frac{1+\cos 2\theta}{2}$）+ 三角函数的合成。
- **【分步标准解答】**
  2倍角の公式・半角の公式を用いて角を $2\theta$ に統一すると、
  $$y = \sqrt{3}\cdot\frac{1}{2}\sin 2\theta + \frac{1 + \cos 2\theta}{2}$$
  $$= \frac{\sqrt{3}}{2}\sin 2\theta + \frac{1}{2}\cos 2\theta + \frac{1}{2}$$
  > 💡 讲师批注：只要看到 $\sin^2\theta,\; \cos^2\theta,\; \sin\theta\cos\theta$ 的线性组合，第一反应就是**降幂升角**化为 $a\sin 2\theta + b\cos 2\theta + c$ 的标准型！

  点 $P\left(\dfrac{\sqrt{3}}{2},\; \dfrac{1}{2}\right)$ は $OP = 1$、角 $\alpha = \dfrac{\pi}{6}$ であるから、合成して
  $$y = \sin\left(2\theta + \frac{\pi}{6}\right) + \frac{1}{2}$$
  $0 \le \theta \le \dfrac{\pi}{2}$ より、$\dfrac{\pi}{6} \le 2\theta + \dfrac{\pi}{6} \le \dfrac{7}{6}\pi$。
  この範囲で $\sin\left(2\theta + \dfrac{\pi}{6}\right)$ は：
  - $2\theta + \dfrac{\pi}{6} = \dfrac{\pi}{2}$、すなわち $\theta = \dfrac{\pi}{6}$ のとき最大値 $1$ をとる。よって $y$ の最大値は $1 + \dfrac{1}{2} = \dfrac{3}{2}$。
  - $2\theta + \dfrac{\pi}{6} = \dfrac{7}{6}\pi$、すなわち $\theta = \dfrac{\pi}{2}$ のとき最小値 $-\dfrac{1}{2}$ をとる。よって $y$ の最小値は $-\dfrac{1}{2} + \dfrac{1}{2} = 0$。
  > 💡 讲师批注：端点检验：$\theta = 0$ 时 $y = 1$；$\theta = \frac{\pi}{6}$ 时 $y = \frac{3}{4} + \frac{3}{4} = \frac{3}{2}$；$\theta = \frac{\pi}{2}$ 时 $y = 0$，验证无误。
- **【最终答案】**
  **最大値 $\dfrac{3}{2}$（$\theta = \dfrac{\pi}{6}$ のとき），最小値 $0$（$\theta = \dfrac{\pi}{2}$ のとき）**

---

#### 演習問題 5-(7)
- **【原题重现与翻译】**
  - 原题：実数 $x, y$ が $x^2 + y^2 = 1$ を満たすとき、$3x^2 + 2xy + y^2$ の最大値と最小値を求めよ。
  - 中文：当实数 $x, y$ 满足 $x^2 + y^2 = 1$ 时，求 $3x^2 + 2xy + y^2$ 的最大值与最小值。
- **【考点定位】**
  - 单位圆参数代换（$x = \cos\theta,\; y = \sin\theta$）+ 二倍角降幂 + 三角函数合成。
- **【分步标准解答】**
  実数 $x, y$ が $x^2 + y^2 = 1$ を満たすので、
  $$x = \cos\theta, \qquad y = \sin\theta \qquad (0 \le \theta < 2\pi)$$
  とおくことができる。このとき、
  $$3x^2 + 2xy + y^2 = 2x^2 + 2xy + (x^2 + y^2)$$
  > 💡 讲师批注：先把 $3x^2 + y^2$ 拆成 $2x^2 + (x^2 + y^2) = 2x^2 + 1$，比直接把 $x^2, y^2$ 分别降幂更省一步计算！
  $$= 2\cos^2\theta + 2\sin\theta\cos\theta + 1$$
  $$= (1 + \cos 2\theta) + \sin 2\theta + 1$$
  $$= \sin 2\theta + \cos 2\theta + 2$$
  $$= \sqrt{2}\sin\left(2\theta + \frac{\pi}{4}\right) + 2$$
  $0 \le \theta < 2\pi$ より、$2\theta + \dfrac{\pi}{4}$ は $\dfrac{\pi}{4} \le 2\theta + \dfrac{\pi}{4} < \dfrac{17}{4}\pi$（2 周分）を動くので、
  $$-1 \le \sin\left(2\theta + \frac{\pi}{4}\right) \le 1$$
  よって、
  $$2 - \sqrt{2} \le 3x^2 + 2xy + y^2 \le 2 + \sqrt{2}$$
  > 💡 讲师批注：最大值在 $2\theta + \frac{\pi}{4} = \frac{\pi}{2}, \frac{5\pi}{2}$（即 $\theta = \frac{\pi}{8}, \frac{9\pi}{8}$）取到，最小值在 $\theta = \frac{5\pi}{8}, \frac{13\pi}{8}$ 取到，均存在对应实数 $(x,y)$。
- **【最终答案】**
  **最大値 $2 + \sqrt{2}$，最小値 $2 - \sqrt{2}$**

---

### 第七章 演習問題 1（内分・外分・重心・対称点）

#### 演習問題 1-(1)
- **【原题重现与翻译】**
  - 原题：3 点 $A(5, 4),\; B(0, -1),\; C(8, -2)$ について、線分 $AB$ を $2:3$ に外分する点を $P$、$3:2$ に外分する点を $Q$ とし、$\triangle ABC$ の重心を $G$ とする。
    - [1] 線分 $PQ$ の中点 $M$ の座標を求めよ。
    - [2] 点 $G$ の座標を求めよ。
    - [3] $\triangle PQS$ の重心が点 $G$ と一致するように、点 $S$ の座標を定めよ。
  - 中文：已知三点 $A(5, 4),\; B(0, -1),\; C(8, -2)$，设外分线段 $AB$ 为 $2:3$ 的点为 $P$，外分线段 $AB$ 为 $3:2$ 的点为 $Q$，$\triangle ABC$ 的重心为 $G$。
    - [1] 求线段 $PQ$ 的中点 $M$ 的坐标。
    - [2] 求点 $G$ 的坐标。
    - [3] 确定点 $S$ 的坐标，使 $\triangle PQS$ 的重心与点 $G$ 重合。
- **【考点定位】**
  - 坐标平面上的外分点公式、中点公式、三角形重心公式。
- **【图解辅助（SVG 矢量图）】**
  直线 $AB$ 上 $Q, B, M, A, P$ 的对称位置关系（$M$ 既是 $AB$ 中点也是 $PQ$ 中点！）：

<svg viewBox="0 0 540 130" width="540" height="130" xmlns="http://www.w3.org/2000/svg" style="background:#fafafa;border:1px solid #e0e0e0;border-radius:6px;">
  <style>
    .ttl { font: bold 13px sans-serif; fill: #2c3e50; }
    .line { stroke: #34495e; stroke-width: 2; }
    .arc1 { fill: none; stroke: #e67e22; stroke-width: 1.5; }
    .arc2 { fill: none; stroke: #2980b9; stroke-width: 1.5; }
    .lbl { font: 11px sans-serif; fill: #2c3e50; text-anchor: middle; }
    .hl { font: bold 11px sans-serif; fill: #c0392b; text-anchor: middle; }
  </style>
  <text x="16" y="22" class="ttl">直線 AB 上の外分点 P (2:3)・Q (3:2) と中点 M の対称構造</text>
  <!-- Line: Q(-10,-11) at x=50, B(0,-1) at x=210, M(2.5,1.5) at x=250, A(5,4) at x=290, P(15,14) at x=450 -->
  <!-- Note: AB = 1 unit = 80px => QB = 2 units = 160px, AP = 2 units = 160px -->
  <line x1="25" y1="78" x2="505" y2="78" class="line"/>
  <!-- Bracket Q to B = 2, B to A = 1, A to P = 2 -->
  <path d="M 50 72 Q 130 44 210 72" class="arc2"/>
  <text x="130" y="52" class="lbl" fill="#2980b9">QB = 2 (AQ:QB = 3:2)</text>
  <path d="M 290 72 Q 370 44 450 72" class="arc1"/>
  <text x="370" y="52" class="lbl" fill="#e67e22">AP = 2 (AP:PB = 2:3)</text>
  <!-- Points -->
  <circle cx="50" cy="78" r="4" fill="#2980b9"/>
  <text x="50" y="98" class="lbl">Q(-10, -11)</text>
  <circle cx="210" cy="78" r="4" fill="#2c3e50"/>
  <text x="210" y="98" class="lbl">B(0, -1)</text>
  <circle cx="250" cy="78" r="5" fill="#e74c3c"/>
  <text x="250" y="116" class="hl">M(5/2, 3/2)</text>
  <circle cx="290" cy="78" r="4" fill="#2c3e50"/>
  <text x="290" y="98" class="lbl">A(5, 4)</text>
  <circle cx="450" cy="78" r="4" fill="#e67e22"/>
  <text x="450" y="98" class="lbl">P(15, 14)</text>
</svg>

- **【分步标准解答】**

  **[1] 線分 $PQ$ の中点 $M$ の座標**
  線分 $AB$ を $2:3$ に外分する点 $P$ の座標は、
  $$P\left(\frac{-3 \cdot 5 + 2 \cdot 0}{2 - 3},\; \frac{-3 \cdot 4 + 2 \cdot (-1)}{2 - 3}\right) = \left(\frac{-15}{-1},\; \frac{-14}{-1}\right) = (15,\; 14)$$
  > 💡 讲师批注：外分公式 $\frac{-nx_1+mx_2}{m-n}$ 中，分母是 $m-n = 2-3 = -1$，负负得正！

  線分 $AB$ を $3:2$ に外分する点 $Q$ の座標は、
  $$Q\left(\frac{-2 \cdot 5 + 3 \cdot 0}{3 - 2},\; \frac{-2 \cdot 4 + 3 \cdot (-1)}{3 - 2}\right) = \left(\frac{-10}{1},\; \frac{-11}{1}\right) = (-10,\; -11)$$
  したがって、線分 $PQ$ の中点 $M$ の座標は、
  $$M\left(\frac{15 + (-10)}{2},\; \frac{14 + (-11)}{2}\right) = \left(\frac{5}{2},\; \frac{3}{2}\right)$$
  > 💡 讲师批注：**几何秒杀验算**：由于 $P, Q$ 分别以互换比例 $2:3$ 与 $3:2$ 外分 $AB$，必有 $AP = QB$，故 $PQ$ 中点必与 $AB$ 中点重合！检验 $AB$ 中点：$\left(\frac{5+0}{2}, \frac{4-1}{2}\right) = \left(\frac{5}{2}, \frac{3}{2}\right)$，完全一致！

  **[2] $\triangle ABC$ の重心 $G$ の座標**
  $$G\left(\frac{5 + 0 + 8}{3},\; \frac{4 + (-1) + (-2)}{3}\right) = \left(\frac{13}{3},\; \frac{1}{3}\right)$$

  **[3] 点 $S$ の座標**
  点 $S$ の座標を $(x, y)$ とすると、$\triangle PQS$ の重心は
  $$\left(\frac{15 + (-10) + x}{3},\; \frac{14 + (-11) + y}{3}\right) = \left(\frac{5 + x}{3},\; \frac{3 + y}{3}\right)$$
  これが点 $G\left(\dfrac{13}{3},\; \dfrac{1}{3}\right)$ と一致するから、
  $$\frac{5 + x}{3} = \frac{13}{3} \implies x = 8, \qquad \frac{3 + y}{3} = \frac{1}{3} \implies y = -2$$
  よって、$S(8,\; -2)$。
  > 💡 讲师批注：因为 $P+Q = A+B$，所以使 $\triangle PQS$ 与 $\triangle ABC$ 重心重合的点 $S$ 恰好就是点 $C(8,-2)$ 本身！
- **【最终答案】**
  **[1] $M\left(\dfrac{5}{2},\; \dfrac{3}{2}\right)$　[2] $G\left(\dfrac{13}{3},\; \dfrac{1}{3}\right)$　[3] $S(8,\; -2)$**

---

#### 演習問題 1-(2)
- **【原题重现与翻译】**
  - 原题：$A(2, -1)$ に関して、点 $P(-1, 1)$ と対称な点 $Q$ の座標を求めよ。
  - 中文：求点 $P(-1, 1)$ 关于点 $A(2, -1)$ 对称的点 $Q$ 的坐标。
- **【考点定位】**
  - 中心对称点公式（对称中心是两点连线的中点）。
- **【分步标准解答】**
  点 $Q$ の座標を $(x, y)$ とする。
  点 $A(2, -1)$ は線分 $PQ$ の中点であるから、
  $$\frac{-1 + x}{2} = 2, \qquad \frac{1 + y}{2} = -1$$
  これを解くと、
  $$-1 + x = 4 \implies x = 5, \qquad 1 + y = -2 \implies y = -3$$
  > 💡 讲师批注：快速心算口诀：**「对称点 = 2 × 对称中心 − 原点」**，即 $x = 2(2) - (-1) = 5$，$y = 2(-1) - 1 = -3$。
- **【最终答案】**
  **$Q(5,\; -3)$**

---

#### 演習問題 1-(3)
- **【原题重现与翻译】**
  - 原题：3 点 $A(a, b),\; B(0, 0),\; C(c, 0)$ と点 $P(x, y)$ がある。$A$ に関して $P$ と対称な点を $Q$ とし、$B$ に関して $Q$ と対称な点を $R$ とする。$C$ に関して $R$ と対称な点が $P$ と一致するとき、$x, y$ を $a, b, c$ を用いて表せ。
  - 中文：已知三点 $A(a, b),\; B(0, 0),\; C(c, 0)$ 及点 $P(x, y)$。设点 $P$ 关于 $A$ 的对称点为 $Q$，点 $Q$ 关于 $B$ 的对称点为 $R$。当点 $R$ 关于 $C$ 的对称点与 $P$ 重合时，用 $a, b, c$ 表示 $x, y$。
- **【考点定位】**
  - 连续中心对称变换与含参一次方程求解。
- **【分步标准解答】**
  点 $Q$ は $A(a, b)$ に関して $P(x, y)$ と対称であるから、
  $$Q(2a - x,\; 2b - y)$$
  > 💡 讲师批注：直接利用「对称点 = $2\times$中心 $-$ 原点」逐次递推，清晰高效。

  次に、点 $R$ は $B(0, 0)$ に関して $Q$ と対称であるから、
  $$R\bigl(2 \cdot 0 - (2a - x),\; 2 \cdot 0 - (2b - y)\bigr) = (x - 2a,\; y - 2b)$$
  さらに、$C(c, 0)$ に関して $R$ と対称な点を $P'$ とすると、
  $$P'\bigl(2c - (x - 2a),\; 2 \cdot 0 - (y - 2b)\bigr) = (2a + 2c - x,\; 2b - y)$$
  条件より $P'$ が $P(x, y)$ と一致するから、
  $$2a + 2c - x = x, \qquad 2b - y = y$$
  これらを解くと、
  $$2x = 2a + 2c \implies x = a + c, \qquad 2y = 2b \implies y = b$$
  > 💡 讲师批注：反向代入验算：$P(a+c, b) \xrightarrow{A(a,b)} Q(a-c, b) \xrightarrow{B(0,0)} R(c-a, -b) \xrightarrow{C(c,0)} (a+c, b) = P$，完美闭合！
- **【最终答案】**
  **$x = a + c,\quad y = b$**

---

### 第七章 演習問題 2（直線の方程式・2直線の平行と垂直・交点）

#### 演習問題 2-(1)
- **【原题重现与翻译】**
  - 原题：点 $(-3, 2)$ を通り、直線 $3x - 4y - 6 = 0$ に平行な直線 $l$ と垂直な直線 $l'$ の方程式をそれぞれ求めよ。
  - 中文：求过点 $(-3, 2)$ 且与直线 $3x - 4y - 6 = 0$ 分别平行（$l$）和垂直（$l'$）的直线方程。
- **【考点定位】**
  - 两直线平行条件与垂直条件（一般式速写法 vs. 点斜式标准法）。
- **【图解辅助（SVG 矢量图）】**
  坐标系中已知直线 $3x-4y-6=0$、平行直线 $l$ 与垂直直线 $l'$ 的几何位置关系：

<svg viewBox="0 0 460 230" width="460" height="230" xmlns="http://www.w3.org/2000/svg" style="background:#fafafa;border:1px solid #e0e0e0;border-radius:6px;">
  <style>
    .ax { stroke: #7f8c8d; stroke-width: 1.3; }
    .base { stroke: #34495e; stroke-width: 2; stroke-dasharray: 5 3; }
    .par { stroke: #2980b9; stroke-width: 2.2; }
    .perp { stroke: #e74c3c; stroke-width: 2.2; }
    .lbl { font: 11px sans-serif; fill: #2c3e50; }
    .hl-b { font: bold 11px sans-serif; fill: #2980b9; }
    .hl-r { font: bold 11px sans-serif; fill: #c0392b; }
  </style>
  <!-- Origin at (230, 130), scale 22px/unit -->
  <line x1="30" y1="130" x2="430" y2="130" class="ax"/>
  <line x1="230" y1="220" x2="230" y2="15" class="ax"/>
  <text x="434" y="134" class="lbl">x</text>
  <text x="236" y="24" class="lbl">y</text>
  <text x="234" y="143" class="lbl">O</text>
  <!-- Base line: 3x - 4y - 6 = 0 => y = 0.75x - 1.5
       x=-4 => y=-4.5 => (142, 229); x=6 => y=3 => (362, 64) -->
  <line x1="142" y1="229" x2="362" y2="64" class="base"/>
  <text x="320" y="114" class="lbl">3x - 4y - 6 = 0</text>
  <!-- Parallel line l: 3x - 4y + 17 = 0 => y = 0.75x + 4.25
       x=-7 => y=-1 => (76, 152); x=1 => y=5 => (252, 20) -->
  <line x1="76" y1="152" x2="252" y2="20" class="par"/>
  <text x="256" y="34" class="hl-b">l: 3x - 4y + 17 = 0 (平行)</text>
  <!-- Perpendicular line l': 4x + 3y + 6 = 0 => y = -4/3 x - 2
       x=-5 => y=4.67 => (120, 27); x=1.5 => y=-4 => (263, 218) -->
  <line x1="120" y1="27" x2="263" y2="218" class="perp"/>
  <text x="266" y="210" class="hl-r">l': 4x + 3y + 6 = 0 (垂直)</text>
  <!-- Point (-3, 2) => (230 - 66, 130 - 44) = (164, 86) -->
  <circle cx="164" cy="86" r="4.5" fill="#e74c3c"/>
  <text x="96" y="82" class="hl-r">P(-3, 2)</text>
</svg>

- **【分步标准解答】**
  **【解法 1：点斜式（傾きを用いる標準解法）】**
  与えられた直線 $3x - 4y - 6 = 0$ を $y$ について解くと、
  $$y = \frac{3}{4}x - \frac{3}{2}$$
  よって、この直線の傾きは $\dfrac{3}{4}$ である。
  - **平行な直線 $l$**：傾きが $\dfrac{3}{4}$ で点 $(-3, 2)$ を通るから、
    $$y - 2 = \frac{3}{4}\{x - (-3)\} = \frac{3}{4}(x + 3)$$
    両辺に $4$ を掛けて整理すると、
    $$4y - 8 = 3x + 9 \implies 3x - 4y + 17 = 0 \quad \left(\text{または } y = \frac{3}{4}x + \frac{17}{4}\right)$$
  - **垂直な直線 $l'$**：傾きを $m$ とすると、垂直条件 $\dfrac{3}{4}m = -1$ より $m = -\dfrac{4}{3}$。
    点 $(-3, 2)$ を通るから、
    $$y - 2 = -\frac{4}{3}(x + 3)$$
    両辺に $3$ を掛けて整理すると、
    $$3y - 6 = -4x - 12 \implies 4x + 3y + 6 = 0 \quad \left(\text{または } y = -\frac{4}{3}x - 2\right)$$

  **【解法 2：一般式速写法（EJU 考场推荐！）】**
  > 💡 讲师批注：与 $ax+by+c=0$ 平行的直线系为 $a(x-x_0)+b(y-y_0)=0$；垂直的直线系为 $b(x-x_0)-a(y-y_0)=0$（系数互换、其中之一变号）。直接代入 $(-3,2)$：
  > - 平行 $l$：$3(x+3) - 4(y-2) = 0 \implies 3x - 4y + 17 = 0$；
  > - 垂直 $l'$：$4(x+3) + 3(y-2) = 0 \implies 4x + 3y + 6 = 0$。3 秒出答案且绝无分数通分失误！
- **【最终答案】**
  **$l:\; 3x - 4y + 17 = 0$（$y = \dfrac{3}{4}x + \dfrac{17}{4}$），　$l':\; 4x + 3y + 6 = 0$（$y = -\dfrac{4}{3}x - 2$）**

---

#### 演習問題 2-(2)
- **【原题重现与翻译】**
  - 原题：2 直線 $x + y - 4 = 0 \cdots\cdots$ ①，$x + y - 4 = 0 \cdots\cdots$ ② の交点を通り、次の条件を満たす直線の方程式をそれぞれ求めよ。
    - [1] 点 $(-1, 2)$ を通る　　[2] 直線 $x + 2y + 2 = 0$ に平行
  - 中文：求经过两直线 $x + y - 4 = 0$ ① 与 $x + y - 4 = 0$ ② 的交点，且满足下列条件的直线方程：[1] 过点 $(-1, 2)$；[2] 平行于直线 $x + 2y + 2 = 0$。

> ⚠️ **教材勘误提示（重大印刷错误）**：经核对原教材第 149 页（`page_0150.jpg`），题干中直线 ① 与直线 ② 被印成了**完全相同的方程 $x + y - 4 = 0$**！两直线重合（一致する），交点有无穷多个（整条直线 $x+y-4=0$ 上的所有点），因此原印刷题干**无法确定唯一交点**，属于明显的排印错误。
>
> **备课处理方案**：为保证学生完整掌握本题原本要考察的 EJU 核心考点——**「过两直线交点的直线束方程 $k(a_1x+b_1y+c_1)+(a_2x+b_2y+c_2)=0$」**，下面我们以将直线 ② 修正为经典配套方程 **$2x - y - 5 = 0$** 为例，完整示范「求交点法」与「直线束法（$k$ 法）」两种日本考场标准解法（授课时也可根据板书替换为任意与 ① 不平行的直线 ②）。

- **【考点定位】**
  - 两直线交点坐标求解、直线束方程（2直線の交点を通る直線の方程式）。
- **【修正示范题分步标准解答（設 ① $x+y-4=0$，② $2x-y-5=0$）】**

  **【解法 1：交点を直接求める方法】**
  ①，② を連立して解くと、
  $$(x + y - 4) + (2x - y - 5) = 0 \implies 3x - 9 = 0 \implies x = 3$$
  ① に代入して $y = 4 - 3 = 1$。よって交点は $(3,\; 1)$。
  - **[1] 点 $(-1, 2)$ を通る直線**：2 点 $(3, 1),\; (-1, 2)$ を通るから、
    $$y - 1 = \frac{2 - 1}{-1 - 3}(x - 3) = -\frac{1}{4}(x - 3) \implies x + 4y - 7 = 0$$
  - **[2] 直線 $x + 2y + 2 = 0$ に平行な直線**：点 $(3, 1)$ を通り傾き $-\dfrac{1}{2}$（一般式係数 $(1, 2)$）であるから、
    $$1 \cdot (x - 3) + 2(y - 1) = 0 \implies x + 2y - 5 = 0$$

  **【解法 2：直線束 $k(x+y-4)+(2x-y-5)=0$ を用いる方法（数学Ⅱ核心！）】**
  2 直線 ①，② の交点を通る直線（ただし ① 自身を除く）は、定数 $k$ を用いて
  $$k(x + y - 4) + (2x - y - 5) = 0 \cdots\cdots \text{③}$$
  と表せる。整理すると、
  $$(k + 2)x + (k - 1)y - (4k + 5) = 0 \cdots\cdots \text{③'}$$
  > 💡 讲师批注：当两直线交点是复杂分数时，**直线束法无需解交点**，直接代入条件求 $k$，省时省力！但务必注意：该式无法表示括号前乘了 $k$ 的那条直线 ① 本身，必要时需单独检验 ① 是否满足条件。
  - **[1]** ③ が点 $(-1, 2)$ を通るから、$x = -1,\; y = 2$ を代入すると、
    $$k(-1 + 2 - 4) + (-2 - 2 - 5) = 0 \implies -3k - 9 = 0 \implies k = -3$$
    これを ③' に代入して、$-x - 4y + 7 = 0 \implies x + 4y - 7 = 0$。
  - **[2]** ③' が直線 $x + 2y + 2 = 0$ に平行である条件（$a_1b_2 - a_2b_1 = 0$）より、
    $$(k + 2) \cdot 2 - 1 \cdot (k - 1) = 0 \implies 2k + 4 - k + 1 = 0 \implies k = -5$$
    これを ③' に代入して、$-3x - 6y + 15 = 0 \implies x + 2y - 5 = 0$。
- **【最终答案】**
  - **原印刷题干**：因 ①② 重合（均为 $x+y-4=0$），**题目有印刷错误，无唯一解**。
  - **修正示范题（② 为 $2x-y-5=0$ 时）**：**[1] $x + 4y - 7 = 0$　[2] $x + 2y - 5 = 0$**
