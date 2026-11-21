# EJU 物理全解讲义 — 切片 001（P.1–P.15）
> **对应教材章节**：物理基礎・第一章 物体の運動（相対速度、等加速度運動、落体・放物運動、力のつりあい、摩擦力、ばねの弾性力、水圧と浮力）  
> **适用对象**：需快速唤醒中国高中物理基础、并掌握纯日文板书与 EJU 考场规范表达的授课教师 / 考生

---

## 1. 本节前置：国内高中物理基础唤醒

本切片涵盖**运动学（キネマティクス）**与**静力学（力のつりあい）**两大基础模块，是整个力学大厦的地基。

### 1.1 运动学核心概念与公式推导

1. **速率与速度、相对速度**
   - **速率（速さ $v$）**：标量（スカラー量），单位时间移动的路程，恒 $\ge 0$。
   - **速度（速度 $\vec{v}$）**：矢量（ベクトル量），既有大小又有方向。
   - **相对速度**：从以速度 $\vec{v}_A$ 运动的观察者 $A$ 来看，以速度 $\vec{v}_B$ 运动的物体 $B$ 的相对速度为：
     $$\vec{v}_{AB} = \vec{v}_B - \vec{v}_A \quad \text{（口诀：被观察者} - \text{观察者 / 相手} - \text{自分）}$$

2. **匀变速直线运动（等加速度直線運動）三大公式**
   设初速度 $v_0$、恒定加速度 $a$、时刻 $t$ 时的速度为 $v$、位移为 $x$：
   - ① **速度-时间公式**（加速度定义 $a = \frac{v - v_0}{t}$ 变形）：
     $$v = v_0 + at$$
   - ② **位移-时间公式**（$v$-$t$ 图像梯形面积 $=$ 矩形 $v_0 t +$ 三角形 $\frac{1}{2}at^2$）：
     $$x = v_0 t + \frac{1}{2}at^2$$
   - ③ **速度-位移公式**（联立 ①② 消去时间 $t$）：
     $$v^2 - v_0^2 = 2ax$$
   - **$v$-$t$ 图像两大核心性质**：
     - **斜率（傾き）** $= $ 加速度 $a$；
     - **与时间轴围成的面积（面積）** $= $ 位移（单向运动时等于路程）。

3. **竖直方向的落体运动**（实质是 $a = \pm g$ 的匀变速直线运动）
   - **自由落体（自由落下）**：取竖直向下为正，$v_0 = 0, a = +g$：
     $$v = gt, \qquad y = \frac{1}{2}gt^2, \qquad v^2 = 2gy$$
   - **竖直下抛（鉛直投げ下ろし）**：取竖直向下为正，$a = +g$：
     $$v = v_0 + gt, \qquad y = v_0 t + \frac{1}{2}gt^2, \qquad v^2 - v_0^2 = 2gy$$
   - **竖直上抛（鉛直投げ上げ）**：取竖直向上为正，$a = -g$：
     $$v = v_0 - gt, \qquad y = v_0 t - \frac{1}{2}gt^2, \qquad v^2 - v_0^2 = -2gy$$

4. **抛体运动（放物運動）的运动分解思想**
   - **平抛运动（水平投射）**：水平方向匀速直线运动（$a_x = 0$）$+$ 竖直方向自由落体（$a_y = g$）。
   - **斜抛运动（斜方投射）**：水平方向匀速直线运动（$v_{0x} = v_0\cos\theta$）$+$ 竖直方向竖直上抛（$v_{0y} = v_0\sin\theta$）。
   - **斜面斜抛**：将坐标轴沿斜面（$x$ 轴）与垂直斜面（$y$ 轴）旋转，把重力加速度 $g$ 分解为 $g\sin\alpha$（沿斜面向下）与 $g\cos\alpha$（垂直斜面向下），两个方向均为匀变速直线运动。

### 1.2 静力学核心概念与力的平衡

1. **受力分析标准四步法（力のつりあいの手順）**
   1. 确定研究对象（着目物体），先画**重力 $mg$**（竖直向下）；
   2. 沿物体轮廓找所有接触点，画出全部**接触力**（支持力、张力、弹力、摩擦力、浮力），**只画受到的力，不画施加给别人的力**；
   3. 设定正交坐标轴（$x$ 轴、$y$ 轴），将不在轴上的力正交分解；
   4. 对单个物体分别列出 $\sum F_x = 0$ 与 $\sum F_y = 0$。

