# 《EJU 教材全解与备课讲义》数学 031（P451–P465）

> **对应源文件**：`work_math/ocr_md/ocr_031_p451-465.md`（第七章《確率と統計推測》之「正規分布（二項分布の正規近似・演習問題7）」「統計的な推測（母集団と標本・標本平均・標本比率・中心極限定理・大数の法則・母平均と母比率の推定・演習問題8）」及全书封底版权页）
> **视觉核对参考图**：`work_math/ref_imgs/page_0451.jpg` – `page_0463.jpg`（注：教材内页印刷页码为 450–462，PDF 页码为 451–463；第 464–465 页为封底与机构联系方式）

---

## 一、国内高中基础知识点唤醒与 EJU 考纲差异对比

本切片对应日本高中数学 **数学 B（確率分布と統計的な推測）** 的收官核心内容，涵盖 **连续型概率密度函数、正态分布与二项分布的正态近似、抽样调查与总体分布、样本均值与样本比例的分布、中心极限定理与大数定律、总体均值与总体比例的区间估计** 六大模块。

### 1.1 连续型随机变量与概率密度函数（連続型確率変数と確率密度関数）

- 设连续型随机变量 $X$ 的取值范围为 $a \le x \le b$，其**概率密度函数（確率密度関数）** $f(x)$ 满足以下三条基本性质：
  1. **非负性**：在定义区间上恒有 $f(x) \ge 0$；
  2. **归一性（全概率为 1）**：$\displaystyle \int_a^b f(x)\,dx = 1$；
  3. **区间概率等于面积**：对任意 $a \le c \le d \le b$，有
     $$P(c \le X \le d) = \int_c^d f(x)\,dx$$
     > 💡 连续型随机变量在单点处的概率恒为 $0$，即 $P(X = c) = 0$，因此 $P(c \le X \le d) = P(c < X < d)$。
- **期望、方差与标准差**：
  $$E(X) = \int_a^b x f(x)\,dx, \qquad V(X) = \int_a^b \{x - E(X)\}^2 f(x)\,dx = \int_a^b x^2 f(x)\,dx - \{E(X)\}^2, \qquad \sigma(X) = \sqrt{V(X)}$$

### 1.2 正态分布与二项分布的正态近似（正規分布・二項分布の正規近似）

- **正态分布 $N(m, \sigma^2)$ 的标准化（標準化）**：
  若 $X$ 服从正态分布 $N(m, \sigma^2)$，令
  $$Z = \frac{X - m}{\sigma}$$
  则 $Z$ 服从**标准正态分布（標準正規分布）** $N(0, 1)$。
- **日本标准正态分布表的定义**：
  日本教科书与考场附表给出的函数值是**半侧面积**：
  $$p(u) = P(0 \le Z \le u) = \frac{1}{\sqrt{2\pi}} \int_0^u e^{-\frac{t^2}{2}}\,dt \qquad (u \ge 0)$$
  利用对称性（左右对称、单侧总面积为 $0.5$），可快速换算任意区间概率：
  - $P(a \le Z \le b) = p(b) - p(a) \quad (0 \le a \le b)$
  - $P(-a \le Z \le b) = p(a) + p(b) \quad (a \ge 0,\; b \ge 0)$
  - $P(Z \ge a) = P(Z \le -a) = 0.5 - p(a) \quad (a \ge 0)$
  - $P(Z \le a) = 0.5 + p(a) \quad (a \ge 0)$
- **二项分布的正态近似（二項分布の正規近似）**：
  设 $X \sim B(n, p)$，其均值为 $np$，标准差为 $\sqrt{np(1-p)}$。当 $n$ 充分大时，标准化变量
  $$Z = \frac{X - np}{\sqrt{np(1-p)}}$$
  近似服从 $N(0, 1)$，即 $X$ 可近似视为服从正态分布 $N\bigl(np,\; np(1-p)\bigr)$。

### 1.3 总体、样本与抽样方式（母集団・標本・抽出）

- **全数调查（全数調査）** vs. **抽样调查（標本調査）**：普查（如国势调查）收集总体全部数据；抽样调查通过**随机抽样（無作為抽出）**（借助抽签或**随机数表 / 乱数表**）抽取**随机样本（無作為標本）**来推断总体。
- **总体分布（母集団分布）**：在容量为 $N$ 的总体中，变量 $x$ 取值 $x_k$ 的频数为 $f_k$，从总体中随机抽取 1 个元素，其值作为随机变量 $X$ 满足 $P(X = x_k) = \dfrac{f_k}{N}$，且：
  $$E(X) = m\;\text{（母平均）}, \qquad \sigma(X) = \sigma\;\text{（母標準偏差）}$$
- **有放回抽样（復元抽出）** vs. **无放回抽样（非復元抽出）**：
  - 有放回抽样抽出的 $n$ 个样本变量 $X_1, X_2, \dots, X_n$ **相互独立**且同分布；
  - 无放回抽样得到的 $X_1, X_2, \dots, X_n$ **不独立（従属）**，但当总体容量 $N$ 充分大且样本容量 $n$ 远小于 $N$（经验标准：$n \le \dfrac{N}{10}$）时，可**近似视为有放回抽样（相互独立）**。
  > ⚠️ **教材勘误提示**：原教材第 452 页（`page_0453.jpg`）`[9.3]` 处将復元抽出释义中的「毎回**もとに**戻しながら」误印为「毎回**ともに**戻しながら」，备课与授课时请留意修正。

### 1.4 样本均值、样本比例、中心极限定理与大数定律

- **样本均值（標本平均）** $\overline{X} = \dfrac{X_1 + X_2 + \cdots + X_n}{n}$ 与 **样本标准差（標本標準偏差）** $S = \sqrt{\dfrac{1}{n}\sum_{k=1}^n (X_k - \overline{X})^2}$：
  $$E(\overline{X}) = m, \qquad V(\overline{X}) = \frac{\sigma^2}{n}, \qquad \sigma(\overline{X}) = \frac{\sigma}{\sqrt{n}}$$
  > ⚠️ **教材勘误提示**：原教材第 456 页（`page_0457.jpg`）`[9.4]解説` 末尾公式 $\sigma(\overline{X}) = \dfrac{\sigma}{\sqrt{n}}$ 的分母 $\sqrt{n}$ 印刷残缺，实际应为 $\dfrac{\sigma}{\sqrt{n}}$。
- **样本比例（標本比率）** $R = \dfrac{T}{n}$（其中 $T \sim B(n, p)$ 为样本中具有特性 $A$ 的个体数，$p$ 为**总体比例 / 母比率**）：
  $$E(R) = p, \qquad V(R) = \frac{p(1-p)}{n}, \qquad \sigma(R) = \sqrt{\frac{p(1-p)}{n}}$$
  当 $n$ 较大时，$R$ 近似服从正态分布 $N\!\left(p,\; \dfrac{p(1-p)}{n}\right)$。
  > 💡 若定义示性变量 $X_k = 1$（具有特性 $A$）或 $0$（不具有），则 $R = \overline{X}$，样本比例本质上是样本均值的特例。
- **中心极限定理（中心極限定理）**：无论总体分布形态如何，只要 $X_1, \dots, X_n$ 独立同分布（均值 $m$、方差 $\sigma^2$），当 $n$ 充分大时，样本均值 $\overline{X}$ 近似服从正态分布 $N\!\left(m,\; \dfrac{\sigma^2}{n}\right)$，即
  $$Z = \frac{\overline{X} - m}{\sigma / \sqrt{n}} \;\text{近似服从}\; N(0, 1)$$
- **大数定律（大数の法則）**：随着样本容量 $n$ 增大，$\sigma(\overline{X}) = \dfrac{\sigma}{\sqrt{n}} \to 0$，$\overline{X}$ 的分布高度集中在 $m$ 附近，以趋近于 $1$ 的概率接近总体均值 $m$。

<svg viewBox="0 0 540 245" width="540" height="245" xmlns="http://www.w3.org/2000/svg" style="display:block;margin:12px auto;background:#fafbfd;border:1px solid #d9e2ec;border-radius:8px;">
  <defs>
    <marker id="arr-lln" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#334e68"/>
    </marker>
  </defs>
  <text x="270" y="22" text-anchor="middle" font-size="13" font-weight="bold" fill="#102a43">大数定律（大数の法則）：n 增大时样本均值分布向 m 集中（σ = 10）</text>
  <!-- Axes -->
  <line x1="45" y1="200" x2="500" y2="200" stroke="#334e68" stroke-width="1.5" marker-end="url(#arr-lln)"/>
  <line x1="270" y1="210" x2="270" y2="36" stroke="#9fb3c8" stroke-width="1.2" stroke-dasharray="4,3"/>
  <text x="506" y="204" font-size="13" font-style="italic" fill="#102a43">x̄</text>
  <text x="270" y="224" text-anchor="middle" font-size="13" font-weight="bold" fill="#102a43">m</text>
  <!-- n = 100 (wide, low, sigma_bar = 1) -->
  <path d="M 65 198 C 120 197, 165 186, 200 165 C 230 148, 250 140, 270 140 C 290 140, 310 148, 340 165 C 375 186, 420 197, 475 198" fill="none" stroke="#3b82f6" stroke-width="2.2"/>
  <text x="382" y="166" font-size="12" font-weight="bold" fill="#2563eb">n = 100 (σ/√n = 1)</text>
  <!-- n = 400 (medium, sigma_bar = 0.5) -->
  <path d="M 140 199 C 185 198, 215 178, 235 138 C 250 108, 260 95, 270 95 C 280 95, 290 108, 305 138 C 325 178, 355 198, 400 199" fill="none" stroke="#10b981" stroke-width="2.2"/>
  <text x="332" y="114" font-size="12" font-weight="bold" fill="#059669">n = 400 (σ/√n = 0.5)</text>
  <!-- n = 900 (narrow, tall, sigma_bar = 1/3) -->
  <path d="M 185 199 C 218 198, 236 172, 248 115 C 257 72, 263 48, 270 48 C 277 48, 283 72, 292 115 C 304 172, 322 198, 355 199" fill="none" stroke="#ef4444" stroke-width="2.4"/>
  <text x="302" y="64" font-size="12" font-weight="bold" fill="#dc2626">n = 900 (σ/√n = 1/3)</text>
</svg>

### 1.5 区间估计：总体均值与总体比例的置信区间（母平均・母比率の推定）

