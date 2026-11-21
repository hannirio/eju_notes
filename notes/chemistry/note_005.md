# EJU 化学基础・第三章 物質の反応（下）& 第四章 物質の反応（2）（切片 005：P61–P75）

> **对应原教材**：格致学苑《EJU 化学対策》「化学基礎・第三章 物質の反応（第 9–14 节）」及「化学基礎・第四章 物質の反応（2）（第 1 节）」（原书页码 P.60–P.74，PDF 第 61–75 页）
> **适用对象**：忘却国内高中化学基础、零起步对接日本 EJU 留考化学体系的同学

---

## 1. 本节前置：国内高中化学基础唤醒

本切片横跨 EJU 化学最核心的两大反应板块——**水溶液中的离子平衡（酸碱 pH、弱电解质电离、盐类水解、中和滴定、缓冲溶液、沉淀溶解平衡）**与**氧化还原反应基础（氧化数、半反应式配平与定量计算）**。在 EJU 真题中，这部分几乎每年贡献 25%–35% 的高分值计算与实验题。

### 1.1 国内高中核心基础快速唤醒
1. **水的离子积与 $\text{pH}$**
   - $25^\circ\text{C}$ 时，任何稀水溶液中都满足水的离子积恒等式：$K_w = [\text{H}^+][\text{OH}^-] = 1.0 \times 10^{-14}\text{ (mol/L)}^2$。
   - $\text{pH}$ 定义为氢离子浓度的负常用对数：$\text{pH} = -\log_{10}[\text{H}^+]$（等价于 $[\text{H}^+] = 10^{-\text{pH}}$）。
   - 常温下：$\text{pH} \lt 7$ 为酸性，$\text{pH} = 7$ 为中性，$\text{pH} \gt 7$ 为碱性。
   - **对数速算必备**：$\log_{10} 2 = 0.30$，$\log_{10} 3 = 0.48$，$\log_{10} 4 = 2\log_{10} 2 = 0.60$，$\log_{10} 5 = 1 - \log_{10} 2 = 0.70$。
2. **弱酸・弱碱的电离平衡与电离常数（$K_a, K_b$）**
   - 强酸（$\text{HCl}, \text{HNO}_3, \text{H}_2\text{SO}_4$）、强碱（$\text{NaOH}, \text{KOH}, \text{Ca(OH)}_2, \text{Ba(OH)}_2$）在水中几乎 $100\%$ 完全电离（电离度 $\alpha \fallingdotseq 1$）。
   - 弱酸（如醋酸 $\text{CH}_3\text{COOH}$）、弱碱（如氨水 $\text{NH}_3\cdot\text{H}_2\text{O}$）部分电离，建立动态平衡：
     $$K_a = \frac{[\text{CH}_3\text{COO}^-][\text{H}^+]}{[\text{CH}_3\text{COOH}]} = \frac{c\alpha^2}{1 - \alpha}$$
   - **近似成立的条件**：当电离度极小（一般 $\alpha \le 0.05$，即 $\alpha \ll 1$）时，可近似 $1 - \alpha \fallingdotseq 1$，立刻推导出三大秒杀公式：
     $$K_a \fallingdotseq c\alpha^2 \quad\Rightarrow\quad \alpha = \sqrt{\frac{K_a}{c}}, \quad [\text{H}^+] = c\alpha = \sqrt{cK_a}$$
   - **若浓度极稀导致 $\alpha \gt 0.05$**：**绝对不能近似**，必须保留 $1 - \alpha$ 解一元二次方程 $c\alpha^2 + K_a\alpha - K_a = 0$！
3. **盐的分类与水解规律（谁强显谁性）**
   - **正盐（正塩）**：酸与碱完全中和的产物（不含可电离的 $\text{H}$ 或 $\text{OH}$），如 $\text{NaCl}, \text{CH}_3\text{COONa}$。
   - **酸式盐（酸性塩）**：含可电离的 $\text{H}$，如 $\text{NaHSO}_4$（强酸酸式盐，完全电离出 $\text{H}^+$，显**酸性**）、$\text{NaHCO}_3$（弱酸酸式盐，水解大于电离，显**碱性**）。
   - **碱式盐（塩基性塩）**：含 $\text{OH}$，如 $\text{MgCl(OH)}, \text{CuCl(OH)}$。
   - 正盐水溶液酸碱性口诀：**强酸强碱盐中性，强酸弱碱盐酸性，弱酸强碱盐碱性**（有弱才水解，谁强显谁性）。
4. **中和滴定与指示剂选择**
   - 中和定量公式：**酸放出的 $\text{H}^+$ 物质的量 $=$ 碱放出的 $\text{OH}^-$ 物质的量**，即 $a \cdot c \cdot V = b \cdot c' \cdot V'$（$a, b$ 分别为酸、碱的元数/价数）。
   - 指示剂选择原则：**指示剂的变色范围必须落在滴定终点（中和点）附近的 $\text{pH}$ 突跃区间内**。
     - 酚酞（フェノールフタレイン）：$8.0\sim 9.8$（无色 $\leftrightarrow$ 红色），适合**强酸+强碱**、**弱酸+强碱**。
     - 甲基橙（メチルオレンジ）：$3.1\sim 4.4$（红 $\leftrightarrow$ 黄），适合**强酸+强碱**、**强酸+弱碱**。
5. **缓冲溶液（緩衝液）**
   - 由“**大量弱酸 + 其共轭碱（强碱盐）**”或“**大量弱碱 + 其共轭酸（强酸盐）**”组成，如 $\text{CH}_3\text{COOH} + \text{CH}_3\text{COONa}$、$\text{NH}_3 + \text{NH}_4\text{Cl}$。加入少量酸或碱时通过平衡移动抵消 $[\text{H}^+]$ 或 $[\text{OH}^-]$ 的剧变，使 $\text{pH}$ 几乎不变。
6. **难溶盐的溶解平衡与溶度积（$K_{\text{sp}}$）**
   - 饱和溶液中溶解速率等于析出速率。对 $\text{A}_m\text{B}_n(\text{固}) \rightleftharpoons m\text{A}^{n+} + n\text{B}^{m-}$，有 $K_{\text{sp}} = [\text{A}^{n+}]^m[\text{B}^{m-}]^n$（仅与温度有关）。
   - **沉淀判定（离子积 $Q$ 与 $K_{\text{sp}}$ 比较）**：$Q \gt K_{\text{sp}}$ 析出沉淀；$Q = K_{\text{sp}}$ 饱和平衡；$Q \lt K_{\text{sp}}$ 不沉淀。
   - **同离子效应**：向难溶盐溶液中加入含相同离子的强电解质，平衡逆向移动，难溶盐溶解度大幅下降。
7. **氧化还原反应核心口诀**
   - **升失氧化还原剂，降得还原氧化剂**（原教材侧栏口诀：降得还原氧化性，升失氧化还原性）。
   - **电子得失守恒**：氧化剂得到的电子总数 $=$ 还原剂失去的电子总数。

---

### 1.2 中日化学体系差异提醒（EJU 避坑必看）

1. **「酸性塩」不一定显「酸性」！（EJU 经典陷阱）**
   - 日文把国内的“酸式盐”称为**酸性塩（さんせいえん）**，把“碱式盐”称为**塩基性塩（えんきせいえん）**。千万不要看到“酸性塩”就以为水溶液一定显酸性！例如 $\text{NaHCO}_3$ 是**酸性塩**，但它的水溶液显**塩基性（碱性）**！
2. **「共洗い（ともあらい）」——润洗仪器的日文专属高频词**：
   - EJU 实验题必考四大玻璃仪器的清洗方式：
     - **液を出して使用する器具（量取并放出固定体积液体）**：**ホールピペット（移液管）**、**ビュレット（滴定管）** $\rightarrow$ 必须用待装液**共洗い（润洗）**，否则残水会稀释溶液导致浓度偏低！
     - **液を入れて使用する器具（盛装液体）**：**メスフラスコ（容量瓶）**、**コニカルビーカー（锥形烧杯）** $\rightarrow$ **绝对不能共洗い**，只需用**蒸留水（蒸馏水）**洗净即可（保留水珠不影响溶质总物质的量）！
3. **「コニカルビーカー」vs「三角フラスコ」**：
   - 国内滴定常用锥形瓶，日本教材在滴定章节常写 **コニカルビーカー（锥形烧杯）**，它和三角烧瓶一样都是“盛液器具”，不需要共洗い。
4. **「酸化数」的书写规范**：
   - 国内写化合价常写 $+2$ 或 $2+$，日本规定**酸化数（氧化数）必须带正负号且写在数字前**，如 $+6, -2, 0$；而离子电荷写在数字后，如 $\text{Fe}^{2+}, \text{SO}_4^{2-}$。
5. **氧化剂/还原剂的「価数（价数）」概念**：
   - 国内高中很少提“6 价氧化剂”，但日本 EJU 非常喜欢直接定义：**$1\text{ mol}$ 氧化剂（或还原剂）能接收（或放出）的电子 $e^-$ 的物质的量，称为氧化剂（或还原剂）的価数**！例如 $\text{K}_2\text{Cr}_2\text{O}_7$ 接收 $6\text{ mol }e^-$，叫 **6 価の酸化剤**；$\text{KMnO}_4$（酸性）接收 $5\text{ mol }e^-$，叫 **5 価の酸化剤**。由此可直接套用和酸碱中和一模一样的公式：$a c V = b c' V'$！
6. **氨水的日文写法**：
   - 国内常写 $\text{NH}_3\cdot\text{H}_2\text{O}$，日本教材统一直接写为 **$\text{NH}_3$**（水溶液称为 アンモニア水），电离平衡写为 $\text{NH}_3 + \text{H}_2\text{O} \rightleftharpoons \text{NH}_4^+ + \text{OH}^-$。

> ⚠️ **原教材印刷勘误提醒（讲师人工逐页核对参考图发现）**：
> 1. **原书 P.63（PDF 第 64 页）**：正塩举例中 `例）NaCl, CH₃COOH` 属于**原书明显印刷错误**！$\text{CH}_3\text{COOH}$（醋酸）是弱酸而非盐，此处正确应为 **`CH₃COONa`**（醋酸钠，正盐；其分子中的 $\text{H}$ 属于甲基不可电离，故为正盐）。
> 2. **原书 P.67（PDF 第 68 页）**：小标题 `アンモニア－塩化アンモニア水溶液の緩衝作用` 中的「塩化アンモニア」为印刷用词笔误，标准日文化学名称应为 **「塩化アンモニウム（$\text{NH}_4\text{Cl}$）」**。
> 3. **原书 P.72（PDF 第 73 页）**：还原剂半反应式表中第一行硫化氢 `H₂S → S + 2H⁺ + 2e` 漏印了电子的负号上标，正确应为 **`H₂S → S + 2H⁺ + 2e⁻`**。
> 4. **原书 P.74（PDF 第 75 页）**：[解法 2] 第二行比例式 `K₂CrO₇ : FeSO₄ = 1 : 6` 漏印了 $\text{Cr}$ 的下标 `2`，正确应为 **`K₂Cr₂O₇ : FeSO₄ = 1 : 6`**。

---

## 2. 日文化学核心词汇、物质名称与假名注音（板书必备）

