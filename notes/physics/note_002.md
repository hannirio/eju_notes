# EJU 物理全解讲义 — 切片 002（P.16–P.30）
> **对应教材章节**：物理基礎・第一章 物体の運動（力のモーメント、剛体のつりあい、重心、運動方程式、空気抵抗、仕事と仕事率、力学的エネルギー保存則、運動量と力積・衝突）  
> **适用对象**：需快速唤醒中国高中物理基础、并掌握纯日文板书与 EJU 考场规范表达的授课教师 / 考生

---

## 1. 本节前置：国内高中物理基础唤醒

本切片打通了整个经典力学的四大支柱：**刚体静力学（力矩与重心）**、**动力学（牛顿第二定律）**、**能量观点（功与机械能）**、**动量观点（动量与碰撞）**。其中“刚体力矩与倾倒条件”在中国新课标高中物理中属于弱化/竞赛内容，但在日本 EJU 中属于**必考高频核心模块**，授课需重点展开。

### 1.1 刚体与力矩（剛体と力のモーメント）

1. **质点与刚体**
   - **质点（質点）**：只有质量、不计大小与形状的理想点，只考虑平动（位置移动）。
   - **刚体（剛体）**：具有一定大小和形状，且在受力时**不发生形变**的理想物体，需同时考虑**平动**与**转动（回転運動）**。

2. **力矩（力のモーメント）**
   衡量力使刚体绕转轴转动本领的物理量。设转轴 $O$ 到力 $F$ 的**作用线（作用線）**的垂直距离（**力臂 / 腕の長さ**）为 $l$：
   $$M = Fl \quad \text{（单位：}\text{N}\cdot\text{m}\text{）}$$
   - **两种等效求法**：① 找力臂 $l = r\sin\theta$，算 $F \cdot (r\sin\theta)$；② 将力分解为垂直于杆的分力 $F_\perp = F\sin\theta$，算 $(F\sin\theta) \cdot r$。
   - **方向规定**：通常规定**逆时针（反時計回り）为正**，**顺时针（時計回り）为负**。

3. **刚体平衡的充要条件（剛体のつりあい条件）**
   1. **合外力为零**（不平动）：$\sum F_x = 0,\quad \sum F_y = 0$；
   2. **任意转轴的合力矩为零**（不转动）：$\sum M = 0$（即顺时针力矩之和 $=$ 逆时针力矩之和）。
   - **选轴黄金技巧**：优先选择**未知力最多（如墙角、地面接触点、铰链）**的点作为转轴，直接令未知力力臂为 $0$ 消元！
   - **三力汇交原理**：若刚体在三个非平行共面力作用下平衡，则这**三个力的作用线必交于同一点**。

4. **重心（重心）**
   - 物体各部分重力的合力作用点，绕重心的重力矩之和为 $0$。
   - **两物体重心**：位于两物体连线上，按**质量的逆比内分**（即 $m_1 l_1 = m_2 l_2$）。
   - **重心通用坐标公式**：质量 $m_1, m_2, \dots$ 位于坐标 $x_1, x_2, \dots$ 时：
     $$x_G = \frac{m_1 x_1 + m_2 x_2 + m_3 x_3 + \cdots}{m_1 + m_2 + m_3 + \cdots}$$

### 1.2 牛顿第二定律与运动方程（運動方程式）

1. **牛顿第二定律**：
   $$m\vec{a} = \vec{F} \quad \text{（加速度方向与合外力方向永远一致）}$$
2. **连接体与运动方程标准五步法（解答手順）**：
   1. 确定研究对象（着目物体），画出全部重力与接触力；
   2. 对**每个物体分别设定 $x, y$ 轴**（将**运动方向设为 $+x$ 方向**）并假定加速度 $a$；
   3. 正交分解所有不在坐标轴上的力；
   4. 分轴立式：静止/匀速用 $\sum F = 0$，加速用 $ma = F_{\text{合}}$；
   5. 若求位移、速度、时间，再联立匀变速直线运动三大公式。
3. **空气阻力与终端速度（終端速度）**：
   下落受阻力 $f = kv$ 时，$ma = mg - kv \implies a = g - \frac{k}{m}v$。随 $v$ 增大，$a$ 减小；当 $a = 0$（即 $mg = kv_f$）时达到恒定的**终端速度（終端速度）** $v_f = \dfrac{mg}{k}$。

### 1.3 功、功率与功能关系（仕事・仕事率・力学的エネルギー）

1. **功（仕事）**：恒力 $F$ 使物体沿力方向移动距离 $x$（或与位移夹角 $\theta$）：
   $$W = Fx \quad \text{（一般形式：} W = Fx\cos\theta\text{，单位：}\text{J} = \text{N}\cdot\text{m}\text{）}$$
   - **功的原理（仕事の原理）**：使用简单机械（杠杆、滑轮、斜面等）不省功。
2. **功率（仕事率）**：单位时间做的功（单位：$\text{W} = \text{J/s}$）：
   $$P = \frac{W}{t} = \frac{Fx}{t} = Fv$$
3. **三种机械能（力学的エネルギー）**：
   - **动能（運動エネルギー）**：$K = \dfrac{1}{2}mv^2$
   - **重力势能（重力による位置エネルギー）**：$U_g = mgh$
   - **弹性势能（ばねの弾性力による位置エネルギー）**：$U_e = \dfrac{1}{2}kx^2$
4. **保守力与机械能守恒**：
   - **保守力（保存力）**：做功与路径无关、只取决于初末位置的力。高中物理仅 4 种：**重力、万有引力、弹簧弹力、静电力**。
   - **机械能守恒定律**：只有保守力做功（非保守力不做功）时，$K_{\text{始}} + U_{\text{始}} = K_{\text{終}} + U_{\text{終}}$。
   - **功能关系（仕事とエネルギーの関係）**：存在摩擦力或外力等**非保守力（非保存力）**做功时：
     $$(\text{初机械能}) + (\text{非保守力/外力做的功}) = (\text{末机械能})$$
     即 $(K_{\text{始}} + U_{\text{始}}) + W_{\text{非保存}} = K_{\text{終}} + U_{\text{終}}$。

### 1.4 动量、冲量与碰撞（運動量・力積・衝突）

1. **动量与冲量**：
   - **动量（運動量）**：$\vec{p} = m\vec{v}$（矢量，单位 $\text{kg}\cdot\text{m/s}$）。
   - **冲量（力積）**：$\vec{I} = \vec{F}\Delta t$（矢量，单位 $\text{N}\cdot\text{s}$）。
   - **动量定理（運動量と力積の関係）**：$m\vec{v}' - m\vec{v} = \vec{F}\Delta t$。
2. **动量守恒定律（運動量保存則）**：系统不受外力冲量（或某方向合外力为 $0$）时，系统总动量（或该方向分动量）守恒：
   $$m_1\vec{v}_1 + m_2\vec{v}_2 = m_1\vec{v}_1' + m_2\vec{v}_2'$$
3. **恢复系数（反発係数 $e$）**：两球沿连心线碰前速度 $v_1, v_2$，碰后速度 $v_1', v_2'$：
   $$e = -\frac{v_1' - v_2'}{v_1 - v_2} \quad (0 \le e \le 1)$$
   - $e = 1$：**（完全）弹性碰撞（弾性衝突）**，机械能守恒；
   - $0 \le e < 1$：**非弹性碰撞（非弾性衝突）**，机械能减少；
   - $e = 0$：**完全非弹性碰撞（完全非弾性衝突）**，碰后两物体共速合体。

### 1.5 中日物理体系与习惯差异提醒