当样本容量 $n$ 充分大时（若总体本身服从正态分布，则总体均值估计对任意 $n$ 均精确成立）：
- **总体均值 $m$ 的置信区间（母平均の信頼区間）**：
  - 置信度 $95\%$（$c = 1.96$）：$\left[\overline{X} - 1.96 \cdot \dfrac{\sigma}{\sqrt{n}},\;\; \overline{X} + 1.96 \cdot \dfrac{\sigma}{\sqrt{n}}\right]$
  - 置信度 $99\%$（$c = 2.58$）：$\left[\overline{X} - 2.58 \cdot \dfrac{\sigma}{\sqrt{n}},\;\; \overline{X} + 2.58 \cdot \dfrac{\sigma}{\sqrt{n}}\right]$
  - 一般置信度 $100(1-\alpha)\%$（满足 $2p(c) = 1-\alpha$）：$\left[\overline{X} - c \cdot \dfrac{\sigma}{\sqrt{n}},\;\; \overline{X} + c \cdot \dfrac{\sigma}{\sqrt{n}}\right]$
- **总体比例 $p$ 的置信区间（母比率の信頼区間）**（由大数定律用 $R$ 替换标准差中的 $p$）：
  - 置信度 $95\%$：$\left[R - 1.96\sqrt{\dfrac{R(1-R)}{n}},\;\; R + 1.96\sqrt{\dfrac{R(1-R)}{n}}\right]$
  - 置信度 $99\%$：$\left[R - 2.58\sqrt{\dfrac{R(1-R)}{n}},\;\; R + 2.58\sqrt{\dfrac{R(1-R)}{n}}\right]$
  > ⚠️ **教材勘误提示**：原教材第 453 页（`page_0454.jpg`）`[9.9] 母比率の推定` 误将「母比率 $p$ に対する」印成了「**母平均 $m$ にたいする**」；此外第 458 页（`page_0459.jpg`）`[9.8]解説` 中「区間 $\overline{X}-1.96\cdot\frac{\sigma}{\sqrt{n}} \le x \le \overline{X}+1.96\cdot\frac{\sigma}{\sqrt{n}}$」处的 $x$ 应理解为 $m$ 所落入的区间端点表示。

### 1.6 国内高中 vs. 日本 EJU 考纲差异与符号习惯

| 对比维度 | 国内高中习惯 | 日本高中 / EJU 习惯 | 备课/应试提醒 |
| :--- | :--- | :--- | :--- |
| **标准正态分布表** | 查累积分布函数 $\Phi(u) = P(Z \le u)$ | 查半侧面积 $p(u) = P(0 \le Z \le u)$ | **最高频坑点！** 查表值最大仅为 $0.5$，求 $P(Z \le u)$ 必须加 $0.5$，求 $P(Z \ge u)$ 必须用 $0.5$ 减 |
| **样本标准差公式** | 高中多用分母 $n$，大学强调无偏分母 $n-1$ | 数学 B 统一定义 $S = \sqrt{\frac{1}{n}\sum (X_k - \overline{X})^2}$ | 本节区间估计直接沿用总体 $\sigma$ 或大样本替换，不考 $t$ 分布 |
| **区间估计与大数定律** | 属大学《概率论与数理统计》内容，高中不考 | 属日本**数学 B** 选修内容（注：现行 EJU 数学出题范围**不含**数学 B 的统计推断，但部分私立大学校内考及共通测试必考） | 国内背景学生几乎零基础，务必讲清「随机区间覆盖固定参数 $m$」的概率含义 |
| **置信区间的记法** | 多写为闭区间 $[a, b]$ | 既可写闭区间 $[a, b]$，也常直接写不等式 $a \le m \le b$ | 两种写法在日文解答中均标准有效，注意按题意保留小数位数 |
| **总体均值符号** | 常用 $\mu$ | 常用 **$m$**，标准差用 $\sigma$ | 正态分布多记作 $N(m, \sigma^2)$ 而非 $N(\mu, \sigma^2)$ |

---

## 二、日文核心词汇与公式假名注音

### 2.1 本切片日文核心词汇

- 正規分布（せいきぶんぷ / seiki bunpu） — 正态分布
- 標準正規分布（ひょうじゅんせいきぶんぷ / hyoujun seiki bunpu） — 标准正态分布
- 正規近似（せいききんじ / seiki kinji） — 正态近似（二项分布的正态近似）
- 二項分布（にこうぶんぷ / nikou bunpu） — 二项分布
- 確率変数（かくりつへんすう / kakuritsu hensuu） — 随机变量
- 確率分布（かくりつぶんぷ / kakuritsu bunpu） — 概率分布
- 確率密度関数（かくりつみつどかんすう / kakuritsu mitsudo kansuu） — 概率密度函数
- 期待値（きたいち / kitaichi） — 数学期望（期望值）
- 分散（ぶんさん / bunsan） — 方差
- 標準偏差（ひょうじゅんへんさ / hyoujun hensa） — 标准差
- 標準化（ひょうじゅんか / hyoujunka） — 标准化
- 正規分布表（せいきぶんぷひょう / seiki bunpuhyou） — 标准正态分布表
- 統計的な推測（とうけいてきなすいそく / toukeiteki na suisoku） — 统计推断（统计推测）
- 全数調査（ぜんすうちょうさ / zensuu chousa） — 普查（全数调查）
- 標本調査（ひょうほんちょうさ / hyouhon chousa） — 抽样调查（样本调查）
- 母集団（ぼしゅうだん / boshuudan） — 总体（母集团）
- 標本（ひょうほん / hyouhon） — 样本
- 抽出（ちゅうしゅつ / chuushutsu） — 抽样、抽取
- 無作為抽出（むさくいちゅうしゅつ / musakui chuushutsu） — 随机抽样
- 無作為標本（むさくいひょうほん / musakui hyouhon） — 随机样本
- 乱数表（らんすうひょう / ransuuhyou） — 随机数表
- 母集団の大きさ（ぼしゅうだんのおおきさ / boshuudan no ookisa） — 总体容量（总体大小 $N$）
- 標本の大きさ（ひょうほんのおおきさ / hyouhon no ookisa） — 样本容量（样本大小 $n$）
- 変量（へんりょう / henryou） — 变量（统计学观测变量）
- 母集団分布（ぼしゅうだんぶんぷ / boshuudan bunpu） — 总体分布
- 母平均（ぼへいきん / boheikin） — 总体均值（母平均）
- 母標準偏差（ぼひょうじゅんへんさ / bohyoujun hensa） — 总体标准差（母标准差）
- 度数（どすう / dosuu） — 频数（度数）
- 階級値（かいきゅうち / kaikyuuchi） — 组中值（阶级值）
- 同時分布（どうじぶんぷ / douji bunpu） — 联合分布（同时分布）
- 従属（じゅうぞく / juuzoku） — 相依、不独立（从属）
- 標本平均（ひょうほんへいきん / hyouhon heikin） — 样本均值
- 標本標準偏差（ひょうほんひょうじゅんへんさ / hyouhon hyoujun hensa） — 样本标准差
- 母比率（ぼひりつ / bohiritsu） — 总体比例（母比率）
- 標本比率（ひょうほんひりつ / hyouhon hiritsu） — 样本比例（样本比率）
- 中心極限定理（ちゅうしんきょくげんていり / chuushin kyokugen teiri） — 中心极限定理
- 大数の法則（たいすうのほうそく / taisuu no housoku） — 大数定律（大数法则）
- 推定（すいてい / suitei） — 估计、推断
- 信頼度（しんらいど / shinraido） — 置信度（置信水平）
- 信頼区間（しんらいくかん / shinrai kukan） — 置信区间
- 信頼区間の幅（しんらいくかんのはば / shinrai kukan no haba） — 置信区间的宽度

### 2.2 核心公式的日本课堂口语读法

1. **正态分布记法与标准化** $X$ は $N(m, \sigma^2)$ に従う、$Z = \dfrac{X - m}{\sigma}$
   - 课堂读法：**エックスは エヌ かっこ エム カンマ シグマのにじょう かっことじ に したがう。ゼット イコール シグマぶんの エックス ひく エム**
   - 备注：$\sigma$ 读作 **シグマ（shiguma）**；「に従う（にしたがう）」即「服从……分布」。
2. **样本均值的期望与标准差** $E(\overline{X}) = m,\; \sigma(\overline{X}) = \dfrac{\sigma}{\sqrt{n}}$
   - 课堂读法：**イー かっこ エックスバー かっことじ イコール エム、シグマ かっこ エックスバー かっことじ イコール ルートエヌ ぶんの シグマ**
   - 备注：$\overline{X}$ 读作 **エックスバー（ekkusu baa）**。
3. **样本比例的标准差** $\sigma(R) = \sqrt{\dfrac{p(1-p)}{n}}$
   - 课堂读法：**シグマ かっこ アール かっことじ イコール ルート エヌぶんの ピー かっこ いち ひく ピー かっことじ**
4. **总体均值 $95\%$ 置信区间** $\left[\overline{X} - 1.96 \cdot \dfrac{\sigma}{\sqrt{n}},\; \overline{X} + 1.96 \cdot \dfrac{\sigma}{\sqrt{n}}\right]$
   - 课堂读法：**エックスバー ひく いってんきゅうろく かける ルートエヌぶんのシグマ から、エックスバー たす いってんきゅうろく かける ルートエヌぶんのシグマ まで**
   - 备注：小数读法逐位报出，如 $1.96$ 读作 **いってん きゅう ろく**，$2.58$ 读作 **にてん ご はち**。

---

## 三、逐题深度解析（不可跳步）

> 📌 **标准正态分布表常用值速查**（本讲义全部计算均严格对应日本高中数学 B 标准正态分布表 $p(u) = P(0 \le Z \le u)$）：
> $p(0.30)=0.1179$，$p(0.50)=0.1915$，$p(0.57)=0.2157$，$p(0.76)=0.2764$，$p(1.00)=0.3413$，$p(1.09)=0.3621$，$p(1.50)=0.4332$，$p(1.64)=0.4495$，$p(1.65)=0.4505$，$p(1.75)=0.4599$，$p(1.80)=0.4641$，$p(1.96)=0.4750$，$p(2.00)=0.4772$，$p(2.58)=0.4951$，$p(3.00)=0.4987$。

---

### 演習問題 7（確率密度関数・正規分布）

#### 演習問題 7-(1)
- **【原题重现与翻译】**
  - 原题：確率変数 $X$ の確率密度関数 $f(x)$ が $f(x) = \dfrac{1}{2}x$ ($0 \le x \le 2$) で与えられているとき、次の確率を求めよ。
    $[1]\; P(0 \le X \le 2) \qquad [2]\; P(0 \le X \le 0.8) \qquad [3]\; P(0.5 \le X \le 1.5)$
  - 中文：已知随机变量 $X$ 的概率密度函数为 $f(x) = \dfrac{1}{2}x$（$0 \le x \le 2$），求下列概率：$[1]\; P(0 \le X \le 2)$；$[2]\; P(0 \le X \le 0.8)$；$[3]\; P(0.5 \le X \le 1.5)$。
