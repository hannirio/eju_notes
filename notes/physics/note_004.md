# EJU 物理全解讲义 — 切片 004（P.46–P.60）
> **对应教材章节**：物理基礎・第二章 熱とエネルギー（物質の三態、ボイル・シャルルの法則、理想気体の状態方程式、気体分子運動論、熱力学第一法則、気体のモル比熱、気体の状態変化、熱サイクル）＋ 物理基礎・第三章 波（波動・波の要素と基本式）  
> **适用对象**：需快速唤醒中国高中热学与机械波基础、并掌握纯日文板书与 EJU 考场规范表达的授课教师 / 考生

---

## 1. 本节前置：国内高中物理基础唤醒

本切片涵盖**热力学核心体系（热学全貌）**以及**机械波（波動）入门**。热力学在 EJU 物理中是“高性价比拿分大户”——模型固定、计算规整，只要打通「状态方程＋热力学第一定律＋ $p$-$V$ 图像」三板斧，几乎可以稳定满分。

### 1.1 物态变化与理想气体状态方程

1. **物质的三态与潜热（物質の三態と潜熱）**
   - **三态**：固体（固体）、液体（液体）、气体（気体）。
   - **潜热（潜熱）**：伴随状态变化（融解、沸腾/蒸发等）吸收或放出的热量，如**融解热（融解熱）**、**蒸发热（蒸発熱）**。
   - **核心规律**：在状态变化（如冰水共存、沸腾）期间，**温度保持恒定**，吸收的热量全部用于破坏分子间作用力（增加分子势能），而非升高温度。

2. **气体实验定律与理想气体状态方程**
   - **压强与大气压**：$p = \dfrac{F}{S}\text{ [Pa = N/m}^2\text{]}$；标准大气压 $1\text{ atm} = 1.013 \times 10^5\text{ Pa}$。
   - **绝对温度（絶対温度）**：$T\text{ [K]} = t\text{ [}^\circ\text{C]} + 273$。
   - **玻意耳定律（ボイルの法則，等温）**：$p_1 V_1 = p_2 V_2$（$n, T$ 一定）。
   - **查理定律（シャルルの法則，等压）**：$\dfrac{V_1}{T_1} = \dfrac{V_2}{T_2}$（$n, p$ 一定）。
   - **玻意耳-查理定律（ボイル・シャルルの法則）**：$\dfrac{p_1 V_1}{T_1} = \dfrac{p_2 V_2}{T_2}$（$n$ 一定）。
   - **阿伏伽德罗定律（アボガドロの法則）**：同温同压下，气体体积 $V$ 与物质的量 $n$ 成正比。$1\text{ mol}$ 含 $N_A = 6.02 \times 10^{23}$ 个粒子，标准状态（$0^\circ\text{C},\ 1.013 \times 10^5\text{ Pa}$）下体积为 $22.4\text{ L} = 22.4 \times 10^{-3}\text{ m}^3$。
   - **理想气体状态方程（理想気体の状態方程式）**：
     $$pV = nRT \qquad \left(R = 8.31\text{ J/(mol}\cdot\text{K)}\right)$$
   - **密度变形公式（热气球/开口容器必杀技）**：设气体质量为 $m$、摩尔质量为 $M$、密度 $\rho = \dfrac{m}{V}$，由 $pV = \dfrac{m}{M}RT$ 可得：
     $$\frac{p}{\rho T} = \frac{R}{M} = \text{一定}$$
     即使气体质量/物质的量 $n$ 发生变化（如热气球开口漏气），只要是**同种气体**，$\dfrac{p}{\rho T}$ 恒为定值！

### 1.2 气体分子运动论（気体分子運動論）

将宏观压强 $p$、温度 $T$ 与微观分子质量 $m$、速度 $v$ 联系起来的经典推导链（边长 $L$ 立方体容器内 $N$ 个分子）：
1. **单次碰撞冲量**：分子以 $v_x$ 垂直弹性撞击壁面 $S$，壁面所受冲量大小 $I = 2mv_x$。
2. **时间 $t$ 内碰撞次数**：往返距离 $2L$ 撞一次，次数为 $\dfrac{v_x t}{2L}$。
3. **单个分子平均作用力**：$\bar{f} = \dfrac{2mv_x \cdot \frac{v_x t}{2L}}{t} = \dfrac{mv_x^2}{L}$。
4. **$N$ 个分子总力与压强**（由运动各向同性 $\overline{v_x^2} = \overline{v_y^2} = \overline{v_z^2} = \dfrac{1}{3}\overline{v^2}$ 及 $V = L^3$）：
   $$F = \frac{Nm\overline{v^2}}{3L}, \qquad p = \frac{F}{L^2} = \frac{Nm\overline{v^2}}{3V} \implies pV = \frac{1}{3}Nm\overline{v^2}$$
5. **分子平均平动动能与方均根速率**：对比 $pV = nRT$（且 $n = \dfrac{N}{N_A}$）：
   $$\frac{1}{2}m\overline{v^2} = \frac{3}{2}\frac{R}{N_A}T = \frac{3}{2}k_B T, \qquad \sqrt{\overline{v^2}} = \sqrt{\frac{3RT}{m N_A}} = \sqrt{\frac{3RT}{M \times 10^{-3}}}$$
   （其中 $k_B = \dfrac{R}{N_A}$ 为玻尔兹曼常数，$M\text{ [g/mol]}$ 为分子量/摩尔质量，换算为 $\text{kg/mol}$ 需乘 $10^{-3}$）。

### 1.3 热力学第一定律、摩尔比热与四大状态变化

1. **理想气体内能（内部エネルギー）**
   - 理想气体忽略分子势能，内能仅由物质的量 $n$ 和绝对温度 $T$ 决定（与变化过程无关）：
     - **单原子分子理想气体（単原子分子理想気体）**：$U = \dfrac{3}{2}nRT = \dfrac{3}{2}pV$
     - **双原子分子理想气体（二原子分子理想気体）**：$U = \dfrac{5}{2}nRT = \dfrac{5}{2}pV$
   - **普适内能变化公式**：无论何种过程，恒有 $\Delta U = n C_v \Delta T$。

2. **气体对外做功与热力学第一定律**
   - **气体对外做功（気体が外部にする仕事 $W_{\text{out}}$）**：数值等于 $p$-$V$ 图像下方面积；膨胀时 $W_{\text{out}} > 0$，压缩时 $W_{\text{out}} < 0$；定压变化时 $W_{\text{out}} = p\Delta V$。
   - **热力学第一定律（日本标准写法）**：
     $$Q_{\text{in}} = \Delta U + W_{\text{out}}$$
     （吸收的热量 $=$ 内能增加量 $+$ 对外做的功）。

3. **摩尔比热与迈耶关系（モル比熱とマイヤーの関係）**
   - **定容摩尔比热（定積モル比熱 $C_v$）**：定容升温 $1\text{ K}$ 所需热量，$Q = n C_v \Delta T$（单原子分子 $C_v = \dfrac{3}{2}R$）。
   - **定压摩尔比热（定圧モル比熱 $C_p$）**：定压升温 $1\text{ K}$ 所需热量，$Q = n C_p \Delta T$（单原子分子 $C_p = \dfrac{5}{2}R$）。
   - **迈耶公式（マイヤーの関係）**：由定压过程 $n C_p \Delta T = n C_v \Delta T + nR\Delta T$ 直接得出：
     $$C_p = C_v + R$$
   - **比热比（比熱比）**：$\gamma = \dfrac{C_p}{C_v}$（单原子分子 $\gamma = \dfrac{5}{3}$）。

4. **四大经典状态变化速查表**

| 状态变化 | 特征条件 | 气体定律 | 做功 $W_{\text{out}}$ | 内能变化 $\Delta U$ | 热力学第一定律 $Q_{\text{in}}$ |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **定圧変化（等压）** | $p = \text{const}$ | $\dfrac{V}{T} = \text{const}$ | $p\Delta V = nR\Delta T$ | $nC_v\Delta T$ | $Q_{\text{in}} = \Delta U + p\Delta V = nC_p\Delta T$ |
| **定積変化（等容）** | $V = \text{const}$ | $\dfrac{p}{T} = \text{const}$ | $0$ | $nC_v\Delta T$ | $Q_{\text{in}} = \Delta U = nC_v\Delta T$ |
| **等温変化（等温）** | $T = \text{const}$ | $pV = \text{const}$ | $p$-$V$ 曲线下面积 | $0$ | $Q_{\text{in}} = W_{\text{out}}$ |
| **断熱変化（绝热）** | $Q_{\text{in}} = 0$ | **泊松定律** $pV^\gamma = \text{const}$ | $-\Delta U$ | $nC_v\Delta T$ | $0 = \Delta U + W_{\text{out}}$ |

5. **热机与热效率（熱機関と熱効率）**
   - 一个完整循环（熱サイクル）后回到初态，总内能变化 $\Delta U_{\text{all}} = 0$，故净功 $W_{\text{正味}} = W_{\text{all}} = Q_{\text{in}} - Q_{\text{out}}$（$p$-$V$ 闭合环面积）。
   - **热效率（熱効率 $e$）**：
     $$e = \frac{W_{\text{正味}}}{Q_{\text{in}}} = \frac{Q_{\text{in}} - Q_{\text{out}}}{Q_{\text{in}}} = 1 - \frac{Q_{\text{out}}}{Q_{\text{in}}} \quad (< 1)$$
     **铁律**：分母 $Q_{\text{in}}$ **只加吸收热量的过程**（$Q > 0$ 的段），绝对不能把放热段（$Q < 0$）也加进分母！

### 1.4 机械波初步（波動の基礎）

- **波长（波長 $\lambda\text{ [m]}$）**：相邻两个波峰（山）或波谷（谷）之间、即一个完整波形的长度。
- **振幅（振幅 $A\text{ [m]}$）**：平衡位置到波峰（或波谷）的最大位移高度（**注意不是波峰到波谷的全高**！）。
- **频率 / 振动数（振動数 $f\text{ [Hz = 1/s]}$）**：媒质 $1$ 秒内完成全振动的次数。
- **周期（周期 $T\text{ [s]}$）**：完成 $1$ 次全振动所需时间，与频率互为倒数：$f = \dfrac{1}{T}$。
- **波速基本式（波の基本式）**：
  $$v = f\lambda = \frac{\lambda}{T}$$

### 1.5 中日物理体系与习惯差异提醒

