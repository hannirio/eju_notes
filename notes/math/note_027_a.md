# 《EJU 教材全解与备课讲义》数学 027-A（P391–P405 上篇）

> **对应源文件**：`work_math/ocr_md/ocr_027_p391-405.md`（定積分と和の極限・不等式〔区分求積法、定積分と不等式、演習問題 16〕、面積〔曲線と $x$ 軸・2曲線間・曲線と $y$ 軸の間の面積、補足 1・補足 2、演習問題 17 (1)–(4)〕）
> **视觉核对参考图**：`work_math/ref_imgs/page_0391.jpg` – `page_0401.jpg`
> **分篇说明**：本切片共含 17 大题（27 小题），为保证每题均配备精准 SVG 图解与零跳步推导，拆分为上篇 `note_027_a.md`（知识点总览 + 词汇 + 演習問題 16 (1)–(5) + 演習問題 17 (1)–(4)）与下篇 `note_027_b.md`（演習問題 17 (5)–(12)）。

---

## 一、国内高中基础知识点唤醒与 EJU 考纲差异对比

本切片对应日本高中 **数学Ⅲ（積分法の応用）** 与 **数学Ⅱ（積分法）** 的核心压轴板块，涵盖 **区分求积法、定积分与不等式、平面图形的面积（含切线与高阶速算公式）** 三大高频考点。

### 1.1 区分求积法（定積分と和の極限）

设函数 $f(x)$ 在闭区间 $[a, b]$ 上连续，将 $[a, b]$ 作 $n$ 等分，步长 $\Delta x = \dfrac{b-a}{n}$，分点 $x_k = a + k\Delta x$，则有：
$$\int_a^b f(x)\,dx = \lim_{n \to \infty} \sum_{k=0}^{n-1} f(x_k)\Delta x = \lim_{n \to \infty} \sum_{k=1}^{n} f(x_k)\Delta x$$
**最常用特例（$a = 0, b = 1$）**：
$$\lim_{n \to \infty} \frac{1}{n} \sum_{k=0}^{n-1} f\!\left(\frac{k}{n}\right) = \lim_{n \to \infty} \frac{1}{n} \sum_{k=1}^{n} f\!\left(\frac{k}{n}\right) = \int_0^1 f(x)\,dx$$
**一般区间推广（上限为 $pn$ 或从 $an+1$ 到 $bn$）**：
$$\lim_{n \to \infty} \frac{1}{n} \sum_{k=an+1}^{bn} f\!\left(\frac{k}{n}\right) = \int_a^b f(x)\,dx$$
> 💡 **实战变形口诀**：先提取因子 $\dfrac{1}{n}$（对应 $dx$），再把剩余通项全部改写为 $\dfrac{k}{n}$（对应 $x$）的函数，最后由 $k$ 的起止范围确定积分下限与上限。

### 1.2 定积分与不等式（定積分と不等式）

1. **保号性**：若 $f(x)$ 在 $[a, b]$（$a < b$）上连续，恒有 $f(x) \ge 0$ 且不恒为 $0$，则：
   $$\int_a^b f(x)\,dx > 0$$
2. **保序性**：若 $f(x), g(x)$ 在 $[a, b]$（$a < b$）上连续，恒有 $f(x) \ge g(x)$ 且不恒相等，则：
   $$\int_a^b f(x)\,dx > \int_a^b g(x)\,dx$$
3. **经典应用**：
   - 放缩被积函数估计无法初等积分的定积分（如 $\int \frac{dx}{\sqrt{1-x^3}}$、$\int e^{-t^2}\,dt$）；
   - 利用单调函数图像与矩形面积比较，证明数列求和不等式（如调和级数 $1 + \frac{1}{2} + \cdots + \frac{1}{n}$ 与 $\log n$ 的夹逼）。

### 1.3 平面图形的面积公式（面積）

1. **曲线与 $x$ 轴之间**：区间 $[a, b]$（$a < b$）上，曲线 $y = f(x)$ 与 $x$ 轴、$x = a$、$x = b$ 围成的面积：
   $$S = \int_a^b |f(x)|\,dx$$
2. **两曲线之间**：区间 $[a, b]$（$a < b$）上，曲线 $y = f(x)$ 与 $y = g(x)$ 围成的面积：
   $$S = \int_a^b |f(x) - g(x)|\,dx = \int_a^b \left\{(\text{上側の曲線}) - (\text{下側の曲線})\right\}dx$$
3. **曲线与 $y$ 轴之间**：区间 $[c, d]$（$c < d$）上，曲线 $x = g(y)$ 与 $y$ 轴、$y = c$、$y = d$ 围成的面积：
   $$S = \int_c^d |g(y)|\,dy$$
   > ⚠️ **教材勘误提示**：原教材第 394 页（`page_0395.jpg`）`[19.3]` 正文中存在两处印刷错误：① 将曲线方程 $x = g(y)$ 误印为 $y = g(x)$（右侧配图正确标注为 $x = g(y)$）；② 将区间条件 $c < d$ 误印为 $c > d$。备课与授课时请务必修正。

### 1.4 切线与图形面积的高频速算公式（補足 1・補足 2）

| 图形结构 | 核心面积公式 | 记忆要点 / 推论 |
| :--- | :--- | :--- |
| **抛物线与直线（$\frac{1}{6}$ 公式）** | $\displaystyle S = \frac{|a|}{6}(\beta - \alpha)^3$ | 交点横坐标 $\alpha < \beta$；两抛物线 $ax^2+\cdots$ 与 $a'x^2+\cdots$ 则将 $|a|$ 换为 $|a-a'|$ |
| **抛物线与切线及竖线 $x=k$（$\frac{1}{3}$ 公式）** | $\displaystyle S = \frac{|a|}{3}|k - \alpha|^3$ | 被积式恰为 $|a|(x-\alpha)^2$，直接利用 $\int (x-\alpha)^2 dx = \frac{(x-\alpha)^3}{3}$ |
| **抛物线与两条切线（$\frac{1}{12}$ 公式）** | $\displaystyle S = \frac{|a|}{12}(\beta - \alpha)^3$ | 两切线交点横坐标必为中点 $x = \dfrac{\alpha + \beta}{2}$；弦切面积比 $S_1 : S_2 = 2 : 1$ |
| **两条同开口抛物线与公切线（$\frac{1}{12}$ 公式）** | $\displaystyle S = \frac{|a|}{12}(\beta - \alpha)^3$ | 两抛物线交点横坐标亦为两切点中点 $x = \dfrac{\alpha + \beta}{2}$ |
| **三次函数与切线（$\frac{1}{12}$ 公式）** | $\displaystyle S = \frac{|a|}{12}(\beta - \alpha)^4$ | 切点 $\alpha$、另一交点 $\beta$；一般地 $\int_\alpha^\beta (x-\alpha)^n(x-\beta)\,dx = -\dfrac{(\beta-\alpha)^{n+2}}{(n+1)(n+2)}$ |

### 1.5 国内高中 vs. 日本 EJU 考纲差异与符号习惯

| 对比维度 | 国内高中习惯 | 日本 EJU 习惯 | 备课/应试提醒 |
| :--- | :--- | :--- | :--- |
| **区分求积法** | 新高考已删去定积分，老教材仅作概念引入，几乎不考极限求和 | **数学Ⅲ高频必考题**，常与分部/裂项积分、根式/对数积分结合 | 务必练熟从 $\sum$ 中提取 $\frac{1}{n}$ 与 $\frac{k}{n}$，尤其注意上限为 $2n$ 或下限为 $n+1$ 的变式 |
| **面积速算公式** | 仅极少数竞赛生接触 $\frac{1}{6}$ 公式 | **$\frac{1}{6}$、$\frac{1}{3}$、$\frac{1}{12}$ 公式为日本考场标配** | EJU 为填空题（マークシート），直接套用可省去 70% 计算时间并大幅降低算错率 |
| **自然对数记号** | 写作 $\ln x$ | 统一写作 **$\log x$**（省略底数 $e$） | 本讲义严格遵循日本考场习惯写作 $\log x$ |
| **几何图形与积分结合** | 较少将圆弧、椭圆、扇形面积与定积分混合 | 极其强调 **「能用初等几何（三角形/扇形/弓形）绝不硬算积分」**（補足 2） | 遇到 $\sqrt{r^2 - x^2}$ 优先联想圆或扇形面积 |

---

## 二、日文核心词汇与公式假名注音

### 2.1 本切片日文核心词汇

