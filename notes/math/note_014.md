# 《EJU 教材全解与备课讲义》数学 014（P196–P210）

> **对应源文件**：`work_math/ocr_md/ocr_014_p196-210.md`（第七章末尾「演習問題 12-(6)」「極座標、極方程式」、第八章《ベクトル》之「ベクトルの演算」「ベクトルの成分」「ベクトルの内積」）
> **视觉核对参考图**：`work_math/ref_imgs/page_0196.jpg`、`page_0197.jpg`、`page_0199.jpg`、`page_0200.jpg`、`page_0202.jpg`、`page_0204.jpg`、`page_0206.jpg`、`page_0207.jpg`、`page_0208.jpg`、`page_0210.jpg`

---

## 一、国内高中基础知识点唤醒与 EJU 考纲差异对比

本切片横跨日本高中 **数学Ⅲ（式と曲線：極座標・極方程式）** 与 **数学C（旧课纲 数学B：平面上のベクトル）** 两大核心板块，涵盖 **极坐标与极方程、平面向量的几何运算、向量的坐标（成分）运算、向量的内积（数量积）** 四大部分。

### 1.1 极坐标与极方程式（極座標・極方程式）

- **极坐标的定义**：在平面上取定点 $O$（**極 / 极点**）与射线 $OX$（**始線 / 始线**）。对平面上任意点 $P$，令 $OP = r$，从始线 $OX$ 逆时针测至射线 $OP$ 的一般角（弧度制）为 $\theta$（**偏角 / 极角**），则 $(r, \theta)$ 称为点 $P$ 的**極座標**。
  - 极点 $O$ 的极坐标记为 $(0, \theta)$（$\theta$ 任意）。
  - 一般情况下，$(r, \theta)$ 与 $(r, \theta + 2n\pi)$（$n \in \mathbb{Z}$）表示同一点；若限制 $r > 0,\; 0 \le \theta < 2\pi$，则极点以外的点与极坐标一一对应。
  - **极方程中允许 $r < 0$ 的重要约定**：在讨论极方程 $r = f(\theta)$ 时，规定当 $r > 0$ 时，$(-r, \theta)$ 与 $(r, \theta + \pi)$ 表示同一点（即沿 $\theta$ 方向的反向延长线取距离 $r$）。
- **极坐标与直角坐标的互化**（原点 $O$ 为极点，$x$ 轴正半轴为始线）：
  $$\begin{cases} x = r\cos\theta \\ y = r\sin\theta \end{cases} \qquad \Longleftrightarrow \qquad \begin{cases} r = \sqrt{x^2+y^2} \\ \cos\theta = \dfrac{x}{r},\; \sin\theta = \dfrac{y}{r} \quad (r \neq 0) \end{cases}$$
- **两点间距离与三角形面积**：设 $A(r_1, \theta_1),\; B(r_2, \theta_2)$（$r_1, r_2 > 0$）：
  $$AB = \sqrt{r_1^2 + r_2^2 - 2r_1r_2\cos(\theta_2 - \theta_1)}, \qquad S_{\triangle OAB} = \frac{1}{2}r_1r_2\left|\sin(\theta_2 - \theta_1)\right|$$
- **常见圆与直线的极方程式**：
  1. 中心在极点 $O$、半径为 $a$ 的圆：$r = a$
  2. 中心在 $(a, 0)$、半径为 $a$ 的圆：$r = 2a\cos\theta$
  3. 中心在 $(r_0, \theta_0)$、半径为 $a$ 的圆：$r^2 - 2rr_0\cos(\theta - \theta_0) + r_0^2 = a^2$
  4. 过极点 $O$、与始线成角 $\alpha$ 的直线：$\theta = \alpha$
  5. 过点 $A(a, \alpha)$（$a > 0$）且垂直于 $OA$ 的直线：$r\cos(\theta - \alpha) = a$

> ⚠️ **教材勘误提示（P197 / `page_0197.jpg` `[15.4]`）**：
> 原教材 `[15.4]` 公式汇总表存在三处明显印刷错误，授课与自习时务必修正：
> 1. ② 中心が $(a, 0)$、半径が $a$ の円：误印为 $r = 2\alpha\cos\theta$，正确应为 **$r = 2a\cos\theta$**；
> 2. ③ 中心が $(r_0, \theta_0)$、半径が $a$ の円：右端误印为 $\alpha^2$，正确应为 **$a^2$**；
> 3. ④ 極 $O$ を通り、始線と $\alpha$ の角をなす直線：**严重误印为 $r = \theta$**，正确应为 **$\theta = \alpha$**（紧接其后的 P198 解説中已印作 $\theta = \alpha$）。

### 1.2 向量的几何运算（ベクトルの演算）

- **基本概念**：只有大小和方向、与起点位置无关的量称为**向量（ベクトル）**，记作 $\overrightarrow{AB}$ 或 $\vec{a}$。
  - **模（大きさ）**：$|\vec{a}|$；**単位ベクトル（单位向量）**：$|\vec{e}| = 1$；**逆ベクトル（相反向量）**：$-\vec{a}$（$-\overrightarrow{AB} = \overrightarrow{BA}$）；**零ベクトル（零向量）**：$\vec{0}$（$|\vec{0}| = 0$，方向任意/不考虑）。
- **加减法与数乘**：
  - 加法（首尾相接）：$\overrightarrow{OA} + \overrightarrow{AC} = \overrightarrow{OC}$
  - 减法（共起点，指向被减向量终点）：$\overrightarrow{OA} - \overrightarrow{OB} = \overrightarrow{BA}$
  - 数乘 $k\vec{a}$：模为 $|k||\vec{a}|$，$k > 0$ 同向，$k < 0$ 反向，$0\vec{a} = \vec{0}$。
- **平行条件与平面向量基本定理（ベクトルの分解）**：
  - 设 $\vec{a} \neq \vec{0},\; \vec{b} \neq \vec{0}$，则 $\vec{a} \parallel \vec{b} \iff$ 存在实数 $k$ 使得 $\vec{b} = k\vec{a}$。
  - 若 $\vec{a}, \vec{b}$ 非零且不平行（$\vec{a} \nparallel \vec{b}$），则平面内任意向量 $\vec{p}$ 可**唯一**表示为 $\vec{p} = s\vec{a} + t\vec{b}$（$s, t \in \mathbb{R}$）。
    $$s\vec{a} + t\vec{b} = s'\vec{a} + t'\vec{b} \iff s = s',\; t = t'$$

> ⚠️ **教材勘误提示（P202 / `page_0202.jpg` `[1.2]` ③）**：
> 原教材将数乘 $k\vec{a}$ 误排为箭头覆盖整体的 $\overrightarrow{ka}$，规范写法应为 **$k\vec{a}$**。

### 1.3 向量的坐标表示（ベクトルの成分）

- 设基本单位向量 $\vec{e}_1 = (1, 0),\; \vec{e}_2 = (0, 1)$，则 $\vec{a} = a_1\vec{e}_1 + a_2\vec{e}_2 = (a_1, a_2)$，模 $|\vec{a}| = \sqrt{a_1^2 + a_2^2}$。
- 两点 $A(a_1, a_2),\; B(b_1, b_2)$ 构成的向量：$\overrightarrow{AB} = (b_1 - a_1,\; b_2 - a_2)$（终点减起点）。
- **坐标平行条件**（$\vec{a} \neq \vec{0},\; \vec{b} \neq \vec{0}$）：
  $$\vec{a} \parallel \vec{b} \iff a_1 b_2 - a_2 b_1 = 0$$

### 1.4 向量的内积（ベクトルの内積）

- **定义**：非零向量 $\vec{a}, \vec{b}$ 的夹角为 $\theta$（$0^\circ \le \theta \le 180^\circ$），则内积定义为实数：
  $$\vec{a} \cdot \vec{b} = |\vec{a}||\vec{b}|\cos\theta$$
  当 $\vec{a} = \vec{0}$ 或 $\vec{b} = \vec{0}$ 时，规定 $\vec{a} \cdot \vec{b} = 0$。
  - **几何意义（正射影）**：$\vec{a} \cdot \vec{b} = |\vec{a}| \cdot (|\vec{b}|\cos\theta)$，即 $\vec{a}$ 的模乘以 $\vec{b}$ 在 $\vec{a}$ 方向上的有向正射影长。
- **坐标公式与夹角公式**：设 $\vec{a} = (a_1, a_2),\; \vec{b} = (b_1, b_2)$：
  $$\vec{a} \cdot \vec{b} = a_1 b_1 + a_2 b_2, \qquad \cos\theta = \frac{\vec{a}\cdot\vec{b}}{|\vec{a}||\vec{b}|} = \frac{a_1 b_1 + a_2 b_2}{\sqrt{a_1^2+a_2^2}\sqrt{b_1^2+b_2^2}} \quad (0^\circ \le \theta \le 180^\circ)$$
- **垂直与平行条件**（$\vec{a} \neq \vec{0},\; \vec{b} \neq \vec{0}$）：
  - 垂直：$\vec{a} \perp \vec{b} \iff \vec{a} \cdot \vec{b} = 0 \iff a_1 b_1 + a_2 b_2 = 0$
  - 平行：$\vec{a} \parallel \vec{b} \iff \vec{a} \cdot \vec{b} = \pm |\vec{a}||\vec{b}| \iff a_1 b_2 - a_2 b_1 = 0$
- **运算律与模长平方公式**：
  $$\vec{a}\cdot\vec{a} = |\vec{a}|^2, \qquad |\vec{a}| = \sqrt{\vec{a}\cdot\vec{a}}$$

> ⚠️ **教材勘误提示（P208 / `page_0208.jpg` `[3.1]` & `[3.4]` ②）**：
> 1. `[3.1]` 中「$\vec{a}=0$ または $\vec{b}=0$」漏印零向量箭头，规范写法应为 **$\vec{a}=\vec{0}$ または $\vec{b}=\vec{0}$**；
> 2. `[3.4]` ② 夹角余弦公式的分母**严重误印**为 $\sqrt{a_1^2+a_2^2} + \sqrt{b_1^2+b_2^2}$（中间多了加号），正确应为乘积 **$\sqrt{a_1^2+a_2^2}\sqrt{b_1^2+b_2^2}$**！

### 1.5 国内高中 vs. 日本 EJU 考纲差异与符号习惯

