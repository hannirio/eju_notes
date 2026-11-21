# EJU 化学基础・第二章 物質の状態（下）＆ 第三章 物質の反応（开篇）（切片 003：P31–P45）

> **对应原教材**：格致学苑《EJU 化学対策》「化学基礎・第二章 物質の状態」（第 8–16 节，原书 P.30–P.43）及「化学基礎・第三章 物質の反応」（第 1 节，原书 P.44），对应 PDF 第 31–45 页
> **适用对象**：忘却国内高中化学基础、零起步对接日本 EJU 留考化学体系的同学

---

## 1. 本节前置：国内高中化学基础唤醒

本切片是整个「理论化学（物理化学部分）」的计算核心，涵盖了**液体的蒸气压与沸腾、固体与气体的溶解度、稀溶液的依数性（沸点上升/凝固点降下/渗透压）、胶体、以及热化学方程式的开篇**。只要把“动态平衡”和“微粒数决定依数性”两条主线打通，所有计算题都是套公式送分题！

### 1.1 国内高中核心基础快速唤醒

1. **气液平衡、饱和蒸气压与沸腾**
   - 把液体装入密闭容器，液体不断蒸发，同时蒸气分子也会撞回液面凝结。当**蒸发速率 $=$ 凝结速率**时，宏观上气液两相不再变化，这就是**气液平衡（気液平衡）**。
   - 此时的气体压强叫**饱和蒸气压（蒸気圧）**。**极其重要**：同一种液体的饱和蒸气压**只取决于温度**（温度越高，蒸气压越大），与容器体积、液体多少、有无其他气体**完全无关**！
   - **沸腾（沸騰）**：不仅在液面，液体内部也剧烈产生气泡的现象。条件是：**液体的饱和蒸气压 $=$ 外界大气压**。因此高原气压低，水不到 $100^\circ\text{C}$ 就沸腾；高压锅气压高，水超过 $100^\circ\text{C}$ 才沸腾。
   - **密闭容器中“是否有液态水残留”的判别法（EJU 必考！）**：
     - 先“假设全部变成气体”，用理想气体状态方程 $PV = nRT$ 算出理论压强 $P$，再与该温度下的饱和蒸气压 $P_0$ 比较：
       - 若 $P \le P_0$：说明没达到饱和，**全部为气体（无液体残留）**，实际水蒸气分压 $= P$。
       - 若 $P \gt P_0$：说明超过了饱和极限，多出来的必然液化，**容器内有液体残留**，实际水蒸气分压被“封顶”在 **$P_0$**！
2. **固体的溶解度与结晶**
   - **溶解度 $S$**：一定温度下，**$100\text{ g}$ 溶剂（通常是水）**中最多能溶解的溶质质量（单位 $\text{g/100g 水}$）。
   - 饱和溶液的“黄金两连比”：
     $$\frac{\text{溶质质量}}{\text{溶液质量}} = \frac{S}{100 + S} \qquad \text{与} \qquad \frac{\text{溶质质量}}{\text{溶剂质量}} = \frac{S}{100}$$
   - **水合物（结晶水合物，如 $\text{CuSO}_4\cdot 5\text{H}_2\text{O}$）的坑**：溶解度表给的永远是**无水物（$\text{CuSO}_4$）**的溶解度！当你把五水合硫酸铜投入水中时，它自带的 $5\text{H}_2\text{O}$ 会**变成溶剂水**；当你降温析出五水合硫酸铜晶体时，它也会从溶液里**顺手带走结晶水**！
3. **气体的溶解度与亨利定律（ヘンリーの法則）**
   - **温度影响**：温度越高，气体分子热运动越剧烈，越容易逃出水面，故**温度越高，气体溶解度越小**（与大多数固体相反）。
   - **压强影响（亨利定律）**：对难溶且不与水反应的气体（如 $\text{N}_2, \text{O}_2, \text{CO}_2$；**不适用于极易溶或与水反应的 $\text{NH}_3, \text{HCl}$**），恒温下溶解在定体积溶剂中的气体**质量（或物质的量）**与该气体的**分压成正比**。
   - **最反直觉的推论**：恒温下，压强增大为 $k$ 倍，溶解的气体物质的量变为 $k$ 倍，但根据玻意耳定律，该压强下气体体积又被压缩为 $\frac{1}{k}$——两者一乘正好抵消！因此，**“在该压强下直接测定的溶解气体体积”与压强无关，始终恒定**；只有**换算回标准状态（$0^\circ\text{C}, 1.013\times 10^5\text{ Pa}$）的体积**才与压强成正比！
4. **稀溶液的依数性（希薄溶液の性質）**
   - 当水中溶入**不挥发性溶质**（如糖、尿素、食盐）后，液面一部分被溶质粒子占领，阻碍了水分子蒸发，导致**蒸气压降下（蒸気圧降下）**。
   - 由此引发三大连锁反应（只取决于**溶质粒子的总浓度**，与粒子种类无关）：
     1. **沸点上升**：$\Delta t = K_b m$（$m$ 为质量摩尔浓度，单位 $\text{mol/kg}$，即**每 $1\text{ kg}$ 溶剂**中溶质粒子的物质的量）。
     2. **凝固点降下**：$\Delta t = K_f m$（冬天撒融雪剂盐就是利用冰点降低）。
     3. **渗透压（浸透圧）**：半透膜只允许水分子通过，水分子自动从低浓度（纯水）向高浓度（溶液）扩散。范特霍夫定律（ファントホッフの法則）：$\Pi = cRT$（$c$ 为物质的量浓度 $\text{mol/L}$）。
   - **电解质必踩大坑**：公式中的浓度必须是**溶液中所有溶质粒子（离子 + 未电离分子）的总浓度**！例如 $\text{Na}_2\text{SO}_4 \to 2\text{Na}^+ + \text{SO}_4^{2-}$ 产生 **3 倍**粒子；$\text{BaCl}_2 \to \text{Ba}^{2+} + 2\text{Cl}^-$ 也产生 **3 倍**粒子！
5. **胶体（コロイド）**
   - 粒子直径 **$10^{-9} \sim 10^{-7}\text{ m}$（$1 \sim 100\text{ nm}$）**：**能透过滤纸，但不能透过半透膜**（利用此性质可用渗析法提纯胶体）。
   - 两大特征现象：**丁达尔效应（チンダル現象）**（光的散射）、**布朗运动（ブラウン運動）**（溶剂分子不规则撞击引起）。
   - 两大分类与聚沉：**疏水胶体（疎水コロイド，如 $\text{Fe(OH)}_3$）**加**少量**电解质就沉淀（叫**凝析**）；**亲水胶体（親水コロイド，如淀粉、蛋白质）**加**大量**电解质才沉淀（叫**盐析**）。
6. **反应热与热化学方程式（反応熱と熱化学方程式）**
   - 化学反应伴随能量变化：反应物总能量高于生成物时**放热（発熱反応）**，反之**吸热（吸熱反応）**。

---

### 1.2 中日化学体系差异提醒（EJU 避坑必看）

1. **质量摩尔浓度 $m$ vs 物质的量浓度 $c$**：
   - 国内高中几乎不考质量摩尔浓度（只到大学物化才学），但 EJU 必考！务必盯紧分母：
     - 沸点上升 / 凝固点降下用 **質量モル濃度 $m = \frac{\text{溶质 [mol]}}{\text{溶剂 [kg]}}$**（分母是**溶剂质量**，单位 $\text{kg}$！）。
     - 渗透压用 **モル濃度 $c = \frac{\text{溶质 [mol]}}{\text{溶液 [L]}}$**（分母是**溶液体积**，单位 $\text{L}$！）。
2. **气体常数 $R$ 的日本常用单位**：
   - 国内常用 $R = 8.314\text{ J/(mol}\cdot\text{K)}$ 或 $0.082\text{ atm}\cdot\text{L/(mol}\cdot\text{K)}$；日本 EJU 统一给定 **$R = 8.3 \times 10^3\text{ Pa}\cdot\text{L/(mol}\cdot\text{K)}$**！代入 $PV=nRT$ 或 $\Pi = cRT$ 时，压强必须用 **$\text{Pa}$**，体积必须用 **$\text{L}$**，温度必须用 **$\text{K}$（$T = t + 273$）**！
3. **热化学方程式的“正负号”与国内完全相反（超高频重灾区！）**：
   - **国内高中（$\Delta H$ 体系）**：放热写 $\Delta H \lt 0$（负号），吸热写 $\Delta H \gt 0$（正号），用 `==` 或 `→` 连接。
   - **日本传统热化学方程式（本教材采用）**：用**等号 `=`** 表示能量守恒！
     - **放热反应**右侧写 **`+ Q kJ`**，如：$\text{C(黒鉛)} + \text{O}_2\text{(気)} = \text{CO}_2\text{(気)} + 394\text{ kJ}$
     - **吸热反应**右侧写 **`- Q kJ`**，如：$\text{C(黒鉛)} + \text{H}_2\text{O(気)} = \text{CO(気)} + \text{H}_2\text{(気)} - 131\text{ kJ}$
     - 物质状态用中文括号标注：`(気)`、`(液)`、`(固)`、`C(黒鉛)`。
     - **定义热（如燃焼熱）**：规定**被研究的物质系数必须为 1**，因此其他物质允许出现分数系数（如 $\frac{1}{2}\text{O}_2$、$\frac{7}{2}\text{O}_2$）。
   - *新课改前瞻提示*：日本高中新课程（2025 年起逐步对接 EJU）正引入国际标准的 **エンタルピー変化 $\Delta H$**（此时放热为负 $\Delta H = -394\text{ kJ/mol}$）。请牢记转换口诀：**“日本旧等号右侧 $+Q$ $\iff$ 国际新写法 $\Delta H = -Q$”**！

> ⚠️ **原教材印刷勘误与漏解提醒（讲师逐页人工核对参考图发现）**：
> 1. **原书 P.31（PDF 第 32 页）**：例题题干明确要求「容器内の圧力と**液体の水の質量**を求めよ」（求容器内压强和**液态水的质量**），但原书解答只算了容器内压强 $1.3 \times 10^5\text{ Pa}$，**漏掉了液态水质量的求解**！本笔记已在对应例题中完整补全（答案：$2.3\text{ g}$）。
> 2. **原书 P.35（PDF 第 36 页）**：章节编号从 `10. 固体の溶解度` 直接跳至 `12. 水和物の溶解度`（缺少第 11 节编号，属原书排版跳号）；此外，第 12 节例题共设 (1)(2)(3) 三小问，但原书**漏印了 (2) 和 (3) 的解答**！本笔记已全部补全。
> 3. **原书 P.37（PDF 第 38 页）**：亨利定律例题的第 (2) 小问在原书上被画了删除线；本笔记仍为您附上 (2) 的标准解法，因为紧随其后的 EJU 真题「問 10」考的正是换算成标准状态的体积！
> 4. **原书 P.42（PDF 第 43 页）**：防衛大・改例题题干中「液注の高さ」系错别字，正确汉字应为 **「液柱（えきちゅう）」**。

---

## 2. 日文化学核心词汇、物质名称与假名注音（板书必备）

### 2.1 蒸气压、沸腾与排水集气
- **気液平衡（きえきへいこう / kieki heikō）** — 气液平衡
- **蒸発・凝縮（じょうはつ・ぎょうしゅく / jōhatsu, gyōshuku）** — 蒸发・凝结（液化）
- **蒸気圧 / 飽和水蒸気圧（じょうきあつ / ほうわすいじょうきあつ / jōkiatsu, hōwa suijōkiatsu）** — 蒸气压 / 饱和水蒸气压
- **蒸気圧曲線（じょうきあつきょくせん / jōkiatsu kyokusen）** — 蒸气压曲线
- **沸騰・沸点（ふっとう・ふってん / futtō, futten）** — 沸腾・沸点
- **外圧・大気圧（がいあつ・たいきあつ / gaiatsu, taikiatsu）** — 外压・大气压
- **ジエチルエーテル（じえちるえーてる / jiechiru ēteru）** — 乙醚（$\text{C}_2\text{H}_5\text{OC}_2\text{H}_5$，沸点 $34^\circ\text{C}$）
- **エタノール（えたのーる / etanōru）** — 乙醇/酒精（$\text{C}_2\text{H}_5\text{OH}$，沸点 $78^\circ\text{C}$）
- **分圧・全圧（ぶんあつ・ぜんあつ / bun'atsu, zen'atsu）** — 分压・总压
- **水上置換法（すいじょうちかんほう / suijō chikanhō）** — 排水集气法
- **捕集（ほしゅう / hoshū）** — 收集（气体）
- **水面を一致させる（すいめんをいっちさせる / suimen o icchi saseru）** — 使管内外液面齐平