| 对比维度 | 中国国内高中物理习惯 | 日本 EJU / 高中物理习惯（授课必强调） |
| :--- | :--- | :--- |
| **热力学第一定律符号约定** | $\Delta U = Q + W$（$W$ 为**外界对气体**做的功） | 教材主流写为 **$Q_{\text{in}} = \Delta U + W_{\text{out}}$**（$W_{\text{out}}$ 为**气体对外界**做的功，膨胀为正），务必看清题干定义是「気体が外部にした仕事」还是「気体がされた仕事」！ |
| **查理定律 vs 盖-吕萨克定律** | 查理定律指**等容**（$p/T = \text{const}$），盖-吕萨克定律指**等压**（$V/T = \text{const}$） | 日本教材统称等压变化 $\dfrac{V}{T} = \text{const}$ 为 **シャルルの法則（查理定律）**，等容变化直接叫 **定積変化**，几乎不提盖-吕萨克之名！ |
| **等容变化术语** | 称作“等容变化” | 日本一律称作 **定積変化（ていせきへんか）**，定容摩尔热容称作 **定積モル比熱 $C_v$**。 |
| **单/双原子分子热容与泊松定律** | 国内高考一般不考 $C_p, C_v$、迈耶公式与 $pV^\gamma = \text{const}$ | EJU 热学**高频必考**！必须牢记单原子 $C_v = \frac{3}{2}R,\ C_p = \frac{5}{2}R,\ \gamma = \frac{5}{3}$ 及迈耶关系 $C_p = C_v + R$。 |
| **分子量 $M$ 的单位陷阱** | 化学常用 $\text{g/mol}$，物理推导常直接给 $\text{kg/mol}$ | 日本物理题若写「分子量 $M\text{ [g]}$」，代入 SI 单位制公式（如方均根速率）时**必须乘 $10^{-3}$** 化为 $\text{kg/mol}$！ |
| **频率的叫法** | 统一称作“频率 $f$” | 机械波中日本主要称 **振動数（しんどうすう）**，交流电与电磁波中常用 **周波数（しゅうはすう）**，符号均为 $f$。 |

---

## 2. 日文物理核心词汇与公式假名注音（板书必备）

### 2.1 核心物理词汇表

#### 物态变化与气体定律
- **熱とエネルギー（ねつとえねるぎー / netsu to enerugī）** — 热与能量
- **物質の三態（ぶっしつのさんたい / busshitsu no santai）** — 物质的三态
- **固体（こたい / kotai）** — 固体
- **液体（えきたい / ekitai）** — 液体
- **気体（きたい / kitai）** — 气体
- **潜熱（せんねつ / sennetsu）** — 潜热
- **状態変化（じょうたいへんか / jōtai henka）** — 状态变化（物态变化 / 气体状态变化）
- **融解熱（ゆうかいねつ / yūkainetsu）** — 融解热
- **蒸発熱（じょうはつねつ / jōhatsunetsu）** — 蒸发热
- **融点（ゆうてん / yūten）** — 熔点
- **沸点（ふってん / futten）** — 沸点
- **融解（ゆうかい / yūkai）** — 熔化 / 融解
- **沸騰（ふっとう / futtō）** — 沸腾
- **ボイルの法則（ぼいるのほうそく / boiru no hōsoku）** — 玻意耳定律
- **シャルルの法則（しゃるるのほうそく / sharuru no hōsoku）** — 查理定律（日本指等压变化 $V/T = \text{const}$）
- **ボイル・シャルルの法則（ぼいる・しゃるるのほうそく / boiru sharuru no hōsoku）** — 玻意耳-查理定律（理想气体综合实验定律）
- **絶対温度（ぜったいおんど / zettai ondo）** — 绝对温度（热力学温度 $T$）

#### 理想气体与分子运动论
- **理想気体（りそうきたい / risō kitai）** — 理想气体
- **理想気体の状態方程式（りそうきたいのじょうたいほうていしき / risō kitai no jōtai hōteishiki）** — 理想气体状态方程
- **物質量（ぶっしつりょう / busshitsuryō）** — 物质的量（$n\text{ [mol]}$）
- **アボガドロの法則（あぼがどろのほうそく / abogadoro no hōsoku）** — 阿伏伽德罗定律
- **アボガドロ定数（あぼがどろていすう / abogadoro teisū）** — 阿伏伽德罗常数（$N_A$）
- **気体定数（きたいていすう / kitai teisū）** — 气体常数（$R$）
- **標準状態（ひょうじゅんじょうたい / hyōjun jōtai）** — 标准状态
- **モル質量（もるしつりょう / moru shitsuryō）** — 摩尔质量
- **分子量（ぶんしりょう / bunshiryō）** — 分子量
- **熱気球（ねつききゅう / netsukikyū）** — 热气球
- **気体分子運動論（きたいぶんしうんどうろん / kitai bunshi undōron）** — 气体分子运动论
- **完全弾性衝突（かんぜんだんせいしょうとつ / kanzen dansei shōtotsu）** — 完全弹性碰撞
- **力積（りきせき / rikiseki）** — 冲量
- **運動の等方性（うんどうのとうほうせい / undō no tōhōsei）** — 运动的各向同性
- **2乗平均速度（にじょうへいきんそくど / nijō heikin sokudo）** — 方均根速率（$\sqrt{\overline{v^2}}$）

#### 热力学第一定律、摩尔比热与热机循环
- **内部エネルギー（ないぶえねるぎー / naibu enerugī）** — 内能（$U$）
- **単原子分子理想気体（たんげんしぶんしりそうきたい / tangenshi bunshi risō kitai）** — 单原子分子理想气体
- **二原子分子理想気体（にげんしぶんしりそうきたい / nigenshi bunshi risō kitai）** — 双原子分子理想气体
- **膨張（ぼうちょう / bōchō）** — 膨胀
- **圧縮（あっしゅく / asshuku）** — 压缩
- **熱力学第一法則（ねつりきがくだいいちほうそく / netsurikigaku dai-ichi hōsoku）** — 热力学第一定律
- **定積モル比熱（ていせきもるひねつ / teiseki moru hinetsu）** — 定容摩尔比热（$C_v$）
- **定圧モル比熱（ていあつもるひねつ / teiatsu moru hinetsu）** — 定压摩尔比热（$C_p$）
- **マイヤーの関係（まいやーのかんけい / maiyā no kankei）** — 迈耶关系（$C_p = C_v + R$）
- **比熱比（ひねつひ / hinetsuhi）** — 比热比（$\gamma = C_p / C_v$）
- **定圧変化（ていあつへんか / teiatsu henka）** — 等压变化
- **定積変化（ていせきへんか / teiseki henka）** — 等容变化
- **等温変化（とうおんへんか / tōon henka）** — 等温变化
- **断熱変化（だんねつへんか / dannetsu henka）** — 绝热变化
- **ポアソンの法則（ぽあそんのほうそく / poason no hōsoku）** — 泊松定律（$pV^\gamma = \text{const}$）
- **熱機関（ねつきかん / netsukikan）** — 热机
- **熱効率（ねつこうりつ / netsukōritsu）** — 热效率（$e$）
- **高温熱源（こうおんねつげん / kōon netsugen）** — 高温热源
- **低温熱源（ていおんねつげん / teion netsugen）** — 低温热源
- **正味の仕事（しょうみのしごと / shōmi no shigoto）** — 净功
- **熱サイクル（ねつさいくる / netsu saikuru）** — 热力学循环

#### 波动基础
- **波動（はどう / hadō）** — 波动
- **波長（はちょう / hachō）** — 波长（$\lambda$）
- **振幅（しんぷく / shinpuku）** — 振幅（$A$）
- **媒質（ばいしつ / baishitsu）** — 媒质 / 介质
- **振動数（しんどうすう / shindōsū）** — 频率 / 振动数（$f$）
- **周波数（しゅうはすう / shūhasū）** — 频率（周波数）
- **ヘルツ（へるつ / herutsu）** — 赫兹（$\text{Hz}$）
- **周期（しゅうき / shūki）** — 周期（$T$）
- **山（やま / yama）** — 波峰
- **谷（たに / tani）** — 波谷

### 2.2 核心公式课堂口语读法（板书念法）

| 公式 | 日本课堂标准板书口语读法 |
| :--- | :--- |
| $pV = nRT$ | 「ピーブイ・イコール、エヌ・アール・ティー」 |
| $\dfrac{p_1 V_1}{T_1} = \dfrac{p_2 V_2}{T_2}$ | 「ティーいちぶんのピーいちブイいち、イコール、ティーにぶんのピーにブイに」 |
| $pV = \dfrac{1}{3}Nm\overline{v^2}$ | 「ピーブイ・イコール、さんぶんのいち・エヌ・エム・ブイにじょうバー」 |
| $\dfrac{1}{2}m\overline{v^2} = \dfrac{3}{2}\dfrac{R}{N_A}T$ | 「にぶんのいち・エム・ブイにじょうバー、イコール、にぶんのさん・エヌエーぶんのアール・ティー」 |
| $Q_{\text{in}} = \Delta U + W_{\text{out}}$ | 「キューイン・イコール、デルタユー、たす、ダブリューアウト」 |
| $\Delta U = nC_v\Delta T$ | 「デルタユー・イコール、エヌ・シーブイ・デルタティー」 |
| $C_p = C_v + R$ | 「シーピー・イコール、シーブイ、たす、アール」 |
| $pV^\gamma = \text{一定}$ | 「ピーブイのガンマじょう・イコール、いってい」 |
| $e = \dfrac{W_{\text{正味}}}{Q_{\text{in}}} = 1 - \dfrac{Q_{\text{out}}}{Q_{\text{in}}}$ | 「イー・イコール、キューインぶんのダブリューしょうみ、イコール、いち・ひく、キューインぶんのキューアウト」 |
| $v = f\lambda$ | 「ブイ・イコール、エフ・ラムダ」 |

---

## 3. 逐题深度解析（一题一解，不可跳步）

---

### 例題 1（教材 P.49 / 页码 48）：熱気球の原理（热气球原理）

#### 【原题重现与翻译】
> **日文原题**：  
> 一般に，圧力 $p$，体積 $V$，質量 $m$，モル質量 $M$，気体定数 $R$，絶対温度 $T$ を用いると理想気体の状態方程式は $pV = \fbox{(1)}$ と表される。ここで，気体の密度を $\rho$ とすると $\rho = \fbox{(2)}$ であるから，状態方程式は $p, \rho, M, R, T$ を用いて $\dfrac{p}{\rho T} = \fbox{(3)}$ と表される。同一気体であれば，物質量が変化したとしても $\fbox{(3)}$ は一定である。  
> 熱気球があり，風船部分の体積は常に $V$，風船内の空気の質量を除いた気球の質量は $M$ である。地表付近の気圧を $p_0$，空気の密度を $\rho_0$，絶対温度を $T_0$ とする。  
> (4) 気球が上昇し始めるときの温度 $T_1$ を求めよ。また，密度 $\rho_0 = 1.20\text{ kg/m}^3$，体積 $V = 1000\text{ m}^3$，質量 $M = 200\text{ kg}$，絶対温度 $T_0 = 300\text{ K}$ のときの $T_1$ の値を求めよ。  
> (5) 気球がある高度に達したとき，温度を $T_2\ (> T_1)$ に保って静止させた。このとき，気球外部の気圧は $p_2$ であった。気球外部の空気の密度 $\rho_2$ を求めよ。
>
> **中文翻译**：  
> 一般地，用压强 $p$、体积 $V$、质量 $m$、摩尔质量 $M$、气体常数 $R$、绝对温度 $T$ 可将理想气体状态方程表示为 $pV = \fbox{(1)}$。此处，设气体密度为 $\rho$，则 $\rho = \fbox{(2)}$，因此状态方程可用 $p, \rho, M, R, T$ 表示为 $\dfrac{p}{\rho T} = \fbox{(3)}$。只要是同种气体，即使物质的量发生变化，$\fbox{(3)}$ 也是恒定的。  
> 有一热气球，气囊部分体积恒为 $V$，除去气囊内空气质量后的气球自身质量为 $M$。设地表附近的气压为 $p_0$、空气密度为 $\rho_0$、绝对温度为 $T_0$。  
> (4) 求气球刚开始上升时气囊内空气的温度 $T_1$。并求当 $\rho_0 = 1.20\text{ kg/m}^3$、$V = 1000\text{ m}^3$、$M = 200\text{ kg}$、$T_0 = 300\text{ K}$ 时 $T_1$ 的数值。  
> (5) 当气球到达某一高度时，将内部温度保持在 $T_2\ (> T_1)$ 并使其静止。此时气球外部的气压为 $p_2$，求气球外部空气的密度 $\rho_2$。

