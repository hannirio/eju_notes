# EJU 物理全解讲义 — 切片 003（P.31–P.45）
> **对应教材章节**：物理基礎・第一章 物体の運動（衝突の応用、慣性力、等速円運動・円錐振り子・鉛直円運動、単振動・ばね振り子・単振り子・浮力と単振動、万有引力とケプラーの法則）＋ 第二章 熱とエネルギー（熱と温度）  
> **适用对象**：需快速唤醒中国高中物理力学压轴与热学入门基础、并掌握纯日文板书与 EJU 考场规范表达的授课教师 / 考生

---

## 1. 本节前置：国内高中物理基础唤醒

本切片是**整个 EJU 力学部分的压轴核心**（动量能量综合、非惯性系、圆周运动、简谐振动、万有引力）与**热学开篇**（热与温度），在 EJU 物理真题中占比极高。

### 1.1 碰撞进阶与动量能量综合

1. **子弹打木块模型（木片に撃ち込まれた弾丸）**
   - **水平方向动量守恒**：无外力，最终共速 $V = \dfrac{m}{M+m}v$。
   - **时间 $\Delta t$**：对木块（或子弹）单独列动量定理（力積と運動量の関係），$F\Delta t = MV - 0$。
   - **打入深度 $x$（相对位移）**：系统内一对滑动阻力做功之和等于系统机械能的减少量（转化为热能）：
     $$-Fx = \frac{1}{2}(M+m)V^2 - \frac{1}{2}mv^2 \implies Fx = \frac{1}{2}\cdot\frac{Mm}{M+m}v^2$$
     > 口诀：**摩擦力 $\times$ 相对位移 $=$ 系统损失的动能**（约化质量公式 $\Delta E_k = \dfrac{1}{2}\mu v_{\text{相}}^2$，其中 $\mu = \dfrac{Mm}{M+m}$）。

2. **地面反弹与光滑平面斜碰（床との衝突・斜め衝突）**
   - **竖直自由落体反弹**：从高度 $h$ 自由下落，撞地前速度 $v = \sqrt{2gh}$，反弹速度大小 $|v'| = ev$，反弹最大高度 $h' = e^2 h$，上升时间 $t' = et$。
   - **光滑水平面斜碰**：平行于接触面方向不受冲量，分速度不变（$v_x' = v_x$）；垂直于接触面方向按恢复系数反弹（$v_y' = -ev_y$）。
   - **反复斜碰**：每次弹跳的最高高度呈公比 $e^2$ 的等比数列（$h, e^2 h, e^4 h, \dots$），每次腾空时间与水平射程呈公比 $e$ 的等比数列（$t, et, e^2 t, \dots$；$l, el, e^2 l, \dots$）。

3. **弹簧连接体碰撞（ばねのついた物体との衝突）**
   - **弹簧最短（或最长）瞬间**：两物体**速度相等**（$v_A = v_B = V$），系统动能最小、弹性势能最大。
   - **分离瞬间**：弹簧恢复原长，整个过程动量守恒 $+$ 机械能守恒，等价于**一维完全弹性碰撞**（$e = 1$），可直接套用恢复系数公式速解。

### 1.2 惯性力、等效重力与圆周运动

1. **惯性力（慣性力）与等效重力加速度（見かけの重力加速度）**
   - 当观察者随参考系以加速度 $\vec{a}$ 运动时，在非惯性系中物体会多出一个假想的惯性力：
     $$\vec{F}_{\text{慣性}} = -m\vec{a} \quad \text{（方向与参考系加速度相反）}$$
   - **等效重力**：将真实重力 $m\vec{g}$ 与恒定惯性力 $-m\vec{a}$ 合成，得 $m\vec{g}' = m(\vec{g} - \vec{a})$。在加速车厢或电梯中，单摆平衡方向、自由释放轨迹、浮力方向（如氦气球向加速方向倾斜！）全部按等效重力场 $\vec{g}'$ 处理。

2. **匀速圆周运动（等速円運動）核心公式**
   - 角速度 $\omega = \dfrac{\theta}{t}$、线速度 $v = r\omega$、周期 $T = \dfrac{2\pi r}{v} = \dfrac{2\pi}{\omega}$、转速 $n = \dfrac{1}{T}$。
   - 向心加速度 $a = \dfrac{v^2}{r} = r\omega^2$，向心力 $F = ma = m\dfrac{v^2}{r} = mr\omega^2$（指向圆心）。
   - **离心力（遠心力）**：随物体一起转动的观察者视角下的惯性力，大小 $f = m\dfrac{v^2}{r} = mr\omega^2$，方向**背离圆心**，可将圆周动力学问题转化为静力学平衡问题！

3. **竖直面内圆周运动最高点临界条件**
   - **轻绳模型（糸）**：绳只能拉不能推，最高点 $T \ge 0 \implies v_{\text{高}} \ge \sqrt{gl}$，由机械能守恒得最低点 $v_0 \ge \sqrt{5gl}$。
   - **轻杆模型（棒）**：杆既能拉也能撑，完成完整圆周运动只需越过最高点，即 $v_{\text{高}} > 0 \implies v_0 > 2\sqrt{gl}$（若仅问“到达最高点”则为 $v_0 \ge 2\sqrt{gl}$）。

### 1.3 简谐振动（単振動）三大模型

1. **简谐振动标准判据与万能周期公式**
   - 只要物体所受合力满足回复力形式 $F = -Kx$（即加速度 $a = -\dfrac{K}{m}x = -\omega^2 x$），物体即做简谐振动：
     $$\omega = \sqrt{\frac{K}{m}}, \qquad T = \frac{2\pi}{\omega} = 2\pi\sqrt{\frac{m}{K}}$$
   - **运动学方程**（初相为 0 时）：$x = A\sin\omega t$，$v = A\omega\cos\omega t$，$a = -A\omega^2\sin\omega t = -\omega^2 x$。
   - **极值规律**：平衡位置（振動中心）速率最大 $v_{\max} = A\omega$、加速度 $a = 0$；两端点（振動両端）速度 $v = 0$、加速度最大 $a_{\max} = A\omega^2$。
   - **参考圆求时间法**：将简谐振动视为半径为 $A$、角速度为 $\omega$ 的匀速圆周运动的投影，求任意两点间时间只需看圆心角 $\Delta\theta$，则 $t = \dfrac{\Delta\theta}{2\pi}T$。

2. **三大经典简谐振动模型**
   - **竖直弹簧振子（鉛直ばね振り子）**：以静平衡位置（$kl = mg$）为原点，重力与平衡伸长弹力恰好抵消，回复力仍为 $F = -kx$，周期 $T = 2\pi\sqrt{\dfrac{m}{k}} = 2\pi\sqrt{\dfrac{l}{g}}$（与水平弹簧振子完全相同，且可直接用 $\frac{1}{2}mv^2 + \frac{1}{2}kx^2 = \text{const}$ 进行振动能量守恒计算！）。
   - **单摆（単振り子）**：小角度近似 $\sin\theta \approx \dfrac{x}{l}$，回复力 $F = -\dfrac{mg}{l}x$，周期 $T = 2\pi\sqrt{\dfrac{l}{g}}$；在非惯性系中只需将 $g$ 替换为等效重力加速度 $g'$。
   - **浮力简谐振动（浮力と単振動）**：漂浮柱体向下偏离平衡位置 $x$ 时，多排开水产生额外浮力 $\Delta F = \rho_0 S g x$，故等效劲度系数 $K = \rho_0 S g$，周期 $T = 2\pi\sqrt{\dfrac{m}{\rho_0 S g}} = 2\pi\sqrt{\dfrac{\rho L}{\rho_0 g}}$。

### 1.4 万有引力与开普勒定律

1. **万有引力定律**：$F = G\dfrac{m_1 m_2}{r^2}$，其中 $G = 6.67 \times 10^{-11}\text{ N}\cdot\text{m}^2/\text{kg}^2$。
2. **万有引力势能**：取无穷远处（無限遠）为零势能面，$U = -G\dfrac{Mm}{r}$（恒为负值）。
3. **黄金代换公式**：忽略地球自转离心力，地表 $mg = G\dfrac{Mm}{R^2} \implies GM = gR^2$。
4. **开普勒三定律（ケプラーの法則）**：
   - 第一定律：行星在以太阳为一个焦点的椭圆轨道上运动；
   - 第二定律：面积速度一定（$\dfrac{1}{2}r v \sin\theta = \text{const}$，近日点与远日点有 $r_1 v_1 = r_2 v_2$）；
   - 第三定律：$\dfrac{T^2}{a^3} = k$（$a$ 为椭圆半长轴，$k = \dfrac{4\pi^2}{GM}$ 仅由中心天体质量决定）。

### 1.5 热力学开篇：热与温度

1. **绝对温度与摄氏温度**：$T\text{ [K]} = t\text{ [}^\circ\text{C]} + 273$（EJU 计算通常取 $273$ 而非 $273.15$），且温差 $\Delta T\text{ [K]} = \Delta t\text{ [}^\circ\text{C]}$。
2. **热容量（熱容量 $C$）与比热容（比熱 $c$）**：
   - 热容量 $C\text{ [J/K]}$：使**整个物体**升温 $1\text{ K}$ 所需热量，$C = mc$。
   - 比热容 $c\text{ [J/(g}\cdot\text{K)]}$：使 **$1\text{ g}$ 物质**升温 $1\text{ K}$ 所需热量。
   - 吸放热公式：$Q = C\Delta T = mc\Delta T$。
3. **热量守恒定律（熱量保存の法則）**：绝热混合达到热平衡时，$Q_{\text{失}} = Q_{\text{得}}$。

### 1.6 中日物理体系与习惯差异提醒

| 对比维度 | 中国国内高中物理习惯 | 日本 EJU / 高中物理习惯（授课必强调） |
| :--- | :--- | :--- |
| **离心力与非惯性系** | 高中阶段一般不提倡使用惯性力与离心力，一律要求地面参考系写 $F = ma$ | 日本教材与 EJU 极其推崇**惯性力（慣性力）与离心力（遠心力）**视角，常并列给出「地上の観測者（運動方程式）」与「回転中/電車内の観測者（つりあい）」两种解法。 |
| **竖直圆周轻杆临界** | 常说“能通过最高点”的条件是 $v_{\text{高}} \ge 0 \implies v_0 \ge 2\sqrt{gl}$ | 日本教材对「円運動する（做完整圆周运动）」较严谨，认为 $v_{\text{高}} = 0$ 会停在最高点，故写作 **$v_0 > 2\sqrt{gl}$**（严格大于号）。 |
| **竖直弹簧振子能量** | 需同时考虑重力势能 $mgh$ 与弹性势能 $\frac{1}{2}k(l+x)^2$ | 日本考场标配结论：以**平衡位置为原点**时，重力势能与平衡弹力功抵消，可直接写**振动能量守恒 $\frac{1}{2}mv^2 + \frac{1}{2}kx^2 = \text{const}$**，大幅省时！ |
| **比热容的基准质量** | 统一采用国际单位制 **$1\text{ kg}$**，单位 $\text{J/(kg}\cdot\text{K)}$ | 日本高中物理传统定义基准常为 **$1\text{ g}$**，单位 $\text{J/(g}\cdot\text{K)}$（如水的比热为 $4.2\text{ J/(g}\cdot\text{K)}$），审题时务必盯紧质量单位是 $\text{g}$ 还是 $\text{kg}$！ |
| **热容量 $C$ 的高频考查** | 国内高中较少单独考核热容量 $C$ | 日本 EJU 热学题极常考「容器の熱容量 $C$（量热器热容量）」，需熟练运用 $Q = C\Delta T$。 |

---

## 2. 日文物理核心词汇与公式假名注音（板书必备）

### 2.1 核心物理词汇表

#### 碰撞进阶与动量能量
- **弾丸（だんがん / dangan）** — 子弹
- **木片（もくへん / mokuhen）** — 木块
- **抵抗力（ていこうりょく / teikōryoku）** — 阻力
- **運動量保存則（うんどうりょうほぞんそく / undōryō hozonsoku）** — 动量守恒定律
- **力積（りきせき / rikiseki）** — 冲量
- **仕事とエネルギーの関係（しごととエネルギーのかんけい / shigoto to enerugī no kankei）** — 功与能的关系（动能定理）
- **力学的エネルギー保存則（りきがくてきエネルギーほぞんそく / rikigakuteki enerugī hozonsoku）** — 机械能守恒定律
- **反発係数 / はねかえり係数（はんぱつけいすう / hanpatsu keisū）** — 恢复系数（$e$）
- **斜め衝突（ななめしょうとつ / naname shōtotsu）** — 斜碰
- **エネルギー損失（エネルギーそんしつ / enerugī sonshitsu）** — 能量损失

