# 《EJU 教材全解与备课讲义》数学 024-A（P346–P352）

> **对应源文件**：`work_math/ocr_md/ocr_024_p346-360.md`（前半部分：演習問題 11 续「漸近線・グラフの概形・2次導関数と極値・共通接線」；第 13 节「微分による方程式・不等式への応用」及演習問題 12）
> **视觉核对参考图**：`work_math/ref_imgs/page_0346.jpg` – `page_0352.jpg`（逐页逐式全量核对）
> **同切片下篇**：[`note_024_b.md`](./note_024_b.md)（P353–P360：不定积分基本性质、各类函数求法及演習問題 13）

---

## 一、国内高中基础知识点唤醒与 EJU 考纲差异对比

本讲义前半部分承接微分的几何应用（渐近线、凹凸性与图像草图、公切线），系统展开 **数学Ⅲ《微分法的应用》** 中最核心的两大压轴板块：**利用导数证明不等式** 与 **利用导数讨论方程实数解的个数（含参分离与切线条数问题）**。

### 1.1 渐近线与二阶导数判别极值

1. **三类渐近线（漸近線）求法**：
   - **垂直渐近线** $x = a$：满足 $\lim_{x \to a+0} f(x) = \pm\infty$ 或 $\lim_{x \to a-0} f(x) = \pm\infty$（通常出现在分母为 $0$ 或对数真数趋近 $+0$ 处）。
   - **水平渐近线** $y = b$：满足 $\lim_{x \to +\infty} f(x) = b$ 或 $\lim_{x \to -\infty} f(x) = b$。
   - **斜渐近线** $y = ax + b$（$a \neq 0$）：满足 $\lim_{x \to +\infty}\{f(x) - (ax+b)\} = 0$（或 $x \to -\infty$）。求法：
     $$a = \lim_{x \to \pm\infty}\frac{f(x)}{x}, \qquad b = \lim_{x \to \pm\infty}\{f(x) - ax\}$$
     对于有理分式，可直接用多项式除法拆为「一次式 $+$ 真分式」快速读出斜渐近线。
2. **利用二阶导数判别极值（第 2 次導関数と極値）**：
   - 若 $f'(a) = 0$ 且 $f''(a) > 0$（局部下凸），则 $f(x)$ 在 $x = a$ 处取得**极小值（極小値）**。
   - 若 $f'(a) = 0$ 且 $f''(a) < 0$（局部上凸），则 $f(x)$ 在 $x = a$ 处取得**极大值（極大値）**。
   - 若 $f''(a) = 0$，则无法仅靠二阶导数判定，需回到一阶导数 $f'(x)$ 在 $x=a$ 两侧的符号变化。

### 1.2 微分在不等式证明中的应用（[13.1] 不等式 $f(x) > g(x)$ の証明）

令 $F(x) = f(x) - g(x)$，通过研究 $F(x)$ 的单调性与最值证明 $F(x) > 0$，常用两大策略：
1. **最小值法**：求出 $F(x)$ 在定义域内的最小值，证明 $F(x)_{\min} > 0$。
2. **单调性 + 端点值法**：证明 $F(x)$ 在 $x \ge a$ 上单调递增（$F'(x) > 0$，或 $F'(x) \ge 0$ 且等号仅在孤立点成立），再验证端点 $F(a) \ge 0$，即可推出 $x > a$ 时 $F(x) > 0$。
   - 若一阶导数 $F'(x)$ 正负不易直接看出，需**继续求二阶导数 $F''(x)$**（甚至三阶导数），逐级反推单调性。
   - **双变量对称/齐次不等式**（如 $a, b$ 满足 $0 < a < b$）：
     - 分离变量法：变形为 $h(a) > h(b)$，转化为单变量函数 $h(x)$ 的单调性。
     - 齐次化换元法：令 $t = \dfrac{b}{a} > 1$，将双变量不等式降为一元函数不等式。

### 1.3 微分在方程实数解中的应用（[13.2]・[13.3]）

1. **实数解的个数（実数解の個数）**：
   - 方程 $f(x) = g(x)$ 的实数解个数 $\iff$ 两曲线 $y = f(x)$ 与 $y = g(x)$ 的**公共点（共有点）**个数。
   - **定数分離法（参变分离）**：若能等价变形为 $h(x) = a$（$a$ 为常数），则固定曲线 $y = h(x)$，上下平移水平直线 $y = a$，直接由极值与端点极限读出交点个数。
   - **3 次方程 $f(x) = 0$ 有 3 个不同实数解的充要条件**：存在极大值与极小值，且
     $$(\text{極大値}) \times (\text{極小値}) < 0$$
2. **实数解的存在性与唯一性（中間値の定理）**：
   - 若 $F(x)$ 在闭区间 $[a, b]$ 上连续，且 $F(a)F(b) < 0$（异号），则开区间 $(a, b)$ 内**至少存在 1 个**实数解。
   - 若在此基础上 $F(x)$ 单调递增（$F'(x) > 0$）或单调递减（$F'(x) < 0$），则实数解**有且仅有 1 个（ただ 1 つ）**。
3. **过曲线外一点的切线条数问题**：
   - 设切点为 $(t, f(t))$，写出切线方程并代入定点 $(p, q)$，得到关于切点横坐标 $t$ 的方程。
   - **关键提醒**：只有当不同切点 $t$ 对应不同切线时（例如严格凸/凹函数 $f''(x)$ 恒正或恒负、或 3 次函数），**切线条数才等于 $t$ 的不同实数解个数**！（对 4 次及以上函数可能出现「一条直线切于两点」的公切线，需特别注意。）

### 1.4 国内高中 vs. 日本 EJU 考纲差异对比

| 对比维度 | 国内高中（高考数学）习惯 | 日本 EJU（数学Ⅲ）习惯 | 备课/应试提醒 |
| :--- | :--- | :--- | :--- |
| **自然对数记号** | 一律写作 $\ln x$ | **一律写作 $\log x$**（底数 $e$ 省略） | **极高频易错点！** 本切片中 $\log(1+x)$、$\log b - \log a$、$2\log x + \log 3$ 全为自然对数 $\ln$ |
| **常用极限提示** | 高考常需自行放缩证明 $\lim\limits_{x\to\infty}\frac{\ln x}{x}=0$ | EJU 题干通常会直接给出「ただし、$\lim\limits_{x\to\infty}\frac{\log x}{x}=0$ を用いてもよい」 | 看到「ただし」给的极限条件，说明解题中**必然要用到它**求渐近线或端点趋势 |
| **增减表（増減表）** | 常以文字分点叙述单调区间 | 必须列出规范的 **増減表**（含 $x, y', y'', y$ 四行及箭头 $\nearrow, \searrow$） | 绘图题与极值题的标准得分步骤，且需标出拐点（変曲点）凹凸性 |
| **斜渐近线与隐函数绘图** | 高考不考斜渐近线与 $y^2 = x^2(8-x^2)$ 绘图 | 数学Ⅲ 常规题型，强调对称性与端点切线斜率 | 绘图务必检查：定义域、对称性、极值、拐点、渐近线、坐标轴交点 |
| **公切线（共通接線）** | 多用两切点联立斜率相等与截距相等 | 4 次曲线自公切线常直接用**恒等式 $(x-\alpha)^2(x-\beta)^2$ 比较系数** | 恒等式法比求导联立省一半计算量，EJU 填空提速神技 |

---

## 二、日文核心词汇与公式假名注音

### 2.1 本部分日文核心词汇

- 第2次導関数（だいにじどうかんすう / dainiji doukansuu） — 二阶导函数（亦称 2次導関数 / にじどうかんすう）
- 極値（きょくち / kyokuchi） — 极值（极大值与极小值的统称）
- 極大値（きょくだいち / kyokudaichi） — 极大值
- 極小値（きょくしょうち / kyokushouchi） — 极小值
- 変曲点（へんきょくてん / henkyokuten） — 拐点
- 増減表（ぞうげんひょう / zougenhyou） — 增减表（单调性与极值变化表）
- 単調増加（たんちょうぞうか / tanchou zouka） — 单调递增（亦作 単調に増加する）
- 単調減少（たんちょうげんしょう / tanchou genshou） — 单调递减（亦作 単調に減少する）
- 漸近線（ぜんきんせん / zenkinsen） — 渐近线
- 概形（がいけい / gaikei） — 草图、大致图形
- 共有点（きょうゆうてん / kyouyuuten） — 公共点
- 中間値の定理（ちゅうかんちのていり / chuukanchi no teiri） — 介值定理（中间值定理）

### 2.2 核心表达的日本课堂口语读法

1. **二阶导数** $f''(x)$
   - 课堂读法：**エフ ツーダッシュ エックス**（或 **エフ ダブルダッシュ エックス**）
   - 备注：一阶导数 $f'(x)$ 读作 **エフ ダッシュ エックス**。
2. **极限条件** $\lim_{x \to \infty} \dfrac{\log x}{x} = 0$
   - 课堂读法：**リミット エックス やじるし むげんだい、エックス ぶんの ログ エックス イコール ゼロ**