| 对比维度 | 国内高中习惯 | 日本 EJU 习惯 | 备课/应试提醒 |
| :--- | :--- | :--- | :--- |
| **极坐标地位** | 新高考已大幅删减或作为选考（选修 4-4） | **理系数学必考（数学Ⅲ / 数学C）**，常与圆锥曲线、参数方程、微积分综合 | 必须熟练掌握 $r < 0$ 的约定与常见曲线极方程（圆、直线、圆锥曲线、双纽线） |
| **向量记号** | 印刷体常用黑体 $\mathbf{a}, \mathbf{b}$，手写加箭头 | 印刷体与手写体均普遍使用箭头 **$\vec{a}, \vec{b}, \vec{0}$** | 考卷中看到 $\vec{a}$ 就是向量，切记 $\vec{a}\cdot\vec{b}$ 的「$\cdot$」绝不可省略或写成 $\times$ |
| **向量坐标术语** | 称「向量的坐标」 | 称 **ベクトルの成分（せいぶん）**，$x$ 成分、$y$ 成分 | 审题时看到「成分を求めよ」即求向量的坐标 $(x, y)$ |
| **内积术语** | 称「数量积」或「点积」 | 统一称 **内積（ないせき）** | EJU 向量大题必考内积与模长平方转化 $|\vec{a}+t\vec{b}|^2$ |
| **平面向量基本定理** | 称「平面向量基本定理」 | 称 **ベクトルの分解**，且直接用 $\vec{a} \neq \vec{0},\; \vec{b} \neq \vec{0},\; \vec{a} \nparallel \vec{b}$ 表述 | 系数比较法（一次独立性）前务必先确认基底非零且不平行 |
| **反演变换** | 竞赛常见 | EJU 轨迹题（演習問題 12-(6)）高频压轴模型 | 牢记 $OP \cdot OQ = 1 \implies X = \frac{x}{x^2+y^2},\; Y = \frac{y}{x^2+y^2}$ |

---

## 二、日文核心词汇与公式假名注音

### 2.1 本切片日文核心词汇

- 極座標（きょくざひょう / kyokuzahyou） — 极坐标
- 極方程式（きょくほうていしき / kyokuhouteishiki） — 极方程（极坐标方程）
- 極（きょく / kyoku） — 极点（极坐标系的原点）
- 始線（しせん / shisen） — 始线（极轴）
- 偏角（へんかく / henkaku） — 偏角、极角
- 直交座標（ちょっこうざひょう / chokkou zahyou） — 直角坐标（笛卡尔坐标）
- レムニスケート（れむにすけーと / remunisukeeto） — 双纽线（伯努利双纽线，lemniscate）
- ベクトル（べくとる / bekutoru） — 向量（矢量）
- 有向線分（ゆうこうせんぶん / yuukou senbun） — 有向线段
- 始点（してん / shiten） — 起点（有向线段或向量的始点）
- 終点（しゅうてん / shuuten） — 终点（有向线段或向量的终点）
- 大きさ（おおきさ / ookisa） — 模、大小（向量的长度）
- 向き（むき / muki） — 方向（向量的指向）
- 単位ベクトル（たんいべくとる / tan'i bekutoru） — 单位向量
- 逆ベクトル（ぎゃくべくとる / gyaku bekutoru） — 相反向量（负向量）
- 零ベクトル（れいべくとる / rei bekutoru） — 零向量（口语亦读 ゼロベクトル）
- 相等（そうとう / soutou） — 相等
- 実数倍（じっすうばい / jissuubai） — 数乘（向量的实数倍）
- ベクトルの分解（べくとるのぶんかい / bekutoru no bunkai） — 向量的分解
- 成分（せいぶん / seibun） — 分量、坐标成分
- 成分表示（せいぶんひょうじ / seibun hyouji） — 坐标表示（分量表示）
- 基本ベクトル（きほんべくとる / kihon bekutoru） — 基本单位向量
- 内積（ないせき / naiseki） — 内积（数量积、点积）
- 正射影（せいしゃえい / seishaei） — 正射影（正投影）
- 正六角形（せいろっかっけい / seirokkakkei） — 正六边形

### 2.2 核心公式的日本课堂口语读法

1. **极坐标转直角坐标** $x = r\cos\theta,\; y = r\sin\theta$
   - 课堂读法：**エックス イコール アール コサイン シータ、ワイ イコール アール サイン シータ**
2. **圆锥曲线统一极方程** $r = \dfrac{ea}{1 + e\cos\theta}$
   - 课堂读法：**アール イコール いち たす イー コサイン シータ ぶんの イー エー**
3. **向量写法** $\overrightarrow{AB} = \vec{a},\; |\vec{a}|$
   - 课堂读法：**ベクトル エービー イコール ベクトル エー**；模长 $|\vec{a}|$ 读作 **ベクトル エー の おおきさ**（或 **ぜったいち ベクトル エー**）。
4. **向量减法** $\overrightarrow{OA} - \overrightarrow{OB} = \overrightarrow{BA}$
   - 课堂读法：**ベクトル オーエー ひく ベクトル オービー イコール ベクトル ビーエー**（口诀：**うしろ ひく まえ**，即「终点减起点」：$\overrightarrow{BA} = \overrightarrow{OA} - \overrightarrow{OB}$）。
5. **向量内积定义** $\vec{a} \cdot \vec{b} = |\vec{a}||\vec{b}|\cos\theta$
   - 课堂读法：**ベクトル エー ドット ベクトル ビー イコール、ベクトル エー の おおきさ かける ベクトル ビー の おおきさ かける コサイン シータ**
   - 备注：内积符号「$\cdot$」在口语中读作 **ドット（dot）** 或 **ないせき（内積）**。
6. **向量垂直条件** $\vec{a} \perp \vec{b} \iff \vec{a} \cdot \vec{b} = 0$
   - 课堂读法：**ベクトル エー すいちょく ベクトル ビー、ひつようじゅうぶんじょうけん、ないせき イコール ゼロ**。

---

## 三、逐题深度解析（不可跳步）

---

### 第七章 演習問題 12（反演轨迹）

#### 演習問題 12-(6)（P196）
- **【原题重现与翻译】**
  - 原题：$O$ は原点とする。点 $P$ が円 $x^2+y^2-2x+2y-2=0$ の周上を動くとき、半直線 $OP$ 上にあって、$OP \cdot OQ = 1$ を満たす点 $Q$ の軌跡を求めよ。
  - 中文：设 $O$ 为原点。当点 $P$ 在圆 $x^2+y^2-2x+2y-2=0$ 的圆周上运动时，求位于射线 $OP$ 上且满足 $OP \cdot OQ = 1$ 的点 $Q$ 的轨迹。
- **【考点定位】**
  - 轨迹方程（連動点の軌跡）、平面反演变换（反転）。
- **【图解辅助（SVG 矢量图）】**

<svg viewBox="0 0 420 300" width="420" height="300" xmlns="http://www.w3.org/2000/svg">
  <rect width="420" height="300" fill="#fafafa" rx="8"/>
  <!-- 坐标轴 (原点 O 在 200, 150，单位长度 45px) -->
  <line x1="30" y1="150" x2="395" y2="150" stroke="#475569" stroke-width="1.5"/>
  <polygon points="395,150 387,146 387,154" fill="#475569"/>
  <line x1="200" y1="285" x2="200" y2="15" stroke="#475569" stroke-width="1.5"/>
  <polygon points="200,15 196,23 204,23" fill="#475569"/>
  <text x="385" y="168" font-size="13" fill="#334155" font-style="italic">x</text>
  <text x="208" y="25" font-size="13" fill="#334155" font-style="italic">y</text>
  <text x="184" y="166" font-size="13" fill="#334155" font-weight="bold">O</text>
  <!-- 单位圆参考虚线 r=1 (45px) -->
  <circle cx="200" cy="150" r="45" fill="none" stroke="#94a3b8" stroke-width="1" stroke-dasharray="4,3"/>
  <!-- 原圆 C1: (x-1)^2+(y+1)^2=4 -> 圆心(245, 195), 半径 90 -->
  <circle cx="245" cy="195" r="90" fill="rgba(59,130,246,0.06)" stroke="#2563eb" stroke-width="2"/>
  <circle cx="245" cy="195" r="3" fill="#2563eb"/>
  <text x="252" y="200" font-size="11" fill="#1d4ed8">(1, -1)</text>
  <text x="292" y="268" font-size="12" fill="#1d4ed8" font-weight="bold">P の円 (半径2)</text>
  <!-- 轨迹圆 C2: (x+1/2)^2+(y-1/2)^2=1 -> 圆心(177.5, 127.5), 半径 45 -->
  <circle cx="177.5" cy="127.5" r="45" fill="rgba(220,38,38,0.08)" stroke="#dc2626" stroke-width="2.2"/>
  <circle cx="177.5" cy="127.5" r="3" fill="#dc2626"/>
  <text x="112" y="124" font-size="11" fill="#b91c1c">(-1/2, 1/2)</text>
  <text x="48" y="78" font-size="12" fill="#b91c1c" font-weight="bold">Q の軌跡 (半径1)</text>
  <!-- 射线 OP 示例：取 P(1, 1) -> (245, 105), Q(1/2, 1/2) -> (222.5, 127.5) -->
  <line x1="200" y1="150" x2="265" y2="85" stroke="#0f766e" stroke-width="1.5" stroke-dasharray="5,3"/>
  <circle cx="245" cy="105" r="4" fill="#2563eb"/>
  <text x="253" y="103" font-size="12" fill="#1d4ed8" font-weight="bold">P(X, Y)</text>
  <circle cx="222.5" cy="127.5" r="4" fill="#dc2626"/>
  <text x="228" y="138" font-size="12" fill="#b91c1c" font-weight="bold">Q(x, y)</text>
  <!-- 原点标注 -->
  <circle cx="200" cy="150" r="3.5" fill="#0f172a"/>
  <text x="20" y="280" font-size="11" fill="#64748b">※ OP・OQ = 1（原点中心・半径1の円に関する反転）</text>
</svg>

