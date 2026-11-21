# 《EJU 教材全解与备课讲义》数学 008（P106–P120）

> **对应源文件**：`work_math/ocr_md/ocr_008_p106-120.md`（第五章《図形の性質》之「円に内接する四角形」「円と直線・2つの円の位置関係」「空間図形」；第六章《三角関数》之「一般角と弧度法」「三角関数」）
> **视觉核对参考图**：`work_math/ref_imgs/page_0107.jpg`, `page_0108.jpg`, `page_0110.jpg`, `page_0111.jpg`, `page_0113.jpg`, `page_0114.jpg`, `page_0115.jpg`, `page_0116.jpg`, `page_0119.jpg`, `page_0120.jpg`

---

## 一、国内高中基础知识点唤醒与 EJU 考纲差异对比

本切片横跨日本高中数学 **数学 A（図形の性質）** 的收官板块与 **数学Ⅱ（三角関数）** 的开篇核心，涵盖 **圆内接四边形、圆幂定理与两圆位置关系、空间图形（线面/面面垂直）、任意角与弧度制、同角三角函数基本关系** 五大模块。

### 1.1 圆内接四边形与四点共圆（円に内接する四角形）

- **圆周角定理之逆（円周角の定理の逆）**：若点 $P, Q$ 在直线 $AB$ 同侧，且 $\angle APB = \angle AQB$，则 $A, B, P, Q$ 四点共圆。
- **定理 12（圆内接四边形的性质）**：
  1. 对角之和为 $180^\circ$（$\angle A + \angle C = 180^\circ,\; \angle B + \angle D = 180^\circ$）；
  2. 任意一个外角等于它的内对角（例：$\angle DCE = \angle BAD$）。
- **定理 13（四边形内接于圆的判定）**：
  1. 一组对角之和为 $180^\circ$；或
  2. 一个外角等于它的内对角。

### 1.2 圆与直线、两圆位置关系（円と直線、2つの円の位置関係）

- **定理 14（切线长定理）**：从圆外一点 $P$ 向圆引两条切线 $PA, PB$（$A, B$ 为切点），则 $PA = PB$。
- **定理 15（弦切角定理 / 接弦定理）**：弦 $AB$ 与端点 $A$ 处切线 $AT$ 所成角 $\angle BAT$，等于该角内部所夹弧 $\overparen{AB}$ 对应的圆周角 $\angle ACB$。
- **定理 16 & 17（圆幂定理 / 方べきの定理）**：
  - 过点 $P$ 的两条割线（或两条相交弦）分别交圆于 $A, B$ 和 $C, D$，则：
    $$PA \cdot PB = PC \cdot PD$$
  - 从圆外一点 $P$ 引切线 $PT$（切点 $T$）和割线 $PAB$，则：
    $$PA \cdot PB = PT^2$$
- **定理 18（圆幂定理之逆）**：若线段 $AB, CD$（或其延长线）交于点 $P$ 且 $PA \cdot PB = PC \cdot PD$，则 $A, B, C, D$ 四点共圆。
- **两圆位置关系与公切线条数**（设大圆半径 $r$，小圆半径 $r'$，$r > r'$，圆心距 $d$）：

| 位置关系 | 日文标准名称 | 圆心距 $d$ 的条件 | 外公切线 | 内公切线 | 公切线总数 |
| :--- | :--- | :--- | :---: | :---: | :---: |
| 外离（互在外部） | 外部にある | $d > r + r'$ | 2 | 2 | **4 本** |
| 外切 | 外接する | $d = r + r'$ | 2 | 1 | **3 本** |
| 相交 | 2点で交わる | $r - r' < d < r + r'$ | 2 | 0 | **2 本** |
| 内切 | 内接する | $d = r - r'$ | 1 | 0 | **1 本** |
| 内含（一在另一内部） | 内部にある | $d < r - r'$ | 0 | 0 | **0 本** |

> ⚠️ **教材勘误提示（P108 / 原书 p.107）**：原教材 `[8.5]` 与 `[8.6]` 表格的第 1 列均将 `[1]` 误印为「外接する」（与第 2 列重复），正确名称应为 **「外部にある」（或「互いに外部にある」）**。另：定理 17 中「このと 2 点」漏印「円」字（应为「この円と 2 点」）；定理 18 末尾「1つ円周上にあ？」应为「1つの円周上にある」。

### 1.3 空间图形（空間図形）

- **空间两直线 $l, m$ 的三种位置关系**：① 相交（1点で交わる）；② 平行（$l \parallel m$）；③ **异面（ねじれの位置）**（不在同一平面内，既不平行也不相交）。
- **两直线的夹角与垂直**：平移至同一点 $O$ 后形成的角 $\theta$ 称为夹角；当 $\theta = 90^\circ$ 时称垂直（$l \perp m$）。日本教材中，**垂直包含异面垂直**；只有「相交且垂直」时才特称 **直交する**。
- **线面垂直判定定理（[9.3] 定理）**：直线 $h$ 垂直于平面 $\alpha$ 内两条相交直线 $l, m \implies h \perp \alpha$。
- **面面垂直判定定理（[9.5] 定理）**：若平面 $\beta$ 包含平面 $\alpha$ 的一条垂线 $h$，则 $\beta \perp \alpha$。

### 1.4 任意角、弧度制与三角函数（一般角と弧度法・三角関数）

- **任意角（一般角）**：射线 $OP$（**動径**）绕原点 $O$ 从始边 $OX$（**始線**）旋转；逆时针为正角，顺时针为负角。终边相同的角通式：$\alpha + 360^\circ \times n$（或 $\alpha + 2n\pi$，$n \in \mathbb{Z}$）。
- **弧度制（弧度法）**：$180^\circ = \pi\text{ rad}$，$1\text{ rad} = \left(\dfrac{180}{\pi}\right)^\circ \approx 57.3^\circ$。常用弧度换算：

| 度数法 | $0^\circ$ | $30^\circ$ | $45^\circ$ | $60^\circ$ | $90^\circ$ | $120^\circ$ | $135^\circ$ | $150^\circ$ | $180^\circ$ | $270^\circ$ | $360^\circ$ |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 弧度法 | $0$ | $\dfrac{\pi}{6}$ | $\dfrac{\pi}{4}$ | $\dfrac{\pi}{3}$ | $\dfrac{\pi}{2}$ | $\dfrac{2}{3}\pi$ | $\dfrac{3}{4}\pi$ | $\dfrac{5}{6}\pi$ | $\pi$ | $\dfrac{3}{2}\pi$ | $2\pi$ |

- **扇形弧长与面积**（半径 $r$，中心角 $\theta$ 弧度）：
  $$l = r\theta, \qquad S = \frac{1}{2}r^2\theta = \frac{1}{2}rl$$
  > ⚠️ **教材勘误提示（P115 / 原书 p.114）**：`[1.1]` 中「半直径 OP」为印刷错误，应为 **「半直線 OP」**；`[1.4]` 中 ②「弧の面積 $S$」应为 **「扇形の面積 $S$」**。

- **任意角三角函数的定义（单位圆 / 半径 $r$ 的圆）**：
  $$\sin\theta = \frac{y}{r}, \qquad \cos\theta = \frac{x}{r}, \qquad \tan\theta = \frac{y}{x} \;\left(\theta \neq \frac{\pi}{2} + n\pi\right)$$
  - 值域：$-1 \le \sin\theta \le 1$，$-1 \le \cos\theta \le 1$，$\tan\theta \in \mathbb{R}$。
- **同角三角函数基本关系（三角関数の相互関係）**：
  $$\text{① }\tan\theta = \frac{\sin\theta}{\cos\theta}, \qquad \text{② }\sin^2\theta + \cos^2\theta = 1, \qquad \text{③ }1 + \tan^2\theta = \frac{1}{\cos^2\theta}$$

### 1.5 国内高中 vs. 日本 EJU 考纲差异对比

| 对比维度 | 国内高中习惯 | 日本 EJU 习惯 | 备课/应试提醒 |
| :--- | :--- | :--- | :--- |
| **平面几何权重** | 高考已基本淡化圆幂定理、弦切角、四点共圆 | **数学 A 必考核心**，EJU 卷面常与三角比/向量联动 | 必须熟练掌握**方べきの定理**、**接弦定理**及四点共圆判定 |
| **圆幂定理名称** | 拆分为相交弦定理、割线定理、切割线定理 | 统称为 **方べきの定理（ほうべきのていり）** | 看到「方べき」即指 $PA\cdot PB = PC\cdot PD$ 或 $PT^2$ |
| **「垂直」与「直交」** | 统称垂直（包括异面垂直） | **垂直**含异面垂直，**直交**专指相交且垂直 | 读立体几何题干时注意区分「垂直」与「直交」 |
| **扇形面积公式** | 习惯写成 $S = \frac{1}{2}|\alpha|r^2 = \frac{1}{2}lr$ | 写作 $S = \frac{1}{2}r^2\theta = \frac{1}{2}rl$（$\theta > 0$） | 弧度制下省略单位 rad，直接写 $\theta = \frac{\pi}{3}$ |
| **三角函数符号记忆** | 口诀「一全正、二正弦、三正切、四余弦」 | 结合单位圆 $x=\cos\theta, y=\sin\theta$ 与象限图记忆 | 求解 $\sin\theta, \cos\theta$ 时**务必先看象限确定正负号** |

---

## 二、日文核心词汇与公式假名注音

### 2.1 本切片日文核心词汇

