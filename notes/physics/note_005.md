# EJU 物理全解讲义 — 切片 005（P.61–P.75）
> **对应教材章节**：物理基礎・第三章 波（波動：正弦波、横波与縦波、重ね合わせの原理、固定端・自由端反射、定常波、波の干渉、反射と屈折；音波：音の3要素、音速、うなり、弦・気柱の固有振動、ドップラー効果；光波：光の屈折・分散、ヤングの干渉実験、回折格子、単スリット）  
> **适用对象**：需快速唤醒中国高中物理“机械波＋声学＋波动光学”基础、并掌握纯日文板书与 EJU 考场规范表达的授课教师 / 考生

---

## 1. 本节前置：国内高中物理基础唤醒

本切片完整覆盖日本高中物理第三章**「波（波動・音波・光波）」**的全部核心理论框架。与国内高中将机械波与波动光学拆在不同选修模块不同，EJU 物理高度强调**“波的统一性”**——无论是绳波、声波还是光波，都服从同一套叠加原理、干涉条件与斯涅尔折射定律。

### 1.1 机械波（波動）核心概念与公式推导

1. **波的基本关系式与正弦波方程**
   - 波速 $v\text{ [m/s]}$、频率 $f\text{ [Hz]}$、周期 $T\text{ [s]}$、波长 $\lambda\text{ [m]}$ 的基本关系：
     $$v = f\lambda = \frac{\lambda}{T}, \qquad f = \frac{1}{T}$$
   - 沿 $+x$ 方向传播的正弦波（原点 $x = 0$ 在 $t = 0$ 时处于平衡位置且向上起振）的波动方程：
     $$y(x, t) = A\sin\frac{2\pi}{T}\left(t - \frac{x}{v}\right) = A\sin 2\pi\left(\frac{t}{T} - \frac{x}{\lambda}\right)$$
     - **物理推导**：位置 $x$ 处的质点，比原点晚 $\Delta t = \dfrac{x}{v}$ 才重复原点的简谐振动，因此将原点振动方程 $y(0, t) = A\sin\dfrac{2\pi}{T}t$ 中的 $t$ 替换为 $t - \dfrac{x}{v}$ 即得；若波沿 $-x$ 方向传播，则括号内为 $t + \dfrac{x}{v}$。
     - **双图辨析**：固定 $x = x_1$ 得到 **$y$-$t$ 图（振動グラフ）**，横轴周期为 $T$；固定 $t = t_1$ 得到 **$y$-$x$ 图（波形グラフ）**，横轴周期为 $\lambda$。

2. **横波与纵波（横波と縦波）**
   - **横波**：质点振动方向 $\perp$ 波的传播方向（如绳波、电磁波/光波）。
   - **纵波（疎密波）**：质点振动方向 $\parallel$ 波的传播方向（如声波）。EJU 高频考法是将纵波的**水平位移**逆时针旋转 $90^\circ$ 画成横波表示图（横波表示）：
     - 设向右为 $+y$（向上画），则横波表示图中**由正变负的零点（下坡过零点）＝密部**，**由负变正的零点（上坡过零点）＝疎部**！

3. **波的叠加、反射与驻波（重ね合わせ・反射・定常波）**
   - **叠加原理**：任意点合位移等于各列波单独引起位移的矢量和 $y = y_1 + y_2$，且两列波相遇后互不干扰、保持各自原状继续传播（**波の独立性**）。
   - **固定端反射**：端点不动，反射波相对入射波**中心对称（点対称）**反转，波峰变波谷，发生**位相 $\pi$ 偏移（半波损失）**。
   - **自由端反射**：端点自由振动，反射波相对入射波**轴对称（線対称）**折回，波峰仍为波峰，**位相不变**。
   - **定常波（驻波）**：振幅、波长、周期均相同的两列相向行波叠加形成。
     - 相邻两**腹（波腹）**或相邻两**節（波节）**间距均为 **$\dfrac{\lambda}{2}$**；相邻腹与节间距为 **$\dfrac{\lambda}{4}$**。

4. **双波源干涉与反射・折射定律**
   - **双波源干涉条件**（**前提：两波源同位相**；若两波源**逆位相**，则强弱条件互换！）：
     - 強め合う条件（相长）：$|l_1 - l_2| = m\lambda \quad (m = 0, 1, 2, \cdots)$
     - 弱め合う条件（相消）：$|l_1 - l_2| = \left(m + \dfrac{1}{2}\right)\lambda \quad (m = 0, 1, 2, \cdots)$
   - **反射定律**：入射角 $i = $ 反射角 $j$（均以**法線**为基准测量）。
   - **屈折の法則（スネルの法則 / 斯涅尔定律）**：波从媒质 1 进入媒质 2，**频率 $f$ 不变**，波速与波长按同比例改变：
     $$\frac{\sin i}{\sin r} = \frac{v_1}{v_2} = \frac{\lambda_1}{\lambda_2} = n_{12} = \frac{n_2}{n_1} = \text{一定}$$

### 1.2 声波（音波）核心概念与公式推导

1. **声音三要素与空气中音速**
   - **音の高さ（音调）** $\leftrightarrow$ 振動数 $f$（可聴音 $20\text{–}20000\text{ Hz}$，高 1 オクターブ即频率 $\times 2$）；
   - **音の強さ（响度/声强）** $\leftrightarrow$ 振幅 $A$ 与能量（单位 $\text{dB}$，能量每增 $10$ 倍增加 $10\text{ dB}$）；
   - **音色（ねいろ）** $\leftrightarrow$ 波形。
   - **空気中の音速**（$t\ [^\circ\text{C}]$ 为摄氏温度）：
     $$V = 331.5 + 0.6t \text{ [m/s]}$$

2. **拍频（うなり）**
   - 频率微差的两声波 $f_1, f_2$ 叠加，每秒响度强弱交替的次数（拍频）：
     $$f = |f_1 - f_2|$$

3. **弦与气柱的固有振动（弦・気柱の固有振動）**
   - **弦（两端固定＝两端均为節）**：
     $$\lambda_n = \frac{2l}{n}, \qquad f_n = \frac{v}{\lambda_n} = \frac{n}{2l}\sqrt{\frac{S}{\rho}} \quad (n = 1, 2, 3, \cdots)$$
     其中弦上横波波速 $v = \sqrt{\dfrac{S}{\rho}}$，$S\text{ [N]}$ 为弦张力，$\rho\text{ [kg/m]}$ 为弦的**线密度**（单位长度质量）。
   - **閉管（一端闭＝節，一端开＝腹；只有奇数倍振动）**：
     $$\lambda_{2n-1} = \frac{4l}{2n - 1}, \qquad f_{2n-1} = \frac{2n - 1}{4l}V \quad (n = 1, 2, 3, \cdots)$$
   - **開管（两端开＝两端均为腹；含全部整数倍振动）**：
     $$\lambda_n = \frac{2l}{n}, \qquad f_n = \frac{n}{2l}V \quad (n = 1, 2, 3, \cdots)$$
   - **開口端補正 $\Delta l$**：实际气柱共鸣中，开口端的波腹略突出管口外侧 $\Delta l$，故有效管长闭管为 $l + \Delta l$，开管为 $l + 2\Delta l$。

4. **多普勒效应（ドップラー効果）**
   - **统一公式（必须死守符号约定：以「声源 $\to$ 观察者」方向为正！）**：
     $$f = \frac{V - v_o}{V - v_s} f_0$$
     - **分步推导**：声源以速度 $v_s$ 移动时，前方波长被压缩为 $\lambda' = \dfrac{V - v_s}{f_0}$；观察者以速度 $v_o$ 移动时，声波相对观察者的速度为 $V_{\text{相対}} = V - v_o$，故听到的频率为 $f = \dfrac{V_{\text{相対}}}{\lambda'} = \dfrac{V - v_o}{V - v_s}f_0$。
     - 若存在风速 $w$（以声源 $\to$ 观察者方向为正），只需将 $V$ 替换为 $V + w$。

### 1.3 光波（光波）核心概念与公式推导

1. **光的折射与色散（光の屈折・分散）**
   - 绝对折射率 $n_a = \dfrac{c}{v_a} \implies v_a = \dfrac{c}{n_a}$；相对折射率 $n_{12} = \dfrac{n_2}{n_1} = \dfrac{v_1}{v_2} = \dfrac{\sin i}{\sin r}$。
   - **光的分散**：同一透明介质对短波长光（紫/青）折射率更大、偏折更剧烈；对长波长光（赤）折射率更小、偏折更弱（口诀：**波長が短い紫ほど大きく曲がる**）。

