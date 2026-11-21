# EJU 物理全解讲义 — 切片 006（P.76–P.90）
> **对应教材章节**：第三章 波（光波：薄膜・くさび形空気層・ニュートンリング・レンズ）＆ 第四章 電気と磁気（静電気力、電場、電気力線、電位、等電位面、コンデンサー、電流、オームの法則、ジュール熱・電力、キルヒホッフの法則）  
> **适用对象**：需快速唤醒中国高中物理基础、并掌握纯日文板书与 EJU 考场规范表达的授课教师 / 考生

---

## 1. 本节前置：国内高中物理基础唤醒

本切片横跨**波动光学（光波の干渉・レンズ）**与**电磁学前半（静電場・コンデンサー・直流回路）**两大核心板块，是 EJU 物理得分率分化最严重的黄金提分区。

### 1.1 波动光学与几何光学核心概念

1. **光程差（光路差）与半波损失（位相のずれ $\pi$）**
   - 光在折射率为 $n$ 的介质中传播几何路程 $L$ 时，等效于在真空中传播的**光学路程（光路長）**为 $nL$。
   - **反射时的相位突变判定口诀**：
     - 光从**光疏介质 $\to$ 光密介质**（$n_1 < n_2$）界面反射：相当于**固定端反射（固定端反射）**，相位突变 $\pi$（等效增加 $\dfrac{\lambda}{2}$ 光程差，俗称“半波损失”）。
     - 光从**光密介质 $\to$ 光疏介质**（$n_1 > n_2$）界面反射：相当于**自由端反射（自由端反射）**，相位**不**突变（无半波损失）。
   - **三大经典干涉模型**（均为 1 次固定端反射 + 1 次自由端反射，即发生 1 次半波损失，故明暗条件与杨氏双缝**恰好相反**）：
     - **薄膜干涉（薄膜による干渉）**：设膜厚 $d$、折射率 $n$、膜内折射角 $\theta$（空气—薄膜—空气）：
       $$\text{明（強め合い）：} 2nd\cos\theta = \left(m + \frac{1}{2}\right)\lambda, \qquad \text{暗（弱め合い）：} 2nd\cos\theta = m\lambda \quad (m = 0, 1, 2, \dots)$$
     - **劈尖空气层（くさび形空気層）**：顶角极小为 $\theta$，距顶棱 $x$ 处空气层厚度 $d = x\tan\theta$，垂直入射（$n_{\text{空気}} \approx 1$）：
       $$\text{明：} 2x\tan\theta = \left(m + \frac{1}{2}\right)\lambda, \qquad \text{暗：} 2x\tan\theta = m\lambda \quad (m = 0, 1, 2, \dots)$$
     - **牛顿环（ニュートンリング）**：曲率半径 $R$ 的平凸透镜置于平面玻璃上，距中心 $r$ 处空气层厚度 $d$ 满足勾股定理 $r^2 = d(2R - d) \approx 2Rd \implies 2d \approx \dfrac{r^2}{R}$：
       $$\text{明リング：} \frac{r^2}{R} = \left(m + \frac{1}{2}\right)\lambda, \qquad \text{暗リング：} \frac{r^2}{R} = m\lambda \quad (m = 0, 1, 2, \dots)$$

2. **薄透镜成像公式（レンズの公式 / 写像公式）**
   $$\frac{1}{a} + \frac{1}{b} = \frac{1}{f}, \qquad \text{倍率 } m = \frac{|b|}{a}$$
   - **符号规定（极重要）**：
     - 物距 $a$：恒为正（$a > 0$）；
     - 像距 $b$：像在透镜**后方**（倒立**実像**）取 $b > 0$；像在透镜**前方**（正立**虚像**）取 $b < 0$；
     - 焦距 $f$：**凸透镜（凸レンズ）**取 $f > 0$；**凹透镜（凹レンズ）**取 $f < 0$。

### 1.2 静电场、电容器与直流电路核心概念

1. **库仑定律、电场强度与电势**
   - **库仑定律（クーロンの法則）**：$F = k\dfrac{|q_1 q_2|}{r^2}$（真空中 $k = \dfrac{1}{4\pi\varepsilon_0} \approx 9.0 \times 10^9\text{ N}\cdot\text{m}^2/\text{C}^2$）。
   - **电场强度（電場）**：定义式 $\vec{E} = \dfrac{\vec{F}}{q}$（$\vec{F} = q\vec{E}$）；点电荷电场 $E = k\dfrac{|q|}{r^2}$；满足矢量叠加原理 $\vec{E} = \vec{E}_1 + \vec{E}_2 + \cdots$。
   - **电势（電位）**：静电力是保守力，电势定义为 $+1\text{ C}$ 正电荷的电势能（単位電荷の位置エネルギー）：
     - 匀强电场：$V = Ed$（单位 $\text{V} = \text{J/C}$，故 $E$ 的单位 $\text{N/C} = \text{V/m}$）；
     - 点电荷电势（取无穷远为零电势）：$V = k\dfrac{q}{r}$（**标量，带正负号直接代数相加**！）。
   - **电场线（電気力線）与等势面（等電位面）**：始终**正交**；沿等势面移动电荷静电力做功为 $0$；线/面越密处电场越强。

2. **平行板电容器（平行板コンデンサー）**
   - **定义式与决定式**：
     $$Q = CV, \qquad C = \varepsilon\frac{S}{d} = \varepsilon_r \varepsilon_0 \frac{S}{d} \quad \left(\text{比誘電率 } \varepsilon_r = \frac{\varepsilon}{\varepsilon_0}\right)$$
   - **静电能（静電エネルギー）**：$V$-$Q$ 图像下方三角形面积：
     $$U = \frac{1}{2}QV = \frac{1}{2}CV^2 = \frac{Q^2}{2C}$$
   - **串并联合成容量**：
     - 并联（並列）：$C = C_1 + C_2$（电压 $V$ 相同，电荷相加）；
     - 串联（直列）：$\dfrac{1}{C} = \dfrac{1}{C_1} + \dfrac{1}{C_2}$（电荷 $Q$ 相同，电压相加）。
   - **极板间插入电介质的“双态对比”**：
     - 始终接电源（$V$ 恒定）：$C \to \varepsilon_r C_0$，$Q \to \varepsilon_r Q_0$，$E = V/d$ 不变，$U \to \varepsilon_r U_0$；
     - 断开电源（$Q$ 恒定）：$C \to \varepsilon_r C_0$，$V \to V_0/\varepsilon_r$，$E \to E_0/\varepsilon_r$，$U \to U_0/\varepsilon_r$。

3. **直流电路核心定律**
   - **电流定义与微观模型**：$I = \dfrac{q}{t} = envS$（$e$：元电荷，$n$：自由电子数密度，$v$：定向移动平均速率，$S$：截面积）。
   - **欧姆定律与电阻定律**：$V = RI$，$R = \rho\dfrac{l}{S}$；金属电阻率随温度升高而增大：$\rho = \rho_0(1 + \alpha t)$。
   - **焦耳定律与电功率**：
     $$P = \frac{W}{t} = IV = I^2 R = \frac{V^2}{R}, \qquad Q = W = Pt = IVt = I^2 Rt = \frac{V^2}{R}t$$
   - **基尔霍夫定律（キルヒホッフの法則）**：
     - 第一定律（节点电流）：$\sum I_{\text{入}} = \sum I_{\text{出}}$（电荷守恒）；
     - 第二定律（回路电压）：任意闭合回路中 $\sum E_{\text{起電力}} = \sum RI$，即沿闭合回路一周电势差之和为 $0$（能量守恒）。

### 1.3 中日物理体系与习惯差异提醒

| 对比维度 | 中国国内高中物理习惯 | 日本 EJU / 高中物理习惯（授课必强调） |
| :--- | :--- | :--- |
| **透镜公式符号** | 常用 $\dfrac{1}{u} + \dfrac{1}{v} = \dfrac{1}{f}$ | 日本一律用 **$a$（物距）、$b$（像距）、$f$（焦距）**：$\dfrac{1}{a} + \dfrac{1}{b} = \dfrac{1}{f}$，放大率 $m = \dfrac{|b|}{a}$。 |
| **电势与电压符号** | 电势用 $\varphi$，电压/电势差用 $U$，电势能用 $E_p$ | 日本**电势与电压统一用 $V$**，**静电能/电势能用 $U$**！绝不可把 $U$ 误当成电压，也不要在日文板书里写 $\varphi$。 |
| **电场强度与电场线** | 称“电场强度”和“电场线” | 日本分别称 **電場（でんば / 電界）** 与 **電気力線（でんきりきせん）**，且高斯定理常直接表述为“场强 $E$ 处每 $1\text{ m}^2$ 穿出 $E$ 条电场线”。 |
| **电阻与电容器符号** | 电阻率 $\rho$、介电常数 $\varepsilon_r$、电容 $C$ | 符号基本一致，但注意日本把“相对介电常数”叫 **比誘電率（$\varepsilon_r$）**，把“静电屏蔽/感应”叫 **静電誘導**，把“极化”叫 **誘電分極**。 |
| **科目归属勘误提醒** | 统称高中物理选修/选择性必修 | 本切片教材页眉虽统一印作「物理基礎」，但薄膜干涉、牛顿环、透镜、静电场、电容器与基尔霍夫定律在 EJU 中均属**「物理（発展）」**范畴。 |

---

## 2. 日文物理核心词汇与公式假名注音（板书必备）

### 2.1 核心物理词汇表

#### 光波的干涉与透镜
- **光波（こうは / kōha）** — 光波
- **干渉（かんしょう / kanshō）** — 干涉
- **薄膜（はくまく / hakumaku）** — 薄膜
- **くさび形空気層（くさびがたくうきそう / kusabigata kūkisō）** — 劈尖形空气层
- **ニュートンリング（にゅーとんりんぐ / nyūton ringu）** — 牛顿环
- **光路差（こうろさ / kōrosa）** — 光程差
- **固定端反射（こていたんはんしゃ / koteitan hansha）** — 固定端反射（有半波损失）
- **自由端反射（じゆうたんはんしゃ / jiyūtan hansha）** — 自由端反射（无半波损失）
- **レンズ（れんず / renzu）** — 透镜
- **凸レンズ（とつれんず / totsu renzu）** — 凸透镜
- **凹レンズ（おうれんず / ō renzu）** — 凹透镜
- **焦点距離（しょうてんきょり / shōten kyori）** — 焦距（$f$）
- **写像公式（しゃぞうこうしき / shazō kōshiki）** — 透镜成像公式
- **倍率（ばいりつ / bairitsu）** — 放大率（$m$）
- **実像（じつぞう / jitsuzō）** — 实像
- **虚像（きょぞう / kyozō）** — 虚像