### 2.1 pH、电离平衡、盐类与缓冲溶液
- **水素イオン指数（すいそいおんしすう / suiso ion shisū）** — 氢离子指数（$\text{pH}$）
- **水のイオン積（みずのいおんせき / mizu no ionseki）** — 水的离子积（$K_w$）
- **電離度（でんりど / denrido）** — 电离度（$\alpha$）
- **電離平衡（でんりへいこう / denri heikō）** — 电离平衡
- **電離定数（でんりていすう / denri teisū）** — 电离常数（酸：$K_a$，碱：$K_b$）
- **近似（きんじ / kinji）** — 近似
- **酢酸（さくさん / sakusan）** — 醋酸/乙酸（$\text{CH}_3\text{COOH}$）
- **酢酸ナトリウム（さくさんなとりうむ / sakusan natoriumu）** — 醋酸钠（$\text{CH}_3\text{COONa}$）
- **酢酸カリウム（さくさんかりうむ / sakusan kariumu）** — 醋酸钾（$\text{CH}_3\text{COOK}$）
- **硫酸（りゅうさん / ryūsan）** — 硫酸（$\text{H}_2\text{SO}_4$）
- **塩酸（えんさん / ensan）** — 盐酸（$\text{HCl}$ 水溶液）
- **アンモニア水（あんもにあすい / anmonia-sui）** — 氨水（$\text{NH}_3$ 水溶液）
- **塩の加水分解（えんのかすいぶんかい / en no kasuibunkai）** — 盐的水解
- **正塩（せいえん / seien）** — 正盐（如 $\text{NaCl}, \text{CH}_3\text{COONa}$）
- **酸性塩（さんせいえん / sanseien）** — 酸式盐（如 $\text{KHSO}_4, \text{NaHCO}_3$）
- **塩基性塩（えんきせいえん / enkiseien）** — 碱式盐（如 $\text{MgCl(OH)}, \text{CuCl(OH)}$）
- **液性（えきせい / ekisei）** — 溶液酸碱性（酸性・中性・塩基性）
- **炭酸水素ナトリウム（たんさんすいそなとりうむ / tansan suiso natoriumu）** — 碳酸氢钠（$\text{NaHCO}_3$）
- **硫酸水素ナトリウム（りゅうさんすいそなとりうむ / ryūsan suiso natoriumu）** — 硫酸氢钠（$\text{NaHSO}_4$）
- **亜硫酸ナトリウム（ありゅうさんなとりうむ / aryūsan natoriumu）** — 亚硫酸钠（$\text{Na}_2\text{SO}_3$）
- **硫酸カリウム（りゅうさんかりうむ / ryūsan kariumu）** — 硫酸钾（$\text{K}_2\text{SO}_4$）
- **硝酸アンモニウム（しょうさんあんもにうむ / shōsan anmoniumu）** — 硝酸铵（$\text{NH}_4\text{NO}_3$）
- **塩化アンモニウム（えんかあんもにうむ / enka anmoniumu）** — 氯化铵（$\text{NH}_4\text{Cl}$）
- **緩衝液・緩衝作用（かんしょうえき・かんしょうさよう / kanshōeki, kanshō sayō）** — 缓冲溶液・缓冲作用

### 2.2 中和滴定、仪器、指示剂与溶解度积
- **中和滴定（ちゅうわてきてい / chūwa tekitei）** — 中和滴定
- **中和点（ちゅうわてん / chūwaten）** — 中和点（滴定终点）
- **中和滴定曲線（ちゅうわてきていきょくせん / chūwa tekitei kyokusen）** — 中和滴定曲线
- **滴下量（てきかりょう / tekikaryō）** — 滴加量
- **ホールピペット（ほーるぴぺっと / hōru pipetto）** — 移液管（胖肚移液管）
- **ビュレット（びゅれっと / byuretto）** — 滴定管
- **メスフラスコ（めすふらすこ / mesu furasuko）** — 容量瓶
- **コニカルビーカー（こにかるびーかー / konikaru bīkā）** — 锥形烧杯
- **共洗い（ともあらい / tomoarai）** — 润洗（用待装溶液冲洗仪器内壁）
- **蒸留水（じょうりゅうすい / jōryūsui）** — 蒸馏水
- **指示薬・変色域（しじやく・へんしょくいき / shijiyaku, henshokuiki）** — 指示剂・变色范围
- **フェノールフタレイン（ふぇのーるふたれいん / fenōru futarein）** — 酚酞（$8.0\sim 9.8$，无色 $\leftrightarrow$ 红）
- **メチルオレンジ（めちるおれんじ / mechiru orenji）** — 甲基橙（$3.1\sim 4.4$，红 $\leftrightarrow$ 黄）
- **メチルレッド（めちるれっど / mechiru reddo）** — 甲基红（$4.2\sim 6.3$，红 $\leftrightarrow$ 黄）
- **水酸化ナトリウム（すいさんかなとりうむ / suisanka natoriumu）** — 氢氧化钠（$\text{NaOH}$）
- **水酸化カルシウム（すいさんかかるしうむ / suisanka karushiumu）** — 氢氧化钙（$\text{Ca(OH)}_2$）
- **難溶性塩（なんようせいえん / nan'yōseien）** — 难溶性盐
- **溶解平衡（ようかいへいこう / yōkai heikō）** — 溶解平衡
- **溶解度積（ようかいどせき / yōkaidoseki）** — 溶度积（$K_{\text{sp}}$）
- **析出・沈殿（せきしゅつ・ちんでん / sekishutsu, chinden）** — 析出・沉淀
- **飽和溶液（ほうわようえき / hōwa yōeki）** — 饱和溶液
- **塩化銀（えんかぎん / enkagin）** — 氯化银（$\text{AgCl}$）
- **クロム酸銀（くろむさんぎん / kuromusan-gin）** — 铬酸银（$\text{Ag}_2\text{CrO}_4$）
- **塩化鉛(II)（えんかなまりに / enka namari ni）** — 氯化铅(II)（$\text{PbCl}_2$）

### 2.3 氧化还原反应与常见氧化剂・还原剂
- **酸化還元反応（さんかかんげんはんのう / sanka kangen hannō）** — 氧化还原反应
- **酸化数（さんかすう / sankasū）** — 氧化数（化合价）
- **酸化剤・還元剤（さんかざい・かんげんざい / sankazai, kangenzai）** — 氧化剂・还原剂
- **半反応式（はんはんのうしき / han-hannōshiki）** — 半反应式
- **過マンガン酸カリウム（かまんがんさんかりうむ / kamangansan kariumu）** — 高锰酸钾（$\text{KMnO}_4$）
- **ニクロム酸カリウム（にくろむさんかりうむ / nikuromusan kariumu）** — 重铬酸钾（$\text{K}_2\text{Cr}_2\text{O}_7$）
- **濃硝酸・希硝酸（のうしょうさん・きしょうさん / nōshōsan, kishōsan）** — 浓硝酸・稀硝酸（$\text{HNO}_3$）
- **熱濃硫酸（ねつのうりゅうさん / netsu nōryūsan）** — 热浓硫酸（$\text{H}_2\text{SO}_4$）
- **塩素（えんそ / enso）** — 氯气（$\text{Cl}_2$）
- **過酸化水素（かさんかすいそ / kasanka suiso）** — 过氧化氢（$\text{H}_2\text{O}_2$）
- **二酸化硫黄（にさんかいおう / nisanka iō）** — 二氧化硫（$\text{SO}_2$）
- **酸化マンガン(IV)（さんかまんがんよん / sanka mangan yon）** — 二氧化锰（$\text{MnO}_2$）
- **オゾン（おぞん / ozon）** — 臭氧（$\text{O}_3$）
- **硫化水素（りゅうかすいそ / ryūka suiso）** — 硫化氢（$\text{H}_2\text{S}$）
- **シュウ酸（しゅうさん / shūsan）** — 草酸/乙二酸（$(\text{COOH})_2$ 或 $\text{H}_2\text{C}_2\text{O}_4$）
- **ヨウ化カリウム（ようかかりうむ / yōka kariumu）** — 碘化钾（$\text{KI}$）
- **ヨウ化物イオン（ようかぶついおん / yōkabutsu ion）** — 碘离子（$\text{I}^-$）
- **硫酸鉄(II)（りゅうさんてつに / ryūsan tetsu ni）** — 硫酸亚铁（$\text{FeSO}_4$）
- **塩化スズ(II)（えんかすずに / enka suzu ni）** — 氯化亚锡（$\text{SnCl}_2$）
- **チオ硫酸イオン（ちおりゅうさんいおん / chio-ryūsan ion）** — 硫代硫酸根离子（$\text{S}_2\text{O}_3^{2-}$）
- **過不足なく反応する（かふそくなくはんのうする / kafusoku naku hannō suru）** — 恰好完全反应（无过量无不足）

### 2.4 关键化学方程式与公式的日语课堂口语读法
1. **$\text{pH}$ 定义式**：$\text{pH} = -\log_{10}[\text{H}^+]$
   - 读法：`ピーエイチ イコール マイナス ログ じゅうの エイチプラスの モル濃度（のうど）`（注：日本化学老派也读 `ペーハー`）
2. **水的离子积**：$K_w = [\text{H}^+][\text{OH}^-] = 1.0 \times 10^{-14}\text{ (mol/L)}^2$
   - 读法：`ケーダブリュー イコール エイチプラス かける オーエイチマイナス イコール いってんぜろ かける じゅうの マイナスじゅうよんじょう モルパーリットルの にじょう`
3. **中和 / 氧化还原定量公式**：$a \times c \times V = b \times c' \times V'$
   - 读法：`エー かける シー かける ブイ イコール ビー かける シーダッシュ かける ブイダッシュ`
4. **高锰酸根酸性半反应式**：$\text{MnO}_4^- + 8\text{H}^+ + 5e^- \rightarrow \text{Mn}^{2+} + 4\text{H}_2\text{O}$
   - 读法：`エムエヌオーフォーマイナス たす はち エイチプラス たす ご イーマイナス やじるし エムエヌにプラス たす よん エイチツーオー`
5. **溶度积公式**：$K_{\text{sp}} = [\text{Pb}^{2+}][\text{Cl}^-]^2$
   - 读法：`ケーエスピー イコール ピービーにプラス かける シーエルマイナスの にじょう`

---

## 3. 核心知识点图解与逐题深度解析

### 3.1 例题 1：$\text{pH}$ 的四大经典计算（原书 P.60 / PDF 第 61 页）

#### 【原题重现与翻译】
> **原文**：次の水溶液の $\text{pH}$ を求めよ。ただし、$\log_{10} 2 = 0.30$ とする。
> (1) $0.0050\text{ mol/L}$ の硫酸。
> (2) $0.20\text{ mol/L}$ の塩酸を水で $100$ 倍に薄めた水溶液。
> (3) $0.010\text{ mol/L}$ のアンモニア水（電離度 $0.025$）。
> (4) $\text{pH }2.0$ の塩酸 $10\text{ mL}$ と $\text{pH }3.0$ の塩酸 $20\text{ mL}$ を混合した水溶液。
>
> **译文**：求下列水溶液的 $\text{pH}$。设 $\log_{10} 2 = 0.30$。
> (1) $0.0050\text{ mol/L}$ 的硫酸。
> (2) 将 $0.20\text{ mol/L}$ 的盐酸用水稀释 $100$ 倍的水溶液。
> (3) $0.010\text{ mol/L}$ 的氨水（电离度 $0.025$）。
> (4) 将 $\text{pH }2.0$ 的盐酸 $10\text{ mL}$ 与 $\text{pH }3.0$ 的盐酸 $20\text{ mL}$ 混合后的水溶液。