2. **三类摩擦力（摩擦力）**
   - **静摩擦力（静止摩擦力）**：物体相对接触面静止时的摩擦力，**没有固定公式**（绝不可直接套用 $f = \mu N$），必须由平衡条件或牛顿第二定律反推。
   - **最大静摩擦力（最大摩擦力）**：刚要开始滑动瞬间的静摩擦力：
     $$f_{\max} = \mu N \quad (\mu\text{：静止摩擦係数})$$
   - **滑动摩擦力（動摩擦力）**：相对滑动过程中的摩擦力：
     $$f' = \mu' N \quad (\mu'\text{：動摩擦係数})$$

3. **胡克定律与弹簧串并联（フックの法則と合成ばね定数）**
   - **胡克定律**：$F = kx$（$k\text{ [N/m]}$ 为劲度系数/ばね定数，$x\text{ [m]}$ 为相对自然长的伸长或压缩量）。
   - **经典易错点**：轻弹簧两端各挂质量 $m$ 的重物（图 2），弹簧弹力仍为 $mg$ 而非 $2mg$，伸长量与一端固定墙面、另一端挂重物 $m$（图 1）完全相同！
   - **并联合成**：$K_{\text{並}} = k_1 + k_2$（伸长量相同，弹力相加）；
   - **串联合成**：$\dfrac{1}{K_{\text{直}}} = \dfrac{1}{k_1} + \dfrac{1}{k_2}$（弹力相同，伸长量相加）。

4. **压强、水压与浮力（圧力・水圧・浮力）**
   - **压强**：$p = \dfrac{F}{S}$，单位 $\text{Pa} = \text{N/m}^2$。
   - **液体内部压强（水圧）**：仅考虑液体 $p = \rho h g$；计入大气压 $p_0$ 时 $p = p_0 + \rho h g$。
   - **浮力与阿基米德原理（アルキメデスの原理）**：由上下表面压力差推导：
     $$F = \{p_0 + \rho(d+h)g\}S - (p_0 + \rho d g)S = \rho h g S = \rho V g = M_{\text{流}} g$$
     即物体所受浮力等于其排开流体的重力（$V$ 为**浸入流体中的体积**）。

### 1.3 中日物理体系与习惯差异提醒

| 对比维度 | 中国国内高中物理习惯 | 日本 EJU / 高中物理习惯（授课必强调） |
| :--- | :--- | :--- |
| **符号运算 vs 有效数字** | 平时计算常取 $g = 10\text{ m/s}^2$ | EJU 正式考题**极少代入具体数值**，一律保留字母 $g$ 进行纯符号运算；若教材/练习题给出 $g = 9.8$ 或 $9.80$，则**极其严格考核有效数字（有効数字）**，如 `240 m` 必须写成 `2.4 × 10² m`（2 位有效数字）。 |
| **约等号写法** | 使用 $\approx$ | 日本教材与考场一律使用 $\fallingdotseq$（读作 ニアリーイコール）。 |
| **摩擦系数符号** | 统一用 $\mu$ 表示动摩擦因数 | 严格区分：$\mu$ 表示**静摩擦系数（静止摩擦係数）**，$\mu'$（ミューダッシュ）表示**动摩擦系数（動摩擦係数）**。 |
| **支持力符号** | 常用 $F_N$ 或 $N$ | 一律使用 **$N$（垂直抗力）**；若同时存在地面与木板两个支持力，地面支持力常记作 **$R$**。 |
| **速度 vs 速率** | 审题时口语常混用“速度” | 严格区分：**速さ**（速率，标量，只答正值）与 **速度**（速度，矢量，必须说明方向或正负号）。 |
| **坐标正方向约定** | 自由落体默认向下为正 | 日本解答必须显式声明正方向（如「鉛直下向きを正とする」），否则扣规范分。 |

---

## 2. 日文物理核心词汇与公式假名注音（板书必备）

### 2.1 核心物理词汇表

#### 运动学基础
- **物理基礎（ぶつりきそ / butsuri kiso）** — 物理基础（日本高中物理前半册）
- **物体の運動（ぶったいのうんどう / buttai no undō）** — 物体的运动
- **速さ（はやさ / hayasa）** — 速率（标量）
- **速度（そくど / sokudo）** — 速度（矢量）
- **スカラー量（スカラーりょう / sukarā-ryō）** — 标量
- **ベクトル（ベクトル / bekutoru）** — 矢量 / 向量
- **相対速度（そうたいそくど / sōtai sokudo）** — 相对速度
- **等速度運動 / 等速直線運動（とうそくちょくせんうんどう / tōsoku chokusen undō）** — 匀速直线运动
- **等加速度直線運動（とうかそくどちょくせんうんどう / tōkasokudo chokusen undō）** — 匀变速直线运动
- **初速度（しょそくど / shosokudo）** — 初速度
- **加速度（かそくど / kasokudo）** — 加速度
- **変位（へんい / hen'i）** — 位移
- **移動距離（いどうきょり / idō kyori）** — 路程 / 移动距离
- **傾き（かたむき / katamuki）** — 斜率
- **面積（めんせき / menseki）** — 面积
- **重力加速度（じゅうりょくかそくど / jūryoku kasokudo）** — 重力加速度
- **自由落下（じゆうらっか / jiyū rakka）** — 自由落体
- **鉛直投げ下ろし（えんちょくなげおろし / enchoku nageoroshi）** — 竖直下抛
- **鉛直投げ上げ（えんちょくなげあげ / enchoku nageage）** — 竖直上抛
- **放物運動（ほうぶつうんどう / hōbutsu undō）** — 抛体运动
- **水平投射（すいへいとうしゃ / suihei tōsha）** — 平抛运动
- **斜方投射（しゃほうとうしゃ / shahō tōsha）** — 斜抛运动
- **最高点（さいこうてん / saikōten）** — 最高点
- **到達距離（とうたつきょり / tōtatsu kyori）** — 射程 / 到达距离
- **モンキーハンティング（もんきーはんてぃんぐ / monkī hantingu）** — 猴子打枪模型
- **斜面（しゃめん / shamen）** — 斜面

#### 力学与静力学
- **力のつりあい / 力の釣り合い（ちからのつりあい / chikara no tsuriai）** — 力的平衡
- **着目物体（ちゃくもくぶったい / chakumoku buttai）** — 研究对象（注目物体）
- **重力（じゅうりょく / jūryoku）** — 重力
- **接触力（せっしょくりょく / sesshokuryoku）** — 接触力
- **垂直抗力（すいちょくこうりょく / suichoku kōryoku）** — 法向支持力
- **張力（ちょうりょく / chōryoku）** — 拉力 / 张力
- **作用・反作用の法則（さよう・はんさようのほうそく / sayō hansayō no hōsoku）** — 作用力与反作用力定律（牛顿第三定律）
- **定滑車（ていかっしゃ / teikassha）** — 定滑轮
- **動滑車（どうかっしゃ / dōkassha）** — 动滑轮
- **体重計（たいじゅうけい / taijūkei）** — 体重计
- **静止摩擦力（せいしまさつりょく / seishi masatsuryoku）** — 静摩擦力
- **最大摩擦力（さいだいまさつりょく / saidai masatsuryoku）** — 最大静摩擦力
- **動摩擦力（どうまさつりょく / dōmasatsuryoku）** — 滑动摩擦力
- **静止摩擦係数（せいしまさつけいすう / seishi masatsu keisū）** — 静摩擦系数（$\mu$）
- **動摩擦係数（どうまさつけいすう / dōmasatsu keisū）** — 动摩擦系数（$\mu'$）
- **ばねの弾性力（ばねのだんせいりょく / bane no dansei-ryoku）** — 弹簧弹力
- **フックの法則（ふっくのほうそく / fukku no hōsoku）** — 胡克定律
- **自然長（しぜんちょう / shizenchō）** — 自然长度（原长）
- **ばね定数（ばねていすう / bane teisū）** — 劲度系数
- **並列接続（へいれつせつぞく / heiretsu setsuzoku）** — 并联
- **直列接続（ちょくれつせつぞく / chokuretsu setsuzoku）** — 串联
- **合成ばね定数（ごうせいばねていすう / gōsei bane teisū）** — 等效劲度系数
- **圧力（あつりょく / atsuryoku）** — 压强
- **パスカル（ぱすかる / pasukaru）** — 帕斯卡（$\text{Pa}$）
- **水圧（すいあつ / suiatsu）** — 水压
- **大気圧（たいきあつ / taikiatsu）** — 大气压
- **密度（みつど / mitsudo）** — 密度
- **浮力（ふりょく / furyoku）** — 浮力
- **流体（りゅうたい / ryūtai）** — 流体
- **アルキメデスの原理（あるきめですのげんり / arukimedesu no genri）** — 阿基米德原理

### 2.2 核心公式课堂口语读法（板书念法）

| 公式 | 日本课堂标准板书口语读法 |
| :--- | :--- |
| $\vec{v}_{AB} = \vec{v}_B - \vec{v}_A$ | 「ブイ・エービー・ベクトル、イコール、ブイビー・ベクトル、ひく、ブイエー・ベクトル」 |
| $v = v_0 + at$ | 「ブイ・イコール、ブイゼロ、たす、エーティー」 |
| $x = v_0 t + \dfrac{1}{2}at^2$ | 「エックス・イコール、ブイゼロティー、たす、にぶんのいち・エーティーにじょう」 |
| $v^2 - v_0^2 = 2ax$ | 「ブイにじょう、ひく、ブイゼロにじょう、イコール、に・エーエックス」 |
| $f = \mu N$ | 「エフ・イコール、ミュー・エヌ」 |
| $f' = \mu' N$ | 「エフダッシュ・イコール、ミューダッシュ・エヌ」 |
| $F = kx$ | 「エフ・イコール、ケーエックス」 |
| $\dfrac{1}{K_{\text{直}}} = \dfrac{1}{k_1} + \dfrac{1}{k_2}$ | 「ケーちょくぶんのいち、イコール、ケーいちぶんのいち、たす、ケーにぶんのいち」 |
| $p = p_0 + \rho h g$ | 「ピー・イコール、ピーゼロ、たす、ロー・エイチ・ジー」 |
| $F = \rho V g$ | 「エフ・イコール、ロー・ブイ・ジー」 |

---

## 3. 逐题深度解析（一题一解，不可跳步）

---

### 例題 1（教材 P.5 / 页码 4）：自由落下与竖直下抛

#### 【原题重现与翻译】
> **日文原题**：  
> 物体 A をビルの屋上から自由落下させてから $1.0\text{ 秒後}$ に物体 B を投げ下ろしたところ，そのさらに $2.0\text{ 秒後}$ に 2 つの物体が同時に地面に到達した。重力加速度を $9.8\text{ m/s}^2$ として次の問に答えよ。  
> (1) ビルの高さ $h$ を求めよ。  
> (2) 地面到達時の物体 A の速さ $v_A$ を求めよ。  
> (3) 物体 B の初速度の大きさ $v_0$ と地面到達時の速さ $v_B$ を求めよ。
>
> **中文翻译**：  
> 从大楼屋顶让物体 A 自由下落，经过 $1.0\text{ s}$ 后将物体 B 竖直向下抛出，再经过 $2.0\text{ s}$ 后两个物体同时到达地面。取重力加速度为 $9.8\text{ m/s}^2$，回答下列问题：  
> (1) 求大楼的高度 $h$。  
> (2) 求物体 A 到达地面时的速率 $v_A$。  
> (3) 求物体 B 的初速度大小 $v_0$ 及到达地面时的速率 $v_B$。

#### 【考点与模型定位】
**一维竖直落体追及相遇模型**（自由落体 $+$ 竖直下抛，利用时间差与相同位移联立求解）。

#### 【多色矢量图解（SVG）】

<svg viewBox="0 0 420 260" width="420" height="260" xmlns="http://www.w3.org/2000/svg" style="background:#fafafa;border:1px solid #e5e7eb;border-radius:8px;">
  <defs>
    <marker id="arr-blue-1" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0,0 L0,6 L7,3 z" fill="#2563eb"/></marker>
    <marker id="arr-blk-1" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0,0 L0,6 L7,3 z" fill="#111827"/></marker>
  </defs>
  <!-- 屋顶与地面 -->
  <line x1="60" y1="50" x2="310" y2="50" stroke="#4b5563" stroke-width="2"/>
  <text x="20" y="54" font-size="12" fill="#374151">O (屋上)</text>
  <line x1="60" y1="220" x2="310" y2="220" stroke="#4b5563" stroke-width="2.5"/>
  <text x="20" y="224" font-size="12" fill="#374151">h (地面)</text>
  <!-- y 轴 -->
  <line x1="70" y1="30" x2="70" y2="245" stroke="#6b7280" stroke-width="1.5" marker-end="url(#arr-blk-1)"/>
  <text x="52" y="248" font-size="12" font-style="italic" fill="#111827">+y</text>

  <!-- 物体 A (t=0) -->
  <circle cx="140" cy="40" r="10" fill="#dbeafe" stroke="#1e40af" stroke-width="1.5"/>
  <text x="136" y="44" font-size="11" font-weight="bold" fill="#1e3a8a">A</text>
  <text x="115" y="24" font-size="11" fill="#374151">t = 0 (v₀=0)</text>
  <!-- 重力 A -->
  <line x1="140" y1="50" x2="140" y2="95" stroke="#2563eb" stroke-width="2" marker-end="url(#arr-blue-1)"/>
  <text x="108" y="85" font-size="11" fill="#2563eb">m_A g</text>

  <!-- 物体 B (t=1.0) -->
  <circle cx="240" cy="40" r="10" fill="#fef3c7" stroke="#b45309" stroke-width="1.5"/>
  <text x="236" y="44" font-size="11" font-weight="bold" fill="#92400e">B</text>
  <text x="218" y="24" font-size="11" fill="#374151">t = 1.0 s</text>
  <!-- 初速度 v0 虚线 -->
  <line x1="252" y1="45" x2="252" y2="95" stroke="#111827" stroke-width="1.8" stroke-dasharray="5,3" marker-end="url(#arr-blk-1)"/>
  <text x="258" y="80" font-size="11" fill="#111827">v₀</text>
  <!-- 重力 B -->
  <line x1="240" y1="50" x2="240" y2="95" stroke="#2563eb" stroke-width="2" marker-end="url(#arr-blue-1)"/>
  <text x="206" y="85" font-size="11" fill="#2563eb">m_B g</text>

  <!-- 落地瞬间 t=3.0 -->
  <circle cx="140" cy="210" r="10" fill="#dbeafe" stroke="#1e40af" stroke-width="1.5"/>
  <text x="136" y="214" font-size="11" font-weight="bold" fill="#1e3a8a">A</text>
  <line x1="140" y1="220" x2="140" y2="250" stroke="#111827" stroke-width="1.8" stroke-dasharray="5,3" marker-end="url(#arr-blk-1)"/>
  <text x="147" y="245" font-size="11" fill="#111827">v_A</text>

  <circle cx="240" cy="210" r="10" fill="#fef3c7" stroke="#b45309" stroke-width="1.5"/>
  <text x="236" y="214" font-size="11" font-weight="bold" fill="#92400e">B</text>
  <line x1="240" y1="220" x2="240" y2="250" stroke="#111827" stroke-width="1.8" stroke-dasharray="5,3" marker-end="url(#arr-blk-1)"/>
  <text x="247" y="245" font-size="11" fill="#111827">v_B</text>
  <text x="172" y="196" font-size="11" fill="#374151">t = 3.0 s 同時着地</text>

  <!-- 重力加速度方向 -->
  <line x1="350" y1="90" x2="350" y2="155" stroke="#111827" stroke-width="2" stroke-dasharray="5,3" marker-end="url(#arr-blk-1)"/>
  <text x="322" y="82" font-size="11" fill="#111827">g = 9.8 m/s²</text>
  <text x="320" y="185" font-size="10" fill="#2563eb">■ 蓝：重力</text>
  <text x="320" y="200" font-size="10" fill="#111827">--- 黑虚：速度/加速度</text>
</svg>

#### 【日本考场规范分步解答】

铅直下向きを正として座標軸をとる。

> 💡 讲师批注：先明确设定「竖直向下为正方向」，这样自由落体和竖直下抛的位移、速度、加速度全为正数，最不易出符号错误。同时务必理清两个时间：A 下落了 $1.0 + 2.0 = 3.0\text{ s}$，B 下落了 $2.0\text{ s}$。

**(1)** 物体 A が地面に到達するまでにかかる時間は $t_A = 1.0 + 2.0 = 3.0\text{ [s]}$ である。  
自由落下の公式 $y = \dfrac{1}{2}gt^2$ より，
$$h = \frac{1}{2} \times 9.8 \times 3.0^2 = 44.1 \fallingdotseq 44\text{ [m]}$$

> 💡 讲师批注：已知条件 $1.0, 2.0, 9.8$ 均为 **2 位有效数字**，所以最终答案写作 $44\text{ m}$；但切记要把未修约的中间值 **$44.1$** 留着给第 (3) 问用！这是日本物理计算题的铁律（途中計算では 1 桁多く残す）。

**(2)** 自由落下の公式 $v = gt$ より，
$$v_A = 9.8 \times 3.0 = 29.4 \fallingdotseq 29\text{ [m/s]}$$

**(3)** 物体 B の落下時間は $t_B = 2.0\text{ [s]}$ である。  
鉛直投げ下ろしの公式 $y = v_0 t + \dfrac{1}{2}gt^2$ より，
$$44.1 = v_0 \times 2.0 + \frac{1}{2} \times 9.8 \times 2.0^2$$
$$44.1 = 2.0 v_0 + 19.6 \implies 2.0 v_0 = 24.5 \implies v_0 = 12.25 \fallingdotseq 12\text{ [m/s]}$$
また，$v = v_0 + gt$ より，地面到達時の物体 B の速さ $v_B$ は，
$$v_B = 12.25 + 9.8 \times 2.0 = 31.85 \fallingdotseq 32\text{ [m/s]}$$

> 💡 讲师批注：注意教材第 5 页原稿印刷中，最后一行把 `32 m/s` 漏印成了 `32 m`，上课时可顺便提醒学生补全单位 `m/s`！另外计算 $v_B$ 时同样要代入未修约的 $v_0 = 12.25$，若误代 $12$ 会算出 $31.6$，虽恰好也约成 $32$，但在别的题中极易产生舍入误差。

#### 【最终答案】
- **(1) $h = 44\text{ m}$**
- **(2) $v_A = 29\text{ m/s}$**
- **(3) $v_0 = 12\text{ m/s}$，$v_B = 32\text{ m/s}$**

---

### 例題 2（教材 P.6 / 页码 5）：水平投射（平抛运动）

#### 【原题重现与翻译】
> **日文原题**：  
> 地上から $160\text{ m}$ の高さを一定の速さ $42\text{ m/s}$ で飛行する飛行機から静かに物体を投下した。重力加速度を $9.8\text{ m/s}^2$ とする。  
> (1) 物体が地面に到達するまでの時間 $t$ を求めよ。  
> (2) 物体の投下点と着地点の水平距離 $L$ を求めよ。  
> (3) 物体の地面到達時の速さ $v$ を求めよ。  
> (4) 物体の地面到達時の速度と地面のなす角を $\theta$ とするとき，$\tan\theta$ を求めよ。  
> (5) 飛行機から見ると物体はどのような運動をしているように見えるか。
>
> **中文翻译**：  
> 从离地高度 $160\text{ m}$、以恒定速率 $42\text{ m/s}$ 水平飞行的飞机上由静止释放一物体（静かに投下）。重力加速度取 $9.8\text{ m/s}^2$。  
> (1) 求物体到达地面所需时间 $t$。  
> (2) 求投下点与着地点之间的水平距离 $L$。  
> (3) 求物体落地时的速率 $v$。  
> (4) 设物体落地时的速度与地面的夹角为 $\theta$，求 $\tan\theta$。  
> (5) 从飞机上看，物体在做怎样的运动？

#### 【考点与模型定位】
**平抛运动（水平投射）＋ 相对运动视角**（核心在于“静かに投下”＝相对飞机初速为 0，故相对地面具有与飞机相同的水平初速度 $v_0 = 42\text{ m/s}$）。

#### 【多色矢量图解（SVG）】

<svg viewBox="0 0 420 260" width="420" height="260" xmlns="http://www.w3.org/2000/svg" style="background:#fafafa;border:1px solid #e5e7eb;border-radius:8px;">
  <defs>
    <marker id="arr-blue-2" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0,0 L0,6 L7,3 z" fill="#2563eb"/></marker>
    <marker id="arr-blk-2" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0,0 L0,6 L7,3 z" fill="#111827"/></marker>
  </defs>
  <!-- 坐标轴 -->
  <line x1="60" y1="40" x2="360" y2="40" stroke="#6b7280" stroke-width="1.5" marker-end="url(#arr-blk-2)"/>
  <text x="366" y="44" font-size="12" font-style="italic" fill="#111827">x</text>
  <line x1="60" y1="40" x2="60" y2="235" stroke="#6b7280" stroke-width="1.5" marker-end="url(#arr-blk-2)"/>
  <text x="44" y="242" font-size="12" font-style="italic" fill="#111827">y</text>
  <text x="44" y="44" font-size="12" fill="#374151">O</text>

  <!-- 地面 -->
  <line x1="40" y1="190" x2="380" y2="190" stroke="#4b5563" stroke-width="2"/>
  <text x="20" y="194" font-size="11" fill="#374151">160m</text>

  <!-- 抛物线轨迹 -->
  <path d="M 60 40 Q 175 40 260 190" fill="none" stroke="#111827" stroke-width="2"/>

  <!-- 飞机位置标记 -->
  <rect x="130" y="32" width="16" height="8" fill="#e5e7eb" stroke="#374151" stroke-width="1"/>
  <line x1="138" y1="40" x2="138" y2="63" stroke="#9ca3af" stroke-dasharray="3,3"/>
  <circle cx="138" cy="63" r="4" fill="#dbeafe" stroke="#1e40af"/>
  <!-- 重力箭头 -->
  <line x1="138" y1="67" x2="138" y2="107" stroke="#2563eb" stroke-width="2" marker-end="url(#arr-blue-2)"/>
  <text x="144" y="98" font-size="11" fill="#2563eb">mg</text>

  <!-- 初速度 -->
  <line x1="60" y1="40" x2="115" y2="40" stroke="#111827" stroke-width="2" stroke-dasharray="5,3" marker-end="url(#arr-blk-2)"/>
  <text x="68" y="30" font-size="11" fill="#111827">v₀ = 42 m/s</text>

  <!-- 落地速度分解 -->
  <line x1="260" y1="190" x2="315" y2="190" stroke="#111827" stroke-width="1.6" stroke-dasharray="4,3" marker-end="url(#arr-blk-2)"/>
  <text x="285" y="182" font-size="11" fill="#111827">v_x = 42</text>
  <line x1="260" y1="190" x2="260" y2="245" stroke="#111827" stroke-width="1.6" stroke-dasharray="4,3" marker-end="url(#arr-blk-2)"/>
  <text x="210" y="232" font-size="11" fill="#111827">v_y = 56</text>
  <line x1="260" y1="190" x2="315" y2="245" stroke="#111827" stroke-width="2.2" stroke-dasharray="5,3" marker-end="url(#arr-blk-2)"/>
  <text x="318" y="238" font-size="11" font-weight="bold" fill="#111827">v = 70</text>
  <!-- 角度弧线 -->
  <path d="M 285 190 A 25 25 0 0 1 278 208" fill="none" stroke="#dc2626" stroke-width="1.5"/>
  <text x="287" y="206" font-size="11" fill="#dc2626">θ</text>
  <!-- 水平距离标注 -->
  <line x1="260" y1="40" x2="260" y2="190" stroke="#9ca3af" stroke-dasharray="3,3"/>
  <text x="255" y="32" font-size="11" fill="#374151">L</text>
</svg>

#### 【日本考场规范分步解答】

投下点を原点とし，水平右向きに $x$ 軸，鉛直下向きに $y$ 軸をとる。

**(1)** 鉛直方向は自由落下運動であるから，$y = \dfrac{1}{2}gt^2$ より，
$$160 = \frac{1}{2} \times 9.8 \times t^2 \implies t^2 = \frac{160}{4.9} = \frac{1600}{49}$$
$t > 0$ より，
$$t = \frac{40}{7} \fallingdotseq 5.71 \fallingdotseq 5.7\text{ [s]}$$

> 💡 讲师批注：不要急着把 $\frac{40}{7}$ 化成小数 $5.71$！保留分数 $\frac{40}{7}$ 带入下一问，与 $42$、$9.8$ 都能完美约分（$42 = 6 \times 7$，$9.8 = 1.4 \times 7$），这是日本出题人的“隐藏彩蛋”。

**(2)** 水平方向は等速直線運動であるから，
$$L = v_0 t = 42 \times \frac{40}{7} = 240 = 2.4 \times 10^2\text{ [m]}$$

> 💡 讲师批注：国内学生常直接写 $240\text{ m}$，但在日本物理中，$240$ 代表 **3 位有效数字**，而题干中 $42$ 和 $9.8$ 都是 **2 位有效数字**，因此必须写成科学计数法 **$2.4 \times 10^2\text{ m}$**！

**(3)** 地面到達時の水平方向の速さを $v_x$，鉛直方向の速さを $v_y$ とすると，
$$v_x = 42\text{ [m/s]}, \qquad v_y = gt = 9.8 \times \frac{40}{7} = 56\text{ [m/s]}$$
したがって，地面到達時の速さ $v$ は三平方の定理より，
$$v = \sqrt{v_x^2 + v_y^2} = \sqrt{42^2 + 56^2} = 14\sqrt{3^2 + 4^2} = 14 \times 5 = 70\text{ [m/s]}$$

> 💡 讲师批注：提取公因数 $14$ 看出勾股数 $3:4:5$，秒出 $70\text{ m/s}$，避免硬算大数平方。

**(4)** 図より，地面とのなす角 $\theta$ に対して，
$$\tan\theta = \frac{v_y}{v_x} = \frac{56}{42} = \frac{4}{3} \fallingdotseq 1.33 \fallingdotseq 1.3$$

**(5)** 飛行機と物体の水平方向の速度は常に等しい（$v_x - v_{\text{機}} = 42 - 42 = 0$）ため，相対速度は鉛直下向きの成分 $v_y = gt$ のみとなる。  
よって，飛行機から見ると物体は真下に**自由落下運動**をしているように見える。

#### 【最终答案】
- **(1) $t = 5.7\text{ s}$**
- **(2) $L = 2.4 \times 10^2\text{ m}$**
- **(3) $v = 70\text{ m/s}$**
- **(4) $\tan\theta = 1.3$**（分数形式 $\dfrac{4}{3}$）
- **(5) 自由落下運動（自由落体运动）**

---

### 例題 3（教材 P.7 / 页码 6）：斜方投射（斜抛运动）

#### 【原题重现与翻译】
> **日文原题**：  
> 地面と $\theta$ をなす方向に小球を初速度 $v_0$ で投射した。重力加速度を $g$ とする。  
> (1) 小球が最高点に達するまでの時間 $t$ を求めよ。  
> (2) 最高点の高さ $h$ を求めよ。  
> (3) 水平方向の到達距離 $L$ とこれが最大になる $\theta\ (0^\circ < \theta < 90^\circ)$ を求めよ。  
> (4) 地面到達時の速さ $v$ を求めよ。
>
> **中文翻译**：  
> 将一小球以初速度 $v_0$ 沿与地面成 $\theta$ 角的方向斜向上抛出，重力加速度为 $g$。  
> (1) 求小球到达最高点所需的时间 $t$。  
> (2) 求最高点的高度 $h$。  
> (3) 求水平射程 $L$ 及使其最大的抛射角 $\theta\ (0^\circ < \theta < 90^\circ)$。  
> (4) 求小球落回地面时的速率 $v$。

#### 【考点与模型定位】
**平地斜抛运动标准纯符号推导**（EJU 最典型出题风格：全程纯字母运算 + 二倍角公式求极值 + 轨迹对称性）。

#### 【多色矢量图解（SVG）】

<svg viewBox="0 0 420 260" width="420" height="260" xmlns="http://www.w3.org/2000/svg" style="background:#fafafa;border:1px solid #e5e7eb;border-radius:8px;">
  <defs>
    <marker id="arr-blue-3" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0,0 L0,6 L7,3 z" fill="#2563eb"/></marker>
    <marker id="arr-blk-3" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0,0 L0,6 L7,3 z" fill="#111827"/></marker>
  </defs>
  <!-- 坐标轴 -->
  <line x1="40" y1="210" x2="390" y2="210" stroke="#4b5563" stroke-width="2" marker-end="url(#arr-blk-3)"/>
  <text x="394" y="214" font-size="12" font-style="italic" fill="#111827">x</text>
  <line x1="60" y1="225" x2="60" y2="25" stroke="#4b5563" stroke-width="1.5" marker-end="url(#arr-blk-3)"/>
  <text x="45" y="30" font-size="12" font-style="italic" fill="#111827">y</text>
  <text x="44" y="224" font-size="12" fill="#374151">O</text>

  <!-- 抛物线 -->
  <path d="M 60 210 Q 195 -30 330 210" fill="none" stroke="#111827" stroke-width="2"/>

  <!-- 最高点标注 -->
  <line x1="60" y1="90" x2="195" y2="90" stroke="#9ca3af" stroke-dasharray="3,3"/>
  <line x1="195" y1="90" x2="195" y2="210" stroke="#9ca3af" stroke-dasharray="3,3"/>
  <text x="45" y="94" font-size="12" font-style="italic" fill="#374151">h</text>
  <circle cx="195" cy="90" r="5" fill="#dbeafe" stroke="#1e40af"/>
  <!-- 最高点重力与速度 -->
  <line x1="195" y1="95" x2="195" y2="140" stroke="#2563eb" stroke-width="2" marker-end="url(#arr-blue-3)"/>
  <text x="201" y="132" font-size="11" fill="#2563eb">mg</text>
  <line x1="200" y1="90" x2="248" y2="90" stroke="#111827" stroke-width="1.8" stroke-dasharray="5,3" marker-end="url(#arr-blk-3)"/>
  <text x="210" y="80" font-size="11" fill="#111827">v_x = v₀cosθ</text>

  <!-- 初速度与分解 -->
  <line x1="60" y1="210" x2="108" y2="132" stroke="#111827" stroke-width="2" stroke-dasharray="5,3" marker-end="url(#arr-blk-3)"/>
  <text x="68" y="150" font-size="11" font-weight="bold" fill="#111827">v₀</text>
  <line x1="60" y1="210" x2="108" y2="210" stroke="#111827" stroke-width="1.5" stroke-dasharray="4,3" marker-end="url(#arr-blk-3)"/>
  <text x="80" y="226" font-size="10" fill="#111827">v₀cosθ</text>
  <line x1="60" y1="210" x2="60" y2="132" stroke="#111827" stroke-width="1.5" stroke-dasharray="4,3" marker-end="url(#arr-blk-3)"/>
  <text x="8" y="165" font-size="10" fill="#111827">v₀sinθ</text>
  <path d="M 85 210 A 25 25 0 0 0 74 189" fill="none" stroke="#dc2626" stroke-width="1.5"/>
  <text x="88" y="200" font-size="11" fill="#dc2626">θ</text>

  <!-- 落地点 -->
  <text x="325" y="226" font-size="12" font-style="italic" fill="#374151">L</text>
  <line x1="330" y1="210" x2="365" y2="250" stroke="#111827" stroke-width="1.8" stroke-dasharray="5,3" marker-end="url(#arr-blk-3)"/>
  <text x="368" y="248" font-size="11" fill="#111827">v = v₀</text>

  <!-- 重力加速度 -->
  <line x1="360" y1="45" x2="360" y2="95" stroke="#111827" stroke-width="1.8" stroke-dasharray="5,3" marker-end="url(#arr-blk-3)"/>
  <text x="348" y="38" font-size="11" fill="#111827">g</text>
</svg>

#### 【日本考场规范分步解答】

投射点を原点とし，水平方向に $x$ 軸，鉛直上向きに $y$ 軸をとる。初速度の成分は $v_{0x} = v_0\cos\theta$，$v_{0y} = v_0\sin\theta$ である。

**(1)** 最高点では鉛直方向の速度成分 $v_y = 0$ となる。  
鉛直投げ上げの公式 $v_y = v_0\sin\theta - gt$ より，
$$0 = v_0\sin\theta - gt \implies t = \frac{v_0\sin\theta}{g}$$

> 💡 讲师批注：强调“最高点不是速度为 0，而是**竖直分速度 $v_y = 0$**”，此时仍有水平速度 $v_0\cos\theta$。

**(2)** 鉛直方向の公式 $v_y^2 - v_{0y}^2 = 2(-g)y$ より，最高点の高さ $h$ は，
$$0 - v_0^2\sin^2\theta = 2(-g)h \implies h = \frac{v_0^2\sin^2\theta}{2g}$$

**(3)** 運動の対称性より，地面に到達するまでの全時間は $2t$ である。  
水平方向は等速直線運動であるから，到達距離 $L$ は，
$$L = (v_0\cos\theta) \cdot 2t = v_0\cos\theta \cdot \frac{2v_0\sin\theta}{g} = \frac{2v_0^2\sin\theta\cos\theta}{g} = \frac{v_0^2\sin 2\theta}{g}$$
$0^\circ < \theta < 90^\circ$ すなわち $0^\circ < 2\theta < 180^\circ$ の範囲で，$\sin 2\theta = 1$ のとき $L$ は最大となる。  
よって $2\theta = 90^\circ$，すなわち $\theta = 45^\circ$ のとき最大。

> 💡 讲师批注：此处用到三角函数二倍角公式 $2\sin\theta\cos\theta = \sin 2\theta$，是 EJU 物理与数学的经典跨学科高频考点。

**(4)** 最高点までの運動とその後の運動は対称である（または力学的エネルギー保存則より同じ高さで速さは等しい）から，$v = v_0$ である。

#### 【最终答案】
- **(1) $t = \dfrac{v_0\sin\theta}{g}$**
- **(2) $h = \dfrac{v_0^2\sin^2\theta}{2g}$**
- **(3) $L = \dfrac{v_0^2\sin 2\theta}{g}$，最大になる角度 $\theta = 45^\circ$**
- **(4) $v = v_0$**

---

### 例題 4（教材 P.8 / 页码 7）：モンキーハンティング（猴子打枪模型）

#### 【原题重现与翻译】
> **日文原题**：  
> 時刻 $t = 0$ に座標 $(l, h)$ の点から小球 B を自由落下させるのと同時に，原点から小球 A を $x$ 軸と角 $\theta$ をなす方向に速さ $v_0$ で打ち出す。重力加速度を $g$ とする。  
> (1) 小球 A の $x$ 座標が $l$ になるときの時刻 $t$ を求めよ。  
> (2) 時刻 $t$ における小球 A の $y$ 座標 $y_A$ と小球 B の $y$ 座標 $y_B$ を求めよ。  
> (3) 2 つの小球が衝突するときの $\tan\theta$ を $l, h$ で表せ。  
> (4) 小球 B の地面到達前に衝突が起こるために $v_0$ が満たすべき条件を $g, l, h$ で表せ。
>
> **中文翻译**：  
> 在时刻 $t = 0$，从坐标 $(l, h)$ 处让小球 B 自由下落，同时从原点以与 $x$ 轴成 $\theta$ 角的方向、速率 $v_0$ 射出小球 A。重力加速度为 $g$。  
> (1) 求小球 A 的 $x$ 坐标到达 $l$ 时的时刻 $t$。  
> (2) 求时刻 $t$ 时小球 A 的 $y$ 坐标 $y_A$ 与小球 B 的 $y$ 坐标 $y_B$。  
> (3) 用 $l, h$ 表示两小球相撞时的 $\tan\theta$。  
> (4) 用 $g, l, h$ 表示小球 B 落地前发生碰撞时 $v_0$ 必须满足的条件。

#### 【考点与模型定位】
**猴子打枪（モンキーハンティング）经典模型**（EJU 及日本国公立二次试验超频考点：瞄准初始位置直线发射，与初速无关必能击中；并结合三角恒等式 $\frac{1}{\cos^2\theta} = 1 + \tan^2\theta$ 求最小初速条件）。

#### 【多色矢量图解（SVG）】

<svg viewBox="0 0 420 260" width="420" height="260" xmlns="http://www.w3.org/2000/svg" style="background:#fafafa;border:1px solid #e5e7eb;border-radius:8px;">
  <defs>
    <marker id="arr-blue-4" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0,0 L0,6 L7,3 z" fill="#2563eb"/></marker>
    <marker id="arr-blk-4" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0,0 L0,6 L7,3 z" fill="#111827"/></marker>
  </defs>
  <!-- 坐标轴 -->
  <line x1="40" y1="220" x2="360" y2="220" stroke="#4b5563" stroke-width="2" marker-end="url(#arr-blk-4)"/>
  <text x="366" y="224" font-size="12" font-style="italic" fill="#111827">x</text>
  <line x1="60" y1="235" x2="60" y2="25" stroke="#4b5563" stroke-width="1.5" marker-end="url(#arr-blk-4)"/>
  <text x="45" y="30" font-size="12" font-style="italic" fill="#111827">y</text>
  <text x="44" y="234" font-size="12" fill="#374151">O</text>

  <!-- 瞄准虚线 -->
  <line x1="60" y1="220" x2="290" y2="50" stroke="#9ca3af" stroke-width="1.5" stroke-dasharray="5,4"/>
  <!-- 坐标辅助线 -->
  <line x1="60" y1="50" x2="290" y2="50" stroke="#d1d5db" stroke-dasharray="3,3"/>
  <text x="44" y="54" font-size="12" font-style="italic" fill="#374151">h</text>
  <line x1="290" y1="50" x2="290" y2="220" stroke="#374151" stroke-width="1.5"/>
  <text x="287" y="236" font-size="12" font-style="italic" fill="#374151">l</text>

  <!-- B 球初始位置与重力 -->
  <circle cx="290" cy="50" r="6" fill="#fef3c7" stroke="#b45309" stroke-width="1.5"/>
  <text x="300" y="50" font-size="12" font-weight="bold" fill="#92400e">B (l, h)</text>
  <line x1="290" y1="56" x2="290" y2="100" stroke="#2563eb" stroke-width="2" marker-end="url(#arr-blue-4)"/>
  <text x="298" y="92" font-size="11" fill="#2563eb">m_B g</text>

  <!-- A 球抛物线轨迹到碰撞点 -->
  <path d="M 60 220 Q 190 120 290 150" fill="none" stroke="#111827" stroke-width="2"/>
  <circle cx="290" cy="150" r="5" fill="#dc2626"/>
  <text x="300" y="154" font-size="11" font-weight="bold" fill="#dc2626">衝突点 (y_A = y_B &gt; 0)</text>

  <!-- A 球初速度 -->
  <line x1="60" y1="220" x2="118" y2="177" stroke="#111827" stroke-width="2" stroke-dasharray="5,3" marker-end="url(#arr-blk-4)"/>
  <text x="90" y="182" font-size="11" font-weight="bold" fill="#111827">v₀</text>
  <path d="M 92 220 A 32 32 0 0 0 85 201" fill="none" stroke="#dc2626" stroke-width="1.5"/>
  <text x="97" y="213" font-size="11" fill="#dc2626">θ</text>

  <!-- 重力加速度 -->
  <line x1="365" y1="75" x2="365" y2="120" stroke="#111827" stroke-width="1.8" stroke-dasharray="5,3" marker-end="url(#arr-blk-4)"/>
  <text x="355" y="68" font-size="11" fill="#111827">g</text>
</svg>

#### 【日本考场规范分步解答】

**(1)** 小球 A の水平方向（$x$ 軸方向）は等速直線運動であるから，
$$l = (v_0\cos\theta) \cdot t \implies t = \frac{l}{v_0\cos\theta}$$

**(2)** 鉛直上向きを $y$ 軸の正とすると，小球 A は初速度 $v_0\sin\theta$ の鉛直投げ上げ，小球 B は初期位置 $h$ からの自由落下であるから，時刻 $t$ における $y$ 座標はそれぞれ，
$$y_A = v_0\sin\theta \cdot t - \frac{1}{2}gt^2, \qquad y_B = h - \frac{1}{2}gt^2$$

> 💡 讲师批注：提醒学生注意 B 的坐标是 **$h - \frac{1}{2}gt^2$**（因为 $y$ 轴向上为正，从高度 $h$ 往下掉，纵坐标在减小）。

**(3)** 時刻 $t$ において 2 球が衝突する条件は $y_A = y_B$ である。
$$v_0\sin\theta \cdot t - \frac{1}{2}gt^2 = h - \frac{1}{2}gt^2 \implies v_0\sin\theta \cdot t = h$$
これに (1) の $t = \dfrac{l}{v_0\cos\theta}$ を代入すると，
$$v_0\sin\theta \cdot \frac{l}{v_0\cos\theta} = h \implies l\tan\theta = h \implies \tan\theta = \frac{h}{l}$$

> 💡 讲师批注：物理本质非常优雅！两球在相同时间内受重力下落的距离都是 $\frac{1}{2}gt^2$，在等式两边直接消掉！换言之，以 B 为参考系，A 相对 B 做**匀速直线运动**，只要一开始瞄准 B（$\tan\theta = h/l$），无论初速度多大（只要落地前能追上），必然击中！

**(4)** 小球 B が地面（$y = 0$）に到達する前に衝突する条件は，衝突時刻 $t$ において $y_B > 0$ である。
$$y_B = h - \frac{1}{2}gt^2 = h - \frac{gl^2}{2v_0^2\cos^2\theta} > 0$$
これを $v_0^2$ について解くと，
$$v_0^2 > \frac{gl^2}{2h\cos^2\theta}$$
ここで三角関数の公式 $\dfrac{1}{\cos^2\theta} = 1 + \tan^2\theta$ および (3) の $\tan\theta = \dfrac{h}{l}$ を用いると，
$$v_0^2 > \frac{gl^2}{2h}\left(1 + \frac{h^2}{l^2}\right) = \frac{g(l^2 + h^2)}{2h}$$
（$v_0 > 0$ より $v_0 > \sqrt{\dfrac{g(l^2 + h^2)}{2h}}$ としても同値）

> 💡 讲师批注：国内高中生常卡在“怎么把 $\cos^2\theta$ 消掉”这一步！务必在黑板上重点圈出公式 **$\dfrac{1}{\cos^2\theta} = 1 + \tan^2\theta$**，这是 EJU 力学推导的常客。

#### 【最终答案】
- **(1) $t = \dfrac{l}{v_0\cos\theta}$**
- **(2) $y_A = v_0\sin\theta \cdot t - \dfrac{1}{2}gt^2$，$y_B = h - \dfrac{1}{2}gt^2$**
- **(3) $\tan\theta = \dfrac{h}{l}$**
- **(4) $v_0^2 > \dfrac{g(l^2 + h^2)}{2h}$**（或 $v_0 > \sqrt{\dfrac{g(l^2 + h^2)}{2h}}$）

---

### 例題 5（教材 P.9 / 页码 8）：斜面への斜方投射（斜面斜抛）

#### 【原题重现与翻译】
> **日文原题**：  
> 水平面と角 $\alpha$ をなす斜面上の 1 点から，斜面上方で斜面と角 $\theta$ をなす方向に初速 $v_0$ で小球を投射したところ，斜面上のある点に落下した。重力加速度を $g$ とする。  
> (1) 斜面に落下するまでの時間 $t$ を求めよ。  
> (2) 斜面方向の到達距離 $L$ を求めよ。  
> 以下，$\alpha = 30^\circ$ とする。  
> (3) (2) の $L$ が最大になるときの $\theta\ (0^\circ < \theta < 60^\circ)$ を求めよ。  
> (4) 小球が斜面に対して垂直に落下するときの $\tan\theta$ を求めよ。
>
> **中文翻译**：  
> 从与水平面成 $\alpha$ 角的斜面上一点，沿斜面上方与斜面成 $\theta$ 角的方向，以初速度 $v_0$ 抛出小球，小球落在斜面上的某一点。重力加速度为 $g$。  
> (1) 求小球落回斜面所需的时间 $t$。  
> (2) 求沿斜面方向的射程 $L$。  
> 以下取 $\alpha = 30^\circ$：  
> (3) 求使 (2) 中 $L$ 最大的 $\theta\ (0^\circ < \theta < 60^\circ)$。  
> (4) 求小球垂直撞击斜面时的 $\tan\theta$。

#### 【考点与模型定位】
**斜面斜抛运动（坐标轴旋转法）**（将 $g$ 分解到沿斜面与垂直斜面方向，结合积化和差公式求最大射程与垂直撞击条件）。

#### 【多色矢量图解（SVG）】

<svg viewBox="0 0 420 260" width="420" height="260" xmlns="http://www.w3.org/2000/svg" style="background:#fafafa;border:1px solid #e5e7eb;border-radius:8px;">
  <defs>
    <marker id="arr-blue-5" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0,0 L0,6 L7,3 z" fill="#2563eb"/></marker>
    <marker id="arr-blk-5" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0,0 L0,6 L7,3 z" fill="#111827"/></marker>
  </defs>
  <!-- 斜面与水平面 -->
  <line x1="50" y1="225" x2="380" y2="225" stroke="#4b5563" stroke-width="2"/>
  <line x1="50" y1="225" x2="360" y2="85" stroke="#374151" stroke-width="2" marker-end="url(#arr-blk-5)"/>
  <text x="364" y="84" font-size="12" font-style="italic" fill="#111827">x (沿斜面)</text>
  <!-- 垂直斜面 y 轴 -->
  <line x1="50" y1="225" x2="10" y2="136" stroke="#374151" stroke-width="1.5" marker-end="url(#arr-blk-5)"/>
  <text x="14" y="132" font-size="12" font-style="italic" fill="#111827">y</text>
  <text x="38" y="240" font-size="12" fill="#374151">O</text>
  <!-- 倾角 alpha -->
  <path d="M 95 225 A 45 45 0 0 0 91 206" fill="none" stroke="#2563eb" stroke-width="1.5"/>
  <text x="100" y="219" font-size="11" fill="#2563eb">α</text>

  <!-- 抛物线 -->
  <path d="M 50 225 Q 155 15 280 121" fill="none" stroke="#111827" stroke-width="2"/>
  <!-- 初速度与夹角 theta -->
  <line x1="50" y1="225" x2="92" y2="148" stroke="#111827" stroke-width="2" stroke-dasharray="5,3" marker-end="url(#arr-blk-5)"/>
  <text x="72" y="148" font-size="11" font-weight="bold" fill="#111827">v₀</text>
  <path d="M 80 211 A 33 33 0 0 0 68 194" fill="none" stroke="#dc2626" stroke-width="1.5"/>
  <text x="80" y="198" font-size="11" fill="#dc2626">θ</text>

  <!-- 落点 -->
  <circle cx="280" cy="121" r="4.5" fill="#dc2626"/>
  <text x="175" y="185" font-size="12" font-weight="bold" fill="#374151">L</text>
  <!-- 垂直落入示意 -->
  <line x1="280" y1="121" x2="300" y2="165" stroke="#111827" stroke-width="1.8" stroke-dasharray="5,3" marker-end="url(#arr-blk-5)"/>
  <text x="304" y="165" font-size="10" fill="#111827">v_y' (垂直時 v_x'=0)</text>

  <!-- 重力加速度分解小图 -->
  <g transform="translate(260,15)">
    <text x="12" y="10" font-size="10" fill="#2563eb">重力(加速度)分解</text>
    <line x1="40" y1="18" x2="40" y2="68" stroke="#2563eb" stroke-width="2" marker-end="url(#arr-blue-5)"/>
    <text x="27" y="55" font-size="10" fill="#2563eb">g</text>
    <!-- g cos alpha -->
    <line x1="40" y1="18" x2="60" y2="60" stroke="#111827" stroke-width="1.5" stroke-dasharray="4,3" marker-end="url(#arr-blk-5)"/>
    <text x="64" y="52" font-size="10" fill="#111827">g cosα</text>
    <!-- g sin alpha -->
    <line x1="60" y1="60" x2="40" y2="68" stroke="#111827" stroke-width="1.5" stroke-dasharray="4,3" marker-end="url(#arr-blk-5)"/>
    <text x="48" y="78" font-size="10" fill="#111827">g sinα</text>
    <text x="43" y="42" font-size="9" fill="#2563eb">α</text>
  </g>