- 円に内接する四角形（えんにないせつするしかっけい / en ni naisetsu suru shikakkei） — 圆内接四边形
- 円周角の定理（えんしゅうかくのていり / enshuukaku no teiri） — 圆周角定理
- 中心角（ちゅうしんかく / chuushinkaku） — 圆心角
- 外接円（がいせつえん / gaisetsuen） — 外接圆
- 外角（がいかく / gaikaku） — 外角
- 対角（たいかく / taikaku） — 对角
- 接線（せっせん / sessen） — 切线
- 接線の長さ（せっせんのながさ / sessen no nagasa） — 切线长
- 弦（げん / gen） — 弦
- 弧（こ / ko） — 弧
- 接弦定理（せつげんていり / setsugen teiri） — 弦切角定理
- 方べきの定理（ほうべきのていり / houbeki no teiri） — 圆幂定理
- 外接する（がいせつする / gaisetsu suru） — 外切
- 内接する（ないせつする / naisetsu suru） — 内切
- 共通弦（きょうつうげん / kyoutsuugen） — 公共弦
- 共通接線（きょうつうせっせん / kyoutsuu sessen） — 公切线
- 共通外接線（きょうつうがいせっせん / kyoutsuu gaisessen） — 外公切线
- 共通内接線（きょうつうないせっせん / kyoutsuu naisessen） — 内公切线
- 空間図形（くうかんずけい / kuukan zukei） — 空间图形（立体几何）
- ねじれの位置（ねじれのいち / nejire no ichi） — 异面（位置关系）
- なす角（なすかく / nasu kaku） — 夹角
- 垂直（すいちょく / suichoku） — 垂直
- 直交する（ちょっこうする / chokkou suru） — 正交、相交垂直
- 垂線（すいせん / suisen） — 垂线
- 交線（こうせん / kousen） — 交线
- 正四面体（せいしめんたい / seishimentai） — 正四面体
- 中点連結定理（ちゅうてんれんけつていり / chuuten renketsu teiri） — 三角形中位线定理
- 三垂線の定理（さんすいせんのていり / sansuisen no teiri） — 三垂线定理
- 三角関数（さんかくかんすう / sankaku kansuu） — 三角函数
- 一般角（いっぱんかく / ippankaku） — 任意角（一般角）
- 半直線（はんちょくせん / hanchokusen） — 射线
- 始線（しせん / shisen） — 始边
- 動径（どうけい / doukei） — 终边（动径）
- 象限（しょうげん / shougen） — 象限
- 弧度法（こどほう / kodohou） — 弧度制
- 度数法（どすうほう / dosuuhou） — 角度制
- ラジアン（らじあん / rajian） — 弧度（radian）
- 扇形（おうぎがた / ougigata） — 扇形
- 単位円（たんいえん / tan'ien） — 单位圆
- 正弦（せいげん / seigen） — 正弦
- 余弦（よげん / yogen） — 余弦
- 正接（せいせつ / seisetsu） — 正切
- 相互関係（そうごかんけい / sougo kankei） — 相互关系

### 2.2 核心公式的日本课堂口语读法

1. **圆幂定理** $PA \cdot PB = PT^2$
   - 课堂读法：**ピーエー かける ピービー イコール ピーティー の にじょう**
2. **线面垂直** $h \perp \alpha$
   - 课堂读法：**エイチ すいちょく アルファ**（垂直符号 $\perp$ 读作 **すいちょく**）
3. **扇形弧长与面积** $l = r\theta,\; S = \dfrac{1}{2}r^2\theta = \dfrac{1}{2}rl$
   - 课堂读法：**エル イコール アール シータ**；**エス イコール にぶんのいち アールのにじょう シータ イコール にぶんのいち アールエル**
4. **同角三角函数关系** $\sin^2\theta + \cos^2\theta = 1$
   - 课堂读法：**サイン にじょう シータ たす コサイン にじょう シータ イコール いち**
5. **正切与余弦关系** $1 + \tan^2\theta = \dfrac{1}{\cos^2\theta}$
   - 课堂读法：**いち たす タンジェント にじょう シータ イコール コサイン にじょう シータ ぶんの いち**

---

## 三、逐题深度解析（不可跳步）

---

### 第五章 演習問題 7（円に内接する四角形，P107）

#### 演習問題 7-(1)
- **【原题重现与翻译】**
  - 原题：下の図で、四角形 $ABCD$ は円に内接している。角 $\theta$ を求めよ。
  - 中文：在下图中，四边形 $ABCD$ 内接于圆，求角 $\theta$。
- **【考点定位】**
  - 圆内接四边形的性质（对角互补、外角等于内对角）与三角形外角定理的综合运用。
- **【图解辅助（SVG 矢量图）】**

<svg viewBox="0 0 680 210" width="100%" xmlns="http://www.w3.org/2000/svg" style="background:#fafafa;border:1px solid #e0e0e0;border-radius:8px;margin:8px 0;">
  <!-- (1) -->
  <g transform="translate(10,10)">
    <text x="5" y="16" font-size="14" font-weight="bold" fill="#222">(1)</text>
    <circle cx="130" cy="100" r="62" fill="none" stroke="#333" stroke-width="1.6"/>
    <!-- A(155,43), B(73,124), C(102,155), D(170,148) approx; let's use exact circle points -->
    <!-- Center (130,100), r=62: A at -55 deg (165.6, 49.2), B at 155 deg (73.8, 126.2), C at 115 deg (103.8, 156.2), D at 65 deg (156.2, 156.2) -->
    <!-- Line AB & DC meet at E: D-C is horizontal y=156.2! Line AB: slope=(126.2-49.2)/(73.8-165.6)=77/(-91.8)=-0.8388; at y=156.2, x=73.8+(156.2-126.2)/(-0.8388)=38.0 -->
    <polygon points="165.6,49.2 73.8,126.2 103.8,156.2 156.2,156.2" fill="rgba(59,130,246,0.08)" stroke="#1d4ed8" stroke-width="1.8"/>
    <line x1="38.0" y1="156.2" x2="73.8" y2="126.2" stroke="#333" stroke-width="1.5"/>
    <line x1="38.0" y1="156.2" x2="103.8" y2="156.2" stroke="#333" stroke-width="1.5"/>
    <!-- Angles -->
    <text x="168" y="45" font-size="13" font-weight="bold" fill="#111">A</text>
    <text x="58" y="125" font-size="13" font-weight="bold" fill="#111">B</text>
    <text x="100" y="174" font-size="13" font-weight="bold" fill="#111">C</text>
    <text x="158" y="174" font-size="13" font-weight="bold" fill="#111">D</text>
    <text x="24" y="162" font-size="13" font-weight="bold" fill="#111">E</text>
    <text x="135" y="76" font-size="12" fill="#dc2626">58°</text>
    <text x="48" y="148" font-size="12" fill="#dc2626">35°</text>
    <text x="86" y="130" font-size="13" font-weight="bold" fill="#2563eb">θ</text>
  </g>

  <!-- (2) -->
  <g transform="translate(230,10)">
    <text x="5" y="16" font-size="14" font-weight="bold" fill="#222">(2)</text>
    <circle cx="95" cy="110" r="56" fill="none" stroke="#333" stroke-width="1.6"/>
    <!-- A(52,147), B(118,161), C(145,134), D(128,65) on circle approx -> let's use exact: center (95,110), r=56 -->
    <!-- A at 140 deg (52.1,146.0), B at 70 deg (114.2,162.6)? Make AB horizontal at y=155: sin(a)=45/56=0.8036 -> a=53.5deg, x=95+-33.3 => A(61.7,155), B(128.3,155) -->
    <!-- D at -55 deg (127.1, 64.1), C at 5 deg (150.8, 114.9) -->
    <!-- Line AB: y=155; Line DC: (127.1,64.1)->(150.8,114.9), slope=50.8/23.7=2.143; at y=155, x=150.8+40.1/2.143=169.5 => E(169.5,155) -->
    <!-- Line AD: (61.7,155)->(127.1,64.1), slope=-90.9/65.4=-1.390; Line BC: (128.3,155)->(150.8,114.9), slope=-40.1/22.5=-1.782 -->
    <!-- Intersection F: -1.390(x-61.7)+155 = -1.782(x-128.3)+155 -> 0.392x = 128.3*1.782 - 61.7*1.390 = 228.63-85.76=142.87 -> x=164? Wait: 142.87/0.392=364 too far. Let's pick C at -10 deg (150.1,100.3), D at -65 deg (118.7,59.2) -->
    <polygon points="61.7,155 128.3,155 147,118 118,60" fill="rgba(59,130,246,0.08)" stroke="#1d4ed8" stroke-width="1.8"/>
    <!-- Extensions to E and F -->
    <line x1="128.3" y1="155" x2="178" y2="155" stroke="#333" stroke-width="1.5"/>
    <line x1="147" y1="118" x2="178" y2="155" stroke="#333" stroke-width="1.5"/>
    <line x1="118" y1="60" x2="162" y2="25" stroke="#333" stroke-width="1.5"/>
    <line x1="147" y1="118" x2="162" y2="25" stroke="#333" stroke-width="1.5"/>
    <text x="48" y="168" font-size="13" font-weight="bold" fill="#111">A</text>
    <text x="122" y="172" font-size="13" font-weight="bold" fill="#111">B</text>
    <text x="152" y="118" font-size="13" font-weight="bold" fill="#111">C</text>
    <text x="106" y="56" font-size="13" font-weight="bold" fill="#111">D</text>
    <text x="180" y="166" font-size="13" font-weight="bold" fill="#111">E</text>
    <text x="165" y="25" font-size="13" font-weight="bold" fill="#111">F</text>
    <text x="74" y="148" font-size="13" font-weight="bold" fill="#2563eb">θ</text>
    <text x="148" y="150" font-size="12" fill="#dc2626">60°</text>
    <text x="140" y="42" font-size="12" fill="#dc2626">20°</text>
  </g>

  <!-- (3) -->
  <g transform="translate(455,10)">
    <text x="5" y="16" font-size="14" font-weight="bold" fill="#222">(3)</text>
    <circle cx="85" cy="105" r="56" fill="none" stroke="#333" stroke-width="1.6"/>
    <!-- A(85,49), B(36,133), C(95,160), D(141,105) -->
    <polygon points="85,49 36,133 95,160 141,105" fill="rgba(59,130,246,0.08)" stroke="#1d4ed8" stroke-width="1.8"/>
    <!-- Point E(198,95) -->
    <line x1="85" y1="49" x2="198" y2="95" stroke="#333" stroke-width="1.5"/>
    <line x1="95" y1="160" x2="198" y2="95" stroke="#333" stroke-width="1.5"/>
    <text x="80" y="42" font-size="13" font-weight="bold" fill="#111">A</text>
    <text x="20" y="140" font-size="13" font-weight="bold" fill="#111">B</text>
    <text x="90" y="178" font-size="13" font-weight="bold" fill="#111">C</text>
    <text x="126" y="108" font-size="13" font-weight="bold" fill="#111">D</text>
    <text x="202" y="99" font-size="13" font-weight="bold" fill="#111">E</text>
    <text x="48" y="130" font-size="13" font-weight="bold" fill="#2563eb">θ</text>
    <text x="122" y="65" font-size="12" fill="#dc2626">20°</text>
    <text x="158" y="99" font-size="12" fill="#dc2626">41°</text>
    <text x="128" y="152" font-size="12" fill="#dc2626">19°</text>
  </g>
