# 《EJU 教材全解与备课讲义》数学 030（P436–P450）

> **对应源文件**：`work_math/ocr_md/ocr_030_p436-450.md`（第七章《確率と統計推測》之「演習問題 4-(6)」「確率変数と確率分布、期待値、分散」「確率変数の変換、確率変数の和と積」「二項分布」「正規分布（基本事項与解説）」）
> **视觉核对参考图**：`work_math/ref_imgs/page_0436.jpg` – `page_0441.jpg`、`page_0443.jpg`、`page_0445.jpg` – `page_0450.jpg`

---

## 一、国内高中基础知识点唤醒与 EJU 考纲差异对比

本切片对应日本高中 **数学 B《確率分布と統計的な推測》** 的核心主干内容，涵盖四大板块：**离散型随机变量与期望/方差/标准差、随机变量的线性变换与独立性（和与积的期望方差）、二项分布、连续型随机变量与正态分布**。

### 1.1 概率变量与概率分布、期望值、方差、标准差（[5.1]–[5.3]）

- **离散型随机变量（離散型確率変数）**：取值 $x_1, x_2, \dots, x_n$ 及对应概率 $p_k = P(X = x_k)$ 满足：
  $$p_k \ge 0 \quad (k = 1, 2, \dots, n), \qquad \sum_{k=1}^{n} p_k = 1$$
- **期望值（期待値 / 平均値）**：
  $$E(X) = m = \sum_{k=1}^{n} x_k p_k = x_1 p_1 + x_2 p_2 + \cdots + x_n p_n$$
- **方差（分散）与标准差（標準偏差）**：
  $$V(X) = E\big((X - m)^2\big) = \sum_{k=1}^{n} (x_k - m)^2 p_k = E(X^2) - \{E(X)\}^2$$
  $$\sigma(X) = \sqrt{V(X)}$$
  > ⚠️ **教材勘误提示**：原教材第 436 页（`page_0437.jpg`）将节号 `[5.3] 分散と標準偏差` 误印为 `[5.2] 分散と標準偏差`（但在下一页 `page_0438.jpg` 的解説中正确标注为 `[5.2][5.3] 解説`）。此外，原教材多处将大写的随机变量记号 $E(X), V(X), \sigma(X)$ 混印为小写的 $E(x), V(x), \sigma(x)$，考场书写应严格统一用大写字母 $X$。

### 1.2 概率变量的变换、独立性与和积性质（[6.1]–[6.4]）

- **线性变换（確率変数の変換）**：对于常数 $a, b$ 与 $Y = aX + b$：
  $$E(aX + b) = aE(X) + b, \qquad V(aX + b) = a^2 V(X), \qquad \sigma(aX + b) = |a|\sigma(X)$$
  > 常数 $b$ 的平移只改变均值，不改变数据的离散程度（方差与标准差不受 $b$ 影响）。
- **事象的独立与从属（事象の独立と従属）**：
  - 当 $P(A) > 0, P(B) > 0$ 时，事件 $A$ 与 $B$ 互相独立 $\iff P_A(B) = P(B) \iff P_B(A) = P(A) \iff P(A \cap B) = P(A)P(B)$。
  - 若不独立，则称 $A$ 与 $B$ **从属（従属）**。
- **随机变量的独立性**：对任意取值 $a, b$ 恒有 $P(X = a,\; Y = b) = P(X = a)P(Y = b)$ 时，称 $X$ 与 $Y$ 互相独立。
- **期望的线性性质与乘积性质**：
  - **无需独立性**恒成立：$E(X + Y) = E(X) + E(Y)$，一般地 $E(aX + bY) = aE(X) + bE(Y)$。
  - **若 $X, Y$ 互相独立**：$E(XY) = E(X)E(Y)$。
- **方差的可加性（必须互相独立！）**：
  - **若 $X, Y$ 互相独立**：$V(X + Y) = V(X) + V(Y)$，一般地：
    $$V(aX + bY) = a^2 V(X) + b^2 V(Y)$$
  > ⚠️ **教材勘误提示**：原教材第 440 页（`page_0441.jpg`）核心公式框 `[6.4] 分散の性質` 末尾将公式误印为 `V(aX + bY) = aV(X) + bV(Y)`，**漏掉了 $a, b$ 的平方**！（而在第 443 页 `page_0444.jpg` 解説中推导为正确的 $a^2 V(X) + b^2 V(Y)$）。备课与授课时务必重点纠偏，这是学生最高频的丢分坑！

### 1.3 二项分布（[7.1]–[7.2]）

- 1 次试验中事件 $A$ 发生概率为 $p$（$0 < p < 1,\; q = 1 - p$），独立重复试验 $n$ 次中 $A$ 发生的次数 $X$ 服从**二项分布 $B(n, p)$**：
  $$P(X = r) = {}_n\mathrm{C}_r\, p^r q^{n-r} \qquad (r = 0, 1, \dots, n)$$
- 均值、方差、标准差（可由指示变量 $X = X_1 + \cdots + X_n$ 轻松推导）：
  $$E(X) = np, \qquad V(X) = npq, \qquad \sigma(X) = \sqrt{npq}$$

### 1.4 连续型随机变量与正态分布（[8.1]–[8.5]）

- **连续型随机变量（連続型確率変数）**与**概率密度函数（確率密度関数）** $f(x)$（$\alpha \le x \le \beta$）：
  1. 恒有 $f(x) \ge 0$；
  2. 区间概率等于面积：$P(a \le X \le b) = \displaystyle\int_a^b f(x)\,dx$；
  3. 总面积为 $1$：$\displaystyle\int_\alpha^\beta f(x)\,dx = 1$；
  4. 期望与方差：$E(X) = m = \displaystyle\int_\alpha^\beta x f(x)\,dx$，$V(X) = \displaystyle\int_\alpha^\beta (x - m)^2 f(x)\,dx$，$\sigma(X) = \sqrt{V(X)}$。
- **正态分布（正規分布） $N(m, \sigma^2)$**：
  $$f(x) = \frac{1}{\sqrt{2\pi}\,\sigma}\, e^{-\frac{(x-m)^2}{2\sigma^2}}, \qquad E(X) = m, \quad \sigma(X) = \sigma$$
  - 曲线关于直线 $x = m$ 对称，在 $x = m$ 处取最大值 $\dfrac{1}{\sqrt{2\pi}\,\sigma}$，$x$ 轴为渐近线；
  - $\sigma$ 越大，曲线越低平、越分散；$\sigma$ 越小，曲线越尖高、越集中于 $m$ 附近。
- **标准化（標準化）与标准正态分布 $N(0, 1)$**：
  $$X \sim N(m, \sigma^2) \implies Z = \frac{X - m}{\sigma} \sim N(0, 1), \qquad f(z) = \frac{1}{\sqrt{2\pi}}\, e^{-\frac{z^2}{2}}$$
  - 日本正态分布表查表记号：$p(u) = P(0 \le Z \le u)$（注意是**从 $0$ 到 $u$** 的半侧面积，而非从 $-\infty$ 到 $u$！）。
- **二项分布的正态近似**：当 $X \sim B(n, p)$ 且 $n$ 充分大时，$X$ 近似服从正态分布 $N(np,\; npq)$。

<svg viewBox="0 0 700 220" width="100%" xmlns="http://www.w3.org/2000/svg" style="background:#fafafa;border:1px solid #e0e0e0;border-radius:8px;margin:12px 0;">
  <!-- 左侧：σ 不同时的正态分布曲线对比 -->
  <text x="170" y="22" text-anchor="middle" font-size="13" font-weight="bold" fill="#2c3e50">正态分布曲线 N(m, σ²) 与 σ 的关系</text>
  <line x1="25" y1="185" x2="325" y2="185" stroke="#333" stroke-width="1.4"/>
  <polygon points="325,185 318,181 318,189" fill="#333"/>
  <text x="330" y="189" font-size="12" fill="#333">x</text>
  <!-- 对称轴 x=m -->
  <line x1="175" y1="38" x2="175" y2="185" stroke="#888" stroke-width="1" stroke-dasharray="4,3"/>
  <text x="175" y="203" text-anchor="middle" font-size="12" fill="#333">m</text>
  <!-- σ=1 尖高 -->
  <path d="M 65 184 C 115 184, 138 170, 152 115 C 161 78, 168 48, 175 48 C 182 48, 189 78, 198 115 C 212 170, 235 184, 285 184" fill="none" stroke="#e74c3c" stroke-width="2.2"/>
  <text x="206" y="64" font-size="11" fill="#e74c3c" font-weight="bold">σ 较小（尖高集中）</text>
  <!-- σ=2 中等 -->
  <path d="M 40 183 C 95 182, 125 150, 145 128 C 158 114, 167 108, 175 108 C 183 108, 192 114, 205 128 C 225 150, 255 182, 310 183" fill="none" stroke="#2980b9" stroke-width="2"/>
  <text x="235" y="128" font-size="11" fill="#2980b9">σ 适中</text>
  <!-- σ=3 低平 -->
  <path d="M 30 180 C 80 176, 120 156, 175 148 C 230 156, 270 176, 320 180" fill="none" stroke="#27ae60" stroke-width="2"/>
  <text x="248" y="164" font-size="11" fill="#27ae60">σ 较大（低平分散）</text>

  <!-- 分隔虚线 -->
  <line x1="355" y1="15" x2="355" y2="205" stroke="#ddd" stroke-width="1" stroke-dasharray="5,4"/>

  <!-- 右侧：标准正态分布 N(0,1) 与 p(u) -->
  <text x="530" y="22" text-anchor="middle" font-size="13" font-weight="bold" fill="#2c3e50">标准正态分布 N(0, 1) 与日本查表记号 p(u)</text>
  <line x1="380" y1="185" x2="675" y2="185" stroke="#333" stroke-width="1.4"/>
  <polygon points="675,185 668,181 668,189" fill="#333"/>
  <text x="680" y="189" font-size="12" fill="#333">z</text>
  <line x1="525" y1="40" x2="525" y2="185" stroke="#333" stroke-width="1.2"/>
  <polygon points="525,40 521,47 529,47" fill="#333"/>
  <text x="512" y="48" font-size="12" fill="#333">y</text>
  <text x="525" y="203" text-anchor="middle" font-size="12" fill="#333">0</text>
  <!-- 阴影区域 0 <= Z <= u -->
  <path d="M 525 185 L 525 65 C 538 65, 550 85, 565 118 C 572 134, 578 145, 583 153 L 583 185 Z" fill="#3498db" fill-opacity="0.32"/>
  <!-- 标准正态曲线 -->
  <path d="M 395 184 C 445 183, 470 165, 488 118 C 501 85, 512 65, 525 65 C 538 65, 549 85, 562 118 C 580 165, 605 183, 655 184" fill="none" stroke="#2c3e50" stroke-width="2.2"/>
  <!-- u 标记 -->
  <line x1="583" y1="153" x2="583" y2="185" stroke="#2980b9" stroke-width="1.5"/>
  <text x="583" y="203" text-anchor="middle" font-size="12" fill="#2980b9" font-weight="bold">u</text>
  <!-- 标注箭头 -->
  <text x="554" y="160" text-anchor="middle" font-size="12" fill="#1a5276" font-weight="bold">p(u)</text>
  <text x="615" y="90" text-anchor="middle" font-size="11.5" fill="#1a5276">p(u) = P(0 ≤ Z ≤ u)</text>
  <text x="615" y="106" text-anchor="middle" font-size="10.5" fill="#7f8c8d">（注意起点为 0，非 −∞）</text>
</svg>