</svg>

#### 【日本考场规范分步解答】

小球の投射位置を原点とし，斜面上向きに $x$ 軸，斜面に垂直上向きに $y$ 軸をとる。  
このとき，初速度および加速度の各成分は，
$$v_{0x} = v_0\cos\theta, \quad v_{0y} = v_0\sin\theta, \qquad a_x = -g\sin\alpha, \quad a_y = -g\cos\alpha$$

> 💡 讲师批注：斜面斜抛如果死守水平/竖直建系，需要联立抛物线方程与斜面直线 $y = x\tan\alpha$，非常繁琐；**旋转坐标系沿斜面建系**后，落回斜面的条件瞬间简化为 **$y = 0$**，一步秒杀！

**(1)** 斜面に落下する条件は $y = 0$ である。$y$ 軸方向の変位の式より，
$$y = v_0\sin\theta \cdot t - \frac{1}{2}g\cos\alpha \cdot t^2 = \frac{1}{2}t(2v_0\sin\theta - g\cos\alpha \cdot t) = 0$$
$t > 0$ より，
$$t = \frac{2v_0\sin\theta}{g\cos\alpha}$$

**(2)** $x$ 軸方向の変位が到達距離 $L$ であるから，
$$L = v_0\cos\theta \cdot t - \frac{1}{2}g\sin\alpha \cdot t^2$$
(1) の $t$ を代入して整理すると，
$$L = v_0\cos\theta \cdot \frac{2v_0\sin\theta}{g\cos\alpha} - \frac{1}{2}g\sin\alpha \cdot \frac{4v_0^2\sin^2\theta}{g^2\cos^2\alpha}$$
$$= \frac{2v_0^2\sin\theta}{g\cos^2\alpha}(\cos\alpha\cos\theta - \sin\alpha\sin\theta) = \frac{2v_0^2\sin\theta\cos(\alpha + \theta)}{g\cos^2\alpha}$$
さらに積和の公式 $2\sin A\cos B = \sin(A+B) + \sin(A-B)$ を用いると，
$$L = \frac{v_0^2\{\sin(2\theta + \alpha) - \sin\alpha\}}{g\cos^2\alpha}$$