#### 【考点与模型定位】
**开口热气球模型（理想气体状态方程密度形式 $\dfrac{p}{\rho T} = \text{const}$ ＋ 浮力平衡）**。核心突破点在于热气球底部开口，因此**内部气压恒等于外部气压**，但加热时内部空气会逸出（$n$ 不守恒），必须改用密度关系 $\dfrac{p}{\rho T} = \text{const}$ 求解！

#### 【多色矢量图解（SVG）】

<svg viewBox="0 0 420 260" width="420" height="260" xmlns="http://www.w3.org/2000/svg" style="background:#fafafa;border:1px solid #e5e7eb;border-radius:8px;">
  <defs>
    <marker id="arr-blue-004-1" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0,0 L0,6 L7,3 z" fill="#2563eb"/></marker>
    <marker id="arr-green-004-1" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0,0 L0,6 L7,3 z" fill="#16a34a"/></marker>
  </defs>
  <!-- 分隔线 -->
  <line x1="210" y1="15" x2="210" y2="245" stroke="#d1d5db" stroke-dasharray="4,4"/>

  <!-- 左图：(4) 地表刚起飞 -->
  <text x="20" y="24" font-size="11" font-weight="bold" fill="#374151">(4) 地表上昇開始時</text>
  <!-- 气球外廓 -->
  <circle cx="95" cy="115" r="36" fill="#fef3c7" stroke="#b45309" stroke-width="1.6"/>
  <line x1="72" y1="143" x2="83" y2="175" stroke="#4b5563" stroke-width="1.2"/>
  <line x1="118" y1="143" x2="107" y2="175" stroke="#4b5563" stroke-width="1.2"/>
  <rect x="83" y="175" width="24" height="16" fill="#e5e7eb" stroke="#374151" stroke-width="1.4"/>
  <!-- 内部状态标注 -->
  <text x="68" y="118" font-size="10" fill="#92400e">p₀, ρ₁, T₁</text>
  <!-- 外部状态标注 -->
  <text x="138" y="112" font-size="10" fill="#374151">外部:</text>
  <text x="138" y="126" font-size="10" fill="#374151">p₀, ρ₀, T₀</text>
  <!-- 浮力（绿） -->
  <line x1="72" y1="86" x2="72" y2="38" stroke="#16a34a" stroke-width="2.2" marker-end="url(#arr-green-004-1)"/>
  <text x="78" y="48" font-size="11" font-weight="bold" fill="#16a34a">浮力 ρ₀Vg</text>
  <!-- 内部空气重力（蓝） -->
  <line x1="95" y1="125" x2="95" y2="168" stroke="#2563eb" stroke-width="2" marker-end="url(#arr-blue-004-1)"/>
  <text x="101" y="164" font-size="10" fill="#2563eb">ρ₁Vg</text>
  <!-- 气球自身重力（蓝） -->
  <line x1="95" y1="191" x2="95" y2="232" stroke="#2563eb" stroke-width="2" marker-end="url(#arr-blue-004-1)"/>
  <text x="102" y="228" font-size="10" fill="#2563eb">Mg</text>
  <line x1="40" y1="242" x2="170" y2="242" stroke="#6b7280" stroke-width="1.5"/>

  <!-- 右图：(5) 高空静止 -->
  <text x="228" y="24" font-size="11" font-weight="bold" fill="#374151">(5) 高空静止時 (T₂ &gt; T₁)</text>
  <circle cx="300" cy="115" r="36" fill="#ffedd5" stroke="#c2410c" stroke-width="1.6"/>
  <line x1="277" y1="143" x2="288" y2="175" stroke="#4b5563" stroke-width="1.2"/>
  <line x1="323" y1="143" x2="312" y2="175" stroke="#4b5563" stroke-width="1.2"/>
  <rect x="288" y="175" width="24" height="16" fill="#e5e7eb" stroke="#374151" stroke-width="1.4"/>
  <text x="275" y="118" font-size="10" fill="#9a3412">p₂, ρ', T₂</text>
  <text x="345" y="112" font-size="10" fill="#374151">外部:</text>
  <text x="345" y="126" font-size="10" fill="#374151">p₂, ρ₂</text>
  <!-- 浮力（绿） -->
  <line x1="277" y1="86" x2="277" y2="38" stroke="#16a34a" stroke-width="2.2" marker-end="url(#arr-green-004-1)"/>
  <text x="283" y="48" font-size="11" font-weight="bold" fill="#16a34a">浮力 ρ₂Vg</text>
  <!-- 内部空气重力（蓝） -->
  <line x1="300" y1="125" x2="300" y2="168" stroke="#2563eb" stroke-width="2" marker-end="url(#arr-blue-004-1)"/>
  <text x="306" y="164" font-size="10" fill="#2563eb">ρ'Vg</text>
  <!-- 气球自身重力（蓝） -->
  <line x1="300" y1="191" x2="300" y2="232" stroke="#2563eb" stroke-width="2" marker-end="url(#arr-blue-004-1)"/>
  <text x="307" y="228" font-size="10" fill="#2563eb">Mg</text>
  <!-- 图例 -->
  <text x="340" y="220" font-size="9.5" fill="#16a34a">■ 绿：浮力</text>
  <text x="340" y="234" font-size="9.5" fill="#2563eb">■ 蓝：重力</text>
</svg>

#### 【日本考场规范分步解答】

**(1)** 物質量 $n$ は質量 $m$ とモル質量 $M$ を用いて $n = \dfrac{m}{M}$ と表される。したがって，理想気体の状態方程式 $pV = nRT$ より，
$$pV = \frac{m}{M}RT$$

**(2)** 密度 $\rho$ は単位体積当たりの質量であるから，
$$\rho = \frac{m}{V}$$

**(3)** (1) の両辺を $V$ で割ると $p = \dfrac{m}{V}\dfrac{RT}{M} = \rho\dfrac{RT}{M}$ となる。よって，
$$\frac{p}{\rho T} = \frac{R}{M}$$

> 💡 讲师批注：提醒学生注意教材中一个小细节——第 (1)–(3) 问的 $M$ 指空气的**摩尔质量**，而第 (4)–(5) 问重新定义了 $M$ 为**气球自身质量**，前后符号复用，做题时切勿混淆。另外，$\dfrac{p}{\rho T} = \text{一定}$ 是处理一切“开口容器 / 漏气 / 热气球”问题的黄金方程。

**(4)** 気球が上昇し始めるときの風船内の空気の密度を $\rho_1$ とする。風船の下部は開いているため，内部の気圧は外部の気圧 $p_0$ と等しい。  
(3) の関係 $\dfrac{p}{\rho T} = \text{一定}$ より，$\dfrac{p_0}{\rho_0 T_0} = \dfrac{p_0}{\rho_1 T_1}$ となるから，
$$\rho_0 T_0 = \rho_1 T_1 \implies \rho_1 = \frac{T_0}{T_1}\rho_0$$
気球が上昇し始める直前の力のつりあい（浮力 $=$ 内部の空気の重力 $+$ 気球本体の重力）より，
$$\rho_0 V g = \rho_1 V g + M g$$
両辺を $g$ で割り，$\rho_1 = \dfrac{T_0}{T_1}\rho_0$ を代入して $T_1$ について解くと，
$$\rho_0 V = \frac{T_0}{T_1}\rho_0 V + M \implies \frac{T_0}{T_1}\rho_0 V = \rho_0 V - M \implies T_1 = \frac{\rho_0 V}{\rho_0 V - M}T_0$$
与えられた数値を代入すると，
$$T_1 = \frac{1.20\text{ kg/m}^3 \times 1000\text{ m}^3}{1.20\text{ kg/m}^3 \times 1000\text{ m}^3 - 200\text{ kg}} \times 300\text{ K} = \frac{1200}{1000} \times 300 = 360\text{ [K]}$$

> 💡 讲师批注：浮力公式 $\rho_{\text{外}} V g$ 中的密度必须是**气球外部的空气密度 $\rho_0$**，而内部空气重力用的是**内部热空气密度 $\rho_1$**，这是最常见的代错陷阱！