2. **三大波动光学干涉/衍射核心条件对比**
   - **ヤングの干渉実験（杨氏双缝干涉）**（双缝距 $d$，缝屏距 $l \gg d, x$，光程差 $\Delta L = |l_1 - l_2| \fallingdotseq d\sin\theta \fallingdotseq \dfrac{dx}{l}$）：
     - 明線：$\dfrac{dx}{l} = m\lambda$；暗線：$\dfrac{dx}{l} = \left(m + \dfrac{1}{2}\right)\lambda \quad (m = 0, 1, 2, \cdots)$；明線間隔 $\Delta x = \dfrac{l\lambda}{d}$。
   - **回折格子（衍射光栅）**（格子定数 $d$，因偏折角 $\theta$ 较大，**不可近似 $\sin\theta \fallingdotseq \tan\theta$**）：
     - 明線：$d\sin\theta = m\lambda \quad (m = 0, 1, 2, \cdots)$。
   - **単スリット（单缝衍射）**（缝宽 $d$，半波带分割法，**明暗条件与双缝恰好相反！**）：
     - 暗線：$d\sin\theta = m\lambda \quad (m = 1, 2, 3, \cdots)$（无 $m = 0$）；
     - 明線：$d\sin\theta = 0$（中央主极大，宽为次极大 2 倍）或 $d\sin\theta \fallingdotseq \left(m + \dfrac{1}{2}\right)\lambda \quad (m = 1, 2, 3, \cdots)$。

### 1.4 中日物理体系与习惯差异提醒

| 对比维度 | 中国国内高中物理习惯 | 日本 EJU / 高中物理习惯（授课必强调） |
| :--- | :--- | :--- |
| **驻波与固有振动** | 高中阶段极少定量考弦的线密度公式与开/闭管谐波 | **EJU 绝对高频考点**！必须熟练画基本/2倍/3倍（开管・弦）与基本/3倍/5倍（闭管）波形图，并熟记 $f_n = \frac{n}{2l}\sqrt{\frac{S}{\rho}}$。 |
| **纵波的横波表示** | 较少用横波图形反推纵波密部与疏部 | 日本物理必考技能！需将向右位移映射为 $+y$，通过斜率正负一眼判别**密部（右下がり零点）**与**疎部（右上がり零点）**。 |
| **多普勒效应符号** | 多用“靠近变高、远离变低”口诀配 $\pm$ 号 | 日本考场统一用公式 $f = \dfrac{V - v_o}{V - v_s}f_0$，并严格规定**「音源から観測者への向きを正とする」**，直接代正负号，不易出错。 |
| **相对折射率写法** | 较少区分 $n_{12}$ 的脚标顺序 | 严格定义 **$n_{12} = \dfrac{n_2}{n_1} = \dfrac{v_1}{v_2}$**（读作：媒質 1 に対する媒質 2 の屈折率），分子是 $n_2$ 而非 $n_1$！ |
| **声波 vs 光波折射** | 重点讲光从空气入水折向法线 | 日本常同时对比声与光：空气 $\to$ 水时，**光变慢（$i > r$）**，而**声变快（$i < r$）**，极易在选择题设坑！ |
| **单缝衍射条件** | 高中仅定性介绍“中央宽亮条纹” | 日本教材直接给出定量暗纹条件 $d\sin\theta = m\lambda\ (m=1,2,\cdots)$，且需特别注意不要与双缝/光栅的明纹条件混淆。 |

---

## 2. 日文物理核心词汇与公式假名注音（板书必备）

### 2.1 核心物理词汇表

#### 波動基礎（波的基本性质）
- **波動（はどう / hadō）** — 波动
- **正弦波（せいげんは / seigenha）** — 正弦波
- **媒質（ばいしつ / baishitsu）** — 介质 / 媒质
- **単振動（たんしんどう / tanshindō）** — 简谐振动
- **振幅（しんぷく / shinpuku）** — 振幅（$A$）
- **周期（しゅうき / shūki）** — 周期（$T$）
- **振動数 / 周波数（しんどうすう / shindōsū；しゅうはすう / shūhasū）** — 频率（$f$）
- **波長（はちょう / hachō）** — 波长（$\lambda$）
- **位相（いそう / isō）** — 相位
- **同位相（どういそう / dōisō）** — 同相位
- **逆位相（ぎゃくいそう / gyaku-isō）** — 反相位
- **横波（よこなみ / yokonami）** — 横波
- **縦波（たてなみ / tatenami）** — 纵波
- **疎密波（そみつは / somitsuha）** — 疏密波（纵波的别称）
- **密（みつ / mitsu）** — 密部（压缩区）
- **疎（そ / so）** — 疏部（稀疏区）
- **重ね合わせの原理（かさねあわせのげんり / kasaneawase no genri）** — 波的叠加原理
- **合成波（ごうせいは / gōseiha）** — 合成波
- **パルス波（ぱるすは / parusuha）** — 脉冲波
- **固定端（こていたん / koteitan）** — 固定端
- **自由端（じゆうたん / jiyūtan）** — 自由端
- **入射波（にゅうしゃは / nyūshaha）** — 入射波
- **反射波（はんしゃは / hanshaha）** — 反射波
- **進行波（しんこうは / shinkōha）** — 行波 / 传播波
- **定常波 / 定在波（ていじょうは / teijōha；ていざいは / teizaiha）** — 驻波
- **腹（はら / hara）** — 波腹
- **節（ふし / fushi）** — 波节
- **波の干渉（なみのかんしょう / nami no kanshō）** — 波的干涉
- **波源（はげん / hagen）** — 波源
- **強め合う（つよめあう / tsuyomeau）** — 相长（干涉加强）
- **弱め合う（よわめあう / yowameau）** — 相消（干涉减弱）
- **境界面（きょうかいめん / kyōkaimen）** — 界面 / 分界面
- **法線（ほうせん / hōsen）** — 法线
- **入射角（にゅうしゃかく / nyūshakaku）** — 入射角（$i$）
- **反射角（はんしゃかく / hanshakaku）** — 反射角（$j$ 或 $i'$）
- **屈折角（くっせつかく / kussetsukaku）** — 折射角（$r$）
- **反射の法則（はんしゃのほうそく / hansha no hōsoku）** — 反射定律
- **屈折の法則 / スネルの法則（くっせつのほうそく / kussetsu no hōsoku；すねるのほうそく / suneru no hōsoku）** — 折射定律 / 斯涅尔定律
- **波面（はめん / hamen）** — 波前 / 波阵面
- **射線（しゃせん / shasen）** — 波线 / 射线

#### 音波（声波、共振与多普勒效应）
- **音波（おんぱ / onpa）** — 声波
- **音の3要素（おとのさんようそ / oto no san-yōso）** — 声音的三要素（音调、响度、音色）
- **可聴音（かちょうおん / kachōon）** — 可听声（20–20000 Hz）
- **超音波（ちょうおんぱ / chōonpa）** — 超声波
- **デシベル（でしべる / deshiberu）** — 分贝（$\text{dB}$）
- **音色（ねいろ / neiro）** — 音色（由波形决定）
- **音速（おんそく / onsoku）** — 声速
- **うなり（うなり / unari）** — 拍 / 拍频现象
- **固有振動（こゆうしんどう / koyū shindō）** — 固有振动
- **固有振動数（こゆうしんどうすう / koyū shindōsū）** — 固有频率
- **基本振動（きほんしんどう / kihon shindō）** — 基频振动（基音）
- **倍振動（ばいしんどう / baishindō）** — 倍频振动（泛音）
- **線密度（せんみつど / senmitsudo）** — 线密度（$\rho\text{ [kg/m]}$）
- **気柱（きちゅう / kichū）** — 气柱
- **閉管（へいかん / heikan）** — 闭管（一端封闭的管）
- **開管（かいかん / kaikan）** — 开管（两端开口的管）
- **開口端補正（かいこうたんほせい / kaikōtan hosei）** — 管口末端校正（$\Delta l$）
- **ドップラー効果（どっぷらーこうか / doppurā kōka）** — 多普勒效应
- **音源（おんげん / ongen）** — 声源（Source）
- **観測者（かんそくしゃ / kansokusha）** — 观察者（Observer）