### 1.5 国内高中 vs. 日本 EJU 考纲差异与符号习惯

| 对比维度 | 国内高中习惯 | 日本 EJU 习惯 | 备课/应试提醒 |
| :--- | :--- | :--- | :--- |
| **方差符号** | $D(X)$（Deviation/Dispersion） | **$V(X)$**（Variance） | 日本教材与考题一律用 $V(X)$，绝不用 $D(X)$ |
| **均值字母** | 常记为 $\mu$ 或 $E(X)$ | 多记为 **$m$** 或 $E(X)$ | 正态分布多写作 $N(m, \sigma^2)$ 而非 $N(\mu, \sigma^2)$ |
| **正态分布表** | 累积分布函数 $\Phi(u) = P(Z \le u)$ | **半侧面积 $p(u) = P(0 \le Z \le u)$** | **最高频坑点！** 查表时记住 $P(Z \le u) = 0.5 + p(u)$（$u \ge 0$） |
| **不独立术语** | 称「不独立」或「相关」 | 称 **従属（じゅうぞく）** | 题干常问「独立か従属かを調べよ」 |
| **EJU 考纲定位** | 高考必考概率分布与二项分布 | EJU 数学コース2 考纲传统上以数学 A 概率为主，但近年新课纲（数学 B《統計的な推測》必修化）趋势下需全面掌握 | 期望、方差、二项分布与正态标准化均为日本大学校内考高频考点 |

---

## 二、日文核心词汇与公式假名注音

### 2.1 本切片日文核心词汇

- 確率変数（かくりつへんすう / kakuritsu hensuu） — 随机变量（概率变量）
- 確率分布（かくりつぶんぷ / kakuritsu bunpu） — 概率分布（简称 分布 / ぶんぷ）
- 従う（したがう / shitagau） — 服从（如 二項分布に従う = 服从二项分布）
- 期待値（きたいち / kitaichi） — 数学期望（期望值）
- 平均値（へいきんち / heikinchi） — 平均值（均值，亦称 平均 / へいきん）
- 分散（ぶんさん / bunsan） — 方差
- 標準偏差（ひょうじゅんへんさ / hyoujun hensa） — 标准差
- 確率変数の変換（かくりつへんすうのへんかん / kakuritsu hensuu no henkan） — 随机变量的线性变换
- 互いに独立（たがいにどくりつ / tagai ni dokuritsu） — 相互独立（亦作 独立 / どくりつ）
- 従属（じゅうぞく / juuzoku） — 相关、从属（不独立）
- 同時分布（どうじぶんぷ / douji bunpu） — 联合分布（同时分布）
- 周辺分布（しゅうへんぶんぷ / shuuhen bunpu） — 边缘分布（周边分布）
- 二項分布（にこうぶんぷ / nikou bunpu） — 二项分布（$B(n, p)$）
- 離散型確率変数（りさんがたかくりつへんすう / risangata kakuritsu hensuu） — 离散型随机变量
- 連続型確率変数（れんぞくがたかくりつへんすう / renzokugata kakuritsu hensuu） — 连续型随机变量
- 確率密度関数（かくりつみつどかんすう / kakuritsu mitsudo kansuu） — 概率密度函数
- 分布曲線（ぶんぷきょくせん / bunpu kyokusen） — 分布曲线
- ヒストグラム（ひすとぐらむ / hisutoguramu） — 直方图（柱状图）
- 階級（かいきゅう / kaikyuu） — 组、组距区间（统计分组的阶级）
- 階級値（かいきゅうち / kaikyuuchi） — 组中值（阶级值）
- 相対度数（そうたいどすう / soutai dosuu） — 频率（相对频数）
- 正規分布（せいきぶんぷ / seiki bunpu） — 正态分布（$N(m, \sigma^2)$）
- 正規分布曲線（せいきぶんぷきょくせん / seiki bunpu kyokusen） — 正态分布曲线
- 標準正規分布（ひょうじゅんせいきぶんぷ / hyoujun seiki bunpu） — 标准正态分布（$N(0, 1)$）
- 標準化（ひょうじゅんか / hyoujunka） — 标准化（$Z = \dfrac{X-m}{\sigma}$）
- 正規分布表（せいきぶんぷひょう / seiki bunpuhyou） — 标准正态分布表
- 折れ線グラフ（おれせんぐらふ / oresen gurafu） — 折线图

### 2.2 核心公式的日本课堂口语读法

1. **方差计算公式** $V(X) = E(X^2) - \{E(X)\}^2$
   - 课堂读法：**ブイ・エックス イコール イー・エックスにじょう ひく かっこ イー・エックス かっことじ の にじょう**
   - 记忆口诀：**「2乗の平均 ひく 平均の2乗」**（にじょうのへいきん ひく へいきんのにじょう）。
2. **标准差定义** $\sigma(X) = \sqrt{V(X)}$
   - 课堂读法：**シグマ・エックス イコール ルート ブイ・エックス**
   - 备注：希腊字母 $\sigma$ 读作 **シグマ（shiguma）**。
3. **线性变换方差公式** $V(aX + b) = a^2 V(X)$
   - 课堂读法：**ブイ・エーエックス たす ビー イコール エーのにじょう ブイ・エックス**
4. **服从二项分布** $X$ は二項分布 $B(n, p)$ に従う
   - 课堂读法：**エックスは にこうぶんぷ ビー・エヌ・ピー に したがう**
5. **服从正态分布** $X$ は正規分布 $N(m, \sigma^2)$ に従う
   - 课堂读法：**エックスは せいきぶんぷ エヌ・エム・シグマにじょう に したがう**
6. **标准化公式** $Z = \dfrac{X - m}{\sigma}$
   - 课堂读法：**ゼット イコール シグマぶんの エックス ひく エム**

---

## 三、逐题深度解析（不可跳步）

---

### 演習問題 4（承接上一切片：確率の乗法定理・排反事象）

#### 演習問題 4-(6)（P436）
- **【原题重现与翻译】**
  - 原题：袋の中に、赤球 2 個と白球 3 個が入っている。$A, B$ がこの順に交互に 1 個ずつ球を取り出し、2 個目の赤球を取り出した方を勝ちとする。ただし、取り出した球はもとに戻さない。この時、$B$ が勝つ確率を求めよ。
  - 中文：袋中有红球 2 个、白球 3 个。$A, B$ 按此顺序轮流每次取出 1 个球，取到第 2 个红球的一方获胜。取出后不放回。求此时 $B$ 获胜的概率。
- **【考点定位】**
  - 非放回抽样的顺序概率（乗法定理与排反事象）；亦可转化为 5 个位置放置 2 个红球的等可能排列模型。
- **【图解辅助（SVG 矢量图）】**

<svg viewBox="0 0 640 165" width="100%" xmlns="http://www.w3.org/2000/svg" style="background:#fafafa;border:1px solid #e0e0e0;border-radius:8px;margin:10px 0;">
  <text x="320" y="22" text-anchor="middle" font-size="13" font-weight="bold" fill="#2c3e50">5次取球顺序与 B 获胜（第2个红球落在第2或第4位）的 4 种情形</text>
  <!-- 顶部列标题 -->
  <text x="155" y="45" text-anchor="middle" font-size="11.5" fill="#7f8c8d">第1次 (A)</text>
  <text x="245" y="45" text-anchor="middle" font-size="11.5" fill="#c0392b" font-weight="bold">第2次 (B)</text>
  <text x="335" y="45" text-anchor="middle" font-size="11.5" fill="#7f8c8d">第3次 (A)</text>
  <text x="425" y="45" text-anchor="middle" font-size="11.5" fill="#c0392b" font-weight="bold">第4次 (B)</text>
  <text x="515" y="45" text-anchor="middle" font-size="11.5" fill="#7f8c8d">第5次 (A)</text>

  <!-- 情形1：第2次 B 胜 -->
  <text x="20" y="74" font-size="11.5" fill="#2c3e50" font-weight="bold">[1] 第2次胜</text>
  <circle cx="155" cy="70" r="11" fill="#e74c3c"/><text x="155" y="74" text-anchor="middle" font-size="10" fill="#fff">赤</text>
  <circle cx="245" cy="70" r="11" fill="#e74c3c" stroke="#f1c40f" stroke-width="2.5"/><text x="245" y="74" text-anchor="middle" font-size="10" fill="#fff">赤</text>
  <text x="335" y="74" text-anchor="middle" font-size="11" fill="#95a5a6">（结束）</text>
  <text x="580" y="74" text-anchor="middle" font-size="11.5" fill="#2980b9">P = 1/10</text>

  <!-- 情形2：第4次 B 胜（3种） -->
  <text x="20" y="104" font-size="11.5" fill="#2c3e50" font-weight="bold">[2] 第4次胜</text>
  <!-- 2a: 赤白白赤 -->
  <circle cx="155" cy="100" r="10" fill="#e74c3c"/><text x="155" y="104" text-anchor="middle" font-size="9.5" fill="#fff">赤</text>
  <circle cx="245" cy="100" r="10" fill="#ecf0f1" stroke="#7f8c8d"/><text x="245" y="104" text-anchor="middle" font-size="9.5" fill="#333">白</text>
  <circle cx="335" cy="100" r="10" fill="#ecf0f1" stroke="#7f8c8d"/><text x="335" y="104" text-anchor="middle" font-size="9.5" fill="#333">白</text>
  <circle cx="425" cy="100" r="10" fill="#e74c3c" stroke="#f1c40f" stroke-width="2.5"/><text x="425" y="104" text-anchor="middle" font-size="9.5" fill="#fff">赤</text>
  <text x="515" y="104" text-anchor="middle" font-size="10" fill="#95a5a6">白</text>
  <text x="580" y="104" text-anchor="middle" font-size="11" fill="#2980b9">1/10</text>

  <!-- 2b: 白赤白赤 -->
  <circle cx="155" cy="126" r="10" fill="#ecf0f1" stroke="#7f8c8d"/><text x="155" y="130" text-anchor="middle" font-size="9.5" fill="#333">白</text>
  <circle cx="245" cy="126" r="10" fill="#e74c3c"/><text x="245" y="130" text-anchor="middle" font-size="9.5" fill="#fff">赤</text>
  <circle cx="335" cy="126" r="10" fill="#ecf0f1" stroke="#7f8c8d"/><text x="335" y="130" text-anchor="middle" font-size="9.5" fill="#333">白</text>
  <circle cx="425" cy="126" r="10" fill="#e74c3c" stroke="#f1c40f" stroke-width="2.5"/><text x="425" y="130" text-anchor="middle" font-size="9.5" fill="#fff">赤</text>
  <text x="515" y="130" text-anchor="middle" font-size="10" fill="#95a5a6">白</text>
  <text x="580" y="130" text-anchor="middle" font-size="11" fill="#2980b9">1/10</text>

  <!-- 2c: 白白赤赤 -->
  <circle cx="155" cy="152" r="10" fill="#ecf0f1" stroke="#7f8c8d"/><text x="155" y="156" text-anchor="middle" font-size="9.5" fill="#333">白</text>
  <circle cx="245" cy="152" r="10" fill="#ecf0f1" stroke="#7f8c8d"/><text x="245" y="156" text-anchor="middle" font-size="9.5" fill="#333">白</text>
  <circle cx="335" cy="152" r="10" fill="#e74c3c"/><text x="335" y="156" text-anchor="middle" font-size="9.5" fill="#fff">赤</text>
  <circle cx="425" cy="152" r="10" fill="#e74c3c" stroke="#f1c40f" stroke-width="2.5"/><text x="425" y="156" text-anchor="middle" font-size="9.5" fill="#fff">赤</text>
  <text x="515" y="156" text-anchor="middle" font-size="10" fill="#95a5a6">白</text>
  <text x="580" y="156" text-anchor="middle" font-size="11" fill="#2980b9">1/10</text>