> 💡 讲师批注：这一步连续用了两个三角公式：① 和角余弦 $\cos\alpha\cos\theta - \sin\alpha\sin\theta = \cos(\alpha+\theta)$；② 积化和差 $2\sin\theta\cos(\alpha+\theta) = \sin(2\theta+\alpha) + \sin(-\alpha) = \sin(2\theta+\alpha) - \sin\alpha$。因为 $\alpha$ 是常数，化成单一三角函数 $\sin(2\theta+\alpha)$ 后，最大值一眼可见！

**(3)** $\alpha = 30^\circ$ のとき，$0^\circ < \theta < 60^\circ$ すなわち $30^\circ < 2\theta + 30^\circ < 150^\circ$ において，$L$ が最大になる条件は，
$$\sin(2\theta + 30^\circ) = 1 \implies 2\theta + 30^\circ = 90^\circ \implies \theta = 30^\circ$$

**(4)** 小球が斜面に対して垂直に落下するとき，落下瞬間の斜面方向（$x$ 軸方向）の速度成分 $v_x'$ が $0$ となる。
$$v_x' = v_0\cos\theta - g\sin 30^\circ \cdot t = 0$$
$\alpha = 30^\circ$ のとき $t = \dfrac{2v_0\sin\theta}{g\cos 30^\circ} = \dfrac{4v_0\sin\theta}{\sqrt{3}g}$ であり，$\sin 30^\circ = \dfrac{1}{2}$ であるから，
$$v_0\cos\theta - \frac{1}{2}g \cdot \frac{4v_0\sin\theta}{\sqrt{3}g} = 0 \implies \cos\theta - \frac{2}{\sqrt{3}}\sin\theta = 0$$
よって，
$$\tan\theta = \frac{\sqrt{3}}{2}$$