### 2.2 固体、水合物与气体的溶解度
- **飽和溶液（ほうわようえき / hōwa yōeki）** — 饱和溶液
- **溶媒・溶質・溶液（ようばい・ようしつ・ようえき / yōbai, yōshitsu, yōeki）** — 溶剂・溶质・溶液
- **溶解平衡（ようかいへいこう / yōkai heikō）** — 溶解平衡
- **析出（せきしゅつ / sekishutsu）** — 析出
- **固体の溶解度（こたいのようかいど / kotai no yōkaido）** — 固体的溶解度
- **溶解度曲線（ようかいどきょくせん / yōkaido kyokusen）** — 溶解度曲线
- **再結晶（さいけっしょう / saikesshō）** — 重结晶
- **質量パーセント濃度（しつりょうぱーせんとのうど / shitsuryō pāsento nōdo）** — 质量分数（质量百分比浓度）
- **水和物（すいわぶつ / suiwabutsu）** — 水合物（结晶水合物）
- **硫酸銅（II）五水和物（りゅうさんどう（に）ごすいわぶつ / ryūsandō (ni) gosuiwabutsu）** — 五水合硫酸铜（$\text{CuSO}_4\cdot 5\text{H}_2\text{O}$，蓝矾）
- **気体の溶解度（きたいのようかいど / kitai no yōkaido）** — 气体的溶解度
- **ヘンリーの法則（へんりーのほうそく / Henrī no hōsoku）** — 亨利定律
- **標準状態（ひょうじゅんじょうたい / hyōjun jōtai）** — 标准状态（$0^\circ\text{C}, 1.013\times 10^5\text{ Pa}$）
- **換算する（かんざんする / kanzan suru）** — 换算

### 2.3 稀溶液的性质、渗透压与胶体
- **希薄溶液（きはくようえき / kihaku yōeki）** — 稀溶液
- **不揮発性（ふきはつせい / fukihatsusei）** — 不挥发性
- **蒸気圧降下（じょうきあつこうか / jōkiatsu kōka）** — 蒸气压下降
- **沸点上昇・沸点上昇度（ふってんじょうしょう・ふってんじょうしょうど / futten jōshō, futten jōshōdo）** — 沸点上升・沸点上升度（$\Delta t$）
- **質量モル濃度（しつりょうもるのうど / shitsuryō moru nōdo）** — 质量摩尔浓度（$m\text{ [mol/kg]}$）
- **モル沸点上昇（もるふってんじょうしょう / moru futten jōshō）** — 摩尔沸点上升常数（$K_b$）
- **凝固点降下・凝固点降下度（ぎょうこてんこうか・ぎょうこてんこうかど / gyōkoten kōka, gyōkoten kōkado）** — 凝固点下降・凝固点下降度（$\Delta t$）
- **モル凝固点降下（もるぎょうこてんこうか / moru gyōkoten kōka）** — 摩尔凝固点下降常数（$K_f$）
- **冷却曲線・過冷却（れいきゃくきょくせん・かれいきゃく / reikyaku kyokusen, kareikyaku）** — 冷却曲线・过冷现象
- **非電解質・電解質（ひでんかいしつ・でんかいしつ / hidenkaishitsu, denkaishitsu）** — 非电解质・电解质
- **グルコース（ぐるこーす / gurukōsu）** — 葡萄糖（$\text{C}_6\text{H}_{12}\text{O}_6$，$M=180$）
- **尿素（にょうそ / nyōso）** — 尿素（$(\text{NH}_2)_2\text{CO}$，$M=60$）
- **硫酸ナトリウム（りゅうさんなとりうむ / ryūsan natoriumu）** — 硫酸钠（$\text{Na}_2\text{SO}_4$，$M=142$）
- **塩化バリウム（えんかばりうむ / enka bariumu）** — 氯化钡（$\text{BaCl}_2$）
- **半透膜（はんとうまく / hantōmaku）** — 半透膜
- **浸透・浸透圧（しんとう・しんとうあつ / shintō, shintōatsu）** — 渗透・渗透压（$\Pi$）
- **ファントホッフの法則（ふぁんとほっふのほうそく / Fanto Hoffu no hōsoku）** — 范特霍夫定律（$\Pi = cRT$）
- **液柱（えきちゅう / ekichū）** — 液柱
- **水銀（すいぎん / suigin）** — 水银/汞（$\text{Hg}$，密度 $13.6\text{ g/cm}^3$）
- **コロイド・コロイド粒子（ころいど・ころいどりゅうし / koroido, koroido ryūshi）** — 胶体・胶体粒子
- **疎水コロイド・凝析（そすいころいど・ぎょうせき / sosui koroido, gyōseki）** — 疏水胶体・凝析（聚沉）
- **親水コロイド・塩析（しんすいころいど・えんせき / shinsui koroido, enseki）** — 亲水胶体・盐析
- **デンプン・タンパク質（でんぷん・たんぱくしつ / denpun, tanpakushitsu）** — 淀粉・蛋白质
- **チンダル現象（ちんだるげんしょう / Chindaru genshō）** — 丁达尔效应
- **ブラウン運動（ぶらうんうんどう / Buraun undō）** — 布朗运动

### 2.4 反应热与热化学方程式
- **反応熱（はんのうねつ / hannōnetsu）** — 反应热
- **熱化学方程式（ねつかがくほうていしき / netsukagaku hōteishiki）** — 热化学方程式
- **発熱反応（はつねつはんのう / hatsunetsu hannō）** — 放热反应
- **吸熱反応（きゅうねつはんのう / kyūnetsu hannō）** — 吸热反应
- **反応物・生成物（はんのうぶつ・せいせいぶつ / hannōbutsu, seiseibutsu）** — 反应物・生成物
- **燃焼熱（ねんしょうねつ / nenshōnetsu）** — 燃烧热
- **エタン（えたん / etan）** — 乙烷（$\text{C}_2\text{H}_6$）

### 关键化学方程式与公式的日语课堂口语读法
1. **$\Delta t = K_b m$ / $\Delta t = K_f m$**
   - 读作：**デルタ・ティー イコール ケー・ビー エム**（/ ケー・エフ エム）
2. **$\Pi = cRT$**
   - 读作：**パイ イコール シー・アール・ティー**（注意大写 $\Pi$ 在日本课堂读作“パイ” *pai*）
3. **$\text{H}_2\text{(気)} + \frac{1}{2}\text{O}_2\text{(気)} = \text{H}_2\text{O(液)} + 286\text{ kJ}$**
   - 读作：**エイチ・ツー（きたい） プラス にぶんのいち オー・ツー（きたい） イコール エイチ・ツー・オー（えきたい） プラス にひゃくはちじゅうろく キロジュール**
4. **$\text{C(黒鉛)} + \text{H}_2\text{O(気)} = \text{CO(気)} + \text{H}_2\text{(気)} - 131\text{ kJ}$**
   - 读作：**シー（こくえん） プラス エイチ・ツー・オー（きたい） イコール シー・オー（きたい） プラス エイチ・ツー（きたい） マイナス ひゃくさんじゅういち キロジュール**

---

## 3. 核心知识点图解与逐题深度解析

---

### 【知识点 8】蒸気圧曲線（蒸气压曲线）与液体存在判别（原书 P.30–31）

#### 图解辅助（SVG 1：三种典型液体的蒸气压曲线与沸点）
<svg viewBox="0 0 420 260" xmlns="http://www.w3.org/2000/svg" style="background:#fafafa;border:1px solid #e2e8f0;border-radius:8px;">
  <!-- 网格与坐标轴 -->
  <line x1="65" y1="220" x2="390" y2="220" stroke="#334155" stroke-width="1.8"/>
  <line x1="65" y1="220" x2="65" y2="25" stroke="#334155" stroke-width="1.8"/>
  <!-- 箭头 -->
  <polygon points="390,220 382,216 382,224" fill="#334155"/>
  <polygon points="65,25 61,33 69,33" fill="#334155"/>
  <!-- 纵轴刻度 -->
  <line x1="65" y1="50" x2="380" y2="50" stroke="#ef4444" stroke-width="1.5" stroke-dasharray="6,4"/>
  <text x="10" y="54" font-size="11" fill="#dc2626" font-weight="bold">大気圧 1.0</text>
  <text x="42" y="88" font-size="10" fill="#475569">0.8</text>
  <line x1="65" y1="84" x2="70" y2="84" stroke="#334155"/>
  <text x="42" y="122" font-size="10" fill="#475569">0.6</text>
  <line x1="65" y1="118" x2="70" y2="118" stroke="#334155"/>
  <text x="42" y="156" font-size="10" fill="#475569">0.4</text>
  <line x1="65" y1="152" x2="70" y2="152" stroke="#334155"/>
  <text x="42" y="190" font-size="10" fill="#475569">0.2</text>
  <line x1="65" y1="186" x2="70" y2="186" stroke="#334155"/>
  <text x="8" y="125" font-size="11" fill="#1e293b" font-weight="bold">蒸気圧</text>
  <text x="6" y="140" font-size="10" fill="#475569">[×10⁵Pa]</text>
  <!-- 横轴刻度 (0℃=65, 100℃=355 => 每1℃=2.9px) -->
  <text x="118" y="236" font-size="10" fill="#475569">20</text>
  <line x1="123" y1="220" x2="123" y2="215" stroke="#334155"/>
  <text x="176" y="236" font-size="10" fill="#475569">40</text>
  <line x1="181" y1="220" x2="181" y2="215" stroke="#334155"/>
  <text x="234" y="236" font-size="10" fill="#475569">60</text>
  <line x1="239" y1="220" x2="239" y2="215" stroke="#334155"/>
  <text x="292" y="236" font-size="10" fill="#475569">80</text>
  <line x1="297" y1="220" x2="297" y2="215" stroke="#334155"/>
  <text x="346" y="236" font-size="10" fill="#475569">100</text>
  <line x1="355" y1="220" x2="355" y2="215" stroke="#334155"/>
  <text x="200" y="253" font-size="11" fill="#1e293b" font-weight="bold">温度 [℃]</text>
  <!-- 乙醚曲线 (0℃约0.25, 34℃=1.0 => x=163.6, y=50) -->
  <path d="M 65 182 Q 125 145 164 50 L 172 30" fill="none" stroke="#8b5cf6" stroke-width="2.5"/>
  <circle cx="164" cy="50" r="4.5" fill="#8b5cf6"/>
  <line x1="164" y1="50" x2="164" y2="220" stroke="#8b5cf6" stroke-width="1.2" stroke-dasharray="3,3"/>
  <text x="155" y="235" font-size="10" fill="#7c3aed" font-weight="bold">34</text>
  <text x="72" y="92" font-size="11" fill="#7c3aed" font-weight="bold">ジエチルエーテル</text>
  <text x="82" y="106" font-size="10" fill="#7c3aed">(沸点 34℃)</text>
  <!-- 乙醇曲线 (78℃=1.0 => x=291.2, y=50) -->
  <path d="M 65 216 Q 210 200 291 50 L 300 32" fill="none" stroke="#0284c7" stroke-width="2.5"/>
  <circle cx="291" cy="50" r="4.5" fill="#0284c7"/>
  <line x1="291" y1="50" x2="291" y2="220" stroke="#0284c7" stroke-width="1.2" stroke-dasharray="3,3"/>
  <text x="275" y="235" font-size="10" fill="#0284c7" font-weight="bold">78</text>
  <text x="188" y="130" font-size="11" fill="#0284c7" font-weight="bold">エタノール</text>
  <text x="188" y="144" font-size="10" fill="#0284c7">(沸点 78℃)</text>
  <!-- 水曲线 (100℃=1.0 => x=355, y=50) -->
  <path d="M 65 219 Q 275 215 355 50 L 363 32" fill="none" stroke="#16a34a" stroke-width="2.5"/>
  <circle cx="355" cy="50" r="4.5" fill="#16a34a"/>
  <line x1="355" y1="50" x2="355" y2="220" stroke="#16a34a" stroke-width="1.2" stroke-dasharray="3,3"/>
  <text x="330" y="155" font-size="11" fill="#15803d" font-weight="bold">水</text>
  <text x="315" y="169" font-size="10" fill="#15803d">(沸点 100℃)</text>
  <!-- 结论注释 -->
  <rect x="75" y="14" width="215" height="24" rx="4" fill="#fef3c7" stroke="#f59e0b" stroke-width="1"/>
  <text x="82" y="30" font-size="10" fill="#92400e" font-weight="bold">分子间力越弱 → 越易挥发 → 蒸气压越高、沸点越低</text>
</svg>

---

#### 【例题 1】（原书 P.31 / PDF 第 32 页）密闭容器内蒸气压与液态水质量的判别计算

**【原题重现与翻译】**
> $10\text{ L}$ の容器に窒素 $0.40\text{ mol}$ と液体の水 $3.6\text{ g}$ を入れて密閉し、$57^\circ\text{C}$ まで温度を上げた。容器内の圧力と液体の水の質量を求めよ。液体の体積と液体に対する気体の溶解は無視できるものとし、気体定数を $R = 8.3 \times 10^3\text{ Pa}\cdot\text{L/(mol}\cdot\text{K)}$、$57^\circ\text{C}$ における飽和水蒸気圧を $2.0 \times 10^4\text{ Pa}$ とする。$\text{H}_2\text{O} = 18$
>
> **中文翻译**：向 $10\text{ L}$ 容器中加入 $0.40\text{ mol}$ 氮气和 $3.6\text{ g}$ 液态水并密闭，升温至 $57^\circ\text{C}$。求容器内的总压强和剩余液态水的质量。忽略液体体积及气体在液体中的溶解，设气体常数 $R = 8.3 \times 10^3\text{ Pa}\cdot\text{L/(mol}\cdot\text{K)}$，$57^\circ\text{C}$ 时饱和水蒸气压为 $2.0 \times 10^4\text{ Pa}$。

