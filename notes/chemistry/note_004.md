# EJU 化学基础・第三章 物質の反応（切片 004：P46–P60）

> **对应原教材**：格致学苑《EJU 化学対策》「化学基礎・第三章 物質の反応」（第 1 节续–第 8 节，原书页码 P.45–P.59，PDF 第 46–60 页）
> **核心主题**：化学反应与热（热化学方程式、盖斯定律、键能与比热）、化学反应速率、化学平衡与勒夏特列原理、酸与碱的定义及强弱
> **适用对象**：忘却国内高中化学基础、零起步对接日本 EJU 留考化学体系的同学

---

## 1. 本节前置：国内高中化学基础唤醒

本切片涵盖物理化学最核心的四大支柱：**反应热（热力学）$\to$ 反应速率（动力学）$\to$ 化学平衡 $\to$ 酸碱基础**。只要把“能量守恒”与“动态平衡”两条主线吃透，EJU 理论化学的计算大题就能稳拿高分。

### 1.1 国内高中核心基础快速唤醒
1. **反应热与盖斯定律（ヘスの法則）**
   - 化学反应伴随能量变化：反应物总能量高于生成物时**放热（発熱反応）**，反之**吸热（吸熱反応）**。
   - **盖斯定律**：化学反应的反应热只取决于反应的**始态（反应物）和终态（生成物）**及其聚集状态，与反应经历的中间途径无关。
   - **键能（結合エネルギー）**：拆开 $1\text{ mol}$ 气态共价键需要**吸收**的能量（断键吸热、成键放热）。
   - **量热公式**：质量为 $m\text{ [g]}$、比热容为 $c\text{ [J/(g}\cdot\text{K)]}$ 的物质温度升高 $\Delta T\text{ [K]}$ 吸收的热量为：
     $$Q = m \cdot c \cdot \Delta T\text{ [J]}$$
2. **活化能与化学反应速率**
   - **活化能（活性化エネルギー）**：普通分子变成能发生有效碰撞的活化分子所需的最小能量。
   - **催化剂（触媒）**：通过改变反应途径**降低正、逆反应的活化能**，从而同等程度加快正逆反应速率，但**自身在反应前后不变，且绝对不改变反应热 $Q$ 和化学平衡位置**。
   - 加快反应速率的 4 大手段：**增大浓度（或气体分压）、升高温度、加入催化剂、增大固体表面积（粉碎）**。
3. **化学平衡与勒夏特列原理**
   - **可逆反应**在密闭容器中达到平衡的标志：$v_{\text{正}} = v_{\text{逆}} \neq 0$，各组分浓度不再随时间变化（动态平衡，并非反应停止）。
   - **平衡常数 $K_c$ 与 $K_p$**：对于 $a\text{A} + b\text{B} \rightleftharpoons y\text{Y} + z\text{Z}$，平衡常数**仅是温度的函数**，与浓度、压强、催化剂无关。
   - **勒夏特列原理（平衡移动原理）**：改变影响平衡的一个条件（浓度、压强、温度），平衡就向能够**减弱（緩和）**这种改变的方向移动。
4. **酸与碱的定义及电离**
   - **阿伦尼乌斯定义**：水中电离出 $\text{H}^+$ 为酸，电离出 $\text{OH}^-$ 为碱。
   - **布朗斯特-劳里定义（质子酸碱理论）**：能**给出 $\text{H}^+$（质子）**的是酸，能**接受 $\text{H}^+$**的是碱（可解释 $\text{NH}_3$ 无 $\text{OH}^-$ 却显碱性）。
   - **强弱电解质与电离度 $\alpha$**：$\alpha = \dfrac{\text{已电离的电解质物质的量}}{\text{溶解的电解质总物质的量}}$（$0 \le \alpha \le 1$）。强酸强碱 $\alpha \approx 1$（写单箭头 `→`），弱酸弱碱 $\alpha \ll 1$（写可逆号 `⇌`）。

---

### 1.2 中日化学体系差异提醒（EJU 避坑必看！）

1. **热化学方程式的写法差异（最高频丢分点！）**
   - **国内高中**：用 `→` 连接，右侧写 $\Delta H$，**放热 $\Delta H \lt 0$，吸热 $\Delta H \gt 0$**，状态用 `(s), (l), (g), (aq)`。
   - **日本教材 / EJU 经典体系**：中间必须写等号 **`=`**（不可写 `→`），热量直接写在右侧，**放热写 `+ Q kJ`，吸热写 `- Q kJ`**！物质状态用汉字括注：`(固)`、`(液)`、`(気)`、`(黒鉛)`、`aq`。
   - **符号换算口诀**：`+ Q kJ`（放热）$\iff \Delta H = -Q\text{ kJ/mol}$；`- Q kJ`（吸热）$\iff \Delta H = +Q\text{ kJ/mol}$。符号恰好相反，切勿混淆！
2. **各类反应热的“$1\text{ mol}$ 基准”与分数系数**
   - 在日本热化学方程式中，为了保证“所求对象为 $1\text{ mol}$”，**允许且经常出现分数系数**（如 $\frac{1}{2}\text{O}_2$、$\frac{7}{2}\text{O}_2$）：
     - **生成熱**：右侧生成物系数必须为 **1**，左侧必须全部是**单质**（碳必须是 `C(黒鉛)`，单质生成热规定为 $0\text{ kJ/mol}$）。
     - **燃焼熱**：左侧可燃物系数必须为 **1**，碳变 $\text{CO}_2(\text{気})$，氢变 $\text{H}_2\text{O}(\text{液})$。
     - **中和熱**：右侧生成的 **$\text{H}_2\text{O}(\text{液})$ 系数必须为 1**。强酸强碱稀溶液中和热恒约为 **$56.5\text{ kJ/mol}$**。
     - **溶解熱**：左侧溶质系数必须为 **1**，大量溶剂水写作 **`+ aq`**，溶液写作 `溶質 aq`。
3. **两大便利公式的“右减左”铁律（注意与国内 $\Delta H$ 区分！）**
   - 在日本热化学方程式（放热为正 $Q$）体系下，**无论是用生成热还是用键能，全部都是“右减左”**！
     - 已知全部物质生成热：$Q = \sum(\text{右辺の生成熱}) - \sum(\text{左辺の生成熱})$
     - 已知全部物质键能：$Q = \sum(\text{右辺の結合エネルギー}) - \sum(\text{左辺の結合エネルギー})$
   - 千万别套用国内“$\Delta H = \text{左键能} - \text{右键能}$”的顺序直接算 $Q$，否则符号会完全反掉！
4. **「塩基（えんき）」与「アルカリ」的区别**
   - 国内统称“碱”，日本学术上统一称为 **塩基（Base）**；其中易溶于水、显强碱性的碱（如 $\text{NaOH}, \text{KOH}, \text{Ba(OH)}_2$）才叫 **アルカリ**。
5. **磷酸（$\text{H}_3\text{PO}_4$）与草酸（$\text{H}_2\text{C}_2\text{O}_4$）的定位**
   - 日本教材把 **リン酸（$\text{H}_3\text{PO}_4$）** 单独归类为 3 价 **中程度の酸（中强酸）**，把 **シュウ酸（$\text{H}_2\text{C}_2\text{O}_4$）** 归为 2 价弱酸，并明确指出 **3 价强盐基不存在（なし）**。

> ⚠️ **原教材印刷勘误提醒（讲师逐页人工核对参考图发现 7 处错误）**：
> 1. **原书 P.45（PDF 第 46 页）**：`例）エチレンC2H2（気）の生成熱 -52kJkJ/mol` 与 `2C(黒鉛)+2H2(気)=C2H2(気)-52kJ` 存在两处印刷错误！乙烯（エチレン）化学式应为 **$\text{C}_2\text{H}_4$**（不是乙炔 $\text{C}_2\text{H}_2$，且左侧有 $2\text{H}_2$ 共 4 个 $\text{H}$），单位应为 **`-52 kJ/mol`**（多印了一个 `kJ`）。
> 2. **原书 P.46（PDF 第 47 页）**：练习 (2) 解答分母误印为 `22.4 mol/L`，标准状态气体摩尔体积的正确单位应为 **`22.4 L/mol`**。
> 3. **原书 P.48（PDF 第 49 页）**：练习 (2) 解答中 `エタンの生成熱を Q とすると` 属于笔误，其下方列的是乙烷完全燃烧的热化学方程式，正确应为 **`エタンの燃焼熱を Q とすると`**。
> 4. **原书 P.50（PDF 第 51 页）**：练习 (2) 解答中 `-Q₁ = -1664 より Q₁ = 1644 kJ/mol` 存在数字印错，正确应为 **`Q₁ = 1664 kJ/mol`**（其下一行计算 `1664/4 = 416` 时用的正是正确的 1664）。
> 5. **原书 P.52（PDF 第 53 页）**：`活性化状態` 定义中 `エネルギーの高いフィ安定な状態` 为错别字，正确应为 **`不安定な状態`**（不稳定状态）。
> 6. **原书 P.58（PDF 第 59 页）**：勒夏特列原理表格第 1 行，`濃度を増やす`（增大浓度）对应的平衡移动方向误印为 `温度が減少する方向`，正确应为 **`濃度が減少する方向`**（浓度减小的方向）。
> 7. **原书 P.59（PDF 第 60 页）**：① `ブレステッド・ローリーの定義` 漏印拨音 `ン`，标准日文为 **ブレンステッド・ローリーの定義**；② 其下方的两个例式上下位置放反——`HCl + H₂O → Cl⁻ + H₃O⁺` 才是典型说明酸（$\text{HCl}$ 给出 $\text{H}^+$）的例子，而 `NH₃ + H₂O → NH₄⁺ + OH⁻` 才是典型说明盐基（$\text{NH}_3$ 接受 $\text{H}^+$）的例子。

---

## 2. 日文化学核心词汇、物质名称与假名注音（板书必备）

### 2.1 反应热、状态变化热与盖斯定律
- **熱化学方程式（ねつかがくほうていしき / netsukagaku hōteishiki）** — 热化学方程式
- **発熱反応・吸熱反応（はつねつはんのう・きゅうねつはんのう / hatsunetsu hannō, kyūnetsu hannō）** — 放热反应・吸热反应
- **反応熱（はんのうねつ / hannōnetsu）** — 反应热
- **生成熱（せいせいねつ / seiseinetsu）** — 生成热
- **燃焼熱（ねんしょうねつ / nenshōnetsu）** — 燃烧热
- **中和熱（ちゅうわねつ / chūwanetsu）** — 中和热
- **溶解熱（ようかいねつ / yōkainetsu）** — 溶解热
- **融解熱・凝固熱（ゆうかいねつ・ぎょうこねつ / yūkainetsu, gyōkonetsu）** — 熔化热・凝固热
- **蒸発熱・凝縮熱（じょうはつねつ・ぎょうしゅくねつ / jōhatsunetsu, gyōshukunetsu）** — 汽化热（蒸发热）・液化热（凝缩热）
- **昇華熱（しょうかねつ / shōkanetsu）** — 升华热
- **ヘスの法則 / 総熱量保存の法則（へすのほうそく / そうねつりょうほぞんのほうそく）** — 盖斯定律 / 总热量守恒定律
- **エネルギー図（えねるぎーず / enerugī-zu）** — 能量图
- **結合エネルギー（けつごうエネルギー / ketsugō enerugī）** — 键能（结合能）
- **解離エネルギー（かいりエネルギー / kairi enerugī）** — 解离能（原子化能）
- **比熱（ひねつ / hinetsu）** — 比热容
- **断熱容器（だんねつようき / dannetsu yōki）** — 绝热容器