#### 【考点定位】
二元强酸的 $[\text{H}^+]$ 计算、强酸稀释、弱碱结合 $K_w$ 求 $\text{pH}$、强酸混合溶液 $\text{pH}$ 计算。

#### 【分步标准解答】

**(1) $0.0050\text{ mol/L}$ 的硫酸（$\text{H}_2\text{SO}_4$）**
- 硫酸是 **2 价强酸**，完全电离：$\text{H}_2\text{SO}_4 \rightarrow 2\text{H}^+ + \text{SO}_4^{2-}$。
- $[\text{H}^+] = 2 \times 0.0050\text{ mol/L} = 0.010\text{ mol/L} = 1.0 \times 10^{-2}\text{ mol/L}$。
- $\text{pH} = -\log_{10}(1.0 \times 10^{-2}) = 2.0$（原书简写为 $2$）。
> 💡 **讲师批注**：算强酸 $\text{pH}$ 第一眼先看**价数**！硫酸是 2 价酸，千万别忘了乘以 $2$！

**(2) $0.20\text{ mol/L}$ 盐酸稀释 $100$ 倍**
- 盐酸是 1 价强酸，稀释 $100$ 倍后浓度变为原来的 $\dfrac{1}{100}$：
  $$[\text{H}^+] = 0.20\text{ mol/L} \times \frac{1}{100} = 2.0 \times 10^{-3}\text{ mol/L}$$
- 代入 $\text{pH}$ 定义：
  $$\text{pH} = -\log_{10}(2.0 \times 10^{-3}) = -(\log_{10} 2.0 - 3) = -(0.30 - 3) = 2.7$$
> 💡 **讲师批注**：对数拆解口诀：**$-\log_{10}(a \times 10^{-n}) = n - \log_{10} a$**。这里 $n=3, a=2.0$，一眼秒出 $3 - 0.30 = 2.7$！

**(3) $0.010\text{ mol/L}$ 氨水（电离度 $\alpha = 0.025$）**
- 氨水是 1 价弱碱，先求 $[\text{OH}^-]$：
  $$[\text{OH}^-] = 1 \times c \times \alpha = 0.010\text{ mol/L} \times 0.025 = 2.5 \times 10^{-4}\text{ mol/L}$$
- 利用 $25^\circ\text{C}$ 水的离子积 $K_w = 1.0 \times 10^{-14}\text{ (mol/L)}^2$ 转化为 $[\text{H}^+]$：
  $$[\text{H}^+] = \frac{K_w}{[\text{OH}^-]} = \frac{1.0 \times 10^{-14}}{2.5 \times 10^{-4}} = 0.40 \times 10^{-10} = 4.0 \times 10^{-11}\text{ mol/L}$$
- 求 $\text{pH}$：
  $$\text{pH} = -\log_{10}(4.0 \times 10^{-11}) = 11 - \log_{10} 4.0 = 11 - 2\log_{10} 2.0 = 11 - 0.60 = 10.4$$
> 💡 **讲师批注**：也可以用 $\text{pOH}$ 速算校验：$\text{pOH} = -\log_{10}(2.5 \times 10^{-4}) = 4 - \log_{10}(10/4) = 4 - (1 - 0.60) = 3.6$，再由 $\text{pH} = 14 - \text{pOH} = 14 - 3.6 = 10.4$，又快又不容易算错指数！

**(4) $\text{pH }2.0$ 盐酸 $10\text{ mL}$ + $\text{pH }3.0$ 盐酸 $20\text{ mL}$**
- $\text{pH }2.0 \Rightarrow [\text{H}^+]_1 = 1.0 \times 10^{-2}\text{ mol/L}$；$\text{pH }3.0 \Rightarrow [\text{H}^+]_2 = 1.0 \times 10^{-3}\text{ mol/L}$。
- 混合后的氢离子总物质的量除以总体积（假设体积具有加和性）：
  $$[\text{H}^+] = \frac{1.0 \times 10^{-2}\text{ mol/L} \times \dfrac{10}{1000}\text{ L} + 1.0 \times 10^{-3}\text{ mol/L} \times \dfrac{20}{1000}\text{ L}}{\dfrac{10}{1000}\text{ L} + \dfrac{20}{1000}\text{ L}} = \frac{0.10 + 0.020}{30}\text{ mol/L} = \frac{0.120}{30} = 4.0 \times 10^{-3}\text{ mol/L}$$
- 求 $\text{pH}$：
  $$\text{pH} = -\log_{10}(4.0 \times 10^{-3}) = 3 - 2\log_{10} 2.0 = 3 - 0.60 = 2.4$$
> 💡 **讲师批注**：注意分子分母中的 $\frac{1}{1000}$ 可以直接约掉，计算混合浓度时直接用“$\text{mL}$ 乘以 $\text{mol/L}$ 再除以总 $\text{mL}$”即可，省时不易出错！

#### 【最终答案】
**(1) $\text{pH} = 2$（或 $2.0$）　(2) $\text{pH} = 2.7$　(3) $\text{pH} = 10.4$　(4) $\text{pH} = 2.4$**

---

### 3.2 例题 2：弱酸・弱碱电离平衡与 $K_a, K_b$ 计算（原书 P.62 / PDF 第 63 页）

#### 【原题重现与翻译】
> **原文**：
> (1) $0.10\text{ mol/L}$ の酢酸水溶液の電離度 $\alpha$、水素イオン濃度 $[\text{H}^+]$、$\text{pH}$ を求めよ。酢酸の電離定数 $K_a = 2.0 \times 10^{-5}\text{ mol/L}$、$\log_{10} 2 = 0.30$、$\sqrt{2} = 1.4$ とする。
> (2) $0.010\text{ mol/L}$ のアンモニア水の電離度 $\alpha$、水酸化物イオン濃度 $[\text{OH}^-]$、$\text{pH}$ を求めよ。アンモニアの電離定数を $K_b = 1.6 \times 10^{-5}\text{ mol/L}$、水のイオン積を $K_w = 1.0 \times 10^{-14}\text{ (mol/L)}^2$、$\log_{10} 2 = 0.30$ とする。
> (3) $1.0 \times 10^{-5}\text{ mol/L}$ の酢酸の電離度 $\alpha$、水素イオン濃度 $[\text{H}^+]$、$\text{pH}$ を求めよ。酢酸の電離定数 $K_a = 5.0 \times 10^{-7}\text{ mol/L}$、$\log_{10} 2 = 0.30$ とする。
>
> **译文**：
> (1) 求 $0.10\text{ mol/L}$ 醋酸水溶液的电离度 $\alpha$、氢离子浓度 $[\text{H}^+]$ 及 $\text{pH}$。设 $K_a = 2.0 \times 10^{-5}\text{ mol/L}$，$\log_{10} 2 = 0.30$，$\sqrt{2} = 1.4$。
> (2) 求 $0.010\text{ mol/L}$ 氨水的电离度 $\alpha$、氢氧根离子浓度 $[\text{OH}^-]$ 及 $\text{pH}$。设 $K_b = 1.6 \times 10^{-5}\text{ mol/L}$，$K_w = 1.0 \times 10^{-14}\text{ (mol/L)}^2$，$\log_{10} 2 = 0.30$。
> (3) 求 $1.0 \times 10^{-5}\text{ mol/L}$ 醋酸的电离度 $\alpha$、氢离子浓度 $[\text{H}^+]$ 及 $\text{pH}$。设 $K_a = 5.0 \times 10^{-7}\text{ mol/L}$，$\log_{10} 2 = 0.30$。

#### 【考点定位】
弱电解质电离平衡（$K_a, K_b$）、$\alpha \ll 1$ 近似公式的适用条件判断与一元二次方程精确求解。

#### 【分步标准解答】

**(1) $0.10\text{ mol/L}$ 醋酸（可近似）**
- 试算近似电离度：
  $$\alpha = \sqrt{\frac{K_a}{c}} = \sqrt{\frac{2.0 \times 10^{-5}}{0.10}} = \sqrt{2 \times 10^{-4}} = \sqrt{2} \times 10^{-2} = 1.4 \times 10^{-2}$$
  由于 $\alpha = 0.014 \ll 1$（小于 $0.05$），近似 $1 - \alpha \fallingdotseq 1$ 合法！
- 求 $[\text{H}^+]$：
  $$[\text{H}^+] = c\alpha = \sqrt{cK_a} = \sqrt{0.10 \times 2.0 \times 10^{-5}} = \sqrt{2 \times 10^{-6}} = 1.4 \times 10^{-3}\text{ mol/L}$$
- 求 $\text{pH}$（**重要技巧**：保留根号形式代对数，精度更高！）：
  $$\text{pH} = -\log_{10}[\text{H}^+] = -\log_{10}\sqrt{2 \times 10^{-6}} = -\frac{1}{2}\log_{10}(2 \times 10^{-6}) = -\frac{1}{2}(0.30 - 6) = 2.85 \fallingdotseq 2.9$$
> 💡 **讲师批注**：本题最精彩的技巧在最后一步！题目没给 $\log_{10} 1.4$，如果你拿 $1.4 \times 10^{-3}$ 去算对数就卡壳了；必须把 $[\text{H}^+]$ 写回 $\sqrt{2 \times 10^{-6}} = (2 \times 10^{-6})^{1/2}$，用对数幂法则把 $\frac{1}{2}$ 提出来，就能完美用上已知的 $\log_{10} 2 = 0.30$！最后按 2 位有效数字修约为 $2.9$。

**(2) $0.010\text{ mol/L}$ 氨水（可近似）**
- 电离平衡：$\text{NH}_3 + \text{H}_2\text{O} \rightleftharpoons \text{NH}_4^+ + \text{OH}^-$，试算近似电离度：
  $$\alpha = \sqrt{\frac{K_b}{c}} = \sqrt{\frac{1.6 \times 10^{-5}}{0.010}} = \sqrt{16 \times 10^{-4}} = 4.0 \times 10^{-2}$$
  由于 $\alpha = 0.040 \le 0.05$，近似合法！
- 求 $[\text{OH}^-]$：
  $$[\text{OH}^-] = \sqrt{cK_b} = \sqrt{0.010 \times 1.6 \times 10^{-5}} = \sqrt{16 \times 10^{-8}} = 4.0 \times 10^{-4}\text{ mol/L}$$
- 求 $[\text{H}^+]$ 与 $\text{pH}$：
  $$[\text{H}^+] = \frac{K_w}{[\text{OH}^-]} = \frac{1.0 \times 10^{-14}}{4.0 \times 10^{-4}} = \frac{1}{4} \times 10^{-10}\text{ mol/L}$$
  $$\text{pH} = -\log_{10}\left(\frac{1}{4} \times 10^{-10}\right) = -(-2\log_{10} 2 - 10) = 2 \times 0.30 + 10 = 10.6$$

