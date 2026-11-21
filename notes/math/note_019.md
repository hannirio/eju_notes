# 《EJU 教材全解与备课讲义》数学 019（P271–P285）

> **对应源文件**：`work_math/ocr_md/ocr_019_p271-285.md`（第十章《数列》之「種々の漸化式」「数学的帰納法」；第十一章《微分積分》之「数列の極限」）
> **视觉核对参考图**：`work_math/ref_imgs/page_0271.jpg` – `page_0285.jpg`（全部 15 页均已逐字逐符号核对）

---

## 一、国内高中基础知识点唤醒与 EJU 考纲差异对比

本切片横跨日本高中数学 **数学B（数列）** 的压轴核心（特殊递推式、相邻三项递推式、联立递推式、分式型递推式、数学归纳法）以及 **数学Ⅲ（極限）** 的开篇基础（无穷数列的极限、夹逼定理、无穷等比数列的收敛条件）。这是 EJU 数学（コース 2 / 理科数学）大题的超高频命题区。

### 1.1 特殊递推式的标准转化套路（種々の漸化式）

在掌握基础两项线性递推 $a_{n+1} = p a_n + q$ 的基础上，本切片系统梳理了以下 6 类高阶递推式：

1. **指数型**：$a_{n+1} = p a_n + q^{n+1}$
   - 两边同除以 $q^{n+1}$，令 $b_n = \dfrac{a_n}{q^n}$，化为 $b_{n+1} = \dfrac{p}{q} b_n + 1$（特征方程法）。
   - 或两边同除以 $p^{n+1}$，化为阶差数列型（当 $p=q$ 时直接化为等差数列）。
2. **倒数型**：$a_{n+1} = \dfrac{a_n}{p a_n + q}$
   - 先说明 $a_n \neq 0$，再取倒数 $\dfrac{1}{a_{n+1}} = q \cdot \dfrac{1}{a_n} + p$，令 $b_n = \dfrac{1}{a_n}$ 求解。
3. **幂根/乘积型**：$a_{n+1} = c \cdot (a_n)^k$（如 $a_{n+1} = 2\sqrt{a_n}$）
   - 先说明 $a_n > 0$，再两边取对数 $\log_2 a_{n+1} = \log_2 c + k \log_2 a_n$，令 $b_n = \log_2 a_n$ 求解。
4. **相邻三项递推式（隣接 3 項間の漸化式）**：$p a_{n+2} + q a_{n+1} + r a_n = 0 \quad (pqr \neq 0)$
   - 构造**特征方程（特性方程式）**：$p x^2 + q x + r = 0$，设两解为 $\alpha, \beta$，可变形为：
     $$a_{n+2} - \alpha a_{n+1} = \beta (a_{n+1} - \alpha a_n), \qquad a_{n+2} - \beta a_{n+1} = \alpha (a_{n+1} - \beta a_n)$$
   - 按特征根分为三类：
     - **含解 $1$（如 $\alpha = 1$）**：$a_{n+2} - a_{n+1} = \beta (a_{n+1} - a_n)$，直接利用**阶差数列（階差数列）**求和。
     - **两个不等于 $1$ 的相异解（$\alpha \neq \beta$）**：分别写出 $a_{n+1} - \alpha a_n = \beta^{n-1}(a_2 - \alpha a_1)$ 与 $a_{n+1} - \beta a_n = \alpha^{n-1}(a_2 - \beta a_1)$，两式相减消去 $a_{n+1}$ 即可得 $a_n$。
     - **重解（$\alpha = \beta$）**：先得 $a_{n+1} - \alpha a_n = \alpha^{n-1}(a_2 - \alpha a_1)$，两边同除以 $\alpha^{n+1}$ 化为等差数列 $\left\{\dfrac{a_n}{\alpha^n}\right\}$。
5. **联立递推式（連立漸化式）**：$\begin{cases} a_{n+1} = p a_n + q b_n \\ b_{n+1} = r a_n + s b_n \end{cases}$
   - **解法 1（线性组合法）**：寻找常数 $x, y$ 使 $a_{n+1} + x b_{n+1} = y(a_n + x b_n)$，构造等比数列 $\{a_n + x b_n\}$。
   - **解法 2（消元法）**：消去 $b_n$ 化为关于 $a_n$ 的相邻三项递推式。
6. **分式型递推式（分数形の漸化式）**：$a_{n+1} = \dfrac{r a_n + s}{p a_n + q} \quad (p \neq 0,\; ps - qr \neq 0)$
   - 构造**特征方程**：$x = \dfrac{rx + s}{px + q} \iff px^2 + (q-r)x - s = 0$，设两解为 $\alpha, \beta$。
   - **若 $\alpha = \beta$（重解）**：令 $b_n = \dfrac{1}{a_n - \alpha}$，化为等差数列 $b_{n+1} = b_n + \dfrac{p}{r - p\alpha}$。
   - **若 $\alpha \neq \beta$（相异解）**：令 $c_n = \dfrac{a_n - \beta}{a_n - \alpha}$，化为等比数列 $c_{n+1} = \dfrac{r - p\beta}{r - p\alpha} c_n$。

### 1.2 数学归纳法（数学的帰納法）

证明关于所有自然数 $n$ 的命题 $P(n)$ 成立的标准两步：
- **[1] 基础步骤**：证明 $n = 1$ 时 $P(1)$ 成立（若命题要求 $n \ge m$，则验证 $n = m$）。
- **[2] 归纳步骤**：假设 $n = k$ 时 $P(k)$ 成立，证明 $n = k+1$ 时 $P(k+1)$ 亦成立。
- **强归纳法（累積帰納法 / $n \le k$ 仮定型）**：当推证 $P(k+1)$ 需要用到 $P(1), P(2), \dots, P(k)$ 全部结论时（如本切片 演習問題 6-(3)），在步骤 [2] 中假设「$n \le k$ 时 $P(n)$ 均成立」。

### 1.3 数列的极限（数列の極限）

1. **收敛与发散的严格定义**：
   - **収束（收敛）**：$\lim_{n\to\infty} a_n = \alpha$（有限定值），$\alpha$ 称为**極限値（极限值）**。
   - **発散（发散）**：不收敛的数列统称发散，细分为三种：
     - 正无穷大发散：$\lim_{n\to\infty} a_n = \infty$（有极限，但**不称极限值**）
     - 负无穷大发散：$\lim_{n\to\infty} a_n = -\infty$（有极限，但**不称极限值**）
     - **振動（振荡）**：如 $\{(-1)^n\}$，**没有极限（極限がない）**。
2. **四则运算性质（前提：$\{a_n\}, \{b_n\}$ 均收敛）**：
   - $\lim_{n\to\infty}(k a_n + l b_n) = k\alpha + l\beta$，$\lim_{n\to\infty} a_n b_n = \alpha\beta$，$\lim_{n\to\infty}\dfrac{a_n}{b_n} = \dfrac{\alpha}{\beta}\;(\beta \neq 0)$。
   - **不定型（不定形）**：$\infty - \infty,\; 0 \times \infty,\; \dfrac{\infty}{\infty},\; \dfrac{0}{0}$ 不能直接套用四则运算，必须先恒等变形。
   > ⚠️ **教材勘误提示**：原教材第 282 页（`page_0283.jpg`）[1.2] ③ 式误印为 $\lim_{n\to\infty}(k a_n + k b_n) = k\alpha + k\beta$（ただし $k, l$ は定数），实际应为 $\lim_{n\to\infty}(k a_n + l b_n) = k\alpha + l\beta$；另第 283 页（`page_0284.jpg`）解説中「性質 1～5」指代 [1.2] 中的 5 条运算法则（定数倍、和、差、积、商）。
3. **大小关系与夹逼定理（はさみうちの原理）**：
   - 若对所有 $n$ 有 $a_n \le b_n$（哪怕严格 $a_n < b_n$），且两者均收敛，则**只能推出 $\alpha \le \beta$**（等号可能成立！如 $a_n = \frac{1}{n} < b_n = \frac{2}{n}$，但极限均为 $0$）。
   - **はさみうちの原理**：若 $a_n \le c_n \le b_n$ 且 $\lim_{n\to\infty} a_n = \lim_{n\to\infty} b_n = \alpha$，则 $\lim_{n\to\infty} c_n = \alpha$。
4. **幂函数型与无穷等比数列的极限**：
   - 当 $k > 0$ 时：$\lim_{n\to\infty} n^k = \infty$，$\lim_{n\to\infty} \dfrac{1}{n^k} = 0$。
   - **无穷等比数列 $\{r^n\}$ 的极限**：
     $$\lim_{n\to\infty} r^n = \begin{cases} \infty & (r > 1) \\ 1 & (r = 1) \\ 0 & (|r| < 1) \\ \text{振動する（極限なし）} & (r \le -1) \end{cases}$$
     **核心结论**：$\{r^n\}$ 收敛的充要条件为 **$-1 < r \le 1$**（注意 $r = 1$ 包含在内，$-1$ 不包含！）。