- **【考点定位】**
  - 连续型随机变量的概率密度函数性质、定积分（或几何面积）求区间概率。
- **【图解辅助（SVG 矢量图）】**

<svg viewBox="0 0 460 205" width="460" height="205" xmlns="http://www.w3.org/2000/svg" style="display:block;margin:10px auto;background:#fafbfd;border:1px solid #d9e2ec;border-radius:8px;">
  <defs>
    <marker id="arr71" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#334e68"/>
    </marker>
  </defs>
  <!-- Left plot: [2] 0 <= x <= 0.8 -->
  <text x="115" y="18" text-anchor="middle" font-size="12" font-weight="bold" fill="#102a43">[2] P(0 ≤ X ≤ 0.8)</text>
  <line x1="25" y1="165" x2="210" y2="165" stroke="#334e68" stroke-width="1.3" marker-end="url(#arr71)"/>
  <line x1="40" y1="180" x2="40" y2="35" stroke="#334e68" stroke-width="1.3" marker-end="url(#arr71)"/>
  <polygon points="40,165 100,165 100,117" fill="#93c5fd" fill-opacity="0.65" stroke="#2563eb" stroke-width="1.2"/>
  <line x1="40" y1="165" x2="190" y2="45" stroke="#1e3a8a" stroke-width="2"/>
  <line x1="190" y1="45" x2="190" y2="165" stroke="#9fb3c8" stroke-dasharray="3,3"/>
  <text x="33" y="178" font-size="11" fill="#334e68">O</text>
  <text x="100" y="179" text-anchor="middle" font-size="11" fill="#1d4ed8">0.8</text>
  <text x="190" y="179" text-anchor="middle" font-size="11" fill="#334e68">2</text>
  <text x="30" y="49" text-anchor="end" font-size="11" fill="#334e68">1</text>
  <text x="148" y="64" font-size="11" fill="#1e3a8a">y = x/2</text>
  <!-- Right plot: [3] 0.5 <= x <= 1.5 -->
  <text x="345" y="18" text-anchor="middle" font-size="12" font-weight="bold" fill="#102a43">[3] P(0.5 ≤ X ≤ 1.5)</text>
  <line x1="250" y1="165" x2="435" y2="165" stroke="#334e68" stroke-width="1.3" marker-end="url(#arr71)"/>
  <line x1="265" y1="180" x2="265" y2="35" stroke="#334e68" stroke-width="1.3" marker-end="url(#arr71)"/>
  <polygon points="302.5,165 377.5,165 377.5,75 302.5,135" fill="#6ee7b7" fill-opacity="0.65" stroke="#059669" stroke-width="1.2"/>
  <line x1="265" y1="165" x2="415" y2="45" stroke="#1e3a8a" stroke-width="2"/>
  <line x1="415" y1="45" x2="415" y2="165" stroke="#9fb3c8" stroke-dasharray="3,3"/>
  <text x="258" y="178" font-size="11" fill="#334e68">O</text>
  <text x="302.5" y="179" text-anchor="middle" font-size="11" fill="#047857">0.5</text>
  <text x="377.5" y="179" text-anchor="middle" font-size="11" fill="#047857">1.5</text>
  <text x="415" y="179" text-anchor="middle" font-size="11" fill="#334e68">2</text>
  <text x="255" y="49" text-anchor="end" font-size="11" fill="#334e68">1</text>
</svg>

- **【分步标准解答】**
  - **$[1]$** $P(0 \le X \le 2)$：
    $$P(0 \le X \le 2) = \int_0^2 \frac{1}{2}x\,dx = \left[\frac{1}{4}x^2\right]_0^2 = \frac{1}{4} \cdot 2^2 - 0 = 1$$
    > 💡 讲师批注：区间 $[0, 2]$ 正是 $X$ 的全部取值范围，由概率密度函数的归一性可知全概率必为 $1$；也可直接算底为 $2$、高为 $1$ 的直角三角形面积 $\frac{1}{2} \times 2 \times 1 = 1$。
  - **$[2]$** $P(0 \le X \le 0.8)$：
    $$P(0 \le X \le 0.8) = \int_0^{0.8} \frac{1}{2}x\,dx = \left[\frac{1}{4}x^2\right]_0^{0.8} = \frac{1}{4} \times (0.8)^2 = \frac{1}{4} \times 0.64 = 0.16$$
    > 💡 讲师批注：几何验算：底为 $0.8$、高为 $f(0.8) = 0.4$ 的三角形面积 $\frac{1}{2} \times 0.8 \times 0.4 = 0.16$（或 $\frac{4}{25}$）。
  - **$[3]$** $P(0.5 \le X \le 1.5)$：
    $$P(0.5 \le X \le 1.5) = \int_{0.5}^{1.5} \frac{1}{2}x\,dx = \left[\frac{1}{4}x^2\right]_{0.5}^{1.5} = \frac{1}{4}\left\{(1.5)^2 - (0.5)^2\right\}$$
    $$= \frac{1}{4}(1.5 + 0.5)(1.5 - 0.5) = \frac{1}{4} \times 2 \times 1 = 0.5$$
    > 💡 讲师批注：用平方差公式 $(1.5)^2 - (0.5)^2 = 2 \times 1 = 2$ 口算最快，避免小数平方出错！几何上这是上底 $0.25$、下底 $0.75$、高 $1$ 的梯形，面积 $\frac{(0.25+0.75)\times 1}{2} = 0.5$。
- **【最终答案】**
  **$[1]\; 1$，$[2]\; 0.16$（$\dfrac{4}{25}$），$[3]\; 0.5$（$\dfrac{1}{2}$）**

---

#### 演習問題 7-(2)
- **【原题重现与翻译】**
  - 原题：確率変数 $X$ のとる値 $x$ の範囲が $0 \le x \le 3$ で、その確率密度が $f(x) = k(4 - x)$ で与えられている。このとき、正の定数 $k$ 値と確率 $P(1 \le X \le 2)$ を求めよ。
  - 中文：已知随机变量 $X$ 的取值范围是 $0 \le x \le 3$，其概率密度函数为 $f(x) = k(4 - x)$。求正的常数 $k$ 的值以及概率 $P(1 \le X \le 2)$。
- **【考点定位】**
  - 利用归一性 $\int_0^3 f(x)\,dx = 1$ 确定待定系数 $k$，再求指定区间的定积分。
- **【分步标准解答】**
  1. **求定数 $k$**：
     確率密度関数の性質より、全区間 $[0, 3]$ での積分値は $1$ であるから、
     $$\int_0^3 k(4 - x)\,dx = 1$$
     $$k \left[4x - \frac{1}{2}x^2\right]_0^3 = 1 \implies k \left(12 - \frac{9}{2}\right) = 1 \implies \frac{15}{2}k = 1 \implies k = \frac{2}{15}$$
     > 💡 讲师批注：检查非负性：当 $k = \frac{2}{15} > 0$ 且 $0 \le x \le 3$ 时，$4 - x \ge 1 > 0$，故 $f(x) > 0$ 恒成立。几何验算：梯形上底 $f(3) = k$、下底 $f(0) = 4k$、高 $3$，面积 $\frac{(4k+k)\times 3}{2} = \frac{15}{2}k = 1 \implies k = \frac{2}{15}$。
  2. **求確率 $P(1 \le X \le 2)$**：
     $$P(1 \le X \le 2) = \int_1^2 \frac{2}{15}(4 - x)\,dx = \frac{2}{15}\left[4x - \frac{1}{2}x^2\right]_1^2$$
     $$= \frac{2}{15}\left\{(8 - 2) - \left(4 - \frac{1}{2}\right)\right\} = \frac{2}{15}\left(6 - \frac{7}{2}\right) = \frac{2}{15} \cdot \frac{5}{2} = \frac{1}{3}$$
     > 💡 讲师批注：几何速算：$f(x) = k(4-x)$ 是一次函数，区间 $[1, 2]$ 恰好居于 $[0, 3]$ 的正中间，长度为全长的 $\frac{1}{3}$，由于梯形中位线高与全梯形中位线高相同（均在 $x = 1.5$ 处取得），面积比直接就是区间长度比 $\frac{1}{3}$！
- **【最终答案】**
  **$k = \dfrac{2}{15}$，$P(1 \le X \le 2) = \dfrac{1}{3}$**

---

#### 演習問題 7-(3)
- **【原题重现与翻译】**
  - 原题：確率変数 $X$ が区間 $0 \le x \le 6$ の任意の値を取ることができ、その確率密度関数が $f(x) = kx(6 - x)$ ($k$ は定数) で与えられている。このとき、$k = \Box$、確率 $P(2 \le X \le 5) = \Box$ である。また、期待値は $\Box$ で、標準偏差は $\Box$。
  - 中文：随机变量 $X$ 可取区间 $0 \le x \le 6$ 内的任意值，其概率密度函数为 $f(x) = kx(6 - x)$（$k$ 为常数）。此时，$k = \Box$，概率 $P(2 \le X \le 5) = \Box$；此外，期望为 $\Box$，标准差为 $\Box$。
- **【考点定位】**
  - 二次函数型概率密度函数的归一性（可结合 $1/6$ 面积公式速算）、区间概率、连续型随机变量的期望与标准差。
- **【图解辅助（SVG 矢量图）】**

