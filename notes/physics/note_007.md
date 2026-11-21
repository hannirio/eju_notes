# EJU 物理全解讲义 — 切片 007（P.91–P.105）
> **对应教材章节**：物理基礎・第四章 電気と磁気（抵抗の接続、電池の起電力と内部抵抗、ホイートストンブリッジ、コンデンサーを含む直流回路、磁極と磁場、電流がつくる磁場、安培力・ローレンツ力・ホール効果、電磁誘導・自己誘導・相互誘導、交流と実効値）  
> **适用对象**：需快速唤醒中国高中电磁学基础、厘清中日磁场符号体系差异（$H$ 与 $B$）、并掌握纯日文板书与 EJU 考场规范表达的授课教师 / 考生  
> **切片说明**：本切片（教材页码 90–104）全篇为**核心概念、定律与高频模型精讲页**（共 0 道原教材编号例题/练习题）；第 3 部分将切片内 8 大 EJU 必考物理模型按规范板书推导与多色 SVG 图解逐一深度拆解。

---

## 1. 本节前置：国内高中物理基础唤醒

本切片横跨**恒定电流（直流回路）**、**磁场（磁気）**、**电磁感应（電磁誘導）**与**交变电流（交流）**四大板块，是 EJU 物理中分值占比仅次于力学、且**中日教材体系差异最大**的区域（尤其是日本高中保留了磁场强度 $H$、磁荷 $m$ 与磁荷库仑定律）。

### 1.1 直流电路后半段核心概念

1. **电阻的串并联（抵抗の接続）**
   - **串联（直列接続）**：电流处处相等 $I = I_1 = I_2$，总电压 $V = V_1 + V_2$，合成电阻：
     $$R = R_1 + R_2$$
   - **并联（並列接続）**：各支路电压相等 $V = V_1 = V_2$，总电流 $I = I_1 + I_2$，合成电阻：
     $$\frac{1}{R} = \frac{1}{R_1} + \frac{1}{R_2} \iff R = \frac{R_1 R_2}{R_1 + R_2}$$

2. **电源电动势与内阻（電池の起電力と内部抵抗）**
   - 路端电压（端子電圧）$V$ 与电动势 $E$、内阻 $r$、干路电流 $I$ 的关系（闭合电路欧姆定律）：
     $$V = E - rI \qquad \left(I = \frac{E}{R + r}\right)$$
   - **$V$-$I$ 特征图像**：纵轴截距为电动势 $E$，斜率为 $-r$，横轴截距（短路电流）为 $\dfrac{E}{r}$。

3. **惠斯通电桥（ホイートストンブリッジ）与含容直流电路**
   - 当电桥四臂电阻满足 $\dfrac{R_1}{R_2} = \dfrac{R_3}{R_4}$（即对角乘积相等 $R_1 R_4 = R_2 R_3$）时，桥路 $BD$ 两端等电势，无电流通过（$I_{BD} = 0$），可将 $BD$ 视为断路或短路。
   - **含电容直流电路（RC 回路）**：
     - 闭合开关瞬间（$t = 0$，初始不带电）：$Q = 0 \implies V_C = 0$，电容器相当于**导线（短路）**，初始电流 $I_0 = \dfrac{E}{R}$；
     - 充分长时间后（定常状態）：充电结束，$I = 0$，电阻两端无电压降，电容器相当于**断路**，$V_C = E$，$Q = CE$。

### 1.2 磁场、安培力与洛伦兹力核心公式

1. **磁荷与磁场强度 $H$（日本高中特色，国内大学才学）**
   - 磁极（N 极、S 极）**无法单独存在**（不存在磁单极子）。磁极所带“磁量”称**磁気量** $m\text{ [Wb]}$。
   - **磁荷库仑定律**：$F = k_m \dfrac{m_1 m_2}{r^2} = \dfrac{1}{4\pi\mu_0}\dfrac{m_1 m_2}{r^2}$。
   - **磁场强度（磁場の強さ）$\vec{H}$**：放置 $+1\text{ Wb}$ 的 N 极所受磁力：
     $$\vec{F} = m\vec{H} \qquad (\text{单位：[N/Wb] 或 [A/m]})$$

2. **三种典型电流产生的磁场（右ねじの法則 / 安培定则）**
   - **无限长直导线（直線電流）**：距导线 $r$ 处，$H = \dfrac{I}{2\pi r}$；
   - **单匝圆形电流圆心（円形電流）**：半径 $r$，$H = \dfrac{I}{2r}$（$N$ 匝则乘 $N$）；
   - **无限长通电螺线管内部（ソレノイド）**：单位长度匝数 $n = \dfrac{N}{l}$，$H = nI$。

3. **磁感应强度（磁束密度）$\vec{B}$ 与磁通量（磁束）$\Phi$**
   - 磁导率（透磁率）$\mu\text{ [N/A}^2]$，真空磁导率 $\mu_0 = 4\pi \times 10^{-7}\text{ N/A}^2$，相对磁导率（比透磁率）$\mu_r = \dfrac{\mu}{\mu_0}$。
   - **核心桥梁公式**：
     $$\vec{B} = \mu \vec{H} \quad (\text{单位：[T] = [Wb/m}^2\text{] = [N/(A}\cdot\text{m)]})$$
   - **磁通量（标量）**：磁场垂直穿过面积 $S$ 时，$\Phi = BS$（若磁感线与法线夹角为 $\theta$，则 $\Phi = BS\cos\theta$）。

4. **安培力、平行电流相互作用、洛伦兹力与霍尔效应**
   - **安培力（電流が磁場から受ける力）**：$F = IBl\sin\theta = \mu IHl\sin\theta$（方向由**弗莱明左手定则**判定）。
   - **两平行直导线间的作用力**：间距 $r$、长度 $l$ 上所受力 $F = \dfrac{\mu_0 I_A I_B}{2\pi r}l$（**同向相吸，反向相斥**）。
   - **洛伦兹力（ローレンツ力）**：$f = qvB\sin\theta$（始终垂直于 $\vec{v}$，**永不做功**）。
   - **带电粒子在匀强磁场中的圆周运动（$\vec{v} \perp \vec{B}$）**：由 $m\dfrac{v^2}{r} = qvB$ 得：
     $$r = \frac{mv}{qB}, \qquad T = \frac{2\pi r}{v} = \frac{2\pi m}{qB} \quad (\text{周期 } T \text{ 与速率 } v \text{ 无关！})$$
   - **霍尔效应（ホール効果）**：稳态时电场力与洛伦兹力平衡 $eE_y = evB \implies V_H = E_y d = vBd$；结合电流微观式 $I = envS = envdt$，可得：
     $$V_H = \frac{IB}{ent}$$

### 1.3 电磁感应、自感互感与交流电

1. **楞次定律（レンツの法則）与法拉第电磁感应定律（ファラデーの電磁誘導の法則）**
   - 感应电流的磁场总是**阻碍（妨げる）**引起感应电流的磁通量变化（增反减同、来拒去留）。
   - $N$ 匝线圈的感应电动势：
     $$V = -N\frac{\Delta \Phi}{\Delta t}$$
2. **自感（自己誘導）与互感（相互誘導）**
   - **自感电动势**：$V = -L\dfrac{\Delta I}{\Delta t}$；长直螺线管自感系数 $L = \mu n^2 S l = \dfrac{\mu N^2 S}{l}\text{ [H]}$。
   - **互感电动势**：$V_2 = -M\dfrac{\Delta I_1}{\Delta t}$；共轴螺线管互感系数 $M = \mu n_1 n_2 S l\text{ [H]}$。
3. **正弦交流电（交流）与有效值（実効値）**
   - 单匝线圈在匀强磁场中以角速度 $\omega$ 匀速转动，磁通量 $\Phi = \Phi_0 \cos\omega t$，感应电动势：
     $$V = -\frac{\Delta \Phi}{\Delta t} = \Phi_0 \omega \sin\omega t = V_0 \sin\omega t \qquad (V_0 = \Phi_0 \omega = BS\omega)$$
   - **有效值**：按一个周期内与直流电在纯电阻上**消耗相同平均功率**（$\bar{P} = \frac{1}{2}I_0 V_0 = I_e V_e$）定义：
     $$V_e = \frac{V_0}{\sqrt{2}}, \qquad I_e = \frac{I_0}{\sqrt{2}}$$

### 1.4 中日物理体系与习惯差异提醒

| 对比维度 | 中国国内高中物理习惯 | 日本 EJU / 高中物理习惯（授课必强调） |
| :--- | :--- | :--- |
| **磁场 $B$ 与 $H$** | 高中阶段**只讲磁感应强度 $B$**，完全不提磁场强度 $H$ 和磁荷 $m$ | 严格区分**磁場の強さ $H\text{ [A/m]}$** 与**磁束密度 $B\text{ [T]}$**，通过 $B = \mu H$ 联系；且所有电流磁场公式先写 $H$（如 $H = nI$），再乘 $\mu$ 得 $B = \mu nI$。 |
| **感应电动势符号** | 常用 $E$ 表示感应电动势（$E = n\frac{\Delta\Phi}{\Delta t}$） | 日本教材与 EJU 极常用 **$V$** 表示感应电动势（$V = -N\frac{\Delta\Phi}{\Delta t}$、$V = -L\frac{\Delta I}{\Delta t}$），并显式带**负号**体现楞次定律。 |
| **有效值下标** | 常用 $U, I$（无下标）或 $U_{\text{有}}$，最大值写 $U_m, I_m$ | 有效值一律用下标 $e$（effective）：**$V_e, I_e$**；最大值一律用下标 $0$：**$V_0, I_0$**。 |
| **左手定则名称** | 简称“左手定则” | 正式全称**フレミングの左手の法則**（弗莱明左手定则）；安培定则称为**右ねじの法則**（右螺旋定则）。 |
| **电阻与电容符号** | 电容常称“电容器”，电阻称“电阻” | 电容器用片假名 **コンデンサー**，线圈用 **コイル**，螺线管用 **ソレノイド**，载流子用 **キャリア**。 |
| **教材页眉归属提醒** | 电磁学全属高中选择性必修二 | 本讲义页眉虽统一印为「物理基礎・第四章」，但实际除欧姆定律外，**电桥、电容、磁场、电磁感应、交流电均属日本高阶《物理》大纲**，EJU 必考！ |

---

## 2. 日文物理核心词汇与公式假名注音（板书必备）

### 2.1 核心物理词汇表