<svg viewBox="0 0 640 210" xmlns="http://www.w3.org/2000/svg" style="max-width:640px;width:100%;height:auto;display:block;margin:12px auto;">
  <rect x="0" y="0" width="640" height="210" fill="#fafafa" rx="8" stroke="#e0e0e0"/>
  <!-- Left plot: a_n = 1/n -->
  <text x="155" y="22" font-size="13" font-weight="bold" text-anchor="middle" fill="#1a237e">収束の例：aₙ = 1/n → 0</text>
  <line x1="40" y1="160" x2="285" y2="160" stroke="#333" stroke-width="1.5"/>
  <polygon points="285,156 293,160 285,164" fill="#333"/>
  <line x1="55" y1="180" x2="55" y2="42" stroke="#333" stroke-width="1.5"/>
  <polygon points="51,42 55,34 59,42" fill="#333"/>
  <text x="295" y="164" font-size="12" fill="#333">n</text>
  <text x="42" y="42" font-size="12" fill="#333">aₙ</text>
  <text x="42" y="175" font-size="11" fill="#333">O</text>
  <!-- y ticks -->
  <line x1="51" y1="70" x2="59" y2="70" stroke="#333"/>
  <text x="38" y="74" font-size="11" fill="#333">1</text>
  <line x1="51" y1="115" x2="59" y2="115" stroke="#333"/>
  <text x="30" y="119" font-size="11" fill="#333">1/2</text>
  <!-- curve & points for 1/n -->
  <path d="M 90 70 Q 125 115, 160 130 T 265 147" fill="none" stroke="#90caf9" stroke-width="1.5" stroke-dasharray="4,3"/>
  <circle cx="90" cy="70" r="3.5" fill="#1565c0"/>
  <circle cx="125" cy="115" r="3.5" fill="#1565c0"/>
  <circle cx="160" cy="130" r="3.5" fill="#1565c0"/>
  <circle cx="195" cy="137.5" r="3.5" fill="#1565c0"/>
  <circle cx="230" cy="142" r="3.5" fill="#1565c0"/>
  <circle cx="265" cy="145" r="3.5" fill="#1565c0"/>
  <text x="87" y="175" font-size="11" fill="#555">1</text>
  <text x="122" y="175" font-size="11" fill="#555">2</text>
  <text x="157" y="175" font-size="11" fill="#555">3</text>
  <text x="192" y="175" font-size="11" fill="#555">4</text>
  <text x="227" y="175" font-size="11" fill="#555">5</text>
  <text x="262" y="175" font-size="11" fill="#555">6</text>

  <!-- Divider -->
  <line x1="320" y1="18" x2="320" y2="195" stroke="#ddd" stroke-dasharray="4,4"/>

  <!-- Right plot: a_n = (-1)^n -->
  <text x="485" y="22" font-size="13" font-weight="bold" text-anchor="middle" fill="#b71c1c">振動の例：aₙ = (-1)ⁿ（極限なし）</text>
  <line x1="355" y1="115" x2="605" y2="115" stroke="#333" stroke-width="1.5"/>
  <polygon points="605,111 613,115 605,119" fill="#333"/>
  <line x1="370" y1="185" x2="370" y2="42" stroke="#333" stroke-width="1.5"/>
  <polygon points="366,42 370,34 374,42" fill="#333"/>
  <text x="616" y="119" font-size="12" fill="#333">n</text>
  <text x="357" y="42" font-size="12" fill="#333">aₙ</text>
  <text x="357" y="129" font-size="11" fill="#333">O</text>
  <!-- y=1 and y=-1 dashed -->
  <line x1="370" y1="65" x2="595" y2="65" stroke="#ef9a9a" stroke-dasharray="4,3"/>
  <text x="355" y="69" font-size="11" fill="#333">1</text>
  <line x1="370" y1="165" x2="595" y2="165" stroke="#ef9a9a" stroke-dasharray="4,3"/>
  <text x="349" y="169" font-size="11" fill="#333">-1</text>
  <!-- zigzag -->
  <polyline points="405,165 440,65 475,165 510,65 545,165 580,65" fill="none" stroke="#e57373" stroke-width="1.2" stroke-dasharray="3,2"/>
  <circle cx="405" cy="165" r="3.5" fill="#c62828"/>
  <circle cx="440" cy="65" r="3.5" fill="#c62828"/>
  <circle cx="475" cy="165" r="3.5" fill="#c62828"/>
  <circle cx="510" cy="65" r="3.5" fill="#c62828"/>
  <circle cx="545" cy="165" r="3.5" fill="#c62828"/>
  <circle cx="580" cy="65" r="3.5" fill="#c62828"/>
  <text x="402" y="130" font-size="10" fill="#555">1</text>
  <text x="437" y="130" font-size="10" fill="#555">2</text>
  <text x="472" y="130" font-size="10" fill="#555">3</text>
  <text x="507" y="130" font-size="10" fill="#555">4</text>
  <text x="542" y="130" font-size="10" fill="#555">5</text>
  <text x="577" y="130" font-size="10" fill="#555">6</text>
</svg>

<svg viewBox="0 0 640 105" xmlns="http://www.w3.org/2000/svg" style="max-width:640px;width:100%;height:auto;display:block;margin:10px auto;">
  <rect x="0" y="0" width="640" height="105" fill="#fafafa" rx="8" stroke="#e0e0e0"/>
  <text x="320" y="20" font-size="13" font-weight="bold" text-anchor="middle" fill="#1a237e">無限等比数列 {rⁿ} の公比 r による収束・発散の分類</text>
  <!-- Number line -->
  <line x1="35" y1="62" x2="600" y2="62" stroke="#333" stroke-width="2"/>
  <polygon points="600,57 610,62 600,67" fill="#333"/>
  <text x="615" y="66" font-size="12" font-weight="bold" fill="#333">r</text>
  <!-- Highlight convergence region (-1, 1] -->
  <line x1="210" y1="62" x2="430" y2="62" stroke="#2e7d32" stroke-width="5"/>
  <!-- Highlight divergence regions -->
  <line x1="35" y1="62" x2="205" y2="62" stroke="#c62828" stroke-width="3" stroke-dasharray="5,3"/>
  <line x1="435" y1="62" x2="595" y2="62" stroke="#e65100" stroke-width="3" stroke-dasharray="5,3"/>
  <!-- Points -1 and 1 -->
  <circle cx="210" cy="62" r="5" fill="#ffffff" stroke="#c62828" stroke-width="2.5"/>
  <text x="210" y="83" font-size="12" font-weight="bold" text-anchor="middle" fill="#333">-1</text>
  <circle cx="430" cy="62" r="5" fill="#2e7d32" stroke="#2e7d32" stroke-width="2"/>
  <text x="430" y="83" font-size="12" font-weight="bold" text-anchor="middle" fill="#333">1</text>
  <!-- Labels -->
  <text x="120" y="45" font-size="11" font-weight="bold" text-anchor="middle" fill="#c62828">振動（極限なし）</text>
  <text x="120" y="96" font-size="10" text-anchor="middle" fill="#c62828">r ≤ -1</text>
  <text x="320" y="45" font-size="11" font-weight="bold" text-anchor="middle" fill="#2e7d32">0 に収束（lim rⁿ = 0）</text>
  <text x="320" y="96" font-size="10" text-anchor="middle" fill="#2e7d32">-1 &lt; r &lt; 1</text>
  <text x="430" y="37" font-size="10" font-weight="bold" text-anchor="middle" fill="#1b5e20">1 に収束</text>
  <text x="520" y="45" font-size="11" font-weight="bold" text-anchor="middle" fill="#e65100">+∞ に発散</text>
  <text x="520" y="96" font-size="10" text-anchor="middle" fill="#e65100">r &gt; 1</text>
</svg>

### 1.4 国内高中 vs. 日本 EJU 考纲差异与备课提醒

| 对比维度 | 国内高中习惯 | 日本 EJU 习惯 | 备课/应试提醒 |
| :--- | :--- | :--- | :--- |
| **相邻三项/分式递推** | 高考已弱化，仅竞赛或压轴题偶尔涉及 | **EJU 数学Ⅱ・B 高频常规题型**，要求熟练写出特征方程并分类变形 | 务必牢记「三项递推 3 种根」「分式递推 2 种根」的标准换元模板 |
| **数学归纳法** | 仅在选修中简单介绍，高考极少直接要求完整书写 | **日本二次校内考必考大题**，严格要求写清 [1] 基础步骤、[2] 归纳假设与推证、以及最终结语 | 需重点训练「先算 $a_2, a_3, a_4$ 猜测通项再用归纳法证明」与「强归纳法（$n \le k$）」 |
| **极限存在与极限值** | 国内高中不考数列极限，大学高数中 $\lim = \infty$ 称「极限不存在」 | 日本高中数学Ⅲ明确区分：**「極限がある（含 $\pm\infty$）」**与**「極限値（仅限收敛的有限值）」** | 审题时务必分清「極限を求めよ」与「極限値を求めよ」的微妙差别 |
| **夹逼定理** | 大学高数称「夹逼准则/迫敛定理」 | 日本统称 **はさみうちの原理**（意为“两面夹击原理”） | 处理含 $\sin, \cos$ 或复杂和式的极限时首选该方法 |
| **无穷等比数列收敛** | 国内高中不系统考查 | 必考判定条件 **$-1 < r \le 1$**（若首项为 $a$，则 $a = 0$ 或 $-1 < r \le 1$） | 极易漏掉 $r = 1$（或 $a = 0$）的边界情况！ |

---

## 二、日文核心词汇与公式假名注音

### 2.1 本切片日文核心词汇

- 漸化式（ぜんかしき / zenkashiki） — 递推公式（递推关系式）
- 隣接3項間の漸化式（りんせつさんこうかんのぜんかしき / rinsetsu sankoukan no zenkashiki） — 相邻三项递推公式
- 特性方程式（とくせいほうていしき / tokusei houteishiki） — 特征方程
- 階差数列（かいさすうれつ / kaisa suuretsu） — 阶差数列
- 等比数列（とうびすうれつ / toubi suuretsu） — 等比数列
- 公比（こうひ / kouhi） — 公比
- 連立漸化式（れんりつぜんかしき / renritsu zenkashiki） — 联立递推公式
- 分数形の漸化式（ぶんすうけいのぜんかしき / bunsuukei no zenkashiki） — 分式型递推公式
- 数学的帰納法（すうがくてききのうほう / suugakuteki kinouhou） — 数学归纳法
- 推測（すいそく / suisoku） — 推测、猜想
- 微分積分（びぶんせきぶん / bibun sekibun） — 微积分
- 無限数列（むげんすうれつ / mugen suuretsu） — 无穷数列
- 極限（きょくげん / kyokugen） — 极限
- 極限値（きょくげんち / kyokugenchi） — 极限值
- 収束（しゅうそく / shuusoku） — 收敛
- 発散（はっさん / hassan） — 发散
- 振動（しんどう / shindou） — 振荡
- 無限大（むげんだい / mugendai） — 无穷大（$\infty$）
- 正の無限大（せいのむげんだい / sei no mugendai） — 正无穷大（$+\infty$）
- 負の無限大（ふのむげんだい / fu no mugendai） — 负无穷大（$-\infty$）
- 不定形（ふていけい / futeikei） — 不定型（未定式）
- はさみうちの原理（はさみうちのげんり / hasamiuchi no genri） — 夹逼定理
- 無限等比数列（むげんとうびすうれつ / mugen toubi suuretsu） — 无穷等比数列