#### 静电力、电场与电势
- **静電気力（せいでんきりょく / seidenkiryoku）** — 静电力（库仑力）
- **クーロンの法則（くーろんのほうそく / kūron no hōsoku）** — 库仑定律
- **荷電粒子（かでんりゅうし / kaden ryūshi）** — 带电粒子
- **電荷 / 電気量（でんか / でんきりょう / denka / denkiryō）** — 电荷 / 电量
- **導体（どうたい / dōtai）** — 导体
- **帯電体（たいでんたい / taidentai）** — 带电体
- **静電誘導（せいでんゆうどう / seiden yūdō）** — 静电感应
- **電場 / 電界（でんば / でんかい / denba / denkai）** — 电场
- **点電荷（てんでんか / tendenka）** — 点电荷
- **電気力線（でんきりきせん / denkiri-kisen）** — 电场线
- **電位（でんい / den'i）** — 电势（$V$）
- **電位差 / 電圧（でんいさ / でんあつ / den'isa / den'atsu）** — 电势差 / 电压
- **保存力（ほぞんりょく / hozonryoku）** — 保守力
- **等電位面（とうでんいめん / tōden'imen）** — 等势面

#### 电容器
- **コンデンサー（こんでんさー / kondensā）** — 电容器
- **平行板コンデンサー（へいこうばんこんでんさー / heikōban kondensā）** — 平行板电容器
- **極板（きょくばん / kyokuban）** — 极板
- **電気容量（でんきようりょう / denki yōryō）** — 电容（$C$）
- **誘電率（ゆうでんりつ / yūdenritsu）** — 介电常数 / 电容率（$\varepsilon$）
- **比誘電率（ひゆうでんりつ / hiyūdenritsu）** — 相对介电常数（$\varepsilon_r$）
- **誘電体（ゆうでんたい / yūdentai）** — 电介质
- **誘電分極（ゆうでんぶんきょく / yūden bunkyoku）** — 电介质极化
- **充電（じゅうでん / jūden）** — 充电
- **放電（ほうでん / hōden）** — 放电
- **静電エネルギー（せいでんえねるぎー / seiden enerugī）** — 静电能（$U$）
- **合成容量（ごうせいようりょう / gōsei yōryō）** — 等效电容

#### 电流、欧姆定律与基尔霍夫定律
- **電流（でんりゅう / denryū）** — 电流（$I$）
- **自由電子（じゆうでんし / jiyū denshi）** — 自由电子
- **数密度（すうみつど / sūmitsudo）** — 数密度（$n$）
- **オームの法則（おーむのほうそく / ōmu no hōsoku）** — 欧姆定律
- **電圧降下（でんあつこうか / den'atsu kōka）** — 电压降
- **電気抵抗（でんきていこう / denki teikō）** — 电阻（$R$）
- **抵抗率 / 比抵抗（ていこうりつ / ひていこう / teikōritsu / hiteikō）** — 电阻率（$\rho$）
- **温度係数（おんどけいすう / ondo keisū）** — 温度系数（$\alpha$）
- **陽イオン（よういおん / yōion）** — 阳离子
- **ジュール熱（じゅーるねつ / jūru netsu）** — 焦耳热
- **ジュールの法則（じゅーるのほうそく / jūru no hōsoku）** — 焦耳定律
- **電力 / 消費電力（でんりょく / しょうひでんりょく / denryoku / shōhi denryoku）** — 电功率（$P$）
- **電力量（でんりょくりょう / denryokuryō）** — 电功 / 电能（$W$）
- **キルヒホッフの法則（きるひほっふのほうそく / kiruhihoffu no hōsoku）** — 基尔霍夫定律
- **分岐点（ぶんきてん / bunkiten）** — 分支点 / 节点

### 2.2 核心公式课堂口语读法（板书念法）

| 公式 | 日本课堂标准板书口语读法 |
| :--- | :--- |
| $2nd\cos\theta = \left(m + \dfrac{1}{2}\right)\lambda$ | 「に・エヌ・ディー・コサインシータ、イコール、かっこ・エム・たす・にぶんのいち・かっこ・ラムダ」 |
| $\dfrac{r^2}{R} = m\lambda$ | 「ラージアールぶんの・スモールアールにじょう、イコール、エム・ラムダ」 |
| $\dfrac{1}{a} + \dfrac{1}{b} = \dfrac{1}{f}$ | 「エーぶんのいち、たす、ビーぶんのいち、イコール、エフぶんのいち」 |
| $F = k\dfrac{q_1 q_2}{r^2}$ | 「エフ・イコール、ケー・かける・アールにじょうぶんの・キューいち・キューに」 |
| $\vec{E} = \dfrac{\vec{F}}{q}$ | 「イー・ベクトル、イコール、キューぶんの・エフ・ベクトル」 |
| $V = k\dfrac{q}{r}$ | 「ブイ・イコール、ケー・かける・アールぶんの・キュー」 |
| $Q = CV,\ C = \varepsilon\dfrac{S}{d}$ | 「キュー・イコール、シーブイ」「シー・イコール、イプシロン・ディーぶんのエス」 |
| $U = \dfrac{1}{2}QV = \dfrac{1}{2}CV^2 = \dfrac{Q^2}{2C}$ | 「ユー・イコール、にぶんのいち・キューブイ、イコール、にぶんのいち・シーブイにじょう、イコール、にシーぶんの・キューにじょう」 |
| $I = envS$ | 「アイ・イコール、イー・エヌ・ブイ・エス」 |
| $R = \rho\dfrac{l}{S}$ | 「アール・イコール、ロー・かける・エスぶんのエル」 |
| $\rho = \rho_0(1 + \alpha t)$ | 「ロー・イコール、ローゼロ・かっこ・いち・たす・アルファティー・かっこ」 |
| $Q = IVt = I^2 Rt = \dfrac{V^2}{R}t$ | 「キュー・イコール、アイ・ブイ・ティー、イコール、アイにじょう・アールティー、イコール、アールぶんの・ブイにじょう・ティー」 |

---

## 3. 逐题深度解析（核心模型与公式推导精讲）

> **切片说明**：本切片（教材 P.76–P.90 / 页码 75–89）全部为**光波与电磁学核心概念及公式推导页**，教材内不含编号例题或练习题。以下按教材顺序拆解为 **8 大核心考场模型**，逐一配备原书要点还原、多色矢量图解（SVG）及日本考场规范推导步骤，可直接用于板书授课。

---

### 核心模型 1（教材 P.76 / 页码 75）：薄膜干渉・くさび形空気層・ニュートンリング

#### 【原书要点与翻译】
> **日文原书要点**：  
> 1. **薄膜による干渉**：明るくなる条件 $2nd\cos\theta = \left(m + \dfrac{1}{2}\right)\lambda$，暗くなる条件 $2nd\cos\theta = m\lambda$（$m = 0, 1, 2, \cdots$）。  
> 2. **くさび形空気層**：明るくなる条件 $2x\tan\theta = \left(m + \dfrac{1}{2}\right)\lambda$，暗くなる条件 $2x\tan\theta = m\lambda$（$m = 0, 1, 2, \cdots$）。  
> 3. **ニュートンリング**：明るいリングの条件 $\dfrac{r^2}{R} = \left(m + \dfrac{1}{2}\right)\lambda$，暗いリングの条件 $\dfrac{r^2}{R} = m\lambda$（$m = 0, 1, 2, \cdots$）。
>
> **中文核心**：三大等厚/等倾干涉模型的光程差与半波损失统一推导。

#### 【考点与模型定位】
**光程差（光路差）＋ 反射位相変化（半波损失）**——EJU 波动光学最高频考点，必考“反射界面是否发生固定端反射”以及“改变折射率 $n$ 或介质时条纹间距如何变化”。

#### 【多色矢量图解（SVG）】