- 区分求積法（くぶんきゅうせきほう / kubun kyuusekihou） — 区分求积法（利用定积分定义求极限的方法）
- 等分（とうぶん / toubun） — 等分（如 $n$ 等分）
- 和の極限（わのきょくげん / wa no kyokugen） — 和的极限
- 面積（めんせき / menseki） — 面积
- 囲まれた部分（かこまれたぶぶん / kakomareta bubun） — 所围成的部分（亦作 囲まれた図形 / かこまれたずけい）
- 上側の曲線（うわがわのきょくせん / uwagawa no kyokusen） — 上方的曲线（上边界曲线）
- 下側の曲線（したがわのきょくせん / shitagawa no kyokusen） — 下方的曲线（下边界曲线）
- 面積比（めんせきひ / mensekihi） — 面积比
- 1/6公式（ろくぶんのいちこうしき / rokubun no ichi koushiki） — $\frac{1}{6}$ 面积公式
- 1/12公式（じゅうにぶんのいちこうしき / juunibun no ichi koushiki） — $\frac{1}{12}$ 面积公式
- 短い方の弧（みじかいほうのこ / mijikai hou no ko） — 较短的弧（劣弧）
- 重なった部分（かさなったぶぶん / kasanatta bubun） — 重叠部分（公共部分）

### 2.2 核心公式的日本课堂口语读法

1. **区分求积法基本式** $\displaystyle \lim_{n \to \infty} \frac{1}{n} \sum_{k=1}^{n} f\!\left(\frac{k}{n}\right) = \int_0^1 f(x)\,dx$
   - 课堂读法：**リミット エヌ やじるし むげんだい、エヌぶんのいち、シグマ ケー イコール いちから エヌまでの エフ かっこ エヌぶんのケー かっことじ、イコール インテグラル ゼロから いちまでの エフエックス ディーエックス**
2. **两曲线间面积公式** $\displaystyle S = \int_a^b |f(x) - g(x)|\,dx$
   - 课堂读法：**エス イコール インテグラル エーから ビーまでの、ぜったいち エフエックス ひく ジーエックス ぜったいちとじ ディーエックス**
   - 备注：课堂口语常直接简述为 **「うえ ひく した を せきぶん（上减去下再积分）」**。
3. **$\frac{1}{6}$ 面积公式** $\displaystyle \int_\alpha^\beta (x - \alpha)(x - \beta)\,dx = -\frac{1}{6}(\beta - \alpha)^3$
   - 课堂读法：**インテグラル アルファから ベータまでの、エックス ひく アルファ かける エックス ひく ベータ ディーエックス、イコール マイナス ろくぶんのいち かっこ ベータ ひく アルファ かっことじ の さんじょう**

---

## 三、逐题深度解析（不可跳步）

---

### 演習問題 16（定積分と和の極限・不等式）

#### 演習問題 16-(1) [1]
- **【原题重现与翻译】**
  - 原题：次の極限値を求めよ。$\displaystyle \lim_{n \to \infty} \sum_{k=1}^{n} \left(\frac{n+k}{n^4}\right)^{\frac{1}{3}}$
  - 中文：求极限值 $\displaystyle \lim_{n \to \infty} \sum_{k=1}^{n} \left(\frac{n+k}{n^4}\right)^{\frac{1}{3}}$。
- **【考点定位】**
  - 区分求积法（提取 $\dfrac{1}{n}$ 与构造 $\dfrac{k}{n}$）、幂函数定积分。
- **【分步标准解答】**
  $$\sum_{k=1}^{n} \left(\frac{n+k}{n^4}\right)^{\frac{1}{3}} = \sum_{k=1}^{n} \left(\frac{1}{n^3} \cdot \frac{n+k}{n}\right)^{\frac{1}{3}} = \frac{1}{n} \sum_{k=1}^{n} \left(1 + \frac{k}{n}\right)^{\frac{1}{3}}$$
  > 💡 讲师批注：看到 $\left(\frac{\cdots}{n^4}\right)^{1/3}$，先把分母 $n^4$ 拆成 $n^3 \cdot n$：其中 $\left(\frac{1}{n^3}\right)^{1/3} = \frac{1}{n}$ 正好提到求和号外充当 $dx$，剩余 $\frac{n+k}{n} = 1 + \frac{k}{n}$ 充当 $1+x$。

  区分求積法により，
  $$\lim_{n \to \infty} \frac{1}{n} \sum_{k=1}^{n} \left(1 + \frac{k}{n}\right)^{\frac{1}{3}} = \int_0^1 (1+x)^{\frac{1}{3}}\,dx$$
  > 💡 讲师批注：$k$ 从 $1$ 到 $n$ 时，$\frac{k}{n}$ 覆盖区间 $[0, 1]$，故积分下限为 $0$、上限为 $1$。

  $$= \left[\frac{3}{4}(1+x)^{\frac{4}{3}}\right]_0^1 = \frac{3}{4}\left(2^{\frac{4}{3}} - 1^{\frac{4}{3}}\right) = \frac{3}{4}\left(2\sqrt[3]{2} - 1\right)$$
  > 💡 讲师批注：验算：$(1+x)^{1/3}$ 在 $[0, 1]$ 上取值介于 $1$ 与 $\sqrt[3]{2} \approx 1.260$ 之间，积分值应略大于 $1.13$；计算 $\frac{3}{4}(2 \times 1.2599 - 1) \approx 1.140$，完全吻合。
- **【最终答案】**
  **$\dfrac{3}{4}\left(2\sqrt[3]{2} - 1\right)$**（亦可写作 $\dfrac{3}{4}\left(2^{\frac{4}{3}} - 1\right)$）

---

#### 演習問題 16-(1) [2]
- **【原题重现与翻译】**
  - 原题：次の極限値を求めよ。$\displaystyle \lim_{n \to \infty} \sum_{k=1}^{n} \frac{n^2}{(k+n)^2(k+2n)}$
  - 中文：求极限值 $\displaystyle \lim_{n \to \infty} \sum_{k=1}^{n} \frac{n^2}{(k+n)^2(k+2n)}$。
- **【考点定位】**
  - 区分求积法、含重因式的有理分式部分分式分解（部分分数分解）。
- **【分步标准解答】**
  分母分子を $n^3$ で割ると，
  $$\sum_{k=1}^{n} \frac{n^2}{(k+n)^2(k+2n)} = \frac{1}{n} \sum_{k=1}^{n} \frac{1}{\left(1 + \dfrac{k}{n}\right)^2\left(2 + \dfrac{k}{n}\right)}$$
  > 💡 讲师批注：分母最高次为 $n^2 \cdot n = n^3$，分子为 $n^2$，齐次化时分子分母同除 $n^3$，自然分离出 $\frac{1}{n}$ 与 $\frac{k}{n}$。

  区分求積法により，
  $$(\text{与式}) = \int_0^1 \frac{1}{(x+1)^2(x+2)}\,dx$$

  ここで，$\dfrac{1}{(x+1)^2(x+2)} = \dfrac{A}{x+1} + \dfrac{B}{(x+1)^2} + \dfrac{C}{x+2}$ とおいて両辺に $(x+1)^2(x+2)$ を掛けると，
  $$1 = A(x+1)(x+2) + B(x+2) + C(x+1)^2$$
  $x = -1$ を代入して $B = 1$；$x = -2$ を代入して $C = 1$；$x^2$ の係数を比較して $A + C = 0 \implies A = -1$。
  > 💡 讲师批注：重因式 $(x+1)^2$ 必须拆成 $\frac{A}{x+1} + \frac{B}{(x+1)^2}$ 两项，切勿漏掉一次项！反向通分验算：$-(x+1)(x+2) + (x+2) + (x+1)^2 = -(x^2+3x+2) + (x+2) + (x^2+2x+1) = 1$，完全正确。

  したがって，
  $$\int_0^1 \left\{-\frac{1}{x+1} + \frac{1}{(x+1)^2} + \frac{1}{x+2}\right\}dx = \left[-\log|x+1| - \frac{1}{x+1} + \log|x+2|\right]_0^1$$
  $$= \left[\log\frac{x+2}{x+1} - \frac{1}{x+1}\right]_0^1 = \left(\log\frac{3}{2} - \frac{1}{2}\right) - (\log 2 - 1) = \frac{1}{2} + \log\frac{3}{4}$$
  > 💡 讲师批注：合并对数 $\log\frac{3}{2} - \log 2 = \log\frac{3}{4}$；注意 $-\frac{1}{2} - (-1) = +\frac{1}{2}$。
- **【最终答案】**
  **$\dfrac{1}{2} + \log\dfrac{3}{4}$**（亦可写作 $\dfrac{1}{2} + \log 3 - 2\log 2$）