### 2.2 核心公式的日本课堂口语读法

1. **相邻三项递推式变形** $a_{n+2} - \alpha a_{n+1} = \beta (a_{n+1} - \alpha a_n)$
   - 课堂读法：**エー エヌ たす に ひく アルファ エー エヌ たす いち イコール ベータ かっこ エー エヌ たす いち ひく アルファ エー エヌ かっことじ**
2. **数列极限** $\lim_{n\to\infty} a_n = \alpha$
   - 课堂读法：**リミット エヌ やじるし むげんだい の エー エヌ イコール アルファ**（也常说 **エヌ を むげんだい に ちかづける とき、エー エヌ は アルファ に しゅうそく する**）
   - 备注：$\lim$ 读作 **リミット（limit）**，$\to$ 读作 **やじるし** 或 **に ちかづける**，$\infty$ 读作 **むげんだい（無限大）**。
3. **发散到正/负无穷大** $\lim_{n\to\infty} a_n = \infty$ / $\lim_{n\to\infty} a_n = -\infty$
   - 课堂读法：**エー エヌ は せいの むげんだい（ふの むげんだい）に はっさん する**
4. **夹逼定理** $a_n \le c_n \le b_n$
   - 课堂读法：**エー エヌ しょうなり イコール シー エヌ しょうなり イコール ビー エヌ**；定理名称读作 **はさみうちの げんり**。
5. **无穷等比数列收敛条件** $-1 < r \le 1$
   - 课堂读法：**マイナス いち しょうなり アール しょうなり イコール いち**

---

## 三、逐题深度解析（不可跳步）

---

### 演習問題 4（種々の漸化式：指数型・逆数型・対数型・$n$ を含む型）

#### 演習問題 4-(3) [1]（P271）
- **【原题重现与翻译】**
  - 原题：次の条件によって定められる数列 $\{a_n\}$ の一般項を求めよ。
    $a_1 = 3,\; a_{n+1} = 2a_n + 3^{n+1}$
  - 中文：求由下列条件确定的数列 $\{a_n\}$ 的通项公式：$a_1 = 3,\; a_{n+1} = 2a_n + 3^{n+1}$。
- **【考点定位】**
  - 指数型线性递推式 $a_{n+1} = p a_n + q^{n+1}$ 的标准解法（同除以 $q^{n+1}$ 降阶为 $b_{n+1} = \frac{p}{q} b_n + 1$）。
- **【分步标准解答】**
  漸化式の両辺を $3^{n+1}$ で割ると，
  $$\frac{a_{n+1}}{3^{n+1}} = \frac{2}{3} \cdot \frac{a_n}{3^n} + 1$$
  > 💡 讲师批注：两边也可以同除以 $2^{n+1}$ 化为阶差数列，但同除以 $3^{n+1}$ 后常数项直接变成 $1$，计算量更小、更不容易出错。

  ここで $b_n = \dfrac{a_n}{3^n}$ とおくと，$b_1 = \dfrac{a_1}{3^1} = \dfrac{3}{3} = 1$ であり，
  $$b_{n+1} = \frac{2}{3} b_n + 1$$
  この特性方程式 $\alpha = \dfrac{2}{3}\alpha + 1$ を解くと $\alpha = 3$ であるから，漸化式は次のように変形できる。
  $$b_{n+1} - 3 = \frac{2}{3}(b_n - 3)$$
  > 💡 讲师批注：检验变形是否正确：展开右边得 $\frac{2}{3}b_n - 2$，移项 $-3$ 到右边得 $\frac{2}{3}b_n + 1$，完全一致。

  よって，数列 $\{b_n - 3\}$ は初項 $b_1 - 3 = 1 - 3 = -2$，公比 $\dfrac{2}{3}$ の等比数列である。
  $$b_n - 3 = -2 \left(\frac{2}{3}\right)^{n-1}$$
  $$b_n = 3 - 2 \left(\frac{2}{3}\right)^{n-1}$$
  したがって，
  $$a_n = 3^n b_n = 3^n \left\{3 - 2 \cdot \frac{2^{n-1}}{3^{n-1}}\right\} = 3^{n+1} - 3 \cdot 2^n$$
  > 💡 讲师批注：最后一步展开时注意 $3^n \cdot \frac{2^{n-1}}{3^{n-1}} = 3 \cdot 2^{n-1}$，再乘以系数 $2$ 得 $3 \cdot 2^n$。代入验算：$n=1 \Rightarrow 9-6=3$；$n=2 \Rightarrow 27-12=15$（递推 $2\cdot 3 + 3^2 = 15$ ✓）。
- **【最终答案】**
  **$a_n = 3^{n+1} - 3 \cdot 2^n$**

---

#### 演習問題 4-(3) [2]（P271）
- **【原题重现与翻译】**
  - 原题：次の条件によって定められる数列 $\{a_n\}$ の一般項を求めよ。
    $a_1 = \dfrac{1}{5},\; a_{n+1} = \dfrac{a_n}{4a_n - 1}$
  - 中文：求由下列条件确定的数列 $\{a_n\}$ 的通项公式：$a_1 = \dfrac{1}{5},\; a_{n+1} = \dfrac{a_n}{4a_n - 1}$。
- **【考点定位】**
  - 倒数型分式递推式 $a_{n+1} = \dfrac{a_n}{p a_n + q}$ 的解法（先证 $a_n \neq 0$ 再取倒数）。
- **【分步标准解答】**
  まず，すべての自然数 $n$ について $a_n \neq 0$ であることを確認する。もし $a_{k+1} = 0$ となる自然数 $k$ が存在すると仮定すると，漸化式より $a_k = 0$ となり，これを繰り返すと $a_1 = 0$ となって $a_1 = \dfrac{1}{5}$ に反する。よって，すべての自然数 $n$ について $a_n \neq 0$ である。
  > 💡 讲师批注：在取倒数之前，**必须先说明 $a_n \neq 0$**，这是日本国公立二次考试和 EJU 記述题的必给采分点，不可省略。

  したがって，漸化式の両辺の逆数をとることができて，
  $$\frac{1}{a_{n+1}} = \frac{4a_n - 1}{a_n} = -\frac{1}{a_n} + 4$$
  ここで $b_n = \dfrac{1}{a_n}$ とおくと，$b_1 = \dfrac{1}{a_1} = 5$ であり，
  $$b_{n+1} = -b_n + 4$$
  特性方程式 $\alpha = -\alpha + 4$ より $\alpha = 2$ であるから，
  $$b_{n+1} - 2 = -(b_n - 2)$$
  よって，数列 $\{b_n - 2\}$ は初項 $b_1 - 2 = 5 - 2 = 3$，公比 $-1$ の等比数列である。
  $$b_n - 2 = 3(-1)^{n-1} \implies b_n = 2 + 3(-1)^{n-1}$$
  ここで，すべての自然数 $n$ について $2 + 3(-1)^{n-1}$ は $5$ または $-1$ であり $0$ にならないから，
  $$a_n = \frac{1}{b_n} = \frac{1}{2 + 3(-1)^{n-1}}$$
  > 💡 讲师批注：本数列实际是一个周期为 $2$ 的振荡数列：$\frac{1}{5}, -1, \frac{1}{5}, -1, \dots$。代入递推式验算：$a_2 = \frac{1/5}{4/5 - 1} = -1$，$a_3 = \frac{-1}{-4 - 1} = \frac{1}{5}$，完全正确！
- **【最终答案】**
  **$a_n = \dfrac{1}{2 + 3(-1)^{n-1}}$**（也可等价写为：$n$ が奇数のとき $\dfrac{1}{5}$，$n$ が偶数のとき $-1$）

---

#### 演習問題 4-(4) [1]（P272）
- **【原题重现与翻译】**
  - 原题：次の条件によって定められる数列 $\{a_n\}$ の一般項を求めよ。
    $a_1 = 1,\; a_{n+1} = 2\sqrt{a_n}$
  - 中文：求由下列条件确定的数列 $\{a_n\}$ 的通项公式：$a_1 = 1,\; a_{n+1} = 2\sqrt{a_n}$。
- **【考点定位】**
  - 根式/幂次型递推式（先证 $a_n > 0$，再两边取对数转化为线性递推式）。