> 💡 讲师批注：“垂直落到斜面上”的数学翻译就是**沿斜面方向速度分量 $v_x' = 0$**，这就是旋转坐标系带来的降维打击优势！

#### 【最终答案】
- **(1) $t = \dfrac{2v_0\sin\theta}{g\cos\alpha}$**
- **(2) $L = \dfrac{v_0^2\{\sin(2\theta + \alpha) - \sin\alpha\}}{g\cos^2\alpha}$**
- **(3) $\theta = 30^\circ$**
- **(4) $\tan\theta = \dfrac{\sqrt{3}}{2}$**

---

### 例題 6（教材 P.11–12 / 页码 10–11）：滑車と板と板上の人の釣り合い（滑轮、木板与人的平衡）

#### 【原题重现与翻译】
> **日文原题**：  
> 図 1 のように，$10.0\text{ kg}$ の板に乗った $60.0\text{ kg}$ の人が定滑車にかけたひもの一端を引っ張って静止している。ひもの質量およびひもと滑車の間の摩擦は無視できるものとし，重力加速度を $9.80\text{ m/s}^2$ とする。  
> (1) どれだけの力でひもを引けば板が地面から離れるか。  
> (2) 図 2 のように板上に $2.00\text{ kg}$ の体重計を置いたとき，どれだけの力でひもを引けば板が地面から離れるか。また，そのとき体重計は何 $\text{kg}$ を示すか。  
> (3) 図 3 のように $5.00\text{ kg}$ の動滑車にもひもをかけたとき，どれだけの力でひもを引けば板が地面から離れるか。
>
> **中文翻译**：  
> 如图 1 所示，质量 $60.0\text{ kg}$ 的人站在质量 $10.0\text{ kg}$ 的木板上，拉着绕过定滑轮的绳子一端保持静止。忽略绳的质量以及绳与滑轮间的摩擦，取重力加速度为 $9.80\text{ m/s}^2$。  
> (1) 用多大的力拉绳子，木板恰好离开地面？  
> (2) 如图 2 所示，在木板上放置质量为 $2.00\text{ kg}$ 的体重计，用多大的力拉绳子木板恰好离开地面？此时体重计的示数是多少 $\text{kg}$？  
> (3) 如图 3 所示，再绕过一个质量为 $5.00\text{ kg}$ 的动滑轮，用多大的力拉绳子木板恰好离开地面？

