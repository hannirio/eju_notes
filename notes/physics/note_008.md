# EJU 物理全解讲义 — 切片 008（P.106–P.115）
> **对应教材章节**：第四章 電気と磁気（変圧器、コイル・コンデンサーを流れる交流、RLC直列回路）＋ 第五章 原子（陰極線、光電効果、X線の発生、物質波、コンプトン効果、ボーア模型）※ P.114–P.115 为教材版权页与封底  
> **适用对象**：需快速唤醒中国高中物理基础、并掌握纯日文板书与 EJU 考场规范表达的授课教师 / 考生

---

## 1. 本节前置：国内高中物理基础唤醒

本切片是全书的收官篇章，涵盖**交流电路进阶（交流回路）**与**近代原子物理（原子）**两大核心板块。两者公式密集、物理图像鲜明，在 EJU 物理考试中极易以“纯符号推导＋图像判读”的形式出现，掌握底层推导即可稳拿高分。

### 1.1 交流电路进阶（変圧器・リアクタンス・RLC直列回路）

1. **理想变压器（変圧器）**
   - **工作原理**：利用一次线圈（一次コイル，匝数 $N_1$）与二次线圈（二次コイル，匝数 $N_2$）之间的**互感现象（相互誘導）**改变交流电压。
   - **直流不可变压**：直流电流恒定 $\implies$ 铁芯中磁通量变化率 $\dfrac{\Delta \Phi}{\Delta t} = 0 \implies$ 无法产生感应电动势。
   - **电压与电流关系**（设无磁通泄漏、无能量损耗的理想变压器，下标 $e$ 表示**有效值 / 実効値**）：
     - 由法拉第电磁感应定律：$V_{1e} = N_1 \left|\dfrac{\Delta \Phi}{\Delta t}\right|_e$，$V_{2e} = N_2 \left|\dfrac{\Delta \Phi}{\Delta t}\right|_e \implies \dfrac{V_{1e}}{V_{2e}} = \dfrac{N_1}{N_2}$；
     - 由输入功率 $=$ 输出功率：$V_{1e} I_{1e} = V_{2e} I_{2e} \implies \dfrac{I_{2e}}{I_{1e}} = \dfrac{N_1}{N_2}$。
     - 合并标准式：
       $$\frac{V_{1e}}{V_{2e}} = \frac{I_{2e}}{I_{1e}} = \frac{N_1}{N_2}$$

2. **纯电感（コイル）与纯电容（コンデンサー）的交流特性**
   设交流电源电压瞬时值为 $V = V_0 \sin \omega t$（角频率 $\omega = 2\pi f$）：
   - **纯电感线圈（自感系数 $L\text{ [H]}$）**：
     - 线圈通过自感电动势阻碍电流变化，因此**电流的相位比电压滞后 $\dfrac{\pi}{2}$**（電流の位相は電圧より $\frac{\pi}{2}$ 遅れる）：
       $$I = \frac{V_0}{\omega L} \sin\left(\omega t - \frac{\pi}{2}\right) = I_0 \sin\left(\omega t - \frac{\pi}{2}\right)$$
     - 峰值/有效值关系：$V_0 = \omega L I_0$（$V_e = \omega L I_e$）。其中 $X_L = \omega L$ 称为**感抗（誘導リアクタンス）**，频率越高阻碍越大（通低频、阻高频）。
   - **纯电容器（电容 $C\text{ [F]}$）**：
     - 由 $I = \dfrac{dQ}{dt} = C\dfrac{dV}{dt} = \omega C V_0 \cos \omega t = \omega C V_0 \sin\left(\omega t + \dfrac{\pi}{2}\right)$，**电流的相位比电压超前 $\dfrac{\pi}{2}$**（電流の位相は電圧より $\frac{\pi}{2}$ 進む）：
       $$I = \omega C V_0 \sin\left(\omega t + \frac{\pi}{2}\right) = I_0 \sin\left(\omega t + \frac{\pi}{2}\right)$$
     - 峰值/有效值关系：$V_0 = \dfrac{I_0}{\omega C}$（$V_e = \dfrac{I_e}{\omega C}$）。其中 $X_C = \dfrac{1}{\omega C}$ 称为**容抗（容量リアクタンス）**，频率越高阻碍越小（隔直流、通高频）。

3. **RLC 串联电路（RLC直列回路）与谐振（共振）**
   - 串联电路中流过 $R, L, C$ 的电流相同，设 $I = I_0 \sin \omega t$，则三个元件两端的电压相位分别为：
     - $V_R$ 与 $I$ **同相**，幅值 $R I_0$；
     - $V_L$ 比 $I$ **超前 $\dfrac{\pi}{2}$**，幅值 $\omega L I_0$；
     - $V_C$ 比 $I$ **滞后 $\dfrac{\pi}{2}$**，幅值 $\dfrac{1}{\omega C} I_0$。
   - **阻抗（インピーダンス）$Z$**：利用电压矢量图（$V_L$ 与 $V_C$ 反向，合矢量与 $V_R$ 垂直）得总电压幅值 $V_0 = \sqrt{(R I_0)^2 + \left(\omega L I_0 - \dfrac{I_0}{\omega C}\right)^2} = Z I_0$，故：
     $$Z = \sqrt{R^2 + \left(\omega L - \frac{1}{\omega C}\right)^2}$$
   - **串联谐振（共振）条件**：当 $\omega L = \dfrac{1}{\omega C}$ 时，阻抗取最小值 $Z_{\min} = R$，电路电流达到最大！此时的**谐振角频率（共振角周波数）**与**谐振频率（共振周波数）**为：
     $$\omega_0 = \frac{1}{\sqrt{LC}}, \qquad f_0 = \frac{1}{2\pi\sqrt{LC}}$$

### 1.2 近代原子物理（原子）核心概念与公式推导

1. **阴极射线（陰極線）与电子的发现**
   - 真空玻璃管（クルックス管 / 克鲁克斯管）加高压放电时，从阴极发出的射线即为阴极射线（本质是高速电子流）。
   - **六大基本性质**（教材 P.109）：① 肉眼不可见；② 撞击荧光物质发荧光；③ 使照相底片感光；④ 使气体电离产生离子；⑤ 撞击小叶轮（羽根車）使其转动（证明具有动量与质量）；⑥ 具有直进性。
   - **偏转实验补充**：在电场中向正极板偏转、在磁场中受洛伦兹力偏转 $\implies$ 证明其带**负电荷**（汤姆孙借此测出电子比荷 $e/m$）。

2. **光电效应（光電効果）与光子假说**
   - **现象**：金属表面受足够高频率的光（如紫外线）照射时逸出电子（光電子）的现象。
   - **光子能量（光子 1 個のエネルギー）**：
     $$E = h\nu = \frac{hc}{\lambda} \quad (h\text{：普朗克常数 } 6.63 \times 10^{-34}\text{ J}\cdot\text{s},\ \nu\text{：光的频率})$$
   - **爱因斯坦光电效应方程（1 個の光電子のエネルギー保存則）**：
     $$h\nu = \frac{1}{2}mv_{\max}^2 + W \quad \Longleftrightarrow \quad K_M = h\nu - W$$
     其中 $W$ 为**逸出功（仕事関数）**，$K_M$ 为光电子的最大初动能。
   - **高频补充关系**：
     - **截止频率（限界振動数）**：$K_M = 0$ 时的最低入射频率 $\nu_0 = \dfrac{W}{h}$；
     - **遏止电压（阻止電圧）$V_0$**：恰好阻止最大动能光电子到达阳极的反向电压，满足 $eV_0 = K_M = h\nu - W$。

3. **X 射线的产生（X線の発生）**
   - 波长约 $10^{-8}\text{ m} \sim 10^{-12}\text{ m}$ 的电磁波，由伦琴（レントゲン）发现。
   - **产生机制**：灯丝（フィラメント）加热放出热电子 $\xrightarrow{\text{加速電圧 } V}$ 高速撞击阳极金属靶 $\to$ 发出 X 射线。
   - **两种 X 射线光谱**：
     - **连续 X 射线（連続 X 線）**：电子减速刹车（韧致辐射）产生，存在**最短波长 $\lambda_0$**（电子动能 $eV$ 全部转化为 1 个光子能量）：
       $$eV = \frac{hc}{\lambda_0} \implies \lambda_0 = \frac{hc}{eV} \quad \text{（仅由加速电压 } V \text{ 决定！）}$$
     - **特征 X 射线（特性 X 線 / 固有 X 線）**：靶原子内层电子被撞出、外层电子跃迁填补空位发出，波长**仅由阳极金属材料种类决定**，与加速电压无关。

4. **物质波（物質波 / ド・ブロイ波）与康普顿效应（コンプトン効果）**
   - **德布罗意物质波**：一切微观粒子都具有波动性，动量 $p = mv$ 的粒子对应波长为：
     $$\lambda = \frac{h}{p} = \frac{h}{mv}$$
   - **光子的动量**：由相对论质能关系 $E = pc$ 与 $E = h\nu$ 得：
     $$p = \frac{h\nu}{c} = \frac{h}{\lambda}$$
   - **康普顿效应**：X 射线照射物质发生散射，散射角为 $\varphi$ 的散射 X 射线波长比入射波长变长（证明光子既有能量又有动量，与静止电子发生弹性碰撞）：
     $$\Delta \lambda = \lambda' - \lambda = \frac{h}{mc}(1 - \cos\varphi) \quad \left(\frac{h}{mc} \text{ 称为电子的康普顿波长}\right)$$