- **【分步标准解答】**
  点 $P$ の座標を $(X, Y)$、点 $Q$ の座標を $(x, y)$ とする。
  点 $P$ は円 $x^2+y^2-2x+2y-2=0$ 上にあるから、
  $$X^2 + Y^2 - 2X + 2Y - 2 = 0 \qquad \cdots \text{①}$$
  ここで、原点 $O(0, 0)$ は①を満たさない（$0+0-0+0-2 = -2 \neq 0$）から、$P \neq O$ すなわち $OP > 0$ である。
  よって、$OP \cdot OQ = 1$ より $OQ > 0$ すなわち $(x, y) \neq (0, 0)$ である。
  > 💡 讲师批注：求轨迹题必须先确认「分母不为零」与「特殊点（如原点）是否需要剔除」。将 $(0,0)$ 代入原圆方程不为 $0$，说明 $P$ 不会经过原点，因此 $OQ = \frac{1}{OP}$ 恒有意义且 $x^2+y^2 > 0$。

  点 $Q$ は半直線 $OP$ 上にあるから、ある正の実数 $k$ を用いて
  $$\overrightarrow{OP} = k\overrightarrow{OQ} \quad (k > 0)$$
  と表せる。これより $OP = k \cdot OQ$ であるから、条件 $OP \cdot OQ = 1$ に代入して
  $$k \cdot OQ^2 = 1 \iff k = \frac{1}{OQ^2} = \frac{1}{x^2+y^2}$$
  > 💡 讲师批注：这是反演问题的核心一步！利用同向向量 $\overrightarrow{OP} = k\overrightarrow{OQ}$ 与长度关系 $OP = k \cdot OQ$，瞬间消去角度，直接得出比例系数 $k = \dfrac{1}{x^2+y^2}$。

  したがって、$X, Y$ は $x, y$ を用いて次のように表される：
  $$X = \frac{x}{x^2+y^2}, \qquad Y = \frac{y}{x^2+y^2}$$
  また、このとき $X^2 + Y^2 = \dfrac{x^2+y^2}{(x^2+y^2)^2} = \dfrac{1}{x^2+y^2}$ である。
  これらを①に代入すると、
  $$\frac{1}{x^2+y^2} - \frac{2x}{x^2+y^2} + \frac{2y}{x^2+y^2} - 2 = 0$$
  $x^2+y^2 > 0$ より、両辺に $x^2+y^2$ を掛けて整理すると、
  $$1 - 2x + 2y - 2(x^2+y^2) = 0$$
  $$2x^2 + 2y^2 + 2x - 2y - 1 = 0$$
  $$x^2 + y^2 + x - y - \frac{1}{2} = 0$$
  平方完成して、
  $$\left(x + \frac{1}{2}\right)^2 + \left(y - \frac{1}{2}\right)^2 = 1 \qquad \cdots \text{②}$$
  > 💡 讲师批注：配方细节：$x^2 + x = (x+\frac{1}{2})^2 - \frac{1}{4}$，$y^2 - y = (y-\frac{1}{2})^2 - \frac{1}{4}$，常数项移到右边得 $\frac{1}{2} + \frac{1}{4} + \frac{1}{4} = 1$。

  逆に、円②上の任意の点 $Q(x, y)$ について、原点 $(0, 0)$ は②上にない（$\frac{1}{4}+\frac{1}{4}=\frac{1}{2} \neq 1$）から、すべての点で $x^2+y^2 > 0$ であり、対応する点 $P$ が円①上に存在する。
  > 💡 讲师批注：轨迹题的规范收尾——确认逆命题成立且无需剔除原点。特值验算：取 $P(1,1)$ 在原圆上，$OP=\sqrt{2} \implies Q(\frac{1}{2}, \frac{1}{2})$，代入②得 $1^2 + 0^2 = 1$，完全正确！

- **【最终答案】**
  **中心 $\left(-\dfrac{1}{2},\; \dfrac{1}{2}\right)$、半径 $1$ の円 $\left(x + \dfrac{1}{2}\right)^2 + \left(y - \dfrac{1}{2}\right)^2 = 1$**

---

### 第七章 演習問題 13（極座標・極方程式）

#### 演習問題 13-(1)（P199）
- **【原题重现与翻译】**
  - 原题：$O$ を極とする極座標に関して、2点 $A\left(4,\; -\dfrac{\pi}{3}\right),\; B\left(3,\; \dfrac{\pi}{3}\right)$ がある。
    $[1]$ 線分 $AB$ の長さ　$[2]$ $\triangle OAB$ の面積を求めよ。
  - 中文：在以 $O$ 为极点的极坐标系中，有两点 $A\left(4,\; -\dfrac{\pi}{3}\right),\; B\left(3,\; \dfrac{\pi}{3}\right)$。求：$[1]$ 线段 $AB$ 的长度；$[2]$ $\triangle OAB$ 的面积。
- **【考点定位】**
  - 极坐标下两点间距离公式（余弦定理）与三角形面积公式。
- **【图解辅助（SVG 矢量图）】**

<svg viewBox="0 0 380 260" width="380" height="260" xmlns="http://www.w3.org/2000/svg">
  <rect width="380" height="260" fill="#fafafa" rx="8"/>
  <!-- 极点 O=(90, 130), 始线 OX -->
  <line x1="90" y1="130" x2="340" y2="130" stroke="#475569" stroke-width="1.5"/>
  <polygon points="340,130 332,126 332,134" fill="#475569"/>
  <text x="344" y="135" font-size="13" fill="#334155" font-weight="bold">X</text>
  <text x="72" y="135" font-size="13" fill="#0f172a" font-weight="bold">O</text>
  <!-- 比例: 1单位=30px. B(3, pi/3) -> (90+45, 130-77.94) = (135, 52.1) -->
  <!-- A(4, -pi/3) -> (90+60, 130+103.92) = (150, 233.9) -->
  <polygon points="90,130 135,52.1 150,233.9" fill="rgba(59,130,246,0.10)" stroke="#2563eb" stroke-width="2"/>
  <!-- 角度弧 -->
  <path d="M 122 130 A 32 32 0 0 0 106 102.3" fill="none" stroke="#dc2626" stroke-width="1.5"/>
  <text x="124" y="114" font-size="12" fill="#dc2626">π/3</text>
  <path d="M 122 130 A 32 32 0 0 1 106 157.7" fill="none" stroke="#0f766e" stroke-width="1.5"/>
  <text x="122" y="156" font-size="12" fill="#0f766e">-π/3</text>
  <!-- 顶点标注 -->
  <circle cx="90" cy="130" r="3.5" fill="#0f172a"/>
  <circle cx="135" cy="52.1" r="4" fill="#2563eb"/>
  <text x="142" y="48" font-size="13" fill="#1d4ed8" font-weight="bold">B(3, π/3)</text>
  <circle cx="150" cy="233.9" r="4" fill="#2563eb"/>
  <text x="158" y="238" font-size="13" fill="#1d4ed8" font-weight="bold">A(4, -π/3)</text>
  <!-- 边长标注 -->
  <text x="96" y="84" font-size="12" fill="#334155">3</text>
  <text x="102" y="192" font-size="12" fill="#334155">4</text>
  <text x="150" y="148" font-size="12" fill="#1e40af" font-weight="bold">AB = √37</text>
  <text x="210" y="90" font-size="12" fill="#475569">∠AOB = π/3 - (-π/3) = 2π/3</text>
</svg>

- **【分步标准解答】**
  2点 $A, B$ の極座標より、$OA = 4,\; OB = 3$、$\angle AOB = \dfrac{\pi}{3} - \left(-\dfrac{\pi}{3}\right) = \dfrac{2\pi}{3}$ である。

  $[1]$ $\triangle OAB$ に余弦定理（極座標の2点間の距離公式）を適用すると、
  $$AB = \sqrt{4^2 + 3^2 - 2 \cdot 4 \cdot 3 \cos\frac{2\pi}{3}}$$
  > 💡 讲师批注：$\cos\dfrac{2\pi}{3} = -\dfrac{1}{2}$，注意负负得正，不要算成减 $12$！

  $$= \sqrt{16 + 9 - 24 \cdot \left(-\frac{1}{2}\right)} = \sqrt{25 + 12} = \sqrt{37}$$

  $[2]$ $\triangle OAB$ の面積 $S$ は、
  $$S = \frac{1}{2} \cdot 4 \cdot 3 \left|\sin\frac{2\pi}{3}\right| = 6 \cdot \frac{\sqrt{3}}{2} = 3\sqrt{3}$$
  > 💡 讲师批注：直角坐标验算：$A(2, -2\sqrt{3}),\; B\left(\frac{3}{2}, \frac{3\sqrt{3}}{2}\right)$，则 $AB^2 = \left(\frac{1}{2}\right)^2 + \left(\frac{7\sqrt{3}}{2}\right)^2 = \frac{1+147}{4} = 37$，$S = \frac{1}{2}\left|2\cdot\frac{3\sqrt{3}}{2} - (-2\sqrt{3})\cdot\frac{3}{2}\right| = 3\sqrt{3}$，完全吻合。

- **【最终答案】**
  **$[1]\; AB = \sqrt{37} \qquad [2]\; S = 3\sqrt{3}$**

---

#### 演習問題 13-(2)（P199）
- **【原题重现与翻译】**
  - 原题：円 $(x-1)^2 + y^2 = 1$ を極方程式で表せ。
  - 中文：将圆 $(x-1)^2 + y^2 = 1$ 用极方程式表示。
- **【考点定位】**
  - 直角坐标方程化为极坐标方程。
- **【分步标准解答】**
  与えられた円の方程式を展開すると、
  $$x^2 - 2x + 1 + y^2 = 1 \iff x^2 + y^2 - 2x = 0$$
  ここに $x = r\cos\theta,\; y = r\sin\theta$（したがって $x^2 + y^2 = r^2$）を代入すると、
  $$r^2 - 2r\cos\theta = 0$$
  $$r(r - 2\cos\theta) = 0$$
  よって、$r = 0$ または $r = 2\cos\theta$。
  > 💡 讲师批注：因式分解后得到 $r=0$ 或 $r=2\cos\theta$，务必检查 $r=0$（极点 $O$）是否已包含在后者中：当 $\theta = \frac{\pi}{2}$ 时，$r = 2\cos\frac{\pi}{2} = 0$，因此 $r = 2\cos\theta$ 已经包含极点，无需额外写 $r=0$。

  $r = 2\cos\theta$ は $\theta = \dfrac{\pi}{2}$ のとき $r = 0$ となり極 $O$ を含むから、求める極方程式は
  $$r = 2\cos\theta$$
  > 💡 讲师批注：也可直接套用 `[15.4]` ②：中心在 $(a, 0)$、半径为 $a$ 的圆极方程为 $r = 2a\cos\theta$，这里 $a = 1$，立刻得 $r = 2\cos\theta$。

- **【最终答案】**
  **$r = 2\cos\theta$**

---

#### 演習問題 13-(3)（P199）
- **【原题重现与翻译】**
  - 原题：次の極方程式はどのような曲線を表すか。直交座標の方程式で答えよ。
    $[1]\; r = \sqrt{3}\cos\theta + \sin\theta \qquad [2]\; r^2\sin 2\theta = 4$
  - 中文：下列极方程式分别表示怎样的曲线？请用直角坐标方程作答。
- **【考点定位】**
  - 极坐标方程化为直角坐标方程、二倍角公式与圆/双曲线的识别。