### 2.2 化学反应速率与化学平衡
- **活性化状態（かっせいかじょうたい / kasseika jōtai）** — 活化状态（过渡态）
- **活性化エネルギー（かっせいかエネルギー / kasseika enerugī）** — 活化能
- **触媒（しょくばい / shokubai）** — 催化剂
- **正反応・逆反応（せいはんのう・ぎゃくはんのう / seihannō, gyakuhannō）** — 正反应・逆反应
- **反応速度（はんのうそくど / hannō sokudo）** — 反应速率
- **反応速度式（はんのうそくどしき / hannō sokudoshiki）** — 反应速率方程
- **反応速度定数（はんのうそくどていすう / hannō sokudo teisū）** — 反应速率常数（$k$）
- **初期濃度（しょきのうど / shoki nōdo）** — 初始浓度
- **可逆反応・不可逆反応（かぎゃくはんのう・ふかぎゃくはんのう）** — 可逆反应・不可逆反应
- **化学平衡（かがくへいこう / kagaku heikō）** — 化学平衡
- **平衡状態（へいこうじょうたい / heikō jōtai）** — 平衡状态
- **濃度平衡定数（のうどへいこうていすう / nōdo heikō teisū）** — 浓度平衡常数（$K_c$）
- **圧平衡定数（あつへいこうていすう / atsu heikō teisū）** — 压强平衡常数（$K_p$）
- **分圧・全圧（ぶんあつ・ぜんあつ / bun'atsu, zen'atsu）** — 分压・总压
- **ルシャトリエの原理（るしゃとりえのげんり / Rushatorye no genri）** — 勒夏特列原理
- **加圧・減圧（かあつ・げんあつ / kaatsu, gen'atsu）** — 加压・减压
- **加熱・冷却（かねつ・れいきゃく / kanetsu, reikyaku）** — 加热・冷却

### 2.3 酸与碱的定义、电离及常见物质名
- **酸・塩基（さん・えんき / san, enki）** — 酸・碱
- **アレニウスの定義（あれにうすのていぎ / Areniusu no teigi）** — 阿伦尼乌斯酸碱定义
- **ブレンステッド・ローリーの定義（ぶれんすてっど・ろーりーのていぎ）** — 布朗斯特-劳里酸碱定义
- **強酸・弱酸（きょうさん・じゃくさん / kyōsan, jakusan）** — 强酸・弱酸
- **強塩基・弱塩基（きょうえんき・じゃくえんき / kyōenki, jakuenki）** — 强碱・弱碱
- **価数（かすう / kasū）** — 元数/价数（1価・2価・3価）
- **電離度（でんりど / denrido）** — 电离度（$\alpha$）
- **電解質（でんかいしつ / denkaishitsu）** — 电解质
- **メタン（めたん / metan）** — 甲烷（$\text{CH}_4$）
- **エタン（えたん / etan）** — 乙烷（$\text{C}_2\text{H}_6$）
- **プロパン（ぷろぱん / puropan）** — 丙烷（$\text{C}_3\text{H}_8$）
- **エチレン（えちれん / echiren）** — 乙烯（$\text{C}_2\text{H}_4$）
- **エタノール（えたのーる / etanōru）** — 乙醇（$\text{C}_2\text{H}_5\text{OH}$）
- **一酸化炭素（いっさんかたんそ / issanka tanso）** — 一氧化碳（$\text{CO}$）
- **ヨウ化水素（ようかすいそ / yōka suiso）** — 碘化氢（$\text{HI}$）
- **二酸化硫黄・三酸化硫黄（にさんかいおう・さんさんかいおう）** — 二氧化硫（$\text{SO}_2$）・三氧化硫（$\text{SO}_3$）
- **希硫酸（きりゅうさん / kiryūsan）** — 稀硫酸（$\text{H}_2\text{SO}_4$ 水溶液）
- **硝酸（しょうさん / shōsan）** — 硝酸（$\text{HNO}_3$）
- **酢酸（さくさん / sakusan）** — 乙酸/醋酸（$\text{CH}_3\text{COOH}$）
- **炭酸（たんさん / tansan）** — 碳酸（$\text{H}_2\text{CO}_3$）
- **硫化水素（りゅうかすいそ / ryūka suiso）** — 硫化氢（$\text{H}_2\text{S}$）
- **シュウ酸（しゅうさん / shūsan）** — 草酸（$\text{H}_2\text{C}_2\text{O}_4$）
- **リン酸（りんさん / rinsan）** — 磷酸（$\text{H}_3\text{PO}_4$）
- **水酸化ナトリウム（すいさんかなとりうむ / suisanka natoriumu）** — 氢氧化钠（$\text{NaOH}$）
- **水酸化カリウム（すいさんかかりうむ / suisanka kariumu）** — 氢氧化钾（$\text{KOH}$）
- **水酸化カルシウム（すいさんかかるしうむ / suisanka karushiumu）** — 氢氧化钙（$\text{Ca(OH)}_2$）
- **水酸化バリウム（すいさんかばりうむ / suisanka bariumu）** — 氢氧化钡（$\text{Ba(OH)}_2$）
- **水酸化マグネシウム（すいさんかまぐねしうむ）** — 氢氧化镁（$\text{Mg(OH)}_2$）
- **水酸化銅(II)（すいさんかどう に）** — 氢氧化铜（$\text{Cu(OH)}_2$）
- **水酸化アルミニウム（すいさんかあるみにうむ）** — 氢氧化铝（$\text{Al(OH)}_3$）
- **水酸化鉄(III)（すいさんかてつ さん）** — 氢氧化铁（$\text{Fe(OH)}_3$）
- **オキソニウムイオン（おきそにうむいおん / okisoniumu ion）** — 水合氢离子（$\text{H}_3\text{O}^+$）

### 关键化学方程式与公式的日语课堂口语读法
1. **热化学方程式**：$\text{C}(\text{黒鉛}) + \text{O}_2(\text{気}) = \text{CO}_2(\text{気}) + 394\text{ kJ}$
   - 日语读法：「シー こくえん たす オーツー きたい イコール シーオーツー きたい プラス さんびゃくきゅうじゅうよん キロジュール」
2. **比热公式**：$Q = mc\Delta T$
   - 日语读法：「キュー イコール エム・シー・デルタティー」
3. **浓度平衡常数**：$K_c = \dfrac{[\text{HI}]^2}{[\text{H}_2][\text{I}_2]}$
   - 日语读法：「ケーシー イコール エイチツーののうど かける アイツーののうど ぶんの エイチアイののうどの にじょう」
4. **可逆反应**：$\text{H}_2 + \text{I}_2 \rightleftharpoons 2\text{HI}$
   - 日语读法：「エイチツー たす アイツー かぎゃくやじるし に エイチアイ」（或读作「へいこう に エイチアイ」）
5. **弱酸电离**：$\text{CH}_3\text{COOH} \rightleftharpoons \text{H}^+ + \text{CH}_3\text{COO}^-$
   - 日语读法：「さくさん かぎゃく すいそイオン たす さくさんイオン」

---

## 3. 核心知识点图解与逐题深度解析

### 3.1 反应热的种类与状态变化热（原书 P.45–P.46 / PDF P.46–P.47）

#### 【核心图解：水的状态变化能量图（SVG）】
<svg viewBox="0 0 420 260" xmlns="http://www.w3.org/2000/svg" style="background:#ffffff;border:1px solid #e2e8f0;border-radius:8px;max-width:100%;">
  <defs>
    <marker id="arr-up-red" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 10 L 5 0 L 10 10 z" fill="#dc2626"/>
    </marker>
    <marker id="arr-dn-blue" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M 0 0 L 5 10 L 10 0 z" fill="#2563eb"/>
    </marker>
    <marker id="arr-axis" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M 0 10 L 5 0 L 10 10 z" fill="#334155"/>
    </marker>
  </defs>
  <!-- 标题 -->
  <text x="210" y="22" text-anchor="middle" font-size="13" font-weight="bold" fill="#0f172a">水 (H₂O) 的状态变化能量图（1 mol 基准）</text>
  <!-- 纵轴 -->
  <line x1="42" y1="235" x2="42" y2="40" stroke="#334155" stroke-width="1.8" marker-end="url(#arr-axis)"/>
  <text x="42" y="34" text-anchor="middle" font-size="10.5" font-weight="bold" fill="#334155">高</text>
  <text x="42" y="248" text-anchor="middle" font-size="10.5" font-weight="bold" fill="#334155">低</text>
  <text x="22" y="138" text-anchor="middle" font-size="11" fill="#475569" writing-mode="tb">エネルギー</text>

  <!-- 三条能级线 -->
  <!-- H2O(気) y=58 -->
  <line x1="65" y1="58" x2="385" y2="58" stroke="#0f172a" stroke-width="2"/>
  <text x="72" y="52" font-size="12" font-weight="bold" fill="#0f172a">H₂O(気)</text>
  <!-- H2O(液) y=178 -->
  <line x1="65" y1="178" x2="310" y2="178" stroke="#0f172a" stroke-width="2"/>
  <text x="72" y="172" font-size="12" font-weight="bold" fill="#0f172a">H₂O(液)</text>
  <!-- H2O(固) y=222 -->
  <line x1="65" y1="222" x2="385" y2="222" stroke="#0f172a" stroke-width="2"/>
  <text x="72" y="216" font-size="12" font-weight="bold" fill="#0f172a">H₂O(固)</text>

  <!-- 放热箭头（向下，蓝色） -->
  <!-- 凝縮熱 44kJ -->
  <line x1="150" y1="60" x2="150" y2="173" stroke="#2563eb" stroke-width="3" marker-end="url(#arr-dn-blue)"/>
  <text x="142" y="114" text-anchor="end" font-size="10.5" font-weight="bold" fill="#1d4ed8">凝縮熱</text>
  <text x="142" y="128" text-anchor="end" font-size="10" fill="#2563eb">44 kJ 発熱 (+)</text>
  <!-- 凝固熱 6.0kJ -->
  <line x1="150" y1="180" x2="150" y2="217" stroke="#2563eb" stroke-width="3" marker-end="url(#arr-dn-blue)"/>
  <text x="142" y="203" text-anchor="end" font-size="10" font-weight="bold" fill="#1d4ed8">凝固熱 6.0 kJ (+)</text>

  <!-- 吸热箭头（向上，红色） -->
  <!-- 蒸発熱 44kJ -->
  <line x1="210" y1="176" x2="210" y2="63" stroke="#dc2626" stroke-width="3" marker-end="url(#arr-up-red)"/>
  <text x="218" y="114" text-anchor="start" font-size="10.5" font-weight="bold" fill="#b91c1c">蒸発熱</text>
  <text x="218" y="128" text-anchor="start" font-size="10" fill="#dc2626">44 kJ 吸熱 (−)</text>
  <!-- 融解熱 6.0kJ -->
  <line x1="210" y1="220" x2="210" y2="183" stroke="#dc2626" stroke-width="3" marker-end="url(#arr-up-red)"/>
  <text x="218" y="203" text-anchor="start" font-size="10" font-weight="bold" fill="#b91c1c">融解熱 6.0 kJ (−)</text>

  <!-- 昇華熱 50kJ -->
  <line x1="322" y1="220" x2="322" y2="63" stroke="#ea580c" stroke-width="3.2" marker-end="url(#arr-up-red)"/>
  <text x="330" y="132" text-anchor="start" font-size="11" font-weight="bold" fill="#c2410c">昇華熱</text>
  <text x="330" y="147" text-anchor="start" font-size="10.5" fill="#ea580c">50 kJ 吸熱 (−)</text>
  <text x="330" y="162" text-anchor="start" font-size="9.5" fill="#64748b">(= 6.0 + 44)</text>