**【考点定位】**
道尔顿分压定律 + 理想气体状态方程 $PV = nRT$ + 液体是否残留的“假想全气化判别法”。

**【分步标准解答】**
1. **换算绝对温度**：
   $$T = 273 + 57 = 330\text{ K}$$
2. **求氮气分压 $P_{\text{N}_2}$**：
   $$P_{\text{N}_2} \times 10 = 0.40 \times 8.3 \times 10^3 \times 330$$
   $$P_{\text{N}_2} = 1.0956 \times 10^5\text{ Pa} \approx 1.10 \times 10^5\text{ Pa}$$
3. **判别水是否全部气化**（假设 $3.6\text{ g}$ 水全部为水蒸气，求理论分压 $P_{\text{H}_2\text{O}}$）：
   $$n_{\text{总水}} = \frac{3.6}{18} = 0.20\text{ mol}$$
   $$P_{\text{H}_2\text{O}} \times 10 = 0.20 \times 8.3 \times 10^3 \times 330 \implies P_{\text{H}_2\text{O}} = 5.478 \times 10^4\text{ Pa} \approx 5.48 \times 10^4\text{ Pa}$$
   - **判别**：因为 $P_{\text{H}_2\text{O}} = 5.48 \times 10^4\text{ Pa} \gt P_0 = 2.0 \times 10^4\text{ Pa}$，说明容器内**仍有液态水残留**，实际水蒸气分压被封顶为饱和水蒸气压 **$2.0 \times 10^4\text{ Pa}$**。
4. **求容器内总压 $P_{\text{全}}$**：
   $$P_{\text{全}} = P_{\text{N}_2} + P_0 = 1.10 \times 10^5 + 2.0 \times 10^4 = 1.30 \times 10^5\text{ Pa} \approx \mathbf{1.3 \times 10^5\text{ Pa}}$$
5. **求剩余液态水的质量（⚠️ 补全原书漏印解答）**：
   - 在恒温恒容下，水蒸气的物质的量（质量）与压强成正比：
     - 气态水的质量占比为 $\frac{P_0}{P_{\text{H}_2\text{O}}} = \frac{2.0 \times 10^4}{5.478 \times 10^4}$
     - 液态水的质量占比为 $\frac{P_{\text{H}_2\text{O}} - P_0}{P_{\text{H}_2\text{O}}} = \frac{5.478 - 2.0}{5.478}$
   - 因此剩余液态水质量为：
     $$m_{\text{液}} = 3.6\text{ g} \times \frac{5.478 - 2.0}{5.478} = 3.6 \times \frac{3.478}{5.478} \approx 2.286\text{ g} \approx \mathbf{2.3\text{ g}}$$
   - （*法二验算*：先由 $2.0\times 10^4 \times 10 = n_{\text{气}} \times 8.3\times 10^3 \times 330$ 得 $n_{\text{气}} \approx 0.0730\text{ mol}$，气态水质量 $0.0730 \times 18 \approx 1.31\text{ g}$，故液态水 $= 3.6 - 1.31 = 2.29 \approx \mathbf{2.3\text{ g}}$。）

> 💡 **讲师批注**：本题是 EJU 物理化学最高频母题！记住口诀：**“先算全气化，再比饱和压；大了就封顶，差值算液化”**。另外中间步骤多保留一位有效数字（如 $1.10\times 10^5$ 和 $5.48\times 10^4$），最后结果再统一四舍五入至 2 位有效数字。

**【最终答案】**
容器内压强：**$1.3 \times 10^5\text{ Pa}$**；剩余液态水的质量：**$2.3\text{ g}$**

---

### 【知识点 9】水上置換法で捕集した気体の圧力（排水法收集气体的压强）（原书 P.32）

#### 图解辅助（SVG 2：排水法集气时液面位置与内部压强的关系）
<svg viewBox="0 0 420 260" xmlns="http://www.w3.org/2000/svg" style="background:#fafafa;border:1px solid #e2e8f0;border-radius:8px;">
  <!-- 水槽 -->
  <rect x="25" y="135" width="370" height="90" fill="#dbeafe" stroke="none"/>
  <polyline points="25,115 25,225 395,225 395,115" fill="none" stroke="#334155" stroke-width="2.2"/>
  <line x1="25" y1="135" x2="395" y2="135" stroke="#2563eb" stroke-width="1.5"/>
  <!-- 左管：内低外高 (×) -->
  <rect x="65" y="55" width="44" height="125" fill="#ffffff" stroke="#334155" stroke-width="2"/>
  <rect x="66" y="155" width="42" height="25" fill="#bfdbfe"/>
  <line x1="65" y1="155" x2="109" y2="155" stroke="#2563eb" stroke-width="1.5"/>
  <text x="80" y="42" font-size="18" fill="#dc2626" font-weight="bold">×</text>
  <text x="48" y="245" font-size="10" fill="#dc2626">P内 ＞ 大気圧</text>
  <!-- 中管：液面一致 (○) -->
  <rect x="180" y="55" width="44" height="125" fill="#ffffff" stroke="#16a34a" stroke-width="2.4"/>
  <rect x="181" y="135" width="42" height="45" fill="#bfdbfe"/>
  <line x1="180" y1="135" x2="224" y2="135" stroke="#16a34a" stroke-width="2"/>
  <text x="193" y="42" font-size="18" fill="#16a34a" font-weight="bold">○</text>
  <!-- 内部气体压强箭头 -->
  <line x1="202" y1="95" x2="202" y2="128" stroke="#16a34a" stroke-width="2.2"/>
  <polygon points="202,132 197,124 207,124" fill="#16a34a"/>
  <text x="185" y="80" font-size="10" fill="#15803d" font-weight="bold">P気体+P水</text>
  <!-- 外部大气压箭头 -->
  <line x1="252" y1="95" x2="252" y2="128" stroke="#0284c7" stroke-width="2.2"/>
  <polygon points="252,132 247,124 257,124" fill="#0284c7"/>
  <text x="236" y="88" font-size="10" fill="#0369a1" font-weight="bold">大気圧</text>
  <text x="148" y="245" font-size="10" fill="#15803d" font-weight="bold">P内 ＝ 大気圧（正确读数）</text>
  <!-- 右管：内高外低 (×) -->
  <rect x="305" y="55" width="44" height="125" fill="#ffffff" stroke="#334155" stroke-width="2"/>
  <rect x="306" y="110" width="42" height="70" fill="#bfdbfe"/>
  <line x1="305" y1="110" x2="349" y2="110" stroke="#2563eb" stroke-width="1.5"/>
  <text x="320" y="42" font-size="18" fill="#dc2626" font-weight="bold">×</text>
  <text x="292" y="245" font-size="10" fill="#dc2626">P内 ＜ 大気圧</text>
  <!-- 顶部公式 -->
  <rect x="65" y="8" width="290" height="22" rx="4" fill="#eff6ff" stroke="#3b82f6"/>
  <text x="76" y="23" font-size="11" fill="#1d4ed8" font-weight="bold">P(捕集気体) ＝ 大気圧 － 飽和水蒸気圧</text>
</svg>

#### 【例题 2】（原书 P.32 / PDF 第 33 页）排水法收集氧气的质量计算

**【原题重现与翻译】**
> $27^\circ\text{C}$、大気圧 $1.0 \times 10^5\text{ Pa}$ において、発生した酸素を水上置換法で捕集し、水面を一致させてから体積を測定したところ、$200\text{ mL}$ であった。得られた酸素の質量を求めよ。酸素の水への溶解は無視できるものとし、気体定数を $R = 8.3 \times 10^3\text{ Pa}\cdot\text{L/(mol}\cdot\text{K)}$、$27^\circ\text{C}$ における飽和水蒸気圧を $3.0 \times 10^3\text{ Pa}$ とする。$\text{O}_2 = 32$
>
> **中文翻译**：在 $27^\circ\text{C}$、大气压 $1.0 \times 10^5\text{ Pa}$ 下，用排水法收集产生的氧气，使管内外水面齐平后测得体积为 $200\text{ mL}$。求得到的氧气质量。忽略氧气在水中的溶解，$27^\circ\text{C}$ 时饱和水蒸气压为 $3.0 \times 10^3\text{ Pa}$。

**【考点定位】**
排水集气法的分压扣除（$P_{\text{O}_2} = P_{\text{大气}} - P_{\text{水}}$）+ 状态方程求质量。

**【分步标准解答】**
1. **求氧气的真实分压**：
   - 水面齐平说明管内总压 $=$ 大气压，而管内气体是“氧气 $+$ 饱和水蒸气”的混合气体，故：
     $$P_{\text{O}_2} = 1.0 \times 10^5 - 3.0 \times 10^3 = 9.7 \times 10^4\text{ Pa}$$
2. **统一单位并代入状态方程 $PV = \frac{w}{M}RT$**：
   - 体积：$V = 200\text{ mL} = 0.20\text{ L}$；温度：$T = 273 + 27 = 300\text{ K}$。
   - 设氧气质量为 $w\text{ [g]}$：
     $$9.7 \times 10^4\text{ Pa} \times 0.20\text{ L} = \frac{w\text{ [g]}}{32\text{ g/mol}} \times 8.3 \times 10^3\text{ Pa}\cdot\text{L/(mol}\cdot\text{K)} \times 300\text{ K}$$
   - 解得：
     $$w = \frac{9.7 \times 10^4 \times 0.20 \times 32}{8.3 \times 10^3 \times 300} = \frac{620800}{2490000} \approx 0.2493\text{ g} \approx \mathbf{0.25\text{ g}}$$

> 💡 **讲师批注**：只要看到题目出现 **「水上置換法」**，大脑立刻响起警报：**一定要减掉该温度下的饱合水蒸气压**！绝对不要直接拿大气压 $1.0\times 10^5\text{ Pa}$ 去代！

**【最终答案】**
**$0.25\text{ g}$**

---

### 【知识点 10】固体の溶解度（固体的溶解度）（原书 P.33–35）

#### 图解辅助（SVG 3：$\text{KNO}_3$、$\text{CuSO}_4$、$\text{NaCl}$ 溶解度曲线与冷却析出示意）
<svg viewBox="0 0 420 260" xmlns="http://www.w3.org/2000/svg" style="background:#fafafa;border:1px solid #e2e8f0;border-radius:8px;">
  <!-- 坐标轴 -->
  <line x1="65" y1="220" x2="385" y2="220" stroke="#334155" stroke-width="1.8"/>
  <line x1="65" y1="220" x2="65" y2="20" stroke="#334155" stroke-width="1.8"/>
  <polygon points="385,220 377,216 377,224" fill="#334155"/>
  <polygon points="65,20 61,28 69,28" fill="#334155"/>
  <!-- 纵轴 (0~160 => 220~28, 每20g=24px) -->
  <text x="42" y="200" font-size="10" fill="#475569">20</text>
  <text x="42" y="176" font-size="10" fill="#475569">40</text>
  <text x="42" y="152" font-size="10" fill="#475569">60</text>
  <text x="42" y="128" font-size="10" fill="#475569">80</text>
  <text x="36" y="104" font-size="10" fill="#475569">100</text>
  <text x="36" y="80" font-size="10" fill="#475569">120</text>
  <text x="36" y="56" font-size="10" fill="#475569">140</text>
  <text x="36" y="32" font-size="10" fill="#475569">160</text>
  <text x="4" y="118" font-size="10" fill="#1e293b" font-weight="bold">溶解度</text>
  <text x="2" y="132" font-size="9" fill="#475569">[g/100g水]</text>
  <!-- 横轴 (0~100℃ => 65~365, 每20℃=60px) -->
  <text x="120" y="236" font-size="10" fill="#475569">20</text>
  <text x="180" y="236" font-size="10" fill="#475569">40</text>
  <text x="240" y="236" font-size="10" fill="#475569">60</text>
  <text x="300" y="236" font-size="10" fill="#475569">80</text>
  <text x="356" y="236" font-size="10" fill="#475569">100</text>
  <text x="200" y="253" font-size="11" fill="#1e293b" font-weight="bold">温度 [℃]</text>
  <!-- KNO3 曲线 (0℃:13, 20℃:32, 40℃:64, 60℃:109, 80℃:169) -->
  <path d="M 65 204 Q 145 182 185 143 T 245 89 L 295 22" fill="none" stroke="#ef4444" stroke-width="2.5"/>
  <text x="108" y="42" font-size="11" fill="#dc2626" font-weight="bold">硝酸カリウム KNO₃</text>
  <!-- 冷却量与析出量示意 (60℃ -> 40℃) -->
  <circle cx="245" cy="89" r="4" fill="#dc2626"/>
  <circle cx="185" cy="143" r="4" fill="#dc2626"/>
  <line x1="245" y1="89" x2="185" y2="89" stroke="#f59e0b" stroke-width="1.8" stroke-dasharray="4,2"/>
  <line x1="185" y1="89" x2="185" y2="143" stroke="#16a34a" stroke-width="2"/>
  <polygon points="185,140 181,132 189,132" fill="#16a34a"/>
  <text x="198" y="83" font-size="10" fill="#d97706" font-weight="bold">← 冷却量</text>
  <text x="142" y="120" font-size="10" fill="#15803d" font-weight="bold">析出量 ↓</text>
  <!-- CuSO4 曲线 (0℃:14, 20℃:20, 40℃:29, 60℃:40, 80℃:55, 100℃:75) -->
  <path d="M 65 203 Q 185 190 245 172 T 365 130" fill="none" stroke="#0284c7" stroke-width="2.4"/>
  <text x="275" y="142" font-size="11" fill="#0284c7" font-weight="bold">硫酸銅 CuSO₄</text>
  <!-- NaCl 曲线 (几乎水平 35.7 -> 39.2) -->
  <line x1="65" y1="177" x2="365" y2="173" stroke="#64748b" stroke-width="2.2"/>
  <text x="270" y="192" font-size="11" fill="#475569" font-weight="bold">塩化ナトリウム NaCl</text>