- **【分步标准解答】**
  $[1]$ $r = \sqrt{3}\cos\theta + \sin\theta$ の両辺に $r$ を掛けると、
  $$r^2 = \sqrt{3}r\cos\theta + r\sin\theta$$
  > 💡 讲师批注：两边同乘 $r$ 可能会引入增根 $r = 0$（原点），必须验证原点是否满足原极方程！令 $\sqrt{3}\cos\theta + \sin\theta = 0$，有解 $\theta = \frac{2\pi}{3}$（此时 $r=0$），故原点原本就在曲线上，两边同乘 $r$ 为等价变形。

  $r^2 = x^2 + y^2,\; r\cos\theta = x,\; r\sin\theta = y$ を代入すると、
  $$x^2 + y^2 = \sqrt{3}x + y$$
  $$x^2 - \sqrt{3}x + y^2 - y = 0$$
  平方完成して、
  $$\left(x - \frac{\sqrt{3}}{2}\right)^2 + \left(y - \frac{1}{2}\right)^2 = \frac{3}{4} + \frac{1}{4} = 1$$
  よって、中心 $\left(\dfrac{\sqrt{3}}{2},\; \dfrac{1}{2}\right)$、半径 $1$ の円を表す。
  > 💡 讲师批注：另解（辅助角合成法）：$r = 2\left(\frac{\sqrt{3}}{2}\cos\theta + \frac{1}{2}\sin\theta\right) = 2\cos\left(\theta - \frac{\pi}{6}\right)$，这是将圆 $r = 2\cos\theta$ 绕极点逆时针旋转 $\frac{\pi}{6}$ 所得的圆，圆心极坐标为 $\left(1, \frac{\pi}{6}\right)$，即直角坐标 $\left(\frac{\sqrt{3}}{2}, \frac{1}{2}\right)$，半径为 $1$！

  $[2]$ 2倍角の公式 $\sin 2\theta = 2\sin\theta\cos\theta$ を用いて変形すると、
  $$r^2 \cdot 2\sin\theta\cos\theta = 4$$
  $$(r\cos\theta)(r\sin\theta) = 2$$
  $x = r\cos\theta,\; y = r\sin\theta$ を代入すると、
  $$xy = 2$$
  よって、直角双曲線 $xy = 2$（$y = \dfrac{2}{x}$）を表す。
  > 💡 讲师批注：看到 $\sin 2\theta$ 立刻联想到 $2\sin\theta\cos\theta$，配合 $r^2$ 恰好凑出 $(r\cos\theta)(r\sin\theta) = xy$。

- **【最终答案】**
  **$[1]$ 円 $\left(x - \dfrac{\sqrt{3}}{2}\right)^2 + \left(y - \dfrac{1}{2}\right)^2 = 1$（中心 $\left(\dfrac{\sqrt{3}}{2},\; \dfrac{1}{2}\right)$、半径 $1$ の円）**
  **$[2]$ 直角双曲線 $xy = 2$（または $y = \dfrac{2}{x}$）**

---

#### 演習問題 13-(4)（P200）
- **【原题重现与翻译】**
  - 原题：$a, e$ を正の定数、点 $A$ の座標を $(a, 0)$ とし、$A$ を通り始線 $OX$ に垂直な直線を $l$ とする。点 $P$ から $l$ に下ろした垂線を $PH$ とするとき、$e = \dfrac{OP}{PH}$ であるような点 $P$ の軌跡の極方程式を求めよ。ただし、極を $O$ とする。
  - 中文：设 $a, e$ 为正常数，点 $A$ 的坐标为 $(a, 0)$，过 $A$ 且垂直于始线 $OX$ 的直线为 $l$。自点 $P$ 向 $l$ 作垂线 $PH$，求满足 $e = \dfrac{OP}{PH}$ 的点 $P$ 的轨迹的极方程式（以 $O$ 为极点）。
- **【考点定位】**
  - 圆锥曲线（2次曲線）的第二定义与统一极方程式推导。
- **【图解辅助（SVG 矢量图）】**

<svg viewBox="0 0 400 240" width="400" height="240" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="240" fill="#fafafa" rx="8"/>
  <!-- 始线 OX -->
  <line x1="40" y1="150" x2="365" y2="150" stroke="#475569" stroke-width="1.5"/>
  <polygon points="365,150 357,146 357,154" fill="#475569"/>
  <text x="370" y="155" font-size="13" fill="#334155" font-weight="bold">X</text>
  <!-- 准线 l: x=a (x=280) -->
  <line x1="280" y1="25" x2="280" y2="215" stroke="#dc2626" stroke-width="2"/>
  <text x="288" y="38" font-size="13" fill="#dc2626" font-weight="bold">l (x = a)</text>
  <!-- 极点 O=(90, 150) -->
  <circle cx="90" cy="150" r="3.5" fill="#0f172a"/>
  <text x="74" y="166" font-size="13" fill="#0f172a" font-weight="bold">O</text>
  <!-- 点 A(a,0)=(280,150) -->
  <circle cx="280" cy="150" r="3.5" fill="#dc2626"/>
  <text x="286" y="167" font-size="12" fill="#dc2626" font-weight="bold">A(a, 0)</text>
  <!-- 动点 P(r, theta)=(205, 70) -->
  <line x1="90" y1="150" x2="205" y2="70" stroke="#2563eb" stroke-width="2"/>
  <line x1="205" y1="70" x2="280" y2="70" stroke="#0f766e" stroke-width="2"/>
  <line x1="205" y1="70" x2="205" y2="150" stroke="#94a3b8" stroke-width="1.2" stroke-dasharray="4,3"/>
  <!-- 直角符号 -->
  <polyline points="271,70 271,79 280,79" fill="none" stroke="#0f766e" stroke-width="1.2"/>
  <polyline points="271,150 271,141 280,141" fill="none" stroke="#dc2626" stroke-width="1.2"/>
  <!-- 偏角弧 -->
  <path d="M 128 150 A 38 38 0 0 0 121.2 128.3" fill="none" stroke="#2563eb" stroke-width="1.5"/>
  <text x="132" y="142" font-size="12" fill="#2563eb">θ</text>
  <!-- 标注 -->
  <circle cx="205" cy="70" r="4" fill="#2563eb"/>
  <text x="180" y="58" font-size="13" fill="#1d4ed8" font-weight="bold">P(r, θ)</text>
  <circle cx="280" cy="70" r="3.5" fill="#0f766e"/>
  <text x="288" y="75" font-size="13" fill="#0f766e" font-weight="bold">H</text>
  <text x="132" y="102" font-size="12" fill="#1d4ed8">r = OP</text>
  <text x="218" y="62" font-size="12" fill="#0f766e">PH = |a - r cosθ|</text>
  <text x="125" y="168" font-size="11" fill="#64748b">r cosθ</text>
  <text x="20" y="226" font-size="11" fill="#475569">0&lt;e&lt;1: 楕円 / e=1: 放物線 / e&gt;1: 双曲線（離心率 e）</text>
</svg>

- **【分步标准解答】**
  点 $P$ の極座標を $(r, \theta)$（まず $r > 0$ とする）とすると、$OP = r$ である。
  直線 $l$ は極 $O$ から距離 $a$ にあり始線 $OX$ に垂直（直交座標で $x = a$）であるから、点 $P$（横座標 $r\cos\theta$）から直線 $l$ までの距離 $PH$ は
  $$PH = |a - r\cos\theta|$$
  条件 $e = \dfrac{OP}{PH}$ すなわち $OP = e \cdot PH$ に代入すると、
  $$r = e|a - r\cos\theta|$$
  > 💡 讲师批注：很多同学容易直接写成 $PH = a - r\cos\theta$ 而漏掉绝对值！当 $e > 1$（双曲线）时，右支上的点位于准线 $l$ 右侧，此时 $r\cos\theta > a$，必须带绝对值分类讨论，再用极方程允许 $r < 0$ 的性质将其统一！

  絶対値を外すと、次の2つの場合がある：
  1. $a - r\cos\theta > 0$ のとき：
     $$r = e(a - r\cos\theta) \implies r(1 + e\cos\theta) = ea \implies r = \frac{ea}{1 + e\cos\theta} \qquad \cdots \text{①}$$
  2. $a - r\cos\theta < 0$ のとき：
     $$r = -e(a - r\cos\theta) \implies r(1 - e\cos\theta) = -ea \implies r = \frac{-ea}{1 - e\cos\theta} \qquad \cdots \text{②}$$

  ここで、極方程式では $r < 0$ の場合も認め、点 $(r, \theta)$ と点 $(-r, \theta + \pi)$ は同じ点を表す。
  ②において $r$ を $-r$、$\theta$ を $\theta + \pi$ に置き換えると、$\cos(\theta + \pi) = -\cos\theta$ より
  $$-r = \frac{-ea}{1 - e(-\cos\theta)} \iff r = \frac{ea}{1 + e\cos\theta}$$
  となり、①と完全に一致する。
  > 💡 讲师批注：这是 EJU 极坐标最经典、最优雅的结论：在允许 $r < 0$ 的约定下，单一极方程 $r = \dfrac{ea}{1 + e\cos\theta}$ 就能完整表达椭圆（$0<e<1$）、抛物线（$e=1$）以及双曲线的**两支**（$e>1$）！

- **【最终答案】**
  **$r = \dfrac{ea}{1 + e\cos\theta}$**

---

#### 演習問題 13-(5)（P200）
- **【原题重现与翻译】**
  - 原题：曲線 $(x^2+y^2)^2 = x^2 - y^2$ の極方程式を求めよ。また、この曲線の概形をかけ。ただし、原点 $O$ を極、$x$ 軸の正の部分を始線とする。
  - 中文：求曲线 $(x^2+y^2)^2 = x^2 - y^2$ 的极方程式，并画出该曲线的草图（以原点 $O$ 为极点，$x$ 轴正半轴为始线）。
- **【考点定位】**
  - 著名极坐标曲线——伯努利双纽线（レムニスケート / Lemniscate）的极方程化简与图像绘制。
- **【图解辅助（SVG 矢量图）】**