</svg>

- **【分步标准解答】**
  - **小问 (1)**：
    四角形 $ABCD$ は円に内接しているから、頂点 $C$ における外角 $\angle ECB$ は内対角 $\angle BAD$ に等しい。
    $$\angle ECB = \angle BAD = 58^\circ$$
    > 💡 讲师批注：直接用「外角等于内对角」一步到位，比先算 $\angle BCD = 180^\circ - 58^\circ = 122^\circ$ 再求补角更高效。

    $\triangle EBC$ において、外角の性質より：
    $$\theta = \angle ABC = \angle BEC + \angle ECB = 35^\circ + 58^\circ = 93^\circ$$
    > 💡 讲师批注：$E, B, A$ 共线，因此 $\theta = \angle ABC$ 正是 $\triangle EBC$ 的外角。

  - **小问 (2)**：
    四角形 $ABCD$ は円に内接しているから、外角 $\angle ECB$ は内対角 $\angle BAD$ に等しい。
    $$\angle ECB = \angle BAD = \theta$$
    また、$\triangle ABF$ において、外角の性質より：
    $$\angle EBC = \angle BAF + \angle BFA = \theta + 20^\circ$$
    > 💡 讲师批注：把两个未知角 $\angle ECB$ 和 $\angle EBC$ 全部转化为含 $\theta$ 的表达式，集中到 $\triangle EBC$ 中列方程！

    $\triangle EBC$ の内角の和は $180^\circ$ であるから：
    $$\angle EBC + \angle ECB + \angle BEC = 180^\circ$$
    $$(\theta + 20^\circ) + \theta + 60^\circ = 180^\circ$$
    $$2\theta = 100^\circ \implies \theta = 50^\circ$$
    > 💡 讲师批注：验算：$\theta=50^\circ \Rightarrow \angle ADE = 180^\circ - 50^\circ - 60^\circ = 70^\circ \Rightarrow \angle ABC = 110^\circ \Rightarrow \angle F = 180^\circ - 50^\circ - 110^\circ = 20^\circ$，完全吻合！

  - **小问 (3)**：
    **解法一（四边形 $ABCE$ 内角和，最简）**：
    四角形 $ABCD$ は円に内接しているから、対角の和は $180^\circ$ である。
    $$\angle BAD + \angle BCD = 180^\circ$$
    四角形 $ABCE$ の内角の和は $360^\circ$ であるから：
    $$\angle ABC + (\angle BAD + 20^\circ) + \angle AEC + (\angle BCD + 19^\circ) = 360^\circ$$
    $$\theta + (\angle BAD + \angle BCD) + 20^\circ + 41^\circ + 19^\circ = 360^\circ$$
    $$\theta + 180^\circ + 80^\circ = 360^\circ \implies \theta = 100^\circ$$
    > 💡 讲师批注：**解法二（延长辅助线）**：延长 $AD$ 交 $CE$ 于 $F$，由外角定理得 $\angle ADC = 20^\circ + 41^\circ + 19^\circ = 80^\circ$，再由圆内接四边形对角互补得 $\theta = 180^\circ - 80^\circ = 100^\circ$。两种方法均得 $100^\circ$！

- **【最终答案】**
  **(1) $\theta = 93^\circ$，(2) $\theta = 50^\circ$，(3) $\theta = 100^\circ$**

---

#### 演習問題 7-(2)
- **【原题重现与翻译】**
  - 原题：右の図のように、鋭角三角形 $ABC$ の頂点 $A$ から $BC$ に下ろした垂線を $AD$ とし、$D$ から $AB, AC$ に下ろした垂線をそれぞれ $DE, DF$ とするとき、4 点 $B, C, F, E$ は 1 つの円周上にあることを証明せよ。
  - 中文：如右图所示，从锐角三角形 $ABC$ 的顶点 $A$ 向 $BC$ 作垂线 $AD$，从 $D$ 向 $AB, AC$ 分别作垂线 $DE, DF$。求证：$B, C, F, E$ 四点共圆。
- **【考点定位】**
  - 圆内接四边形的判定定理（定理 13）与圆周角定理的联动证明。
- **【图解辅助（SVG 矢量图）】**

<svg viewBox="0 0 320 220" width="52%" xmlns="http://www.w3.org/2000/svg" style="background:#fafafa;border:1px solid #e0e0e0;border-radius:8px;margin:8px 0;">
  <!-- A(180,25), B(45,180), C(275,180), D(180,180) -->
  <!-- AB: from (180,25) to (45,180), vec=(-135,155), len^2=18225+24025=42250. D(180,180): AD=(0,155), proj on AB: (0*-135+155*155)/42250 = 24025/42250 = 0.5686 -> E = (180-76.8, 25+88.1) = (103.2, 113.1) -->
  <!-- AC: from (180,25) to (275,180), vec=(95,155), len^2=9025+24025=33050. proj: 24025/33050 = 0.7269 -> F = (180+69.1, 25+112.7) = (249.1, 137.7) -->
  <!-- Auxiliary circle on AD: center (180, 102.5), r=77.5 -->
  <circle cx="180" cy="102.5" r="77.5" fill="none" stroke="#93c5fd" stroke-width="1.3" stroke-dasharray="5,4"/>
  <!-- Triangle ABC -->
  <polygon points="180,25 45,180 275,180" fill="none" stroke="#1e293b" stroke-width="2"/>
  <!-- AD, DE, DF, EF -->
  <line x1="180" y1="25" x2="180" y2="180" stroke="#1e293b" stroke-width="1.6"/>
  <line x1="180" y1="180" x2="103.2" y2="113.1" stroke="#2563eb" stroke-width="1.6"/>
  <line x1="180" y1="180" x2="249.1" y2="137.7" stroke="#2563eb" stroke-width="1.6"/>
  <line x1="103.2" y1="113.1" x2="249.1" y2="137.7" stroke="#dc2626" stroke-width="1.8"/>
  <!-- Right angle at D -->
  <polyline points="170,180 170,170 180,170" fill="none" stroke="#1e293b" stroke-width="1.2"/>
  <!-- Labels -->
  <text x="176" y="18" font-size="14" font-weight="bold" fill="#111">A</text>
  <text x="30" y="188" font-size="14" font-weight="bold" fill="#111">B</text>
  <text x="280" y="188" font-size="14" font-weight="bold" fill="#111">C</text>
  <text x="175" y="198" font-size="14" font-weight="bold" fill="#111">D</text>
  <text x="86" y="110" font-size="14" font-weight="bold" fill="#2563eb">E</text>
  <text x="255" y="136" font-size="14" font-weight="bold" fill="#2563eb">F</text>
  <text x="188" y="88" font-size="11" fill="#3b82f6">直径 AD の補助円</text>
</svg>

- **【分步标准解答】**
  【証明】
  仮定より $\angle AED = 90^\circ,\; \angle AFD = 90^\circ$ であるから：
  $$\angle AED + \angle AFD = 180^\circ$$
  よって、四角形 $AEDF$ は円（線分 $AD$ を直径とする円）に内接する。
  > 💡 讲师批注：这是解「双垂足四点共圆」问题的黄金第一步：先证 $A, E, D, F$ 共圆，把角 $\angle AEF$ 转移到 $\angle ADF$！

  したがって、弧 $DF$ に対する円周角は等しいから：
  $$\angle AEF = \angle ADF \qquad \cdots \text{①}$$
  一方、直角三角形 $ADC$ と直角三角形 $DFC$ において、$\angle ADC = \angle DFC = 90^\circ$ であるから：
  $$\angle ADF = 90^\circ - \angle CDF, \qquad \angle FCB = 90^\circ - \angle CDF$$
  よって：
  $$\angle ADF = \angle FCB \qquad \cdots \text{②}$$
  > 💡 讲师批注：同角（$\angle CDF$）的余角相等，直接得到 $\angle ADF = \angle C$。

  ①、② から：
  $$\angle AEF = \angle FCB$$
  四角形 $BCFE$ において、頂点 $E$ における外角 $\angle AEF$ が内対角 $\angle FCB$ に等しいから、4 点 $B, C, F, E$ は 1 つの円周上にある。（証明終）

- **【最终答案】**
  **如上证明成立（利用 $A, E, D, F$ 共圆转移圆周角，证得外角 $\angle AEF = \angle FCB$）。**

---

### 第五章 演習問題 8（円と直線、2つの円の位置関係，P110–P111）

#### 演習問題 8-(1)
- **【原题重现与翻译】**
  - 原题：線分 $AB$ を直径とする半径 $1$ の円 $O$ があり、右の図のように線分 $AB$ の延長上の点 $P$ からこの円に接線 $PT$ を引く。$\angle BAT = 30^\circ$ のとき
    - [1] $PB = BT = 1$ であることを示せ。
    - [2] 方べきの定理を利用して、接線 $PT$ の長さを求めよ。
  - 中文：已知以线段 $AB$ 为直径、半径为 $1$ 的圆 $O$，如图所示从线段 $AB$ 延长线上的点 $P$ 向圆引切线 $PT$。当 $\angle BAT = 30^\circ$ 时，
    - [1] 证明 $PB = BT = 1$；
    - [2] 利用圆幂定理，求切线 $PT$ 的长度。
- **【考点定位】**
  - 半圆所对圆周角为直角、弦切角定理（定理 15）、圆幂定理（定理 17）。
- **【图解辅助（SVG 矢量图）】**

<svg viewBox="0 0 360 190" width="56%" xmlns="http://www.w3.org/2000/svg" style="background:#fafafa;border:1px solid #e0e0e0;border-radius:8px;margin:8px 0;">
  <!-- O(110,105), r=60 -> A(50,105), B(170,105), P(230,105) -->
  <!-- angle BAT = 30 deg -> angle BOT = 60 deg -> T = (110+60*cos60, 105-60*sin60) = (140, 53.04) -->
  <circle cx="110" cy="105" r="60" fill="none" stroke="#1e293b" stroke-width="1.8"/>
  <line x1="50" y1="105" x2="230" y2="105" stroke="#1e293b" stroke-width="1.8"/>
  <line x1="50" y1="105" x2="140" y2="53.04" stroke="#2563eb" stroke-width="1.6"/>
  <line x1="170" y1="105" x2="140" y2="53.04" stroke="#2563eb" stroke-width="1.6"/>
  <line x1="230" y1="105" x2="140" y2="53.04" stroke="#dc2626" stroke-width="1.8"/>
  <!-- Center dot -->
  <circle cx="110" cy="105" r="2.5" fill="#1e293b"/>
  <!-- Labels -->
  <text x="35" y="110" font-size="14" font-weight="bold" fill="#111">A</text>
  <text x="105" y="123" font-size="13" font-weight="bold" fill="#111">O</text>
  <text x="166" y="123" font-size="14" font-weight="bold" fill="#111">B</text>
  <text x="234" y="110" font-size="14" font-weight="bold" fill="#111">P</text>
  <text x="136" y="45" font-size="14" font-weight="bold" fill="#dc2626">T</text>
  <text x="72" y="100" font-size="12" fill="#2563eb">30°</text>
  <text x="195" y="100" font-size="12" fill="#dc2626">30°</text>
  <text x="148" y="88" font-size="12" fill="#2563eb">60°</text>