---

#### 演習問題 16-(2) [1]
- **【原题重现与翻译】**
  - 原题：次の極限値を求めよ。$\displaystyle \lim_{n \to \infty} \sum_{k=1}^{2n} \frac{1}{3n+k}$
  - 中文：求极限值 $\displaystyle \lim_{n \to \infty} \sum_{k=1}^{2n} \frac{1}{3n+k}$。
- **【考点定位】**
  - 区分求积法（求和上限为 $2n$ 时的区间 $[0, 2]$ 转换）。
- **【分步标准解答】**
  $$\sum_{k=1}^{2n} \frac{1}{3n+k} = \frac{1}{n} \sum_{k=1}^{2n} \frac{1}{3 + \dfrac{k}{n}}$$
  > 💡 讲师批注：当 $k = 1$ 时 $\frac{k}{n} \to 0$；当 $k = 2n$ 时 $\frac{k}{n} = 2$。区间 $[0, 2]$ 被步长 $\Delta x = \frac{1}{n}$ 分成 $2n$ 份，因此直接对应 $\int_0^2$！

  区分求積法により，
  $$\lim_{n \to \infty} \frac{1}{n} \sum_{k=1}^{2n} \frac{1}{3 + \dfrac{k}{n}} = \int_0^2 \frac{1}{3+x}\,dx = \Big[\log|3+x|\Big]_0^2 = \log 5 - \log 3 = \log\frac{5}{3}$$
  > 💡 讲师批注：也可用 $N = 2n$ 换元：$\frac{2}{2n}\sum_{k=1}^{2n}\frac{1}{3 + 2\cdot\frac{k}{2n}} \to \int_0^1 \frac{2}{3+2x}\,dx = [\log(3+2x)]_0^1 = \log\frac{5}{3}$，结果完全一致。
- **【最终答案】**
  **$\log\dfrac{5}{3}$**

---

#### 演習問題 16-(2) [2]
- **【原题重现与翻译】**
  - 原题：次の極限値を求めよ。$\displaystyle \lim_{n \to \infty} \frac{1}{\sqrt{n}} \sum_{k=n+1}^{2n} \frac{1}{\sqrt{k}}$
  - 中文：求极限值 $\displaystyle \lim_{n \to \infty} \frac{1}{\sqrt{n}} \sum_{k=n+1}^{2n} \frac{1}{\sqrt{k}}$。
- **【考点定位】**
  - 区分求积法（求和下限为 $n+1$、上限为 $2n$）。
- **【分步标准解答】**
  $$\frac{1}{\sqrt{n}} \sum_{k=n+1}^{2n} \frac{1}{\sqrt{k}} = \frac{1}{n} \sum_{k=n+1}^{2n} \sqrt{\frac{n}{k}} = \frac{1}{n} \sum_{k=n+1}^{2n} \frac{1}{\sqrt{\dfrac{k}{n}}}$$
  > 💡 讲师批注：将 $\frac{1}{\sqrt{n}}$ 改写为 $\frac{1}{n} \cdot \sqrt{n}$，把 $\sqrt{n}$ 送入求和号内与 $\frac{1}{\sqrt{k}}$ 结合，立刻得到 $\frac{1}{\sqrt{k/n}}$！当 $k$ 从 $n+1$ 到 $2n$ 时，$\frac{k}{n}$ 覆盖区间 $[1, 2]$。

  区分求積法により，
  $$\lim_{n \to \infty} \frac{1}{n} \sum_{k=n+1}^{2n} \frac{1}{\sqrt{\dfrac{k}{n}}} = \int_1^2 x^{-\frac{1}{2}}\,dx = \Big[2\sqrt{x}\Big]_1^2 = 2\sqrt{2} - 2 = 2(\sqrt{2} - 1)$$
  > 💡 讲师批注：也可令 $k = n + j$（$j = 1, \dots, n$），化为 $\frac{1}{n}\sum_{j=1}^n \frac{1}{\sqrt{1 + j/n}} \to \int_0^1 \frac{dx}{\sqrt{1+x}} = [2\sqrt{1+x}]_0^1 = 2(\sqrt{2}-1)$，双法互验无误。
- **【最终答案】**
  **$2(\sqrt{2} - 1)$**

---

#### 演習問題 16-(3) [1]
- **【原题重现与翻译】**
  - 原题：次の不等式を証明せよ。$0 < x < \dfrac{1}{2}$ のとき $1 < \dfrac{1}{\sqrt{1-x^3}} < \dfrac{1}{\sqrt{1-x^2}}$
  - 中文：证明不等式：当 $0 < x < \dfrac{1}{2}$ 时，$1 < \dfrac{1}{\sqrt{1-x^3}} < \dfrac{1}{\sqrt{1-x^2}}$。
- **【考点定位】**
  - 幂函数大小比较与不等式同向变形（为第 [2] 问积分放缩铺垫）。
- **【分步标准解答】**
  $0 < x < \dfrac{1}{2}$ より $0 < x < 1$ であるから，各辺に正の数 $x^2$ を掛けて，
  $$0 < x^3 < x^2 < 1$$
  > 💡 讲师批注：$0 < x < 1$ 时高次幂更小，即 $x^3 < x^2$。

  よって，
  $$0 < 1 - x^2 < 1 - x^3 < 1$$
  各辺はすべて正であるから，正の平方根をとると，
  $$0 < \sqrt{1 - x^2} < \sqrt{1 - x^3} < 1$$
  さらに各辺の逆数をとると，不等号の向きが逆転して，
  $$1 < \frac{1}{\sqrt{1 - x^3}} < \frac{1}{\sqrt{1 - x^2}}$$
  > 💡 讲师批注：取倒数前必须确认各边均为正数，且不等号方向翻转。
- **【最终答案】**
  **（証明完了 / 证明完毕）**

---

#### 演習問題 16-(3) [2]
- **【原题重现与翻译】**
  - 原题：次の不等式を証明せよ。$\displaystyle \frac{1}{2} < \int_0^{\frac{1}{2}} \frac{dx}{\sqrt{1-x^3}} < \frac{\pi}{6}$
  - 中文：证明不等式：$\displaystyle \frac{1}{2} < \int_0^{\frac{1}{2}} \frac{dx}{\sqrt{1-x^3}} < \frac{\pi}{6}$。
- **【考点定位】**
  - 定积分保序性、三角换元法（$x = \sin\theta$）。
- **【分步标准解答】**
  [1] の結果より，閉区間 $\left[0, \dfrac{1}{2}\right]$ において，
  $$1 \le \frac{1}{\sqrt{1-x^3}} \le \frac{1}{\sqrt{1-x^2}}$$
  が成り立ち，いずれの不等号も等号が成り立つのは $x = 0$ のときだけ（常には等しくない）である。
  > 💡 讲师批注：必须明确写出一句「等号不恒成立（常には等しくない）」，才能由 $\le$ 推出积分后的严格不等号 $<$，这是日本考场证明题的关键采分点。

  したがって，定積分の大小関係より，
  $$\int_0^{\frac{1}{2}} 1\,dx < \int_0^{\frac{1}{2}} \frac{dx}{\sqrt{1-x^3}} < \int_0^{\frac{1}{2}} \frac{dx}{\sqrt{1-x^2}}$$

  左辺を計算すると，
  $$\int_0^{\frac{1}{2}} 1\,dx = \Big[x\Big]_0^{\frac{1}{2}} = \frac{1}{2}$$

  右辺について，$x = \sin\theta\;\left(0 \le \theta \le \dfrac{\pi}{6}\right)$ とおくと，$dx = \cos\theta\,d\theta$，$\sqrt{1-x^2} = \cos\theta$ であり，積分範囲は $x: 0 \to \dfrac{1}{2}$ に対して $\theta: 0 \to \dfrac{\pi}{6}$ となるから，
  $$\int_0^{\frac{1}{2}} \frac{dx}{\sqrt{1-x^2}} = \int_0^{\frac{\pi}{6}} \frac{\cos\theta}{\cos\theta}\,d\theta = \int_0^{\frac{\pi}{6}} 1\,d\theta = \Big[\theta\Big]_0^{\frac{\pi}{6}} = \frac{\pi}{6}$$
  > 💡 讲师批注：在 $0 \le \theta \le \frac{\pi}{6}$ 上 $\cos\theta > 0$，故 $\sqrt{1-\sin^2\theta} = \cos\theta$ 无需加绝对值。

  以上より，
  $$\frac{1}{2} < \int_0^{\frac{1}{2}} \frac{dx}{\sqrt{1-x^3}} < \frac{\pi}{6}$$