</svg>

> 💡 **讲师批注**：从能量图一眼就能看出 **$\text{昇華熱} = \text{融解熱} + \text{蒸発熱}$**（$50 = 6.0 + 44\text{ kJ/mol}$），这就是盖斯定律在物态变化中的最直观体现！记住口诀：**能级由高往低掉 $\to$ 放热（`+`）；由低往高爬 $\to$ 吸热（`-`）**。

---

#### 练习组 1：热化学方程式的书写（原书 P.46 / PDF P.47）

##### 【原题重现与翻译】
> 熱化学方程式で表せ。（用热化学方程式表示下列变化。）
> (1) エタノール $\text{C}_2\text{H}_5\text{OH}$ の生成熱は $277\text{ kJ}$ である。
> （乙醇 $\text{C}_2\text{H}_5\text{OH}$ 的生成热为 $277\text{ kJ}$。）
> (2) 標準状態で $5.6\text{ L}$ のプロパン $\text{C}_3\text{H}_8$ が完全燃焼すると $555\text{ kJ}$ の熱が生じた。
> （标准状态下 $5.6\text{ L}$ 丙烷 $\text{C}_3\text{H}_8$ 完全燃烧放出了 $555\text{ kJ}$ 的热量。）
> (3) $0.10\text{ mol/L}$ の希硫酸 $500\text{ mL}$ が多量の水に溶解すると $4.8\text{ kJ}$ の熱が生じた。
> （$0.10\text{ mol/L}$ 的稀硫酸 $500\text{ mL}$ 溶解于大量水中时放出了 $4.8\text{ kJ}$ 的热量。）

##### 【考点定位】
生成热、燃烧热、溶解热的 $1\text{ mol}$ 基准定义，以及热化学方程式的规范书写（物质状态、等号、符号与有效数字）。

##### 【分步标准解答】
- **(1) 乙醇的生成热**：
  - 基准：右侧生成 **$1\text{ mol}$ $\text{C}_2\text{H}_5\text{OH}(\text{液})$**。
  - 左侧必须是构成它的稳定单质：$\text{C}(\text{黒鉛})$、$\text{H}_2(\text{気})$、$\text{O}_2(\text{気})$。
  - 按原子守恒配平左侧：$2\text{C} + 3\text{H}_2 + \frac{1}{2}\text{O}_2$。生成热为正值（无负号），表示放热 `+ 277 kJ`。
  > 💡 **讲师批注**：写生成热时，碳的单质**必须写 `C(黒鉛)`**（不能写金刚石，也不能只写 `C(固)`），常温下乙醇是液体 `(液)`。

- **(2) 丙烷的燃烧热**：
  - 第 1 步：求标准状态下 $5.6\text{ L}$ 丙烷的物质的量：
    $$n(\text{C}_3\text{H}_8) = \frac{5.6\text{ L}}{22.4\text{ L/mol}} = 0.25\text{ mol}$$
  - 第 2 步：换算成 $1\text{ mol}$ 丙烷完全燃烧放出的热量：
    $$Q = \frac{555\text{ kJ}}{0.25\text{ mol}} = 2220\text{ kJ/mol} \fallingdotseq 2.2 \times 10^3\text{ kJ/mol}$$
  - 第 3 步：写出 $1\text{ mol}$ $\text{C}_3\text{H}_8(\text{気})$ 完全燃烧生成 $\text{CO}_2(\text{気})$ 和 $\text{H}_2\text{O}(\text{液})$ 的热化学方程式（注意有效数字：题中 $5.6\text{ L}$ 为 2 位有效数字，故保留 2 位写成 $2.2 \times 10^3\text{ kJ}$）。
  > 💡 **讲师批注**：再次提醒，原书解答中分母误印成 `22.4 mol/L`，正确单位是 **`22.4 L/mol`**！另外燃烧热生成的水默认是**液态 $\text{H}_2\text{O}(\text{液})$**。

- **(3) 硫酸的溶解热**：
  - 第 1 步：求溶质 $\text{H}_2\text{SO}_4$ 的物质的量：
    $$n(\text{H}_2\text{SO}_4) = 0.10\text{ mol/L} \times \frac{500}{1000}\text{ L} = 0.050\text{ mol}$$
  - 第 2 步：换算成 $1\text{ mol}$ $\text{H}_2\text{SO}_4$ 溶解于大量水时放出的热量：
    $$Q = \frac{4.8\text{ kJ}}{0.050\text{ mol}} = 96\text{ kJ/mol}$$
  - 第 3 步：写出溶解热的热化学方程式（大量水用 `aq` 表示）。
  > 💡 **讲师批注**：原题虽然写了“希硫酸”，但教材最终按浓硫酸（纯液体 $\text{H}_2\text{SO}_4(\text{液})$）的溶解热 $96\text{ kJ/mol}$ 来书写。考试遇到此类题直接按题干给定的浓度、体积算出物质的量，再归化到 $1\text{ mol}$ 即可。

##### 【最终答案】
- **(1) $2\text{C}(\text{黒鉛}) + 3\text{H}_2(\text{気}) + \dfrac{1}{2}\text{O}_2(\text{気}) = \text{C}_2\text{H}_5\text{OH}(\text{液}) + 277\text{ kJ}$**
- **(2) $\text{C}_3\text{H}_8(\text{気}) + 5\text{O}_2(\text{気}) = 3\text{CO}_2(\text{気}) + 4\text{H}_2\text{O}(\text{液}) + 2.2 \times 10^3\text{ kJ}$**
- **(3) $\text{H}_2\text{SO}_4(\text{液}) + \text{aq} = \text{H}_2\text{SO}_4\text{ aq} + 96\text{ kJ}$**

---

### 3.2 盖斯定律（ヘスの法則）与反应热计算（原书 P.47–P.49 / PDF P.48–P.50）

#### 【核心图解：盖斯定律能量图（$\text{C} \to \text{CO} \to \text{CO}_2$ 路径无关性）】
<svg viewBox="0 0 420 260" xmlns="http://www.w3.org/2000/svg" style="background:#ffffff;border:1px solid #e2e8f0;border-radius:8px;max-width:100%;">
  <defs>
    <marker id="hess-dn-blue" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M 0 0 L 5 10 L 10 0 z" fill="#2563eb"/>
    </marker>
    <marker id="hess-dn-green" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M 0 0 L 5 10 L 10 0 z" fill="#059669"/>
    </marker>
    <marker id="hess-dn-red" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M 0 0 L 5 10 L 10 0 z" fill="#dc2626"/>
    </marker>
    <marker id="hess-axis" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M 0 10 L 5 0 L 10 10 z" fill="#334155"/>
    </marker>
  </defs>
  <text x="210" y="22" text-anchor="middle" font-size="13" font-weight="bold" fill="#0f172a">ヘスの法則（盖斯定律）能量图：求 CO 生成热 Q</text>
  <!-- 纵轴 -->
  <line x1="42" y1="230" x2="42" y2="42" stroke="#334155" stroke-width="1.8" marker-end="url(#hess-axis)"/>
  <text x="42" y="36" text-anchor="middle" font-size="10.5" font-weight="bold" fill="#334155">高</text>
  <text x="42" y="244" text-anchor="middle" font-size="10.5" font-weight="bold" fill="#334155">低</text>
  <text x="22" y="138" text-anchor="middle" font-size="11" fill="#475569" writing-mode="tb">エネルギー</text>

  <!-- 三条能级线 -->
  <line x1="70" y1="58" x2="365" y2="58" stroke="#0f172a" stroke-width="2.2"/>
  <text x="215" y="50" text-anchor="middle" font-size="12" font-weight="bold" fill="#0f172a">C(黒鉛) + O₂(気)</text>

  <line x1="70" y1="112" x2="245" y2="112" stroke="#0f172a" stroke-width="2"/>
  <text x="175" y="104" text-anchor="middle" font-size="12" font-weight="bold" fill="#0f172a">CO(気) + ½ O₂(気)</text>

  <line x1="70" y1="220" x2="365" y2="220" stroke="#0f172a" stroke-width="2.2"/>
  <text x="215" y="212" text-anchor="middle" font-size="12" font-weight="bold" fill="#0f172a">CO₂(気)</text>

  <!-- 左侧路径：两步 -->
  <line x1="95" y1="60" x2="95" y2="107" stroke="#dc2626" stroke-width="3.2" marker-end="url(#hess-dn-red)"/>
  <text x="104" y="88" font-size="11.5" font-weight="bold" fill="#dc2626">Q kJ（所求）</text>

  <line x1="95" y1="114" x2="95" y2="215" stroke="#2563eb" stroke-width="3.2" marker-end="url(#hess-dn-blue)"/>
  <text x="104" y="168" font-size="11.5" font-weight="bold" fill="#1d4ed8">283 kJ（CO 燃焼熱）</text>

  <!-- 右侧路径：一步 -->
  <line x1="305" y1="60" x2="305" y2="215" stroke="#059669" stroke-width="3.5" marker-end="url(#hess-dn-green)"/>
  <text x="314" y="135" font-size="11.5" font-weight="bold" fill="#047857">394 kJ</text>
  <text x="314" y="150" font-size="10" fill="#059669">(C 燃焼熱)</text>

  <!-- 底部公式框 -->
  <rect x="75" y="230" width="285" height="24" rx="5" fill="#fef2f2" stroke="#fca5a5"/>
  <text x="217" y="246" text-anchor="middle" font-size="11.5" font-weight="bold" fill="#991b1b">Q + 283 = 394  ⇒  Q = 394 − 283 = 111 kJ</text>
</svg>

---

#### 练习组 2：盖斯定律与生成热便利公式计算（原书 P.48–P.49 / PDF P.49–P.50）

##### 【原题重现与翻译】
> (1) メタン $\text{CH}_4$，炭素，水素の燃焼熱は $891\text{ kJ/mol}$，$394\text{ kJ/mol}$，$286\text{ kJ/mol}$ である。メタンの生成熱を整数値で答えよ。
> （甲烷 $\text{CH}_4$、碳、氢气的燃烧热分别为 $891\text{ kJ/mol}$、$394\text{ kJ/mol}$、$286\text{ kJ/mol}$。用整数求出甲烷的生成热。）
> (2) 一酸化炭素，水素の燃焼熱は $283\text{ kJ/mol}$，$286\text{ kJ/mol}$，一酸化炭素，エタン $\text{C}_2\text{H}_6$ の生成熱は $111\text{ kJ/mol}$，$85\text{ kJ/mol}$ である。エタンの燃焼熱を整数値で答えよ。
> （一氧化碳、氢气的燃烧热分别为 $283\text{ kJ/mol}$、$286\text{ kJ/mol}$，一氧化碳、乙烷 $\text{C}_2\text{H}_6$ 的生成热分别为 $111\text{ kJ/mol}$、$85\text{ kJ/mol}$。用整数求出乙烷的燃烧热。）
> (3) 次の熱化学方程式からエチレン $\text{C}_2\text{H}_4$ の燃焼熱を求め，整数値で答えよ。
> （由下列热化学方程式求乙烯 $\text{C}_2\text{H}_4$ 的燃烧热，用整数回答。）
> $$\begin{aligned}
> 2\text{C}(\text{黒鉛}) + 2\text{H}_2(\text{気}) &= \text{C}_2\text{H}_4(\text{気}) - 52\text{ kJ} \quad \cdots\text{①} \\
> \text{C}(\text{黒鉛}) + \text{O}_2(\text{気}) &= \text{CO}_2(\text{気}) + 394\text{ kJ} \quad \cdots\text{②} \\
> \text{H}_2(\text{気}) + \frac{1}{2}\text{O}_2(\text{気}) &= \text{H}_2\text{O}(\text{液}) + 286\text{ kJ} \quad \cdots\text{③}
> \end{aligned}$$