#### 惯性力与圆周运动
- **慣性力（かんせいりょく / kanseiryoku）** — 惯性力
- **見かけの力（みかけのちから / mikake no chikara）** — 假想力 / 视在力
- **見かけの重力加速度（みかけのじゅうりょくかそくど / mikake no jūryoku kasokudo）** — 等效重力加速度（$g'$）
- **観測者（かんそくしゃ / kansokusha）** — 观察者
- **等速円運動（とうそくえんうんどう / tōsoku en'undō）** — 匀速圆周运动
- **角速度（かくそくど / kakusokudo）** — 角速度（$\omega$）
- **接線方向（せっせんほうこう / sessen hōkō）** — 切线方向
- **周期（しゅうき / shūki）** — 周期（$T$）
- **回転数（かいてんすう / kaitensū）** — 转速（$n$）
- **向心力（こうしんりょく / kōshinryoku）** — 向心力
- **遠心力（えんしんりょく / enshinryoku）** — 离心力
- **円錐振り子（えんすいふりこ / ensui furiko）** — 圆锥摆
- **母線（ぼせん / bosen）** — 母线（圆锥侧面）
- **鉛直面内の円運動（えんちょくめんないのえんうんどう / enchokumen-nai no en'undō）** — 竖直面内的圆周运动

#### 简谐振动与单摆
- **単振動（たんしんどう / tanshindō）** — 简谐振动
- **振幅（しんぷく / shinpuku）** — 振幅（$A$）
- **振動数（しんどうすう / shindōsū）** — 频率（$f$）
- **角振動数（かくしんどうすう / kakushindōsū）** — 角频率（$\omega$）
- **振動中心（しんどうちゅうしん / shindō chūshin）** — 振动中心（平衡位置）
- **復元力（ふくげんりょく / fukugenryoku）** — 回复力
- **鉛直ばね振り子（えんちょくばねふりこ / enchoku bane furiko）** — 竖直弹簧振子
- **単振り子（たんふりこ / tanfuriko）** — 单摆
- **反時計回り（はんとけいまわり / hantokeimawari）** — 逆时针方向
- **運動方程式（うんどうほうていしき / undō hōteishiki）** — 运动方程（牛顿第二定律）

#### 万有引力与天体运动
- **万有引力（ばんゆういんりょく / ban'yū inryoku）** — 万有引力
- **万有引力定数（ばんゆういんりょくていすう / ban'yū inryoku teisū）** — 万有引力常量（$G$）
- **万有引力による位置エネルギー（ばんゆういんりょくによるいちエネルギー / ban'yū inryoku ni yoru ichi enerugī）** — 万有引力势能
- **無限遠（むげんえん / mugen'en）** — 无穷远处
- **ケプラーの法則（けぷらーのほうそく / Kepurā no hōsoku）** — 开普勒定律
- **楕円（だえん / daen）** — 椭圆
- **焦点（しょうてん / shōten）** — 焦点
- **面積速度（めんせきそくど / menseki sokudo）** — 面积速度
- **公転周期（こうてんしゅうき / kōten shūki）** — 公转周期
- **長半径（ちょうはんけい / chōhankei）** — 半长轴（$a$）
- **近日点・遠日点（きんじつてん・えんじつてん / kinjitsuten / enjitsuten）** — 近日点・远日点

#### 热与温度基础
- **熱とエネルギー（ねつとエネルギー / netsu to enerugī）** — 热与能量
- **熱運動（ねつうんどう / netsu undō）** — 热运动
- **温度（おんど / ondo）** — 温度
- **絶対温度（ぜったいおんど / zettai ondo）** — 绝对温度（$T\text{ [K]}$）
- **セルシウス温度（せるしうすおんど / serushiusu ondo）** — 摄氏温度（$t\text{ [}^\circ\text{C]}$）
- **熱量（ねつりょう / netsuryō）** — 热量（$Q$）
- **熱平衡状態（ねつへいこうじょうたい / netsu heikō jōtai）** — 热平衡状态
- **熱容量（ねつようりょう / netsuyōryō）** — 热容量（$C$）
- **比熱（ひねつ / hinetsu）** — 比热容（$c$）
- **熱量保存の法則（ねつりょうほぞんのほうそく / netsuryō hozon no hōsoku）** — 热量守恒定律
- **ケルビン（けるびん / kerubin）** — 开尔文（热力学温度单位 $\text{K}$）

### 2.2 核心公式课堂口语读法（板书念法）

| 公式 | 日本课堂标准板书口语读法 |
| :--- | :--- |
| $e = -\dfrac{v'}{v} = \sqrt{\dfrac{h'}{h}}$ | 「イー・イコール、マイナス・ブイぶんのブイダッシュ、イコール、ルート・エイチぶんのエイチダッシュ」 |
| $\vec{F} = -m\vec{a}$ | 「エフ・ベクトル・イコール、マイナス・エム・エー・ベクトル」 |
| $F = m\dfrac{v^2}{r} = mr\omega^2$ | 「エフ・イコール、エム・アールぶんのブイにじょう、イコール、エム・アール・オメガにじょう」 |
| $a = -\omega^2 x$ | 「エー・イコール、マイナス・オメガにじょう・エックス」 |
| $F = -Kx$ | 「エフ・イコール、マイナス・ラージケー・エックス」 |
| $T = \dfrac{2\pi}{\omega} = 2\pi\sqrt{\dfrac{m}{K}}$ | 「ティー・イコール、オメガぶんのにパイ、イコール、にパイ・ルート・ケーぶんのエム」 |
| $T = 2\pi\sqrt{\dfrac{l}{g}}$ | 「ティー・イコール、にパイ・ルート・ジーぶんのエル」 |
| $F = G\dfrac{m_1 m_2}{r^2}$ | 「エフ・イコール、ジー・アールにじょうぶんの、エムいち・エムに」 |
| $U = -G\dfrac{Mm}{r}$ | 「ユー・イコール、マイナス・ジー・アールぶんの、ラージエム・スモールエム」 |
| $\dfrac{T^2}{a^3} = k$ | 「エーさんじょうぶんの・ティーにじょう、イコール、ケー（一定）」 |
| $Q = C\Delta T = mc\Delta T$ | 「キュー・イコール、ラージシー・デルタティー、イコール、エム・スモールシー・デルタティー」 |

---

## 3. 逐题深度解析（一题一解，不可跳步）

---

### 例題 1（教材 P.31 / 页码 30）：木片に撃ち込まれた弾丸（子弹打木块模型）

#### 【原题重现与翻译】
> **日文原题**：  
> なめらかな水平面上で静止している質量 $M$ の直方体の木片に向かって質量 $m$ の弾丸を速さ $v$ で水平に撃ち込んだところ，弾丸がある深さまで食い込んだところで一体となって動き始めた。このときまで，弾丸は木片から一定の大きさ $F$ の抵抗力を受けた。  
> (1) 一体となった後の速さ $V$ を求めよ。  
> (2) 一体となるまでの時間 $\Delta t$ を求めよ。  
> (3) 弾丸が食い込んだ深さ $x$ を求めよ。
>
> **中文翻译**：  
> 质量为 $M$ 的长方体木块静止在光滑水平面上，质量为 $m$ 的子弹以速率 $v$ 水平射入木块，当子弹嵌入一定深度后与木块成为一体共同运动。在此之前，子弹受到来自木块的恒定大小 $F$ 的阻力。  
> (1) 求二者合为一体后的共同速率 $V$。  
> (2) 求从射入到合为一体所需的时间 $\Delta t$。  
> (3) 求子弹嵌入木块的深度 $x$。

#### 【考点与模型定位】
**完全非弹性碰撞（子弹打木块模型）**：动量守恒求共速 $+$ 动量定理求作用时间 $+$ 动能定理（功能关系）求相对位移。

#### 【多色矢量图解（SVG）】

<svg viewBox="0 0 420 260" width="420" height="260" xmlns="http://www.w3.org/2000/svg" style="background:#fafafa;border:1px solid #e5e7eb;border-radius:8px;">
  <defs>
    <marker id="arr-red-003-1" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0,0 L0,6 L7,3 z" fill="#dc2626"/></marker>
    <marker id="arr-blk-003-1" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0,0 L0,6 L7,3 z" fill="#111827"/></marker>
    <marker id="arr-dim-003-1" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto"><path d="M0,0 L0,6 L6,3 z" fill="#4b5563"/></marker>
  </defs>
  <!-- 上图：碰撞前 -->
  <text x="16" y="22" font-size="11" font-weight="bold" fill="#374151">衝突前</text>
  <line x1="25" y1="105" x2="395" y2="105" stroke="#4b5563" stroke-width="2"/>
  <rect x="140" y="30" width="75" height="75" fill="#e5e7eb" stroke="#374151" stroke-width="1.8"/>
  <text x="172" y="72" font-size="13" font-weight="bold" fill="#1f2937">M</text>
  <!-- 子弹 -->
  <circle cx="52" cy="68" r="6" fill="#9ca3af" stroke="#1f2937" stroke-width="1.5"/>
  <text x="46" y="55" font-size="11" font-style="italic" fill="#1f2937">m</text>
  <line x1="60" y1="68" x2="115" y2="68" stroke="#111827" stroke-width="1.8" stroke-dasharray="5,3" marker-end="url(#arr-blk-003-1)"/>
  <text x="84" y="60" font-size="11" font-style="italic" fill="#111827">v</text>

  <!-- 下图：合为一体 -->
  <text x="16" y="132" font-size="11" font-weight="bold" fill="#374151">一体後</text>
  <line x1="25" y1="215" x2="395" y2="215" stroke="#4b5563" stroke-width="2"/>
  <!-- 木块移动距离 d 的辅助虚线 -->
  <line x1="140" y1="105" x2="140" y2="238" stroke="#6b7280" stroke-width="1" stroke-dasharray="3,3"/>
  <line x1="220" y1="140" x2="220" y2="238" stroke="#6b7280" stroke-width="1" stroke-dasharray="3,3"/>
  <line x1="258" y1="178" x2="258" y2="238" stroke="#6b7280" stroke-width="1" stroke-dasharray="3,3"/>
  <!-- 木块本体（带弹孔槽） -->
  <path d="M 220 140 L 295 140 L 295 215 L 220 215 L 220 183 L 258 183 L 258 173 L 220 173 Z" fill="#e5e7eb" stroke="#374151" stroke-width="1.8"/>
  <!-- 子弹嵌入 -->
  <circle cx="258" cy="178" r="5.5" fill="#9ca3af" stroke="#1f2937" stroke-width="1.5"/>
  <!-- 相互阻力 F（红色） -->
  <line x1="252" y1="178" x2="228" y2="178" stroke="#dc2626" stroke-width="2" marker-end="url(#arr-red-003-1)"/>
  <text x="234" y="168" font-size="11" fill="#dc2626">F</text>
  <line x1="264" y1="178" x2="288" y2="178" stroke="#dc2626" stroke-width="2" marker-end="url(#arr-red-003-1)"/>
  <text x="275" y="168" font-size="11" fill="#dc2626">F</text>
  <!-- 共速 V -->
  <line x1="305" y1="178" x2="358" y2="178" stroke="#111827" stroke-width="1.8" stroke-dasharray="5,3" marker-end="url(#arr-blk-003-1)"/>
  <text x="328" y="170" font-size="12" font-style="italic" fill="#111827">V</text>

  <!-- 尺寸标注 d 与 x -->
  <line x1="142" y1="232" x2="218" y2="232" stroke="#4b5563" stroke-width="1.2" marker-end="url(#arr-dim-003-1)"/>
  <text x="176" y="229" font-size="11" font-style="italic" fill="#374151">d</text>
  <line x1="222" y1="232" x2="256" y2="232" stroke="#4b5563" stroke-width="1.2" marker-end="url(#arr-dim-003-1)"/>
  <text x="236" y="229" font-size="11" font-style="italic" fill="#374151">x</text>

  <!-- 图例 -->
  <text x="302" y="242" font-size="10" fill="#dc2626">■ 红：抵抗力 F</text>
  <text x="302" y="254" font-size="10" fill="#111827">--- 黑虚：速度方向</text>
</svg>

#### 【日本考场规范分步解答】

水平右向きを正とする。

**(1)** 水平方向には外力がはたらかないので，運動量保存則より，
$$mv + 0 = (M + m)V$$
$$\therefore \quad V = \frac{m}{M + m}v$$

> 💡 讲师批注：阻力 $F$ 是子弹与木块之间的**内力**，在光滑水平面上系统水平方向合外力为 $0$，因此动量严格守恒。

**(2)** 木片は弾丸から右向きに大きさ $F$ の力（抵抗力の反作用）を受ける。  
木片に関する力積と運動量の関係より，
$$F\Delta t = MV - 0$$
(1) の結果を代入して，
$$\Delta t = \frac{MV}{F} = \frac{Mmv}{(M + m)F}$$

> 💡 讲师批注：用**木块**列动量定理比用子弹更简单（木块初动量为 $0$，没有负号烦恼）！当然用子弹列 $-F\Delta t = mV - mv$ 也会得到完全相同的结果。

**(3)** 一体となるまでに木片が進んだ距離を $d$ とすると，弾丸が進んだ距離は $x + d$ である。  
- 木片が受けた仕事：$W_M = Fd$
- 弾丸が受けた仕事：$W_m = -F(x + d)$