</svg>

- **【分步标准解答】**
  $A, B$ が交互に球を取り出すので、$B$ が勝つのは、**2 回目**または **4 回目**に 2 個目の赤球を取り出す場合である。これら 2 つの事象は互いに排反である。
  > 💡 讲师批注：总共只有 5 个球，第 1, 3, 5 次由 $A$ 取，第 2, 4 次由 $B$ 取。因此 $B$ 获胜只可能发生在第 2 次或第 4 次。

  **[1] 2 回目に $B$ が勝つ場合（1 回目：赤、2 回目：赤）**
  $$P_1 = \frac{2}{5} \times \frac{1}{4} = \frac{1}{10}$$
  > 💡 讲师批注：取出不放回，第 1 次取红概率 $\frac{2}{5}$，剩 4 球（1 红 3 白），第 2 次取红概率 $\frac{1}{4}$。

  **[2] 4 回目に $B$ が勝つ場合（1〜3 回目に赤 1 個・白 2 個が出て、4 回目に赤が出る）**
  1〜3 回目の出方は（赤, 白, 白）、（白, 赤, 白）、（白, 白, 赤）の 3 通りあり、いずれの確率も等しく
  $$\frac{2}{5} \times \frac{3}{4} \times \frac{2}{3} \times \frac{1}{2} = \frac{1}{10}$$
  > 💡 讲师批注：不放回抽样中，只要红白球出现个数相同，分子都是 $2 \times 3 \times 2 \times 1$、分母都是 $5 \times 4 \times 3 \times 2$，因此 3 种顺序的概率完全相等。

  よって、4 回目に $B$ が勝つ確率は
  $$P_2 = 3 \times \frac{1}{10} = \frac{3}{10}$$

  以上 [1], [2] は互いに排反であるから、求める確率は
  $$P = P_1 + P_2 = \frac{1}{10} + \frac{3}{10} = \frac{4}{10} = \frac{2}{5}$$
  > 💡 讲师批注（别解・秒杀验算）：将 5 个球全部排成一列，2 个红球的位置共有 ${}_5\mathrm{C}_2 = 10$ 种等可能情况。$B$ 胜即第 2 个红球在第 2 位（1 种）或第 4 位（前 3 位任选 1 位放第 1 个红球，3 种），共 $1+3=4$ 种，故 $P = \frac{4}{10} = \frac{2}{5}$。同时 $A$ 胜为第 3 位（2 种）或第 5 位（4 种），共 $\frac{6}{10} = \frac{3}{5}$，两者之和为 $1$，验算无误。

- **【最终答案】**
  **$\dfrac{2}{5}$**

---

### 演習問題 5（確率分布・期待値・分散・標準偏差）

#### 演習問題 5-(1)（P438）
- **【原题重现与翻译】**
  - 原题：1 から 8 までの整数をそれぞれ 1 個ずつ記した 8 枚のカードから無作為に 4 枚取り出す。取り出された 4 枚のカードに記されている数のうち最小の数を $X$ とすると、$X$ は確率変数である。$X$ の確率分布を求めよ。また、$P(X \ge 3)$ を求めよ。
  - 中文：从分别写有 1 到 8 的整数的 8 张卡片中随机抽取 4 张。记抽出的 4 张卡片上数字的最小值为 $X$，则 $X$ 是一个随机变量。求 $X$ 的概率分布，并求 $P(X \ge 3)$。
- **【考点定位】**
  - 离散型随机变量取值范围确定、组合计数求概率分布、不等式事件概率 $P(X \ge a)$。
- **【图解辅助（SVG 矢量图）】**

<svg viewBox="0 0 600 185" width="100%" xmlns="http://www.w3.org/2000/svg" style="background:#fafafa;border:1px solid #e0e0e0;border-radius:8px;margin:10px 0;">
  <text x="300" y="22" text-anchor="middle" font-size="13" font-weight="bold" fill="#2c3e50">最小数 X 的概率分布柱状图（分母统一为 70）</text>
  <!-- 坐标轴 -->
  <line x1="60" y1="150" x2="540" y2="150" stroke="#333" stroke-width="1.4"/>
  <line x1="60" y1="38" x2="60" y2="150" stroke="#333" stroke-width="1.4"/>
  <text x="45" y="45" font-size="11" fill="#333">P</text>
  <text x="550" y="154" font-size="11" fill="#333">X</text>
  <!-- 柱子：高按 35 -> 105px (3px per 1/70) -->
  <!-- X=1: 35/70 -->
  <rect x="95" y="45" width="52" height="105" fill="#95a5a6" fill-opacity="0.6" stroke="#7f8c8d"/>
  <text x="121" y="40" text-anchor="middle" font-size="11" fill="#2c3e50">35/70</text>
  <text x="121" y="167" text-anchor="middle" font-size="12" fill="#333">1</text>
  <!-- X=2: 20/70 -->
  <rect x="185" y="90" width="52" height="60" fill="#95a5a6" fill-opacity="0.6" stroke="#7f8c8d"/>
  <text x="211" y="85" text-anchor="middle" font-size="11" fill="#2c3e50">20/70</text>
  <text x="211" y="167" text-anchor="middle" font-size="12" fill="#333">2</text>
  <!-- X=3: 10/70 (高亮 X>=3) -->
  <rect x="275" y="120" width="52" height="30" fill="#3498db" fill-opacity="0.7" stroke="#2980b9"/>
  <text x="301" y="115" text-anchor="middle" font-size="11" fill="#1a5276" font-weight="bold">10/70</text>
  <text x="301" y="167" text-anchor="middle" font-size="12" fill="#1a5276" font-weight="bold">3</text>
  <!-- X=4: 4/70 -->
  <rect x="365" y="138" width="52" height="12" fill="#3498db" fill-opacity="0.7" stroke="#2980b9"/>
  <text x="391" y="133" text-anchor="middle" font-size="11" fill="#1a5276" font-weight="bold">4/70</text>
  <text x="391" y="167" text-anchor="middle" font-size="12" fill="#1a5276" font-weight="bold">4</text>
  <!-- X=5: 1/70 -->
  <rect x="455" y="147" width="52" height="3" fill="#3498db" fill-opacity="0.7" stroke="#2980b9"/>
  <text x="481" y="141" text-anchor="middle" font-size="11" fill="#1a5276" font-weight="bold">1/70</text>
  <text x="481" y="167" text-anchor="middle" font-size="12" fill="#1a5276" font-weight="bold">5</text>
  <!-- 括号标注 P(X>=3) -->
  <path d="M 272 100 L 272 93 L 510 93 L 510 100" fill="none" stroke="#2980b9" stroke-width="1.3"/>
  <text x="391" y="86" text-anchor="middle" font-size="11.5" fill="#2980b9" font-weight="bold">P(X ≥ 3) = (10 + 4 + 1)/70 = 3/14</text>
</svg>

- **【分步标准解答】**
  8 枚のカードから 4 枚を取り出す総数は
  $${}_8\mathrm{C}_4 = \frac{8 \times 7 \times 6 \times 5}{4 \times 3 \times 2 \times 1} = 70\text{（通り）}$$
  取り出した 4 枚のカードのうち最小の数が $X$ であるから、残り 3 枚は $X$ より大きい数でなければならない。よって、$X$ のとりうる値は $1, 2, 3, 4, 5$ である。
  > 💡 讲师批注：因为必须还有 3 张比 $X$ 大的卡片，所以 $X$ 最大只能是 $8 - 3 = 5$（此时取出的 4 张为 $5, 6, 7, 8$）。

  $X = k$（$k = 1, 2, 3, 4, 5$）となるのは、数 $k$ のカード 1 枚と、$k+1$ から $8$ までの $(8 - k)$ 枚から 3 枚を取り出す場合であるから
  $$P(X = k) = \frac{{}_{8-k}\mathrm{C}_3}{{}_8\mathrm{C}_4} = \frac{{}_{8-k}\mathrm{C}_3}{70}$$
  各 $k$ について計算すると：
  - $P(X = 1) = \dfrac{{}_7\mathrm{C}_3}{70} = \dfrac{35}{70} = \dfrac{1}{2}$
  - $P(X = 2) = \dfrac{{}_6\mathrm{C}_3}{70} = \dfrac{20}{70} = \dfrac{2}{7}$
  - $P(X = 3) = \dfrac{{}_5\mathrm{C}_3}{70} = \dfrac{10}{70} = \dfrac{1}{7}$
  - $P(X = 4) = \dfrac{{}_4\mathrm{C}_3}{70} = \dfrac{4}{70} = \dfrac{2}{35}$
  - $P(X = 5) = \dfrac{{}_3\mathrm{C}_3}{70} = \dfrac{1}{70}$
  > 💡 讲师批注：验算总和 $\frac{35 + 20 + 10 + 4 + 1}{70} = \frac{70}{70} = 1$（其实这也是组合恒等式朱世杰恒等式 $\sum_{j=3}^7 {}_j\mathrm{C}_3 = {}_8\mathrm{C}_4$ 的直接体现！）。注意最终概率分布表中一般写成最简分数（也可保留分母 70 方便后续计算，如演習問題 5-(4)）。

  また、$P(X \ge 3)$ は
  $$P(X \ge 3) = P(X = 3) + P(X = 4) + P(X = 5) = \frac{10}{70} + \frac{4}{70} + \frac{1}{70} = \frac{15}{70} = \frac{3}{14}$$
  > 💡 讲师批注（验算）：$X \ge 3$ 等价于 4 张卡片全部从 $\{3, 4, 5, 6, 7, 8\}$ 这 6 张中选取，直接得 $P(X \ge 3) = \frac{{}_6\mathrm{C}_4}{{}_8\mathrm{C}_4} = \frac{15}{70} = \frac{3}{14}$，完全一致！

- **【最终答案】**
  **$X$ の確率分布は以下の表の通り：**

  | $X$ | $1$ | $2$ | $3$ | $4$ | $5$ | 計 |
  | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
  | $P$ | $\dfrac{1}{2}$ | $\dfrac{2}{7}$ | $\dfrac{1}{7}$ | $\dfrac{2}{35}$ | $\dfrac{1}{70}$ | $1$ |

  **$P(X \ge 3) = \dfrac{3}{14}$**

---

#### 演習問題 5-(2)（P439）
- **【原题重现与翻译】**
  - 原题：目の数が $2, 2, 4, 4, 5, 6$ である特製のサイコロが 1 個ある。このサイコロを繰り返し 2 回投げて、出た目の数の和を 5 で割った余りを $X$ とする。確率変数 $X$ の期待値 $E(X)$ を求めよ。
  - 中文：有一个点数分别为 $2, 2, 4, 4, 5, 6$ 的特制骰子。将此骰子重复掷 2 次，记两次点数之和除以 5 的余数为 $X$。求随机变量 $X$ 的期望值 $E(X)$。
- **【考点定位】**
  - 非标准骰子的样本空间统计（模 5 余数归类）、离散型随机变量的期望计算。
- **【图解辅助（SVG 矢量图）】**