#### 直流电路与电桥、电容器
- **合成抵抗（ごうせいていこう / gōsei teikō）** — 等效电阻 / 合成电阻
- **電池（でんち / denchi）** — 电池 / 电源
- **起電力（きでんりょく / kidenryoku）** — 电动势（$E$）
- **内部抵抗（ないぶていこう / naibu teikō）** — 内阻 / 内部电阻（$r$）
- **端子電圧（たんしでんあつ / tanshi den'atsu）** — 路端电压 / 端电压（$V$）
- **ホイートストンブリッジ（ほいーとすとんぶりっじ / hoītosuton burijji）** — 惠斯通电桥
- **直流回路（ちょくりゅうかいろ / chokuryū kairo）** — 直流电路
- **コンデンサー（こんでんさー / kondensā）** — 电容器
- **電気容量（でんきようりょう / denki yōryō）** — 电容（$C$）
- **スイッチ（すいっち / suitchi）** — 开关

#### 磁极、磁场与电流的磁场
- **磁気（じき / jiki）** — 磁 / 磁学
- **磁石（じしゃく / jishaku）** — 磁铁 / 磁体
- **磁極（じきょく / jikyoku）** — 磁极（N 极、S 极）
- **磁気量（じきりょう / jikiryō）** — 磁荷 / 磁极强度（$m$）
- **ウェーバ（うぇーば / wēba）** — 韦伯（$\text{Wb}$）
- **磁気力（じきりょく / jikiryoku）** — 磁力
- **磁気に関するクーロンの法則（じきにかんするくーろんのほうそく / jiki ni kansuru Kūron no hōsoku）** — 磁荷库仑定律
- **磁場 / 磁界（じば・じかい / jiba / jikai）** — 磁场（$H$）
- **磁力線（じりょくせん / jiryokusen）** — 磁感线
- **右ねじの法則（みぎねじのほうそく / migineji no hōsoku）** — 右手螺旋定则（安培定则）
- **直線電流（ちょくせんでんりゅう / chokusen denryū）** — 直线电流
- **円形電流（えんけいでんりゅう / enkei denryū）** — 环形电流
- **ソレノイド（それのいど / sorenoido）** — 螺线管
- **導線（どうせん / dōsen）** — 导线

#### 安培力、磁通密度、洛伦兹力与霍尔效应
- **フレミングの左手の法則（ふれみんぐのひだりてのほうそく / Furemingu no hidarite no hōsoku）** — 弗莱明左手定则
- **透磁率（とうじりつ / tōjiritsu）** — 磁导率（$\mu$）
- **真空の透磁率（しんくうのとうじりつ / shinkū no tōjiritsu）** — 真空磁导率（$\mu_0$）
- **比透磁率（ひとうじりつ / hitōjiritsu）** — 相对磁导率（$\mu_r$）
- **誘電率（ゆうでんりつ / yūdenritsu）** — 介电常数（$\varepsilon$）
- **真空の誘電率（しんくうのゆうでんりつ / shinkū no yūdenritsu）** — 真空介电常数（$\varepsilon_0$）
- **比誘電率（ひゆうでんりつ / hiyūdenritsu）** — 相对介电常数（$\varepsilon_r$）
- **平行電流（へいこうでんりゅう / heikō denryū）** — 平行电流
- **磁束密度（じそくみつど / jisoku mitsudo）** — 磁感应强度 / 磁通密度（$B$）
- **テスラ（てすら / tesura）** — 特斯拉（$\text{T}$）
- **磁束（じそく / jisoku）** — 磁通量（$\Phi$）
- **ローレンツ力（ろーれんつりょく / Rōrentsu-ryoku）** — 洛伦兹力
- **荷電粒子（かでんりゅうし / kaden ryūshi）** — 带电粒子
- **陰極線（いんきょくせん / inkyokusen）** — 阴极射线
- **らせん運動（らせんうんどう / rasen undō）** — 螺旋运动
- **ホール効果（ほーるこうか / Hōru kōka）** — 霍尔效应
- **キャリア（きゃりあ / kyaria）** — 载流子
- **自由電子（じゆうでんし / jiyū denshi）** — 自由电子
- **ホール電圧（ほーるでんあつ / Hōru den'atsu）** — 霍尔电压（$V_H$）

#### 电磁感应、自感互感与交流电
- **電磁誘導（でんじゆうどう / denji yūdō）** — 电磁感应
- **誘導起電力（ゆうどうきでんりょく / yūdō kidenryoku）** — 感应电动势
- **誘導電流（ゆうどうでんりゅう / yūdō denryū）** — 感应电流
- **レンツの法則（れんつのほうそく / Rentsu no hōsoku）** — 楞次定律
- **ファラデーの電磁誘導の法則（ふぁらでーのでんじゆうどうのほうそく / Faradē no denji yūdō no hōsoku）** — 法拉第电磁感应定律
- **コイル（こいる / koiru）** — 线圈
- **自己誘導（じこゆうどう / jiko yūdō）** — 自感
- **逆起電力（ぎゃくきでんりょく / gyakukidenryoku）** — 反电动势 / 自感电动势
- **自己インダクタンス（じこいんだくたんす / jiko indakutansu）** — 自感系数（$L$）
- **ヘンリー（へんりー / henrī）** — 亨利（$\text{H}$）
- **鉄心（てっしん / tesshin）** — 铁芯
- **相互誘導（そうごゆうどう / sōgo yūdō）** — 互感
- **1次コイル / 2次コイル（いちじこいる・にじこいる / ichiji koiru / niji koiru）** — 原线圈 / 副线圈
- **相互インダクタンス（そうごいんだくたんす / sōgo indakutansu）** — 互感系数（$M$）
- **交流（こうりゅう / kōryū）** — 交流电（AC）
- **交流電圧（こうりゅうでんあつ / kōryū den'atsu）** — 交流电压
- **交流電流（こうりゅうでんりゅう / kōryū denryū）** — 交流电流
- **実効値（じっこうち / jikkōchi）** — 有效值（$V_e, I_e$）
- **消費電力（しょうひでんりょく / shōhi denryoku）** — 消耗功率

### 2.2 核心公式课堂口语读法（板书念法）

| 公式 | 日本课堂标准板书口语读法 |
| :--- | :--- |
| $V = E - rI$ | 「ブイ・イコール、イー、ひく、スモールアール・アイ」 |
| $\dfrac{R_1}{R_2} = \dfrac{R_3}{R_4}$ | 「アールにぶんの・アールいち、イコール、アールよんぶんの・アールさん」 |
| $H = \dfrac{I}{2\pi r}$ | 「エイチ・イコール、にパイアールぶんの・アイ」 |
| $H = nI$ | 「エイチ・イコール、エヌ・アイ」 |
| $\vec{B} = \mu\vec{H}$ | 「ビー・ベクトル・イコール、ミュー・エイチ・ベクトル」 |
| $\Phi = BS$ | 「ファイ・イコール、ビー・エス」 |
| $F = IBl\sin\theta$ | 「エフ・イコール、アイ・ビー・エル・サインシータ」 |
| $f = qvB\sin\theta$ | 「エフ・イコール、キュー・ブイ・ビー・サインシータ」 |
| $r = \dfrac{mv}{qB},\; T = \dfrac{2\pi m}{qB}$ | 「アール・イコール、キュービーぶんの・エムブイ」「ティー・イコール、キュービーぶんの・にパイエム」 |
| $V_H = E_y d = vBd$ | 「ブイ・エイチ・イコール、イーワイ・ディー、イコール、ブイ・ビー・ディー」 |
| $V = -N\dfrac{\Delta\Phi}{\Delta t}$ | 「ブイ・イコール、マイナス・エヌ・デルタティーぶんの・デルタファイ」 |
| $V = -L\dfrac{\Delta I}{\Delta t}$ | 「ブイ・イコール、マイナス・エル・デルタティーぶんの・デルタアイ」 |
| $V_2 = -M\dfrac{\Delta I_1}{\Delta t}$ | 「ブイに・イコール、マイナス・エム・デルタティーぶんの・デルタアイいち」 |
| $V = V_0\sin\omega t$ | 「ブイ・イコール、ブイゼロ・サイン・オメガティー」 |
| $V_e = \dfrac{1}{\sqrt{2}}V_0$ | 「ブイ・イー・イコール、ルートにぶんのいち・ブイゼロ」 |

---

## 3. 核心物理模型与公式深度推导（一模型一解，配齐板书 SVG）

> **说明**：本切片（教材 P.91–P.105 / 页码 90–104）全篇为概念与定律精讲页，**不含原教材编号例题与练习题（0 题）**。下面将本切片最具考场价值的 **8 大核心模型与未写全的隐藏推导**（含霍尔电压完整式、自感/互感系数公式、有效值功率推导等）逐一按日本考场规范补全。

---

### 核心模型 1（教材 P.91 / 页码 90）：電池の起電力と内部抵抗

#### 【教材原页内容与翻译】
> **日文原文**：  
> 電池の端子電圧を $V\text{ [V]}$、起電力を $E\text{ [V]}$、内部抵抗を $r\text{ [}\Omega\text{]}$、電流を $I\text{ [A]}$ とすると以下の関係があります：$V = E - rI$。
>
> **中文翻译**：  
> 设电池的路端电压为 $V\text{ [V]}$、电动势为 $E\text{ [V]}$、内阻为 $r\text{ [}\Omega\text{]}$、电流为 $I\text{ [A]}$，则满足关系式：$V = E - rI$。

#### 【考点与模型定位】
**闭合电路欧姆定律与 $V$-$I$ 特征图像法**（EJU 电路实验题高频考点：从 $V$-$I$ 直线的截距与斜率读取电池的 $E$ 和 $r$）。

#### 【多色矢量图解（SVG）】