- **【分步标准解答】**
  $a_1 = 1 > 0$ および漸化式 $a_{n+1} = 2\sqrt{a_n}$ より，すべての自然数 $n$ について $a_n > 0$ である。
  > 💡 讲师批注：取对数前务必说明真数条件 $a_n > 0$！由于递推式系数含 $2$，因此选择以 $2$ 为底的对数 $\log_2$ 最简洁。

  両辺の $2$ を底とする対数をとると，
  $$\log_2 a_{n+1} = \log_2 \left(2 a_n^{\frac{1}{2}}\right) = 1 + \frac{1}{2}\log_2 a_n$$
  ここで $b_n = \log_2 a_n$ とおくと，$b_1 = \log_2 1 = 0$ であり，
  $$b_{n+1} = \frac{1}{2} b_n + 1$$
  特性方程式 $\alpha = \dfrac{1}{2}\alpha + 1$ より $\alpha = 2$ であるから，
  $$b_{n+1} - 2 = \frac{1}{2}(b_n - 2)$$
  よって，数列 $\{b_n - 2\}$ は初項 $b_1 - 2 = 0 - 2 = -2$，公比 $\dfrac{1}{2}$ の等比数列である。
  $$b_n - 2 = -2 \left(\frac{1}{2}\right)^{n-1} = -\left(\frac{1}{2}\right)^{n-2}$$
  $$b_n = 2 - \left(\frac{1}{2}\right)^{n-2} = 2 - \frac{1}{2^{n-2}}$$
  したがって，$\log_2 a_n = 2 - \dfrac{1}{2^{n-2}}$ より，
  $$a_n = 2^{\,2 - \frac{1}{2^{n-2}}}$$
  > 💡 讲师批注：验算前三项：$n=1 \Rightarrow 2^{2-2}=1$；$n=2 \Rightarrow 2^{2-1}=2$（递推 $2\sqrt{1}=2$ ✓）；$n=3 \Rightarrow 2^{2-1/2}=2\sqrt{2}$（递推 $2\sqrt{2}$ ✓）。
- **【最终答案】**
  **$a_n = 2^{\,2 - \frac{1}{2^{n-2}}}$**（或写作 **$2^{2 - 2^{2-n}}$**）

---

#### 演習問題 4-(4) [2]（P272）
- **【原题重现与翻译】**
  - 原题（教材原印）：$a_1 = \dfrac{1}{2},\; (n+1)a_{n+1} = (n-1)a_{n-1} \quad (n \ge 2)$
  - > ⚠️ **教材勘误提示**：原教材第 271 页（`page_0272.jpg`）将左边误印为 $(n+1)a_{n+1}$。若按原印，令 $n=2$ 可得 $3a_3 = a_1$，但令 $n=3$ 得 $4a_4 = 2a_2$，因题干未给出 $a_2$，所有偶数项均无法确定！结合条件 $(n \ge 2)$ 与初项 $a_1 = \dfrac{1}{2} = \dfrac{1}{1\cdot 2}$，原题正确题干应为：**$a_1 = \dfrac{1}{2},\; (n+1)a_n = (n-1)a_{n-1} \quad (n \ge 2)$**。以下按修正后题干给出标准解答。
  - 中文（修正后）：求由 $a_1 = \dfrac{1}{2},\; (n+1)a_n = (n-1)a_{n-1} \ (n \ge 2)$ 确定的数列 $\{a_n\}$ 的通项公式。
- **【考点定位】**
  - 含 $n$ 的变系数递推式（补齐对称因子构造常数列）。
- **【分步标准解答】**
  $(n+1)a_n = (n-1)a_{n-1} \ (n \ge 2)$ の両辺に $n$ を掛けると，
  $$n(n+1)a_n = (n-1)n a_{n-1} \qquad (n \ge 2)$$
  > 💡 讲师批注：观察左边系数 $(n+1)$ 与右边系数 $(n-1)$ 中间恰好缺了一个 $n$！两边同乘 $n$ 后，左边变成 $n(n+1)a_n$，右边变成 $(n-1)n a_{n-1}$，恰好是同一函数 $f(n) = n(n+1)a_n$ 的相邻两项！

  ここで $b_n = n(n+1)a_n$ とおくと，$n \ge 2$ のとき $b_n = b_{n-1}$ であるから，
  $$b_n = b_{n-1} = \cdots = b_1$$
  また，$b_1 = 1 \cdot 2 \cdot a_1 = 2 \cdot \frac{1}{2} = 1$ であるから，すべての自然数 $n$ について，
  $$n(n+1)a_n = 1$$
  よって，
  $$a_n = \frac{1}{n(n+1)}$$
  > 💡 讲师批注：验算 $n=1$：$a_1 = \frac{1}{1\cdot 2} = \frac{1}{2}$ 满足初值；$n=2$：$3a_2 = 1\cdot a_1 \Rightarrow 3\cdot \frac{1}{6} = \frac{1}{2}$ ✓。
- **【最终答案】**
  **$a_n = \dfrac{1}{n(n+1)}$**

---

#### 演習問題 4-(5)（P273）
- **【原题重现与翻译】**
  - 原题：$a_1 = 2,\; a_{n+1} = \dfrac{n+2}{n}a_n + 1$ によって定められる数列 $\{a_n\}$ がある。
    [1] $\dfrac{a_n}{n(n+1)} = b_n$ とおくとき，$b_{n+1}$ を $b_n$ と $n$ の式で表せ。
    [2] $a_n$ を $n$ の式で表せ。
  - 中文：已知数列 $\{a_n\}$ 由 $a_1 = 2,\; a_{n+1} = \dfrac{n+2}{n}a_n + 1$ 确定。
    [1] 设 $\dfrac{a_n}{n(n+1)} = b_n$，用 $b_n$ 与 $n$ 表示 $b_{n+1}$。
    [2] 用 $n$ 表示 $a_n$。
- **【考点定位】**
  - 含 $n$ 的分式系数递推式换元 + 裂项相消（部分分数分解）求阶差数列和。
- **【分步标准解答】**
  **[1]** $a_{n+1} = \dfrac{n+2}{n}a_n + 1$ の両辺を $(n+1)(n+2)$ で割ると，
  $$\frac{a_{n+1}}{(n+1)(n+2)} = \frac{a_n}{n(n+1)} + \frac{1}{(n+1)(n+2)}$$
  > 💡 讲师批注：因为 $b_n = \dfrac{a_n}{n(n+1)}$，所以 $b_{n+1} = \dfrac{a_{n+1}}{(n+1)(n+2)}$。两边同除以 $(n+1)(n+2)$ 即可精确凑出 $b_{n+1}$ 与 $b_n$。

  $\dfrac{a_n}{n(n+1)} = b_n$ より $\dfrac{a_{n+1}}{(n+1)(n+2)} = b_{n+1}$ であるから，
  $$b_{n+1} = b_n + \frac{1}{(n+1)(n+2)}$$

  **[2]** $b_1 = \dfrac{a_1}{1 \cdot 2} = \dfrac{2}{2} = 1$ であり，[1] より
  $$b_{n+1} - b_n = \frac{1}{(n+1)(n+2)} = \frac{1}{n+1} - \frac{1}{n+2}$$
  $n \ge 2$ のとき，階差数列の公式より
  $$b_n = b_1 + \sum_{k=1}^{n-1} \left(\frac{1}{k+1} - \frac{1}{k+2}\right)$$
  $$= 1 + \left\{\left(\frac{1}{2} - \frac{1}{3}\right) + \left(\frac{1}{3} - \frac{1}{4}\right) + \cdots + \left(\frac{1}{n} - \frac{1}{n+1}\right)\right\}$$
  $$= 1 + \left(\frac{1}{2} - \frac{1}{n+1}\right) = \frac{3}{2} - \frac{1}{n+1} = \frac{3n+1}{2(n+1)}$$
  > 💡 讲师批注：使用阶差数列求和公式 $\sum_{k=1}^{n-1}$ 时，**必须声明 $n \ge 2$**，最后再单独验证 $n = 1$ 是否也成立！

  $n = 1$ のとき，$\dfrac{3 \cdot 1 + 1}{2(1+1)} = \dfrac{4}{4} = 1 = b_1$ となるから，この式は $n = 1$ のときも成り立つ。
  したがって，すべての自然数 $n$ について，
  $$a_n = n(n+1)b_n = n(n+1) \cdot \frac{3n+1}{2(n+1)} = \frac{n(3n+1)}{2}$$
  > 💡 讲师批注：验算：$n=1 \Rightarrow 2$；$n=2 \Rightarrow \frac{2\cdot 7}{2}=7$（递推 $\frac{3}{1}\cdot 2 + 1 = 7$ ✓）；$n=3 \Rightarrow \frac{3\cdot 10}{2}=15$（递推 $\frac{4}{2}\cdot 7 + 1 = 15$ ✓）。
- **【最终答案】**
  **[1] $b_{n+1} = b_n + \dfrac{1}{(n+1)(n+2)}$**
  **[2] $a_n = \dfrac{n(3n+1)}{2}$**

---

### 演習問題 5（隣接 3 項間・連立・分数形・$S_n$ を含む漸化式）