| 对比维度 | 中国国内高中物理习惯 | 日本 EJU / 高中物理习惯（授课必强调） |
| :--- | :--- | :--- |
| **牛顿第二定律写法** | 习惯写 $F = ma$（力在左） | 日本物理教材与考场一律写 **$ma = F$**（加速度项在左，受力项在右）。 |
| **动能与势能符号** | 动能 $E_k$、势能 $E_p$ | 动能一律用 **$K$**，势能一律用 **$U$**，功用 $W$，机械能常用 $E = K + U$。 |
| **静/动摩擦系数符号** | 常统一写 $\mu$ | 日本不同教材存在两套记法：① $(\mu, \mu')$（本教材 P.13）；② $(\mu_0, \mu)$（本教材 P.17–28）。**务必以题干给定符号为准**，切勿惯性代错！ |
| **“抗力”的含义** | 国内常把支持力称为“反力/支持力” | 日本区分 **垂直抗力（法向支持力 $N$）** 与 **抗力（$R = \vec{N} + \vec{f}$，即接触面施加的法向支持力与摩擦力的合力）**！ |
| **碰撞与恢复系数 $e$** | 选修教材一带而过，较少考 $e$ | EJU **必考核心公式** $e = -\dfrac{v_1' - v_2'}{v_1 - v_2}$，且二维斜碰高频考查等质量弹性碰撞的 $90^\circ$ 垂直结论。 |
| **不等号写法** | 使用 $\le, \ge$ | 日本印刷体常写作 $\leqq, \geqq$，两者含义完全相同。 |

---

## 2. 日文物理核心词汇与公式假名注音（板书必备）

### 2.1 核心物理词汇表

#### 刚体、力矩与重心
- **質点（しつてん / shitsuten）** — 质点
- **剛体（ごうたい / gōtai）** — 刚体
- **力のモーメント（ちからのもーめんと / chikara no mōmento）** — 力矩
- **回転軸（かいてんじく / kaitenjiku）** — 转轴
- **作用線（さようせん / sayōsen）** — 力的作用线
- **腕の長さ（うでのながさ / ude no nagasa）** — 力臂
- **抗力（こうりょく / kōryoku）** — 总约束反力（垂直抗力与摩擦力的合力）
- **一様な棒（いちようなぼう / ichiyō na bō）** — 均匀细棒
- **重心（じゅうしん / jūshin）** — 重心 / 质心
- **内分（ないぶん / naibun）** — 内分
- **転倒 / 倒れる条件（てんとう・たおれるじょうけん / tentō, taoreru jōken）** — 倾倒条件

#### 牛顿第二定律与空气阻力
- **運動の第2法則（うんどうのだいにほうそく / undō no daini hōsoku）** — 牛顿第二定律
- **運動方程式（うんどうほうていしき / undō hōteishiki）** — 运动方程（$ma = F$）
- **あらい斜面（あらいしゃめん / arai shamen）** — 粗糙斜面
- **なめらかな面（なめらかなめん / nameraka na men）** — 光滑表面
- **空気抵抗（くうきていこう / kūki teikō）** — 空气阻力
- **終端速度（しゅうたんそくど / shūtan sokudo）** — 终端速度 / 收尾速度
- **比例定数（ひれいていすう / hirei teisū）** — 比例常数

#### 功、功率与机械能
- **仕事（しごと / shigoto）** — 功（$W$）
- **ジュール（じゅーる / jūru）** — 焦耳（$\text{J}$）
- **仕事の原理（しごとのげんり / shigoto no genri）** — 功的原理
- **仕事率（しごとりつ / shigotoritsu）** — 功率（$P$）
- **ワット（わっと / watto）** — 瓦特（$\text{W}$）
- **エネルギー（えねるぎー / enerugī）** — 能量
- **運動エネルギー（うんどうえねるぎー / undō enerugī）** — 动能（$K$）
- **位置エネルギー（いちえねるぎー / ichi enerugī）** — 势能（$U$）
- **重力による位置エネルギー（じゅうりょくによるいちえねるぎー / jūryoku ni yoru ichi enerugī）** — 重力势能
- **弾性力による位置エネルギー（だんせいりょくによるいちえねるぎー / dansei-ryoku ni yoru ichi enerugī）** — 弹性势能
- **保存力（ほぞんりょく / hozonryoku）** — 保守力
- **非保存力（ひほぞんりょく / hihozonryoku）** — 非保守力
- **万有引力（ばんゆういんりょく / ban'yū inryoku）** — 万有引力
- **静電気力（せいでんきりょく / seidenkiryoku）** — 静电力
- **力学的エネルギー（りきがくてきえねるぎー / rikigakuteki enerugī）** — 机械能
- **力学的エネルギー保存則（りきがくてきえねるぎーほぞんそく / rikigakuteki enerugī hozonsoku）** — 机械能守恒定律
- **仕事とエネルギーの関係（しごととえねるぎーのかんけい / shigoto to enerugī no kankei）** — 功能关系

#### 动量、冲量与碰撞
- **運動量（うんどうりょう / undōryō）** — 动量（$\vec{p}$）
- **力積（りきせき / rikiseki）** — 冲量（$\vec{I}$）
- **運動量保存則（うんどうりょうほぞんそく / undōryō hozonsoku）** — 动量守恒定律
- **物体系（ぶったいけい / buttaikei）** — 物体系 / 系统
- **外力（がいりょく / gairyoku）** — 外力
- **反発係数 / はねかえり係数（はんぱつけいすう・はねかえりけいすう / hanpatsu keisū, hanekaeri keisū）** — 恢复系数（$e$）
- **弾性衝突（だんせいしょうとつ / dansei shōtotsu）** — 弹性碰撞
- **非弾性衝突（ひだんせいしょうとつ / hidansei shōtotsu）** — 非弹性碰撞
- **完全非弾性衝突（かんぜんひだんせいしょうとつ / kanzen hidansei shōtotsu）** — 完全非弹性碰撞
- **斜め衝突（ななめしょうとつ / naname shōtotsu）** — 斜碰 / 二维碰撞
- **反時計回り / 時計回り（はんとけいまわり・とけいまわり / hantokeimawari, tokeimawari）** — 逆时针 / 顺时针

### 2.2 核心公式课堂口语读法（板书念法）

| 公式 | 日本课堂标准板书口语读法 |
| :--- | :--- |
| $M = Fl$ | 「エム・イコール、エフ・エル」 |
| $x_G = \dfrac{m_1 x_1 + m_2 x_2}{m_1 + m_2}$ | 「エックスジー・イコール、エムいち・たす・エムに、ぶんの、エムいちエックスいち・たす・エムにエックスに」 |
| $m\vec{a} = \vec{F}$ | 「エム・エー・ベクトル、イコール、エフ・ベクトル」 |
| $W = Fx$ | 「ダブリュー・イコール、エフ・エックス」 |
| $P = \dfrac{W}{t} = Fv$ | 「ピー・イコール、ティーぶんのダブリュー、イコール、エフ・ブイ」 |
| $K = \dfrac{1}{2}mv^2$ | 「ケー・イコール、にぶんのいち・エムブイにじょう」 |
| $U = mgh,\ U = \dfrac{1}{2}kx^2$ | 「ユー・イコール、エムジーエイチ」「ユー・イコール、にぶんのいち・ケーエックスにじょう」 |
| $\vec{p} = m\vec{v},\ \vec{I} = \vec{F}\Delta t$ | 「ピー・ベクトル・イコール、エム・ブイ・ベクトル」「アイ・ベクトル・イコール、エフ・ベクトル・デルタティー」 |
| $m\vec{v}' - m\vec{v} = \vec{F}\Delta t$ | 「エム・ブイダッシュ・ひく・エム・ブイ、イコール、エフ・デルタティー」 |
| $e = -\dfrac{v_1' - v_2'}{v_1 - v_2}$ | 「イー・イコール、マイナス、ブイいち・ひく・ブイに、ぶんの、ブイいちダッシュ・ひく・ブイにダッシュ」 |

> 💡 **教材勘误提示（P.21 / 页码 20）**：本页大标题印刷为「重心運動の第2法則」，系排版时误将上一页标题「重心」与本页标题「運動の第2法則」拼接所致，授课时向学生说明正确标题为「**運動の第2法則（牛顿第二定律）**」即可。

---

## 3. 逐题深度解析（一题一解，不可跳步）

---

### 例題 1（教材 P.17 / 页码 16）：水平棒の釣り合い（水平杆的平衡与重物移动临界）

#### 【原题重现与翻译】
> **日文原题**：  
> 長さ $L$，質量 $M$ の一様な棒の一端を壁につけ，他端を壁と軽い糸でつないで固定したところ，棒は水平な状態で静止した。このとき，糸と棒のなす角は $\theta$ であった。重力加速度の大きさを $g$ とする。  
> (1) 糸の張力 $T$ を求めよ。  
> (2) 棒が壁から受ける垂直抗力 $N$ を求めよ。  
> (3) 棒が壁から受ける摩擦力 $F$ を求めよ。  
> (4) 棒が壁から受ける抗力の向きを図示せよ。  
> (5) 質量 $M$ のおもりを棒の右端に吊り下げた後，おもりの位置をゆっくりと左に移動させると，壁からの距離が $x$ になったところで棒がすべりはじめる。静止摩擦係数を $\mu_0$ として $x$ を求めよ。
>
> **中文翻译**：  
> 将一根长 $L$、质量 $M$ 的均匀细棒一端抵在竖直墙壁上，另一端用轻绳连接到墙壁上固定，棒在水平状态下保持静止，此时细绳与棒的夹角为 $\theta$。重力加速度大小为 $g$。  
> (1) 求绳的张力 $T$。  
> (2) 求棒受到墙壁的法向支持力 $N$。  
> (3) 求棒受到墙壁的静摩擦力 $F$。  
> (4) 图示棒受到墙壁的总约束反力（抗力）的方向。  
> (5) 将质量为 $M$ 的重物挂在棒的右端后，将重物的位置缓慢向左移动，当重物距墙壁距离为 $x$ 时棒开始滑动。设静摩擦系数为 $\mu_0$，求 $x$。

#### 【考点与模型定位】
**刚体水平杆三力平衡 + 力矩平衡 + 动载临界滑动模型**（注意：教材 P.17 仅印出了 (1)–(4) 的解答，**漏印了 (5) 的解答**，下文已做完整补全）。

#### 【多色矢量图解（SVG）】

<svg viewBox="0 0 420 260" width="420" height="260" xmlns="http://www.w3.org/2000/svg" style="background:#fafafa;border:1px solid #e5e7eb;border-radius:8px;">
  <defs>
    <marker id="arr-blue-002-1" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0,0 L0,6 L7,3 z" fill="#2563eb"/></marker>
    <marker id="arr-green-002-1" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0,0 L0,6 L7,3 z" fill="#16a34a"/></marker>
    <marker id="arr-red-002-1" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0,0 L0,6 L7,3 z" fill="#dc2626"/></marker>
    <marker id="arr-blk-002-1" markerWidth="7" markerHeight="7" refX="5" refY="3" orient="auto"><path d="M0,0 L0,6 L6,3 z" fill="#111827"/></marker>
  </defs>
  <!-- 左侧：受力分析与力矩分解 -->
  <text x="18" y="20" font-size="11" font-weight="bold" fill="#374151">(1)-(3) 受力とモーメント</text>
  <!-- 墙壁 -->
  <line x1="42" y1="32" x2="42" y2="230" stroke="#374151" stroke-width="2.5"/>
  <path d="M 34 40 L 42 32 M 34 56 L 42 48 M 34 72 L 42 64 M 34 88 L 42 80 M 34 104 L 42 96 M 34 120 L 42 112 M 34 136 L 42 128 M 34 152 L 42 144 M 34 168 L 42 160 M 34 184 L 42 176 M 34 200 L 42 192 M 34 216 L 42 208" stroke="#9ca3af" stroke-width="1"/>
  <!-- 水平棒 -->
  <rect x="42" y="150" width="160" height="8" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>
  <circle cx="42" cy="154" r="3" fill="#111827"/>
  <text x="28" y="164" font-size="11" font-weight="bold" fill="#111827">O</text>
  <!-- 细绳 -->
  <line x1="42" y1="70" x2="202" y2="150" stroke="#4b5563" stroke-width="1.5"/>
  <!-- 角度 theta -->
  <path d="M 172 150 A 30 30 0 0 1 175 137" fill="none" stroke="#dc2626" stroke-width="1.5"/>
  <text x="160" y="146" font-size="11" fill="#dc2626">θ</text>
  <!-- 重力 Mg -->
  <line x1="122" y1="158" x2="122" y2="225" stroke="#2563eb" stroke-width="2" marker-end="url(#arr-blue-002-1)"/>
  <text x="128" y="218" font-size="11" fill="#2563eb">Mg</text>
  <text x="72" y="176" font-size="10" fill="#4b5563">L/2</text>
  <!-- 支持力 N -->
  <line x1="42" y1="154" x2="100" y2="154" stroke="#16a34a" stroke-width="2" marker-end="url(#arr-green-002-1)"/>
  <text x="84" y="146" font-size="11" fill="#16a34a">N</text>
  <!-- 摩擦力 F -->
  <line x1="42" y1="154" x2="42" y2="108" stroke="#dc2626" stroke-width="2" marker-end="url(#arr-red-002-1)"/>
  <text x="48" y="122" font-size="11" fill="#dc2626">F</text>
  <!-- 张力 T 及其分量 -->
  <line x1="202" y1="150" x2="146" y2="122" stroke="#16a34a" stroke-width="2.2" marker-end="url(#arr-green-002-1)"/>
  <text x="148" y="114" font-size="11" font-weight="bold" fill="#16a34a">T</text>
  <line x1="202" y1="150" x2="202" y2="122" stroke="#16a34a" stroke-width="1.4" stroke-dasharray="4,2" marker-end="url(#arr-green-002-1)"/>
  <text x="172" y="102" font-size="10" fill="#16a34a">Tsinθ</text>
  <line x1="202" y1="150" x2="146" y2="150" stroke="#16a34a" stroke-width="1.4" stroke-dasharray="4,2" marker-end="url(#arr-green-002-1)"/>
  <text x="155" y="172" font-size="10" fill="#16a34a">Tcosθ</text>

  <!-- 分隔线 -->
  <line x1="224" y1="16" x2="224" y2="245" stroke="#d1d5db" stroke-dasharray="4,4"/>

  <!-- 右侧：(4) 三力汇交与抗力方向 -->
  <text x="240" y="20" font-size="11" font-weight="bold" fill="#374151">(4) 抗力の向き（作用線1点交差）</text>
  <line x1="252" y1="45" x2="252" y2="215" stroke="#374151" stroke-width="2.5"/>
  <rect x="252" y="150" width="144" height="7" fill="#e5e7eb" stroke="#374151" stroke-width="1.5"/>
  <!-- 细绳 -->
  <line x1="252" y1="78" x2="396" y2="150" stroke="#4b5563" stroke-width="1.5"/>
  <!-- 重力作用线向上延伸交于 (324, 114) -->
  <line x1="324" y1="157" x2="324" y2="210" stroke="#2563eb" stroke-width="2" marker-end="url(#arr-blue-002-1)"/>
  <text x="330" y="205" font-size="11" fill="#2563eb">Mg</text>
  <line x1="324" y1="150" x2="324" y2="100" stroke="#9ca3af" stroke-width="1.2" stroke-dasharray="3,3"/>
  <!-- 交点 -->
  <circle cx="324" cy="114" r="3.5" fill="#111827"/>
  <!-- 抗力合力 R 指向交点 -->
  <line x1="252" y1="150" x2="318" y2="117" stroke="#dc2626" stroke-width="2.2" marker-end="url(#arr-red-002-1)"/>
  <text x="266" y="124" font-size="11" font-weight="bold" fill="#dc2626">抗力 R</text>
  <!-- 分力虚线框 -->
  <line x1="252" y1="150" x2="252" y2="114" stroke="#dc2626" stroke-width="1.2" stroke-dasharray="3,2"/>
  <line x1="252" y1="114" x2="324" y2="114" stroke="#9ca3af" stroke-width="1" stroke-dasharray="3,2"/>
  <text x="236" y="132" font-size="10" fill="#dc2626">F</text>
  <text x="285" y="168" font-size="10" fill="#16a34a">N</text>
  <text x="238" y="238" font-size="10" fill="#374151">※ 重力・張力・抗力の作用線が1点で交わる</text>
</svg>

#### 【日本考场规范分步解答】

**(1)(2)(3)** 棒が受ける力は，重力 $Mg$，糸の張力 $T$，壁からの垂直抗力 $N$，壁からの静止摩擦力 $F$（上向きと仮定）である。  
- 水平方向の力のつりあいより，
  $$N = T\cos\theta \quad \cdots\text{①}$$
- 鉛直方向の力のつりあいより，
  $$F + T\sin\theta = Mg \quad \cdots\text{②}$$
- 壁との接点 $\text{O}$ のまわりの力のモーメントのつりあいより，
  $$Mg \times \frac{L}{2} = T\sin\theta \times L \quad \cdots\text{③}$$

③ より $T\sin\theta = \dfrac{1}{2}Mg$ であるから，
$$T = \frac{Mg}{2\sin\theta}$$
これを ① に代入して，
$$N = \frac{Mg}{2\sin\theta} \cdot \cos\theta = \frac{Mg}{2\tan\theta}$$
また，② に代入して，
$$F = Mg - \frac{1}{2}Mg = \frac{1}{2}Mg$$

> 💡 讲师批注：取墙壁接触点 $O$ 为转轴，直接消掉 $N$ 和 $F$ 两个未知力，一步就求出 $T\sin\theta = \frac{1}{2}Mg$！千万不要选棒的右端或中点为轴，那样会让式子变复杂。

**(4)** 剛体に働く 3 つの力（重力 $Mg$，糸の張力 $T$，壁からの抗力 $\vec{R} = \vec{N} + \vec{F}$）がつりあっているとき，これら 3 つの力の作用線は 1 点で交わる。  
したがって，重力 $Mg$ の作用線と張力 $T$ の作用線の交点に向かって，棒の左端から引いた向き（右図の赤矢印，水平面から上向きに角 $\theta$ をなす向き）が抗力の向きである。

> 💡 讲师批注：用代数也能验算抗力方向：$\tan\phi = \dfrac{F}{N} = \dfrac{\frac{1}{2}Mg}{\frac{Mg}{2\tan\theta}} = \tan\theta \implies \phi = \theta$，恰好与绳子对称！

**(5)（教材未附解答，完整补充）**  
質量 $M$ のおもりが壁から距離 $x$ の位置にあるときの張力を $T'$，垂直抗力を $N'$，静止摩擦力を $F'$ とする。  
- 水平方向の力のつりあいより，$N' = T'\cos\theta$
- 鉛直方向の力のつりあいより，$F' + T'\sin\theta = Mg + Mg = 2Mg$
- 壁との接点 $\text{O}$ のまわりの力のモーメントのつりあいより，
  $$Mg \times \frac{L}{2} + Mg \times x = T'\sin\theta \times L \implies T'\sin\theta = Mg\left(\frac{1}{2} + \frac{x}{L}\right)$$
これより $N'$ と $F'$ を求めると，
$$N' = \frac{T'\sin\theta}{\tan\theta} = \frac{Mg}{\tan\theta}\left(\frac{1}{2} + \frac{x}{L}\right), \qquad F' = 2Mg - T'\sin\theta = Mg\left(\frac{3}{2} - \frac{x}{L}\right)$$
棒がすべりはじめる直前は最大摩擦力に達しているから，$F' = \mu_0 N'$ が成り立つ。
$$Mg\left(\frac{3}{2} - \frac{x}{L}\right) = \mu_0 \cdot \frac{Mg}{\tan\theta}\left(\frac{1}{2} + \frac{x}{L}\right)$$
両辺を $Mg$ で割り，$\tan\theta$ を掛けて整理すると，
$$\left(\frac{3}{2} - \frac{x}{L}\right)\tan\theta = \mu_0\left(\frac{1}{2} + \frac{x}{L}\right)$$
$$\frac{x}{L}(\tan\theta + \mu_0) = \frac{3\tan\theta - \mu_0}{2} \implies x = \frac{3\tan\theta - \mu_0}{2(\tan\theta + \mu_0)}L$$