弾丸と木片の系全体に関する仕事とエネルギーの関係より，
$$Fd - F(x + d) = \frac{1}{2}(M + m)V^2 - \frac{1}{2}mv^2$$
左辺を整理すると $-Fx$ となるので，
$$-Fx = \frac{1}{2}(M + m)\left(\frac{m}{M+m}v\right)^2 - \frac{1}{2}mv^2 = \frac{1}{2}mv^2\left(\frac{m}{M+m} - 1\right) = -\frac{Mmv^2}{2(M + m)}$$
$$\therefore \quad x = \frac{Mmv^2}{2(M + m)F}$$

> 💡 讲师批注：极其经典的一步——$Fd - F(x+d) = -Fx$，木块对地位移 $d$ 自动消去！这正是“**一对滑动摩擦力做功之和 $= -f \cdot x_{\text{相対}}$**”的严格证明。

#### 【最终答案】
- **(1) $V = \dfrac{m}{M + m}v$**
- **(2) $\Delta t = \dfrac{Mmv}{(M + m)F}$**
- **(3) $x = \dfrac{Mmv^2}{2(M + m)F}$**

---

### 例題 2（教材 P.33 / 页码 32）：ばねのついた物体との衝突（弹簧连接体碰撞）

#### 【原题重现与翻译】
> **日文原题**：  
> なめらかな平面上に質量 $m$ の物体 A と質量 $M\ (> m)$ の物体 B がおかれており，物体 B には自然長 $l$，ばね定数 $k$ の軽いばねが水平に取り付けられている。物体 A に速さ $v$ を与えて物体 B のばねに衝突させた。衝突によるエネルギー損失はないものとする。  
> (1) 衝突後，ばねが最も縮んだときの物体 A と物体 B の速さを求めよ。  
> (2) ばねが最も縮んだときの自然長からの縮み $x$ を求めよ。  
> (3) 2 物体が分離した後の物体 A と物体 B の速さを求めよ。
>
> **中文翻译**：  
> 光滑水平面上放置着质量为 $m$ 的物体 A 与质量为 $M\ (> m)$ 的物体 B，物体 B 上水平固定着一根自然长为 $l$、劲度系数为 $k$ 的轻弹簧。给物体 A 以速率 $v$ 使其撞向物体 B 的弹簧。设碰撞过程无能量损失。  
> (1) 求碰撞后弹簧被压缩至最短时，物体 A 与物体 B 的速率。  
> (2) 求弹簧被压缩至最短时相对于自然长的压缩量 $x$。  
> (3) 求两物体分离后物体 A 与物体 B 的速率。

#### 【考点与模型定位】
**弹簧碰撞模型（动量守恒 $+$ 机械能守恒）**：最压缩状态 $=$ 共速状态；分离状态 $=$ 完全弹性碰撞（$e = 1$）。

#### 【多色矢量图解（SVG）】

<svg viewBox="0 0 420 260" width="420" height="260" xmlns="http://www.w3.org/2000/svg" style="background:#fafafa;border:1px solid #e5e7eb;border-radius:8px;">
  <defs>
    <marker id="arr-green-003-2" markerWidth="7" markerHeight="7" refX="5" refY="3" orient="auto"><path d="M0,0 L0,6 L6,3 z" fill="#16a34a"/></marker>
    <marker id="arr-blk-003-2" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0,0 L0,6 L7,3 z" fill="#111827"/></marker>
  </defs>
  <!-- 阶段 1：碰撞前 -->
  <text x="14" y="25" font-size="11" font-weight="bold" fill="#374151">① 衝突前</text>
  <line x1="20" y1="72" x2="400" y2="72" stroke="#4b5563" stroke-width="1.8"/>
  <rect x="65" y="42" width="34" height="30" fill="#dbeafe" stroke="#1e40af" stroke-width="1.5"/>
  <text x="77" y="61" font-size="12" font-weight="bold" fill="#1e3a8a">A</text>
  <line x1="68" y1="34" x2="108" y2="34" stroke="#111827" stroke-width="1.6" stroke-dasharray="4,2" marker-end="url(#arr-blk-003-2)"/>
  <text x="83" y="28" font-size="11" font-style="italic" fill="#111827">v</text>
  <!-- 弹簧原长 -->
  <path d="M 180 57 L 190 57 L 194 49 L 200 65 L 206 49 L 212 65 L 218 49 L 224 65 L 230 57 L 240 57" fill="none" stroke="#16a34a" stroke-width="1.8"/>
  <rect x="240" y="42" width="38" height="30" fill="#fef3c7" stroke="#b45309" stroke-width="1.5"/>
  <text x="254" y="61" font-size="12" font-weight="bold" fill="#92400e">B</text>

  <!-- 阶段 2：最压缩（共速 V） -->
  <text x="14" y="108" font-size="11" font-weight="bold" fill="#374151">② 最縮（共速）</text>
  <line x1="20" y1="156" x2="400" y2="156" stroke="#4b5563" stroke-width="1.8"/>
  <rect x="172" y="126" width="34" height="30" fill="#dbeafe" stroke="#1e40af" stroke-width="1.5"/>
  <text x="184" y="145" font-size="12" font-weight="bold" fill="#1e3a8a">A</text>
  <line x1="175" y1="118" x2="210" y2="118" stroke="#111827" stroke-width="1.6" stroke-dasharray="4,2" marker-end="url(#arr-blk-003-2)"/>
  <text x="188" y="112" font-size="11" font-style="italic" fill="#111827">V</text>
  <!-- 压缩弹簧 -->
  <path d="M 206 141 L 212 141 L 215 132 L 219 150 L 223 132 L 227 150 L 231 132 L 235 150 L 239 141 L 244 141" fill="none" stroke="#16a34a" stroke-width="2"/>
  <!-- 弹力示意 -->
  <line x1="206" y1="141" x2="184" y2="141" stroke="#16a34a" stroke-width="1.8" marker-end="url(#arr-green-003-2)"/>
  <line x1="244" y1="141" x2="266" y2="141" stroke="#16a34a" stroke-width="1.8" marker-end="url(#arr-green-003-2)"/>
  <text x="216" y="169" font-size="10" fill="#16a34a">縮み x (kx)</text>
  <rect x="244" y="126" width="38" height="30" fill="#fef3c7" stroke="#b45309" stroke-width="1.5"/>
  <text x="258" y="145" font-size="12" font-weight="bold" fill="#92400e">B</text>
  <line x1="248" y1="118" x2="283" y2="118" stroke="#111827" stroke-width="1.6" stroke-dasharray="4,2" marker-end="url(#arr-blk-003-2)"/>
  <text x="261" y="112" font-size="11" font-style="italic" fill="#111827">V</text>

  <!-- 阶段 3：分离后 -->
  <text x="14" y="192" font-size="11" font-weight="bold" fill="#374151">③ 分離後 (M&gt;m)</text>
  <line x1="20" y1="240" x2="400" y2="240" stroke="#4b5563" stroke-width="1.8"/>
  <rect x="145" y="210" width="34" height="30" fill="#dbeafe" stroke="#1e40af" stroke-width="1.5"/>
  <text x="157" y="229" font-size="12" font-weight="bold" fill="#1e3a8a">A</text>
  <line x1="175" y1="202" x2="140" y2="202" stroke="#111827" stroke-width="1.6" stroke-dasharray="4,2" marker-end="url(#arr-blk-003-2)"/>
  <text x="148" y="196" font-size="11" font-style="italic" fill="#111827">V_A' (&lt;0)</text>
  <path d="M 248 225 L 258 225 L 262 217 L 268 233 L 274 217 L 280 233 L 286 217 L 292 233 L 298 225 L 308 225" fill="none" stroke="#16a34a" stroke-width="1.8"/>
  <rect x="308" y="210" width="38" height="30" fill="#fef3c7" stroke="#b45309" stroke-width="1.5"/>
  <text x="322" y="229" font-size="12" font-weight="bold" fill="#92400e">B</text>
  <line x1="312" y1="202" x2="358" y2="202" stroke="#111827" stroke-width="1.6" stroke-dasharray="4,2" marker-end="url(#arr-blk-003-2)"/>
  <text x="328" y="196" font-size="11" font-style="italic" fill="#111827">V_B'</text>
</svg>

#### 【日本考场规范分步解答】

物体 A から物体 B の向き（右向き）を正とする。

**(1)** ばねが最も縮んだとき，物体 A と物体 B の速度は等しくなる。この速さを $V$ とする。  
運動量保存則より，
$$mv = (M + m)V \implies V = \frac{m}{M + m}v$$

> 💡 讲师批注：只要 $v_A > v_B$ 弹簧就在继续压缩；当 $v_A = v_B$ 时距离达到极小值（压缩量最大）；之后 $v_A < v_B$ 弹簧开始恢复伸长。

**(2)** 衝突によるエネルギー損失がないので，力学的エネルギー保存則より，
$$\frac{1}{2}mv^2 = \frac{1}{2}(M + m)V^2 + \frac{1}{2}kx^2$$
(1) の $V = \dfrac{m}{M+m}v$ を代入して，
$$\frac{1}{2}kx^2 = \frac{1}{2}mv^2 - \frac{1}{2}\frac{m^2}{M+m}v^2 = \frac{1}{2}\frac{Mm}{M+m}v^2$$
$$\therefore \quad x = v\sqrt{\frac{Mm}{k(M + m)}}$$

> 💡 讲师批注：仔细对比例题 1 第 (3) 问！子弹打木块损失的动能 $\dfrac{Mmv^2}{2(M+m)}$ 变成了摩擦热 $Fx$；而本题完全没有损耗，这部分动能全部转化为了最大弹性势能 $\dfrac{1}{2}kx^2$，公式结构高度统一！