<svg viewBox="0 0 640 165" xmlns="http://www.w3.org/2000/svg" style="max-width:640px;width:100%;height:auto;display:block;margin:10px auto;">
  <rect x="0" y="0" width="640" height="165" fill="#fafafa" rx="8" stroke="#e0e0e0"/>
  <!-- Top box -->
  <rect x="170" y="10" width="300" height="32" rx="6" fill="#e8eaf6" stroke="#3f51b5" stroke-width="1.5"/>
  <text x="320" y="30" font-size="12" font-weight="bold" text-anchor="middle" fill="#1a237e">特性方程式 px² + qx + r = 0 の解 α, β</text>
  <!-- Arrows -->
  <line x1="240" y1="42" x2="105" y2="68" stroke="#555" stroke-width="1.3"/>
  <line x1="320" y1="42" x2="320" y2="68" stroke="#555" stroke-width="1.3"/>
  <line x1="400" y1="42" x2="535" y2="68" stroke="#555" stroke-width="1.3"/>
  <!-- Case 1 -->
  <rect x="15" y="70" width="185" height="82" rx="6" fill="#e8f5e9" stroke="#2e7d32" stroke-width="1.2"/>
  <text x="107" y="88" font-size="11" font-weight="bold" text-anchor="middle" fill="#1b5e20">[1] α ≠ β かつ α, β ≠ 1</text>
  <text x="107" y="106" font-size="10" text-anchor="middle" fill="#333">2 本の等比数列を作り</text>
  <text x="107" y="122" font-size="10" text-anchor="middle" fill="#333">aₙ₊₁ を消去して aₙ を得る</text>
  <text x="107" y="141" font-size="10" font-weight="bold" text-anchor="middle" fill="#2e7d32">→ 演習 5-(1)[1]</text>
  <!-- Case 2 -->
  <rect x="220" y="70" width="200" height="82" rx="6" fill="#fff3e0" stroke="#ef6c00" stroke-width="1.2"/>
  <text x="320" y="88" font-size="11" font-weight="bold" text-anchor="middle" fill="#e65100">[2] 解に 1 を含む（α = 1）</text>
  <text x="320" y="106" font-size="10" text-anchor="middle" fill="#333">aₙ₊₂ - aₙ₊₁ = β(aₙ₊₁ - aₙ)</text>
  <text x="320" y="122" font-size="10" text-anchor="middle" fill="#333">階差数列の公式で一発解決</text>
  <text x="320" y="141" font-size="10" font-weight="bold" text-anchor="middle" fill="#ef6c00">→ 演習 5-(1)[2]</text>
  <!-- Case 3 -->
  <rect x="440" y="70" width="185" height="82" rx="6" fill="#fce4ec" stroke="#c2185b" stroke-width="1.2"/>
  <text x="532" y="88" font-size="11" font-weight="bold" text-anchor="middle" fill="#880e4f">[3] 重解（α = β）</text>
  <text x="532" y="106" font-size="10" text-anchor="middle" fill="#333">aₙ₊₁ - αaₙ = αⁿ⁻¹(a₂ - αa₁)</text>
  <text x="532" y="122" font-size="10" text-anchor="middle" fill="#333">両辺を αⁿ⁺¹ で割り等差数列化</text>
  <text x="532" y="141" font-size="10" font-weight="bold" text-anchor="middle" fill="#c2185b">→ 演習 5-(1)[3]</text>
</svg>

#### 演習問題 5-(1) [1]（P277）
- **【原题重现与翻译】**
  - 原题：次の条件によって定められる数列 $\{a_n\}$ の一般項を求めよ。
    $a_1 = 0,\; a_2 = 1,\; a_{n+2} = 4a_{n+1} + 6a_n$
  - 中文：求由 $a_1 = 0,\; a_2 = 1,\; a_{n+2} = 4a_{n+1} + 6a_n$ 确定的数列 $\{a_n\}$ 的通项公式。
- **【考点定位】**
  - 相邻三项递推式（特征方程有两个不等于 $1$ 的相异实根）。
- **【分步标准解答】**
  漸化式を $a_{n+2} - 4a_{n+1} - 6a_n = 0$ と変形すると，特性方程式は
  $$x^2 - 4x - 6 = 0$$
  これを解くと $x = 2 \pm \sqrt{10}$。そこで $\alpha = 2 + \sqrt{10},\; \beta = 2 - \sqrt{10}$ とおくと，漸化式は次の 2 通りに変形できる。
  $$a_{n+2} - \alpha a_{n+1} = \beta(a_{n+1} - \alpha a_n) \qquad \cdots \text{①}$$
  $$a_{n+2} - \beta a_{n+1} = \alpha(a_{n+1} - \beta a_n) \qquad \cdots \text{②}$$
  > 💡 讲师批注：即使特征根是无理数（$2 \pm \sqrt{10}$），也**先用字母 $\alpha, \beta$ 代写全程**，直到最后一步才代回具体数值，可极大避免根号计算出错！

  ① より，数列 $\{a_{n+1} - \alpha a_n\}$ は初項 $a_2 - \alpha a_1 = 1 - 0 = 1$，公比 $\beta$ の等比数列であるから，
  $$a_{n+1} - \alpha a_n = \beta^{n-1} \qquad \cdots \text{③}$$
  ② より，数列 $\{a_{n+1} - \beta a_n\}$ は初項 $a_2 - \beta a_1 = 1 - 0 = 1$，公比 $\alpha$ の等比数列であるから，
  $$a_{n+1} - \beta a_n = \alpha^{n-1} \qquad \cdots \text{④}$$
  ④ $-$ ③ より，
  $$(\alpha - \beta)a_n = \alpha^{n-1} - \beta^{n-1}$$
  ここで $\alpha - \beta = (2 + \sqrt{10}) - (2 - \sqrt{10}) = 2\sqrt{10}$ であるから，
  $$a_n = \frac{1}{2\sqrt{10}}\left\{(2 + \sqrt{10})^{n-1} - (2 - \sqrt{10})^{n-1}\right\} = \frac{\sqrt{10}}{20}\left\{(2 + \sqrt{10})^{n-1} - (2 - \sqrt{10})^{n-1}\right\}$$
  > 💡 讲师批注：验算 $n=1,2,3,4$：$a_1 = 0$，$a_2 = 1$，$a_3 = \frac{8\sqrt{10}}{2\sqrt{10}} = 4$（递推 $4\cdot 1 + 6\cdot 0 = 4$ ✓），$a_4 = \frac{44\sqrt{10}}{2\sqrt{10}} = 22$（递推 $4\cdot 4 + 6\cdot 1 = 22$ ✓）。
- **【最终答案】**
  **$a_n = \dfrac{\sqrt{10}}{20}\left\{(2 + \sqrt{10})^{n-1} - (2 - \sqrt{10})^{n-1}\right\}$**

---

#### 演習問題 5-(1) [2]（P277）
- **【原题重现与翻译】**
  - 原题：次の条件によって定められる数列 $\{a_n\}$ の一般項を求めよ。
    $a_1 = 1,\; a_2 = 2,\; a_{n+2} + 4a_{n+1} - 5a_n = 0$
  - 中文：求由 $a_1 = 1,\; a_2 = 2,\; a_{n+2} + 4a_{n+1} - 5a_n = 0$ 确定的数列 $\{a_n\}$ 的通项公式。
- **【考点定位】**
  - 相邻三项递推式（特征方程的根包含 $1$ → 阶差数列法）。
- **【分步标准解答】**
  特性方程式 $x^2 + 4x - 5 = 0$ を解くと，$(x - 1)(x + 5) = 0$ より $x = 1, -5$。
  解に $1$ を含むので，漸化式は次のように変形できる。
  $$a_{n+2} - a_{n+1} = -5(a_{n+1} - a_n)$$
  > 💡 讲师批注：看到系数之和 $1 + 4 - 5 = 0$，应立刻反应出特征方程必有根 $x = 1$，直接变形为阶差数列比列两个方程相减快一倍！

  よって，数列 $\{a_{n+1} - a_n\}$ は初項 $a_2 - a_1 = 2 - 1 = 1$，公比 $-5$ の等比数列であるから，
  $$a_{n+1} - a_n = (-5)^{n-1}$$
  $n \ge 2$ のとき，階差数列の公式より
  $$a_n = a_1 + \sum_{k=1}^{n-1} (-5)^{k-1} = 1 + \frac{1 \cdot \left\{1 - (-5)^{n-1}\right\}}{1 - (-5)}$$
  $$= 1 + \frac{1 - (-5)^{n-1}}{6} = \frac{7 - (-5)^{n-1}}{6}$$
  $n = 1$ のとき，$\dfrac{7 - (-5)^0}{6} = \dfrac{6}{6} = 1 = a_1$ となるから，この式は $n = 1$ のときも成り立つ。
  > 💡 讲师批注：验算：$n=2 \Rightarrow \frac{7+5}{6} = 2$ ✓；$n=3 \Rightarrow \frac{7-25}{6} = -3$（递推 $-4(2)+5(1)=-3$ ✓）。
- **【最终答案】**
  **$a_n = \dfrac{7 - (-5)^{n-1}}{6}$**

---

#### 演習問題 5-(1) [3]（P277）
- **【原题重现与翻译】**
  - 原题：次の条件によって定められる数列 $\{a_n\}$ の一般項を求めよ。
    $a_1 = 0,\; a_2 = 2,\; a_{n+2} - 4a_{n+1} + 4a_n = 0$
  - 中文：求由 $a_1 = 0,\; a_2 = 2,\; a_{n+2} - 4a_{n+1} + 4a_n = 0$ 确定的数列 $\{a_n\}$ 的通项公式。
- **【考点定位】**
  - 相邻三项递推式（特征方程有重解 → 同除以 $\alpha^{n+1}$ 化为等差数列）。
- **【分步标准解答】**
  特性方程式 $x^2 - 4x + 4 = 0$ を解くと，$(x - 2)^2 = 0$ より重解 $x = 2$ をもつ。
  したがって，漸化式は次のように変形できる。
  $$a_{n+2} - 2a_{n+1} = 2(a_{n+1} - 2a_n)$$
  よって，数列 $\{a_{n+1} - 2a_n\}$ は初項 $a_2 - 2a_1 = 2 - 0 = 2$，公比 $2$ の等比数列であるから，
  $$a_{n+1} - 2a_n = 2 \cdot 2^{n-1} = 2^n$$
  この両辺を $2^{n+1}$ で割ると，
  $$\frac{a_{n+1}}{2^{n+1}} - \frac{a_n}{2^n} = \frac{1}{2}$$
  > 💡 讲师批注：重解型的关键一步就是两边同除以 $\alpha^{n+1}$（此处为 $2^{n+1}$），右边常数化为 $\frac{1}{2}$，直接变成等差数列！

  よって，数列 $\left\{\dfrac{a_n}{2^n}\right\}$ は初項 $\dfrac{a_1}{2^1} = 0$，公差 $\dfrac{1}{2}$ の等差数列である。
  $$\frac{a_n}{2^n} = 0 + (n - 1) \cdot \frac{1}{2} = \frac{n - 1}{2}$$
  したがって，
  $$a_n = (n - 1) \cdot 2^{n-1}$$
  > 💡 讲师批注：验算：$n=1 \Rightarrow 0$；$n=2 \Rightarrow 2$；$n=3 \Rightarrow 8$（递推 $4(2)-4(0)=8$ ✓）；$n=4 \Rightarrow 24$（递推 $4(8)-4(2)=24$ ✓）。