</svg>

- **【分步标准解答】**
  - **[1] の証明**：
    線分 $AB$ は円 $O$ の直径であるから、$AB = 2$ であり、円周角の定理より $\angle ATB = 90^\circ$ である。
    直角三角形 $ATB$ において、$\angle BAT = 30^\circ$ であるから：
    $$BT = AB \sin 30^\circ = 2 \times \frac{1}{2} = 1, \qquad \angle ABT = 90^\circ - 30^\circ = 60^\circ$$
    > 💡 讲师批注：直接利用 $30^\circ\text{–}60^\circ\text{–}90^\circ$ 直角三角形边长比 $1:2:\sqrt{3}$ 亦得 $BT = 1$。

    また、直線 $PT$ は円 $O$ の接線であるから、接弦定理より：
    $$\angle PTB = \angle BAT = 30^\circ$$
    $\triangle PTB$ において、外角の性質より $\angle ABT = \angle PTB + \angle TPB$ であるから：
    $$\angle TPB = \angle ABT - \angle PTB = 60^\circ - 30^\circ = 30^\circ$$
    よって $\angle TPB = \angle PTB = 30^\circ$ となり、$\triangle PBT$ は二等辺三角形であるから：
    $$PB = BT = 1$$
    > 💡 讲师批注：弦切角定理 + 外角定理，完美证明等腰三角形。

  - **[2] の解答**：
    [1] より $PB = 1$、直径 $AB = 2$ であるから：
    $$PA = PB + AB = 1 + 2 = 3$$
    方べきの定理（定理 17）より：
    $$PT^2 = PB \cdot PA = 1 \times 3 = 3$$
    $PT > 0$ であるから：
    $$PT = \sqrt{3}$$
    > 💡 讲师批注：验算：连结 $OT$，在 $\mathrm{Rt}\triangle OTP$ 中 $OT=1, OP=2 \implies PT = \sqrt{2^2-1^2} = \sqrt{3}$，完全一致！

- **【最终答案】**
  **[1] 証明完畢；[2] $PT = \sqrt{3}$**

---

#### 演習問題 8-(2)
> ⚠️ **教材勘误提示（P110 / 原书 p.109）**：原教材题干在「交点を $E$」之后漏印了一整句，印成「辺 $AB, CD$ の延長の交点を $E, F$ からこの円に引いた…」，导致点 $F$ 未定义。根据日本经典原题，完整题干应补全为：**「辺 $AB, CD$ の延長の交点を $E$、辺 $AD, BC$ の延長の交点を $F$ とし、2 点 $E, F$ からこの円に引いた…」**。以下按补全后的正确题干进行严格证明。

- **【原题重现与翻译】**
  - 原题（补全勘误）：円に内接する四角形 $ABCD$ の辺 $AB, CD$ の延長の交点を $E$、**辺 $AD, BC$ の延長の交点を $F$ とし、2 点 $E, F$** からこの円に引いた接線の接点をそれぞれ $S, T$ とするとき、等式 $ES^2 + FT^2 = EF^2$ が成り立つことを証明せよ。
  - 中文：圆内接四边形 $ABCD$ 的边 $AB, CD$ 的延长线交于点 $E$，边 $AD, BC$ 的延长线交于点 $F$。从两点 $E, F$ 向该圆引切线，切点分别为 $S, T$。求证：$ES^2 + FT^2 = EF^2$。
- **【考点定位】**
  - 圆幂定理（定理 16、17）、辅助圆构造与四点共圆判定（定理 13）。**（竞赛/EJU 压轴级经典几何证明题）**
- **【图解辅助（SVG 矢量图）】**

<svg viewBox="0 0 420 260" width="66%" xmlns="http://www.w3.org/2000/svg" style="background:#fafafa;border:1px solid #e0e0e0;border-radius:8px;margin:8px 0;">
  <!-- Using verified coordinates scaled & flipped:
       Orig: O(0,0), r=1; A(-1,0), B(0,-1), C(0.6,-0.8), D(0,1), E(1,-2), F(-3,-2), G(0,-2).
       Map (x,y) -> (260 + 55*x, 110 - 55*y):
       O(260,110), r=55
       A(205,110), B(260,165), C(293,154), D(260,55), E(315,220), F(95,220), G(260,220)
       Aux circle CDFG: center(-1.5, -0.5) -> (177.5, 137.5), R=sqrt(4.5)*55 = 116.67 -->
  <!-- Auxiliary circle CDFG -->
  <circle cx="177.5" cy="137.5" r="116.67" fill="none" stroke="#10b981" stroke-width="1.4" stroke-dasharray="5,4"/>
  <!-- Main circle O -->
  <circle cx="260" cy="110" r="55" fill="none" stroke="#1e293b" stroke-width="2"/>
  <!-- Lines -->
  <!-- F-A-D -->
  <line x1="95" y1="220" x2="260" y2="55" stroke="#475569" stroke-width="1.5"/>
  <!-- F-B-C -->
  <line x1="95" y1="220" x2="293" y2="154" stroke="#475569" stroke-width="1.5"/>
  <!-- A-B-E -->
  <line x1="205" y1="110" x2="315" y2="220" stroke="#475569" stroke-width="1.5"/>
  <!-- D-C-E -->
  <line x1="260" y1="55" x2="315" y2="220" stroke="#475569" stroke-width="1.5"/>
  <!-- E-G-F -->
  <line x1="95" y1="220" x2="315" y2="220" stroke="#dc2626" stroke-width="2"/>
  <!-- CG & BG -->
  <line x1="293" y1="154" x2="260" y2="220" stroke="#10b981" stroke-width="1.5" stroke-dasharray="3,2"/>
  <!-- Points -->
  <circle cx="205" cy="110" r="3" fill="#1e293b"/>
  <circle cx="260" cy="165" r="3" fill="#1e293b"/>
  <circle cx="293" cy="154" r="3" fill="#1e293b"/>
  <circle cx="260" cy="55" r="3" fill="#1e293b"/>
  <circle cx="315" cy="220" r="3.5" fill="#dc2626"/>
  <circle cx="95" cy="220" r="3.5" fill="#dc2626"/>
  <circle cx="260" cy="220" r="3.5" fill="#10b981"/>
  <!-- Labels -->
  <text x="190" y="108" font-size="13" font-weight="bold" fill="#111">A</text>
  <text x="247" y="182" font-size="13" font-weight="bold" fill="#111">B</text>
  <text x="301" y="154" font-size="13" font-weight="bold" fill="#111">C</text>
  <text x="262" y="47" font-size="13" font-weight="bold" fill="#111">D</text>
  <text x="322" y="226" font-size="14" font-weight="bold" fill="#dc2626">E</text>
  <text x="80" y="226" font-size="14" font-weight="bold" fill="#dc2626">F</text>
  <text x="255" y="238" font-size="14" font-weight="bold" fill="#10b981">G</text>
  <text x="108" y="62" font-size="11" fill="#10b981">△CDF の外接円</text>
</svg>

- **【分步标准解答】**
  【証明】
  線分 $EF$ 上に、$\triangle CDF$ の外接円との交点 $G$ をとる。（ただし、一般性を失わず、辺 $AB, DC$ の延長が $B, C$ 側で交わって $E$、辺 $DA, CB$ の延長が $A, B$ 側（または $D, C$ 側）で交わって $F$ となる配置で考える。）
  > 💡 讲师批注：本题核心思路是**把 $EF^2$ 拆成 $EF \cdot EG + EF \cdot FG$**！为此必须在线段 $EF$ 上构造点 $G$，使 $ES^2 = EF \cdot EG$ 且 $FT^2 = EF \cdot FG$。

  **ステップ 1：$ES^2 = EG \cdot EF$ を示す**
  4 点 $C, D, F, G$ は同一円周上にあるから、方べきの定理より：
  $$EG \cdot EF = EC \cdot ED$$
  一方、もとの円に対しても方べきの定理より：
  $$ES^2 = EC \cdot ED$$
  したがって：
  $$ES^2 = EG \cdot EF \qquad \cdots \text{①}$$

  **ステップ 2：4 点 $B, C, G, E$ が同一円周上にあることを示し、$FT^2 = FG \cdot FE$ を導く**
  四角形 $CDFG$ は円に内接しているから、外角は内対角に等しく：
  $$\angle EGC = \angle CDF$$
  また、四角形 $ABCD$ も円に内接しているから、対角の和は $180^\circ$（外角は内対角に等しい）：
  $$\angle CDF = \angle ABC = 180^\circ - \angle EBC$$
  よって：
  $$\angle EGC + \angle EBC = \angle CDF + (180^\circ - \angle CDF) = 180^\circ$$
  > 💡 讲师批注：关键一步！通过 $\angle CDF$ 作为桥梁，证明四边形 $EBGC$ 的一组对角互补，从而推出 $B, C, G, E$ 四点共圆！

  したがって、4 点 $B, C, G, E$ は 1 つの円周上にある。この円に対して方べきの定理を用いると：
  $$FG \cdot FE = FC \cdot FB$$
  一方、もとの円に対しても方べきの定理より：
  $$FT^2 = FC \cdot FB$$
  したがって：
  $$FT^2 = FG \cdot FE \qquad \cdots \text{②}$$

  **ステップ 3：① と ② を辺々加える**
  $$ES^2 + FT^2 = EG \cdot EF + FG \cdot EF = (EG + FG) \cdot EF = EF \cdot EF = EF^2$$
  よって、等式 $ES^2 + FT^2 = EF^2$ が成り立つ。（証明終）
  > 💡 讲师批注：数值验算（单位圆 $A(-1,0), B(0,-1), C(\frac{3}{5},-\frac{4}{5}), D(0,1)$）：$E(1,-2), F(-3,-2)$，$ES^2 = 5-1=4$，$FT^2 = 13-1=12$，$EF^2 = 4^2 = 16 = 4+12$，交点 $G(0,-2)$ 恰好落在线段 $EF$ 上！