<svg viewBox="0 0 420 260" width="420" height="260" xmlns="http://www.w3.org/2000/svg">
  <rect width="420" height="260" fill="#fafafa" rx="8"/>
  <!-- 坐标轴 原点 (210, 130), 单位长度 140px -->
  <line x1="30" y1="130" x2="395" y2="130" stroke="#475569" stroke-width="1.5"/>
  <polygon points="395,130 387,126 387,134" fill="#475569"/>
  <line x1="210" y1="245" x2="210" y2="15" stroke="#475569" stroke-width="1.5"/>
  <polygon points="210,15 206,23 214,23" fill="#475569"/>
  <text x="385" y="148" font-size="13" fill="#334155" font-style="italic">x</text>
  <text x="218" y="25" font-size="13" fill="#334155" font-style="italic">y</text>
  <!-- 原点切线 y = x 和 y = -x -->
  <line x1="120" y1="220" x2="300" y2="40" stroke="#94a3b8" stroke-width="1.2" stroke-dasharray="5,4"/>
  <line x1="120" y1="40" x2="300" y2="220" stroke="#94a3b8" stroke-width="1.2" stroke-dasharray="5,4"/>
  <text x="295" y="36" font-size="11" fill="#64748b">θ = π/4 (y = x)</text>
  <text x="295" y="226" font-size="11" fill="#64748b">θ = -π/4 (y = -x)</text>
  <!-- 伯努利双纽线 r^2 = cos(2θ), a=140px
       右半支: (210,130) -> (295.7, 80.5) [最高点 θ=π/6, x=0.6124, y=0.3536] -> (350,130) -> (295.7, 179.5) -> (210,130) -->
  <path d="M 210 130
           C 242 98, 272 80.5, 295.7 80.5
           C 326 80.5, 350 100, 350 130
           C 350 160, 326 179.5, 295.7 179.5
           C 272 179.5, 242 162, 210 130
           C 178 98, 148 80.5, 124.3 80.5
           C 94 80.5, 70 100, 70 130
           C 70 160, 94 179.5, 124.3 179.5
           C 148 179.5, 178 162, 210 130 Z"
        fill="rgba(37,99,235,0.08)" stroke="#2563eb" stroke-width="2.5"/>
  <!-- 关键点 -->
  <circle cx="210" cy="130" r="3.5" fill="#0f172a"/>
  <text x="196" y="148" font-size="12" fill="#0f172a" font-weight="bold">O</text>
  <circle cx="350" cy="130" r="4" fill="#dc2626"/>
  <text x="353" y="122" font-size="12" fill="#dc2626" font-weight="bold">1</text>
  <circle cx="70" cy="130" r="4" fill="#dc2626"/>
  <text x="52" y="122" font-size="12" fill="#dc2626" font-weight="bold">-1</text>
  <!-- 第一象限最高点标注 -->
  <circle cx="295.7" cy="80.5" r="3.5" fill="#0f766e"/>
  <text x="260" y="68" font-size="11" fill="#0f766e">最大 y = √2/4 (θ=π/6)</text>
  <text x="20" y="246" font-size="12" fill="#1e40af" font-weight="bold">レムニスケート（双紐線）：r² = cos 2θ</text>
</svg>

- **【分步标准解答】**
  1. **極方程式の導出**：
     $x = r\cos\theta,\; y = r\sin\theta$（したがって $x^2+y^2 = r^2$）を $(x^2+y^2)^2 = x^2 - y^2$ に代入すると、
     $$(r^2)^2 = r^2\cos^2\theta - r^2\sin^2\theta$$
     2倍角の公式 $\cos^2\theta - \sin^2\theta = \cos 2\theta$ より、
     $$r^4 = r^2\cos 2\theta \iff r^2(r^2 - \cos 2\theta) = 0$$
     よって $r = 0$ または $r^2 = \cos 2\theta$。
     $r^2 = \cos 2\theta$ は $\theta = \dfrac{\pi}{4}$ のとき $r = 0$ となり極 $O$ を含むから、求める極方程式は
     $$r^2 = \cos 2\theta$$
     > 💡 讲师批注：$\cos^2\theta - \sin^2\theta = \cos 2\theta$ 是本题变形的点睛之笔，千万不要停留在 $r^2 = \cos^2\theta - \sin^2\theta$。

  2. **曲線の概形の調査**：
     - **対称性**：元の方程式 $(x^2+y^2)^2 = x^2 - y^2$ は $x$ を $-x$ に、また $y$ を $-y$ に代えても変わらないから、曲線は **$x$ 軸、$y$ 軸、および原点 $O$ に関して対称**である。
     - **第1象限（$0 \le \theta \le \dfrac{\pi}{2}$）での増減**：
       $r^2 = \cos 2\theta \ge 0$ より、$0 \le 2\theta \le \dfrac{\pi}{2}$ すなわち $0 \le \theta \le \dfrac{\pi}{4}$ の範囲でのみ曲線が存在する（$\dfrac{\pi}{4} < \theta \le \dfrac{\pi}{2}$ には存在しない）。
       $0 \le \theta \le \dfrac{\pi}{4}$ において $\theta$ が $0$ から $\dfrac{\pi}{4}$ まで増加するとき、$r = \sqrt{\cos 2\theta}$ は $1$ から $0$ まで単調に減少する：
       - $\theta = 0$ のとき $r = 1$（点 $(1, 0)$）
       - $\theta = \dfrac{\pi}{6}$ のとき $r = \dfrac{1}{\sqrt{2}}$（このとき $y = r\sin\theta = \dfrac{\sqrt{2}}{4}$ で最大値をとる）
       - $\theta = \dfrac{\pi}{4}$ のとき $r = 0$（原点 $O$ に直線 $y = x$ に接しながら近づく）
     - 対称性より、他の象限にも折り返すと、上図のような横向きの「$\infty$」字型の曲線（**レムニスケート / 双纽线**）が得られる。

- **【最终答案】**
  **極方程式：$r^2 = \cos 2\theta$（概形は上の SVG 図を参照：原点で $y = \pm x$ に接し、$(\pm 1, 0)$ を通る「$\infty$」型のレムニスケート）**

---

### 第八章 演習問題 1（ベクトルの演算）

#### 演習問題 1-(1)（P204）
- **【原题重现与翻译】**
  - 原题：次の等式が成り立つことを証明せよ。
    $$\overrightarrow{AB} + \overrightarrow{EC} + \overrightarrow{FD} = \overrightarrow{EB} + \overrightarrow{FC} + \overrightarrow{AD}$$
  - 中文：证明上述向量等式成立。
- **【考点定位】**
  - 向量减法的「统一始点法」（$\overrightarrow{XY} = \overrightarrow{OY} - \overrightarrow{OX}$）。
- **【分步标准解答】**
  任意の点 $O$ を始点として、各ベクトルを差の形に表すと、
  $$\begin{aligned}
  \text{左辺} &= (\overrightarrow{OB} - \overrightarrow{OA}) + (\overrightarrow{OC} - \overrightarrow{OE}) + (\overrightarrow{OD} - \overrightarrow{OF}) \\
  &= (\overrightarrow{OB} - \overrightarrow{OE}) + (\overrightarrow{OC} - \overrightarrow{OF}) + (\overrightarrow{OD} - \overrightarrow{OA}) \\
  &= \overrightarrow{EB} + \overrightarrow{FC} + \overrightarrow{AD} = \text{右辺}
  \end{aligned}$$
  よって、与えられた等式は成り立つ。（証明終）
  > 💡 讲师批注：所有涉及多点向量加减恒等式的证明，**「统一始点拆成差向量」**（或把右边移项到左边合并成闭环 $\overrightarrow{AE}+\overrightarrow{EF}+\overrightarrow{FA}=\vec{0}$）都是百试百灵的必杀技！

- **【最终答案】**
  **证明见上（利用任意始点 $O$ 展开为差向量重新组合即得证）。**

---

#### 演習問題 1-(2)（P204）
- **【原题重现与翻译】**
  - 原题：
    $[1]$ $\vec{x} = 2\vec{a} - 3\vec{b} - \vec{c},\; \vec{y} = -4\vec{a} + 5\vec{b} - 3\vec{c}$ のとき、$\vec{x} - \vec{y}$ を $\vec{a}, \vec{b}, \vec{c}$ で表せ。
    $[2]$ $4\vec{x} - 3\vec{a} = \vec{x} + 6\vec{b}$ を満たす $\vec{x}$ を $\vec{a}, \vec{b}$ で表せ。
    $[3]$ $3\vec{x} + \vec{y} = \vec{a},\; 5\vec{x} + 2\vec{y} = \vec{b}$ を満たす $\vec{x}, \vec{y}$ を $\vec{a}, \vec{b}$ で表せ。
  - 中文：按要求将未知向量用 $\vec{a}, \vec{b}, \vec{c}$ 表示。
- **【考点定位】**
  - 向量的线性运算（与多项式/一次方程组运算律完全一致）。
- **【分步标准解答】**
  $[1]$
  $$\begin{aligned}
  \vec{x} - \vec{y} &= (2\vec{a} - 3\vec{b} - \vec{c}) - (-4\vec{a} + 5\vec{b} - 3\vec{c}) \\
  &= (2 + 4)\vec{a} + (-3 - 5)\vec{b} + (-1 + 3)\vec{c} \\
  &= 6\vec{a} - 8\vec{b} + 2\vec{c}
  \end{aligned}$$
  > 💡 讲师批注：去括号时注意负号变号：$-(-4\vec{a}) = +4\vec{a}$，$-(-3\vec{c}) = +3\vec{c}$。

  $[2]$ 移項して整理すると、
  $$4\vec{x} - \vec{x} = 3\vec{a} + 6\vec{b}$$
  $$3\vec{x} = 3\vec{a} + 6\vec{b}$$
  両辺を $3$ で割って、
  $$\vec{x} = \vec{a} + 2\vec{b}$$

  $[3]$ 与えられた連立方程式を
  $$\begin{cases} 3\vec{x} + \vec{y} = \vec{a} & \cdots \text{①} \\ 5\vec{x} + 2\vec{y} = \vec{b} & \cdots \text{②} \end{cases}$$
  とおく。$\text{①} \times 2 - \text{②}$ より、
  $$(6\vec{x} + 2\vec{y}) - (5\vec{x} + 2\vec{y}) = 2\vec{a} - \vec{b}$$
  $$\vec{x} = 2\vec{a} - \vec{b}$$
  これを①に代入すると、
  $$3(2\vec{a} - \vec{b}) + \vec{y} = \vec{a}$$
  $$\vec{y} = \vec{a} - 6\vec{a} + 3\vec{b} = -5\vec{a} + 3\vec{b}$$
  > 💡 讲师批注：代回②验算：$5(2\vec{a}-\vec{b}) + 2(-5\vec{a}+3\vec{b}) = (10-10)\vec{a} + (-5+6)\vec{b} = \vec{b}$，完全正确！

- **【最终答案】**
  **$[1]\; \vec{x} - \vec{y} = 6\vec{a} - 8\vec{b} + 2\vec{c}$**
  **$[2]\; \vec{x} = \vec{a} + 2\vec{b}$**
  **$[3]\; \vec{x} = 2\vec{a} - \vec{b},\quad \vec{y} = -5\vec{a} + 3\vec{b}$**

---

#### 演習問題 1-(3)（P204）
- **【原题重现与翻译】**
  - 原题：正六角形 $ABCDEF$ において、中心を $O$，辺 $CD$ を $2:1$ 内分する点を $P$，辺 $EF$ の中点を $Q$ とする。$\overrightarrow{AB} = \vec{a},\; \overrightarrow{AF} = \vec{b}$ とするとき、ベクトル $\overrightarrow{BC}, \overrightarrow{EF}, \overrightarrow{CE}, \overrightarrow{AC}, \overrightarrow{BD}, \overrightarrow{QP}$ をそれぞれ $\vec{a}, \vec{b}$ で表せ。
  - 中文：在正六边形 $ABCDEF$ 中，中心为 $O$，点 $P$ 将边 $CD$ 按 $2:1$ 内分，点 $Q$ 为边 $EF$ 的中点。设 $\overrightarrow{AB} = \vec{a},\; \overrightarrow{AF} = \vec{b}$，分别用 $\vec{a}, \vec{b}$ 表示向量 $\overrightarrow{BC}, \overrightarrow{EF}, \overrightarrow{CE}, \overrightarrow{AC}, \overrightarrow{BD}, \overrightarrow{QP}$。