3. **唯一实数解**「実数解はただ 1 つである」
   - 课堂读法：**じっすうかい は ただ ひとつ である**（实数解有且仅有一个）。

---

## 三、逐题深度解析（不可跳步）

---

### 演習問題 11（续：漸近線・グラフの概形・2次導関数と極値・共通接線）

#### 演習問題 11-(2)
- **【原题重现与翻译】**
  - 原题：曲線 (1) $y = \dfrac{x^3}{x^2 - 4}$，(2) $y = 2x + \sqrt{x^2 - 1}$ の漸近線の方程式を求めよ。
  - 中文：求曲线 (1) $y = \dfrac{x^3}{x^2 - 4}$，(2) $y = 2x + \sqrt{x^2 - 1}$ 的渐近线方程。
- **【考点定位】**
  - 垂直渐近线与斜渐近线的求法；多项式拆分与根式有理化求极限（注意 $x \to -\infty$ 时 $\sqrt{x^2} = -x$）。
- **【图解辅助（SVG 矢量图）】**
  <svg viewBox="0 0 640 240" width="100%" xmlns="http://www.w3.org/2000/svg" style="background:#fafafa;border:1px solid #e5e7eb;border-radius:8px;">
    <!-- 左图：(1) y = x^3/(x^2-4) -->
    <g transform="translate(0,0)">
      <text x="155" y="20" font-size="13" font-weight="bold" fill="#1e293b" text-anchor="middle">(1) y = x³/(x²-4) 的 3 条渐近线</text>
      <!-- 坐标轴 -->
      <line x1="25" y1="130" x2="290" y2="130" stroke="#64748b" stroke-width="1.2"/>
      <line x1="155" y1="30" x2="155" y2="225" stroke="#64748b" stroke-width="1.2"/>
      <text x="285" y="144" font-size="11" fill="#475569">x</text>
      <text x="162" y="40" font-size="11" fill="#475569">y</text>
      <text x="145" y="143" font-size="11" fill="#475569">O</text>
      <!-- 渐近线 x=-2, x=2, y=x -->
      <line x1="115" y1="32" x2="115" y2="222" stroke="#ef4444" stroke-width="1.3" stroke-dasharray="5,4"/>
      <line x1="195" y1="32" x2="195" y2="222" stroke="#ef4444" stroke-width="1.3" stroke-dasharray="5,4"/>
      <line x1="65" y1="220" x2="245" y2="40" stroke="#ef4444" stroke-width="1.3" stroke-dasharray="5,4"/>
      <text x="108" y="220" font-size="10" fill="#dc2626" text-anchor="end">x=-2</text>
      <text x="200" y="220" font-size="10" fill="#dc2626">x=2</text>
      <text x="248" y="46" font-size="10" fill="#dc2626">y=x</text>
      <!-- 曲线示意 -->
      <path d="M 121 40 Q 130 130 155 130 Q 180 130 189 220" fill="none" stroke="#2563eb" stroke-width="2"/>
      <path d="M 203 38 C 210 95, 222 86, 265 40" fill="none" stroke="#2563eb" stroke-width="2"/>
      <path d="M 107 222 C 100 165, 88 174, 45 220" fill="none" stroke="#2563eb" stroke-width="2"/>
    </g>
    <!-- 分隔线 -->
    <line x1="320" y1="15" x2="320" y2="225" stroke="#cbd5e1" stroke-width="1"/>
    <!-- 右图：(2) y = 2x + sqrt(x^2-1) -->
    <g transform="translate(320,0)">
      <text x="160" y="20" font-size="13" font-weight="bold" fill="#1e293b" text-anchor="middle">(2) y = 2x + √(x²-1) 的 2 条斜渐近线</text>
      <line x1="25" y1="130" x2="295" y2="130" stroke="#64748b" stroke-width="1.2"/>
      <line x1="160" y1="30" x2="160" y2="225" stroke="#64748b" stroke-width="1.2"/>
      <text x="290" y="144" font-size="11" fill="#475569">x</text>
      <text x="167" y="40" font-size="11" fill="#475569">y</text>
      <text x="148" y="143" font-size="11" fill="#475569">O</text>
      <!-- 渐近线 y=3x (x>0) 与 y=x (x<0) -->
      <line x1="160" y1="130" x2="210" y2="30" stroke="#ef4444" stroke-width="1.3" stroke-dasharray="5,4"/>
      <line x1="160" y1="130" x2="65" y2="225" stroke="#ef4444" stroke-width="1.3" stroke-dasharray="5,4"/>
      <text x="215" y="40" font-size="10" fill="#dc2626">y=3x (x→+∞)</text>
      <text x="58" y="205" font-size="10" fill="#dc2626">y=x (x→-∞)</text>
      <!-- 曲线两支：右支起点 (1,2) -> (180,90)，左支起点 (-1,-2) -> (140,170) -->
      <path d="M 180 90 Q 186 70 212 34" fill="none" stroke="#2563eb" stroke-width="2"/>
      <path d="M 140 170 Q 130 155 68 216" fill="none" stroke="#2563eb" stroke-width="2"/>
      <circle cx="180" cy="90" r="3" fill="#2563eb"/>
      <circle cx="140" cy="170" r="3" fill="#2563eb"/>
      <text x="186" y="96" font-size="10" fill="#1d4ed8">(1, 2)</text>
      <text x="144" y="176" font-size="10" fill="#1d4ed8">(-1, -2)</text>
    </g>
  </svg>
- **【分步标准解答】**
  **(1)** 関数の定義域は $x \neq \pm 2$ である。
  - **垂直漸近線**：
    $$\lim_{x \to 2 \pm 0} \frac{x^3}{x^2 - 4} = \pm\infty, \qquad \lim_{x \to -2 \pm 0} \frac{x^3}{x^2 - 4} = \pm\infty$$
    よって、直線 $x = 2$ および $x = -2$ は漸近線である。
    > 💡 讲师批注：检查分母 $x^2-4=0$ 的解 $x=\pm 2$，此时分子 $x^3 = \pm 8 \neq 0$，故必为垂直渐近线。

  - **斜漸近線**：式を変形すると
    $$y = \frac{x(x^2 - 4) + 4x}{x^2 - 4} = x + \frac{4x}{x^2 - 4}$$
    したがって
    $$\lim_{x \to \pm\infty} (y - x) = \lim_{x \to \pm\infty} \frac{4x}{x^2 - 4} = \lim_{x \to \pm\infty} \frac{\frac{4}{x}}{1 - \frac{4}{x^2}} = 0$$
    よって、直線 $y = x$ も漸近線である。
    > 💡 讲师批注：分子次数比分母恰好高 1 次的有理函数，直接做多项式带余除法 $y = (\text{一次式}) + (\text{真分式})$，商式即为斜渐近线！

  **(2)** 関数の定義域は $x^2 - 1 \ge 0$、すなわち $x \le -1,\; x \ge 1$ である。定義域内で連続なので垂直漸近線はない。
  - **$x \to +\infty$ のとき**（$x > 0$ より $\sqrt{x^2} = x$）：
    $$\lim_{x \to +\infty} \frac{y}{x} = \lim_{x \to +\infty} \left(2 + \sqrt{1 - \frac{1}{x^2}}\right) = 2 + 1 = 3$$
    $$\lim_{x \to +\infty} (y - 3x) = \lim_{x \to +\infty} \left(\sqrt{x^2 - 1} - x\right) = \lim_{x \to +\infty} \frac{(x^2 - 1) - x^2}{\sqrt{x^2 - 1} + x} = \lim_{x \to +\infty} \frac{-1}{\sqrt{x^2 - 1} + x} = 0$$
    よって、直線 $y = 3x$ は漸近線である。
    > 💡 讲师批注：遇到 $\infty - \infty$ 型根式极限，务必进行**分子有理化**。

  - **$x \to -\infty$ のとき**（$x < 0$ より $\sqrt{x^2} = -x$ に注意！）：
    $$\lim_{x \to -\infty} \frac{y}{x} = \lim_{x \to -\infty} \left(2 - \sqrt{1 - \frac{1}{x^2}}\right) = 2 - 1 = 1$$
    $$\lim_{x \to -\infty} (y - x) = \lim_{x \to -\infty} \left(x + \sqrt{x^2 - 1}\right) = \lim_{x \to -\infty} \frac{x^2 - (x^2 - 1)}{x - \sqrt{x^2 - 1}} = \lim_{x \to -\infty} \frac{1}{x - \sqrt{x^2 - 1}} = 0$$
    よって、直線 $y = x$ も漸近線である。
    > 💡 讲师批注：**最高频易错点！** 当 $x \to -\infty$ 时，$x < 0$，所以 $\dfrac{\sqrt{x^2-1}}{x} = -\sqrt{1 - \frac{1}{x^2}} \to -1$，绝不能漏掉负号！同时在有理化后，分母 $x - \sqrt{x^2-1} \to (-\infty) - (+\infty) = -\infty$，故极限为 $0$。