- **【最终答案】**
  **$a_n = (n - 1) \cdot 2^{n-1}$**

---

#### 演習問題 5-(2)（P278）
- **【原题重现与翻译】**
  - 原题：数列 $\{a_n\}, \{b_n\}$ を $a_1 = b_1 = 1,\; a_{n+1} = a_n + 4b_n,\; b_{n+1} = a_n + b_n$ で定めるとき
    [1] $a_{n+1} + x b_{n+1} = y(a_n + x b_n)$ を満たす $x, y$ の組を 2 組求めよ。
    [2] 数列 $\{a_n\}, \{b_n\}$ の一般項を求めよ。
  - 中文：设数列 $\{a_n\}, \{b_n\}$ 由 $a_1 = b_1 = 1,\; a_{n+1} = a_n + 4b_n,\; b_{n+1} = a_n + b_n$ 确定。
    [1] 求满足 $a_{n+1} + x b_{n+1} = y(a_n + x b_n)$ 的两组 $(x, y)$。
    [2] 求数列 $\{a_n\}, \{b_n\}$ 的通项公式。
- **【考点定位】**
  - 联立递推式（待定系数构造等比数列法）。
- **【分步标准解答】**
  **[1]** $a_{n+1} = a_n + 4b_n,\; b_{n+1} = a_n + b_n$ より，
  $$a_{n+1} + x b_{n+1} = (a_n + 4b_n) + x(a_n + b_n) = (1 + x)a_n + (4 + x)b_n$$
  これが $y(a_n + x b_n) = y a_n + xy b_n$ と恒等的に等しくなるように係数を比較すると，
  $$y = 1 + x \quad \cdots \text{①}, \qquad xy = 4 + x \quad \cdots \text{②}$$
  ① を ② に代入して，
  $$x(1 + x) = 4 + x \implies x^2 = 4 \implies x = \pm 2$$
  - $x = 2$ のとき，① より $y = 3$。
  - $x = -2$ のとき，① より $y = -1$。
  > 💡 讲师批注：这两组 $(x, y)$ 本质上对应转移矩阵 $\begin{pmatrix} 1 & 4 \\ 1 & 1 \end{pmatrix}$ 的左特征向量与特征值 $y = 3, -1$。

  **[2]** [1] の結果より，次の 2 つの漸化式が成り立つ。
  $$a_{n+1} + 2b_{n+1} = 3(a_n + 2b_n), \qquad a_{n+1} - 2b_{n+1} = -(a_n - 2b_n)$$
  数列 $\{a_n + 2b_n\}$ は初項 $a_1 + 2b_1 = 1 + 2 = 3$，公比 $3$ の等比数列であるから，
  $$a_n + 2b_n = 3 \cdot 3^{n-1} = 3^n \qquad \cdots \text{③}$$
  数列 $\{a_n - 2b_n\}$ は初項 $a_1 - 2b_1 = 1 - 2 = -1$，公比 $-1$ の等比数列であるから，
  $$a_n - 2b_n = (-1) \cdot (-1)^{n-1} = (-1)^n \qquad \cdots \text{④}$$
  (③ $+$ ④) $\div 2$ より，
  $$a_n = \frac{3^n + (-1)^n}{2}$$
  (③ $-$ ④) $\div 4$ より，
  $$b_n = \frac{3^n - (-1)^n}{4}$$
  > 💡 讲师批注：验算：$n=1 \Rightarrow a_1=1, b_1=1$；$n=2 \Rightarrow a_2=5, b_2=2$（递推 $a_2=1+4=5, b_2=1+1=2$ ✓）；$n=3 \Rightarrow a_3=13, b_3=7$（递推 $a_3=5+8=13, b_3=5+2=7$ ✓）。
- **【最终答案】**
  **[1] $(x, y) = (2, 3),\; (-2, -1)$**
  **[2] $a_n = \dfrac{3^n + (-1)^n}{2},\quad b_n = \dfrac{3^n - (-1)^n}{4}$**

---

#### 演習問題 5-(3)（P279）
- **【原题重现与翻译】**
  - 原题：数列 $\{a_n\}$ が $a_1 = 4,\; a_{n+1} = \dfrac{4a_n + 8}{a_n + 6}$ で定められている。
    [1] $b_n = \dfrac{a_n + 4}{a_n - 2}$ とおくとき，$b_{n+1}$ を $b_n$ で表せ。
    [2] 数列 $\{a_n\}$ の一般項を求めよ。
  - 中文：已知数列 $\{a_n\}$ 由 $a_1 = 4,\; a_{n+1} = \dfrac{4a_n + 8}{a_n + 6}$ 确定。
    [1] 设 $b_n = \dfrac{a_n + 4}{a_n - 2}$，用 $b_n$ 表示 $b_{n+1}$。
    [2] 求数列 $\{a_n\}$ 的通项公式。
- **【考点定位】**
  - 分式型递推式（特征方程 $x = \frac{4x+8}{x+6} \iff x^2 + 2x - 8 = 0$ 的两相异根 $\alpha = 2, \beta = -4$）。
- **【分步标准解答】**
  **[1]** まず $a_n > 2$ を確認する。$a_1 = 4 > 2$ であり，$a_k > 2$ のとき $a_{k+1} - 2 = \dfrac{4a_k + 8 - 2(a_k + 6)}{a_k + 6} = \dfrac{2(a_k - 2)}{a_k + 6} > 0$ より $a_{k+1} > 2$。よって，すべての自然数 $n$ について $a_n > 2$ であり，分母 $a_n - 2 \neq 0$ である。
  > 💡 讲师批注：即使题目给出了换元式 $b_n = \frac{a_n+4}{a_n-2}$，严谨作答时也应顺手确认分母 $a_n - 2 \neq 0$。同时注意观察：换元分子分母中的 $-4$ 和 $2$ 正是特征方程 $x = \frac{4x+8}{x+6}$ 的两个根！

  したがって，
  $$b_{n+1} = \frac{a_{n+1} + 4}{a_{n+1} - 2} = \frac{\dfrac{4a_n + 8}{a_n + 6} + 4}{\dfrac{4a_n + 8}{a_n + 6} - 2}$$
  分母・分子に $a_n + 6$ を掛けて整理すると，
  $$b_{n+1} = \frac{(4a_n + 8) + 4(a_n + 6)}{(4a_n + 8) - 2(a_n + 6)} = \frac{8a_n + 32}{2a_n - 4} = \frac{8(a_n + 4)}{2(a_n - 2)} = 4b_n$$

  **[2]** $b_1 = \dfrac{a_1 + 4}{a_1 - 2} = \dfrac{4 + 4}{4 - 2} = 4$ であり，[1] より数列 $\{b_n\}$ は初項 $4$，公比 $4$ の等比数列であるから，
  $$b_n = 4 \cdot 4^{n-1} = 4^n$$
  よって，$\dfrac{a_n + 4}{a_n - 2} = 4^n$ である。両辺に $a_n - 2$ を掛けて $a_n$ について解くと，
  $$a_n + 4 = 4^n(a_n - 2)$$
  $$(4^n - 1)a_n = 2 \cdot 4^n + 4$$
  すべての自然数 $n$ について $4^n - 1 \neq 0$ であるから，
  $$a_n = \frac{2 \cdot 4^n + 4}{4^n - 1}$$
  > 💡 讲师批注：验算：$n=1 \Rightarrow \frac{12}{3} = 4$ ✓；$n=2 \Rightarrow \frac{36}{15} = \frac{12}{5}$（递推 $\frac{16+8}{4+6} = \frac{12}{5}$ ✓）。
- **【最终答案】**
  **[1] $b_{n+1} = 4b_n$**
  **[2] $a_n = \dfrac{2 \cdot 4^n + 4}{4^n - 1}$**

---

#### 演習問題 5-(4)（P279）
- **【原题重现与翻译】**
  - 原题：数列 $\{a_n\}$ の初項から第 $n$ 項までの和 $S_n$ が，一般項 $a_n$ を用いて $S_n = -2a_n - 2n + 5$ と表されるとき，一般項 $a_n$ を $n$ で表せ。
  - 中文：已知数列 $\{a_n\}$ 的前 $n$ 项和 $S_n$ 可用通项 $a_n$ 表示为 $S_n = -2a_n - 2n + 5$，求通项公式 $a_n$。
- **【考点定位】**
  - $S_n$ 与 $a_n$ 的关系（$S_1 = a_1$，$S_{n+1} - S_n = a_{n+1}$）结合 $a_{n+1} = pa_n + q$ 型递推式。