</svg>

#### 【例题 3】（原书 P.34–35 / PDF 第 35–36 页）硝酸钾溶解度三大经典题型

**【原题重现与翻译】**
> $\text{KNO}_3$ の溶解度は、$20^\circ\text{C}$ で $32\text{ g/100g 水}$、$40^\circ\text{C}$ で $64\text{ g/100g 水}$ である。以下の問いに有効数字 2 桁で答えよ。
> (1) $40^\circ\text{C}$ の $\text{KNO}_3$ 飽和水溶液 $200\text{ g}$ を $20^\circ\text{C}$ に冷却したときに析出する $\text{KNO}_3$ の質量は何 $\text{g}$ か。
> (2) 質量パーセント濃度 $10\%$ の $\text{KNO}_3$ 水溶液 $200\text{ g}$ を $20^\circ\text{C}$ で飽和溶液にするために必要な $\text{KNO}_3$ は何 $\text{g}$ か。
> (3) $40^\circ\text{C}$ の $\text{KNO}_3$ 飽和水溶液 $200\text{ g}$ から水を $20\text{ g}$ 蒸発させたときに析出する結晶は何 $\text{g}$ か。
>
> **中文翻译**：$\text{KNO}_3$ 的溶解度在 $20^\circ\text{C}$ 时为 $32\text{ g/100g 水}$，在 $40^\circ\text{C}$ 时为 $64\text{ g/100g 水}$。保留 2 位有效数字回答以下问题：
> (1) 将 $40^\circ\text{C}$ 的 $\text{KNO}_3$ 饱和水溶液 $200\text{ g}$ 冷却至 $20^\circ\text{C}$，析出多少 $\text{g}$ $\text{KNO}_3$？
> (2) 使质量分数 $10\%$ 的 $\text{KNO}_3$ 水溶液 $200\text{ g}$ 在 $20^\circ\text{C}$ 下达到饱和，需再加入多少 $\text{g}$ $\text{KNO}_3$？
> (3) 将 $40^\circ\text{C}$ 的 $\text{KNO}_3$ 饱和水溶液 $200\text{ g}$ 恒温蒸发掉 $20\text{ g}$ 水，析出多少 $\text{g}$ 晶体？

**【考点定位】**
饱和溶液比例式 $\frac{\text{溶质}}{\text{溶液}} = \frac{S}{100+S}$ 与 $\frac{\text{溶质}}{\text{溶剂}} = \frac{S}{100}$ 的灵活运用（冷却析出、补加溶质、恒温蒸发）。

**【分步标准解答】**
- **(1) 冷却析出**（设析出 $\text{KNO}_3$ 为 $x\text{ [g]}$）：
  - **常规法（溶质 / 溶液）**：原 $40^\circ\text{C}$ 饱和液中含溶质 $200 \times \frac{64}{100+64}$；析出 $x\text{ g}$ 后剩余溶液为 $200 - x$，在 $20^\circ\text{C}$ 饱和：
    $$\frac{200 \times \frac{64}{100+64} - x}{200 - x} = \frac{32}{100+32} \implies x \approx \mathbf{39\text{ g}}$$
  - **秒杀别解（析出量 / 原饱和溶液质量）**：每 $100+64=164\text{ g}$ 饱和溶液从 $40^\circ\text{C}$ 降到 $20^\circ\text{C}$ 会析出 $64 - 32 = 32\text{ g}$ 溶质，故：
    $$\frac{x}{200} = \frac{64 - 32}{100 + 64} = \frac{32}{164} \implies x = \frac{6400}{164} \approx 39.02 \approx \mathbf{39\text{ g}}$$

- **(2) 补加溶质达饱和**（设需加 $\text{KNO}_3$ 为 $x\text{ [g]}$）：
  - 原溶液含溶质：$200 \times \frac{10}{100} = 20\text{ g}$，含溶剂水：$200 \times \frac{90}{100} = 180\text{ g}$。
  - **利用溶质 / 溶剂（最简洁！）**：
    $$\frac{20 + x}{180} = \frac{32}{100} \implies 20 + x = 57.6 \implies x = 37.6 \approx \mathbf{38\text{ g}}$$

- **(3) 恒温蒸发溶剂析出**（设析出 $\text{KNO}_3$ 为 $x\text{ [g]}$）：
  - **秒杀别解（抓住本质！）**：原本就已经是 $40^\circ\text{C}$ 饱和溶液，恒温蒸干 $20\text{ g}$ 水，那么原本溶解在这 $20\text{ g}$ 水里的 $\text{KNO}_3$ 必然全部析出！
    $$\frac{x}{20} = \frac{64}{100} \implies x = 12.8 \approx \mathbf{13\text{ g}}$$
  - （常规法 $\frac{200\times \frac{64}{164} - x}{200 - 20 - x} = \frac{64}{164}$ 同样解得 $x = 12.8 \approx 13\text{ g}$。）

> 💡 **讲师批注**：无水物溶解度计算只需记住两个“秒杀技巧”：① **降温析出**直接用 $\frac{x}{m_{\text{原液}}} = \frac{S_1 - S_2}{100 + S_1}$；② **恒温蒸发**直接用 $\frac{x}{m_{\text{蒸发水}}} = \frac{S}{100}$！省下 80% 计算时间！

**【最终答案】**
(1) **$39\text{ g}$**　(2) **$38\text{ g}$**　(3) **$13\text{ g}$**

---

### 【知识点 12】水和物の溶解度（水合物的溶解度）（原书 P.35）

> *注：原书节号由 10 直接跳至 12（缺失第 11 节编号）。*

#### 【例题 4】（原书 P.35 / PDF 第 36 页）五水合硫酸铜溶解度三连问（⚠️ 补全原书漏印的 (2)(3) 解答）

**【原题重现与翻译】**
> 硫酸銅（II）$\text{CuSO}_4$ の溶解度は、$20^\circ\text{C}$ で $20\text{ g/100g 水}$、$60^\circ\text{C}$ で $40\text{ g/100g 水}$ である。以下の問いに整数値で答えよ。$\text{CuSO}_4 = 160,\ \text{H}_2\text{O} = 18$
> (1) 硫酸銅（II）五水和物 $\text{CuSO}_4\cdot 5\text{H}_2\text{O}$ は、$60^\circ\text{C}$ で水 $200\text{ g}$ に何 $\text{g}$ まで溶けるか。
> (2) 硫酸銅（II）五水和物 $\text{CuSO}_4\cdot 5\text{H}_2\text{O}$ $200\text{ g}$ を全て溶かして $60^\circ\text{C}$ の飽和水溶液を作るために必要な水は何 $\text{g}$ か。
> (3) $60^\circ\text{C}$ の硫酸銅（II）$\text{CuSO}_4$ 飽和水溶液 $200\text{ g}$ を $20^\circ\text{C}$ にまで冷却したとき、何 $\text{g}$ の硫酸銅（II）五水和物 $\text{CuSO}_4\cdot 5\text{H}_2\text{O}$ の結晶が析出するか。
>
> **中文翻译**：无水 $\text{CuSO}_4$ 的溶解度在 $20^\circ\text{C}$ 为 $20\text{ g/100g 水}$，$60^\circ\text{C}$ 为 $40\text{ g/100g 水}$。用整数值回答：
> (1) $60^\circ\text{C}$ 时，$200\text{ g}$ 水中最多能溶解多少 $\text{g}$ $\text{CuSO}_4\cdot 5\text{H}_2\text{O}$？
> (2) 将 $200\text{ g}$ $\text{CuSO}_4\cdot 5\text{H}_2\text{O}$ 全部溶解配成 $60^\circ\text{C}$ 饱和水溶液，需加水多少 $\text{g}$？
> (3) 将 $60^\circ\text{C}$ 的 $\text{CuSO}_4$ 饱和水溶液 $200\text{ g}$ 冷却至 $20^\circ\text{C}$，析出多少 $\text{g}$ $\text{CuSO}_4\cdot 5\text{H}_2\text{O}$ 晶体？

**【考点定位】**
结晶水合物的溶解与析出计算（核心：把 $\text{CuSO}_4\cdot 5\text{H}_2\text{O}$ 拆分为 $\frac{160}{250}$ 的无水溶质和 $\frac{90}{250}$ 的结晶水！）。

**【分步标准解答】**
首先记住黄金拆分比例：$\text{CuSO}_4\cdot 5\text{H}_2\text{O}$ 的式量 $= 160 + 5 \times 18 = \mathbf{250}$。
因此任意 $x\text{ [g]}$ 的 $\text{CuSO}_4\cdot 5\text{H}_2\text{O}$ 中：
- 含无水溶质 $\text{CuSO}_4$：$\frac{160}{250}x = \frac{16}{25}x\text{ [g]}$
- 含结晶水 $5\text{H}_2\text{O}$：$\frac{90}{250}x = \frac{9}{25}x\text{ [g]}$

- **(1) 求最大溶解量**（设溶解的 $\text{CuSO}_4\cdot 5\text{H}_2\text{O}$ 为 $x\text{ [g]}$）：
  - **溶质 / 溶液法**：溶质为 $\frac{160}{250}x$，溶液总质量为 $200 + x$：
    $$\frac{\frac{160}{250}x}{200 + x} = \frac{40}{100 + 40} = \frac{2}{7}$$
    $$7 \times \frac{16}{25}x = 2(200 + x) \implies 4.48x = 400 + 2x \implies 2.48x = 400 \implies x \approx 161.29 \approx \mathbf{161\text{ g}}$$
  - （*别解：溶质 / 溶剂法* $\frac{\frac{160}{250}x}{200 + \frac{90}{250}x} = \frac{40}{100}$，解得同样为 $161\text{ g}$。）

- **(2) 求配制饱和液所需加水量**（⚠️ 原书漏印，设另需加水 $y\text{ [g]}$）：
  - $200\text{ g}$ $\text{CuSO}_4\cdot 5\text{H}_2\text{O}$ 中：
    - 无水溶质 $\text{CuSO}_4$ 质量 $= 200 \times \frac{160}{250} = 128\text{ g}$
    - 自带结晶水质量 $= 200 \times \frac{90}{250} = 72\text{ g}$
  - $60^\circ\text{C}$ 溶解度为 $40\text{ g/100g 水}$，总溶剂水质量为 $y + 72$：
    $$\frac{128}{y + 72} = \frac{40}{100} \implies y + 72 = 320 \implies y = \mathbf{248\text{ g}}$$

- **(3) 冷却析出五水合硫酸铜晶体质量**（⚠️ 原书漏印，设析出 $\text{CuSO}_4\cdot 5\text{H}_2\text{O}$ 为 $z\text{ [g]}$）：
  - 原 $60^\circ\text{C}$ 饱和液 $200\text{ g}$ 中含无水 $\text{CuSO}_4$ 质量 $= 200 \times \frac{40}{100+40} = \frac{400}{7}\text{ g}$。
  - 析出 $z\text{ g}$ 晶体后，溶液中剩余无水溶质 $= \frac{400}{7} - \frac{160}{250}z$，剩余溶液总质量 $= 200 - z$，在 $20^\circ\text{C}$（$S=20$）饱和：
    $$\frac{\frac{400}{7} - \frac{160}{250}z}{200 - z} = \frac{20}{100 + 20} = \frac{1}{6}$$
    $$6 \times \frac{400}{7} - 6 \times \frac{16}{25}z = 200 - z \implies \frac{2400}{7} - 200 = \left(\frac{96}{25} - 1\right)z$$
    $$\frac{1000}{7} = \frac{71}{25}z \implies z = \frac{25000}{497} \approx 50.30 \approx \mathbf{50\text{ g}}$$

> 💡 **讲师批注**：水合物题千万别用“秒杀差值公式” $\frac{S_1 - S_2}{100+S_1}$，因为析出晶体时**水也变少了**！老老实实列 $\frac{\text{剩余无水溶质}}{\text{剩余溶液总质量}} = \frac{S}{100+S}$，把晶体拆成 $\frac{160}{250}z$（溶质）和整体 $-z$（溶液），百发百中绝不出错！