- **【考点定位】**
  - 正六边形的几何对称性与向量基底分解。
- **【图解辅助（SVG 矢量图）】**

<svg viewBox="0 0 380 280" width="380" height="280" xmlns="http://www.w3.org/2000/svg">
  <rect width="380" height="280" fill="#fafafa" rx="8"/>
  <!-- 正六边形中心 O=(190, 140), 外接圆半径 R=95
       A(左下左) 210° -> (107.7, 187.5)
       B(正下)   270° -> (190, 235)
       C(右下)   330° -> (272.3, 187.5)
       D(右上)    30° -> (272.3, 92.5)
       E(正上)    90° -> (190, 45)
       F(左上)   150° -> (107.7, 92.5)
       注：SVG y轴向下，故A=(107.7,187.5), B=(190,235), C=(272.3,187.5), D=(272.3,92.5), E=(190,45), F=(107.7,92.5) 逆时针排列！ -->
  <polygon points="107.7,187.5 190,235 272.3,187.5 272.3,92.5 190,45 107.7,92.5"
           fill="rgba(59,130,246,0.05)" stroke="#334155" stroke-width="1.8"/>
  <!-- 内部辅助线过中心 O -->
  <line x1="107.7" y1="187.5" x2="272.3" y2="92.5" stroke="#cbd5e1" stroke-width="1.2" stroke-dasharray="4,3"/>
  <line x1="190" y1="235" x2="190" y2="45" stroke="#cbd5e1" stroke-width="1.2" stroke-dasharray="4,3"/>
  <line x1="272.3" y1="187.5" x2="107.7" y2="92.5" stroke="#cbd5e1" stroke-width="1.2" stroke-dasharray="4,3"/>
  <!-- 基底向量 a = AB, b = AF -->
  <defs>
    <marker id="arrBlue" markerWidth="8" markerHeight="8" refX="7" refY="3.5" orient="auto">
      <polygon points="0,0 8,3.5 0,7" fill="#2563eb"/>
    </marker>
    <marker id="arrRed" markerWidth="8" markerHeight="8" refX="7" refY="3.5" orient="auto">
      <polygon points="0,0 8,3.5 0,7" fill="#dc2626"/>
    </marker>
    <marker id="arrGreen" markerWidth="8" markerHeight="8" refX="7" refY="3.5" orient="auto">
      <polygon points="0,0 8,3.5 0,7" fill="#0f766e"/>
    </marker>
  </defs>
  <line x1="107.7" y1="187.5" x2="184" y2="231.5" stroke="#2563eb" stroke-width="2.5" marker-end="url(#arrBlue)"/>
  <line x1="107.7" y1="187.5" x2="107.7" y2="99" stroke="#dc2626" stroke-width="2.5" marker-end="url(#arrRed)"/>
  <!-- 点 P (CD 2:1 内分): C=(272.3,187.5), D=(272.3,92.5) -> P=(272.3, 124.2) -->
  <!-- 点 Q (EF 中点): E=(190,45), F=(107.7,92.5) -> Q=(148.9, 68.75) -->
  <line x1="148.9" y1="68.75" x2="266" y2="121.3" stroke="#0f766e" stroke-width="2.3" marker-end="url(#arrGreen)"/>
  <circle cx="272.3" cy="124.2" r="4" fill="#0f766e"/>
  <circle cx="148.9" cy="68.75" r="4" fill="#0f766e"/>
  <circle cx="190" cy="140" r="3" fill="#475569"/>
  <!-- 顶点标注 -->
  <text x="90" y="196" font-size="13" fill="#0f172a" font-weight="bold">A</text>
  <text x="185" y="253" font-size="13" fill="#0f172a" font-weight="bold">B</text>
  <text x="279" y="195" font-size="13" fill="#0f172a" font-weight="bold">C</text>
  <text x="279" y="94" font-size="13" fill="#0f172a" font-weight="bold">D</text>
  <text x="186" y="36" font-size="13" fill="#0f172a" font-weight="bold">E</text>
  <text x="90" y="94" font-size="13" fill="#0f172a" font-weight="bold">F</text>
  <text x="196" y="152" font-size="12" fill="#475569" font-weight="bold">O</text>
  <text x="281" y="129" font-size="13" fill="#0f766e" font-weight="bold">P</text>
  <text x="278" y="159" font-size="11" fill="#64748b">2</text>
  <text x="278" y="110" font-size="11" fill="#64748b">1</text>
  <text x="134" y="61" font-size="13" fill="#0f766e" font-weight="bold">Q</text>
  <!-- 向量名 -->
  <text x="135" y="226" font-size="13" fill="#2563eb" font-weight="bold">a</text>
  <text x="88" y="146" font-size="13" fill="#dc2626" font-weight="bold">b</text>
  <text x="208" y="88" font-size="12" fill="#0f766e" font-weight="bold">QP</text>
</svg>

- **【分步标准解答】**
  正六角形の性質より、四角形 $ABOF$ はひし形であるから、
  $$\overrightarrow{AO} = \overrightarrow{AB} + \overrightarrow{AF} = \vec{a} + \vec{b}$$
  また、対辺の平行性と長さの関係より、
  $$\overrightarrow{BC} = \overrightarrow{AO} = \overrightarrow{FE} = \vec{a} + \vec{b}, \qquad \overrightarrow{CD} = \overrightarrow{AF} = \vec{b}, \qquad \overrightarrow{ED} = \overrightarrow{AB} = \vec{a}$$
  > 💡 讲师批注：解正六边形向量题的**黄金起手式**：先看出 $ABOF$ 是菱形，立即得到 $\overrightarrow{AO} = \vec{a}+\vec{b}$，从而正六边形 6 条边方向的向量全部打通（$\vec{a},\; \vec{b},\; \vec{a}+\vec{b}$ 及其相反向量）！

  これを用いて、各ベクトルを順次求める：
  1. $\overrightarrow{BC} = \overrightarrow{AO} = \vec{a} + \vec{b}$
  2. $\overrightarrow{EF} = -\overrightarrow{FE} = -\overrightarrow{BC} = -\vec{a} - \vec{b}$
  3. $\overrightarrow{CE} = \overrightarrow{CD} + \overrightarrow{DE} = \overrightarrow{AF} + (-\overrightarrow{AB}) = -\vec{a} + \vec{b}$
  4. $\overrightarrow{AC} = \overrightarrow{AB} + \overrightarrow{BC} = \vec{a} + (\vec{a} + \vec{b}) = 2\vec{a} + \vec{b}$
  5. $\overrightarrow{BD} = \overrightarrow{BC} + \overrightarrow{CD} = (\vec{a} + \vec{b}) + \vec{b} = \vec{a} + 2\vec{b}$
  6. 点 $Q$ は辺 $EF$ の中点より $\overrightarrow{QE} = \dfrac{1}{2}\overrightarrow{FE} = \dfrac{1}{2}(\vec{a} + \vec{b})$、
     点 $P$ は辺 $CD$ を $2:1$ に内分するから $DP:PC = 1:2$、すなわち $\overrightarrow{DP} = \dfrac{1}{3}\overrightarrow{DC} = -\dfrac{1}{3}\overrightarrow{CD} = -\dfrac{1}{3}\vec{b}$。
     よって、経路 $Q \to E \to D \to P$ に沿って足し合わせると、
     $$\begin{aligned}
     \overrightarrow{QP} &= \overrightarrow{QE} + \overrightarrow{ED} + \overrightarrow{DP} \\
     &= \frac{1}{2}(\vec{a} + \vec{b}) + \vec{a} + \left(-\frac{1}{3}\vec{b}\right) \\
     &= \left(\frac{1}{2} + 1\right)\vec{a} + \left(\frac{1}{2} - \frac{1}{3}\right)\vec{b} \\
     &= \frac{3}{2}\vec{a} + \frac{1}{6}\vec{b}
     \end{aligned}$$
  > 💡 讲师批注：计算 $\overrightarrow{DP}$ 时切忌把 $2:1$ 的比例看反！题干是「辺 $CD$ を $2:1$ に内分」，即 $CP:PD = 2:1$，所以从 $D$ 到 $P$ 占 $\overrightarrow{DC}$ 的 $\frac{1}{3}$。

- **【最终答案】**
  **$\overrightarrow{BC} = \vec{a} + \vec{b},\quad \overrightarrow{EF} = -\vec{a} - \vec{b},\quad \overrightarrow{CE} = -\vec{a} + \vec{b},$**
  **$\overrightarrow{AC} = 2\vec{a} + \vec{b},\quad \overrightarrow{BD} = \vec{a} + 2\vec{b},\quad \overrightarrow{QP} = \dfrac{3}{2}\vec{a} + \dfrac{1}{6}\vec{b}$**

---

### 第八章 演習問題 2（ベクトルの成分）

#### 演習問題 2-(1)（P206）
- **【原题重现与翻译】**
  - 原题：2つのベクトル $\vec{a} = (3, -1),\; \vec{b} = (7-2t,\; -5+t)$ が平行になるように、$t$ の値を定めよ。
  - 中文：确定实数 $t$ 的值，使两个向量 $\vec{a} = (3, -1)$ 与 $\vec{b} = (7-2t,\; -5+t)$ 平行。
- **【考点定位】**
  - 向量平行的坐标（成分）充要条件：$a_1 b_2 - a_2 b_1 = 0$。
- **【分步标准解答】**
  $\vec{a} = (3, -1) \neq \vec{0}$ であり、また $7-2t = 0$ と $-5+t = 0$ を同時に満たす実数 $t$ は存在しないから、任意の $t$ に対して $\vec{b} \neq \vec{0}$ である。
  よって、$\vec{a} \parallel \vec{b}$ となる条件は $a_1 b_2 - a_2 b_1 = 0$ より、
  $$3(-5 + t) - (-1)(7 - 2t) = 0$$
  > 💡 讲师批注：平行条件「交叉相乘之差为 $0$」（$a_1 b_2 - a_2 b_1 = 0$）极易与垂直条件「对应相乘之和为 $0$」（$a_1 b_1 + a_2 b_2 = 0$）混淆，务必牢记！

  $$-15 + 3t + 7 - 2t = 0$$
  $$t - 8 = 0 \implies t = 8$$
  > 💡 讲师批注：代回验算：$t = 8$ 时 $\vec{b} = (-9, 3) = -3(3, -1) = -3\vec{a}$，确实平行（反向）。

- **【最终答案】**
  **$t = 8$**

---