- **【最终答案】**
  **（証明完了 / 证明完毕）**

---

#### 演習問題 16-(4)
- **【原题重现与翻译】**
  - 原题：不等式 $\displaystyle \int_0^a e^{-t^2}\,dt \ge a - \frac{a^2}{3}$ を証明せよ。ただし、$a \ge 0$ とする。
  - 中文：证明不等式 $\displaystyle \int_0^a e^{-t^2}\,dt \ge a - \frac{a^2}{3}$，其中 $a \ge 0$。
  > ⚠️ **教材勘误提示**：日本高中教材经典原题为 $\displaystyle \int_0^a e^{-t^2}\,dt \ge a - \frac{a^3}{3}$（由 $e^{-t^2} \ge 1 - t^2$ 积分一步即得），原教材第 392 页（`page_0393.jpg`）极可能将 $a^3$ 误印为 $a^2$。但经严格验算，**印刷版不等式 $\displaystyle \int_0^a e^{-t^2}\,dt \ge a - \frac{a^2}{3}$ 对所有 $a \ge 0$ 竟然同样成立**！下面同时给出**版本 A（严格按印刷版 $a - \frac{a^2}{3}$ 证明）**与**版本 B（按经典原型 $a - \frac{a^3}{3}$ 证明）**，供备课双保险使用。
- **【考点定位】**
  - 利用微分法证明积分不等式（含变上限积分求导）、利用切线不等式 $e^x \ge 1 + x$ 进行积分放缩。
- **【分步标准解答】**

  **【版本 A：严格按原教材印刷版 $\displaystyle \int_0^a e^{-t^2}\,dt \ge a - \frac{a^2}{3}$ 证明】**

  $F(a) = \displaystyle \int_0^a e^{-t^2}\,dt - \left(a - \frac{a^2}{3}\right)$（$a \ge 0$）とおくと，$F(0) = 0$ である。
  両辺を $a$ で微分すると，
  $$F'(a) = e^{-a^2} - 1 + \frac{2}{3}a$$
  > 💡 讲师批注：对变上限积分求导得 $\frac{d}{da}\int_0^a e^{-t^2}\,dt = e^{-a^2}$。只要证得对任意 $a \ge 0$ 均有 $F'(a) \ge 0$，即可由 $F(0)=0$ 得 $F(a) \ge 0$。

  ここで $g(a) = F'(a) = e^{-a^2} - 1 + \dfrac{2}{3}a$（$a \ge 0$）とおき，さらに微分すると，
  $$g'(a) = -2a e^{-a^2} + \frac{2}{3} = 2\left(\frac{1}{3} - a e^{-a^2}\right)$$
  $h(a) = a e^{-a^2}$（$a \ge 0$）の増減を調べると，$h'(a) = (1 - 2a^2)e^{-a^2}$ より，$h(a)$ は $a = \dfrac{1}{\sqrt{2}}$ で最大値 $h\!\left(\dfrac{1}{\sqrt{2}}\right) = \dfrac{1}{\sqrt{2e}}$ をとる。
  $2e < 6 < 9$ より $\dfrac{1}{\sqrt{2e}} > \dfrac{1}{3}$ であり，また $h(0) = 0$，$\displaystyle \lim_{a \to \infty} h(a) = 0$ であるから，$g'(a) = 0$ すなわち $a e^{-a^2} = \dfrac{1}{3}$ は $a > 0$ にちょうど 2 つの解 $a_1, a_2$（$0 < a_1 < \dfrac{1}{\sqrt{2}} < a_2$）をもつ。
  > 💡 讲师批注：验证 $a_2$ 的位置：$h(1) = \frac{1}{e} \approx 0.368 > \frac{1}{3}$，由于 $h(a)$ 在 $(\frac{1}{\sqrt{2}}, \infty)$ 上单调递减，必有 $a_2 > 1$！

  増減表より $g(a)$ は $0 \le a \le a_1$ で増加，$a_1 \le a \le a_2$ で減少，$a \ge a_2$ で増加するから，$g(a)$ の最小値の候補は $g(0)$ または極小値 $g(a_2)$ である。
  - $g(0) = e^0 - 1 + 0 = 0$；
  - $a_2 e^{-a_2^2} = \dfrac{1}{3}$ より $e^{-a_2^2} = \dfrac{1}{3a_2}$ であり，$h(1) = \dfrac{1}{e} > \dfrac{1}{3}$ から $a_2 > 1$ なので，
    $$g(a_2) = \frac{1}{3a_2} - 1 + \frac{2}{3}a_2 = \frac{2a_2^2 - 3a_2 + 1}{3a_2} = \frac{(2a_2 - 1)(a_2 - 1)}{3a_2} > 0$$
  > 💡 讲师批注：把 $e^{-a_2^2} = \frac{1}{3a_2}$ 代回 $g(a_2)$ 瞬间消去超越函数，化为二次因式 $\frac{(2a_2-1)(a_2-1)}{3a_2}$，由 $a_2 > 1$ 一眼看出严格大于 $0$！

  よって，すべての $a \ge 0$ に対して $F'(a) = g(a) \ge 0$ が成り立つ。したがって $F(a)$ は $a \ge 0$ で単調に増加し，$F(a) \ge F(0) = 0$，すなわち，
  $$\int_0^a e^{-t^2}\,dt \ge a - \frac{a^2}{3}$$

  ---

  **【版本 B：经典原型题 $\displaystyle \int_0^a e^{-t^2}\,dt \ge a - \frac{a^3}{3}$ 的简洁证明】**

  任意の実数 $x$ に対して $e^x \ge 1 + x$ が成り立つ（$\because (e^x - 1 - x)' = e^x - 1$ より $x = 0$ で最小値 $0$）。
  $x = -t^2$ を代入すると，すべての実数 $t$ に対して $e^{-t^2} \ge 1 - t^2$ が成り立つ。
  両辺を区間 $[0, a]$（$a \ge 0$）で積分すると，
  $$\int_0^a e^{-t^2}\,dt \ge \int_0^a (1 - t^2)\,dt = \left[t - \frac{t^3}{3}\right]_0^a = a - \frac{a^3}{3}$$
- **【最终答案】**
  **（証明完了 / 证明完毕）**

---

#### 演習問題 16-(5)
- **【原题重现与翻译】**
  - 原题：$n$ は 2 以上の自然数とする。次の不等式を証明せよ。
    $$\log(n+1) < 1 + \frac{1}{2} + \frac{1}{3} + \cdots + \frac{1}{n} < \log n + 1$$
  - 中文：设 $n$ 为不小于 2 的自然数，证明不等式 $\displaystyle \log(n+1) < 1 + \frac{1}{2} + \frac{1}{3} + \cdots + \frac{1}{n} < \log n + 1$。
- **【考点定位】**
  - 单调函数与阶梯矩形面积比较（定积分估计调和级数）。