- **【最终答案】**
  **(1) $x = 2,\; x = -2,\; y = x$**
  **(2) $y = 3x,\; y = x$**

---

#### 演習問題 11-(3)
- **【原题重现与翻译】**
  - 原题：関数 $y^2 = x^2(8 - x^2)$ が定める $x$ の関数 $y$ のグラフの概形をかけ。
  - 中文：画出由方程 $y^2 = x^2(8 - x^2)$ 确定的 $x$ 的函数 $y$ 的图像草图。
- **【考点定位】**
  - 隐函数图像的对称性分析、导数与二阶导数判定单调性与凹凸性、端点切线斜率（含垂直切线）。
- **【图解辅助（SVG 矢量图）】**
  <svg viewBox="0 0 460 270" width="85%" xmlns="http://www.w3.org/2000/svg" style="background:#fafafa;border:1px solid #e5e7eb;border-radius:8px;">
    <text x="230" y="20" font-size="13" font-weight="bold" fill="#1e293b" text-anchor="middle">y² = x²(8 - x²) 的图像概形（横卧 8 字形）</text>
    <!-- 坐标轴 -->
    <line x1="30" y1="145" x2="430" y2="145" stroke="#64748b" stroke-width="1.3"/>
    <line x1="230" y1="30" x2="230" y2="255" stroke="#64748b" stroke-width="1.3"/>
    <text x="422" y="160" font-size="12" fill="#475569">x</text>
    <text x="238" y="42" font-size="12" fill="#475569">y</text>
    <text x="218" y="160" font-size="11" fill="#475569">O</text>
    <!-- 辅助虚线与刻度：1单位 x = 50px, 1单位 y = 22px；x=2 -> 330, x=2√2≈2.828 -> 371.4; y=4 -> 57 -->
    <line x1="330" y1="57" x2="330" y2="233" stroke="#94a3b8" stroke-width="1" stroke-dasharray="4,3"/>
    <line x1="130" y1="57" x2="130" y2="233" stroke="#94a3b8" stroke-width="1" stroke-dasharray="4,3"/>
    <line x1="130" y1="57" x2="330" y2="57" stroke="#94a3b8" stroke-width="1" stroke-dasharray="4,3"/>
    <line x1="130" y1="233" x2="330" y2="233" stroke="#94a3b8" stroke-width="1" stroke-dasharray="4,3"/>
    <!-- 曲线：第 I 象限 (230,145) -> (330,57) -> (371.4,145) 等四象限对称 -->
    <path d="M 230 145 C 265 95, 295 57, 330 57 C 356 57, 371.4 95, 371.4 145 C 371.4 195, 356 233, 330 233 C 295 233, 265 195, 230 145 Z" fill="rgba(37,99,235,0.06)" stroke="#2563eb" stroke-width="2.2"/>
    <path d="M 230 145 C 195 95, 165 57, 130 57 C 104 57, 88.6 95, 88.6 145 C 88.6 195, 104 233, 130 233 C 165 233, 195 195, 230 145 Z" fill="rgba(37,99,235,0.06)" stroke="#2563eb" stroke-width="2.2"/>
    <!-- 关键点 -->
    <circle cx="330" cy="57" r="3.5" fill="#dc2626"/>
    <circle cx="330" cy="233" r="3.5" fill="#dc2626"/>
    <circle cx="130" cy="57" r="3.5" fill="#dc2626"/>
    <circle cx="130" cy="233" r="3.5" fill="#dc2626"/>
    <circle cx="371.4" cy="145" r="3.5" fill="#2563eb"/>
    <circle cx="88.6" cy="145" r="3.5" fill="#2563eb"/>
    <circle cx="230" cy="145" r="3.5" fill="#2563eb"/>
    <!-- 标注 -->
    <text x="330" y="48" font-size="11" fill="#dc2626" text-anchor="middle">(2, 4)</text>
    <text x="130" y="48" font-size="11" fill="#dc2626" text-anchor="middle">(-2, 4)</text>
    <text x="330" y="250" font-size="11" fill="#dc2626" text-anchor="middle">(2, -4)</text>
    <text x="130" y="250" font-size="11" fill="#dc2626" text-anchor="middle">(-2, -4)</text>
    <text x="377" y="160" font-size="11" fill="#1d4ed8">2√2</text>
    <text x="83" y="160" font-size="11" fill="#1d4ed8" text-anchor="end">-2√2</text>
    <text x="236" y="54" font-size="10" fill="#475569">4</text>
    <text x="236" y="242" font-size="10" fill="#475569">-4</text>
  </svg>
- **【分步标准解答】**
  1. **定義域と対称性**：
     $y^2 \ge 0$ より $x^2(8 - x^2) \ge 0$、すなわち $-2\sqrt{2} \le x \le 2\sqrt{2}$。
     また、$x$ を $-x$ に、あるいは $y$ を $-y$ に置き換えても方程式は変わらないため、グラフは **$x$ 軸、$y$ 軸、および原点に関して対称** である。
     > 💡 讲师批注：先看对称性可以省去 3/4 的计算量！只需完整研究第一象限 $0 \le x \le 2\sqrt{2},\; y \ge 0$ 即可。

  2. **第 1 象限（$0 \le x \le 2\sqrt{2},\; y \ge 0$）での増減と凹凸**：
     この範囲で $y = x\sqrt{8 - x^2}$ である。$0 < x < 2\sqrt{2}$ で微分すると
     $$y' = 1 \cdot \sqrt{8 - x^2} + x \cdot \frac{-2x}{2\sqrt{8 - x^2}} = \frac{(8 - x^2) - x^2}{\sqrt{8 - x^2}} = \frac{2(4 - x^2)}{\sqrt{8 - x^2}} = \frac{2(2 - x)(2 + x)}{\sqrt{8 - x^2}}$$
     $y' = 0$ とすると $x = 2$。さらに微分すると
     $$y'' = \frac{-4x\sqrt{8 - x^2} - 2(4 - x^2)\cdot\frac{-x}{\sqrt{8 - x^2}}}{8 - x^2} = \frac{-4x(8 - x^2) + 2x(4 - x^2)}{(8 - x^2)^{\frac{3}{2}}} = \frac{2x(x^2 - 12)}{(8 - x^2)^{\frac{3}{2}}}$$
     $0 < x < 2\sqrt{2}$ では $x^2 < 8 < 12$ より常に $y'' < 0$（上に凸）である。
     > 💡 讲师批注：验证 $y'' < 0$ 确保在第一象限没有拐点，曲线平滑上凸。

  3. **増減表と端点の様子**：
     - $x \to +0$ のとき $y' \to \dfrac{8}{\sqrt{8}} = 2\sqrt{2}$（原点での接線の傾きは $\pm 2\sqrt{2}$）。
     - $x \to 2\sqrt{2} - 0$ のとき $y' \to -\infty$（点 $(2\sqrt{2}, 0)$ での接線は $y$ 軸に平行）。

     | $x$ | $0$ | $\cdots$ | $2$ | $\cdots$ | $2\sqrt{2}$ |
     | :---: | :---: | :---: | :---: | :---: | :---: |
     | $y'$ | ($2\sqrt{2}$) | $+$ | $0$ | $-$ | ($-\infty$) |
     | $y''$ | | $-$ | $-$ | $-$ | |
     | $y$ | $0$ | $\nearrow$（上凸） | $4$（極大） | $\searrow$（上凸） | $0$ |

     これを $x$ 軸・$y$ 軸に関して対称移動すると、上図のグラフの概形を得る。
- **【最终答案】**
  **如上图所示：关于 $x$ 轴、$y$ 轴、原点均对称的横卧「8 字形」闭合曲线，经过 $(0,0)$、$(\pm 2\sqrt{2}, 0)$（此处切线垂直于 $x$ 轴），极值点为 $(\pm 2, 4)$ 与 $(\pm 2, -4)$。**

---

#### 演習問題 11-(4)
- **【原题重现与翻译】**
  - 原题：関数 $y = (-x + 1)e^{-x + 1}$ のグラフの概形をかけ。ただし、$\lim_{x \to \infty} x^3 e^{-x} = 0$。
  - 中文：画出函数 $y = (-x + 1)e^{-x + 1}$ 的图像草图。已知 $\lim_{x \to \infty} x^3 e^{-x} = 0$。
- **【考点定位】**
  - 含指数函数 $e^{-x}$ 的增减表、极值、拐点与水平渐近线分析。