#### 【考点与模型定位】
**多物体连接体静力学平衡模型（人-板-滑轮系统）**（重点训练“隔离法受力分析”、作用力与反作用力 $N$、临界脱离条件 $R = 0$ 以及动滑轮自身重力的处理）。

#### 【多色矢量图解（SVG）】

<svg viewBox="0 0 420 260" width="420" height="260" xmlns="http://www.w3.org/2000/svg" style="background:#fafafa;border:1px solid #e5e7eb;border-radius:8px;">
  <defs>
    <marker id="arr-blue-6" markerWidth="7" markerHeight="7" refX="5" refY="3" orient="auto"><path d="M0,0 L0,6 L6,3 z" fill="#2563eb"/></marker>
    <marker id="arr-grn-6" markerWidth="7" markerHeight="7" refX="5" refY="3" orient="auto"><path d="M0,0 L0,6 L6,3 z" fill="#16a34a"/></marker>
  </defs>
  <!-- 天花板 -->
  <line x1="20" y1="20" x2="400" y2="20" stroke="#374151" stroke-width="2.5"/>

  <!-- === 左侧：图 1 受力图 === -->
  <text x="58" y="250" font-size="11" font-weight="bold" fill="#374151">図1（定滑車）</text>
  <line x1="100" y1="20" x2="100" y2="48" stroke="#374151" stroke-width="2"/>
  <circle cx="100" cy="48" r="16" fill="#fff" stroke="#374151" stroke-width="1.8"/>
  <!-- 绳子 -->
  <line x1="84" y1="48" x2="84" y2="165" stroke="#4b5563" stroke-width="1.5"/>
  <line x1="116" y1="48" x2="116" y2="95" stroke="#4b5563" stroke-width="1.5"/>
  <line x1="116" y1="95" x2="65" y2="205" stroke="#4b5563" stroke-width="1.3"/>
  <line x1="116" y1="95" x2="165" y2="205" stroke="#4b5563" stroke-width="1.3"/>
  <!-- 地面与木板 -->
  <line x1="40" y1="218" x2="185" y2="218" stroke="#374151" stroke-width="2"/>
  <rect x="65" y="205" width="100" height="13" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>
  <!-- 人简笔画 -->
  <circle cx="115" cy="145" r="8" fill="#fff" stroke="#374151" stroke-width="1.5"/>
  <line x1="115" y1="153" x2="115" y2="185" stroke="#374151" stroke-width="1.8"/>
  <line x1="115" y1="163" x2="84" y2="155" stroke="#374151" stroke-width="1.5"/>
  <line x1="115" y1="185" x2="105" y2="205" stroke="#374151" stroke-width="1.5"/>
  <line x1="115" y1="185" x2="125" y2="205" stroke="#374151" stroke-width="1.5"/>

  <!-- 图 1 绿色张力与支持力 -->
  <line x1="84" y1="152" x2="84" y2="115" stroke="#16a34a" stroke-width="2" marker-end="url(#arr-grn-6)"/>
  <text x="68" y="130" font-size="11" font-weight="bold" fill="#16a34a">T</text>
  <line x1="116" y1="95" x2="116" y2="62" stroke="#16a34a" stroke-width="2" marker-end="url(#arr-grn-6)"/>
  <text x="122" y="80" font-size="11" font-weight="bold" fill="#16a34a">T</text>
  <line x1="128" y1="205" x2="128" y2="170" stroke="#16a34a" stroke-width="2" marker-end="url(#arr-grn-6)"/>
  <text x="132" y="182" font-size="11" font-weight="bold" fill="#16a34a">N</text>
  <line x1="152" y1="218" x2="152" y2="188" stroke="#16a34a" stroke-width="1.8" marker-end="url(#arr-grn-6)"/>
  <text x="157" y="198" font-size="10" fill="#16a34a">R→0</text>
  <!-- 图 1 蓝色重力 -->
  <line x1="102" y1="175" x2="102" y2="232" stroke="#2563eb" stroke-width="2" marker-end="url(#arr-blue-6)"/>
  <text x="46" y="234" font-size="10" fill="#2563eb">60g</text>
  <line x1="142" y1="212" x2="142" y2="236" stroke="#2563eb" stroke-width="1.8" marker-end="url(#arr-blue-6)"/>
  <text x="148" y="236" font-size="10" fill="#2563eb">10g</text>

  <!-- === 右侧：图 3 动滑轮受力图 === -->
  <text x="270" y="250" font-size="11" font-weight="bold" fill="#374151">図3（動滑車 5.00kg）</text>
  <line x1="305" y1="20" x2="305" y2="48" stroke="#374151" stroke-width="2"/>
  <circle cx="305" cy="48" r="16" fill="#fff" stroke="#374151" stroke-width="1.8"/>
  <!-- 动滑轮 -->
  <circle cx="321" cy="92" r="12" fill="#fef3c7" stroke="#b45309" stroke-width="1.6"/>
  <!-- 绳子 -->
  <line x1="289" y1="48" x2="289" y2="165" stroke="#4b5563" stroke-width="1.5"/>
  <line x1="321" y1="48" x2="321" y2="80" stroke="#4b5563" stroke-width="1.5"/>
  <line x1="333" y1="20" x2="333" y2="92" stroke="#4b5563" stroke-width="1.5"/>
  <line x1="321" y1="104" x2="321" y2="132" stroke="#4b5563" stroke-width="1.5"/>
  <line x1="321" y1="132" x2="270" y2="205" stroke="#4b5563" stroke-width="1.3"/>
  <line x1="321" y1="132" x2="370" y2="205" stroke="#4b5563" stroke-width="1.3"/>
  <!-- 地面与木板 -->
  <line x1="245" y1="218" x2="395" y2="218" stroke="#374151" stroke-width="2"/>
  <rect x="270" y="205" width="100" height="13" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>
  <!-- 人 -->
  <circle cx="320" cy="155" r="7" fill="#fff" stroke="#374151" stroke-width="1.5"/>
  <line x1="320" y1="162" x2="320" y2="188" stroke="#374151" stroke-width="1.8"/>
  <line x1="320" y1="170" x2="289" y2="162" stroke="#374151" stroke-width="1.5"/>
  <line x1="320" y1="188" x2="310" y2="205" stroke="#374151" stroke-width="1.5"/>
  <line x1="320" y1="188" x2="330" y2="205" stroke="#374151" stroke-width="1.5"/>

  <!-- 图 3 受力箭头 -->
  <line x1="289" y1="158" x2="289" y2="124" stroke="#16a34a" stroke-width="2" marker-end="url(#arr-grn-6)"/>
  <text x="274" y="138" font-size="11" font-weight="bold" fill="#16a34a">T</text>
  <line x1="309" y1="92" x2="309" y2="62" stroke="#16a34a" stroke-width="1.8" marker-end="url(#arr-grn-6)"/>
  <text x="295" y="75" font-size="10" fill="#16a34a">T</text>
  <line x1="333" y1="92" x2="333" y2="62" stroke="#16a34a" stroke-width="1.8" marker-end="url(#arr-grn-6)"/>
  <text x="338" y="75" font-size="10" fill="#16a34a">T</text>
  <!-- 动滑轮重力与S -->
  <line x1="321" y1="104" x2="321" y2="126" stroke="#2563eb" stroke-width="1.8" marker-end="url(#arr-blue-6)"/>
  <text x="338" y="114" font-size="10" fill="#2563eb">5g + S</text>
  <line x1="314" y1="132" x2="314" y2="108" stroke="#16a34a" stroke-width="1.8" marker-end="url(#arr-grn-6)"/>
  <text x="300" y="122" font-size="10" fill="#16a34a">S</text>
  <!-- 图例 -->
  <text x="192" y="42" font-size="10" fill="#2563eb">■ 蓝：重力</text>
  <text x="192" y="56" font-size="10" fill="#16a34a">■ 绿：张力/支持力</text>