- **【分步标准解答】**
  与えられた式 $S_n = -2a_n - 2n + 5 \quad \cdots \text{①}$ において，$n = 1$ とおくと，$S_1 = a_1$ であるから，
  $$a_1 = -2a_1 - 2 \cdot 1 + 5 \implies 3a_1 = 3 \implies a_1 = 1$$
  また，① で $n$ を $n + 1$ に置き換えると，
  $$S_{n+1} = -2a_{n+1} - 2(n+1) + 5 \qquad \cdots \text{②}$$
  ② $-$ ① より，$S_{n+1} - S_n = a_{n+1}$ であるから，
  $$a_{n+1} = (-2a_{n+1} + 2a_n) - 2$$
  $$3a_{n+1} = 2a_n - 2 \implies a_{n+1} = \frac{2}{3}a_n - \frac{2}{3}$$
  > 💡 讲师批注：用 $S_{n+1} - S_n = a_{n+1}$ 对所有 $n \ge 1$ 直接成立，比用 $S_n - S_{n-1} = a_n \ (n \ge 2)$ 省去一次分类验证！

  特性方程式 $\alpha = \dfrac{2}{3}\alpha - \dfrac{2}{3}$ を解くと $\alpha = -2$ であるから，漸化式は次のように変形できる。
  $$a_{n+1} + 2 = \frac{2}{3}(a_n + 2)$$
  よって，数列 $\{a_n + 2\}$ は初項 $a_1 + 2 = 1 + 2 = 3$，公比 $\dfrac{2}{3}$ の等比数列である。
  $$a_n + 2 = 3 \left(\frac{2}{3}\right)^{n-1}$$
  したがって，
  $$a_n = 3 \left(\frac{2}{3}\right)^{n-1} - 2$$
  > 💡 讲师批注：验算：$n=1 \Rightarrow a_1=1, S_1=1$；$n=2 \Rightarrow a_2=0, S_2=1$（右端 $-2(0)-4+5=1$ ✓）；$n=3 \Rightarrow a_3=-\frac{2}{3}, S_3=\frac{1}{3}$（右端 $-2(-\frac{2}{3})-6+5=\frac{1}{3}$ ✓）。
- **【最终答案】**
  **$a_n = 3\left(\dfrac{2}{3}\right)^{n-1} - 2$**

---

### 演習問題 6（数学的帰納法）

<svg viewBox="0 0 640 100" xmlns="http://www.w3.org/2000/svg" style="max-width:640px;width:100%;height:auto;display:block;margin:10px auto;">
  <rect x="0" y="0" width="640" height="100" fill="#fafafa" rx="8" stroke="#e0e0e0"/>
  <text x="320" y="20" font-size="12" font-weight="bold" text-anchor="middle" fill="#1a237e">数学的帰納法の論理構造（ドミノ倒しモデル）</text>
  <!-- Step 1 -->
  <rect x="25" y="34" width="110" height="48" rx="6" fill="#e3f2fd" stroke="#1565c0" stroke-width="1.5"/>
  <text x="80" y="54" font-size="11" font-weight="bold" text-anchor="middle" fill="#0d47a1">[1] 起点の確認</text>
  <text x="80" y="71" font-size="11" text-anchor="middle" fill="#333">P(1) が真</text>
  <!-- Arrow -->
  <line x1="135" y1="58" x2="175" y2="58" stroke="#1565c0" stroke-width="1.8"/>
  <polygon points="175,54 183,58 175,62" fill="#1565c0"/>
  <!-- Chain -->
  <rect x="185" y="40" width="52" height="36" rx="5" fill="#fff" stroke="#78909c"/>
  <text x="211" y="62" font-size="11" text-anchor="middle" fill="#333">P(2)</text>
  <line x1="237" y1="58" x2="262" y2="58" stroke="#78909c" stroke-width="1.5"/>
  <polygon points="262,54 269,58 262,62" fill="#78909c"/>
  <text x="285" y="62" font-size="14" text-anchor="middle" fill="#555">…</text>
  <line x1="300" y1="58" x2="325" y2="58" stroke="#78909c" stroke-width="1.5"/>
  <polygon points="325,54 332,58 325,62" fill="#78909c"/>
  <!-- Step 2 -->
  <rect x="335" y="34" width="175" height="48" rx="6" fill="#fff3e0" stroke="#e65100" stroke-width="1.5"/>
  <text x="422" y="54" font-size="11" font-weight="bold" text-anchor="middle" fill="#bf360c">[2] 連鎖の証明</text>
  <text x="422" y="71" font-size="11" text-anchor="middle" fill="#333">P(k) 真 ⇒ P(k+1) 真</text>
  <!-- Final -->
  <line x1="510" y1="58" x2="532" y2="58" stroke="#2e7d32" stroke-width="1.8"/>
  <polygon points="532,54 540,58 532,62" fill="#2e7d32"/>
  <rect x="542" y="34" width="80" height="48" rx="6" fill="#e8f5e9" stroke="#2e7d32" stroke-width="1.5"/>
  <text x="582" y="54" font-size="10" font-weight="bold" text-anchor="middle" fill="#1b5e20">すべての n</text>
  <text x="582" y="71" font-size="10" text-anchor="middle" fill="#1b5e20">で P(n) 真</text>
</svg>

#### 演習問題 6-(1)（P281）
- **【原题重现与翻译】**
  - 原题：$n$ が自然数のとき，数学的帰納法を用いて次の等式を証明せよ。
    $1 \cdot 1! + 2 \cdot 2! + \cdots + n \cdot n! = (n + 1)! - 1$
  - 中文：当 $n$ 为自然数时，用数学归纳法证明下列等式：$1 \cdot 1! + 2 \cdot 2! + \cdots + n \cdot n! = (n + 1)! - 1$。
- **【考点定位】**
  - 数学归纳法证明含阶乘的等式。
- **【分步标准解答】**
  与えられた等式を (A) とする。

  **[1] $n = 1$ のとき**
  $$(\text{左辺}) = 1 \cdot 1! = 1, \qquad (\text{右辺}) = (1 + 1)! - 1 = 2! - 1 = 1$$
  よって，$n = 1$ のとき (A) は成り立つ。

  **[2] $n = k$ のとき (A) が成り立つと仮定する**
  すなわち，
  $$1 \cdot 1! + 2 \cdot 2! + \cdots + k \cdot k! = (k + 1)! - 1 \qquad \cdots \text{①}$$
  が成り立つと仮定する。
  $n = k + 1$ のときの (A) の左辺を計算すると，① を用いて
  $$\begin{aligned}
  (\text{左辺}) &= (1 \cdot 1! + 2 \cdot 2! + \cdots + k \cdot k!) + (k + 1) \cdot (k + 1)! \\
  &= \{(k + 1)! - 1\} + (k + 1) \cdot (k + 1)! \\
  &= \{1 + (k + 1)\}(k + 1)! - 1 \\
  &= (k + 2) \cdot (k + 1)! - 1 \\
  &= (k + 2)! - 1 = \{(k + 1) + 1\}! - 1
  \end{aligned}$$
  > 💡 讲师批注：关键变形是提取公因式 $(k+1)!$，并利用阶乘定义 $(k+2)\cdot(k+1)! = (k+2)!$。注意书写时**切勿把待证的 $n=k+1$ 等式直接拿来变形**，应从左端出发推导出右端！

  これは $n = k + 1$ のときの (A) の右辺に等しいから，$n = k + 1$ のときにも (A) は成り立つ。

  以上 [1], [2] より，すべての自然数 $n$ について (A) が成り立つ。（証明終）
- **【最终答案】**
  **証明完了（すべての自然数 $n$ について成り立つ）**

---

#### 演習問題 6-(2)（P281）
- **【原题重现与翻译】**
  - 原题：$a_1 = 1,\; a_{n+1} = \dfrac{a_n}{1 + (2n+1)a_n}$ によって定められる数列 $\{a_n\}$ について
    [1] $a_2, a_3, a_4$ を求めよ。
    [2] $a_n$ を $n$ で表す式を推測し，それを数学的帰納法で証明せよ。
  - 中文：对于由 $a_1 = 1,\; a_{n+1} = \dfrac{a_n}{1 + (2n+1)a_n}$ 确定的数列 $\{a_n\}$：
    [1] 求 $a_2, a_3, a_4$。
    [2] 推测用 $n$ 表示 $a_n$ 的表达式，并用数学归纳法加以证明。
- **【考点定位】**
  - 递推式求前几项 → 归纳猜想通项公式 → 数学归纳法证明（日本考场经典两问结构）。
- **【分步标准解答】**
  **[1]** 漸化式に $n = 1, 2, 3$ を順に代入すると，
  $$a_2 = \frac{a_1}{1 + 3a_1} = \frac{1}{1 + 3 \cdot 1} = \frac{1}{4}$$
  $$a_3 = \frac{a_2}{1 + 5a_2} = \frac{\dfrac{1}{4}}{1 + 5 \cdot \dfrac{1}{4}} = \frac{1}{4 + 5} = \frac{1}{9}$$
  $$a_4 = \frac{a_3}{1 + 7a_3} = \frac{\dfrac{1}{9}}{1 + 7 \cdot \dfrac{1}{9}} = \frac{1}{9 + 7} = \frac{1}{16}$$

  **[2]** $a_1 = \dfrac{1}{1^2},\; a_2 = \dfrac{1}{2^2},\; a_3 = \dfrac{1}{3^2},\; a_4 = \dfrac{1}{4^2}$ であるから，一般項は次のように推測される。
  $$a_n = \frac{1}{n^2} \qquad \cdots \text{①}$$
  これがすべての自然数 $n$ について成り立つことを数学的帰納法で証明する。

  **[i] $n = 1$ のとき**
  $a_1 = 1 = \dfrac{1}{1^2}$ であるから，① は成り立つ。

  **[ii] $n = k$ のとき ① が成り立つと仮定する**
  すなわち，$a_k = \dfrac{1}{k^2}$ と仮定すると，漸化式より
  $$a_{k+1} = \frac{a_k}{1 + (2k+1)a_k} = \frac{\dfrac{1}{k^2}}{1 + (2k+1)\cdot \dfrac{1}{k^2}} = \frac{1}{k^2 + 2k + 1} = \frac{1}{(k+1)^2}$$
  よって，$n = k + 1$ のときにも ① は成り立つ。

  以上 [i], [ii] より，すべての自然数 $n$ について $a_n = \dfrac{1}{n^2}$ が成り立つ。（証明終）
  > 💡 讲师批注：本题若不限制用归纳法，直接取倒数 $\frac{1}{a_{n+1}} - \frac{1}{a_n} = 2n+1$，立刻看出是奇数求和 $\sum (2k+1)$，从而 $\frac{1}{a_n} = n^2$！这也印证了猜测的 100% 准确性。