<svg viewBox="0 0 420 205" width="420" height="205" xmlns="http://www.w3.org/2000/svg" style="display:block;margin:10px auto;background:#fafbfd;border:1px solid #d9e2ec;border-radius:8px;">
  <defs>
    <marker id="arr73" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#334e68"/>
    </marker>
  </defs>
  <text x="210" y="20" text-anchor="middle" font-size="12" font-weight="bold" fill="#102a43">f(x) = (1/36)x(6 − x)（关于 x = 3 对称）</text>
  <!-- Axes: x in [0,6] mapped to [60,360] (50px/unit), y in [0,0.25] mapped to [170,50] (480px/unit) -->
  <line x1="40" y1="170" x2="395" y2="170" stroke="#334e68" stroke-width="1.4" marker-end="url(#arr73)"/>
  <line x1="60" y1="185" x2="60" y2="35" stroke="#334e68" stroke-width="1.4" marker-end="url(#arr73)"/>
  <!-- Shaded region 2 <= x <= 5: x=2->160, y=8/36=0.222->63.3; x=3->210, y=0.25->50; x=5->310, y=5/36=0.139->103.3 -->
  <path d="M 160 170 L 160 63.3 Q 210 36.7 260 63.3 L 310 103.3 L 310 170 Z" fill="#bfdbfe" fill-opacity="0.7" stroke="none"/>
  <!-- Full parabola x=0..6: M 60 170 Q 210 -70 360 170 -->
  <path d="M 60 170 Q 210 -70 360 170" fill="none" stroke="#1d4ed8" stroke-width="2.2"/>
  <!-- Vertical lines -->
  <line x1="160" y1="63.3" x2="160" y2="170" stroke="#2563eb" stroke-width="1.2"/>
  <line x1="310" y1="103.3" x2="310" y2="170" stroke="#2563eb" stroke-width="1.2"/>
  <line x1="210" y1="50" x2="210" y2="170" stroke="#dc2626" stroke-width="1.2" stroke-dasharray="4,3"/>
  <!-- Labels -->
  <text x="53" y="183" font-size="11" fill="#334e68">0</text>
  <text x="160" y="185" text-anchor="middle" font-size="11" font-weight="bold" fill="#1d4ed8">2</text>
  <text x="210" y="185" text-anchor="middle" font-size="11" font-weight="bold" fill="#dc2626">3 = E(X)</text>
  <text x="310" y="185" text-anchor="middle" font-size="11" font-weight="bold" fill="#1d4ed8">5</text>
  <text x="360" y="185" text-anchor="middle" font-size="11" fill="#334e68">6</text>
  <text x="52" y="54" text-anchor="end" font-size="11" fill="#334e68">1/4</text>
  <text x="235" y="125" text-anchor="middle" font-size="12" font-weight="bold" fill="#1e40af">面積 = 2/3</text>
</svg>

- **【分步标准解答】**
  1. **求定数 $k$**：
     $$\int_0^6 kx(6 - x)\,dx = 1$$
     $$\int_0^6 (6x - x^2)\,dx = \left[3x^2 - \frac{1}{3}x^3\right]_0^6 = 3 \cdot 36 - \frac{216}{3} = 108 - 72 = 36$$
     よって、$36k = 1 \implies k = \dfrac{1}{36}$。
     > 💡 讲师批注：直接套用**$\frac{1}{6}$ 面积公式** $\int_0^6 x(6-x)\,dx = \frac{1}{6}(6 - 0)^3 = 36$，一秒可得 $k = \frac{1}{36}$！
  2. **求確率 $P(2 \le X \le 5)$**：
     $$P(2 \le X \le 5) = \frac{1}{36}\int_2^5 (6x - x^2)\,dx = \frac{1}{36}\left[3x^2 - \frac{1}{3}x^3\right]_2^5$$
     $$= \frac{1}{36}\left\{\left(3 \cdot 25 - \frac{125}{3}\right) - \left(3 \cdot 4 - \frac{8}{3}\right)\right\} = \frac{1}{36}\left\{(75 - 12) - \frac{125 - 8}{3}\right\}$$
     $$= \frac{1}{36}\left(63 - \frac{117}{3}\right) = \frac{1}{36}(63 - 39) = \frac{24}{36} = \frac{2}{3}$$
     > 💡 讲师批注：把同类项先合并（整数减整数 $75-12=63$，分数减分数 $\frac{125-8}{3}=39$），恰好能整除，计算量大幅降低。
  3. **求期待値 $E(X)$**：
     $$E(X) = \int_0^6 x f(x)\,dx = \frac{1}{36}\int_0^6 (6x^2 - x^3)\,dx = \frac{1}{36}\left[2x^3 - \frac{1}{4}x^4\right]_0^6$$
     $$= \frac{1}{36}\left(2 \cdot 216 - \frac{1296}{4}\right) = \frac{1}{36}(432 - 324) = \frac{108}{36} = 3$$
     > 💡 讲师批注：因为密度函数 $f(x) = \frac{1}{36}x(6-x)$ 的图像关于直线 $x = 3$ 轴对称，所以期望必然是 $E(X) = 3$！考试填空题可直接利用对称性秒答。
  4. **求分散 $V(X)$ 与標準偏差 $\sigma(X)$**：
     まず $E(X^2)$ を求める：
     $$E(X^2) = \int_0^6 x^2 f(x)\,dx = \frac{1}{36}\int_0^6 (6x^3 - x^4)\,dx = \frac{1}{36}\left[\frac{3}{2}x^4 - \frac{1}{5}x^5\right]_0^6$$
     $$= \frac{1}{36}\left(\frac{3}{2} \cdot 6^4 - \frac{1}{5} \cdot 6^5\right) = 6^2\left(\frac{3}{2} - \frac{6}{5}\right) = 36 \cdot \frac{3}{10} = \frac{54}{5}$$
     > 💡 讲师批注：先约去 $6^2 = 36$ 再提公因式，避免直接算 $6^5 = 7776$！

     よって、分散 $V(X)$ は
     $$V(X) = E(X^2) - \{E(X)\}^2 = \frac{54}{5} - 3^2 = \frac{54}{5} - \frac{45}{5} = \frac{9}{5}$$
     したがって、標準偏差 $\sigma(X)$ は
     $$\sigma(X) = \sqrt{V(X)} = \sqrt{\frac{9}{5}} = \frac{3}{\sqrt{5}} = \frac{3\sqrt{5}}{5}$$
- **【最终答案】**
  **$k = \dfrac{1}{36}$，$P(2 \le X \le 5) = \dfrac{2}{3}$，期待値 $3$，標準偏差 $\dfrac{3\sqrt{5}}{5}$**

---

#### 演習問題 7-(4)
- **【原题重现与翻译】**
  - 原题：確率変数 $Z$ が正規分布 $N(0, 1)$ に従うとき、次の確率を求めよ。
    $[1]\; P(0.3 \le Z \le 1.8) \qquad [2]\; P(Z \le -0.5)$
  - 中文：当随机变量 $Z$ 服从标准正态分布 $N(0, 1)$ 时，求下列概率：$[1]\; P(0.3 \le Z \le 1.8)$；$[2]\; P(Z \le -0.5)$。
  > ⚠️ **教材勘误提示**：原教材第 451 页（`page_0452.jpg`）将助词「$Z$ **が**正規分布」误印为「$Z$ **の**正規分布」。
- **【考点定位】**
  - 标准正态分布表的直接查表与对称性换算。
- **【图解辅助（SVG 矢量图）】**

<svg viewBox="0 0 480 185" width="480" height="185" xmlns="http://www.w3.org/2000/svg" style="display:block;margin:10px auto;background:#fafbfd;border:1px solid #d9e2ec;border-radius:8px;">
  <!-- Left: [1] 0.3 <= Z <= 1.8 -->
  <text x="120" y="18" text-anchor="middle" font-size="12" font-weight="bold" fill="#102a43">[1] P(0.3 ≤ Z ≤ 1.8)</text>
  <line x1="20" y1="150" x2="225" y2="150" stroke="#334e68" stroke-width="1.3"/>
  <line x1="120" y1="150" x2="120" y2="42" stroke="#9fb3c8" stroke-dasharray="3,3"/>
  <!-- Shaded 0.3 to 1.8 (center 120, scale 30px/unit -> 129 to 174) -->
  <path d="M 129 150 L 129 52 C 145 58, 158 100, 174 131 L 174 150 Z" fill="#93c5fd" fill-opacity="0.7"/>
  <!-- Bell curve -->
  <path d="M 30 149 C 60 148, 82 120, 96 80 C 106 54, 113 48, 120 48 C 127 48, 134 54, 144 80 C 158 120, 180 148, 210 149" fill="none" stroke="#1e3a8a" stroke-width="2"/>
  <line x1="129" y1="52" x2="129" y2="150" stroke="#2563eb" stroke-width="1.2"/>
  <line x1="174" y1="131" x2="174" y2="150" stroke="#2563eb" stroke-width="1.2"/>
  <text x="116" y="166" text-anchor="end" font-size="11" fill="#334e68">0</text>
  <text x="133" y="166" text-anchor="start" font-size="11" fill="#1d4ed8">0.3</text>
  <text x="174" y="166" text-anchor="middle" font-size="11" fill="#1d4ed8">1.8</text>
  <!-- Right: [2] Z <= -0.5 -->
  <text x="360" y="18" text-anchor="middle" font-size="12" font-weight="bold" fill="#102a43">[2] P(Z ≤ −0.5) = P(Z ≥ 0.5)</text>
  <line x1="255" y1="150" x2="460" y2="150" stroke="#334e68" stroke-width="1.3"/>
  <line x1="360" y1="150" x2="360" y2="42" stroke="#9fb3c8" stroke-dasharray="3,3"/>
  <!-- Shaded Z <= -0.5 (center 360, -0.5 -> 345) -->
  <path d="M 270 149 C 300 148, 322 120, 336 80 C 340 68, 343 60, 345 57 L 345 150 L 270 150 Z" fill="#fca5a5" fill-opacity="0.7"/>
  <!-- Bell curve -->
  <path d="M 270 149 C 300 148, 322 120, 336 80 C 346 54, 353 48, 360 48 C 367 48, 374 54, 384 80 C 398 120, 420 148, 450 149" fill="none" stroke="#1e3a8a" stroke-width="2"/>
  <line x1="345" y1="57" x2="345" y2="150" stroke="#dc2626" stroke-width="1.2"/>
  <text x="364" y="166" text-anchor="start" font-size="11" fill="#334e68">0</text>
  <text x="342" y="166" text-anchor="end" font-size="11" fill="#dc2626">−0.5</text>
</svg>

- **【分步标准解答】**
  - **$[1]$** $P(0.3 \le Z \le 1.8)$：
    $$P(0.3 \le Z \le 1.8) = P(0 \le Z \le 1.8) - P(0 \le Z \le 0.3) = p(1.8) - p(0.3)$$
    正規分布表より $p(1.8) = 0.4641$、$p(0.3) = 0.1179$ であるから、
    $$P(0.3 \le Z \le 1.8) = 0.4641 - 0.1179 = 0.3462$$
    > 💡 讲师批注：两端同在 $0$ 的右侧，用「大面积减去小面积」。
  - **$[2]$** $P(Z \le -0.5)$：
    正規分布曲線の対称性より、
    $$P(Z \le -0.5) = P(Z \ge 0.5) = 0.5 - P(0 \le Z \le 0.5) = 0.5 - p(0.5)$$
    正規分布表より $p(0.5) = 0.1915$ であるから、
    $$P(Z \le -0.5) = 0.5 - 0.1915 = 0.3085$$
    > 💡 讲师批注：画图最保险！左侧半边总面积为 $0.5$，挖掉 $[-0.5, 0]$ 的面积 $p(0.5)$ 即得尾部面积。