**【最终答案】**
(1) **$161\text{ g}$**　(2) **$248\text{ g}$**　(3) **$50\text{ g}$**

---

### 【知识点 13】気体の溶解度とヘンリーの法則（气体溶解度与亨利定律）（原书 P.36–37）

#### 图解辅助（SVG 4：亨利定律加压溶解模型）
<svg viewBox="0 0 420 260" xmlns="http://www.w3.org/2000/svg" style="background:#fafafa;border:1px solid #e2e8f0;border-radius:8px;">
  <!-- 顶部标题 -->
  <rect x="45" y="10" width="330" height="24" rx="4" fill="#fef3c7" stroke="#f59e0b"/>
  <text x="58" y="26" font-size="11" fill="#92400e" font-weight="bold">恒温下：压强 P 变为 k 倍 → 溶解的 mol/质量 变 k 倍，同压体积不变！</text>
  <!-- 容器1: P -->
  <g transform="translate(30,50)">
    <text x="38" y="12" font-size="12" fill="#0284c7" font-weight="bold">P</text>
    <line x1="42" y1="16" x2="42" y2="34" stroke="#0284c7" stroke-width="2.5"/>
    <polygon points="42,38 37,30 47,30" fill="#0284c7"/>
    <rect x="10" y="38" width="65" height="10" fill="#94a3b8"/>
    <polyline points="10,25 10,165 75,165 75,25" fill="none" stroke="#334155" stroke-width="2"/>
    <rect x="11" y="125" width="63" height="39" fill="#bae6fd"/>
    <!-- 气体分子 -->
    <circle cx="25" cy="65" r="3.5" fill="#475569"/>
    <circle cx="55" cy="70" r="3.5" fill="#475569"/>
    <circle cx="38" cy="90" r="3.5" fill="#475569"/>
    <circle cx="22" cy="110" r="3.5" fill="#475569"/>
    <circle cx="60" cy="108" r="3.5" fill="#475569"/>
    <!-- 溶解的1个分子 -->
    <circle cx="42" cy="145" r="4" fill="#dc2626"/>
    <text x="15" y="185" font-size="10" fill="#1e293b">溶解量: 1 mol</text>
    <text x="8" y="199" font-size="10" fill="#15803d">当前压体积: V</text>
  </g>
  <!-- 容器2: 2P -->
  <g transform="translate(165,50)">
    <text x="35" y="12" font-size="12" fill="#0284c7" font-weight="bold">2P</text>
    <line x1="42" y1="16" x2="42" y2="68" stroke="#0284c7" stroke-width="2.5"/>
    <polygon points="42,72 37,64 47,64" fill="#0284c7"/>
    <rect x="10" y="72" width="65" height="10" fill="#94a3b8"/>
    <polyline points="10,25 10,165 75,165 75,25" fill="none" stroke="#334155" stroke-width="2"/>
    <rect x="11" y="125" width="63" height="39" fill="#bae6fd"/>
    <circle cx="22" cy="95" r="3.5" fill="#475569"/>
    <circle cx="45" cy="92" r="3.5" fill="#475569"/>
    <circle cx="63" cy="98" r="3.5" fill="#475569"/>
    <circle cx="30" cy="112" r="3.5" fill="#475569"/>
    <circle cx="55" cy="114" r="3.5" fill="#475569"/>
    <!-- 溶解的2个分子 -->
    <circle cx="30" cy="145" r="4" fill="#dc2626"/>
    <circle cx="54" cy="145" r="4" fill="#dc2626"/>
    <text x="15" y="185" font-size="10" fill="#1e293b">溶解量: 2 mol</text>
    <text x="8" y="199" font-size="10" fill="#15803d">当前压体积: V</text>
  </g>
  <!-- 容器3: 3P -->
  <g transform="translate(300,50)">
    <text x="35" y="12" font-size="12" fill="#0284c7" font-weight="bold">3P</text>
    <line x1="42" y1="16" x2="42" y2="85" stroke="#0284c7" stroke-width="2.5"/>
    <polygon points="42,89 37,81 47,81" fill="#0284c7"/>
    <rect x="10" y="89" width="65" height="10" fill="#94a3b8"/>
    <polyline points="10,25 10,165 75,165 75,25" fill="none" stroke="#334155" stroke-width="2"/>
    <rect x="11" y="125" width="63" height="39" fill="#bae6fd"/>
    <circle cx="20" cy="108" r="3.5" fill="#475569"/>
    <circle cx="36" cy="112" r="3.5" fill="#475569"/>
    <circle cx="52" cy="107" r="3.5" fill="#475569"/>
    <circle cx="65" cy="114" r="3.5" fill="#475569"/>
    <!-- 溶解的3个分子 -->
    <circle cx="22" cy="145" r="4" fill="#dc2626"/>
    <circle cx="42" cy="145" r="4" fill="#dc2626"/>
    <circle cx="62" cy="145" r="4" fill="#dc2626"/>
    <text x="15" y="185" font-size="10" fill="#1e293b">溶解量: 3 mol</text>
    <text x="8" y="199" font-size="10" fill="#15803d">当前压体积: V</text>
  </g>
</svg>

#### 【例题 5】（原书 P.37 / PDF 第 38 页）混合气体的亨利定律计算

**【原题重现与翻译】**
> 標準状態（$0^\circ\text{C},\ 1.0 \times 10^5\text{ Pa}$）において、窒素、酸素は水 $1\text{ L}$ にそれぞれ $24\text{ mL}$、$48\text{ mL}$ 溶ける。ここで、窒素と酸素の物質量比が $4:1$ である混合気体を $0^\circ\text{C},\ 1.0 \times 10^5\text{ Pa}$ に保って $10\text{ L}$ の水と接触させた。$\text{N}_2 = 28,\ \text{O}_2 = 32$
> (1) 水に溶解している窒素と酸素のこの条件下における体積 $[\text{mL}]$ を求めよ。
> ~~(2) 水に溶解している窒素と酸素の標準状態に換算した体積 $[\text{mL}]$ を求めよ。~~（*原书画删除线，此处一并精讲*）
> (3) 水に溶解している窒素と酸素の質量を求めよ。
>
> **中文翻译**：在标准状态（$0^\circ\text{C},\ 1.0 \times 10^5\text{ Pa}$）下，氮气、氧气在 $1\text{ L}$ 水中分别溶解 $24\text{ mL}$、$48\text{ mL}$。现将物质的量之比为 $4:1$ 的氮气与氧气混合气体保持在 $0^\circ\text{C},\ 1.0 \times 10^5\text{ Pa}$ 下与 $10\text{ L}$ 水接触。求：
> (1) 溶于水的氮气和氧气在各自当前分压条件下的体积 $[\text{mL}]$；
> (2) 换算为标准状态的体积 $[\text{mL}]$；
> (3) 溶于水的氮气和氧气的质量。

**【考点定位】**
亨利定律的混合气体分压应用 + “当前条件下体积 vs 标准状态体积”的经典区分。

**【分步标准解答】**
首先求混合气体中各组分的分压：
- $P_{\text{N}_2} = 1.0 \times 10^5 \times \frac{4}{4+1} = 8.0 \times 10^4\text{ Pa}$
- $P_{\text{O}_2} = 1.0 \times 10^5 \times \frac{1}{4+1} = 2.0 \times 10^4\text{ Pa}$

- **(1) 当前条件（各自所处分压）下的体积**：
  - 溶解气体在**该分压下测定**的体积与压强无关，**只与水的体积成正比**（$1\text{ L} \to 10\text{ L}$）：
    - 氮气体积：$24\text{ mL} \times 10 = \mathbf{2.4 \times 10^2\text{ mL}}$
    - 氧气体积：$48\text{ mL} \times 10 = \mathbf{4.8 \times 10^2\text{ mL}}$

- **(2) 换算为标准状态（$0^\circ\text{C}, 1.0\times 10^5\text{ Pa}$）的体积（拓展补全）**：
  - 标准状态体积与**分压**和**水的体积**均成正比：
    - 氮气：$24\text{ mL} \times \frac{8.0 \times 10^4}{1.0 \times 10^5} \times \frac{10}{1} = 192\text{ mL} \approx \mathbf{1.9 \times 10^2\text{ mL}}$
    - 氧气：$48\text{ mL} \times \frac{2.0 \times 10^4}{1.0 \times 10^5} \times \frac{10}{1} = \mathbf{96\text{ mL}}$

- **(3) 溶解的氮气和氧气的质量**：
  - 溶解气体的质量与**分压**和**水的体积**均成正比（$1\text{ mol}$ 标况体积 $22.4\text{ L}$）：
    - 氮气质量：
      $$\frac{24 \times 10^{-3}\text{ L}}{22.4\text{ L/mol}} \times 28\text{ g/mol} \times \frac{8.0 \times 10^4\text{ Pa}}{1.0 \times 10^5\text{ Pa}} \times \frac{10\text{ L}}{1\text{ L}} = \mathbf{0.24\text{ g}}$$
    - 氧气质量：
      $$\frac{48 \times 10^{-3}\text{ L}}{22.4\text{ L/mol}} \times 32\text{ g/mol} \times \frac{2.0 \times 10^4\text{ Pa}}{1.0 \times 10^5\text{ Pa}} \times \frac{10\text{ L}}{1\text{ L}} \approx 0.137 \approx \mathbf{0.14\text{ g}}$$

> 💡 **讲师批注**：第 (1) 问是日本高考最爱挖的“文字坑”！看到 **「この条件下における体積」**（在此条件下的体积），直接无视压强，只乘水的倍数；看到 **「標準状態に換算した体積」** 或 **「質量 / 物質量」**，必须乘以 $\frac{P_{\text{分}}}{P_{\text{标}}} \times \frac{V_{\text{水}}}{V_{\text{标水}}}$！

**【最终答案】**
(1) $\text{N}_2$: **$2.4 \times 10^2\text{ mL}$**，$\text{O}_2$: **$4.8 \times 10^2\text{ mL}$**
(2)（拓展）$\text{N}_2$: **$1.9 \times 10^2\text{ mL}$**，$\text{O}_2$: **$96\text{ mL}$**
(3) $\text{N}_2$: **$0.24\text{ g}$**，$\text{O}_2$: **$0.14\text{ g}$**

---

#### 【真题演练・問 10】（原书 P.37 / PDF 第 38 页，EJU 历年真题）

**【原题重现与翻译】**
> 問 10　温度 $20^\circ\text{C}$、圧力 $1.0 \times 10^5\text{ Pa}$ において、酸素（oxygen）は水 $1.0\text{ L}$ あたり $1.4 \times 10^{-3}\text{ mol}$ 溶解する（dissolve）。$20^\circ\text{C}$、$5.0 \times 10^5\text{ Pa}$ で水 $2.0\text{ L}$ に溶解する酸素は、標準状態に換算すると何 $\text{L}$ か。最も近い値を、次の ①～⑤ の中から一つ選びなさい。
> ① $0.031$　② $0.063$　③ $0.16$　④ $0.31$　⑤ $0.63$
>
> **中文翻译**：在 $20^\circ\text{C}$、$1.0 \times 10^5\text{ Pa}$ 下，每 $1.0\text{ L}$ 水中溶解氧气 $1.4 \times 10^{-3}\text{ mol}$。在 $20^\circ\text{C}$、$5.0 \times 10^5\text{ Pa}$ 下溶于 $2.0\text{ L}$ 水中的氧气，换算成标准状态是多少 $\text{L}$？

**【考点定位】**
亨利定律（温度相同，溶解物质的量与压强、水体积成正比）+ 标况摩尔体积 $22.4\text{ L/mol}$。

**【分步标准解答】**
1. **求 $20^\circ\text{C}$、$5.0 \times 10^5\text{ Pa}$ 下溶于 $2.0\text{ L}$ 水中的 $\text{O}_2$ 物质的量**：
   - 温度仍为 $20^\circ\text{C}$ 不变，压强变为 $5$ 倍，水的体积变为 $2$ 倍：
     $$n(\text{O}_2) = 1.4 \times 10^{-3}\text{ mol} \times \frac{5.0 \times 10^5}{1.0 \times 10^5} \times \frac{2.0}{1.0} = 1.4 \times 10^{-2}\text{ mol}$$
2. **换算为标准状态下的体积**：
   $$V = 1.4 \times 10^{-2}\text{ mol} \times 22.4\text{ L/mol} = 0.3136\text{ L} \approx \mathbf{0.31\text{ L}}$$
   对应选项 **④**。

> 💡 **讲师批注**：注意千万不要把题目里的 $20^\circ\text{C}$ 带去算体积——人家问的是「標準状態に換算すると」（换算到 $0^\circ\text{C}, 1\text{ atm}$），所以求出 $\text{mol}$ 数后**直接乘以 $22.4\text{ L/mol}$** 即可！

**【最终答案】**
**④（$0.31\text{ L}$）**

---

### 【知识点 14】希薄溶液の性質（沸点上升、凝固点降下与冷却曲线）（原书 P.38–40）