<svg viewBox="0 0 420 260" width="420" height="260" xmlns="http://www.w3.org/2000/svg" style="background:#fafafa;border:1px solid #e5e7eb;border-radius:8px;">
  <defs>
    <marker id="arr-blue-006-1" markerWidth="7" markerHeight="7" refX="5" refY="3" orient="auto"><path d="M0,0 L0,6 L6,3 z" fill="#2563eb"/></marker>
    <marker id="arr-red-006-1" markerWidth="7" markerHeight="7" refX="5" refY="3" orient="auto"><path d="M0,0 L0,6 L6,3 z" fill="#dc2626"/></marker>
    <marker id="arr-blk-006-1" markerWidth="7" markerHeight="7" refX="5" refY="3" orient="auto"><path d="M0,0 L0,6 L6,3 z" fill="#111827"/></marker>
  </defs>
  <!-- 左：薄膜干涉 -->
  <text x="20" y="20" font-size="11" font-weight="bold" fill="#111827">① 薄膜による干渉 (空気-膜n-空気)</text>
  <rect x="15" y="75" width="175" height="65" fill="#dbeafe" opacity="0.65" stroke="#2563eb" stroke-width="1.2"/>
  <text x="158" y="133" font-size="10" fill="#1e40af">屈折率 n</text>
  <!-- 厚度 d -->
  <line x1="178" y1="75" x2="178" y2="140" stroke="#374151" stroke-width="1" stroke-dasharray="3,2"/>
  <text x="182" y="112" font-size="11" font-style="italic" fill="#374151">d</text>
  <!-- 入射光线1 & 反射光线1 (D点固定端) -->
  <line x1="35" y1="35" x2="95" y2="75" stroke="#dc2626" stroke-width="1.6" marker-end="url(#arr-red-006-1)"/>
  <line x1="95" y1="75" x2="155" y2="35" stroke="#dc2626" stroke-width="1.6" marker-end="url(#arr-red-006-1)"/>
  <circle cx="95" cy="75" r="3.5" fill="#dc2626"/>
  <text x="84" y="67" font-size="10" font-weight="bold" fill="#dc2626">D(固:π)</text>
  <!-- 入射光线2 -> A -> E(自由端) -> D -->
  <line x1="15" y1="45" x2="55" y2="75" stroke="#2563eb" stroke-width="1.6" marker-end="url(#arr-blue-006-1)"/>
  <line x1="55" y1="75" x2="75" y2="140" stroke="#2563eb" stroke-width="1.6"/>
  <line x1="75" y1="140" x2="95" y2="75" stroke="#2563eb" stroke-width="1.6"/>
  <circle cx="75" cy="140" r="3.5" fill="#16a34a"/>
  <text x="58" y="154" font-size="10" font-weight="bold" fill="#16a34a">E(自:0)</text>
  <!-- 法线与折射角 θ -->
  <line x1="55" y1="60" x2="55" y2="135" stroke="#6b7280" stroke-width="1" stroke-dasharray="3,3"/>
  <text x="58" y="108" font-size="10" fill="#374151">θ</text>
  <!-- 光程差公式框 -->
  <text x="18" y="176" font-size="10.5" fill="#111827">光路差 ΔL = 2nd cosθ</text>
  <text x="18" y="194" font-size="10" fill="#dc2626">明: 2nd cosθ = (m + 1/2)λ</text>
  <text x="18" y="210" font-size="10" fill="#2563eb">暗: 2nd cosθ = mλ</text>
  <text x="18" y="232" font-size="9.5" fill="#6b7280">※ 1回固定端反射→明暗逆転</text>

  <!-- 分隔线 -->
  <line x1="210" y1="12" x2="210" y2="248" stroke="#d1d5db" stroke-dasharray="4,4"/>

  <!-- 右上：劈尖空气层 -->
  <text x="222" y="20" font-size="11" font-weight="bold" fill="#111827">② くさび形空気層</text>
  <rect x="225" y="102" width="175" height="12" fill="#e5e7eb" stroke="#374151" stroke-width="1.2"/>
  <polygon points="225,102 395,62 398,74 228,102" fill="#e5e7eb" stroke="#374151" stroke-width="1.2"/>
  <text x="255" y="99" font-size="10" fill="#dc2626">θ</text>
  <line x1="335" y1="42" x2="335" y2="102" stroke="#2563eb" stroke-width="1.4" marker-end="url(#arr-blue-006-1)"/>
  <line x1="342" y1="102" x2="342" y2="42" stroke="#dc2626" stroke-width="1.4" marker-end="url(#arr-red-006-1)"/>
  <text x="348" y="76" font-size="9.5" fill="#16a34a">自</text>
  <text x="348" y="99" font-size="9.5" fill="#dc2626">固</text>
  <text x="275" y="126" font-size="10" fill="#111827">d = x tanθ → ΔL = 2x tanθ</text>

  <!-- 右下：牛顿环 -->
  <text x="222" y="150" font-size="11" font-weight="bold" fill="#111827">③ ニュートンリング</text>
  <line x1="230" y1="228" x2="395" y2="228" stroke="#374151" stroke-width="2"/>
  <path d="M 245 198 Q 312 248 380 198 L 380 192 L 245 192 Z" fill="#dbeafe" stroke="#2563eb" stroke-width="1.3"/>
  <!-- 半径与弦关系 -->
  <line x1="312" y1="158" x2="312" y2="228" stroke="#6b7280" stroke-width="1" stroke-dasharray="3,2"/>
  <line x1="312" y1="158" x2="358" y2="213" stroke="#111827" stroke-width="1.2"/>
  <text x="340" y="182" font-size="10" font-style="italic" fill="#111827">R</text>
  <line x1="312" y1="213" x2="358" y2="213" stroke="#dc2626" stroke-width="1.2"/>
  <text x="330" y="210" font-size="10" font-style="italic" fill="#dc2626">r</text>
  <text x="362" y="224" font-size="10" font-style="italic" fill="#2563eb">d</text>
  <text x="225" y="247" font-size="10" fill="#111827">r² = d(2R−d) ≒ 2Rd ⇒ ΔL = 2d = r²/R</text>
</svg>

#### 【日本考场规范分步推导】