#### 光波（光的折射、色散、干涉与衍射）
- **光波（こうは / kōha）** — 光波
- **相対屈折率（そうたいくっせつりつ / sōtai kussetsuritsu）** — 相对折射率（$n_{12}$）
- **絶対屈折率（ぜったいくっせつりつ / zettai kussetsuritsu）** — 绝对折射率（$n$）
- **単色光（たんしょくこう / tanshokukō）** — 单色光
- **白色光（はくしょくこう / hakushokukō）** — 白色光
- **プリズム（ぷりずむ / purizumu）** — 三棱镜
- **光の分散（ひかりのぶんさん / hikari no bunsan）** — 光的色散
- **ヤングの干渉実験（やんぐのかんしょうじっけん / yangu no kanshō jikken）** — 杨氏双缝干涉实验
- **単スリット（たんすりっと / tan-suritto）** — 单缝
- **複スリット（ふくすりっと / fuku-suritto）** — 双缝
- **経路差 / 光路差（けいろさ / keirosa；こうろさ / kōrosa）** — 路程差 / 光程差
- **明線（めいせん / meisen）** — 明条纹（亮纹）
- **暗線（あんせん / ansen）** — 暗条纹（暗纹）
- **干渉縞（かんしょうじま / kanshōjima）** — 干涉条纹
- **回折格子（かいせつこうし / kaisetsu kōshi）** — 衍射光栅
- **格子定数（こうしていすう / kōshi teisū）** — 光栅常数（$d$）
- **スクリーン（すくりーん / sukurīn）** — 光屏 / 屏幕

### 2.2 核心公式课堂口语读法（板书念法）

| 公式 | 日本课堂标准板书口语读法 |
| :--- | :--- |
| $y = A\sin 2\pi\left(\dfrac{t}{T} - \dfrac{x}{\lambda}\right)$ | 「ワイ・イコール、エー・サイン、にパイ・かっこ、ラージティーぶんのティー、ひく、ラムダぶんのエックス・かっこ」 |
| $\|l_1 - l_2\| = \left(m + \dfrac{1}{2}\right)\lambda$ | 「ぜったいち・エルいち・ひく・エルに、イコール、かっこ・エム・たす・にぶんのいち・かっこ・ラムダ」 |
| $\dfrac{\sin i}{\sin r} = \dfrac{v_1}{v_2} = n_{12}$ | 「サインアールぶんの・サインアイ、イコール、ブイにぶんの・ブイいち、イコール、エヌ・いちに」 |
| $V = 331.5 + 0.6t$ | 「ブイ・イコール、さんびゃくさんじゅういってんご、たす、れいてんろく・ティー」 |
| $f = \|f_1 - f_2\|$ | 「エフ・イコール、ぜったいち・エフいち・ひく・エフに」 |
| $f_n = \dfrac{n}{2l}\sqrt{\dfrac{S}{\rho}}$ | 「エフエヌ・イコール、にエルぶんのエヌ、ルート・ローぶんのエス」 |
| $f_{2n-1} = \dfrac{2n-1}{4l}V$ | 「エフ・にエヌひくいち、イコール、よんエルぶんの・にエヌひくいち・ブイ」 |
| $f = \dfrac{V - v_o}{V - v_s}f_0$ | 「エフ・イコール、ラージブイ・ひく・ブイエス・ぶんの、ラージブイ・ひく・ブイオー、かける・エフゼロ」 |
| $\dfrac{dx}{l} = m\lambda$ | 「エルぶんの・ディーエックス、イコール、エム・ラムダ」 |
| $d\sin\theta = m\lambda$ | 「ディー・サインシータ、イコール、エム・ラムダ」 |

---

## 3. 逐题深度解析（一题一解，不可跳步）

> [!NOTE]
> **本切片题量说明**：教材 P.61–P.75（页码 60–74）为第三章「波（波動・音波・光波）」的全套核心概念、实验原理与公式推导专讲，**不含原书编号例题或练习题（共 0 题）**；对应章节的例题与练习题将在后续切片中集中展开。  
> 为便于纯日文板书授课与考前速查，本节将 P.60–P.74 全部 15 页浓缩提炼为 **6 大核心物理模型深度解析**，每一模型均配备标准多色矢量 SVG 图解、日文考场规范推导与教材勘误批注。

---

### 核心模型 1（教材 P.60–P.62）：正弦波双图辨析与固定端 / 自由端反射

#### 【原教材要点与翻译】
> **日文核心表述**：  
> - 正弦波を表す式：$y = A\sin\dfrac{2\pi}{T}\left(t - \dfrac{x}{v}\right) = A\sin 2\pi\left(\dfrac{t}{T} - \dfrac{x}{\lambda}\right)$  
> - **固定端での反射**：反射波は入射波を固定端を中心に**点対称**に写したような形になる（山 $\to$ 谷，**位相が $\pi$ ズレる**）。  
> - **自由端での反射**：反射波は入射波を反射面で**線対称**に折り返したような形になる（山 $\to$ 山，**位相は変わらない**）。

#### 【考点与模型定位】
**$y$-$x$ 波形图与 $y$-$t$ 振动图互换 ＋ 固定端/自由端反射波作图法**（EJU 波动必考作图题：先画“穿透墙面的虚拟入射波”，再按点对称或线对称翻折回来，最后与原入射波逐点叠加求合成波）。

#### 【多色矢量图解（SVG）】

<svg viewBox="0 0 420 260" width="420" height="260" xmlns="http://www.w3.org/2000/svg" style="background:#fafafa;border:1px solid #e5e7eb;border-radius:8px;">
  <defs>
    <marker id="arr-blue-005-1" markerWidth="7" markerHeight="7" refX="5" refY="3" orient="auto"><path d="M0,0 L0,6 L6,3 z" fill="#2563eb"/></marker>
    <marker id="arr-green-005-1" markerWidth="7" markerHeight="7" refX="5" refY="3" orient="auto"><path d="M0,0 L0,6 L6,3 z" fill="#16a34a"/></marker>
    <marker id="arr-red-005-1" markerWidth="7" markerHeight="7" refX="5" refY="3" orient="auto"><path d="M0,0 L0,6 L6,3 z" fill="#dc2626"/></marker>
    <marker id="arr-blk-005-1" markerWidth="7" markerHeight="7" refX="5" refY="3" orient="auto"><path d="M0,0 L0,6 L6,3 z" fill="#111827"/></marker>
  </defs>

  <!-- 左半：固定端反射 -->
  <text x="38" y="22" font-size="11" font-weight="bold" fill="#111827">固定端反射（点対称・位相 π ずれ）</text>
  <line x1="20" y1="95" x2="195" y2="95" stroke="#6b7280" stroke-width="1.2"/>
  <!-- 固定端壁 -->
  <line x1="150" y1="40" x2="150" y2="150" stroke="#374151" stroke-width="2.5"/>
  <circle cx="150" cy="95" r="4" fill="#111827"/>
  <!-- 入射波（蓝色实线）与穿透虚波（蓝色虚线） -->
  <path d="M 80 95 Q 115 45 150 95" fill="none" stroke="#2563eb" stroke-width="2"/>
  <path d="M 150 95 Q 170 67 190 95" fill="none" stroke="#2563eb" stroke-width="1.3" stroke-dasharray="4,3"/>
  <line x1="95" y1="55" x2="132" y2="55" stroke="#111827" stroke-width="1.4" stroke-dasharray="4,3" marker-end="url(#arr-blk-005-1)"/>
  <text x="86" y="47" font-size="10" fill="#2563eb">入射波 (山)</text>
  <!-- 反射波（红色实线，倒扣为谷） -->
  <path d="M 110 95 Q 130 123 150 95" fill="none" stroke="#dc2626" stroke-width="2"/>
  <line x1="138" y1="132" x2="105" y2="132" stroke="#dc2626" stroke-width="1.4" stroke-dasharray="4,3" marker-end="url(#arr-red-005-1)"/>
  <text x="72" y="146" font-size="10" fill="#dc2626">反射波 (谷・逆位相)</text>

  <!-- 中间分隔线 -->
  <line x1="210" y1="12" x2="210" y2="248" stroke="#d1d5db" stroke-dasharray="4,4"/>

  <!-- 右半：自由端反射 -->
  <text x="232" y="22" font-size="11" font-weight="bold" fill="#111827">自由端反射（線対称・位相不変）</text>
  <line x1="225" y1="95" x2="405" y2="95" stroke="#6b7280" stroke-width="1.2"/>
  <!-- 自由端导杆与圆环 -->
  <line x1="355" y1="40" x2="355" y2="150" stroke="#9ca3af" stroke-width="1.8" stroke-dasharray="4,2"/>
  <circle cx="355" cy="95" r="4.5" fill="#fff" stroke="#16a34a" stroke-width="2"/>
  <!-- 入射波（蓝色实线）与穿透虚波 -->
  <path d="M 285 95 Q 320 45 355 95" fill="none" stroke="#2563eb" stroke-width="2"/>
  <path d="M 355 95 Q 375 67 395 95" fill="none" stroke="#2563eb" stroke-width="1.3" stroke-dasharray="4,3"/>
  <line x1="300" y1="55" x2="337" y2="55" stroke="#111827" stroke-width="1.4" stroke-dasharray="4,3" marker-end="url(#arr-blk-005-1)"/>
  <text x="288" y="47" font-size="10" fill="#2563eb">入射波 (山)</text>
  <!-- 反射波（绿色实线，仍为山） -->
  <path d="M 315 95 Q 335 67 355 95" fill="none" stroke="#16a34a" stroke-width="2"/>
  <line x1="342" y1="115" x2="308" y2="115" stroke="#16a34a" stroke-width="1.4" stroke-dasharray="4,3" marker-end="url(#arr-green-005-1)"/>
  <text x="275" y="130" font-size="10" fill="#16a34a">反射波 (山・同位相)</text>

  <!-- 下半部：纵波的横波表示速查 -->
  <line x1="15" y1="168" x2="405" y2="168" stroke="#e5e7eb" stroke-width="1.2"/>
  <text x="112" y="185" font-size="11" font-weight="bold" fill="#111827">縦波の横波表示（右向き変位を +y）</text>
  <line x1="35" y1="222" x2="385" y2="222" stroke="#4b5563" stroke-width="1.3" marker-end="url(#arr-blk-005-1)"/>
  <text x="389" y="226" font-size="10" font-style="italic" fill="#111827">x</text>
  <!-- 正弦波 -->
  <path d="M 50 222 Q 85 186 120 222 T 190 222 T 260 222 T 330 222" fill="none" stroke="#2563eb" stroke-width="2"/>
  <!-- 密部（下坡过零点） -->
  <circle cx="120" cy="222" r="4" fill="#dc2626"/>
  <text x="114" y="246" font-size="11" font-weight="bold" fill="#dc2626">密</text>
  <circle cx="260" cy="222" r="4" fill="#dc2626"/>
  <text x="254" y="246" font-size="11" font-weight="bold" fill="#dc2626">密</text>
  <!-- 疎部（上坡过零点） -->
  <circle cx="190" cy="222" r="4" fill="#16a34a"/>
  <text x="184" y="246" font-size="11" font-weight="bold" fill="#16a34a">疎</text>
  <circle cx="330" cy="222" r="4" fill="#16a34a"/>
  <text x="324" y="246" font-size="11" font-weight="bold" fill="#16a34a">疎</text>
  <text x="25" y="202" font-size="9.5" fill="#4b5563">右下がり零点＝密 / 右上がり零点＝疎</text>