- **【图解辅助（SVG 矢量图）】**
  <svg viewBox="0 0 460 250" width="85%" xmlns="http://www.w3.org/2000/svg" style="background:#fafafa;border:1px solid #e5e7eb;border-radius:8px;">
    <text x="230" y="20" font-size="13" font-weight="bold" fill="#1e293b" text-anchor="middle">y = (-x + 1)e^(-x+1) 的图像概形</text>
    <!-- 坐标轴：原点 (120, 155)，x: 1单位=55px，y: 1单位=35px (但下方放大以看清极小点与拐点) -->
    <line x1="25" y1="155" x2="435" y2="155" stroke="#64748b" stroke-width="1.3"/>
    <line x1="120" y1="30" x2="120" y2="235" stroke="#64748b" stroke-width="1.3"/>
    <text x="427" y="170" font-size="12" fill="#475569">x</text>
    <text x="128" y="42" font-size="12" fill="#475569">y</text>
    <text x="108" y="170" font-size="11" fill="#475569">O</text>
    <!-- 渐近线说明 -->
    <text x="365" y="146" font-size="10" fill="#dc2626">漸近線 y = 0 (x→+∞)</text>
    <!-- 关键坐标：x=0 -> (120, 75)[y=e]; x=1 -> (175, 155)[y=0]; x=2 -> (230, 200)[y=-1/e]; x=3 -> (285, 182)[y=-2/e²] -->
    <path d="M 92 32 C 102 52, 112 65, 120 75 C 145 110, 160 135, 175 155 C 195 182, 212 200, 230 200 C 250 200, 268 190, 285 182 C 320 166, 365 158, 425 156.5" fill="none" stroke="#2563eb" stroke-width="2.2"/>
    <!-- 辅助虚线 -->
    <line x1="230" y1="155" x2="230" y2="200" stroke="#94a3b8" stroke-width="1" stroke-dasharray="4,3"/>
    <line x1="120" y1="200" x2="230" y2="200" stroke="#94a3b8" stroke-width="1" stroke-dasharray="4,3"/>
    <line x1="285" y1="155" x2="285" y2="182" stroke="#94a3b8" stroke-width="1" stroke-dasharray="4,3"/>
    <line x1="120" y1="182" x2="285" y2="182" stroke="#94a3b8" stroke-width="1" stroke-dasharray="4,3"/>
    <!-- 关键点 -->
    <circle cx="120" cy="75" r="3.5" fill="#2563eb"/>
    <circle cx="175" cy="155" r="3.5" fill="#2563eb"/>
    <circle cx="230" cy="200" r="3.5" fill="#dc2626"/>
    <circle cx="285" cy="182" r="3.5" fill="#16a34a"/>
    <!-- 标签 -->
    <text x="128" y="78" font-size="11" fill="#1d4ed8">(0, e)</text>
    <text x="180" y="148" font-size="11" fill="#1d4ed8">1</text>
    <text x="230" y="148" font-size="11" fill="#475569" text-anchor="middle">2</text>
    <text x="285" y="148" font-size="11" fill="#475569" text-anchor="middle">3</text>
    <text x="114" y="204" font-size="10" fill="#dc2626" text-anchor="end">-1/e</text>
    <text x="114" y="185" font-size="10" fill="#16a34a" text-anchor="end">-2/e²</text>
    <text x="230" y="218" font-size="10" fill="#dc2626" text-anchor="middle">極小点 (2, -1/e)</text>
    <text x="300" y="198" font-size="10" fill="#16a34a">変曲点 (3, -2/e²)</text>
  </svg>
- **【分步标准解答】**
  1. **導関数と第 2 次導関数**：
     $$y' = (-1)e^{-x+1} + (-x+1)(-e^{-x+1}) = (x - 2)e^{-x+1}$$
     $$y'' = 1 \cdot e^{-x+1} + (x - 2)(-e^{-x+1}) = (3 - x)e^{-x+1}$$
     $e^{-x+1} > 0$ より、$y' = 0 \iff x = 2$、$y'' = 0 \iff x = 3$。
     > 💡 讲师批注：求导时利用公式 $\{(ax+b)e^{-x+1}\}' = (a - ax - b)e^{-x+1}$，切勿漏掉复合函数 $e^{-x+1}$ 的内层导数 $-1$。

  2. **極限と漸近線**：
     - $x \to -\infty$ のとき、$-x + 1 \to +\infty$、$e^{-x+1} \to +\infty$ より $\lim_{x \to -\infty} y = +\infty$。
     - $x \to +\infty$ のとき、$x > 1$ で $0 < x e^{-x} < x^3 e^{-x}$ かつ $\lim_{x \to \infty} x^3 e^{-x} = 0$ より、はさみうちの原理から $\lim_{x \to \infty} x e^{-x} = 0$。よって
       $$\lim_{x \to \infty} y = e \lim_{x \to \infty} \left(-x e^{-x} + e^{-x}\right) = e(0 + 0) = 0$$
       さらに $x > 1$ で $y < 0$ より、$x \to +\infty$ でグラフは $x$ 軸の下側から $x$ 軸（漸近線 $y = 0$）に限りなく近づく。
     > 💡 讲师批注：原题给出的条件是 $\lim_{x\to\infty} x^3 e^{-x} = 0$（指数为 $3$），严格写法是用 $0 < x e^{-x} < x^3 e^{-x}\ (x>1)$ 夹逼推出 $\lim_{x\to\infty} x e^{-x} = 0$。

  3. **増減表と特徴点**：
     $x = 0$ のとき $y = e$、$x = 1$ のとき $y = 0$、$x = 2$ のとき $y = -\dfrac{1}{e}$、$x = 3$ のとき $y = -\dfrac{2}{e^2}$。

     | $x$ | $-\infty$ | $\cdots$ | $2$ | $\cdots$ | $3$ | $\cdots$ | $+\infty$ |
     | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
     | $y'$ | | $-$ | $0$ | $+$ | $+$ | $+$ | |
     | $y''$ | | $+$ | $+$ | $+$ | $0$ | $-$ | |
     | $y$ | ($+\infty$) | $\searrow$（下凸） | $-\dfrac{1}{e}$（極小） | $\nearrow$（下凸） | $-\dfrac{2}{e^2}$（変曲点） | $\nearrow$（上凸） | ($-0$) |

- **【最终答案】**
  **如上图所示：过 $(0, e)$、$(1, 0)$，在 $x=2$ 处取极小值 $-\dfrac{1}{e}$，在 $\left(3, -\dfrac{2}{e^2}\right)$ 处有拐点，且以 $x$ 轴（$y=0$）为 $x \to +\infty$ 时的水平渐近线。**

---

#### 演習問題 11-(5)
- **【原题重现与翻译】**
  - 原题：2 次導関数を利用して、次の関数の極値を求めよ。
    [1] $f(x) = x^4 - 4x^3 + 4x^2 + 1$
    [2] $f(x) = 2\sin x - \sqrt{3}x \quad (0 \le x \le 2\pi)$
  - 中文：利用二阶导数，求下列函数的极值。
    [1] $f(x) = x^4 - 4x^3 + 4x^2 + 1$
    [2] $f(x) = 2\sin x - \sqrt{3}x \quad (0 \le x \le 2\pi)$
- **【考点定位】**
  - 利用 $f'(a)=0$ 且 $f''(a)$ 的正负号快速判定极值（免列增减表）。
- **【分步标准解答】**
  **[1]** $f(x) = x^4 - 4x^3 + 4x^2 + 1$ を微分すると
  $$f'(x) = 4x^3 - 12x^2 + 8x = 4x(x - 1)(x - 2)$$
  $$f''(x) = 12x^2 - 24x + 8$$
  $f'(x) = 0$ を解くと $x = 0,\; 1,\; 2$。それぞれにおける $f''(x)$ の符号を調べる。
  - $x = 0$ のとき：$f''(0) = 8 > 0$ より、$f(x)$ は極小値 $f(0) = 1$ をとる。
  - $x = 1$ のとき：$f''(1) = 12 - 24 + 8 = -4 < 0$ より、$f(x)$ は極大値 $f(1) = 1 - 4 + 4 + 1 = 2$ をとる。
  - $x = 2$ のとき：$f''(2) = 48 - 48 + 8 = 8 > 0$ より、$f(x)$ は極小値 $f(2) = 16 - 32 + 16 + 1 = 1$ をとる。
  > 💡 讲师批注：巧算验算——$f(x) = x^2(x-2)^2 + 1$，图像关于 $x=1$ 轴对称，W 字形谷底在 $x=0, 2$（值为 $1$），波峰在 $x=1$（值为 $2$），100% 吻合！

  **[2]** $f(x) = 2\sin x - \sqrt{3}x$ を微分すると
  $$f'(x) = 2\cos x - \sqrt{3}, \qquad f''(x) = -2\sin x$$
  $0 < x < 2\pi$ の範囲で $f'(x) = 0$ を解くと
  $$\cos x = \frac{\sqrt{3}}{2} \implies x = \frac{\pi}{6},\; \frac{11}{6}\pi$$
  それぞれにおける $f''(x)$ の符号を調べる。
  - $x = \dfrac{\pi}{6}$ のとき：$f''\left(\dfrac{\pi}{6}\right) = -2 \cdot \dfrac{1}{2} = -1 < 0$ より、極大値
    $$f\left(\frac{\pi}{6}\right) = 2 \cdot \frac{1}{2} - \sqrt{3}\cdot\frac{\pi}{6} = 1 - \frac{\sqrt{3}}{6}\pi$$
  - $x = \dfrac{11}{6}\pi$ のとき：$f''\left(\dfrac{11}{6}\pi\right) = -2 \cdot \left(-\frac{1}{2}\right) = 1 > 0$ より、極小値
    $$f\left(\frac{11}{6}\pi\right) = 2 \cdot \left(-\frac{1}{2}\right) - \sqrt{3}\cdot\frac{11}{6}\pi = -1 - \frac{11\sqrt{3}}{6}\pi$$
  > 💡 讲师批注：区间端点 $x=0$ 与 $x=2\pi$ 不是极值点（极值要求在点左右两侧均有定义且单调性反转）。