<svg viewBox="0 0 600 205" width="100%" xmlns="http://www.w3.org/2000/svg" style="background:#fafafa;border:1px solid #e0e0e0;border-radius:8px;margin:10px 0;">
  <text x="300" y="22" text-anchor="middle" font-size="13" font-weight="bold" fill="#2c3e50">2次投掷点数和 mod 5 加权统计表（总计 6×6 = 36 种）</text>
  <!-- 表格左半：4×4 余数矩阵 -->
  <g transform="translate(30,38)" font-size="11.5">
    <!-- 表头背景 -->
    <rect x="0" y="0" width="90" height="30" fill="#ecf0f1" stroke="#bdc3c7"/>
    <rect x="90" y="0" width="60" height="30" fill="#d6eaf8" stroke="#bdc3c7"/>
    <rect x="150" y="0" width="60" height="30" fill="#d6eaf8" stroke="#bdc3c7"/>
    <rect x="210" y="0" width="60" height="30" fill="#d6eaf8" stroke="#bdc3c7"/>
    <rect x="270" y="0" width="60" height="30" fill="#d6eaf8" stroke="#bdc3c7"/>
    <text x="45" y="19" text-anchor="middle" font-weight="bold" fill="#2c3e50">1回目 \ 2回目</text>
    <text x="120" y="19" text-anchor="middle" font-weight="bold" fill="#1a5276">2 (×2)</text>
    <text x="180" y="19" text-anchor="middle" font-weight="bold" fill="#1a5276">4 (×2)</text>
    <text x="240" y="19" text-anchor="middle" font-weight="bold" fill="#1a5276">5 (×1)</text>
    <text x="300" y="19" text-anchor="middle" font-weight="bold" fill="#1a5276">6 (×1)</text>

    <!-- Row 1: 2 (×2) -->
    <rect x="0" y="30" width="90" height="30" fill="#d6eaf8" stroke="#bdc3c7"/>
    <text x="45" y="49" text-anchor="middle" font-weight="bold" fill="#1a5276">2 (×2)</text>
    <rect x="90" y="30" width="60" height="30" fill="#fff" stroke="#bdc3c7"/><text x="120" y="49" text-anchor="middle">余4 (4)</text>
    <rect x="150" y="30" width="60" height="30" fill="#fff" stroke="#bdc3c7"/><text x="180" y="49" text-anchor="middle">余1 (4)</text>
    <rect x="210" y="30" width="60" height="30" fill="#fff" stroke="#bdc3c7"/><text x="240" y="49" text-anchor="middle">余2 (2)</text>
    <rect x="270" y="30" width="60" height="30" fill="#fff" stroke="#bdc3c7"/><text x="300" y="49" text-anchor="middle">余3 (2)</text>

    <!-- Row 2: 4 (×2) -->
    <rect x="0" y="60" width="90" height="30" fill="#d6eaf8" stroke="#bdc3c7"/>
    <text x="45" y="79" text-anchor="middle" font-weight="bold" fill="#1a5276">4 (×2)</text>
    <rect x="90" y="60" width="60" height="30" fill="#fff" stroke="#bdc3c7"/><text x="120" y="79" text-anchor="middle">余1 (4)</text>
    <rect x="150" y="60" width="60" height="30" fill="#fff" stroke="#bdc3c7"/><text x="180" y="79" text-anchor="middle">余3 (4)</text>
    <rect x="210" y="60" width="60" height="30" fill="#fff" stroke="#bdc3c7"/><text x="240" y="79" text-anchor="middle">余4 (2)</text>
    <rect x="270" y="60" width="60" height="30" fill="#fff" stroke="#bdc3c7"/><text x="300" y="79" text-anchor="middle">余0 (2)</text>

    <!-- Row 3: 5 (×1) -->
    <rect x="0" y="90" width="90" height="30" fill="#d6eaf8" stroke="#bdc3c7"/>
    <text x="45" y="109" text-anchor="middle" font-weight="bold" fill="#1a5276">5 (×1)</text>
    <rect x="90" y="90" width="60" height="30" fill="#fff" stroke="#bdc3c7"/><text x="120" y="109" text-anchor="middle">余2 (2)</text>
    <rect x="150" y="90" width="60" height="30" fill="#fff" stroke="#bdc3c7"/><text x="180" y="109" text-anchor="middle">余4 (2)</text>
    <rect x="210" y="90" width="60" height="30" fill="#fff" stroke="#bdc3c7"/><text x="240" y="109" text-anchor="middle">余0 (1)</text>
    <rect x="270" y="90" width="60" height="30" fill="#fff" stroke="#bdc3c7"/><text x="300" y="109" text-anchor="middle">余1 (1)</text>

    <!-- Row 4: 6 (×1) -->
    <rect x="0" y="120" width="90" height="30" fill="#d6eaf8" stroke="#bdc3c7"/>
    <text x="45" y="139" text-anchor="middle" font-weight="bold" fill="#1a5276">6 (×1)</text>
    <rect x="90" y="120" width="60" height="30" fill="#fff" stroke="#bdc3c7"/><text x="120" y="139" text-anchor="middle">余3 (2)</text>
    <rect x="150" y="120" width="60" height="30" fill="#fff" stroke="#bdc3c7"/><text x="180" y="139" text-anchor="middle">余0 (2)</text>
    <rect x="210" y="120" width="60" height="30" fill="#fff" stroke="#bdc3c7"/><text x="240" y="139" text-anchor="middle">余1 (1)</text>
    <rect x="270" y="120" width="60" height="30" fill="#fff" stroke="#bdc3c7"/><text x="300" y="139" text-anchor="middle">余2 (1)</text>
  </g>

  <!-- 右侧汇总框 -->
  <g transform="translate(385,48)" font-size="11.5">
    <rect x="0" y="0" width="185" height="135" rx="6" fill="#fef9e7" stroke="#f39c12"/>
    <text x="92" y="22" text-anchor="middle" font-weight="bold" fill="#b7791f">各余数频数汇总（/36）</text>
    <text x="18" y="44" fill="#2c3e50">X = 0：2 + 1 + 2 = 5</text>
    <text x="18" y="64" fill="#2c3e50">X = 1：4 + 4 + 1 + 1 = 10</text>
    <text x="18" y="84" fill="#2c3e50">X = 2：2 + 2 + 1 = 5</text>
    <text x="18" y="104" fill="#2c3e50">X = 3：2 + 4 + 2 = 8</text>
    <text x="18" y="124" fill="#2c3e50">X = 4：4 + 2 + 2 = 8</text>
  </g>
</svg>

- **【分步标准解答】**
  サイコロの 6 つの面をすべて区別して考えると、2 回投げたときの目の出方は $6 \times 6 = 36$ 通りであり、これらは同様に確からしい。
  > 💡 讲师批注：即使点数有重复（两个 2、两个 4），也必须把骰子的 6 个面视作**等可能的基本事件**（即点数 2 和 4 各占 2 份权重，5 和 6 各占 1 份权重）。

  出た目の和と、それを 5 で割った余り $X$ の対応を調べる：
  - $X = 0$（和が 10）：$(4, 6)$ が $2 \times 1 = 2$ 通り、$(6, 4)$ が $1 \times 2 = 2$ 通り、$(5, 5)$ が $1 \times 1 = 1$ 通り $\implies$ 計 $5$ 通り
  - $X = 1$（和が 6 または 11）：$(2, 4)$ が $2 \times 2 = 4$ 通り、$(4, 2)$ が $2 \times 2 = 4$ 通り、$(5, 6)$ が $1$ 通り、$(6, 5)$ が $1$ 通り $\implies$ 計 $10$ 通り
  - $X = 2$（和が 7 または 12）：$(2, 5)$ が $2$ 通り、$(5, 2)$ が $2$ 通り、$(6, 6)$ が $1$ 通り $\implies$ 計 $5$ 通り
  - $X = 3$（和が 8）：$(2, 6)$ が $2$ 通り、$(6, 2)$ が $2$ 通り、$(4, 4)$ が $2 \times 2 = 4$ 通り $\implies$ 計 $8$ 通り
  - $X = 4$（和が 4 または 9）：$(2, 2)$ が $2 \times 2 = 4$ 通り、$(4, 5)$ が $2$ 通り、$(5, 4)$ が $2$ 通り $\implies$ 計 $8$ 通り
  > 💡 讲师批注：务必先验算总频数 $5 + 10 + 5 + 8 + 8 = 36$，确保不重不漏！

  よって、$X$ の確率分布は次の表のようになる。

  | $X$ | $0$ | $1$ | $2$ | $3$ | $4$ | 計 |
  | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
  | $P$ | $\dfrac{5}{36}$ | $\dfrac{10}{36}$ | $\dfrac{5}{36}$ | $\dfrac{8}{36}$ | $\dfrac{8}{36}$ | $1$ |

  したがって、期待値 $E(X)$ は
  $$E(X) = 0 \cdot \frac{5}{36} + 1 \cdot \frac{10}{36} + 2 \cdot \frac{5}{36} + 3 \cdot \frac{8}{36} + 4 \cdot \frac{8}{36}$$
  $$= \frac{0 + 10 + 10 + 24 + 32}{36} = \frac{76}{36} = \frac{19}{9}$$
  > 💡 讲师批注：保持同分母 36 直接把分子相加再约分，比先约分再通分快得多且不易算错。

- **【最终答案】**
  **$E(X) = \dfrac{19}{9}$**

---

#### 演習問題 5-(3)（P439）
- **【原题重现与翻译】**
  - 原题：$A$ のゲームは 5 枚の 100 円硬貨を同時に投げた時、表の出た硬貨をもらえる。$B$ ゲームは 1 つのサイコロを投げて、3 以上の目が出るとその目の枚数だけの 100 円硬貨をもらえ、2 以下の目が出るとその目の枚数だけの 100 円硬貨を支払う。$A, B$ どちらのゲームに参加する方が有利か。
  - 中文：$A$ 游戏是同时抛 5 枚 100 日元硬币，正面朝上的硬币归玩家所有。$B$ 游戏是掷 1 个骰子，若掷出 3 点及以上则获得与点数相同枚数的 100 日元硬币；若掷出 2 点及以下则需支付与点数相同枚数的 100 日元硬币。参加 $A, B$ 哪个游戏更有利？
- **【考点定位】**
  - 数学期望的实际决策应用（比较收益期望值；注意支出记为负值）。
- **【分步标准解答】**
  **[1] $A$ のゲームで得られる金額 $X$（円）の期待値**
  表の出る硬貨の枚数を $K$ とすると、$K$ のとりうる値は $0, 1, 2, 3, 4, 5$ であり、各確率は反復試行の確率より $P(K = k) = {}_5\mathrm{C}_k \left(\dfrac{1}{2}\right)^5$ である。
  $$E(K) = 0 \cdot \frac{1}{32} + 1 \cdot \frac{5}{32} + 2 \cdot \frac{10}{32} + 3 \cdot \frac{10}{32} + 4 \cdot \frac{5}{32} + 5 \cdot \frac{1}{32} = \frac{80}{32} = \frac{5}{2}$$
  > 💡 讲师批注：学完二项分布后可直接秒杀：$K \sim B\left(5, \frac{1}{2}\right) \implies E(K) = 5 \times \frac{1}{2} = \frac{5}{2}$。

  よって、$A$ のゲームで得られる金額の期待値は
  $$E(X) = 100 \times \frac{5}{2} = 250\text{（円）}$$

  **[2] $B$ のゲームで得られる金額 $Y$（円）の期待値**
  支払う金額を負の値で表すと、出た目に対する $Y$ の値は次の表のようになる。

  | 出た目 | $1$ | $2$ | $3$ | $4$ | $5$ | $6$ | 計 |
  | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
  | $Y$（円） | $-100$ | $-200$ | $300$ | $400$ | $500$ | $600$ | — |
  | $P$ | $\dfrac{1}{6}$ | $\dfrac{1}{6}$ | $\dfrac{1}{6}$ | $\dfrac{1}{6}$ | $\dfrac{1}{6}$ | $\dfrac{1}{6}$ | $1$ |

  > 💡 讲师批注：易错点在于把「支払う（支付）」误记成 $0$ 或正数！支付 1 枚和 2 枚 100 日元硬币分别记为 $-100$ 和 $-200$。

  よって、$B$ のゲームで得られる金額の期待値は
  $$E(Y) = \frac{-100 - 200 + 300 + 400 + 500 + 600}{6} = \frac{1500}{6} = 250\text{（円）}$$

  $E(X) = E(Y) = 250$ 円であるから、$A, B$ どちらも有利さは同じである。
  > 💡 讲师批注：期望值相等时，千万不要强行选 A 或 B，直接回答「どちらも同じ（どちらとも言えない）」即可。