- **【图解辅助（SVG 矢量图）】**
<svg viewBox="0 0 460 220" width="460" height="220" xmlns="http://www.w3.org/2000/svg" style="background:#fff;border:1px solid #e2e8f0;border-radius:6px;">
  <!-- 坐标轴 -->
  <line x1="40" y1="185" x2="430" y2="185" stroke="#1e293b" stroke-width="1.5"/>
  <polygon points="430,185 422,181 422,189" fill="#1e293b"/>
  <line x1="55" y1="198" x2="55" y2="18" stroke="#1e293b" stroke-width="1.5"/>
  <polygon points="55,18 51,26 59,26" fill="#1e293b"/>
  <text x="435" y="190" font-size="13" font-style="italic" fill="#1e293b">x</text>
  <text x="44" y="20" font-size="13" font-style="italic" fill="#1e293b">y</text>
  <text x="40" y="200" font-size="12" fill="#1e293b">O</text>
  <!-- 左矩形（上界 1/k，浅蓝） -->
  <rect x="115" y="45" width="60" height="140" fill="#dbeafe" fill-opacity="0.55" stroke="#2563eb" stroke-width="1.2" stroke-dasharray="4,2"/>
  <rect x="175" y="115" width="60" height="70" fill="#dbeafe" fill-opacity="0.55" stroke="#2563eb" stroke-width="1.2" stroke-dasharray="4,2"/>
  <rect x="235" y="138" width="60" height="47" fill="#dbeafe" fill-opacity="0.55" stroke="#2563eb" stroke-width="1.2" stroke-dasharray="4,2"/>
  <rect x="315" y="154" width="60" height="31" fill="#dbeafe" fill-opacity="0.55" stroke="#2563eb" stroke-width="1.2" stroke-dasharray="4,2"/>
  <!-- 右矩形（下界 1/(k+1)，浅橙） -->
  <rect x="115" y="115" width="60" height="70" fill="#fed7aa" fill-opacity="0.6" stroke="#ea580c" stroke-width="1.2"/>
  <rect x="175" y="138" width="60" height="47" fill="#fed7aa" fill-opacity="0.6" stroke="#ea580c" stroke-width="1.2"/>
  <rect x="235" y="150" width="60" height="35" fill="#fed7aa" fill-opacity="0.6" stroke="#ea580c" stroke-width="1.2"/>
  <rect x="315" y="160" width="60" height="25" fill="#fed7aa" fill-opacity="0.6" stroke="#ea580c" stroke-width="1.2"/>
  <!-- 曲线 y = 1/x -->
  <path d="M 98 22 Q 110 40 115 45 Q 140 92 175 115 Q 205 130 235 138 Q 275 147 315 154 Q 355 159 405 164" fill="none" stroke="#dc2626" stroke-width="2.2"/>
  <text x="125" y="34" font-size="13" fill="#dc2626" font-weight="bold">y = 1/x</text>
  <!-- 刻度标注 -->
  <text x="111" y="200" font-size="12" fill="#1e293b">1</text>
  <text x="171" y="200" font-size="12" fill="#1e293b">2</text>
  <text x="231" y="200" font-size="12" fill="#1e293b">3</text>
  <text x="297" y="198" font-size="12" fill="#1e293b">…</text>
  <text x="311" y="200" font-size="12" fill="#1e293b">n</text>
  <text x="364" y="200" font-size="12" fill="#1e293b">n+1</text>
  <text x="42" y="49" font-size="12" fill="#1e293b">1</text>
  <line x1="51" y1="45" x2="59" y2="45" stroke="#1e293b" stroke-width="1.2"/>
  <!-- 图例 -->
  <rect x="260" y="24" width="12" height="10" fill="#dbeafe" stroke="#2563eb" stroke-dasharray="3,1"/>
  <text x="278" y="33" font-size="11" fill="#1e40af">上矩形和 = 1 + 1/2 + … + 1/n</text>
  <rect x="260" y="42" width="12" height="10" fill="#fed7aa" stroke="#ea580c"/>
  <text x="278" y="51" font-size="11" fill="#9a3412">下矩形和 = 1/2 + … + 1/n (至 n)</text>
</svg>
- **【分步标准解答】**
  関数 $y = \dfrac{1}{x}$ は $x > 0$ で単調に減少する。
  任意の自然数 $k$ に対して，$k \le x \le k+1$ のとき，
  $$\frac{1}{k+1} \le \frac{1}{x} \le \frac{1}{k}$$
  が成り立ち，いずれも常には等しくない。よって定積分の大小関係より，
  $$\int_k^{k+1} \frac{1}{k+1}\,dx < \int_k^{k+1} \frac{1}{x}\,dx < \int_k^{k+1} \frac{1}{k}\,dx$$
  すなわち，
  $$\frac{1}{k+1} < \int_k^{k+1} \frac{1}{x}\,dx < \frac{1}{k} \quad \cdots \text{①}$$
  > 💡 讲师批注：核心不等式 ① 一举两得：用右半边证左不等式，用左半边证右不等式！

  **（左の不等式の証明）**
  ① の右側の不等式 $\displaystyle \int_k^{k+1} \frac{1}{x}\,dx < \frac{1}{k}$ において，$k = 1, 2, \dots, n$ として辺々を加えると，
  $$\sum_{k=1}^{n} \int_k^{k+1} \frac{1}{x}\,dx < \sum_{k=1}^{n} \frac{1}{k}$$
  左辺は $\displaystyle \int_1^{n+1} \frac{1}{x}\,dx = \Big[\log x\Big]_1^{n+1} = \log(n+1)$ であるから，
  $$\log(n+1) < 1 + \frac{1}{2} + \frac{1}{3} + \cdots + \frac{1}{n}$$

  **（右の不等式の証明）**
  $n \ge 2$ であるから，① の左側の不等式 $\displaystyle \frac{1}{k+1} < \int_k^{k+1} \frac{1}{x}\,dx$ において，$k = 1, 2, \dots, n-1$ として辺々を加えると，
  $$\sum_{k=1}^{n-1} \frac{1}{k+1} < \sum_{k=1}^{n-1} \int_k^{k+1} \frac{1}{x}\,dx$$
  すなわち，
  $$\frac{1}{2} + \frac{1}{3} + \cdots + \frac{1}{n} < \int_1^n \frac{1}{x}\,dx = \Big[\log x\Big]_1^n = \log n$$
  両辺に $1$ を加えて，
  $$1 + \frac{1}{2} + \frac{1}{3} + \cdots + \frac{1}{n} < \log n + 1$$
  > 💡 讲师批注：右半边求和只取到 $k = n-1$（这就是题干要求 $n \ge 2$ 的原因），从而左侧正好是 $\frac{1}{2} + \cdots + \frac{1}{n}$，最后两边补加 $1$ 即得目标式。

  以上より，題意の不等式が示された。
- **【最终答案】**
  **（証明完了 / 证明完毕）**

---

### 演習問題 17（面積：前篇 (1)–(4)）

#### 演習問題 17-(1) [1]
- **【原题重现与翻译】**
  - 原题：次の曲線、直線と $x$ 軸で囲まれた図形の面積 $S$ を求めよ。$y = x^2 - 3x - 4$
  - 中文：求曲线 $y = x^2 - 3x - 4$ 与 $x$ 轴围成的图形面积 $S$。
- **【考点定位】**
  - 抛物线与 $x$ 轴围成的面积、$\frac{1}{6}$ 面积公式。
- **【图解辅助（SVG 矢量图）】**
<svg viewBox="0 0 340 200" width="340" height="200" xmlns="http://www.w3.org/2000/svg" style="background:#fff;border:1px solid #e2e8f0;border-radius:6px;">
  <!-- 坐标轴 -->
  <line x1="25" y1="65" x2="315" y2="65" stroke="#1e293b" stroke-width="1.5"/>
  <polygon points="315,65 307,61 307,69" fill="#1e293b"/>
  <line x1="100" y1="185" x2="100" y2="15" stroke="#1e293b" stroke-width="1.5"/>
  <polygon points="100,15 96,23 104,23" fill="#1e293b"/>
  <text x="320" y="69" font-size="13" font-style="italic" fill="#1e293b">x</text>
  <text x="88" y="20" font-size="13" font-style="italic" fill="#1e293b">y</text>
  <text x="86" y="80" font-size="12" fill="#1e293b">O</text>
  <!-- 阴影区域 x in [-1, 4] -> px in [65, 240], 顶点 x=1.5 -> px=152.5, y=-6.25 -> py=159 -->
  <path d="M 65 65 Q 152.5 253 240 65 Z" fill="#bfdbfe" fill-opacity="0.7" stroke="none"/>
  <!-- 抛物线 -->
  <path d="M 48 25 Q 152.5 270 257 25" fill="none" stroke="#2563eb" stroke-width="2.2"/>
  <text x="200" y="34" font-size="12" fill="#2563eb" font-weight="bold">y = x² - 3x - 4</text>
  <text x="148" y="112" font-size="15" font-style="italic" fill="#1e3a8a" font-weight="bold">S</text>
  <!-- 交点 -->
  <circle cx="65" cy="65" r="3" fill="#dc2626"/>
  <circle cx="240" cy="65" r="3" fill="#dc2626"/>
  <text x="50" y="56" font-size="12" fill="#dc2626">-1</text>
  <text x="242" y="56" font-size="12" fill="#dc2626">4</text>
</svg>
- **【分步标准解答】**
  $y = 0$ とすると，$x^2 - 3x - 4 = (x + 1)(x - 4) = 0$ より $x = -1,\; 4$。
  $-1 \le x \le 4$ で $y \le 0$ であるから，
  $$S = -\int_{-1}^{4} (x^2 - 3x - 4)\,dx = -\int_{-1}^{4} (x+1)(x-4)\,dx$$
  > 💡 讲师批注：曲线在 $x$ 轴下方，积分前必须加负号！

  $\dfrac{1}{6}$ 公式より，
  $$S = -\left\{-\frac{1}{6}(4 - (-1))^3\right\} = \frac{1}{6} \cdot 5^3 = \frac{125}{6}$$
  > 💡 讲师批注：直接积分验算：$-\left[\frac{x^3}{3} - \frac{3}{2}x^2 - 4x\right]_{-1}^4 = -\left(\frac{64}{3}-40\right) + \left(-\frac{1}{3}-\frac{3}{2}+4\right) = \frac{56}{3} + \frac{13}{6} = \frac{125}{6}$，完全一致。