1. **薄膜による干渉**：光線 1（点 D で反射）と光線 2（点 A で屈折 $\to$ 点 E で反射 $\to$ 点 D で再び空気中へ）の光学的距離の差（光路差）$\Delta L$ を求める。  
   スネルの法則および幾何学的対称性より，
   $$\Delta L = n(\overline{\text{AE}} + \overline{\text{ED}}) - \overline{\text{BD}} = n(\overline{\text{CE}} + \overline{\text{ED}}) = n \cdot \overline{\text{CD}'} = 2nd\cos\theta$$
   ここで，点 D（空気 $\to$ 薄膜）は屈折率の大きい媒質との境界面なので**固定端反射（位相が $\pi$ ずれる）**，点 E（薄膜 $\to$ 空気）は**自由端反射（位相のずれなし）**である。  
   したがって，明暗の条件は通常と逆転し，
   $$\text{明：} 2nd\cos\theta = \left(m + \frac{1}{2}\right)\lambda, \qquad \text{暗：} 2nd\cos\theta = m\lambda \quad (m = 0, 1, 2, \cdots)$$

> 💡 讲师批注：**教材补遗提醒**！教材 P.76（页码 75）此处默认上下均为空气（$n_{\text{上}} < n_{\text{膜}} > n_{\text{下}}$），故仅发生 1 次半波损失。若考题改为“玻璃板上的防反射镀膜”（$n_{\text{空気}} < n_{\text{膜}} < n_{\text{ガラス}}$），则上下两个界面**都是**固定端反射（共 2 次半波损失，相位差抵消），明暗条件将恢复为 $2nd\cos\theta = m\lambda$ 为明！务必在课堂上点破这一 EJU 高频陷阱。

2. **くさび形空気層**：頂点から距離 $x$ の位置における空気層の厚さ $d$ は $d = x\tan\theta$。ほぼ垂直入射（$\cos 0^\circ = 1$）かつ空気の屈折率 $n \fallingdotseq 1$ より，光路差は $\Delta L = 2d = 2x\tan\theta$。上面は自由端反射，下面は固定端反射（1 回のみ位相 $\pi$ ずれ）ゆえ，
   $$\text{明：} 2x\tan\theta = \left(m + \frac{1}{2}\right)\lambda, \qquad \text{暗：} 2x\tan\theta = m\lambda \quad (m = 0, 1, 2, \cdots)$$

3. **ニュートンリング**：曲率半径 $R$ の球面について，三平方の定理より $R^2 = r^2 + (R - d)^2 \implies r^2 = 2Rd - d^2$。  
   $d \ll R$ であるから $d^2$ を無視すると $2d \fallingdotseq \dfrac{r^2}{R}$。くさび形空気層と同様に下面のみで固定端反射が起こるため，
   $$\text{明リング：} \frac{r^2}{R} = \left(m + \frac{1}{2}\right)\lambda, \qquad \text{暗リング：} \frac{r^2}{R} = m\lambda \quad (m = 0, 1, 2, \cdots)$$

> 💡 讲师批注：中心点 $r = 0$ 处对应 $m = 0$，满足暗环条件，因此反射光观察到的牛顿环中心一定是**暗点（暗い）**！但若从下方看**透射光（透過光）**，由于二次反射发生两次固定端反射（或无半波损失），中心反而为**亮点**。

---

### 核心模型 2（教材 P.77 / 页码 76）：レンズの公式（写像公式）と作図

#### 【原书要点与翻译】
> **日文原书要点**：  
> レンズの公式（写像公式）：$\dfrac{1}{a} + \dfrac{1}{b} = \dfrac{1}{f}$，倍率：$m = \dfrac{|b|}{a}$。  
> 物体とレンズとの距離 $a$：常に正；レンズと像との距離 $b$：レンズ後方は正，レンズ手前は負；焦点距離 $f$：凸レンズは正，凹レンズは負。

#### 【考点与模型定位】
**几何光学薄透镜成像（相似三角形推导写像公式 ＋ 正负号规则判定实像/虚像）**。

#### 【多色矢量图解（SVG）】

<svg viewBox="0 0 420 260" width="420" height="260" xmlns="http://www.w3.org/2000/svg" style="background:#fafafa;border:1px solid #e5e7eb;border-radius:8px;">
  <defs>
    <marker id="arr-red-006-2" markerWidth="7" markerHeight="7" refX="5" refY="3" orient="auto"><path d="M0,0 L0,6 L6,3 z" fill="#dc2626"/></marker>
    <marker id="arr-blue-006-2" markerWidth="7" markerHeight="7" refX="5" refY="3" orient="auto"><path d="M0,0 L0,6 L6,3 z" fill="#2563eb"/></marker>
    <marker id="arr-grn-006-2" markerWidth="7" markerHeight="7" refX="5" refY="3" orient="auto"><path d="M0,0 L0,6 L6,3 z" fill="#16a34a"/></marker>
  </defs>
  <!-- 上半：凸透镜实像 -->
  <text x="15" y="18" font-size="11" font-weight="bold" fill="#111827">① 凸レンズ（f &gt; 0, a &gt; f → 倒立実像 b &gt; 0）</text>
  <line x1="20" y1="75" x2="400" y2="75" stroke="#6b7280" stroke-width="1.2"/>
  <!-- 凸透镜 -->
  <path d="M 200 30 Q 212 75 200 120 Q 188 75 200 30 Z" fill="#dbeafe" stroke="#2563eb" stroke-width="1.5"/>
  <text x="205" y="72" font-size="10" fill="#111827">O</text>
  <!-- 焦点 F1, F2 -->
  <circle cx="140" cy="75" r="2.5" fill="#111827"/><text x="135" y="90" font-size="10" fill="#111827">F₁</text>
  <circle cx="260" cy="75" r="2.5" fill="#111827"/><text x="255" y="90" font-size="10" fill="#111827">F₂</text>
  <!-- 物体 AA' -->
  <line x1="80" y1="75" x2="80" y2="42" stroke="#16a34a" stroke-width="2.2" marker-end="url(#arr-grn-006-2)"/>
  <text x="68" y="42" font-size="10" fill="#16a34a">A</text><text x="72" y="88" font-size="10" fill="#374151">A'</text>
  <!-- 光线 1: 平行光 -> 过 F2 -->
  <line x1="80" y1="42" x2="200" y2="42" stroke="#dc2626" stroke-width="1.4"/>
  <line x1="200" y1="42" x2="320" y2="108" stroke="#dc2626" stroke-width="1.4" marker-end="url(#arr-red-006-2)"/>
  <!-- 光线 2: 过光心 O -->
  <line x1="80" y1="42" x2="320" y2="108" stroke="#2563eb" stroke-width="1.4" marker-end="url(#arr-blue-006-2)"/>
  <!-- 倒立实像 BB' -->
  <line x1="320" y1="75" x2="320" y2="108" stroke="#dc2626" stroke-width="2.2" marker-end="url(#arr-red-006-2)"/>
  <text x="326" y="112" font-size="10" fill="#dc2626">B</text><text x="316" y="70" font-size="10" fill="#374151">B'</text>
  <!-- 距离标注 a, b, f -->
  <text x="132" y="118" font-size="10" fill="#374151">←─── a ───→</text>
  <text x="252" y="118" font-size="10" fill="#374151">←─── b ───→</text>

  <!-- 分隔线 -->
  <line x1="15" y1="132" x2="405" y2="132" stroke="#d1d5db" stroke-dasharray="4,4"/>

  <!-- 下半：凹透镜虚像 -->
  <text x="15" y="150" font-size="11" font-weight="bold" fill="#111827">② 凹レンズ（f &lt; 0 → 常に正立虚像 b &lt; 0）</text>
  <line x1="20" y1="205" x2="400" y2="205" stroke="#6b7280" stroke-width="1.2"/>
  <!-- 凹透镜 -->
  <path d="M 192 162 L 208 162 Q 202 205 208 248 L 192 248 Q 198 205 192 162 Z" fill="#dbeafe" stroke="#2563eb" stroke-width="1.5"/>
  <text x="208" y="202" font-size="10" fill="#111827">O</text>
  <!-- 焦点 -->
  <circle cx="140" cy="205" r="2.5" fill="#111827"/><text x="135" y="220" font-size="10" fill="#111827">F₁</text>
  <circle cx="260" cy="205" r="2.5" fill="#111827"/><text x="255" y="220" font-size="10" fill="#111827">F₂</text>
  <!-- 物体 -->
  <line x1="80" y1="205" x2="80" y2="172" stroke="#16a34a" stroke-width="2.2" marker-end="url(#arr-grn-006-2)"/>
  <text x="68" y="172" font-size="10" fill="#16a34a">A</text>
  <!-- 平行光发散，反向延长过 F1 -->
  <line x1="80" y1="172" x2="200" y2="172" stroke="#dc2626" stroke-width="1.4"/>
  <line x1="200" y1="172" x2="265" y2="136" stroke="#dc2626" stroke-width="1.4" marker-end="url(#arr-red-006-2)"/>
  <line x1="140" y1="205" x2="200" y2="172" stroke="#dc2626" stroke-width="1.2" stroke-dasharray="3,3"/>
  <!-- 过光心 -->
  <line x1="80" y1="172" x2="290" y2="230" stroke="#2563eb" stroke-width="1.4" marker-end="url(#arr-blue-006-2)"/>
  <!-- 正立虚像 -->
  <line x1="160" y1="205" x2="160" y2="194" stroke="#dc2626" stroke-width="2" marker-end="url(#arr-red-006-2)"/>
  <text x="155" y="189" font-size="10" fill="#dc2626">B(虚像)</text>
  <text x="275" y="185" font-size="10.5" font-weight="bold" fill="#111827">1/a + 1/b = 1/f</text>
  <text x="275" y="203" font-size="10.5" fill="#dc2626">m = |b| / a</text>
</svg>

#### 【日本考场规范分步推导】

上図の凸レンズにおいて，点 $\text{P}$ をレンズ上端の光線通過点とする。
1. $\triangle \text{OAA}' \propto \triangle \text{OBB}'$ より，倍率 $m$ は，
   $$m = \frac{\text{BB}'}{\text{AA}'} = \frac{b}{a} \quad \cdots\text{①}$$
2. また，$\triangle \text{OPF}_2 \propto \triangle \text{B}'\text{BF}_2$ かつ $\text{OP} = \text{AA}'$ であるから，
   $$\frac{\text{BB}'}{\text{AA}'} = \frac{\text{BB}'}{\text{OP}} = \frac{b - f}{f} \quad \cdots\text{②}$$
3. ①，② より，
   $$\frac{b}{a} = \frac{b - f}{f} \implies bf = ab - af$$
   両辺を $abf$ で割ると，**写像公式（レンズの公式）**が得られる：
   $$\frac{1}{a} + \frac{1}{b} = \frac{1}{f}$$

> 💡 讲师批注：EJU 必考组合透镜（2 枚のレンズ）！计算第二枚透镜的物距 $a_2$ 时，用「两透镜间距 $L$ 减去第一枚透镜的像距 $b_1$」，即 $a_2 = L - b_1$（若 $a_2 < 0$ 则为虚物，直接带负号代入公式依然成立）。

---

### 核心模型 3（教材 P.78–80 / 页码 77–79）：クーロンの法則・静電誘導・電場と電気力線

#### 【原书要点与翻译】
> **日文原书要点**：  
> - **クーロンの法則**：$F = k\dfrac{q_1 q_2}{r^2}$。  
> - **静電誘導**：導体に帯電体を近づけると引き寄せ合う現象。  
> - **電場**：$\vec{E} = \dfrac{\vec{F}}{q}$（$\vec{F} = q\vec{E}$），点電荷のまわりの電場 $E = k\dfrac{q}{r^2}$，電場の和 $\vec{E} = \vec{E}_1 + \vec{E}_2 + \cdots$。  
> - **電気力線の性質**：①正電荷から出て負電荷に入る；②途切れたり急に始まったりしない；③交わったり枝分かれしたりしない；④電場の強さ $E\text{ [N/C]}$ の場所に $1\text{ m}^2$ 当たり $E$ 本の密度で描く。

#### 【考点与模型定位】
**静电力与力学平衡综合（带电小球受力分析）＋ 电场叠加与电场线判读**。

#### 【多色矢量图解（SVG）】

<svg viewBox="0 0 420 260" width="420" height="260" xmlns="http://www.w3.org/2000/svg" style="background:#fafafa;border:1px solid #e5e7eb;border-radius:8px;">
  <defs>
    <marker id="arr-blue-006-3" markerWidth="7" markerHeight="7" refX="5" refY="3" orient="auto"><path d="M0,0 L0,6 L6,3 z" fill="#2563eb"/></marker>
    <marker id="arr-grn-006-3" markerWidth="7" markerHeight="7" refX="5" refY="3" orient="auto"><path d="M0,0 L0,6 L6,3 z" fill="#16a34a"/></marker>
    <marker id="arr-red-006-3" markerWidth="7" markerHeight="7" refX="5" refY="3" orient="auto"><path d="M0,0 L0,6 L6,3 z" fill="#dc2626"/></marker>
    <marker id="arr-blk-006-3" markerWidth="6" markerHeight="6" refX="4" refY="3" orient="auto"><path d="M0,0 L0,6 L5,3 z" fill="#111827"/></marker>
  </defs>
  <!-- 左半：静电感应与受力分析 -->
  <text x="16" y="20" font-size="11" font-weight="bold" fill="#111827">① 静電誘導と導体球の力のつりあい</text>
  <line x1="75" y1="35" x2="155" y2="35" stroke="#374151" stroke-width="2.5"/>
  <!-- 竖直虚线与角度 θ -->
  <line x1="115" y1="35" x2="115" y2="145" stroke="#9ca3af" stroke-dasharray="3,3"/>
  <!-- 绳子 -->
  <line x1="115" y1="35" x2="88" y2="132" stroke="#4b5563" stroke-width="1.6"/>
  <path d="M 115 72 A 37 37 0 0 1 105 70" fill="none" stroke="#dc2626" stroke-width="1.4"/>
  <text x="103" y="84" font-size="10" fill="#dc2626">θ</text>
  <!-- 负电棒 -->
  <rect x="18" y="142" width="38" height="22" rx="8" fill="#cbd5e1" stroke="#475569" stroke-width="1.3" transform="rotate(-30 37 153)"/>
  <text x="26" y="158" font-size="11" font-weight="bold" fill="#1e40af">− −</text>
  <!-- 导体球 -->
  <circle cx="88" cy="132" r="15" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>
  <text x="76" y="137" font-size="11" font-weight="bold" fill="#dc2626">+</text>
  <text x="93" y="136" font-size="11" font-weight="bold" fill="#2563eb">−</text>
  <!-- 受力箭头：重力(蓝)、张力(绿)、静电力(红) -->
  <line x1="88" y1="147" x2="88" y2="210" stroke="#2563eb" stroke-width="2" marker-end="url(#arr-blue-006-3)"/>
  <text x="94" y="205" font-size="11" fill="#2563eb">mg</text>
  <line x1="88" y1="132" x2="104" y2="76" stroke="#16a34a" stroke-width="2" marker-end="url(#arr-grn-006-3)"/>
  <text x="80" y="96" font-size="11" fill="#16a34a">T</text>
  <line x1="88" y1="132" x2="40" y2="132" stroke="#dc2626" stroke-width="2" marker-end="url(#arr-red-006-3)"/>
  <text x="38" y="123" font-size="11" fill="#dc2626">F (静電気力)</text>
  <text x="16" y="238" font-size="9.5" fill="#374151">近い側に逆符号(+)→引力が勝つ</text>

  <!-- 分隔线 -->
  <line x1="205" y1="12" x2="205" y2="248" stroke="#d1d5db" stroke-dasharray="4,4"/>

  <!-- 右半：电场线示例 -->
  <text x="220" y="20" font-size="11" font-weight="bold" fill="#111827">② 電気力線（正→負・平行板）</text>
  <!-- 异种电荷 -->
  <circle cx="250" cy="85" r="10" fill="#fee2e2" stroke="#dc2626" stroke-width="1.5"/>
  <text x="246" y="89" font-size="12" font-weight="bold" fill="#dc2626">+</text>
  <circle cx="370" cy="85" r="10" fill="#dbeafe" stroke="#2563eb" stroke-width="1.5"/>
  <text x="366" y="89" font-size="12" font-weight="bold" fill="#2563eb">−</text>
  <line x1="260" y1="85" x2="358" y2="85" stroke="#111827" stroke-width="1.3" marker-end="url(#arr-blk-006-3)"/>
  <path d="M 256 76 Q 310 38 364 76" fill="none" stroke="#111827" stroke-width="1.3" marker-end="url(#arr-blk-006-3)"/>
  <path d="M 256 94 Q 310 132 364 94" fill="none" stroke="#111827" stroke-width="1.3" marker-end="url(#arr-blk-006-3)"/>
  <path d="M 250 75 Q 310 15 370 75" fill="none" stroke="#111827" stroke-width="1.1" stroke-dasharray="3,2"/>

  <!-- 平行板一様電場 -->
  <rect x="240" y="155" width="12" height="75" fill="#fee2e2" stroke="#dc2626" stroke-width="1.3"/>
  <text x="242" y="175" font-size="10" fill="#dc2626">+</text>
  <text x="242" y="196" font-size="10" fill="#dc2626">+</text>
  <text x="242" y="218" font-size="10" fill="#dc2626">+</text>
  <rect x="368" y="155" width="12" height="75" fill="#dbeafe" stroke="#2563eb" stroke-width="1.3"/>
  <text x="371" y="175" font-size="10" fill="#2563eb">−</text>
  <text x="371" y="196" font-size="10" fill="#2563eb">−</text>
  <text x="371" y="218" font-size="10" fill="#2563eb">−</text>
  <line x1="254" y1="168" x2="365" y2="168" stroke="#111827" stroke-width="1.3" marker-end="url(#arr-blk-006-3)"/>
  <line x1="254" y1="192" x2="365" y2="192" stroke="#111827" stroke-width="1.3" marker-end="url(#arr-blk-006-3)"/>
  <line x1="254" y1="216" x2="365" y2="216" stroke="#111827" stroke-width="1.3" marker-end="url(#arr-blk-006-3)"/>
  <text x="282" y="245" font-size="10" fill="#111827">一様電場 E = 一定</text>
</svg>

#### 【日本考场规范解析与教材勘误】

1. **静電誘導の仕組み**：帯電していない導体球に負に帯電した棒を近づけると，導体内の自由電子が反発して遠い側へ移動し，近い側が正，遠い側が負に帯電する。近い側の引力の方が遠い側の斥力より強いため，全体として引き寄せられる。
2. **電場の定義とガウスの法則への橋渡し**：点電荷 $Q$ から出る電気力線の総本数 $N$ は，半径 $r$ の球面上で面積 $4\pi r^2$ と電場 $E = k\dfrac{Q}{r^2}$ の積になるため，
   $$N = E \cdot 4\pi r^2 = 4\pi k Q = \frac{Q}{\varepsilon_0}$$
   この「総本数 $N = 4\pi k Q = \dfrac{Q}{\varepsilon_0}$」は平行板コンデンサーの電場 $E = \dfrac{Q}{\varepsilon_0 S}$ を一瞬で導く最強の武器となる。

> 💡 讲师批注：**发现教材勘误（P.79 / 页码 78）**：原文第一行印作「なんらかの電荷 ($q_1$) を置いたときに…」，此处下标 `1` 为从上一页库仑定律复制残留的印刷笔误，应改为 $q$。此外，教材 P.78（页码 77）库仑定律写作 $F = k\dfrac{q_1 q_2}{r^2}$，授课时请提醒学生：求力的**大小**时应加上绝对值 $F = k\dfrac{|q_1 q_2|}{r^2}$。

---

### 核心模型 4（教材 P.81–82 / 页码 80–81）：電位・$V=Ed$・点電荷による電位と等電位面

#### 【原书要点与翻译】
> **日文原书要点**：  
> - 静電気力は保存力であり，仕事は経路によらない（$\text{A} \to \text{B}$ と $\text{A} \to \text{B}' \to \text{B}$ は同じ）。  
> - **電位**：$+1\text{ C}$ の電荷（正の単位電荷）の位置エネルギー。一様電場では $V = Ed$。  
> - **点電荷による電位**：$V = k\dfrac{q}{r}$。  
> - **等電位面の性質**：①等電位面に沿って動かしても仕事は $0$；②電気力線と常に直交する；③等電位面が密なところは電場が強い。

#### 【考点与模型定位】
**电势能与静电力做功（$W_{\text{電}} = q(V_A - V_B)$）＋ 等势面与电场线几何判读**。

#### 【多色矢量图解（SVG）】

<svg viewBox="0 0 420 260" width="420" height="260" xmlns="http://www.w3.org/2000/svg" style="background:#fafafa;border:1px solid #e5e7eb;border-radius:8px;">
  <defs>
    <marker id="arr-red-006-4" markerWidth="7" markerHeight="7" refX="5" refY="3" orient="auto"><path d="M0,0 L0,6 L6,3 z" fill="#dc2626"/></marker>
    <marker id="arr-blk-006-4" markerWidth="7" markerHeight="7" refX="5" refY="3" orient="auto"><path d="M0,0 L0,6 L6,3 z" fill="#111827"/></marker>
    <marker id="arr-blue-006-4" markerWidth="7" markerHeight="7" refX="5" refY="3" orient="auto"><path d="M0,0 L0,6 L6,3 z" fill="#2563eb"/></marker>
  </defs>
  <!-- 左半：一様電場中的电势与路径无关 -->
  <text x="15" y="20" font-size="11" font-weight="bold" fill="#111827">① 一様電場と電位 V = Ed（保存力）</text>
  <!-- 等势面竖线 -->
  <line x1="45" y1="40" x2="45" y2="180" stroke="#2563eb" stroke-width="1.4" stroke-dasharray="4,3"/>
  <line x1="110" y1="40" x2="110" y2="180" stroke="#2563eb" stroke-width="1.4" stroke-dasharray="4,3"/>
  <line x1="175" y1="40" x2="175" y2="180" stroke="#2563eb" stroke-width="1.4" stroke-dasharray="4,3"/>
  <text x="36" y="195" font-size="10" fill="#2563eb">V_A</text>
  <text x="166" y="195" font-size="10" fill="#2563eb">V_B</text>
  <!-- 电场线 -->
  <line x1="25" y1="60" x2="195" y2="60" stroke="#111827" stroke-width="1.2" marker-end="url(#arr-blk-006-4)"/>
  <line x1="25" y1="110" x2="195" y2="110" stroke="#111827" stroke-width="1.2" marker-end="url(#arr-blk-006-4)"/>
  <line x1="25" y1="160" x2="195" y2="160" stroke="#111827" stroke-width="1.2" marker-end="url(#arr-blk-006-4)"/>
  <text x="180" y="53" font-size="11" font-weight="bold" fill="#111827">E</text>
  <!-- 路径 A -> B (曲线) vs A -> B' -> B -->
  <circle cx="45" cy="75" r="3.5" fill="#dc2626"/><text x="30" y="75" font-size="11" font-weight="bold" fill="#dc2626">A</text>
  <circle cx="175" cy="75" r="3.5" fill="#16a34a"/><text x="180" y="78" font-size="10" fill="#16a34a">B'</text>
  <circle cx="175" cy="145" r="3.5" fill="#dc2626"/><text x="181" y="150" font-size="11" font-weight="bold" fill="#dc2626">B</text>
  <path d="M 45 75 Q 115 95 175 145" fill="none" stroke="#dc2626" stroke-width="1.8" marker-end="url(#arr-red-006-4)"/>
  <line x1="45" y1="75" x2="170" y2="75" stroke="#16a34a" stroke-width="1.6" stroke-dasharray="4,2" marker-end="url(#arr-blue-006-4)"/>
  <line x1="175" y1="75" x2="175" y2="140" stroke="#16a34a" stroke-width="1.6" stroke-dasharray="4,2"/>
  <text x="98" y="70" font-size="10" fill="#16a34a">d</text>
  <text x="18" y="220" font-size="10" fill="#111827">W(A→B) = W(A→B') + 0 = qEd</text>
  <text x="18" y="238" font-size="10" fill="#dc2626">電位差 V = V_A − V_B = Ed</text>

  <!-- 分隔线 -->
  <line x1="212" y1="12" x2="212" y2="248" stroke="#d1d5db" stroke-dasharray="4,4"/>

  <!-- 右半：点电荷等势面与电场线正交 -->
  <text x="225" y="20" font-size="11" font-weight="bold" fill="#111827">② 点電荷の等電位面 (V = kq/r)</text>
  <!-- 同心圆等势面（内密外疏） -->
  <circle cx="315" cy="122" r="24" fill="none" stroke="#2563eb" stroke-width="1.5"/>
  <circle cx="315" cy="122" r="46" fill="none" stroke="#2563eb" stroke-width="1.3"/>
  <circle cx="315" cy="122" r="76" fill="none" stroke="#2563eb" stroke-width="1.1"/>
  <!-- 放射状电场线 -->
  <line x1="315" y1="122" x2="315" y2="38" stroke="#111827" stroke-width="1.2" marker-end="url(#arr-blk-006-4)"/>
  <line x1="315" y1="122" x2="315" y2="206" stroke="#111827" stroke-width="1.2" marker-end="url(#arr-blk-006-4)"/>
  <line x1="315" y1="122" x2="230" y2="122" stroke="#111827" stroke-width="1.2" marker-end="url(#arr-blk-006-4)"/>
  <line x1="315" y1="122" x2="400" y2="122" stroke="#111827" stroke-width="1.2" marker-end="url(#arr-blk-006-4)"/>
  <line x1="315" y1="122" x2="375" y2="62" stroke="#111827" stroke-width="1.2" marker-end="url(#arr-blk-006-4)"/>
  <line x1="315" y1="122" x2="255" y2="182" stroke="#111827" stroke-width="1.2" marker-end="url(#arr-blk-006-4)"/>
  <!-- 中心正电荷 -->
  <circle cx="315" cy="122" r="10" fill="#fee2e2" stroke="#dc2626" stroke-width="1.6"/>
  <text x="309" y="126" font-size="11" font-weight="bold" fill="#dc2626">+q</text>
  <!-- 标注 -->
  <text x="225" y="226" font-size="10" fill="#2563eb">● 青円：等電位面（常に直交）</text>
  <text x="225" y="242" font-size="10" fill="#111827">● 密なほど電場が強い（r小→E大）</text>
</svg>

#### 【日本考场规范解析】

- **電場（ベクトル）と電位（スカラー）の対比**：複数の点電荷があるとき，合成電場 $\vec{E}$ は**ベクトル和**だが，合成電位 $V$ は符号を含めた**単なるスカラー和（足し算）** $V = k\dfrac{q_1}{r_1} + k\dfrac{q_2}{r_2} + \cdots$ で求められる。
- **静電気力のする仕事と外力のする仕事**：電荷 $q$ を電位 $V_A$ の点から $V_B$ の点へゆっくり運ぶとき，
  - 静電気力のする仕事：$W_{\text{静}} = q(V_A - V_B)$
  - 外力のする仕事：$W_{\text{外}} = q(V_B - V_A) = \Delta U$

> 💡 讲师批注：EJU 必考易错点——审清题目问的是「静電気力がする仕事（静电力做功：$q(V_{\text{始}} - V_{\text{終}})$）」还是「外力がする仕事（外力做功：$q(V_{\text{終}} - V_{\text{始}})$）」，两者符号恰好相反！

---

### 核心模型 5（教材 P.83–84 / 页码 82–83）：平行板コンデンサーと誘電体挿入の二状態比較

#### 【原书要点与翻译】
> **日文原书要点**：  
> - 電気容量 $C$：$Q = CV$，$C = \varepsilon\dfrac{S}{d}$，比誘電率 $\varepsilon_r = \dfrac{\varepsilon}{\varepsilon_0}$。  
> - 極板間に誘電体を挿入すると**誘電分極**が起こり，元の電場が弱められる。電源接続時・切断時のどちらでも電気容量は $C = \varepsilon_r C_0$ となる。

#### 【考点与模型定位】
**平行板电容器动态分析（插入电介质 / 改变极板间距 $d$ 时，接电源 vs 断电源的 $C, Q, V, E, U$ 变化规律）**——EJU 电学最经典选择题模型。

#### 【多色矢量图解（SVG）】

<svg viewBox="0 0 420 260" width="420" height="260" xmlns="http://www.w3.org/2000/svg" style="background:#fafafa;border:1px solid #e5e7eb;border-radius:8px;">
  <defs>
    <marker id="arr-blk-006-5" markerWidth="7" markerHeight="7" refX="5" refY="3" orient="auto"><path d="M0,0 L0,6 L6,3 z" fill="#111827"/></marker>
    <marker id="arr-red-006-5" markerWidth="7" markerHeight="7" refX="5" refY="3" orient="auto"><path d="M0,0 L0,6 L6,3 z" fill="#dc2626"/></marker>
  </defs>
  <text x="18" y="20" font-size="11.5" font-weight="bold" fill="#111827">平行板コンデンサーへの誘電体挿入（誘電分極）</text>
  <!-- 上极板 (+) -->
  <rect x="35" y="45" width="165" height="14" fill="#fee2e2" stroke="#dc2626" stroke-width="1.5"/>
  <text x="48" y="56" font-size="11" font-weight="bold" fill="#dc2626">+   +   +   +   +   +   +   +</text>
  <line x1="117" y1="30" x2="117" y2="45" stroke="#374151" stroke-width="1.6"/>
  <!-- 电介质 -->
  <rect x="42" y="65" width="151" height="90" fill="#e0f2fe" stroke="#2563eb" stroke-width="1.4"/>
  <text x="52" y="79" font-size="11" font-weight="bold" fill="#2563eb">−    −    −    −    −    −</text>
  <text x="52" y="149" font-size="11" font-weight="bold" fill="#dc2626">+    +    +    +    +    +</text>
  <!-- 原电场向下，极化内电场向上 -->
  <line x1="88" y1="86" x2="88" y2="132" stroke="#111827" stroke-width="2" marker-end="url(#arr-blk-006-5)"/>
  <text x="52" y="114" font-size="10.5" fill="#111827">E₀ (元)</text>
  <line x1="145" y1="132" x2="145" y2="96" stroke="#dc2626" stroke-width="2" marker-end="url(#arr-red-006-5)"/>
  <text x="150" y="114" font-size="10.5" fill="#dc2626">E' (分極)</text>
  <!-- 下极板 (-) -->
  <rect x="35" y="161" width="165" height="14" fill="#dbeafe" stroke="#2563eb" stroke-width="1.5"/>
  <text x="48" y="172" font-size="11" font-weight="bold" fill="#2563eb">−   −   −   −   −   −   −   −</text>
  <line x1="117" y1="175" x2="117" y2="195" stroke="#374151" stroke-width="1.6"/>
  <text x="206" y="112" font-size="10.5" font-style="italic" fill="#374151">d</text>
  <text x="35" y="218" font-size="10.5" fill="#111827">合成電場 E = E₀ − E' = E₀ / ε_r</text>
  <text x="35" y="238" font-size="10.5" font-weight="bold" fill="#2563eb">C = ε_r ε₀ S/d = ε_r C₀</text>

  <!-- 右侧：双态对比卡片 -->
  <rect x="235" y="42" width="172" height="92" rx="6" fill="#fff" stroke="#16a34a" stroke-width="1.4"/>
  <text x="245" y="60" font-size="10.5" font-weight="bold" fill="#16a34a">Case A: 電源接続（V 一定）</text>
  <text x="245" y="78" font-size="10" fill="#111827">• C → ε_r 倍</text>
  <text x="245" y="94" font-size="10" fill="#111827">• Q = CV → ε_r 倍（充電）</text>
  <text x="245" y="110" font-size="10" fill="#111827">• E = V/d → 変化なし</text>
  <text x="245" y="126" font-size="10" fill="#111827">• U = ½CV² → ε_r 倍</text>

  <rect x="235" y="146" width="172" height="92" rx="6" fill="#fff" stroke="#dc2626" stroke-width="1.4"/>
  <text x="245" y="164" font-size="10.5" font-weight="bold" fill="#dc2626">Case B: 電源切断（Q 一定）</text>
  <text x="245" y="182" font-size="10" fill="#111827">• C → ε_r 倍</text>
  <text x="245" y="198" font-size="10" fill="#111827">• V = Q/C → 1/ε_r 倍</text>
  <text x="245" y="214" font-size="10" fill="#111827">• E = V/d → 1/ε_r 倍</text>
  <text x="245" y="230" font-size="10" fill="#111827">• U = Q²/(2C) → 1/ε_r 倍</text>
</svg>

#### 【日本考场规范解析】

1. **電源につないだまま挿入（$V$ 一定）**：$C = \varepsilon_r C_0$ より，$Q = CV = \varepsilon_r Q_0$，$U = \dfrac{1}{2}CV^2 = \varepsilon_r U_0$。
2. **電源を切ってから挿入（$Q$ 一定）**：孤立極板の電荷保存より $Q = Q_0$。したがって $V = \dfrac{Q_0}{C} = \dfrac{V_0}{\varepsilon_r}$，$E = \dfrac{V}{d} = \dfrac{E_0}{\varepsilon_r}$，$U = \dfrac{Q_0^2}{2C} = \dfrac{U_0}{\varepsilon_r}$。

> 💡 讲师批注：极易混淆的问题——“断开电源后插入电介质，静电能 $U$ 减少了，能量去哪儿了？”答案：极化电荷受极板吸引，极板对电介质做正功（把电介质往里吸），因此静电能转化为**外力做负功（或电介质的动能）**！

---

### 核心模型 6（教材 P.85–86 / 页码 84–85）：静電エネルギー・串並列接続と極板分割法

#### 【原书要点与翻译】
> **日文原书要点**：  
> - **静電エネルギー**：$U = \dfrac{1}{2}QV = \dfrac{1}{2}CV^2 = \dfrac{Q^2}{2C}$（$V$-$Q$ グラフの三角形の面積）。  
> - **合成容量**：並列 $C = C_1 + C_2$，直列 $\dfrac{1}{C} = \dfrac{1}{C_1} + \dfrac{1}{C_2}$。  
> - **極板分割**：極板間に挟む誘電体が直方体で極板の形と同じなら，電気力線の形が変わらないので横方向（並列）にも縦方向（直列）にも分割できる。

#### 【考点与模型定位】
**部分填充介质/导体的电容器等效拆解（横切并联、竖切串联）**——EJU 大题必考技巧！

#### 【多色矢量图解（SVG）】

<svg viewBox="0 0 420 260" width="420" height="260" xmlns="http://www.w3.org/2000/svg" style="background:#fafafa;border:1px solid #e5e7eb;border-radius:8px;">
  <defs>
    <marker id="arr-blk-006-6" markerWidth="7" markerHeight="7" refX="5" refY="3" orient="auto"><path d="M0,0 L0,6 L6,3 z" fill="#111827"/></marker>
  </defs>
  <!-- 左：V-Q 图像求静电能 -->
  <text x="15" y="20" font-size="11" font-weight="bold" fill="#111827">① 静電エネルギー（V-Q 面積）</text>
  <line x1="35" y1="190" x2="180" y2="190" stroke="#374151" stroke-width="1.6" marker-end="url(#arr-blk-006-6)"/>
  <line x1="35" y1="190" x2="35" y2="45" stroke="#374151" stroke-width="1.6" marker-end="url(#arr-blk-006-6)"/>
  <text x="148" y="206" font-size="10" fill="#111827">電荷 Q</text>
  <text x="12" y="42" font-size="10" fill="#111827">V</text>
  <polygon points="35,190 150,190 150,70" fill="#dbeafe" stroke="#2563eb" stroke-width="1.8"/>
  <text x="145" y="203" font-size="10" fill="#2563eb">Q</text>
  <text x="20" y="75" font-size="10" fill="#2563eb">V</text>
  <line x1="35" y1="70" x2="150" y2="70" stroke="#9ca3af" stroke-dasharray="3,3"/>
  <text x="72" y="160" font-size="11" font-weight="bold" fill="#1e40af">U = ½QV</text>
  <text x="18" y="226" font-size="10" fill="#374151">傾き = 1/C，面積 = 静電エネルギー</text>
  <text x="18" y="242" font-size="10" fill="#dc2626">※ 電池の仕事は QV（半分は熱損失）</text>

  <!-- 分隔线 -->
  <line x1="205" y1="12" x2="205" y2="248" stroke="#d1d5db" stroke-dasharray="4,4"/>

  <!-- 右上：横向分割 -> 并联 -->
  <text x="218" y="20" font-size="11" font-weight="bold" fill="#111827">② 面積分割（横）＝ 並列接続</text>
  <line x1="225" y1="48" x2="295" y2="48" stroke="#111827" stroke-width="2"/>
  <line x1="225" y1="82" x2="295" y2="82" stroke="#111827" stroke-width="2"/>
  <rect x="225" y="49" width="35" height="32" fill="#93c5fd" opacity="0.7"/>
  <text x="234" y="69" font-size="10" fill="#1e3a8a">ε_r</text>
  <text x="270" y="69" font-size="10" fill="#6b7280">空</text>
  <text x="303" y="70" font-size="13" font-weight="bold" fill="#111827">=</text>
  <!-- 并联等效 -->
  <polyline points="355,34 355,44 330,44 330,56" fill="none" stroke="#111827" stroke-width="1.3"/>
  <polyline points="355,44 385,44 385,56" fill="none" stroke="#111827" stroke-width="1.3"/>
  <rect x="320" y="56" width="20" height="18" fill="#93c5fd"/>
  <line x1="318" y1="56" x2="342" y2="56" stroke="#111827" stroke-width="2"/>
  <line x1="318" y1="74" x2="342" y2="74" stroke="#111827" stroke-width="2"/>
  <line x1="373" y1="56" x2="397" y2="56" stroke="#111827" stroke-width="2"/>
  <line x1="373" y1="74" x2="397" y2="74" stroke="#111827" stroke-width="2"/>
  <polyline points="330,74 330,86 385,86 385,74" fill="none" stroke="#111827" stroke-width="1.3"/>
  <line x1="355" y1="86" x2="355" y2="96" stroke="#111827" stroke-width="1.3"/>
  <text x="225" y="112" font-size="10" fill="#16a34a">C = C₁ + C₂ （電位差 V 共通）</text>

  <!-- 右下：纵向分割 -> 串联 -->
  <text x="218" y="142" font-size="11" font-weight="bold" fill="#111827">③ 間隔分割（縦）＝ 直列接続</text>
  <line x1="225" y1="165" x2="295" y2="165" stroke="#111827" stroke-width="2"/>
  <line x1="225" y1="205" x2="295" y2="205" stroke="#111827" stroke-width="2"/>
  <rect x="225" y="166" width="70" height="20" fill="#93c5fd" opacity="0.7"/>
  <text x="252" y="180" font-size="10" fill="#1e3a8a">ε_r</text>
  <text x="252" y="200" font-size="10" fill="#6b7280">空</text>
  <text x="303" y="190" font-size="13" font-weight="bold" fill="#111827">=</text>
  <!-- 串联等效 -->
  <line x1="360" y1="152" x2="360" y2="162" stroke="#111827" stroke-width="1.3"/>
  <rect x="338" y="162" width="44" height="16" fill="#93c5fd"/>
  <line x1="335" y1="162" x2="385" y2="162" stroke="#111827" stroke-width="2"/>
  <line x1="335" y1="178" x2="385" y2="178" stroke="#111827" stroke-width="2"/>
  <line x1="360" y1="178" x2="360" y2="196" stroke="#111827" stroke-width="1.3"/>
  <line x1="335" y1="196" x2="385" y2="196" stroke="#111827" stroke-width="2"/>
  <line x1="335" y1="212" x2="385" y2="212" stroke="#111827" stroke-width="2"/>
  <line x1="360" y1="212" x2="360" y2="222" stroke="#111827" stroke-width="1.3"/>
  <text x="225" y="242" font-size="10" fill="#dc2626">1/C = 1/C₁ + 1/C₂ （電気量 Q 共通）</text>
</svg>

#### 【日本考场规范解析】

- **導体板を挿入した場合の秒殺テクニック**：極板間に厚さ $a$ の**導体板**（金属板）を挿入すると，導体内部は電場 $0$（等電位）となるため，実効的な極板間隔が $d - a$ に縮んだことと完全に等価であり，$C = \varepsilon_0\dfrac{S}{d - a}$ となる（導体板を上下どの位置に置いても同じ！）。

> 💡 讲师批注：把电容充电过程中**电池做的功 $W_{\text{電}} = QV$** 与**电容器储存的静电能 $U = \frac{1}{2}QV$** 对比强调：充电时无论电阻多大，总有一半能量（$\frac{1}{2}QV$）在回路电阻上变成焦耳热耗散掉！这是 EJU 能量守恒大题的必考点。

---

### 核心模型 7（教材 P.87–89 / 页码 86–88）：電流のミクロモデル・オームの法則・抵抗率の温度変化とジュール熱

#### 【原书要点与翻译】
> **日文原书要点**：  
> - **電流**：$I = \dfrac{q}{t} = envS$（電流の向きは自由電子の動く向きと逆）。  
> - **オームの法則と抵抗率**：$V = RI$，$R = \rho\dfrac{l}{S}$，温度変化 $\rho = \rho_0(1 + \alpha t)$。  
> - **ジュールの法則・電力・電力量**：$P = \dfrac{W}{t} = IV = I^2 R = \dfrac{V^2}{R}$，$Q = W = Pt = IVt = I^2 Rt = \dfrac{V^2}{R}t$。

#### 【考点与模型定位】
**自由电子微观推导欧姆定律（$I = envS \to R = \rho\frac{l}{S}$）＋ 非线性元件（電球）$I$-$V$ 曲线特性**。

#### 【多色矢量图解（SVG）】

<svg viewBox="0 0 420 260" width="420" height="260" xmlns="http://www.w3.org/2000/svg" style="background:#fafafa;border:1px solid #e5e7eb;border-radius:8px;">
  <defs>
    <marker id="arr-blk-006-7" markerWidth="7" markerHeight="7" refX="5" refY="3" orient="auto"><path d="M0,0 L0,6 L6,3 z" fill="#111827"/></marker>
    <marker id="arr-red-006-7" markerWidth="7" markerHeight="7" refX="5" refY="3" orient="auto"><path d="M0,0 L0,6 L6,3 z" fill="#dc2626"/></marker>
    <marker id="arr-blue-006-7" markerWidth="7" markerHeight="7" refX="5" refY="3" orient="auto"><path d="M0,0 L0,6 L6,3 z" fill="#2563eb"/></marker>
  </defs>
  <!-- 左半：电流微观模型 I = envS -->
  <text x="15" y="20" font-size="11" font-weight="bold" fill="#111827">① 電流のミクロモデル（I = envS）</text>
  <!-- 圆柱导线 -->
  <rect x="30" y="75" width="160" height="54" fill="#e5e7eb" stroke="#4b5563" stroke-width="1.3"/>
  <ellipse cx="70" cy="102" rx="10" ry="27" fill="#dbeafe" stroke="#2563eb" stroke-width="1.6"/>
  <ellipse cx="150" cy="102" rx="10" ry="27" fill="none" stroke="#2563eb" stroke-width="1.4" stroke-dasharray="3,2"/>
  <text x="64" y="143" font-size="10.5" fill="#2563eb">断面積 S</text>
  <!-- 1秒移动距离 v -->
  <line x1="70" y1="62" x2="150" y2="62" stroke="#111827" stroke-width="1.3"/>
  <text x="92" y="56" font-size="10.5" fill="#111827">v·1s = v [m]</text>
  <!-- 自由电子向左，电流向右 -->
  <circle cx="112" cy="102" r="5" fill="#2563eb"/>
  <text x="109" y="105" font-size="9" font-weight="bold" fill="#fff">−</text>
  <line x1="106" y1="102" x2="78" y2="102" stroke="#111827" stroke-width="1.6" stroke-dasharray="4,2" marker-end="url(#arr-blk-006-7)"/>
  <text x="84" y="96" font-size="10" fill="#111827">v (電子)</text>
  <line x1="75" y1="168" x2="155" y2="168" stroke="#dc2626" stroke-width="2" marker-end="url(#arr-red-006-7)"/>
  <text x="86" y="162" font-size="10.5" font-weight="bold" fill="#dc2626">電流 I の向き</text>
  <text x="18" y="205" font-size="10" fill="#111827">1秒間の通過体積 = vS</text>
  <text x="18" y="222" font-size="10" fill="#111827">通過電子数 = nvS → I = envS</text>
  <text x="18" y="240" font-size="10" fill="#2563eb">抵抗率 ρ = k/(e²n)，R = ρl/S</text>

  <!-- 分隔线 -->
  <line x1="210" y1="12" x2="210" y2="248" stroke="#d1d5db" stroke-dasharray="4,4"/>

  <!-- 右半：非オーム抵抗（温度上升电阻增大）I-V 曲线 -->
  <text x="222" y="20" font-size="11" font-weight="bold" fill="#111827">② 金属・電球の I-V 特性曲線</text>
  <line x1="240" y1="190" x2="395" y2="190" stroke="#374151" stroke-width="1.6" marker-end="url(#arr-blk-006-7)"/>
  <line x1="240" y1="190" x2="240" y2="45" stroke="#374151" stroke-width="1.6" marker-end="url(#arr-blk-006-7)"/>
  <text x="372" y="206" font-size="10" fill="#111827">電圧 V</text>
  <text x="218" y="44" font-size="10" fill="#111827">I</text>
  <!-- 理想欧姆直线 -->
  <line x1="240" y1="190" x2="335" y2="55" stroke="#9ca3af" stroke-width="1.4" stroke-dasharray="4,3"/>
  <text x="315" y="52" font-size="9.5" fill="#6b7280">R 一定 (傾き1/R)</text>
  <!-- 实际弯曲曲线 -->
  <path d="M 240 190 Q 275 110 385 88" fill="none" stroke="#dc2626" stroke-width="2.2"/>
  <text x="305" y="118" font-size="10" fill="#dc2626">温度↑ → 陽イオン振動↑</text>
  <text x="305" y="134" font-size="10" fill="#dc2626">→ ρ↑・R↑ → 傾き↓</text>
  <text x="224" y="226" font-size="10" fill="#111827">ρ = ρ₀(1 + αt)</text>
  <text x="224" y="242" font-size="10" fill="#2563eb">ジュール熱 Q = IVt = I²Rt = V²t/R</text>
</svg>

#### 【日本考场规范推导与教材勘误补全】

導線内の自由電子（電荷 $-e$）が電場 $E = \dfrac{V}{l}$ から受ける静電気力 $eE$ と，陽イオンとの衝突による比例抵抗力 $kv$ がつり合って一定速度 $v$ で進むとすると，
$$eE = kv \implies v = \frac{eE}{k} = \frac{eV}{kl}$$
これを電流の式 $I = envS$ に代入すると，
$$I = en\left(\frac{eV}{kl}\right)S = \frac{e^2 n S}{kl} V \implies V = \left(\frac{k}{e^2 n}\right)\frac{l}{S} I$$
ここでかっこ内の量 $\rho = \dfrac{k}{e^2 n}$ を**抵抗率（比抵抗）**とおけば，オームの法則 $V = RI$ および $R = \rho\dfrac{l}{S}$ が導かれる。

> 💡 讲师批注：**发现教材勘误（P.88 / 页码 87）**：教材原文直接提到「『電気抵抗』で示した通り，$k$ は流れを妨害する力の係数で，$n$ は自由電子の数密度です。…このかっこ内の量を抵抗率といい $\rho$ で表します」，但本教材并未收录上面这 3 行微观推导，导致 $k$ 与“括号内的量”悬空无出处。授课时请直接用上面的 3 行板书替学生补齐逻辑闭环！

---

### 核心模型 8（教材 P.90 / 页码 89）：キルヒホッフの法則（第1法則・第2法則）

#### 【原书要点与翻译】
> **日文原书要点**：  
> - **キルヒホッフの第1法則**：電気回路の任意の分岐点について，そこに流れ込む電流の和は，そこから流れ出る電流の和に等しい。  
> - **キルヒホッフの第2法則**：電気回路の任意の一回りの閉じた経路について，電位差の和は $0$ である（図において $V_3 = V_4$，$V_1 = V_2 + V_3$）。

#### 【考点与模型定位】
**复杂直流电路多回路方程列写（KCL 节点电流 ＋ KVL 回路电势平衡）**。

#### 【多色矢量图解（SVG）】

<svg viewBox="0 0 420 260" width="420" height="260" xmlns="http://www.w3.org/2000/svg" style="background:#fafafa;border:1px solid #e5e7eb;border-radius:8px;">
  <defs>
    <marker id="arr-red-006-8" markerWidth="7" markerHeight="7" refX="5" refY="3" orient="auto"><path d="M0,0 L0,6 L6,3 z" fill="#dc2626"/></marker>
    <marker id="arr-blue-006-8" markerWidth="7" markerHeight="7" refX="5" refY="3" orient="auto"><path d="M0,0 L0,6 L6,3 z" fill="#2563eb"/></marker>
    <marker id="arr-grn-006-8" markerWidth="7" markerHeight="7" refX="5" refY="3" orient="auto"><path d="M0,0 L0,6 L6,3 z" fill="#16a34a"/></marker>
  </defs>
  <!-- 左半：基尔霍夫第一定律 KCL -->
  <text x="16" y="22" font-size="11" font-weight="bold" fill="#111827">① キルヒホッフの第1法則（KCL）</text>
  <line x1="30" y1="120" x2="180" y2="120" stroke="#374151" stroke-width="2"/>
  <line x1="105" y1="45" x2="105" y2="195" stroke="#374151" stroke-width="2"/>
  <circle cx="105" cy="120" r="4.5" fill="#111827"/>
  <!-- 流入 I1, I2 (红) -->
  <line x1="45" y1="112" x2="90" y2="112" stroke="#dc2626" stroke-width="2" marker-end="url(#arr-red-006-8)"/>
  <text x="58" y="104" font-size="11" font-weight="bold" fill="#dc2626">I₁</text>
  <line x1="114" y1="58" x2="114" y2="105" stroke="#dc2626" stroke-width="2" marker-end="url(#arr-red-006-8)"/>
  <text x="122" y="84" font-size="11" font-weight="bold" fill="#dc2626">I₂</text>
  <!-- 流出 I3, I4 (蓝) -->
  <line x1="114" y1="135" x2="114" y2="182" stroke="#2563eb" stroke-width="2" marker-end="url(#arr-blue-006-8)"/>
  <text x="122" y="165" font-size="11" font-weight="bold" fill="#2563eb">I₃</text>
  <line x1="120" y1="112" x2="165" y2="112" stroke="#2563eb" stroke-width="2" marker-end="url(#arr-blue-006-8)"/>
  <text x="142" y="104" font-size="11" font-weight="bold" fill="#2563eb">I₄</text>
  <text x="42" y="222" font-size="11.5" font-weight="bold" fill="#111827">I₁ + I₂ = I₃ + I₄</text>
  <text x="36" y="240" font-size="10" fill="#6b7280">（電荷保存：流入和＝流出和）</text>

  <!-- 分隔线 -->
  <line x1="205" y1="12" x2="205" y2="248" stroke="#d1d5db" stroke-dasharray="4,4"/>

  <!-- 右半：基尔霍夫第二定律 KVL -->
  <text x="218" y="22" font-size="11" font-weight="bold" fill="#111827">② キルヒホッフの第2法則（KVL）</text>
  <!-- 外框回路 -->
  <polyline points="235,175 235,95 255,95" fill="none" stroke="#374151" stroke-width="1.6"/>
  <!-- 电阻 V2 -->
  <rect x="255" y="88" width="32" height="14" fill="#fef3c7" stroke="#b45309" stroke-width="1.4"/>
  <text x="264" y="116" font-size="10" fill="#b45309">V₂</text>
  <line x1="287" y1="95" x2="310" y2="95" stroke="#374151" stroke-width="1.6"/>
  <!-- 并联分支：上 V4，下 V3 -->
  <polyline points="310,95 310,60 332,60" fill="none" stroke="#374151" stroke-width="1.6"/>
  <rect x="332" y="53" width="32" height="14" fill="#fef3c7" stroke="#b45309" stroke-width="1.4"/>
  <text x="342" y="80" font-size="10" fill="#b45309">V₄</text>
  <polyline points="364,60 390,60 390,175 318,175" fill="none" stroke="#374151" stroke-width="1.6"/>
  <line x1="310" y1="95" x2="332" y2="95" stroke="#374151" stroke-width="1.6"/>
  <rect x="332" y="88" width="32" height="14" fill="#fef3c7" stroke="#b45309" stroke-width="1.4"/>
  <text x="342" y="116" font-size="10" fill="#b45309">V₃</text>
  <line x1="364" y1="95" x2="390" y2="95" stroke="#374151" stroke-width="1.6"/>
  <!-- 电源 V1 -->
  <line x1="235" y1="175" x2="308" y2="175" stroke="#374151" stroke-width="1.6"/>
  <line x1="308" y1="163" x2="308" y2="187" stroke="#dc2626" stroke-width="2.2"/>
  <line x1="316" y1="168" x2="316" y2="182" stroke="#2563eb" stroke-width="3"/>
  <text x="306" y="156" font-size="10.5" font-weight="bold" fill="#dc2626">V₁</text>
  <!-- 顺时针环路箭头 -->
  <path d="M 275 148 A 28 16 0 1 1 315 135" fill="none" stroke="#16a34a" stroke-width="1.5" stroke-dasharray="4,2" marker-end="url(#arr-grn-006-8)"/>
  <text x="235" y="218" font-size="11" font-weight="bold" fill="#111827">V₁ = V₂ + V₃， V₃ = V₄</text>
  <text x="235" y="238" font-size="10" fill="#16a34a">（一閉回路：Σ起電力 = Σ電圧降下）</text>
</svg>

#### 【日本考场规范解析】

- **第1法則の立式**：分岐点において，流入電流と流出電流を等置する：
  $$I_1 + I_2 = I_3 + I_4$$
- **第2法則の立式**：「時計回り」など 1 周の向きを決め，電池の負極 $\to$ 正極を通過するときは $+E$（電位上昇），抵抗を電流と同じ向きに通過するときは $-RI$（電位降下）として総和を $0$ とおく（あるいは「起電力の和 $=$ 電圧降下の和」）：
  $$V_1 - V_2 - V_3 = 0 \implies V_1 = V_2 + V_3, \qquad V_3 - V_4 = 0 \implies V_3 = V_4$$

> 💡 讲师批注：解多电源复杂回路题的标准三步法：① 在各支路**任意假设电流方向**（算出来若是负数，说明实际方向相反，完全不需要重算）；② 用 KCL 减少未知电流个数；③ 选独立闭合回路列 KVL 方程求解。

---

## 4. 全局术语表同步说明

本切片新增的 **57 条** 日文物理核心术语与假名注音（已避开切片 001 既有词条）已写入 [.glossary_006.md](file:///Users/baohan/Desktop/EJU/notes_物理/.glossary_006.md)，待主控合并去重至全局术语表。