**(3) $1.0 \times 10^{-5}\text{ mol/L}$ 醋酸（不可近似！）**
- 先心算试探：$\sqrt{\dfrac{K_a}{c}} = \sqrt{\dfrac{5.0 \times 10^{-7}}{1.0 \times 10^{-5}}} = \sqrt{0.05} \approx 0.22 \gt 0.05$！**$\alpha$ 太大，绝对不能使用 $1 - \alpha \fallingdotseq 1$ 近似**！
- 使用精确式 $K_a = \dfrac{c\alpha^2}{1 - \alpha}$ 整理为一元二次方程：
  $$c\alpha^2 + K_a\alpha - K_a = 0$$
  代入 $c = 1.0 \times 10^{-5}$，$K_a = 5.0 \times 10^{-7}$：
  $$1.0 \times 10^{-5}\alpha^2 + 5.0 \times 10^{-7}\alpha - 5.0 \times 10^{-7} = 0$$
  两边同除以 $5.0 \times 10^{-7}$（即乘以 $2 \times 10^6$）化简为整系数方程：
  $$20\alpha^2 + \alpha - 1 = 0 \quad\Rightarrow\quad (5\alpha - 1)(4\alpha + 1) = 0$$
- 因 $\alpha \gt 0$，解得 $\alpha = \dfrac{1}{5} = 0.20$。
- 求 $[\text{H}^+]$ 与 $\text{pH}$：
  $$[\text{H}^+] = c\alpha = 1.0 \times 10^{-5} \times 0.20 = 2.0 \times 10^{-6}\text{ mol/L}$$
  $$\text{pH} = -\log_{10}(2.0 \times 10^{-6}) = 6 - \log_{10} 2.0 = 6 - 0.30 = 5.7$$
> 💡 **讲师批注**：这道题是 EJU 极高明的“反套路”题！凡是题目里 $c$ 和 $K_a$ 数量级相差不超过 2 个数量级（如本题仅差 $20$ 倍），一定要立刻警觉并因式分解解一元二次方程！

#### 【最终答案】
- **(1) $\alpha = 1.4 \times 10^{-2}$，$[\text{H}^+] = 1.4 \times 10^{-3}\text{ mol/L}$，$\text{pH} = 2.9$**
- **(2) $\alpha = 4.0 \times 10^{-2}$，$[\text{OH}^-] = 4.0 \times 10^{-4}\text{ mol/L}$，$\text{pH} = 10.6$**
- **(3) $\alpha = 0.20$，$[\text{H}^+] = 2.0 \times 10^{-6}\text{ mol/L}$，$\text{pH} = 5.7$**

---

### 3.3 例题 3：盐的分类与水溶液液性判定（原书 P.63 / PDF 第 64 页）

#### 【原题重现与翻译】
> **原文**：次の塩の種類と水溶液の液性を答えよ。
> (1) $\text{CH}_3\text{COOK}$　(2) $\text{NaHCO}_3$　(3) $\text{Na}_2\text{SO}_3$　(4) $\text{K}_2\text{SO}_4$　(5) $\text{NaHSO}_4$　(6) $\text{NH}_4\text{NO}_3$
>
> **译文**：回答下列盐的种类及其水溶液的酸碱性（液性）。

#### 【考点定位】
正塩・酸性塩・塩基性塩的识别，以及盐类水解（谁强显谁性）与两种必考酸式盐（$\text{NaHCO}_3$ vs $\text{NaHSO}_4$）的液性。

#### 【分步标准解答】

| 编号 | 化学式 | 组成来源（酸 + 碱） | 盐的种类判定 | 水溶液液性及微观原因 |
| :---: | :---: | :--- | :---: | :--- |
| **(1)** | $\text{CH}_3\text{COOK}$ | 弱酸 $\text{CH}_3\text{COOH}$ + 强碱 $\text{KOH}$ | **正塩** | **塩基性**（$\text{CH}_3\text{COO}^- + \text{H}_2\text{O} \rightleftharpoons \text{CH}_3\text{COOH} + \text{OH}^-$） |
| **(2)** | $\text{NaHCO}_3$ | 弱酸 $\text{H}_2\text{CO}_3$ + 强碱 $\text{NaOH}$ | **酸性塩** | **塩基性**（$\text{HCO}_3^-$ 水解趋势大于电离趋势，生成 $\text{OH}^-$） |
| **(3)** | $\text{Na}_2\text{SO}_3$ | 弱酸 $\text{H}_2\text{SO}_3$ + 强碱 $\text{NaOH}$ | **正塩** | **塩基性**（$\text{SO}_3^{2-} + \text{H}_2\text{O} \rightleftharpoons \text{HSO}_3^- + \text{OH}^-$） |
| **(4)** | $\text{K}_2\text{SO}_4$ | 强酸 $\text{H}_2\text{SO}_4$ + 强碱 $\text{KOH}$ | **正塩** | **中性**（强酸强碱盐不水解） |
| **(5)** | $\text{NaHSO}_4$ | 强酸 $\text{H}_2\text{SO}_4$ + 强碱 $\text{NaOH}$ | **酸性塩** | **酸性**（水溶液中几乎完全电离：$\text{NaHSO}_4 \rightarrow \text{Na}^+ + \text{H}^+ + \text{SO}_4^{2-}$） |
| **(6)** | $\text{NH}_4\text{NO}_3$ | 强酸 $\text{HNO}_3$ + 弱碱 $\text{NH}_3$ | **正塩** | **酸性**（$\text{NH}_4^+ + \text{H}_2\text{O} \rightleftharpoons \text{NH}_3 + \text{H}_3\text{O}^+$） |

> 💡 **讲师批注**：两大高频失分点——① $\text{CH}_3\text{COOK}$ 和 $\text{NH}_4\text{NO}_3$ 化学式里虽然有 $\text{H}$，但那不是“多元酸未中和完留下的 $\text{H}$”，它们都是**正塩**！② $\text{NaHCO}_3$ 是**酸性塩**但显**塩基性**，而 $\text{NaHSO}_4$ 是**酸性塩**且显**酸性**，EJU 选择题几乎年年拿这一对做文章！

#### 【最终答案】
**(1) 正塩、塩基性　(2) 酸性塩、塩基性　(3) 正塩、塩基性　(4) 正塩、中性　(5) 酸性塩、酸性　(6) 正塩、酸性**

---

### 3.4 核心实验与图像图解：中和滴定仪器、曲线与指示剂（原书 P.64–P.65 / PDF 第 65–66 页）

#### 【图解辅助 1：中和滴定四大玻璃仪器“共洗い（润洗）”判定】

<svg viewBox="0 0 420 260" xmlns="http://www.w3.org/2000/svg" style="max-width:100%;height:auto;background:#fafbfc;border:1px solid #e1e4e8;border-radius:8px;">
  <text x="210" y="20" text-anchor="middle" font-size="13" font-weight="bold" fill="#1e293b">中和滴定四大实验器具：共洗い（润洗）判定总图</text>
  <!-- 左侧：需要共洗い -->
  <rect x="12" y="32" width="192" height="216" rx="8" fill="#fef2f2" stroke="#fca5a5" stroke-width="1.5"/>
  <rect x="24" y="40" width="168" height="24" rx="5" fill="#dc2626"/>
  <text x="108" y="56" text-anchor="middle" font-size="11" font-weight="bold" fill="#ffffff">液を出して使用：共洗い必要！</text>
  <!-- ホールピペット -->
  <line x1="62" y1="74" x2="62" y2="108" stroke="#1d4ed8" stroke-width="3"/>
  <ellipse cx="62" cy="126" rx="10" ry="20" fill="#dbeafe" stroke="#1d4ed8" stroke-width="2"/>
  <line x1="62" y1="146" x2="62" y2="188" stroke="#1d4ed8" stroke-width="3"/>
  <line x1="55" y1="90" x2="69" y2="90" stroke="#dc2626" stroke-width="1.5"/>
  <text x="62" y="205" text-anchor="middle" font-size="10" font-weight="bold" fill="#1e3a8a">ホールピペット</text>
  <text x="62" y="219" text-anchor="middle" font-size="9.5" fill="#475569">（移液管）</text>
  <!-- ビュレット -->
  <rect x="148" y="74" width="10" height="92" fill="#dbeafe" stroke="#1d4ed8" stroke-width="1.8"/>
  <line x1="148" y1="86" x2="155" y2="86" stroke="#1e40af" stroke-width="1"/>
  <line x1="148" y1="98" x2="155" y2="98" stroke="#1e40af" stroke-width="1"/>
  <line x1="148" y1="110" x2="155" y2="110" stroke="#1e40af" stroke-width="1"/>
  <line x1="148" y1="122" x2="155" y2="122" stroke="#1e40af" stroke-width="1"/>
  <line x1="148" y1="134" x2="155" y2="134" stroke="#1e40af" stroke-width="1"/>
  <line x1="148" y1="146" x2="155" y2="146" stroke="#1e40af" stroke-width="1"/>
  <!-- 活塞 -->
  <rect x="142" y="168" width="22" height="6" rx="2" fill="#475569"/>
  <line x1="153" y1="174" x2="153" y2="188" stroke="#1d4ed8" stroke-width="2.5"/>
  <text x="153" y="205" text-anchor="middle" font-size="10" font-weight="bold" fill="#1e3a8a">ビュレット</text>
  <text x="153" y="219" text-anchor="middle" font-size="9.5" fill="#475569">（滴定管）</text>
  <text x="108" y="238" text-anchor="middle" font-size="9.5" fill="#b91c1c">※ 残水会稀释待测液，导致浓度偏低</text>

  <!-- 右侧：不需要共洗い -->
  <rect x="216" y="32" width="192" height="216" rx="8" fill="#f0fdf4" stroke="#86efac" stroke-width="1.5"/>
  <rect x="228" y="40" width="168" height="24" rx="5" fill="#16a34a"/>
  <text x="312" y="56" text-anchor="middle" font-size="11" font-weight="bold" fill="#ffffff">液を入れて使用：蒸留水即可！</text>
  <!-- メスフラスコ -->
  <rect x="261" y="76" width="10" height="8" rx="2" fill="#64748b"/>
  <rect x="262" y="84" width="8" height="44" fill="#dcfce7" stroke="#15803d" stroke-width="1.8"/>
  <line x1="259" y1="104" x2="273" y2="104" stroke="#dc2626" stroke-width="1.5"/>
  <path d="M 262 128 L 244 176 Q 242 186 252 186 L 280 186 Q 290 186 288 176 L 270 128 Z" fill="#dcfce7" stroke="#15803d" stroke-width="1.8"/>
  <text x="266" y="205" text-anchor="middle" font-size="10" font-weight="bold" fill="#166534">メスフラスコ</text>
  <text x="266" y="219" text-anchor="middle" font-size="9.5" fill="#475569">（容量瓶）</text>
  <!-- コニカルビーカー -->
  <path d="M 342 114 L 330 186 L 382 186 L 370 114 Z" fill="#dcfce7" stroke="#15803d" stroke-width="1.8"/>
  <ellipse cx="356" cy="114" rx="14" ry="3.5" fill="#bbf7d0" stroke="#15803d" stroke-width="1.5"/>
  <line x1="354" y1="138" x2="364" y2="138" stroke="#15803d" stroke-width="1"/>
  <line x1="354" y1="152" x2="366" y2="152" stroke="#15803d" stroke-width="1"/>
  <line x1="354" y1="166" x2="368" y2="166" stroke="#15803d" stroke-width="1"/>
  <text x="356" y="205" text-anchor="middle" font-size="10" font-weight="bold" fill="#166534">コニカルビーカー</text>
  <text x="356" y="219" text-anchor="middle" font-size="9.5" fill="#475569">（锥形烧杯）</text>
  <text x="312" y="238" text-anchor="middle" font-size="9.5" fill="#15803d">※ 残水不改变溶质 mol，严禁共洗い</text>