- **【最终答案】**
  **期待値はいずれも $250$ 円で等しいため、$A, B$ どちらも同じ（どちらが有利とも言えない）。**

---

#### 演習問題 5-(4)（P440）
- **【原题重现与翻译】**
  - 原题：$X$ の確率分布が右の表のようになる時、期待値 $E(X)$、分散 $V(X)$、標準偏差 $\sigma(X)$ を求めよ。

    | $X$ | $1$ | $2$ | $3$ | $4$ | $5$ | 計 |
    | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
    | $P$ | $\dfrac{35}{70}$ | $\dfrac{20}{70}$ | $\dfrac{10}{70}$ | $\dfrac{4}{70}$ | $\dfrac{1}{70}$ | $1$ |

  - 中文：当 $X$ 的概率分布如上表所示时，求期望值 $E(X)$、方差 $V(X)$ 与标准差 $\sigma(X)$。
- **【考点定位】**
  - 利用 $V(X) = E(X^2) - \{E(X)\}^2$ 高效计算方差与标准差。（本题分布表即 演習問題 5-(1) 的结果。）
- **【分步标准解答】**
  **[1] 期待値 $E(X)$**
  $$E(X) = 1 \cdot \frac{35}{70} + 2 \cdot \frac{20}{70} + 3 \cdot \frac{10}{70} + 4 \cdot \frac{4}{70} + 5 \cdot \frac{1}{70}$$
  $$= \frac{35 + 40 + 30 + 16 + 5}{70} = \frac{126}{70} = \frac{9}{5}$$
  > 💡 讲师批注：$126$ 与 $70$ 都能被 $14$ 整除（$126 = 14 \times 9,\; 70 = 14 \times 5$），化简为 $\frac{9}{5}$。

  **[2] $X^2$ の期待値 $E(X^2)$ と分散 $V(X)$**
  $$E(X^2) = 1^2 \cdot \frac{35}{70} + 2^2 \cdot \frac{20}{70} + 3^2 \cdot \frac{10}{70} + 4^2 \cdot \frac{4}{70} + 5^2 \cdot \frac{1}{70}$$
  $$= \frac{35 + 80 + 90 + 64 + 25}{70} = \frac{294}{70} = \frac{21}{5}$$
  > 💡 讲师批注：当均值 $E(X)$ 是分数时，用定义 $\sum (x_k - m)^2 p_k$ 会产生大量分数平方运算，极易出错；优先使用公式 $V(X) = E(X^2) - \{E(X)\}^2$！注意 $294 = 14 \times 21$。

  よって、分散 $V(X)$ は
  $$V(X) = E(X^2) - \{E(X)\}^2 = \frac{21}{5} - \left(\frac{9}{5}\right)^2 = \frac{105 - 81}{25} = \frac{24}{25}$$

  **[3] 標準偏差 $\sigma(X)$**
  $$\sigma(X) = \sqrt{V(X)} = \sqrt{\frac{24}{25}} = \frac{2\sqrt{6}}{5}$$
  > 💡 讲师批注：$\sqrt{24} = 2\sqrt{6}$，不要忘记化简根式。

- **【最终答案】**
  **$E(X) = \dfrac{9}{5},\qquad V(X) = \dfrac{24}{25},\qquad \sigma(X) = \dfrac{2\sqrt{6}}{5}$**

---

#### 演習問題 5-(5)（P440，经 `page_0440.jpg` 视觉核对完整补全）
- **【原题重现与翻译】**
  - 原题：袋の中に 1 と書いてあるカードが 3 枚、2 と書いてあるカードが 1 枚、3 と書いてあるカードが 1 枚、合計 5 枚のカードが入っている。この袋から 1 枚カードを取り出し、それを戻さずにもう 1 枚カードを取り、これら 2 枚のカードに書かれている数字の平均を $X$ とする。$X$ の期待値 $E(X)$、分散 $V(X)$、標準偏差 $\sigma(X)$ を求めよ。
  - 中文：袋中有写着 1 的卡片 3 张、写着 2 的卡片 1 张、写着 3 的卡片 1 张，共 5 张卡片。从袋中取出 1 张卡片，不放回再取出 1 张卡片，记这 2 张卡片上数字的平均值为 $X$。求 $X$ 的期望值 $E(X)$、方差 $V(X)$ 与标准差 $\sigma(X)$。
- **【考点定位】**
  - 非放回抽样（等价于同时抽 2 张）的样本均值分布及其期望、方差、标准差。
- **【分步标准解答】**
  1 枚取り出して戻さずにもう 1 枚取り出す試行において、2 枚の数字の平均は順序によらないため、5 枚のカードから同時に 2 枚を取り出すと考えてよい。取り出し方の総数は ${}_5\mathrm{C}_2 = 10$ 通りである。
  > 💡 讲师批注：题目关注的是两张卡片的平均值，与先后顺序无关，因此按组合 ${}_5\mathrm{C}_2 = 10$ 计算比按排列 $5 \times 4 = 20$ 更简洁，概率完全一致。

  取り出した 2 枚の数字の組と平均 $X$、およびその確率は次の通り：
  - $\{1, 1\}$ のとき $X = \dfrac{1+1}{2} = 1$：${}_3\mathrm{C}_2 = 3$ 通り $\implies P(X = 1) = \dfrac{3}{10}$
  - $\{1, 2\}$ のとき $X = \dfrac{1+2}{2} = \dfrac{3}{2}$：$3 \times 1 = 3$ 通り $\implies P\!\left(X = \dfrac{3}{2}\right) = \dfrac{3}{10}$
  - $\{1, 3\}$ のとき $X = \dfrac{1+3}{2} = 2$：$3 \times 1 = 3$ 通り $\implies P(X = 2) = \dfrac{3}{10}$
  - $\{2, 3\}$ のとき $X = \dfrac{2+3}{2} = \dfrac{5}{2}$：$1 \times 1 = 1$ 通り $\implies P\!\left(X = \dfrac{5}{2}\right) = \dfrac{1}{10}$

  よって、$X$ の確率分布は次の表のようになる。

  | $X$ | $1$ | $\dfrac{3}{2}$ | $2$ | $\dfrac{5}{2}$ | 計 |
  | :---: | :---: | :---: | :---: | :---: | :---: |
  | $P$ | $\dfrac{3}{10}$ | $\dfrac{3}{10}$ | $\dfrac{3}{10}$ | $\dfrac{1}{10}$ | $1$ |

  **[1] 期待値 $E(X)$**
  $$E(X) = 1 \cdot \frac{3}{10} + \frac{3}{2} \cdot \frac{3}{10} + 2 \cdot \frac{3}{10} + \frac{5}{2} \cdot \frac{1}{10} = \frac{6 + 9 + 12 + 5}{20} = \frac{32}{20} = \frac{8}{5}$$
  > 💡 讲师批注（验算）：袋中 5 张卡的总体均值为 $\frac{1+1+1+2+3}{5} = \frac{8}{5}$。无论放回与否，随机抽取 2 张卡的样本均值之期望必等于总体均值 $\frac{8}{5}$，瞬间验证无误！

  **[2] $X^2$ の期待値 $E(X^2)$ と分散 $V(X)$**
  $$E(X^2) = 1^2 \cdot \frac{3}{10} + \left(\frac{3}{2}\right)^2 \cdot \frac{3}{10} + 2^2 \cdot \frac{3}{10} + \left(\frac{5}{2}\right)^2 \cdot \frac{1}{10}$$
  $$= \frac{12 + 27 + 48 + 25}{40} = \frac{112}{40} = \frac{14}{5}$$
  $$V(X) = E(X^2) - \{E(X)\}^2 = \frac{14}{5} - \left(\frac{8}{5}\right)^2 = \frac{70 - 64}{25} = \frac{6}{25}$$

  **[3] 標準偏差 $\sigma(X)$**
  $$\sigma(X) = \sqrt{V(X)} = \sqrt{\frac{6}{25}} = \frac{\sqrt{6}}{5}$$

- **【最终答案】**
  **$E(X) = \dfrac{8}{5},\qquad V(X) = \dfrac{6}{25},\qquad \sigma(X) = \dfrac{\sqrt{6}}{5}$**

---

### 演習問題 6（確率変数の変換・独立と従属・和と積・二項分布）

#### 演習問題 6-(1)（P445）
- **【原题重现与翻译】**
  - 原题：袋の中に赤球が 4 個、白球が 6 個入っている。この袋の中から同時に 4 個の球を取り出すとき、赤球の個数を $X$ とする。確率変数 $2X + 3$ の期待値 $E(2X + 3)$ と分散 $V(2X + 3)$、標準偏差 $\sigma(2X + 3)$ を求めよ。
  - 中文：袋中有红球 4 个、白球 6 个。从袋中同时取出 4 个球，记红球个数为 $X$。求随机变量 $2X + 3$ 的期望值 $E(2X + 3)$、方差 $V(2X + 3)$ 与标准差 $\sigma(2X + 3)$。
- **【考点定位】**
  - 超几何分布的概率计算 + 随机变量线性变换公式 $E(aX+b) = aE(X)+b,\; V(aX+b) = a^2V(X),\; \sigma(aX+b) = |a|\sigma(X)$。
- **【图解辅助（SVG 矢量图）】**

<svg viewBox="0 0 600 135" width="100%" xmlns="http://www.w3.org/2000/svg" style="background:#fafafa;border:1px solid #e0e0e0;border-radius:8px;margin:10px 0;">
  <text x="300" y="20" text-anchor="middle" font-size="13" font-weight="bold" fill="#2c3e50">线性变换 Y = 2X + 3 对均值与标准差的几何影响</text>
  <!-- 原分布 X -->
  <text x="45" y="55" font-size="12" font-weight="bold" fill="#2c3e50">原変数 X</text>
  <line x1="110" y1="52" x2="550" y2="52" stroke="#95a5a6" stroke-width="1.5"/>
  <circle cx="200" cy="52" r="5" fill="#2980b9"/>
  <text x="200" y="41" text-anchor="middle" font-size="11" fill="#2980b9" font-weight="bold">E(X) = 8/5</text>
  <!-- 离散宽度 σ(X) = 4/5 -->
  <line x1="168" y1="64" x2="232" y2="64" stroke="#2980b9" stroke-width="2"/>
  <line x1="168" y1="59" x2="168" y2="69" stroke="#2980b9" stroke-width="1.5"/>
  <line x1="232" y1="59" x2="232" y2="69" stroke="#2980b9" stroke-width="1.5"/>
  <text x="200" y="79" text-anchor="middle" font-size="10.5" fill="#2980b9">±σ(X) = ±4/5</text>

  <!-- 箭头：×2 + 3 -->
  <path d="M 290 66 Q 330 82 365 95" fill="none" stroke="#e67e22" stroke-width="1.8" stroke-dasharray="4,2"/>
  <text x="355" y="76" font-size="11" fill="#d35400" font-weight="bold">×2（宽度翻倍）+ 3（整体右移）</text>

  <!-- 变换后分布 Y=2X+3 -->
  <text x="30" y="106" font-size="12" font-weight="bold" fill="#c0392b">Y = 2X + 3</text>
  <line x1="110" y1="103" x2="550" y2="103" stroke="#95a5a6" stroke-width="1.5"/>
  <circle cx="410" cy="103" r="5" fill="#c0392b"/>
  <text x="410" y="92" text-anchor="middle" font-size="11" fill="#c0392b" font-weight="bold">E(Y) = 31/5</text>
  <!-- 离散宽度 σ(Y) = 8/5 (翻倍) -->
  <line x1="346" y1="115" x2="474" y2="115" stroke="#c0392b" stroke-width="2"/>
  <line x1="346" y1="110" x2="346" y2="120" stroke="#c0392b" stroke-width="1.5"/>
  <line x1="474" y1="110" x2="474" y2="120" stroke="#c0392b" stroke-width="1.5"/>
  <text x="410" y="129" text-anchor="middle" font-size="10.5" fill="#c0392b">±σ(Y) = ±2σ(X) = ±8/5（方差放大 2² = 4 倍）</text>