<svg viewBox="0 0 420 240" width="420" height="240" xmlns="http://www.w3.org/2000/svg" style="background:#fafafa;border:1px solid #e5e7eb;border-radius:8px;">
  <defs>
    <marker id="arr-blk-007-1" markerWidth="7" markerHeight="7" refX="5" refY="3" orient="auto"><path d="M0,0 L0,6 L6,3 z" fill="#111827"/></marker>
    <marker id="arr-grn-007-1" markerWidth="7" markerHeight="7" refX="5" refY="3" orient="auto"><path d="M0,0 L0,6 L6,3 z" fill="#16a34a"/></marker>
    <marker id="arr-blue-007-1" markerWidth="7" markerHeight="7" refX="5" refY="3" orient="auto"><path d="M0,0 L0,6 L6,3 z" fill="#2563eb"/></marker>
  </defs>
  <!-- 左侧：V-I 图像 -->
  <text x="48" y="24" font-size="11" font-weight="bold" fill="#374151">端子電圧 V - 電流 I グラフ</text>
  <line x1="40" y1="190" x2="185" y2="190" stroke="#111827" stroke-width="1.5" marker-end="url(#arr-blk-007-1)"/>
  <line x1="40" y1="190" x2="40" y2="42" stroke="#111827" stroke-width="1.5" marker-end="url(#arr-blk-007-1)"/>
  <text x="180" y="206" font-size="11" fill="#111827">I [A]</text>
  <text x="18" y="48" font-size="11" fill="#111827">V</text>
  <text x="27" y="203" font-size="10" fill="#374151">O</text>
  <!-- 直线 V = E - rI -->
  <line x1="40" y1="68" x2="158" y2="190" stroke="#2563eb" stroke-width="2.2"/>
  <circle cx="40" cy="68" r="3.5" fill="#2563eb"/>
  <text x="47" y="72" font-size="11" font-weight="bold" fill="#2563eb">E (起電力)</text>
  <circle cx="158" cy="190" r="3.5" fill="#dc2626"/>
  <text x="148" y="179" font-size="11" fill="#dc2626">E / r</text>
  <text x="98" y="122" font-size="11" fill="#2563eb">傾き = -r</text>

  <!-- 分隔线 -->
  <line x1="210" y1="15" x2="210" y2="225" stroke="#d1d5db" stroke-dasharray="4,4"/>

  <!-- 右侧：等效电路 -->
  <text x="255" y="24" font-size="11" font-weight="bold" fill="#374151">内部抵抗を含む直流回路</text>
  <!-- 外回路导线 -->
  <polyline points="235,165 235,62 395,62 395,165" fill="none" stroke="#374151" stroke-width="1.8"/>
  <!-- 外电阻 R -->
  <rect x="292" y="52" width="46" height="20" fill="#fee2e2" stroke="#dc2626" stroke-width="1.6"/>
  <text x="303" y="45" font-size="11" font-weight="bold" fill="#dc2626">抵抗 R</text>
  <!-- 电流箭头 -->
  <line x1="235" y1="125" x2="235" y2="95" stroke="#16a34a" stroke-width="2" marker-end="url(#arr-grn-007-1)"/>
  <text x="242" y="114" font-size="11" font-weight="bold" fill="#16a34a">電流 I</text>

  <!-- 电池虚线框（含内阻 r 与起电力 E） -->
  <rect x="255" y="136" width="122" height="58" rx="4" fill="#eff6ff" stroke="#2563eb" stroke-width="1.3" stroke-dasharray="4,3"/>
  <line x1="235" y1="165" x2="270" y2="165" stroke="#374151" stroke-width="1.8"/>
  <!-- 内阻 r -->
  <rect x="270" y="157" width="34" height="16" fill="#fee2e2" stroke="#dc2626" stroke-width="1.4"/>
  <text x="266" y="150" font-size="10" fill="#dc2626">内部抵抗 r</text>
  <line x1="304" y1="165" x2="338" y2="165" stroke="#374151" stroke-width="1.8"/>
  <!-- 电池极板（左长正、右短负） -->
  <line x1="338" y1="150" x2="338" y2="180" stroke="#2563eb" stroke-width="2"/>
  <line x1="346" y1="157" x2="346" y2="173" stroke="#2563eb" stroke-width="3.2"/>
  <line x1="346" y1="165" x2="395" y2="165" stroke="#374151" stroke-width="1.8"/>
  <text x="328" y="191" font-size="10" fill="#2563eb">起電力 E</text>

  <!-- 端子电压 V 标注 -->
  <line x1="258" y1="210" x2="374" y2="210" stroke="#2563eb" stroke-width="1.4" marker-end="url(#arr-blue-007-1)"/>
  <text x="276" y="226" font-size="11" font-weight="bold" fill="#2563eb">端子電圧 V = E - rI</text>
</svg>

#### 【日本考场规范推导与板书步骤】
キルヒホッフの第 2 法則（閉回路の電圧降下の和＝起電力の和）より，外抵抗 $R$ を流れる電流を $I$ とすると，
$$E = RI + rI \implies RI = E - rI$$
ここで，電池の両端の電圧（端子電圧）は外抵抗にかかる電圧 $V = RI$ に等しいから，
$$V = E - rI$$

> 💡 讲师批注：提醒学生“电池是一个整体黑盒（图中蓝虚线框）”，电压表接在电池正负极两端测到的永远是**端子電圧 $V = E - rI$**，只有断路（$I = 0$）时才等于起電力 $E$！当电路外电阻 $R \to 0$（短路）时，$V = 0$，短路电流 $I_{\text{短}} = \dfrac{E}{r}$。

#### 【核心结论】
- **$V = E - rI$**；$V$-$I$ 图像纵截距 $= E$，斜率 $= -r$，横截距 $= \dfrac{E}{r}$。

---

### 核心模型 2（教材 P.92 / 页码 91）：ホイートストンブリッジ & コンデンサーを含む直流回路

#### 【教材原页内容与翻译】
> **日文原文**：  
> 各抵抗が $\dfrac{R_1}{R_2} = \dfrac{R_3}{R_4}$ を満たすとき，BD 間（回路のブリッジ部分）には電流が流れません。このような電気回路をホイートストンブリッジといいます。  
> $C\text{ [F]}$ の電気容量のコンデンサーと，$R\text{ [}\Omega\text{]}$ の抵抗と，$E\text{ [V]}$ の起電力で内部抵抗が無い電池と，スイッチを直列につないだ回路を考えます。
>
> **中文翻译**：  
> 当各电阻满足 $\dfrac{R_1}{R_2} = \dfrac{R_3}{R_4}$ 时，BD 间（电路的桥路部分）不流过电流，这种电路称为惠斯通电桥。  
> 考虑将电容为 $C\text{ [F]}$ 的电容器、电阻 $R\text{ [}\Omega\text{]}$、电动势为 $E\text{ [V]}$ 且无内阻的电池以及开关串联组成的直流电路。

#### 【考点与模型定位】
**电桥平衡的等电势判定法** $+$ **RC 直流电路的暂态（スイッチを閉じた直後）与稳态（十分時間が経過した後）分析**。

#### 【多色矢量图解（SVG）】

<svg viewBox="0 0 420 240" width="420" height="240" xmlns="http://www.w3.org/2000/svg" style="background:#fafafa;border:1px solid #e5e7eb;border-radius:8px;">
  <defs>
    <marker id="arr-grn-007-2" markerWidth="7" markerHeight="7" refX="5" refY="3" orient="auto"><path d="M0,0 L0,6 L6,3 z" fill="#16a34a"/></marker>
  </defs>
  <!-- 左侧：惠斯通电桥 -->
  <text x="30" y="22" font-size="11" font-weight="bold" fill="#374151">ホイートストンブリッジ</text>
  <!-- 菱形四边 -->
  <line x1="35" y1="115" x2="115" y2="55" stroke="#374151" stroke-width="1.8"/>
  <line x1="35" y1="115" x2="115" y2="175" stroke="#374151" stroke-width="1.8"/>
  <line x1="115" y1="55" x2="195" y2="115" stroke="#374151" stroke-width="1.8"/>
  <line x1="115" y1="175" x2="195" y2="115" stroke="#374151" stroke-width="1.8"/>
  <!-- 桥路 BD -->
  <line x1="115" y1="55" x2="115" y2="175" stroke="#2563eb" stroke-width="1.8" stroke-dasharray="4,3"/>
  <rect x="108" y="98" width="14" height="34" fill="#dbeafe" stroke="#2563eb" stroke-width="1.4"/>
  <text x="126" y="119" font-size="10" font-weight="bold" fill="#2563eb">I=0</text>
  <!-- 四个电阻标签 -->
  <text x="58" y="78" font-size="11" font-weight="bold" fill="#dc2626">R₁</text>
  <text x="58" y="160" font-size="11" font-weight="bold" fill="#dc2626">R₂</text>
  <text x="158" y="78" font-size="11" font-weight="bold" fill="#dc2626">R₃</text>
  <text x="158" y="160" font-size="11" font-weight="bold" fill="#dc2626">R₄</text>
  <!-- 节点字母 -->
  <text x="20" y="119" font-size="11" font-weight="bold" fill="#111827">A</text>
  <text x="111" y="48" font-size="11" font-weight="bold" fill="#111827">B</text>
  <text x="200" y="119" font-size="11" font-weight="bold" fill="#111827">C</text>
  <text x="111" y="190" font-size="11" font-weight="bold" fill="#111827">D</text>
  <!-- 电源回路 -->
  <polyline points="35,115 35,205 110,205" fill="none" stroke="#374151" stroke-width="1.5"/>
  <polyline points="195,115 195,205 120,205" fill="none" stroke="#374151" stroke-width="1.5"/>
  <line x1="110" y1="194" x2="110" y2="216" stroke="#2563eb" stroke-width="2"/>
  <line x1="118" y1="199" x2="118" y2="211" stroke="#2563eb" stroke-width="3"/>
  <text x="55" y="228" font-size="10" fill="#2563eb">平衡条件: V_B = V_D</text>

  <!-- 分隔线 -->
  <line x1="222" y1="15" x2="222" y2="225" stroke="#d1d5db" stroke-dasharray="4,4"/>

  <!-- 右侧：RC 直流回路 -->
  <text x="242" y="22" font-size="11" font-weight="bold" fill="#374151">RC 直流回路（過渡→定常）</text>
  <!-- 回路框 -->
  <polyline points="250,175 250,68 278,68" fill="none" stroke="#374151" stroke-width="1.8"/>
  <!-- 电阻 R -->
  <rect x="278" y="60" width="38" height="16" fill="#fee2e2" stroke="#dc2626" stroke-width="1.5"/>
  <text x="292" y="53" font-size="11" font-weight="bold" fill="#dc2626">R</text>
  <line x1="316" y1="68" x2="352" y2="68" stroke="#374151" stroke-width="1.8"/>
  <!-- 电容 C -->
  <line x1="352" y1="53" x2="352" y2="83" stroke="#2563eb" stroke-width="2.2"/>
  <line x1="362" y1="53" x2="362" y2="83" stroke="#2563eb" stroke-width="2.2"/>
  <text x="348" y="45" font-size="11" font-weight="bold" fill="#2563eb">C (Q, V)</text>
  <polyline points="362,68 395,68 395,175 340,175" fill="none" stroke="#374151" stroke-width="1.8"/>
  <!-- 电池 E -->
  <line x1="332" y1="162" x2="332" y2="188" stroke="#2563eb" stroke-width="2"/>
  <line x1="340" y1="168" x2="340" y2="182" stroke="#2563eb" stroke-width="3.2"/>
  <text x="328" y="156" font-size="11" font-weight="bold" fill="#2563eb">E</text>
  <!-- 开关 S -->
  <line x1="250" y1="175" x2="275" y2="175" stroke="#374151" stroke-width="1.8"/>
  <circle cx="277" cy="175" r="2.5" fill="#111827"/>
  <line x1="277" y1="175" x2="305" y2="162" stroke="#111827" stroke-width="1.8"/>
  <circle cx="307" cy="175" r="2.5" fill="#111827"/>
  <line x1="307" y1="175" x2="332" y2="175" stroke="#374151" stroke-width="1.8"/>
  <text x="285" y="192" font-size="10" fill="#374151">スイッチ S</text>
  <!-- 电流 I -->
  <line x1="250" y1="138" x2="250" y2="104" stroke="#16a34a" stroke-width="2" marker-end="url(#arr-grn-007-2)"/>
  <text x="256" y="124" font-size="11" font-weight="bold" fill="#16a34a">I</text>
  <!-- 标注 -->
  <text x="234" y="212" font-size="10" fill="#374151">直後(t=0): V=0, I=E/R</text>
  <text x="234" y="227" font-size="10" fill="#2563eb">十分後: I=0, V=E, Q=CE</text>