- **【最终答案】**
  **$S = \dfrac{125}{6}$**

---

#### 演習問題 17-(1) [2]
- **【原题重现与翻译】**
  - 原题：次の曲線、直線と $x$ 軸で囲まれた図形の面積 $S$ を求めよ。$y = x^3 - 2x^2 - x + 2$
  - 中文：求曲线 $y = x^3 - 2x^2 - x + 2$ 与 $x$ 轴围成的图形面积 $S$。
- **【考点定位】**
  - 三次函数与 $x$ 轴围成的面积（跨越 $x$ 轴须分段去绝对值）。
- **【图解辅助（SVG 矢量图）】**
<svg viewBox="0 0 350 200" width="350" height="200" xmlns="http://www.w3.org/2000/svg" style="background:#fff;border:1px solid #e2e8f0;border-radius:6px;">
  <!-- 坐标轴 -->
  <line x1="25" y1="115" x2="325" y2="115" stroke="#1e293b" stroke-width="1.5"/>
  <polygon points="325,115 317,111 317,119" fill="#1e293b"/>
  <line x1="145" y1="188" x2="145" y2="15" stroke="#1e293b" stroke-width="1.5"/>
  <polygon points="145,15 141,23 149,23" fill="#1e293b"/>
  <text x="330" y="119" font-size="13" font-style="italic" fill="#1e293b">x</text>
  <text x="133" y="20" font-size="13" font-style="italic" fill="#1e293b">y</text>
  <text x="132" y="130" font-size="12" fill="#1e293b">O</text>
  <!-- 映射: x=0 -> 145, 1单位=65px; y=0 -> 115, 1单位=28px -->
  <!-- S1: [-1, 1] -> [80, 210], 极大值 x=-0.22, y=2.11 -> (131, 56) -->
  <path d="M 80 115 C 102 68, 130 48, 155 62 C 180 76, 198 100, 210 115 Z" fill="#bfdbfe" fill-opacity="0.7"/>
  <!-- S2: [1, 2] -> [210, 275], 极小值 x=1.55, y=-0.63 -> (246, 133) -->
  <path d="M 210 115 C 225 136, 255 140, 275 115 Z" fill="#fed7aa" fill-opacity="0.75"/>
  <!-- 三次曲线 -->
  <path d="M 60 175 C 72 135, 80 115, 80 115 C 102 68, 130 48, 155 62 C 180 76, 198 100, 210 115 C 225 136, 255 140, 275 115 C 288 95, 298 62, 306 25" fill="none" stroke="#2563eb" stroke-width="2.2"/>
  <text x="195" y="34" font-size="12" fill="#2563eb" font-weight="bold">y = (x+1)(x-1)(x-2)</text>
  <text x="148" y="96" font-size="13" font-style="italic" fill="#1e3a8a" font-weight="bold">S₁</text>
  <text x="236" y="130" font-size="12" font-style="italic" fill="#9a3412" font-weight="bold">S₂</text>
  <!-- 零点 -->
  <circle cx="80" cy="115" r="3" fill="#dc2626"/>
  <circle cx="210" cy="115" r="3" fill="#dc2626"/>
  <circle cx="275" cy="115" r="3" fill="#dc2626"/>
  <text x="64" y="108" font-size="12" fill="#dc2626">-1</text>
  <text x="206" y="108" font-size="12" fill="#dc2626">1</text>
  <text x="279" y="130" font-size="12" fill="#dc2626">2</text>
</svg>
- **【分步标准解答】**
  $$y = x^2(x - 2) - (x - 2) = (x - 2)(x^2 - 1) = (x + 1)(x - 1)(x - 2)$$
  $y = 0$ より，$x = -1,\; 1,\; 2$。
  符号を調べると，$-1 \le x \le 1$ で $y \ge 0$，$1 \le x \le 2$ で $y \le 0$ である。
  > 💡 讲师批注：绝对不能直接算 $\int_{-1}^2 y\,dx$，否则 $S_1$ 和 $S_2$ 会正负抵消！

  したがって，
  $$S = \int_{-1}^{1} (x^3 - 2x^2 - x + 2)\,dx - \int_1^2 (x^3 - 2x^2 - x + 2)\,dx$$
  第 1 項は偶関数・奇関数の性質を利用すると，
  $$\int_{-1}^{1} (x^3 - 2x^2 - x + 2)\,dx = 2\int_0^1 (-2x^2 + 2)\,dx = 2\left[-\frac{2}{3}x^3 + 2x\right]_0^1 = 2 \cdot \frac{4}{3} = \frac{8}{3}$$
  > 💡 讲师批注：在对称区间 $[-1, 1]$ 上奇函数 $x^3 - x$ 积分为 $0$，巧用对称性可省去一半算术！

  第 2 項は，
  $$-\int_1^2 (x^3 - 2x^2 - x + 2)\,dx = -\left[\frac{1}{4}x^4 - \frac{2}{3}x^3 - \frac{1}{2}x^2 + 2x\right]_1^2$$
  $$= -\left\{\left(4 - \frac{16}{3} - 2 + 4\right) - \left(\frac{1}{4} - \frac{2}{3} - \frac{1}{2} + 2\right)\right\} = -\left(\frac{2}{3} - \frac{13}{12}\right) = \frac{5}{12}$$
  よって，
  $$S = \frac{8}{3} + \frac{5}{12} = \frac{37}{12}$$
- **【最终答案】**
  **$S = \dfrac{37}{12}$**

---

#### 演習問題 17-(2) [1]
- **【原题重现与翻译】**
  - 原题：次の曲線、直線と $x$ 軸で囲まれた図形の面積 $S$ を求めよ。$y = -\cos^2 x\;\left(0 \le x \le \dfrac{\pi}{2}\right)$，$x$ 軸，$y$ 軸
  - 中文：求曲线 $y = -\cos^2 x\;\left(0 \le x \le \dfrac{\pi}{2}\right)$ 与 $x$ 轴、$y$ 轴围成的图形面积 $S$。
- **【考点定位】**
  - 三角函数平方的降幂积分（半角公式 $\cos^2 x = \frac{1+\cos 2x}{2}$）。
- **【图解辅助（SVG 矢量图）】**
<svg viewBox="0 0 320 175" width="320" height="175" xmlns="http://www.w3.org/2000/svg" style="background:#fff;border:1px solid #e2e8f0;border-radius:6px;">
  <line x1="30" y1="40" x2="295" y2="40" stroke="#1e293b" stroke-width="1.5"/>
  <polygon points="295,40 287,36 287,44" fill="#1e293b"/>
  <line x1="65" y1="160" x2="65" y2="15" stroke="#1e293b" stroke-width="1.5"/>
  <polygon points="65,15 61,23 69,23" fill="#1e293b"/>
  <text x="300" y="44" font-size="13" font-style="italic" fill="#1e293b">x</text>
  <text x="53" y="20" font-size="13" font-style="italic" fill="#1e293b">y</text>
  <text x="50" y="54" font-size="12" fill="#1e293b">O</text>
  <!-- y = -cos^2 x from x=0 (65, 130) to x=pi/2 (245, 40) -->
  <path d="M 65 40 L 245 40 C 195 40, 145 130, 65 130 Z" fill="#bfdbfe" fill-opacity="0.7"/>
  <path d="M 65 130 C 145 130, 195 40, 245 40" fill="none" stroke="#2563eb" stroke-width="2.2"/>
  <text x="155" y="128" font-size="12" fill="#2563eb" font-weight="bold">y = -cos²x</text>
  <text x="115" y="75" font-size="14" font-style="italic" fill="#1e3a8a" font-weight="bold">S</text>
  <text x="44" y="134" font-size="12" fill="#1e293b">-1</text>
  <text x="236" y="30" font-size="12" fill="#dc2626">π/2</text>
  <circle cx="245" cy="40" r="3" fill="#dc2626"/>
</svg>
- **【分步标准解答】**
  $0 \le x \le \dfrac{\pi}{2}$ において，常に $y = -\cos^2 x \le 0$ であるから，
  $$S = \int_0^{\frac{\pi}{2}} \left\{-(-\cos^2 x)\right\}dx = \int_0^{\frac{\pi}{2}} \cos^2 x\,dx$$
  半角の公式 $\cos^2 x = \dfrac{1 + \cos 2x}{2}$ を用いると，
  $$S = \int_0^{\frac{\pi}{2}} \frac{1 + \cos 2x}{2}\,dx = \left[\frac{x}{2} + \frac{\sin 2x}{4}\right]_0^{\frac{\pi}{2}} = \left(\frac{\pi}{4} + 0\right) - (0 + 0) = \frac{\pi}{4}$$
  > 💡 讲师批注：$\int_0^{\pi/2}\cos^2 x\,dx = \frac{\pi}{4}$ 是高频定积分结论（沃利斯公式特例），可以熟记用于快速验算。