**(5)** 温度を $T_2$ にしたときの気球内部の空気の密度を $\rho'$ とする。内部の気圧は外部の気圧 $p_2$ と等しいから，地表付近の外部の空気 $(p_0, \rho_0, T_0)$ と気球内部の空気 $(p_2, \rho', T_2)$ に対して (3) の関係を用いると，
$$\frac{p_0}{\rho_0 T_0} = \frac{p_2}{\rho' T_2} \implies \rho' = \frac{p_2 T_0}{p_0 T_2}\rho_0$$
高空での力のつりあいより，
$$\rho_2 V g = \rho' V g + M g$$
両辺を $Vg$ で割り，$\rho'$ を代入すると，
$$\rho_2 = \rho' + \frac{M}{V} = \frac{p_2 T_0}{p_0 T_2}\rho_0 + \frac{M}{V}$$

> 💡 讲师批注：第 (5) 问非常巧妙！题目**没有给出高空外部的温度**，所以千万别把高空外部空气拿去套 $\frac{p}{\rho T} = \text{const}$！正确路线是：先用地表空气 $(p_0, \rho_0, T_0)$ 和高空**内部**空气 $(p_2, \rho', T_2)$ 求出 $\rho'$，再通过浮力平衡反推出高空外部密度 $\rho_2$。

#### 【最终答案】
- **(1) $\dfrac{m}{M}RT$**
- **(2) $\dfrac{m}{V}$**
- **(3) $\dfrac{R}{M}$**
- **(4) $T_1 = \dfrac{\rho_0 V}{\rho_0 V - M}T_0$，数値 $T_1 = 360\text{ K}$**
- **(5) $\rho_2 = \dfrac{p_2 T_0}{p_0 T_2}\rho_0 + \dfrac{M}{V}$**

---

### 例題 2（教材 P.50–51 / 页码 49–50）：気体分子運動論（气体分子运动论推导）

> **⚠️ 教材印刷勘误提示**：教材原稿中**页码 50（P.51）与页码 51（P.52）完全重复印刷**，内容一字不差，属排版重页；另外页码 50 解答 (4) 第一行漏印了 $v_x^2$ 上方的平均横线（应为 $\overline{v_x^2}$）。本讲义已作规范修正。

#### 【原题重现与翻译】
> **日文原题**：  
> 1 辺の長さ $L$ の立方体の容器内に質量 $m\text{ [kg]}$ の分子が $N$ 個入っている。図のように座標軸を取り，1 個の分子が速度 $\vec{v} = (v_x, v_y, v_z)$ で $x$ 軸に垂直な面 $S$ に完全弾性衝突したとする。分子 1 個の衝突で面 $S$ が受ける力積の大きさは $\fbox{(1)}$ である。この分子は時間 $t$ の間に $\fbox{(2)}$ 回だけ面 $S$ と衝突するから，面 $S$ がこの分子から受ける時間 $t$ の間の平均の力の大きさは $\bar{f} = \fbox{(3)}$ である。速度 $v$ の 2 乗の平均値を $\overline{v^2}$ とすると三平方の定理より $\overline{v^2} = \overline{v_x^2} + \overline{v_y^2} + \overline{v_z^2}$ であり，また運動の等方性より $\overline{v_x^2} = \overline{v_y^2} = \overline{v_z^2}$ である。よって，面 $S$ が $N$ 個の分子から受ける力の大きさ $F$ を $\overline{v^2}$ を用いて表すと $F = \fbox{(4)}$ であるから，立方体の体積を $V$ とすると面 $S$ が受ける圧力は $P = \fbox{(5)}$ である。これを理想気体の状態方程式と比較すると，アボガドロ定数 $N_A$ を用いて分子 1 個の平均の運動エネルギーが $\dfrac{1}{2}m\overline{v^2} = \fbox{(6)}$ と表せる。さらに，分子量 $M\text{ [g]}$ を用いると，分子の 2 乗平均速度を $\sqrt{\overline{v^2}} = \fbox{(7)}$ と表せる。
>
> **中文翻译**：  
> 边长为 $L$ 的立方体容器内装有 $N$ 个质量为 $m\text{ [kg]}$ 的分子。如图所示建立坐标轴，设 1 个分子以速度 $\vec{v} = (v_x, v_y, v_z)$ 与垂直于 $x$ 轴的壁面 $S$ 发生完全弹性碰撞。1 个分子单次碰撞时，壁面 $S$ 受到的冲量大小为 $\fbox{(1)}$。该分子在时间 $t$ 内与壁面 $S$ 碰撞 $\fbox{(2)}$ 次，因此壁面 $S$ 在时间 $t$ 内受到该分子的平均作用力大小为 $\bar{f} = \fbox{(3)}$。设速度 $v$ 平方的平均值为 $\overline{v^2}$，由勾股定理有 $\overline{v^2} = \overline{v_x^2} + \overline{v_y^2} + \overline{v_z^2}$，又由运动的各向同性有 $\overline{v_x^2} = \overline{v_y^2} = \overline{v_z^2}$。由此，面 $S$ 受到 $N$ 个分子的作用力大小 $F$ 用 $\overline{v^2}$ 表示为 $F = \fbox{(4)}$；设立方体体积为 $V$，则面 $S$ 所受压强为 $P = \fbox{(5)}$。将其与理想气体状态方程比较，用阿伏伽德罗常数 $N_A$ 可将单个分子的平均动能表示为 $\dfrac{1}{2}m\overline{v^2} = \fbox{(6)}$。进一步，用分子量 $M\text{ [g]}$ 可将分子的方均根速率表示为 $\sqrt{\overline{v^2}} = \fbox{(7)}$。

#### 【考点与模型定位】
**气体分子运动论完整 7 步推导**（EJU 及国公立大学校内考几乎年年出现的“填空大题”模板，从冲量 $\to$ 碰撞次数 $\to$ 平均力 $\to$ 总力 $\to$ 压强 $\to$ 平均动能 $\to$ 方均根速率，一步不能跳）。

#### 【多色矢量图解（SVG）】

<svg viewBox="0 0 420 260" width="420" height="260" xmlns="http://www.w3.org/2000/svg" style="background:#fafafa;border:1px solid #e5e7eb;border-radius:8px;">
  <defs>
    <marker id="arr-blk-004-2" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0,0 L0,6 L7,3 z" fill="#111827"/></marker>
    <marker id="arr-red-004-2" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0,0 L0,6 L7,3 z" fill="#dc2626"/></marker>
    <marker id="arr-green-004-2" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0,0 L0,6 L7,3 z" fill="#16a34a"/></marker>
  </defs>
  <!-- 左侧：立方体容器 -->
  <text x="20" y="22" font-size="11" font-weight="bold" fill="#374151">立方体容器 (1辺 L, V = L³)</text>
  <!-- 后面正方形 -->
  <rect x="65" y="65" width="90" height="90" fill="none" stroke="#9ca3af" stroke-width="1.2" stroke-dasharray="4,3"/>
  <!-- 前面正方形 -->
  <rect x="35" y="95" width="90" height="90" fill="none" stroke="#374151" stroke-width="1.6"/>
  <!-- 棱线 -->
  <line x1="35" y1="95" x2="65" y2="65" stroke="#374151" stroke-width="1.5"/>
  <line x1="125" y1="95" x2="155" y2="65" stroke="#374151" stroke-width="1.5"/>
  <line x1="125" y1="185" x2="155" y2="155" stroke="#374151" stroke-width="1.5"/>
  <line x1="35" y1="185" x2="65" y2="155" stroke="#9ca3af" stroke-width="1.2" stroke-dasharray="4,3"/>
  <!-- 面 S 高亮 -->
  <polygon points="125,95 155,65 155,155 125,185" fill="#dbeafe" fill-opacity="0.6" stroke="#2563eb" stroke-width="1.8"/>
  <text x="134" y="132" font-size="12" font-weight="bold" fill="#1e40af">S</text>
  <!-- 坐标轴 -->
  <line x1="65" y1="155" x2="188" y2="155" stroke="#111827" stroke-width="1.4" marker-end="url(#arr-blk-004-2)"/>
  <text x="192" y="159" font-size="11" font-style="italic" fill="#111827">x</text>
  <line x1="65" y1="155" x2="65" y2="38" stroke="#111827" stroke-width="1.4" marker-end="url(#arr-blk-004-2)"/>
  <text x="53" y="42" font-size="11" font-style="italic" fill="#111827">z</text>
  <line x1="65" y1="155" x2="18" y2="202" stroke="#111827" stroke-width="1.4" marker-end="url(#arr-blk-004-2)"/>
  <text x="10" y="212" font-size="11" font-style="italic" fill="#111827">y</text>
  <!-- 分子 -->
  <circle cx="92" cy="122" r="5" fill="#374151"/>
  <line x1="97" y1="122" x2="122" y2="112" stroke="#111827" stroke-width="1.5" stroke-dasharray="4,2" marker-end="url(#arr-blk-004-2)"/>
  <text x="98" y="108" font-size="10" fill="#111827">v</text>
  <text x="72" y="200" font-size="10" fill="#374151">L</text>

  <!-- 分隔线 -->
  <line x1="215" y1="15" x2="215" y2="245" stroke="#d1d5db" stroke-dasharray="4,4"/>

  <!-- 右侧：面 S 弹性碰撞放大图 -->
  <text x="235" y="22" font-size="11" font-weight="bold" fill="#374151">面 S での完全弾性衝突</text>
  <!-- 壁面 S -->
  <line x1="345" y1="50" x2="345" y2="215" stroke="#1e40af" stroke-width="3"/>
  <text x="335" y="232" font-size="11" font-weight="bold" fill="#1e40af">面 S</text>
  <!-- 入射分子 -->
  <circle cx="255" cy="85" r="11" fill="#e5e7eb" stroke="#111827" stroke-width="1.5"/>
  <text x="250" y="89" font-size="11" font-style="italic" fill="#111827">m</text>
  <line x1="266" y1="85" x2="315" y2="85" stroke="#111827" stroke-width="1.8" stroke-dasharray="5,3" marker-end="url(#arr-blk-004-2)"/>
  <text x="280" y="76" font-size="11" fill="#111827">+v_x</text>
  <!-- 碰撞路径 -->
  <path d="M 315 85 Q 345 85 345 125 Q 345 165 315 165" fill="none" stroke="#9ca3af" stroke-width="1.4" stroke-dasharray="3,3"/>
  <!-- 反弹分子 -->
  <circle cx="255" cy="165" r="11" fill="#e5e7eb" stroke="#111827" stroke-width="1.5"/>
  <text x="250" y="169" font-size="11" font-style="italic" fill="#111827">m</text>
  <line x1="315" y1="165" x2="270" y2="165" stroke="#111827" stroke-width="1.8" stroke-dasharray="5,3" marker-end="url(#arr-blk-004-2)"/>
  <text x="280" y="182" font-size="11" fill="#111827">-v_x</text>
  <!-- 冲量箭头（作用力与反作用力） -->
  <line x1="345" y1="125" x2="300" y2="125" stroke="#16a34a" stroke-width="2.4" marker-end="url(#arr-green-004-2)"/>
  <text x="235" y="129" font-size="10" fill="#16a34a">分子が受ける -2mv_x</text>
  <line x1="345" y1="125" x2="395" y2="125" stroke="#dc2626" stroke-width="2.4" marker-end="url(#arr-red-004-2)"/>
  <text x="352" y="114" font-size="10" font-weight="bold" fill="#dc2626">面Sが受ける</text>
  <text x="360" y="142" font-size="10.5" font-weight="bold" fill="#dc2626">I = 2mv_x</text>
</svg>

#### 【日本考场规范分步解答】

**(1)** 力積と運動量の関係より，図の右向き（$+x$ 方向）を正とすると，1 回の完全弾性衝突で分子が面 $S$ から受ける力積 $I$ は，
$$I = (-mv_x) - mv_x = -2mv_x$$
作用・反作用の法則より，面 $S$ が分子から受ける力積の大きさは **$2mv_x$** である。

> 💡 讲师批注：完全弹性碰撞壁面时，$y, z$ 方向速度分量不变，只有 $x$ 方向速度从 $+v_x$ 反转为 $-v_x$，因此动量变化量大小为 $2mv_x$（千万不要漏掉系数 $2$！）。

**(2)** 分子は時間 $t$ の間に $x$ 軸方向へ合計距離 $v_x t$ だけ進み，往復距離 $2L$ を進むごとに面 $S$ と 1 回衝突するから，時間 $t$ 内の衝突回数は，
$$\frac{v_x t}{2L}$$

> 💡 讲师批注：为什么是除以 $2L$ 而不是 $L$？因为分子撞完右壁 $S$ 后，必须先飞到左壁反弹回来，走完一个来回 $2L$ 才能再次撞击右壁 $S$。

**(3)** 面 $S$ が時間 $t$ の間に分子 1 個から受ける力積の合計は，
$$2mv_x \times \frac{v_x t}{2L} = \frac{mv_x^2}{L}t$$
平均の力を $\bar{f}$ とすると $\bar{f} t = \dfrac{mv_x^2}{L}t$ より，
$$\bar{f} = \frac{mv_x^2}{L}$$

**(4)** $N$ 個の分子全体から受ける平均の力の大きさ $F$ は，各分子の $v_x^2$ の平均値 $\overline{v_x^2}$ を用いて，
$$F = N \cdot \frac{m\overline{v_x^2}}{L}$$
ここで $\overline{v^2} = \overline{v_x^2} + \overline{v_y^2} + \overline{v_z^2}$ および運動の等方性 $\overline{v_x^2} = \overline{v_y^2} = \overline{v_z^2}$ より，$\overline{v_x^2} = \dfrac{1}{3}\overline{v^2}$ であるから，
$$F = \frac{Nm\overline{v^2}}{3L}$$

**(5)** 面 $S$ の面積は $L^2$，立方体の体積は $V = L^3$ であるから，面 $S$ が受ける圧力 $P$ は，
$$P = \frac{F}{L^2} = \frac{\dfrac{Nm\overline{v^2}}{3L}}{L^2} = \frac{Nm\overline{v^2}}{3L^3} = \frac{Nm\overline{v^2}}{3V}$$

**(6)** (5) より $PV = \dfrac{1}{3}Nm\overline{v^2}$。これを理想気体の状態方程式 $PV = nRT$ と比較すると，
$$\frac{1}{3}Nm\overline{v^2} = nRT$$
ここで物質量 $n = \dfrac{N}{N_A}$ であるから，両辺に $\dfrac{3}{2N}$ を掛けると，
$$\frac{1}{2}m\overline{v^2} = \frac{3}{2}\frac{n}{N}RT = \frac{3}{2}\frac{R}{N_A}T$$

> 💡 讲师批注：极其重要的物理结论——分子的平均平动动能 $\dfrac{1}{2}m\overline{v^2} = \dfrac{3}{2}k_B T$ **只与绝对温度 $T$ 成正比，与气体种类（分子质量 $m$）完全无关**！即同温下氢气与氧气的分子平均平动动能完全相等。

**(7)** (6) の式 $\dfrac{1}{2}m\overline{v^2} = \dfrac{3}{2}\dfrac{R}{N_A}T$ より $\overline{v^2} = \dfrac{3RT}{mN_A}$。  
ここで分子 1 個の質量 $m\text{ [kg]}$ とアボガドロ定数 $N_A$ の積 $mN_A$ は $1\text{ mol}$ の質量（$\text{kg}$ 単位）に等しく，分子量 $M\text{ [g]}$ を用いると $mN_A = M \times 10^{-3}\text{ [kg/mol]}$ であるから，
$$\sqrt{\overline{v^2}} = \sqrt{\frac{3RT}{mN_A}} = \sqrt{\frac{3RT}{M \times 10^{-3}}}$$

> 💡 讲师批注：**必考单位陷阱**！题干明确写了「分子量 $M\text{ [g]}$」，而 $R = 8.31\text{ J/(mol}\cdot\text{K)}$ 是 SI 单位制（含 $\text{kg}$），所以分母绝对不能写成 $\sqrt{\frac{3RT}{M}}$，必须乘上 $10^{-3}$ 写成 $\sqrt{\frac{3RT}{M \times 10^{-3}}}$！

#### 【最终答案】
- **(1) $2mv_x$**
- **(2) $\dfrac{v_x t}{2L}$**
- **(3) $\dfrac{mv_x^2}{L}$**
- **(4) $\dfrac{Nm\overline{v^2}}{3L}$**
- **(5) $\dfrac{Nm\overline{v^2}}{3V}$**
- **(6) $\dfrac{3}{2}\dfrac{R}{N_A}T$**
- **(7) $\sqrt{\dfrac{3RT}{M \times 10^{-3}}}$**

---

### 例題 3（教材 P.57 / 页码 56）：熱サイクル ①（矩形循环）

> **⚠️ 教材印刷勘误提示**：教材页码 56 原稿解答存在两处印刷疏漏：  
> 1. 第 (1) 问表格中 `C → D` 一行的 $\Delta U$ 与 $Q_{\text{in}}$ 均漏印了字母 $n$（原印 `-12RT_0`，正确应为 **$-12nRT_0$**）；  
> 2. 第 (2) 问最终答案印为 $\dfrac{12}{51}$，**未约分**！分子分母同除以 $3$ 应化为最简分数 **$\dfrac{4}{17}$**。

#### 【原题重现与翻译】
> **日文原题**：  
> $n\text{ [mol]}$ の単原子分子理想気体を右図のようなサイクルで状態変化させた。状態 A の気体の温度を $T_0$，気体定数を $R$ とする。  
> (1) 各過程における内部エネルギーの変化 $\Delta U$，気体が外部にした仕事 $W_{\text{out}}$，気体が吸収した熱量 $Q_{\text{in}}$ を $n, R, T_0$ を用いて表せ。  
> (2) このサイクルの熱効率 $e$ を求め，分数で答えよ。
>
> **中文翻译**：  
> 使 $n\text{ [mol]}$ 的单原子分子理想气体按右图所示循环进行状态变化（$A(V_0, P_0) \to B(V_0, 3P_0) \to C(4V_0, 3P_0) \to D(4V_0, P_0) \to A$）。设状态 A 的气体温度为 $T_0$，气体常数为 $R$。  
> (1) 用 $n, R, T_0$ 表示各过程中的内能变化 $\Delta U$、气体对外做的功 $W_{\text{out}}$ 以及气体吸收的热量 $Q_{\text{in}}$。  
> (2) 求该循环的热效率 $e$，用分数表示。

#### 【考点与模型定位】
**标准矩形热循环（定容-定压-定容-定压）**。核心技巧是先利用 $pV = nRT$ 把四个顶点温度 $T_A, T_B, T_C, T_D$ 全部标在图上，再逐段填表计算 $(\Delta U, W_{\text{out}}, Q_{\text{in}})$，最后用 $\sum \Delta U = 0$ 与 $\sum Q_{\text{in}} = \sum W_{\text{out}}$ 双向验算！

#### 【多色矢量图解（SVG）】

<svg viewBox="0 0 420 260" width="420" height="260" xmlns="http://www.w3.org/2000/svg" style="background:#fafafa;border:1px solid #e5e7eb;border-radius:8px;">
  <defs>
    <marker id="arr-blk-004-3" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0,0 L0,6 L7,3 z" fill="#111827"/></marker>
    <marker id="arr-red-004-3" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0,0 L0,6 L7,3 z" fill="#dc2626"/></marker>
    <marker id="arr-blue-004-3" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0,0 L0,6 L7,3 z" fill="#2563eb"/></marker>
  </defs>
  <!-- 坐标轴 -->
  <line x1="55" y1="225" x2="310" y2="225" stroke="#374151" stroke-width="1.8" marker-end="url(#arr-blk-004-3)"/>
  <text x="315" y="229" font-size="12" font-style="italic" fill="#111827">V</text>
  <line x1="55" y1="225" x2="55" y2="25" stroke="#374151" stroke-width="1.8" marker-end="url(#arr-blk-004-3)"/>
  <text x="40" y="30" font-size="12" font-style="italic" fill="#111827">P</text>
  <text x="40" y="238" font-size="11" fill="#374151">O</text>

  <!-- 净功面积填充 -->
  <rect x="100" y="65" width="160" height="105" fill="#fef3c7" fill-opacity="0.65"/>
  <text x="132" y="122" font-size="11" font-weight="bold" fill="#92400e">W_all = 6nRT₀</text>

  <!-- 辅助虚线 -->
  <line x1="55" y1="65" x2="100" y2="65" stroke="#9ca3af" stroke-dasharray="3,3"/>
  <line x1="55" y1="170" x2="100" y2="170" stroke="#9ca3af" stroke-dasharray="3,3"/>
  <line x1="100" y1="170" x2="100" y2="225" stroke="#9ca3af" stroke-dasharray="3,3"/>
  <line x1="260" y1="170" x2="260" y2="225" stroke="#9ca3af" stroke-dasharray="3,3"/>
  <text x="26" y="70" font-size="11" fill="#374151">3P₀</text>
  <text x="32" y="174" font-size="11" fill="#374151">P₀</text>
  <text x="94" y="242" font-size="11" fill="#374151">V₀</text>
  <text x="250" y="242" font-size="11" fill="#374151">4V₀</text>

  <!-- 吸热过程（红）：A→B, B→C -->
  <line x1="100" y1="170" x2="100" y2="73" stroke="#dc2626" stroke-width="2.4" marker-end="url(#arr-red-004-3)"/>
  <line x1="100" y1="65" x2="252" y2="65" stroke="#dc2626" stroke-width="2.4" marker-end="url(#arr-red-004-3)"/>
  <!-- 放热过程（蓝）：C→D, D→A -->
  <line x1="260" y1="65" x2="260" y2="162" stroke="#2563eb" stroke-width="2.4" marker-end="url(#arr-blue-004-3)"/>
  <line x1="260" y1="170" x2="108" y2="170" stroke="#2563eb" stroke-width="2.4" marker-end="url(#arr-blue-004-3)"/>

  <!-- 顶点与温度标注 -->
  <circle cx="100" cy="170" r="3.5" fill="#111827"/>
  <text x="72" y="186" font-size="10.5" font-weight="bold" fill="#111827">A(T₀)</text>
  <circle cx="100" cy="65" r="3.5" fill="#111827"/>
  <text x="68" y="55" font-size="10.5" font-weight="bold" fill="#111827">B(3T₀)</text>
  <circle cx="260" cy="65" r="3.5" fill="#111827"/>
  <text x="266" y="58" font-size="10.5" font-weight="bold" fill="#111827">C(12T₀)</text>
  <circle cx="260" cy="170" r="3.5" fill="#111827"/>
  <text x="266" y="180" font-size="10.5" font-weight="bold" fill="#111827">D(4T₀)</text>

  <!-- 图例 -->
  <text x="318" y="80" font-size="10" fill="#dc2626">■ 红：吸熱 (Q&gt;0)</text>
  <text x="318" y="98" font-size="10" fill="#2563eb">■ 蓝：放熱 (Q&lt;0)</text>
  <text x="318" y="116" font-size="10" fill="#92400e">■ 黄：正味の仕事</text>
</svg>

#### 【日本考场规范分步解答】

状態 A での状態方程式より $P_0 V_0 = nRT_0$ である。ボイル・シャルルの法則（$T \propto PV$）より，各状態の絶対温度は次のように求まる。
$$T_A = T_0, \quad T_B = 3T_0, \quad T_C = 12T_0, \quad T_D = 4T_0$$

> 💡 讲师批注：解一切热循环题的**第 0 步**永远是先求各点温度！因为 $PV \propto T$，直接用 $P, V$ 的倍数相乘即可口算：$B(3\times 1 = 3T_0)$，$C(3\times 4 = 12T_0)$，$D(1\times 4 = 4T_0)$。

**(1)** 単原子分子理想気体であるから，$\Delta U = \dfrac{3}{2}nR\Delta T$ および熱力学第一法則 $Q_{\text{in}} = \Delta U + W_{\text{out}}$ を各過程に適用する。

- **過程 $\text{A} \to \text{B}$（定積変化）**：
  - $\Delta U = \dfrac{3}{2}nR(3T_0 - T_0) = 3nRT_0$
  - $W_{\text{out}} = 0$
  - $Q_{\text{in}} = \Delta U + W_{\text{out}} = 3nRT_0$

- **過程 $\text{B} \to \text{C}$（定圧膨張）**：
  - $\Delta U = \dfrac{3}{2}nR(12T_0 - 3T_0) = \dfrac{27}{2}nRT_0$
  - $W_{\text{out}} = 3P_0(4V_0 - V_0) = 9P_0 V_0 = 9nRT_0$
  - $Q_{\text{in}} = \dfrac{27}{2}nRT_0 + 9nRT_0 = \dfrac{45}{2}nRT_0$

- **過程 $\text{C} \to \text{D}$（定積変化）**：
  - $\Delta U = \dfrac{3}{2}nR(4T_0 - 12T_0) = -12nRT_0$
  - $W_{\text{out}} = 0$
  - $Q_{\text{in}} = \Delta U + W_{\text{out}} = -12nRT_0$

- **過程 $\text{D} \to \text{A}$（定圧圧縮）**：
  - $\Delta U = \dfrac{3}{2}nR(T_0 - 4T_0) = -\dfrac{9}{2}nRT_0$
  - $W_{\text{out}} = P_0(V_0 - 4V_0) = -3P_0 V_0 = -3nRT_0$
  - $Q_{\text{in}} = -\dfrac{9}{2}nRT_0 + (-3nRT_0) = -\dfrac{15}{2}nRT_0$

まとめると下表の通りである：

| 過程 | $\Delta U$ | $W_{\text{out}}$ | $Q_{\text{in}}$ |
| :--- | :---: | :---: | :---: |
| $\text{A} \to \text{B}$ | $3nRT_0$ | $0$ | $3nRT_0$ |
| $\text{B} \to \text{C}$ | $\dfrac{27}{2}nRT_0$ | $9nRT_0$ | $\dfrac{45}{2}nRT_0$ |
| $\text{C} \to \text{D}$ | $-12nRT_0$ | $0$ | $-12nRT_0$ |
| $\text{D} \to \text{A}$ | $-\dfrac{9}{2}nRT_0$ | $-3nRT_0$ | $-\dfrac{15}{2}nRT_0$ |

> 💡 讲师批注：填完表务必花 5 秒做**闭环验算**：$\sum \Delta U = 3 + 13.5 - 12 - 4.5 = 0$（完美归零！）；$\sum W_{\text{out}} = 9 - 3 = 6nRT_0$，与矩形面积 $(3P_0 - P_0)(4V_0 - V_0) = 6P_0 V_0 = 6nRT_0$ 完全吻合！

**(2)** 1 サイクルの間に気体が熱を**吸収**する過程は $Q_{\text{in}} > 0$ の $\text{A} \to \text{B}$ と $\text{B} \to \text{C}$ のみである。  
したがって，熱効率 $e$ は，
$$e = \frac{W_{\text{all}}}{Q_{\text{in(吸熱)}}} = \frac{W_{\text{A}\to\text{B}} + W_{\text{B}\to\text{C}} + W_{\text{C}\to\text{D}} + W_{\text{D}\to\text{A}}}{Q_{\text{A}\to\text{B}} + Q_{\text{B}\to\text{C}}}$$
$$= \frac{0 + 9nRT_0 + 0 - 3nRT_0}{3nRT_0 + \dfrac{45}{2}nRT_0} = \frac{6nRT_0}{\dfrac{51}{2}nRT_0} = \frac{12}{51} = \frac{4}{17}$$

> 💡 讲师批注：千万提醒学生：教材答案写成 $\dfrac{12}{51}$ 忘了约分！$12 = 3 \times 4,\ 51 = 3 \times 17$，考场上必须化简成最简分数 **$\dfrac{4}{17}$**。

#### 【最终答案】
- **(1)** 见上表（注意 $\text{C}\to\text{D}$ 为 $-12nRT_0$）
- **(2) $e = \dfrac{4}{17}$**

---

### 例題 4（教材 P.58 / 页码 57）：熱サイクル ②（含等温过程的循环）

#### 【原题重现与翻译】
> **日文原题**：  
> 単原子分子理想気体を右図のようなサイクルで状態変化させた。$\text{B} \to \text{C}$ は等温変化で，この間に気体に $Q$ の熱を与えた。  
> (1) 各過程における内部エネルギーの変化 $\Delta U$，気体が外部にした仕事 $W_{\text{out}}$，気体が吸収した熱量 $Q_{\text{in}}$ を $P_0, V_0, Q$ を用いて表せ。  
> (2) このサイクルの熱効率 $e$ を求めよ。
>
> **中文翻译**：  
> 使单原子分子理想气体按右图所示循环进行状态变化（$A(V_0, P_0) \to B(V_0, 3P_0) \to C(3V_0, P_0) \to A$）。其中 $\text{B} \to \text{C}$ 为等温变化，在此过程中向气体供给热量 $Q$。  
> (1) 用 $P_0, V_0, Q$ 表示各过程中的内能变化 $\Delta U$、气体对外做的功 $W_{\text{out}}$ 以及气体吸收的热量 $Q_{\text{in}}$。  
> (2) 求该循环的热效率 $e$。

#### 【考点与模型定位】
**含等温过程的三段循环**（用 $P_0 V_0$ 直接代换 $nRT$，且等温过程功无法用初等几何直接求面积，必须利用等温 $\Delta U = 0 \implies W_{\text{out}} = Q$ 反推）。

#### 【多色矢量图解（SVG）】

<svg viewBox="0 0 420 260" width="420" height="260" xmlns="http://www.w3.org/2000/svg" style="background:#fafafa;border:1px solid #e5e7eb;border-radius:8px;">
  <defs>
    <marker id="arr-blk-004-4" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0,0 L0,6 L7,3 z" fill="#111827"/></marker>
    <marker id="arr-red-004-4" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0,0 L0,6 L7,3 z" fill="#dc2626"/></marker>
    <marker id="arr-blue-004-4" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0,0 L0,6 L7,3 z" fill="#2563eb"/></marker>
  </defs>
  <!-- 坐标轴 -->
  <line x1="55" y1="225" x2="310" y2="225" stroke="#374151" stroke-width="1.8" marker-end="url(#arr-blk-004-4)"/>
  <text x="315" y="229" font-size="12" font-style="italic" fill="#111827">V</text>
  <line x1="55" y1="225" x2="55" y2="25" stroke="#374151" stroke-width="1.8" marker-end="url(#arr-blk-004-4)"/>
  <text x="40" y="30" font-size="12" font-style="italic" fill="#111827">P</text>
  <text x="40" y="238" font-size="11" fill="#374151">O</text>

  <!-- 净功面积填充 -->
  <path d="M 105 170 L 105 60 Q 145 148 255 170 Z" fill="#fef3c7" fill-opacity="0.7"/>
  <text x="115" y="156" font-size="10.5" font-weight="bold" fill="#92400e">W_all = Q - 2P₀V₀</text>

  <!-- 辅助虚线 -->
  <line x1="55" y1="60" x2="105" y2="60" stroke="#9ca3af" stroke-dasharray="3,3"/>
  <line x1="55" y1="170" x2="105" y2="170" stroke="#9ca3af" stroke-dasharray="3,3"/>
  <line x1="105" y1="170" x2="105" y2="225" stroke="#9ca3af" stroke-dasharray="3,3"/>
  <line x1="255" y1="170" x2="255" y2="225" stroke="#9ca3af" stroke-dasharray="3,3"/>
  <text x="26" y="65" font-size="11" fill="#374151">3P₀</text>
  <text x="32" y="174" font-size="11" fill="#374151">P₀</text>
  <text x="98" y="242" font-size="11" fill="#374151">V₀</text>
  <text x="245" y="242" font-size="11" fill="#374151">3V₀</text>

  <!-- A→B（定积吸热，红） -->
  <line x1="105" y1="170" x2="105" y2="68" stroke="#dc2626" stroke-width="2.4" marker-end="url(#arr-red-004-4)"/>
  <!-- B→C（等温吸热，红双曲线） -->
  <path d="M 105 60 Q 145 148 248 168" fill="none" stroke="#dc2626" stroke-width="2.4" marker-end="url(#arr-red-004-4)"/>
  <text x="172" y="112" font-size="10.5" fill="#dc2626">等温変化 (吸熱 Q)</text>
  <!-- C→A（定压放热，蓝） -->
  <line x1="255" y1="170" x2="113" y2="170" stroke="#2563eb" stroke-width="2.4" marker-end="url(#arr-blue-004-4)"/>

  <!-- 顶点 -->
  <circle cx="105" cy="170" r="3.5" fill="#111827"/>
  <text x="86" y="185" font-size="11" font-weight="bold" fill="#111827">A</text>
  <circle cx="105" cy="60" r="3.5" fill="#111827"/>
  <text x="88" y="54" font-size="11" font-weight="bold" fill="#111827">B</text>
  <circle cx="255" cy="170" r="3.5" fill="#111827"/>
  <text x="262" y="176" font-size="11" font-weight="bold" fill="#111827">C</text>

  <!-- 图例 -->
  <text x="308" y="75" font-size="10" fill="#dc2626">■ 红：吸熱過程</text>
  <text x="308" y="93" font-size="10" fill="#2563eb">■ 蓝：放熱過程</text>
  <text x="308" y="111" font-size="10" fill="#374151">※ P_B V_B = P_C V_C</text>
  <text x="318" y="125" font-size="10" fill="#374151">= 3P₀V₀</text>
</svg>

#### 【日本考场规范分步解答】

**(1)** 単原子分子理想気体の内部エネルギーは $U = \dfrac{3}{2}nRT = \dfrac{3}{2}PV$ であるから，各過程について以下が成り立つ。

- **過程 $\text{A} \to \text{B}$（定積変化）**：
  - $\Delta U = \dfrac{3}{2}(3P_0 V_0 - P_0 V_0) = 3P_0 V_0$
  - $W_{\text{out}} = 0$
  - $Q_{\text{in}} = \Delta U + W_{\text{out}} = 3P_0 V_0$

- **過程 $\text{B} \to \text{C}$（等温変化）**：
  - 等温変化であるから $\Delta T = 0$，よって $\Delta U = 0$。
  - 熱力学第一法則 $Q_{\text{in}} = \Delta U + W_{\text{out}}$ と $Q_{\text{in}} = Q$ より，$W_{\text{out}} = Q$。

> 💡 讲师批注：高中阶段尚未学习微积分求等温功 $nRT\ln(V_2/V_1)$，因此题目必然把等温吸热量 $Q$ 直接作为已知量给出，考的正是「等温 $\Delta U = 0 \implies W_{\text{out}} = Q_{\text{in}}$」这一核心性质！

- **過程 $\text{C} \to \text{A}$（定圧圧縮）**：
  - $\Delta U = \dfrac{3}{2}(P_0 V_0 - P_0 \cdot 3V_0) = -3P_0 V_0$
  - $W_{\text{out}} = P_0(V_0 - 3V_0) = -2P_0 V_0$
  - $Q_{\text{in}} = \Delta U + W_{\text{out}} = -3P_0 V_0 + (-2P_0 V_0) = -5P_0 V_0$

まとめると下表の通りである：

| 過程 | $\Delta U$ | $W_{\text{out}}$ | $Q_{\text{in}}$ |
| :--- | :---: | :---: | :---: |
| $\text{A} \to \text{B}$ | $3P_0 V_0$ | $0$ | $3P_0 V_0$ |
| $\text{B} \to \text{C}$ | $0$ | $Q$ | $Q$ |
| $\text{C} \to \text{A}$ | $-3P_0 V_0$ | $-2P_0 V_0$ | $-5P_0 V_0$ |

**(2)** 吸熱過程は $\text{A} \to \text{B}$ と $\text{B} \to \text{C}$ の 2 過程であるから，熱効率 $e$ は，
$$e = \frac{W_{\text{all}}}{Q_{\text{in(吸熱)}}} = \frac{W_{\text{A}\to\text{B}} + W_{\text{B}\to\text{C}} + W_{\text{C}\to\text{A}}}{Q_{\text{A}\to\text{B}} + Q_{\text{B}\to\text{C}}} = \frac{0 + Q - 2P_0 V_0}{3P_0 V_0 + Q} = \frac{Q - 2P_0 V_0}{Q + 3P_0 V_0}$$

> 💡 讲师批注：用 $e = 1 - \dfrac{Q_{\text{out}}}{Q_{\text{in}}}$ 验算：$Q_{\text{out}} = 5P_0 V_0$，则 $1 - \dfrac{5P_0 V_0}{Q + 3P_0 V_0} = \dfrac{Q - 2P_0 V_0}{Q + 3P_0 V_0}$，完全一致！

#### 【最终答案】
- **(1)** 见上表
- **(2) $e = \dfrac{Q - 2P_0 V_0}{Q + 3P_0 V_0}$**

---

### 例題 5（教材 P.59 / 页码 58）：熱サイクル ③（含绝热过程的循环与泊松定律）

#### 【原题重现与翻译】
> **日文原题**：  
> $n\text{ [mol]}$ の理想気体を右図のようなサイクルで状態変化させた。$\text{B} \to \text{C}$ は断熱変化である。状態 A，B，C の絶対温度を $T_A, T_B, T_C$，定積モル比熱を $C_v$，定圧モル比熱を $C_p$ とする。  
> (1) 各過程における内部エネルギーの変化 $\Delta U$，気体が外部にした仕事 $W_{\text{out}}$，気体が吸収した熱量 $Q_{\text{in}}$ を $n, T_A, T_B, T_C, C_v, C_p$ を用いて表せ。  
> (2) このサイクルの熱効率 $e$ を $\gamma\left(= \dfrac{C_p}{C_v}\right), T_A, T_B, T_C$ を用いて表せ。  
> (3) 単原子分子理想気体の断熱変化では $PV^\gamma$ が一定であることが知られている。このときの熱効率 $e$ を求め，%（整数値）で答えよ。必要なら $2^{\frac{5}{3}} \fallingdotseq \dfrac{16}{5}$ を用いよ。
>
> **中文翻译**：  
> 使 $n\text{ [mol]}$ 的理想气体按右图所示循环进行状态变化（$A(V_0, P_0) \to B(V_0, P_B) \to C(2V_0, P_0) \to A$）。其中 $\text{B} \to \text{C}$ 为绝热变化。设状态 A、B、C 的绝对温度分别为 $T_A, T_B, T_C$，定容摩尔比热为 $C_v$，定压摩尔比热为 $C_p$。  
> (1) 用 $n, T_A, T_B, T_C, C_v, C_p$ 表示各过程中的内能变化 $\Delta U$、气体对外做的功 $W_{\text{out}}$ 以及气体吸收的热量 $Q_{\text{in}}$。  
> (2) 用 $\gamma\left(= \dfrac{C_p}{C_v}\right), T_A, T_B, T_C$ 表示该循环的热效率 $e$。  
> (3) 已知单原子分子理想气体绝热变化时 $PV^\gamma$ 为定值。求此时的热效率 $e$，用百分数（整数值）作答。必要时可使用 $2^{\frac{5}{3}} \fallingdotseq \dfrac{16}{5}$。

#### 【考点与模型定位】
**含绝热过程的综合循环（定容-绝热-定压）＋ 迈耶公式消去 $R$ ＋ 泊松定律求温度比**。属于 EJU 物理热学压轴难度，非常值得在课堂上精讲！

#### 【多色矢量图解（SVG）】

<svg viewBox="0 0 420 260" width="420" height="260" xmlns="http://www.w3.org/2000/svg" style="background:#fafafa;border:1px solid #e5e7eb;border-radius:8px;">
  <defs>
    <marker id="arr-blk-004-5" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0,0 L0,6 L7,3 z" fill="#111827"/></marker>
    <marker id="arr-red-004-5" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0,0 L0,6 L7,3 z" fill="#dc2626"/></marker>
    <marker id="arr-blue-004-5" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0,0 L0,6 L7,3 z" fill="#2563eb"/></marker>
    <marker id="arr-green-004-5" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0,0 L0,6 L7,3 z" fill="#16a34a"/></marker>
  </defs>
  <!-- 坐标轴 -->
  <line x1="55" y1="225" x2="300" y2="225" stroke="#374151" stroke-width="1.8" marker-end="url(#arr-blk-004-5)"/>
  <text x="305" y="229" font-size="12" font-style="italic" fill="#111827">V</text>
  <line x1="55" y1="225" x2="55" y2="25" stroke="#374151" stroke-width="1.8" marker-end="url(#arr-blk-004-5)"/>
  <text x="40" y="30" font-size="12" font-style="italic" fill="#111827">P</text>
  <text x="40" y="238" font-size="11" fill="#374151">O</text>

  <!-- 净功面积 -->
  <path d="M 110 175 L 110 50 Q 145 142 230 175 Z" fill="#fef3c7" fill-opacity="0.7"/>

  <!-- 辅助虚线 -->
  <line x1="55" y1="50" x2="110" y2="50" stroke="#9ca3af" stroke-dasharray="3,3"/>
  <line x1="55" y1="175" x2="110" y2="175" stroke="#9ca3af" stroke-dasharray="3,3"/>
  <line x1="110" y1="175" x2="110" y2="225" stroke="#9ca3af" stroke-dasharray="3,3"/>
  <line x1="230" y1="175" x2="230" y2="225" stroke="#9ca3af" stroke-dasharray="3,3"/>
  <text x="28" y="54" font-size="11" fill="#374151">P_B</text>
  <text x="32" y="179" font-size="11" fill="#374151">P₀</text>
  <text x="103" y="242" font-size="11" fill="#374151">V₀</text>
  <text x="220" y="242" font-size="11" fill="#374151">2V₀</text>

  <!-- A→B（定积吸热，红） -->
  <line x1="110" y1="175" x2="110" y2="58" stroke="#dc2626" stroke-width="2.4" marker-end="url(#arr-red-004-5)"/>
  <!-- B→C（绝热膨胀，绿，更陡） -->
  <path d="M 110 50 Q 145 142 223 172" fill="none" stroke="#16a34a" stroke-width="2.4" marker-end="url(#arr-green-004-5)"/>
  <text x="165" y="102" font-size="10.5" font-weight="bold" fill="#16a34a">断熱変化 (Q=0)</text>
  <text x="165" y="118" font-size="10" fill="#16a34a">PV^γ = 一定</text>
  <!-- C→A（定压放热，蓝） -->
  <line x1="230" y1="175" x2="118" y2="175" stroke="#2563eb" stroke-width="2.4" marker-end="url(#arr-blue-004-5)"/>

  <!-- 顶点 -->
  <circle cx="110" cy="175" r="3.5" fill="#111827"/>
  <text x="82" y="190" font-size="10.5" font-weight="bold" fill="#111827">A(T_A)</text>
  <circle cx="110" cy="50" r="3.5" fill="#111827"/>
  <text x="84" y="42" font-size="10.5" font-weight="bold" fill="#111827">B(T_B)</text>
  <circle cx="230" cy="175" r="3.5" fill="#111827"/>
  <text x="236" y="182" font-size="10.5" font-weight="bold" fill="#111827">C(T_C)</text>

  <!-- 图例 -->
  <text x="292" y="70" font-size="10" fill="#dc2626">■ 红：定積吸熱</text>
  <text x="292" y="88" font-size="10" fill="#16a34a">■ 绿：断熱膨張 (Q=0)</text>
  <text x="292" y="106" font-size="10" fill="#2563eb">■ 蓝：定圧放熱</text>
  <text x="292" y="132" font-size="9.5" fill="#374151">単原子分子:</text>
  <text x="292" y="146" font-size="9.5" fill="#374151">γ = 5/3</text>
  <text x="292" y="160" font-size="9.5" fill="#374151">T_C = 2T_A</text>
  <text x="292" y="174" font-size="9.5" fill="#374151">T_B = (16/5)T_A</text>
</svg>

#### 【日本考场规范分步解答】

**(1)** どの変化においても常に $\Delta U = nC_v\Delta T$ が成り立つ。また，使用可能な文字に $R$ が含まれていないことに注意する。

- **過程 $\text{A} \to \text{B}$（定積変化）**：
  - $\Delta U = nC_v(T_B - T_A)$
  - $W_{\text{out}} = 0$
  - $Q_{\text{in}} = \Delta U + W_{\text{out}} = nC_v(T_B - T_A)$

- **過程 $\text{B} \to \text{C}$（断熱変化）**：
  - $\Delta U = nC_v(T_C - T_B)$
  - 断熱変化より $Q_{\text{in}} = 0$
  - 熱力学第一法則 $0 = \Delta U + W_{\text{out}}$ より，$W_{\text{out}} = -\Delta U = -nC_v(T_C - T_B)$

- **過程 $\text{C} \to \text{A}$（定圧圧縮）**：
  - $\Delta U = nC_v(T_A - T_C)$
  - 定圧モル比熱の定義より $Q_{\text{in}} = nC_p(T_A - T_C)$
  - 熱力学第一法則 $W_{\text{out}} = Q_{\text{in}} - \Delta U$（またはマイヤーの関係 $R = C_p - C_v$）より，
    $$W_{\text{out}} = n(C_p - C_v)(T_A - T_C)$$

> 💡 讲师批注：超级细心的审题点！题目(1) 明确限定**只能用 $n, T_A, T_B, T_C, C_v, C_p$**，没有给 $R$！所以定压做功 $W_{\text{out}} = nR(T_A - T_C)$ 必须用迈耶关系 $R = C_p - C_v$（或直接 $Q_{\text{in}} - \Delta U$）写成 $n(C_p - C_v)(T_A - T_C)$，否则会丢分！

まとめると下表の通りである：

| 過程 | $\Delta U$ | $W_{\text{out}}$ | $Q_{\text{in}}$ |
| :--- | :---: | :---: | :---: |
| $\text{A} \to \text{B}$ | $nC_v(T_B - T_A)$ | $0$ | $nC_v(T_B - T_A)$ |
| $\text{B} \to \text{C}$ | $nC_v(T_C - T_B)$ | $-nC_v(T_C - T_B)$ | $0$ |
| $\text{C} \to \text{A}$ | $nC_v(T_A - T_C)$ | $n(C_p - C_v)(T_A - T_C)$ | $nC_p(T_A - T_C)$ |

**(2)** 吸熱過程は $\text{A} \to \text{B}$ のみ（$Q_{\text{A}\to\text{B}} = nC_v(T_B - T_A) > 0$），放熱過程は $\text{C} \to \text{A}$ のみ（放出熱量 $Q_{\text{out}} = -Q_{\text{C}\to\text{A}} = nC_p(T_C - T_A) > 0$）である。  
したがって，熱効率 $e$ は，
$$e = \frac{W_{\text{all}}}{Q_{\text{A}\to\text{B}}} = \frac{0 - nC_v(T_C - T_B) + n(C_p - C_v)(T_A - T_C)}{nC_v(T_B - T_A)}$$
$$= \frac{C_v(T_B - T_A) - C_p(T_C - T_A)}{C_v(T_B - T_A)} = 1 - \frac{C_p}{C_v}\cdot\frac{T_C - T_A}{T_B - T_A} = 1 - \gamma\cdot\frac{T_C - T_A}{T_B - T_A}$$

> 💡 讲师批注：教学生一个秒杀技巧——当循环中只有一段吸热、一段放热（另一段绝热 $Q=0$）时，直接套用 **$e = 1 - \dfrac{Q_{\text{out}}}{Q_{\text{in}}} = 1 - \dfrac{nC_p(T_C - T_A)}{nC_v(T_B - T_A)} = 1 - \gamma\dfrac{T_C - T_A}{T_B - T_A}$**，一步出答案，比合并 $W_{\text{all}}$ 快三倍还不易算错符号！

**(3)** 単原子分子理想気体であるから，$\gamma = \dfrac{C_p}{C_v} = \dfrac{\frac{5}{2}R}{\frac{3}{2}R} = \dfrac{5}{3}$ である。  
- **過程 $\text{C} \to \text{A}$（定圧）** にシャルルの法則を用いると，
  $$\frac{V_0}{T_A} = \frac{2V_0}{T_C} \implies T_C = 2T_A$$
- **過程 $\text{B} \to \text{C}$（断熱）** にポアソンの法則 $PV^\gamma = \text{一定}$ を用いると，
  $$P_B V_0^{\frac{5}{3}} = P_0 (2V_0)^{\frac{5}{3}} \implies P_B = 2^{\frac{5}{3}} P_0 \fallingdotseq \frac{16}{5}P_0$$
- **状態 A と状態 B（定積）** にボイル・シャルルの法則を用いると（$\dfrac{P_0}{T_A} = \dfrac{P_B}{T_B}$），
  $$T_B = \frac{P_B}{P_0}T_A = \frac{16}{5}T_A$$
  （なお，状態 B と C で $\dfrac{\frac{16}{5}P_0 V_0}{T_B} = \dfrac{P_0 \cdot 2V_0}{T_C}$ としても同様に $T_B = \dfrac{8}{5}T_C = \dfrac{16}{5}T_A$ を得る。）

これらを (2) の式に代入すると，
$$e = 1 - \frac{5}{3}\cdot\frac{2T_A - T_A}{\dfrac{16}{5}T_A - T_A} = 1 - \frac{5}{3}\cdot\frac{1}{\dfrac{11}{5}} = 1 - \frac{25}{33} = \frac{8}{33} = 0.2424\dots \fallingdotseq 24\%$$

> 💡 讲师批注：也可以直接记忆泊松定律的**温度-体积形式 $TV^{\gamma - 1} = \text{一定}$** 来验算：$T_B V_0^{2/3} = T_C (2V_0)^{2/3} \implies T_B = 2^{2/3} T_C = 2^{2/3} \cdot 2T_A = 2^{5/3} T_A = \dfrac{16}{5}T_A$，连 $P_B$ 都不用求，直接一步直达 $T_B$！

#### 【最终答案】
- **(1)** 见上表
- **(2) $e = 1 - \gamma\cdot\dfrac{T_C - T_A}{T_B - T_A}$**
- **(3) $e = 24\%$**

---

### 核心模型图解补充（教材概念页板书素材）

为方便纯日文板书授课，将本切片核心概念页（三态加热曲线 P.46、四大状态变化 $p$-$V$ 图对比 P.55–56、波动基本要素 P.60）配齐多色 SVG 板书图：

#### 补充图 A：物质三态加热曲线（P.46） & 波动要素图（P.60）

<svg viewBox="0 0 420 230" width="420" height="230" xmlns="http://www.w3.org/2000/svg" style="background:#fafafa;border:1px solid #e5e7eb;border-radius:8px;">
  <defs>
    <marker id="arr-blk-004-6" markerWidth="7" markerHeight="7" refX="5" refY="3" orient="auto"><path d="M0,0 L0,6 L6,3 z" fill="#111827"/></marker>
    <marker id="arr-red-004-6" markerWidth="7" markerHeight="7" refX="5" refY="3" orient="auto"><path d="M0,0 L0,6 L6,3 z" fill="#dc2626"/></marker>
    <marker id="arr-blue-004-6" markerWidth="7" markerHeight="7" refX="5" refY="3" orient="auto"><path d="M0,0 L0,6 L6,3 z" fill="#2563eb"/></marker>
  </defs>
  <!-- 左半：三态加热曲线 -->
  <text x="35" y="20" font-size="11" font-weight="bold" fill="#374151">物質の三態と潜熱 (水)</text>
  <line x1="35" y1="195" x2="200" y2="195" stroke="#374151" stroke-width="1.5" marker-end="url(#arr-blk-004-6)"/>
  <text x="155" y="212" font-size="10" fill="#374151">加熱時間</text>
  <line x1="35" y1="195" x2="35" y2="32" stroke="#374151" stroke-width="1.5" marker-end="url(#arr-blk-004-6)"/>
  <text x="10" y="34" font-size="9.5" fill="#374151">温度</text>
  <!-- 加热折线 -->
  <polyline points="35,175 55,150 92,150 125,85 172,85 190,42" fill="none" stroke="#dc2626" stroke-width="2.2"/>
  <line x1="35" y1="150" x2="55" y2="150" stroke="#9ca3af" stroke-dasharray="2,2"/>
  <line x1="35" y1="85" x2="125" y2="85" stroke="#9ca3af" stroke-dasharray="2,2"/>
  <text x="8" y="153" font-size="9.5" fill="#374151">0°C</text>
  <text x="4" y="88" font-size="9.5" fill="#374151">100°C</text>
  <text x="58" y="143" font-size="9" fill="#2563eb">融解熱</text>
  <text x="132" y="78" font-size="9" fill="#2563eb">蒸発熱</text>
  <text x="54" y="166" font-size="8.5" fill="#4b5563">固+液</text>
  <text x="134" y="102" font-size="8.5" fill="#4b5563">液+気</text>

  <!-- 分隔线 -->
  <line x1="212" y1="15" x2="212" y2="215" stroke="#d1d5db" stroke-dasharray="4,4"/>

  <!-- 右半：波动要素图 -->
  <text x="242" y="20" font-size="11" font-weight="bold" fill="#374151">波の要素 (v = fλ, f = 1/T)</text>
  <!-- 平衡位置 -->
  <line x1="225" y1="125" x2="405" y2="125" stroke="#6b7280" stroke-width="1.3" stroke-dasharray="4,3"/>
  <!-- 正弦波 -->
  <path d="M 230 125 Q 250 55 270 125 T 310 125 T 350 125 T 390 125" fill="none" stroke="#2563eb" stroke-width="2.4"/>
  <!-- 山、谷 -->
  <text x="244" y="78" font-size="10" font-weight="bold" fill="#1e40af">山</text>
  <text x="284" y="182" font-size="10" font-weight="bold" fill="#1e40af">谷</text>
  <!-- 波长标注 -->
  <line x1="250" y1="62" x2="330" y2="62" stroke="#dc2626" stroke-width="1.6" marker-end="url(#arr-red-004-6)"/>
  <line x1="250" y1="56" x2="250" y2="85" stroke="#dc2626" stroke-width="1" stroke-dasharray="2,2"/>
  <line x1="330" y1="56" x2="330" y2="85" stroke="#dc2626" stroke-width="1" stroke-dasharray="2,2"/>
  <text x="274" y="54" font-size="10.5" font-weight="bold" fill="#dc2626">波長 λ</text>
  <!-- 振幅标注 -->
  <line x1="330" y1="125" x2="330" y2="92" stroke="#16a34a" stroke-width="2"/>
  <text x="336" y="114" font-size="10.5" font-weight="bold" fill="#16a34a">振幅 A</text>
  <text x="232" y="208" font-size="9.5" fill="#dc2626">※ 振幅は中心から山まで（山〜谷は 2A）</text>
</svg>

#### 补充图 B：四大状态变化 $p$-$V$ 曲线斜率对比（P.55–56）

<svg viewBox="0 0 420 220" width="420" height="220" xmlns="http://www.w3.org/2000/svg" style="background:#fafafa;border:1px solid #e5e7eb;border-radius:8px;">
  <defs>
    <marker id="arr-blk-004-7" markerWidth="7" markerHeight="7" refX="5" refY="3" orient="auto"><path d="M0,0 L0,6 L6,3 z" fill="#111827"/></marker>
    <marker id="arr-red-004-7" markerWidth="7" markerHeight="7" refX="5" refY="3" orient="auto"><path d="M0,0 L0,6 L6,3 z" fill="#dc2626"/></marker>
    <marker id="arr-blue-004-7" markerWidth="7" markerHeight="7" refX="5" refY="3" orient="auto"><path d="M0,0 L0,6 L6,3 z" fill="#2563eb"/></marker>
    <marker id="arr-green-004-7" markerWidth="7" markerHeight="7" refX="5" refY="3" orient="auto"><path d="M0,0 L0,6 L6,3 z" fill="#16a34a"/></marker>
  </defs>
  <text x="20" y="20" font-size="11" font-weight="bold" fill="#374151">同一始点 A からの 4 大状態変化の比較（p-V グラフ）</text>
  <!-- 坐标轴 -->
  <line x1="45" y1="195" x2="275" y2="195" stroke="#374151" stroke-width="1.6" marker-end="url(#arr-blk-004-7)"/>
  <text x="280" y="199" font-size="12" font-style="italic" fill="#111827">V</text>
  <line x1="45" y1="195" x2="45" y2="32" stroke="#374151" stroke-width="1.6" marker-end="url(#arr-blk-004-7)"/>
  <text x="32" y="36" font-size="12" font-style="italic" fill="#111827">p</text>

  <!-- 起点 A -->
  <circle cx="110" cy="85" r="4" fill="#111827"/>
  <text x="95" y="80" font-size="11" font-weight="bold" fill="#111827">A</text>

  <!-- 1. 定积变化（上） -->
  <line x1="110" y1="85" x2="110" y2="42" stroke="#dc2626" stroke-width="2.2" marker-end="url(#arr-red-004-7)"/>
  <text x="116" y="48" font-size="10" fill="#dc2626">定積 (W=0)</text>
  <!-- 2. 定压变化（右） -->
  <line x1="110" y1="85" x2="235" y2="85" stroke="#2563eb" stroke-width="2.2" marker-end="url(#arr-blue-004-7)"/>
  <text x="172" y="78" font-size="10" fill="#2563eb">定圧 (W = pΔV)</text>
  <!-- 3. 等温变化 -->
  <path d="M 110 85 Q 155 128 235 142" fill="none" stroke="#111827" stroke-width="2" stroke-dasharray="5,3" marker-end="url(#arr-blk-004-7)"/>
  <text x="192" y="133" font-size="10" fill="#111827">等温 (pV=一定)</text>
  <!-- 4. 绝热变化（更陡） -->
  <path d="M 110 85 Q 140 155 215 178" fill="none" stroke="#16a34a" stroke-width="2.4" marker-end="url(#arr-green-004-7)"/>
  <text x="160" y="185" font-size="10" font-weight="bold" fill="#16a34a">断熱 (pV^γ=一定, より急!)</text>

  <!-- 右侧要点框 -->
  <rect x="292" y="45" width="118" height="135" rx="6" fill="#ffffff" stroke="#d1d5db"/>
  <text x="300" y="65" font-size="10" font-weight="bold" fill="#374151">重要ポイント</text>
  <text x="300" y="85" font-size="9.5" fill="#16a34a">• 断熱線は等温線</text>
  <text x="306" y="99" font-size="9.5" fill="#16a34a">より傾きが急！</text>
  <text x="300" y="120" font-size="9.5" fill="#374151">• 膨張時の仕事:</text>
  <text x="306" y="134" font-size="9.5" fill="#2563eb">定圧 &gt; 等温 &gt; 断熱</text>
  <text x="300" y="155" font-size="9.5" fill="#dc2626">• 常に ΔU=nC_vΔT</text>
  <text x="300" y="170" font-size="9.5" fill="#dc2626">• 常に pV=nRT</text>
</svg>

---

## 4. 全局术语表同步说明

本切片新增的 **63 条** 日文物理核心术语与假名注音（覆盖热学全章与波动入门，已避开切片 001 已有基础力学词条）已写入暂存术语文件 [.glossary_004.md](file:///Users/baohan/Desktop/EJU/notes_物理/.glossary_004.md)，供主控汇总去重合并至全局术语表 [glossary_all.md](file:///Users/baohan/Desktop/EJU/notes_物理/glossary_all.md)。