#### 图解辅助（SVG 5：蒸气压降下与沸点上升原理图）
<svg viewBox="0 0 420 260" xmlns="http://www.w3.org/2000/svg" style="background:#fafafa;border:1px solid #e2e8f0;border-radius:8px;">
  <!-- 坐标轴 -->
  <line x1="65" y1="220" x2="385" y2="220" stroke="#334155" stroke-width="1.8"/>
  <line x1="65" y1="220" x2="65" y2="25" stroke="#334155" stroke-width="1.8"/>
  <polygon points="385,220 377,216 377,224" fill="#334155"/>
  <polygon points="65,25 61,33 69,33" fill="#334155"/>
  <text x="16" y="34" font-size="11" fill="#1e293b" font-weight="bold">蒸気圧</text>
  <text x="195" y="252" font-size="11" fill="#1e293b" font-weight="bold">温度 [℃]</text>
  <text x="53" y="234" font-size="10" fill="#475569">0</text>
  <!-- 大气压水平虚线 -->
  <line x1="65" y1="95" x2="365" y2="95" stroke="#64748b" stroke-width="1.4" stroke-dasharray="5,4"/>
  <text x="18" y="99" font-size="11" fill="#334155" font-weight="bold">大気圧</text>
  <!-- 纯水蒸气压曲线 -->
  <path d="M 105 140 Q 210 125 280 42" fill="none" stroke="#1e293b" stroke-width="2.5"/>
  <text x="125" y="58" font-size="11" fill="#1e293b" font-weight="bold">水の蒸気圧曲線</text>
  <!-- 稀薄水溶液蒸气压曲线 -->
  <path d="M 105 175 Q 245 162 325 58" fill="none" stroke="#0284c7" stroke-width="2.5"/>
  <text x="298" y="45" font-size="11" fill="#0284c7" font-weight="bold">希薄水溶液の</text>
  <text x="305" y="59" font-size="11" fill="#0284c7" font-weight="bold">蒸気圧曲線</text>
  <!-- 交点 (纯水100℃: x=228, y=95; 溶液100+Δt: x=292, y=95) -->
  <circle cx="228" cy="95" r="4.5" fill="#1e293b"/>
  <circle cx="292" cy="95" r="4.5" fill="#0284c7"/>
  <line x1="228" y1="95" x2="228" y2="220" stroke="#64748b" stroke-width="1.2" stroke-dasharray="3,3"/>
  <line x1="292" y1="95" x2="292" y2="220" stroke="#0284c7" stroke-width="1.2" stroke-dasharray="3,3"/>
  <text x="216" y="236" font-size="11" fill="#1e293b" font-weight="bold">100</text>
  <text x="268" y="236" font-size="11" fill="#0284c7" font-weight="bold">100 + Δt</text>
  <!-- 蒸气压降下向下箭头 -->
  <line x1="165" y1="128" x2="165" y2="162" stroke="#dc2626" stroke-width="2"/>
  <polygon points="165,166 161,158 169,158" fill="#dc2626"/>
  <line x1="228" y1="100" x2="228" y2="144" stroke="#dc2626" stroke-width="2"/>
  <polygon points="228,148 224,140 232,140" fill="#dc2626"/>
  <text x="95" y="156" font-size="11" fill="#dc2626" font-weight="bold">蒸気圧降下 ↓</text>
  <!-- 沸点上升度水平箭头 -->
  <line x1="234" y1="95" x2="284" y2="95" stroke="#16a34a" stroke-width="2.2"/>
  <polygon points="287,95 279,91 279,99" fill="#16a34a"/>
  <line x1="228" y1="205" x2="292" y2="205" stroke="#16a34a" stroke-width="1.8"/>
  <text x="234" y="190" font-size="10" fill="#15803d" font-weight="bold">沸点上昇度</text>
  <text x="252" y="202" font-size="11" fill="#15803d" font-weight="bold">Δt</text>
</svg>

#### 【例题 6】（原书 P.39 / PDF 第 40 页）摩尔沸点上升常数与非电解质/电解质沸点计算

**【原题重现与翻译】**
> 水 $100\text{ g}$ にグルコース $\text{C}_6\text{H}_{12}\text{O}_6$ $9.0\text{ g}$ を溶かすと、大気圧下における沸点が $0.26\text{ K}$ 上昇する。
> $\text{C}_6\text{H}_{12}\text{O}_6 = 180,\ (\text{NH}_2)_2\text{CO} = 60,\ \text{Na}_2\text{SO}_4 = 142$
> (1) 水 $500\text{ g}$ に尿素 $(\text{NH}_2)_2\text{CO}$ を $6.0\text{ g}$ 溶かした溶液の沸点を小数第 2 位まで求めよ。
> (2) 水 $500\text{ g}$ に硫酸ナトリウム $\text{Na}_2\text{SO}_4$ を $28.4\text{ g}$ 溶かした溶液の沸点を小数第 2 位まで求めよ。
>
> **中文翻译**：将 $9.0\text{ g}$ 葡萄糖溶于 $100\text{ g}$ 水中，大气压下沸点上升 $0.26\text{ K}$。求：
> (1) 将 $6.0\text{ g}$ 尿素溶于 $500\text{ g}$ 水中所得溶液的沸点（保留至小数第 2 位）；
> (2) 将 $28.4\text{ g}$ 硫酸钠溶于 $500\text{ g}$ 水中所得溶液的沸点（保留至小数第 2 位）。

**【考点定位】**
$\Delta t = K_b m$、质量摩尔浓度 $m$ 的计算、强电解质完全电离后的总离子数（$\text{Na}_2\text{SO}_4 \to 2\text{Na}^+ + \text{SO}_4^{2-}$，系数 $\times 3$）。

**【分步标准解答】**
1. **由葡萄糖溶液求水的摩尔沸点上升常数 $K_b$**：
   - 葡萄糖是非电解质，质量摩尔浓度为：
     $$m = \frac{\frac{9.0}{180}\text{ mol}}{\frac{100}{1000}\text{ kg}} = \frac{0.050}{0.100} = 0.50\text{ mol/kg}$$
   - 代入 $\Delta t = K_b m$：
     $$0.26\text{ K} = K_b \times 0.50\text{ mol/kg} \implies K_b = 0.52\text{ K}\cdot\text{kg/mol}$$
2. **(1) 尿素水溶液的沸点**：
   - 尿素 $(\text{NH}_2)_2\text{CO}$ 为**非电解质**：
     $$\Delta t = 0.52\text{ K}\cdot\text{kg/mol} \times \frac{\frac{6.0}{60}\text{ mol}}{\frac{500}{1000}\text{ kg}} = 0.52 \times 0.20 = 0.104\text{ K}$$
   - 沸点 $= 100 + 0.104 = 100.104 \approx \mathbf{100.10^\circ\text{C}}$
3. **(2) 硫酸钠水溶液的沸点**：
   - $\text{Na}_2\text{SO}_4$ 为强电解质，水中完全电离：$\text{Na}_2\text{SO}_4 \longrightarrow 2\text{Na}^+ + \text{SO}_4^{2-}$（$1\text{ mol}$ 溶质产生 **$3\text{ mol}$ 粒子**！）：
     $$\Delta t = 0.52\text{ K}\cdot\text{kg/mol} \times \frac{\frac{28.4}{142}\text{ mol}}{\frac{500}{1000}\text{ kg}} \times 3 = 0.52 \times 0.40 \times 3 = 0.624\text{ K}$$
   - 沸点 $= 100 + 0.624 = 100.624 \approx \mathbf{100.62^\circ\text{C}}$

> 💡 **讲师批注**：温差 $\Delta t$ 的单位 $\text{K}$ 与 ${}^\circ\text{C}$ 数值完全等价（升高 $0.104\text{ K}$ 就是升高 $0.104^\circ\text{C}$）！做依数性计算前，第一步永远先默念：**“它是电解质吗？电离出几个离子？”**

**【最终答案】**
(1) **$100.10^\circ\text{C}$**　(2) **$100.62^\circ\text{C}$**

---

#### 图解辅助（SVG 6：纯溶剂与溶液的冷却曲线——过冷现象与凝固点测定）
<svg viewBox="0 0 420 260" xmlns="http://www.w3.org/2000/svg" style="background:#fafafa;border:1px solid #e2e8f0;border-radius:8px;">
  <!-- 坐标轴 -->
  <line x1="85" y1="225" x2="395" y2="225" stroke="#334155" stroke-width="1.8"/>
  <line x1="85" y1="225" x2="85" y2="20" stroke="#334155" stroke-width="1.8"/>
  <polygon points="395,225 387,221 387,229" fill="#334155"/>
  <polygon points="85,20 81,28 89,28" fill="#334155"/>
  <text x="52" y="30" font-size="11" fill="#1e293b" font-weight="bold">温度</text>
  <text x="335" y="246" font-size="11" fill="#1e293b" font-weight="bold">冷却時間</text>
  <text x="72" y="238" font-size="10" fill="#475569">0</text>
  <!-- 纯溶剂冷却曲线 A-B-C-D -->
  <path d="M 118 28 L 132 65 Q 145 110 155 115 Q 162 115 168 65 L 300 65 L 355 95" fill="none" stroke="#1e293b" stroke-width="2.4"/>
  <!-- 标注点 A, B, C, D -->
  <circle cx="132" cy="65" r="3.5" fill="#1e293b"/>
  <text x="137" y="61" font-size="10" fill="#1e293b" font-weight="bold">A</text>
  <circle cx="155" cy="115" r="4" fill="#dc2626"/>
  <text x="142" y="127" font-size="10" fill="#dc2626" font-weight="bold">B (過冷却・凝固開始)</text>
  <circle cx="168" cy="65" r="3.5" fill="#1e293b"/>
  <text x="172" y="60" font-size="10" fill="#1e293b" font-weight="bold">C</text>
  <circle cx="300" cy="65" r="3.5" fill="#1e293b"/>
  <text x="304" y="60" font-size="10" fill="#1e293b" font-weight="bold">D (凝固終了)</text>
  <text x="200" y="54" font-size="10" fill="#1e293b" font-weight="bold">純溶媒の冷却曲線（水平！）</text>
  <!-- 纯溶剂凝固点虚线 -->
  <line x1="85" y1="65" x2="168" y2="65" stroke="#64748b" stroke-width="1.2" stroke-dasharray="4,3"/>
  <text x="6" y="69" font-size="10" fill="#1e293b" font-weight="bold">純溶媒の凝固点</text>
  <!-- 溶液冷却曲线 A'-B'-C'-D' -->
  <path d="M 122 105 L 136 140 Q 148 188 158 194 Q 164 194 172 145 L 300 162 L 355 198" fill="none" stroke="#0284c7" stroke-width="2.4"/>
  <circle cx="136" cy="140" r="3.5" fill="#0284c7"/>
  <text x="140" y="137" font-size="10" fill="#0284c7" font-weight="bold">A'</text>
  <circle cx="158" cy="194" r="3.5" fill="#dc2626"/>
  <text x="143" y="206" font-size="10" fill="#dc2626" font-weight="bold">B'</text>
  <circle cx="172" cy="145" r="3.5" fill="#0284c7"/>
  <text x="175" y="141" font-size="10" fill="#0284c7" font-weight="bold">C'</text>
  <circle cx="300" cy="162" r="3.5" fill="#0284c7"/>
  <text x="305" y="159" font-size="10" fill="#0284c7" font-weight="bold">D'</text>
  <text x="195" y="142" font-size="10" fill="#0284c7" font-weight="bold">溶液の冷却曲線（右下がり！）</text>
  <!-- 溶液凝固点外推虚线 -->
  <line x1="85" y1="140" x2="172" y2="145" stroke="#0284c7" stroke-width="1.2" stroke-dasharray="4,3"/>
  <text x="12" y="144" font-size="10" fill="#0284c7" font-weight="bold">溶液の凝固点</text>
  <!-- 凝固点降下度 Δt -->
  <line x1="96" y1="68" x2="96" y2="137" stroke="#16a34a" stroke-width="2"/>
  <polygon points="96,65 92,72 100,72" fill="#16a34a"/>
  <polygon points="96,140 92,133 100,133" fill="#16a34a"/>
  <text x="10" y="102" font-size="10" fill="#15803d" font-weight="bold">凝固点降下度</text>
  <text x="45" y="116" font-size="11" fill="#15803d" font-weight="bold">Δt</text>
  <!-- 相区划分 -->
  <line x1="158" y1="194" x2="158" y2="225" stroke="#94a3b8" stroke-dasharray="2,2"/>
  <line x1="300" y1="65" x2="300" y2="225" stroke="#94a3b8" stroke-dasharray="2,2"/>
  <text x="105" y="218" font-size="10" fill="#475569">液体</text>
  <text x="202" y="218" font-size="10" fill="#475569">液体と固体</text>
  <text x="325" y="218" font-size="10" fill="#475569">固体</text>
</svg>