- **【最终答案】**
  **$[1]\; 0.3462$，$[2]\; 0.3085$**

---

#### 演習問題 7-(5)
- **【原题重现与翻译】**
  - 原题：確率変数 $X$ が正規分布 $N(36, 4^2)$ に従うとき、次の確率を求めよ。
    $[1]\; P(X \le 42) \qquad [2]\; P(30 \le X \le 38)$
  - 中文：当随机变量 $X$ 服从正态分布 $N(36, 4^2)$ 时，求下列概率：$[1]\; P(X \le 42)$；$[2]\; P(30 \le X \le 38)$。
  > ⚠️ **教材勘误提示**：原教材第 451 页（`page_0452.jpg`）题干误印为「確率変数 **$Z$ の**正規分布 $N(36, 4^2)$」，与小题中的 $X$ 冲突，应修正为「確率変数 **$X$ が**正規分布 $N(36, 4^2)$」。
- **【考点定位】**
  - 一般正态分布的标准化变换 $Z = \dfrac{X - m}{\sigma}$ 与查表计算。
- **【分步标准解答】**
  $X$ は正規分布 $N(36, 4^2)$ に従うから、平均 $m = 36$、標準偏差 $\sigma = 4$ である。
  $$Z = \frac{X - 36}{4}$$
  とおくと、$Z$ は標準正規分布 $N(0, 1)$ に従う。
  - **$[1]$** $P(X \le 42)$：
    $X = 42$ のとき $Z = \dfrac{42 - 36}{4} = \dfrac{6}{4} = 1.5$ であるから、
    $$P(X \le 42) = P(Z \le 1.5) = 0.5 + P(0 \le Z \le 1.5) = 0.5 + p(1.5)$$
    正規分布表より $p(1.5) = 0.4332$ であるから、
    $$P(X \le 42) = 0.5 + 0.4332 = 0.9332$$
    > 💡 讲师批注：$Z \le 1.5$ 包含 $Z \le 0$ 的整片左半侧（面积 $0.5$）以及 $[0, 1.5]$（面积 $p(1.5)$），故相加。
  - **$[2]$** $P(30 \le X \le 38)$：
    $X = 30$ のとき $Z = \dfrac{30 - 36}{4} = -1.5$、$X = 38$ のとき $Z = \dfrac{38 - 36}{4} = 0.5$ であるから、
    $$P(30 \le X \le 38) = P(-1.5 \le Z \le 0.5) = P(-1.5 \le Z \le 0) + P(0 \le Z \le 0.5)$$
    $$= p(1.5) + p(0.5) = 0.4332 + 0.1915 = 0.6247$$
    > 💡 讲师批注：跨过对称轴 $Z = 0$ 时（一负一正），直接把两边的 $p(|z|)$ 相加！
- **【最终答案】**
  **$[1]\; 0.9332$，$[2]\; 0.6247$**

---

#### 演習問題 7-(6)
- **【原题重现与翻译】**
  - 原题：ある高校における 3 年男子の身長 $X$ が、平均 $170.9\,\mathrm{cm}$、標準偏差 $5.4\,\mathrm{cm}$ の正規分布に従うものとする。このとき
    $[1]$ 身長 $175\,\mathrm{cm}$ 以上の生徒は何 $\%$ いるか。
    $[2]$ 身長 $165\,\mathrm{cm}$ 以上 $174\,\mathrm{cm}$ 以下の生徒は何 $\%$ いるか。
    $[3]$ 身長の高い方から $4\%$ の中に入るのは、約何 $\mathrm{cm}$ 以上の生徒か。
  - 中文：设某高中高三男生的身高 $X$ 服从平均 $170.9\,\mathrm{cm}$、标准差 $5.4\,\mathrm{cm}$ 的正态分布。问：
    $[1]$ 身高在 $175\,\mathrm{cm}$ 以上的学生占百分之几？
    $[2]$ 身高在 $165\,\mathrm{cm}$ 以上 $174\,\mathrm{cm}$ 以下的学生占百分之几？
    $[3]$ 进入身高前 $4\%$ 的大约是身高多少 $\mathrm{cm}$ 以上的学生？
- **【考点定位】**
  - 正态分布的实际应用：正向求概率（百分比）与逆向查表求分位点。
- **【图解辅助（SVG 矢量图）】**

<svg viewBox="0 0 420 185" width="420" height="185" xmlns="http://www.w3.org/2000/svg" style="display:block;margin:10px auto;background:#fafbfd;border:1px solid #d9e2ec;border-radius:8px;">
  <text x="210" y="18" text-anchor="middle" font-size="12" font-weight="bold" fill="#102a43">[3] 逆查表：右侧尾部面积 0.04 ⇔ 中央面积 p(u) = 0.46</text>
  <line x1="30" y1="145" x2="390" y2="145" stroke="#334e68" stroke-width="1.4"/>
  <line x1="210" y1="145" x2="210" y2="38" stroke="#9fb3c8" stroke-dasharray="4,3"/>
  <!-- Shaded 0 to u (u=1.75 -> 210 + 70 = 280) -->
  <path d="M 210 145 L 210 44 C 225 44, 240 55, 255 88 C 265 110, 273 125, 280 132 L 280 145 Z" fill="#bfdbfe" fill-opacity="0.7"/>
  <!-- Shaded tail >= u -->
  <path d="M 280 132 C 292 140, 310 144, 355 145 L 280 145 Z" fill="#fca5a5" fill-opacity="0.85"/>
  <!-- Bell curve -->
  <path d="M 65 144 C 110 143, 145 115, 165 88 C 180 55, 195 44, 210 44 C 225 44, 240 55, 255 88 C 275 115, 310 143, 355 144" fill="none" stroke="#1e3a8a" stroke-width="2"/>
  <line x1="280" y1="132" x2="280" y2="145" stroke="#dc2626" stroke-width="1.5"/>
  <text x="210" y="162" text-anchor="middle" font-size="11" fill="#334e68">Z = 0 (170.9 cm)</text>
  <text x="288" y="162" text-anchor="start" font-size="11" font-weight="bold" fill="#dc2626">u = 1.75 (180.35 cm)</text>
  <text x="242" y="114" text-anchor="middle" font-size="11" font-weight="bold" fill="#1e40af">0.46</text>
  <text x="322" y="128" text-anchor="middle" font-size="11" font-weight="bold" fill="#dc2626">4% (0.04)</text>
</svg>

- **【分步标准解答】**
  $X$ は正規分布 $N(170.9,\; 5.4^2)$ に従うから、
  $$Z = \frac{X - 170.9}{5.4}$$
  とおくと、$Z$ は標準正規分布 $N(0, 1)$ に従う。
  - **$[1]$** 身長 $175\,\mathrm{cm}$ 以上の割合：
    $X = 175$ のとき、
    $$Z = \frac{175 - 170.9}{5.4} = \frac{4.1}{5.4} = 0.7592\cdots \fallingdotseq 0.76$$
    正規分布表より $p(0.76) = 0.2764$ であるから、
    $$P(X \ge 175) \fallingdotseq P(Z \ge 0.76) = 0.5 - p(0.76) = 0.5 - 0.2764 = 0.2236$$
    よって、約 **$22.4\%$**（小数点第 2 位までなら $22.36\%$）。
    > 💡 讲师批注：日本标准正态分布表精确到小数点后 2 位，因此标准化结果 $Z$ 需四舍五入至小数点后 2 位再查表。
  - **$[2]$** 身長 $165\,\mathrm{cm}$ 以上 $174\,\mathrm{cm}$ 以下の割合：
    - $X = 165$ のとき：$Z = \dfrac{165 - 170.9}{5.4} = \dfrac{-5.9}{5.4} = -1.0925\cdots \fallingdotseq -1.09$
    - $X = 174$ のとき：$Z = \dfrac{174 - 170.9}{5.4} = \dfrac{3.1}{5.4} = 0.5740\cdots \fallingdotseq 0.57$

    正規分布表より $p(1.09) = 0.3621$、$p(0.57) = 0.2157$ であるから、
    $$P(165 \le X \le 174) \fallingdotseq P(-1.09 \le Z \le 0.57) = p(1.09) + p(0.57)$$
    $$= 0.3621 + 0.2157 = 0.5778$$
    よって、約 **$57.8\%$**（$57.78\%$）。
  - **$[3]$** 高い方から $4\%$ の中に入る身長：
    求める身長を $x\,\mathrm{cm}$、対応する標準化変数を $u = \dfrac{x - 170.9}{5.4}$ ($u > 0$) とすると、
    $$P(Z \ge u) = 0.04 \iff 0.5 - p(u) = 0.04 \iff p(u) = 0.46$$
    正規分布表で $p(u)$ が $0.4600$ に最も近い $u$ を探すと、
    $$p(1.75) = 0.4599, \qquad p(1.76) = 0.4608$$
    より $u \fallingdotseq 1.75$ を得る。したがって、
    $$\frac{x - 170.9}{5.4} = 1.75 \implies x = 170.9 + 5.4 \times 1.75 = 170.9 + 9.45 = 180.35$$
    よって、約 **$180.4\,\mathrm{cm}$ 以上**（整数値に丸める場合は約 $180\,\mathrm{cm}$ 以上）。
    > 💡 讲师批注：逆查表常见错误是直接去表里找 $0.04$！一定要先用 $0.5 - 0.04 = 0.46$ 转换为「从 $0$ 到 $u$ 的面积」再去查表。
- **【最终答案】**
  **$[1]$ 約 $22.4\%$（$22.36\%$），$[2]$ 約 $57.8\%$（$57.78\%$），$[3]$ 約 $180.4\,\mathrm{cm}$ 以上（$180.35\,\mathrm{cm}$）**

---

### 解説例題（[9.3] 復元抽出・非復元抽出の同時分布）

#### 例題（P456 / 印刷頁 455）
- **【原题重现与翻译】**
  - 原题：赤球、白球、黒球がそれぞれ 1 個、2 個、3 個ある。これらすべての球を母集団として、次のような方法で大きさ 2 の無作為標本を抽出し、その球の色を順に $X_1, X_2$ とするとき、$X_1, X_2$ の同時分布の表を $(1)$ 復元抽出、$(2)$ 非復元抽出の各場合に求めよ。
  - 中文：有红球 1 个、白球 2 个、黑球 3 个。以这全部 6 个球为总体，按以下方式抽取容量为 2 的随机样本，依次记其颜色为 $X_1, X_2$。分别求 $(1)$ 有放回抽样、$(2)$ 无放回抽样时 $X_1, X_2$ 的联合分布表。