> 💡 讲师批注：为什么重物往**左**移反而容易滑？看式子一目了然：当 $x$ 减小时，$T'\sin\theta$ 减小导致压墙力 $N'$ 减小（最大静摩擦力变小），同时墙面需承担的竖直摩擦力 $F'$ 却增大！此消彼长，必然在临界点 $x$ 处下滑。注意该解成立隐含 $3\tan\theta > \mu_0$（否则移到墙根也不会滑）。

#### 【最终答案】
- **(1) $T = \dfrac{Mg}{2\sin\theta}$**
- **(2) $N = \dfrac{Mg}{2\tan\theta}$**
- **(3) $F = \dfrac{1}{2}Mg$**
- **(4) 棒の左端から，重力と張力の作用線の交点へ向かう向き（水平から上向きに角 $\theta$）**
- **(5) $x = \dfrac{3\tan\theta - \mu_0}{2(\tan\theta + \mu_0)}L$**

---

### 例題 2（教材 P.18 / 页码 17）：壁に立てかけた棒の釣り合い（斜靠光滑墙的梯子平衡）

#### 【原题重现与翻译】
> **日文原题**：  
> 長さ $L$，質量 $M$ の一様な棒を床と角 $\theta$ をなすようになめらかな壁に立てかける。棒と床の間の静止摩擦係数を $\mu_0$ とする。  
> (1) 棒がすべりはじめないための角度の条件を求めよ。  
> (2) 質量 $3M$ の人は棒の上をどこまで登れるか。
>
> **中文翻译**：  
> 将一根长 $L$、质量 $M$ 的均匀细棒斜靠在光滑的竖直墙壁上，棒与水平地板的夹角为 $\theta$。设棒与地板之间的静摩擦系数为 $\mu_0$。  
> (1) 求棒不开始滑动所需满足的角度条件。  
> (2) 质量为 $3M$ 的人沿棒最多能爬到什么位置？

#### 【考点与模型定位】
**经典“梯子靠墙”模型**（光滑墙无摩擦 + 粗糙地有静摩擦 + 力臂计算双视角；教材 P.18 仅印了 (1) 的解答，**漏印了 (2) 的解答**，下文已完整补全）。

#### 【多色矢量图解（SVG）】

<svg viewBox="0 0 420 260" width="420" height="260" xmlns="http://www.w3.org/2000/svg" style="background:#fafafa;border:1px solid #e5e7eb;border-radius:8px;">
  <defs>
    <marker id="arr-blue-002-2" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0,0 L0,6 L7,3 z" fill="#2563eb"/></marker>
    <marker id="arr-green-002-2" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0,0 L0,6 L7,3 z" fill="#16a34a"/></marker>
    <marker id="arr-red-002-2" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0,0 L0,6 L7,3 z" fill="#dc2626"/></marker>
  </defs>
  <!-- 墙与地板 -->
  <line x1="65" y1="25" x2="65" y2="215" stroke="#374151" stroke-width="2.5"/>
  <line x1="65" y1="215" x2="365" y2="215" stroke="#374151" stroke-width="2.5"/>
  <text x="15" y="110" font-size="10" fill="#6b7280">なめらか</text>
  <text x="15" y="124" font-size="10" fill="#6b7280">な壁</text>
  <!-- 斜棒 (65, 55) 到 (265, 215) -->
  <line x1="65" y1="55" x2="265" y2="215" stroke="#374151" stroke-width="6" stroke-linecap="round"/>
  <line x1="65" y1="55" x2="265" y2="215" stroke="#e5e7eb" stroke-width="3" stroke-linecap="round"/>
  <!-- 角度 theta -->
  <path d="M 225 215 A 40 40 0 0 1 234 190" fill="none" stroke="#dc2626" stroke-width="1.5"/>
  <text x="210" y="206" font-size="11" fill="#dc2626">θ</text>
  <!-- 支点 O -->
  <circle cx="265" cy="215" r="3.5" fill="#111827"/>
  <text x="272" y="229" font-size="11" font-weight="bold" fill="#111827">O (回転軸)</text>

  <!-- 墙支持力 R (光滑无摩擦) -->
  <line x1="65" y1="55" x2="135" y2="55" stroke="#16a34a" stroke-width="2.2" marker-end="url(#arr-green-002-2)"/>
  <text x="115" y="47" font-size="11" font-weight="bold" fill="#16a34a">R</text>
  <!-- R 的力臂 Lsinθ -->
  <line x1="135" y1="55" x2="290" y2="55" stroke="#9ca3af" stroke-dasharray="3,3"/>
  <line x1="285" y1="55" x2="285" y2="215" stroke="#6b7280" stroke-width="1" stroke-dasharray="4,2"/>
  <text x="292" y="140" font-size="11" fill="#374151">Lsinθ</text>

  <!-- 棒重力 Mg (中点 165, 135) -->
  <line x1="165" y1="135" x2="165" y2="195" stroke="#2563eb" stroke-width="2" marker-end="url(#arr-blue-002-2)"/>
  <text x="142" y="185" font-size="11" fill="#2563eb">Mg</text>
  <line x1="165" y1="195" x2="165" y2="215" stroke="#9ca3af" stroke-dasharray="2,2"/>
  <text x="188" y="232" font-size="10" fill="#374151">(L/2)cosθ</text>

  <!-- (2) 人 3Mg 示意 (沿棒距离 x) -->
  <circle cx="125" cy="103" r="6" fill="#fef3c7" stroke="#b45309" stroke-width="1.5"/>
  <line x1="125" y1="109" x2="125" y2="168" stroke="#2563eb" stroke-width="2" stroke-dasharray="4,2" marker-end="url(#arr-blue-002-2)"/>
  <text x="80" y="152" font-size="10" fill="#2563eb">3Mg ((2)のみ)</text>
  <text x="195" y="138" font-size="10" fill="#b45309">下端から距離 x</text>

  <!-- 地面支持力 N 与摩擦力 F -->
  <line x1="265" y1="215" x2="265" y2="145" stroke="#16a34a" stroke-width="2.2" marker-end="url(#arr-green-002-2)"/>
  <text x="250" y="160" font-size="11" font-weight="bold" fill="#16a34a">N</text>
  <line x1="265" y1="215" x2="205" y2="215" stroke="#dc2626" stroke-width="2.2" marker-end="url(#arr-red-002-2)"/>
  <text x="225" y="207" font-size="11" font-weight="bold" fill="#dc2626">F</text>