- **【最终答案】**
  **$S = \dfrac{\pi}{4}$**

---

#### 演習問題 17-(2) [2]
- **【原题重现与翻译】**
  - 原题：次の曲線、直線と $x$ 軸で囲まれた図形の面積 $S$ を求めよ。$y = (3 - x)e^x$，$x = 0$，$x = 2$，$x$ 轴
  - 中文：求曲线 $y = (3 - x)e^x$ 与直线 $x = 0$、$x = 2$ 及 $x$ 轴围成的图形面积 $S$。
- **【考点定位】**
  - 多项式与指数函数乘积的分部积分法（部分積分法）。
- **【分步标准解答】**
  $0 \le x \le 2$ において，$3 - x > 0$ かつ $e^x > 0$ より常に $y > 0$ であるから，
  $$S = \int_0^2 (3 - x)e^x\,dx$$
  部分積分法により（$(e^x)' = e^x$ とみなして），
  $$S = \Big[(3 - x)e^x\Big]_0^2 - \int_0^2 (-1)e^x\,dx = (1 \cdot e^2 - 3 \cdot e^0) + \Big[e^x\Big]_0^2$$
  $$= (e^2 - 3) + (e^2 - 1) = 2e^2 - 4$$
  > 💡 讲师批注：求导验算：$\{(4-x)e^x\}' = -e^x + (4-x)e^x = (3-x)e^x$，故原函数为 $(4-x)e^x$，代入 $2$ 与 $0$ 得 $2e^2 - 4$，100% 准确！
- **【最终答案】**
  **$S = 2e^2 - 4$**

---

#### 演習問題 17-(3) [1]
- **【原题重现与翻译】**
  - 原题：次の曲線や直線で囲まれた図形の面積 $S$ を求めよ。$y = x^2 - x - 1$，$y = x + 2$
  - 中文：求抛物线 $y = x^2 - x - 1$ 与直线 $y = x + 2$ 围成的图形面积 $S$。
- **【考点定位】**
  - 抛物线与直线围成的面积、$\frac{1}{6}$ 面积公式。
- **【图解辅助（SVG 矢量图）】**
<svg viewBox="0 0 320 200" width="320" height="200" xmlns="http://www.w3.org/2000/svg" style="background:#fff;border:1px solid #e2e8f0;border-radius:6px;">
  <line x1="25" y1="150" x2="295" y2="150" stroke="#1e293b" stroke-width="1.5"/>
  <polygon points="295,150 287,146 287,154" fill="#1e293b"/>
  <line x1="115" y1="188" x2="115" y2="15" stroke="#1e293b" stroke-width="1.5"/>
  <polygon points="115,15 111,23 119,23" fill="#1e293b"/>
  <text x="300" y="154" font-size="13" font-style="italic" fill="#1e293b">x</text>
  <text x="103" y="20" font-size="13" font-style="italic" fill="#1e293b">y</text>
  <text x="102" y="164" font-size="12" fill="#1e293b">O</text>
  <!-- 映射: x=0->115 (40px/u), y=0->150 (22px/u) -->
  <!-- 交点 (-1,1)->(75,128), (3,5)->(235,40), 顶点 (0.5,-1.25)->(135,177.5) -->
  <path d="M 75 128 Q 145 220 235 40 L 75 128 Z" fill="#bfdbfe" fill-opacity="0.7"/>
  <path d="M 55 82 Q 140 250 250 15" fill="none" stroke="#2563eb" stroke-width="2.2"/>
  <line x1="45" y1="145" x2="265" y2="23" stroke="#16a34a" stroke-width="2"/>
  <text x="180" y="140" font-size="11" fill="#2563eb" font-weight="bold">y = x²-x-1</text>
  <text x="125" y="65" font-size="11" fill="#16a34a" font-weight="bold">y = x+2</text>
  <text x="148" y="122" font-size="14" font-style="italic" fill="#1e3a8a" font-weight="bold">S</text>
  <circle cx="75" cy="128" r="3" fill="#dc2626"/>
  <circle cx="235" cy="40" r="3" fill="#dc2626"/>
  <text x="42" y="125" font-size="11" fill="#dc2626">(-1,1)</text>
  <text x="240" y="44" font-size="11" fill="#dc2626">(3,5)</text>
</svg>
- **【分步标准解答】**
  2 つの式の交点の $x$ 座標を求めると，
  $$x^2 - x - 1 = x + 2 \iff x^2 - 2x - 3 = 0 \iff (x + 1)(x - 3) = 0$$
  よって $x = -1,\; 3$。
  $-1 \le x \le 3$ では直線 $y = x + 2$ が放物線 $y = x^2 - x - 1$ の上側にあるから，
  $$S = \int_{-1}^{3} \left\{(x + 2) - (x^2 - x - 1)\right\}dx = -\int_{-1}^{3} (x + 1)(x - 3)\,dx$$
  $\dfrac{1}{6}$ 公式より，
  $$S = \frac{1}{6}\left\{3 - (-1)\right\}^3 = \frac{64}{6} = \frac{32}{3}$$
- **【最终答案】**
  **$S = \dfrac{32}{3}$**

---

#### 演習問題 17-(3) [2]
- **【原题重现与翻译】**
  - 原题：次の曲線や直線で囲まれた図形の面積 $S$ を求めよ。$y = x^3 - 4x$，$y = 3x^2$
  - 中文：求曲线 $y = x^3 - 4x$ 与 $y = 3x^2$ 围成的图形面积 $S$。
- **【考点定位】**
  - 三次函数与二次函数围成的两段区域面积（判断上下位置切换）。
- **【分步标准解答】**
  交点の $x$ 座標を求めると，
  $$x^3 - 4x = 3x^2 \iff x^3 - 3x^2 - 4x = 0 \iff x(x + 1)(x - 4) = 0$$
  よって $x = -1,\; 0,\; 4$。
  $h(x) = (x^3 - 4x) - 3x^2 = x(x + 1)(x - 4)$ とおくと，
  - $-1 \le x \le 0$ のとき $h(x) \ge 0$（$y = x^3 - 4x$ が上側）
  - $0 \le x \le 4$ のとき $h(x) \le 0$（$y = 3x^2$ が上側）
  > 💡 讲师批注：画简单符号数轴即可判断上下关系：$x > 4$ 时 $h > 0$，过单根 $4, 0, -1$ 依次变号，故 $[0, 4]$ 为负、$[-1, 0]$ 为正。

  したがって，
  $$S = \int_{-1}^{0} (x^3 - 3x^2 - 4x)\,dx - \int_0^4 (x^3 - 3x^2 - 4x)\,dx$$
  $$= \left[\frac{1}{4}x^4 - x^3 - 2x^2\right]_{-1}^{0} - \left[\frac{1}{4}x^4 - x^3 - 2x^2\right]_{0}^{4}$$
  $$= \left\{0 - \left(\frac{1}{4} + 1 - 2\right)\right\} - \left\{(64 - 64 - 32) - 0\right\} = \frac{3}{4} + 32 = \frac{131}{4}$$
  > 💡 讲师批注：注意代入 $x = 4$ 时 $\frac{1}{4}\cdot 4^4 - 4^3 = 64 - 64 = 0$ 恰好抵消，只剩 $-2 \cdot 16 = -32$，计算非常清爽！
- **【最终答案】**
  **$S = \dfrac{131}{4}$**

---

#### 演習問題 17-(4) [1]
- **【原题重现与翻译】**
  - 原题：次の曲線や直線で囲まれた図形の面積 $S$ を求めよ。$y = e\log x$，$y = -1$，$y = 2e$，$y$ 軸
  - 中文：求曲线 $y = e\log x$ 与直线 $y = -1$、$y = 2e$ 及 $y$ 轴围成的图形面积 $S$。
- **【考点定位】**
  - 对 $y$ 积分求曲线与 $y$ 轴之间的面积（化为 $x = g(y)$）。