</svg>

- **【分步标准解答】**
  10 個の球から 4 個を取り出す総数は ${}_{10}\mathrm{C}_4 = \dfrac{10 \times 9 \times 8 \times 7}{4 \times 3 \times 2 \times 1} = 210$ 通りである。
  $X$ のとりうる値は $0, 1, 2, 3, 4$ であり、各確率は
  - $P(X = 0) = \dfrac{{}_4\mathrm{C}_0 \cdot {}_6\mathrm{C}_4}{210} = \dfrac{15}{210}$
  - $P(X = 1) = \dfrac{{}_4\mathrm{C}_1 \cdot {}_6\mathrm{C}_3}{210} = \dfrac{80}{210}$
  - $P(X = 2) = \dfrac{{}_4\mathrm{C}_2 \cdot {}_6\mathrm{C}_2}{210} = \dfrac{90}{210}$
  - $P(X = 3) = \dfrac{{}_4\mathrm{C}_3 \cdot {}_6\mathrm{C}_1}{210} = \dfrac{24}{210}$
  - $P(X = 4) = \dfrac{{}_4\mathrm{C}_4 \cdot {}_6\mathrm{C}_0}{210} = \dfrac{1}{210}$
  > 💡 讲师批注：验算分子和 $15 + 80 + 90 + 24 + 1 = 210$，准确无误。

  これより $X$ の期待値・分散・標準偏差を求める：
  $$E(X) = \frac{0 \cdot 15 + 1 \cdot 80 + 2 \cdot 90 + 3 \cdot 24 + 4 \cdot 1}{210} = \frac{336}{210} = \frac{8}{5}$$
  $$E(X^2) = \frac{0^2 \cdot 15 + 1^2 \cdot 80 + 2^2 \cdot 90 + 3^2 \cdot 24 + 4^2 \cdot 1}{210} = \frac{80 + 360 + 216 + 16}{210} = \frac{672}{210} = \frac{16}{5}$$
  $$V(X) = E(X^2) - \{E(X)\}^2 = \frac{16}{5} - \left(\frac{8}{5}\right)^2 = \frac{80 - 64}{25} = \frac{16}{25}$$
  $$\sigma(X) = \sqrt{\frac{16}{25}} = \frac{4}{5}$$
  > 💡 讲师批注（超几何分布验算）：$E(X) = 4 \cdot \frac{4}{10} = \frac{8}{5}$；$V(X) = 4 \cdot \frac{4}{10} \cdot \frac{6}{10} \cdot \frac{10 - 4}{10 - 1} = \frac{24}{25} \cdot \frac{2}{3} = \frac{16}{25}$，100% 吻合！

  したがって、確率変数の変換公式より
  $$E(2X + 3) = 2E(X) + 3 = 2 \cdot \frac{8}{5} + 3 = \frac{31}{5}$$
  $$V(2X + 3) = 2^2 V(X) = 4 \cdot \frac{16}{25} = \frac{64}{25}$$
  $$\sigma(2X + 3) = |2|\sigma(X) = 2 \cdot \frac{4}{5} = \frac{8}{5}$$
  > 💡 讲师批注：千万不要去重新算 $2X+3$ 的概率分布表！直接用转换公式不仅省时，而且完全避免计算失误。注意 $+3$ 对方差和标准差无影响。

- **【最终答案】**
  **$E(2X + 3) = \dfrac{31}{5},\qquad V(2X + 3) = \dfrac{64}{25},\qquad \sigma(2X + 3) = \dfrac{8}{5}$**

---

#### 演習問題 6-(2)（P445）
- **【原题重现与翻译】**
  - 原题：確率変数 $X$ の期待値を $m$、標準偏差を $\sigma$ とする。確率変数 $Z = \dfrac{X - m}{\sigma}$ について $E(Z) = 0,\; \sigma(Z) = 1$ であることを示せ。
  - 中文：设随机变量 $X$ 的期望值为 $m$、标准差为 $\sigma$。证明随机变量 $Z = \dfrac{X - m}{\sigma}$ 满足 $E(Z) = 0,\; \sigma(Z) = 1$。
- **【考点定位】**
  - 随机变量的标准化（標準化）定理证明；线性变换公式的直接应用。
- **【分步标准解答】**
  題意より $E(X) = m,\; \sigma(X) = \sigma$（ただし標準偏差の定義および分母にあることから $\sigma > 0$）である。
  $Z$ を $X$ の 1 次式に書き直すと
  $$Z = \frac{X - m}{\sigma} = \frac{1}{\sigma} X - \frac{m}{\sigma}$$
  > 💡 讲师批注：先改写成 $aX + b$ 的标准线性形式（其中 $a = \frac{1}{\sigma},\; b = -\frac{m}{\sigma}$），即可直接套用 [6.1] 的变换公式。

  したがって、期待値の性質より
  $$E(Z) = E\!\left(\frac{1}{\sigma} X - \frac{m}{\sigma}\right) = \frac{1}{\sigma} E(X) - \frac{m}{\sigma} = \frac{1}{\sigma} \cdot m - \frac{m}{\sigma} = 0$$
  また、標準偏差の性質および $\sigma > 0$ より
  $$\sigma(Z) = \sigma\!\left(\frac{1}{\sigma} X - \frac{m}{\sigma}\right) = \left|\frac{1}{\sigma}\right| \sigma(X) = \frac{1}{\sigma} \cdot \sigma = 1$$
  よって、$E(Z) = 0,\; \sigma(Z) = 1$ が示された。（証明終）
  > 💡 讲师批注：写清 $\sigma > 0$ 从而 $\left|\frac{1}{\sigma}\right| = \frac{1}{\sigma}$，是日本考场证明题拿满分的严谨细节。这也正是第 8 节「正态分布标准化」的理论基石。

- **【最终答案】**
  **証明は上記の通り（$E(Z) = 0,\; \sigma(Z) = 1$）。**

---

#### 演習問題 6-(3)（P445）
- **【原题重现与翻译】**
  - 原题：確率変数 $X$ の期待値は $540$、分散は $8100$ である。$a, b$ は定数で $a > 0$ として、$Y = aX + b$ で定まる確率変数 $Y$ の期待値が $50$、標準偏差が $10$ になるとき、$a, b$ の値を求めよ。
  - 中文：随机变量 $X$ 的期望值为 $540$、方差为 $8100$。设 $a, b$ 为常数且 $a > 0$，由 $Y = aX + b$ 确定的随机变量 $Y$ 的期望值为 $50$、标准差为 $10$，求 $a, b$ 的值。
- **【考点定位】**
  - 线性变换公式逆向求参数（实质为日本考试中「偏差値」换算公式 $T = 10 \cdot \frac{X-m}{\sigma} + 50$ 的原型！）。
- **【分步标准解答】**
  題意より $E(X) = 540,\; V(X) = 8100$ であるから、$X$ の標準偏差は
  $$\sigma(X) = \sqrt{V(X)} = \sqrt{8100} = 90$$
  > 💡 讲师批注：先将 $X$ 的方差开方得到标准差 $\sigma(X) = 90$，再与 $\sigma(Y) = 10$ 建立方程，数字立刻变得非常清爽。

  $Y = aX + b$ に対して、変換公式および $a > 0$ より
  $$\sigma(Y) = |a|\sigma(X) = a \cdot 90 = 10 \implies a = \frac{1}{9}$$
  また、期待値の変換公式より
  $$E(Y) = aE(X) + b = \frac{1}{9} \times 540 + b = 50$$
  $$60 + b = 50 \implies b = -10$$
  > 💡 讲师批注（验算与背景拓展）：代入 $Y = \frac{1}{9}X - 10$，得 $E(Y) = 60 - 10 = 50$，$V(Y) = \frac{1}{81} \times 8100 = 100 \implies \sigma(Y) = 10$，完全正确！顺带一提，日本升学体系里的**偏差值（へんさち）**正是把原始成绩线性变换为「均值 50、标准差 10」的分数。

- **【最终答案】**
  **$a = \dfrac{1}{9},\qquad b = -10$**

---

#### 演習問題 6-(4)（P446）
- **【原题重现与翻译】**
  - 原题：1 個のサイコロを 2 回続けて投げるとき、出る目の数を順に $m, n$ とする。$m < 3$ である事象を $A$、積 $mn$ が奇数である事象を $B$、$|m - n| < 5$ である事象を $C$ とするとき、$A$ と $B$、$A$ と $C$ はそれぞれ独立か従属かを調べよ。
  - 中文：连续掷 1 个骰子 2 次，记出现的点数依次为 $m, n$。设事件 $A$ 为 $m < 3$，事件 $B$ 为乘积 $mn$ 是奇数，事件 $C$ 为 $|m - n| < 5$。判断 $A$ 与 $B$、$A$ 与 $C$ 分别是独立还是从属。
- **【考点定位】**
  - 事件独立性的充要判定：$P(A \cap B) = P(A)P(B)$ 是否成立。
- **【图解辅助（SVG 矢量图）】**