</svg>

#### 【日本考场规范分步解答】

**(1)** 棒がなめらかな壁から受ける垂直抗力を $R$，床から受ける垂直抗力を $N$，静止摩擦力を $F$（左向き）とする。  
- 水平方向の力のつりあいより，
  $$R = F \quad \cdots\text{①}$$
- 鉛直方向の力のつりあいより，
  $$Mg = N \quad \cdots\text{②}$$
- 床との接点 $\text{O}$ のまわりの力のモーメントのつりあいより，
  $$R \times L\sin\theta = Mg \times \frac{L}{2}\cos\theta \implies R = \frac{Mg}{2\tan\theta} \quad \cdots\text{③}$$
棒がすべりはじめないための摩擦力の条件は $F \le \mu_0 N$ であるから，①②③ を代入して，
$$\frac{Mg}{2\tan\theta} \le \mu_0 Mg \implies \tan\theta \ge \frac{1}{2\mu_0}$$

> 💡 讲师批注：本题再次印证“**选未知力最多的地板接触点 $O$ 为转轴**”的威力！若选壁面接触点为轴也能做，但要同时算 $N$ 和 $F$ 两个力矩。注意墙壁是**光滑（なめらか）**的，所以墙面**没有摩擦力**！

**(2)（教材未附解答，完整补充）**  
質量 $3M$ の人が棒の下端 $\text{O}$ から棒に沿って距離 $x$ の位置まで登ったときの，壁からの垂直抗力を $R'$，床からの垂直抗力を $N'$，静止摩擦力を $F'$ とする。  
- 水平方向の力のつりあいより，$R' = F'$
- 鉛直方向の力のつりあいより，$N' = Mg + 3Mg = 4Mg$
- 下端 $\text{O}$ のまわりの力のモーメントのつりあいより，
  $$R' \times L\sin\theta = Mg \times \frac{L}{2}\cos\theta + 3Mg \times x\cos\theta$$
  両辺を $L\sin\theta$ で割ると，
  $$R' = \frac{Mg}{\tan\theta}\left(\frac{1}{2} + \frac{3x}{L}\right)$$
すべりはじめないための条件 $F' \le \mu_0 N'$ より，
$$\frac{Mg}{\tan\theta}\left(\frac{1}{2} + \frac{3x}{L}\right) \le \mu_0 \cdot 4Mg$$
両辺を $Mg$ で割り整理すると，
$$\frac{1}{2} + \frac{3x}{L} \le 4\mu_0\tan\theta \implies \frac{3x}{L} \le \frac{8\mu_0\tan\theta - 1}{2}$$
$$\therefore x \le \frac{8\mu_0\tan\theta - 1}{6}L$$
なお，$\dfrac{8\mu_0\tan\theta - 1}{6} \ge 1$ すなわち $\tan\theta \ge \dfrac{7}{8\mu_0}$ のときは，棒の上端（$x = L$）まで登ることができる。

> 💡 讲师批注：提醒学生思考一个极好的物理细节：人越往上爬（$x$ 越大），人的重力力臂 $x\cos\theta$ 越大，逼得墙推力 $R'$ 与地摩擦力 $F'$ 越来越大，而总支持力 $N' = 4Mg$ 却不变！所以爬得越高越容易滑。此外当 $\tan\theta \ge \frac{7}{8\mu_0}$ 时算出的 $x$ 会超过棒长 $L$，此时应答“能爬到棒的顶端 $L$”。

#### 【最终答案】
- **(1) $\tan\theta \ge \dfrac{1}{2\mu_0}$**
- **(2) 下端から距離 $x = \dfrac{8\mu_0\tan\theta - 1}{6}L$ の位置まで**（ただし $\tan\theta \ge \dfrac{7}{8\mu_0}$ のときは上端 $L$ まで）

---

### 例題 3（教材 P.19 / 页码 18）：剛体が倒れる条件（长方体滑动与倾倒的竞争条件）

> 💡 **教材勘误提示**：教材 P.19 标题印为「剛体が倒れた条件」，语义上应为「**剛体が倒れる条件**（刚体倾倒的条件）」。

#### 【原题重现与翻译】
> **日文原题**：  
> 水平な床の上に底辺 $b$，高さ $h$，質量 $m$ の一様な直方体が置かれている。この直方体の上端に糸をつけ，水平に張力 $T$ で引く。静止摩擦係数を $\mu_0$，重力加速度を $g$ とする。  
> (1) 直方体が床の上をすべりはじめるための $T$ の条件を求めよ。  
> (2) 直方体が倒れないための $T$ の条件を求めよ。  
> (3) 直方体が倒れる前にすべりはじめるための $\mu_0$ の条件を求めよ。
>
> **中文翻译**：  
> 在水平地板上放置一个底边宽 $b$、高 $h$、质量 $m$ 的均匀长方体。在长方体上端系一根细绳，沿水平方向以张力 $T$ 拉动。设静摩擦系数为 $\mu_0$，重力加速度为 $g$。  
> (1) 求长方体在地板上开始滑动所需满足的 $T$ 的条件。  
> (2) 求长方体不倾倒所需满足的 $T$ 的条件。  
> (3) 求长方体在倾倒前先开始滑动所需满足的 $\mu_0$ 的条件。

#### 【考点与模型定位】
**刚体平动（滑动）与转动（倾倒）竞争模型**（核心秘密：随着拉力 $T$ 增大，地板支持力 $N$ 的作用点不断向右端移动，**倾倒瞬间 $N$ 的作用点恰好移到最右下角支点**！）。

#### 【多色矢量图解（SVG）】

<svg viewBox="0 0 420 260" width="420" height="260" xmlns="http://www.w3.org/2000/svg" style="background:#fafafa;border:1px solid #e5e7eb;border-radius:8px;">
  <defs>
    <marker id="arr-blue-002-3" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0,0 L0,6 L7,3 z" fill="#2563eb"/></marker>
    <marker id="arr-green-002-3" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0,0 L0,6 L7,3 z" fill="#16a34a"/></marker>
    <marker id="arr-red-002-3" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0,0 L0,6 L7,3 z" fill="#dc2626"/></marker>
  </defs>
  <!-- 左图：未倾倒 -->
  <text x="48" y="24" font-size="11" font-weight="bold" fill="#374151">まだまだ倒れない</text>
  <line x1="25" y1="215" x2="190" y2="215" stroke="#374151" stroke-width="2.5"/>
  <rect x="60" y="65" width="80" height="150" fill="#e5e7eb" stroke="#374151" stroke-width="1.8"/>
  <text x="96" y="57" font-size="11" fill="#374151">b</text>
  <text x="45" y="142" font-size="11" fill="#374151">h</text>
  <!-- 拉力 T -->
  <line x1="140" y1="65" x2="188" y2="65" stroke="#dc2626" stroke-width="2.2" marker-end="url(#arr-red-002-3)"/>
  <text x="176" y="57" font-size="11" font-weight="bold" fill="#dc2626">T</text>
  <!-- 重力 mg -->
  <line x1="100" y1="140" x2="100" y2="200" stroke="#2563eb" stroke-width="2" marker-end="url(#arr-blue-002-3)"/>
  <text x="76" y="182" font-size="11" fill="#2563eb">mg</text>
  <!-- 支持力 N 偏右 -->
  <line x1="122" y1="215" x2="122" y2="155" stroke="#16a34a" stroke-width="2" marker-end="url(#arr-green-002-3)"/>
  <text x="126" y="170" font-size="11" fill="#16a34a">N</text>
  <!-- 摩擦力 F -->
  <line x1="100" y1="215" x2="55" y2="215" stroke="#dc2626" stroke-width="2" marker-end="url(#arr-red-002-3)"/>
  <text x="64" y="208" font-size="11" fill="#dc2626">F</text>
  <text x="48" y="238" font-size="10" fill="#6b7280">Nの作用点は底面内部</text>

  <!-- 分隔线 -->
  <line x1="210" y1="16" x2="210" y2="245" stroke="#d1d5db" stroke-dasharray="4,4"/>

  <!-- 右图：倒れる直前 -->
  <text x="275" y="24" font-size="11" font-weight="bold" fill="#dc2626">倒れる直前（臨界）</text>
  <line x1="230" y1="215" x2="400" y2="215" stroke="#374151" stroke-width="2.5"/>
  <rect x="260" y="65" width="80" height="150" fill="#e5e7eb" stroke="#374151" stroke-width="1.8"/>
  <text x="296" y="57" font-size="11" fill="#374151">b</text>
  <text x="245" y="142" font-size="11" fill="#374151">h</text>
  <!-- 拉力 T -->
  <line x1="340" y1="65" x2="392" y2="65" stroke="#dc2626" stroke-width="2.2" marker-end="url(#arr-red-002-3)"/>
  <text x="380" y="57" font-size="11" font-weight="bold" fill="#dc2626">T</text>
  <!-- 重力 mg -->
  <line x1="300" y1="140" x2="300" y2="200" stroke="#2563eb" stroke-width="2" marker-end="url(#arr-blue-002-3)"/>
  <text x="276" y="182" font-size="11" fill="#2563eb">mg</text>
  <!-- 支持力 N 移至右下角支点 -->
  <circle cx="340" cy="215" r="4" fill="#111827"/>
  <line x1="340" y1="215" x2="340" y2="155" stroke="#16a34a" stroke-width="2.2" marker-end="url(#arr-green-002-3)"/>
  <text x="346" y="170" font-size="11" font-weight="bold" fill="#16a34a">N</text>
  <!-- 摩擦力 F -->
  <line x1="340" y1="215" x2="292" y2="215" stroke="#dc2626" stroke-width="2" marker-end="url(#arr-red-002-3)"/>
  <text x="312" y="208" font-size="11" fill="#dc2626">F</text>
  <text x="308" y="234" font-size="10" fill="#374151">b/2</text>
  <text x="348" y="232" font-size="10" font-weight="bold" fill="#111827">支点</text>