- **【最终答案】**
  **如上证明成立（构造 $\triangle CDF$ 外接圆交 $EF$ 于 $G$，两次使用圆幂定理合并得证）。**

---

#### 演習問題 8-(3)
- **【原题重现与翻译】**
  - 原题：右の図のように、半径 $5$ の円 $O$ と半径 $12$ の円 $O'$ があり、$OO' = 25$ である。この時、共通外接線 $AB$ の長さと共通内接線 $CD$ の長さを求めよ。
  - 中文：如右图所示，有半径为 $5$ 的圆 $O$ 和半径为 $12$ 的圆 $O'$，圆心距 $OO' = 25$。求外公切线 $AB$ 的长度和内公切线 $CD$ 的长度。
  > ⚠️ **教材勘误提示（P111 / 原书 p.110）**：原题漏印了圆名「$O$」（印作「半径 5 の円と半径 12 の円 $O'$」），且「共通接線 $CD$」结合图形应为「共通**内**接線 $CD$」。
- **【考点定位】**
  - 两圆外公切线长公式 $\sqrt{d^2 - (r-r')^2}$ 与内公切线长公式 $\sqrt{d^2 - (r+r')^2}$ 的几何推导（平移构造直角三角形）。
- **【图解辅助（SVG 矢量图）】**

<svg viewBox="0 0 420 220" width="66%" xmlns="http://www.w3.org/2000/svg" style="background:#fafafa;border:1px solid #e0e0e0;border-radius:8px;margin:8px 0;">
  <!-- O(80,115), r1=25 (rep 5); O'(205,115), r2=60 (rep 12); d=125 (rep 25) -->
  <!-- Wait, let's scale by 6: O(85,115), r1=30; O'(235,115), r2=72; d=150 -->
  <!-- External tangent AB: sin(alpha)=(72-30)/150 = 42/150 = 0.28, cos=0.96.
       A = (85 - 30*0.28, 115 - 30*0.96) = (76.6, 86.2)
       B = (235 - 72*0.28, 115 - 72*0.96) = (214.8, 45.9)
       H on O'B: (235 - 42*0.28, 115 - 42*0.96) = (223.2, 74.7) -->
  <!-- Internal tangent CD: sin(beta)=(72+30)/150 = 102/150 = 0.68, cos=0.7332.
       C on circle O (upper-right): (85 + 30*0.68, 115 - 30*0.7332) = (105.4, 93.0)
       D on circle O' (lower-left): (235 - 72*0.68, 115 + 72*0.7332) = (186.0, 167.8) -->
  <circle cx="85" cy="115" r="30" fill="none" stroke="#1e293b" stroke-width="1.8"/>
  <circle cx="235" cy="115" r="72" fill="none" stroke="#1e293b" stroke-width="1.8"/>
  <!-- OO' -->
  <line x1="85" y1="115" x2="235" y2="115" stroke="#64748b" stroke-width="1.4" stroke-dasharray="4,3"/>
  <!-- External tangent AB -->
  <line x1="50" y1="93.9" x2="255" y2="34.2" stroke="#2563eb" stroke-width="1.8"/>
  <!-- OH parallel to AB -->
  <line x1="85" y1="115" x2="223.2" y2="74.7" stroke="#2563eb" stroke-width="1.3" stroke-dasharray="4,3"/>
  <!-- Radii OA, O'B -->
  <line x1="85" y1="115" x2="76.6" y2="86.2" stroke="#2563eb" stroke-width="1.3"/>
  <line x1="235" y1="115" x2="214.8" y2="45.9" stroke="#2563eb" stroke-width="1.3"/>
  <!-- Internal tangent CD -->
  <line x1="90" y1="78.8" x2="205" y2="185.4" stroke="#dc2626" stroke-width="1.8"/>
  <!-- Radii OC, O'D -->
  <line x1="85" y1="115" x2="105.4" y2="93.0" stroke="#dc2626" stroke-width="1.3"/>
  <line x1="235" y1="115" x2="186.0" y2="167.8" stroke="#dc2626" stroke-width="1.3"/>
  <!-- Dots & Labels -->
  <circle cx="85" cy="115" r="2.5" fill="#1e293b"/>
  <circle cx="235" cy="115" r="2.5" fill="#1e293b"/>
  <text x="72" y="130" font-size="13" font-weight="bold" fill="#111">O</text>
  <text x="240" y="128" font-size="13" font-weight="bold" fill="#111">O'</text>
  <text x="64" y="80" font-size="13" font-weight="bold" fill="#2563eb">A</text>
  <text x="208" y="38" font-size="13" font-weight="bold" fill="#2563eb">B</text>
  <text x="228" y="78" font-size="12" fill="#2563eb">H</text>
  <text x="108" y="90" font-size="13" font-weight="bold" fill="#dc2626">C</text>
  <text x="172" y="182" font-size="13" font-weight="bold" fill="#dc2626">D</text>
  <text x="148" y="111" font-size="12" fill="#475569">25</text>
  <text x="68" y="106" font-size="11" fill="#2563eb">5</text>
  <text x="230" y="66" font-size="11" fill="#2563eb">12</text>
  <!-- Legend -->
  <text x="320" y="75" font-size="12" fill="#2563eb">外公切线 AB=24</text>
  <text x="320" y="100" font-size="12" fill="#dc2626">内公切线 CD=4√21</text>
</svg>

- **【分步标准解答】**
  - **共通外接線 $AB$ の長さ**：
    点 $O$ から線分 $O'B$ に垂線 $OH$ を下ろす。$OA \perp AB,\; O'B \perp AB$ より、四角形 $OABH$ は長方形となるから：
    $$OH = AB, \qquad BH = OA = 5$$
    よって：
    $$O'H = O'B - BH = 12 - 5 = 7$$
    直角三角形 $OHO'$ において、三平方の定理（勾股定理）より：
    $$AB = OH = \sqrt{OO'^2 - O'H^2} = \sqrt{25^2 - 7^2} = \sqrt{625 - 49} = \sqrt{576} = 24$$
    > 💡 讲师批注：熟记经典勾股数组 $(7, 24, 25)$，可以瞬间秒出答案！

  - **共通内接線 $CD$ の長さ**：
    点 $O$ から直線 $O'D$ に垂線 $OK$ を下ろす（$K$ は線分 $O'D$ の延長上）。$OC \perp CD,\; O'D \perp CD$ より、四角形 $OCDK$ は長方形となるから：
    $$OK = CD, \qquad DK = OC = 5$$
    よって：
    $$O'K = O'D + DK = 12 + 5 = 17$$
    直角三角形 $OKO'$ において、三平方の定理より：
    $$CD = OK = \sqrt{OO'^2 - O'K^2} = \sqrt{25^2 - 17^2} = \sqrt{(25 - 17)(25 + 17)} = \sqrt{8 \times 42} = \sqrt{336} = 4\sqrt{21}$$
    > 💡 讲师批注：计算 $\sqrt{25^2 - 17^2}$ 时优先用平方差 $(25-17)(25+17) = 8 \times 42 = 16 \times 21$，比硬算 $625 - 289$ 快且不易出错！

- **【最终答案】**
  **$AB = 24,\quad CD = 4\sqrt{21}$**

---

#### 演習問題 8-(4)
- **【原题重现与翻译】**
  - 原题：点 $A$ で外接する 2 つの円 $O, O'$ の共通接線の接点をそれぞれ $B, C$ とする。
    - [1] $\triangle ABC$ は直角三角形であることを示せ。
    - [2] 円 $O$ の直径 $BD$ を引くとき、3 点 $D, A, C$ は 1 つの直線上にあることを証明せよ。
  - 中文：两圆 $O, O'$ 外切于点 $A$，它们的外公切线的切点分别为 $B, C$。
    - [1] 证明 $\triangle ABC$ 是直角三角形；
    - [2] 作圆 $O$ 的直径 $BD$，证明 $D, A, C$ 三点共线。
- **【考点定位】**
  - 切线长定理（定理 14）、内公切线辅助线构造、半圆所对圆周角为直角。
- **【图解辅助（SVG 矢量图）】**

<svg viewBox="0 0 380 200" width="60%" xmlns="http://www.w3.org/2000/svg" style="background:#fafafa;border:1px solid #e0e0e0;border-radius:8px;margin:8px 0;">
  <!-- O(110,115), r1=55; O'(205,115), r2=40; d=95 -> A(165,115) -->
  <!-- External tangent BC: sin(a)=(55-40)/95 = 15/95 = 0.1579, cos(a)=0.9875
       B = (110 + 55*0.1579, 115 - 55*0.9875) = (118.7, 60.7)
       C = (205 + 40*0.1579, 115 - 40*0.9875) = (211.3, 75.5)
       D = opposite of B on circle O = (101.3, 169.3)
       Inner common tangent at A: x=165; meets BC at M: slope=(75.5-60.7)/(211.3-118.7)=14.8/92.6=0.1598
       M = (165, 60.7 + 0.1598*(165-118.7)) = (165, 68.1) -->
  <circle cx="110" cy="115" r="55" fill="none" stroke="#1e293b" stroke-width="1.8"/>
  <circle cx="205" cy="115" r="40" fill="none" stroke="#1e293b" stroke-width="1.8"/>
  <!-- External tangent BC -->
  <line x1="75" y1="53.7" x2="255" y2="82.5" stroke="#1e293b" stroke-width="1.8"/>
  <!-- Inner common tangent MA -->
  <line x1="165" y1="52" x2="165" y2="155" stroke="#10b981" stroke-width="1.5" stroke-dasharray="4,3"/>
  <!-- Diameter BD -->
  <line x1="118.7" y1="60.7" x2="101.3" y2="169.3" stroke="#2563eb" stroke-width="1.6"/>
  <!-- Triangle ABC & collinear D-A-C -->
  <line x1="118.7" y1="60.7" x2="165" y2="115" stroke="#dc2626" stroke-width="1.8"/>
  <line x1="101.3" y1="169.3" x2="211.3" y2="75.5" stroke="#dc2626" stroke-width="1.8"/>
  <!-- Dots -->
  <circle cx="110" cy="115" r="2.2" fill="#1e293b"/>
  <circle cx="205" cy="115" r="2.2" fill="#1e293b"/>
  <circle cx="165" cy="115" r="3" fill="#dc2626"/>
  <circle cx="165" cy="68.1" r="3" fill="#10b981"/>
  <!-- Labels -->
  <text x="95" y="120" font-size="12" font-weight="bold" fill="#111">O</text>
  <text x="208" y="120" font-size="12" font-weight="bold" fill="#111">O'</text>
  <text x="115" y="52" font-size="13" font-weight="bold" fill="#111">B</text>
  <text x="212" y="68" font-size="13" font-weight="bold" fill="#111">C</text>
  <text x="171" y="122" font-size="13" font-weight="bold" fill="#dc2626">A</text>
  <text x="92" y="185" font-size="13" font-weight="bold" fill="#2563eb">D</text>
  <text x="169" y="64" font-size="13" font-weight="bold" fill="#10b981">M</text>
  <text x="265" y="110" font-size="11" fill="#10b981">共通内接線 AM</text>
  <text x="265" y="128" font-size="11" fill="#10b981">MA = MB = MC</text>