</svg>

#### 【图解辅助 2：中和滴定三大曲线与指示剂选择】

<svg viewBox="0 0 420 260" xmlns="http://www.w3.org/2000/svg" style="max-width:100%;height:auto;background:#fafbfc;border:1px solid #e1e4e8;border-radius:8px;">
  <text x="210" y="18" text-anchor="middle" font-size="12.5" font-weight="bold" fill="#1e293b">中和滴定曲線と指示薬の選択（原书 P.65）</text>
  <!-- 图例 -->
  <rect x="65" y="26" width="12" height="8" fill="#f43f5e" opacity="0.35"/>
  <text x="81" y="34" font-size="9" fill="#be123c">フェノールフタレイン (8.0–9.8)</text>
  <rect x="235" y="26" width="12" height="8" fill="#f59e0b" opacity="0.35"/>
  <text x="251" y="34" font-size="9" fill="#b45309">メチルオレンジ (3.1–4.4)</text>

  <!-- 图 1：強酸 + 強塩基 -->
  <text x="74" y="54" text-anchor="middle" font-size="10.5" font-weight="bold" fill="#1e293b">強酸 + 強塩基</text>
  <rect x="24" y="60" width="100" height="140" fill="#ffffff" stroke="#334155" stroke-width="1.5"/>
  <!-- PP 变色带 (pH 8.0-9.8 -> y=102 to 120) -->
  <rect x="25" y="102" width="98" height="18" fill="#f43f5e" opacity="0.28"/>
  <!-- MO 变色带 (pH 3.1-4.4 -> y=156 to 169) -->
  <rect x="25" y="156" width="98" height="13" fill="#f59e0b" opacity="0.32"/>
  <!-- pH=7 虚线 -->
  <line x1="24" y1="130" x2="124" y2="130" stroke="#94a3b8" stroke-dasharray="3,2" stroke-width="1"/>
  <!-- 滴定曲线 -->
  <path d="M 24 190 Q 68 188 74 176 L 74 84 Q 80 72 124 70" fill="none" stroke="#2563eb" stroke-width="2.2"/>
  <circle cx="74" cy="130" r="3" fill="#dc2626"/>
  <text x="96" y="138" font-size="8.5" fill="#dc2626">中和点=7</text>
  <text x="48" y="114" font-size="9" font-weight="bold" fill="#15803d">PP 可</text>
  <text x="96" y="166" font-size="9" font-weight="bold" fill="#15803d">MO 可</text>
  <text x="19" y="66" text-anchor="end" font-size="8.5" fill="#475569">14</text>
  <text x="19" y="133" text-anchor="end" font-size="8.5" fill="#475569">7</text>
  <text x="19" y="201" text-anchor="end" font-size="8.5" fill="#475569">0</text>
  <text x="74" y="213" text-anchor="middle" font-size="8.5" fill="#475569">10 mL</text>

  <!-- 图 2：弱酸 + 強塩基 -->
  <text x="210" y="54" text-anchor="middle" font-size="10.5" font-weight="bold" fill="#1e293b">弱酸 + 強塩基</text>
  <rect x="160" y="60" width="100" height="140" fill="#ffffff" stroke="#334155" stroke-width="1.5"/>
  <rect x="161" y="102" width="98" height="18" fill="#f43f5e" opacity="0.28"/>
  <rect x="161" y="156" width="98" height="13" fill="#f59e0b" opacity="0.32"/>
  <line x1="160" y1="130" x2="260" y2="130" stroke="#94a3b8" stroke-dasharray="3,2" stroke-width="1"/>
  <!-- 弱酸起点高(pH~3)，缓冲平缓区，中和点~8.5 -->
  <path d="M 160 170 Q 175 152 200 148 Q 210 144 210 115 L 210 86 Q 216 74 260 71" fill="none" stroke="#2563eb" stroke-width="2.2"/>
  <circle cx="210" cy="114" r="3" fill="#dc2626"/>
  <text x="234" y="126" text-anchor="middle" font-size="8.5" fill="#dc2626">中和点&gt;7</text>
  <text x="184" y="114" font-size="9" font-weight="bold" fill="#15803d">PP 可</text>
  <text x="234" y="166" text-anchor="middle" font-size="9" font-weight="bold" fill="#dc2626">MO 不可✕</text>
  <text x="210" y="213" text-anchor="middle" font-size="8.5" fill="#475569">10 mL</text>

  <!-- 图 3：強酸 + 弱塩基 -->
  <text x="346" y="54" text-anchor="middle" font-size="10.5" font-weight="bold" fill="#1e293b">強酸 + 弱塩基</text>
  <rect x="296" y="60" width="100" height="140" fill="#ffffff" stroke="#334155" stroke-width="1.5"/>
  <rect x="297" y="102" width="98" height="18" fill="#f43f5e" opacity="0.28"/>
  <rect x="297" y="156" width="98" height="13" fill="#f59e0b" opacity="0.32"/>
  <line x1="296" y1="130" x2="396" y2="130" stroke="#94a3b8" stroke-dasharray="3,2" stroke-width="1"/>
  <!-- 强酸起点低，中和点~5，弱碱终点低(pH~11) -->
  <path d="M 296 190 Q 340 188 346 176 L 346 122 Q 352 110 396 105" fill="none" stroke="#2563eb" stroke-width="2.2"/>
  <circle cx="346" cy="148" r="3" fill="#dc2626"/>
  <text x="370" y="143" text-anchor="middle" font-size="8.5" fill="#dc2626">中和点&lt;7</text>
  <text x="322" y="114" text-anchor="middle" font-size="9" font-weight="bold" fill="#dc2626">PP 不可✕</text>
  <text x="370" y="166" text-anchor="middle" font-size="9" font-weight="bold" fill="#15803d">MO 可</text>
  <text x="346" y="213" text-anchor="middle" font-size="8.5" fill="#475569">10 mL</text>

  <!-- 底部口诀 -->
  <rect x="24" y="224" width="372" height="26" rx="5" fill="#eff6ff" stroke="#bfdbfe"/>
  <text x="210" y="241" text-anchor="middle" font-size="10" font-weight="bold" fill="#1e40af">秒杀口诀：中和点显碱性 → 选酚酞(PP)；中和点显酸性 → 选甲基橙(MO)；中性 → 均可！</text>
</svg>

#### 【图解辅助 3：酸碱价数与中和点滴下量对比（原书 P.65 下半部分）】
- ① $0.1\text{ mol/L}$ 1 价强酸 $\text{HCl}$ $10\text{ mL}$ 用 $0.1\text{ mol/L}$ 1 价强碱 $\text{NaOH}$ 滴定 $\rightarrow$ 中和点 **$10\text{ mL}$**。
- ② $0.1\text{ mol/L}$ 1 价强酸 $\text{HCl}$ $10\text{ mL}$ 用 $0.1\text{ mol/L}$ 2 价强碱 $\text{Ca(OH)}_2$ 滴定 $\rightarrow$ 碱价数翻倍，所需体积减半，中和点 **$5\text{ mL}$**。
- ③ $0.1\text{ mol/L}$ 2 价强酸 $\text{H}_2\text{SO}_4$ $10\text{ mL}$ 用 $0.1\text{ mol/L}$ 1 价强碱 $\text{NaOH}$ 滴定 $\rightarrow$ 酸价数翻倍，所需体积翻倍，中和点 **$20\text{ mL}$**（且起点 $[\text{H}^+]$ 更高，起始 $\text{pH}$ 更低）。

<svg viewBox="0 0 420 260" xmlns="http://www.w3.org/2000/svg" style="max-width:100%;height:auto;background:#fafbfc;border:1px solid #e1e4e8;border-radius:8px;">
  <text x="210" y="20" text-anchor="middle" font-size="13" font-weight="bold" fill="#1e293b">価数と滴下量：三条滴定曲线对比（原书 P.65）</text>
  <!-- 坐标系 -->
  <rect x="52" y="34" width="210" height="176" fill="#ffffff" stroke="#334155" stroke-width="1.6"/>
  <line x1="52" y1="122" x2="262" y2="122" stroke="#94a3b8" stroke-dasharray="4,3" stroke-width="1.2"/>
  <text x="45" y="42" text-anchor="end" font-size="10" fill="#334155">14</text>
  <text x="45" y="125" text-anchor="end" font-size="10" fill="#334155">7</text>
  <text x="45" y="210" text-anchor="end" font-size="10" fill="#334155">0</text>
  <text x="34" y="30" font-size="10.5" font-weight="bold" fill="#334155">pH</text>
  <!-- x轴刻度: 5->92, 10->132, 20->212 -->
  <text x="92" y="224" text-anchor="middle" font-size="10" fill="#dc2626" font-weight="bold">5</text>
  <text x="132" y="224" text-anchor="middle" font-size="10" fill="#2563eb" font-weight="bold">10</text>
  <text x="212" y="224" text-anchor="middle" font-size="10" fill="#059669" font-weight="bold">20</text>
  <text x="157" y="242" text-anchor="middle" font-size="10.5" fill="#334155">塩基滴下量 (mL)</text>

  <!-- 曲线 ② (5 mL, Ca(OH)2 2价碱终点略高) -->
  <path d="M 52 197 Q 86 194 92 180 L 92 64 Q 98 50 262 46" fill="none" stroke="#dc2626" stroke-width="2.2"/>
  <circle cx="92" cy="122" r="3.5" fill="#dc2626"/>
  <text x="80" y="114" font-size="11" font-weight="bold" fill="#dc2626">②</text>

  <!-- 曲线 ① (10 mL, HCl + NaOH) -->
  <path d="M 52 197 Q 124 194 132 180 L 132 68 Q 138 56 262 52" fill="none" stroke="#2563eb" stroke-width="2.2"/>
  <circle cx="132" cy="122" r="3.5" fill="#2563eb"/>
  <text x="140" y="114" font-size="11" font-weight="bold" fill="#2563eb">①</text>

  <!-- 曲线 ③ (20 mL, H2SO4 起点更低) -->
  <path d="M 52 203 Q 204 198 212 182 L 212 68 Q 218 57 262 55" fill="none" stroke="#059669" stroke-width="2.2"/>
  <circle cx="212" cy="122" r="3.5" fill="#059669"/>
  <text x="220" y="114" font-size="11" font-weight="bold" fill="#059669">③</text>

  <!-- 右侧说明框 -->
  <rect x="274" y="42" width="136" height="162" rx="6" fill="#f8fafc" stroke="#cbd5e1"/>
  <text x="282" y="64" font-size="10.5" font-weight="bold" fill="#dc2626">② 中和点 = 5 mL</text>
  <text x="282" y="79" font-size="9.2" fill="#475569">HCl (1価) + Ca(OH)₂ (2価)</text>
  <text x="282" y="92" font-size="9" fill="#64748b">碱价数×2 → 体积÷2</text>

  <text x="282" y="116" font-size="10.5" font-weight="bold" fill="#2563eb">① 中和点 = 10 mL</text>
  <text x="282" y="131" font-size="9.2" fill="#475569">HCl (1価) + NaOH (1価)</text>
  <text x="282" y="144" font-size="9" fill="#64748b">同浓度同价 → 体积相等</text>

  <text x="282" y="168" font-size="10.5" font-weight="bold" fill="#059669">③ 中和点 = 20 mL</text>
  <text x="282" y="183" font-size="9.2" fill="#475569">H₂SO₄ (2価) + NaOH (1価)</text>
  <text x="282" y="196" font-size="9" fill="#64748b">酸价数×2 → 体积×2</text>