</svg>

#### 【日本考场规范分步解答】

**(1)** 床からの垂直抗力を $N$，静止摩擦力を $F$ とすると，
- 水平方向の力のつりあいより，$F = T$
- 鉛直方向の力のつりあいより，$N = mg$

すべりはじめるための条件は $F > \mu_0 N$ であるから，
$$T > \mu_0 mg$$

**(2)** 直方体が右下に傾いて倒れる直前，垂直抗力 $N$ の作用点は底面の右端（支点）に移動する。  
この右端の支点のまわりで，時計回りのモーメント（倒そうとするモーメント）が反時計回りのモーメント（戻そうとするモーメント）以下であれば倒れないから，
$$T \times h \le mg \times \frac{b}{2} \implies T \le \frac{mgb}{2h}$$

> 💡 讲师批注：把“底面右下角”选为转轴极其巧妙：$N$ 和 $F$ 都通过该支点，力臂全为 $0$！此时只要比较拉力 $T$ 的顺时针力矩 $Th$ 与重力 $mg$ 的逆时针力矩 $mg \cdot \frac{b}{2}$ 即可！

**(3)** 倒れる前にすべりはじめるためには，すべりはじめる張力 $\mu_0 mg$ が倒れる限界の張力 $\dfrac{mgb}{2h}$ より小さければよい。  
よって (1)，(2) より，
$$\mu_0 mg < \frac{mgb}{2h} \implies \mu_0 < \frac{b}{2h}$$

> 💡 讲师批注：记住物理直觉：物体越**矮胖**（$\frac{b}{2h}$ 大）或地面越**光滑**（$\mu_0$ 小），越容易先滑后倒；反之又高又瘦且地面粗糙，一拉就会直接翻倒。

#### 【最终答案】
- **(1) $T > \mu_0 mg$**
- **(2) $T \le \dfrac{mgb}{2h}$**
- **(3) $\mu_0 < \dfrac{b}{2h}$**

---

### 例題 4（教材 P.22–24 / 页码 21–23）：あらい斜面上の物体の運動（粗糙斜面滑轮连接体全分析）

#### 【原题重现与翻译】
> **日文原题**：  
> 傾斜角 $\theta$ のあらい斜面上に質量 $m$ の物体 A を置き，物体 A と糸でつながれた物体 B を斜面の頂上に取り付けたなめらかに回る滑車を通して静かにつり下ろす。物体と斜面の間の静止摩擦係数を $\mu_0$，動摩擦係数を $\mu$，重力加速度の大きさを $g$ とする。  
> (1) 物体 B の質量が $M_0$ のとき，物体 A は静止したままであった。$M_0$ が満たすべき条件を不等式で表せ。  
> (2) 物体 B の質量が $M_1$ のとき，物体 A は斜面上方に動き始めた。2 物体の加速度の大きさ $a_1$ と糸の張力の大きさ $T_1$ を求めよ。  
> (3) 物体 B の質量が $M_2$ のとき，物体 A は斜面下方に動き始めた。2 物体の加速度の大きさ $a_2$ と糸の張力の大きさ $T_2$ を求めよ。
>
> **中文翻译**：  
> 在倾角为 $\theta$ 的粗糙斜面上放置质量为 $m$ 的物体 A，将与物体 A 用轻绳相连的物体 B 跨过安装在斜面顶端的光滑定滑轮后轻轻下放。设物体与斜面间的静摩擦系数为 $\mu_0$，动摩擦系数为 $\mu$，重力加速度大小为 $g$。  
> (1) 当物体 B 的质量为 $M_0$ 时，物体 A 保持静止。用不等式表示 $M_0$ 必须满足的条件。  
> (2) 当物体 B 的质量为 $M_1$ 时，物体 A 开始沿斜面向上运动。求两物体的加速度大小 $a_1$ 与绳的张力大小 $T_1$。  
> (3) 当物体 B 的质量为 $M_2$ 时，物体 A 开始沿斜面向下运动。求两物体的加速度大小 $a_2$ 与绳的张力大小 $T_2$。

#### 【考点与模型定位】
**粗糙斜面滑轮连接体综合模型**（静摩擦力方向双临界讨论 + 牛顿第二定律隔离法列运动方程）。

#### 【多色矢量图解（SVG）】

<svg viewBox="0 0 420 260" width="420" height="260" xmlns="http://www.w3.org/2000/svg" style="background:#fafafa;border:1px solid #e5e7eb;border-radius:8px;">
  <defs>
    <marker id="arr-blue-002-4" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0,0 L0,6 L7,3 z" fill="#2563eb"/></marker>
    <marker id="arr-green-002-4" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0,0 L0,6 L7,3 z" fill="#16a34a"/></marker>
    <marker id="arr-red-002-4" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0,0 L0,6 L7,3 z" fill="#dc2626"/></marker>
    <marker id="arr-blk-002-4" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0,0 L0,6 L7,3 z" fill="#111827"/></marker>
  </defs>
  <text x="16" y="20" font-size="11" font-weight="bold" fill="#374151">例：(2) A が斜面上方に加速（B が下降）する場合の受力図</text>
  <!-- 斜面 -->
  <polygon points="40,220 290,220 290,95" fill="#f3f4f6" stroke="#374151" stroke-width="2"/>
  <path d="M 85 220 A 45 45 0 0 0 80 200" fill="none" stroke="#dc2626" stroke-width="1.5"/>
  <text x="90" y="214" font-size="11" fill="#dc2626">θ</text>
  <!-- 定滑轮 -->
  <circle cx="295" cy="88" r="11" fill="#fff" stroke="#374151" stroke-width="1.8"/>
  <circle cx="295" cy="88" r="2.5" fill="#374151"/>

  <!-- 物体 A (斜面上，倾角 arctan(0.5) ≈ 26.57°) -->
  <g transform="translate(165, 158) rotate(-26.57)">
    <rect x="-24" y="-30" width="48" height="30" fill="#dbeafe" stroke="#1e40af" stroke-width="1.5"/>
    <text x="-6" y="-11" font-size="12" font-weight="bold" fill="#1e3a8a">A</text>
    <!-- 支持力 N -->
    <line x1="0" y1="-30" x2="0" y2="-75" stroke="#16a34a" stroke-width="2" marker-end="url(#arr-green-002-4)"/>
    <text x="6" y="-66" font-size="11" font-weight="bold" fill="#16a34a">N</text>
    <!-- 张力 T1 -->
    <line x1="24" y1="-15" x2="88" y2="-15" stroke="#16a34a" stroke-width="2.2" marker-end="url(#arr-green-002-4)"/>
    <text x="58" y="-22" font-size="11" font-weight="bold" fill="#16a34a">T₁</text>
    <!-- 摩擦力 μN (沿斜面向下) -->
    <line x1="-24" y1="-2" x2="-74" y2="-2" stroke="#dc2626" stroke-width="2" marker-end="url(#arr-red-002-4)"/>
    <text x="-76" y="-10" font-size="10" font-weight="bold" fill="#dc2626">μN (or f)</text>
    <!-- 加速度 a1 (沿斜面向上) -->
    <line x1="-15" y1="-48" x2="35" y2="-48" stroke="#111827" stroke-width="1.8" stroke-dasharray="5,3" marker-end="url(#arr-blk-002-4)"/>
    <text x="15" y="-54" font-size="11" fill="#111827">a₁</text>
    <!-- 重力分量虚线 -->
    <line x1="0" y1="-15" x2="-30" y2="-15" stroke="#2563eb" stroke-width="1.5" stroke-dasharray="3,2" marker-end="url(#arr-blue-002-4)"/>
    <text x="-68" y="-22" font-size="9" fill="#2563eb">mgsinθ</text>
    <line x1="0" y1="-15" x2="0" y2="35" stroke="#2563eb" stroke-width="1.5" stroke-dasharray="3,2" marker-end="url(#arr-blue-002-4)"/>
    <text x="6" y="32" font-size="9" fill="#2563eb">mgcosθ</text>
  </g>
  <!-- A 的竖直重力 mg -->
  <line x1="158" y1="145" x2="158" y2="205" stroke="#2563eb" stroke-width="2.2" marker-end="url(#arr-blue-002-4)"/>
  <text x="140" y="212" font-size="11" font-weight="bold" fill="#2563eb">mg</text>

  <!-- 绳子连接 A 与 B -->
  <line x1="215" y1="117" x2="290" y2="78" stroke="#4b5563" stroke-width="1.5"/>
  <line x1="306" y1="88" x2="306" y2="148" stroke="#4b5563" stroke-width="1.5"/>

  <!-- 物体 B -->
  <rect x="290" y="148" width="32" height="32" fill="#fef3c7" stroke="#b45309" stroke-width="1.5"/>
  <text x="301" y="168" font-size="12" font-weight="bold" fill="#92400e">B</text>
  <!-- B 的张力 T1 -->
  <line x1="306" y1="148" x2="306" y2="108" stroke="#16a34a" stroke-width="2.2" marker-end="url(#arr-green-002-4)"/>
  <text x="312" y="122" font-size="11" font-weight="bold" fill="#16a34a">T₁</text>
  <!-- B 的重力 M1g -->
  <line x1="306" y1="180" x2="306" y2="236" stroke="#2563eb" stroke-width="2.2" marker-end="url(#arr-blue-002-4)"/>
  <text x="313" y="232" font-size="11" font-weight="bold" fill="#2563eb">M₁g</text>
  <!-- B 的加速度 a1 -->
  <line x1="346" y1="145" x2="346" y2="195" stroke="#111827" stroke-width="1.8" stroke-dasharray="5,3" marker-end="url(#arr-blk-002-4)"/>
  <text x="352" y="175" font-size="11" fill="#111827">a₁</text>
  <text x="342" y="112" font-size="10" fill="#6b7280">(3)はa₂・μN</text>
  <text x="342" y="125" font-size="10" fill="#6b7280">の向きが逆</text>
</svg>

#### 【日本考场规范分步解答】

**(1)** 糸の張力を $T$，垂直抗力を $N$，静止摩擦力を $f$ とする。静止の限界には 2 通りある。

**(i) 物体 A が斜面上方に動き出そうとするとき**（静止摩擦力 $f$ は斜面下向き）  
- 物体 A について：
  - 斜面方向（$x$ 軸）のつりあい：$T = mg\sin\theta + f$
  - 斜面に垂直な方向（$y$ 軸）のつりあい：$N = mg\cos\theta$
- 物体 B について：鉛直方向のつりあい：$M_0 g = T$

動き出さない条件は $f \le \mu_0 N$ であるから，$f = M_0 g - mg\sin\theta$ を代入して，
$$M_0 g - mg\sin\theta \le \mu_0 mg\cos\theta \implies M_0 \le m(\sin\theta + \mu_0\cos\theta)$$