</svg>

- **【分步标准解答】**
  - **[1] の証明**：
    点 $A$ における 2 つの円 $O, O'$ の共通内接線を引き、共通外接線 $BC$ との交点を $M$ とする。
    接線の長さの性質（定理 14）より、円 $O$ について $MB = MA$、円 $O'$ について $MC = MA$ であるから：
    $$MA = MB = MC$$
    > 💡 讲师批注：两圆外切求角度/共线问题，**「过切点作内公切线」**是最经典、最万能的辅助线！

    よって、$\triangle MAB$ と $\triangle MAC$ はともに二等辺三角形となるから：
    $$\angle MAB = \angle MBA, \qquad \angle MAC = \angle MCA$$
    $\triangle ABC$ の内角の和は $180^\circ$ であるから：
    $$\angle MBA + \angle MCA + (\angle MAB + \angle MAC) = 180^\circ$$
    $$2(\angle MAB + \angle MAC) = 180^\circ \implies \angle BAC = \angle MAB + \angle MAC = 90^\circ$$
    したがって、$\triangle ABC$ は $\angle BAC = 90^\circ$ の直角三角形である。

  - **[2] の証明**：
    線分 $BD$ は円 $O$ の直径であるから、円周角の定理より：
    $$\angle BAD = 90^\circ$$
    また、[1] より：
    $$\angle BAC = 90^\circ$$
    ここで、2 点 $D, C$ は直線 $AB$ に関して反対側にあるから：
    $$\angle DAC = \angle DAB + \angle BAC = 90^\circ + 90^\circ = 180^\circ$$
    したがって、3 点 $D, A, C$ は 1 つの直線上にある。（証明終）

- **【最终答案】**
  **[1]、[2] 均如上证明成立。**

---

### 第五章 演習問題 9（空間図形，P113–P114）

#### 演習問題 9-(1)
- **【原题重现与翻译】**
  - 原题：正四面体 $ABCD$ について、次のことを証明せよ。
    - [1] 辺 $AB$ の中点を $M$ とする。① 辺 $AB$ は平面 $CDM$ に垂直である。② 辺 $AB$ と辺 $CD$ は垂直である。
    - [2] 辺 $BC, AC, AD, BD$ の中点をそれぞれ $P, Q, R, S$ とするとき、四角形 $PQRS$ は正方形である。
  - 中文：关于正四面体 $ABCD$，求证：
    - [1] 设边 $AB$ 的中点为 $M$。① 边 $AB$ 垂直于平面 $CDM$；② 边 $AB$ 与边 $CD$ 垂直。
    - [2] 设边 $BC, AC, AD, BD$ 的中点分别为 $P, Q, R, S$，证明四边形 $PQRS$ 是正方形。
- **【考点定位】**
  - 线面垂直判定定理（[9.3] 定理）、正四面体对棱垂直性质、三角形中位线定理（中点連結定理）。
- **【图解辅助（SVG 矢量图）】**

<svg viewBox="0 0 380 230" width="60%" xmlns="http://www.w3.org/2000/svg" style="background:#fafafa;border:1px solid #e0e0e0;border-radius:8px;margin:8px 0;">
  <!-- A(180,25), B(65,185), C(290,195), D(240,120) -->
  <!-- Midpoints:
       M(AB) = (122.5, 105)
       P(BC) = (177.5, 190)
       Q(AC) = (235, 110)
       R(AD) = (210, 72.5)
       S(BD) = (152.5, 152.5) -->
  <!-- Back edges (dashed) -->
  <line x1="65" y1="185" x2="240" y2="120" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="5,4"/>
  <!-- Plane CDM highlight -->
  <polygon points="290,195 240,120 122.5,105" fill="rgba(59,130,246,0.10)" stroke="#3b82f6" stroke-width="1.3" stroke-dasharray="4,3"/>
  <!-- Square PQRS -->
  <polygon points="177.5,190 235,110 210,72.5 152.5,152.5" fill="rgba(16,185,129,0.18)" stroke="#10b981" stroke-width="2"/>
  <!-- Front edges of tetrahedron -->
  <line x1="180" y1="25" x2="65" y2="185" stroke="#1e293b" stroke-width="2"/>
  <line x1="180" y1="25" x2="290" y2="195" stroke="#1e293b" stroke-width="2"/>
  <line x1="180" y1="25" x2="240" y2="120" stroke="#1e293b" stroke-width="1.8"/>
  <line x1="65" y1="185" x2="290" y2="195" stroke="#1e293b" stroke-width="2"/>
  <line x1="290" y1="195" x2="240" y2="120" stroke="#1e293b" stroke-width="1.8"/>
  <!-- Points -->
  <circle cx="122.5" cy="105" r="3" fill="#2563eb"/>
  <circle cx="177.5" cy="190" r="3" fill="#10b981"/>
  <circle cx="235" cy="110" r="3" fill="#10b981"/>
  <circle cx="210" cy="72.5" r="3" fill="#10b981"/>
  <circle cx="152.5" cy="152.5" r="3" fill="#10b981"/>
  <!-- Labels -->
  <text x="176" y="18" font-size="14" font-weight="bold" fill="#111">A</text>
  <text x="48" y="192" font-size="14" font-weight="bold" fill="#111">B</text>
  <text x="296" y="202" font-size="14" font-weight="bold" fill="#111">C</text>
  <text x="248" y="122" font-size="14" font-weight="bold" fill="#111">D</text>
  <text x="104" y="103" font-size="13" font-weight="bold" fill="#2563eb">M</text>
  <text x="172" y="210" font-size="13" font-weight="bold" fill="#059669">P</text>
  <text x="242" y="106" font-size="13" font-weight="bold" fill="#059669">Q</text>
  <text x="216" y="68" font-size="13" font-weight="bold" fill="#059669">R</text>
  <text x="136" y="158" font-size="13" font-weight="bold" fill="#059669">S</text>
</svg>

- **【分步标准解答】**
  - **[1] ① の証明**：
    正四面体 $ABCD$ の各面はすべて正三角形である。
    正三角形 $ABC$ において、$M$ は辺 $AB$ の中点であるから：$AB \perp CM$。
    正三角形 $ABD$ において、$M$ は辺 $AB$ の中点であるから：$AB \perp DM$。
    辺 $AB$ は、平面 $CDM$ 上の交わる 2 直線 $CM, DM$ に垂直であるから、直線と平面の垂直の定理より：
    $$AB \perp \text{平面 } CDM$$
    > 💡 讲师批注：证明线面垂直的标准模板：**「平面内的两条相交直线」**缺一不可！

  - **[1] ② の証明**：
    ① より $AB \perp \text{平面 } CDM$ であり、辺 $CD$ は平面 $CDM$ 上にあるから、直線と平面の垂直の定義より：
    $$AB \perp CD$$
    > 💡 讲师批注：这是极其重要的结论：**正四面体的任意两组对棱互相垂直**（异面垂直），在后续空间向量与体积计算中频繁使用。

  - **[2] の証明**：
    $\triangle ABC$ において、$P, Q$ はそれぞれ辺 $BC, AC$ の中点であるから、中点連結定理より：
    $$PQ \parallel AB, \qquad PQ = \frac{1}{2}AB$$
    $\triangle ABD$ において、$S, R$ はそれぞれ辺 $BD, AD$ の中点であるから、中点連結定理より：
    $$SR \parallel AB, \qquad SR = \frac{1}{2}AB$$
    よって、$PQ \parallel SR$ かつ $PQ = SR$ であるから、四角形 $PQRS$ は**平行四辺形**である。
    > 💡 讲师批注：先证平行四边形（一组对边平行且相等），再证「邻边相等」和「夹角为 $90^\circ$」。

    また、$\triangle ACD$ において中点連結定理より：
    $$QR \parallel CD, \qquad QR = \frac{1}{2}CD$$
    正四面体では $AB = CD$ であるから：$PQ = QR$。
    さらに、[1] ② より $AB \perp CD$ であり、$PQ \parallel AB,\; QR \parallel CD$ であるから：
    $$PQ \perp QR \quad (\text{すなわち } \angle PQR = 90^\circ)$$
    したがって、四角形 $PQRS$ は隣り合う 2 辺が等しく 1 つの角が直角である平行四辺形、すなわち**正方形**である。（証明終）

- **【最终答案】**
  **[1]、[2] 均如上证明成立。**

---

#### 演習問題 9-(2)
- **【原题重现与翻译】**
  - 原题：平面 $\alpha$ とその上にない点 $A$ があり、また、$\alpha$ 上に直線 $l$ と $l$ 上にない点 $O$ があるとする。$l$ 上の 1 点を $B$ とするとき、$AB \perp l,\; OB \perp l,\; OA \perp OB$ ならば $OA \perp \alpha$ が成り立つことを証明せよ。
  - 中文：已知平面 $\alpha$ 及其外一点 $A$，$\alpha$ 内有直线 $l$ 与不在 $l$ 上的点 $O$。设 $B$ 为 $l$ 上一点，若 $AB \perp l,\; OB \perp l,\; OA \perp OB$，求证：$OA \perp \alpha$。
- **【考点定位】**
  - 线面垂直判定定理的两次连续应用（**三垂线定理的逆定理**）。
- **【图解辅助（SVG 矢量图）】**