</svg>

#### 【日本考场规范推导与板书步骤】
1. **ホイートストンブリッジの平衡条件**：  
   BD 間に電流が流れないとき，B 点と D 点の電位は等しい（$V_B = V_D$）。また，分岐しないため $I_1 = I_3$，$I_2 = I_4$ が成り立つ。  
   したがって，AB 間と AD 間の電圧降下，および BC 間と DC 間の電圧降下はそれぞれ等しい：
   $$R_1 I_1 = R_2 I_2 \quad \cdots\text{①}, \qquad R_3 I_1 = R_4 I_2 \quad \cdots\text{②}$$
   ① $\div$ ② より $I_1, I_2$ を消去すると，
   $$\frac{R_1}{R_3} = \frac{R_2}{R_4} \iff \frac{R_1}{R_2} = \frac{R_3}{R_4}$$
2. **RC 直流回路のキルヒホッフの式**：  
   任意の時刻において $Q = CV$ であり，閉回路について：
   $$E = RI + V = RI + \frac{Q}{C}$$
   - **スイッチを閉じた直後**：$Q = 0 \implies I = \dfrac{E}{R}$。
   - **十分時間が経過した後（定常状態）**：$I = 0 \implies V = E,\; Q = CE$。

> 💡 讲师批注：EJU 经常把惠斯通电桥画成歪斜的电路（非标准菱形）来迷惑学生，教学生只需抓住节点 A、B、C、D 的拓扑连接关系并检验 $R_1 R_4 = R_2 R_3$ 即可秒杀！

#### 【核心结论】
- **电桥平衡**：$\dfrac{R_1}{R_2} = \dfrac{R_3}{R_4}$（$I_{BD} = 0$）；**RC 稳态**：$I = 0,\; V = E,\; Q = CE$。

---

### 核心模型 3（教材 P.95–96 / 页码 94–95）：電流がつくる磁場 & 電流が磁場から受ける力

#### 【教材原页内容与翻译】
> **日文原文**：  
> 直線電流がつくる磁場 $H = \dfrac{I}{2\pi r}$，円形電流がつくる磁場 $H = \dfrac{I}{2r}$，ソレノイドがつくる磁場 $H = nI$。  
> 一様な磁場の中に置かれた導線を流れる電流が受ける力の大きさは $F = \mu IHl\sin\theta = IBl\sin\theta$。
>
> **中文翻译**：  
> 直线电流产生的磁场 $H = \dfrac{I}{2\pi r}$，环形电流中心磁场 $H = \dfrac{I}{2r}$，通电螺线管内部磁场 $H = nI$。  
> 置于匀强磁场中的通电导线所受安培力大小为 $F = \mu IHl\sin\theta = IBl\sin\theta$。

#### 【考点与模型定位】
**三大基本电流磁场公式（右ねじの法則）** $+$ **安培力公式与弗莱明左手定则（フレミングの左手の法則）**。

#### 【多色矢量图解（SVG）】

<svg viewBox="0 0 420 245" width="420" height="245" xmlns="http://www.w3.org/2000/svg" style="background:#fafafa;border:1px solid #e5e7eb;border-radius:8px;">
  <defs>
    <marker id="arr-blue-007-3" markerWidth="7" markerHeight="7" refX="5" refY="3" orient="auto"><path d="M0,0 L0,6 L6,3 z" fill="#2563eb"/></marker>
    <marker id="arr-grn-007-3" markerWidth="7" markerHeight="7" refX="5" refY="3" orient="auto"><path d="M0,0 L0,6 L6,3 z" fill="#16a34a"/></marker>
    <marker id="arr-red-007-3" markerWidth="7" markerHeight="7" refX="5" refY="3" orient="auto"><path d="M0,0 L0,6 L6,3 z" fill="#dc2626"/></marker>
  </defs>
  <!-- 左半：直线电流右螺旋定则 -->
  <text x="26" y="22" font-size="11" font-weight="bold" fill="#374151">直線電流の磁場 (右ねじの法則)</text>
  <!-- 垂直导线 -->
  <line x1="100" y1="42" x2="100" y2="195" stroke="#16a34a" stroke-width="3" marker-end="url(#arr-grn-007-3)"/>
  <text x="108" y="60" font-size="11" font-weight="bold" fill="#16a34a">電流 I (下向き)</text>
  <!-- 同心椭圆磁感线（俯视顺时针） -->
  <ellipse cx="100" cy="118" rx="68" ry="22" fill="none" stroke="#2563eb" stroke-width="1.6"/>
  <ellipse cx="100" cy="118" rx="40" ry="13" fill="none" stroke="#2563eb" stroke-width="1.2" stroke-dasharray="4,2"/>
  <!-- 切线方向箭头（顺时针，前方指向左） -->
  <line x1="120" y1="139" x2="90" y2="140" stroke="#2563eb" stroke-width="2" marker-end="url(#arr-blue-007-3)"/>
  <line x1="100" y1="118" x2="165" y2="118" stroke="#6b7280" stroke-dasharray="3,2"/>
  <text x="132" y="114" font-size="10" fill="#374151">r</text>
  <text x="155" y="142" font-size="11" font-weight="bold" fill="#2563eb">H (時計回り)</text>
  <text x="52" y="220" font-size="11" font-weight="bold" fill="#2563eb">H = I / (2πr)</text>

  <!-- 分隔线 -->
  <line x1="210" y1="15" x2="210" y2="230" stroke="#d1d5db" stroke-dasharray="4,4"/>

  <!-- 右半：安培力立体图 -->
  <text x="235" y="22" font-size="11" font-weight="bold" fill="#374151">電流が磁場から受ける力 (左手)</text>
  <!-- 磁场线 B (斜向右上，从N到S) -->
  <line x1="230" y1="175" x2="365" y2="115" stroke="#2563eb" stroke-width="1.4" marker-end="url(#arr-blue-007-3)"/>
  <line x1="242" y1="190" x2="377" y2="130" stroke="#2563eb" stroke-width="1.4" marker-end="url(#arr-blue-007-3)"/>
  <line x1="254" y1="205" x2="389" y2="145" stroke="#2563eb" stroke-width="1.4" marker-end="url(#arr-blue-007-3)"/>
  <text x="366" y="110" font-size="11" font-weight="bold" fill="#2563eb">B = μH</text>
  <text x="225" y="198" font-size="10" fill="#6b7280">N極</text>
  <text x="385" y="138" font-size="10" fill="#6b7280">S極</text>
  <!-- 导线电流 I (斜向右下，与B成角theta) -->
  <line x1="270" y1="126" x2="352" y2="188" stroke="#16a34a" stroke-width="3" marker-end="url(#arr-grn-007-3)"/>
  <text x="342" y="200" font-size="11" font-weight="bold" fill="#16a34a">I (長さ l)</text>
  <!-- 夹角 theta -->
  <path d="M 326 151 A 20 20 0 0 1 324 166" fill="none" stroke="#dc2626" stroke-width="1.4"/>
  <text x="331" y="164" font-size="10" fill="#dc2626">θ</text>
  <!-- 安培力 F (竖直向上) -->
  <line x1="308" y1="155" x2="308" y2="62" stroke="#dc2626" stroke-width="2.5" marker-end="url(#arr-red-007-3)"/>
  <text x="315" y="74" font-size="11" font-weight="bold" fill="#dc2626">F = IBl sinθ</text>
  <text x="230" y="226" font-size="10" fill="#dc2626">■ 红：安培力 F</text>
  <text x="315" y="226" font-size="10" fill="#2563eb">■ 蓝：磁束密度 B</text>
</svg>

#### 【日本考场规范推导与板书步骤】
1. 磁場の強さ $H\text{ [A/m]}$ と磁束密度 $B\text{ [T]}$ の関係 $\vec{B} = \mu\vec{H}$ より，
   $$F = \mu I H l \sin\theta = I B l \sin\theta$$
2. 力の向きは**フレミングの左手の法則**（中指：電流 $I$，人差し指：磁場 $B$，親指：力 $F$）で定める。

> 💡 讲师批注：**教材 P.96（页码 95）表述勘误提醒**：正文第一句先假设导线与磁场「垂直（$\theta = 90^\circ$）」，但下方公式直接给出了带 $\sin\theta$ 的一般式，未在正文中定义 $\theta$。授课时务必补充：$\theta$ 是**电流方向与磁场方向的夹角**；垂直时 $\sin 90^\circ = 1 \implies F = IBl$，平行时 $\sin 0^\circ = 0 \implies F = 0$。

#### 【核心结论】
- 三种电流磁场：$H_{\text{直}} = \dfrac{I}{2\pi r}$，$H_{\text{円}} = \dfrac{I}{2r}$，$H_{\text{ソ}} = nI$；安培力 **$F = IBl\sin\theta$**。

---

### 核心模型 4（教材 P.97 / 页码 96）：平行な電流の間にはたらく力

#### 【教材原页内容与翻译】
> **日文原文**：  
> 平行な電流の間にはたらく力は $F = \dfrac{\mu_0 I_A I_B}{2\pi r}l$。同じ向きの平行な電流は引き合い，反対向きの平行な電流は反発し合います。
>
> **中文翻译**：  
> 平行电流之间相互作用的力为 $F = \dfrac{\mu_0 I_A I_B}{2\pi r}l$。同向平行电流相互吸引，反向平行电流相互排斥。