##### 【考点定位】
热化学方程式的联立消元法、以及“全部生成热已知时：$Q = \sum(\text{右辺生成熱}) - \sum(\text{左辺生成熱})$”的秒杀公式。

##### 【分步标准解答】
- **(1) 求甲烷 $\text{CH}_4$ 的生成热 $Q$**
  - 写出已知 3 个燃烧热的热化学方程式：
    - ① $\text{CH}_4(\text{気}) + 2\text{O}_2(\text{気}) = \text{CO}_2(\text{気}) + 2\text{H}_2\text{O}(\text{液}) + 891\text{ kJ}$
    - ② $\text{C}(\text{黒鉛}) + \text{O}_2(\text{気}) = \text{CO}_2(\text{気}) + 394\text{ kJ}$
    - ③ $\text{H}_2(\text{気}) + \frac{1}{2}\text{O}_2(\text{気}) = \text{H}_2\text{O}(\text{液}) + 286\text{ kJ}$
  - 目标式（甲烷生成热）：④ $\text{C}(\text{黒鉛}) + 2\text{H}_2(\text{気}) = \text{CH}_4(\text{気}) + Q\text{ kJ}$
  - 联立消元：由 $\text{②} + 2 \times \text{③} - \text{①}$ 直接消去 $\text{O}_2, \text{CO}_2, \text{H}_2\text{O}$：
    $$Q = 394 + 286 \times 2 - 891 = 394 + 572 - 891 = 75\text{ kJ/mol}$$
  > 💡 **讲师批注**：也可以直接套用“燃烧热便利公式”（与生成热相反，是**左减右**）：$Q = \sum(\text{左辺燃焼熱}) - \sum(\text{右辺燃焼熱}) = (394 + 2 \times 286) - 891 = 75\text{ kJ/mol}$！

- **(2) 求乙烷 $\text{C}_2\text{H}_6$ 的燃烧热 $Q$**
  - 写出已知 4 个热化学方程式：
    - ① $\text{CO}(\text{気}) + \frac{1}{2}\text{O}_2(\text{気}) = \text{CO}_2(\text{気}) + 283\text{ kJ}$
    - ② $\text{H}_2(\text{気}) + \frac{1}{2}\text{O}_2(\text{気}) = \text{H}_2\text{O}(\text{液}) + 286\text{ kJ}$
    - ③ $\text{C}(\text{黒鉛}) + \frac{1}{2}\text{O}_2(\text{気}) = \text{CO}(\text{気}) + 111\text{ kJ}$
    - ④ $2\text{C}(\text{黒鉛}) + 3\text{H}_2(\text{気}) = \text{C}_2\text{H}_6(\text{気}) + 85\text{ kJ}$
  - 目标式（乙烷燃烧热）：⑤ $\text{C}_2\text{H}_6(\text{気}) + \frac{7}{2}\text{O}_2(\text{気}) = 2\text{CO}_2(\text{気}) + 3\text{H}_2\text{O}(\text{液}) + Q\text{ kJ}$
  - 联立消元：观察各物质系数，执行 $2 \times \text{①} + 3 \times \text{②} + 2 \times \text{③} - \text{④}$：
    $$Q = 283 \times 2 + 286 \times 3 + 111 \times 2 - 85 = 566 + 858 + 222 - 85 = 1561\text{ kJ/mol}$$
  > 💡 **讲师批注**：或者先用 ① + ③ 算出 $\text{CO}_2$ 的生成热 $= 283 + 111 = 394\text{ kJ/mol}$，再用生成热便利公式“右减左”：$Q = (394 \times 2 + 286 \times 3) - 85 = 1646 - 85 = 1561\text{ kJ/mol}$，更快更不容易出错！

- **(3) 求乙烯 $\text{C}_2\text{H}_4$ 的燃烧热 $Q$**
  - 观察题干：①、②、③ 恰好分别给出了 $\text{C}_2\text{H}_4(\text{気})$（$-52$）、$\text{CO}_2(\text{気})$（$394$）、$\text{H}_2\text{O}(\text{液})$（$286$）的**生成热**！（单质 $\text{O}_2$ 生成热为 $0$）
  - 目标式：$\text{C}_2\text{H}_4(\text{気}) + 3\text{O}_2(\text{気}) = 2\text{CO}_2(\text{気}) + 2\text{H}_2\text{O}(\text{液}) + Q\text{ kJ}$
  - 直接套用**生成热便利公式（右减左）**：
    $$Q = (394 \times 2 + 286 \times 2) - (-52 + 0) = (788 + 572) + 52 = 1360 + 52 = 1412\text{ kJ/mol}$$
  > 💡 **讲师批注**：乙烯生成热是**负数**（$-52\text{ kJ/mol}$），代入公式时务必带括号写作 `- (-52)`，负负得正！

##### 【最终答案】
- **(1) $75\text{ kJ/mol}$**
- **(2) $1561\text{ kJ/mol}$**
- **(3) $1412\text{ kJ/mol}$**

---

### 3.3 键能（結合エネルギー）与解离能（解離エネルギー）（原书 P.49–P.50 / PDF P.50–P.51）

#### 【核心图解：甲烷与丙烷的共价键数及解离能路径（SVG）】
<svg viewBox="0 0 420 260" xmlns="http://www.w3.org/2000/svg" style="background:#ffffff;border:1px solid #e2e8f0;border-radius:8px;max-width:100%;">
  <text x="210" y="22" text-anchor="middle" font-size="13" font-weight="bold" fill="#0f172a">結合エネルギー（键能）与解離エネルギー（原子化能）解析</text>

  <!-- 左侧框：CH4 -->
  <rect x="14" y="36" width="166" height="145" rx="8" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>
  <text x="97" y="54" text-anchor="middle" font-size="11.5" font-weight="bold" fill="#1e40af">① メタン CH₄</text>
  <!-- CH4 结构式 -->
  <circle cx="97" cy="106" r="13" fill="#dbeafe" stroke="#2563eb" stroke-width="1.5"/>
  <text x="97" y="110" text-anchor="middle" font-size="12" font-weight="bold" fill="#1e3a8a">C</text>
  <!-- 4 条 C-H 键 -->
  <line x1="97" y1="93" x2="97" y2="75" stroke="#dc2626" stroke-width="2.2"/>
  <line x1="97" y1="119" x2="97" y2="137" stroke="#dc2626" stroke-width="2.2"/>
  <line x1="84" y1="106" x2="66" y2="106" stroke="#dc2626" stroke-width="2.2"/>
  <line x1="110" y1="106" x2="128" y2="106" stroke="#dc2626" stroke-width="2.2"/>
  <text x="97" y="71" text-anchor="middle" font-size="11" font-weight="bold" fill="#334155">H</text>
  <text x="97" y="150" text-anchor="middle" font-size="11" font-weight="bold" fill="#334155">H</text>
  <text x="56" y="110" text-anchor="middle" font-size="11" font-weight="bold" fill="#334155">H</text>
  <text x="138" y="110" text-anchor="middle" font-size="11" font-weight="bold" fill="#334155">H</text>
  <text x="97" y="170" text-anchor="middle" font-size="10.5" font-weight="bold" fill="#b91c1c">含 4 条 C–H 键</text>

  <!-- 右侧框：C3H8 -->
  <rect x="192" y="36" width="214" height="145" rx="8" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>
  <text x="299" y="54" text-anchor="middle" font-size="11.5" font-weight="bold" fill="#065f46">② プロパン C₃H₈</text>
  <!-- 3 个 C -->
  <line x1="252" y1="106" x2="299" y2="106" stroke="#059669" stroke-width="3.2"/>
  <line x1="299" y1="106" x2="346" y2="106" stroke="#059669" stroke-width="3.2"/>
  <!-- 8 条 C-H 键 -->
  <line x1="252" y1="94" x2="252" y2="78" stroke="#dc2626" stroke-width="2"/>
  <line x1="252" y1="118" x2="252" y2="134" stroke="#dc2626" stroke-width="2"/>
  <line x1="240" y1="106" x2="224" y2="106" stroke="#dc2626" stroke-width="2"/>
  <line x1="299" y1="94" x2="299" y2="78" stroke="#dc2626" stroke-width="2"/>
  <line x1="299" y1="118" x2="299" y2="134" stroke="#dc2626" stroke-width="2"/>
  <line x1="346" y1="94" x2="346" y2="78" stroke="#dc2626" stroke-width="2"/>
  <line x1="346" y1="118" x2="346" y2="134" stroke="#dc2626" stroke-width="2"/>
  <line x1="358" y1="106" x2="374" y2="106" stroke="#dc2626" stroke-width="2"/>
  <!-- C 原子圆 -->
  <circle cx="252" cy="106" r="11" fill="#d1fae5" stroke="#059669" stroke-width="1.5"/>
  <text x="252" y="110" text-anchor="middle" font-size="11" font-weight="bold" fill="#064e3b">C</text>
  <circle cx="299" cy="106" r="11" fill="#d1fae5" stroke="#059669" stroke-width="1.5"/>
  <text x="299" y="110" text-anchor="middle" font-size="11" font-weight="bold" fill="#064e3b">C</text>
  <circle cx="346" cy="106" r="11" fill="#d1fae5" stroke="#059669" stroke-width="1.5"/>
  <text x="346" y="110" text-anchor="middle" font-size="11" font-weight="bold" fill="#064e3b">C</text>
  <!-- H 标注 -->
  <text x="252" y="73" text-anchor="middle" font-size="10" font-weight="bold" fill="#334155">H</text>
  <text x="252" y="146" text-anchor="middle" font-size="10" font-weight="bold" fill="#334155">H</text>
  <text x="214" y="110" text-anchor="middle" font-size="10" font-weight="bold" fill="#334155">H</text>
  <text x="299" y="73" text-anchor="middle" font-size="10" font-weight="bold" fill="#334155">H</text>
  <text x="299" y="146" text-anchor="middle" font-size="10" font-weight="bold" fill="#334155">H</text>
  <text x="346" y="73" text-anchor="middle" font-size="10" font-weight="bold" fill="#334155">H</text>
  <text x="346" y="146" text-anchor="middle" font-size="10" font-weight="bold" fill="#334155">H</text>
  <text x="384" y="110" text-anchor="middle" font-size="10" font-weight="bold" fill="#334155">H</text>
  <text x="299" y="170" text-anchor="middle" font-size="10.5" font-weight="bold" fill="#047857">含 2 条 C–C 键 + 8 条 C–H 键</text>

  <!-- 底部便利公式总结 -->
  <rect x="14" y="192" width="392" height="56" rx="6" fill="#fffbeb" stroke="#fcd34d" stroke-width="1.5"/>
  <text x="210" y="211" text-anchor="middle" font-size="11.5" font-weight="bold" fill="#92400e">键能计算核心铁律（务必记牢！）</text>
  <text x="210" y="227" text-anchor="middle" font-size="10.5" fill="#78350f">① 解离能 = 分子拆成气态单原子所需总吸热量（全为单原子，且必须为気体）</text>
  <text x="210" y="242" text-anchor="middle" font-size="10.5" fill="#78350f">② 便利公式：反応熱 Q = (右辺の結合エネルギー総和) − (左辺の結合エネルギー総和)</text>