</svg>

#### 【讲师批注与教材勘误】
> 💡 讲师批注（勘误 1 & 2）：  
> 1. 教材 P.60 正文第 1 行印刷为「引っ張**っ**り上げたり」，多了一个促音「っ」，正确写法应为「引っ張り上げたり」。  
> 2. 教材 P.62 固定端反射第一句写「下図のように…**左図**のようになります」，实际配图在正文正下方（「下図」），授课提示学生不必寻找左侧图。  
> 3. **反射波作图三步铁律**：① 让入射波无视反射面继续向右穿过；② 自由端将穿过部分**左右翻转（線対称）**，固定端将穿过部分**左右翻转后再上下翻转（点対称）**；③ 反射面左侧的**入射波＋反射波**逐点相加得合成波。

---

### 核心模型 2（教材 P.63–P.64）：定常波、双波源干涉与斯涅尔折射定律

#### 【原教材要点与翻译】
> **日文核心表述**：  
> - **2つの波源から出た波の干渉条件**（同位相のとき）：  
>   強め合う条件：$|l_1 - l_2| = m\lambda$，弱め合う条件：$|l_1 - l_2| = \left(m + \dfrac{1}{2}\right)\lambda \quad (m = 0, 1, 2, \cdots)$  
> - **屈折の法則（スネルの法則）**：$\dfrac{\sin i}{\sin r} = \dfrac{v_1}{v_2} = n_{12} = \text{一定}$

#### 【考点与模型定位】
**驻波腹节间距 ＋ 波程差干涉条件 ＋ 惠更斯波前推折射定律**（重点辨析波面与射线的垂直关系，入射角 $i$、折射角 $r$ 既是射线与法线的夹角，也等于波面与界面的夹角）。

#### 【多色矢量图解（SVG）】

<svg viewBox="0 0 420 260" width="420" height="260" xmlns="http://www.w3.org/2000/svg" style="background:#fafafa;border:1px solid #e5e7eb;border-radius:8px;">
  <defs>
    <marker id="arr-blue-005-2" markerWidth="7" markerHeight="7" refX="5" refY="3" orient="auto"><path d="M0,0 L0,6 L6,3 z" fill="#2563eb"/></marker>
    <marker id="arr-green-005-2" markerWidth="7" markerHeight="7" refX="5" refY="3" orient="auto"><path d="M0,0 L0,6 L6,3 z" fill="#16a34a"/></marker>
    <marker id="arr-red-005-2" markerWidth="7" markerHeight="7" refX="5" refY="3" orient="auto"><path d="M0,0 L0,6 L6,3 z" fill="#dc2626"/></marker>
    <marker id="arr-blk-005-2" markerWidth="7" markerHeight="7" refX="5" refY="3" orient="auto"><path d="M0,0 L0,6 L6,3 z" fill="#111827"/></marker>
  </defs>

  <!-- 左半：定常波（腹与節） -->
  <text x="38" y="22" font-size="11" font-weight="bold" fill="#111827">定常波（腹と節の間隔）</text>
  <line x1="15" y1="115" x2="200" y2="115" stroke="#6b7280" stroke-width="1.2"/>
  <!-- 包络双波形 -->
  <path d="M 25 115 Q 55 60 85 115 T 145 115 T 195 95" fill="none" stroke="#2563eb" stroke-width="2"/>
  <path d="M 25 115 Q 55 170 85 115 T 145 115 T 195 135" fill="none" stroke="#2563eb" stroke-width="1.5" stroke-dasharray="4,3"/>
  <!-- 節与腹标注 -->
  <circle cx="25" cy="115" r="3.5" fill="#dc2626"/>
  <circle cx="85" cy="115" r="3.5" fill="#dc2626"/>
  <circle cx="145" cy="115" r="3.5" fill="#dc2626"/>
  <text x="79" y="135" font-size="10" font-weight="bold" fill="#dc2626">節</text>
  <text x="139" y="135" font-size="10" font-weight="bold" fill="#dc2626">節</text>
  <line x1="55" y1="88" x2="55" y2="142" stroke="#16a34a" stroke-width="1.5" stroke-dasharray="3,2"/>
  <text x="49" y="75" font-size="10" font-weight="bold" fill="#16a34a">腹</text>
  <text x="109" y="160" font-size="10" font-weight="bold" fill="#16a34a">腹</text>
  <!-- 间距标注 -->
  <line x1="25" y1="190" x2="85" y2="190" stroke="#111827" stroke-width="1.2"/>
  <line x1="25" y1="185" x2="25" y2="195" stroke="#111827" stroke-width="1.2"/>
  <line x1="85" y1="185" x2="85" y2="195" stroke="#111827" stroke-width="1.2"/>
  <text x="43" y="206" font-size="10" fill="#111827">λ / 2</text>
  <text x="20" y="232" font-size="9.5" fill="#4b5563">節〜節 = 腹〜腹 = λ/2</text>
  <text x="20" y="246" font-size="9.5" fill="#4b5563">腹〜節 = λ/4</text>

  <!-- 分隔线 -->
  <line x1="210" y1="12" x2="210" y2="248" stroke="#d1d5db" stroke-dasharray="4,4"/>

  <!-- 右半：波的屈折 -->
  <text x="242" y="22" font-size="11" font-weight="bold" fill="#111827">波の屈折（スネルの法則）</text>
  <!-- 媒质 2 浅色背景 -->
  <rect x="220" y="128" width="190" height="115" fill="#eff6ff"/>
  <!-- 境界面 -->
  <line x1="220" y1="128" x2="410" y2="128" stroke="#374151" stroke-width="2"/>
  <text x="225" y="121" font-size="10" fill="#374151">媒質 1 (v₁, λ₁)</text>
  <text x="225" y="143" font-size="10" fill="#1e40af">媒質 2 (v₂, λ₂)</text>
  <!-- 法线 -->
  <line x1="315" y1="38" x2="315" y2="235" stroke="#6b7280" stroke-width="1.3" stroke-dasharray="4,3"/>
  <text x="320" y="48" font-size="10" fill="#6b7280">法線</text>
  <!-- 入射射线（蓝） -->
  <line x1="248" y1="48" x2="315" y2="128" stroke="#2563eb" stroke-width="2.2" marker-end="url(#arr-blue-005-2)"/>
  <!-- 入射波面（垂直于射线） -->
  <line x1="254" y1="74" x2="282" y2="51" stroke="#2563eb" stroke-width="1.2"/>
  <line x1="274" y1="98" x2="302" y2="75" stroke="#2563eb" stroke-width="1.2"/>
  <!-- 折射射线（红，偏向法线 v1 > v2） -->
  <line x1="315" y1="128" x2="352" y2="225" stroke="#dc2626" stroke-width="2.2" marker-end="url(#arr-red-005-2)"/>
  <!-- 折射波面（间距变密 λ2 < λ1） -->
  <line x1="314" y1="162" x2="342" y2="151" stroke="#dc2626" stroke-width="1.2"/>
  <line x1="322" y1="184" x2="350" y2="173" stroke="#dc2626" stroke-width="1.2"/>
  <!-- 角度弧线 i 与 r -->
  <path d="M 315 95 A 33 33 0 0 0 294 103" fill="none" stroke="#2563eb" stroke-width="1.5"/>
  <text x="301" y="90" font-size="11" font-style="italic" fill="#2563eb">i</text>
  <path d="M 315 162 A 34 34 0 0 0 327 160" fill="none" stroke="#dc2626" stroke-width="1.5"/>
  <text x="319" y="175" font-size="11" font-style="italic" fill="#dc2626">r</text>
  <text x="235" y="236" font-size="10" font-weight="bold" fill="#111827">sin i / sin r = v₁/v₂ = λ₁/λ₂</text>