**(3)** 分離後の物体 A，B の速度をそれぞれ $V_A', V_B'$ とする。分離時はばねが自然長に戻っており，弾性エネルギーは $0$ である。  
**【解法 1：動量保存＋力学的エネルギー保存】**  
運動量保存則より，
$$mv = mV_A' + MV_B' \quad \cdots\text{①}$$
力学的エネルギー保存則より，
$$\frac{1}{2}mv^2 = \frac{1}{2}mV_A'^2 + \frac{1}{2}MV_B'^2 \quad \cdots\text{②}$$
①より $m(v - V_A') = MV_B'$，②より $m(v - V_A')(v + V_A') = MV_B'^2$。  
$V_B' \neq 0$ で両辺を割ると $v + V_A' = V_B'$ となるので，①と連立して，
$$V_A' = -\frac{M - m}{M + m}v, \qquad V_B' = \frac{2m}{M + m}v$$
ここで $M > m$ より $V_A' < 0$（左向きに跳ね返る）。求めるのは**速さ（正の値）**であるから，
$$\text{物体 A の速さ：}\frac{M - m}{M + m}v, \qquad \text{物体 B の速さ：}\frac{2m}{M + m}v$$

**【別解：反発係数 $e = 1$ の利用】**  
エネルギー損失がないため弾性衝突（$e = 1$）とみなせる。反発係数の式より，
$$1 = -\frac{V_A' - V_B'}{v - 0} \implies V_B' - V_A' = v$$
これを①と連立すれば即座に同じ結果を得る。

> 💡 讲师批注：考场上强烈推荐**別解**！直接用 $e = 1$ 联立一次方程，避免解二次方程浪费时间。另外务必注意审题：题干问的是「速さ（速率）」，已知 $M > m$，所以物体 A 的速率要去掉负号写 $\dfrac{M - m}{M + m}v$！

#### 【最终答案】
- **(1) $V = \dfrac{m}{M + m}v$**
- **(2) $x = v\sqrt{\dfrac{Mm}{k(M + m)}}$**
- **(3) 物体 A の速さ：$\dfrac{M - m}{M + m}v$，物体 B の速さ：$\dfrac{2m}{M + m}v$**

---

### 例題 3（教材 P.34 / 页码 33）：慣性力（加速电车内的悬球与等效重力）

#### 【原题重现与翻译】
> **日文原题**：  
> 一定の加速度で加速中の電車内に天井から糸で吊り下げられた質量 $m$ の小球があり，角度が $\theta$ だけ傾いたところで静止している。このときの小球の床からの高さは $h$ であった。重力加速度の大きさを $g$ とする。  
> (1) 電車の加速度の大きさと糸の張力の大きさを求めよ。  
> (2) 糸が切れたとき，電車内における小球の水平方向の移動距離 $x$ を求めよ。
>
> **中文翻译**：  
> 在以恒定加速度加速行驶的电车内，用轻绳从天花板悬挂一个质量为 $m$ 的小球，小球在偏离竖直方向 $\theta$ 角处保持相对静止，此时小球距车厢地板的高度为 $h$。设重力加速度大小为 $g$。  
> (1) 求电车的加速度大小及细绳张力大小。  
> (2) 当细绳剪断时，求小球落到地板前在电车内水平方向的移动距离 $x$。

#### 【考点与模型定位】
**非惯性系惯性力（慣性力）＋ 等效重力加速度（見かけの重力加速度）模型**（对比车内观察者静力平衡视角与地面观察者牛顿第二定律视角）。

#### 【多色矢量图解（SVG）】

<svg viewBox="0 0 420 260" width="420" height="260" xmlns="http://www.w3.org/2000/svg" style="background:#fafafa;border:1px solid #e5e7eb;border-radius:8px;">
  <defs>
    <marker id="arr-blue-003-3" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0,0 L0,6 L7,3 z" fill="#2563eb"/></marker>
    <marker id="arr-green-003-3" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0,0 L0,6 L7,3 z" fill="#16a34a"/></marker>
    <marker id="arr-red-003-3" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0,0 L0,6 L7,3 z" fill="#dc2626"/></marker>
    <marker id="arr-blk-003-3" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0,0 L0,6 L7,3 z" fill="#111827"/></marker>
  </defs>
  <!-- 车厢外框 -->
  <rect x="28" y="30" width="275" height="190" fill="#ffffff" stroke="#374151" stroke-width="2"/>
  <circle cx="75" cy="233" r="13" fill="#4b5563"/>
  <circle cx="75" cy="233" r="5" fill="#ffffff"/>
  <circle cx="255" cy="233" r="13" fill="#4b5563"/>
  <circle cx="255" cy="233" r="5" fill="#ffffff"/>
  <text x="38" y="22" font-size="11" font-weight="bold" fill="#374151">電車内の観測者（慣性力視点）</text>

  <!-- 电车加速度 a -->
  <line x1="315" y1="125" x2="365" y2="125" stroke="#111827" stroke-width="2" stroke-dasharray="5,3" marker-end="url(#arr-blk-003-3)"/>
  <text x="334" y="116" font-size="12" font-style="italic" fill="#111827">a</text>

  <!-- 悬点与竖直虚线 -->
  <line x1="175" y1="30" x2="175" y2="115" stroke="#9ca3af" stroke-width="1.2" stroke-dasharray="4,3"/>
  <!-- 细绳 -->
  <line x1="175" y1="30" x2="125" y2="116" stroke="#374151" stroke-width="1.8"/>
  <!-- 角度 θ 弧线 -->
  <path d="M 175 62 A 32 32 0 0 1 159 58" fill="none" stroke="#374151" stroke-width="1.2"/>
  <text x="161" y="75" font-size="11" fill="#374151">θ</text>

  <!-- 剪断后沿等效重力直线下落轨迹 -->
  <line x1="125" y1="116" x2="65" y2="220" stroke="#9ca3af" stroke-width="1.5" stroke-dasharray="5,4"/>
  <!-- 高度 h 与水平位移 x -->
  <line x1="125" y1="116" x2="125" y2="220" stroke="#9ca3af" stroke-width="1" stroke-dasharray="3,3"/>
  <text x="129" y="195" font-size="11" font-style="italic" fill="#374151">h</text>
  <line x1="65" y1="215" x2="125" y2="215" stroke="#374151" stroke-width="1.2"/>
  <text x="90" y="211" font-size="11" font-style="italic" fill="#374151">x</text>

  <!-- 小球 -->
  <circle cx="125" cy="116" r="8" fill="#dbeafe" stroke="#1e40af" stroke-width="1.5"/>

  <!-- 张力 T（绿色）及正交分解 -->
  <line x1="125" y1="116" x2="155" y2="64" stroke="#16a34a" stroke-width="2.2" marker-end="url(#arr-green-003-3)"/>
  <text x="148" y="60" font-size="11" font-weight="bold" fill="#16a34a">T</text>
  <line x1="125" y1="116" x2="125" y2="64" stroke="#16a34a" stroke-width="1.3" stroke-dasharray="3,2" marker-end="url(#arr-green-003-3)"/>
  <text x="86" y="72" font-size="10" fill="#16a34a">T cosθ</text>
  <line x1="125" y1="116" x2="155" y2="116" stroke="#16a34a" stroke-width="1.3" stroke-dasharray="3,2" marker-end="url(#arr-green-003-3)"/>
  <text x="158" y="120" font-size="10" fill="#16a34a">T sinθ</text>

  <!-- 重力 mg（蓝色） -->
  <line x1="125" y1="116" x2="125" y2="168" stroke="#2563eb" stroke-width="2.2" marker-end="url(#arr-blue-003-3)"/>
  <text x="130" y="168" font-size="11" font-weight="bold" fill="#2563eb">mg</text>

  <!-- 惯性力 ma（红色） -->
  <line x1="125" y1="116" x2="88" y2="116" stroke="#dc2626" stroke-width="2.2" marker-end="url(#arr-red-003-3)"/>
  <text x="64" y="112" font-size="11" font-weight="bold" fill="#dc2626">ma</text>

  <!-- 等效重力合力 mg'（黑虚） -->
  <line x1="125" y1="116" x2="95" y2="168" stroke="#111827" stroke-width="1.8" stroke-dasharray="4,2" marker-end="url(#arr-blk-003-3)"/>
  <text x="72" y="168" font-size="11" fill="#111827">mg'</text>

  <!-- 图例 -->
  <text x="310" y="185" font-size="10" fill="#2563eb">■ 蓝：重力 mg</text>
  <text x="310" y="200" font-size="10" fill="#16a34a">■ 绿：張力 T</text>
  <text x="310" y="215" font-size="10" fill="#dc2626">■ 红：慣性力 ma</text>
  <text x="310" y="230" font-size="10" fill="#111827">--- 黑虚：加速度/合力</text>
</svg>

#### 【日本考场规范分步解答】

電車の加速度の大きさを $a$，糸の張力の大きさを $T$ とする。

**(1) 【解法 1：電車内の観測者（慣性力とつりあい）】**  
電車内の観測者から見ると，小球には左向きに大きさ $ma$ の慣性力がはたらいて静止している。
$$\begin{cases} \text{水平方向のつりあい：} & T\sin\theta = ma \\ \text{鉛直方向のつりあい：} & T\cos\theta = mg \end{cases}$$
両辺の比をとると $\tan\theta = \dfrac{a}{g}$，また第 2 式より，
$$\therefore \quad a = g\tan\theta, \qquad T = \frac{mg}{\cos\theta}$$

**【別解：地上の観測者（運動方程式）】**  
地上の観測者から見ると，小球は電車と同じく右向きに加速度 $a$ で運動している。
$$\begin{cases} \text{水平方向の運動方程式：} & ma = T\sin\theta \\ \text{鉛直方向のつりあい：} & T\cos\theta = mg \end{cases}$$
$$\therefore \quad a = g\tan\theta, \qquad T = \frac{mg}{\cos\theta}$$

> 💡 讲师批注：注意教材第 34 页（页码 33）別解末尾印刷中，`T = mg/cosθ` 的分母底部轻微裁切，板书时规范写清 $\dfrac{mg}{\cos\theta}$ 即可。另外教材下方补充的**氦气球（風船）模型**是 EJU 高频考点：因浮力方向与等效重力 $\vec{g}'$ 严格相反，加速电车内的氦气球会**向前倾斜**（与重球方向相反）！

**(2)** 糸が切れた瞬間，電車内の観測者から見ると，小球は初速度 $0$ で重力 $mg$ と慣性力 $ma$ の合力（見かけの重力 $mg'$，鉛直方向から角度 $\theta$ 傾いた方向）に沿って等加速度直線運動をする。  
したがって，床までの高さ $h$ を落下する間の水平方向の移動距離 $x$ は幾何学的関係より直ちに求まる：
$$x = h\tan\theta$$

> 💡 讲师批注：若用地面参考系算第 (2) 问，需要分别写小球平抛与电车匀加速再求相对位移，极其繁琐；而切换到**车内非惯性系**后，小球直接沿原绳子延长线做直线落体，一步 $x = h\tan\theta$ 秒杀！这就是日本物理强调非惯性系的威力。

#### 【最终答案】
- **(1) $a = g\tan\theta$，$T = \dfrac{mg}{\cos\theta}$**
- **(2) $x = h\tan\theta$**

---

### 例題 4（教材 P.36 / 页码 35）：円錐振り子（光滑圆锥面上的圆锥摆）

#### 【原题重现与翻译】
> **日文原题**：  
> 頂点からの垂線と母線が角 $\theta$ をなす円錐の頂点に長さ $l$ の軽い糸の一端を固定し，もう一端に質量 $m$ の小さいおもりをつけて側面で角速度 $\omega$ の等速円運動をさせた。円錐面とおもりの間に摩擦はなく，重力加速度の大きさを $g$ とする。  
> (1) 糸の張力 $S$ と垂直抗力 $N$ を求めよ。  
> (2) 角速度 $\omega$ を徐々に大きくしていく。側面から離れて等速円運動を始めるときの周期 $T$ と速さ $v$ を求めよ。
>
> **中文翻译**：  
> 一圆锥的母线与顶点垂线（中心轴）夹角为 $\theta$。在圆锥顶点固定一根长为 $l$ 的轻绳一端，另一端系一质量为 $m$ 的小重物，使其紧贴圆锥侧面以角速度 $\omega$ 做匀速圆周运动。圆锥面与重物间无摩擦，重力加速度大小为 $g$。  
> (1) 求细绳的张力 $S$ 与圆锥面的支持力 $N$。  
> (2) 逐渐增大角速度 $\omega$，求重物刚要脱离圆锥侧面做匀速圆周运动时的周期 $T$ 与速率 $v$。

#### 【考点与模型定位】
**圆锥摆动力学临界模型**：圆周半径 $r = l\sin\theta$，水平向心方向与竖直平衡方向正交分解 $+$ 脱离面临界条件 $N = 0$。

#### 【多色矢量图解（SVG）】

<svg viewBox="0 0 420 260" width="420" height="260" xmlns="http://www.w3.org/2000/svg" style="background:#fafafa;border:1px solid #e5e7eb;border-radius:8px;">
  <defs>
    <marker id="arr-blue-003-4" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0,0 L0,6 L7,3 z" fill="#2563eb"/></marker>
    <marker id="arr-green-003-4" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0,0 L0,6 L7,3 z" fill="#16a34a"/></marker>
    <marker id="arr-red-003-4" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0,0 L0,6 L7,3 z" fill="#dc2626"/></marker>
  </defs>
  <text x="16" y="22" font-size="11" font-weight="bold" fill="#374151">回転中の観測者（遠心力視点）</text>

  <!-- 圆锥体 -->
  <line x1="165" y1="30" x2="70" y2="230" stroke="#4b5563" stroke-width="1.8"/>
  <line x1="165" y1="30" x2="260" y2="230" stroke="#4b5563" stroke-width="1.8"/>
  <ellipse cx="165" cy="230" rx="95" ry="18" fill="none" stroke="#4b5563" stroke-width="1.5"/>
  <!-- 中心轴 -->
  <line x1="165" y1="30" x2="165" y2="230" stroke="#9ca3af" stroke-width="1.2" stroke-dasharray="4,3"/>
  <!-- 圆周运动轨迹椭圆 -->
  <ellipse cx="165" cy="145" rx="54" ry="11" fill="none" stroke="#6b7280" stroke-width="1.3" stroke-dasharray="4,3"/>
  <!-- 半径 r = l sinθ -->
  <line x1="165" y1="145" x2="219" y2="145" stroke="#374151" stroke-width="1.2" stroke-dasharray="3,2"/>
  <text x="172" y="160" font-size="10" fill="#374151">r = l sinθ</text>

  <!-- 顶角 θ -->
  <path d="M 165 65 A 35 35 0 0 0 180 62" fill="none" stroke="#374151" stroke-width="1.2"/>
  <text x="169" y="78" font-size="11" fill="#374151">θ</text>
  <!-- 细绳 l -->
  <line x1="165" y1="30" x2="219" y2="145" stroke="#1f2937" stroke-width="2"/>
  <text x="196" y="82" font-size="11" font-style="italic" fill="#1f2937">l</text>

  <!-- 小球 -->
  <circle cx="219" cy="145" r="7" fill="#dbeafe" stroke="#1e40af" stroke-width="1.5"/>

  <!-- 张力 S（绿色，沿母线向上） -->
  <line x1="219" y1="145" x2="191" y2="85" stroke="#16a34a" stroke-width="2.2" marker-end="url(#arr-green-003-4)"/>
  <text x="180" y="96" font-size="11" font-weight="bold" fill="#16a34a">S</text>
  <!-- S 的分解虚线 -->
  <line x1="219" y1="145" x2="219" y2="85" stroke="#16a34a" stroke-width="1.2" stroke-dasharray="3,2" marker-end="url(#arr-green-003-4)"/>
  <text x="223" y="92" font-size="10" fill="#16a34a">S cosθ</text>
  <line x1="219" y1="145" x2="191" y2="145" stroke="#16a34a" stroke-width="1.2" stroke-dasharray="3,2" marker-end="url(#arr-green-003-4)"/>
  <text x="172" y="139" font-size="10" fill="#16a34a">S sinθ</text>

  <!-- 支持力 N（绿色，垂直母线向外上方） -->
  <line x1="219" y1="145" x2="269" y2="121" stroke="#16a34a" stroke-width="2.2" marker-end="url(#arr-green-003-4)"/>
  <text x="272" y="122" font-size="11" font-weight="bold" fill="#16a34a">N</text>
  <!-- N 的分解 -->
  <line x1="219" y1="145" x2="269" y2="145" stroke="#16a34a" stroke-width="1.2" stroke-dasharray="3,2"/>
  <text x="268" y="138" font-size="10" fill="#16a34a">N cosθ</text>

  <!-- 离心力 mrω²（红色，水平向右） -->
  <line x1="219" y1="145" x2="295" y2="145" stroke="#dc2626" stroke-width="2.2" marker-end="url(#arr-red-003-4)"/>
  <text x="285" y="160" font-size="10" font-weight="bold" fill="#dc2626">m(l sinθ)ω²</text>

  <!-- 重力 mg（蓝色，竖直向下） -->
  <line x1="219" y1="145" x2="219" y2="205" stroke="#2563eb" stroke-width="2.2" marker-end="url(#arr-blue-003-4)"/>
  <text x="224" y="203" font-size="11" font-weight="bold" fill="#2563eb">mg</text>

  <!-- 图例 -->
  <text x="295" y="48" font-size="10" fill="#2563eb">■ 蓝：重力 mg</text>
  <text x="295" y="64" font-size="10" fill="#16a34a">■ 绿：張力 S / 抗力 N</text>
  <text x="295" y="80" font-size="10" fill="#dc2626">■ 红：遠心力 mrω²</text>
</svg>

#### 【日本考场规范分步解答】

円運動の半径は $r = l\sin\theta$ である。水平方向（中心向きを正）を $x$ 軸，鉛直上向きを $y$ 軸とする。

**(1) 【解法 1：地上の観測者（運動方程式）】**
$$\begin{cases} x\text{ 軸方向の運動方程式：} & m(l\sin\theta)\omega^2 = S\sin\theta - N\cos\theta \quad \cdots\text{①} \\ y\text{ 軸方向のつりあい：} & S\cos\theta + N\sin\theta = mg \quad \cdots\text{②} \end{cases}$$

**【別解：回転中の観測者（遠心力とつりあい）】**  
外向きに大きさ $m(l\sin\theta)\omega^2$ の遠心力を加えると，
$$\begin{cases} x\text{ 軸方向のつりあい：} & S\sin\theta = m(l\sin\theta)\omega^2 + N\cos\theta \\ y\text{ 軸方向のつりあい：} & S\cos\theta + N\sin\theta = mg \end{cases}$$

① $\times \sin\theta +$ ② $\times \cos\theta$ より $N$ を消去すると（$\sin^2\theta + \cos^2\theta = 1$），
$$S = mg\cos\theta + ml\omega^2\sin^2\theta$$
② $\times \sin\theta -$ ① $\times \cos\theta$ より $S$ を消去すると，
$$N = mg\sin\theta - ml\omega^2\sin\theta\cos\theta$$

> 💡 讲师批注：解联立方程①②的绝招是**直接配凑 $\sin^2\theta + \cos^2\theta = 1$**！千万不要傻傻地代入消元，两行就能写出极其对称的 $S$ 与 $N$ 表达式。

**(2)** おもりが円錐の側面から離れる瞬間の条件は $N = 0$ である。  
(1) の結果より，
$$mg\sin\theta - ml\omega^2\sin\theta\cos\theta = 0$$
$\sin\theta \neq 0$ より両辺を $m\sin\theta$ で割ると，
$$\omega^2 = \frac{g}{l\cos\theta} \implies \omega = \sqrt{\frac{g}{l\cos\theta}}$$
したがって，周期 $T$ と速さ $v$ は，
$$T = \frac{2\pi}{\omega} = 2\pi\sqrt{\frac{l\cos\theta}{g}}$$
$$v = r\omega = l\sin\theta \cdot \sqrt{\frac{g}{l\cos\theta}} = \sqrt{gl\sin\theta\tan\theta}$$

> 💡 讲师批注：注意周期公式 $T = 2\pi\sqrt{\dfrac{l\cos\theta}{g}} = 2\pi\sqrt{\dfrac{h}{g}}$（$h = l\cos\theta$ 是摆球到悬点的竖直高度），这是普通圆锥摆的经典周期公式！

#### 【最终答案】
- **(1) $S = mg\cos\theta + ml\omega^2\sin^2\theta$，$N = mg\sin\theta - ml\omega^2\sin\theta\cos\theta$**
- **(2) $T = 2\pi\sqrt{\dfrac{l\cos\theta}{g}}$，$v = \sqrt{gl\sin\theta\tan\theta}$**

---

### 例題 5（教材 P.37 / 页码 36）：振り子（竖直面内圆周运动：轻绳 vs 轻杆）

#### 【原题重现与翻译】
> **日文原题**：  
> 質量 $m$ の小球に長さ $l$ の軽い糸をつけ，点 O を中心に鉛直面内で円運動させるために最下点で初速度 $v_0$ を与えた。重力加速度の大きさを $g$ とする。  
> (1) 円運動するための $v_0$ の条件を求めよ。  
> (2) 糸の代わりに（※原文誤植「変わりに」）軽い棒を用いたとき，円運動するための $v_0$ の条件を求めよ。
>
> **中文翻译**：  
> 用长为 $l$ 的轻绳系住质量为 $m$ 的小球，为使其以点 O 为圆心在竖直面内做完整圆周运动，在最低点赋予其初速度 $v_0$。设重力加速度大小为 $g$。  
> (1) 求能完成圆周运动的 $v_0$ 满足的条件。  
> (2) 将细绳换为轻杆时，求能完成圆周运动的 $v_0$ 满足的条件。

#### 【考点与模型定位】
**竖直面内圆周运动最高点临界模型**：能量守恒 $+$ 最高点向心力方程（轻绳 $T \ge 0 \implies v_0 \ge \sqrt{5gl}$；轻杆 $v > 0 \implies v_0 > 2\sqrt{gl}$）。

#### 【多色矢量图解（SVG）】

<svg viewBox="0 0 420 260" width="420" height="260" xmlns="http://www.w3.org/2000/svg" style="background:#fafafa;border:1px solid #e5e7eb;border-radius:8px;">
  <defs>
    <marker id="arr-blue-003-5" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0,0 L0,6 L7,3 z" fill="#2563eb"/></marker>
    <marker id="arr-green-003-5" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0,0 L0,6 L7,3 z" fill="#16a34a"/></marker>
    <marker id="arr-red-003-5" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0,0 L0,6 L7,3 z" fill="#dc2626"/></marker>
    <marker id="arr-blk-003-5" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0,0 L0,6 L7,3 z" fill="#111827"/></marker>
  </defs>
  <text x="18" y="22" font-size="11" font-weight="bold" fill="#374151">最高点での力のつりあい（小球上の観測者）</text>

  <!-- 圆周轨道 -->
  <circle cx="170" cy="145" r="78" fill="none" stroke="#6b7280" stroke-width="1.6" stroke-dasharray="5,4"/>
  <!-- 圆心 O 与细绳 -->
  <circle cx="170" cy="145" r="3" fill="#111827"/>
  <text x="155" y="149" font-size="11" font-weight="bold" fill="#111827">O</text>
  <line x1="170" y1="67" x2="170" y2="223" stroke="#374151" stroke-width="1.6"/>
  <text x="176" y="190" font-size="11" font-style="italic" fill="#374151">l</text>

  <!-- 最高点小球 -->
  <circle cx="170" cy="67" r="9" fill="#dbeafe" stroke="#1e40af" stroke-width="1.5"/>
  <!-- 最高点速度 v（黑虚） -->
  <line x1="160" y1="54" x2="112" y2="54" stroke="#111827" stroke-width="1.8" stroke-dasharray="5,3" marker-end="url(#arr-blk-003-5)"/>
  <text x="130" y="47" font-size="11" font-style="italic" fill="#111827">v</text>
  <!-- 离心力 mv²/l（红色，向上） -->
  <line x1="170" y1="58" x2="170" y2="18" stroke="#dc2626" stroke-width="2.2" marker-end="url(#arr-red-003-5)"/>
  <text x="178" y="34" font-size="11" font-weight="bold" fill="#dc2626">mv²/l (遠心力)</text>
  <!-- 重力 mg（蓝色，向下） -->
  <line x1="166" y1="76" x2="166" y2="122" stroke="#2563eb" stroke-width="2.2" marker-end="url(#arr-blue-003-5)"/>
  <text x="140" y="114" font-size="11" font-weight="bold" fill="#2563eb">mg</text>
  <!-- 张力 T（绿色，向下） -->
  <line x1="174" y1="76" x2="174" y2="114" stroke="#16a34a" stroke-width="2.2" marker-end="url(#arr-green-003-5)"/>
  <text x="180" y="108" font-size="11" font-weight="bold" fill="#16a34a">T</text>

  <!-- 最低点小球 -->
  <circle cx="170" cy="223" r="9" fill="#fef3c7" stroke="#b45309" stroke-width="1.5"/>
  <!-- 最低点初速度 v0（黑虚） -->
  <line x1="179" y1="234" x2="232" y2="234" stroke="#111827" stroke-width="1.8" stroke-dasharray="5,3" marker-end="url(#arr-blk-003-5)"/>
  <text x="200" y="249" font-size="11" font-style="italic" fill="#111827">v₀</text>

  <!-- 高度差 2l 标注 -->
  <line x1="262" y1="67" x2="262" y2="223" stroke="#4b5563" stroke-width="1.2"/>
  <line x1="256" y1="67" x2="268" y2="67" stroke="#4b5563" stroke-width="1.2"/>
  <line x1="256" y1="223" x2="268" y2="223" stroke="#4b5563" stroke-width="1.2"/>
  <text x="270" y="149" font-size="11" fill="#374151">高さ 2l</text>

  <!-- 图例 -->
  <text x="295" y="190" font-size="10" fill="#2563eb">■ 蓝：重力 mg</text>
  <text x="295" y="205" font-size="10" fill="#16a34a">■ 绿：張力 T</text>
  <text x="295" y="220" font-size="10" fill="#dc2626">■ 红：遠心力 mv²/l</text>
  <text x="295" y="235" font-size="10" fill="#111827">--- 黑虚：速度方向</text>
</svg>

#### 【日本考场规范分步解答】

最高点における小球の速さを $v$，糸の張力を $T$ とする。

**(1)** 最高点において，  
- **中心方向の運動方程式**（小球上の観測者なら遠心力とのつりあい）：
  $$m\frac{v^2}{l} = T + mg \quad \cdots\text{①}$$
- **力学的エネルギー保存則**（最下点を位置エネルギーの基準とする）：
  $$\frac{1}{2}mv_0^2 = \frac{1}{2}mv^2 + mg \cdot 2l \quad \cdots\text{②}$$

②より $v^2 = v_0^2 - 4gl$。これを①に代入して $T$ を求めると，
$$T = m\frac{v^2}{l} - mg = \frac{mv_0^2}{l} - 5mg$$
糸がたるまずに最高点を通過する条件は $T \ge 0$ であるから，
$$\frac{mv_0^2}{l} - 5mg \ge 0 \implies v_0 \ge \sqrt{5gl}$$

> 💡 讲师批注：轻绳不能提供向上的推力，故最高点必须满足 $T \ge 0$（即 $v \ge \sqrt{gl}$）。当 $v_0 = \sqrt{5gl}$ 时，小球在最高点瞬间张力恰好为 $0$，全靠重力充当向心力完成圆周运动。

**(2)** 軽い棒は小球を押す力（上向きの抗力）も及ぼせるため，糸のようにたるむことはない。最高点を越えて円運動を続けるための条件は $v > 0$（すなわち $v^2 > 0$）である。  
②より，
$$v^2 = v_0^2 - 4gl > 0 \implies v_0 > 2\sqrt{gl}$$

> 💡 讲师批注：
> 1. **教材勘误**：教材第 37 页（页码 36）第 (2) 问原题中「糸の**変わり**に」为日文同音错别字，正确汉字应为「糸の**代わり**に（代替细绳）」。
> 2. **中日细节差异**：国内高中常表述为“能通过最高点”写 $v_0 \ge 2\sqrt{gl}$，而日本教材严谨区分：若 $v_0 = 2\sqrt{gl}$，小球会在最高点处速度减为 $0$ 停住而无法继续做圆周运动，因此「円運動するための条件」写严格大于号 **$v_0 > 2\sqrt{gl}$**。

#### 【最终答案】
- **(1) $v_0 \ge \sqrt{5gl}$**
- **(2) $v_0 > 2\sqrt{gl}$**

---

### 例題 6（教材 P.39–40 / 页码 38–39）：鉛直ばね振り子（竖直弹簧振子）

#### 【原题重现与翻译】
> **日文原题**：  
> 天井から（※原文多印一字「に」）つりさげられたばねに質量 $m$ の小球をつけたところ，自然長から $l$ 伸びて静止した。この点を原点として鉛直下向きに $x$ 軸をとり，$x = d$ の点まで小球を持ち下げて時刻 $t = 0$ に静かに小球を放したところ，小球は単振動した。重力加速度の大きさを $g$ とする。  
> (1) ばね定数 $k$ を求めよ。  
> (2) 単振動の周期 $T$ と振幅 $A$ を求めよ。  
> (3) 速さの最大値 $v$ を求めよ。  
> (4) 時刻 $t$ における $x$ 座標を求めよ。  
> (5) 最初に $x = -\dfrac{1}{2}d$ を通過するときの速さ $v'$ と時刻 $t'$ を求めよ。
>
> **中文翻译**：  
> 在天花板悬挂的轻弹簧下端挂上质量为 $m$ 的小球后，弹簧比自然长伸长了 $l$ 并静止。以此平衡点为原点、竖直向下为 $+x$ 轴，将小球下拉至 $x = d$ 处，在时刻 $t = 0$ 时由静止释放，小球开始做简谐振动。设重力加速度大小为 $g$。  
> (1) 求弹簧劲度系数 $k$。  
> (2) 求简谐振动的周期 $T$ 与振幅 $A$。  
> (3) 求速率的最大值 $v$。  
> (4) 求时刻 $t$ 时的 $x$ 坐标。  
> (5) 求小球首次通过 $x = -\dfrac{1}{2}d$ 时的速率 $v'$ 与时刻 $t'$。

#### 【考点与模型定位】
**竖直弹簧振子完整题型**：静平衡求 $k$ $+$ 运动方程证简谐（重力与平衡弹力抵消）$+$ 振动能量守恒求速 $+$ 参考圆（圆心角 $120^\circ$）求时刻。

#### 【多色矢量图解（SVG）】

<svg viewBox="0 0 420 265" width="420" height="265" xmlns="http://www.w3.org/2000/svg" style="background:#fafafa;border:1px solid #e5e7eb;border-radius:8px;">
  <defs>
    <marker id="arr-blue-003-6" markerWidth="7" markerHeight="7" refX="5" refY="3" orient="auto"><path d="M0,0 L0,6 L6,3 z" fill="#2563eb"/></marker>
    <marker id="arr-green-003-6" markerWidth="7" markerHeight="7" refX="5" refY="3" orient="auto"><path d="M0,0 L0,6 L6,3 z" fill="#16a34a"/></marker>
    <marker id="arr-blk-003-6" markerWidth="7" markerHeight="7" refX="5" refY="3" orient="auto"><path d="M0,0 L0,6 L6,3 z" fill="#111827"/></marker>
  </defs>
  <!-- 天花板 -->
  <line x1="145" y1="22" x2="365" y2="22" stroke="#374151" stroke-width="2.5"/>
  <!-- 左侧：参考圆（第5问 120° 示意） -->
  <text x="16" y="22" font-size="11" font-weight="bold" fill="#374151">等速円運動の正射影</text>
  <circle cx="72" cy="148" r="56" fill="none" stroke="#4b5563" stroke-width="1.5"/>
  <line x1="72" y1="80" x2="72" y2="215" stroke="#9ca3af" stroke-width="1"/>
  <line x1="12" y1="148" x2="132" y2="148" stroke="#9ca3af" stroke-width="1" stroke-dasharray="3,2"/>
  <!-- 120° 扇形与箭头 -->
  <line x1="72" y1="148" x2="72" y2="204" stroke="#dc2626" stroke-width="1.6"/>
  <line x1="72" y1="148" x2="120.5" y2="120" stroke="#dc2626" stroke-width="1.8" marker-end="url(#arr-blk-003-6)"/>
  <path d="M 72 172 A 24 24 0 0 0 92.8 136" fill="none" stroke="#dc2626" stroke-width="1.6"/>
  <text x="86" y="168" font-size="11" font-weight="bold" fill="#dc2626">120°</text>
  <circle cx="72" cy="204" r="4" fill="#dc2626"/>
  <text x="44" y="218" font-size="10" fill="#374151">t=0 (x=d)</text>
  <circle cx="120.5" cy="120" r="4" fill="#dc2626"/>
  <text x="82" y="110" font-size="10" fill="#dc2626">t' (x=-d/2)</text>

  <!-- 坐标虚线水平对齐 -->
  <line x1="132" y1="92" x2="388" y2="92" stroke="#9ca3af" stroke-width="1" stroke-dasharray="3,3"/>
  <text x="392" y="96" font-size="10" fill="#374151">-d</text>
  <line x1="120" y1="120" x2="388" y2="120" stroke="#dc2626" stroke-width="1" stroke-dasharray="3,2"/>
  <text x="392" y="124" font-size="10" font-weight="bold" fill="#dc2626">-d/2</text>
  <line x1="132" y1="148" x2="388" y2="148" stroke="#4b5563" stroke-width="1.2" stroke-dasharray="4,3"/>
  <text x="392" y="152" font-size="11" font-weight="bold" fill="#111827">O</text>
  <line x1="132" y1="204" x2="388" y2="204" stroke="#9ca3af" stroke-width="1" stroke-dasharray="3,3"/>
  <text x="392" y="208" font-size="10" fill="#374151">+d</text>

  <!-- x 轴 -->
  <line x1="382" y1="78" x2="382" y2="238" stroke="#111827" stroke-width="1.4" marker-end="url(#arr-blk-003-6)"/>
  <text x="387" y="242" font-size="11" font-style="italic" fill="#111827">+x</text>

  <!-- 中间弹簧1：平衡位置 O -->
  <text x="166" y="40" font-size="10" fill="#374151">つりあい(O)</text>
  <path d="M 192 22 L 192 48 L 185 53 L 199 61 L 185 69 L 199 77 L 185 85 L 199 93 L 185 101 L 199 109 L 185 117 L 192 122 L 192 140" fill="none" stroke="#16a34a" stroke-width="1.6"/>
  <circle cx="192" cy="148" r="8" fill="#dbeafe" stroke="#1e40af" stroke-width="1.5"/>
  <!-- 受力 kl 与 mg -->
  <line x1="192" y1="140" x2="192" y2="106" stroke="#16a34a" stroke-width="2" marker-end="url(#arr-green-003-6)"/>
  <text x="198" y="114" font-size="10" fill="#16a34a">kl</text>
  <line x1="192" y1="156" x2="192" y2="190" stroke="#2563eb" stroke-width="2" marker-end="url(#arr-blue-003-6)"/>
  <text x="198" y="186" font-size="10" fill="#2563eb">mg</text>

  <!-- 右侧弹簧2：一般位移 x (>0) -->
  <text x="275" y="40" font-size="10" fill="#374151">変位 x</text>
  <path d="M 290 22 L 290 50 L 283 56 L 297 68 L 283 80 L 297 92 L 283 104 L 297 116 L 283 128 L 297 140 L 283 152 L 290 158 L 290 170" fill="none" stroke="#16a34a" stroke-width="1.6"/>
  <circle cx="290" cy="178" r="8" fill="#fef3c7" stroke="#b45309" stroke-width="1.5"/>
  <line x1="290" y1="170" x2="290" y2="124" stroke="#16a34a" stroke-width="2" marker-end="url(#arr-green-003-6)"/>
  <text x="296" y="136" font-size="10" fill="#16a34a">k(l+x)</text>
  <line x1="290" y1="186" x2="290" y2="220" stroke="#2563eb" stroke-width="2" marker-end="url(#arr-blue-003-6)"/>
  <text x="296" y="218" font-size="10" fill="#2563eb">mg</text>

  <!-- 图例 -->
  <text x="16" y="248" font-size="10" fill="#2563eb">■ 蓝：重力 mg</text>
  <text x="108" y="248" font-size="10" fill="#16a34a">■ 绿：弾性力 k(l+x)</text>
  <text x="228" y="248" font-size="10" fill="#dc2626">■ 红：位相角 120° = T/3</text>
</svg>

#### 【日本考场规范分步解答】

**(1)** 静止時（つりあい位置）において，重力とばねの弾性力がつりあっているので，
$$kl = mg \implies k = \frac{mg}{l}$$

**(2)** つりあい位置を原点とし，鉛直下向きを正とする座標 $x$ における小球の運動方程式は，
$$ma = mg - k(l + x)$$
(1) の $kl = mg$ を代入すると $mg$ が相殺し，
$$ma = -kx = -\frac{mg}{l}x \implies a = -\frac{g}{l}x$$
単振動の加速度の式 $a = -\omega^2 x$ と比較すると，角振動数は $\omega = \sqrt{\dfrac{g}{l}}$ となる。  
したがって，周期 $T$ と振幅 $A$（つりあい位置から最下点までの距離）は，
$$T = \frac{2\pi}{\omega} = 2\pi\sqrt{\frac{l}{g}}, \qquad A = d$$

> 💡 讲师批注：注意教材第 39 页（页码 38）原题第一行「天井から**に**つりさげられたばね」多印了一个助词「に」，属轻微笔误。另外请重点提醒学生：竖直弹簧振子中 $kl = mg$ 使得 $T = 2\pi\sqrt{m/k} = 2\pi\sqrt{l/g}$，这个结论在 EJU 中极高频出现！

**(3)** 単振動のエネルギー保存則より，振動中心（$x = 0$）での最大運動エネルギーと最下点（$x = d$）での最大弾性エネルギーが等しい：
$$\frac{1}{2}mv^2 = \frac{1}{2}kd^2 \implies v = d\sqrt{\frac{k}{m}} = d\sqrt{\frac{g}{l}}$$
**【別解】** 単振動の最大速さの公式より直接：
$$v = A\omega = d\sqrt{\frac{g}{l}}$$

**(4)** 時刻 $t = 0$ に正の端（$x = +d$）から静かに放したので，変位の式は $\cos$ 型となる：
$$x = A\cos\omega t = d\cos\left(\sqrt{\frac{g}{l}}\,t\right)$$

> 💡 讲师批注：区分 $\sin$ 与 $\cos$ 的口诀：从平衡位置 $O$ 出发用 $\sin$，从端点 $\pm A$ 静止释放用 $\pm\cos$！

**(5)** 振動の力学的エネルギー保存則より，$x = -\dfrac{1}{2}d$ での速さを $v'$ とすると，
$$\frac{1}{2}mv'^2 + \frac{1}{2}k\left(-\frac{1}{2}d\right)^2 = \frac{1}{2}kd^2$$
$$\frac{1}{2}mv'^2 = \frac{3}{8}kd^2 \implies v'^2 = \frac{3k}{4m}d^2 = \frac{3g}{4l}d^2 \implies v' = \frac{d}{2}\sqrt{\frac{3g}{l}}$$
また，時刻 $t'$ は $x = d\cos\omega t' = -\dfrac{1}{2}d$ より $\cos\omega t' = -\dfrac{1}{2}$。最初に通過する位相角は $\omega t' = \dfrac{2\pi}{3}\ (120^\circ)$ であるから，
$$t' = \frac{120^\circ}{360^\circ}T = \frac{1}{3}T = \frac{2\pi}{3}\sqrt{\frac{l}{g}}$$

> 💡 讲师批注：第 (5) 问求时刻 $t'$ 用**参考圆（等速円運動の正射影）**最直观：从最下端 $x = +d$（相位 $0^\circ$）逆时针转到 $x = -\dfrac{1}{2}d$，经过了 $90^\circ + 30^\circ = 120^\circ$，正好是 $\dfrac{1}{3}$ 个周期！

#### 【最终答案】
- **(1) $k = \dfrac{mg}{l}$**
- **(2) $T = 2\pi\sqrt{\dfrac{l}{g}}$，$A = d$**
- **(3) $v = d\sqrt{\dfrac{g}{l}}$**
- **(4) $x = d\cos\left(\sqrt{\dfrac{g}{l}}\,t\right)$**
- **(5) $v' = \dfrac{d}{2}\sqrt{\dfrac{3g}{l}}$，$t' = \dfrac{2\pi}{3}\sqrt{\dfrac{l}{g}}$**

---

### 例題 7（教材 P.41 / 页码 40）：単振り子（单摆与非惯性系中的单摆周期）

#### 【原题重现与翻译】
> **日文原题**：  
> 長さ $l$ の糸に質量 $m$ のおもりをつけた単振り子を振動させた。最下点を原点，水平右方向を正とする $x$ 軸をとる。重力加速度の大きさを $g$ とする。  
> (1) 位置 $x\ (> 0)$ にあるおもりにはたらく接線方向の力 $F$ を $m, l, x, g$ で表せ。ただし，反時計回りを正とする。  
> (2) $\theta$ が小さいとき，(1) の力は $x$ 軸に沿っているとみなせる。周期 $T$ を求めよ。  
> (3) この単振り子を加速度 $\alpha$ で上昇中のエレベーター内で振動させたときの周期 $T'$ を求めよ。  
> (4) この単振り子を加速度 $\beta$ で移動中の電車内で振動させたときの周期 $T''$ を求めよ。
>
> **中文翻译**：  
> 使一摆长为 $l$、摆球质量为 $m$ 的单摆做振动。以最低点为原点，水平向右为 $+x$ 轴。设重力加速度大小为 $g$。  
> (1) 用 $m, l, x, g$ 表示位于 $x\ (> 0)$ 处的摆球所受切线方向的力 $F$（取逆时针方向为正）。  
> (2) 当摆角 $\theta$ 很小时，可将 (1) 的力视为沿 $x$ 轴方向。求周期 $T$。  
> (3) 求此单摆在以加速度 $\alpha$ 匀加速上升的电梯内振动时的周期 $T'$。  
> (4) 求此单摆在以水平加速度 $\beta$ 加速行驶的电车内振动时的周期 $T''$。

#### 【考点与模型定位】
**单摆周期公式推导 $+$ 等效重力加速度 $g'$ 替换法**（电梯超重 $g' = g + \alpha$；水平加速电车 $g' = \sqrt{g^2 + \beta^2}$）。

#### 【多色矢量图解（SVG）】

<svg viewBox="0 0 420 260" width="420" height="260" xmlns="http://www.w3.org/2000/svg" style="background:#fafafa;border:1px solid #e5e7eb;border-radius:8px;">
  <defs>
    <marker id="arr-blue-003-7" markerWidth="7" markerHeight="7" refX="5" refY="3" orient="auto"><path d="M0,0 L0,6 L6,3 z" fill="#2563eb"/></marker>
    <marker id="arr-green-003-7" markerWidth="7" markerHeight="7" refX="5" refY="3" orient="auto"><path d="M0,0 L0,6 L6,3 z" fill="#16a34a"/></marker>
    <marker id="arr-red-003-7" markerWidth="7" markerHeight="7" refX="5" refY="3" orient="auto"><path d="M0,0 L0,6 L6,3 z" fill="#dc2626"/></marker>
    <marker id="arr-blk-003-7" markerWidth="7" markerHeight="7" refX="5" refY="3" orient="auto"><path d="M0,0 L0,6 L6,3 z" fill="#111827"/></marker>
  </defs>
  <!-- 左图：标准单摆 -->
  <text x="16" y="20" font-size="11" font-weight="bold" fill="#374151">(1)(2) 単振り子の復元力</text>
  <line x1="40" y1="32" x2="175" y2="32" stroke="#374151" stroke-width="2.2"/>
  <line x1="95" y1="32" x2="95" y2="175" stroke="#9ca3af" stroke-width="1.2" stroke-dasharray="4,3"/>
  <line x1="95" y1="32" x2="152" y2="162" stroke="#374151" stroke-width="1.8"/>
  <text x="130" y="96" font-size="11" font-style="italic" fill="#374151">l</text>
  <!-- 角度 θ -->
  <path d="M 95 68 A 36 36 0 0 0 110 65" fill="none" stroke="#374151" stroke-width="1.2"/>
  <text x="99" y="80" font-size="11" fill="#374151">θ</text>
  <!-- x 坐标水平线 -->
  <line x1="95" y1="162" x2="152" y2="162" stroke="#4b5563" stroke-width="1.2" stroke-dasharray="3,2"/>
  <text x="120" y="156" font-size="11" font-style="italic" fill="#374151">x</text>
  <!-- 原点 O 与摆球 -->
  <circle cx="95" cy="175" r="5" fill="#e5e7eb" stroke="#6b7280" stroke-width="1.2"/>
  <text x="82" y="192" font-size="11" fill="#374151">O</text>
  <line x1="75" y1="175" x2="188" y2="175" stroke="#111827" stroke-width="1.2" marker-end="url(#arr-blk-003-7)"/>
  <text x="190" y="179" font-size="11" font-style="italic" fill="#111827">x</text>
  <circle cx="152" cy="162" r="7" fill="#dbeafe" stroke="#1e40af" stroke-width="1.5"/>
  <!-- 张力 T（绿） -->
  <line x1="152" y1="162" x2="132" y2="117" stroke="#16a34a" stroke-width="1.8" marker-end="url(#arr-green-003-7)"/>
  <!-- 重力 mg（蓝） -->
  <line x1="152" y1="162" x2="152" y2="225" stroke="#2563eb" stroke-width="2" marker-end="url(#arr-blue-003-7)"/>
  <text x="157" y="222" font-size="11" font-weight="bold" fill="#2563eb">mg</text>
  <!-- 切线回复力 mg sinθ（蓝虚线分解） -->
  <line x1="152" y1="162" x2="128" y2="173" stroke="#dc2626" stroke-width="2" marker-end="url(#arr-red-003-7)"/>
  <text x="92" y="210" font-size="10" font-weight="bold" fill="#dc2626">F = -mg sinθ</text>
  <line x1="128" y1="173" x2="152" y2="225" stroke="#9ca3af" stroke-width="1" stroke-dasharray="2,2"/>

  <!-- 分隔线 -->
  <line x1="212" y1="14" x2="212" y2="248" stroke="#d1d5db" stroke-dasharray="4,4"/>

  <!-- 右上：(3) 电梯 -->
  <text x="226" y="20" font-size="11" font-weight="bold" fill="#374151">(3) 上昇エレベーター (g' = g+α)</text>
  <rect x="232" y="30" width="95" height="82" fill="#ffffff" stroke="#374151" stroke-width="1.6"/>
  <line x1="278" y1="30" x2="278" y2="62" stroke="#374151" stroke-width="1.5"/>
  <circle cx="278" cy="67" r="6" fill="#dbeafe" stroke="#1e40af" stroke-width="1.4"/>
  <line x1="274" y1="73" x2="274" y2="99" stroke="#2563eb" stroke-width="1.8" marker-end="url(#arr-blue-003-7)"/>
  <text x="252" y="96" font-size="10" fill="#2563eb">mg</text>
  <line x1="282" y1="73" x2="282" y2="99" stroke="#dc2626" stroke-width="1.8" marker-end="url(#arr-red-003-7)"/>
  <text x="287" y="96" font-size="10" fill="#dc2626">mα</text>
  <!-- 上升加速度 α -->
  <line x1="348" y1="95" x2="348" y2="48" stroke="#111827" stroke-width="1.8" stroke-dasharray="4,2" marker-end="url(#arr-blk-003-7)"/>
  <text x="355" y="74" font-size="11" font-style="italic" fill="#111827">α</text>

  <!-- 右下：(4) 加速电车 -->
  <text x="226" y="136" font-size="11" font-weight="bold" fill="#374151">(4) 加速電車 (g' = √(g²+β²))</text>
  <rect x="232" y="146" width="125" height="82" fill="#ffffff" stroke="#374151" stroke-width="1.6"/>
  <line x1="312" y1="146" x2="280" y2="182" stroke="#374151" stroke-width="1.5"/>
  <circle cx="280" cy="182" r="6" fill="#dbeafe" stroke="#1e40af" stroke-width="1.4"/>
  <line x1="280" y1="188" x2="280" y2="218" stroke="#2563eb" stroke-width="1.8" marker-end="url(#arr-blue-003-7)"/>
  <text x="285" y="218" font-size="10" fill="#2563eb">mg</text>
  <line x1="274" y1="182" x2="245" y2="182" stroke="#dc2626" stroke-width="1.8" marker-end="url(#arr-red-003-7)"/>
  <text x="236" y="176" font-size="10" fill="#dc2626">mβ</text>
  <line x1="280" y1="182" x2="253" y2="213" stroke="#111827" stroke-width="1.6" stroke-dasharray="3,2" marker-end="url(#arr-blk-003-7)"/>
  <text x="236" y="218" font-size="10" fill="#111827">mg'</text>
  <!-- 加速度 β -->
  <line x1="366" y1="188" x2="405" y2="188" stroke="#111827" stroke-width="1.8" stroke-dasharray="4,2" marker-end="url(#arr-blk-003-7)"/>
  <text x="380" y="180" font-size="11" font-style="italic" fill="#111827">β</text>
</svg>

#### 【日本考场规范分步解答】

**(1)** 位置 $x\ (> 0)$ における糸の鉛直方向からの振れ角を $\theta$ とすると，$\sin\theta = \dfrac{x}{l}$ である。  
おもりにはたらく重力の接線成分は時計回り（負の向き）であるから，
$$F = -mg\sin\theta = -\frac{mg}{l}x$$

> 💡 讲师批注：务必注意**负号**！题干规定反时针（向右上方）为正方向，当小球在 $x > 0$（右侧）时，重力的切线分力指向最低点（顺时针方向），因此必带负号。

**(2)** $\theta$ が小さいとき，$x$ 軸方向の運動方程式は，
$$ma = -\frac{mg}{l}x \implies a = -\frac{g}{l}x$$
単振動の加速度 $a = -\omega^2 x$ と比較すると $\omega = \sqrt{\dfrac{g}{l}}$ であるから，周期 $T$ は，
$$T = \frac{2\pi}{\omega} = 2\pi\sqrt{\frac{l}{g}}$$

**(3)** 上向きに加速度 $\alpha$ で上昇中のエレベーター内の観測者から見ると，おもりには下向きに大きさ $m\alpha$ の慣性力がはたらく。  
したがって，見かけの重力加速度は $g' = g + \alpha$ となるから，(2) の $g$ を $g'$ で置き換えて，
$$T' = 2\pi\sqrt{\frac{l}{g + \alpha}}$$

**(4)** 水平方向に加速度 $\beta$ で移動中の電車内の観測者から見ると，おもりには進行方向と逆向き（水平向き）に大きさ $m\beta$ の慣性力がはたらく。  
重力 $mg$ と慣性力 $m\beta$ は直交しているため，見かけの重力加速度の大きさは $g' = \sqrt{g^2 + \beta^2}$ となる。したがって，
$$T'' = 2\pi\sqrt{\frac{l}{\sqrt{g^2 + \beta^2}}}$$

> 💡 讲师批注：非惯性系单摆周期的终极通杀法：只需算出合成后的**等效重力加速度大小 $g'$**，直接替换 $T = 2\pi\sqrt{l/g}$ 中的 $g$ 即可！注意若是自由落体电梯（向下加速 $\alpha = g$），则 $g' = 0$，单摆不会振动（$T \to \infty$）。

#### 【最终答案】
- **(1) $F = -\dfrac{mg}{l}x$**
- **(2) $T = 2\pi\sqrt{\dfrac{l}{g}}$**
- **(3) $T' = 2\pi\sqrt{\dfrac{l}{g + \alpha}}$**
- **(4) $T'' = 2\pi\sqrt{\dfrac{l}{\sqrt{g^2 + \beta^2}}}$**

---

### 例題 8（教材 P.42 / 页码 41）：浮力と単振動（浮力导致的简谐振动）

#### 【原题重现与翻译】
> **日文原题**：  
> 密度 $\rho$，断面積 $S$，長さ $L$ の一様な直方体を水面に浮かべて静止させた。水の密度を $\rho_0\ (> \rho)$，重力加速度の大きさを $g$ とする。  
> (1) 静止状態における水面下の長さ $l$ を求めよ。  
> (2) 直方体の上面が水面と一致するまで押し下げてから静かに手を放したところ，直方体は上下に振動した。振動の周期 $T$ と振幅 $A$ を求めよ。  
> (3) 振動中に静止状態と同じ位置に来たときの速さ $v$ を求めよ。また，最初にその位置に来るまでにかかる時間 $t$ を求めよ。
>
> **中文翻译**：  
> 将密度为 $\rho$、截面积为 $S$、长度为 $L$ 的均匀长方体漂浮在水面上并保持静止。设水的密度为 $\rho_0\ (> \rho)$，重力加速度大小为 $g$。  
> (1) 求静止状态下水面以下的长度 $l$。  
> (2) 将长方体向下压至其上表面恰好与水面齐平后由静止释放，长方体开始上下振动。求振动的周期 $T$ 与振幅 $A$。  
> (3) 求振动过程中经过静止平衡位置时的速率 $v$，以及从释放到首次到达该位置所需的时间 $t$。

#### 【考点与模型定位】
**浮力简谐振动模型**：浮力变化量 $\Delta F_{\text{浮}} = \rho_0 S g x$ 充当回复力（等效弹簧劲度系数 $K = \rho_0 S g$）。

#### 【多色矢量图解（SVG）】

<svg viewBox="0 0 420 260" width="420" height="260" xmlns="http://www.w3.org/2000/svg" style="background:#fafafa;border:1px solid #e5e7eb;border-radius:8px;">
  <defs>
    <marker id="arr-blue-003-8" markerWidth="7" markerHeight="7" refX="5" refY="3" orient="auto"><path d="M0,0 L0,6 L6,3 z" fill="#2563eb"/></marker>
    <marker id="arr-green-003-8" markerWidth="7" markerHeight="7" refX="5" refY="3" orient="auto"><path d="M0,0 L0,6 L6,3 z" fill="#16a34a"/></marker>
    <marker id="arr-blk-003-8" markerWidth="7" markerHeight="7" refX="5" refY="3" orient="auto"><path d="M0,0 L0,6 L6,3 z" fill="#111827"/></marker>
  </defs>
  <!-- 水域背景 -->
  <rect x="24" y="105" width="330" height="142" fill="#e0f2fe" stroke="none"/>
  <line x1="24" y1="105" x2="354" y2="105" stroke="#0284c7" stroke-width="2"/>
  <text x="32" y="236" font-size="11" fill="#0369a1">水 (密度 ρ₀)</text>

  <!-- 坐标参考线 -->
  <line x1="36" y1="60" x2="375" y2="60" stroke="#6b7280" stroke-width="1" stroke-dasharray="3,3"/>
  <text x="380" y="64" font-size="11" font-weight="bold" fill="#111827">O</text>
  <line x1="150" y1="84" x2="375" y2="84" stroke="#6b7280" stroke-width="1" stroke-dasharray="3,3"/>
  <text x="380" y="88" font-size="11" font-style="italic" fill="#374151">x</text>
  <line x1="265" y1="105" x2="375" y2="105" stroke="#0284c7" stroke-width="1" stroke-dasharray="3,2"/>
  <text x="378" y="109" font-size="10" fill="#dc2626">L-l (=A)</text>
  <!-- +x 轴 -->
  <line x1="370" y1="45" x2="370" y2="165" stroke="#111827" stroke-width="1.4" marker-end="url(#arr-blk-003-8)"/>
  <text x="376" y="168" font-size="11" font-style="italic" fill="#111827">+x</text>

  <!-- 状态 1：つりあい -->
  <text x="58" y="42" font-size="11" font-weight="bold" fill="#374151">つりあい</text>
  <rect x="60" y="60" width="46" height="125" fill="#d1d5db" fill-opacity="0.75" stroke="#374151" stroke-width="1.8"/>
  <text x="79" y="75" font-size="10" fill="#374151">ρ</text>
  <!-- 浮力与重力 -->
  <line x1="83" y1="120" x2="83" y2="86" stroke="#16a34a" stroke-width="2" marker-end="url(#arr-green-003-8)"/>
  <text x="46" y="95" font-size="9.5" font-weight="bold" fill="#16a34a">ρ₀Slg</text>
  <line x1="83" y1="138" x2="83" y2="174" stroke="#2563eb" stroke-width="2" marker-end="url(#arr-blue-003-8)"/>
  <text x="64" y="182" font-size="9.5" font-weight="bold" fill="#2563eb">ρSLg</text>
  <text x="110" y="150" font-size="10" font-style="italic" fill="#374151">l</text>

  <!-- 状态 2：変位 x -->
  <text x="166" y="42" font-size="11" font-weight="bold" fill="#374151">変位 x</text>
  <rect x="166" y="84" width="46" height="125" fill="#d1d5db" fill-opacity="0.75" stroke="#374151" stroke-width="1.8"/>
  <line x1="189" y1="145" x2="189" y2="96" stroke="#16a34a" stroke-width="2.2" marker-end="url(#arr-green-003-8)"/>
  <text x="148" y="100" font-size="9" font-weight="bold" fill="#16a34a">ρ₀S(l+x)g</text>
  <line x1="189" y1="162" x2="189" y2="198" stroke="#2563eb" stroke-width="2" marker-end="url(#arr-blue-003-8)"/>
  <text x="171" y="206" font-size="9.5" font-weight="bold" fill="#2563eb">ρSLg</text>
  <text x="216" y="164" font-size="10" fill="#374151">l+x</text>

  <!-- 状态 3：最下点（释放瞬间） -->
  <text x="274" y="42" font-size="11" font-weight="bold" fill="#374151">最下点(t=0)</text>
  <rect x="275" y="105" width="46" height="125" fill="#d1d5db" fill-opacity="0.75" stroke="#374151" stroke-width="1.8"/>
  <text x="292" y="170" font-size="11" font-style="italic" fill="#374151">L</text>

  <!-- 图例 -->
  <text x="218" y="242" font-size="10" fill="#2563eb">■ 蓝：重力 ρSLg</text>
  <text x="312" y="242" font-size="10" fill="#16a34a">■ 绿：浮力</text>
</svg>

#### 【日本考场规范分步解答】

直方体の質量は $m = \rho SL$ である。

**(1)** 静止状態（つりあい）では重力と浮力がつりあっているので，
$$\rho SLg = \rho_0 Slg \implies l = \frac{\rho}{\rho_0}L$$

**(2)** 静止状態における直方体の上面の位置を原点 $O$ とし，鉛直下向きを正とする $x$ 軸をとる。  
位置 $x$ にあるとき，水面下の長さは $l + x$ であるから，運動方程式は，
$$\rho SLa = \rho SLg - \rho_0 S(l + x)g$$
(1) の $\rho SLg = \rho_0 Slg$ を代入すると，
$$\rho SLa = -\rho_0 Sgx \implies a = -\frac{\rho_0 g}{\rho L}x$$
単振動の式 $a = -\omega^2 x$ と比較すると，角振動数は $\omega = \sqrt{\dfrac{\rho_0 g}{\rho L}}$ となる。  
したがって，周期 $T$ と振幅 $A$（上面が水面と一致するまでの押し下げ距離 $L - l$）は，
$$T = \frac{2\pi}{\omega} = 2\pi\sqrt{\frac{\rho L}{\rho_0 g}}, \qquad A = L - l = \left(1 - \frac{\rho}{\rho_0}\right)L$$

> 💡 讲师批注：把浮力振动类比成弹簧振子就一目了然！等效劲度系数 $K = \rho_0 Sg$，物体质量 $m = \rho SL$，代入万能周期公式 $T = 2\pi\sqrt{\dfrac{m}{K}} = 2\pi\sqrt{\dfrac{\rho SL}{\rho_0 Sg}} = 2\pi\sqrt{\dfrac{\rho L}{\rho_0 g}}$，瞬间验算无误！

**(3)** 静止状態と同じ位置は**振動中心**であるため，このときの速さ $v$ は最大速さ $v_{\max} = A\omega$ である。  
（または力学的エネルギー保存則 $\dfrac{1}{2}\rho SL v^2 = \dfrac{1}{2}\rho_0 Sg (L - l)^2$ より）
$$v = A\omega = \left(1 - \frac{\rho}{\rho_0}\right)L\sqrt{\frac{\rho_0 g}{\rho L}}$$
また，最下点（振動の端）から最初に振動中心に来るまでの時間はちょうど $\dfrac{1}{4}$ 周期であるから，
$$t = \frac{T}{4} = \frac{\pi}{2}\sqrt{\frac{\rho L}{\rho_0 g}}$$

> 💡 讲师批注：请提醒学生注意一个隐含前提：柱体在向上弹起到达最高点（$x = -A$）时不能完全离开水面，否则脱离水面后浮力为 $0$ 将不再是简谐振动！本题题干中释放点为上表面齐平（$A = L - l$），只要 $l \ge L - l$（即 $\rho \ge \dfrac{1}{2}\rho_0$）就不会脱离水面；EJU 难题偶尔会追问这个「飛び出さない条件」！

#### 【最终答案】
- **(1) $l = \dfrac{\rho}{\rho_0}L$**
- **(2) $T = 2\pi\sqrt{\dfrac{\rho L}{\rho_0 g}}$，$A = \left(1 - \dfrac{\rho}{\rho_0}\right)L$**
- **(3) $v = \left(1 - \dfrac{\rho}{\rho_0}\right)L\sqrt{\dfrac{\rho_0 g}{\rho L}}$，$t = \dfrac{\pi}{2}\sqrt{\dfrac{\rho L}{\rho_0 g}}$**

---

### 核心模型图解补充（教材 P.32 & P.43–44 概念页板书素材）

为方便纯日文板书授课，将切片内高频考查的两大概念页（反复斜碰等比规律、开普勒定律与万有引力势能）也配齐标准多色 SVG 图解：

#### 补充图 A：滑らかな平面との繰り返し斜め衝突（P.32） & ケプラーの法則（P.44）

<svg viewBox="0 0 420 220" width="420" height="220" xmlns="http://www.w3.org/2000/svg" style="background:#fafafa;border:1px solid #e5e7eb;border-radius:8px;">
  <defs>
    <marker id="arr-blk-003-s" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto"><path d="M0,0 L0,6 L6,3 z" fill="#111827"/></marker>
    <marker id="arr-red-003-s" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto"><path d="M0,0 L0,6 L6,3 z" fill="#dc2626"/></marker>
  </defs>
  <!-- 左半：反复斜碰 -->
  <text x="16" y="20" font-size="11" font-weight="bold" fill="#374151">繰り返し斜め衝突 (等比数列)</text>
  <line x1="20" y1="175" x2="205" y2="175" stroke="#374151" stroke-width="1.8" marker-end="url(#arr-blk-003-s)"/>
  <line x1="25" y1="175" x2="25" y2="38" stroke="#374151" stroke-width="1.4" marker-end="url(#arr-blk-003-s)"/>
  <!-- 第1跳 -->
  <path d="M 25 175 Q 65 25 105 175" fill="none" stroke="#2563eb" stroke-width="2"/>
  <line x1="65" y1="100" x2="65" y2="175" stroke="#6b7280" stroke-width="1" stroke-dasharray="3,2"/>
  <text x="68" y="138" font-size="10" fill="#2563eb">h</text>
  <text x="54" y="190" font-size="10" fill="#374151">t, l</text>
  <!-- 第2跳 -->
  <path d="M 105 175 Q 133 95 161 175" fill="none" stroke="#2563eb" stroke-width="2"/>
  <line x1="133" y1="135" x2="133" y2="175" stroke="#6b7280" stroke-width="1" stroke-dasharray="3,2"/>
  <text x="135" y="155" font-size="9.5" fill="#2563eb">e²h</text>
  <text x="120" y="190" font-size="9.5" fill="#374151">et, el</text>
  <!-- 第3跳 -->
  <path d="M 161 175 Q 180 135 199 175" fill="none" stroke="#2563eb" stroke-width="2"/>
  <text x="172" y="152" font-size="9" fill="#2563eb">e⁴h</text>
  <text x="166" y="190" font-size="9" fill="#374151">e²t, e²l</text>
  <text x="26" y="209" font-size="9.5" fill="#dc2626">水平：等速直線 / 鉛直：v_y' = -ev_y</text>

  <!-- 分隔线 -->
  <line x1="214" y1="14" x2="214" y2="208" stroke="#d1d5db" stroke-dasharray="4,4"/>

  <!-- 右半：开普勒定律 -->
  <text x="228" y="20" font-size="11" font-weight="bold" fill="#374151">ケプラーの法則 (S₁ = S₂)</text>
  <ellipse cx="318" cy="112" rx="84" ry="52" fill="none" stroke="#374151" stroke-width="1.8"/>
  <!-- 长半轴 a -->
  <line x1="234" y1="112" x2="402" y2="112" stroke="#9ca3af" stroke-width="1" stroke-dasharray="3,2"/>
  <line x1="318" y1="60" x2="318" y2="164" stroke="#9ca3af" stroke-width="1" stroke-dasharray="3,2"/>
  <text x="355" y="126" font-size="11" font-style="italic" fill="#374151">a</text>
  <!-- 面积 S1（近日点） -->
  <path d="M 272 112 L 234 112 A 84 52 0 0 1 258 76 Z" fill="#dbeafe" stroke="#2563eb" stroke-width="1.2"/>
  <text x="246" y="102" font-size="10" font-weight="bold" fill="#1e40af">S₁</text>
  <!-- 面积 S2（远日点） -->
  <path d="M 272 112 L 382 78 A 84 52 0 0 1 394 92 Z" fill="#dbeafe" stroke="#2563eb" stroke-width="1.2"/>
  <text x="364" y="96" font-size="10" font-weight="bold" fill="#1e40af">S₂</text>
  <!-- 太阳（焦点） -->
  <circle cx="272" cy="112" r="6" fill="#f59e0b" stroke="#b45309" stroke-width="1.4"/>
  <text x="260" y="132" font-size="10" font-weight="bold" fill="#b45309">太陽</text>
  <!-- 近日点・远日点 -->
  <circle cx="234" cy="112" r="3" fill="#dc2626"/>
  <text x="220" y="146" font-size="9.5" fill="#dc2626">近日点(速)</text>
  <circle cx="402" cy="112" r="3" fill="#16a34a"/>
  <text x="368" y="146" font-size="9.5" fill="#16a34a">遠日点(遅)</text>
  <text x="242" y="196" font-size="10" fill="#111827">第3法則：T² / a³ = k (一定)</text>
</svg>

---

## 4. 全局术语表同步说明

本切片新增的 **56 条** 日文物理核心术语与假名注音已整理写入本切片术语清单：[`.glossary_003.md`](file:///Users/baohan/Desktop/EJU/notes_物理/.glossary_003.md)，待主控统一合并去重写入全局术语表 [glossary_all.md](file:///Users/baohan/Desktop/EJU/notes_物理/glossary_all.md)。