- **【最终答案】**
  **[1] $x = 1$ 时极大值 $2$；$x = 0,\; 2$ 时极小值 $1$。**
  **[2] $x = \dfrac{\pi}{6}$ 时极大值 $1 - \dfrac{\sqrt{3}}{6}\pi$；$x = \dfrac{11}{6}\pi$ 时极小值 $-1 - \dfrac{11\sqrt{3}}{6}\pi$。**

---

#### 演習問題 11-(6)
- **【原题重现与翻译】**
  - 原题：関数 $y = x^3(x - 4)$ のグラフと異なる 2 点で接する直線の方程式を求めよ。
  - 中文：求与函数 $y = x^3(x - 4)$ 的图像在两个不同点处相切的直线方程。
- **【考点定位】**
  - 4 次曲线的双切线（自公切线）求法；多项式恒等式比较系数法（避免繁琐的联立求导方程）。
- **【图解辅助（SVG 矢量图）】**
  <svg viewBox="0 0 420 220" width="80%" xmlns="http://www.w3.org/2000/svg" style="background:#fafafa;border:1px solid #e5e7eb;border-radius:8px;">
    <text x="210" y="20" font-size="13" font-weight="bold" fill="#1e293b" text-anchor="middle">y = x³(x - 4) 与双切线 y = -8x - 4</text>
    <!-- 坐标轴 -->
    <line x1="30" y1="75" x2="390" y2="75" stroke="#64748b" stroke-width="1.2"/>
    <line x1="150" y1="28" x2="150" y2="205" stroke="#64748b" stroke-width="1.2"/>
    <text x="382" y="89" font-size="11" fill="#475569">x</text>
    <text x="157" y="40" font-size="11" fill="#475569">y</text>
    <text x="139" y="89" font-size="11" fill="#475569">O</text>
    <!-- 4次曲线示意：过 (0,0) 拐点水平切线，极小点 (3,-27)，过 (4,0) -->
    <path d="M 92 32 C 110 68, 128 75, 150 75 C 180 75, 225 182, 270 182 C 305 182, 325 110, 345 38" fill="none" stroke="#2563eb" stroke-width="2.2"/>
    <!-- 双切线 y = -8x - 4：切点 α = 1-√3 ≈ -0.73, β = 1+√3 ≈ 2.73 -->
    <line x1="88" y1="55" x2="315" y2="202" stroke="#dc2626" stroke-width="1.8"/>
    <!-- 切点标注 -->
    <circle cx="115" cy="72.5" r="3.5" fill="#dc2626"/>
    <circle cx="261" cy="167" r="3.5" fill="#dc2626"/>
    <text x="108" y="96" font-size="10" fill="#dc2626" text-anchor="middle">切点 α=1-√3</text>
    <text x="278" y="160" font-size="10" fill="#dc2626">切点 β=1+√3</text>
    <text x="316" y="198" font-size="11" fill="#dc2626">y = -8x - 4</text>
    <text x="330" y="89" font-size="10" fill="#475569">4</text>
  </svg>
- **【分步标准解答】**
  求める直線の方程式を $y = mx + n$ とし、曲線 $y = x^4 - 4x^3$ との異なる 2 つの接点の $x$ 座標を $\alpha,\; \beta$（$\alpha \neq \beta$）とする。
  このとき、方程式 $x^4 - 4x^3 - (mx + n) = 0$ は $\alpha,\; \beta$ をともに 2 重解としてもつから、次の恒等式が成り立つ：
  $$x^4 - 4x^3 - mx - n = (x - \alpha)^2(x - \beta)^2$$
  > 💡 讲师批注：这是 EJU 与日本国公立大学二次考试的**王牌技巧**！4 次多项式减去一次式在两个点相切，差式必能因式分解为 $(x-\alpha)^2(x-\beta)^2$，完全不需要写两条切线联立 4 个未知数！

  ここで $\alpha + \beta = p$、$\alpha\beta = q$ とおくと、右辺は
  $$\{x^2 - (\alpha + \beta)x + \alpha\beta\}^2 = (x^2 - px + q)^2 = x^4 - 2px^3 + (p^2 + 2q)x^2 - 2pqx + q^2$$
  両辺の係数を比較すると：
  $$\begin{cases} -2p = -4 & \cdots ① \\ p^2 + 2q = 0 & \cdots ② \\ -2pq = -m & \cdots ③ \\ q^2 = -n & \cdots ④ \end{cases}$$
  ①より $p = 2$。②に代入して $4 + 2q = 0 \implies q = -2$。
  ③④に代入して：
  $$m = 2pq = 2 \cdot 2 \cdot (-2) = -8, \qquad n = -q^2 = -(-2)^2 = -4$$
  最後に、$\alpha,\; \beta$ が異なる 2 つの実数であることを確認する。$\alpha,\; \beta$ は 2 次方程式 $t^2 - 2t - 2 = 0$ の 2 解であり、判別式
  $$\frac{D}{4} = (-1)^2 - 1 \cdot (-2) = 3 > 0$$
  より確かに異なる 2 実数解（$1 \pm \sqrt{3}$）をもつ。
  > 💡 讲师批注：千万别漏掉最后一步「检验 $D > 0$」！若求出的 $p, q$ 对应虚数根，则双切线不存在。
- **【最终答案】**
  **$y = -8x - 4$**

---

### 演習問題 12（微分による方程式・不等式への応用）

#### 演習問題 12-(1)
- **【原题重现与翻译】**
  - 原题：$x > 0$ のとき、次の不等式が成り立つことを証明せよ。
    [1] $\log(1 + x) < \dfrac{1 + x}{2}$
    [2] $x^2 + 2e^{-x} > e^{-2x} + 1$
  - 中文：证明当 $x > 0$ 时，下列不等式成立。
    [1] $\log(1 + x) < \dfrac{1 + x}{2}$
    [2] $x^2 + 2e^{-x} > e^{-2x} + 1$
- **【考点定位】**
  - 不等式证明的两大基本法：[1] 求最小值 $>0$；[2] 连续求二阶导数 + 端点值为 $0$ 逐级推正。
- **【分步标准解答】**
  **[1]** $f(x) = \dfrac{1 + x}{2} - \log(1 + x)$（$x > 0$）とおく。微分すると
  $$f'(x) = \frac{1}{2} - \frac{1}{1 + x} = \frac{(1 + x) - 2}{2(1 + x)} = \frac{x - 1}{2(1 + x)}$$
  $x > 0$ における $f(x)$ の増減表は次の通り：

  | $x$ | $(0)$ | $\cdots$ | $1$ | $\cdots$ |
  | :---: | :---: | :---: | :---: | :---: |
  | $f'(x)$ | | $-$ | $0$ | $+$ |
  | $f(x)$ | | $\searrow$ | 極小 | $\nearrow$ |

  よって、$f(x)$ は $x = 1$ で最小値 $f(1) = 1 - \log 2$ をとる。
  ここで $e \fallingdotseq 2.718 > 2$ より $\log 2 < \log e = 1$ であるから、
  $$f(1) = 1 - \log 2 > 0$$
  したがって、$x > 0$ のとき常に $f(x) \ge f(1) > 0$、すなわち $\log(1 + x) < \dfrac{1 + x}{2}$ が成り立つ。（証明終）
  > 💡 讲师批注：本题在 $x=0$ 处 $f(0) = \frac{1}{2} > 0$，但 $f(x)$ 在 $(0,1)$ 先减后增，所以必须通过**最小值 $f(1) > 0$**来证明。

  **[2]** $f(x) = x^2 + 2e^{-x} - e^{-2x} - 1$（$x \ge 0$）とおく。微分すると
  $$f'(x) = 2x - 2e^{-x} + 2e^{-2x} = 2\left(x - e^{-x} + e^{-2x}\right)$$
  さらに微分すると
  $$f''(x) = 2\left(1 + e^{-x} - 2e^{-2x}\right) = 2(1 - e^{-x})(1 + 2e^{-x})$$
  > 💡 讲师批注：关键一步！把 $1 + e^{-x} - 2e^{-2x}$ 看作关于 $e^{-x}$ 的二次式，十字相乘分解为 $(1 - e^{-x})(1 + 2e^{-x})$，正负号瞬间明朗！

  $x > 0$ のとき $0 < e^{-x} < 1$ であるから、$1 - e^{-x} > 0$ かつ $1 + 2e^{-x} > 0$。ゆえに $f''(x) > 0$。
  したがって、$f'(x)$ は $x \ge 0$ で単調に増加する。
  ここで $f'(0) = 2(0 - 1 + 1) = 0$ より、$x > 0$ のとき $f'(x) > f'(0) = 0$。
  ゆえに、$f(x)$ も $x \ge 0$ で単調に増加する。
  ここで $f(0) = 0 + 2 - 1 - 1 = 0$ より、$x > 0$ のとき $f(x) > f(0) = 0$。
  すなわち、$x^2 + 2e^{-x} > e^{-2x} + 1$ が成り立つ。（証明終）