- **【考点定位】**
  - 独立乘法定理（有放回）与条件概率乘法定理（无放回）的对比。
- **【分步标准解答】**
  - **$(1)$ 復元抽出（独立）**：毎回 6 個の球から抽出するため、$P(X_1 = i,\; X_2 = j) = P(X_1 = i)P(X_2 = j)$（分母均为 $6 \times 6 = 36$）：

    | $X_1 \backslash X_2$ | 赤 | 白 | 黒 | 計 |
    | :---: | :---: | :---: | :---: | :---: |
    | **赤** | $\frac{1}{36}$ | $\frac{2}{36}$ | $\frac{3}{36}$ | $\frac{6}{36}$ |
    | **白** | $\frac{2}{36}$ | $\frac{4}{36}$ | $\frac{6}{36}$ | $\frac{12}{36}$ |
    | **黒** | $\frac{3}{36}$ | $\frac{6}{36}$ | $\frac{9}{36}$ | $\frac{18}{36}$ |
    | **計** | $\frac{6}{36}$ | $\frac{12}{36}$ | $\frac{18}{36}$ | $1$ |

  - **$(2)$ 非復元抽出（従属）**：1 回目に 6 個から取り出し、戻さずに残り 5 個から 2 回目を取り出す（分母均为 $6 \times 5 = 30$）。特に赤球は 1 個しかないため $P(X_1=\text{赤},\; X_2=\text{赤}) = 0$：

    | $X_1 \backslash X_2$ | 赤 | 白 | 黒 | 計 |
    | :---: | :---: | :---: | :---: | :---: |
    | **赤** | $0$ | $\frac{2}{30}$ | $\frac{3}{30}$ | $\frac{5}{30}$ |
    | **白** | $\frac{2}{30}$ | $\frac{2}{30}$ | $\frac{6}{30}$ | $\frac{10}{30}$ |
    | **黒** | $\frac{3}{30}$ | $\frac{6}{30}$ | $\frac{6}{30}$ | $\frac{15}{30}$ |
    | **計** | $\frac{5}{30}$ | $\frac{10}{30}$ | $\frac{15}{30}$ | $1$ |

    > 💡 讲师批注：注意观察两张表的边缘分布（計）：无论是 $(1)$ 还是 $(2)$，$X_1$ 与 $X_2$ 的各自边缘概率完全一致（赤 $\frac{1}{6}$、白 $\frac{2}{6}$、黒 $\frac{3}{6}$），因此即便在非復元抽出下，也有 $E(X_1) = E(X_2) = m$ 与 $\sigma(X_1) = \sigma(X_2) = \sigma$！
- **【最终答案】**
  **如上两表所示。**

---

### 演習問題 8（統計的な推測）

#### 演習問題 8-(1)
- **【原题重现与翻译】**
  - 原题：$1, 2, 3, 4, 5$ の数字が書かれている札が、それぞれ 1 枚、2 枚、3 枚、4 枚、5 枚ずつある。これを母集団とし、札の数字を変量 $X$ とするとき、母集団分布、母平均 $m$、母標準偏差 $\sigma$ を求めよ。
  - 中文：写有数字 $1, 2, 3, 4, 5$ 的卡片分别有 1 张、2 张、3 张、4 张、5 张。将其作为总体，卡片上的数字记为变量 $X$，求总体分布、总体均值 $m$ 和总体标准差 $\sigma$。
- **【考点定位】**
  - 离散型总体分布、总体均值 $m = E(X)$、总体方差 $\sigma^2 = E(X^2) - m^2$ 与总体标准差 $\sigma$ 的计算。
- **【分步标准解答】**
  1. **母集団分布**：
     札の総数は $N = 1 + 2 + 3 + 4 + 5 = 15$（枚）である。各数字 $k$ ($k = 1, 2, 3, 4, 5$) のとる確率は $\dfrac{k}{15}$ となるから、母集団分布は次の表の通りである：

     | $X$ | $1$ | $2$ | $3$ | $4$ | $5$ | 計 |
     | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
     | $P$ | $\dfrac{1}{15}$ | $\dfrac{2}{15}$ | $\dfrac{3}{15}$ | $\dfrac{4}{15}$ | $\dfrac{5}{15}$ | $1$ |

     > 💡 讲师批注：概率行不约分保留同分母 $15$，后续算期望和方差时非常方便统一通分。
  2. **母平均 $m$**：
     $$m = E(X) = 1 \cdot \frac{1}{15} + 2 \cdot \frac{2}{15} + 3 \cdot \frac{3}{15} + 4 \cdot \frac{4}{15} + 5 \cdot \frac{5}{15}$$
     $$= \frac{1 + 4 + 9 + 16 + 25}{15} = \frac{55}{15} = \frac{11}{3}$$
     > 💡 讲师批注：分子恰为平方和 $\sum_{k=1}^5 k^2 = \frac{5 \times 6 \times 11}{6} = 55$。
  3. **母標準偏差 $\sigma$**：
     まず $E(X^2)$ を求める：
     $$E(X^2) = 1^2 \cdot \frac{1}{15} + 2^2 \cdot \frac{2}{15} + 3^2 \cdot \frac{3}{15} + 4^2 \cdot \frac{4}{15} + 5^2 \cdot \frac{5}{15}$$
     $$= \frac{1 + 8 + 27 + 64 + 125}{15} = \frac{225}{15} = 15$$
     > 💡 讲师批注：分子恰为立方和 $\sum_{k=1}^5 k^3 = \left(\frac{5 \times 6}{2}\right)^2 = 15^2 = 225$，除以 $15$ 恰好得整数 $15$！

     よって、母分散 $\sigma^2$ は
     $$\sigma^2 = E(X^2) - m^2 = 15 - \left(\frac{11}{3}\right)^2 = \frac{135 - 121}{9} = \frac{14}{9}$$
     したがって、母標準偏差 $\sigma$ は
     $$\sigma = \sqrt{\frac{14}{9}} = \frac{\sqrt{14}}{3}$$
- **【最终答案】**
  **母集団分布：如上表；母平均 $m = \dfrac{11}{3}$；母標準偏差 $\sigma = \dfrac{\sqrt{14}}{3}$**

---

#### 演習問題 8-(2)
- **【原题重现与翻译】**
  - 原题：ある県において、参議院議員選挙における有権者の A 政党支持率は $30\%$ であるという。この県の有権者の中から、無作為に $n$ 人を抽出するとき、$k$ 番目に抽出された人が A 政党支持なら $1$、不支持なら $0$ の値を対応させる確率変数を $X_k$ とする。
    $[1]$ 標本平均 $\overline{X} = \dfrac{X_1 + X_2 + \cdots + X_n}{n}$ について、期待値 $E(\overline{X})$ を求めよ。
    $[2]$ 標本平均 $\overline{X}$ の標準偏差 $\sigma(\overline{X})$ を $0.02$ 以下にするためには、抽出される標本の大きさは、少なくとも何人以上必要か。
  - 中文：某县在参议院议员选举中，选民对 A 政党的支持率为 $30\%$。从该县选民中随机抽取 $n$ 人，令随机变量 $X_k$ 表示第 $k$ 个被抽中的人：支持 A 政党记为 $1$，不支持记为 $0$。
    $[1]$ 求样本均值 $\overline{X} = \dfrac{X_1 + X_2 + \cdots + X_n}{n}$ 的期望 $E(\overline{X})$。
    $[2]$ 为使样本均值 $\overline{X}$ 的标准差 $\sigma(\overline{X})$ 不超过 $0.02$，抽取的样本容量至少需要多少人以上？
- **【考点定位】**
  - 0-1 示性变量的均值与方差、样本均值（即样本比例）的期望与标准差、样本容量反推不等式。
- **【分步标准解答】**
  1. **母集団の母平均 $m$ と母標準偏差 $\sigma$**：
     母集団における支持率は $p = 0.3$ であるから、1 人を無作為に抽出したときの確率変数 $X_k$ の確率分布は次のようになる：
     $$P(X_k = 1) = 0.3, \qquad P(X_k = 0) = 0.7$$
     よって、母平均 $m$ と母分散 $\sigma^2$ は
     $$m = E(X_k) = 1 \times 0.3 + 0 \times 0.7 = 0.3$$
     $$\sigma^2 = E(X_k^2) - m^2 = (1^2 \times 0.3 + 0^2 \times 0.7) - 0.3^2 = 0.3 - 0.09 = 0.21$$
     （したがって $\sigma = \sqrt{0.21}$）
     > 💡 讲师批注：本题中 $\overline{X}$ 其实就是 A 政党支持者的**样本比例 $R$**，直接套用样本比例公式 $E(R) = p = 0.3$、$\sigma(R) = \sqrt{\frac{p(1-p)}{n}} = \sqrt{\frac{0.3 \times 0.7}{n}} = \sqrt{\frac{0.21}{n}}$ 也能瞬间验证！
  2. **$[1]$ $E(\overline{X})$**：
     県の有権者数（母集団の大きさ）は十分大きいので、$X_1, \dots, X_n$ は互いに独立とみなせる。よって、
     $$E(\overline{X}) = m = 0.3$$
  3. **$[2]$ 必要な標本の大きさ $n$**：
     $$\sigma(\overline{X}) = \frac{\sigma}{\sqrt{n}} = \sqrt{\frac{0.21}{n}}$$
     条件 $\sigma(\overline{X}) \le 0.02$ より、両辺は正であるから 2 乗して
     $$\frac{0.21}{n} \le (0.02)^2 = 0.0004$$
     $$n \ge \frac{0.21}{0.0004} = \frac{2100}{4} = 525$$
     > 💡 讲师批注：将小数同时乘以 $10000$ 变为整数除法 $\frac{2100}{4} = 525$，恰为整数，无需进位。
- **【最终答案】**
  **$[1]\; E(\overline{X}) = 0.3$，$[2]$ 少なくとも $525$ 人以上**

---

#### 演習問題 8-(3)
- **【原题重现与翻译】**
  - 原题：体長が平均 $50\,\mathrm{cm}$、標準偏差 $3\,\mathrm{cm}$ の正規分布に従う生物集団があるとする。
    $[1]$ 体長が $47\,\mathrm{cm}$ から $56\,\mathrm{cm}$ までのものは全体の何 $\%$ であるか。
    $[2]$ 4 つの個体を無作為に取り出したとき、体長の標本平均が $53\,\mathrm{cm}$ 以上となる確率を求めよ。
  - 中文：设某生物群体的体长服从平均 $50\,\mathrm{cm}$、标准差 $3\,\mathrm{cm}$ 的正态分布。
    $[1]$ 体长在 $47\,\mathrm{cm}$ 到 $56\,\mathrm{cm}$ 之间的个体占整体的百分之几？
    $[2]$ 随机抽取 4 个个体时，求其体长的样本均值在 $53\,\mathrm{cm}$ 以上的概率。