**(ii) 物体 A が斜面下方に動き出そうとするとき**（静止摩擦力 $f$ は斜面上向き）  
- 物体 A について：
  - $x$ 軸方向のつりあい：$T + f = mg\sin\theta$
  - $y$ 軸方向のつりあい：$N = mg\cos\theta$
- 物体 B について：$M_0 g = T$

動き出さない条件は $f \le \mu_0 N$ であるから，$f = mg\sin\theta - M_0 g$ を代入して，
$$mg\sin\theta - M_0 g \le \mu_0 mg\cos\theta \implies m(\sin\theta - \mu_0\cos\theta) \le M_0$$

(i)，(ii) より，
$$m(\sin\theta - \mu_0\cos\theta) \le M_0 \le m(\sin\theta + \mu_0\cos\theta)$$

> 💡 讲师批注：切记静摩擦力是“变色龙”，既能朝下（挡住 A 往上滑）也能朝上（挡住 A 往下滑），所以必然给出 $M_0$ 的**上界和下界**！另外若 $\tan\theta < \mu_0$，则左侧 $m(\sin\theta - \mu_0\cos\theta) < 0$，此时只要 $M_0 > 0$ 就绝不会下滑。

**(2)** 物体 A は斜面上方に，物体 B は鉛直下方にそれぞれ加速度 $a_1$ で運動する。動摩擦力 $\mu N$ は運動と逆の斜面下向きにはたらく。  
- 物体 A について：
  - 斜面上向きを正とする運動方程式：$m a_1 = T_1 - mg\sin\theta - \mu N \quad \cdots\text{①}$
  - 斜面に垂直な方向のつりあい：$N = mg\cos\theta \quad \cdots\text{②}$
- 物体 B について：
  - 鉛直下向きを正とする運動方程式：$M_1 a_1 = M_1 g - T_1 \quad \cdots\text{③}$

① $+$ ③ より張力 $T_1$ を消去し，② を代入すると，
$$(M_1 + m)a_1 = M_1 g - mg\sin\theta - \mu mg\cos\theta$$
$$\therefore a_1 = \frac{M_1 - m(\sin\theta + \mu\cos\theta)}{M_1 + m}g$$
これを ③ の $T_1 = M_1(g - a_1)$ に代入すると，
$$T_1 = M_1 g \left\{1 - \frac{M_1 - m(\sin\theta + \mu\cos\theta)}{M_1 + m}\right\} = \frac{M_1 m(1 + \sin\theta + \mu\cos\theta)}{M_1 + m}g$$

> 💡 讲师批注：求张力 $T_1$ 时，代入 **B 的运动方程 $T_1 = M_1(g - a_1)$** 比代入 A 的方程快 3 倍！同时教学生“分子分母通分技巧”：分子里 $M_1$ 恰好一正一负抵消，只剩漂亮的对称因子 $M_1 m$！

**(3)** 物体 A は斜面下方に，物体 B は鉛直上方にそれぞれ加速度 $a_2$ で運動する。動摩擦力 $\mu N$ は運動と逆の斜面上向きにはたらく。  
- 物体 A について：
  - 斜面下向きを正とする運動方程式：$m a_2 = mg\sin\theta - T_2 - \mu N \quad \cdots\text{④}$
  - 斜面に垂直な方向のつりあい：$N = mg\cos\theta \quad \cdots\text{⑤}$
- 物体 B について：
  - 鉛直上向きを正とする運動方程式：$M_2 a_2 = T_2 - M_2 g \quad \cdots\text{⑥}$

④ $+$ ⑥ より $T_2$ を消去し，⑤ を代入すると，
$$(M_2 + m)a_2 = mg\sin\theta - \mu mg\cos\theta - M_2 g$$
$$\therefore a_2 = \frac{m(\sin\theta - \mu\cos\theta) - M_2}{M_2 + m}g$$
これを ⑥ の $T_2 = M_2(g + a_2)$ に代入すると，
$$T_2 = M_2 g \left\{1 + \frac{m(\sin\theta - \mu\cos\theta) - M_2}{M_2 + m}\right\} = \frac{M_2 m(1 + \sin\theta - \mu\cos\theta)}{M_2 + m}g$$

> 💡 讲师批注：对比 (2) 和 (3) 的张力公式：只要把 $+\mu\cos\theta$ 换成 $-\mu\cos\theta$（以及 $M_1 \to M_2$），结构完全镜像对称！这是极佳的考场验算手段。

#### 【最终答案】
- **(1) $m(\sin\theta - \mu_0\cos\theta) \le M_0 \le m(\sin\theta + \mu_0\cos\theta)$**
- **(2) $a_1 = \dfrac{M_1 - m(\sin\theta + \mu\cos\theta)}{M_1 + m}g$，$T_1 = \dfrac{M_1 m(1 + \sin\theta + \mu\cos\theta)}{M_1 + m}g$**
- **(3) $a_2 = \dfrac{m(\sin\theta - \mu\cos\theta) - M_2}{M_2 + m}g$，$T_2 = \dfrac{M_2 m(1 + \sin\theta - \mu\cos\theta)}{M_2 + m}g$**

---

### 例題 5（教材 P.25 / 页码 24）：空気抵抗を受ける物体の運動（受空气阻力下落的终端速度）

#### 【原题重现与翻译】
> **日文原题**：  
> 質量 $m\text{ [kg]}$ の球を初速度 $0$ で落下させる。球の速さが $v\text{ [m/s]}$ のとき $kv\text{ [N]}$（$k$：比例定数）の抵抗力を空気から受けるものとして問いに答えよ。ただし，重力加速度の大きさを $g\text{ [m/s}^2]$ とする。  
> (1) 球の速さが $v\text{ [m/s]}$ となった瞬間の加速度の大きさを求めよ。  
> (2) 十分時間が経過すると，球の速さは一定になる。このときの速さ $v_f$ を求めよ。  
> (3) 球の $v$-$t$ 図の概形を描け。
>
> **中文翻译**：  
> 让质量为 $m\text{ [kg]}$ 的小球由初速度 $0$ 开始下落。当小球速率为 $v\text{ [m/s]}$ 时，受到空气施加的大小为 $kv\text{ [N]}$（$k$ 为比例常数）的阻力。取重力加速度大小为 $g\text{ [m/s}^2]$，回答以下问题：  
> (1) 求小球速率达到 $v\text{ [m/s]}$ 瞬间的加速度大小。  
> (2) 经过足够长时间后，小球速率趋于恒定，求此时的速率 $v_f$。  
> (3) 画出小球的 $v$-$t$ 图像概形。

#### 【考点与模型定位】
**变加速直线运动与终端速度（終端速度）模型**（EJU 图像选择题高频考点：重点抓 $v$-$t$ 图的**原点切线斜率 $g$** 与**水平渐近线 $v_f = mg/k$**）。

#### 【多色矢量图解（SVG）】

<svg viewBox="0 0 420 260" width="420" height="260" xmlns="http://www.w3.org/2000/svg" style="background:#fafafa;border:1px solid #e5e7eb;border-radius:8px;">
  <defs>
    <marker id="arr-blue-002-5" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0,0 L0,6 L7,3 z" fill="#2563eb"/></marker>
    <marker id="arr-red-002-5" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0,0 L0,6 L7,3 z" fill="#dc2626"/></marker>
    <marker id="arr-blk-002-5" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0,0 L0,6 L7,3 z" fill="#111827"/></marker>
  </defs>
  <!-- 左侧：受力对比（加速中 vs 终端速度） -->
  <text x="18" y="22" font-size="11" font-weight="bold" fill="#374151">(1) 加速中</text>
  <circle cx="52" cy="115" r="11" fill="#dbeafe" stroke="#1e40af" stroke-width="1.5"/>
  <circle cx="52" cy="115" r="2.5" fill="#1e3a8a"/>
  <line x1="52" y1="126" x2="52" y2="195" stroke="#2563eb" stroke-width="2.2" marker-end="url(#arr-blue-002-5)"/>
  <text x="58" y="190" font-size="11" fill="#2563eb">mg</text>
  <line x1="52" y1="104" x2="52" y2="68" stroke="#dc2626" stroke-width="2" marker-end="url(#arr-red-002-5)"/>
  <text x="58" y="76" font-size="11" fill="#dc2626">kv</text>
  <!-- 加速度 a -->
  <line x1="26" y1="95" x2="26" y2="145" stroke="#111827" stroke-width="1.8" stroke-dasharray="5,3" marker-end="url(#arr-blk-002-5)"/>
  <text x="14" y="124" font-size="11" fill="#111827">a</text>

  <text x="108" y="22" font-size="11" font-weight="bold" fill="#374151">(2) 終端 (a=0)</text>
  <circle cx="135" cy="115" r="11" fill="#fef3c7" stroke="#b45309" stroke-width="1.5"/>
  <circle cx="135" cy="115" r="2.5" fill="#92400e"/>
  <line x1="135" y1="126" x2="135" y2="195" stroke="#2563eb" stroke-width="2.2" marker-end="url(#arr-blue-002-5)"/>
  <text x="141" y="190" font-size="11" fill="#2563eb">mg</text>
  <line x1="135" y1="104" x2="135" y2="35" stroke="#dc2626" stroke-width="2.2" marker-end="url(#arr-red-002-5)"/>
  <text x="141" y="48" font-size="11" fill="#dc2626">kv_f</text>
  <text x="106" y="220" font-size="10" fill="#374151">mg = kv_f</text>

  <!-- 分隔线 -->
  <line x1="184" y1="16" x2="184" y2="245" stroke="#d1d5db" stroke-dasharray="4,4"/>

  <!-- 右侧：(3) v-t 图 -->
  <text x="200" y="22" font-size="11" font-weight="bold" fill="#374151">(3) v-t 図の概形</text>
  <!-- 坐标轴 -->
  <line x1="220" y1="215" x2="400" y2="215" stroke="#374151" stroke-width="1.8" marker-end="url(#arr-blk-002-5)"/>
  <text x="396" y="232" font-size="12" font-style="italic" fill="#111827">t</text>
  <line x1="220" y1="225" x2="220" y2="42" stroke="#374151" stroke-width="1.8" marker-end="url(#arr-blk-002-5)"/>
  <text x="205" y="48" font-size="12" font-style="italic" fill="#111827">v</text>
  <text x="206" y="228" font-size="11" fill="#374151">O</text>
  <!-- 渐近线 v = mg/k -->
  <line x1="220" y1="105" x2="392" y2="105" stroke="#dc2626" stroke-width="1.4" stroke-dasharray="5,4"/>
  <text x="188" y="102" font-size="10" font-weight="bold" fill="#dc2626">mg</text>
  <line x1="188" y1="105" x2="208" y2="105" stroke="#dc2626" stroke-width="1"/>
  <text x="195" y="116" font-size="10" font-weight="bold" fill="#dc2626">k</text>
  <!-- 原点切线 v = gt -->
  <line x1="220" y1="215" x2="290" y2="45" stroke="#6b7280" stroke-width="1.3" stroke-dasharray="4,3"/>
  <text x="292" y="55" font-size="10" fill="#6b7280">v = gt (傾き g)</text>
  <!-- 指数趋近曲线 -->
  <path d="M 220 215 C 245 154, 275 112, 390 107" fill="none" stroke="#111827" stroke-width="2.4"/>
  <text x="265" y="160" font-size="10" fill="#111827">傾き(加速度)が</text>
  <text x="265" y="173" font-size="10" fill="#111827">次第に 0 に近づく</text>