- **【最终答案】**
  **证明完毕（[1] 由最小值 $f(1)=1-\log 2 > 0$ 得证；[2] 由 $f''(x)>0 \implies f'(x)>0 \implies f(x)>0$ 逐级得证）。**

---

#### 演習問題 12-(2)
- **【原题重现与翻译】**
  - 原题：$0 < a < b < 2\pi$ のとき、不等式 $b\sin\dfrac{a}{2} > a\sin\dfrac{b}{2}$ が成り立つことを証明せよ。
  - 中文：证明当 $0 < a < b < 2\pi$ 时，不等式 $b\sin\dfrac{a}{2} > a\sin\dfrac{b}{2}$ 成立。
- **【考点定位】**
  - 双变量不等式的**分离变量法**：构造一元函数 $f(t) = \dfrac{\sin t}{t}$ 并证明其单调递减。
- **【分步标准解答】**
  $a > 0,\; b > 0$ であるから、示すべき不等式の両辺を $\dfrac{ab}{2} > 0$ で割ると、次と同値である：
  $$\frac{\sin\frac{a}{2}}{\frac{a}{2}} > \frac{\sin\frac{b}{2}}{\frac{b}{2}}$$
  > 💡 讲师批注：看到「$b$ 配 $a$、$a$ 配 $b$」的交叉乘积结构，立刻两边同除以 $ab$（或 $\frac{ab}{2}$），实现左右变量彻底分离！

  ここで関数 $f(t) = \dfrac{\sin t}{t}$（$0 < t < \pi$）を考える。微分すると
  $$f'(t) = \frac{t\cos t - \sin t}{t^2}$$
  分子を $g(t) = t\cos t - \sin t$（$0 \le t \le \pi$）とおいて微分すると
  $$g'(t) = (\cos t - t\sin t) - \cos t = -t\sin t$$
  $0 < t < \pi$ のとき $t > 0$ かつ $\sin t > 0$ より $g'(t) < 0$。
  ゆえに $g(t)$ は $0 \le t \le \pi$ で単調に減少し、$g(0) = 0$ であるから、$0 < t < \pi$ のとき $g(t) < g(0) = 0$。
  したがって $0 < t < \pi$ で $f'(t) < 0$ となり、$f(t)$ は区間 $(0, \pi)$ で単調に減少する。
  条件 $0 < a < b < 2\pi$ より $0 < \dfrac{a}{2} < \dfrac{b}{2} < \pi$ であるから
  $$f\left(\frac{a}{2}\right) > f\left(\frac{b}{2}\right) \iff \frac{\sin\frac{a}{2}}{\frac{a}{2}} > \frac{\sin\frac{b}{2}}{\frac{b}{2}}$$
  両辺に $\dfrac{ab}{2} > 0$ を掛けて、$b\sin\dfrac{a}{2} > a\sin\dfrac{b}{2}$ が成り立つ。（証明終）
  > 💡 讲师批注：几何直观——$\dfrac{\sin t}{t}$ 表示原点 $O$ 与曲线 $y=\sin t$ 上点 $(t, \sin t)$ 连线的斜率。因 $y=\sin t$ 在 $(0, \pi)$ 上严格上凸，割线斜率随 $t$ 增大而严格减小！
- **【最终答案】**
  **证明完毕（通过构造 $f(t) = \dfrac{\sin t}{t}$ 在 $(0, \pi)$ 上严格单调递减得证）。**

---

#### 演習問題 12-(3)
- **【原题重现与翻译】**
  - 原题：$0 < a < b$ のとき、不等式 $\sqrt{ab} < \dfrac{b - a}{\log b - \log a} < \dfrac{a + b}{2}$ が成り立つことを示せ。
  - 中文：证明当 $0 < a < b$ 时，不等式 $\sqrt{ab} < \dfrac{b - a}{\log b - \log a} < \dfrac{a + b}{2}$ 成立。
- **【考点定位】**
  - 著名的**对数平均不等式（ALG 不等式）**；齐次化换元 $t = \dfrac{b}{a} > 1$ 降维为一元函数求导。
- **【分步标准解答】**
  $0 < a < b$ より $t = \dfrac{b}{a}$ とおくと $t > 1$（すなわち $b = at$）であり、$\log b - \log a = \log\dfrac{b}{a} = \log t > 0$ である。
  > 💡 讲师批注：这是一个关于 $(a, b)$ 的一次齐次不等式！令 $t = \frac{b}{a} > 1$ 可以立刻消去一个变量，把双变量难题变成简单的单变量求导题。

  **(i) 左辺の不等式 $\sqrt{ab} < \dfrac{b - a}{\log b - \log a}$ の証明**：
  両辺を $a > 0$ で割り、$b = at$ を代入すると、示すべき不等式は
  $$\sqrt{t} < \frac{t - 1}{\log t} \iff \log t < \frac{t - 1}{\sqrt{t}} = \sqrt{t} - \frac{1}{\sqrt{t}}$$
  と同値である。そこで $f(t) = \sqrt{t} - \dfrac{1}{\sqrt{t}} - \log t$（$t \ge 1$）とおく。微分すると
  $$f'(t) = \frac{1}{2\sqrt{t}} + \frac{1}{2t\sqrt{t}} - \frac{1}{t} = \frac{t + 1 - 2\sqrt{t}}{2t\sqrt{t}} = \frac{(\sqrt{t} - 1)^2}{2t\sqrt{t}}$$
  $t > 1$ のとき $f'(t) > 0$ より、$f(t)$ は $t \ge 1$ で単調に増加する。
  $f(1) = 1 - 1 - 0 = 0$ であるから、$t > 1$ のとき $f(t) > 0$、よって左辺の不等式が成り立つ。

  **(ii) 右辺の不等式 $\dfrac{b - a}{\log b - \log a} < \dfrac{a + b}{2}$ の証明**：
  同様に両辺を $a > 0$ で割ると、示すべき不等式は
  $$\frac{t - 1}{\log t} < \frac{1 + t}{2} \iff \log t > \frac{2(t - 1)}{t + 1}$$
  と同値である。そこで $g(t) = \log t - \dfrac{2(t - 1)}{t + 1}$（$t \ge 1$）とおく。微分すると
  $$g'(t) = \frac{1}{t} - \frac{2(t + 1) - 2(t - 1)}{(t + 1)^2} = \frac{1}{t} - \frac{4}{(t + 1)^2} = \frac{(t + 1)^2 - 4t}{t(t + 1)^2} = \frac{(t - 1)^2}{t(t + 1)^2}$$
  $t > 1$ のとき $g'(t) > 0$ より、$g(t)$ は $t \ge 1$ で単調に増加する。
  $g(1) = 0 - 0 = 0$ であるから、$t > 1$ のとき $g(t) > 0$、よって右辺の不等式が成り立つ。

  (i), (ii) より、題意の不等式が証明された。（証明終）
  > 💡 讲师批注：这道题在国内外名校考题中反复出现（俗称「飘带不等式 / 对数均值不等式」），记住 $t = b/a > 1$ 后两个导数分子都能恰好配成完全平方 $(\sqrt{t}-1)^2$ 与 $(t-1)^2$！
- **【最终答案】**
  **证明完毕（令 $t = \dfrac{b}{a} > 1$ 分别构造 $f(t)$ 与 $g(t)$ 均单调递增且 $f(1)=g(1)=0$）。**

---

#### 演習問題 12-(4) & (5)
- **【原题重现与翻译】**
  - 原题：
    (4) 方程式 $2x^3 - 6x + 3 = 0$ の異なる実数解の個数を求めよ。
    (5) $a$ は実数の定数とする。方程式 $2x^3 - 6x + 3 - a = 0$ の異なる実数解の個数を調べよ。
  - 中文：
    (4) 求方程 $2x^3 - 6x + 3 = 0$ 的不同实数解的个数。
    (5) 设 $a$ 为实常数，讨论方程 $2x^3 - 6x + 3 - a = 0$ 的不同实数解的个数。
- **【考点定位】**
  - 3 次函数图像与水平直线 $y=0$、$y=a$ 的交点个数（定数分離法）。