- **【考点定位】**
  - 正态总体中单个观测值 $X \sim N(m, \sigma^2)$ 与样本均值 $\overline{X} \sim N(m, \sigma^2/n)$ 的分布区分。
- **【图解辅助（SVG 矢量图）】**

<svg viewBox="0 0 480 185" width="480" height="185" xmlns="http://www.w3.org/2000/svg" style="display:block;margin:10px auto;background:#fafbfd;border:1px solid #d9e2ec;border-radius:8px;">
  <!-- Left: [1] X ~ N(50, 3^2), 47 <= X <= 56 -->
  <text x="120" y="18" text-anchor="middle" font-size="12" font-weight="bold" fill="#102a43">[1] X ~ N(50, 3²)：−1 ≤ Z ≤ 2</text>
  <line x1="20" y1="148" x2="225" y2="148" stroke="#334e68" stroke-width="1.3"/>
  <line x1="120" y1="148" x2="120" y2="42" stroke="#9fb3c8" stroke-dasharray="3,3"/>
  <!-- Shaded -1 to 2 (center 120, scale 30px/unit -> 90 to 180) -->
  <path d="M 90 148 L 90 88 C 102 58, 111 48, 120 48 C 129 48, 138 58, 150 88 C 160 112, 170 132, 180 140 L 180 148 Z" fill="#93c5fd" fill-opacity="0.7"/>
  <path d="M 30 147 C 60 146, 78 122, 90 88 C 102 58, 111 48, 120 48 C 129 48, 138 58, 150 88 C 162 122, 180 146, 210 147" fill="none" stroke="#1e3a8a" stroke-width="2"/>
  <line x1="90" y1="88" x2="90" y2="148" stroke="#2563eb" stroke-width="1.2"/>
  <line x1="180" y1="140" x2="180" y2="148" stroke="#2563eb" stroke-width="1.2"/>
  <text x="90" y="164" text-anchor="middle" font-size="11" fill="#1d4ed8">47 (−1)</text>
  <text x="120" y="164" text-anchor="middle" font-size="11" fill="#334e68">50</text>
  <text x="180" y="164" text-anchor="middle" font-size="11" fill="#1d4ed8">56 (2)</text>
  <!-- Right: [2] Xbar ~ N(50, 1.5^2), Xbar >= 53 -->
  <text x="360" y="18" text-anchor="middle" font-size="12" font-weight="bold" fill="#102a43">[2] X̄ ~ N(50, 1.5²)：Z ≥ 2</text>
  <line x1="255" y1="148" x2="460" y2="148" stroke="#334e68" stroke-width="1.3"/>
  <line x1="360" y1="148" x2="360" y2="42" stroke="#9fb3c8" stroke-dasharray="3,3"/>
  <path d="M 420 140 C 432 145, 442 147, 450 147 L 450 148 L 420 148 Z" fill="#fca5a5" fill-opacity="0.85"/>
  <path d="M 270 147 C 300 146, 318 122, 330 88 C 342 58, 351 48, 360 48 C 369 48, 378 58, 390 88 C 402 122, 420 146, 450 147" fill="none" stroke="#1e3a8a" stroke-width="2"/>
  <line x1="420" y1="140" x2="420" y2="148" stroke="#dc2626" stroke-width="1.4"/>
  <text x="360" y="164" text-anchor="middle" font-size="11" fill="#334e68">50 (0)</text>
  <text x="420" y="164" text-anchor="middle" font-size="11" font-weight="bold" fill="#dc2626">53 (2)</text>
  <text x="432" y="128" text-anchor="middle" font-size="11" font-weight="bold" fill="#dc2626">0.0228</text>
</svg>

- **【分步标准解答】**
  - **$[1]$** 個体の体長 $X$ は $N(50, 3^2)$ に従う。$Z = \dfrac{X - 50}{3}$ とおくと $Z \sim N(0, 1)$ であり、
    - $X = 47 \implies Z = \dfrac{47 - 50}{3} = -1$
    - $X = 56 \implies Z = \dfrac{56 - 50}{3} = 2$

    よって、正規分布表より $p(1) = 0.3413$、$p(2) = 0.4772$ であるから、
    $$P(47 \le X \le 56) = P(-1 \le Z \le 2) = p(1) + p(2) = 0.3413 + 0.4772 = 0.8185$$
    したがって、全体の **$81.85\%$**（約 $81.9\%$）。
  - **$[2]$** 大きさ $n = 4$ の無作為標本の標本平均 $\overline{X}$ を考える。
    母集団が正規分布 $N(50, 3^2)$ に従うから、標本平均 $\overline{X}$ は $n = 4$ であっても**厳密に**正規分布
    $$N\!\left(50,\; \frac{3^2}{4}\right) = N\!\left(50,\; 1.5^2\right)$$
    に従う。
    > 💡 讲师批注：最常见的错误是忘记除以 $\sqrt{n} = \sqrt{4} = 2$，误把标准差仍当作 $3$！本题样本均值的标准差是 $\frac{3}{\sqrt{4}} = 1.5$。

    $Z = \dfrac{\overline{X} - 50}{1.5}$ とおくと、$\overline{X} = 53$ のとき $Z = \dfrac{53 - 50}{1.5} = 2$ であるから、
    $$P(\overline{X} \ge 53) = P(Z \ge 2) = 0.5 - p(2) = 0.5 - 0.4772 = 0.0228$$
- **【最终答案】**
  **$[1]\; 81.85\%$（約 $81.9\%$），$[2]\; 0.0228$**

---

#### 演習問題 8-(4)
- **【原题重现与翻译】**
  - 原题：母平均 $0$、母標準偏差 $1$ をもつ母集団から抽出した大きさ $n$ の標本の標本平均 $\overline{X}$ が $-0.1$ 以上 $0.1$ 以下である確率 $P(|\overline{X}| \le 0.1)$ を、$n = 100, 400, 900$ の各場合について求めよ。
  - 中文：从总体均值为 $0$、总体标准差为 $1$ 的总体中抽取容量为 $n$ 的样本，分别在 $n = 100, 400, 900$ 时，求样本均值 $\overline{X}$ 落在 $-0.1$ 以上 $0.1$ 以下的概率 $P(|\overline{X}| \le 0.1)$。
- **【考点定位】**
  - 中心极限定理与大数定律的数值验证（展示 $n$ 增大时 $\overline{X}$ 落入母平均邻域的概率迅速趋近于 $1$）。
- **【分步标准解答】**
  $n$ は十分大きいので、中心極限定理により、標本平均 $\overline{X}$ は近似的に正規分布 $N\!\left(0,\; \dfrac{1^2}{n}\right)$ に従う。
  したがって、
  $$Z = \frac{\overline{X} - 0}{1 / \sqrt{n}} = \sqrt{n}\,\overline{X}$$
  は近似的に標準正規分布 $N(0, 1)$ に従う。よって、
  $$P(|\overline{X}| \le 0.1) = P\left(|Z| \le 0.1\sqrt{n}\right) = 2\,p\left(0.1\sqrt{n}\right)$$
  > 💡 讲师批注：把一般表达式 $2\,p(0.1\sqrt{n})$ 先推出来，再分别代入 $n = 100, 400, 900$，结构极其清爽！

  - **$n = 100$ のとき**：$0.1\sqrt{100} = 1$ より、
    $$P(|\overline{X}| \le 0.1) = 2\,p(1) = 2 \times 0.3413 = 0.6826$$
  - **$n = 400$ のとき**：$0.1\sqrt{400} = 2$ より、
    $$P(|\overline{X}| \le 0.1) = 2\,p(2) = 2 \times 0.4772 = 0.9544$$
  - **$n = 900$ のとき**：$0.1\sqrt{900} = 3$ より、
    $$P(|\overline{X}| \le 0.1) = 2\,p(3) = 2 \times 0.4987 = 0.9974$$
    > 💡 讲师批注：这三个数值 $0.6826, 0.9544, 0.9974$ 正是统计学著名的 **$1\sigma, 2\sigma, 3\sigma$ 法则（68-95-99.7 规律）**，直观印证了大数定律：$n$ 越大，样本均值偏离母平均不超过 $0.1$ 的概率越接近 $1$。
- **【最终答案】**
  **$n = 100$ のとき $0.6826$、$n = 400$ のとき $0.9544$、$n = 900$ のとき $0.9974$**

---

#### 演習問題 8-(5)
- **【原题重现与翻译】**
  - 原题：ある工場で大量生産されている電球の中から無作為に抽出した 25 個について試験したところ、それらの寿命の平均値は 1500 時間であった。製品全体の平均寿命を信頼度 $90\%$ で推定せよ。ただし、製品の寿命は正規分布に従い、標準偏差は 110 時間である。
  - 中文：从某工厂大量生产的灯泡中随机抽取 25 个进行测试，测得其寿命的平均值为 1500 小时。试以 $90\%$ 的置信度估计该产品整体的平均寿命。已知产品寿命服从正态分布，标准差为 110 小时。
  > ⚠️ **教材勘误提示**：原教材第 461 页（`page_0462.jpg`）将「25 個に**ついて**試験したところ」漏印「て」字作「につい」，并将句尾「推定**せよ**。」误印为过去式「推定**した**。」。
- **【考点定位】**
  - 总体均值 $m$ 的区间估计（非 $95\% / 99\%$ 的一般置信度 $90\%$ 的临界值查表）。
- **【图解辅助（SVG 矢量图）】**