#### 【考点与模型定位】
**电流磁场 $+$ 安培力两步叠加推导**（同时检验**右螺旋定则**与**弗莱明左手定则**以及**牛顿第三定律**）。

#### 【多色矢量图解（SVG）】

<svg viewBox="0 0 420 230" width="420" height="230" xmlns="http://www.w3.org/2000/svg" style="background:#fafafa;border:1px solid #e5e7eb;border-radius:8px;">
  <defs>
    <marker id="arr-grn-007-4" markerWidth="7" markerHeight="7" refX="5" refY="3" orient="auto"><path d="M0,0 L0,6 L6,3 z" fill="#16a34a"/></marker>
    <marker id="arr-red-007-4" markerWidth="7" markerHeight="7" refX="5" refY="3" orient="auto"><path d="M0,0 L0,6 L6,3 z" fill="#dc2626"/></marker>
  </defs>
  <!-- 左半：同向相吸 -->
  <text x="40" y="22" font-size="11" font-weight="bold" fill="#374151">同じ向き：引き合う（引力）</text>
  <line x1="65" y1="185" x2="65" y2="48" stroke="#16a34a" stroke-width="2.5" marker-end="url(#arr-grn-007-4)"/>
  <text x="44" y="60" font-size="11" font-weight="bold" fill="#16a34a">I_A</text>
  <line x1="150" y1="185" x2="150" y2="48" stroke="#16a34a" stroke-width="2.5" marker-end="url(#arr-grn-007-4)"/>
  <text x="157" y="60" font-size="11" font-weight="bold" fill="#16a34a">I_B</text>
  <!-- B_A 在 B 处垂直纸面向里 (×) -->
  <circle cx="150" cy="82" r="7" fill="#eff6ff" stroke="#2563eb" stroke-width="1.3"/>
  <line x1="146" y1="78" x2="154" y2="86" stroke="#2563eb" stroke-width="1.3"/>
  <line x1="154" y1="78" x2="146" y2="86" stroke="#2563eb" stroke-width="1.3"/>
  <text x="160" y="86" font-size="10" fill="#2563eb">B_A (紙面裏)</text>
  <!-- 相吸力箭头 -->
  <line x1="65" y1="125" x2="100" y2="125" stroke="#dc2626" stroke-width="2.2" marker-end="url(#arr-red-007-4)"/>
  <text x="78" y="118" font-size="10" font-weight="bold" fill="#dc2626">F</text>
  <line x1="150" y1="125" x2="115" y2="125" stroke="#dc2626" stroke-width="2.2" marker-end="url(#arr-red-007-4)"/>
  <text x="128" y="118" font-size="10" font-weight="bold" fill="#dc2626">F</text>
  <!-- 间距 r -->
  <line x1="65" y1="196" x2="150" y2="196" stroke="#6b7280" stroke-dasharray="3,2"/>
  <text x="103" y="210" font-size="11" fill="#374151">r</text>

  <!-- 分隔线 -->
  <line x1="215" y1="15" x2="215" y2="215" stroke="#d1d5db" stroke-dasharray="4,4"/>

  <!-- 右半：反向相斥 -->
  <text x="242" y="22" font-size="11" font-weight="bold" fill="#374151">反対向き：反発し合う（斥力）</text>
  <line x1="280" y1="185" x2="280" y2="48" stroke="#16a34a" stroke-width="2.5" marker-end="url(#arr-grn-007-4)"/>
  <text x="259" y="60" font-size="11" font-weight="bold" fill="#16a34a">I_A</text>
  <line x1="355" y1="48" x2="355" y2="185" stroke="#16a34a" stroke-width="2.5" marker-end="url(#arr-grn-007-4)"/>
  <text x="362" y="176" font-size="11" font-weight="bold" fill="#16a34a">I_B</text>
  <!-- B_A 在 B 处仍向里 (×) -->
  <circle cx="355" cy="82" r="7" fill="#eff6ff" stroke="#2563eb" stroke-width="1.3"/>
  <line x1="351" y1="78" x2="359" y2="86" stroke="#2563eb" stroke-width="1.3"/>
  <line x1="359" y1="78" x2="351" y2="86" stroke="#2563eb" stroke-width="1.3"/>
  <text x="365" y="86" font-size="10" fill="#2563eb">B_A (裏)</text>
  <!-- 相斥力箭头 -->
  <line x1="280" y1="125" x2="245" y2="125" stroke="#dc2626" stroke-width="2.2" marker-end="url(#arr-red-007-4)"/>
  <text x="252" y="118" font-size="10" font-weight="bold" fill="#dc2626">F</text>
  <line x1="355" y1="125" x2="390" y2="125" stroke="#dc2626" stroke-width="2.2" marker-end="url(#arr-red-007-4)"/>
  <text x="372" y="118" font-size="10" font-weight="bold" fill="#dc2626">F</text>
  <text x="255" y="212" font-size="11" font-weight="bold" fill="#dc2626">F = (μ₀ I_A I_B / 2πr) l</text>
</svg>

#### 【日本考场规范推导与板书步骤】
1. まず，導線 A の電流 $I_A$ が距離 $r$ 離れた導線 B の位置につくる磁場の強さ $H_A$ および磁束密度 $B_A$ は，
   $$H_A = \frac{I_A}{2\pi r} \implies B_A = \mu_0 H_A = \frac{\mu_0 I_A}{2\pi r}$$
   向きは右ねじの法則より，紙面の表から裏へ向かう向き（$\otimes$）である。
2. 次に，この磁束密度 $B_A$ の中で導線 B（長さ $l$，電流 $I_B$）が受ける力 $F$ は，$B_A$ と $I_B$ が垂直であるから，
   $$F = I_B B_A l = \frac{\mu_0 I_A I_B}{2\pi r}l$$
3. フレミングの左手の法則より，$I_A$ と $I_B$ が同向きのとき導線 B は左向き（A に近づく向き）の力を受け，作用・反作用の法則より導線 A は右向きの同じ大きさの力を受ける（引き合う）。

> 💡 讲师批注：切记“同向相吸、反向相斥”与静电荷“同性相斥、异性相吸”**正好相反**！这是 EJU 选择题最爱挖的坑。

#### 【核心结论】
- **$F = \dfrac{\mu_0 I_A I_B}{2\pi r}l$**（同向引き合う，反対向き反発し合う）。

---

### 核心模型 5（教材 P.99 / 页码 98）：ローレンツ力と磁場中の荷電粒子の運動

#### 【教材原页内容与翻译】
> **日文原文**：  
> 磁束密度 $B\text{ [T]}$ の磁場の中を電気量 $q\text{ [C]}$ の荷電粒子が速度 $v\text{ [m/s]}$ で進み，磁場と速度のなす角が $\theta$ のとき，ローレンツ力は $f = qvB\sin\theta$。  
> 磁場中の荷電粒子の等速円運動：$r = \dfrac{mv}{qB}$，$T = \dfrac{2\pi m}{qB}$。
>
> **中文翻译**：  
> 电荷量为 $q\text{ [C]}$ 的带电粒子以速度 $v\text{ [m/s]}$ 在磁感应强度为 $B\text{ [T]}$ 的磁场中运动，速度与磁场夹角为 $\theta$ 时，所受洛伦兹力为 $f = qvB\sin\theta$。  
> 垂直射入匀强磁场时做匀速圆周运动，半径 $r = \dfrac{mv}{qB}$，周期 $T = \dfrac{2\pi m}{qB}$。

#### 【考点与模型定位】
**洛伦兹力提供向心力（匀速圆周运动）** $+$ **斜入射螺旋运动（らせん運動）**（回旋加速器、质谱仪的核心基础）。

#### 【多色矢量图解（SVG）】

<svg viewBox="0 0 420 245" width="420" height="245" xmlns="http://www.w3.org/2000/svg" style="background:#fafafa;border:1px solid #e5e7eb;border-radius:8px;">
  <defs>
    <marker id="arr-red-007-5" markerWidth="7" markerHeight="7" refX="5" refY="3" orient="auto"><path d="M0,0 L0,6 L6,3 z" fill="#dc2626"/></marker>
    <marker id="arr-blk-007-5" markerWidth="7" markerHeight="7" refX="5" refY="3" orient="auto"><path d="M0,0 L0,6 L6,3 z" fill="#111827"/></marker>
  </defs>
  <!-- 匀强磁场背景 ⊗ -->
  <text x="16" y="22" font-size="11" font-weight="bold" fill="#374151">一様磁場 B (紙面表→裏 ⊗) 中の正電荷 +q の等速円運動</text>
  <g stroke="#93c5fd" stroke-width="1.2">
    <circle cx="45" cy="55" r="5" fill="none"/><line x1="42" y1="52" x2="48" y2="58"/><line x1="48" y1="52" x2="42" y2="58"/>
    <circle cx="45" cy="125" r="5" fill="none"/><line x1="42" y1="122" x2="48" y2="128"/><line x1="48" y1="122" x2="42" y2="128"/>
    <circle cx="45" cy="195" r="5" fill="none"/><line x1="42" y1="192" x2="48" y2="198"/><line x1="48" y1="192" x2="42" y2="198"/>
    <circle cx="255" cy="55" r="5" fill="none"/><line x1="252" y1="52" x2="258" y2="58"/><line x1="258" y1="52" x2="252" y2="58"/>
    <circle cx="255" cy="195" r="5" fill="none"/><line x1="252" y1="192" x2="258" y2="198"/><line x1="258" y1="192" x2="252" y2="198"/>
  </g>
  <!-- 圆周轨道 -->
  <circle cx="150" cy="130" r="72" fill="none" stroke="#111827" stroke-width="1.8"/>
  <circle cx="150" cy="130" r="3" fill="#111827"/>
  <text x="155" y="134" font-size="11" fill="#374151">O</text>
  <!-- 半径 r -->
  <line x1="150" y1="130" x2="222" y2="130" stroke="#6b7280" stroke-dasharray="4,3"/>
  <text x="184" y="124" font-size="11" font-style="italic" fill="#374151">r</text>

  <!-- 底部粒子 +q（逆时针旋转：向右运动，洛伦兹力向上指向圆心） -->
  <circle cx="150" cy="202" r="8" fill="#fee2e2" stroke="#dc2626" stroke-width="1.5"/>
  <text x="143" y="206" font-size="10" font-weight="bold" fill="#dc2626">+q</text>
  <!-- 速度 v (黑虚线向右) -->
  <line x1="158" y1="202" x2="215" y2="202" stroke="#111827" stroke-width="2" stroke-dasharray="5,3" marker-end="url(#arr-blk-007-5)"/>
  <text x="218" y="206" font-size="11" font-weight="bold" fill="#111827">v</text>
  <!-- 洛伦兹力 f (红实线指向圆心) -->
  <line x1="150" y1="194" x2="150" y2="148" stroke="#dc2626" stroke-width="2.2" marker-end="url(#arr-red-007-5)"/>
  <text x="106" y="176" font-size="11" font-weight="bold" fill="#dc2626">f = qvB</text>

  <!-- 右侧粒子位置 -->
  <circle cx="222" cy="130" r="6" fill="#fee2e2" stroke="#dc2626" stroke-width="1.4"/>
  <line x1="222" y1="124" x2="222" y2="75" stroke="#111827" stroke-width="1.8" stroke-dasharray="5,3" marker-end="url(#arr-blk-007-5)"/>
  <text x="228" y="88" font-size="11" fill="#111827">v</text>
  <line x1="216" y1="130" x2="174" y2="130" stroke="#dc2626" stroke-width="2" marker-end="url(#arr-red-007-5)"/>

  <!-- 右侧公式卡片 -->
  <rect x="275" y="48" width="132" height="162" rx="6" fill="#ffffff" stroke="#d1d5db" stroke-width="1.2"/>
  <text x="285" y="70" font-size="11" font-weight="bold" fill="#111827">中心向き運動方程式</text>
  <text x="285" y="92" font-size="11" fill="#dc2626">m v² / r = qvB</text>
  <text x="285" y="120" font-size="11" font-weight="bold" fill="#2563eb">r = mv / (qB)</text>
  <text x="285" y="146" font-size="11" font-weight="bold" fill="#2563eb">T = 2πm / (qB)</text>
  <text x="285" y="174" font-size="10" fill="#dc2626">■ 红：ローレンツ力</text>
  <text x="285" y="190" font-size="10" fill="#111827">--- 黑虚：速度 v</text>
  <text x="285" y="204" font-size="9.5" fill="#4b5563">※ 負電荷は逆回転</text>