- **【图解辅助（SVG 矢量图）】**
  <svg viewBox="0 0 420 230" width="80%" xmlns="http://www.w3.org/2000/svg" style="background:#fafafa;border:1px solid #e5e7eb;border-radius:8px;">
    <text x="210" y="20" font-size="13" font-weight="bold" fill="#1e293b" text-anchor="middle">y = 2x³ - 6x + 3 与水平直线 y = a 的交点</text>
    <!-- 坐标轴：O(190, 145), x:1单位=45px, y:1单位=13px -->
    <line x1="30" y1="145" x2="360" y2="145" stroke="#64748b" stroke-width="1.3"/>
    <line x1="190" y1="30" x2="190" y2="215" stroke="#64748b" stroke-width="1.3"/>
    <text x="352" y="160" font-size="11" fill="#475569">x</text>
    <text x="197" y="40" font-size="11" fill="#475569">y</text>
    <text x="178" y="160" font-size="11" fill="#475569">O</text>
    <!-- 3次曲线：(-1,7)->(145,54), (0,3)->(190,106), (1,-1)->(235,158) -->
    <path d="M 98 212 C 118 115, 130 54, 145 54 C 165 54, 178 90, 190 106 C 202 122, 215 158, 235 158 C 252 158, 266 95, 282 32" fill="none" stroke="#2563eb" stroke-width="2.2"/>
    <!-- 临界水平线 y=7, y=-1 -->
    <line x1="50" y1="54" x2="345" y2="54" stroke="#dc2626" stroke-width="1.3" stroke-dasharray="5,4"/>
    <line x1="50" y1="158" x2="345" y2="158" stroke="#dc2626" stroke-width="1.3" stroke-dasharray="5,4"/>
    <text x="348" y="58" font-size="11" fill="#dc2626">y = 7 (2個)</text>
    <text x="348" y="162" font-size="11" fill="#dc2626">y = -1 (2個)</text>
    <text x="348" y="110" font-size="10" fill="#16a34a">-1&lt;a&lt;7 (3個)</text>
    <text x="348" y="40" font-size="10" fill="#475569">a&gt;7 (1個)</text>
    <text x="348" y="188" font-size="10" fill="#475569">a&lt;-1 (1個)</text>
    <!-- 极值点 -->
    <circle cx="145" cy="54" r="3.5" fill="#dc2626"/>
    <circle cx="235" cy="158" r="3.5" fill="#dc2626"/>
    <text x="145" y="45" font-size="10" fill="#dc2626" text-anchor="middle">(-1, 7)</text>
    <text x="235" y="174" font-size="10" fill="#dc2626" text-anchor="middle">(1, -1)</text>
  </svg>
- **【分步标准解答】**
  $f(x) = 2x^3 - 6x + 3$ とおく。微分すると
  $$f'(x) = 6x^2 - 6 = 6(x + 1)(x - 1)$$
  $f'(x) = 0$ を解くと $x = -1,\; 1$。増減表は次の通り：

  | $x$ | $\cdots$ | $-1$ | $\cdots$ | $1$ | $\cdots$ |
  | :---: | :---: | :---: | :---: | :---: | :---: |
  | $f'(x)$ | $+$ | $0$ | $-$ | $0$ | $+$ |
  | $f(x)$ | $\nearrow$ | $7$（極大） | $\searrow$ | $-1$（極小） | $\nearrow$ |

  - **(4)** 方程式 $f(x) = 0$ の異なる実数解の個数は、曲線 $y = f(x)$ と $x$ 軸（$y = 0$）の共有点の個数に等しい。
    極大値 $f(-1) = 7 > 0$、極小値 $f(1) = -1 < 0$（かつ $\lim_{x\to\pm\infty} f(x) = \pm\infty$）より、共有点は **3 個** である。
  - **(5)** 方程式を $2x^3 - 6x + 3 = a$（すなわち $f(x) = a$）と変形する。
    曲線 $y = f(x)$ と水平直線 $y = a$ の共有点の個数を上図より読み取ると：
    - $a < -1$ または $a > 7$ のとき：**1 個**
    - $a = -1$ または $a = 7$ のとき：**2 個**
    - $-1 < a < 7$ のとき：**3 個**
  > 💡 讲师批注：把 (4) 视为 (5) 中 $a=0$ 的特例，可以立刻互相验算：$0 \in (-1, 7)$，确实对应 3 个不同实数解！
- **【最终答案】**
  **(4) 3 个**
  **(5) $a < -1$ 或 $a > 7$ 时 1 个；$a = -1$ 或 $a = 7$ 时 2 个；$-1 < a < 7$ 时 3 个。**

---

#### 演習問題 12-(6)
- **【原题重现与翻译】**
  - 原题：3 次方程式 $x^3 - 3a^2 x + 4a = 0$ が異なる 3 個の実数解をもつとき、定数 $a$ の値の範囲を求めよ。
  - 中文：当三次方程 $x^3 - 3a^2 x + 4a = 0$ 有 3 个不同实数解时，求常数 $a$ 的取值范围。
- **【考点定位】**
  - 无法定数分离的含参三次方程：利用「**极大值 $\times$ 极小值 $< 0$**」统一求解（无需对 $a>0$ 与 $a<0$ 繁琐分类）。
- **【分步标准解答】**
  $f(x) = x^3 - 3a^2 x + 4a$ とおく。微分すると
  $$f'(x) = 3x^2 - 3a^2 = 3(x + a)(x - a)$$
  - **$a = 0$ のとき**：$f(x) = x^3$ となり、方程式 $x^3 = 0$ の実数解は $x = 0$ の 1 個のみなので不適。
  - **$a \neq 0$ のとき**：$f'(x) = 0$ は異なる 2 実数解 $x = -a,\; a$ をもち、$f(x)$ はこの 2 点で極大値と極小値をとる。
    3 次方程式 $f(x) = 0$ が異なる 3 個の実数解をもつための必要十分条件は、
    $$(\text{極大値}) \times (\text{極小値}) < 0 \iff f(a) \cdot f(-a) < 0$$
    > 💡 讲师批注：使用乘积 $f(a)f(-a) < 0$ 的最大好处是**不用区分哪个是极大值、哪个是极小值**（不必分 $a>0$ 与 $a<0$ 讨论）！

    それぞれ計算すると：
    $$f(a) = a^3 - 3a^3 + 4a = -2a^3 + 4a = -2a(a^2 - 2)$$
    $$f(-a) = -a^3 + 3a^3 + 4a = 2a^3 + 4a = 2a(a^2 + 2)$$
    よって条件は
    $$f(a)f(-a) = -4a^2(a^2 - 2)(a^2 + 2) < 0$$
    $a \neq 0$ より $4a^2 > 0$、また常に $a^2 + 2 > 0$ であるから、両辺を $-4a^2(a^2 + 2) < 0$ で割ると
    $$a^2 - 2 > 0 \iff a < -\sqrt{2},\; \sqrt{2} < a$$
    （これは $a \neq 0$ を満たす。）
  > 💡 讲师批注：代入特值验算——取 $a=2$，$f(x) = x^3 - 12x + 8$，$f(-2) = 24 > 0,\; f(2) = -8 < 0$，确实有 3 个不同实数解！
- **【最终答案】**
  **$a < -\sqrt{2},\; \sqrt{2} < a$**

---

#### 演習問題 12-(7)
- **【原题重现与翻译】**
  - 原题：$a$ を定数とする。方程式 $ax = 2\log x + \log 3$ の実数解の個数について調べよ。ただし、$\lim_{x \to \infty} \dfrac{\log x}{x} = 0$ を用いてもよい。
  - 中文：设 $a$ 为常数，讨论方程 $ax = 2\log x + \log 3$ 的实数解个数。已知可使用 $\lim_{x \to \infty} \dfrac{\log x}{x} = 0$。
- **【考点定位】**
  - 真数条件 $x > 0$ + 定数分離法 $a = \dfrac{2\log x + \log 3}{x}$ + 渐近线 $y = 0$ 处交点个数的临界讨论。
- **【图解辅助（SVG 矢量图）】**
  <svg viewBox="0 0 430 220" width="80%" xmlns="http://www.w3.org/2000/svg" style="background:#fafafa;border:1px solid #e5e7eb;border-radius:8px;">
    <text x="215" y="20" font-size="13" font-weight="bold" fill="#1e293b" text-anchor="middle">y = (2log x + log 3)/x 与 y = a 的交点个数</text>
    <!-- 坐标轴：O(70, 145) -->
    <line x1="35" y1="145" x2="395" y2="145" stroke="#64748b" stroke-width="1.3"/>
    <line x1="70" y1="30" x2="70" y2="210" stroke="#64748b" stroke-width="1.3"/>
    <text x="387" y="160" font-size="11" fill="#475569">x</text>
    <text x="77" y="42" font-size="11" fill="#475569">y</text>
    <text x="58" y="160" font-size="11" fill="#475569">O</text>
    <!-- 曲线：x->+0 时 y->-∞；x=1/√3 时 y=0；x=e/√3 时极大值 2√3/e；x->+∞ 时 y->+0 -->
    <path d="M 85 208 C 92 175, 102 156, 110 145 C 125 120, 148 65, 175 65 C 210 65, 255 128, 380 140" fill="none" stroke="#2563eb" stroke-width="2.2"/>
    <!-- 临界线 y = 2√3/e -->
    <line x1="55" y1="65" x2="380" y2="65" stroke="#dc2626" stroke-width="1.3" stroke-dasharray="5,4"/>
    <line x1="175" y1="65" x2="175" y2="145" stroke="#94a3b8" stroke-width="1" stroke-dasharray="4,3"/>
    <circle cx="175" cy="65" r="3.5" fill="#dc2626"/>
    <circle cx="110" cy="145" r="3" fill="#2563eb"/>
    <!-- 标注 -->
    <text x="64" y="69" font-size="10" fill="#dc2626" text-anchor="end">2√3/e</text>
    <text x="175" y="160" font-size="10" fill="#475569" text-anchor="middle">e/√3</text>
    <text x="112" y="160" font-size="10" fill="#475569">1/√3</text>
    <text x="305" y="57" font-size="10" fill="#475569">a &gt; 2√3/e (0個)</text>
    <text x="305" y="79" font-size="10" fill="#dc2626">a = 2√3/e (1個)</text>
    <text x="305" y="110" font-size="10" fill="#16a34a">0 &lt; a &lt; 2√3/e (2個)</text>
    <text x="305" y="172" font-size="10" fill="#1d4ed8">a ≤ 0 (1個)</text>
  </svg>