</svg>

#### 【讲师批注与教材勘误】
> 💡 讲师批注（勘误 3）：  
> 1. 教材 P.63 给出的干涉条件 $|l_1 - l_2| = m\lambda$（強め合い）与 $(m + \frac{1}{2})\lambda$（弱め合い）**漏写了核心前提「同位相の 2 つの波源」**！在 EJU 考试中经常故意把两波源设为**逆位相**，此时强弱条件必须彻底对调！  
> 2. 无论折射如何发生，**振動数 $f$ 永远不变**（由波源决定），因此 $\dfrac{v_1}{v_2} = \dfrac{f\lambda_1}{f\lambda_2} = \dfrac{\lambda_1}{\lambda_2}$，波速越小的媒质中波长越短、波面越密、射线越贴近法线。

---

### 核心模型 3（教材 P.65–P.68）：弦与気柱（閉管・開管）的固有振動模式

#### 【原教材要点与翻译】
> **日文核心表述**：  
> - **空気中の音速**：$V = 331.5 + 0.6t\text{ [m/s]}$；**うなりの振動数**：$f = |f_1 - f_2|$。  
> - **弦の固有振動**：両端が**節**。$\lambda_n = \dfrac{2l}{n}$，$\ f_n = \dfrac{n}{2l}\sqrt{\dfrac{S}{\rho}}\ (n = 1, 2, 3, \cdots)$。  
> - **閉管の固有振動**：閉口端が**節**，開口端が**腹**。$\lambda_{2n-1} = \dfrac{4l}{2n-1}$，$\ f_{2n-1} = \dfrac{2n-1}{4l}V\ (n = 1, 2, 3, \cdots)$（奇数倍のみ）。  
> - **開管の固有振動**：両端が**腹**。$\lambda_n = \dfrac{2l}{n}$，$\ f_n = \dfrac{n}{2l}V\ (n = 1, 2, 3, \cdots)$。

#### 【考点与模型定位】
**两端边界条件定波形法**（不需要死背 6 个公式！只要记住“固定端/闭口端＝節，开口端＝腹”，画出基本振动数出管长 $l$ 包含几个 $\dfrac{\lambda}{4}$，所有波长与频率 3 秒内秒推）。

#### 【多色矢量图解（SVG）】