</svg>

#### 【日本考场规范分步解答】

**(1)** ひもの張力を $T$，人が板から受ける垂直抗力を $N$，板が地面から受ける垂直抗力を $R$ とする。  
- 人が受ける力のつりあいより：
  $$T + N = 60.0 \times 9.80 \quad \cdots\text{①}$$
- 板が受ける力のつりあいより（人から下向きの反作用 $N$ を受ける）：
  $$T + R = N + 10.0 \times 9.80 \quad \cdots\text{②}$$

① $+$ ② より $N$ を消去すると，$2T + R = 70.0 \times 9.80$。  
板が地面から離れる条件は $R = 0$ であるから，
$$2T = 70.0 \times 9.80 \implies T = 35.0 \times 9.80 = 343\text{ [N]}$$

> 💡 讲师批注：本题也可将“人＋板”视为整体！整体受两根向上绳子拉力 $2T$、地面支持力 $R$、总重力 $70.0g$，瞬间写出 $2T + R = 70.0g$。但**必须同时教学生隔离法**，因为第 (2) 问求体重计示数必须求出内力 $N$！

**(2)** 板と体重計を一体（質量 $10.0 + 2.00 = 12.0\text{ kg}$）とみなし，人が「板＋体重計」から受ける垂直抗力を $N$，「板＋体重計」が地面から受ける垂直抗力を $R$ とする。  
- 人が受ける力のつりあいより：
  $$T + N = 60.0 \times 9.80$$