> 💡 **冷却曲线核心考点（EJU 选择题常考！）**：
> 1. 为什么在 $B$（$B'$）点温度低于凝固点还没结冰？——**過冷却（过冷现象）**，一旦开始结晶放出凝固热，温度瞬间回升到 $C$（$C'$）。
> 2. 为什么纯溶剂 $C \to D$ 是**水平线**，而溶液 $C' \to D'$ 是**向右下方倾斜的斜线**？——因为溶液凝固时**只有纯溶剂（水）结冰析出**，导致剩余溶液的**浓度越来越高**，凝固点随之不断降低！
> 3. **溶液的真实凝固点**如何读？——将 $C'D'$ 直线**向左延长**与降温线相交于 **$A'$** 对应的纵坐标！

#### 【例题 7】（原书 P.40 / PDF 第 41 页）利用凝固点降下测定未知非电解质的分子量

**【原题重现与翻译】**
> 水 $100\text{ g}$ に非電解質 A を $6.84\text{ g}$ 溶かした水溶液の凝固点を測定したところ、$-0.37^\circ\text{C}$ であった。A の分子量を整数値で答えよ。水のモル凝固点降下を $1.85\text{ K}\cdot\text{kg/mol}$ とする。
>
> **中文翻译**：将 $6.84\text{ g}$ 非电解质 A 溶于 $100\text{ g}$ 水中，测得水溶液凝固点为 $-0.37^\circ\text{C}$。求 A 的分子量（整数）。已知水的摩尔凝固点降下常数为 $1.85\text{ K}\cdot\text{kg/mol}$。

**【考点定位】**
$\Delta t = K_f m$ 反推未知非电解质的分子量 $M$。

**【分步标准解答】**
1. **求凝固点降下度 $\Delta t$**：
   $$\Delta t = 0 - (-0.37) = 0.37\text{ K}$$
2. **设 A 的分子量为 $M$，代入 $\Delta t = K_f m$**：
   $$0.37\text{ K} = 1.85\text{ K}\cdot\text{kg/mol} \times \frac{\frac{6.84}{M}\text{ mol}}{\frac{100}{1000}\text{ kg}}$$
   $$0.37 = 1.85 \times \frac{68.4}{M} \implies M = \frac{1.85 \times 68.4}{0.37} = 5 \times 68.4 = \mathbf{342}$$

> 💡 **讲师批注**：算出 $M = 342$ 要有化学直觉——这正是**蔗糖（スクロース，$\text{C}_{12}\text{H}_{22}\text{O}_{11}$）**的分子量！计算时先约分 $\frac{1.85}{0.37} = 5$，口算秒出答案！

**【最终答案】**
**$M = 342$**

---

### 【知识点 15】浸透圧（渗透压）与范特霍夫定律（原书 P.41–42）

#### 图解辅助（SVG 7：U 字管渗透压原理三阶段演变）
<svg viewBox="0 0 420 260" xmlns="http://www.w3.org/2000/svg" style="background:#fafafa;border:1px solid #e2e8f0;border-radius:8px;">
  <!-- 顶部公式 -->
  <rect x="65" y="10" width="290" height="24" rx="4" fill="#eff6ff" stroke="#3b82f6"/>
  <text x="82" y="26" font-size="11" fill="#1d4ed8" font-weight="bold">ファントホッフの法則：Π ＝ cRT （電解質は全粒子濃度！）</text>
  <!-- 阶段1：初始等高 -->
  <g transform="translate(22,55)">
    <text x="18" y="10" font-size="10" fill="#334155" font-weight="bold">① 初始状态</text>
    <!-- U形管液体 -->
    <path d="M 16 70 L 16 125 A 32 32 0 0 0 48 157 L 48 135 A 10 10 0 0 1 38 125 L 38 70 Z" fill="#e0f2fe"/>
    <path d="M 48 157 A 32 32 0 0 0 80 125 L 80 70 L 58 70 L 58 125 A 10 10 0 0 1 48 135 Z" fill="#fde68a"/>
    <!-- U形管轮廓 -->
    <path d="M 16 25 L 16 125 A 32 32 0 0 0 80 125 L 80 25" fill="none" stroke="#334155" stroke-width="2"/>
    <path d="M 38 25 L 38 125 A 10 10 0 0 0 58 125 L 58 25" fill="none" stroke="#334155" stroke-width="2"/>
    <!-- 半透膜 -->
    <line x1="48" y1="135" x2="48" y2="157" stroke="#dc2626" stroke-width="2.5" stroke-dasharray="3,2"/>
    <text x="19" y="105" font-size="9" fill="#0369a1">純</text>
    <text x="19" y="116" font-size="9" fill="#0369a1">溶</text>
    <text x="19" y="127" font-size="9" fill="#0369a1">媒</text>
    <text x="64" y="105" font-size="9" fill="#b45309">溶</text>
    <text x="64" y="118" font-size="9" fill="#b45309">液</text>
    <text x="31" y="174" font-size="10" fill="#dc2626" font-weight="bold">半透膜</text>
  </g>
  <!-- 阶段2：渗透平衡出现液面差 h -->
  <g transform="translate(158,55)">
    <text x="10" y="10" font-size="10" fill="#15803d" font-weight="bold">② 浸透平衡 (液面差h)</text>
    <path d="M 16 88 L 16 125 A 32 32 0 0 0 48 157 L 48 135 A 10 10 0 0 1 38 125 L 38 88 Z" fill="#e0f2fe"/>
    <path d="M 48 157 A 32 32 0 0 0 80 125 L 80 48 L 58 48 L 58 125 A 10 10 0 0 1 48 135 Z" fill="#fde68a"/>
    <path d="M 16 25 L 16 125 A 32 32 0 0 0 80 125 L 80 25" fill="none" stroke="#334155" stroke-width="2"/>
    <path d="M 38 25 L 38 125 A 10 10 0 0 0 58 125 L 58 25" fill="none" stroke="#334155" stroke-width="2"/>
    <line x1="48" y1="135" x2="48" y2="157" stroke="#dc2626" stroke-width="2.5" stroke-dasharray="3,2"/>
    <!-- 液面差 h -->
    <line x1="38" y1="88" x2="58" y2="88" stroke="#16a34a" stroke-dasharray="2,2"/>
    <line x1="48" y1="48" x2="48" y2="88" stroke="#16a34a" stroke-width="1.8"/>
    <text x="41" y="72" font-size="11" fill="#15803d" font-weight="bold">h</text>
    <!-- 渗透方向箭头 -->
    <line x1="34" y1="146" x2="60" y2="146" stroke="#0284c7" stroke-width="2"/>
    <polygon points="64,146 57,142 57,150" fill="#0284c7"/>
    <text x="36" y="133" font-size="9" fill="#0284c7" font-weight="bold">浸透→</text>
    <text x="31" y="174" font-size="10" fill="#dc2626" font-weight="bold">半透膜</text>
  </g>
  <!-- 阶段3：加压 Π 使液面恢复等高 -->
  <g transform="translate(294,55)">
    <text x="8" y="10" font-size="10" fill="#7c3aed" font-weight="bold">③ 加压 Π 恢复等高</text>
    <path d="M 16 70 L 16 125 A 32 32 0 0 0 48 157 L 48 135 A 10 10 0 0 1 38 125 L 38 70 Z" fill="#e0f2fe"/>
    <path d="M 48 157 A 32 32 0 0 0 80 125 L 80 70 L 58 70 L 58 125 A 10 10 0 0 1 48 135 Z" fill="#fde68a"/>
    <path d="M 16 25 L 16 125 A 32 32 0 0 0 80 125 L 80 25" fill="none" stroke="#334155" stroke-width="2"/>
    <path d="M 38 25 L 38 125 A 10 10 0 0 0 58 125 L 58 25" fill="none" stroke="#334155" stroke-width="2"/>
    <line x1="48" y1="135" x2="48" y2="157" stroke="#dc2626" stroke-width="2.5" stroke-dasharray="3,2"/>
    <!-- 向下加压箭头 -->
    <line x1="69" y1="30" x2="69" y2="62" stroke="#7c3aed" stroke-width="2.8"/>
    <polygon points="69,67 64,58 74,58" fill="#7c3aed"/>
    <text x="53" y="25" font-size="10" fill="#7c3aed" font-weight="bold">浸透圧 Π</text>
    <text x="31" y="174" font-size="10" fill="#dc2626" font-weight="bold">半透膜</text>
  </g>
</svg>

#### 【例题 8】（原书 P.42 / PDF 第 43 页）为什么测定高分子分子量首选“渗透压法”？

**【原题重现与翻译】**
> (1) 分子量 $1$ 万の非電解質 $1.0\text{ g}$ を水に溶かして作った $1.0\text{ L}$ の溶液の $27^\circ\text{C}$ における浸透圧 $\Pi$ は何 $\text{Pa}$ か。気体定数 $R = 8.3 \times 10^3\text{ Pa}\cdot\text{L/(K}\cdot\text{mol)}$ とする。
> (2) (1) と同じ溶液の凝固点降下度 $\Delta t$ は何 $\text{K}$ か。ただし、溶媒の質量は $1.0\text{ kg}$ と近似でき、水のモル凝固点降下を $K_f = 1.85\text{ K}\cdot\text{kg/mol}$ とする。
>
> **中文翻译**：
> (1) 将 $1.0\text{ g}$ 分子量为 $1$ 万的非电解质溶于水配成 $1.0\text{ L}$ 溶液，求 $27^\circ\text{C}$ 时的渗透压 $\Pi\text{ [Pa]}$。
> (2) 求同一溶液的凝固点降下度 $\Delta t\text{ [K]}$（溶剂质量近似为 $1.0\text{ kg}$，$K_f = 1.85\text{ K}\cdot\text{kg/mol}$）。

**【考点定位】**
$\Pi = cRT$ 与 $\Delta t = K_f m$ 的直接计算对比（理解为何蛋白质等高分子化合物必须用渗透压法测分子量）。

**【分步标准解答】**
- **(1) 求渗透压 $\Pi$**：
  - 溶质物质的量 $n = \frac{1.0}{10000} = 1.0 \times 10^{-4}\text{ mol}$，浓度 $c = 1.0 \times 10^{-4}\text{ mol/L}$，温度 $T = 273 + 27 = 300\text{ K}$。
  - 代入 $\Pi = cRT$：
    $$\Pi = \frac{1.0 \times 10^{-4}\text{ mol}}{1.0\text{ L}} \times 8.3 \times 10^3\text{ Pa}\cdot\text{L/(K}\cdot\text{mol)} \times 300\text{ K} = 249\text{ Pa} \approx \mathbf{2.5 \times 10^2\text{ Pa}}$$
- **(2) 求凝固点降下度 $\Delta t$**：
  $$\Delta t = 1.85\text{ K}\cdot\text{kg/mol} \times \frac{1.0 \times 10^{-4}\text{ mol}}{1.0\text{ kg}} = 1.85 \times 10^{-4}\text{ K} \approx \mathbf{1.9 \times 10^{-4}\text{ K}}$$

> 💡 **讲师批注**：这道题背后藏着一个 EJU 简答/选择题高频结论！同样是分子量 $1$ 万的高分子溶液，凝固点只下降了 $0.00019\text{ K}$（普通温度计根本测不出来！），但渗透压高达 $250\text{ Pa}$（相当于约 $2.5\text{ cm}$ 的水柱高度，肉眼清晰可测！）。因此：**测定高分子化合物（如タンパク質、合成高分子）的分子量，必须采用「浸透圧法」**！

**【最终答案】**
(1) **$2.5 \times 10^2\text{ Pa}$**　(2) **$1.9 \times 10^{-4}\text{ K}$**

---

#### 【例题 9】（原书 P.42 / PDF 第 43 页，防衛大・改）液柱法测定氯化钡水溶液的渗透压与浓度

**【原题重现与翻译】**
> 希薄な塩化バリウム水溶液の浸透圧を図の装置で $27^\circ\text{C}$ において測定したところ、液柱（*原书误印为「液注」*）の高さ $h$ は $60\text{ cm}$ となった。$1.0 \times 10^5\text{ Pa} = 760\text{ mmHg}$、水銀の密度を $13.6\text{ g/cm}^3$、水溶液の密度を $1.0\text{ g/cm}^3$ とするとき、浸透圧と塩化バリウム水溶液のモル濃度を求めよ。ただし、水の浸透による溶液の濃度変化は無視できるものとする。［防衛大・改］
>
> **中文翻译**：用图示装置在 $27^\circ\text{C}$ 下测定稀氯化钡水溶液的渗透压，测得液柱高度 $h = 60\text{ cm}$。已知 $1.0 \times 10^5\text{ Pa} = 760\text{ mmHg}$，水银密度 $13.6\text{ g/cm}^3$，水溶液密度 $1.0\text{ g/cm}^3$，求渗透压和氯化钡水溶液的物质的量浓度（忽略水渗入引起的浓度变化）。

**【考点定位】**
水柱高度与水银柱高度的压强换算（$\rho_1 h_1 = \rho_2 h_2$）+ 强电解质 $\text{BaCl}_2$ 的渗透压计算（粒子数 $\times 3$）。