</svg>

#### 【日本考场规范分步解答】

**(1)** 鉛直下向きを正とし，速さ $v$ の瞬間の加速度を $a$ とすると，運動方程式より，
$$ma = mg - kv$$
よって，
$$a = g - \frac{kv}{m}\text{ [m/s}^2]$$

**(2)** 速さが一定になったとき加速度 $a = 0$ であるから，(1) の式より，
$$0 = g - \frac{k v_f}{m} \implies v_f = \frac{mg}{k}\text{ [m/s]}$$
（**別解**：力のつりあい $mg = k v_f$ より $v_f = \dfrac{mg}{k}\text{ [m/s]}$）

**(3)** $t = 0$ では $v = 0$ より $a = g$（グラフの原点における接線の傾きは $g$，すなわち直線 $v = gt$ に接する）。時間が経つにつれて $v$ が増加し，加速度 $a = g - \dfrac{kv}{m}$（グラフの傾き）は次第に小さくなり，最終的に水平な漸近線 $v = \dfrac{mg}{k}$ に近づく（上図の右グラフ）。

> 💡 讲师批注：画 $v$-$t$ 概形图时，日本考场给分点有 3 个：① 过原点且原点处切线为 $v = gt$（不能画成先平后陡）；② 曲线单调递增且上凸（斜率渐减）；③ 标明水平渐近线数值 $\dfrac{mg}{k}$。顺便科普：雨滴落地不会砸死人，正是因为空气阻力使其达到了恒定的**终端速度（終端速度）**。

#### 【最终答案】
- **(1) $a = g - \dfrac{kv}{m}\text{ [m/s}^2]$**
- **(2) $v_f = \dfrac{mg}{k}\text{ [m/s]}$**
- **(3) 原点を通過し，接線 $v = gt$ から始まり漸近線 $v = \dfrac{mg}{k}$ に近づく上に凸の曲線（上図参照）**

---

### 例題 6（教材 P.28 / 页码 27）：仕事とエネルギーの関係（粗糙斜面往返的功能关系）

#### 【原题重现与翻译】
> **日文原题**：  
> 傾斜角 $30^\circ$ のあらい斜面上の最下点 $\text{O}$ に質量 $m$ の物体をおいて斜面上向きの初速度 $v_0$ を与えたところ，点 $\text{A}$ まですべり上がった後に再び最下点 $\text{O}$ まで戻ってきた。物体と斜面の間の動摩擦係数を $\mu$，重力加速度の大きさを $g$ とする。  
> (1) 斜面に沿ってすべり上がった距離 $x$ を求めよ。  
> (2) 再び最下点 $\text{O}$ に戻ってきたときの速さ $v_1$ を求めよ。
>
> **中文翻译**：  
> 在倾角为 $30^\circ$ 的粗糙斜面最底端 $\text{O}$ 处放置质量为 $m$ 的物体，赋予其沿斜面向上的初速度 $v_0$。物体沿斜面滑行至最高点 $\text{A}$ 后，又滑回最底端 $\text{O}$。设物体与斜面间的动摩擦系数为 $\mu$，重力加速度大小为 $g$。  
> (1) 求物体沿斜面上滑的距离 $x$。  
> (2) 求物体再次滑回最底端 $\text{O}$ 时的速率 $v_1$。

#### 【考点与模型定位】
**含滑动摩擦力的往返功能关系模型**（核心公式：`初机械能 + 非保守力做功 = 末机械能`；牢记无论上滑还是下滑，滑动摩擦力永远做**负功**！）。

#### 【多色矢量图解（SVG）】

<svg viewBox="0 0 420 260" width="420" height="260" xmlns="http://www.w3.org/2000/svg" style="background:#fafafa;border:1px solid #e5e7eb;border-radius:8px;">
  <defs>
    <marker id="arr-blue-002-6" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0,0 L0,6 L7,3 z" fill="#2563eb"/></marker>
    <marker id="arr-green-002-6" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0,0 L0,6 L7,3 z" fill="#16a34a"/></marker>
    <marker id="arr-red-002-6" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0,0 L0,6 L7,3 z" fill="#dc2626"/></marker>
    <marker id="arr-blk-002-6" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0,0 L0,6 L7,3 z" fill="#111827"/></marker>
  </defs>
  <!-- 斜面 (倾角 30°) -->
  <polygon points="45,220 355,220 355,41" fill="#f3f4f6" stroke="#374151" stroke-width="2"/>
  <path d="M 92 220 A 47 47 0 0 0 86 196" fill="none" stroke="#dc2626" stroke-width="1.5"/>
  <text x="95" y="213" font-size="11" fill="#dc2626">30°</text>
  <text x="36" y="236" font-size="12" font-weight="bold" fill="#111827">O (h=0)</text>

  <!-- 最高点 A -->
  <g transform="translate(270, 90) rotate(-30)">
    <rect x="-18" y="-22" width="36" height="22" fill="#fef3c7" stroke="#b45309" stroke-width="1.5" stroke-dasharray="3,2"/>
  </g>
  <text x="260" y="54" font-size="11" font-weight="bold" fill="#92400e">A (v = 0)</text>
  <!-- 高度 h = x/2 标注 -->
  <line x1="270" y1="90" x2="270" y2="220" stroke="#6b7280" stroke-width="1.2" stroke-dasharray="4,3"/>
  <text x="276" y="160" font-size="11" fill="#374151">h = x sin30° = x/2</text>

  <!-- 上滑过程物体（中段） -->
  <g transform="translate(155, 156) rotate(-30)">
    <rect x="-18" y="-22" width="36" height="22" fill="#dbeafe" stroke="#1e40af" stroke-width="1.5"/>
    <!-- 支持力 N -->
    <line x1="0" y1="-22" x2="0" y2="-65" stroke="#16a34a" stroke-width="2" marker-end="url(#arr-green-002-6)"/>
    <text x="6" y="-56" font-size="11" font-weight="bold" fill="#16a34a">N</text>
    <!-- 上滑摩擦力 μN (向下) -->
    <line x1="-18" y1="-2" x2="-60" y2="-2" stroke="#dc2626" stroke-width="2" marker-end="url(#arr-red-002-6)"/>
    <text x="-76" y="-10" font-size="10" fill="#dc2626">上り: μN</text>
    <!-- 上滑初速箭头 -->
    <line x1="-10" y1="-36" x2="36" y2="-36" stroke="#111827" stroke-width="1.8" stroke-dasharray="5,3" marker-end="url(#arr-blk-002-6)"/>
    <text x="12" y="-42" font-size="11" fill="#111827">v₀ (上り)</text>
    <!-- 距离 x 标注 -->
    <text x="48" y="-54" font-size="11" font-weight="bold" fill="#374151">距離 x</text>
  </g>
  <!-- 重力 mg -->
  <line x1="150" y1="146" x2="150" y2="205" stroke="#2563eb" stroke-width="2.2" marker-end="url(#arr-blue-002-6)"/>
  <text x="156" y="200" font-size="11" font-weight="bold" fill="#2563eb">mg</text>

  <!-- 下滑回 O 速度标注 -->
  <line x1="110" y1="195" x2="64" y2="222" stroke="#111827" stroke-width="1.8" stroke-dasharray="5,3" marker-end="url(#arr-blk-002-6)"/>
  <text x="58" y="188" font-size="11" fill="#111827">v₁ (下り)</text>
  <text x="16" y="22" font-size="10" fill="#dc2626">※ 上りも下りも動摩擦力 μN = μmgcos30° は常に負の仕事 (-μNx)</text>
</svg>

#### 【日本考场规范分步解答】

最下点 $\text{O}$ を重力による位置エネルギーの基準面（$h = 0$）とする。  
斜面に垂直な方向の力のつりあいより，垂直抗力は $N = mg\cos 30^\circ$ であるから，動摩擦力の大きさは $\mu N = \mu mg\cos 30^\circ$ である。  
また，点 $\text{A}$ の高さは $h = x\sin 30^\circ = \dfrac{x}{2}$ である。

**(1)** 点 $\text{O}$ から点 $\text{A}$ までの運動について，仕事とエネルギーの関係  
$$(\text{最初の力学的エネルギー}) + (\text{非保存力がした仕事}) = (\text{最後の力学的エネルギー})$$
より，
$$\frac{1}{2}mv_0^2 + 0 + (-\mu mg\cos 30^\circ \cdot x) = 0 + mg \cdot \frac{x}{2}$$
$\cos 30^\circ = \dfrac{\sqrt{3}}{2}$ を代入して両辺を $\dfrac{m}{2}$ で割ると，
$$v_0^2 - \sqrt{3}\mu gx = gx \implies (1 + \sqrt{3}\mu)gx = v_0^2$$
$$\therefore x = \frac{v_0^2}{(1 + \sqrt{3}\mu)g}$$

> 💡 讲师批注：用能量关系列式比“牛顿第二定律求加速度 $a$ $\to$ $v^2 - v_0^2 = 2ax$”更加通用且不易漏项！切记把**滑动摩擦力做的负功 $-\mu mg\cos 30^\circ \cdot x$** 写在等式左边（或理解为初机械能减去克服摩擦做的功等于末机械能）。

**(2)** 点 $\text{A}$ から点 $\text{O}$ に戻るまでの運動について，仕事とエネルギーの関係より，
$$0 + mg \cdot \frac{x}{2} + (-\mu mg\cos 30^\circ \cdot x) = \frac{1}{2}mv_1^2 + 0$$
両辺を $\dfrac{m}{2}$ で割り，$\cos 30^\circ = \dfrac{\sqrt{3}}{2}$ を代入すると，
$$v_1^2 = gx - \sqrt{3}\mu gx = (1 - \sqrt{3}\mu)gx$$
これに (1) の $x = \dfrac{v_0^2}{(1 + \sqrt{3}\mu)g}$ を代入して，
$$v_1^2 = \frac{1 - \sqrt{3}\mu}{1 + \sqrt{3}\mu}\,v_0^2$$
$v_1 > 0$ より，
$$v_1 = \sqrt{\frac{1 - \sqrt{3}\mu}{1 + \sqrt{3}\mu}}\,v_0$$

> 💡 讲师批注：验算技巧：① 当光滑（$\mu = 0$）时，$v_1 = v_0$，完美符合机械能守恒！② 根号内 $1 - \sqrt{3}\mu > 0 \iff \mu < \frac{1}{\sqrt{3}} = \tan 30^\circ$，正好对应物体能自行滑下来的物理条件！③ 也可直接对全过程 $\text{O} \to \text{A} \to \text{O}$ 列式：$\frac{1}{2}mv_0^2 - 2\mu mg\cos 30^\circ \cdot x = \frac{1}{2}mv_1^2$，一步直达同一结果。