<svg viewBox="0 0 420 260" width="420" height="260" xmlns="http://www.w3.org/2000/svg" style="background:#fafafa;border:1px solid #e5e7eb;border-radius:8px;">
  <defs>
    <marker id="arr-blk-005-3" markerWidth="7" markerHeight="7" refX="5" refY="3" orient="auto"><path d="M0,0 L0,6 L6,3 z" fill="#111827"/></marker>
  </defs>

  <!-- 三列标题 -->
  <text x="32" y="20" font-size="11" font-weight="bold" fill="#2563eb">① 弦（両端＝節）</text>
  <text x="160" y="20" font-size="11" font-weight="bold" fill="#dc2626">② 閉管（閉＝節・開＝腹）</text>
  <text x="302" y="20" font-size="11" font-weight="bold" fill="#16a34a">③ 開管（両端＝腹）</text>

  <!-- 分隔虚线 -->
  <line x1="142" y1="10" x2="142" y2="250" stroke="#e5e7eb" stroke-dasharray="4,3"/>
  <line x1="282" y1="10" x2="282" y2="250" stroke="#e5e7eb" stroke-dasharray="4,3"/>

  <!-- ① 弦：基本振動、2倍振動、3倍振動 -->
  <!-- 基本 -->
  <text x="14" y="48" font-size="9.5" fill="#374151">基本 (n=1)</text>
  <line x1="22" y1="68" x2="128" y2="68" stroke="#9ca3af" stroke-width="1"/>
  <path d="M 22 68 Q 75 45 128 68" fill="none" stroke="#2563eb" stroke-width="1.8"/>
  <path d="M 22 68 Q 75 91 128 68" fill="none" stroke="#2563eb" stroke-width="1.3" stroke-dasharray="3,2"/>
  <text x="36" y="98" font-size="9.5" fill="#2563eb">l = λ₁/2 → λ₁ = 2l</text>
  <!-- 2倍 -->
  <text x="14" y="122" font-size="9.5" fill="#374151">2倍 (n=2)</text>
  <line x1="22" y1="142" x2="128" y2="142" stroke="#9ca3af" stroke-width="1"/>
  <path d="M 22 142 Q 48.5 122 75 142 T 128 142" fill="none" stroke="#2563eb" stroke-width="1.8"/>
  <path d="M 22 142 Q 48.5 162 75 142 T 128 142" fill="none" stroke="#2563eb" stroke-width="1.3" stroke-dasharray="3,2"/>
  <text x="36" y="172" font-size="9.5" fill="#2563eb">l = λ₂ → f₂ = 2f₁</text>
  <!-- 3倍 -->
  <text x="14" y="196" font-size="9.5" fill="#374151">3倍 (n=3)</text>
  <line x1="22" y1="216" x2="128" y2="216" stroke="#9ca3af" stroke-width="1"/>
  <path d="M 22 216 Q 39.6 198 57.3 216 T 92.6 216 T 128 216" fill="none" stroke="#2563eb" stroke-width="1.8"/>
  <path d="M 22 216 Q 39.6 234 57.3 216 T 92.6 216 T 128 216" fill="none" stroke="#2563eb" stroke-width="1.3" stroke-dasharray="3,2"/>
  <text x="26" y="246" font-size="9.5" font-weight="bold" fill="#2563eb">fₙ = (n/2l)√(S/ρ)</text>

  <!-- ② 閉管：基本(1倍)、3倍、5倍 -->
  <!-- 基本 -->
  <text x="155" y="48" font-size="9.5" fill="#374151">基本 (1倍)</text>
  <polyline points="268,54 162,54 162,82 268,82" fill="none" stroke="#374151" stroke-width="1.5"/>
  <path d="M 162 68 Q 215 56 268 56" fill="none" stroke="#dc2626" stroke-width="1.8"/>
  <path d="M 162 68 Q 215 80 268 80" fill="none" stroke="#dc2626" stroke-width="1.3" stroke-dasharray="3,2"/>
  <text x="176" y="98" font-size="9.5" fill="#dc2626">l = λ₁/4 → λ₁ = 4l</text>
  <!-- 3倍 -->
  <text x="155" y="122" font-size="9.5" fill="#374151">3倍振動（2倍なし！）</text>
  <polyline points="268,128 162,128 162,156 268,156" fill="none" stroke="#374151" stroke-width="1.5"/>
  <path d="M 162 142 Q 197 120 232.6 142 Q 250 153 268 153" fill="none" stroke="#dc2626" stroke-width="1.8"/>
  <path d="M 162 142 Q 197 164 232.6 142 Q 250 131 268 131" fill="none" stroke="#dc2626" stroke-width="1.3" stroke-dasharray="3,2"/>
  <text x="172" y="172" font-size="9.5" fill="#dc2626">l = 3λ₃/4 → f₃ = 3f₁</text>
  <!-- 5倍 -->
  <text x="155" y="196" font-size="9.5" fill="#374151">5倍振動</text>
  <polyline points="268,202 162,202 162,230 268,230" fill="none" stroke="#374151" stroke-width="1.5"/>
  <path d="M 162 216 Q 183 196 204.4 216 T 246.8 216 Q 257 206 268 206" fill="none" stroke="#dc2626" stroke-width="1.8"/>
  <path d="M 162 216 Q 183 236 204.4 216 T 246.8 216 Q 257 226 268 226" fill="none" stroke="#dc2626" stroke-width="1.3" stroke-dasharray="3,2"/>
  <text x="160" y="246" font-size="9.5" font-weight="bold" fill="#dc2626">f₂ₙ₋₁ = (2n-1)V / 4l</text>

  <!-- ③ 開管：基本、2倍、3倍 -->
  <!-- 基本 -->
  <text x="295" y="48" font-size="9.5" fill="#374151">基本 (n=1)</text>
  <line x1="300" y1="54" x2="404" y2="54" stroke="#374151" stroke-width="1.5"/>
  <line x1="300" y1="82" x2="404" y2="82" stroke="#374151" stroke-width="1.5"/>
  <path d="M 300 56 Q 326 56 352 68 Q 378 80 404 80" fill="none" stroke="#16a34a" stroke-width="1.8"/>
  <path d="M 300 80 Q 326 80 352 68 Q 378 56 404 56" fill="none" stroke="#16a34a" stroke-width="1.3" stroke-dasharray="3,2"/>
  <text x="312" y="98" font-size="9.5" fill="#16a34a">l = λ₁/2 → λ₁ = 2l</text>
  <!-- 2倍 -->
  <text x="295" y="122" font-size="9.5" fill="#374151">2倍 (n=2)</text>
  <line x1="300" y1="128" x2="404" y2="128" stroke="#374151" stroke-width="1.5"/>
  <line x1="300" y1="156" x2="404" y2="156" stroke="#374151" stroke-width="1.5"/>
  <path d="M 300 130 Q 313 130 326 142 Q 352 162 378 142 Q 391 130 404 130" fill="none" stroke="#16a34a" stroke-width="1.8"/>
  <path d="M 300 154 Q 313 154 326 142 Q 352 122 378 142 Q 391 154 404 154" fill="none" stroke="#16a34a" stroke-width="1.3" stroke-dasharray="3,2"/>
  <text x="312" y="172" font-size="9.5" fill="#16a34a">l = λ₂ → f₂ = 2f₁</text>
  <!-- 3倍 -->
  <text x="295" y="196" font-size="9.5" fill="#374151">3倍 (n=3)</text>
  <line x1="300" y1="202" x2="404" y2="202" stroke="#374151" stroke-width="1.5"/>
  <line x1="300" y1="230" x2="404" y2="230" stroke="#374151" stroke-width="1.5"/>
  <path d="M 300 204 Q 309 204 317 216 Q 335 234 352 216 Q 369 198 387 216 Q 395 228 404 228" fill="none" stroke="#16a34a" stroke-width="1.8"/>
  <path d="M 300 228 Q 309 228 317 216 Q 335 198 352 216 Q 369 234 387 216 Q 395 204 404 204" fill="none" stroke="#16a34a" stroke-width="1.3" stroke-dasharray="3,2"/>
  <text x="308" y="246" font-size="9.5" font-weight="bold" fill="#16a34a">fₙ = nV / 2l</text>
</svg>

#### 【讲师批注与教材勘误】
> 💡 讲师批注（勘误 4 & 5）：  
> 1. 教材 P.65 声音强度单位印刷为 `[db]`，国际规范写法应为 **`[dB]`**（分贝中的 B 为贝尔姓氏首字母，必须大写）；且空气音速公式 $V = 331.5 + 0.6t$ 中的 $t$ 为**摄氏温度 $[^\circ\text{C}]$**。  
> 2. 教材 P.67 弦的固有振动数公式 $f_n = \dfrac{n}{2l}\sqrt{\dfrac{S}{\rho}}$ 中未给出字母定义，授课务必板书注明：**$S\text{ [N]}$ 是弦的张力（張力）**，**$\rho\text{ [kg/m]}$ 是弦的线密度（線密度，単位長さあたりの質量）**，绝非体积密度 $[\text{kg/m}^3]$！  
> 3. **气柱的“位移波”与“压强/密疏波”反相规律**：开口端空气自由进出，位移振幅最大（**変位の腹**），但压强恒等于大气压，故压强变化为 0（**圧力変化の節**）；闭口端则相反，是**変位の節・圧力変化の腹**。这是 EJU 选择题超级高频坑点！

---

### 核心模型 4（教材 P.69）：ドップラー効果（多普勒效应）

#### 【原教材要点与翻译】
> **日文核心表述**：  
> $$f = \frac{V - v_o}{V - v_s} f_0$$  
> - $f$：観測者が感知する振動数，$V$：音速，$f_0$：音源の振動数，$v_o$：観測者の速度，$v_s$：音源の速度。  
> - **符号ルール**：**音源から観測者への向きを正とする**（以声源指向观察者的方向为正）。

#### 【考点与模型定位】
**一维直线多普勒效应 ＋ 反射壁（移动墙壁）二次多普勒模型**（反射壁题型标准解法：第一步把墙当作“观测者”求墙接收到的频率 $f_{\text{壁}}$，第二步把墙当作“声源”发出频率 $f_{\text{壁}}$ 给真正的观测者，两步连乘即可零失误）。

#### 【多色矢量图解（SVG）】