<svg viewBox="0 0 620 220" width="100%" xmlns="http://www.w3.org/2000/svg" style="background:#fafafa;border:1px solid #e0e0e0;border-radius:8px;margin:10px 0;">
  <!-- 左图：A 与 B -->
  <text x="150" y="20" text-anchor="middle" font-size="12.5" font-weight="bold" fill="#2c3e50">A (m&lt;3) 与 B (mn奇) 的 6×6 点阵</text>
  <g transform="translate(45,32)">
    <!-- 阴影 A: m=1,2 (前两行) -->
    <rect x="20" y="0" width="168" height="56" fill="#d6eaf8" fill-opacity="0.7"/>
    <!-- 网格与标签 -->
    <text x="10" y="18" text-anchor="middle" font-size="10" fill="#555">1</text>
    <text x="10" y="46" text-anchor="middle" font-size="10" fill="#555">2</text>
    <text x="10" y="74" text-anchor="middle" font-size="10" fill="#555">3</text>
    <text x="10" y="102" text-anchor="middle" font-size="10" fill="#555">4</text>
    <text x="10" y="130" text-anchor="middle" font-size="10" fill="#555">5</text>
    <text x="10" y="158" text-anchor="middle" font-size="10" fill="#555">6</text>
    <text x="-8" y="88" text-anchor="middle" font-size="11" font-weight="bold" fill="#333">m</text>
    <text x="34" y="180" text-anchor="middle" font-size="10" fill="#555">1</text>
    <text x="62" y="180" text-anchor="middle" font-size="10" fill="#555">2</text>
    <text x="90" y="180" text-anchor="middle" font-size="10" fill="#555">3</text>
    <text x="118" y="180" text-anchor="middle" font-size="10" fill="#555">4</text>
    <text x="146" y="180" text-anchor="middle" font-size="10" fill="#555">5</text>
    <text x="174" y="180" text-anchor="middle" font-size="10" fill="#555">6</text>
    <text x="202" y="180" text-anchor="middle" font-size="11" font-weight="bold" fill="#333">n</text>
    <!-- 网格线 -->
    <rect x="20" y="0" width="168" height="168" fill="none" stroke="#95a5a6"/>
    <line x1="20" y1="28" x2="188" y2="28" stroke="#ccc"/><line x1="20" y1="56" x2="188" y2="56" stroke="#2980b9" stroke-width="1.5"/>
    <line x1="20" y1="84" x2="188" y2="84" stroke="#ccc"/><line x1="20" y1="112" x2="188" y2="112" stroke="#ccc"/><line x1="20" y1="140" x2="188" y2="140" stroke="#ccc"/>
    <line x1="48" y1="0" x2="48" y2="168" stroke="#ccc"/><line x1="76" y1="0" x2="76" y2="168" stroke="#ccc"/><line x1="104" y1="0" x2="104" y2="168" stroke="#ccc"/>
    <line x1="132" y1="0" x2="132" y2="168" stroke="#ccc"/><line x1="160" y1="0" x2="160" y2="168" stroke="#ccc"/>
    <!-- B: m,n 皆奇 (9点), 其中 A∩B 用红实心, 其余用橙实心 -->
    <circle cx="34" cy="14" r="6" fill="#e74c3c"/><circle cx="90" cy="14" r="6" fill="#e74c3c"/><circle cx="146" cy="14" r="6" fill="#e74c3c"/>
    <circle cx="34" cy="70" r="5" fill="#f39c12"/><circle cx="90" cy="70" r="5" fill="#f39c12"/><circle cx="146" cy="70" r="5" fill="#f39c12"/>
    <circle cx="34" cy="126" r="5" fill="#f39c12"/><circle cx="90" cy="126" r="5" fill="#f39c12"/><circle cx="146" cy="126" r="5" fill="#f39c12"/>
  </g>
  <text x="150" y="214" text-anchor="middle" font-size="11" fill="#27ae60" font-weight="bold">P(A∩B)=3/36 = (12/36)(9/36) → 独立</text>

  <!-- 分隔线 -->
  <line x1="310" y1="15" x2="310" y2="210" stroke="#ddd" stroke-dasharray="4,3"/>

  <!-- 右图：A 与 C -->
  <text x="465" y="20" text-anchor="middle" font-size="12.5" font-weight="bold" fill="#2c3e50">A (m&lt;3) 与 C (|m−n|&lt;5) 的 6×6 点阵</text>
  <g transform="translate(360,32)">
    <rect x="20" y="0" width="168" height="56" fill="#d6eaf8" fill-opacity="0.7"/>
    <text x="10" y="18" text-anchor="middle" font-size="10" fill="#555">1</text>
    <text x="10" y="46" text-anchor="middle" font-size="10" fill="#555">2</text>
    <text x="10" y="74" text-anchor="middle" font-size="10" fill="#555">3</text>
    <text x="10" y="102" text-anchor="middle" font-size="10" fill="#555">4</text>
    <text x="10" y="130" text-anchor="middle" font-size="10" fill="#555">5</text>
    <text x="10" y="158" text-anchor="middle" font-size="10" fill="#555">6</text>
    <text x="-8" y="88" text-anchor="middle" font-size="11" font-weight="bold" fill="#333">m</text>
    <text x="34" y="180" text-anchor="middle" font-size="10" fill="#555">1</text>
    <text x="62" y="180" text-anchor="middle" font-size="10" fill="#555">2</text>
    <text x="90" y="180" text-anchor="middle" font-size="10" fill="#555">3</text>
    <text x="118" y="180" text-anchor="middle" font-size="10" fill="#555">4</text>
    <text x="146" y="180" text-anchor="middle" font-size="10" fill="#555">5</text>
    <text x="174" y="180" text-anchor="middle" font-size="10" fill="#555">6</text>
    <text x="202" y="180" text-anchor="middle" font-size="11" font-weight="bold" fill="#333">n</text>
    <rect x="20" y="0" width="168" height="168" fill="none" stroke="#95a5a6"/>
    <line x1="20" y1="28" x2="188" y2="28" stroke="#ccc"/><line x1="20" y1="56" x2="188" y2="56" stroke="#2980b9" stroke-width="1.5"/>
    <line x1="20" y1="84" x2="188" y2="84" stroke="#ccc"/><line x1="20" y1="112" x2="188" y2="112" stroke="#ccc"/><line x1="20" y1="140" x2="188" y2="140" stroke="#ccc"/>
    <line x1="48" y1="0" x2="48" y2="168" stroke="#ccc"/><line x1="76" y1="0" x2="76" y2="168" stroke="#ccc"/><line x1="104" y1="0" x2="104" y2="168" stroke="#ccc"/>
    <line x1="132" y1="0" x2="132" y2="168" stroke="#ccc"/><line x1="160" y1="0" x2="160" y2="168" stroke="#ccc"/>
    <!-- 补集 C_bar: 仅 (1,6) 和 (6,1) 用 × 标出 -->
    <rect x="160" y="0" width="28" height="28" fill="#e74c3c" fill-opacity="0.35"/>
    <text x="174" y="19" text-anchor="middle" font-size="14" font-weight="bold" fill="#c0392b">×</text>
    <rect x="20" y="140" width="28" height="28" fill="#e74c3c" fill-opacity="0.35"/>
    <text x="34" y="159" text-anchor="middle" font-size="14" font-weight="bold" fill="#c0392b">×</text>
  </g>
  <text x="465" y="214" text-anchor="middle" font-size="11" fill="#c0392b" font-weight="bold">P(A∩C)=11/36 ≠ (1/3)(17/18)=17/54 → 従属</text>
</svg>

- **【分步标准解答】**
  目の組 $(m, n)$ の総数は $6 \times 6 = 36$ 通りであり、これらは同様に確からしい。
  各事象の確率を求める：
  - 事象 $A$（$m < 3$）：$m \in \{1, 2\},\; n \in \{1, 2, 3, 4, 5, 6\}$ より $2 \times 6 = 12$ 通り
    $$P(A) = \frac{12}{36} = \frac{1}{3}$$
  - 事象 $B$（$mn$ が奇数）：$m, n$ がともに奇数（$\{1, 3, 5\}$）より $3 \times 3 = 9$ 通り
    $$P(B) = \frac{9}{36} = \frac{1}{4}$$
  - 事象 $C$（$|m - n| < 5$）：余事象 $\overline{C}$（$|m - n| \ge 5$、すなわち $|m - n| = 5$）は $(1, 6), (6, 1)$ の 2 通りのみであるから
    $$P(C) = 1 - \frac{2}{36} = \frac{34}{36} = \frac{17}{18}$$
  > 💡 讲师批注：求 $|m - n| < 5$ 切忌正着数 34 个点！用**余事象** $|m - n| = 5$（仅有 $(1, 6), (6, 1)$ 两个角点）瞬间得到 $36 - 2 = 34$。

  **[1] $A$ と $B$ について**
  $A \cap B$ は「$m < 3$ かつ $m, n$ がともに奇数」、すなわち $m = 1,\; n \in \{1, 3, 5\}$ の 3 通りである。
  $$P(A \cap B) = \frac{3}{36} = \frac{1}{12}$$
  一方、$P(A)P(B) = \dfrac{1}{3} \times \dfrac{1}{4} = \dfrac{1}{12}$。
  よって $P(A \cap B) = P(A)P(B)$ が成り立つから、**$A$ と $B$ は互いに独立である**。

  **[2] $A$ と $C$ について**
  $A \cap C$ は「$m \in \{1, 2\}$ かつ $|m - n| < 5$」である。$A$ の 12 通りのうち、$|m - n| = 5$ となるのは $(1, 6)$ の 1 通りのみなので、$A \cap C$ は $12 - 1 = 11$ 通りである。
  $$P(A \cap C) = \frac{11}{36}$$
  一方、$P(A)P(C) = \dfrac{1}{3} \times \dfrac{17}{18} = \dfrac{17}{54}$。
  $\dfrac{11}{36} = \dfrac{33}{108} \neq \dfrac{34}{108} = \dfrac{17}{54}$ より $P(A \cap C) \neq P(A)P(C)$ であるから、**$A$ と $C$ は従属である**。
  > 💡 讲师批注：千万不要凭直觉猜独立性！判断事件独立与否，必须老老实实算出 $P(A \cap B)$ 与 $P(A)P(B)$ 进行数值比对。

- **【最终答案】**
  **$A$ と $B$ は独立、$A$ と $C$ は従属**

---

#### 演習問題 6-(5)（P446）
- **【原题重现与翻译】**
  - 原题：1 個のサイコロを投げて、出た目の数が素数のときその数を $X$ とし、それ以外のとき $X = 6$ とする。次に、2 枚の硬貨を投げて、表の出た硬貨の枚数を $Y$ とする。$Z = 2X + Y$ で表される確率変数 $Z$ の期待値 $E(Z)$ と分散 $V(Z)$ を求めよ。
  - 中文：掷 1 个骰子，当点数为素数时记该数为 $X$，否则记 $X = 6$。接着抛 2 枚硬币，记正面朝上的枚数为 $Y$。求随机变量 $Z = 2X + Y$ 的期望值 $E(Z)$ 和方差 $V(Z)$。
- **【考点定位】**
  - 独立随机变量线性组合的期望与方差：$E(aX+bY) = aE(X)+bE(Y)$、$V(aX+bY) = a^2V(X)+b^2V(Y)$。