</svg>

---

### 3.5 例题 4：中和反应定量计算（原书 P.66 / PDF 第 67 页）

#### 【原题重现与翻译】
> **原文**：
> (1) $0.10\text{ mol/L}$ の硫酸 $30\text{ mL}$ と中和する $0.15\text{ mol/L}$ の水酸化ナトリウム水溶液は何 $\text{mL}$ か。
> (2) 固体の水酸化カルシウム $0.37\text{ g}$ と中和する $0.10\text{ mol/L}$ の塩酸は何 $\text{mL}$ か。$\text{Ca(OH)}_2 = 74$
> (3) $0.10\text{ mol/L}$ の塩酸と $0.10\text{ mol/L}$ の硫酸が計 $30\text{ mL}$ ある。この中和に $0.10\text{ mol/L}$ の水酸化ナトリウム水溶液 $50\text{ mL}$ を要した。最初にあった塩酸と硫酸はそれぞれ何 $\text{mL}$ か。
> (4) $0.30\text{ mol/L}$ の塩酸 $10\text{ mL}$ と $0.10\text{ mol/L}$ の水酸化ナトリウム水溶液 $10\text{ mL}$ の混合溶液の $\text{pH}$ を求めよ。
>
> **译文**：
> (1) 与 $0.10\text{ mol/L}$ 硫酸 $30\text{ mL}$ 中和的 $0.15\text{ mol/L}$ 氢氧化钠水溶液为多少 $\text{mL}$？
> (2) 与 $0.37\text{ g}$ 固体氢氧化钙中和的 $0.10\text{ mol/L}$ 盐酸为多少 $\text{mL}$？（$\text{Ca(OH)}_2 = 74$）
> (3) 有 $0.10\text{ mol/L}$ 盐酸与 $0.10\text{ mol/L}$ 硫酸共 $30\text{ mL}$。中和该混合液需 $0.10\text{ mol/L}$ 氢氧化钠水溶液 $50\text{ mL}$。最初的盐酸与硫酸各有多少 $\text{mL}$？
> (4) 求 $0.30\text{ mol/L}$ 盐酸 $10\text{ mL}$ 与 $0.10\text{ mol/L}$ 氢氧化钠水溶液 $10\text{ mL}$ 混合后的 $\text{pH}$。

#### 【考点定位】
中和反应物质的量守恒 $acV = bc'V'$、固体碱中和、混合酸列方程组、过量酸碱混合求 $\text{pH}$。

#### 【分步标准解答】

**(1) 硫酸与 $\text{NaOH}$ 中和**
- 设 $\text{NaOH}$ 水溶液体积为 $V\text{ [mL]}$。由 $n(\text{H}^+) = n(\text{OH}^-)$：
  $$2 \times 0.10\text{ mol/L} \times \frac{30}{1000}\text{ L} = 1 \times 0.15\text{ mol/L} \times \frac{V}{1000}\text{ L}$$
- 解得 $V = \dfrac{6.0}{0.15} = 40\text{ mL}$。

**(2) 固体 $\text{Ca(OH)}_2$ 与盐酸中和**
- 设盐酸体积为 $V\text{ [mL]}$。$\text{Ca(OH)}_2$ 是 2 价碱，其物质的量为 $\dfrac{0.37\text{ g}}{74\text{ g/mol}} = 5.0 \times 10^{-3}\text{ mol}$。
- 由 $n(\text{H}^+) = n(\text{OH}^-)$：
  $$1 \times 0.10\text{ mol/L} \times \frac{V}{1000}\text{ L} = 2 \times \frac{0.37\text{ g}}{74\text{ g/mol}} = 1.0 \times 10^{-2}\text{ mol}$$
- 解得 $V = 100\text{ mL}$（有效数字 2 位写作 $1.0 \times 10^2\text{ mL}$，原书作 $100\text{ mL}$）。

**(3) 混合酸中和（二元一次方程组）**
- 设最初盐酸体积为 $V_1\text{ [mL]}$，硫酸体积为 $V_2\text{ [mL]}$。依题意列方程组：
  $$\begin{cases} V_1 + V_2 = 30 \\ 1 \times 0.10 \times \dfrac{V_1}{1000} + 2 \times 0.10 \times \dfrac{V_2}{1000} = 1 \times 0.10 \times \dfrac{50}{1000} \end{cases}$$
- 第二式两边同除以 $\dfrac{0.10}{1000}$ 得 $V_1 + 2V_2 = 50$。
- 与第一式相减得 $V_2 = 20\text{ mL}$，代回得 $V_1 = 10\text{ mL}$。

**(4) 酸过量混合液的 $\text{pH}$**
- 先比较 $\text{H}^+$ 与 $\text{OH}^-$ 的物质的量：
  - $n(\text{H}^+) = 1 \times 0.30 \times \dfrac{10}{1000} = 3.0 \times 10^{-3}\text{ mol}$
  - $n(\text{OH}^-) = 1 \times 0.10 \times \dfrac{10}{1000} = 1.0 \times 10^{-3}\text{ mol}$
- 酸过量，剩余 $\text{H}^+$ 浓度（**切记除以混合总体积 $20\text{ mL}$！**）：
  $$[\text{H}^+] = \frac{1 \times 0.30 \times \dfrac{10}{1000} - 1 \times 0.10 \times \dfrac{10}{1000}}{\dfrac{10}{1000} + \dfrac{10}{1000}} = \frac{2.0 \times 10^{-3}\text{ mol}}{20 \times 10^{-3}\text{ L}} = 1.0 \times 10^{-1}\text{ mol/L}$$
- 因此 $\text{pH} = -\log_{10}(1.0 \times 10^{-1}) = 1$（或 $1.0$）。
> 💡 **讲师批注**：第 (4) 题最常犯的错误是忘记体积翻倍（直接 $0.30 - 0.10 = 0.20$）！任何两种溶液混合求浓度，**必须除以总体积 $V_1 + V_2$**！

#### 【最终答案】
**(1) $40\text{ mL}$　(2) $100\text{ mL}$　(3) 塩酸 $10\text{ mL}$、硫酸 $20\text{ mL}$　(4) $\text{pH} = 1$**

---

### 3.6 核心机理图解：缓冲溶液的抗酸抗碱机制（原书 P.67 / PDF 第 68 页）

<svg viewBox="0 0 420 260" xmlns="http://www.w3.org/2000/svg" style="max-width:100%;height:auto;background:#fafbfc;border:1px solid #e1e4e8;border-radius:8px;">
  <defs>
    <marker id="arrRed" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#dc2626"/>
    </marker>
    <marker id="arrBlue" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#2563eb"/>
    </marker>
  </defs>
  <text x="210" y="20" text-anchor="middle" font-size="12.5" font-weight="bold" fill="#1e293b">緩衝液の仕組み（酢酸－酢酸ナトリウム水溶液）</text>

  <!-- 中央缓冲池 -->
  <rect x="95" y="34" width="230" height="58" rx="10" fill="#eff6ff" stroke="#3b82f6" stroke-width="1.8"/>
  <text x="210" y="54" text-anchor="middle" font-size="11" font-weight="bold" fill="#1e3a8a">溶液中多量共存的两大“储备库”</text>
  <rect x="110" y="62" width="90" height="22" rx="4" fill="#dbeafe" stroke="#2563eb"/>
  <text x="155" y="77" text-anchor="middle" font-size="10.5" font-weight="bold" fill="#1d4ed8">CH₃COOH (多量)</text>
  <rect x="220" y="62" width="90" height="22" rx="4" fill="#fee2e2" stroke="#dc2626"/>
  <text x="265" y="77" text-anchor="middle" font-size="10.5" font-weight="bold" fill="#b91c1c">CH₃COO⁻ (多量)</text>

  <!-- 左侧：加入少量の塩基 (OH-) -->
  <path d="M 135 94 L 105 124" stroke="#2563eb" stroke-width="2" marker-end="url(#arrBlue)"/>
  <rect x="14" y="128" width="186" height="90" rx="8" fill="#f0f9ff" stroke="#7dd3fc" stroke-width="1.5"/>
  <text x="107" y="146" text-anchor="middle" font-size="10.5" font-weight="bold" fill="#0369a1">加入少量碱 (OH⁻) 时</text>
  <text x="107" y="166" text-anchor="middle" font-size="10" font-weight="bold" fill="#1e293b">CH₃COOH + OH⁻ → CH₃COO⁻ + H₂O</text>
  <text x="107" y="185" text-anchor="middle" font-size="9.5" fill="#475569">弱酸分子“吃掉”外来的 OH⁻</text>
  <text x="107" y="203" text-anchor="middle" font-size="9.5" font-weight="bold" fill="#0284c7">→ [OH⁻] 增幅被缓和，pH 几乎不变</text>

  <!-- 右侧：加入少量の酸 (H+) -->
  <path d="M 285 94 L 315 124" stroke="#dc2626" stroke-width="2" marker-end="url(#arrRed)"/>
  <rect x="220" y="128" width="186" height="90" rx="8" fill="#fef2f2" stroke="#fca5a5" stroke-width="1.5"/>
  <text x="313" y="146" text-anchor="middle" font-size="10.5" font-weight="bold" fill="#b91c1c">加入少量酸 (H⁺) 时</text>
  <text x="313" y="166" text-anchor="middle" font-size="10" font-weight="bold" fill="#1e293b">CH₃COO⁻ + H⁺ → CH₃COOH</text>
  <text x="313" y="185" text-anchor="middle" font-size="9.5" fill="#475569">醋酸根“抓走”外来的 H⁺</text>
  <text x="313" y="203" text-anchor="middle" font-size="9.5" font-weight="bold" fill="#dc2626">→ [H⁺] 增幅被缓和，pH 几乎不变</text>

  <!-- 底部类比 -->
  <rect x="14" y="226" width="392" height="24" rx="5" fill="#f8fafc" stroke="#cbd5e1"/>
  <text x="210" y="242" text-anchor="middle" font-size="9.8" fill="#334155">同理（NH₃ + NH₄Cl）：加 H⁺ 时 NH₃ + H⁺ → NH₄⁺；加 OH⁻ 时 NH₄⁺ + OH⁻ → NH₃ + H₂O</text>
</svg>

---

### 3.7 例题 5：难溶盐溶解度积 $K_{\text{sp}}$ 与同离子效应（原书 P.69 / PDF 第 70 页）