#### 演習問題 2-(2)（P207）
- **【原题重现与翻译】**
  - 原题：3点 $A(1, 3),\; B(3, -2),\; C(4, 1)$ がある。
    $[1]$ $\overrightarrow{AB},\; \overrightarrow{BC},\; \overrightarrow{CA}$ の成分と大きさをそれぞれ求めよ。
    $[2]$ 四角形 $ABCD$ が平行四辺形であるとき、点 $D$ の座標を求めよ。
    $[3]$ $[2]$ の平行四辺形について、2本の対角線の長さを求めよ。
  - 中文：已知三点 $A(1, 3),\; B(3, -2),\; C(4, 1)$。
    $[1]$ 分别求 $\overrightarrow{AB},\; \overrightarrow{BC},\; \overrightarrow{CA}$ 的坐标（成分）与模长；
    $[2]$ 当四边形 $ABCD$ 为平行四边形时，求点 $D$ 的坐标；
    $[3]$ 求 $[2]$ 中平行四边形的两条对角线的长度。
- **【考点定位】**
  - 坐标平面上的向量表示、模长公式、平行四边形的向量判定。
- **【图解辅助（SVG 矢量图）】**

<svg viewBox="0 0 360 280" width="360" height="280" xmlns="http://www.w3.org/2000/svg">
  <rect width="360" height="280" fill="#fafafa" rx="8"/>
  <!-- 坐标系: 原点 O=(60, 210), 1单位=30px
       A(1,3) -> (90, 120)
       B(3,-2)-> (150, 270)? 稍微上移原点: O=(60, 195), 1单位=26px
       A(1,3) -> (86, 117)
       B(3,-2)-> (138, 247)
       C(4,1) -> (164, 169)
       D(2,6) -> (112, 39) -->
  <line x1="25" y1="195" x2="290" y2="195" stroke="#475569" stroke-width="1.5"/>
  <polygon points="290,195 282,191 282,199" fill="#475569"/>
  <line x1="60" y1="268" x2="60" y2="18" stroke="#475569" stroke-width="1.5"/>
  <polygon points="60,18 56,26 64,26" fill="#475569"/>
  <text x="282" y="212" font-size="12" fill="#334155" font-style="italic">x</text>
  <text x="68" y="28" font-size="12" fill="#334155" font-style="italic">y</text>
  <text x="45" y="210" font-size="12" fill="#334155">O</text>
  <!-- 平行四边形 ABCD -->
  <polygon points="86,117 138,247 164,169 112,39" fill="rgba(59,130,246,0.08)" stroke="#2563eb" stroke-width="2"/>
  <!-- 对角线 AC, BD -->
  <line x1="86" y1="117" x2="164" y2="169" stroke="#dc2626" stroke-width="1.6" stroke-dasharray="5,3"/>
  <line x1="138" y1="247" x2="112" y2="39" stroke="#0f766e" stroke-width="1.6" stroke-dasharray="5,3"/>
  <!-- 顶点 -->
  <circle cx="86" cy="117" r="3.5" fill="#1d4ed8"/>
  <text x="32" y="114" font-size="12" fill="#1d4ed8" font-weight="bold">A(1, 3)</text>
  <circle cx="138" cy="247" r="3.5" fill="#1d4ed8"/>
  <text x="145" y="255" font-size="12" fill="#1d4ed8" font-weight="bold">B(3, -2)</text>
  <circle cx="164" cy="169" r="3.5" fill="#1d4ed8"/>
  <text x="172" y="173" font-size="12" fill="#1d4ed8" font-weight="bold">C(4, 1)</text>
  <circle cx="112" cy="39" r="3.5" fill="#dc2626"/>
  <text x="120" y="38" font-size="12" fill="#dc2626" font-weight="bold">D(2, 6)</text>
  <!-- 对角线标注 -->
  <text x="200" y="80" font-size="12" fill="#dc2626">AC = √13</text>
  <text x="200" y="102" font-size="12" fill="#0f766e">BD = √65</text>
  <text x="200" y="128" font-size="11" fill="#475569">AD = BC = (1, 3)</text>
</svg>

- **【分步标准解答】**
  $[1]$ 終点の座標から始点の座標を引いて、
  - $\overrightarrow{AB} = (3 - 1,\; -2 - 3) = (2, -5)$
    $$|\overrightarrow{AB}| = \sqrt{2^2 + (-5)^2} = \sqrt{4 + 25} = \sqrt{29}$$
  - $\overrightarrow{BC} = (4 - 3,\; 1 - (-2)) = (1, 3)$
    $$|\overrightarrow{BC}| = \sqrt{1^2 + 3^2} = \sqrt{1 + 9} = \sqrt{10}$$
  - $\overrightarrow{CA} = (1 - 4,\; 3 - 1) = (-3, 2)$
    $$|\overrightarrow{CA}| = \sqrt{(-3)^2 + 2^2} = \sqrt{9 + 4} = \sqrt{13}$$
  > 💡 讲师批注：快速验算技巧：封闭三角形三边向量之和必为零向量：$\overrightarrow{AB}+\overrightarrow{BC}+\overrightarrow{CA} = (2+1-3,\; -5+3+2) = (0, 0)$，说明坐标全部正确！

  $[2]$ 点 $D$ の座標を $(x, y)$ とする。
  四角形 $ABCD$ が平行四辺形（頂点が $A \to B \to C \to D$ の順）であるための条件は $\overrightarrow{AD} = \overrightarrow{BC}$ である。
  $$\overrightarrow{AD} = (x - 1,\; y - 3), \qquad \overrightarrow{BC} = (1, 3)$$
  より、
  $$x - 1 = 1,\quad y - 3 = 3 \implies x = 2,\quad y = 6$$
  よって、$D(2, 6)$。
  > 💡 讲师批注：审题注意！「四角形 $ABCD$ が平行四辺形」按固定顶点顺序排列，只有唯一解 $D(2, 6)$；若题目问「4点 $A, B, C, D$ を頂点とする平行四辺形」才需要分 3 种情况讨论。

  $[3]$ 平行四辺形 $ABCD$ の2本の対角線は $AC$ と $BD$ である。
  - $AC = |\overrightarrow{CA}| = \sqrt{13}$
  - $\overrightarrow{BD} = (2 - 3,\; 6 - (-2)) = (-1, 8)$ より、
    $$BD = |\overrightarrow{BD}| = \sqrt{(-1)^2 + 8^2} = \sqrt{1 + 64} = \sqrt{65}$$
  > 💡 讲师批注：平行四边形对角线恒等式验算：$AC^2 + BD^2 = 2(AB^2 + BC^2)$。左边 $= 13 + 65 = 78$，右边 $= 2(29 + 10) = 78$，完美验证！

- **【最终答案】**
  **$[1]$ $\overrightarrow{AB} = (2, -5),\; |\overrightarrow{AB}| = \sqrt{29}$；$\overrightarrow{BC} = (1, 3),\; |\overrightarrow{BC}| = \sqrt{10}$；$\overrightarrow{CA} = (-3, 2),\; |\overrightarrow{CA}| = \sqrt{13}$**
  **$[2]$ $D(2, 6)$**
  **$[3]$ $\sqrt{13},\; \sqrt{65}$**

---

#### 演習問題 2-(3)（P207）
- **【原题重现与翻译】**
  - 原题：$t$ は実数とする。$\vec{a} = (2, 1),\; \vec{b} = (3, 4)$ に対して、$|\vec{a} + t\vec{b}|$ は $t = \square$ のとき最小値 $\square$ をとる。
  - 中文：设 $t$ 为实数。对于 $\vec{a} = (2, 1),\; \vec{b} = (3, 4)$，当 $t = \square$ 时，$|\vec{a} + t\vec{b}|$ 取最小值 $\square$。
- **【考点定位】**
  - 含参向量模长的最小值（配方求二次函数最值 / 几何正射影垂足法）。
- **【图解辅助（SVG 矢量图）】**

<svg viewBox="0 0 360 220" width="360" height="220" xmlns="http://www.w3.org/2000/svg">
  <rect width="360" height="220" fill="#fafafa" rx="8"/>
  <!-- 几何意义：从原点 O 到直线 P(t) = a + t*b 的最短距离即为垂线段长 -->
  <!-- 设 O=(80, 160), 1单位=45px
       a=(2,1) -> (170, 115)
       b=(3,4) 方向向量 (0.6, 0.8), SVG中 (0.6, -0.8)
       t=-2/5 时垂足 H = (4/5, -3/5) -> (80+36, 160+27) = (116, 187)
       直线 l 过 A(170,115) 方向 (3,-4): t=-1 -> (-1,-3)不对, (2-3, 1-4)=(-1,-3) -> (35, 295) -->
  <!-- 直线 a + t*b -->
  <line x1="89" y1="223" x2="233" y2="31" stroke="#94a3b8" stroke-width="1.8" stroke-dasharray="5,3"/>
  <text x="236" y="42" font-size="12" fill="#475569">直線 a + t b</text>
  <!-- 原点 O=(80,160), A=(170,115), H=(116,187) -->
  <defs>
    <marker id="arrB2" markerWidth="7" markerHeight="7" refX="6" refY="3.5" orient="auto">
      <polygon points="0,0 7,3.5 0,7" fill="#2563eb"/>
    </marker>
    <marker id="arrR2" markerWidth="7" markerHeight="7" refX="6" refY="3.5" orient="auto">
      <polygon points="0,0 7,3.5 0,7" fill="#dc2626"/>
    </marker>
  </defs>
  <line x1="80" y1="160" x2="165" y2="117.5" stroke="#2563eb" stroke-width="2" marker-end="url(#arrB2)"/>
  <line x1="80" y1="160" x2="112" y2="184" stroke="#dc2626" stroke-width="2.4" marker-end="url(#arrR2)"/>
  <!-- 直角符号在 H(116, 187) -->
  <polyline points="109,181.75 114.25,174.75 121.25,180" fill="none" stroke="#dc2626" stroke-width="1.3"/>
  <circle cx="80" cy="160" r="3.5" fill="#0f172a"/>
  <text x="64" y="164" font-size="13" fill="#0f172a" font-weight="bold">O</text>
  <circle cx="170" cy="115" r="3.5" fill="#2563eb"/>
  <text x="178" y="122" font-size="12" fill="#1d4ed8" font-weight="bold">A(2, 1)</text>
  <text x="116" y="132" font-size="12" fill="#1d4ed8">a</text>
  <circle cx="116" cy="187" r="3.5" fill="#dc2626"/>
  <text x="123" y="198" font-size="12" fill="#dc2626" font-weight="bold">H (t = -2/5)</text>
  <text x="200" y="145" font-size="12" fill="#dc2626" font-weight="bold">最小値 OH = 1</text>
  <text x="200" y="165" font-size="11" fill="#475569">(a + t b) ⊥ b のとき最小</text>
</svg>