</svg>

#### 【日本考场规范推导与板书步骤】
磁場と垂直に速さ $v$ で入射した質量 $m$，電気量 $q\ (>0)$ の荷電粒子は，常に速度に垂直な大きさ $f = qvB$ のローレンツ力を受ける。この力は仕事をしないため速さ $v$ は一定であり，粒子は半径 $r$ の等速円運動を行う。  
中心方向の運動方程式より，
$$m\frac{v^2}{r} = qvB \implies r = \frac{mv}{qB}$$
また，1 回転にかかる周期 $T$ は，
$$T = \frac{2\pi r}{v} = \frac{2\pi}{v} \cdot \frac{mv}{qB} = \frac{2\pi m}{qB}$$

> 💡 讲师批注：**教材 P.99（页码 98）配图说明**：原书下方配图实际画的是速度 $\vec{v}$ 与磁场 $\vec{B}$ 成斜角 $\theta$ 时的**螺旋运动（らせん運動）**，此时垂直分量 $v_\perp = v\sin\theta$ 决定圆周半径 $r = \dfrac{mv\sin\theta}{qB}$，平行分量 $v_\parallel = v\cos\theta$ 决定沿磁场方向的匀速直线推进（螺距 $L = v_\parallel T$），周期 $T = \dfrac{2\pi m}{qB}$ 仍不变！另外对负电荷（如电子 $-e$），用左手定则时**中指必须指向运动方向的反方向**！

#### 【核心结论】
- **$r = \dfrac{mv}{qB}$**，**$T = \dfrac{2\pi m}{qB}$**（周期与速率 $v$、轨道半径 $r$ 均无关）。

---

### 核心模型 6（教材 P.100 / 页码 99）：ホール効果（霍尔效应）

#### 【教材原页内容与翻译】
> **日文原文**：  
> 電流が流れている物体に磁場を掛けると，キャリアがローレンツ力を受け，物体の端に移動し，物体内に電位差が生じます。この現象をホール効果といいます。  
> 物体の $z$ 軸方向の厚さを $t\text{ [m]}$，$y$ 軸方向の大きさを $d\text{ [m]}$，自由電子の電気量を $-e\text{ [C]}$，速さを $v\text{ [m/s]}$，数密度を $n\text{ [個/m}^3\text{]}$，$y$ 軸方向の電場を $E_y\text{ [V/m]}$，ホール電圧を $V_H\text{ [V]}$ とすると，$V_H = E_y d = vBd$。
>
> **中文翻译**：  
> 给通有电流的导体施加磁场时，载流子受洛伦兹力向导体侧面偏转，从而在导体内部产生电势差，此现象称为霍尔效应。  
> 设导体沿 $z$ 轴厚度为 $t\text{ [m]}$，沿 $y$ 轴宽度为 $d\text{ [m]}$，自由电子电荷量为 $-e\text{ [C]}$，定向移动速率为 $v\text{ [m/s]}$，数密度为 $n\text{ [个/m}^3\text{]}$，横向电场为 $E_y\text{ [V/m]}$，霍尔电压为 $V_H\text{ [V]}$，则有 $V_H = E_y d = vBd$。

#### 【考点与模型定位】
**洛伦兹力与静电力平衡模型** $+$ **载流子电性判定**（区分自由电子与空穴/正电荷载流子，EJU 物理压轴大题超级常客）。

#### 【多色矢量图解（SVG）】

<svg viewBox="0 0 420 250" width="420" height="250" xmlns="http://www.w3.org/2000/svg" style="background:#fafafa;border:1px solid #e5e7eb;border-radius:8px;">
  <defs>
    <marker id="arr-blue-007-6" markerWidth="7" markerHeight="7" refX="5" refY="3" orient="auto"><path d="M0,0 L0,6 L6,3 z" fill="#2563eb"/></marker>
    <marker id="arr-grn-007-6" markerWidth="7" markerHeight="7" refX="5" refY="3" orient="auto"><path d="M0,0 L0,6 L6,3 z" fill="#16a34a"/></marker>
    <marker id="arr-red-007-6" markerWidth="7" markerHeight="7" refX="5" refY="3" orient="auto"><path d="M0,0 L0,6 L6,3 z" fill="#dc2626"/></marker>
    <marker id="arr-blk-007-6" markerWidth="7" markerHeight="7" refX="5" refY="3" orient="auto"><path d="M0,0 L0,6 L6,3 z" fill="#111827"/></marker>
  </defs>
  <text x="18" y="22" font-size="11" font-weight="bold" fill="#374151">ホール効果（俯視図：自由電子 -e がキャリアの場合）</text>
  <!-- 导体板矩形（x向右，y向上，B垂直纸面向外⊙） -->
  <rect x="70" y="65" width="230" height="110" fill="#f3f4f6" stroke="#374151" stroke-width="1.8"/>
  <!-- Q面（上方，+y）与 P面（下方，-y） -->
  <text x="150" y="57" font-size="11" font-weight="bold" fill="#dc2626">Q 面 (+ + + + + 高電位)</text>
  <text x="150" y="191" font-size="11" font-weight="bold" fill="#2563eb">P 面 (- - - - - 低電位)</text>
  <!-- 宽度 d 标注 -->
  <line x1="315" y1="65" x2="315" y2="175" stroke="#6b7280" stroke-dasharray="3,2"/>
  <text x="321" y="124" font-size="11" font-style="italic" fill="#374151">d (y方向)</text>

  <!-- 磁场 B 垂直纸面向外 ⊙ (+z) -->
  <circle cx="95" cy="90" r="7" fill="#eff6ff" stroke="#2563eb" stroke-width="1.4"/>
  <circle cx="95" cy="90" r="2" fill="#2563eb"/>
  <text x="106" y="94" font-size="11" font-weight="bold" fill="#2563eb">B (+z 紙面表)</text>

  <!-- 电流 I 向右 (+x) -->
  <line x1="20" y1="120" x2="66" y2="120" stroke="#16a34a" stroke-width="2.5" marker-end="url(#arr-grn-007-6)"/>
  <text x="22" y="111" font-size="11" font-weight="bold" fill="#16a34a">電流 I (+x)</text>

  <!-- 自由电子 -e 及其受力 -->
  <circle cx="205" cy="120" r="8" fill="#dbeafe" stroke="#1e40af" stroke-width="1.5"/>
  <text x="199" y="124" font-size="11" font-weight="bold" fill="#1e3a8a">-e</text>
  <!-- 电子速度 v 向左 (-x) -->
  <line x1="197" y1="120" x2="145" y2="120" stroke="#111827" stroke-width="2" stroke-dasharray="5,3" marker-end="url(#arr-blk-007-6)"/>
  <text x="150" y="112" font-size="11" font-weight="bold" fill="#111827">v (-x)</text>
  <!-- 洛伦兹力 f_L 向下 (-y 指向 P 面) -->
  <line x1="205" y1="128" x2="205" y2="168" stroke="#dc2626" stroke-width="2.2" marker-end="url(#arr-red-007-6)"/>
  <text x="212" y="160" font-size="11" font-weight="bold" fill="#dc2626">f_L = evB</text>
  <!-- 静电力 f_E 向上 (+y 指向 Q 面) -->
  <line x1="205" y1="112" x2="205" y2="72" stroke="#2563eb" stroke-width="2.2" marker-end="url(#arr-blue-007-6)"/>
  <text x="212" y="88" font-size="11" font-weight="bold" fill="#2563eb">f_E = eE_y</text>

  <!-- 电场 E_y 方向 (Q→P 向下) -->
  <line x1="278" y1="78" x2="278" y2="160" stroke="#2563eb" stroke-width="1.4" stroke-dasharray="4,3" marker-end="url(#arr-blue-007-6)"/>
  <text x="283" y="124" font-size="10" fill="#2563eb">E_y</text>

  <!-- 底部公式 -->
  <text x="22" y="218" font-size="11" font-weight="bold" fill="#111827">定常状態：eE_y = evB  ⇒  V_H = E_y d = vBd = IB / (ent)</text>
  <text x="22" y="236" font-size="10" fill="#dc2626">■ 红：ローレンツ力　■ 蓝：静電気力/磁場　■ 绿：電流　--- 黑虚：電子速度</text>
</svg>