<svg viewBox="0 0 340 200" width="54%" xmlns="http://www.w3.org/2000/svg" style="background:#fafafa;border:1px solid #e0e0e0;border-radius:8px;margin:8px 0;">
  <!-- Plane alpha -->
  <polygon points="35,145 120,85 305,120 220,180" fill="rgba(226,232,240,0.45)" stroke="#475569" stroke-width="1.6"/>
  <!-- Line l on alpha -->
  <line x1="95" y1="120" x2="185" y2="172" stroke="#1e293b" stroke-width="1.8"/>
  <!-- Points: B(135,143), O(220,130), A(220,30) -->
  <line x1="220" y1="30" x2="220" y2="130" stroke="#dc2626" stroke-width="2"/>
  <line x1="220" y1="30" x2="135" y2="143" stroke="#2563eb" stroke-width="1.8"/>
  <line x1="220" y1="130" x2="135" y2="143" stroke="#2563eb" stroke-width="1.8"/>
  <!-- Auxiliary l' through O parallel to l -->
  <line x1="185" y1="110" x2="260" y2="153" stroke="#10b981" stroke-width="1.3" stroke-dasharray="4,3"/>
  <!-- Right angle at O (OA perp OB) -->
  <polyline points="210,131.5 210,121.5 220,120" fill="none" stroke="#dc2626" stroke-width="1.2"/>
  <!-- Labels -->
  <text x="216" y="22" font-size="14" font-weight="bold" fill="#dc2626">A</text>
  <text x="228" y="135" font-size="14" font-weight="bold" fill="#111">O</text>
  <text x="122" y="156" font-size="14" font-weight="bold" fill="#111">B</text>
  <text x="188" y="175" font-size="14" font-style="italic" fill="#111">l</text>
  <text x="262" y="158" font-size="12" font-style="italic" fill="#10b981">l' (∥ l)</text>
  <text x="55" y="148" font-size="14" font-weight="bold" fill="#475569">α</text>
</svg>

- **【分步标准解答】**
  【証明】
  仮定より、直線 $l$ は平面 $OAB$ 上の交わる 2 直線 $AB, OB$ に垂直であるから、直線と平面の垂直の定理より：
  $$l \perp \text{平面 } OAB$$
  直線 $OA$ は平面 $OAB$ 上にあるから、垂直の定義より：
  $$l \perp OA \quad (\text{すなわち } OA \perp l)$$
  > 💡 讲师批注：先证 $l \perp \text{平面 } OAB$，从而「免费」获得 $OA \perp l$！

  さらに、仮定より $OA \perp OB$ である。
  ここで、点 $O$ は $l$ 上にないから、直線 $l$ と直線 $OB$ は平面 $\alpha$ 上で点 $B$ で交わる 2 直線である（あるいは、$\alpha$ 上で点 $O$ を通り $l$ に平行な直線 $l'$ を引くと、$OA \perp l'$ かつ $OA \perp OB$ で $l'$ と $OB$ は点 $O$ で交わる）。
  したがって、直線 $OA$ は平面 $\alpha$ 上の交わる 2 直線に垂直であるから、直線と平面の垂直の定理より：
  $$OA \perp \alpha$$
  （証明終）

- **【最终答案】**
  **如上证明成立（两次运用线面垂直判定定理，即三垂线定理之逆）。**

---

### 第六章 演習問題 1（三角関数の相互関係，P119–P120）

#### 【课内例题回顾】（P119 / 原书 p.118 `[2.3] 解説(2)`）
- **原题**：$\theta$ が第 2 象限の角で、$\sin\theta = \dfrac{4}{5}$ のとき、$\cos\theta, \tan\theta$ の値を求めよ。
- **速解**：$\cos^2\theta = 1 - \left(\dfrac{4}{5}\right)^2 = \dfrac{9}{25}$。第 2 象限より $\cos\theta < 0$ ゆえ $\cos\theta = -\dfrac{3}{5}$、$\tan\theta = \dfrac{4/5}{-3/5} = -\dfrac{4}{3}$。

---

#### 演習問題 1-(1)
> ⚠️ **教材勘误提示（P119 / 原书 p.118）**：经核对参考图 `page_0119.jpg`，原教材仅印出「$\dfrac{3}{2}\pi < \theta < 2\pi$ とする。$\cos\theta$ と $\tan\theta$ の値を求めよ。」，**漏印了 $\sin\theta$ 的具体数值**（无法求出唯一数值）。以下先给出**通用参数解**（设 $\sin\theta = k,\; -1 < k < 0$），再以日本教材高频典型值 $\sin\theta = -\dfrac{3}{5}$ 示范完整板书过程，备课时可直接向学生补充该条件。

- **【原题重现与翻译】**
  - 原题：$\dfrac{3}{2}\pi < \theta < 2\pi$ とする。【※原書欠落：$\sin\theta = k\;(-1 < k < 0)$ のとき】$\cos\theta$ と $\tan\theta$ の値を求めよ。
  - 中文：设 $\dfrac{3}{2}\pi < \theta < 2\pi$（补充条件：$\sin\theta = k$，$-1 < k < 0$），求 $\cos\theta$ 和 $\tan\theta$ 的值。
- **【考点定位】**
  - 象限角的符号判定（第 4 象限 $\cos\theta > 0,\; \tan\theta < 0$）与同角三角函数基本关系。
- **【图解辅助（SVG 矢量图：单位圆与象限符号总图）】**

<svg viewBox="0 0 380 210" width="60%" xmlns="http://www.w3.org/2000/svg" style="background:#fafafa;border:1px solid #e0e0e0;border-radius:8px;margin:8px 0;">
  <!-- Axes -->
  <line x1="20" y1="105" x2="210" y2="105" stroke="#475569" stroke-width="1.4"/>
  <line x1="115" y1="15" x2="115" y2="195" stroke="#475569" stroke-width="1.4"/>
  <!-- Unit circle -->
  <circle cx="115" cy="105" r="70" fill="none" stroke="#1e293b" stroke-width="1.8"/>
  <!-- Q4 ray example (cos=0.8, sin=-0.6) -> (115+56, 105+42) = (171, 147) -->
  <line x1="115" y1="105" x2="171" y2="147" stroke="#dc2626" stroke-width="2"/>
  <circle cx="171" cy="147" r="3.5" fill="#dc2626"/>
  <line x1="171" y1="105" x2="171" y2="147" stroke="#dc2626" stroke-width="1.2" stroke-dasharray="3,2"/>
  <!-- Quadrant signs -->
  <text x="140" y="65" font-size="11" fill="#2563eb" font-weight="bold">第1象限</text>
  <text x="140" y="79" font-size="10" fill="#334155">全正 (+,+,+)</text>
  <text x="48" y="65" font-size="11" fill="#2563eb" font-weight="bold">第2象限</text>
  <text x="48" y="79" font-size="10" fill="#334155">sin +</text>
  <text x="48" y="140" font-size="11" fill="#2563eb" font-weight="bold">第3象限</text>
  <text x="48" y="154" font-size="10" fill="#334155">tan +</text>
  <text x="130" y="165" font-size="11" fill="#dc2626" font-weight="bold">第4象限</text>
  <text x="130" y="179" font-size="10" fill="#dc2626">cos +</text>
  <!-- Labels -->
  <text x="202" y="100" font-size="12" fill="#111">x</text>
  <text x="120" y="24" font-size="12" fill="#111">y</text>
  <text x="102" y="118" font-size="11" fill="#111">O</text>
  <!-- Right note box -->
  <rect x="225" y="35" width="145" height="140" rx="6" fill="#fff" stroke="#cbd5e1" stroke-width="1.2"/>
  <text x="235" y="58" font-size="12" font-weight="bold" fill="#1e293b">第 4 象限の符号</text>
  <text x="235" y="80" font-size="12" fill="#475569">3π/2 &lt; θ &lt; 2π</text>
  <text x="235" y="104" font-size="12" fill="#dc2626">• sin θ &lt; 0</text>
  <text x="235" y="126" font-size="12" fill="#10b981">• cos θ &gt; 0</text>
  <text x="235" y="148" font-size="12" fill="#dc2626">• tan θ &lt; 0</text>
</svg>

- **【分步标准解答】**
  - **通用解法（$\sin\theta = k,\; -1 < k < 0$ とおく）**：
    $\sin^2\theta + \cos^2\theta = 1$ より：
    $$\cos^2\theta = 1 - \sin^2\theta = 1 - k^2$$
    $\dfrac{3}{2}\pi < \theta < 2\pi$ より、$\theta$ は第 4 象限の角であるから $\cos\theta > 0$。よって：
    $$\cos\theta = \sqrt{1 - k^2}$$
    また：
    $$\tan\theta = \frac{\sin\theta}{\cos\theta} = \frac{k}{\sqrt{1 - k^2}}$$
  - **补充典型数值示范（例：$\sin\theta = -\dfrac{3}{5}$ とした場合）**：
    $$\cos^2\theta = 1 - \left(-\frac{3}{5}\right)^2 = \frac{16}{25}$$
    $\cos\theta > 0$ より $\cos\theta = \dfrac{4}{5}$。また $\tan\theta = \dfrac{-3/5}{4/5} = -\dfrac{3}{4}$。
    > 💡 讲师批注：无论补充何种数值（如 $-\frac{1}{3}, -\frac{3}{5}, -\frac{5}{13}$），核心考点都是「由 $\frac{3}{2}\pi < \theta < 2\pi$ 判断 $\cos\theta > 0$」。

- **【最终答案】**
  **通用解（$\sin\theta = k$）：$\cos\theta = \sqrt{1-k^2},\; \tan\theta = \dfrac{k}{\sqrt{1-k^2}}$（示范 $\sin\theta = -\dfrac{3}{5}$ 时：$\cos\theta = \dfrac{4}{5},\; \tan\theta = -\dfrac{3}{4}$）**

---

#### 演習問題 1-(2)
- **【原题重现与翻译】**
  - 原题：$\tan\theta = 7$ のとき、$\sin\theta$ と $\cos\theta$ の値を求めよ。
  - 中文：当 $\tan\theta = 7$ 时，求 $\sin\theta$ 和 $\cos\theta$ 的值。
- **【考点定位】**
  - 公式 $1 + \tan^2\theta = \dfrac{1}{\cos^2\theta}$ 的应用，以及**未给定象限时必须分类讨论**的易错点。