</svg>

---

#### 练习组 3：键能与解离能计算（原书 P.50 / PDF P.51）

##### 【原题重现与翻译】
> (1) $\text{H}-\text{H}$，$\text{N}\equiv\text{N}$，$\text{N}-\text{H}$ の結合エネルギーは $436\text{ kJ/mol}$，$946\text{ kJ/mol}$，$391\text{ kJ/mol}$ である。アンモニア $\text{NH}_3$ の生成熱を求めよ。
> （$\text{H}-\text{H}$、$\text{N}\equiv\text{N}$、$\text{N}-\text{H}$ 的键能分别为 $436\text{ kJ/mol}$、$946\text{ kJ/mol}$、$391\text{ kJ/mol}$。求氨气 $\text{NH}_3$ 的生成热。）
> (2) 以下の熱化学方程式を用いて，メタン $\text{CH}_4$ 中の 1 つの $\text{C}-\text{H}$ の結合エネルギーとプロパン $\text{C}_3\text{H}_8$ 中の 1 つの $\text{C}-\text{C}$ の結合エネルギーを求めよ。［北海道大］
> （利用下列热化学方程式，求甲烷 $\text{CH}_4$ 中 1 条 $\text{C}-\text{H}$ 键的键能与丙烷 $\text{C}_3\text{H}_8$ 中 1 条 $\text{C}-\text{C}$ 键的键能。［北海道大学］）
> $$\begin{aligned}
> \text{C}(\text{黒鉛}) &= \text{C}(\text{気}) - 715\text{ kJ} \quad \cdots\text{①} \\
> \text{C}(\text{黒鉛}) + 2\text{H}_2(\text{気}) &= \text{CH}_4(\text{気}) + 75\text{ kJ} \quad \cdots\text{②} \\
> 3\text{C}(\text{黒鉛}) + 4\text{H}_2(\text{気}) &= \text{C}_3\text{H}_8(\text{気}) + 105\text{ kJ} \quad \cdots\text{③} \\
> \text{H}_2(\text{気}) &= 2\text{H}(\text{気}) - 437\text{ kJ} \quad \cdots\text{④}
> \end{aligned}$$

##### 【考点定位】
键能便利公式的直接应用、利用盖斯定律求多原子分子的解离能（原子化能）并拆分出单键键能。

##### 【分步标准解答】
- **(1) 求 $\text{NH}_3$ 的生成热 $Q$**
  - 写出 $\text{NH}_3$ 生成热的目标式：
    $$\frac{1}{2}\text{N}_2(\text{気}) + \frac{3}{2}\text{H}_2(\text{気}) = \text{NH}_3(\text{気}) + Q\text{ kJ}$$
  - **方法一（便利公式秒杀——右减左）**：
    - 右边：$1\text{ mol}$ $\text{NH}_3$ 含 $3\text{ mol}$ $\text{N}-\text{H}$ 键 $\Rightarrow 391 \times 3 = 1173\text{ kJ}$
    - 左边：$\frac{1}{2}\text{ mol}$ $\text{N}\equiv\text{N}$ 键 + $\frac{3}{2}\text{ mol}$ $\text{H}-\text{H}$ 键 $\Rightarrow 946 \times \frac{1}{2} + 436 \times \frac{3}{2} = 473 + 654 = 1127\text{ kJ}$
    - 故 $Q = 1173 - 1127 = 46\text{ kJ/mol}$。
  - **方法二（联立热化学方程式）**：
    - ① $\text{H}_2(\text{気}) = 2\text{H}(\text{気}) - 436\text{ kJ}$
    - ② $\text{N}_2(\text{気}) = 2\text{N}(\text{気}) - 946\text{ kJ}$
    - ③ $\text{NH}_3(\text{気}) = \text{N}(\text{気}) + 3\text{H}(\text{気}) - (391 \times 3)\text{ kJ}$
    - 由 $\frac{1}{2}\times\text{②} + \frac{3}{2}\times\text{①} - \text{③}$ 得 $Q = (-946)\times\frac{1}{2} + (-436)\times\frac{3}{2} - \{-(391\times 3)\} = 46\text{ kJ/mol}$。

- **(2) 求 $\text{C}-\text{H}$ 键能与 $\text{C}-\text{C}$ 键能（北海道大真题）**
  - **第 1 步：求 $\text{CH}_4$ 的解离能 $Q_1$ 及 $\text{C}-\text{H}$ 键能**
    - 设 $\text{CH}_4(\text{気}) = \text{C}(\text{気}) + 4\text{H}(\text{気}) - Q_1\text{ kJ}$（注意断键吸热，前面是负号 `- Q₁`）。
    - 用已知式组合：$\text{①} + 2\times\text{④} - \text{②}$ 即可得到上式：
      $$-Q_1 = (-715) + (-437 \times 2) - 75 = -715 - 874 - 75 = -1664$$
      $$\therefore Q_1 = 1664\text{ kJ/mol}$$
    - 甲烷含 4 条等价 $\text{C}-\text{H}$ 键，故 1 条 $\text{C}-\text{H}$ 键的键能为：
      $$E(\text{C}-\text{H}) = \frac{1664}{4} = 416\text{ kJ/mol}$$
  - **第 2 步：求 $\text{C}_3\text{H}_8$ 的解离能 $Q_2$ 及 $\text{C}-\text{C}$ 键能**
    - 设 $\text{C}_3\text{H}_8(\text{気}) = 3\text{C}(\text{気}) + 8\text{H}(\text{気}) - Q_2\text{ kJ}$。
    - 用已知式组合：$3\times\text{①} + 4\times\text{④} - \text{③}$：
      $$-Q_2 = (-715 \times 3) + (-437 \times 4) - 105 = -2145 - 1748 - 105 = -3998$$
      $$\therefore Q_2 = 3998\text{ kJ/mol}$$
    - 如上方 SVG 所示，丙烷 $\text{C}_3\text{H}_8$ 共有 **2 条 $\text{C}-\text{C}$ 键** 和 **8 条 $\text{C}-\text{H}$ 键**：
      $$2 \cdot E(\text{C}-\text{C}) + 8 \cdot E(\text{C}-\text{H}) = 3998$$
      $$E(\text{C}-\text{C}) = \frac{3998 - 416 \times 8}{2} = \frac{3998 - 3328}{2} = \frac{670}{2} = 335\text{ kJ/mol}$$
  > 💡 **讲师批注**：① 凡是出现固体碳 $\text{C}(\text{黒鉛})$ 时，**不能**直接套用键能公式，因为必须把 $\text{C}(\text{黒鉛})$ 变成气态碳原子 $\text{C}(\text{気})$（升华热 $715\text{ kJ/mol}$）；② 记住规律：直链烷烃 $\text{C}_n\text{H}_{2n+2}$ 中有 **$(n-1)$ 条 $\text{C}-\text{C}$ 键** 和 **$(2n+2)$ 条 $\text{C}-\text{H}$ 键**，千万别把丙烷数成 3 条 $\text{C}-\text{C}$ 键！

##### 【最终答案】
- **(1) $46\text{ kJ/mol}$**
- **(2) $\text{C}-\text{H}$ 键能：$416\text{ kJ/mol}$；$\text{C}-\text{C}$ 键能：$335\text{ kJ/mol}$**

---

### 3.4 温度与热量（比热计算）（原书 P.51 / PDF P.52）

#### 练习组 4：量热实验与燃烧加热计算（原书 P.51 / PDF P.52）

##### 【原题重现与翻译】
> (1) 水 $100\text{ mL}$ が入った断熱容器に固体の水酸化ナトリウム $2.0\text{ g}$ を入れて溶かしたところ，液温が $5.2\text{ K}$ 上昇した。水溶液の体積を $100\text{ mL}$，密度を $1.02\text{ g/cm}^3$，比熱を $4.2\text{ J/(g}\cdot\text{K)}$ とするとき，固体の水酸化ナトリウムの溶解熱を求めよ。$\text{NaOH} = 40$
> （向盛有 $100\text{ mL}$ 水的绝热容器中加入 $2.0\text{ g}$ 固体氢氧化钠溶解，液温上升了 $5.2\text{ K}$。若水溶液体积为 $100\text{ mL}$、密度为 $1.02\text{ g/cm}^3$、比热为 $4.2\text{ J/(g}\cdot\text{K)}$，求固体氢氧化钠的溶解热。$\text{NaOH} = 40$）
> (2) プロパン $\text{C}_3\text{H}_8$ の燃焼によって，温度 $20^\circ\text{C}$ の水 $10\text{ L}$ を加熱することを試みた。プロパンを $0.010\text{ mol/s}$ の燃焼速度で反応させたとき，水の温度が $50^\circ\text{C}$ になるのに必要な時間［秒］を有効数字 2 桁で答えよ。プロパンの燃焼熱は $2220\text{ kJ/mol}$，水の密度は $1.0\text{ g/mL}$，水の比熱は $4.2\text{ J/(g}\cdot^\circ\text{C)}$ であるとする。［北海道大］
> （尝试通过燃烧丙烷 $\text{C}_3\text{H}_8$ 来加热 $10\text{ L}$ 温度为 $20^\circ\text{C}$ 的水。当丙烷以 $0.010\text{ mol/s}$ 的速率燃烧时，求水温升至 $50^\circ\text{C}$ 所需的时间［秒］，保留 2 位有效数字。已知丙烷燃烧热为 $2220\text{ kJ/mol}$，水密度为 $1.0\text{ g/mL}$，水比热为 $4.2\text{ J/(g}\cdot^\circ\text{C)}$。［北海道大学］）

##### 【考点定位】
量热公式 $Q = mc\Delta T$、单位换算（$\text{J} \leftrightarrow \text{kJ}$、$\text{L} \leftrightarrow \text{mL}$、$\text{cm}^3 = \text{mL}$）以及有效数字处理。

##### 【分步标准解答】
- **(1) 求 $\text{NaOH}(\text{固})$ 的溶解热**
  - 第 1 步：计算溶液吸收的热量（即 $2.0\text{ g}$ $\text{NaOH}$ 溶解发出的热量 $Q$）：
    - 溶液质量 $m = 1.02\text{ g/cm}^3 \times 100\text{ mL} = 102\text{ g}$
    - $Q = m c \Delta T = 102\text{ g} \times 4.2\text{ J/(g}\cdot\text{K)} \times 5.2\text{ K} = 2227.68\text{ J} \fallingdotseq 2.23\text{ kJ}$
  - 第 2 步：计算 $\text{NaOH}$ 的物质的量：
    $$n(\text{NaOH}) = \frac{2.0\text{ g}}{40\text{ g/mol}} = 0.050\text{ mol}$$
  - 第 3 步：换算成 $1\text{ mol}$ 的溶解热（题中 $2.0$、$5.2$、$4.2$ 均为 2 位有效数字）：
    $$Q_{\text{溶}} = \frac{2.23\text{ kJ}}{0.050\text{ mol}} = 44.6\text{ kJ/mol} \fallingdotseq 45\text{ kJ/mol}$$
  > 💡 **讲师批注**：特别注意两点：① 计算 $Q$ 时用的是**整个水溶液的总质量**（$102\text{ g}$），不是纯水的 $100\text{ g}$！② $Q = mc\Delta T$ 算出来的单位是 **$\text{J}$（焦耳）**，一定要除以 $1000$ 换算成 **$\text{kJ}$（千焦）** 再除以 $\text{mol}$！