- **【图解辅助（SVG 矢量图）】**
<svg viewBox="0 0 320 205" width="320" height="205" xmlns="http://www.w3.org/2000/svg" style="background:#fff;border:1px solid #e2e8f0;border-radius:6px;">
  <line x1="25" y1="145" x2="295" y2="145" stroke="#1e293b" stroke-width="1.5"/>
  <polygon points="295,145 287,141 287,149" fill="#1e293b"/>
  <line x1="65" y1="195" x2="65" y2="15" stroke="#1e293b" stroke-width="1.5"/>
  <polygon points="65,15 61,23 69,23" fill="#1e293b"/>
  <text x="300" y="149" font-size="13" font-style="italic" fill="#1e293b">x</text>
  <text x="53" y="20" font-size="13" font-style="italic" fill="#1e293b">y</text>
  <text x="50" y="160" font-size="12" fill="#1e293b">O</text>
  <!-- y=2e -> py=35, y=-1 -> py=172 -->
  <!-- x = e^(y/e) 阴影 -->
  <path d="M 65 35 L 255 35 C 185 85, 115 130, 82 172 L 65 172 Z" fill="#bfdbfe" fill-opacity="0.7"/>
  <!-- 曲线 x = e^(y/e) -->
  <path d="M 74 188 C 85 162, 118 128, 175 88 C 215 60, 245 42, 268 26" fill="none" stroke="#2563eb" stroke-width="2.2"/>
  <line x1="65" y1="35" x2="275" y2="35" stroke="#16a34a" stroke-width="1.4" stroke-dasharray="4,2"/>
  <line x1="65" y1="172" x2="140" y2="172" stroke="#16a34a" stroke-width="1.4" stroke-dasharray="4,2"/>
  <text x="42" y="39" font-size="12" fill="#16a34a" font-weight="bold">2e</text>
  <text x="44" y="176" font-size="12" fill="#16a34a" font-weight="bold">-1</text>
  <text x="195" y="115" font-size="12" fill="#2563eb" font-weight="bold">x = e^(y/e)</text>
  <text x="115" y="95" font-size="15" font-style="italic" fill="#1e3a8a" font-weight="bold">S</text>
</svg>
- **【分步标准解答】**
  $y = e\log x$ を $x$ について解くと，$\log x = \dfrac{y}{e}$ より，
  $$x = e^{\frac{y}{e}}$$
  常に $x = e^{\frac{y}{e}} > 0$ であるから，求める面積 $S$ は $y$ で積分して，
  $$S = \int_{-1}^{2e} e^{\frac{y}{e}}\,dy = \left[e \cdot e^{\frac{y}{e}}\right]_{-1}^{2e} = e\left(e^2 - e^{-\frac{1}{e}}\right) = e^3 - e^{1 - \frac{1}{e}}$$
  > 💡 讲师批注：把对数函数改写成指数函数 $x = e^{y/e}$ 对 $y$ 积分，彻底避免了对 $\log x$ 的分部积分与分段讨论！注意 $\int e^{ay}\,dy = \frac{1}{a}e^{ay}$，这里 $a = \frac{1}{e}$，故系数为 $\frac{1}{1/e} = e$。
- **【最终答案】**
  **$S = e^3 - e^{1 - \frac{1}{e}}$**（亦可写作 $e\left(e^2 - e^{-\frac{1}{e}}\right)$）

---

#### 演習問題 17-(4) [2]
- **【原题重现与翻译】**
  - 原题：次の曲線や直線で囲まれた図形の面積 $S$ を求めよ。$y = -\cos x\;(0 \le x \le \pi)$，$x = \dfrac{1}{2}$，$y = -\dfrac{1}{2}$，$y$ 軸
  - 中文：求曲线 $y = -\cos x\;(0 \le x \le \pi)$ 与直线 $x = \dfrac{1}{2}$、$y = -\dfrac{1}{2}$ 及 $y$ 轴围成的图形面积 $S$。
- **【考点定位】**
  - 三角函数与直线的相对位置判断（弧度大小比较 $\dfrac{1}{2} < \dfrac{\pi}{3}$）与定积分。
- **【图解辅助（SVG 矢量图）】**
<svg viewBox="0 0 330 195" width="330" height="195" xmlns="http://www.w3.org/2000/svg" style="background:#fff;border:1px solid #e2e8f0;border-radius:6px;">
  <line x1="25" y1="88" x2="305" y2="88" stroke="#1e293b" stroke-width="1.5"/>
  <polygon points="305,88 297,84 297,92" fill="#1e293b"/>
  <line x1="65" y1="185" x2="65" y2="15" stroke="#1e293b" stroke-width="1.5"/>
  <polygon points="65,15 61,23 69,23" fill="#1e293b"/>
  <text x="310" y="92" font-size="13" font-style="italic" fill="#1e293b">x</text>
  <text x="53" y="20" font-size="13" font-style="italic" fill="#1e293b">y</text>
  <text x="50" y="102" font-size="12" fill="#1e293b">O</text>
  <!-- 映射: x=0->65, pi->265 (63.7px/rad); y=0->88 (70px/u) -->
  <!-- x=1/2 -> 97, y=-cos(0.5)=-0.878 -> 149.4; x=pi/3=1.047 -> 131.7, y=-0.5 -> 123 -->
  <path d="M 65 123 L 97 123 L 97 149.4 Q 81 158 65 158 Z" fill="#bfdbfe" fill-opacity="0.8"/>
  <!-- y = -cos x -->
  <path d="M 65 158 C 110 158, 145 110, 165 88 C 185 66, 220 18, 265 18" fill="none" stroke="#2563eb" stroke-width="2.2"/>
  <!-- 直线 y = -1/2 与 x = 1/2 -->
  <line x1="45" y1="123" x2="210" y2="123" stroke="#16a34a" stroke-width="1.5" stroke-dasharray="4,2"/>
  <line x1="97" y1="45" x2="97" y2="172" stroke="#ea580c" stroke-width="1.5" stroke-dasharray="4,2"/>
  <text x="195" y="45" font-size="12" fill="#2563eb" font-weight="bold">y = -cos x</text>
  <text x="215" y="127" font-size="11" fill="#16a34a" font-weight="bold">y = -1/2</text>
  <text x="101" y="55" font-size="11" fill="#ea580c" font-weight="bold">x = 1/2</text>
  <text x="75" y="143" font-size="13" font-style="italic" fill="#1e3a8a" font-weight="bold">S</text>
  <text x="44" y="162" font-size="11" fill="#1e293b">-1</text>
  <text x="125" y="102" font-size="11" fill="#64748b">π/3</text>
  <circle cx="131.7" cy="123" r="2.5" fill="#64748b"/>
</svg>
- **【分步标准解答】**
  曲線 $y = -\cos x$ と直線 $y = -\dfrac{1}{2}$ の交点は，$0 \le x \le \pi$ で $-\cos x = -\dfrac{1}{2} \implies \cos x = \dfrac{1}{2}$ より $x = \dfrac{\pi}{3}$ である。
  $\pi > 3$ より $\dfrac{\pi}{3} > 1 > \dfrac{1}{2}$ であるから，区間 $0 \le x \le \dfrac{1}{2}$ において，常に
  $$-\cos x < -\frac{1}{2}$$
  が成り立つ（直線 $y = -\dfrac{1}{2}$ が上側，曲線 $y = -\cos x$ が下側）。
  > 💡 讲师批注：千万不要把 $x = \frac{1}{2}$ 误看成 $x = \frac{\pi}{2}$！因为 $0.5 < \frac{\pi}{3} \approx 1.047$，在 $[0, \frac{1}{2}]$ 上曲线全程位于 $y = -\frac{1}{2}$ 下方，不存在交点切换。

  したがって，求める面積 $S$ は，
  $$S = \int_0^{\frac{1}{2}} \left\{-\frac{1}{2} - (-\cos x)\right\}dx = \int_0^{\frac{1}{2}} \left(\cos x - \frac{1}{2}\right)dx$$
  $$= \left[\sin x - \frac{1}{2}x\right]_0^{\frac{1}{2}} = \sin\frac{1}{2} - \frac{1}{4}$$
  > 💡 讲师批注：验算数值：$\sin 0.5 - 0.25 \approx 0.4794 - 0.25 = 0.2294 > 0$；区域宽 $0.5$，高度介于 $0.5$（左端）与 $1 - \cos 0.5 \to 0.878 - 0.5 = 0.378$（右端）之间，面积约 $0.5 \times 0.459 = 0.2295$，完全吻合！
- **【最终答案】**
  **$S = \sin\dfrac{1}{2} - \dfrac{1}{4}$**

---

> 👉 **续接下篇**：演習問題 17 (5)–(12) 完整解析请见 [`note_027_b.md`](./note_027_b.md)。