- **【分步标准解答】**
  $1 + \tan^2\theta = \dfrac{1}{\cos^2\theta}$ より：
  $$\frac{1}{\cos^2\theta} = 1 + 7^2 = 50 \implies \cos^2\theta = \frac{1}{50}$$
  よって：
  $$\cos\theta = \pm \frac{1}{\sqrt{50}} = \pm \frac{1}{5\sqrt{2}} = \pm \frac{\sqrt{2}}{10}$$
  > 💡 讲师批注：**高频失分点！** 题目未限制 $\theta$ 的象限，由于 $\tan\theta = 7 > 0$，$\theta$ 可能是第 1 象限角（$\sin>0, \cos>0$），也可能是第 3 象限角（$\sin<0, \cos<0$），绝对不能只写正值！

  また、$\sin\theta = \tan\theta \cos\theta = 7\cos\theta$ であるから：
  - $\cos\theta = \dfrac{\sqrt{2}}{10}$ のとき（第 1 象限）：$\sin\theta = 7 \cdot \dfrac{\sqrt{2}}{10} = \dfrac{7\sqrt{2}}{10}$
  - $\cos\theta = -\dfrac{\sqrt{2}}{10}$ のとき（第 3 象限）：$\sin\theta = 7 \cdot \left(-\dfrac{\sqrt{2}}{10}\right) = -\dfrac{7\sqrt{2}}{10}$
  > 💡 讲师批注：务必用「複号同順」（复号同序）或分情况写清配对关系，切忌写成 $\sin\theta = \pm\frac{7\sqrt{2}}{10}, \cos\theta = \pm\frac{\sqrt{2}}{10}$ 而不注明同号！验算：$\left(\frac{7\sqrt{2}}{10}\right)^2 + \left(\frac{\sqrt{2}}{10}\right)^2 = \frac{98+2}{100} = 1$。

- **【最终答案】**
  **$(\sin\theta,\; \cos\theta) = \left(\dfrac{7\sqrt{2}}{10},\; \dfrac{\sqrt{2}}{10}\right)$ または $\left(-\dfrac{7\sqrt{2}}{10},\; -\dfrac{\sqrt{2}}{10}\right)$**（亦可写作 $\sin\theta = \pm\dfrac{7\sqrt{2}}{10},\; \cos\theta = \pm\dfrac{\sqrt{2}}{10}$ （複号同順））

---

#### 演習問題 1-(3)
- **【原题重现与翻译】**
  - 原题：$\sin\theta + \cos\theta = \dfrac{\sqrt{3}}{2}$ とする。次の式の値を求めよ。
    - [1] $\sin\theta\cos\theta,\quad \sin^3\theta + \cos^3\theta$
    - [2] $\dfrac{\pi}{2} < \theta < \pi,\quad \cos\theta - \sin\theta$
  - 中文：已知 $\sin\theta + \cos\theta = \dfrac{\sqrt{3}}{2}$，求下列各式的值：
    - [1] $\sin\theta\cos\theta,\quad \sin^3\theta + \cos^3\theta$；
    - [2] 当 $\dfrac{\pi}{2} < \theta < \pi$ 时，求 $\cos\theta - \sin\theta$。
- **【考点定位】**
  - 三角对称式求值（$\sin\theta \pm \cos\theta$ 与 $\sin\theta\cos\theta$ 的相互转化）、立方和公式及象限符号判定。
- **【分步标准解答】**
  - **[1] の解答**：
    $\sin\theta + \cos\theta = \dfrac{\sqrt{3}}{2}$ の両辺を 2 乗すると：
    $$(\sin\theta + \cos\theta)^2 = \frac{3}{4}$$
    $$\sin^2\theta + 2\sin\theta\cos\theta + \cos^2\theta = \frac{3}{4}$$
    $\sin^2\theta + \cos^2\theta = 1$ であるから：
    $$1 + 2\sin\theta\cos\theta = \frac{3}{4} \implies 2\sin\theta\cos\theta = -\frac{1}{4} \implies \sin\theta\cos\theta = -\frac{1}{8}$$
    > 💡 讲师批注：核心恒等式 $(\sin\theta \pm \cos\theta)^2 = 1 \pm 2\sin\theta\cos\theta$ 务必达到肌肉记忆！

    次に、対称式の変形公式 $a^3 + b^3 = (a+b)^3 - 3ab(a+b)$ を用いると：
    $$\sin^3\theta + \cos^3\theta = (\sin\theta + \cos\theta)^3 - 3\sin\theta\cos\theta(\sin\theta + \cos\theta)$$
    $$= \left(\frac{\sqrt{3}}{2}\right)^3 - 3\left(-\frac{1}{8}\right)\left(\frac{\sqrt{3}}{2}\right) = \frac{3\sqrt{3}}{8} + \frac{3\sqrt{3}}{16} = \frac{9\sqrt{3}}{16}$$
    > 💡 讲师批注：也可用因式分解式 $(\sin\theta+\cos\theta)(\sin^2\theta-\sin\theta\cos\theta+\cos^2\theta) = \frac{\sqrt{3}}{2}\left(1+\frac{1}{8}\right) = \frac{9\sqrt{3}}{16}$，计算更轻快！

  - **[2] の解答**：
    $$(\cos\theta - \sin\theta)^2 = \cos^2\theta - 2\sin\theta\cos\theta + \sin^2\theta = 1 - 2\left(-\frac{1}{8}\right) = 1 + \frac{1}{4} = \frac{5}{4}$$
    ここで、$\dfrac{\pi}{2} < \theta < \pi$（第 2 象限）であるから、$\sin\theta > 0$ かつ $\cos\theta < 0$ である。
    よって $\cos\theta - \sin\theta < 0$ となるから：
    $$\cos\theta - \sin\theta = -\sqrt{\frac{5}{4}} = -\frac{\sqrt{5}}{2}$$
    > 💡 讲师批注：开方前**必须判断 $\cos\theta - \sin\theta$ 的正负号**！第 2 象限中「负数减正数必为负」，所以取负号。

- **【最终答案】**
  **[1] $\sin\theta\cos\theta = -\dfrac{1}{8},\quad \sin^3\theta + \cos^3\theta = \dfrac{9\sqrt{3}}{16}$；[2] $\cos\theta - \sin\theta = -\dfrac{\sqrt{5}}{2}$**

---

#### 演習問題 1-(4)
- **【原题重现与翻译】**
  - 原题：$a$ を正の定数とし、$\theta$ を $0 \le \theta \le \pi$ を満たす角とする。2 次方程式 $2x^2 - 2(2a-1)x - a = 0$ の 2 つの解が $\sin\theta, \cos\theta$ であるとき、$a, \sin\theta, \cos\theta$ の値をそれぞれ求めよ。
  - 中文：设 $a$ 为正定数，$\theta$ 为满足 $0 \le \theta \le \pi$ 的角。当一元二次方程 $2x^2 - 2(2a-1)x - a = 0$ 的两个解为 $\sin\theta, \cos\theta$ 时，分别求 $a, \sin\theta, \cos\theta$ 的值。
- **【考点定位】**
  - 二次方程根与系数的关系（韦达定理）+ 三角恒等式 $\sin^2\theta + \cos^2\theta = 1$ + 角度范围对 $\sin\theta, \cos\theta$ 符号的筛选。
- **【分步标准解答】**
  2 次方程式 $2x^2 - 2(2a-1)x - a = 0$ の 2 つの解が $\sin\theta, \cos\theta$ であるから、解と係数の関係より：
  $$\sin\theta + \cos\theta = \frac{2(2a-1)}{2} = 2a - 1 \qquad \cdots \text{①}$$
  $$\sin\theta\cos\theta = -\frac{a}{2} \qquad \cdots \text{②}$$
  > 💡 讲师批注：使用韦达定理 $\alpha+\beta = -\frac{b}{a},\; \alpha\beta = \frac{c}{a}$ 时，注意首项系数是 $2$，别忘了除以 $2$！

  $(\sin\theta + \cos\theta)^2 = \sin^2\theta + \cos^2\theta + 2\sin\theta\cos\theta = 1 + 2\sin\theta\cos\theta$ に ①、② を代入すると：
  $$(2a - 1)^2 = 1 + 2\left(-\frac{a}{2}\right)$$
  $$4a^2 - 4a + 1 = 1 - a$$
  $$4a^2 - 3a = 0 \implies a(4a - 3) = 0$$
  $a$ は正の定数（$a > 0$）であるから：
  $$a = \frac{3}{4}$$
  > 💡 讲师批注：注意舍去 $a = 0$（题干明确 $a > 0$）。

  $a = \dfrac{3}{4}$ をもとの 2 次方程式に代入すると：
  $$2x^2 - 2\left(2 \cdot \frac{3}{4} - 1\right)x - \frac{3}{4} = 0$$
  $$2x^2 - x - \frac{3}{4} = 0 \implies 8x^2 - 4x - 3 = 0$$
  解の公式より：
  $$x = \frac{4 \pm \sqrt{(-4)^2 - 4 \cdot 8 \cdot (-3)}}{2 \cdot 8} = \frac{4 \pm \sqrt{16 + 96}}{16} = \frac{4 \pm \sqrt{112}}{16} = \frac{4 \pm 4\sqrt{7}}{16} = \frac{1 \pm \sqrt{7}}{4}$$
  ここで、$0 \le \theta \le \pi$ であるから $\sin\theta \ge 0$ である。
  $2 < \sqrt{7} < 3$ より：
  $$\frac{1 + \sqrt{7}}{4} > 0, \qquad \frac{1 - \sqrt{7}}{4} < 0$$
  （かつ両者とも $[-1, 1]$ の範囲にあるから、実数角 $\theta$ が確かに存在する。）
  したがって：
  $$\sin\theta = \frac{1 + \sqrt{7}}{4}, \qquad \cos\theta = \frac{1 - \sqrt{7}}{4}$$
  > 💡 讲师批注：验算：① $\sin^2\theta + \cos^2\theta = \frac{(1+\sqrt{7})^2+(1-\sqrt{7})^2}{16} = \frac{16}{16} = 1$；② $\sin\theta+\cos\theta = \frac{1}{2} = 2\cdot\frac{3}{4}-1$；③ $\sin\theta\cos\theta = \frac{1-7}{16} = -\frac{3}{8} = -\frac{3/4}{2}$，100% 准确！

- **【最终答案】**
  **$a = \dfrac{3}{4},\quad \sin\theta = \dfrac{1 + \sqrt{7}}{4},\quad \cos\theta = \dfrac{1 - \sqrt{7}}{4}$**