#### 【日本考场规范推导与板书步骤】
1. **定常状態の力のつりあい**：  
   $+x$ 方向に電流 $I$ が流れるとき，自由電子（$-e$）は $-x$ 方向に速さ $v$ で移動する。フレミングの左手の法則より，自由電子は $-y$ 方向（P 面側）へ大きさ $evB$ のローレンツ力を受ける。その結果，P 面が負，Q 面が正に帯電し，Q 面から P 面へ向かう電場 $E_y$ が生じる。  
   定常状態では自由電子が受ける静電気力 $eE_y$ とローレンツ力 $evB$ がつりあうから，
   $$eE_y = evB \implies E_y = vB$$
   一様な電場における電位差の式 $V = Ed$ より，ホール電圧 $V_H$ は，
   $$V_H = E_y d = vBd$$
2. **電流 $I$ を用いた表式（教材未写出但 EJU 必考的延伸步骤）**：  
   断面積 $S = dt$ を流れる電流は $I = envS = envdt$ であるから，$v = \dfrac{I}{endt}$ を代入すると，
   $$V_H = \frac{I}{endt} \cdot Bd = \frac{IB}{ent}$$

> 💡 讲师批注：教材 P.100 正文专门定义了厚度 $t$ 和数密度 $n$，却在 $V_H = vBd$ 处戛然而止！讲课时务必补出 $I = envdt \implies V_H = \dfrac{IB}{ent}$：注意 **$d$ 被完美约掉了**，霍尔电压与厚度 $t$ 成反比！另外顺带提醒：如果载流子是正电荷（p 型半导体的空穴），速度方向为 $+x$，所受洛伦兹力仍指向 **$-y$（P 面）**，因此 **P 面带正电、Q 面带负电**——通过测量 P、Q 两面谁电势高，就能判断半导体是 n 型还是 p 型！

#### 【核心结论】
- **$V_H = E_y d = vBd = \dfrac{IB}{ent}$**；自由电子为载流子时 $V_Q > V_P$，正电荷为载流子时 $V_P > V_Q$。

---

### 核心模型 7（教材 P.101–103 / 页码 100–102）：電磁誘導・自己誘導・相互誘導

#### 【教材原页内容与翻译】
> **日文原文**：  
> ファラデーの電磁誘導の法則：$V = -N\dfrac{\Delta\Phi}{\Delta t}$。  
> 自己誘導：長さ $l\text{ [m]}$，断面積 $S\text{ [m}^2\text{]}$，単位長さ当たりの巻き数 $n\text{ [回/m]}$，巻き数 $N(=nl)$，透磁率 $\mu\text{ [N/A}^2\text{]}$ の鉄心入りコイルについて，$V = -L\dfrac{\Delta I}{\Delta t}$。  
> 相互誘導：1 次コイル $L_1$（$n_1$），2 次コイル $L_2$（$n_2$），共通の断面積 $S$・透磁率 $\mu$ について，$V_2 = -M\dfrac{\Delta I_1}{\Delta t}$。
>
> **中文翻译**：  
> 法拉第电磁感应定律：$V = -N\dfrac{\Delta\Phi}{\Delta t}$。  
> 自感：长度 $l$、截面积 $S$、单位长度匝数 $n$、总匝数 $N = nl$、铁芯磁导率 $\mu$ 的螺线管，$V = -L\dfrac{\Delta I}{\Delta t}$。  
> 互感：原线圈 $L_1$（$n_1$）、副线圈 $L_2$（$n_2$），共同截面积 $S$、磁导率 $\mu$，$V_2 = -M\dfrac{\Delta I_1}{\Delta t}$。

#### 【考点与模型定位】
**楞次定律方向判定** $+$ **法拉第定律推导长直螺线管自感系数 $L$ 与互感系数 $M$**（教材仅列参数与结果，考场常要求完整推导 $L = \mu n^2 Sl$）。

#### 【多色矢量图解（SVG）】

<svg viewBox="0 0 420 245" width="420" height="245" xmlns="http://www.w3.org/2000/svg" style="background:#fafafa;border:1px solid #e5e7eb;border-radius:8px;">
  <defs>
    <marker id="arr-blue-007-7" markerWidth="7" markerHeight="7" refX="5" refY="3" orient="auto"><path d="M0,0 L0,6 L6,3 z" fill="#2563eb"/></marker>
    <marker id="arr-grn-007-7" markerWidth="7" markerHeight="7" refX="5" refY="3" orient="auto"><path d="M0,0 L0,6 L6,3 z" fill="#16a34a"/></marker>
    <marker id="arr-blk-007-7" markerWidth="7" markerHeight="7" refX="5" refY="3" orient="auto"><path d="M0,0 L0,6 L6,3 z" fill="#111827"/></marker>
  </defs>
  <!-- 左半：楞次定律（N极靠近） -->
  <text x="20" y="22" font-size="11" font-weight="bold" fill="#374151">レンツの法則 (N極を近づける)</text>
  <!-- 条形磁铁 -->
  <rect x="20" y="88" width="42" height="26" fill="#9ca3af" stroke="#374151" stroke-width="1.3"/>
  <rect x="62" y="88" width="32" height="26" fill="#fca5a5" stroke="#dc2626" stroke-width="1.3"/>
  <text x="36" y="105" font-size="11" font-weight="bold" fill="#ffffff">S</text>
  <text x="73" y="105" font-size="11" font-weight="bold" fill="#991b1b">N</text>
  <!-- 运动方向 v -->
  <line x1="42" y1="126" x2="88" y2="126" stroke="#111827" stroke-width="2" stroke-dasharray="5,3" marker-end="url(#arr-blk-007-7)"/>
  <text x="54" y="140" font-size="10" fill="#111827">近づく</text>
  <!-- 线圈 -->
  <ellipse cx="132" cy="101" rx="8" ry="28" fill="none" stroke="#374151" stroke-width="1.8"/>
  <ellipse cx="148" cy="101" rx="8" ry="28" fill="none" stroke="#374151" stroke-width="1.8"/>
  <ellipse cx="164" cy="101" rx="8" ry="28" fill="none" stroke="#374151" stroke-width="1.8"/>
  <ellipse cx="180" cy="101" rx="8" ry="28" fill="none" stroke="#374151" stroke-width="1.8"/>
  <!-- 感应磁场（向左抵抗原磁场增加） -->
  <line x1="175" y1="101" x2="112" y2="101" stroke="#2563eb" stroke-width="2" marker-end="url(#arr-blue-007-7)"/>
  <text x="115" y="65" font-size="10" font-weight="bold" fill="#2563eb">妨げる磁場 B' (左向き)</text>
  <!-- 感应电流方向 -->
  <line x1="140" y1="120" x2="140" y2="85" stroke="#16a34a" stroke-width="2" marker-end="url(#arr-grn-007-7)"/>
  <text x="108" y="160" font-size="10" font-weight="bold" fill="#16a34a">誘導電流 (手前を上向き)</text>
  <text x="25" y="195" font-size="11" font-weight="bold" fill="#111827">V = - N (ΔΦ / Δt)</text>
  <text x="25" y="214" font-size="9.5" fill="#4b5563">※ 左端が N 極となり反発</text>

  <!-- 分隔线 -->
  <line x1="210" y1="15" x2="210" y2="230" stroke="#d1d5db" stroke-dasharray="4,4"/>

  <!-- 右半：铁芯螺线管自感/互感 -->
  <text x="225" y="22" font-size="11" font-weight="bold" fill="#374151">鉄心入りソレノイド (自己/相互誘導)</text>
  <!-- 铁芯圆柱 -->
  <rect x="232" y="76" width="160" height="44" rx="4" fill="#e5e7eb" stroke="#4b5563" stroke-width="1.5"/>
  <ellipse cx="392" cy="98" rx="6" ry="22" fill="#d1d5db" stroke="#4b5563" stroke-width="1.5"/>
  <text x="401" y="102" font-size="11" font-style="italic" fill="#374151">S</text>
  <!-- 绕线 -->
  <path d="M 244,120 C 240,70 256,70 256,120 M 264,120 C 260,70 276,70 276,120 M 284,120 C 280,70 296,70 296,120 M 304,120 C 300,70 316,70 316,120 M 324,120 C 320,70 336,70 336,120 M 344,120 C 340,70 356,70 356,120 M 364,120 C 360,70 376,70 376,120" fill="none" stroke="#16a34a" stroke-width="1.8"/>
  <!-- 长度 l -->
  <line x1="236" y1="58" x2="386" y2="58" stroke="#6b7280" stroke-dasharray="3,2"/>
  <text x="308" y="52" font-size="11" font-style="italic" fill="#374151">l (N = nl)</text>
  <!-- 内部磁场 B = μnI -->
  <line x1="242" y1="98" x2="378" y2="98" stroke="#2563eb" stroke-width="2" marker-end="url(#arr-blue-007-7)"/>
  <text x="275" y="138" font-size="10.5" font-weight="bold" fill="#2563eb">B = μnI, Φ = μnSI</text>
  <!-- 自感与互感公式 -->
  <text x="225" y="166" font-size="11" font-weight="bold" fill="#dc2626">自己誘導: V = -L(ΔI/Δt)</text>
  <text x="242" y="184" font-size="11" fill="#111827">L = μ n² S l = μ N² S / l</text>
  <text x="225" y="208" font-size="11" font-weight="bold" fill="#dc2626">相互誘導: V₂ = -M(ΔI₁/Δt)</text>
  <text x="242" y="226" font-size="11" fill="#111827">M = μ n₁ n₂ S l</text>
</svg>

#### 【日本考场规范推导与板书步骤】
1. **自己インダクタンス $L$ の導出**：  
   ソレノイド内部の磁場の強さは $H = nI$，磁束密度は $B = \mu H = \mu n I$ であるから，コイルを貫く磁束は $\Phi = BS = \mu n S I$。  
   電流が $\Delta t$ の間に $\Delta I$ だけ変化するとき，ファラデーの電磁誘導の法則より逆起電力 $V$ は，
   $$V = -N\frac{\Delta \Phi}{\Delta t} = -(nl)\frac{\mu n S \Delta I}{\Delta t} = -(\mu n^2 S l)\frac{\Delta I}{\Delta t}$$
   これを $V = -L\dfrac{\Delta I}{\Delta t}$ と比較すると，自己インダクタンス $L\text{ [H]}$ は，
   $$L = \mu n^2 S l = \frac{\mu N^2 S}{l}$$
2. **相互インダクタンス $M$ の導出**：  
   1 次コイル（単位長さ当たり巻き数 $n_1$）の電流 $I_1$ がつくる磁束 $\Phi_1 = \mu n_1 S I_1$ がすべて 2 次コイル（長さ $l$，総巻き数 $N_2 = n_2 l$）を貫くとき，
   $$V_2 = -N_2 \frac{\Delta \Phi_1}{\Delta t} = -(n_2 l)\frac{\mu n_1 S \Delta I_1}{\Delta t} = -(\mu n_1 n_2 S l)\frac{\Delta I_1}{\Delta t} \implies M = \mu n_1 n_2 S l$$