- 「板＋体重計」が受ける力のつりあいより：
  $$T + R = N + 12.0 \times 9.80$$

地面から離れる条件 $R = 0$ を代入し，2 式を足し合わせると，
$$2T = 72.0 \times 9.80 \implies T = 36.0 \times 9.80 = 352.8 \fallingdotseq 353\text{ [N]}$$
これを人のつりあいの式に代入すると，
$$N = (60.0 - 36.0) \times 9.80 = 24.0 \times 9.80\text{ [N]}$$
体重計は人が体重計を押す力 $N$ を質量に換算した値 $\dfrac{N}{g}$ を示すから，
$$\frac{N}{9.80} = 24.0\text{ [kg]}$$

> 💡 讲师批注：高频陷阱提醒！体重计测的**不是人的重力 $60\text{ kg}$**，而是人对体重计的压力（大小等于支持力 $N$），再除以 $g$ 换算成 $\text{kg}$！另外注意 $60.0, 10.0, 2.00, 9.80$ 均为 **3 位有效数字**，故 $352.8 \fallingdotseq 353\text{ N}$，$24.0\text{ kg}$ 的 `.0` 不可省略。

**(3)** 人と滑車の間のひもの張力を $T$，板と動滑車の間のひもの張力を $S$ とする。  
- 人が受ける力のつりあいより：
  $$T + N = 60.0 \times 9.80 \quad \cdots\text{①}$$
- 板が受ける力のつりあいより：
  $$S + R = N + 10.0 \times 9.80 \quad \cdots\text{②}$$
- 動滑車が受ける力のつりあいより（上向きに $2T$，下向きに $S$ と自身の重力）：
  $$2T = S + 5.00 \times 9.80 \quad \cdots\text{③}$$

① $+$ ② $+$ ③ より $N$ と $S$ を消去すると，
$$3T + R = (60.0 + 10.0 + 5.00) \times 9.80 = 75.0 \times 9.80$$
地面から離れる条件は $R = 0$ であるから，
$$T = 25.0 \times 9.80 = 245\text{ [N]}$$

> 💡 讲师批注：切记动滑轮有质量 $5.00\text{ kg}$，所以不能直接说 $S = 2T$，而是 **$2T = S + 5.00g$**！若将“人＋板＋动滑轮”看作整体，共有 3 股绳向上拉（总拉力 $3T$），总质量 $75.0\text{ kg}$，直接 $3T = 75.0g \implies T = 245\text{ N}$，秒算验算！

#### 【最终答案】
- **(1) $343\text{ N}$**
- **(2) 張力 $353\text{ N}$，体重計の示度 $24.0\text{ kg}$**
- **(3) $245\text{ N}$**

---

### 核心模型图解补充（教材 P.13–15 概念页板书素材）

为方便纯日文板书授课，将切片末尾三页核心概念（摩擦力、弹簧易错双图、阿基米德浮力推导）也配齐标准多色 SVG 图解：

#### 补充图 A：水平面摩擦力受力图（P.13） & 弹簧易错构图（P.14）

<svg viewBox="0 0 420 220" width="420" height="220" xmlns="http://www.w3.org/2000/svg" style="background:#fafafa;border:1px solid #e5e7eb;border-radius:8px;">
  <defs>
    <marker id="arr-b-s" markerWidth="7" markerHeight="7" refX="5" refY="3" orient="auto"><path d="M0,0 L0,6 L6,3 z" fill="#2563eb"/></marker>
    <marker id="arr-g-s" markerWidth="7" markerHeight="7" refX="5" refY="3" orient="auto"><path d="M0,0 L0,6 L6,3 z" fill="#16a34a"/></marker>
    <marker id="arr-r-s" markerWidth="7" markerHeight="7" refX="5" refY="3" orient="auto"><path d="M0,0 L0,6 L6,3 z" fill="#dc2626"/></marker>
  </defs>
  <!-- 左半：摩擦力 -->
  <text x="48" y="22" font-size="11" font-weight="bold" fill="#374151">静止/動摩擦力の図示</text>
  <line x1="20" y1="135" x2="195" y2="135" stroke="#374151" stroke-width="2"/>
  <rect x="78" y="85" width="54" height="50" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>
  <!-- 重力 -->
  <line x1="105" y1="110" x2="105" y2="180" stroke="#2563eb" stroke-width="2" marker-end="url(#arr-b-s)"/>
  <text x="111" y="176" font-size="11" fill="#2563eb">mg</text>
  <!-- 支持力 -->
  <line x1="105" y1="135" x2="105" y2="42" stroke="#16a34a" stroke-width="2" marker-end="url(#arr-g-s)"/>
  <text x="112" y="54" font-size="11" fill="#16a34a">N</text>
  <!-- 外力与摩擦力 -->
  <line x1="132" y1="110" x2="185" y2="110" stroke="#dc2626" stroke-width="2" marker-end="url(#arr-r-s)"/>
  <text x="168" y="102" font-size="11" fill="#dc2626">F</text>
  <line x1="78" y1="133" x2="28" y2="133" stroke="#dc2626" stroke-width="2" marker-end="url(#arr-r-s)"/>
  <text x="36" y="124" font-size="11" fill="#dc2626">f (or f')</text>

  <!-- 分隔线 -->
  <line x1="210" y1="15" x2="210" y2="205" stroke="#d1d5db" stroke-dasharray="4,4"/>

  <!-- 右半：弹簧两端挂重物 -->
  <text x="232" y="22" font-size="11" font-weight="bold" fill="#374151">ばねの伸び（両端 mg → 伸び x）</text>
  <!-- 桌面与滑轮 -->
  <polyline points="245,170 245,80 385,80 385,170" fill="none" stroke="#374151" stroke-width="1.8"/>
  <circle cx="245" cy="80" r="8" fill="#fff" stroke="#374151" stroke-width="1.5"/>
  <circle cx="385" cy="80" r="8" fill="#fff" stroke="#374151" stroke-width="1.5"/>
  <!-- 弹簧锯齿 -->
  <path d="M 245 72 L 275 72 L 281 64 L 289 80 L 297 64 L 305 80 L 313 64 L 321 80 L 329 64 L 337 80 L 345 72 L 385 72" fill="none" stroke="#16a34a" stroke-width="1.8"/>
  <text x="285" y="54" font-size="10" fill="#16a34a">弾性力 kx = mg</text>
  <!-- 左右重物 -->
  <line x1="237" y1="80" x2="237" y2="120" stroke="#4b5563" stroke-width="1.5"/>
  <rect x="227" y="120" width="20" height="28" fill="#dbeafe" stroke="#1e40af"/>
  <line x1="237" y1="148" x2="237" y2="185" stroke="#2563eb" stroke-width="2" marker-end="url(#arr-b-s)"/>
  <text x="215" y="182" font-size="10" fill="#2563eb">mg</text>
  <line x1="237" y1="120" x2="237" y2="94" stroke="#16a34a" stroke-width="1.8" marker-end="url(#arr-g-s)"/>

  <line x1="393" y1="80" x2="393" y2="120" stroke="#4b5563" stroke-width="1.5"/>
  <rect x="383" y="120" width="20" height="28" fill="#dbeafe" stroke="#1e40af"/>
  <line x1="393" y1="148" x2="393" y2="185" stroke="#2563eb" stroke-width="2" marker-end="url(#arr-b-s)"/>
  <text x="398" y="182" font-size="10" fill="#2563eb">mg</text>
  <line x1="393" y1="120" x2="393" y2="94" stroke="#16a34a" stroke-width="1.8" marker-end="url(#arr-g-s)"/>
  <text x="242" y="205" font-size="10" fill="#dc2626">※ 2mg ではない！片側固定と全く同じ伸び</text>
</svg>

---

## 4. 全局术语表同步说明

本切片新增的 **52 条** 日文物理核心术语与假名注音已去重同步写入全局术语表：[glossary_all.md](file:///Users/baohan/Desktop/EJU/notes_物理/glossary_all.md)。