- **【分步标准解答】**
  真数条件より $x > 0$ である。よって $x \neq 0$ より、与えられた方程式は
  $$a = \frac{2\log x + \log 3}{x}$$
  と同値である。右辺を $f(x) = \dfrac{2\log x + \log 3}{x}$（$x > 0$）とおき、微分すると
  $$f'(x) = \frac{\frac{2}{x}\cdot x - (2\log x + \log 3)\cdot 1}{x^2} = \frac{2 - (2\log x + \log 3)}{x^2} = \frac{2 - \log(3x^2)}{x^2}$$
  $f'(x) = 0$ を解くと
  $$\log(3x^2) = 2 \iff 3x^2 = e^2 \iff x = \frac{e}{\sqrt{3}} \quad (x > 0)$$
  このとき極大値は
  $$f\left(\frac{e}{\sqrt{3}}\right) = \frac{\log\left(3 \cdot \frac{e^2}{3}\right)}{\frac{e}{\sqrt{3}}} = \frac{2\sqrt{3}}{e}$$
  > 💡 讲师批注：把 $2\log x + \log 3$ 合并为 $\log(3x^2)$ 可以让解 $f'(x)=0$ 与代回求极值都无比简洁！

  また、端点の極限は：
  $$\lim_{x \to +0} f(x) = -\infty, \qquad \lim_{x \to \infty} f(x) = \lim_{x \to \infty} \left(2\cdot\frac{\log x}{x} + \frac{\log 3}{x}\right) = 0$$
  （$x > \dfrac{1}{\sqrt{3}}$ のとき $f(x) > 0$ なので、$x \to \infty$ で $y=0$ に上から近づく。）

  | $x$ | $(0)$ | $\cdots$ | $\dfrac{e}{\sqrt{3}}$ | $\cdots$ | $(\infty)$ |
  | :---: | :---: | :---: | :---: | :---: | :---: |
  | $f'(x)$ | | $+$ | $0$ | $-$ | |
  | $f(x)$ | ($-\infty$) | $\nearrow$ | $\dfrac{2\sqrt{3}}{e}$（極大） | $\searrow$ | ($+0$) |

  曲線 $y = f(x)$ と直線 $y = a$ の共有点の個数を上図より調べると、以下のようになる。
  > 💡 讲师批注：特别注意 **$a = 0$** 的边界！$y=0$ 是 $x\to\infty$ 的渐近线（右边永不相交），但在 $x = 1/\sqrt{3}$ 处与曲线有唯一交点，故 $a=0$ 归入「1 个」而非「2 个」！
- **【最终答案】**
  **$a > \dfrac{2\sqrt{3}}{e}$ 时 0 个；$a = \dfrac{2\sqrt{3}}{e}$ 或 $a \le 0$ 时 1 个；$0 < a < \dfrac{2\sqrt{3}}{e}$ 时 2 个。**

---

#### 演習問題 12-(8)
- **【原题重现与翻译】**
  - 原题：$f(x) = -e^x$ とする。実数 $b$ に対して、点 $(0, b)$ を通る曲線 $y = f(x)$ の接線の本数を求めよ。ただし、$\lim_{x \to -\infty} x e^x = 0$。
  - 中文：设 $f(x) = -e^x$。对实数 $b$，求过点 $(0, b)$ 的曲线 $y = f(x)$ 的切线条数。已知 $\lim_{x \to -\infty} x e^x = 0$。
- **【考点定位】**
  - 过定点切线条数问题 $\longrightarrow$ 转化为切点横坐标 $t$ 的方程实数解个数（并说明「切点与切线一一对应」）。
- **【图解辅助（SVG 矢量图）】**
  <svg viewBox="0 0 430 220" width="80%" xmlns="http://www.w3.org/2000/svg" style="background:#fafafa;border:1px solid #e5e7eb;border-radius:8px;">
    <text x="215" y="20" font-size="13" font-weight="bold" fill="#1e293b" text-anchor="middle">g(t) = (t - 1)e^t 与水平直线 y = b 的交点</text>
    <!-- 坐标轴：O(190, 105) -->
    <line x1="30" y1="105" x2="395" y2="105" stroke="#64748b" stroke-width="1.3"/>
    <line x1="190" y1="30" x2="190" y2="205" stroke="#64748b" stroke-width="1.3"/>
    <text x="387" y="120" font-size="11" fill="#475569">t</text>
    <text x="197" y="42" font-size="11" fill="#475569">y</text>
    <text x="178" y="120" font-size="11" fill="#475569">O</text>
    <!-- 曲线：t->-∞ 时 y->-0；t=0 时极小点 (0,-1)->(190,165)；t=1 时 (1,0)->(245,105)；t->+∞ 时 y->+∞ -->
    <path d="M 40 107.5 C 100 110, 145 140, 190 165 C 215 165, 232 132, 245 105 C 258 76, 268 50, 275 32" fill="none" stroke="#2563eb" stroke-width="2.2"/>
    <!-- 临界线 y = -1 -->
    <line x1="40" y1="165" x2="360" y2="165" stroke="#dc2626" stroke-width="1.3" stroke-dasharray="5,4"/>
    <circle cx="190" cy="165" r="3.5" fill="#dc2626"/>
    <circle cx="245" cy="105" r="3" fill="#2563eb"/>
    <!-- 标签 -->
    <text x="182" y="178" font-size="10" fill="#dc2626" text-anchor="end">-1</text>
    <text x="252" y="120" font-size="10" fill="#475569">1</text>
    <text x="300" y="72" font-size="10" fill="#1d4ed8">b ≥ 0 (1本)</text>
    <text x="300" y="138" font-size="10" fill="#16a34a">-1 &lt; b &lt; 0 (2本)</text>
    <text x="300" y="160" font-size="10" fill="#dc2626">b = -1 (1本)</text>
    <text x="300" y="192" font-size="10" fill="#475569">b &lt; -1 (0本)</text>
  </svg>
- **【分步标准解答】**
  $f'(x) = -e^x$ である。曲線 $y = f(x)$ 上の点 $(t, -e^t)$ における接線の方程式は
  $$y - (-e^t) = -e^t(x - t) \iff y = -e^t x + (t - 1)e^t$$
  この接線が点 $(0, b)$ を通るための条件は、$x = 0,\; y = b$ を代入して
  $$b = (t - 1)e^t \quad \cdots ①$$
  ここで、$f'(t) = -e^t$ は $t$ に関して単調に減少するから、異なる接点 $t$ に対して接線の傾きはすべて異なり、接線は一致しない。したがって、**求める接線の本数は、$t$ の方程式 ① の異なる実数解の個数に等しい**。
  > 💡 讲师批注：在日本描述式考题中，写明「不同切点对应不同切线（如斜率 $-e^t$ 单调，或 $f''(x) = -e^x < 0$ 严格上凸）」是拿到满分的必写采分点！

  $g(t) = (t - 1)e^t$ とおいて微分すると
  $$g'(t) = 1 \cdot e^t + (t - 1)e^t = t e^t$$
  $e^t > 0$ より $g'(t) = 0 \iff t = 0$。また端点の極限は
  $$\lim_{t \to -\infty} g(t) = \lim_{t \to -\infty} (t e^t - e^t) = 0 - 0 = 0, \qquad \lim_{t \to \infty} g(t) = +\infty$$
  （$t < 1$ で $g(t) < 0$ より、$t \to -\infty$ で $y = 0$ に下から近づく。）

  | $t$ | $(-\infty)$ | $\cdots$ | $0$ | $\cdots$ | $(\infty)$ |
  | :---: | :---: | :---: | :---: | :---: | :---: |
  | $g'(t)$ | | $-$ | $0$ | $+$ | |
  | $g(t)$ | ($-0$) | $\searrow$ | $-1$（極小） | $\nearrow$ | ($+\infty$) |

  曲線 $y = g(t)$ と水平直線 $y = b$ の共有点の個数を上図より読み取ると、求める接線の本数を得る。
- **【最终答案】**
  **$b < -1$ 时 0 条；$b = -1$ 或 $b \ge 0$ 时 1 条；$-1 < b < 0$ 时 2 条。**