5. **玻尔氢原子模型（ボーアの原子模型）**
   - **经典电磁理论的矛盾**：绕核做圆周运动的电子有向心加速度，按经典理论会不断辐射电磁波损失能量，导致轨道半径连续缩小直至坠入原子核，且应发出连续光谱——与氢原子稳定存在且只发**线状光谱（線スペクトル）**矛盾。
   - **玻尔两大核心假设**：
     1. **量子条件（ボーアの量子条件）**：电子轨道角动量量子化（等价于轨道周长等于电子德布罗意波长的整数倍 $2\pi r = n\lambda$）：
        $$mvr = n\frac{h}{2\pi} \qquad (n = 1, 2, 3, \cdots)$$
     2. **振动数条件（频率条件）**：电子从高能级 $E_n$ 跃迁至低能级 $E_{n'}$ 时，辐射光子的能量为 $h\nu = E_n - E_{n'}$。
   - **联立库仑力充当向心力 $m\dfrac{v^2}{r} = k_0\dfrac{e^2}{r^2}$ 与量子条件可得**：
     - **轨道半径**：$r_n = \dfrac{h^2}{4\pi^2 k_0 m e^2} \cdot n^2 \propto n^2$
     - **能级公式**：$E_n = -\dfrac{2\pi^2 k_0^2 m e^4}{h^2} \cdot \dfrac{1}{n^2} = -\dfrac{13.6}{n^2}\text{ [eV]}$
     - **里德伯公式（リュードベリの式）**：
       $$\frac{1}{\lambda} = R\left(\frac{1}{n'^2} - \frac{1}{n^2}\right) \quad (n' = 1, 2, 3, \cdots;\ n = n'+1, n'+2, \cdots)$$
       其中 $n'=1$ 为**莱曼系（ライマン系列，紫外线）**，$n'=2$ 为**巴尔末系（バルマー系列，可见光）**，$n'=3$ 为**帕邢系（パッシェン系列，红外线）**。

### 1.3 中日物理体系与习惯差异提醒

| 对比维度 | 中国国内高中物理习惯 | 日本 EJU / 高中物理习惯（授课必强调） |
| :--- | :--- | :--- |
| **交流电有效值符号** | 常用 $U, I$（或 $U_{\text{有}}$），峰值用 $U_m, I_m$ | 峰值一律用 **$V_0, I_0$**，有效值一律加下标 `e` 写作 **$V_e, I_e$**（effective value），如变压器公式写作 $\dfrac{V_{1e}}{V_{2e}} = \dfrac{I_{2e}}{I_{1e}} = \dfrac{N_1}{N_2}$。 |
| **频率符号区分** | 交流与光学常混用 $f$ 或 $\nu$ | 交流电路中频率用 **$f$（周波数）**，角频率用 **$\omega$（角周波数）**；原子/光学中频率常用 **$\nu$（振動数，读作 ニュー）**，如 $E = h\nu$。 |
| **逸出功与静电力常量** | 逸出功常写 $W_0$，库仑常量写 $k$ | 逸出功通常直接写 **$W$（仕事関数）**；库仑定律比例常数一律写 **$k_0$**（以与波数/弹簧常量 $k$ 区分）。 |
| **课程归属与教材勘误** | 交流电属选修，原子物理属近代物理 | 日本官方课标中本切片全部属于「物理（専門）」，但本教材页眉沿用了「物理基礎」。此外教材存在三处需在课堂指出的瑕疵：① **P.107（页码 106）**两幅交流电路图漏印了交流电源圆圈符号；② **P.111（页码 110）**X 射线页未列出必考的最短波长公式 $\lambda_0 = \frac{hc}{eV}$；③ **P.113（页码 112）**大标题将「**ボーア模型**（Bohr 模型）」误印为「**ボール模型**（球模型）」！ |

---

## 2. 日文物理核心词汇与公式假名注音（板书必备）

### 2.1 核心物理词汇表

#### 交流电路进阶（変圧器・RLC回路）
- **変圧器（へんあつき / hen'atsuki）** — 变压器
- **相互誘導（そうごゆうどう / sōgo yūdō）** — 互感（相互诱导）
- **交流（こうりゅう / kōryū）** — 交流电
- **直流（ちょくりゅう / chokuryū）** — 直流电
- **実効値（じっこうち / jikkōchi）** — 有效值（下标 $e$）
- **一次コイル（いちじこいる / ichiji koiru）** — 一次线圈（原线圈）
- **二次コイル（にじこいる / niji koiru）** — 二次线圈（副线圈）
- **巻数（まきすう / makisū）** — 匝数（$N_1, N_2$）
- **自己インダクタンス（じこいんだくたんす / jiko indakutansu）** — 自感系数（$L$）
- **電気容量（でんきようりょう / denki yōryō）** — 电容（$C$）
- **位相（いそう / isō）** — 相位
- **位相が遅れる（いそうがおくれる / isō ga okureru）** — 相位滞后
- **位相が進む（いそうがすすむ / isō ga susumu）** — 相位超前
- **リアクタンス（りあくたんす / riakutansu）** — 电抗（感抗 $\omega L$、容抗 $\frac{1}{\omega C}$）
- **RLC直列回路（あーるえるしーちょくれつかいろ / RLC chokuretsu kairo）** — RLC 串联电路
- **インピーダンス（いんぴーだんす / inpīdansu）** — 阻抗（$Z$）
- **共振（きょうしん / kyōshin）** — 谐振 / 共振
- **共振角周波数（きょうしんかくしゅうはすう / kyōshin kakushūhasū）** — 谐振角频率（$\omega_0$）
- **共振周波数（きょうしんしゅうはすう / kyōshin shūhasū）** — 谐振频率（$f_0$）

#### 原子物理（陰極線・光電効果・X線・量子模型）
- **原子（げんし / genshi）** — 原子
- **陰極線（いんきょくせん / inkyokusen）** — 阴极射线
- **クルックス管（くるっくすかん / kurukkusu-kan）** — 克鲁克斯管（阴极射线管）
- **陰極（いんきょく / inkyoku）** — 阴极
- **陽極（ようきょく / yōkyoku）** — 阳极
- **蛍光（けいこう / keikō）** — 荧光
- **蛍光板（けいこうばん / keikōban）** — 荧光屏 / 荧光板
- **感光（かんこう / kankō）** — 感光
- **電離（でんり / denri）** — 电离
- **羽根車（はねぐるま / haneguruma）** — 叶轮 / 风车
- **直進性（ちょくしんせい / chokushinsei）** — 直进性
- **スリット（すりっと / suritto）** — 狭缝
- **比荷（ひか / hika）** — 比荷（$e/m$）
- **光電効果（こうでんこうか / kōden kōka）** — 光电效应
- **光電子（こうでんし / kōdenshi）** — 光电子
- **箔検電器（はくけんでんき / haku kendenki）** — 验电器（箔片验电器）
- **紫外線（しがいせん / shigaisen）** — 紫外线
- **光電管（こうでんかん / kōdenkan）** — 光电管
- **光子（こうし / kōshi）** — 光子
- **プランク定数（ぷらんくていすう / puranku teisū）** — 普朗克常数（$h$）
- **仕事関数（しごとかんすう / shigoto kansū）** — 逸出功（$W$）
- **限界振動数（げんかいしんどうすう / genkai shindōsū）** — 截止频率（$\nu_0$）
- **阻止電圧（そしでんあつ / soshi den'atsu）** — 遏止电压（$V_0$）
- **X線（えっくすせん / ekkusu-sen）** — X 射线
- **フィラメント（ふぃらめんと / firamento）** — 灯丝
- **熱電子（ねつでんし / netsudenshi）** — 热电子
- **加速電圧（かそくでんあつ / kasoku den'atsu）** — 加速电压
- **連続X線（れんぞくえっくすせん / renzoku ekkusu-sen）** — 连续 X 射线
- **特性X線 / 固有X線（とくせいえっくすせん / こゆうえっくすせん / tokusei / koyū ekkusu-sen）** — 特征 X 射线 / 固有 X 射线
- **最短波長（さいたんはちょう / saitan hachō）** — 最短波长（$\lambda_0$）
- **粒子性（りゅうしせい / ryūshisei）** — 粒子性
- **波動性（はどうせい / hadōsei）** — 波动性
- **物質波 / ド・ブロイ波（ぶっしつは / どぶろいは / busshitsuha / do buroi-ha）** — 物质波 / 德布罗意波
- **電子波（でんしは / denshiha）** — 电子波
- **コンプトン効果（こんぷとんこうか / konputon kōka）** — 康普顿效应
- **散乱X線（さんらんえっくすせん / sanran ekkusu-sen）** — 散射 X 射线
- **ボーア模型 / ボーアの原子模型（ぼーあもけい / bōa mokei）** — 玻尔原子模型（注意纠正教材误印“ボール模型”）
- **連続スペクトル（れんぞくすぺくとる / renzoku supekutoru）** — 连续光谱
- **線スペクトル（せんすぺくとる / sen supekutoru）** — 线状光谱
- **リュードベリの式（りゅーどべりのしき / ryūdoberi no shiki）** — 里德伯公式
- **ボーアの量子条件（ぼーあのりょうしじょうけん / bōa no ryōshi jōken）** — 玻尔量子条件
- **軌道半径（きどうはんけい / kidō hankei）** — 轨道半径
- **エネルギー準位（えねるぎーじゅんい / enerugī jun'i）** — 能级
- **基底状態（きていじょうたい / kitei jōtai）** — 基态（$n=1$）
- **励起状態（れいきじょうたい / reiki jōtai）** — 激发态（$n \ge 2$）

### 2.2 核心公式课堂口语读法（板书念法）

| 公式 | 日本课堂标准板书口语读法 |
| :--- | :--- |
| $\dfrac{V_{1e}}{V_{2e}} = \dfrac{I_{2e}}{I_{1e}} = \dfrac{N_1}{N_2}$ | 「ブイ・ツー・イーぶんの・ブイ・ワン・イー、イコール、アイ・ワン・イーぶんの・アイ・ツー・イー、イコール、エヌ・ツーぶんの・エヌ・ワン」 |
| $V_0 = \omega L I_0,\quad V_0 = \dfrac{I_0}{\omega C}$ | 「ブイゼロ・イコール、オメガ・エル・アイゼロ」「ブイゼロ・イコール、オメガ・シーぶんの・アイゼロ」 |
| $Z = \sqrt{R^2 + \left(\omega L - \dfrac{1}{\omega C}\right)^2}$ | 「ゼット・イコール、ルート、アールにじょう、たす、かっこ、オメガエル・ひく・オメガシーぶんのいち、かっことじの・にじょう」 |
| $f_0 = \dfrac{1}{2\pi\sqrt{LC}}$ | 「エフゼロ・イコール、にパイ・ルート・エルシーぶんの・いち」 |
| $E = h\nu = \dfrac{hc}{\lambda}$ | 「イー・イコール、エイチ・ニュー、イコール、ラムダぶんの・エイチ・シー」 |
| $K_M = h\nu - W$ | 「ケーエム・イコール、エイチ・ニュー、ひく、ダブリュー」 |
| $\lambda_0 = \dfrac{hc}{eV}$ | 「ラムダゼロ・イコール、イー・ブイぶんの・エイチ・シー」 |
| $\lambda = \dfrac{h}{p} = \dfrac{h}{mv}$ | 「ラムダ・イコール、ピーぶんの・エイチ、イコール、エム・ブイぶんの・エイチ」 |
| $\Delta\lambda = \dfrac{h}{mc}(1 - \cos\varphi)$ | 「デルタ・ラムダ・イコール、エムシーぶんの・エイチ、かっこ、いち・ひく・コサイン・ファイ」 |
| $mvr = n\dfrac{h}{2\pi}$ | 「エム・ブイ・アール・イコール、エヌ・かける、にパイぶんの・エイチ」 |
| $\dfrac{1}{\lambda} = R\left(\dfrac{1}{n'^2} - \dfrac{1}{n^2}\right)$ | 「ラムダぶんのいち・イコール、アール、かっこ、エヌダッシュにじょうぶんのいち・ひく・エヌにじょうぶんのいち」 |

---

## 3. 逐题深度解析（一题一解，不可跳步）

> **说明**：本切片教材原文（P.106–P.113，页码 105–112）全部为知识点与公式精讲页（P.114–P.115 为版权页与封底），**原书不含编号例题或练习题**。为保证授课闭环并直接覆盖 EJU 真实考法，下面针对本切片五大核心模块精编 **5 道 EJU 标准典例 / 核心推导题**，逐一配齐多色 SVG 板书图与纯日文规范解答。

---

### 核心典例 1（对应教材 P.106–108 / 页码 105–107）：理想变压器与 RLC 串联谐振电路

#### 【原题重现与翻译】
> **日文题目（针对教材 P.106–108 核心公式配套典例）**：  
> 一次コイルの巻数が $N_1$，二次コイルの巻数が $N_2$ の理想変圧器の一次側に，実効値 $V_{1e}$，角周波数 $\omega$ の交流電源を接続した。二次側には抵抗値 $R$ の抵抗，自己インダクタンス $L$ のコイル，電気容量 $C$ のコンデンサーを直列に接続した。  
> (1) 二次側の電圧の実効値 $V_{2e}$ を求めよ。  
> (2) 二次側の RLC 直列回路のインピーダンス $Z$ と，二次側を流れる電流の実効値 $I_{2e}$ を求めよ。  
> (3) 一次側を流れる電流の実効値 $I_{1e}$ を求めよ。  
> (4) 二次側の電流が最大となる共振角周波数 $\omega_0$ と，そのときの二次側消費電力 $P$ を求めよ。
>
> **中文翻译**：  
> 将有效值为 $V_{1e}$、角频率为 $\omega$ 的交流电源接入一次线圈匝数为 $N_1$、二次线圈匝数为 $N_2$ 的理想变压器的原边。副边串联接入阻值为 $R$ 的电阻、自感系数为 $L$ 的线圈和电容为 $C$ 的电容器。  
> (1) 求副边电压的有效值 $V_{2e}$。  
> (2) 求副边 RLC 串联电路的阻抗 $Z$ 及流过副边的电流有效值 $I_{2e}$。  
> (3) 求流过原边的电流有效值 $I_{1e}$。  
> (4) 求使副边电流达到最大的谐振角频率 $\omega_0$ 以及此时副边的消耗功率 $P$。

#### 【考点与模型定位】
**理想变压器变比 ＋ RLC 串联阻抗矢量图 ＋ 谐振最大电流与功率**（一次打通教材 P.106–108 全部交流公式，顺便补全教材 P.107 缺失的交流电源符号）。

#### 【多色矢量图解（SVG）】

<svg viewBox="0 0 420 260" width="420" height="260" xmlns="http://www.w3.org/2000/svg" style="background:#fafafa;border:1px solid #e5e7eb;border-radius:8px;">
  <defs>
    <marker id="arr-blue-008-1" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0,0 L0,6 L7,3 z" fill="#2563eb"/></marker>
    <marker id="arr-grn-008-1" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0,0 L0,6 L7,3 z" fill="#16a34a"/></marker>
    <marker id="arr-red-008-1" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0,0 L0,6 L7,3 z" fill="#dc2626"/></marker>
    <marker id="arr-blk-008-1" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0,0 L0,6 L7,3 z" fill="#111827"/></marker>
  </defs>
  <!-- 左侧：变压器与RLC电路 -->
  <text x="16" y="20" font-size="11" font-weight="bold" fill="#374151">変圧器 ＋ RLC直列回路</text>
  <!-- 交流电源 -->
  <circle cx="38" cy="115" r="14" fill="#fff" stroke="#111827" stroke-width="1.6"/>
  <path d="M 30 115 Q 34 107 38 115 T 46 115" fill="none" stroke="#111827" stroke-width="1.5"/>
  <text x="12" y="142" font-size="10" fill="#111827">V₁e, ω</text>
  <!-- 一次线圈导线与电流 -->
  <polyline points="38,101 38,55 88,55" fill="none" stroke="#374151" stroke-width="1.6"/>
  <polyline points="38,129 38,175 88,175" fill="none" stroke="#374151" stroke-width="1.6"/>
  <line x1="48" y1="47" x2="78" y2="47" stroke="#111827" stroke-width="1.5" stroke-dasharray="4,2" marker-end="url(#arr-blk-008-1)"/>
  <text x="53" y="42" font-size="10" fill="#111827">I₁e</text>
  <!-- 一次线圈绕组 -->
  <path d="M 88 55 Q 98 63 88 71 Q 98 79 88 87 Q 98 95 88 103 Q 98 111 88 119 Q 98 127 88 135 Q 98 143 88 151 Q 98 159 88 167 L 88 175" fill="none" stroke="#2563eb" stroke-width="1.8"/>
  <text x="68" y="118" font-size="10" fill="#2563eb">N₁</text>
  <!-- 铁芯 -->
  <line x1="102" y1="48" x2="102" y2="182" stroke="#4b5563" stroke-width="2.5"/>
  <line x1="108" y1="48" x2="108" y2="182" stroke="#4b5563" stroke-width="2.5"/>
  <!-- 二次线圈绕组 -->
  <path d="M 122 55 Q 112 65 122 75 Q 112 85 122 95 Q 112 105 122 115 Q 112 125 122 135 Q 112 145 122 155 Q 112 165 122 175" fill="none" stroke="#16a34a" stroke-width="1.8"/>
  <text x="128" y="118" font-size="10" fill="#16a34a">N₂</text>
  <!-- 二次回路导线 -->
  <line x1="122" y1="55" x2="155" y2="55" stroke="#374151" stroke-width="1.6"/>
  <!-- 电阻 R -->
  <rect x="155" y="48" width="28" height="14" fill="#fff" stroke="#374151" stroke-width="1.5"/>
  <text x="165" y="42" font-size="10" fill="#374151">R</text>
  <!-- 电感 L -->
  <path d="M 183 55 L 191 55 Q 195 45 199 55 Q 203 45 207 55 Q 211 45 215 55 Q 219 45 223 55 L 230 55" fill="none" stroke="#2563eb" stroke-width="1.6"/>
  <text x="203" y="42" font-size="10" fill="#2563eb">L</text>
  <!-- 电容 C -->
  <line x1="230" y1="55" x2="245" y2="55" stroke="#374151" stroke-width="1.6"/>
  <line x1="245" y1="43" x2="245" y2="67" stroke="#dc2626" stroke-width="2"/>
  <line x1="252" y1="43" x2="252" y2="67" stroke="#dc2626" stroke-width="2"/>
  <text x="244" y="38" font-size="10" fill="#dc2626">C</text>
  <polyline points="252,55 266,55 266,175 122,175" fill="none" stroke="#374151" stroke-width="1.6"/>
  <!-- 二次电流箭头 -->
  <line x1="220" y1="184" x2="180" y2="184" stroke="#111827" stroke-width="1.5" stroke-dasharray="4,2" marker-end="url(#arr-blk-008-1)"/>
  <text x="192" y="198" font-size="10" fill="#111827">I₂e</text>

  <!-- 分隔线 -->
  <line x1="278" y1="15" x2="278" y2="245" stroke="#d1d5db" stroke-dasharray="4,4"/>

  <!-- 右侧：RLC 电压相位矢量图 -->
  <text x="292" y="20" font-size="11" font-weight="bold" fill="#374151">電圧ベクトル図</text>
  <!-- 基准电流方向 -->
  <line x1="305" y1="140" x2="405" y2="140" stroke="#111827" stroke-width="1.4" stroke-dasharray="4,3" marker-end="url(#arr-blk-008-1)"/>
  <text x="396" y="153" font-size="10" fill="#111827">I₂</text>
  <!-- VR -->
  <line x1="305" y1="140" x2="365" y2="140" stroke="#16a34a" stroke-width="2.2" marker-end="url(#arr-grn-008-1)"/>
  <text x="322" y="155" font-size="10" fill="#16a34a">V_R = RI₂</text>
  <!-- VL 向上超前90度 -->
  <line x1="305" y1="140" x2="305" y2="55" stroke="#2563eb" stroke-width="2" marker-end="url(#arr-blue-008-1)"/>
  <text x="310" y="64" font-size="10" fill="#2563eb">V_L = ωLI₂</text>
  <!-- VC 向下滞后90度 -->
  <line x1="305" y1="140" x2="305" y2="195" stroke="#dc2626" stroke-width="2" marker-end="url(#arr-red-008-1)"/>
  <text x="310" y="195" font-size="10" fill="#dc2626">V_C = I₂/(ωC)</text>
  <!-- 合成电压 V2 -->
  <line x1="365" y1="140" x2="365" y2="85" stroke="#9ca3af" stroke-dasharray="3,3"/>
  <line x1="305" y1="85" x2="365" y2="85" stroke="#9ca3af" stroke-dasharray="3,3"/>
  <line x1="305" y1="140" x2="365" y2="85" stroke="#dc2626" stroke-width="2.2" marker-end="url(#arr-red-008-1)"/>
  <text x="369" y="88" font-size="10" font-weight="bold" fill="#dc2626">V₂ = ZI₂</text>
  <text x="288" y="226" font-size="9.5" fill="#374151">共振時：V_L = V_C → Z = R</text>
  <text x="288" y="242" font-size="9.5" fill="#2563eb">ω₀ = 1/√(LC)</text>
</svg>

#### 【日本考场规范分步解答】

**(1)** 理想変圧器の電圧と巻数の関係式 $\dfrac{V_{1e}}{V_{2e}} = \dfrac{N_1}{N_2}$ より，
$$V_{2e} = \frac{N_2}{N_1} V_{1e}$$

> 💡 讲师批注：记住口诀「**電圧は巻数に比例、電流は巻数に反比例**」（电压与匝数成正比，电流与匝数成反比）。下标 `e` 表示有效值，考场务必与题干符号一致。

**(2)** RLC 直列回路のインピーダンス $Z$ は，
$$Z = \sqrt{R^2 + \left(\omega L - \frac{1}{\omega C}\right)^2}$$
交流回路のオームの法則 $V_{2e} = Z I_{2e}$ より，二次側を流れる電流の実効値 $I_{2e}$ は，
$$I_{2e} = \frac{V_{2e}}{Z} = \frac{N_2 V_{1e}}{N_1 \sqrt{R^2 + \left(\omega L - \dfrac{1}{\omega C}\right)^2}}$$

> 💡 讲师批注：阻抗 $Z$ 的几何本质就是右侧 SVG 中的直角三角形斜边！千万不要把 $\omega L$ 和 $\frac{1}{\omega C}$ 相加，因为电感电压超前电流 $\frac{\pi}{2}$、电容电压滞后电流 $\frac{\pi}{2}$，二者相位相差 $\pi$（完全反向），所以是**相减**。

**(3)** 理想変圧器の電流と巻数の関係式 $\dfrac{I_{2e}}{I_{1e}} = \dfrac{N_1}{N_2}$ より，
$$I_{1e} = \frac{N_2}{N_1} I_{2e} = \left(\frac{N_2}{N_1}\right)^2 \frac{V_{1e}}{\sqrt{R^2 + \left(\omega L - \dfrac{1}{\omega C}\right)^2}}$$

> 💡 讲师批注：也可直接由能量守恒 $P_1 = P_2$ 验证，原边等效阻抗为 $Z_{\text{eq}} = \left(\frac{N_1}{N_2}\right)^2 Z$，这在国公立二次试验中非常常见。

**(4)** 二次側の電流 $I_{2e}$ が最大となるのは，インピーダンス $Z$ が最小となるとき，すなわち $\omega L - \dfrac{1}{\omega C} = 0$（共振状態）のときである。  
したがって，共振角周波数 $\omega_0$ は，
$$\omega_0 L = \frac{1}{\omega_0 C} \implies \omega_0^2 = \frac{1}{LC} \implies \omega_0 = \frac{1}{\sqrt{LC}}$$
このとき $Z = R$ となり，電圧と電流の位相差は $0$ であるから，消費電力 $P$ はすべて抵抗 $R$ で消費され，
$$P = \frac{V_{2e}^2}{R} = \frac{1}{R}\left(\frac{N_2}{N_1} V_{1e}\right)^2$$

> 💡 讲师批注：电感 $L$ 和电容 $C$ 在一个周期内的平均消耗功率恒为 $0$（只储能不耗能），电路消耗的有功功率永远只发生在电阻 $R$ 上（$P = R I_e^2$）。谐振时 $V_{2e}$ 全部加在 $R$ 两端，故直接用 $\frac{V_{2e}^2}{R}$ 一步出结果！

#### 【最终答案】
- **(1) $V_{2e} = \dfrac{N_2}{N_1} V_{1e}$**
- **(2) $Z = \sqrt{R^2 + \left(\omega L - \dfrac{1}{\omega C}\right)^2}$，$I_{2e} = \dfrac{N_2 V_{1e}}{N_1 \sqrt{R^2 + \left(\omega L - \dfrac{1}{\omega C}\right)^2}}$**
- **(3) $I_{1e} = \left(\dfrac{N_2}{N_1}\right)^2 \dfrac{V_{1e}}{\sqrt{R^2 + \left(\omega L - \dfrac{1}{\omega C}\right)^2}}$**
- **(4) $\omega_0 = \dfrac{1}{\sqrt{LC}}$，$P = \dfrac{1}{R}\left(\dfrac{N_2}{N_1} V_{1e}\right)^2$**

---

### 核心典例 2（对应教材 P.109 / 页码 108）：阴极射线在电场中的偏转与比荷测定

#### 【原题重现与翻译】
> **日文题目（针对教材 P.109 阴极射线管图配套典例）**：  
> 図のように，真空管内で陰極から出た電子（質量 $m$，電気量 $-e$）を加速電圧 $V_0$ で加速し，スリットを通して速さ $v_0$ で水平方向（$x$ 軸の正の向き）に打ち出した。その後，長さ $l$，間隔 $d$ の平行極板間（上側が $+$ 極，下側が $-$ 極，極板間電圧 $V$）に入射させた。重力は無視できるものとする。  
> (1) 加速後の電子の速さ $v_0$ を $e, m, V_0$ で表せ。  
> (2) 極板間を通過する際，電子は上向き・下向きのどちらに偏向するか。また，極板を出るときの $y$ 方向の変位 $y_1$ を $l, d, V, V_0$ で表せ。  
> (3) 極板間に紙面の表から裏へ向かう一様な磁束密度 $B$ の磁場を加えたところ，電子は直進した。電子の比荷 $\dfrac{e}{m}$ を $d, V, V_0, B$ で表せ。
>
> **中文翻译**：  
> 如图所示，在真空管内将从阴极射出的电子（质量 $m$，电荷量 $-e$）经加速电压 $V_0$ 加速，通过狭缝以速率 $v_0$ 沿水平方向（$x$ 轴正方向）射出。随后射入长为 $l$、间距为 $d$ 的平行极板间（上板为 $+$ 极，下板为 $-$ 极，板间电压为 $V$）。忽略重力。  
> (1) 用 $e, m, V_0$ 表示加速后电子的速率 $v_0$。  
> (2) 电子通过极板间时向上还是向下偏转？并用 $l, d, V, V_0$ 表示电子离开极板时在 $y$ 方向的偏转位移 $y_1$。  
> (3) 在极板间施加垂直纸面向里的匀强磁场（磁感应强度 $B$）后，电子恰好沿直线通过。用 $d, V, V_0, B$ 表示电子的比荷 $\dfrac{e}{m}$。

#### 【考点与模型定位】
**阴极射线偏转模型（汤姆孙测比荷原理）**（加速电场动能定理 ＋ 偏转电场类平抛运动 ＋ 速度选择器 $eE = ev_0B$）。

#### 【多色矢量图解（SVG）】

<svg viewBox="0 0 420 260" width="420" height="260" xmlns="http://www.w3.org/2000/svg" style="background:#fafafa;border:1px solid #e5e7eb;border-radius:8px;">
  <defs>
    <marker id="arr-blue-008-2" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0,0 L0,6 L7,3 z" fill="#2563eb"/></marker>
    <marker id="arr-red-008-2" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0,0 L0,6 L7,3 z" fill="#dc2626"/></marker>
    <marker id="arr-blk-008-2" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0,0 L0,6 L7,3 z" fill="#111827"/></marker>
  </defs>
  <!-- 阴极与狭缝 -->
  <line x1="28" y1="115" x2="28" y2="155" stroke="#374151" stroke-width="3"/>
  <text x="16" y="106" font-size="10" fill="#374151">陰極</text>
  <line x1="78" y1="90" x2="78" y2="127" stroke="#374151" stroke-width="2.5"/>
  <line x1="78" y1="143" x2="78" y2="180" stroke="#374151" stroke-width="2.5"/>
  <text x="58" y="84" font-size="10" fill="#374151">スリット</text>
  <text x="42" y="172" font-size="10" fill="#2563eb">加速 V₀</text>

  <!-- 中心参考线 x 轴 -->
  <line x1="28" y1="135" x2="385" y2="135" stroke="#9ca3af" stroke-width="1.2" stroke-dasharray="4,3" marker-end="url(#arr-blk-008-2)"/>
  <text x="389" y="139" font-size="11" font-style="italic" fill="#111827">x</text>

  <!-- 平行极板 -->
  <rect x="130" y="65" width="150" height="8" fill="#fee2e2" stroke="#dc2626" stroke-width="1.5"/>
  <text x="196" y="57" font-size="11" font-weight="bold" fill="#dc2626">＋極 (V)</text>
  <rect x="130" y="197" width="150" height="8" fill="#dbeafe" stroke="#2563eb" stroke-width="1.5"/>
  <text x="196" y="220" font-size="11" font-weight="bold" fill="#2563eb">－極</text>
  <!-- 极板尺寸 l 与 d -->
  <line x1="130" y1="232" x2="280" y2="232" stroke="#4b5563" stroke-width="1"/>
  <text x="200" y="246" font-size="11" font-style="italic" fill="#374151">l</text>
  <line x1="118" y1="73" x2="118" y2="197" stroke="#4b5563" stroke-width="1"/>
  <text x="106" y="139" font-size="11" font-style="italic" fill="#374151">d</text>

  <!-- 电场线 E (向下) -->
  <line x1="155" y1="78" x2="155" y2="190" stroke="#2563eb" stroke-width="1.2" stroke-dasharray="3,3" marker-end="url(#arr-blue-008-2)"/>
  <line x1="255" y1="78" x2="255" y2="190" stroke="#2563eb" stroke-width="1.2" stroke-dasharray="3,3" marker-end="url(#arr-blue-008-2)"/>
  <text x="160" y="185" font-size="10" fill="#2563eb">E = V/d</text>

  <!-- 电子入射速度与抛物线偏转轨迹 -->
  <line x1="82" y1="135" x2="124" y2="135" stroke="#111827" stroke-width="1.8" stroke-dasharray="5,3" marker-end="url(#arr-blk-008-2)"/>
  <text x="93" y="126" font-size="11" fill="#111827">v₀</text>
  <path d="M 130 135 Q 205 135 280 95" fill="none" stroke="#111827" stroke-width="2"/>
  <line x1="280" y1="95" x2="365" y2="50" stroke="#111827" stroke-width="1.8" stroke-dasharray="5,3" marker-end="url(#arr-blk-008-2)"/>
  <!-- 荧光板 -->
  <line x1="370" y1="35" x2="370" y2="215" stroke="#16a34a" stroke-width="3"/>
  <text x="352" y="232" font-size="10" fill="#16a34a">蛍光板</text>

  <!-- 电子受力（静电引力向上、洛伦兹力向下） -->
  <circle cx="205" cy="125" r="5" fill="#fef3c7" stroke="#b45309" stroke-width="1.5"/>
  <text x="202" y="128" font-size="9" font-weight="bold" fill="#92400e">-</text>
  <line x1="205" y1="120" x2="205" y2="85" stroke="#dc2626" stroke-width="2" marker-end="url(#arr-red-008-2)"/>
  <text x="211" y="96" font-size="10" fill="#dc2626">F_E = eE</text>
  <line x1="205" y1="130" x2="205" y2="165" stroke="#2563eb" stroke-width="1.8" marker-end="url(#arr-blue-008-2)"/>
  <text x="211" y="162" font-size="10" fill="#2563eb">f_L = ev₀B (直進時)</text>
  <!-- 偏转位移 y1 -->
  <line x1="280" y1="135" x2="280" y2="95" stroke="#dc2626" stroke-width="1.5"/>
  <text x="285" y="118" font-size="11" fill="#dc2626">y₁</text>
</svg>

#### 【日本考场规范分步解答】

**(1)** 加速区間におけるエネルギー保存則（運動エネルギーと仕事の定理）より，
$$\frac{1}{2}mv_0^2 = eV_0 \implies v_0 = \sqrt{\frac{2eV_0}{m}}$$

> 💡 讲师批注：电子从阴极（低电势）向阳极（高电势）加速，电势能减少 $eV_0$ 全部转化为动能。注意在高速非相对论范围内（EJU 默认）直接用 $\frac{1}{2}mv_0^2 = eV_0$。

**(2)** 平行極板間の電場は下向き（$+$ 極から $-$ 極向き）で大きさ $E = \dfrac{V}{d}$ である。電子は負電荷をもつため，電場と逆向きすなわち**上向き**に大きさ $F_E = eE = \dfrac{eV}{d}$ の静電気力を受ける。したがって，電子は**上向き**に偏向する。

極板間を通過する時間 $t$ は，水平方向（$x$ 方向）が等速直線運動であるから，
$$t = \frac{l}{v_0}$$
鉛直上向きを $y$ 軸の正とすると，$y$ 方向の加速度 $a_y$ は運動方程式 $ma_y = \dfrac{eV}{d}$ より，
$$a_y = \frac{eV}{md}$$
よって，極板を出るときの変位 $y_1$ は，
$$y_1 = \frac{1}{2}a_y t^2 = \frac{1}{2}\cdot\frac{eV}{md}\cdot\frac{l^2}{v_0^2}$$
これに (1) の $v_0^2 = \dfrac{2eV_0}{m}$ を代入すると，
$$y_1 = \frac{eVl^2}{2md} \cdot \frac{m}{2eV_0} = \frac{Vl^2}{4dV_0}$$

> 💡 讲师批注：极其经典的结论——**$y_1 = \dfrac{Vl^2}{4dV_0}$ 与粒子的质量 $m$ 和电荷量 $e$ 完全无关！** 只要经过同一加速电压 $V_0$ 再进入同一偏转电场，任何带电粒子的偏转轨迹完全重合。

**(3)** 紙面の表から裏へ向かう磁場 $B$ 中を右向きに運動する負電荷（電子）には，フレミングの左手の法則より**下向き**（電流の向きは左向き）に大きさ $f_L = ev_0 B$ のローレンツ力がはたらく。  
電子が直進する条件は，上向きの静電気力と下向きのローレンツ力がつりあうことであるから，
$$eE = ev_0 B \implies v_0 = \frac{E}{B} = \frac{V}{dB}$$
これを (1) の関係式 $\dfrac{1}{2}mv_0^2 = eV_0$ に代入すると，
$$\frac{e}{m} = \frac{v_0^2}{2V_0} = \frac{V^2}{2d^2 B^2 V_0}$$

> 💡 讲师批注：提醒学生用左手定则判断**负电荷**洛伦兹力时，中指必须指向速度的反方向（向左），磁场垂直向里（掌心朝外），大拇指恰好**向下**，与向上的静电力平衡！

#### 【最终答案】
- **(1) $v_0 = \sqrt{\dfrac{2eV_0}{m}}$**
- **(2) 上向き，$y_1 = \dfrac{Vl^2}{4dV_0}$**
- **(3) $\dfrac{e}{m} = \dfrac{V^2}{2d^2 B^2 V_0}$**

---

### 核心典例 3（对应教材 P.110 / 页码 109）：光电效应与遏止电压图像分析

#### 【原题重现与翻译】
> **日文题目（针对教材 P.110 光电管电路与公式配套典例）**：  
> 光電管の陰極 C に振動数 $\nu$ の単色光を当てたところ，光電子が飛び出した。陰極の金属の仕事関数を $W$，プランク定数を $h$，電子の質量を $m$，電気素量を $e$ とする。  
> (1) 飛び出す光電子の運動エネルギーの最大値 $K_M$ および速さの最大値 $v_{\max}$ を求めよ。  
> (2) 陰極 C に対して陽極 A の電位を低くしていき，光電流がちょうど $0$ になるときの電位差の大きさ（阻止電圧）$V_0$ を $\nu, h, W, e$ で表せ。  
> (3) 横軸に振動数 $\nu$，縦軸に阻止電圧 $V_0$ をとってグラフを描くと，傾き $a$，横軸切片 $\nu_0$ の直線が得られた。プランク定数 $h$ と仕事関数 $W$ を $e, a, \nu_0$ で表せ。
>
> **中文翻译**：  
> 用频率为 $\nu$ 的单色光照射光电管的阴极 C，有光电子逸出。设阴极金属的逸出功为 $W$，普朗克常数为 $h$，电子质量为 $m$，元电荷为 $e$。  
> (1) 求逸出光电子的最大动能 $K_M$ 及最大速率 $v_{\max}$。  
> (2) 逐渐降低阳极 A 相对于阴极 C 的电势，当光电流恰好减为 $0$ 时两极板间的电势差大小（遏止电压）记为 $V_0$，用 $\nu, h, W, e$ 表示 $V_0$。  
> (3) 以频率 $\nu$ 为横轴、遏止电压 $V_0$ 为纵轴作图，得到一条斜率为 $a$、横轴截距为 $\nu_0$ 的直线。用 $e, a, \nu_0$ 表示普朗克常数 $h$ 与逸出功 $W$。

#### 【考点与模型定位】
**光电效应方程 ＋ 遏止电压能量守恒 ＋ $V_0\text{-}\nu$ 线性图像反推物理常量**（EJU 原子物理第一高频大题模型）。

#### 【多色矢量图解（SVG）】

<svg viewBox="0 0 420 260" width="420" height="260" xmlns="http://www.w3.org/2000/svg" style="background:#fafafa;border:1px solid #e5e7eb;border-radius:8px;">
  <defs>
    <marker id="arr-blue-008-3" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0,0 L0,6 L7,3 z" fill="#2563eb"/></marker>
    <marker id="arr-red-008-3" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0,0 L0,6 L7,3 z" fill="#dc2626"/></marker>
    <marker id="arr-blk-008-3" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0,0 L0,6 L7,3 z" fill="#111827"/></marker>
  </defs>
  <!-- 左侧：光电管示意 -->
  <text x="18" y="22" font-size="11" font-weight="bold" fill="#374151">光電管（逆電圧 V₀）</text>
  <circle cx="105" cy="115" r="62" fill="#fff" stroke="#4b5563" stroke-width="1.8"/>
  <!-- 阴极 C（右侧弧形，正电势） -->
  <path d="M 135 72 A 50 50 0 0 1 135 158" fill="none" stroke="#dc2626" stroke-width="4"/>
  <text x="142" y="118" font-size="11" font-weight="bold" fill="#dc2626">C (+)</text>
  <!-- 阳极 A（左侧点，负电势） -->
  <circle cx="68" cy="115" r="5" fill="#2563eb"/>
  <text x="48" y="102" font-size="11" font-weight="bold" fill="#2563eb">A (-)</text>
  <!-- 入射光子波浪线 -->
  <path d="M 55 58 Q 62 52 68 62 T 82 68 T 96 76 T 112 85" fill="none" stroke="#16a34a" stroke-width="1.8"/>
  <line x1="112" y1="85" x2="128" y2="95" stroke="#16a34a" stroke-width="1.8" marker-end="url(#arr-blk-008-3)"/>
  <text x="20" y="54" font-size="10" fill="#16a34a">光子 hν</text>
  <!-- 光电子飞出与受反向静电力 -->
  <circle cx="116" cy="115" r="4.5" fill="#fef3c7" stroke="#b45309"/>
  <line x1="111" y1="115" x2="78" y2="115" stroke="#111827" stroke-width="1.6" stroke-dasharray="4,2" marker-end="url(#arr-blk-008-3)"/>
  <text x="86" y="108" font-size="10" fill="#111827">v_max</text>
  <line x1="116" y1="126" x2="140" y2="126" stroke="#dc2626" stroke-width="1.8" marker-end="url(#arr-red-008-3)"/>
  <text x="90" y="142" font-size="9.5" fill="#dc2626">減速力 eE</text>
  <text x="35" y="205" font-size="10" fill="#374151">Aに達する直前で v=0</text>
  <text x="42" y="222" font-size="10.5" font-weight="bold" fill="#2563eb">eV₀ = K_M = hν - W</text>

  <!-- 分隔线 -->
  <line x1="200" y1="15" x2="200" y2="245" stroke="#d1d5db" stroke-dasharray="4,4"/>

  <!-- 右侧：V0 - ν 图像 -->
  <text x="245" y="22" font-size="11" font-weight="bold" fill="#374151">阻止電圧 V₀ − 振動数 ν グラフ</text>
  <!-- 坐标轴 -->
  <line x1="220" y1="175" x2="405" y2="175" stroke="#374151" stroke-width="1.6" marker-end="url(#arr-blk-008-3)"/>
  <text x="406" y="180" font-size="11" font-style="italic" fill="#111827">ν</text>
  <line x1="240" y1="242" x2="240" y2="40" stroke="#374151" stroke-width="1.6" marker-end="url(#arr-blk-008-3)"/>
  <text x="246" y="48" font-size="11" font-style="italic" fill="#111827">V₀</text>
  <text x="226" y="188" font-size="10" fill="#374151">O</text>

  <!-- 延长虚线与实线 -->
  <line x1="240" y1="225" x2="290" y2="175" stroke="#9ca3af" stroke-width="1.5" stroke-dasharray="4,3"/>
  <line x1="290" y1="175" x2="388" y2="77" stroke="#dc2626" stroke-width="2.2"/>
  <!-- 截距标注 -->
  <circle cx="290" cy="175" r="3.5" fill="#dc2626"/>
  <text x="285" y="191" font-size="11" fill="#dc2626">ν₀</text>
  <circle cx="240" cy="225" r="3.5" fill="#2563eb"/>
  <text x="246" y="232" font-size="10" fill="#2563eb">-W/e</text>
  <!-- 斜率标注 -->
  <line x1="315" y1="150" x2="355" y2="150" stroke="#2563eb" stroke-width="1.2" stroke-dasharray="3,2"/>
  <line x1="355" y1="150" x2="355" y2="110" stroke="#2563eb" stroke-width="1.2" stroke-dasharray="3,2"/>
  <text x="359" y="135" font-size="10.5" fill="#2563eb">傾き a = h/e</text>
</svg>

#### 【日本考场规范分步解答】

**(1)** 光電効果における光電子 1 個のエネルギー保存則より，最大運動エネルギー $K_M$ は，
$$K_M = h\nu - W$$
また，$K_M = \dfrac{1}{2}mv_{\max}^2$ であるから，速さの最大値 $v_{\max}$ は，
$$\frac{1}{2}mv_{\max}^2 = h\nu - W \implies v_{\max} = \sqrt{\frac{2(h\nu - W)}{m}}$$

> 💡 讲师批注：提醒学生区分“光子能量 $h\nu$”与“光的强度（強さ）”。增强入射光强度只是增加**单位时间的光子数**（使饱和光电流增大），但**不会改变单个光子的能量 $h\nu$**，因此 $K_M$ 和遏止电压 $V_0$ 均与光强无关！

**(2)** 陽極 A の電位が陰極 C より $V_0$ だけ低いとき，最大の運動エネルギー $K_M$ で飛び出した光電子がちょうど陽極 A に到達する直前で速さ $0$ になる。  
静電気力のする仕事 $-eV_0$ と運動エネルギーの変化の関係より，
$$0 - K_M = -eV_0 \implies eV_0 = K_M = h\nu - W$$
したがって，阻止電圧 $V_0$ は，
$$V_0 = \frac{h}{e}\nu - \frac{W}{e}$$

**(3)** (2) の結果 $V_0 = \dfrac{h}{e}\nu - \dfrac{W}{e}$ は，$\nu$ の 1 次関数である。  
直線の傾き $a$ との比較より，
$$a = \frac{h}{e} \implies h = ea$$
また，横軸切片 $\nu = \nu_0$ では $V_0 = 0$ であるから，
$$0 = \frac{h}{e}\nu_0 - \frac{W}{e} \implies W = h\nu_0 = ea\nu_0$$

> 💡 讲师批注：金属种类改变时，只有逸出功 $W$（从而横截距 $\nu_0$ 和纵截距 $-W/e$）发生平移，而直线的**斜率 $\dfrac{h}{e}$ 是宇宙普适常数**，所有金属的 $V_0\text{-}\nu$ 直线彼此平行！这是 EJU 选择题极爱的图像陷阱。

#### 【最终答案】
- **(1) $K_M = h\nu - W$，$v_{\max} = \sqrt{\dfrac{2(h\nu - W)}{m}}$**
- **(2) $V_0 = \dfrac{h\nu - W}{e}$**
- **(3) $h = ea$，$W = ea\nu_0$**

---

### 核心典例 4（对应教材 P.111–112 / 页码 110–111）：X 射线最短波长与康普顿散射

#### 【原题重现与翻译】
> **日文题目（针对教材 P.111–112 X 射线与康普顿效应配套典例）**：  
> (1) 加速電圧 $V$ で加速した電子を陽極の金属ターゲットに衝突させると X 線が発生する。発生する連続 X 線の最短波長 $\lambda_0$ を，プランク定数 $h$，光速 $c$，電気素量 $e$，$V$ を用いて表せ。また，加速電圧 $V$ を大きくしたとき，連続 X 線の最短波長 $\lambda_0$ と特性 X 線の波長はそれぞれどのように変化するか。  
> (2) 波長 $\lambda$ の X 線を静止している質量 $m$ の電子に当てたところ，入射方向と角 $\varphi = 90^\circ$ をなす方向に波長 $\lambda'$ の X 線が散乱された。散乱後の波長 $\lambda'$ を $\lambda, h, m, c$ で表し，このとき電子が得た運動エネルギー $K$ を $h, c, \lambda, \lambda'$ で表せ。
>
> **中文翻译**：  
> (1) 将经加速电压 $V$ 加速的电子撞击阳极金属靶产生 X 射线。用普朗克常数 $h$、光速 $c$、元电荷 $e$、$V$ 表示所产生连续 X 射线的最短波长 $\lambda_0$。此外，增大加速电压 $V$ 时，连续 X 射线的最短波长 $\lambda_0$ 与特征 X 射线的波长分别如何变化？  
> (2) 将波长为 $\lambda$ 的 X 射线照射到静止的、质量为 $m$ 的电子上，在与入射方向成 $\varphi = 90^\circ$ 的方向上测得散射 X 射线的波长为 $\lambda'$。用 $\lambda, h, m, c$ 表示散射后的波长 $\lambda'$，并用 $h, c, \lambda, \lambda'$ 表示此时电子获得的动能 $K$。

#### 【考点与模型定位】
**X 射线光谱（杜安-亨特定律 $\lambda_0 = \frac{hc}{eV}$）＋ 康普顿散射波长偏移与能量守恒**（直接补足教材 P.111 遗漏的最短波长公式，并串联 P.112 康普顿效应）。

#### 【多色矢量图解（SVG）】

<svg viewBox="0 0 420 260" width="420" height="260" xmlns="http://www.w3.org/2000/svg" style="background:#fafafa;border:1px solid #e5e7eb;border-radius:8px;">
  <defs>
    <marker id="arr-blue-008-4" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0,0 L0,6 L7,3 z" fill="#2563eb"/></marker>
    <marker id="arr-grn-008-4" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0,0 L0,6 L7,3 z" fill="#16a34a"/></marker>
    <marker id="arr-red-008-4" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0,0 L0,6 L7,3 z" fill="#dc2626"/></marker>
    <marker id="arr-blk-008-4" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0,0 L0,6 L7,3 z" fill="#111827"/></marker>
  </defs>
  <!-- 左侧：X 射线光谱图 -->
  <text x="16" y="22" font-size="11" font-weight="bold" fill="#374151">X線スペクトル（V 増大時）</text>
  <line x1="30" y1="200" x2="195" y2="200" stroke="#374151" stroke-width="1.6" marker-end="url(#arr-blk-008-4)"/>
  <text x="180" y="216" font-size="10" fill="#111827">波長 λ</text>
  <line x1="30" y1="200" x2="30" y2="40" stroke="#374151" stroke-width="1.6" marker-end="url(#arr-blk-008-4)"/>
  <text x="35" y="48" font-size="10" fill="#111827">強さ</text>
  <!-- 原加速电压 V 曲线 -->
  <path d="M 65 200 Q 92 120 120 155 L 124 85 L 128 160 L 138 110 L 142 170 Q 160 190 185 194" fill="none" stroke="#2563eb" stroke-width="1.8"/>
  <text x="60" y="214" font-size="10" fill="#2563eb">λ₀</text>
  <!-- 增大电压 V' > V 曲线（左移但特征峰位置不变） -->
  <path d="M 46 200 Q 76 80 120 130 L 124 55 L 128 135 L 138 82 L 142 148 Q 160 180 185 188" fill="none" stroke="#dc2626" stroke-width="1.6" stroke-dasharray="4,2"/>
  <text x="38" y="214" font-size="10" fill="#dc2626">λ₀'</text>
  <text x="112" y="48" font-size="9.5" fill="#dc2626">特性X線(位置不変)</text>
  <text x="38" y="238" font-size="9.5" fill="#374151">V 大 → λ₀ = hc/(eV) 左へ移動</text>

  <!-- 分隔线 -->
  <line x1="208" y1="15" x2="208" y2="245" stroke="#d1d5db" stroke-dasharray="4,4"/>

  <!-- 右侧：康普顿散射示意图 -->
  <text x="232" y="22" font-size="11" font-weight="bold" fill="#374151">コンプトン効果（φ = 90°）</text>
  <!-- 入射光子 -->
  <line x1="225" y1="130" x2="295" y2="130" stroke="#16a34a" stroke-width="2" marker-end="url(#arr-grn-008-4)"/>
  <text x="224" y="118" font-size="10" fill="#16a34a">入射X線 (λ, p=h/λ)</text>
  <!-- 延长参考虚线 -->
  <line x1="305" y1="130" x2="390" y2="130" stroke="#9ca3af" stroke-dasharray="4,3"/>
  <!-- 静止电子 -->
  <circle cx="305" cy="130" r="6" fill="#fef3c7" stroke="#b45309" stroke-width="1.5"/>
  <text x="301" y="133" font-size="9" font-weight="bold" fill="#92400e">e⁻</text>
  <!-- 散射光子（向上 90 度） -->
  <line x1="305" y1="124" x2="305" y2="52" stroke="#dc2626" stroke-width="2" marker-end="url(#arr-red-008-4)"/>
  <text x="312" y="64" font-size="10" fill="#dc2626">散乱X線</text>
  <text x="312" y="78" font-size="10" fill="#dc2626">(λ', p'=h/λ')</text>
  <!-- 直角符号 -->
  <polyline points="305,114 321,114 321,130" fill="none" stroke="#dc2626" stroke-width="1.3"/>
  <text x="325" y="116" font-size="10" fill="#dc2626">φ=90°</text>
  <!-- 反冲电子 -->
  <line x1="309" y1="135" x2="370" y2="195" stroke="#111827" stroke-width="1.8" stroke-dasharray="5,3" marker-end="url(#arr-blk-008-4)"/>
  <text x="335" y="212" font-size="10" fill="#111827">反跳電子 (K, mv)</text>
  <text x="225" y="238" font-size="9.5" fill="#2563eb">Δλ = (h/mc)(1 - cos90°) = h/(mc)</text>
</svg>

#### 【日本考场规范分步解答】

**(1)** 加速電圧 $V$ で加速された電子 1 個の運動エネルギーは $eV$ である。  
このエネルギーがすべて 1 個の X 線光子のエネルギーに変換されるとき，光子のエネルギーは最大となり，波長は最短（$\lambda_0$）となる。エネルギー保存則より，
$$eV = \frac{hc}{\lambda_0} \implies \lambda_0 = \frac{hc}{eV}$$
また，加速電圧 $V$ を大きくすると，
- **連続 X 線の最短波長 $\lambda_0$**：$\lambda_0 \propto \dfrac{1}{V}$ より**短くなる**（スペクトルの左端が左へ移動する）。
- **特性 X 線の波長**：陽極ターゲットの金属原子固有のエネルギー準位差で決まるため，**変化しない**（強さだけが大きくなる）。

> 💡 讲师批注：这两点对比是 EJU 物理 X 射线题目的“必杀考点”：改电压 $V \implies$ 动 $\lambda_0$、不动特性峰；改阳极金属材料 $\implies$ 不动 $\lambda_0$、动特性峰！

**(2)** コンプトン効果による波長の伸びの公式 $\Delta \lambda = \lambda' - \lambda = \dfrac{h}{mc}(1 - \cos\varphi)$ に $\varphi = 90^\circ$（$\cos 90^\circ = 0$）を代入すると，
$$\lambda' - \lambda = \frac{h}{mc}(1 - 0) = \frac{h}{mc} \implies \lambda' = \lambda + \frac{h}{mc}$$
また，衝突前後のエネルギー保存則より，入射光子のエネルギーは散乱光子のエネルギーと電子の運動エネルギー $K$ の和に等しいから，
$$\frac{hc}{\lambda} = \frac{hc}{\lambda'} + K \implies K = hc\left(\frac{1}{\lambda} - \frac{1}{\lambda'}\right)$$

> 💡 讲师批注：コンプトン公式 $\Delta\lambda = \frac{h}{mc}(1 - \cos\varphi)$ 的本质是**光子-电子弹性碰撞的动量守恒＋能量守恒**联立（并在 $v \ll c$ 下近似）。注意波长偏移量 $\Delta\lambda$ 居然与入射波长 $\lambda$ 无关，只与散射角 $\varphi$ 有关！

#### 【最终答案】
- **(1) $\lambda_0 = \dfrac{hc}{eV}$；最短波長 $\lambda_0$ は短くなり，特性 X 線の波長は変化しない。**
- **(2) $\lambda' = \lambda + \dfrac{h}{mc}$，$K = hc\left(\dfrac{1}{\lambda} - \dfrac{1}{\lambda'}\right)$**

---

### 核心典例 5（对应教材 P.113 / 页码 112）：玻尔氢原子模型完整推导与里德伯公式

#### 【原题重现与翻译】
> **日文题目（针对教材 P.113 玻尔模型四大核心公式完整推导）**：  
> ボーアの水素原子模型では，質量 $m$，電気量 $-e$ の電子が静止した陽子（電気量 $+e$）のまわりを半径 $r$，速さ $v$ で等速円運動していると考える。クーロンの法則の比例定数を $k_0$，プランク定数を $h$，光速を $c$，量子数を $n\ (n = 1, 2, 3, \cdots)$ とする。  
> (1) 電子の等速円運動の運動方程式と，ボーアの量子条件（ド・ブロイ波の定常波条件 $2\pi r = n\lambda$ から導け）を立て，軌道半径 $r_n$ を $n, h, k_0, m, e$ で表せ。  
> (2) 量子数 $n$ の定常状態における電子の力学的エネルギー（エネルギー準位）$E_n$ を $n, h, k_0, m, e$ で表せ。  
> (3) 電子が量子数 $n$ の状態から $n'\ (n > n')$ の状態へ遷移するときに放出される光子の波長 $\lambda$ について，リュードベリの式 $\dfrac{1}{\lambda} = R\left(\dfrac{1}{n'^2} - \dfrac{1}{n^2}\right)$ を導き，リュードベリ定数 $R$ を $h, c, k_0, m, e$ で表せ。
>
> **中文翻译**：  
> 在玻尔氢原子模型中，设质量为 $m$、电荷量为 $-e$ 的电子绕静止的质子（电荷量 $+e$）做半径为 $r$、速率为 $v$ 的匀速圆周运动。设库仑定律比例常数为 $k_0$，普朗克常数为 $h$，光速为 $c$，量子数为 $n\ (n = 1, 2, 3, \cdots)$。  
> (1) 列出电子做匀速圆周运动的运动方程与玻尔量子条件（请由德布罗意波的驻波条件 $2\pi r = n\lambda$ 导出），并用 $n, h, k_0, m, e$ 表示轨道半径 $r_n$。  
> (2) 用 $n, h, k_0, m, e$ 表示量子数为 $n$ 的定态中电子的机械能（能级）$E_n$。  
> (3) 电子从量子数 $n$ 的状态跃迁到 $n'\ (n > n')$ 的状态时辐射波长为 $\lambda$ 的光子，推导里德伯公式 $\dfrac{1}{\lambda} = R\left(\dfrac{1}{n'^2} - \dfrac{1}{n^2}\right)$，并用 $h, c, k_0, m, e$ 表示里德伯常量 $R$。

#### 【考点与模型定位】
**玻尔氢原子模型“全套公式推导”**（EJU 及日本国公立大学物理最经典的压轴推导题，考场上必须能从零默写并推导，切忌死记硬背导致 $\pi$ 或 $2$ 的系数出错）。

#### 【多色矢量图解（SVG）】

<svg viewBox="0 0 420 260" width="420" height="260" xmlns="http://www.w3.org/2000/svg" style="background:#fafafa;border:1px solid #e5e7eb;border-radius:8px;">
  <defs>
    <marker id="arr-blue-008-5" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0,0 L0,6 L7,3 z" fill="#2563eb"/></marker>
    <marker id="arr-red-008-5" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0,0 L0,6 L7,3 z" fill="#dc2626"/></marker>
    <marker id="arr-blk-008-5" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0,0 L0,6 L7,3 z" fill="#111827"/></marker>
  </defs>
  <!-- 左侧：电子圆周运动与驻波轨道 -->
  <text x="18" y="20" font-size="11" font-weight="bold" fill="#374151">ボーア模型（円運動＋定常波）</text>
  <!-- 轨道圆 -->
  <circle cx="105" cy="130" r="62" fill="none" stroke="#9ca3af" stroke-width="1.4" stroke-dasharray="4,3"/>
  <!-- 驻波示意 (n=3 近似波动环) -->
  <path d="M 167 130 C 175 100 142 74 136 76 C 122 60 88 60 74 76 C 68 74 35 100 43 130 C 35 160 68 186 74 184 C 88 200 122 200 136 184 C 142 186 175 160 167 130 Z" fill="none" stroke="#16a34a" stroke-width="1.5"/>
  <!-- 原子核（质子） -->
  <circle cx="105" cy="130" r="10" fill="#fee2e2" stroke="#dc2626" stroke-width="1.6"/>
  <text x="99" y="134" font-size="10" font-weight="bold" fill="#dc2626">+e</text>
  <!-- 电子 -->
  <circle cx="167" cy="130" r="6" fill="#dbeafe" stroke="#2563eb" stroke-width="1.5"/>
  <text x="176" y="134" font-size="10" fill="#2563eb">-e (m)</text>
  <!-- 库仑向心力（指向圆心，红） -->
  <line x1="161" y1="130" x2="122" y2="130" stroke="#dc2626" stroke-width="2" marker-end="url(#arr-red-008-5)"/>
  <text x="122" y="146" font-size="9.5" fill="#dc2626">F = k₀e²/r²</text>
  <!-- 切向速度 v（黑虚线） -->
  <line x1="167" y1="124" x2="167" y2="76" stroke="#111827" stroke-width="1.8" stroke-dasharray="5,3" marker-end="url(#arr-blk-008-5)"/>
  <text x="173" y="88" font-size="11" fill="#111827">v</text>
  <text x="26" y="222" font-size="10" fill="#16a34a">定常波条件：2πr = nλ = n(h/mv)</text>
  <text x="45" y="240" font-size="10" fill="#374151">⇒ mvr = n·h/(2π)</text>

  <!-- 分隔线 -->
  <line x1="215" y1="15" x2="215" y2="245" stroke="#d1d5db" stroke-dasharray="4,4"/>

  <!-- 右侧：氢原子能级与跃迁图 -->
  <text x="242" y="20" font-size="11" font-weight="bold" fill="#374151">水素原子のエネルギー準位</text>
  <!-- 能级线 -->
  <line x1="245" y1="50" x2="365" y2="50" stroke="#374151" stroke-width="1.2" stroke-dasharray="3,2"/>
  <text x="223" y="54" font-size="9" fill="#374151">n=∞</text>
  <text x="370" y="54" font-size="9.5" fill="#374151">0 eV</text>

  <line x1="245" y1="74" x2="365" y2="74" stroke="#374151" stroke-width="1.5"/>
  <text x="223" y="78" font-size="9" fill="#374151">n=3</text>
  <text x="370" y="78" font-size="9.5" fill="#374151">-1.51</text>

  <line x1="245" y1="112" x2="365" y2="112" stroke="#374151" stroke-width="1.6"/>
  <text x="223" y="116" font-size="9" fill="#374151">n=2</text>
  <text x="370" y="116" font-size="9.5" fill="#374151">-3.40</text>

  <line x1="245" y1="215" x2="365" y2="215" stroke="#111827" stroke-width="2.2"/>
  <text x="223" y="219" font-size="9.5" font-weight="bold" fill="#111827">n=1</text>
  <text x="370" y="219" font-size="9.5" font-weight="bold" fill="#111827">-13.6</text>

  <!-- 莱曼系跃迁 (n=2 -> 1, 蓝) -->
  <line x1="275" y1="112" x2="275" y2="210" stroke="#2563eb" stroke-width="2" marker-end="url(#arr-blue-008-5)"/>
  <text x="235" y="166" font-size="9.5" fill="#2563eb">ライマン</text>
  <text x="238" y="179" font-size="9" fill="#2563eb">(紫外線)</text>

  <!-- 巴尔末系跃迁 (n=3 -> 2, 红) -->
  <line x1="330" y1="74" x2="330" y2="108" stroke="#dc2626" stroke-width="2" marker-end="url(#arr-red-008-5)"/>
  <text x="335" y="96" font-size="9.5" fill="#dc2626">バルマー</text>
  <text x="336" y="107" font-size="8.5" fill="#dc2626">(可視光)</text>
  <text x="242" y="240" font-size="9.5" fill="#374151">放出光子：hν = hc/λ = E_n - E_n'</text>
</svg>

#### 【日本考场规范分步解答】

**(1)** 陽子と電子の間にはたらくクーロン力が向心力となるから，円運動の運動方程式は，
$$m\frac{v^2}{r} = k_0 \frac{e^2}{r^2} \quad \cdots\text{①}$$
また，電子のド・ブロイ波長 $\lambda = \dfrac{h}{mv}$ が円軌道上で定常波をつくる条件 $2\pi r = n\lambda$ より，ボーアの量子条件は，
$$2\pi r = n\frac{h}{mv} \implies mvr = n\frac{h}{2\pi} \quad \cdots\text{②}$$
② より $v = \dfrac{nh}{2\pi mr}$ を ① に代入して $v$ を消去すると，
$$\frac{m}{r}\cdot\frac{n^2 h^2}{4\pi^2 m^2 r^2} = k_0 \frac{e^2}{r^2} \implies \frac{n^2 h^2}{4\pi^2 m r} = k_0 e^2$$
よって，量子数 $n$ の軌道半径 $r_n$ は，
$$r_n = \frac{h^2}{4\pi^2 k_0 m e^2} \cdot n^2 \qquad (n = 1, 2, 3, \cdots)$$

> 💡 讲师批注：牢记“**轨道半径与 $n^2$ 成正比**”（$r_1 : r_2 : r_3 = 1 : 4 : 9$），同时顺便纠正教材 P.113 大标题的印刷错误——是「**ボーア模型**（Bohr）」，不是「ボール模型」！

**(2)** 電子の力学的エネルギー $E_n$ は，運動エネルギー $K = \dfrac{1}{2}mv^2$ と静電気力による位置エネルギー $U = -k_0 \dfrac{e^2}{r_n}$（無限遠基準）の和である。  
① より $mv^2 = k_0 \dfrac{e^2}{r_n}$ であるから，$K = \dfrac{1}{2}k_0 \dfrac{e^2}{r_n}$ となり，
$$E_n = K + U = \frac{1}{2}k_0\frac{e^2}{r_n} - k_0\frac{e^2}{r_n} = -\frac{k_0 e^2}{2r_n}$$
これに (1) の $r_n$ を代入すると，
$$E_n = -\frac{k_0 e^2}{2} \cdot \frac{4\pi^2 k_0 m e^2}{h^2 n^2} = -\frac{2\pi^2 k_0^2 m e^4}{h^2} \cdot \frac{1}{n^2} \qquad (n = 1, 2, 3, \cdots)$$

> 💡 讲师批注：万有引力卫星和氢原子电子同构！记住黄金结论：**$E = -K = \dfrac{1}{2}U = -\dfrac{k_0 e^2}{2r}$**。千万别漏掉负号（束缚态总能量必为负），且 $n$ 越大，轨道越远，能级 $E_n$ 越接近 $0$（能量越高）。

**(3)** 振動数条件 $h\nu = \dfrac{hc}{\lambda} = E_n - E_{n'}$ に (2) の結果を代入すると，
$$\frac{hc}{\lambda} = \left(-\frac{2\pi^2 k_0^2 m e^4}{h^2 n^2}\right) - \left(-\frac{2\pi^2 k_0^2 m e^4}{h^2 n'^2}\right) = \frac{2\pi^2 k_0^2 m e^4}{h^2}\left(\frac{1}{n'^2} - \frac{1}{n^2}\right)$$
両辺を $hc$ で割ると，
$$\frac{1}{\lambda} = \frac{2\pi^2 k_0^2 m e^4}{c h^3}\left(\frac{1}{n'^2} - \frac{1}{n^2}\right)$$
したがって，リュードベリ定数 $R$ は，
$$R = \frac{2\pi^2 k_0^2 m e^4}{c h^3}$$

> 💡 讲师批注：注意括号内是 **$\dfrac{1}{n'^2} - \dfrac{1}{n^2}$**（低能级 $n'$ 在前，高能级 $n$ 在后，这样结果才为正值）！另外 $R$ 的分母是 $ch^3$（三次方！），切记由 $E_n$ 除以 $hc$ 现场推出来，比死背靠谱一万倍。

#### 【最终答案】
- **(1) $r_n = \dfrac{h^2}{4\pi^2 k_0 m e^2} \cdot n^2$**
- **(2) $E_n = -\dfrac{2\pi^2 k_0^2 m e^4}{h^2} \cdot \dfrac{1}{n^2}$**
- **(3) $\dfrac{1}{\lambda} = R\left(\dfrac{1}{n'^2} - \dfrac{1}{n^2}\right)$，其中 $R = \dfrac{2\pi^2 k_0^2 m e^4}{c h^3}$**

---

## 4. 全局术语表同步说明

本切片新增的 **64 条** 日文物理核心术语与假名注音已整理写入切片术语表 [.glossary_008.md](file:///Users/baohan/Desktop/EJU/notes_物理/.glossary_008.md)，待主控流程合并去重至全局术语表 [glossary_all.md](file:///Users/baohan/Desktop/EJU/notes_物理/glossary_all.md)。