#### 【最终答案】
- **(1) $x = \dfrac{v_0^2}{(1 + \sqrt{3}\mu)g}$**
- **(2) $v_1 = \sqrt{\dfrac{1 - \sqrt{3}\mu}{1 + \sqrt{3}\mu}}\,v_0$**

---

### 例題 7（教材 P.30 / 页码 29）：水平面上の 2 物体の斜め衝突（等质量二维弹性斜碰）

#### 【原题重现与翻译】
> **日文原题**：  
> なめらかな水平面上を $x$ 軸の正方向に速さ $v$ で進んできた質量 $m$ の物体 A が原点 $\text{O}$ で同じ質量 $m$ の物体 B と弾性衝突し，物体 A は $x$ 軸の正方向から反時計回りに $60^\circ$ の方向，物体 B は $x$ 軸の正方向から時計回りに $\theta\ (0^\circ < \theta < 90^\circ)$ の方向へ進んだ。衝突後の物体 A，B の速さ $V_A, V_B$ と $\theta$ を求めよ。
>
> **中文翻译**：  
> 在光滑水平面上，质量为 $m$ 的物体 A 沿 $x$ 轴正方向以速率 $v$ 运动，在原点 $\text{O}$ 与静止的相同质量 $m$ 的物体 B 发生弹性碰撞。碰撞后，物体 A 沿 $x$ 轴正方向逆时针旋转 $60^\circ$ 的方向运动，物体 B 沿 $x$ 轴正方向顺时针旋转 $\theta\ (0^\circ < \theta < 90^\circ)$ 的方向运动。求碰撞后物体 A、B 的速率 $V_A, V_B$ 以及角度 $\theta$。

#### 【考点与模型定位】
**二维弹性斜碰模型（台球碰撞）**（平面动量守恒分量分解 $+$ 弹性碰撞动能守恒；同时掌握 EJU 考场必背二级结论：**等质量一静一动弹性斜碰，碰后速度夹角必为 $90^\circ$**）。

#### 【多色矢量图解（SVG）】

<svg viewBox="0 0 420 260" width="420" height="260" xmlns="http://www.w3.org/2000/svg" style="background:#fafafa;border:1px solid #e5e7eb;border-radius:8px;">
  <defs>
    <marker id="arr-blk-002-7" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0,0 L0,6 L7,3 z" fill="#111827"/></marker>
    <marker id="arr-blue-002-7" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0,0 L0,6 L7,3 z" fill="#2563eb"/></marker>
    <marker id="arr-red-002-7" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0,0 L0,6 L7,3 z" fill="#dc2626"/></marker>
  </defs>
  <!-- 坐标轴 -->
  <line x1="25" y1="150" x2="385" y2="150" stroke="#4b5563" stroke-width="1.6" marker-end="url(#arr-blk-002-7)"/>
  <text x="388" y="154" font-size="12" font-style="italic" fill="#111827">x</text>
  <line x1="140" y1="242" x2="140" y2="20" stroke="#4b5563" stroke-width="1.6" marker-end="url(#arr-blk-002-7)"/>
  <text x="124" y="28" font-size="12" font-style="italic" fill="#111827">y</text>

  <!-- 碰前 A 球 -->
  <circle cx="55" cy="150" r="10" fill="#dbeafe" stroke="#1e40af" stroke-width="1.5"/>
  <text x="51" y="154" font-size="11" font-weight="bold" fill="#1e3a8a">A</text>
  <line x1="67" y1="150" x2="112" y2="150" stroke="#111827" stroke-width="2" stroke-dasharray="5,3" marker-end="url(#arr-blk-002-7)"/>
  <text x="84" y="140" font-size="11" font-weight="bold" fill="#111827">v</text>

  <!-- 原点静止 B 球 -->
  <circle cx="140" cy="150" r="10" fill="#fef3c7" stroke="#b45309" stroke-width="1.5"/>
  <text x="136" y="154" font-size="11" font-weight="bold" fill="#92400e">B</text>
  <text x="122" y="172" font-size="10" fill="#374151">O (静止)</text>

  <!-- 碰后 A 球 (60° 方向) -->
  <line x1="145" y1="141" x2="195" y2="55" stroke="#111827" stroke-width="1.8" stroke-dasharray="5,3" marker-end="url(#arr-blk-002-7)"/>
  <circle cx="195" cy="55" r="9" fill="#dbeafe" stroke="#1e40af" stroke-width="1.5"/>
  <text x="191" y="59" font-size="10" font-weight="bold" fill="#1e3a8a">A</text>
  <text x="208" y="52" font-size="11" font-weight="bold" fill="#111827">V_A</text>
  <!-- A 速度分解 -->
  <line x1="195" y1="55" x2="230" y2="55" stroke="#2563eb" stroke-width="1.4" stroke-dasharray="3,2" marker-end="url(#arr-blue-002-7)"/>
  <text x="234" y="59" font-size="10" fill="#2563eb">V_A cos60°</text>
  <line x1="195" y1="55" x2="195" y2="20" stroke="#2563eb" stroke-width="1.4" stroke-dasharray="3,2" marker-end="url(#arr-blue-002-7)"/>
  <text x="202" y="28" font-size="10" fill="#2563eb">V_A sin60°</text>
  <!-- 60° 弧 -->
  <path d="M 172 150 A 32 32 0 0 0 156 122" fill="none" stroke="#dc2626" stroke-width="1.5"/>
  <text x="170" y="132" font-size="11" fill="#dc2626">60°</text>

  <!-- 碰后 B 球 (θ = 30° 方向) -->
  <line x1="149" y1="155" x2="265" y2="222" stroke="#111827" stroke-width="1.8" stroke-dasharray="5,3" marker-end="url(#arr-blk-002-7)"/>
  <circle cx="265" cy="222" r="9" fill="#fef3c7" stroke="#b45309" stroke-width="1.5"/>
  <text x="261" y="226" font-size="10" font-weight="bold" fill="#92400e">B</text>
  <text x="278" y="238" font-size="11" font-weight="bold" fill="#111827">V_B</text>
  <!-- B 速度分解 -->
  <line x1="265" y1="222" x2="325" y2="222" stroke="#2563eb" stroke-width="1.4" stroke-dasharray="3,2" marker-end="url(#arr-blue-002-7)"/>
  <text x="328" y="226" font-size="10" fill="#2563eb">V_B cosθ</text>
  <line x1="265" y1="222" x2="265" y2="255" stroke="#2563eb" stroke-width="1.4" stroke-dasharray="3,2" marker-end="url(#arr-blue-002-7)"/>
  <text x="202" y="248" font-size="10" fill="#2563eb">V_B sinθ</text>
  <!-- θ 弧 -->
  <path d="M 180 150 A 40 40 0 0 1 175 170" fill="none" stroke="#dc2626" stroke-width="1.5"/>
  <text x="184" y="166" font-size="11" fill="#dc2626">θ</text>

  <!-- 右上角二级结论提示框 -->
  <rect x="275" y="75" width="132" height="52" rx="6" fill="#fff" stroke="#d1d5db" stroke-width="1.2"/>
  <text x="283" y="93" font-size="10" font-weight="bold" fill="#dc2626">同質量弾性斜め衝突</text>
  <text x="283" y="108" font-size="10" fill="#374151">v² = V_A² + V_B² より</text>
  <text x="283" y="121" font-size="10" font-weight="bold" fill="#111827">60° + θ = 90° (直交!)</text>
</svg>

#### 【日本考场规范分步解答】

- $x$ 軸方向の運動量保存則より，
  $$mv = mV_A\cos 60^\circ + mV_B\cos\theta \implies v = \frac{1}{2}V_A + V_B\cos\theta \quad \cdots\text{①}$$
- $y$ 軸方向の運動量保存則より，
  $$0 = mV_A\sin 60^\circ + m(-V_B\sin\theta) \implies V_B\sin\theta = \frac{\sqrt{3}}{2}V_A \quad \cdots\text{②}$$
- 弾性衝突であるから力学的エネルギー保存則が成り立ち，
  $$\frac{1}{2}mv^2 = \frac{1}{2}mV_A^2 + \frac{1}{2}mV_B^2 \implies v^2 = V_A^2 + V_B^2 \quad \cdots\text{③}$$

① より $V_B\cos\theta = v - \dfrac{1}{2}V_A$。これと ② の両辺をそれぞれ 2 乗して足し合わせ，$\cos^2\theta + \sin^2\theta = 1$ を用いると，
$$V_B^2 = \left(v - \frac{1}{2}V_A\right)^2 + \left(\frac{\sqrt{3}}{2}V_A\right)^2 = v^2 - vV_A + \frac{1}{4}V_A^2 + \frac{3}{4}V_A^2 = v^2 - vV_A + V_A^2$$
これに ③ の $V_B^2 = v^2 - V_A^2$ を代入すると，
$$v^2 - V_A^2 = v^2 - vV_A + V_A^2 \implies 2V_A^2 - vV_A = 0 \implies V_A(2V_A - v) = 0$$
衝突後 $V_A > 0$ であるから，
$$V_A = \frac{1}{2}v$$
これを ③ に代入すると，$V_B^2 = v^2 - \dfrac{1}{4}v^2 = \dfrac{3}{4}v^2$。$V_B > 0$ より，
$$V_B = \frac{\sqrt{3}}{2}v$$
最後に ② に代入すると，
$$\sin\theta = \frac{\sqrt{3}V_A}{2V_B} = \frac{\sqrt{3} \cdot \frac{1}{2}v}{2 \cdot \frac{\sqrt{3}}{2}v} = \frac{1}{2}$$
$0^\circ < \theta < 90^\circ$ より，
$$\theta = 30^\circ$$

> 💡 讲师批注：**EJU 选择题 5 秒秒杀大法**！由动量守恒矢量式 $\vec{v} = \vec{V}_A + \vec{V}_B$ 与能量守恒 $v^2 = V_A^2 + V_B^2$（勾股定理！）可知，矢量 $\vec{V}_A, \vec{V}_B, \vec{v}$ 必构成一个以 $v$ 为斜边的**直角三角形**！因此碰后两球速度方向**必然互相垂直**：$60^\circ + \theta = 90^\circ \implies \theta = 30^\circ$，紧接着由直角三角形边角关系直接口算 $V_A = v\cos 60^\circ = \frac{1}{2}v$，$V_B = v\sin 60^\circ = \frac{\sqrt{3}}{2}v$！

#### 【最终答案】
- **$V_A = \dfrac{1}{2}v$，$V_B = \dfrac{\sqrt{3}}{2}v$，$\theta = 30^\circ$**

---

## 4. 全局术语表同步说明

本切片新增的 **46 条** 日文物理核心术语与假名注音（已与切片 001 去重）已写入 [.glossary_002.md](file:///Users/baohan/Desktop/EJU/notes_物理/.glossary_002.md)，供主控合并至全局术语表 [glossary_all.md](file:///Users/baohan/Desktop/EJU/notes_物理/glossary_all.md)。