**【图解辅助（SVG 8：防衛大・改 漏斗半透膜渗透压测定装置）】**
<svg viewBox="0 0 420 260" xmlns="http://www.w3.org/2000/svg" style="background:#fafafa;border:1px solid #e2e8f0;border-radius:8px;">
  <!-- 外部烧杯与纯水 -->
  <rect x="95" y="135" width="150" height="90" fill="#e0f2fe"/>
  <polyline points="95,110 95,225 245,225 245,110" fill="none" stroke="#334155" stroke-width="2.2"/>
  <line x1="95" y1="135" x2="245" y2="135" stroke="#0284c7" stroke-width="1.5"/>
  <text x="102" y="155" font-size="10" fill="#0369a1">純水</text>
  <!-- 倒置长颈漏斗与内部 BaCl2 溶液 -->
  <path d="M 164 48 L 164 142 Q 140 155 140 198 L 200 198 Q 200 155 176 142 L 176 48 Z" fill="#fde68a"/>
  <path d="M 164 22 L 164 142 Q 140 155 140 198" fill="none" stroke="#334155" stroke-width="2"/>
  <path d="M 176 22 L 176 142 Q 200 155 200 198" fill="none" stroke="#334155" stroke-width="2"/>
  <!-- 底部半透膜 -->
  <line x1="140" y1="198" x2="200" y2="198" stroke="#dc2626" stroke-width="3" stroke-dasharray="4,2"/>
  <text x="152" y="214" font-size="11" fill="#dc2626" font-weight="bold">半透膜</text>
  <text x="151" y="182" font-size="10" fill="#92400e" font-weight="bold">BaCl₂</text>
  <!-- 液柱高度 h = 60 cm 标注 -->
  <line x1="145" y1="48" x2="164" y2="48" stroke="#16a34a" stroke-dasharray="3,2"/>
  <line x1="152" y1="50" x2="152" y2="133" stroke="#16a34a" stroke-width="2"/>
  <polygon points="152,48 148,55 156,55" fill="#16a34a"/>
  <polygon points="152,135 148,128 156,128" fill="#16a34a"/>
  <text x="103" y="96" font-size="11" fill="#15803d" font-weight="bold">h = 60 cm</text>
  <!-- 右侧换算说明框 -->
  <rect x="260" y="55" width="148" height="125" rx="6" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.2"/>
  <text x="270" y="76" font-size="11" fill="#1e293b" font-weight="bold">水柱 → 水银柱换算</text>
  <text x="270" y="98" font-size="10" fill="#475569">等压：ρ水·h水 = ρHg·hHg</text>
  <text x="270" y="118" font-size="10" fill="#0284c7" font-weight="bold">hHg = 60 × (1.0 / 13.6) cm</text>
  <text x="270" y="140" font-size="10" fill="#dc2626" font-weight="bold">BaCl₂ → Ba²⁺ + 2Cl⁻</text>
  <text x="270" y="158" font-size="10" fill="#dc2626">(全粒子浓度 = 3c !)</text>
</svg>

**【分步标准解答】**
1. **将 $60\text{ cm}$ 水柱换算为压强 $\Pi\text{ [Pa]}$**：
   - 已知 $760\text{ mmHg} = 76\text{ cmHg} = 1.0 \times 10^5\text{ Pa}$。
   - $60\text{ cm}$ 水柱等效的水银柱高度为 $60\text{ cm} \times \frac{1.0\text{ g/cm}^3}{13.6\text{ g/cm}^3}$。
   - 列比例式：
     $$76\text{ cm} : 1.0 \times 10^5\text{ Pa} = \left(60\text{ cm} \times \frac{1.0}{13.6}\right) : \Pi\text{ [Pa]}$$
     $$\Pi = 1.0 \times 10^5 \times \frac{60 \times 1.0}{76 \times 13.6} \approx 5.805 \times 10^3\text{ Pa} \approx \mathbf{5.8 \times 10^3\text{ Pa}}$$
2. **求氯化钡水溶液的物质的量浓度 $c\text{ [mol/L]}$**：
   - $\text{BaCl}_2$ 完全电离为 $1$ 个 $\text{Ba}^{2+}$ 和 $2$ 个 $\text{Cl}^-$，总离子浓度为 **$3c$**！
   - 代入 $\Pi = (3c)RT$（中间值取 $5.80 \times 10^3\text{ Pa}$）：
     $$5.80 \times 10^3\text{ Pa} = (3c\text{ mol/L}) \times 8.3 \times 10^3\text{ Pa}\cdot\text{L/(K}\cdot\text{mol)} \times (273 + 27)\text{ K}$$
     $$c = \frac{5.80 \times 10^3}{3 \times 8.3 \times 10^3 \times 300} = \frac{5.80}{7470} \approx 7.76 \times 10^{-4}\text{ mol/L} \approx \mathbf{7.8 \times 10^{-4}\text{ mol/L}}$$

> 💡 **讲师批注**：水柱压强换算还有一个物理通用口诀：$P = \rho g h$，或者更直接记住在 $1\text{ atm} = 1.0\times 10^5\text{ Pa}$ 下，$76\text{ cmHg}$ 相当于 $76 \times 13.6 \approx 1034\text{ cm}$（约 $10.3\text{ m}$）水柱！本题 $60\text{ cm}$ 水柱就是 $\frac{60}{1034} \times 1.0\times 10^5 \approx 5.8\times 10^3\text{ Pa}$，一步验算超快！

**【最终答案】**
渗透压：**$5.8 \times 10^3\text{ Pa}$**；氯化钡水溶液的物质的量浓度：**$7.8 \times 10^{-4}\text{ mol/L}$**

---

### 【知识点 16】コロイド（胶体）（原书 P.43 / PDF 第 44 页）

| 维度 | 核心要点（EJU 选择题高频考点） |
| :--- | :--- |
| **胶体粒子大小** | 直径 **$10^{-9} \sim 10^{-7}\text{ m}$**（**能透过滤纸，不能透过半透膜**） |
| **疎水コロイド（疏水胶体）** | 难水合，加**少量电解质**即沉淀（**凝析**），例：金属氢氧化物（$\text{Fe(OH)}_3$ 等） |
| **親水コロイド（亲水胶体）** | 易水合，需加**大量电解质**才沉淀（**盐析**），例：淀粉（デンプン）、蛋白质（タンパク質）等有机物 |
| **チンダル現象（丁达尔效应）** | 侧面照射光线时，光通路发亮——原因：**胶体粒子对光的散射（散乱）** |
| **ブラウン運動（布朗运动）** | 胶体粒子的不规则运动——原因：**热运动的溶剂分子对胶体粒子的不规则撞击（不規則な衝突）** |

---

### 【第三章・知识点 1】反応熱と熱化学方程式（反应热与热化学方程式）（原书 P.44 / PDF 第 45 页）

#### 图解辅助（SVG 9：放热反应与吸热反应的能量图对比）
<svg viewBox="0 0 420 260" xmlns="http://www.w3.org/2000/svg" style="background:#fafafa;border:1px solid #e2e8f0;border-radius:8px;">
  <!-- 左侧：放热反应 -->
  <g transform="translate(15,15)">
    <text x="48" y="16" font-size="12" fill="#dc2626" font-weight="bold">発熱反応 (+394 kJ)</text>
    <!-- 纵轴 -->
    <line x1="25" y1="205" x2="25" y2="35" stroke="#334155" stroke-width="1.6"/>
    <polygon points="25,32 21,40 29,40" fill="#334155"/>
    <text x="18" y="28" font-size="10" fill="#334155">高</text>
    <text x="18" y="218" font-size="10" fill="#334155">低</text>
    <text x="4" y="100" font-size="10" fill="#475569">エ</text>
    <text x="4" y="113" font-size="10" fill="#475569">ネ</text>
    <text x="4" y="126" font-size="10" fill="#475569">ル</text>
    <text x="4" y="139" font-size="10" fill="#475569">ギ</text>
    <text x="4" y="152" font-size="10" fill="#475569">ー</text>
    <!-- 反应物能级（高） -->
    <line x1="42" y1="68" x2="170" y2="68" stroke="#1e293b" stroke-width="2.2"/>
    <text x="46" y="60" font-size="11" fill="#1e293b" font-weight="bold">反応物  C + O₂</text>
    <!-- 生成物能级（低） -->
    <line x1="42" y1="185" x2="170" y2="185" stroke="#1e293b" stroke-width="2.2"/>
    <text x="52" y="177" font-size="11" fill="#1e293b" font-weight="bold">生成物  CO₂</text>
    <!-- 向下放热箭头 -->
    <line x1="145" y1="70" x2="145" y2="178" stroke="#dc2626" stroke-width="3"/>
    <polygon points="145,184 139,174 151,174" fill="#dc2626"/>
    <text x="152" y="130" font-size="11" fill="#dc2626" font-weight="bold">394 kJ</text>
    <text x="152" y="144" font-size="9" fill="#dc2626">放出</text>
    <!-- 方程式 -->
    <text x="32" y="232" font-size="10" fill="#dc2626" font-weight="bold">C + O₂ = CO₂ + 394 kJ</text>
  </g>
  <!-- 中间分割线 -->
  <line x1="210" y1="20" x2="210" y2="245" stroke="#cbd5e1" stroke-dasharray="4,3"/>
  <!-- 右侧：吸热反应 -->
  <g transform="translate(220,15)">
    <text x="46" y="16" font-size="12" fill="#0284c7" font-weight="bold">吸熱反応 (-131 kJ)</text>
    <line x1="25" y1="205" x2="25" y2="35" stroke="#334155" stroke-width="1.6"/>
    <polygon points="25,32 21,40 29,40" fill="#334155"/>
    <text x="18" y="28" font-size="10" fill="#334155">高</text>
    <text x="18" y="218" font-size="10" fill="#334155">低</text>
    <!-- 生成物能级（高） -->
    <line x1="42" y1="68" x2="170" y2="68" stroke="#1e293b" stroke-width="2.2"/>
    <text x="42" y="60" font-size="11" fill="#1e293b" font-weight="bold">生成物  CO + H₂</text>
    <!-- 反应物能级（低） -->
    <line x1="42" y1="185" x2="170" y2="185" stroke="#1e293b" stroke-width="2.2"/>
    <text x="42" y="177" font-size="11" fill="#1e293b" font-weight="bold">反応物  C + H₂O</text>
    <!-- 向上吸热箭头 -->
    <line x1="145" y1="183" x2="145" y2="75" stroke="#0284c7" stroke-width="3"/>
    <polygon points="145,69 139,79 151,79" fill="#0284c7"/>
    <text x="152" y="130" font-size="11" fill="#0284c7" font-weight="bold">131 kJ</text>
    <text x="152" y="144" font-size="9" fill="#0284c7">吸収</text>
    <!-- 方程式 -->
    <text x="20" y="232" font-size="10" fill="#0284c7" font-weight="bold">C + H₂O = CO + H₂ - 131 kJ</text>
  </g>
</svg>

#### 燃烧热（燃焼熱）热化学方程式书写示例（原书 P.44）
- **定义**：$1\text{ mol}$ 物质完全燃烧时**放出的热量**（必为放热反应，报数值时不带正负号）。
- **书写铁律**：被燃烧物质系数必须为 **$1$**；生成的水为**液态 $\text{H}_2\text{O(液)}$**，碳生成 $\text{CO}_2\text{(気)}$。
  - 氢气的燃烧热（$286\text{ kJ/mol}$）：
    $$\text{H}_2\text{(気)} + \frac{1}{2}\text{O}_2\text{(気)} = \text{H}_2\text{O(液)} + 286\text{ kJ}$$
  - 石墨的燃烧热（$394\text{ kJ/mol}$）：
    $$\text{C(黒鉛)} + \text{O}_2\text{(気)} = \text{CO}_2\text{(気)} + 394\text{ kJ}$$
  - 乙烷的燃烧热（$1560\text{ kJ/mol}$）：
    $$\text{C}_2\text{H}_6\text{(気)} + \frac{7}{2}\text{O}_2\text{(気)} = 2\text{CO}_2\text{(気)} + 3\text{H}_2\text{O(液)} + 1560\text{ kJ}$$

---

## 4. 全局术语与物质名录同步

本切片新增的全部日文核心术语与化学物质已按主题分类同步写入全局术语分片文件：[glossary_003.md](file:///Users/baohan/Desktop/EJU/notes_化学/_glossary_parts/glossary_003.md)，涵盖：
- 蒸气压与排水集气核心词汇（`気液平衡`、`飽和水蒸気圧`、`ジエチルエーテル`、`エタノール`、`水上置換法` 等）
- 固体/水合物/气体溶解度核心词汇（`溶解平衡`、`析出`、`硫酸銅（II）五水和物`、`ヘンリーの法則` 等）
- 稀溶液依数性、渗透压与胶体核心词汇（`蒸気圧降下`、`沸点上昇`、`質量モル濃度`、`凝固点降下`、`過冷却`、`半透膜`、`ファントホッフの法則`、`疎水コロイド/凝析`、`親水コロイド/塩析`、`チンダル現象`、`ブラウン運動` 等）
- 热化学开篇核心词汇（`反応熱`、`熱化学方程式`、`発熱反応`、`吸熱反応`、`燃焼熱`、`エタン` 等）