<svg viewBox="0 0 420 240" width="420" height="240" xmlns="http://www.w3.org/2000/svg" style="background:#fafafa;border:1px solid #e5e7eb;border-radius:8px;">
  <defs>
    <marker id="arr-blue-005-4" markerWidth="7" markerHeight="7" refX="5" refY="3" orient="auto"><path d="M0,0 L0,6 L6,3 z" fill="#2563eb"/></marker>
    <marker id="arr-green-005-4" markerWidth="7" markerHeight="7" refX="5" refY="3" orient="auto"><path d="M0,0 L0,6 L6,3 z" fill="#16a34a"/></marker>
    <marker id="arr-red-005-4" markerWidth="7" markerHeight="7" refX="5" refY="3" orient="auto"><path d="M0,0 L0,6 L6,3 z" fill="#dc2626"/></marker>
    <marker id="arr-blk-005-4" markerWidth="7" markerHeight="7" refX="5" refY="3" orient="auto"><path d="M0,0 L0,6 L6,3 z" fill="#111827"/></marker>
  </defs>

  <!-- 顶部正方向轴 -->
  <line x1="65" y1="28" x2="355" y2="28" stroke="#dc2626" stroke-width="2" marker-end="url(#arr-red-005-4)"/>
  <text x="112" y="20" font-size="11" font-weight="bold" fill="#dc2626">正の向き：音源 S → 観測者 O</text>

  <!-- 偏心波前圆（声源向右移动导致前方波长压缩） -->
  <circle cx="150" cy="122" r="22" fill="none" stroke="#93c5fd" stroke-width="1.3"/>
  <circle cx="135" cy="122" r="46" fill="none" stroke="#93c5fd" stroke-width="1.3"/>
  <circle cx="120" cy="122" r="70" fill="none" stroke="#93c5fd" stroke-width="1.3"/>
  <circle cx="105" cy="122" r="94" fill="none" stroke="#93c5fd" stroke-width="1.3"/>

  <!-- 地面线 -->
  <line x1="20" y1="168" x2="400" y2="168" stroke="#4b5563" stroke-width="1.5"/>

  <!-- 声源 S -->
  <circle cx="165" cy="122" r="11" fill="#dbeafe" stroke="#2563eb" stroke-width="2"/>
  <text x="161" y="126" font-size="11" font-weight="bold" fill="#1e3a8a">S</text>
  <line x1="176" y1="122" x2="215" y2="122" stroke="#111827" stroke-width="1.8" stroke-dasharray="4,3" marker-end="url(#arr-blk-005-4)"/>
  <text x="184" y="114" font-size="10.5" font-weight="bold" fill="#111827">v_s</text>

  <!-- 压缩后的波长标注 -->
  <line x1="172" y1="152" x2="181" y2="152" stroke="#2563eb" stroke-width="1.5"/>
  <text x="195" y="156" font-size="10" fill="#2563eb">前方：λ' = (V - v_s)/f₀</text>

  <!-- 观察者 O -->
  <circle cx="330" cy="122" r="11" fill="#dcfce7" stroke="#16a34a" stroke-width="2"/>
  <text x="325" y="126" font-size="11" font-weight="bold" fill="#14532d">O</text>
  <line x1="341" y1="122" x2="380" y2="122" stroke="#111827" stroke-width="1.8" stroke-dasharray="4,3" marker-end="url(#arr-blk-005-4)"/>
  <text x="350" y="114" font-size="10.5" font-weight="bold" fill="#111827">v_o</text>

  <!-- 公式总结框 -->
  <rect x="38" y="182" width="344" height="46" rx="6" fill="#fff" stroke="#cbd5e1" stroke-width="1.2"/>
  <text x="54" y="201" font-size="11" font-weight="bold" fill="#111827">公式：f = { (V - v_o) / (V - v_s) } · f₀</text>
  <text x="54" y="219" font-size="10" fill="#4b5563">※ 風速 w（S→O 向きを正）があるとき：V を V + w に置換</text>
</svg>

#### 【讲师批注】
> 💡 讲师批注：  
> 1. 千万提醒学生：若观测者迎着声源跑（$O \to S$），与正方向（$S \to O$）相反，故 $v_o < 0$，代入分子变成 $V - (-|v_o|) = V + |v_o|$，听到的频率变高！  
> 2. **斜向多普勒效应（二次试验/难题拓展）**：当声源或观测者的运动方向与连线 $SO$ 成夹角 $\theta$ 时，只需取速度沿连线 $SO$ 方向的投影 $v_s\cos\theta$、$v_o\cos\theta$ 代入同一公式即可。

---

### 核心模型 5（教材 P.70–P.71）：光的屈折与プリズム（三棱镜）色散

#### 【原教材要点与翻译】
> **日文核心表述**：  
> - **相対屈折率**：$n_{12} = \dfrac{\sin i}{\sin r} = \dfrac{v_1}{v_2} = \dfrac{n_2}{n_1}$；**絶対屈折率**：$n_a = \dfrac{c}{v_a} \implies v_a = \dfrac{c}{n_a}$。  
> - **光の分散**：白色光をプリズムに通すと，波長の長い**赤**はあまり曲げられず，波長の短い**青・紫**は大きく曲げられる（赤・橙・黄・緑・青・藍・紫）。

#### 【考点与模型定位】
**光密/光疏折射偏折方向 ＋ 玻璃对不同色光折射率大小排序（$n_{\text{赤}} < n_{\text{紫}}$）**。

#### 【多色矢量图解（SVG）】

<svg viewBox="0 0 420 240" width="420" height="240" xmlns="http://www.w3.org/2000/svg" style="background:#fafafa;border:1px solid #e5e7eb;border-radius:8px;">
  <defs>
    <marker id="arr-blue-005-5" markerWidth="7" markerHeight="7" refX="5" refY="3" orient="auto"><path d="M0,0 L0,6 L6,3 z" fill="#2563eb"/></marker>
    <marker id="arr-red-005-5" markerWidth="7" markerHeight="7" refX="5" refY="3" orient="auto"><path d="M0,0 L0,6 L6,3 z" fill="#dc2626"/></marker>
    <marker id="arr-purp-005-5" markerWidth="7" markerHeight="7" refX="5" refY="3" orient="auto"><path d="M0,0 L0,6 L6,3 z" fill="#7c3aed"/></marker>
    <marker id="arr-blk-005-5" markerWidth="7" markerHeight="7" refX="5" refY="3" orient="auto"><path d="M0,0 L0,6 L6,3 z" fill="#111827"/></marker>
  </defs>

  <text x="112" y="22" font-size="11.5" font-weight="bold" fill="#111827">プリズムによる白色光の分散（n_赤 &lt; n_紫）</text>

  <!-- 三棱镜 -->
  <polygon points="185,48 120,185 250,185" fill="#e0f2fe" fill-opacity="0.7" stroke="#0284c7" stroke-width="2"/>
  <text x="164" y="176" font-size="10.5" font-weight="bold" fill="#0369a1">プリズム</text>

  <!-- 白色入射光 -->
  <line x1="35" y1="138" x2="150" y2="112" stroke="#111827" stroke-width="2.5" marker-end="url(#arr-blk-005-5)"/>
  <text x="42" y="122" font-size="11" font-weight="bold" fill="#111827">白色光</text>

  <!-- 棱镜内部：红光（偏折小）与紫光（偏折大） -->
  <line x1="150" y1="112" x2="218" y2="118" stroke="#dc2626" stroke-width="2"/>
  <line x1="150" y1="112" x2="225" y2="132" stroke="#7c3aed" stroke-width="2"/>

  <!-- 出射红光 -->
  <line x1="218" y1="118" x2="345" y2="128" stroke="#dc2626" stroke-width="2.2" marker-end="url(#arr-red-005-5)"/>
  <text x="352" y="131" font-size="11" font-weight="bold" fill="#dc2626">赤（λ大・n小）</text>
  <!-- 中间色光示意 -->
  <line x1="221" y1="125" x2="345" y2="152" stroke="#16a34a" stroke-width="1.5" stroke-dasharray="3,2"/>
  <!-- 出射紫光 -->
  <line x1="225" y1="132" x2="345" y2="178" stroke="#7c3aed" stroke-width="2.2" marker-end="url(#arr-purp-005-5)"/>
  <text x="352" y="181" font-size="11" font-weight="bold" fill="#7c3aed">紫（λ小・n大）</text>

  <!-- 底部对比总结 -->
  <text x="42" y="214" font-size="10" fill="#374151">絶対屈折率の目安：空気 ≒ 1.00，水 ≒ 1.33，ガラス ≒ 1.5，ダイヤモンド ≒ 2.42</text>
  <text x="42" y="230" font-size="10" fill="#dc2626">※ 空気→水：光は遅くなり法線へ近づく（i &gt; r）；音は速くなり法線から離れる（i &lt; r）</text>
</svg>

#### 【讲师批注】
> 💡 讲师批注：  
> 1. 教材 P.70 给出了四种常见物质的绝对折射率（空气 $1.0003$、水 $1.3330$、玻璃 $1.4585$、金刚石 $2.4195$），提醒学生：**EJU 计算中空气的绝对折射率通常近似取 $1$**，因此光从空气进入折射率 $n$ 的媒质直接用 $\dfrac{\sin i}{\sin r} = n$。  
> 2. 金刚石折射率高达 $2.42$，临界角极小（约 $24.4^\circ$），极易发生全反射，这也是钻石璀璨夺目的物理原因（可顺带预告下一节「全反射」）。

---

### 核心模型 6（教材 P.72–P.74）：ヤングの干渉実験・回折格子・単スリット三大光路对比

#### 【原教材要点与翻译】
> **日文核心表述**：  
> - **ヤングの干渉実験**：明線 $\dfrac{dx}{l} = m\lambda$，暗線 $\dfrac{dx}{l} = \left(m + \dfrac{1}{2}\right)\lambda \quad (m = 0, 1, 2, \cdots)$。  
> - **回折格子**：明線 $d\sin\theta = m\lambda \quad (m = 0, 1, 2, \cdots)$（$d$：格子定数）。  
> - **単スリット**：明線 $d\sin\theta = 0,\ \left(m + \dfrac{1}{2}\right)\lambda$，暗線 $d\sin\theta = m\lambda \quad (m = 1, 2, 3, \cdots)$。