- **(2) 求加热水所需时间（北海道大真题）**
  - 第 1 步：计算 $10\text{ L}$ 水从 $20^\circ\text{C}$ 升至 $50^\circ\text{C}$ 所需热量 $Q$：
    - 水的质量 $m = 1.0\text{ g/mL} \times (10 \times 10^3\text{ mL}) = 1.0 \times 10^4\text{ g}$
    - 温升 $\Delta T = 50 - 20 = 30^\circ\text{C}$
    - $Q = 1.0 \times 10^4\text{ g} \times 4.2\text{ J/(g}\cdot^\circ\text{C)} \times 30^\circ\text{C} = 1.26 \times 10^6\text{ J} = 1.26 \times 10^3\text{ kJ}$
  - 第 2 步：计算所需丙烷的物质的量 $n$：
    $$n = \frac{1.26 \times 10^3\text{ kJ}}{2220\text{ kJ/mol}} \fallingdotseq 0.568\text{ mol}$$
  - 第 3 步：根据燃烧速率 $0.010\text{ mol/s}$ 求时间 $t$：
    $$t = \frac{0.568\text{ mol}}{0.010\text{ mol/s}} = 56.8\text{ 秒} \fallingdotseq 57\text{ 秒}$$

##### 【最终答案】
- **(1) $45\text{ kJ/mol}$**
- **(2) $57\text{ 秒}$**

---

### 3.5 化学反应的机理与反应速率（原书 P.52–P.54 / PDF P.53–P.55）

#### 【核心图解：活化能与催化剂的能量曲线图（SVG）】
<svg viewBox="0 0 420 260" xmlns="http://www.w3.org/2000/svg" style="background:#ffffff;border:1px solid #e2e8f0;border-radius:8px;max-width:100%;">
  <defs>
    <marker id="act-arr" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse">
      <path d="M 0 10 L 5 0 L 10 10 z" fill="#334155"/>
    </marker>
    <marker id="act-red" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse">
      <path d="M 0 10 L 5 0 L 10 10 z" fill="#dc2626"/>
    </marker>
    <marker id="act-blue" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse">
      <path d="M 0 10 L 5 0 L 10 10 z" fill="#2563eb"/>
    </marker>
    <marker id="act-green" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse">
      <path d="M 0 10 L 5 0 L 10 10 z" fill="#059669"/>
    </marker>
  </defs>
  <text x="210" y="20" text-anchor="middle" font-size="13" font-weight="bold" fill="#0f172a">活性化エネルギー（活化能）与触媒（催化剂）的作用</text>

  <!-- 纵轴 -->
  <line x1="38" y1="225" x2="38" y2="35" stroke="#334155" stroke-width="1.6" marker-end="url(#act-arr)"/>
  <text x="20" y="130" text-anchor="middle" font-size="11" fill="#475569" writing-mode="tb">エネルギー</text>

  <!-- 水平辅助线 -->
  <!-- 无催化峰顶 y=48 -->
  <line x1="50" y1="48" x2="388" y2="48" stroke="#94a3b8" stroke-width="1" stroke-dasharray="4,3"/>
  <!-- 有催化峰顶 y=98 -->
  <line x1="78" y1="98" x2="355" y2="98" stroke="#93c5fd" stroke-width="1" stroke-dasharray="4,3"/>
  <!-- 反应物水平线 y=150 -->
  <line x1="50" y1="150" x2="235" y2="150" stroke="#64748b" stroke-width="1.3"/>
  <!-- 生成物水平线 y=202 -->
  <line x1="175" y1="202" x2="388" y2="202" stroke="#64748b" stroke-width="1.3"/>

  <!-- 曲线1：無触媒（红色） -->
  <path d="M 60 150 C 130 150, 165 48, 205 48 C 245 48, 265 202, 330 202" fill="none" stroke="#dc2626" stroke-width="2.6"/>
  <!-- 曲线2：触媒あり（蓝色） -->
  <path d="M 60 150 C 135 150, 170 98, 205 98 C 240 98, 265 202, 330 202" fill="none" stroke="#2563eb" stroke-width="2.6"/>

  <!-- 标注节点 -->
  <text x="205" y="42" text-anchor="middle" font-size="10.5" font-weight="bold" fill="#b91c1c">活性化状態（触媒なし）</text>
  <text x="205" y="92" text-anchor="middle" font-size="10.5" font-weight="bold" fill="#1d4ed8">活性化状態（触媒あり）</text>
  <text x="115" y="144" text-anchor="middle" font-size="11" font-weight="bold" fill="#0f172a">反応物</text>
  <text x="310" y="196" text-anchor="middle" font-size="11" font-weight="bold" fill="#0f172a">生成物</text>

  <!-- E1 正反应无催化 -->
  <line x1="62" y1="52" x2="62" y2="146" stroke="#dc2626" stroke-width="1.6" marker-start="url(#act-red)" marker-end="url(#act-red)"/>
  <text x="54" y="102" text-anchor="end" font-size="11" font-weight="bold" fill="#dc2626">E₁</text>
  <!-- E3 正反应有催化 -->
  <line x1="88" y1="102" x2="88" y2="146" stroke="#2563eb" stroke-width="1.6" marker-start="url(#act-blue)" marker-end="url(#act-blue)"/>
  <text x="95" y="128" text-anchor="start" font-size="11" font-weight="bold" fill="#2563eb">E₃</text>

  <!-- E2 逆反应无催化 -->
  <line x1="378" y1="52" x2="378" y2="198" stroke="#dc2626" stroke-width="1.6" marker-start="url(#act-red)" marker-end="url(#act-red)"/>
  <text x="385" y="128" text-anchor="start" font-size="11" font-weight="bold" fill="#dc2626">E₂</text>
  <!-- E4 逆反应有催化 -->
  <line x1="350" y1="102" x2="350" y2="198" stroke="#2563eb" stroke-width="1.6" marker-start="url(#act-blue)" marker-end="url(#act-blue)"/>
  <text x="343" y="152" text-anchor="end" font-size="11" font-weight="bold" fill="#2563eb">E₄</text>

  <!-- 反应热 Q（绿色） -->
  <line x1="210" y1="154" x2="210" y2="198" stroke="#059669" stroke-width="2" marker-start="url(#act-green)" marker-end="url(#act-green)"/>
  <text x="203" y="180" text-anchor="end" font-size="11" font-weight="bold" fill="#047857">反応熱 Q</text>

  <!-- 底部恒等式 -->
  <rect x="45" y="226" width="350" height="26" rx="5" fill="#ecfdf5" stroke="#6ee7b7"/>
  <text x="220" y="243" text-anchor="middle" font-size="11" font-weight="bold" fill="#065f46">重要恒等式：Q = E₂ − E₁ = E₄ − E₃（触媒不影响 Q！）</text>
</svg>

> 💡 **讲师批注**：在放热反应中（如上图），**正反应活化能 + 反应热 = 逆反应活化能**，即 $Q = E_2 - E_1 = E_4 - E_3$。另外一定要牢记：**反应速率式 $v = k[\text{A}]^x[\text{B}]^y$ 的指数 $x, y$ 必须通过实验测定，不能直接由化学方程式系数判断**！

---

#### 练习组 5：反应速率方程与速率常数测定（原书 P.54 / PDF P.55）

##### 【原题重现与翻译】
> 物質 A と物質 B から物質 C が生成する化学反応において，ある温度で A と B の初期濃度を変えて，反応初期の C の生成速度を求める実験 1, 2, 3 を行った。
> （在物质 A 与物质 B 生成物质 C 的化学反应中，某温度下改变 A 和 B 的初始浓度，测定了反应初期 C 的生成速率，实验 1, 2, 3 数据如下表。）
>
> | | A の初期濃度 $[\text{mol/L}]$ | B の初期濃度 $[\text{mol/L}]$ | C の生成速度 $[\text{mol/(L}\cdot\text{s)}]$ |
> | :---: | :---: | :---: | :---: |
> | **実験 1** | $0.30$ | $1.00$ | $1.8 \times 10^{-2}$ |
> | **実験 2** | $0.30$ | $0.50$ | $9.0 \times 10^{-3}$ |
> | **実験 3** | $0.60$ | $0.50$ | $3.6 \times 10^{-2}$ |
>
> C の生成速度 $v$ は，A のモル濃度を $[\text{A}]$，B のモル濃度を $[\text{B}]$，反応速度定数を $k$ とすると，$v = k[\text{A}]^x[\text{B}]^y$ と表すことができる。
> （1）実験 1, 2, 3 の結果をもとに，$x$ と $y$ にあてはまる適切な値を求めよ。（求 $x$ 和 $y$ 的值。）
> （2）反応速度定数 $k$ を有効数字 2 桁で求め，単位とともに記せ。（求反应速率常数 $k$，保留 2 位有效数字并写明单位。）
> （3）A の初期濃度を $0.20\text{ mol/L}$，B の初期濃度を $0.50\text{ mol/L}$ としたとき，反応初期の C の生成速度を有効数字 2 桁で答えよ。［大阪市立大］
> （当 A 初始浓度为 $0.20\text{ mol/L}$、B 为 $0.50\text{ mol/L}$ 时，求反应初期 C 的生成速率，保留 2 位有效数字。［大阪市立大学］）

##### 【考点定位】
控制变量法确定反应级数（$x, y$）、反应速率常数 $k$ 的数值及**单位推导**（EJU 必考！）。

##### 【分步标准解答】
- **(1) 控制变量法求 $x$ 与 $y$**
  - **比较实验 2 与实验 1**（$[\text{A}]$ 保持 $0.30$ 不变）：
    - $[\text{B}]$ 从 $0.50 \to 1.00$，变为原来的 **$2$ 倍**；
    - 速率 $v$ 从 $9.0 \times 10^{-3} \to 1.8 \times 10^{-2}$，变为原来的 **$2$ 倍**。
    - 由 $2^y = 2$ 得 **$y = 1$**。
  - **比较实验 2 与实验 3**（$[\text{B}]$ 保持 $0.50$ 不变）：
    - $[\text{A}]$ 从 $0.30 \to 0.60$，变为原来的 **$2$ 倍**；
    - 速率 $v$ 从 $9.0 \times 10^{-3} \to 3.6 \times 10^{-2}$，变为原来的 **$4$ 倍**。
    - 由 $2^x = 4$ 得 **$x = 2$**。

- **(2) 求反应速率常数 $k$ 及其单位**
  - 速率方程为 $v = k[\text{A}]^2[\text{B}]$，代入实验 1 数据：
    $$k = \frac{v}{[\text{A}]^2[\text{B}]} = \frac{1.8 \times 10^{-2}}{0.30^2 \times 1.00} = \frac{1.8 \times 10^{-2}}{0.090} = 0.20$$
  - **推导单位**（把各物理量单位代入分式约分）：
    $$\text{单位} = \frac{\text{mol/(L}\cdot\text{s)}}{(\text{mol/L})^2 \cdot (\text{mol/L})} = \frac{\text{mol}}{\text{L}\cdot\text{s}} \times \frac{\text{L}^3}{\text{mol}^3} = \text{L}^2/(\text{mol}^2\cdot\text{s})$$
  > 💡 **讲师批注**：$k$ 的单位不是固定的，随总级数 $n = x + y$ 变化！记住通用公式：**$\text{L}^{n-1}/(\text{mol}^{n-1}\cdot\text{s})$**。本题 $n = 2 + 1 = 3$，故 $n - 1 = 2$，单位就是 $\text{L}^2/(\text{mol}^2\cdot\text{s})$。同时注意保留 2 位有效数字要写成 **$0.20$**，不能漏写末尾的 `0`！