- **【分步标准解答】**
  **[1] $X$ の期待値 $E(X)$ と分散 $V(X)$**
  サイコロの目 $1, 2, 3, 4, 5, 6$ のうち素数は $2, 3, 5$ であり、それ以外の $1, 4, 6$（3 通り）のとき $X = 6$ となる。
  > 💡 讲师批注：**经典陷阱：$1$ 不是素数！** $1 \sim 6$ 中的素数只有 $2, 3, 5$，因此 $X = 6$ 对应 $1, 4, 6$ 这 3 种情况，概率为 $\frac{3}{6} = \frac{1}{2}$。

  よって $X$ の確率分布は：

  | $X$ | $2$ | $3$ | $5$ | $6$ | 計 |
  | :---: | :---: | :---: | :---: | :---: | :---: |
  | $P$ | $\dfrac{1}{6}$ | $\dfrac{1}{6}$ | $\dfrac{1}{6}$ | $\dfrac{3}{6}$ | $1$ |

  $$E(X) = 2 \cdot \frac{1}{6} + 3 \cdot \frac{1}{6} + 5 \cdot \frac{1}{6} + 6 \cdot \frac{3}{6} = \frac{2 + 3 + 5 + 18}{6} = \frac{28}{6} = \frac{14}{3}$$
  $$E(X^2) = 2^2 \cdot \frac{1}{6} + 3^2 \cdot \frac{1}{6} + 5^2 \cdot \frac{1}{6} + 6^2 \cdot \frac{3}{6} = \frac{4 + 9 + 25 + 108}{6} = \frac{146}{6} = \frac{73}{3}$$
  $$V(X) = E(X^2) - \{E(X)\}^2 = \frac{73}{3} - \left(\frac{14}{3}\right)^2 = \frac{219 - 196}{9} = \frac{23}{9}$$

  **[2] $Y$ の期待値 $E(Y)$ と分散 $V(Y)$**
  $Y$ は二項分布 $B\!\left(2, \dfrac{1}{2}\right)$ に従うから
  $$E(Y) = 2 \cdot \frac{1}{2} = 1, \qquad V(Y) = 2 \cdot \frac{1}{2} \cdot \left(1 - \frac{1}{2}\right) = \frac{1}{2}$$
  > 💡 讲师批注：亦可用分布表 $Y = 0(\frac{1}{4}),\; 1(\frac{1}{2}),\; 2(\frac{1}{4})$ 验证：$E(Y)=1,\; E(Y^2)=\frac{3}{2},\; V(Y)=\frac{1}{2}$。

  **[3] $Z = 2X + Y$ の期待値 $E(Z)$ と分散 $V(Z)$**
  サイコロ投げと硬貨投げは互いに独立な試行であるから、確率変数 $X$ と $Y$ は**互いに独立**である。よって
  $$E(Z) = E(2X + Y) = 2E(X) + E(Y) = 2 \cdot \frac{14}{3} + 1 = \frac{31}{3}$$
  $$V(Z) = V(2X + Y) = 2^2 V(X) + V(Y) = 4 \cdot \frac{23}{9} + \frac{1}{2} = \frac{92}{9} + \frac{1}{2} = \frac{184 + 9}{18} = \frac{193}{18}$$
  > 💡 讲师批注：务必写明「$X$ と $Y$ は互いに独立であるから」再展开方差！同时切记系数 $2$ 提出方差外要平方变为 $4$。

- **【最终答案】**
  **$E(Z) = \dfrac{31}{3},\qquad V(Z) = \dfrac{193}{18}$**

---

#### 演習問題 6-(6)（P447）
- **【原题重现与翻译】**
  - 原题：袋の中に ①、③、⑤ のカードがそれぞれ 3 枚、4 枚、1 枚ずつ入っている。この袋の中から 1 枚取り出しては袋に戻す試行を 5 回繰り返し、$k$ 回目（$k = 1, 2, \dots, 5$）に出たカードの番号が $p$ のとき $kp$ を得点として得られる。このとき、得点の合計の期待値と分散を求めよ。
  - 中文：袋中装有编号为 ①、③、⑤ 的卡片各 3 张、4 张、1 张。从袋中每次有放回地抽取 1 张，重复 5 次。若第 $k$ 次（$k = 1, 2, \dots, 5$）抽出的卡片编号为 $p$，则获得 $kp$ 分。求得分总和的期望值与方差。
- **【考点定位】**
  - 独立同分布（i.i.d.）随机变量加权和的期望与方差：$E\!\left(\sum k X_k\right)$ 与 $V\!\left(\sum k X_k\right)$。
- **【分步标准解答】**
  $k$ 回目（$k = 1, 2, 3, 4, 5$）に取り出したカードの番号を確率変数 $X_k$ とする。取り出したカードを戻す（復元抽出）ので、$X_1, X_2, X_3, X_4, X_5$ は**互いに独立**であり、すべて同じ確率分布に従う。
  各 $X_k$ の確率分布は次の表のようになる（総数 $3 + 4 + 1 = 8$ 枚）：

  | $X_k$ | $1$ | $3$ | $5$ | 計 |
  | :---: | :---: | :---: | :---: | :---: |
  | $P$ | $\dfrac{3}{8}$ | $\dfrac{4}{8}$ | $\dfrac{1}{8}$ | $1$ |

  これより $E(X_k)$ と $V(X_k)$ を求める：
  $$E(X_k) = 1 \cdot \frac{3}{8} + 3 \cdot \frac{4}{8} + 5 \cdot \frac{1}{8} = \frac{3 + 12 + 5}{8} = \frac{20}{8} = \frac{5}{2}$$
  $$E(X_k^2) = 1^2 \cdot \frac{3}{8} + 3^2 \cdot \frac{4}{8} + 5^2 \cdot \frac{1}{8} = \frac{3 + 36 + 25}{8} = \frac{64}{8} = 8$$
  $$V(X_k) = E(X_k^2) - \{E(X_k)\}^2 = 8 - \left(\frac{5}{2}\right)^2 = 8 - \frac{25}{4} = \frac{7}{4}$$

  得点の合計を $S$ とすると、$S = X_1 + 2X_2 + 3X_3 + 4X_4 + 5X_5$ である。
  したがって、期待値 $E(S)$ は
  $$E(S) = E(X_1) + 2E(X_2) + 3E(X_3) + 4E(X_4) + 5E(X_5)$$
  $$= (1 + 2 + 3 + 4 + 5) \cdot \frac{5}{2} = 15 \cdot \frac{5}{2} = \frac{75}{2}$$

  また、$X_1, X_2, X_3, X_4, X_5$ は互いに独立であるから、分散 $V(S)$ は
  $$V(S) = 1^2 V(X_1) + 2^2 V(X_2) + 3^2 V(X_3) + 4^2 V(X_4) + 5^2 V(X_5)$$
  $$= (1 + 4 + 9 + 16 + 25) \cdot \frac{7}{4} = 55 \cdot \frac{7}{4} = \frac{385}{4}$$
  > 💡 讲师批注：**最高频易错点！** 计算 $V(S)$ 时，每一项的系数 $k$ 提出方差外都必须**平方**，得到 $\sum_{k=1}^5 k^2 = \frac{5 \times 6 \times 11}{6} = 55$，千万不要错写成 $15 \times \frac{7}{4}$！

- **【最终答案】**
  **期待値：$\dfrac{75}{2}$、\quad 分散：$\dfrac{385}{4}$**

---

#### 演習問題 6-(7)（P447）
- **【原题重现与翻译】**
  - 原题：赤球 5 個、白球 3 個、青球 2 個入っている箱から任意に 1 個を取り出し、色を調べてもとに戻す試行を 5 回繰り返す。このとき、赤球または白球が出る回数を $X$ とする。確率変数 $X$ の期待値、分散、標準偏差を求めよ。
  - 中文：箱中有红球 5 个、白球 3 个、蓝球 2 个。任意取出 1 个查看颜色后放回，重复此试验 5 次。记出现红球或白球的次数为 $X$。求随机变量 $X$ 的期望值、方差与标准差。
- **【考点定位】**
  - 二项分布 $B(n, p)$ 的识别与公式 $E(X) = np,\; V(X) = npq,\; \sigma(X) = \sqrt{npq}$ 的直接应用。
- **【图解辅助（SVG 矢量图）】**

<svg viewBox="0 0 580 175" width="100%" xmlns="http://www.w3.org/2000/svg" style="background:#fafafa;border:1px solid #e0e0e0;border-radius:8px;margin:10px 0;">
  <text x="290" y="22" text-anchor="middle" font-size="13" font-weight="bold" fill="#2c3e50">二项分布 B(5, 4/5) 概率分布柱状图（E(X) = 4）</text>
  <line x1="55" y1="142" x2="525" y2="142" stroke="#333" stroke-width="1.4"/>
  <line x1="55" y1="35" x2="55" y2="142" stroke="#333" stroke-width="1.4"/>
  <text x="42" y="42" font-size="11" fill="#333">P</text>
  <text x="535" y="146" font-size="11" fill="#333">X</text>
  <!-- 概率：0:0.0003, 1:0.0064, 2:0.0512, 3:0.2048, 4:0.4096, 5:0.3277; 按 0.45 -> 100px -->
  <!-- X=0 -->
  <rect x="80" y="141" width="44" height="1" fill="#3498db" stroke="#2980b9"/>
  <text x="102" y="136" text-anchor="middle" font-size="9.5" fill="#555">0.0003</text>
  <text x="102" y="158" text-anchor="middle" font-size="11.5" fill="#333">0</text>
  <!-- X=1 -->
  <rect x="152" y="140" width="44" height="2" fill="#3498db" stroke="#2980b9"/>
  <text x="174" y="135" text-anchor="middle" font-size="9.5" fill="#555">0.0064</text>
  <text x="174" y="158" text-anchor="middle" font-size="11.5" fill="#333">1</text>
  <!-- X=2 -->
  <rect x="224" y="130" width="44" height="12" fill="#3498db" stroke="#2980b9"/>
  <text x="246" y="125" text-anchor="middle" font-size="9.5" fill="#555">0.0512</text>
  <text x="246" y="158" text-anchor="middle" font-size="11.5" fill="#333">2</text>
  <!-- X=3 -->
  <rect x="296" y="96" width="44" height="46" fill="#3498db" fill-opacity="0.7" stroke="#2980b9"/>
  <text x="318" y="91" text-anchor="middle" font-size="10" fill="#2c3e50">0.2048</text>
  <text x="318" y="158" text-anchor="middle" font-size="11.5" fill="#333">3</text>
  <!-- X=4 (均值峰值) -->
  <rect x="368" y="51" width="44" height="91" fill="#e74c3c" fill-opacity="0.75" stroke="#c0392b"/>
  <text x="390" y="46" text-anchor="middle" font-size="10.5" fill="#c0392b" font-weight="bold">0.4096</text>
  <text x="390" y="158" text-anchor="middle" font-size="12" fill="#c0392b" font-weight="bold">4 (=E(X))</text>
  <!-- X=5 -->
  <rect x="440" y="69" width="44" height="73" fill="#3498db" fill-opacity="0.7" stroke="#2980b9"/>
  <text x="462" y="64" text-anchor="middle" font-size="10" fill="#2c3e50">0.3277</text>
  <text x="462" y="158" text-anchor="middle" font-size="11.5" fill="#333">5</text>
</svg>

- **【分步标准解答】**
  1 回の試行で赤球または白球が出る確率 $p$ は、総数 $5 + 3 + 2 = 10$ 個のうち赤球または白球が $5 + 3 = 8$ 個であるから
  $$p = \frac{5 + 3}{10} = \frac{8}{10} = \frac{4}{5}$$
  よって、$q = 1 - p = 1 - \dfrac{4}{5} = \dfrac{1}{5}$ である。
  もとに戻しながら（復元抽出）同じ試行を 5 回繰り返すから、$X$ は二項分布 $B\!\left(5,\; \dfrac{4}{5}\right)$ に従う。
  > 💡 讲师批注：只要题目出现「**もとに戻す（有放回）**」「**$n$ 回繰り返す（独立重复 $n$ 次）**」「**出る回数（成功次数）**」三大关键词，立刻识别为二项分布 $B(n, p)$！

  したがって、二項分布の平均・分散・標準偏差の公式より
  $$E(X) = np = 5 \times \frac{4}{5} = 4$$
  $$V(X) = npq = 5 \times \frac{4}{5} \times \frac{1}{5} = \frac{4}{5}$$
  $$\sigma(X) = \sqrt{V(X)} = \sqrt{\frac{4}{5}} = \frac{2}{\sqrt{5}} = \frac{2\sqrt{5}}{5}$$
  > 💡 讲师批注：最后一步注意**分母有理化**，将 $\frac{2}{\sqrt{5}}$ 化为 $\frac{2\sqrt{5}}{5}$。

- **【最终答案】**
  **期待値：$4$、\quad 分散：$\dfrac{4}{5}$、\quad 標準偏差：$\dfrac{2\sqrt{5}}{5}$**