> 💡 讲师批注：教材 P.102–103 正文把所有符号 $l, S, n, N, \mu, n_1, n_2$ 都声明了一遍，却没有印出 $L = \mu n^2 S l$ 和 $M = \mu n_1 n_2 S l$ 的推导过程（且 P.103 漏定义了 2 次线圈长度 $l$）。这正是讲师板书展现功力的最佳环节——用 3 行代数瞬间连通法拉第定律与电感系数！

#### 【核心结论】
- **$V = -N\dfrac{\Delta\Phi}{\Delta t}$**；**$L = \mu n^2 S l$**；**$M = \mu n_1 n_2 S l$**。

---

### 核心模型 8（教材 P.104–105 / 页码 103–104）：交流の発生と実効値

#### 【教材原页内容与翻译】
> **日文原文**：  
> 回転するコイルの誘導起電力：$V = V_0\sin\omega t$，$V_0 = \Phi_0\omega$。  
> 交流の実効値：抵抗器に交流を流したときに消費される電力が平均値をとる瞬間の電圧や電流の値（直流に換算した値）。$V_e = \dfrac{1}{\sqrt{2}}V_0$，$I_e = \dfrac{1}{\sqrt{2}}I_0$。
>
> **中文翻译**：  
> 旋转线圈产生的感应电动势：$V = V_0\sin\omega t$，$V_0 = \Phi_0\omega$。  
> 交流电的有效值：在纯电阻上消耗的电功率取平均值时的等效直流电压或电流值。$V_e = \dfrac{1}{\sqrt{2}}V_0$，$I_e = \dfrac{1}{\sqrt{2}}I_0$。

#### 【考点与模型定位】
**交流发电机相位关系（$\Phi$ 为余弦 $\implies V$ 为正弦）** $+$ **瞬时功率 $\sin^2\omega t$ 图形对称法求有效值**。

#### 【多色矢量图解（SVG）】

<svg viewBox="0 0 420 250" width="420" height="250" xmlns="http://www.w3.org/2000/svg" style="background:#fafafa;border:1px solid #e5e7eb;border-radius:8px;">
  <defs>
    <marker id="arr-blk-007-8" markerWidth="6" markerHeight="6" refX="4.5" refY="3" orient="auto"><path d="M0,0 L0,6 L5.5,3 z" fill="#111827"/></marker>
  </defs>
  <!-- 左半：Φ-t 与 V-t 相位对比 -->
  <text x="20" y="20" font-size="11" font-weight="bold" fill="#374151">Φ-t (cos) と V-t (sin) の位相</text>
  <!-- 上图：Φ = Φ0 cos(ωt) -->
  <line x1="25" y1="75" x2="195" y2="75" stroke="#111827" stroke-width="1.2" marker-end="url(#arr-blk-007-8)"/>
  <line x1="35" y1="110" x2="35" y2="35" stroke="#111827" stroke-width="1.2" marker-end="url(#arr-blk-007-8)"/>
  <text x="18" y="42" font-size="10" fill="#2563eb">Φ</text>
  <text x="192" y="87" font-size="10" fill="#111827">t</text>
  <!-- cos 曲线：起点 (35,47) -> 过零 (71,75) -> 谷 (107,103) -> 过零 (143,75) -> 峰 (179,47) -->
  <path d="M 35,47 C 53,47 59,75 71,75 C 83,75 89,103 107,103 C 125,103 131,75 143,75 C 155,75 161,47 179,47" fill="none" stroke="#2563eb" stroke-width="2"/>
  <text x="12" y="51" font-size="9.5" fill="#2563eb">Φ₀</text>
  <text x="126" y="46" font-size="9.5" fill="#2563eb">Φ = Φ₀cosωt</text>

  <!-- 下图：V = V0 sin(ωt) -->
  <line x1="25" y1="175" x2="195" y2="175" stroke="#111827" stroke-width="1.2" marker-end="url(#arr-blk-007-8)"/>
  <line x1="35" y1="215" x2="35" y2="130" stroke="#111827" stroke-width="1.2" marker-end="url(#arr-blk-007-8)"/>
  <text x="18" y="138" font-size="10" fill="#dc2626">V</text>
  <text x="192" y="187" font-size="10" fill="#111827">t</text>
  <!-- sin 曲线：起点 (35,175) -> 峰 (71,147) -> 过零 (107,175) -> 谷 (143,203) -> 过零 (179,175) -->
  <path d="M 35,175 C 47,175 53,147 71,147 C 89,147 95,175 107,175 C 119,175 125,203 143,203 C 161,203 167,175 179,175" fill="none" stroke="#dc2626" stroke-width="2"/>
  <text x="12" y="151" font-size="9.5" fill="#dc2626">V₀</text>
  <text x="103" y="190" font-size="9" fill="#374151">T/2</text>
  <text x="176" y="190" font-size="9" fill="#374151">T</text>
  <text x="48" y="230" font-size="10" font-weight="bold" fill="#dc2626">V = -ΔΦ/Δt = V₀sinωt</text>

  <!-- 分隔线 -->
  <line x1="210" y1="15" x2="210" y2="235" stroke="#d1d5db" stroke-dasharray="4,4"/>

  <!-- 右半：瞬时功率 P = I0 V0 sin²(ωt) 与平均功率 -->
  <text x="232" y="20" font-size="11" font-weight="bold" fill="#374151">消費電力 P と実効値の導出</text>
  <line x1="228" y1="145" x2="405" y2="145" stroke="#111827" stroke-width="1.3" marker-end="url(#arr-blk-007-8)"/>
  <line x1="238" y1="155" x2="238" y2="42" stroke="#111827" stroke-width="1.3" marker-end="url(#arr-blk-007-8)"/>
  <text x="224" y="48" font-size="10" fill="#16a34a">P</text>
  <text x="400" y="158" font-size="10" fill="#111827">t</text>
  <!-- sin² 曲线（两个波峰，频率加倍） -->
  <path d="M 238,145 C 254,145 262,65 278,65 C 294,65 302,145 318,145 C 334,145 342,65 358,65 C 374,65 382,145 398,145" fill="#dcfce7" fill-opacity="0.45" stroke="#16a34a" stroke-width="2"/>
  <!-- 最大值虚线 I0 V0 -->
  <line x1="238" y1="65" x2="398" y2="65" stroke="#9ca3af" stroke-dasharray="3,3"/>
  <text x="214" y="69" font-size="9.5" fill="#374151">I₀V₀</text>
  <!-- 平均功率线 1/2 I0 V0 -->
  <line x1="238" y1="105" x2="398" y2="105" stroke="#dc2626" stroke-width="1.8" stroke-dasharray="5,3"/>
  <text x="260" y="100" font-size="10" font-weight="bold" fill="#dc2626">平均電力 P̄ = ½ I₀V₀ = I_e V_e</text>
  <text x="312" y="158" font-size="9" fill="#374151">T/2</text>
  <text x="392" y="158" font-size="9" fill="#374151">T</text>
  <!-- 结论公式 -->
  <text x="235" y="190" font-size="11.5" font-weight="bold" fill="#2563eb">V_e = V₀ / √2 ,  I_e = I₀ / √2</text>
  <text x="235" y="212" font-size="10" fill="#374151">※ 波の上半分を下の谷へ埋めると</text>
  <text x="245" y="227" font-size="10" fill="#374151">　高さ ½ I₀V₀ の長方形になる！</text>
</svg>

#### 【日本考场规范推导与板书步骤】
1. **交流起電力の発生**：  
   時刻 $t = 0$ でコイル面が磁場に垂直（磁束最大 $\Phi_0 = BS$）のとき，角速度 $\omega$ で回転すると時刻 $t$ における磁束は $\Phi = \Phi_0 \cos\omega t$。  
   ファラデーの電磁誘導の法則（1 巻きコイル $N = 1$）より，
   $$V = -\frac{d\Phi}{dt} = -(-\Phi_0\omega\sin\omega t) = \Phi_0\omega\sin\omega t = V_0\sin\omega t \qquad (V_0 = \Phi_0\omega)$$
   （※ $N$ 巻きコイルの場合は $V_0 = N\Phi_0\omega = NBS\omega$）
2. **交流の実効値の導出**：  
   抵抗 $R$ に交流電圧 $V = V_0\sin\omega t$ を加えると，流れる電流は $I = \dfrac{V}{R} = I_0\sin\omega t$（$I_0 = \dfrac{V_0}{R}$）。  
   瞬間の消費電力 $P$ は半角の公式より，
   $$P = IV = I_0 V_0 \sin^2\omega t = \frac{1}{2}I_0 V_0 (1 - \cos 2\omega t)$$
   1 周期にわたる $\cos 2\omega t$ の平均値は $0$ であるから，平均消費電力 $\bar{P}$ は，
   $$\bar{P} = \frac{1}{2}I_0 V_0 = \left(\frac{I_0}{\sqrt{2}}\right)\left(\frac{V_0}{\sqrt{2}}\right) = I_e V_e$$
   したがって，実効値は $V_e = \dfrac{V_0}{\sqrt{2}}$，$I_e = \dfrac{I_0}{\sqrt{2}}$ と定義される。

> 💡 讲师批注：日本家庭用电标称 `100 V` 指的是**有效值 $V_e = 100\text{ V}$**，其实际电压峰值是 $V_0 = 100\sqrt{2} \fallingdotseq 141\text{ V}$！另外注意 $P$-$t$ 图像（绿线）的周期是原交流电周期 $T$ 的**一半（$T/2$）**，也就是频率变为 $2f$。

#### 【核心结论】
- **$V = V_0\sin\omega t$**（单匝 $V_0 = \Phi_0\omega$，$N$ 匝 $V_0 = NBS\omega$）；**$V_e = \dfrac{1}{\sqrt{2}}V_0$，$I_e = \dfrac{1}{\sqrt{2}}I_0$**。

---

## 4. 全局术语表同步说明

本切片新增的 **62 条** 日文物理核心术语与假名注音已写入切片术语文件：[.glossary_007.md](file:///Users/baohan/Desktop/EJU/notes_物理/.glossary_007.md)，待主控统一合并去重写入全局术语表 [glossary_all.md](file:///Users/baohan/Desktop/EJU/notes_物理/glossary_all.md)。