- **(3) 代入新初始浓度求生成速率 $v$**
  $$v = 0.20 \times (0.20)^2 \times 0.50 = 0.20 \times 0.040 \times 0.50 = 4.0 \times 10^{-3}\text{ mol/(L}\cdot\text{s)}$$

##### 【最终答案】
- **(1) $x = 2,\; y = 1$**
- **(2) $0.20\text{ L}^2/(\text{mol}^2\cdot\text{s})$**
- **(3) $4.0 \times 10^{-3}\text{ mol/(L}\cdot\text{s)}$**

---

### 3.6 化学平衡与平衡常数计算（原书 P.55–P.57 / PDF P.56–P.58）

#### 【核心图解：化学平衡建立过程三联图（$\text{H}_2 + \text{I}_2 \rightleftharpoons 2\text{HI}$）（SVG）】
<svg viewBox="0 0 420 260" xmlns="http://www.w3.org/2000/svg" style="background:#ffffff;border:1px solid #e2e8f0;border-radius:8px;max-width:100%;">
  <defs>
    <marker id="eq-arr" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="5" markerHeight="5" orient="auto">
      <path d="M 0 10 L 5 0 L 10 10 z" fill="#334155"/>
    </marker>
    <marker id="eq-arr-r" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="5" markerHeight="5" orient="auto">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#334155"/>
    </marker>
  </defs>
  <text x="210" y="20" text-anchor="middle" font-size="13" font-weight="bold" fill="#0f172a">平衡状態に至る過程（H₂ + I₂ ⇌ 2HI）三联核心曲线</text>

  <!-- 子图 1：浓度变化 -->
  <g transform="translate(10,32)">
    <rect x="0" y="0" width="128" height="215" rx="6" fill="#f8fafc" stroke="#cbd5e1"/>
    <text x="64" y="18" text-anchor="middle" font-size="10.5" font-weight="bold" fill="#1e40af">① 濃度変化</text>
    <!-- 坐标轴 -->
    <line x1="22" y1="185" x2="22" y2="35" stroke="#334155" stroke-width="1.4" marker-end="url(#eq-arr)"/>
    <line x1="22" y1="185" x2="118" y2="185" stroke="#334155" stroke-width="1.4" marker-end="url(#eq-arr-r)"/>
    <text x="12" y="110" text-anchor="middle" font-size="9.5" fill="#475569" writing-mode="tb">濃度</text>
    <text x="70" y="202" text-anchor="middle" font-size="9.5" fill="#475569">経過時間</text>
    <!-- 平衡竖线 -->
    <line x1="80" y1="38" x2="80" y2="185" stroke="#94a3b8" stroke-width="1.2" stroke-dasharray="3,2"/>
    <text x="84" y="48" font-size="8.5" fill="#475569">→平衡</text>
    <!-- HI 曲线（红） -->
    <path d="M 22 185 Q 45 75, 80 72 L 114 72" fill="none" stroke="#dc2626" stroke-width="2.2"/>
    <text x="98" y="66" text-anchor="middle" font-size="9" font-weight="bold" fill="#dc2626">HI</text>
    <!-- H2, I2 曲线（蓝） -->
    <path d="M 22 100 Q 45 155, 80 158 L 114 158" fill="none" stroke="#2563eb" stroke-width="2.2"/>
    <text x="98" y="151" text-anchor="middle" font-size="9" font-weight="bold" fill="#2563eb">H₂, I₂</text>
  </g>

  <!-- 子图 2：反应速度变化 -->
  <g transform="translate(146,32)">
    <rect x="0" y="0" width="128" height="215" rx="6" fill="#f8fafc" stroke="#cbd5e1"/>
    <text x="64" y="18" text-anchor="middle" font-size="10.5" font-weight="bold" fill="#065f46">② 反応速度変化</text>
    <line x1="22" y1="185" x2="22" y2="35" stroke="#334155" stroke-width="1.4" marker-end="url(#eq-arr)"/>
    <line x1="22" y1="185" x2="118" y2="185" stroke="#334155" stroke-width="1.4" marker-end="url(#eq-arr-r)"/>
    <text x="12" y="110" text-anchor="middle" font-size="9.5" fill="#475569" writing-mode="tb">反応速度</text>
    <text x="70" y="202" text-anchor="middle" font-size="9.5" fill="#475569">経過時間</text>
    <line x1="80" y1="38" x2="80" y2="185" stroke="#94a3b8" stroke-width="1.2" stroke-dasharray="3,2"/>
    <text x="84" y="48" font-size="8.5" fill="#475569">→平衡</text>
    <!-- 正反应速度（绿） -->
    <path d="M 22 65 Q 45 120, 80 125 L 114 125" fill="none" stroke="#059669" stroke-width="2.2"/>
    <text x="54" y="88" font-size="8.5" font-weight="bold" fill="#059669">正反応</text>
    <!-- 逆反应速度（橙） -->
    <path d="M 22 185 Q 45 130, 80 125 L 114 125" fill="none" stroke="#ea580c" stroke-width="2.2"/>
    <text x="54" y="162" font-size="8.5" font-weight="bold" fill="#ea580c">逆反応</text>
    <text x="98" y="118" text-anchor="middle" font-size="8.5" font-weight="bold" fill="#0f172a">v₁ = v₂</text>
  </g>

  <!-- 子图 3：触媒的影响 -->
  <g transform="translate(282,32)">
    <rect x="0" y="0" width="128" height="215" rx="6" fill="#f8fafc" stroke="#cbd5e1"/>
    <text x="64" y="18" text-anchor="middle" font-size="10.5" font-weight="bold" fill="#7c3aed">③ 触媒の影響</text>
    <line x1="22" y1="185" x2="22" y2="35" stroke="#334155" stroke-width="1.4" marker-end="url(#eq-arr)"/>
    <line x1="22" y1="185" x2="118" y2="185" stroke="#334155" stroke-width="1.4" marker-end="url(#eq-arr-r)"/>
    <text x="12" y="110" text-anchor="middle" font-size="9.5" fill="#475569" writing-mode="tb">HI 濃度</text>
    <text x="70" y="202" text-anchor="middle" font-size="9.5" fill="#475569">経過時間</text>
    <!-- 两条平衡时间线 -->
    <line x1="56" y1="45" x2="56" y2="185" stroke="#7c3aed" stroke-width="1.1" stroke-dasharray="3,2"/>
    <line x1="88" y1="45" x2="88" y2="185" stroke="#94a3b8" stroke-width="1.1" stroke-dasharray="3,2"/>
    <!-- 触媒あり（紫） -->
    <path d="M 22 185 Q 34 80, 56 76 L 114 76" fill="none" stroke="#7c3aed" stroke-width="2.2"/>
    <text x="48" y="68" text-anchor="middle" font-size="8.5" font-weight="bold" fill="#7c3aed">触媒あり</text>
    <!-- 触媒なし（灰） -->
    <path d="M 22 185 Q 50 85, 88 76 L 114 76" fill="none" stroke="#64748b" stroke-width="2"/>
    <text x="88" y="115" text-anchor="middle" font-size="8.5" font-weight="bold" fill="#475569">触媒なし</text>
    <text x="72" y="176" text-anchor="middle" font-size="8" fill="#6d28d9">终点高度完全相同！</text>
  </g>
</svg>

---

#### 练习组 6：化学平衡常数与三段式计算（原书 P.56–P.57 / PDF P.57–P.58）

##### 【原题重现与翻译】
> $\text{H}_2 + \text{I}_2 \rightleftharpoons 2\text{HI} \quad \cdots\text{①}$ について考える。
> （1）①の正反応の反応速度 $v_1$ は $\text{H}_2$ と $\text{I}_2$ の濃度に比例し，逆反応の反応速度 $v_2$ は $\text{HI}$ の濃度の 2 乗に比例する。正反応の反応速度定数 $k_1$ と逆反応の反応速度定数 $k_2$ を用いて①の平衡定数 $K$ を表せ。
> （① 的正反应速率 $v_1$ 与 $\text{H}_2, \text{I}_2$ 浓度成正比，逆反应速率 $v_2$ 与 $\text{HI}$ 浓度的平方成正比。用 $k_1, k_2$ 表示平衡常数 $K$。）
> （2）一定体積の容器に $2.5\text{ mol}$ の $\text{H}_2$ と $2.5\text{ mol}$ の $\text{I}_2$ を入れたところ，①が平衡状態に達して $\text{H}_2$ は $0.50\text{ mol}$ になった。この温度における平衡定数 $K$ を求めよ。
> （在恒容容器中加入 $2.5\text{ mol}$ $\text{H}_2$ 和 $2.5\text{ mol}$ $\text{I}_2$，达到平衡时 $\text{H}_2$ 变为 $0.50\text{ mol}$。求该温度下的平衡常数 $K$。）
> （3）最初に $2.0\text{ mol}$ の $\text{H}_2$ と $2.0\text{ mol}$ の $\text{I}_2$ を入れて (2) と同じ温度で平衡に達したときに生成する $\text{HI}$ の物質量を求めよ。
> （最初加入 $2.0\text{ mol}$ $\text{H}_2$ 和 $2.0\text{ mol}$ $\text{I}_2$，在与 (2) 相同温度下达到平衡时，求生成的 $\text{HI}$ 的物质的量。）

##### 【考点定位】
平衡常数的动力学推导（$v_1 = v_2$）、化学平衡“三段式（反応前・変化量・平衡時）”计算，以及气体分子数不变的反应中容积 $V$ 自动消去的技巧。

##### 【分步标准解答】
- **(1) 用 $k_1, k_2$ 表示平衡常数 $K$**
  - 由题意写出正、逆反应速率方程：
    $$v_1 = k_1[\text{H}_2][\text{I}_2], \qquad v_2 = k_2[\text{HI}]^2$$
  - 平衡状态下 $v_1 = v_2$，即 $k_1[\text{H}_2][\text{I}_2] = k_2[\text{HI}]^2$，移项得：
    $$K = \frac{[\text{HI}]^2}{[\text{H}_2][\text{I}_2]} = \frac{k_1}{k_2}$$

- **(2) 三段式求平衡常数 $K$**
  - 列出物质变化三段式：

  | 阶段 | $\text{H}_2$ | $+$ | $\text{I}_2$ | $\rightleftharpoons$ | $2\text{HI}$ |
  | :---: | :---: | :---: | :---: | :---: | :---: |
  | **反応前** | $2.5\text{ mol}$ | | $2.5\text{ mol}$ | | $0\text{ mol}$ |
  | **変化量** | $-2.0\text{ mol}$ | | $-2.0\text{ mol}$ | | $+2.0 \times 2\text{ mol}$ |
  | **平衡時** | $0.50\text{ mol}$ | | $0.50\text{ mol}$ | | $4.0\text{ mol}$ |

  - 设容器容积为 $V\text{ [L]}$，代入平衡常数表达式：
    $$K = \frac{[\text{HI}]^2}{[\text{H}_2][\text{I}_2]} = \frac{\left(\dfrac{4.0}{V}\right)^2}{\left(\dfrac{0.50}{V}\right)\left(\dfrac{0.50}{V}\right)} = \frac{16}{0.25} = 64$$
  > 💡 **讲师批注**：本题左右两边系数之和相等（$1 + 1 = 2$），所以 $V^2$ 完美消去，$K$ 无单位！以后只要遇到**前后气体分子数相等**的平衡计算，可以直接用**物质的量**代替浓度算 $K$，省时省力！