<svg viewBox="0 0 430 185" width="430" height="185" xmlns="http://www.w3.org/2000/svg" style="display:block;margin:10px auto;background:#fafbfd;border:1px solid #d9e2ec;border-radius:8px;">
  <text x="215" y="18" text-anchor="middle" font-size="12" font-weight="bold" fill="#102a43">信頼度 90%：2p(c) = 0.90 ⇔ p(c) = 0.45 ⇒ c ≈ 1.645</text>
  <line x1="30" y1="145" x2="400" y2="145" stroke="#334e68" stroke-width="1.4"/>
  <line x1="215" y1="145" x2="215" y2="38" stroke="#9fb3c8" stroke-dasharray="4,3"/>
  <!-- Shaded -c to c (c=1.645 -> +-66px -> 149 to 281) -->
  <path d="M 149 145 L 149 128 C 165 110, 180 55, 215 44 C 250 55, 265 110, 281 128 L 281 145 Z" fill="#a7f3d0" fill-opacity="0.75"/>
  <!-- Bell curve -->
  <path d="M 65 144 C 110 143, 138 135, 149 128 C 168 108, 185 44, 215 44 C 245 44, 262 108, 281 128 C 292 135, 320 143, 365 144" fill="none" stroke="#1e3a8a" stroke-width="2"/>
  <line x1="149" y1="128" x2="149" y2="145" stroke="#059669" stroke-width="1.4"/>
  <line x1="281" y1="128" x2="281" y2="145" stroke="#059669" stroke-width="1.4"/>
  <text x="149" y="162" text-anchor="middle" font-size="11" font-weight="bold" fill="#047857">−1.645</text>
  <text x="215" y="162" text-anchor="middle" font-size="11" fill="#334e68">0</text>
  <text x="281" y="162" text-anchor="middle" font-size="11" font-weight="bold" fill="#047857">+1.645</text>
  <text x="186" y="114" text-anchor="middle" font-size="11" font-weight="bold" fill="#065f46">0.45</text>
  <text x="244" y="114" text-anchor="middle" font-size="11" font-weight="bold" fill="#065f46">0.45</text>
  <text x="115" y="132" text-anchor="middle" font-size="10" fill="#64748b">0.05</text>
  <text x="315" y="132" text-anchor="middle" font-size="10" fill="#64748b">0.05</text>
</svg>

- **【分步标准解答】**
  1. **標本平均の分布の確認**：
     製品の寿命が正規分布 $N(m, 110^2)$ に従うので、$n = 25$ の標本平均 $\overline{X}$ は厳密に正規分布 $N\!\left(m,\; \dfrac{110^2}{25}\right)$ に従う。
     標本平均の標準偏差は
     $$\frac{\sigma}{\sqrt{n}} = \frac{110}{\sqrt{25}} = \frac{110}{5} = 22$$
     > 💡 讲师批注：尽管 $n = 25$ 不算大，但题干明确给出了「产品的寿命服从正态分布」，因此 $\overline{X}$ 精确服从正态分布，无需依赖中心极限定理！
  2. **信頼度 $90\%$ に対する臨界値 $c$ を求める**：
     $$2p(c) = 0.90 \iff p(c) = 0.4500$$
     正規分布表より $p(1.64) = 0.4495$、$p(1.65) = 0.4505$ であるから、中間値をとって $c = 1.645$ を得る。
  3. **信頼区間の計算**：
     誤差の限界（半幅）は
     $$1.645 \times \frac{110}{\sqrt{25}} = 1.645 \times 22 = 36.19$$
     よって、母平均 $m$ に対する信頼度 $90\%$ の信頼区間は
     $$1500 - 36.19 \le m \le 1500 + 36.19$$
     すなわち
     $$1463.81 \le m \le 1536.19 \qquad (\text{小数第 1 位までなら } 1463.8 \le m \le 1536.2)$$
     > 💡 讲师批注：日本部分参考书在查表不插值时，会直接取 $c = 1.64$（得 $[1463.92,\; 1536.08]$，约 $[1464,\; 1536]$）或 $c = 1.65$（得 $[1463.7,\; 1536.3]$，约 $[1464,\; 1536]$）。四舍五入至整数小时时，三种取值完全一致，均为 **$1464$ 時間以上 $1536$ 時間以下**！
- **【最终答案】**
  **$1463.8 \le m \le 1536.2$（精密値 $[1463.81,\; 1536.19]$；整数に丸めると $1464$ 時間以上 $1536$ 時間以下）**

---

#### 演習問題 8-(6)
- **【原题重现与翻译】**
  - 原题：ある高校の 1 年生 100 人について、バス通学者は 64 人であった。これを無作為標本として、この高校の 1 年生全体におけるバス通学者の割合を信頼度 $95\%$ で推定せよ。
  - 中文：调查某高中高一学生 100 人，其中乘公交车上学的有 64 人。将其作为随机样本，以 $95\%$ 的置信度估计该校高一全体学生中乘公交车上学的比例。
- **【考点定位】**
  - 总体比例 $p$ 的 $95\%$ 置信区间公式。
- **【分步标准解答】**
  1. **標本比率 $R$ の計算**：
     標本の大きさ $n = 100$、バス通学者の人数は $64$ 人であるから、標本比率 $R$ は
     $$R = \frac{64}{100} = 0.64$$
  2. **標準誤差 $\sqrt{\dfrac{R(1-R)}{n}}$ の計算**：
     $$\sqrt{\frac{R(1-R)}{n}} = \sqrt{\frac{0.64 \times (1 - 0.64)}{100}} = \sqrt{\frac{0.64 \times 0.36}{100}} = \frac{0.8 \times 0.6}{10} = 0.048$$
     > 💡 讲师批注：不要把 $0.64 \times 0.36$ 乘出来再开根号！直接看出 $0.64 = 0.8^2$、$0.36 = 0.6^2$、$100 = 10^2$，逐项开方得 $\frac{0.8 \times 0.6}{10} = 0.048$，又快又零失误！
  3. **信頼度 $95\%$ の信頼区間の計算**：
     信頼度 $95\%$ に対する係数は $1.96$ であるから、
     $$1.96 \times 0.048 = 0.09408$$
     よって、母比率 $p$ の信頼度 $95\%$ の信頼区間は
     $$0.64 - 0.09408 \le p \le 0.64 + 0.09408$$
     $$0.54592 \le p \le 0.73408$$
     小数第 4 位を四捨五入すると、$0.546 \le p \le 0.734$（約 $54.6\%$ 以上 $73.4\%$ 以下）。
- **【最终答案】**
  **$0.546 \le p \le 0.734$（精密値 $[0.54592,\; 0.73408]$；すなわち約 $54.6\%$ 以上 $73.4\%$ 以下）**

---

#### 演習問題 8-(7)
- **【原题重现与翻译】**
  - 原题：ある意見に対する賛成率は約 $60\%$ と予想されている。この意見に対する賛成率を、信頼度 $95\%$ で信頼区間の幅が $8\%$ 以下になるように推定したい。何人以上抽出して調べればよいか。
  - 中文：预计对某意见的赞成率约为 $60\%$。希望在 $95\%$ 置信度下估计该意见的赞成率，且使置信区间的宽度不超过 $8\%$。至少应抽取多少人进行调查？
- **【考点定位】**
  - 总体比例置信区间的**宽度（幅）**公式与最小样本容量 $n$ 的求解。
- **【图解辅助（SVG 矢量图）】**

<svg viewBox="0 0 440 120" width="440" height="120" xmlns="http://www.w3.org/2000/svg" style="display:block;margin:10px auto;background:#fafbfd;border:1px solid #d9e2ec;border-radius:8px;">
  <defs>
    <marker id="arr87" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#dc2626"/>
    </marker>
  </defs>
  <!-- Number line -->
  <line x1="30" y1="68" x2="410" y2="68" stroke="#334e68" stroke-width="1.5"/>
  <!-- Interval bar -->
  <line x1="95" y1="68" x2="345" y2="68" stroke="#2563eb" stroke-width="4"/>
  <circle cx="95" cy="68" r="4.5" fill="#2563eb"/>
  <circle cx="220" cy="68" r="4.5" fill="#102a43"/>
  <circle cx="345" cy="68" r="4.5" fill="#2563eb"/>
  <!-- Width arrow -->
  <line x1="98" y1="36" x2="342" y2="36" stroke="#dc2626" stroke-width="1.6" marker-start="url(#arr87)" marker-end="url(#arr87)"/>
  <text x="220" y="26" text-anchor="middle" font-size="12" font-weight="bold" fill="#dc2626">信頼区間の幅 = 2 × 1.96 × √(R(1−R)/n) ≤ 0.08</text>
  <!-- Endpoint labels -->
  <text x="95" y="92" text-anchor="middle" font-size="11" fill="#1d4ed8">R − 1.96·SE</text>
  <text x="220" y="92" text-anchor="middle" font-size="11" font-weight="bold" fill="#102a43">R ≈ 0.6</text>
  <text x="345" y="92" text-anchor="middle" font-size="11" fill="#1d4ed8">R + 1.96·SE</text>
  <text x="157" y="59" text-anchor="middle" font-size="10" fill="#486581">半幅 ≤ 0.04</text>
  <text x="282" y="59" text-anchor="middle" font-size="10" fill="#486581">半幅 ≤ 0.04</text>
</svg>

- **【分步标准解答】**
  1. **信頼区間の幅の立式**：
     抽出する人数を $n$ 人とすると、標本比率は $R \fallingdotseq 0.6$ とみなせる。
     信頼度 $95\%$ の信頼区間は $\left[R - 1.96\sqrt{\dfrac{R(1-R)}{n}},\;\; R + 1.96\sqrt{\dfrac{R(1-R)}{n}}\right]$ であるから、**信頼区間の幅（全幅）**は
     $$2 \times 1.96\sqrt{\frac{R(1-R)}{n}}$$
     > 💡 讲师批注：**最高频易错点！**「信頼区間の幅（宽度）」是右端点减去左端点，等于**2 倍的误差界限**！千万不要漏乘最前面的 $2$（如果漏乘 $2$，算出的样本量会少 4 倍）。
  2. **不等式を解く**：
     幅が $8\%$ ($= 0.08$) 以下となる条件は、$R = 0.6$ を代入して
     $$2 \times 1.96\sqrt{\frac{0.6 \times 0.4}{n}} \le 0.08$$
     両辺を $2$ で割ると
     $$1.96\sqrt{\frac{0.24}{n}} \le 0.04$$
     $$\sqrt{\frac{0.24}{n}} \le \frac{0.04}{1.96} = \frac{4}{196} = \frac{1}{49}$$
     > 💡 讲师批注：先约分 $\frac{0.04}{1.96} = \frac{1}{49}$ 再平方，比直接算 $1.96^2$ 再除 $0.04^2$ 简单十倍！

     両辺は正であるから 2 乗して
     $$\frac{0.24}{n} \le \frac{1}{49^2} = \frac{1}{2401}$$
     $$n \ge 0.24 \times 2401 = 576.24$$
  3. **整数化（切り上げ）**：
     $n$ は自然数であるから、$n \ge 577$。
     > 💡 讲师批注：人数必须向上取整（切り上げ），即使小数部分是 $0.24$，取 $576$ 人时宽度仍略大于 $8\%$，因此至少需要 **$577$ 人**！
- **【最终答案】**
  **$577$ 人以上**