#### 【原题重现与翻译】
> **原文**：$\text{PbCl}_2$ の溶解度積を $K_{\text{sp}} = [\text{Pb}^{2+}][\text{Cl}^-]^2 = 3.2 \times 10^{-8}\text{ [(mol/L)}^3\text{]}$ とする。
> (1) 水に対する $\text{PbCl}_2$ の溶解度（$\text{mol/L}$）を求めよ。ただし、溶解による体積変化は無視する。
> (2) $0.10\text{ mol/L}$ の $\text{HCl}$ に対する $\text{PbCl}_2$ の溶解度（$\text{mol/L}$）を求めよ。ただし、溶解による体積変化は無視する。
>
> **译文**：设 $\text{PbCl}_2$ 的溶度积 $K_{\text{sp}} = [\text{Pb}^{2+}][\text{Cl}^-]^2 = 3.2 \times 10^{-8}\text{ [(mol/L)}^3\text{]}$。
> (1) 求 $\text{PbCl}_2$ 在纯水中的溶解度（$\text{mol/L}$），忽略溶解引起的体积变化。
> (2) 求 $\text{PbCl}_2$ 在 $0.10\text{ mol/L}$ 盐酸中的溶解度（$\text{mol/L}$），忽略溶解引起的体积变化。

#### 【考点定位】
$\text{AB}_2$ 型难溶盐的溶解度与 $K_{\text{sp}}$ 换算、同离子效应（共通イオン効果）的近似计算。

#### 【分步标准解答】

**(1) 在纯水中的溶解度**
- 设 $\text{PbCl}_2$ 在纯水中的溶解度为 $x\text{ [mol/L]}$，列三段式：
  $$\text{PbCl}_2(\text{固}) \rightleftharpoons \text{Pb}^{2+} + 2\text{Cl}^-$$
  平衡时：$[\text{Pb}^{2+}] = x$，$[\text{Cl}^-] = 2x$。
- 代入溶度积表达式（**千万别漏掉系数 2 和平方！**）：
  $$K_{\text{sp}} = [\text{Pb}^{2+}][\text{Cl}^-]^2 = x \times (2x)^2 = 4x^3 = 3.2 \times 10^{-8}$$
- 化简求解：
  $$x^3 = \frac{3.2 \times 10^{-8}}{4} = 0.80 \times 10^{-8} = 8.0 \times 10^{-9} \quad\Rightarrow\quad x = 2.0 \times 10^{-3}\text{ mol/L}$$
> 💡 **讲师批注**：开立方根时，先把科学计数法的指数凑成 **3 的倍数**（如 $8.0 \times 10^{-9}$），开立方立刻得 $2.0 \times 10^{-3}$，绝不卡壳！

**(2) 在 $0.10\text{ mol/L HCl}$ 中的溶解度（同离子效应）**
- $\text{HCl}$ 是强酸完全电离：$\text{HCl} \rightarrow \text{H}^+ + \text{Cl}^-$，提供 $[\text{Cl}^-] = 0.10\text{ mol/L}$。
- 设 $\text{PbCl}_2$ 在该盐酸中的溶解度为 $y\text{ [mol/L]}$，则平衡时：
  $$[\text{Pb}^{2+}] = y, \quad [\text{Cl}^-] = 0.10 + 2y$$
- 由于同离子效应使 $y$ 极小（$2y \ll 0.10$），可近似 $[\text{Cl}^-] = 0.10 + 2y \fallingdotseq 0.10\text{ mol/L}$。
- 代入 $K_{\text{sp}}$：
  $$K_{\text{sp}} = [\text{Pb}^{2+}][\text{Cl}^-]^2 = y \times (0.10)^2 = 3.2 \times 10^{-8}$$
  $$y = \frac{3.2 \times 10^{-8}}{1.0 \times 10^{-2}} = 3.2 \times 10^{-6}\text{ mol/L}$$
  （检验：$2y = 6.4 \times 10^{-6} \ll 0.10$，近似完全合理！）
> 💡 **讲师批注**：对比 (1) 和 (2) 可以直观感受到**同离子效应**的威力——仅仅加入了 $0.10\text{ mol/L}$ 的 $\text{Cl}^-$，$\text{PbCl}_2$ 的溶解度就从 $2.0 \times 10^{-3}$ 暴跌了 600 多倍到 $3.2 \times 10^{-6}\text{ mol/L}$！

#### 【最终答案】
**(1) $2.0 \times 10^{-3}\text{ mol/L}$　(2) $3.2 \times 10^{-6}\text{ mol/L}$**

---

### 3.8 必背速查：EJU 高频氧化剂・还原剂半反应式总表（原书 P.71–P.72 / PDF 第 72–73 页）

> 💡 **讲师批注**：以下两张表是 EJU 化学**必须背到肌肉记忆**的核心资产！只要记住“反应前 $\rightarrow$ 反应后”的物质变化，半反应式可以现场 3 秒配平：**① 先配变价原子 $\rightarrow$ ② 用 $\text{H}_2\text{O}$ 配平氧 $\text{O}$ $\rightarrow$ ③ 用 $\text{H}^+$ 配平氢 $\text{H}$ $\rightarrow$ ④ 用 $e^-$ 配平电荷**。

#### ① 常见氧化剂（自身被还原，氧化数降低）
| 氧化剂（日文名） | 化学式 | 氧化数变化 | 半反应式 | 价数 |
| :--- | :---: | :---: | :--- | :---: |
| **ニクロム酸カリウム**（重铬酸钾） | $\text{K}_2\text{Cr}_2\text{O}_7$ | $\text{Cr}: +6 \to +3$ | $\text{Cr}_2\text{O}_7^{2-} + 14\text{H}^+ + 6e^- \rightarrow 2\text{Cr}^{3+} + 7\text{H}_2\text{O}$ | **6** |
| **過マンガン酸カリウム**（酸性） | $\text{KMnO}_4$ | $\text{Mn}: +7 \to +2$ | $\text{MnO}_4^- + 8\text{H}^+ + 5e^- \rightarrow \text{Mn}^{2+} + 4\text{H}_2\text{O}$ | **5** |
| **過マンガン酸カリウム**（中・碱性） | $\text{KMnO}_4$ | $\text{Mn}: +7 \to +4$ | $\text{MnO}_4^- + 2\text{H}_2\text{O} + 3e^- \rightarrow \text{MnO}_2 + 4\text{OH}^-$ | **3** |
| **希硝酸**（稀硝酸） | $\text{HNO}_3$ | $\text{N}: +5 \to +2$ | $\text{HNO}_3 + 3\text{H}^+ + 3e^- \rightarrow \text{NO} + 2\text{H}_2\text{O}$ | **3** |
| **濃硝酸**（浓硝酸） | $\text{HNO}_3$ | $\text{N}: +5 \to +4$ | $\text{HNO}_3 + \text{H}^+ + e^- \rightarrow \text{NO}_2 + \text{H}_2\text{O}$ | **1** |
| **熱濃硫酸**（热浓硫酸） | $\text{H}_2\text{SO}_4$ | $\text{S}: +6 \to +4$ | $\text{H}_2\text{SO}_4 + 2\text{H}^+ + 2e^- \rightarrow \text{SO}_2 + 2\text{H}_2\text{O}$ | **2** |
| **塩素**（氯气） | $\text{Cl}_2$ | $\text{Cl}: 0 \to -1$ | $\text{Cl}_2 + 2e^- \rightarrow 2\text{Cl}^-$ | **2** |
| **酸化マンガン(IV)**（二氧化锰） | $\text{MnO}_2$ | $\text{Mn}: +4 \to +2$ | $\text{MnO}_2 + 4\text{H}^+ + 2e^- \rightarrow \text{Mn}^{2+} + 2\text{H}_2\text{O}$ | **2** |
| **過酸化水素**（作氧化剂） | $\text{H}_2\text{O}_2$ | $\text{O}: -1 \to -2$ | $\text{H}_2\text{O}_2 + 2\text{H}^+ + 2e^- \rightarrow 2\text{H}_2\text{O}$ | **2** |
| **二酸化硫黄**（作氧化剂，遇 $\text{H}_2\text{S}$） | $\text{SO}_2$ | $\text{S}: +4 \to 0$ | $\text{SO}_2 + 4\text{H}^+ + 4e^- \rightarrow \text{S} + 2\text{H}_2\text{O}$ | **4** |
| **酸素 / オゾン**（氧气/臭氧） | $\text{O}_2 / \text{O}_3$ | $\text{O}: 0 \to -2$ | $\text{O}_2 \to 2\text{H}_2\text{O}$；$\text{O}_3 + 2\text{H}^+ + 2e^- \rightarrow \text{H}_2\text{O} + \text{O}_2$ | 4 / 2 |

#### ② 常见还原剂（自身被氧化，氧化数升高）
| 还原剂（日文名） | 化学式 | 氧化数变化 | 半反应式 | 价数 |
| :--- | :---: | :---: | :--- | :---: |
| **硫化水素**（硫化氢） | $\text{H}_2\text{S}$ | $\text{S}: -2 \to 0$ | $\text{H}_2\text{S} \rightarrow \text{S} + 2\text{H}^+ + 2e^-$ | **2** |
| **硫酸鉄(II)**（硫酸亚铁） | $\text{FeSO}_4$ | $\text{Fe}: +2 \to +3$ | $\text{Fe}^{2+} \rightarrow \text{Fe}^{3+} + e^-$ | **1** |
| **塩化スズ(II)**（氯化亚锡） | $\text{SnCl}_2$ | $\text{Sn}: +2 \to +4$ | $\text{Sn}^{2+} \rightarrow \text{Sn}^{4+} + 2e^-$ | **2** |
| **シュウ酸**（草酸） | $\text{H}_2\text{C}_2\text{O}_4$ | $\text{C}: +3 \to +4$ | $\text{H}_2\text{C}_2\text{O}_4 \rightarrow 2\text{CO}_2 + 2\text{H}^+ + 2e^-$ | **2** |
| **ヨウ化カリウム**（碘化钾） | $\text{KI}$ | $\text{I}: -1 \to 0$ | $2\text{I}^- \rightarrow \text{I}_2 + 2e^-$ | **1**（每 $\text{I}^-$） |
| **過酸化水素**（作还原剂，遇 $\text{KMnO}_4$） | $\text{H}_2\text{O}_2$ | $\text{O}: -1 \to 0$ | $\text{H}_2\text{O}_2 \rightarrow \text{O}_2 + 2\text{H}^+ + 2e^-$ | **2** |
| **二酸化硫黄**（作还原剂） | $\text{SO}_2$ | $\text{S}: +4 \to +6$ | $\text{SO}_2 + 2\text{H}_2\text{O} \rightarrow \text{SO}_4^{2-} + 4\text{H}^+ + 2e^-$ | **2** |
| **チオ硫酸イオン**（硫代硫酸根） | $\text{S}_2\text{O}_3^{2-}$ | $+2 \to +2.5$（特殊） | $2\text{S}_2\text{O}_3^{2-} \rightarrow \text{S}_4\text{O}_6^{2-} + 2e^-$ | **1** |

---

### 3.9 例题 6：氧化还原反应方程式三步配平实战（原书 P.73 / PDF 第 74 页）