#### 【考点与模型定位】
**波动光学三大核心实验的光程差几何推导与明暗条件精准辨析**（特别注意：杨氏双缝 $l \gg d, x$ 可近似 $\sin\theta \fallingdotseq \tan\theta = \dfrac{x}{l}$；衍射光栅 $\theta$ 较大不可近似；单缝衍射暗纹条件恰与前两者的明纹条件形式相同，且 $m$ 从 $1$ 开始！）。

#### 【多色矢量图解（SVG）】

<svg viewBox="0 0 420 260" width="420" height="260" xmlns="http://www.w3.org/2000/svg" style="background:#fafafa;border:1px solid #e5e7eb;border-radius:8px;">
  <defs>
    <marker id="arr-blue-005-6" markerWidth="7" markerHeight="7" refX="5" refY="3" orient="auto"><path d="M0,0 L0,6 L6,3 z" fill="#2563eb"/></marker>
    <marker id="arr-red-005-6" markerWidth="7" markerHeight="7" refX="5" refY="3" orient="auto"><path d="M0,0 L0,6 L6,3 z" fill="#dc2626"/></marker>
    <marker id="arr-blk-005-6" markerWidth="7" markerHeight="7" refX="5" refY="3" orient="auto"><path d="M0,0 L0,6 L6,3 z" fill="#111827"/></marker>
  </defs>

  <!-- 左半：杨氏双缝光程差几何 -->
  <text x="26" y="20" font-size="11" font-weight="bold" fill="#111827">① ヤングの干渉（経路差 ≒ d sinθ ≒ dx/l）</text>
  <!-- 双缝挡板 -->
  <line x1="60" y1="36" x2="60" y2="108" stroke="#374151" stroke-width="3"/>
  <line x1="60" y1="116" x2="60" y2="160" stroke="#374151" stroke-width="3"/>
  <line x1="60" y1="168" x2="60" y2="215" stroke="#374151" stroke-width="3"/>
  <text x="42" y="116" font-size="10" font-weight="bold" fill="#111827">S₁</text>
  <text x="42" y="168" font-size="10" font-weight="bold" fill="#111827">S₂</text>
  <text x="24" y="142" font-size="10" font-style="italic" fill="#111827">d</text>
  <!-- 屏幕 -->
  <line x1="230" y1="36" x2="230" y2="215" stroke="#374151" stroke-width="2.5"/>
  <!-- 中心轴 -->
  <line x1="60" y1="138" x2="230" y2="138" stroke="#9ca3af" stroke-dasharray="4,3"/>
  <text x="235" y="142" font-size="10" fill="#374151">O</text>
  <!-- 两条光线到 P 点 -->
  <line x1="60" y1="112" x2="230" y2="62" stroke="#2563eb" stroke-width="1.6"/>
  <line x1="60" y1="164" x2="230" y2="62" stroke="#2563eb" stroke-width="1.6"/>
  <!-- 中心连线 -->
  <line x1="60" y1="138" x2="230" y2="62" stroke="#6b7280" stroke-width="1.2" stroke-dasharray="3,2"/>
  <circle cx="230" cy="62" r="3.5" fill="#dc2626"/>
  <text x="235" y="65" font-size="10" font-weight="bold" fill="#dc2626">P</text>
  <!-- 垂线标出光程差 d sinθ -->
  <line x1="60" y1="112" x2="82" y2="151" stroke="#dc2626" stroke-width="1.6"/>
  <line x1="60" y1="164" x2="82" y2="151" stroke="#dc2626" stroke-width="2.5"/>
  <text x="72" y="176" font-size="10" font-weight="bold" fill="#dc2626">d sinθ</text>
  <!-- 角度 theta 与 x, l 标注 -->
  <path d="M 92 138 A 32 32 0 0 0 89 125" fill="none" stroke="#16a34a" stroke-width="1.4"/>
  <text x="96" y="134" font-size="10" fill="#16a34a">θ</text>
  <text x="236" y="102" font-size="10" font-style="italic" fill="#dc2626">x</text>
  <line x1="60" y1="226" x2="230" y2="226" stroke="#4b5563" stroke-width="1.2"/>
  <text x="142" y="240" font-size="10.5" font-style="italic" fill="#111827">l</text>

  <!-- 分隔线 -->
  <line x1="262" y1="12" x2="262" y2="248" stroke="#d1d5db" stroke-dasharray="4,4"/>

  <!-- 右半：单缝衍射强度分布与暗纹 -->
  <text x="276" y="20" font-size="11" font-weight="bold" fill="#111827">② 単スリット強度分布</text>
  <!-- 屏幕竖轴 -->
  <line x1="378" y1="36" x2="378" y2="215" stroke="#374151" stroke-width="1.5"/>
  <!-- 光强分布曲线（中央宽主极大 + 两侧弱次极大） -->
  <path d="M 378 46 Q 368 56 378 66 Q 355 82 378 96 Q 290 126 378 156 Q 355 170 378 186 Q 368 196 378 206" fill="#dbeafe" fill-opacity="0.55" stroke="#2563eb" stroke-width="1.8"/>
  <!-- 中心与暗纹点 -->
  <line x1="278" y1="126" x2="386" y2="126" stroke="#9ca3af" stroke-dasharray="3,2"/>
  <text x="383" y="129" font-size="10" font-weight="bold" fill="#2563eb">P₀</text>
  <circle cx="378" cy="96" r="3" fill="#dc2626"/>
  <text x="383" y="99" font-size="9.5" fill="#dc2626">暗 m=1</text>
  <circle cx="378" cy="156" r="3" fill="#dc2626"/>
  <text x="383" y="159" font-size="9.5" fill="#dc2626">暗 m=1</text>
  <circle cx="378" cy="66" r="3" fill="#dc2626"/>
  <text x="383" y="69" font-size="9.5" fill="#dc2626">暗 m=2</text>
  <text x="272" y="232" font-size="9.5" font-weight="bold" fill="#dc2626">暗線：d sinθ = mλ (m=1,2…)</text>
  <text x="272" y="246" font-size="9.5" fill="#4b5563">※ ヤング・回折格子と明暗逆！</text>
</svg>

#### 【讲师批注与教材勘误】
> 💡 讲师批注（勘误 6 & 7）：  
> 1. **回折格子暗纹条件的严谨性提醒（教材 P.73）**：教材在回折格子下方写「暗線の条件：$d\sin\theta = \left(m + \dfrac{1}{2}\right)\lambda$」，物理上不够严谨！由于光栅包含成千上万条狭缝（$N \gg 1$），只要方向稍微偏离明纹条件 $d\sin\theta = m\lambda$，大量微弱相移的光就会迅速相互抵消变暗（严格零光强条件是 $Nd\sin\theta = k\lambda$，$k$ 不为 $N$ 的倍数），$\left(m + \frac{1}{2}\right)\lambda$ 仅仅是相邻两缝恰好反相的特例。EJU 考试对光栅**只考明線条件 $d\sin\theta = m\lambda$** 及由 $\sin\theta < 1$ 推出的最高级数 $m_{\max}$。  
> 2. **単スリット半波带分割法（教材 P.74）**：教材配图在单缝上下两端标出了 $B_0$、$B_{12}$ 却未解释含义。授课用最直观的“两两配对法”讲透：当单缝上下两端光程差 $d\sin\theta = \lambda$（即 $m=1$）时，把单缝分成上下两半，上半缝任意一点总能在下半缝距离 $\dfrac{d}{2}$ 处找到光程差恰好为 $\dfrac{\lambda}{2}$ 的对应点，两两完全抵消形成**第 1 级暗纹**；同理 $d\sin\theta = m\lambda$ 时分成 $2m$ 份两两抵消。因此单缝的 $d\sin\theta = m\lambda\ (m=1,2,\cdots)$ 是**暗線**而非明線！另外，教材所给次极大明线条件 $d\sin\theta = \left(m+\frac{1}{2}\right)\lambda$ 仅为近似位置。

---

## 4. 全局术语表同步说明

本切片新增的 **77 条** 日文物理核心术语与假名注音（覆盖波動基礎、音波、光波三大模块）已按规范格式写入独立切片术语表：[`.glossary_005.md`](file:///Users/baohan/Desktop/EJU/notes_物理/.glossary_005.md)，待主控合并去重至全局术语表 [`glossary_all.md`](file:///Users/baohan/Desktop/EJU/notes_物理/glossary_all.md)。