- **【分步标准解答】**
  $\vec{a} + t\vec{b}$ の成分は、
  $$\vec{a} + t\vec{b} = (2, 1) + t(3, 4) = (2 + 3t,\; 1 + 4t)$$
  したがって、大きさの2乗は
  $$\begin{aligned}
  |\vec{a} + t\vec{b}|^2 &= (2 + 3t)^2 + (1 + 4t)^2 \\
  &= (4 + 12t + 9t^2) + (1 + 8t + 16t^2) \\
  &= 25t^2 + 20t + 5 \\
  &= 25\left(t^2 + \frac{4}{5}t\right) + 5 \\
  &= 25\left(t + \frac{2}{5}\right)^2 - 25 \cdot \frac{4}{25} + 5 \\
  &= 25\left(t + \frac{2}{5}\right)^2 + 1
  \end{aligned}$$
  > 💡 讲师批注：求 $|\vec{a}+t\vec{b}|$ 最小值的通法是**先平方去掉根号**，化为关于 $t$ 的二次函数配方，最后记得**开平方**（本题 $\sqrt{1}=1$ 恰好相等，但若最小平方值是 $2$ 则答案是 $\sqrt{2}$，切勿忘开根号！）。

  $|\vec{a} + t\vec{b}| \ge 0$ であるから、$|\vec{a} + t\vec{b}|$ は $t = -\dfrac{2}{5}$ のとき最小値 $\sqrt{1} = 1$ をとる。
  > 💡 讲师批注：**内积秒杀验算**：几何上当 $(\vec{a}+t\vec{b}) \perp \vec{b}$ 时模长最小，即 $\vec{a}\cdot\vec{b} + t|\vec{b}|^2 = 0 \implies (2\cdot 3 + 1\cdot 4) + 25t = 0 \implies t = -\frac{10}{25} = -\frac{2}{5}$，此时 $\vec{a} - \frac{2}{5}\vec{b} = \left(\frac{4}{5}, -\frac{3}{5}\right)$，模长恰为 $1$！

- **【最终答案】**
  **$t = -\dfrac{2}{5}$ のとき最小値 $1$**

---

### 第八章 演習問題 3（ベクトルの内積）

#### 演習問題 3-(1)（P210）
- **【原题重现与翻译】**
  - 原题：$p$ を正の数とし、ベクトル $\vec{a} = (1, 1)$ と $\vec{b} = (1, -p)$ があるとする。いま、$\vec{a}$ と $\vec{b}$ のなす角が $60^\circ$ のとき、$p$ の値を求めよ。
  - 中文：设 $p$ 为正数，已知向量 $\vec{a} = (1, 1)$ 与 $\vec{b} = (1, -p)$。若 $\vec{a}$ 与 $\vec{b}$ 的夹角为 $60^\circ$，求 $p$ 的值。
- **【考点定位】**
  - 向量内积与夹角公式、无理方程求解与增根检验。
- **【图解辅助（SVG 矢量图）】**

<svg viewBox="0 0 340 240" width="340" height="240" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="240" fill="#fafafa" rx="8"/>
  <!-- 原点 O=(80, 140), 1单位=110px -->
  <line x1="30" y1="140" x2="310" y2="140" stroke="#475569" stroke-width="1.5"/>
  <polygon points="310,140 302,136 302,144" fill="#475569"/>
  <line x1="80" y1="225" x2="80" y2="18" stroke="#475569" stroke-width="1.5"/>
  <polygon points="80,18 76,26 84,26" fill="#475569"/>
  <text x="302" y="156" font-size="12" fill="#334155" font-style="italic">x</text>
  <text x="88" y="28" font-size="12" fill="#334155" font-style="italic">y</text>
  <text x="64" y="155" font-size="12" fill="#334155">O</text>
  <defs>
    <marker id="arrB3" markerWidth="8" markerHeight="8" refX="7" refY="3.5" orient="auto">
      <polygon points="0,0 8,3.5 0,7" fill="#2563eb"/>
    </marker>
    <marker id="arrR3" markerWidth="8" markerHeight="8" refX="7" refY="3.5" orient="auto">
      <polygon points="0,0 8,3.5 0,7" fill="#dc2626"/>
    </marker>
  </defs>
  <!-- a=(1,1) -> (190, 30) -->
  <line x1="80" y1="140" x2="185" y2="35" stroke="#2563eb" stroke-width="2.2" marker-end="url(#arrB3)"/>
  <text x="195" y="38" font-size="12" fill="#1d4ed8" font-weight="bold">a = (1, 1)</text>
  <!-- b=(1, -(2-sqrt(3))) = (1, -0.268) -> (190, 169.5) -->
  <line x1="80" y1="140" x2="184" y2="167.9" stroke="#dc2626" stroke-width="2.2" marker-end="url(#arrR3)"/>
  <text x="195" y="176" font-size="12" fill="#dc2626" font-weight="bold">b = (1, -p)</text>
  <!-- 角度弧: 45° 和 -15°, 合计 60° -->
  <path d="M 122 140 A 42 42 0 0 0 109.7 110.3" fill="none" stroke="#2563eb" stroke-width="1.3"/>
  <text x="125" y="124" font-size="11" fill="#2563eb">45°</text>
  <path d="M 122 140 A 42 42 0 0 1 120.6 150.9" fill="none" stroke="#dc2626" stroke-width="1.3"/>
  <text x="128" y="153" font-size="11" fill="#dc2626">15°</text>
  <text x="195" y="110" font-size="12" fill="#0f766e" font-weight="bold">なす角 60°</text>
  <text x="195" y="128" font-size="11" fill="#475569">p = tan 15° = 2 - √3</text>
</svg>

- **【分步标准解答】**
  各ベクトルの大きさと内積を求めると、
  $$|\vec{a}| = \sqrt{1^2 + 1^2} = \sqrt{2}, \qquad |\vec{b}| = \sqrt{1^2 + (-p)^2} = \sqrt{1 + p^2}$$
  $$\vec{a} \cdot \vec{b} = 1 \cdot 1 + 1 \cdot (-p) = 1 - p$$
  $\vec{a}$ と $\vec{b}$ のなす角が $60^\circ$ であるから、内積の定義より
  $$\vec{a} \cdot \vec{b} = |\vec{a}||\vec{b}|\cos 60^\circ$$
  $$1 - p = \sqrt{2}\sqrt{1 + p^2} \cdot \frac{1}{2}$$
  $$2(1 - p) = \sqrt{2(1 + p^2)} \qquad \cdots \text{①}$$
  > 💡 讲师批注：**最高频失分点！** 两边平方之前，必须先写出右端 $\ge 0$ 所决定的隐含符号条件 $1 - p > 0$（即 $p < 1$）。若直接平方而不验根，就会把对应夹角 $120^\circ$ 的增根 $p = 2 + \sqrt{3}$ 误留下来！

  ここで右辺は正であるから、$1 - p > 0$ すなわち $p < 1$ でなければならない。
  条件 $p > 0$ と合わせて $0 < p < 1$ …… ②。
  ①の両辺を2乗すると、
  $$4(1 - 2p + p^2) = 2(1 + p^2)$$
  $$2 - 4p + 2p^2 = 1 + p^2$$
  $$p^2 - 4p + 1 = 0$$
  解の公式より、
  $$p = 2 \pm \sqrt{3}$$
  ②を満たすのは $p = 2 - \sqrt{3}$ である（$2 + \sqrt{3} > 1$ は不適）。
  > 💡 讲师批注：几何角度验算：$\vec{a}=(1,1)$ 倾角 $45^\circ$，$\vec{b}=(1,-p)$ 在第四象限且与 $\vec{a}$ 成 $60^\circ$ 角，故其方向角为 $-15^\circ$，于是 $p = \tan 15^\circ = 2 - \sqrt{3}$，瞬间确认 100% 正确！

- **【最终答案】**
  **$p = 2 - \sqrt{3}$**

---

#### 演習問題 3-(2)（P210）
- **【原题重现与翻译】**
  - 原题：$\vec{a} = (-1, 3),\; \vec{b} = (m, n)$（$m$ と $n$ は正の数）、$|\vec{b}| = \sqrt{5}$ のとき、$\vec{a}$ と $\vec{b}$ のなす角は $45^\circ$ である。このとき、$m, n$ の値を求めよ。
  - 中文：已知 $\vec{a} = (-1, 3),\; \vec{b} = (m, n)$（$m, n$ 为正数），$|\vec{b}| = \sqrt{5}$，且 $\vec{a}$ 与 $\vec{b}$ 的夹角为 $45^\circ$。求 $m, n$ 的值。
- **【考点定位】**
  - 向量内积定义与坐标公式联立求解未知向量。
- **【分步标准解答】**
  $|\vec{b}| = \sqrt{5}$ より $|\vec{b}|^2 = 5$ であるから、
  $$m^2 + n^2 = 5 \qquad \cdots \text{①}$$
  また、$|\vec{a}| = \sqrt{(-1)^2 + 3^2} = \sqrt{10}$、$\vec{a} \cdot \vec{b} = -m + 3n$ である。
  $\vec{a}$ と $\vec{b}$ のなす角が $45^\circ$ であるから、内積の定義 $\vec{a} \cdot \vec{b} = |\vec{a}||\vec{b}|\cos 45^\circ$ より、
  $$-m + 3n = \sqrt{10} \cdot \sqrt{5} \cdot \frac{1}{\sqrt{2}}$$
  > 💡 讲师批注：先化简右边根式：$\dfrac{\sqrt{10}\cdot\sqrt{5}}{\sqrt{2}} = \sqrt{\dfrac{50}{2}} = \sqrt{25} = 5$，非常清爽！

  $$-m + 3n = 5 \iff m = 3n - 5 \qquad \cdots \text{②}$$
  ②を①に代入すると、
  $$(3n - 5)^2 + n^2 = 5$$
  $$9n^2 - 30n + 25 + n^2 = 5$$
  $$10n^2 - 30n + 20 = 0$$
  両辺を $10$ で割って、
  $$n^2 - 3n + 2 = 0$$
  $$(n - 1)(n - 2) = 0$$
  よって $n = 1$ または $n = 2$。
  - $n = 1$ のとき、②より $m = 3 \cdot 1 - 5 = -2$（$m > 0$ に反するため不適）
  - $n = 2$ のとき、②より $m = 3 \cdot 2 - 5 = 1$（$m > 0,\; n > 0$ を満たす）

  > 💡 讲师批注：代回验算：$\vec{b} = (1, 2)$ 时 $|\vec{b}| = \sqrt{5}$，$\cos\theta = \dfrac{-1\cdot 1 + 3\cdot 2}{\sqrt{10}\cdot\sqrt{5}} = \dfrac{5}{5\sqrt{2}} = \dfrac{1}{\sqrt{2}} \implies \theta = 45^\circ$，完全正确！

- **【最终答案】**
  **$m = 1,\quad n = 2$**