#### 【原题重现与翻译】
> **原文**：酸化還元反応式の作り方（硫酸酸性条件下で $\text{KMnO}_4$ と $\text{H}_2\text{O}_2$ が反応する場合）
> ① 酸化剤・還元剤の半反応式を作る
> ② 両辺を足し合わせて $e^-$ 消去する
> ③ 省略されているイオンを補う
>
> **译文**：氧化还原反应方程式的书写三步法（硫酸酸性条件下 $\text{KMnO}_4$ 与 $\text{H}_2\text{O}_2$ 的反应）。

#### 【考点定位】
半反应式合并消去 $e^-$、补齐旁观离子（$\text{K}^+, \text{SO}_4^{2-}$）生成完整化学方程式。

#### 【分步标准解答】
- **第 1 步：写出氧化剂与还原剂的半反应式**
  - 还原剂（$\text{H}_2\text{O}_2$ 遇强氧化剂 $\text{KMnO}_4$ 时显还原性）：$\text{H}_2\text{O}_2 \rightarrow \text{O}_2 + 2\text{H}^+ + 2e^-$　……（式 ①）
  - 氧化剂（酸性 $\text{MnO}_4^-$）：$\text{MnO}_4^- + 8\text{H}^+ + 5e^- \rightarrow \text{Mn}^{2+} + 4\text{H}_2\text{O}$　……（式 ②）
- **第 2 步：消去电子 $e^-$ 得到离子方程式**
  - $2$ 和 $5$ 的最小公倍数为 $10$，故将 $(\text{式 ①}) \times 5 + (\text{式 ②}) \times 2$：
    $$2\text{MnO}_4^- + 5\text{H}_2\text{O}_2 + 16\text{H}^+ \rightarrow 2\text{Mn}^{2+} + 5\text{O}_2 + 8\text{H}_2\text{O} + 10\text{H}^+$$
  - 两边约去 $10\text{H}^+$，得净离子方程式：
    $$2\text{MnO}_4^- + 5\text{H}_2\text{O}_2 + 6\text{H}^+ \rightarrow 2\text{Mn}^{2+} + 5\text{O}_2 + 8\text{H}_2\text{O}$$
- **第 3 步：补齐省略的旁观离子（$\text{K}^+$ 与 $\text{SO}_4^{2-}$）**
  - 左边 $2\text{MnO}_4^-$ 来自 $2\text{KMnO}_4$（补入 $2\text{K}^+$）；$6\text{H}^+$ 来自 $3\text{H}_2\text{SO}_4$（补入 $3\text{SO}_4^{2-}$）。
  - 右边同样补入 $2\text{K}^+$ 和 $3\text{SO}_4^{2-}$，与 $2\text{Mn}^{2+}$ 组合生成 $2\text{MnSO}_4$ 和 $\text{K}_2\text{SO}_4$：
    $$2\text{KMnO}_4 + 5\text{H}_2\text{O}_2 + 3\text{H}_2\text{SO}_4 \rightarrow 2\text{MnSO}_4 + 5\text{O}_2 + 8\text{H}_2\text{O} + \text{K}_2\text{SO}_4$$
> 💡 **讲师批注**：在硫酸酸性条件下，**凡是左边的 $2n\text{H}^+$ 一律用 $n\text{H}_2\text{SO}_4$ 补齐**！左边补了多少个 $\text{K}^+$ 和 $\text{SO}_4^{2-}$，右边就严格按同样数量配成硫酸盐，绝不会配平出错！

#### 【最终答案】
**$2\text{KMnO}_4 + 5\text{H}_2\text{O}_2 + 3\text{H}_2\text{SO}_4 \rightarrow 2\text{MnSO}_4 + 5\text{O}_2 + 8\text{H}_2\text{O} + \text{K}_2\text{SO}_4$**

---

### 3.10 例题 7：氧化还原定量计算（原书 P.74 / PDF 第 75 页）

#### 【原题重现与翻译】
> **原文**：$0.20\text{ mol/L}$ の硫酸鉄(II) 水溶液 $15\text{ mL}$ と過不足なく反応する $0.10\text{ mol/L}$ の硫酸酸性のニクロム酸カリウム水溶液は何 $\text{mL}$ か。
>
> **译文**：与 $0.20\text{ mol/L}$ 硫酸亚铁（$\text{FeSO}_4$）水溶液 $15\text{ mL}$ 恰好完全反应的 $0.10\text{ mol/L}$ 硫酸酸性重铬酸钾（$\text{K}_2\text{Cr}_2\text{O}_7$）水溶液为多少 $\text{mL}$？

#### 【考点定位】
氧化还原滴定定量计算（电子得失守恒公式 $a c V = b c' V'$ vs 化学方程式系数比法）。

#### 【图解辅助 4：氧化还原电子转移与守恒可视化】

<svg viewBox="0 0 420 260" xmlns="http://www.w3.org/2000/svg" style="max-width:100%;height:auto;background:#fafbfc;border:1px solid #e1e4e8;border-radius:8px;">
  <defs>
    <marker id="arrOrange" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#ea580c"/>
    </marker>
  </defs>
  <text x="210" y="20" text-anchor="middle" font-size="12.5" font-weight="bold" fill="#1e293b">酸化還元滴定の電子授受モデル（K₂Cr₂O₇ + FeSO₄）</text>

  <!-- 左侧：还原剂 FeSO4 -->
  <rect x="20" y="54" width="150" height="126" rx="8" fill="#eff6ff" stroke="#3b82f6" stroke-width="1.8"/>
  <rect x="32" y="62" width="126" height="22" rx="4" fill="#2563eb"/>
  <text x="95" y="77" text-anchor="middle" font-size="10.5" font-weight="bold" fill="#ffffff">還元剤：FeSO₄ (1価)</text>
  <text x="95" y="106" text-anchor="middle" font-size="12" font-weight="bold" fill="#1e3a8a">Fe²⁺ → Fe³⁺ + e⁻</text>
  <text x="95" y="126" text-anchor="middle" font-size="10" fill="#1d4ed8">酸化数：+2 → +3（升・失・氧化）</text>
  <text x="95" y="146" text-anchor="middle" font-size="9.5" fill="#475569">0.20 mol/L × 15 mL</text>
  <text x="95" y="164" text-anchor="middle" font-size="9.5" font-weight="bold" fill="#1e40af">放出 e⁻ = 1 × 0.20 × 15/1000</text>

  <!-- 右侧：氧化剂 K2Cr2O7 -->
  <rect x="250" y="54" width="150" height="126" rx="8" fill="#fef2f2" stroke="#ef4444" stroke-width="1.8"/>
  <rect x="262" y="62" width="126" height="22" rx="4" fill="#dc2626"/>
  <text x="325" y="77" text-anchor="middle" font-size="10.5" font-weight="bold" fill="#ffffff">酸化剤：K₂Cr₂O₇ (6価)</text>
  <text x="325" y="106" text-anchor="middle" font-size="11" font-weight="bold" fill="#991b1b">Cr₂O₇²⁻ + 6e⁻ → 2Cr³⁺</text>
  <text x="325" y="126" text-anchor="middle" font-size="10" fill="#b91c1c">酸化数：+6 → +3（降・得・还原）</text>
  <text x="325" y="146" text-anchor="middle" font-size="9.5" fill="#475569">0.10 mol/L × V mL</text>
  <text x="325" y="164" text-anchor="middle" font-size="9.5" font-weight="bold" fill="#991b1b">受取 e⁻ = 6 × 0.10 × V/1000</text>

  <!-- 电子流动箭头 -->
  <path d="M 172 104 Q 210 72 246 104" fill="none" stroke="#ea580c" stroke-width="2.5" marker-end="url(#arrOrange)"/>
  <rect x="182" y="66" width="56" height="20" rx="10" fill="#ffedd5" stroke="#ea580c"/>
  <text x="210" y="80" text-anchor="middle" font-size="10.5" font-weight="bold" fill="#c2410c">e⁻ 转移</text>
  <text x="210" y="124" text-anchor="middle" font-size="9.5" font-weight="bold" fill="#ea580c">得失电子守恒</text>
  <text x="210" y="140" text-anchor="middle" font-size="11" font-weight="bold" fill="#0f172a">a·c·V = b·c'·V'</text>

  <!-- 底部公式条 -->
  <rect x="20" y="196" width="380" height="48" rx="6" fill="#f0fdf4" stroke="#86efac"/>
  <text x="210" y="215" text-anchor="middle" font-size="10.5" font-weight="bold" fill="#166534">6 × 0.10 × (V / 1000) = 1 × 0.20 × (15 / 1000)  ⇒  V = 5.0 mL</text>
  <text x="210" y="233" text-anchor="middle" font-size="9.5" fill="#15803d">口诀：降得还原氧化剂（6価），升失氧化还原剂（1価），无需写全反应式即可秒杀！</text>
</svg>

#### 【分步标准解答】

**［解法 1］电子得失守恒（价数法，EJU 考场推荐秒杀法）**
- 设重铬酸钾水溶液体积为 $V\text{ [mL]}$。
- $\text{K}_2\text{Cr}_2\text{O}_7$ 为 **6 价氧化剂**（$1\text{ mol}$ 接受 $6\text{ mol }e^-$），$\text{FeSO}_4$ 为 **1 价还原剂**（$1\text{ mol}$ 放出 $1\text{ mol }e^-$）。
- 由氧化剂得电子数 $=$ 还原剂失电子数（$a c V = b c' V'$）：
  $$6 \times 0.10\text{ mol/L} \times \frac{V}{1000}\text{ L} = 1 \times 0.20\text{ mol/L} \times \frac{15}{1000}\text{ L}$$
- 解得：$0.60 V = 3.0 \quad\Rightarrow\quad V = 5.0\text{ mL}$。

**［解法 2］完整化学方程式系数比法**
- 配平完整反应式：
  $$\text{K}_2\text{Cr}_2\text{O}_7 + 6\text{FeSO}_4 + 7\text{H}_2\text{SO}_4 \rightarrow \text{Cr}_2(\text{SO}_4)_3 + 3\text{Fe}_2(\text{SO}_4)_3 + 7\text{H}_2\text{O} + \text{K}_2\text{SO}_4$$
- 由物质的量之比 $\text{K}_2\text{Cr}_2\text{O}_7 : \text{FeSO}_4 = 1 : 6$：
  $$1 : 6 = \left(0.10 \times \frac{V}{1000}\right) : \left(0.20 \times \frac{15}{1000}\right)$$
- 解得 $V = 5.0\text{ mL}$。
> 💡 **讲师批注**：强烈建议 EJU 考场优先使用**解法 1**！因为不必浪费时间配平旁观离子和硫酸系数，只需记住常用氧化剂/还原剂的“价数”（$\text{K}_2\text{Cr}_2\text{O}_7=6$，$\text{KMnO}_4=5$，$\text{FeSO}_4=1$，$\text{H}_2\text{C}_2\text{O}_4=2$，$\text{H}_2\text{O}_2=2$），10 秒钟就能拿到满分！同时注意保留 **2 位有效数字**写作 $5.0\text{ mL}$。

#### 【最终答案】
**$5.0\text{ mL}$**

---

## 4. 全局术语与物质名录同步

本切片新增的全部日文化学核心词汇（酸碱平衡、滴定仪器与指示剂、难溶盐溶解平衡、氧化还原与常见氧化剂/还原剂等，含平假名与罗马音）已按分类同步写入 `/Users/baohan/Desktop/EJU/notes_化学/_glossary_parts/glossary_005.md`。