- **【最终答案】**
  **[1] $a_2 = \dfrac{1}{4},\quad a_3 = \dfrac{1}{9},\quad a_4 = \dfrac{1}{16}$**
  **[2] $a_n = \dfrac{1}{n^2}$（証明完了）**

---

#### 演習問題 6-(3)（P282）
- **【原题重现与翻译】**
  - 原题：数列 $\{a_n\}$（ただし $a_n > 0$）について，関係式 $(a_1 + a_2 + \cdots + a_n)^2 = a_1^3 + a_2^3 + \cdots + a_n^3$ が成り立つとき，$a_n = n$ であることを証明せよ。
  - 中文：已知正项数列 $\{a_n\}$（$a_n > 0$）满足关系式 $(a_1 + a_2 + \cdots + a_n)^2 = a_1^3 + a_2^3 + \cdots + a_n^3$，证明：$a_n = n$。
- **【考点定位】**
  - **强数学归纳法（$n \le k$ 仮定型）**——推证 $n = k+1$ 时需要用到 $a_1, a_2, \dots, a_k$ 的全部信息。
- **【分步标准解答】**
  すべての自然数 $n$ について $a_n = n \ \cdots \text{①}$ が成り立つことを数学的帰納法で証明する。

  **[1] $n = 1$ のとき**
  与えられた関係式に $n = 1$ を代入すると，
  $$a_1^2 = a_1^3 \implies a_1^2(a_1 - 1) = 0$$
  $a_1 > 0$ であるから，$a_1 = 1$。よって，$n = 1$ のとき ① は成り立つ。

  **[2] $n \le k$ のすべての自然数 $n$ について ① が成り立つと仮定する**
  すなわち，$a_1 = 1,\; a_2 = 2,\; \cdots,\; a_k = k$ と仮定する。
  > 💡 讲师批注：为什么这里必须用「$n \le k$ 均成立」的强归纳假设？因为关系式左边出现了 $a_1 + a_2 + \cdots + a_k$，仅假设 $a_k = k$ 无法算出前 $k$ 项之和！

  $n = k + 1$ のときの関係式は
  $$(a_1 + a_2 + \cdots + a_k + a_{k+1})^2 = a_1^3 + a_2^3 + \cdots + a_k^3 + a_{k+1}^3$$
  左辺を展開すると，
  $$(a_1 + \cdots + a_k)^2 + 2(a_1 + \cdots + a_k)a_{k+1} + a_{k+1}^2 = (a_1^3 + \cdots + a_k^3) + a_{k+1}^3$$
  ここで，$n = k$ のときの関係式より $(a_1 + \cdots + a_k)^2 = a_1^3 + \cdots + a_k^3$ であるから，両辺からこれを消去して，
  $$2(a_1 + a_2 + \cdots + a_k)a_{k+1} + a_{k+1}^2 = a_{k+1}^3$$
  帰納法の仮定より $a_1 + a_2 + \cdots + a_k = 1 + 2 + \cdots + k = \dfrac{k(k+1)}{2}$ であるから，これを代入すると，
  $$k(k + 1)a_{k+1} + a_{k+1}^2 = a_{k+1}^3$$
  $$a_{k+1}^3 - a_{k+1}^2 - k(k + 1)a_{k+1} = 0$$
  $a_{k+1} > 0$ より両辺を $a_{k+1}$ で割ると，
  $$a_{k+1}^2 - a_{k+1} - k(k + 1) = 0$$
  $$\{a_{k+1} - (k + 1)\}(a_{k+1} + k) = 0$$
  $a_{k+1} > 0$ および $k \ge 1$ より $a_{k+1} + k > 0$ であるから，
  $$a_{k+1} = k + 1$$
  よって，$n = k + 1$ のときにも ① は成り立つ。

  以上 [1], [2] より，すべての自然数 $n$ について $a_n = n$ が成り立つ。（証明終）
  > 💡 讲师批注：因式分解 $a_{k+1}^2 - a_{k+1} - k(k+1) = 0$ 时，把常数项看成 $-(k+1) \cdot k$，一次项系数为 $-1 = -(k+1) + k$，一步十字相乘即可。
- **【最终答案】**
  **証明完了（すべての自然数 $n$ について $a_n = n$ が成り立つ）**

---

### 第十一章 [1.3] 解説 例（はさみうちの原理）

#### [1.3] 解説 例（P284）
- **【原题重现与翻译】**
  - 原题：極限 $\lim_{n\to\infty} \dfrac{1}{n}\sin\dfrac{n\pi}{4}$ を求めよ。
  - 中文：求极限 $\lim_{n\to\infty} \dfrac{1}{n}\sin\dfrac{n\pi}{4}$。
- **【考点定位】**
  - 夹逼定理（はさみうちの原理）与三角函数有界性 $-1 \le \sin\theta \le 1$ 的联合应用。
- **【图解辅助（SVG 矢量图）】**

<svg viewBox="0 0 600 185" xmlns="http://www.w3.org/2000/svg" style="max-width:600px;width:100%;height:auto;display:block;margin:10px auto;">
  <rect x="0" y="0" width="600" height="185" fill="#fafafa" rx="8" stroke="#e0e0e0"/>
  <text x="300" y="20" font-size="13" font-weight="bold" text-anchor="middle" fill="#1a237e">はさみうちの原理：-1/n ≤ (1/n)sin(nπ/4) ≤ 1/n</text>
  <!-- Axes -->
  <line x1="40" y1="100" x2="555" y2="100" stroke="#333" stroke-width="1.5"/>
  <polygon points="555,96 565,100 555,104" fill="#333"/>
  <line x1="55" y1="170" x2="55" y2="35" stroke="#333" stroke-width="1.5"/>
  <polygon points="51,35 55,27 59,35" fill="#333"/>
  <text x="572" y="104" font-size="12" fill="#333">n</text>
  <text x="42" y="38" font-size="12" fill="#333">y</text>
  <text x="42" y="114" font-size="11" fill="#333">O</text>
  <!-- Upper envelope y = 1/n -->
  <path d="M 95 40 Q 175 78, 300 90 T 545 96" fill="none" stroke="#c62828" stroke-width="1.8" stroke-dasharray="5,3"/>
  <text x="210" y="58" font-size="11" font-weight="bold" fill="#c62828">y = 1/n → 0</text>
  <!-- Lower envelope y = -1/n -->
  <path d="M 95 160 Q 175 122, 300 110 T 545 104" fill="none" stroke="#1565c0" stroke-width="1.8" stroke-dasharray="5,3"/>
  <text x="210" y="152" font-size="11" font-weight="bold" fill="#1565c0">y = -1/n → 0</text>
  <!-- Sample points of (1/n)sin(n*pi/4) for n=1..12 -->
  <!-- n=1: 0.707 -> y=100-42=58; n=2: 0.5 -> y=70; n=3: 0.236 -> y=86; n=4: 0 -> y=100;
       n=5: -0.141 -> y=108.5; n=6: -0.167 -> y=110; n=7: -0.101 -> y=106; n=8: 0 -> y=100;
       n=9: 0.079 -> y=95; n=10: 0.1 -> y=94; n=11: 0.064 -> y=96; n=12: 0 -> y=100 -->
  <polyline points="95,58 135,70 175,86 215,100 255,108.5 295,110 335,106 375,100 415,95 455,94 495,96 535,100" fill="none" stroke="#2e7d32" stroke-width="1.4"/>
  <circle cx="95" cy="58" r="3.2" fill="#2e7d32"/>
  <circle cx="135" cy="70" r="3.2" fill="#2e7d32"/>
  <circle cx="175" cy="86" r="3.2" fill="#2e7d32"/>
  <circle cx="215" cy="100" r="3.2" fill="#2e7d32"/>
  <circle cx="255" cy="108.5" r="3.2" fill="#2e7d32"/>
  <circle cx="295" cy="110" r="3.2" fill="#2e7d32"/>
  <circle cx="335" cy="106" r="3.2" fill="#2e7d32"/>
  <circle cx="375" cy="100" r="3.2" fill="#2e7d32"/>
  <circle cx="415" cy="95" r="3.2" fill="#2e7d32"/>
  <circle cx="455" cy="94" r="3.2" fill="#2e7d32"/>
  <circle cx="495" cy="96" r="3.2" fill="#2e7d32"/>
  <circle cx="535" cy="100" r="3.2" fill="#2e7d32"/>
  <text x="455" y="78" font-size="11" font-weight="bold" fill="#2e7d32">cₙ = (1/n)sin(nπ/4)</text>
</svg>

- **【分步标准解答】**
  すべての自然数 $n$ について，$-1 \le \sin\dfrac{n\pi}{4} \le 1$ である。
  $n > 0$ より，各辺を $n$ で割ると，
  $$-\frac{1}{n} \le \frac{1}{n}\sin\frac{n\pi}{4} \le \frac{1}{n}$$
  > 💡 讲师批注：由于 $\sin\frac{n\pi}{4}$ 随 $n$ 周期振荡而没有极限，因此**绝对不能**拆成 $\left(\lim \frac{1}{n}\right)\left(\lim \sin\frac{n\pi}{4}\right)$ 来算！必须借助有界性与夹逼定理。

  ここで，$\lim_{n\to\infty} \left(-\dfrac{1}{n}\right) = 0$，$\lim_{n\to\infty} \dfrac{1}{n} = 0$ であるから，はさみうちの原理により，
  $$\lim_{n\to\infty} \frac{1}{n}\sin\frac{n\pi}{4} = 0$$
- **【最终答案】**
  **$0$**