- **(3) 相同温度下求新投料平衡时 $\text{HI}$ 的物质的量**
  - **关键点**：温度不变 $\Rightarrow$ 平衡常数 **$K = 64$ 不变**！
  - 设 $\text{H}_2$ 反应消耗了 $x\text{ mol}$，列三段式：

  | 阶段 | $\text{H}_2$ | $+$ | $\text{I}_2$ | $\rightleftharpoons$ | $2\text{HI}$ |
  | :---: | :---: | :---: | :---: | :---: | :---: |
  | **反応前** | $2.0\text{ mol}$ | | $2.0\text{ mol}$ | | $0\text{ mol}$ |
  | **変化量** | $-x\text{ mol}$ | | $-x\text{ mol}$ | | $+2x\text{ mol}$ |
  | **平衡時** | $(2.0 - x)\text{ mol}$ | | $(2.0 - x)\text{ mol}$ | | $2x\text{ mol}$ |

  - 代入 $K = 64$（容积 $V$ 消去）：
    $$\frac{(2x)^2}{(2.0 - x)^2} = 64$$
  - 两边同时开平方（因为 $0 \lt x \lt 2.0$，分子分母均为正数）：
    $$\frac{2x}{2.0 - x} = 8 \implies 2x = 16 - 8x \implies 10x = 16 \implies x = 1.6$$
  - 故生成 $\text{HI}$ 的物质的量为 $2x = 2 \times 1.6 = 3.2\text{ mol}$。
  > 💡 **讲师批注**：千万不要手滑直接把 $x = 1.6\text{ mol}$ 当作答案！题目问的是 **$\text{HI}$ 的物质的量**，它是 **$2x$**，所以一定要乘以 2 得到 $3.2\text{ mol}$！

##### 【最终答案】
- **(1) $K = \dfrac{k_1}{k_2}$**
- **(2) $64$**
- **(3) $3.2\text{ mol}$**

---

### 3.7 勒夏特列原理（ルシャトリエの原理）（原书 P.58–P.59 / PDF P.59–P.60）

#### 练习组 7：10 道条件变化判断平衡移动方向（原书 P.58–P.59 / PDF P.59–P.60）

##### 【原题重现与翻译】
> 次の平衡状態にカッコ内の条件変化を与えると平衡はどちらに移動するか。（对下列平衡状态施加括号内的条件变化时，平衡向哪一方向移动？）
> (1) $\text{NH}_3 + \text{H}_2\text{O} \rightleftharpoons \text{NH}_4^+ + \text{OH}^-$ （$\text{NaOH}$ を加える / 加入 $\text{NaOH}$）
> (2) $2\text{SO}_2 + \text{O}_2 \rightleftharpoons 2\text{SO}_3$ （加圧する / 加压）
> (3) $\text{H}_2 + \text{I}_2 \rightleftharpoons 2\text{HI}$ （減圧する / 减压）
> (4) $\text{N}_2 + 3\text{H}_2 \rightleftharpoons 2\text{NH}_3 + 92\text{ kJ}$ （加熱する / 加热）
> (5) $3\text{O}_2 \rightleftharpoons 2\text{O}_3 - 285\text{ kJ}$ （冷却する / 冷却）
> (6) $\text{N}_2 + 3\text{H}_2 \rightleftharpoons 2\text{NH}_3$ （触媒を加える / 加入催化剂）
> (7) $\text{C}(\text{固}) + \text{H}_2\text{O}(\text{気}) \rightleftharpoons \text{CO} + \text{H}_2$ （加圧する / 加压）
> (8) $\text{N}_2 + 3\text{H}_2 \rightleftharpoons 2\text{NH}_3$ （体積を小さくする / 缩小体积）
> (9) $\text{N}_2 + 3\text{H}_2 \rightleftharpoons 2\text{NH}_3$ （温度・体積一定でアルゴンを加える / 恒温恒容下加入氩气）
> (10) $\text{N}_2 + 3\text{H}_2 \rightleftharpoons 2\text{NH}_3$ （温度・全圧一定でアルゴンを加える / 恒温恒压下加入氩气）

##### 【考点定位】
浓度、压强、温度、催化剂、固体不计入气体分子数、以及**恒容 vs 恒压通入惰性气体**（EJU 选择题超级高频坑！）。

##### 【分步标准解答】
- **(1)** 加入 $\text{NaOH}$ 使溶液中 $[\text{OH}^-]$ 增大 $\to$ 平衡向减小 $[\text{OH}^-]$ 的方向移动 $\Rightarrow$ **左に移動**。
- **(2)** 左侧气体分子数 $2 + 1 = 3$，右侧为 $2$；加压时向**气体分子数减少**的方向移动（$3 \to 2$） $\Rightarrow$ **右に移動**。
- **(3)** 左侧气体分子数 $1 + 1 = 2$，右侧为 $2$；前后气体分子数相等，改变压强不影响平衡 $\Rightarrow$ **移動しない**。
- **(4)** 正反应 `+ 92 kJ` 为放热反应，逆反应为吸热反应；加热时向**吸热方向**移动 $\Rightarrow$ **左に移動**。
- **(5)** 正反应 `- 285 kJ` 为吸热反应，逆反应为放热反应；冷却时向**放热方向**移动 $\Rightarrow$ **左に移動**。
- **(6)** 催化剂同等加快正逆反应速率，**不改变平衡位置** $\Rightarrow$ **移動しない**。
- **(7)** **陷阱题！** $\text{C}(\text{固})$ 是固体不计入气体分子数！因此左侧气体分子数为 **$1$**（只有 $\text{H}_2\text{O}(\text{気})$），右侧气体分子数为 **$1 + 1 = 2$**（$\text{CO}, \text{H}_2$）。加压向气体分子数减少的方向移动（$2 \to 1$） $\Rightarrow$ **左に移動**。
- **(8)** 缩小容器体积等价于**加压**；左侧气体 $1 + 3 = 4$，右侧为 $2$，向分子数减少方向移动 $\Rightarrow$ **右に移動**。
- **(9)** **经典必考题！** 恒温恒容下充入不参与反应的稀有气体 $\text{Ar}$，虽然容器总压升高，但 $\text{N}_2, \text{H}_2, \text{NH}_3$ 的**各自浓度和分压均未改变** $\Rightarrow$ **移動しない**。
- **(10)** **经典必考题！** 恒温**恒全压**下充入 $\text{Ar}$，为维持总压不变容器体积必须**膨胀**，导致 $\text{N}_2, \text{H}_2, \text{NH}_3$ 的分压（浓度）全部降低，**等效于减压** $\to$ 向气体分子数增加的方向移动（$2 \to 4$） $\Rightarrow$ **左に移動**。

> 💡 **讲师批注**：把 (9) 和 (10) 刻进 DNA！判断充入惰性气体的铁律：**只看反应物/生成物自身的浓度（分压）变没变**！恒容 $\to$ 体积不变 $\to$ 浓度不变 $\to$ 不移动；恒压 $\to$ 体积变大 $\to$ 浓度变小（等效减压） $\to$ 向气体分子数多的方向移动！

##### 【最终答案】
- **(1) 左に移動　(2) 右に移動　(3) 移動しない　(4) 左に移動　(5) 左に移動**
- **(6) 移動しない　(7) 左に移動　(8) 右に移動　(9) 移動しない　(10) 左に移動**

---

### 3.8 酸与碱的定义、分类与电离度（原书 P.59 / PDF P.60）

#### ① 两大酸碱定义对比
| 定义体系 | 酸（さん） | 塩基（えんき） | 典型例式 |
| :--- | :--- | :--- | :--- |
| **アレニウスの定義**（阿伦尼乌斯） | 溶于水产生 $\text{H}^+$ 的物质 | 溶于水产生 $\text{OH}^-$ 的物质 | 酸：$\text{HCl} \to \text{H}^+ + \text{Cl}^-$<br>塩基：$\text{NaOH} \to \text{Na}^+ + \text{OH}^-$ |
| **ブレンステッド・ローリーの定義**（布朗斯特-劳里） | **给出 $\text{H}^+$** 的物质 | **接受 $\text{H}^+$** 的物质 | $\underbrace{\text{HCl}}_{\text{酸}} + \underbrace{\text{H}_2\text{O}}_{\text{塩基}} \to \text{Cl}^- + \text{H}_3\text{O}^+$<br>$\underbrace{\text{NH}_3}_{\text{塩基}} + \underbrace{\text{H}_2\text{O}}_{\text{酸}} \to \text{NH}_4^+ + \text{OH}^-$ |

> 💡 **讲师批注**：注意看上表中 **$\text{H}_2\text{O}$ 的双重身份**：遇到比它强的酸 $\text{HCl}$ 时，水接受 $\text{H}^+$ 作**塩基**；遇到碱 $\text{NH}_3$ 时，水给出 $\text{H}^+$ 作**酸**！这就是 EJU 常考的“水在布朗斯特-劳里定义中既可作酸又可作碱”。

#### ② 代表性强弱酸碱必背速查表（原书 P.59）
| 价数 | 強酸（强酸） | 弱酸（弱酸） | 強塩基（强碱） | 弱塩基（弱碱） |
| :---: | :--- | :--- | :--- | :--- |
| **1 価** | 塩酸 $\text{HCl}$<br>硝酸 $\text{HNO}_3$ | 酢酸 $\text{CH}_3\text{COOH}$ | 水酸化カリウム $\text{KOH}$<br>水酸化ナトリウム $\text{NaOH}$ | アンモニア $\text{NH}_3$ |
| **2 価** | 硫酸 $\text{H}_2\text{SO}_4$ | 炭酸 $\text{H}_2\text{CO}_3$<br>硫化水素 $\text{H}_2\text{S}$<br>シュウ酸 $\text{H}_2\text{C}_2\text{O}_4$ | 水酸化バリウム $\text{Ba(OH)}_2$<br>水酸化カルシウム $\text{Ca(OH)}_2$ | $\text{Mg(OH)}_2$<br>$\text{Cu(OH)}_2$ など |
| **3 価** | *(中程度の酸)* リン酸 $\text{H}_3\text{PO}_4$ | — | **なし（无）** | $\text{Al(OH)}_3$<br>$\text{Fe(OH)}_3$ など |

- **电离度公式**：
  $$\alpha = \frac{\text{電離した電解質の物質量}}{\text{溶かした電解質の物質量}} \qquad (0 \le \alpha \le 1)$$
  - 强酸・强碱：$\alpha \approx 1$（水溶液中几乎 $100\%$ 电离），写单向箭头 `→`。
  - 弱酸・弱碱：$\alpha \ll 1$（水溶液中仅部分电离），写可逆号 `⇌`。

---

## 4. 全局术语与物质名录同步

本切片新增的全部日文化学核心词汇与物质名录（含平假名注音与罗马音）已按分类同步写入 `./notes_化学/_glossary_parts/glossary_004.md`，待全局汇总合并至 `./notes_化学/glossary_all.md`。
