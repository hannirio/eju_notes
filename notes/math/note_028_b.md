# 《EJU 教材全解与备课讲义》数学 028-b（P411–P420）

> **对应源文件**：`work_math/ocr_md/ocr_028_p406-420.md`（后半部分：第十一章《微分積分》之「体積・曲線の長さ」演習問題 18–19，以及第十二章《確率と統計推測》之「順列」演習問題 1 (1)–(5)；前半部分 P406–P410 见 `note_028_a.md`）
> **视觉核对参考图**：`work_math/ref_imgs/page_0411.jpg` – `page_0420.jpg`（对应教材印制页码 P410–P419）

---

## 一、国内高中基础知识点唤醒与 EJU 考纲差异对比

本讲义承接 `note_028_a.md`，前半部分完成日本高中 **数学Ⅲ（積分法の応用：体積・曲線の長さ）** 的收官，后半部分正式开启 **数学A（場合の数と確率：順列・円順列・じゅず順列・重複順列）** 的系统学习。

### 1.1 第十一章收官：定积分求体积与曲线弧长

1. **一般立体的体积（截面积积分）**：
   设立体夹在垂直于 $x$ 轴的两平面 $x = a,\; x = b$（$a < b$）之间，过坐标 $x$ 且垂直于 $x$ 轴的截面面积为 $S(x)$，则体积为
   $$V = \int_a^b S(x)\,dx$$
2. **绕 $x$ 轴旋转体的体积**：
   - **单曲线**：由 $y = f(x)$、$x$ 轴及 $x = a,\; x = b$ 围成的区域绕 $x$ 轴旋转一周：
     $$V = \pi \int_a^b \{f(x)\}^2\,dx = \pi \int_a^b y^2\,dx$$
   - **双曲线（同号）**：若在 $[a, b]$ 上 $f(x)$ 与 $g(x)$ 同号（$f(x)g(x) \ge 0$），则所围区域绕 $x$ 轴旋转一周：
     $$V = \pi \int_a^b \left|\{f(x)\}^2 - \{g(x)\}^2\right|\,dx$$
   - **易错警报（跨 $x$ 轴区域）**：若区域跨越 $x$ 轴（即 $f(x)$ 与 $g(x)$ 异号），**严禁直接套用双曲线相减公式**！必须将下方图形翻折到上方（取绝对值 $|f(x)|$ 与 $|g(x)|$），以每一处离 $x$ 轴最远的曲线作为外半径，截面为实心圆而非圆环（详见演習問題 18-(3)）。
3. **绕 $y$ 轴旋转体的体积**：
   由曲线 $x = g(y)$、$y$ 轴及 $y = c,\; y = d$（$c < d$）围成的区域绕 $y$ 轴旋转一周：
   $$V = \pi \int_c^d x^2\,dy$$
4. **曲线的长度（弧长公式）**：
   - **参数方程（媒介変数表示）**：$x = f(t),\; y = g(t)$（$\alpha \le t \le \beta$）
     $$L = \int_\alpha^\beta \sqrt{\left(\frac{dx}{dt}\right)^2 + \left(\frac{dy}{dt}\right)^2}\,dt = \int_\alpha^\beta \sqrt{\{f'(t)\}^2 + \{g'(t)\}^2}\,dt$$
   - **直角坐标（直交座標）**：$y = f(x)$（$a \le x \le b$）
     $$L = \int_a^b \sqrt{1 + \left(\frac{dy}{dx}\right)^2}\,dx = \int_a^b \sqrt{1 + \{f'(x)\}^2}\,dx$$

> ⚠️ **教材勘误提示（P415 / 教材印制页 P414）**：
> 原教材在「曲線の長さ [2] 直交座標」中将公式误印为 $L = \int_\alpha^\beta \sqrt{1 + (\frac{dy}{dx})^2}\,dt = \int_\alpha^\beta \sqrt{1 + [f'(x)]^2}\,dt$。正确写法积分上下限应为 $a \to b$，积分微元应为 $dx$，即 $L = \displaystyle\int_a^b \sqrt{1 + \{f'(x)\}^2}\,dx$。

### 1.2 第十二章开篇：排列、圆排列、项链排列与重复排列

1. **排列（順列）**：从 $n$ 个不同元素中取 $r$ 个排成一列（$0 \le r \le n$）：
   $${}_n\mathrm{P}_r = n(n-1)(n-2)\cdots(n-r+1) = \frac{n!}{(n-r)!}$$
   特别地，${}_n\mathrm{P}_n = n!$，并规定 $0! = 1,\; {}_n\mathrm{P}_0 = 1$。
   > ⚠️ **教材勘误提示（P417 / 教材印制页 P416）**：
   > 原教材「[1.1] 順列」第二行将全排列误印为「特に、${}_n\mathrm{P}_r = n(n-1)(n-2)\cdots 3\cdot 2\cdot 1$」，此处下标应为 ${}_n\mathrm{P}_n$（同页下方解説部分印制正确）。
2. **圆排列（円順列）**：将 $n$ 个不同元素排成一个圆圈（旋转后重合视为同一种）：
   $$\frac{{}_n\mathrm{P}_n}{n} = (n - 1)!$$
   若从 $n$ 个不同元素中取 $r$ 个做圆排列，总数为 $\dfrac{{}_n\mathrm{P}_r}{r} = {}_n\mathrm{C}_r \cdot (r - 1)!$。
3. **项链排列（じゅず順列 / 数珠順列）**：将 $n$ 个不同元素穿成项链（**旋转或空间翻转**后重合均视为同一种，当 $n \ge 3$ 时）：
   $$\frac{(n - 1)!}{2}$$
4. **重复排列（重複順列）**：从 $n$ 个不同元素中允许重复地取 $r$ 个排成一列：
   $$n^r$$

### 1.3 国内高中 vs. 日本 EJU 考纲差异对比

| 对比维度 | 国内高中习惯 | 日本 EJU 习惯 | 备课/应试提醒 |
| :--- | :--- | :--- | :--- |
| **旋转体体积与弧长** | 新高考已完全删除，仅在大学高数出现 | **理系数学（コース2）必考核心模块** | 必须熟练掌握绕 $x$ 轴、绕 $y$ 轴、跨轴旋转及星形线等弧长计算 |
| **排列记号** | 用 $\mathrm{A}_n^r$ 表示排列数 | 用 **${}_n\mathrm{P}_r$** 表示排列数（Permutation） | 书写与读法务必切换为 ${}_n\mathrm{P}_r$，切勿写成 $\mathrm{A}_n^r$ |
| **项链排列（じゅず順列）** | 仅作竞赛拓展，较少考 | **EJU 数学A 常规基础考点** | 牢记关键词「首飾り（项链）」「腕輪（手镯）」「じゅず（念珠）」需除以 $2$ |
| **区域涂色与字典序** | 常规基础题，常考复杂图 | **EJU 填空高频题**（逻辑清晰、重步步推导） | 涂色题按「邻接度最高」的区块优先排顺序，可大幅减少分类讨论 |

---

## 二、日文核心词汇与公式假名注音

### 2.1 本部分日文核心词汇

- 体積（たいせき / taiseki） — 体积
- 断面積（だんめんせき / danmenseki） — 截面积（横截面积）
- 切り口（きりくち / kirikuchi） — 切口、截面
- 回転体（かいてんたい / kaitentai） — 旋转体
- $x$ 軸の周り（エックスじくのまわり / ekkusu-jiku no mawari） — 绕 $x$ 轴
- 曲線の長さ（きょくせんのながさ / kyokusen no nagasa） — 曲线的长度（弧长）
- アステロイド（あすてろいど / asuteroido） — 星形线（内摆线）
- 順列（じゅんれつ / junretsu） — 排列
- 階乗（かいじょう / kaijou） — 阶乘
- 円順列（えんじゅんれつ / enjunretsu） — 圆排列
- じゅず順列（じゅずじゅんれつ / juzu junretsu） — 项链排列（念珠排列）
- 首飾り（くびかざり / kubikazari） — 项链
- 重複順列（ちょうふくじゅんれつ / choufuku junretsu） — 重复排列
- 隣り合う（となりあう / tonariau） — 相邻
- 両端（りょうたん / ryoutan） — 两端
- アルファベット順（あるふぁべっとじゅん / arufabetto-jun） — 字母顺序（字典序）
- 塗り分ける（ぬりわける / nuriwakeru） — 涂色区分

### 2.2 核心公式的日本课堂口语读法

1. **绕 $x$ 轴旋转体体积** $V = \pi\displaystyle\int_a^b y^2\,dx$
   - 课堂读法：**ブイ イコール パイ インテグラル エーから ビーまでの ワイ の にじょう ディーエックス**
2. **曲线弧长公式（直角坐标）** $L = \displaystyle\int_a^b \sqrt{1 + \{f'(x)\}^2}\,dx$
   - 课堂读法：**エル イコール インテグラル エーから ビーまでの ルート いち たす エフダッシュ エックス の にじょう ディーエックス**
3. **排列数** ${}_n\mathrm{P}_r = \dfrac{n!}{(n - r)!}$
   - 课堂读法：**エヌ ピー アール イコール かっこ エヌ ひく アール かっことじ の かいじょう ぶんの エヌ の かいじょう**（或读作 **ピー の エヌ、アール**）
4. **圆排列与项链排列** $(n - 1)!$、$\dfrac{(n - 1)!}{2}$
   - 课堂读法：**かっこ エヌ ひく いち かっことじ の かいじょう** / **にぶんの かっこ エヌ ひく いち かっことじ の かいじょう**

---

## 三、逐题深度解析（不可跳步）

---

### 第十一章 演習問題 18（定積分の応用：体積）

#### 演習問題 18-(1)
- **【原题重现与翻译】**
  - 原题：次の曲線や座標軸で囲まれた部分を $x$ 軸の周りに $1$ 回転させてできる立体の体積 $V$ を求めよ。
    - [1] $y = 1 - \sqrt{x},\; x$ 軸，$y$ 軸
    - [2] $y = 1 + \cos x\; (-\pi \le x \le \pi),\; x$ 軸
  - 中文：求由下列曲线与坐标轴围成的部分绕 $x$ 轴旋转一周所形成立体的体积 $V$。
    - [1] $y = 1 - \sqrt{x}$、$x$ 轴、$y$ 轴
    - [2] $y = 1 + \cos x\; (-\pi \le x \le \pi)$、$x$ 轴
- **【考点定位】**
  - 绕 $x$ 轴旋转体体积的基本公式 $V = \pi\int_a^b y^2\,dx$ + 幂函数积分与三角函数降幂（倍角公式）积分。
- **【图解辅助（SVG 矢量图）】**

<svg viewBox="0 0 460 190" width="460" height="190" xmlns="http://www.w3.org/2000/svg" style="background:#fafafa;border:1px solid #e0e0e0;border-radius:6px;">
  <style>
    .axis { stroke: #333; stroke-width: 1.3; }
    .curve { fill: none; stroke: #2471a3; stroke-width: 2.2; }
    .area { fill: #d6eaf8; fill-opacity: 0.7; }
    .lbl { font: 11.5px sans-serif; fill: #2c3e50; }
    .math { font: italic 11.5px serif; fill: #2c3e50; }
  </style>
  <!-- Left: [1] y = 1 - sqrt(x) -->
  <text x="15" y="20" class="lbl" font-weight="bold">[1] y = 1 - √x（绕 x 轴）</text>
  <line x1="25" y1="145" x2="195" y2="145" class="axis"/>
  <polygon points="195,145 188,141 188,149" fill="#333"/>
  <line x1="50" y1="168" x2="50" y2="35" class="axis"/>
  <polygon points="50,35 46,42 54,42" fill="#333"/>
  <path d="M 50,55 Q 80,125 160,145 L 50,145 Z" class="area"/>
  <path d="M 50,55 Q 80,125 160,145" class="curve"/>
  <text x="188" y="160" class="math">x</text>
  <text x="57" y="44" class="math">y</text>
  <text x="36" y="160" class="lbl">O</text>
  <text x="36" y="60" class="lbl">1</text>
  <text x="156" y="160" class="lbl">1</text>
  <text x="88" y="105" class="lbl" fill="#1b4f72">V = π/6</text>
  <!-- Right: [2] y = 1 + cos x -->
  <text x="235" y="20" class="lbl" font-weight="bold">[2] y = 1 + cos x（偶函数对称）</text>
  <line x1="230" y1="145" x2="445" y2="145" class="axis"/>
  <polygon points="445,145 438,141 438,149" fill="#333"/>
  <line x1="335" y1="168" x2="335" y2="35" class="axis"/>
  <polygon points="335,35 331,42 339,42" fill="#333"/>
  <path d="M 255,145 C 285,145 305,55 335,55 C 365,55 385,145 415,145 Z" class="area"/>
  <path d="M 255,145 C 285,145 305,55 335,55 C 365,55 385,145 415,145" class="curve"/>
  <text x="438" y="160" class="math">x</text>
  <text x="342" y="44" class="math">y</text>
  <text x="322" y="160" class="lbl">O</text>
  <text x="340" y="62" class="lbl">2</text>
  <text x="245" y="160" class="lbl">-π</text>
  <text x="410" y="160" class="lbl">π</text>
  <text x="358" y="128" class="lbl" fill="#1b4f72">V = 3π²</text>
</svg>

- **【分步标准解答】**
  - **[1] $y = 1 - \sqrt{x}$ の回転体**：
    曲線と $x$ 軸との交点は $1 - \sqrt{x} = 0$ より $x = 1$。
    よって積分区間は $0 \le x \le 1$ であるから、
    $$V = \pi \int_0^1 (1 - \sqrt{x})^2\,dx = \pi \int_0^1 \left(1 - 2x^{\frac{1}{2}} + x\right)\,dx$$
    $$= \pi \left[x - 2 \cdot \frac{2}{3}x^{\frac{3}{2}} + \frac{1}{2}x^2\right]_0^1 = \pi \left(1 - \frac{4}{3} + \frac{1}{2}\right) = \frac{\pi}{6}$$
    > 💡 讲师批注：把 $\sqrt{x}$ 改写成幂形式 $x^{1/2}$，用 $\int x^n dx = \frac{1}{n+1}x^{n+1}$ 积分最不易漏系数 $\frac{2}{3}$。

  - **[2] $y = 1 + \cos x$ の回転体**：
    $y^2 = (1 + \cos x)^2$ は偶関数（$y$ 軸に関して対称）であるから、積分区間 $[-\pi, \pi]$ を $[0, \pi]$ の $2$ 倍に書き換えると、
    $$V = \pi \int_{-\pi}^\pi (1 + \cos x)^2\,dx = 2\pi \int_0^\pi (1 + 2\cos x + \cos^2 x)\,dx$$
    半角の公式 $\cos^2 x = \dfrac{1 + \cos 2x}{2}$ を用いると、
    $$V = 2\pi \int_0^\pi \left(1 + 2\cos x + \frac{1 + \cos 2x}{2}\right)\,dx = 2\pi \int_0^\pi \left(\frac{3}{2} + 2\cos x + \frac{1}{2}\cos 2x\right)\,dx$$
    $$= 2\pi \left[\frac{3}{2}x + 2\sin x + \frac{1}{4}\sin 2x\right]_0^\pi = 2\pi \left(\frac{3}{2}\pi + 0 + 0\right) = 3\pi^2$$
    > 💡 讲师批注：在 $[0, \pi]$ 上，$\sin x$ 和 $\sin 2x$ 在两端点处全为 $0$，真正贡献积分值的只有常数项 $\frac{3}{2}$！

- **【最终答案】**
  - **[1] $V = \dfrac{\pi}{6}$**
  - **[2] $V = 3\pi^2$**

---

#### 演習問題 18-(2)
- **【原题重现与翻译】**
  - 原题：次の図形を $x$ 軸の周りに $1$ 回転させてできる立体の体積 $V$ を求めよ。
    - [1] 放物線 $y = -x^2 + 4x$ と直線 $y = x$ で囲まれた図形。
    - [2] 円 $x^2 + (y - 2)^2 = 4$ の周及び内部
  - 中文：求将下列图形绕 $x$ 轴旋转一周所形成立体的体积 $V$。
    - [1] 由抛物线 $y = -x^2 + 4x$ 与直线 $y = x$ 围成的图形。
    - [2] 圆 $x^2 + (y - 2)^2 = 4$ 的圆周及其内部。
- **【考点定位】**
  - 双曲线间（圆环截面）绕 $x$ 轴旋转体体积 $V = \pi\int_a^b (y_{\text{上}}^2 - y_{\text{下}}^2)\,dx$ + 利用圆面积求定积分（无需三角换元）。
- **【图解辅助（SVG 矢量图）】**

<svg viewBox="0 0 460 200" width="460" height="200" xmlns="http://www.w3.org/2000/svg" style="background:#fafafa;border:1px solid #e0e0e0;border-radius:6px;">
  <style>
    .axis { stroke: #333; stroke-width: 1.3; }
    .curve { fill: none; stroke: #2471a3; stroke-width: 2.2; }
    .lin { stroke: #c0392b; stroke-width: 2; }
    .area { fill: #d6eaf8; fill-opacity: 0.7; }
    .lbl { font: 11.5px sans-serif; fill: #2c3e50; }
    .math { font: italic 11.5px serif; fill: #2c3e50; }
  </style>
  <!-- Left: [1] parabola & line -->
  <text x="14" y="20" class="lbl" font-weight="bold">[1] 放物線と直線</text>
  <line x1="25" y1="160" x2="210" y2="160" class="axis"/>
  <polygon points="210,160 203,156 203,164" fill="#333"/>
  <line x1="45" y1="180" x2="45" y2="32" class="axis"/>
  <polygon points="45,32 41,39 49,39" fill="#333"/>
  <!-- x in [0,4] -> [45, 185] (35px/u), y in [0,4] -> [160, 40] (30px/u) -->
  <!-- (0,0)=(45,160), (2,4)=(115,40), (3,3)=(150,70), (4,0)=(185,160) -->
  <path d="M 45,160 Q 115,-20 150,70 L 45,160 Z" class="area"/>
  <path d="M 45,160 Q 115,-20 185,160" class="curve"/>
  <line x1="35" y1="168.5" x2="175" y2="48.5" class="lin"/>
  <circle cx="150" cy="70" r="3" fill="#c0392b"/>
  <text x="202" y="175" class="math">x</text>
  <text x="52" y="42" class="math">y</text>
  <text x="33" y="175" class="lbl">O</text>
  <text x="146" y="175" class="lbl">3</text>
  <line x1="150" y1="70" x2="150" y2="160" stroke="#7f8c8d" stroke-dasharray="3,3"/>
  <text x="155" y="72" class="lbl">(3, 3)</text>
  <text x="68" y="88" class="lbl" fill="#1b4f72">V=108π/5</text>
  <!-- Right: [2] circle x^2 + (y-2)^2 = 4 -->
  <text x="240" y="20" class="lbl" font-weight="bold">[2] 円 x² + (y - 2)² = 4</text>
  <line x1="235" y1="160" x2="445" y2="160" class="axis"/>
  <polygon points="445,160 438,156 438,164" fill="#333"/>
  <line x1="340" y1="185" x2="340" y2="28" class="axis"/>
  <polygon points="340,28 336,35 344,35" fill="#333"/>
  <!-- Circle centered at (340, 104), radius 56 -->
  <circle cx="340" cy="104" r="56" fill="#d6eaf8" fill-opacity="0.7" stroke="#2471a3" stroke-width="2.2"/>
  <circle cx="340" cy="104" r="2.8" fill="#c0392b"/>
  <text x="438" y="175" class="math">x</text>
  <text x="347" y="38" class="math">y</text>
  <text x="326" y="175" class="lbl">O</text>
  <text x="346" y="108" class="lbl" fill="#c0392b">(0, 2)</text>
  <text x="398" y="175" class="lbl">2</text>
  <text x="276" y="175" class="lbl">-2</text>
  <text x="345" y="45" class="lbl">4</text>
  <text x="398" y="76" class="lbl" fill="#2471a3">y₁=2+√(4-x²)</text>
  <text x="398" y="138" class="lbl" fill="#2471a3">y₂=2-√(4-x²)</text>
</svg>

- **【分步标准解答】**
  - **[1] 放物線 $y = -x^2 + 4x$ と直線 $y = x$**：
    交点の $x$ 座標を求める：
    $$-x^2 + 4x = x \implies x^2 - 3x = 0 \implies x(x - 3) = 0 \implies x = 0,\; 3$$
    区間 $0 \le x \le 3$ において、$-x^2 + 4x \ge x \ge 0$ であるから、求める体積 $V$ は
    $$V = \pi \int_0^3 \left\{(-x^2 + 4x)^2 - x^2\right\}\,dx = \pi \int_0^3 (x^4 - 8x^3 + 16x^2 - x^2)\,dx$$
    $$= \pi \int_0^3 (x^4 - 8x^3 + 15x^2)\,dx = \pi \left[\frac{1}{5}x^5 - 2x^4 + 5x^3\right]_0^3$$
    $$= \pi \left(\frac{243}{5} - 162 + 135\right) = \pi \left(\frac{243}{5} - 27\right) = \frac{108}{5}\pi$$
    > 💡 讲师批注：切勿写成 $\pi\int_0^3 \{(-x^2+4x) - x\}^2\,dx$！圆环截面积是 $\pi(R^2 - r^2)$，不是 $\pi(R - r)^2$，这是初学旋转体最常踩的坑！

  - **[2] 円 $x^2 + (y - 2)^2 = 4$ の周及び内部**：
    円の方程式を $y$ について解くと、$-2 \le x \le 2$ の範囲で、
    - 上側の半円：$y_1 = 2 + \sqrt{4 - x^2}$
    - 下側の半円：$y_2 = 2 - \sqrt{4 - x^2}$
    $y_1 \ge y_2 \ge 0$ であり、図形は $y$ 軸に関して対称であるから、
    $$V = \pi \int_{-2}^2 (y_1^2 - y_2^2)\,dx = 2\pi \int_0^2 (y_1 + y_2)(y_1 - y_2)\,dx$$
    ここで $y_1 + y_2 = 4$、$y_1 - y_2 = 2\sqrt{4 - x^2}$ であるから、
    $$V = 2\pi \int_0^2 4 \cdot 2\sqrt{4 - x^2}\,dx = 16\pi \int_0^2 \sqrt{4 - x^2}\,dx$$
    定積分 $\displaystyle\int_0^2 \sqrt{4 - x^2}\,dx$ は半径 $2$ の円の $\dfrac{1}{4}$ の面積に等しいから、
    $$\int_0^2 \sqrt{4 - x^2}\,dx = \frac{1}{4} \cdot \pi \cdot 2^2 = \pi$$
    よって、
    $$V = 16\pi \cdot \pi = 16\pi^2$$
    > 💡 讲师批注：先用平方差 $y_1^2 - y_2^2 = (y_1 + y_2)(y_1 - y_2)$ 化简，再用「四分之一圆面积」直接读出 $\int_0^2 \sqrt{4-x^2}\,dx = \pi$，无需繁琐三角换元！亦可用**帕普斯-古尔丁定理（パップス＝ギュルダンの定理）**秒验：$V = (\text{圆面积 } 4\pi) \times (\text{圆心轨迹周长 } 2\pi \cdot 2) = 16\pi^2$！

- **【最终答案】**
  - **[1] $V = \dfrac{108}{5}\pi$**
  - **[2] $V = 16\pi^2$**

---

#### 演習問題 18-(3)
- **【原题重现与翻译】**
  - 原题：放物線 $y = x^2 - 2x$ と直線 $y = -x + 2$ で囲まれた部分を $x$ 軸の周りに $1$ 回転させてできる立体の体積 $V$ を求めよ。
  - 中文：求由抛物线 $y = x^2 - 2x$ 与直线 $y = -x + 2$ 围成的部分绕 $x$ 轴旋转一周所形成立体的体积 $V$。
- **【考点定位】**
  - **跨 $x$ 轴区域**绕 $x$ 轴旋转体体积（高难必考易错题：将 $x$ 轴下方部分对称翻折到上方比较绝对值大小）。
- **【图解辅助（SVG 矢量图）】**
  将 $0 \le x \le 2$ 中处于 $x$ 轴下方的抛物线 $y = x^2 - 2x$ 翻折到 $x$ 轴上方得虚线 $y = 2x - x^2$，它与直线 $y = -x + 2$ 交于 $x = 1$：

<svg viewBox="0 0 420 220" width="420" height="220" xmlns="http://www.w3.org/2000/svg" style="background:#fafafa;border:1px solid #e0e0e0;border-radius:6px;">
  <style>
    .axis { stroke: #333; stroke-width: 1.4; }
    .par { fill: none; stroke: #2471a3; stroke-width: 2.2; }
    .flip { fill: none; stroke: #8e44ad; stroke-width: 1.8; stroke-dasharray: 5,3; }
    .lin { stroke: #c0392b; stroke-width: 2; }
    .a1 { fill: #d6eaf8; fill-opacity: 0.65; }
    .a2 { fill: #fdebd0; fill-opacity: 0.7; }
    .a3 { fill: #e8daef; fill-opacity: 0.75; }
    .lbl { font: 11.5px sans-serif; fill: #2c3e50; }
    .math { font: italic 11.5px serif; fill: #2c3e50; }
  </style>
  <!-- Origin (150, 145), x scale: 80px/u, y scale: 35px/u -->
  <!-- (-1,3)=(70,40), (0,2)=(150,75), (1,1)=(230,110), (1,-1)=(230,180), (2,0)=(310,145) -->
  <line x1="30" y1="145" x2="395" y2="145" class="axis"/>
  <polygon points="395,145 387,141 387,149" fill="#333"/>
  <line x1="150" y1="205" x2="150" y2="18" class="axis"/>
  <polygon points="150,18 146,26 154,26" fill="#333"/>
  <!-- Shaded regions for rotation profile -->
  <!-- [-1, 0]: washer between line and parabola -->
  <path d="M 70,40 L 150,75 L 150,145 Q 110,120 70,40 Z" class="a1"/>
  <!-- [0, 1]: solid disk up to line -->
  <path d="M 150,75 L 230,110 L 230,145 L 150,145 Z" class="a2"/>
  <!-- [1, 2]: solid disk up to flipped parabola -->
  <path d="M 230,110 Q 270,110 310,145 L 230,145 Z" class="a3"/>
  <!-- Original parabola y = x^2 - 2x -->
  <path d="M 58,15 Q 150,215 230,180 Q 275,180 330,115" class="par"/>
  <!-- Flipped parabola y = 2x - x^2 on [0, 2] -->
  <path d="M 150,145 Q 230,75 310,145" class="flip"/>
  <!-- Line y = -x + 2 -->
  <line x1="50" y1="31.25" x2="350" y2="162.5" class="lin"/>
  <!-- Vertical guides -->
  <line x1="70" y1="40" x2="70" y2="145" stroke="#7f8c8d" stroke-dasharray="3,3"/>
  <line x1="230" y1="110" x2="230" y2="145" stroke="#7f8c8d" stroke-dasharray="3,3"/>
  <circle cx="70" cy="40" r="3.2" fill="#c0392b"/>
  <circle cx="230" cy="110" r="3.5" fill="#8e44ad"/>
  <circle cx="310" cy="145" r="3.2" fill="#c0392b"/>
  <text x="388" y="161" class="math">x</text>
  <text x="157" y="28" class="math">y</text>
  <text x="136" y="161" class="lbl">O</text>
  <text x="61" y="161" class="lbl">-1</text>
  <text x="226" y="161" class="lbl">1</text>
  <text x="307" y="161" class="lbl">2</text>
  <text x="76" y="37" class="lbl">(-1, 3)</text>
  <text x="236" y="102" class="lbl" fill="#8e44ad">翻折交点 (1, 1)</text>
  <text x="172" y="196" class="math" fill="#2471a3">y = x² - 2x</text>
  <text x="285" y="75" class="math" fill="#8e44ad">y = -(x² - 2x)</text>
  <text x="295" y="128" class="math" fill="#c0392b">y = -x + 2</text>
</svg>

- **【分步标准解答】**
  1. **交点と $x$ 軸との位置関係の確認**：
     放物線と直線の交点の $x$ 座標は、
     $$x^2 - 2x = -x + 2 \implies x^2 - x - 2 = 0 \implies (x + 1)(x - 2) = 0 \implies x = -1,\; 2$$
     また、放物線 $y = x(x - 2)$ は $x = 0,\; 2$ で $x$ 軸と交わり、$0 \le x \le 2$ では $x$ 軸の下側（$y \le 0$）にある。

  2. **$x$ 軸の下側部分を対称折り返して外半径を決定する**：
     図形が $x$ 軸をまたぐ区間 $0 \le x \le 2$ においては、回転体の断面（$x$ 軸に垂直な切り口）は穴のない円板となり、その半径は直線 $y = -x + 2$ と折り返した放物線 $y = -(x^2 - 2x) = -x^2 + 2x$ のうち**大きい方**となる。
     両者の差をとると、
     $$(-x + 2) - (-x^2 + 2x) = x^2 - 3x + 2 = (x - 1)(x - 2)$$
     - $0 \le x \le 1$ では $(x - 1)(x - 2) \ge 0$ より、$-x + 2 \ge -x^2 + 2x$（直線が外側）
     - $1 \le x \le 2$ では $(x - 1)(x - 2) \le 0$ より、$-x^2 + 2x \ge -x + 2$（放物線が外側）
     - $-1 \le x \le 0$ では両曲線とも $y \ge 0$ で $-x + 2 \ge x^2 - 2x \ge 0$（断面は円環）

     > 💡 讲师批注：这就是跨 $x$ 轴旋转体最核心的一步！在 $[0, 2]$ 上，由于区域包含 $x$ 轴上的线段，旋转后内部是**完全实心的**，且在 $x = 1$ 处外轮廓从「直线」切换为「翻折后的抛物线」，千万不能漏掉这个切换点！

  3. **区間ごとに定積分して体積 $V$ を計算する**：
     $$V = \pi \int_{-1}^0 \left\{(-x + 2)^2 - (x^2 - 2x)^2\right\}\,dx + \pi \int_0^1 (-x + 2)^2\,dx + \pi \int_1^2 (-x^2 + 2x)^2\,dx$$
     第 $1$ 項の前半と第 $2$ 項を合わせると、
     $$V = \pi \int_{-1}^1 (-x + 2)^2\,dx - \pi \int_{-1}^0 (x^2 - 2x)^2\,dx + \pi \int_1^2 (x^2 - 2x)^2\,dx$$
     それぞれの定積分を計算する：
     - $\displaystyle\int_{-1}^1 (-x + 2)^2\,dx = \left[-\frac{1}{3}(-x + 2)^3\right]_{-1}^1 = -\frac{1}{3}(1^3 - 3^3) = \frac{26}{3}$
     - 原始関数 $F(x) = \displaystyle\int (x^2 - 2x)^2\,dx = \int (x^4 - 4x^3 + 4x^2)\,dx = \frac{1}{5}x^5 - x^4 + \frac{4}{3}x^3$ とおくと、
       - $F(0) = 0$
       - $F(-1) = -\dfrac{1}{5} - 1 - \dfrac{4}{3} = -\dfrac{38}{15} \implies \displaystyle\int_{-1}^0 (x^2 - 2x)^2\,dx = 0 - \left(-\frac{38}{15}\right) = \frac{38}{15}$
       - $F(1) = \dfrac{1}{5} - 1 + \dfrac{4}{3} = \dfrac{8}{15}$
       - $F(2) = \dfrac{32}{5} - 16 + \dfrac{32}{3} = \dfrac{16}{15} \implies \displaystyle\int_1^2 (x^2 - 2x)^2\,dx = \frac{16}{15} - \frac{8}{15} = \frac{8}{15}$

     よって、
     $$V = \pi \left(\frac{26}{3} - \frac{38}{15} + \frac{8}{15}\right) = \pi \cdot \frac{130 - 38 + 8}{15} = \frac{100}{15}\pi = \frac{20}{3}\pi$$
     > 💡 讲师批注：自检小技巧——由于抛物线 $y = (x-1)^2 - 1$ 关于 $x = 1$ 对称，必有 $\int_1^2 (x^2-2x)^2\,dx = \int_0^1 (x^2-2x)^2\,dx = F(1) = \frac{8}{15}$，与 $F(2) - F(1) = \frac{16}{15} - \frac{8}{15} = \frac{8}{15}$ 完全一致！

- **【最终答案】**
  **$V = \dfrac{20}{3}\pi$**

---

#### 演習問題 18-(4)
- **【原题重现与翻译】**
  - 原题：次の回転体の体積 $V$ を求めよ。
    - [1] 楕円 $\dfrac{x^2}{9} + \dfrac{y^2}{4} = 1$ を $y$ 軸の周りに $1$ 回転させてできる回転体。
    - [2] 曲線 $C : y = \log(x^2 + 1)\; (0 \le x \le 1)$ と直線 $y = \log 2$、及び $y$ 軸で囲まれた部分を $y$ 軸の周りに $1$ 回転させてできる回転体。
  - 中文：求下列旋转体的体积 $V$。
    - [1] 将椭圆 $\dfrac{x^2}{9} + \dfrac{y^2}{4} = 1$ 绕 $y$ 轴旋转一周所形成的旋转体。
    - [2] 将由曲线 $C : y = \log(x^2 + 1)\; (0 \le x \le 1)$、直线 $y = \log 2$ 以及 $y$ 轴所围成的部分绕 $y$ 轴旋转一周所形成的旋转体。
- **【考点定位】**
  - 绕 $y$ 轴旋转体体积公式 $V = \pi\int_c^d x^2\,dy$（将 $x^2$ 直接表示为 $y$ 的函数）。
- **【图解辅助（SVG 矢量图）】**

<svg viewBox="0 0 460 190" width="460" height="190" xmlns="http://www.w3.org/2000/svg" style="background:#fafafa;border:1px solid #e0e0e0;border-radius:6px;">
  <style>
    .axis { stroke: #333; stroke-width: 1.3; }
    .curve { fill: none; stroke: #2471a3; stroke-width: 2.2; }
    .area { fill: #d6eaf8; fill-opacity: 0.7; }
    .lbl { font: 11.5px sans-serif; fill: #2c3e50; }
    .math { font: italic 11.5px serif; fill: #2c3e50; }
  </style>
  <!-- Left: [1] ellipse around y-axis -->
  <text x="14" y="20" class="lbl" font-weight="bold">[1] 楕円 x²/9 + y²/4 = 1（绕 y 轴）</text>
  <line x1="25" y1="108" x2="210" y2="108" class="axis"/>
  <polygon points="210,108 203,104 203,112" fill="#333"/>
  <line x1="115" y1="180" x2="115" y2="32" class="axis"/>
  <polygon points="115,32 111,39 119,39" fill="#333"/>
  <ellipse cx="115" cy="108" rx="68" ry="45" fill="#d6eaf8" fill-opacity="0.65" stroke="#2471a3" stroke-width="2.2"/>
  <text x="202" y="123" class="math">x</text>
  <text x="122" y="42" class="math">y</text>
  <text x="186" y="123" class="lbl">3</text>
  <text x="34" y="123" class="lbl">-3</text>
  <text x="120" y="58" class="lbl">2</text>
  <text x="120" y="167" class="lbl">-2</text>
  <text x="130" y="96" class="lbl" fill="#1b4f72">V = 24π</text>
  <!-- Right: [2] y = log(x^2+1) around y-axis -->
  <text x="235" y="20" class="lbl" font-weight="bold">[2] y = log(x² + 1)（绕 y 轴）</text>
  <line x1="240" y1="158" x2="440" y2="158" class="axis"/>
  <polygon points="440,158 433,154 433,162" fill="#333"/>
  <line x1="280" y1="178" x2="280" y2="32" class="axis"/>
  <polygon points="280,32 276,39 284,39" fill="#333"/>
  <!-- (0,0)=(280,158), (1, log2)=(395, 65) -->
  <path d="M 280,158 Q 335,155 395,65 L 280,65 Z" class="area"/>
  <path d="M 280,158 Q 335,155 395,65" class="curve"/>
  <line x1="265" y1="65" x2="420" y2="65" stroke="#c0392b" stroke-dasharray="4,3"/>
  <line x1="395" y1="65" x2="395" y2="158" stroke="#7f8c8d" stroke-dasharray="3,3"/>
  <text x="433" y="173" class="math">x</text>
  <text x="287" y="42" class="math">y</text>
  <text x="266" y="173" class="lbl">O</text>
  <text x="391" y="173" class="lbl">1</text>
  <text x="242" y="69" class="lbl" fill="#c0392b">log 2</text>
  <text x="294" y="102" class="lbl" fill="#1b4f72">x² = eʸ - 1</text>
</svg>

- **【分步标准解答】**
  - **[1] 楕円の $y$ 軸回転体**：
    楕円の方程式から $x^2$ を $y$ で表すと、
    $$x^2 = 9\left(1 - \frac{y^2}{4}\right) \quad (-2 \le y \le 2)$$
    $x$ 軸に関する対称性より、
    $$V = \pi \int_{-2}^2 x^2\,dy = 2\pi \int_0^2 9\left(1 - \frac{y^2}{4}\right)\,dy = 18\pi \left[y - \frac{y^3}{12}\right]_0^2$$
    $$= 18\pi \left(2 - \frac{8}{12}\right) = 18\pi \cdot \frac{4}{3} = 24\pi$$
    > 💡 讲师批注：椭球体体积速记验算公式为 $V = \dfrac{4}{3}\pi a^2 b$（绕半轴 $b$ 旋转），此处 $a = 3,\; b = 2$，得 $\dfrac{4}{3}\pi \cdot 9 \cdot 2 = 24\pi$，瞬间验算完毕！

  - **[2] $y = \log(x^2 + 1)$ の $y$ 軸回転体**：
    $0 \le x \le 1$ において $y = \log(x^2 + 1)$ は単調に増加し、$x = 0$ のとき $y = 0$、$x = 1$ のとき $y = \log 2$ である。
    $y = \log(x^2 + 1)$ を $x^2$ について解くと、
    $$x^2 + 1 = e^y \implies x^2 = e^y - 1$$
    よって、求める体積 $V$ は
    $$V = \pi \int_0^{\log 2} x^2\,dy = \pi \int_0^{\log 2} (e^y - 1)\,dy = \pi \left[e^y - y\right]_0^{\log 2}$$
    $$= \pi \left\{(e^{\log 2} - \log 2) - (e^0 - 0)\right\} = \pi \{(2 - \log 2) - 1\} = \pi(1 - \log 2)$$
    > 💡 讲师批注：绕 $y$ 轴旋转体只需要 $x^2$，**不需要开根号求 $x$**！直接由 $e^y = x^2 + 1$ 得出 $x^2 = e^y - 1$ 即可一步积分，非常清爽！

- **【最终答案】**
  - **[1] $V = 24\pi$**
  - **[2] $V = \pi(1 - \log 2)$**

---

#### 演習問題 18-(5)
- **【原题重现与翻译】**
  - 原题：曲線 $C : y = \log x$ に原点から接線 $l$ を引く。曲線 $C$ と接線 $l$ 及び $x$ 軸で囲まれた図形を $D$ とするとき、次の回転体の体積を求めよ。
    - [1] $D$ を $x$ 軸の周りに $1$ 回転させてできる回転体の体積 $V_x$
    - [2] $D$ を $y$ 軸の周りに $1$ 回転させてできる回転体の体積 $V_y$
  - 中文：从原点向曲线 $C : y = \log x$ 引切线 $l$。设由曲线 $C$、切线 $l$ 以及 $x$ 轴所围成的图形为 $D$，求下列旋转体的体积。
    - [1] 将 $D$ 绕 $x$ 轴旋转一周所形成的旋转体体积 $V_x$
    - [2] 将 $D$ 绕 $y$ 轴旋转一周所形成的旋转体体积 $V_y$
- **【考点定位】**
  - 对数函数过原点的切线方程 + 绕 $x$ 轴旋转（圆锥减曲线旋转 + 分部积分求 $\int (\log x)^2 dx$）+ 绕 $y$ 轴旋转。
- **【图解辅助（SVG 矢量图）】**

<svg viewBox="0 0 380 200" width="380" height="200" xmlns="http://www.w3.org/2000/svg" style="background:#fafafa;border:1px solid #e0e0e0;border-radius:6px;">
  <style>
    .axis { stroke: #333; stroke-width: 1.4; }
    .curve { fill: none; stroke: #2471a3; stroke-width: 2.2; }
    .lin { stroke: #c0392b; stroke-width: 2; }
    .area { fill: #d6eaf8; fill-opacity: 0.75; }
    .lbl { font: 11.5px sans-serif; fill: #2c3e50; }
    .math { font: italic 11.5px serif; fill: #2c3e50; }
  </style>
  <!-- Origin (55, 165), x scale: 85px/u, y scale: 100px/u -->
  <!-- (1, 0) = (140, 165), (e=2.718, 1) = (286, 65) -->
  <line x1="25" y1="165" x2="360" y2="165" class="axis"/>
  <polygon points="360,165 352,161 352,169" fill="#333"/>
  <line x1="55" y1="188" x2="55" y2="20" class="axis"/>
  <polygon points="55,20 51,28 59,28" fill="#333"/>
  <!-- Shaded region D -->
  <path d="M 55,165 L 286,65 Q 200,98 140,165 Z" class="area"/>
  <!-- Curve y = log x -->
  <path d="M 118,195 Q 130,175 140,165 Q 200,98 286,65 Q 320,52 348,43" class="curve"/>
  <!-- Tangent line l: y = x/e -->
  <line x1="55" y1="165" x2="345" y2="39.5" class="lin"/>
  <line x1="286" y1="65" x2="286" y2="165" stroke="#7f8c8d" stroke-dasharray="3,3"/>
  <line x1="55" y1="65" x2="286" y2="65" stroke="#7f8c8d" stroke-dasharray="3,3"/>
  <circle cx="286" cy="65" r="3.5" fill="#c0392b"/>
  <text x="352" y="180" class="math">x</text>
  <text x="62" y="30" class="math">y</text>
  <text x="41" y="180" class="lbl">O</text>
  <text x="136" y="180" class="lbl">1</text>
  <text x="282" y="180" class="math">e</text>
  <text x="41" y="69" class="lbl">1</text>
  <text x="255" y="55" class="lbl" fill="#c0392b">接点 (e, 1)</text>
  <text x="155" y="138" class="lbl" fill="#1b4f72" font-weight="bold">D</text>
  <text x="308" y="34" class="math" fill="#c0392b">l: y = x/e</text>
  <text x="295" y="92" class="math" fill="#2471a3">C: y = log x</text>
</svg>

- **【分步标准解答】**
  0. **接線 $l$ の方程式を求める**：
     曲線 $C : y = \log x$ 上の接点を $(t, \log t)$（$t > 0$）とおく。$y' = \dfrac{1}{x}$ より、接線の方程式は
     $$y - \log t = \frac{1}{t}(x - t) \implies y = \frac{1}{t}x + \log t - 1$$
     これが原点 $(0, 0)$ を通るから、
     $$0 = \log t - 1 \implies \log t = 1 \implies t = e$$
     よって接点は $(e, 1)$ であり、接線 $l$ の方程式は $y = \dfrac{1}{e}x$ である。

  - **[1] $x$ 軸の周りの回転体の体積 $V_x$**：
    図形 $D$ を $x$ 軸の周りに $1$ 回転させた立体は、「直線 $l$（$0 \le x \le e$）が作る底面の半径 $1$、高さ $e$ の円錐」から「曲線 $C$（$1 \le x \le e$）が作る回転体」をくり抜いたものである。
    $$V_x = \frac{1}{3}\pi \cdot 1^2 \cdot e - \pi \int_1^e (\log x)^2\,dx$$
    ここで部分積分法を $2$ 回用いて $\displaystyle\int_1^e (\log x)^2\,dx$ を計算する：
    $$\int_1^e 1 \cdot (\log x)^2\,dx = \left[x(\log x)^2\right]_1^e - \int_1^e x \cdot \frac{2\log x}{x}\,dx = e - 2\int_1^e \log x\,dx$$
    さらに $\displaystyle\int_1^e \log x\,dx = \left[x\log x - x\right]_1^e = (e - e) - (0 - 1) = 1$ であるから、
    $$\int_1^e (\log x)^2\,dx = e - 2$$
    よって、
    $$V_x = \frac{e}{3}\pi - \pi(e - 2) = \pi\left(2 - \frac{2}{3}e\right) = \frac{2(3 - e)}{3}\pi$$
    > 💡 讲师批注：把直线部分直接当圆锥用 $\frac{1}{3}\pi r^2 h$ 计算，既省时又能避免积分分段出错！另外 $\int_1^e (\log x)^2 dx = e - 2$ 是 EJU 高频积分，建议牢记。

  - **[2] $y$ 軸の周りの回転体の体積 $V_y$**：
    $y$ の範囲は $0 \le y \le 1$ であり、右側の境界は $C : x = e^y$、左側の境界は $l : x = ey$ である。
    よって、
    $$V_y = \pi \int_0^1 \left\{(e^y)^2 - (ey)^2\right\}\,dy = \pi \int_0^1 (e^{2y} - e^2 y^2)\,dy$$
    $$= \pi \left[\frac{1}{2}e^{2y} - \frac{e^2}{3}y^3\right]_0^1 = \pi \left\{\left(\frac{1}{2}e^2 - \frac{1}{3}e^2\right) - \left(\frac{1}{2} - 0\right)\right\}$$
    $$= \pi \left(\frac{1}{6}e^2 - \frac{1}{2}\right) = \frac{e^2 - 3}{6}\pi$$

- **【最终答案】**
  - **[1] $V_x = \dfrac{2(3 - e)}{3}\pi$**
  - **[2] $V_y = \dfrac{e^2 - 3}{6}\pi$**

---

#### 演習問題 18-(6)
- **【原题重现与翻译】**
  - 原题：曲線 $x = \tan\theta,\; y = \cos 2\theta\; \left(-\dfrac{\pi}{2} < \theta < \dfrac{\pi}{2}\right)$ と $x$ 軸で囲まれた部分を $x$ 軸の周りに $1$ 回転させてできる回転体の体積 $V$ を求めよ。
  - 中文：求由曲线 $x = \tan\theta,\; y = \cos 2\theta\; \left(-\dfrac{\pi}{2} < \theta < \dfrac{\pi}{2}\right)$ 与 $x$ 轴所围成的部分绕 $x$ 轴旋转一周所形成的旋转体体积 $V$。
  > ⚠️ **教材勘误提示（P415 / 教材印制页 P414）**：
  > 原题干印作「曲線 $x=\tan\theta, y=\cos 2\theta\,(-\frac{\pi}{2}<\theta<\frac{\pi}{2})$ と $x$ 軸の周りに $1$ 回転させてできる回転体の体積 $V$ を求めよ」，漏印了「で囲まれた部分を $x$ 軸」。结合曲线在 $-\frac{\pi}{4} \le \theta \le \frac{\pi}{4}$ 上满足 $y \ge 0$ 且与 $x$ 轴交于 $(\pm 1, 0)$，题意为该曲线与 $x$ 轴所围封闭图形绕 $x$ 轴旋转一周的体积。
- **【考点定位】**
  - 参数方程表示的旋转体体积（$V = \pi\int_a^b y^2\,dx = \pi\int_\alpha^\beta y(\theta)^2 \frac{dx}{d\theta}\,d\theta$）+ 三角函数倍角恒等变形。
- **【图解辅助（SVG 矢量图）】**

<svg viewBox="0 0 380 190" width="380" height="190" xmlns="http://www.w3.org/2000/svg" style="background:#fafafa;border:1px solid #e0e0e0;border-radius:6px;">
  <style>
    .axis { stroke: #333; stroke-width: 1.4; }
    .curve { fill: none; stroke: #2471a3; stroke-width: 2.2; }
    .area { fill: #d6eaf8; fill-opacity: 0.75; }
    .lbl { font: 11.5px sans-serif; fill: #2c3e50; }
    .math { font: italic 11.5px serif; fill: #2c3e50; }
  </style>
  <!-- Origin (190, 120), x scale: 80px/u, y scale: 75px/u -->
  <line x1="30" y1="120" x2="355" y2="120" class="axis"/>
  <polygon points="355,120 347,116 347,124" fill="#333"/>
  <line x1="190" y1="180" x2="190" y2="18" class="axis"/>
  <polygon points="190,18 186,26 194,26" fill="#333"/>
  <!-- Shaded area between x=-1 (110) and x=1 (270), y=(1-x^2)/(1+x^2), peak (190, 45) -->
  <path d="M 110,120 C 135,90 160,45 190,45 C 220,45 245,90 270,120 Z" class="area"/>
  <!-- Full curve approaching y=-1 (195) -->
  <path d="M 40,175 C 70,165 95,140 110,120 C 135,90 160,45 190,45 C 220,45 245,90 270,120 C 285,140 310,165 340,175" class="curve"/>
  <circle cx="110" cy="120" r="3" fill="#c0392b"/>
  <circle cx="270" cy="120" r="3" fill="#c0392b"/>
  <text x="348" y="135" class="math">x</text>
  <text x="197" y="28" class="math">y</text>
  <text x="176" y="135" class="lbl">O</text>
  <text x="98" y="136" class="lbl">-1</text>
  <text x="272" y="136" class="lbl">1</text>
  <text x="196" y="42" class="lbl">1</text>
  <text x="242" y="60" class="math" fill="#2471a3">y = (1 - x²)/(1 + x²)</text>
  <text x="152" y="96" class="lbl" fill="#1b4f72" font-weight="bold">V = π(4 - π)</text>
</svg>

- **【分步标准解答】**
  1. **曲線と $x$ 軸の交点および対称性**：
     $y = \cos 2\theta = 0$ を $-\dfrac{\pi}{2} < \theta < \dfrac{\pi}{2}$ の範囲で解くと、
     $$2\theta = \pm \frac{\pi}{2} \implies \theta = \pm \frac{\pi}{4}$$
     このとき $x = \tan\left(\pm\dfrac{\pi}{4}\right) = \pm 1$ である。
     また、$\theta$ を $-\theta$ に置き換えると $x \to -x,\; y \to y$ となるから、この曲線は $y$ 軸に関して対称であり、$-\dfrac{\pi}{4} \le \theta \le \dfrac{\pi}{4}$ で $y \ge 0$ である。

  2. **置換積分（媒介変数）による体積計算**：
     対称性より、
     $$V = 2\pi \int_0^1 y^2\,dx$$
     $x = \tan\theta$ より $\dfrac{dx}{d\theta} = \dfrac{1}{\cos^2\theta}$、$x : 0 \to 1$ のとき $\theta : 0 \to \dfrac{\pi}{4}$ であるから、
     $$V = 2\pi \int_0^{\frac{\pi}{4}} \cos^2 2\theta \cdot \frac{1}{\cos^2\theta}\,d\theta$$
     ここで $\cos 2\theta = 2\cos^2\theta - 1$ を代入して被積分関数を整理すると、
     $$\frac{\cos^2 2\theta}{\cos^2\theta} = \frac{(2\cos^2\theta - 1)^2}{\cos^2\theta} = \frac{4\cos^4\theta - 4\cos^2\theta + 1}{\cos^2\theta} = 4\cos^2\theta - 4 + \frac{1}{\cos^2\theta}$$
     さらに半角公式 $4\cos^2\theta = 2(1 + \cos 2\theta) = 2 + 2\cos 2\theta$ を用いると、
     $$= 2\cos 2\theta - 2 + \frac{1}{\cos^2\theta}$$
     > 💡 讲师批注：把 $\cos 2\theta$ 展开为 $2\cos^2\theta - 1$ 之后除以 $\cos^2\theta$，立刻变成三项可以直接口算原函数的基本三角函数（$\sin 2\theta,\; -2\theta,\; \tan\theta$）！切忌消去 $\theta$ 化为有理函数再硬拆，参数法快一倍！

     よって、
     $$V = 2\pi \int_0^{\frac{\pi}{4}} \left(2\cos 2\theta - 2 + \frac{1}{\cos^2\theta}\right)\,d\theta = 2\pi \left[\sin 2\theta - 2\theta + \tan\theta\right]_0^{\frac{\pi}{4}}$$
     $$= 2\pi \left\{\left(1 - \frac{\pi}{2} + 1\right) - 0\right\} = 2\pi\left(2 - \frac{\pi}{2}\right) = \pi(4 - \pi)$$
- **【最终答案】**
  **$V = \pi(4 - \pi)$**（または $4\pi - \pi^2$）

---

### 第十一章 演習問題 19（定積分の応用：曲線の長さ）

#### 演習問題 19-(1)
- **【原题重现与翻译】**
  - 原题：次の曲線の長さを求めよ。[1] では $a > 0$ とする。
    - [1] アステロイド $x = a\cos^3 t,\; y = a\sin^3 t\; (0 \le t \le 2\pi)$
    - [2] $y = \log(x + \sqrt{x^2 - 1})\; (\sqrt{2} \le x \le 4)$
  - 中文：求下列曲线的长度。在 [1] 中设 $a > 0$。
    - [1] 星形线 $x = a\cos^3 t,\; y = a\sin^3 t\; (0 \le t \le 2\pi)$
    - [2] $y = \log(x + \sqrt{x^2 - 1})\; (\sqrt{2} \le x \le 4)$
- **【考点定位】**
  - 参数方程弧长公式（利用对称性避开绝对值符号）+ 直角坐标弧长公式（凑根号下完全平方）。
- **【图解辅助（SVG 矢量图）】**

<svg viewBox="0 0 420 190" width="420" height="190" xmlns="http://www.w3.org/2000/svg" style="background:#fafafa;border:1px solid #e0e0e0;border-radius:6px;">
  <style>
    .axis { stroke: #333; stroke-width: 1.3; }
    .curve { fill: none; stroke: #2471a3; stroke-width: 2.2; }
    .hi { fill: none; stroke: #c0392b; stroke-width: 2.8; }
    .lbl { font: 11.5px sans-serif; fill: #2c3e50; }
    .math { font: italic 11.5px serif; fill: #2c3e50; }
  </style>
  <!-- Left: [1] Astroid -->
  <text x="15" y="20" class="lbl" font-weight="bold">[1] アステロイド（4 象限完全対称）</text>
  <line x1="25" y1="108" x2="195" y2="108" class="axis"/>
  <polygon points="195,108 188,104 188,112" fill="#333"/>
  <line x1="110" y1="180" x2="110" y2="32" class="axis"/>
  <polygon points="110,32 106,39 114,39" fill="#333"/>
  <!-- Astroid centered at (110, 108), radius 62 -->
  <path d="M 110,46 Q 110,108 48,108 Q 110,108 110,170 Q 110,108 172,108" class="curve"/>
  <!-- Q1 highlighted -->
  <path d="M 172,108 Q 110,108 110,46" class="hi"/>
  <text x="188" y="123" class="math">x</text>
  <text x="116" y="40" class="math">y</text>
  <text x="174" y="123" class="math">a</text>
  <text x="34" y="123" class="math">-a</text>
  <text x="116" y="54" class="math">a</text>
  <text x="116" y="176" class="math">-a</text>
  <text x="132" y="75" class="lbl" fill="#c0392b">L/4 (0≤t≤π/2)</text>
  <!-- Right: [2] y = log(x + sqrt(x^2-1)) -->
  <text x="230" y="20" class="lbl" font-weight="bold">[2] y = log(x + √(x²-1))</text>
  <line x1="235" y1="158" x2="405" y2="158" class="axis"/>
  <polygon points="405,158 398,154 398,162" fill="#333"/>
  <line x1="255" y1="175" x2="255" y2="35" class="axis"/>
  <polygon points="255,35 251,42 259,42" fill="#333"/>
  <!-- (1,0)=(285,158), (sqrt2, 0.88)=(298,114), (4, 2.06)=(375,55) -->
  <path d="M 285,158 Q 287,132 298,114" class="curve"/>
  <path d="M 298,114 Q 325,78 375,55" class="hi"/>
  <line x1="298" y1="114" x2="298" y2="158" stroke="#7f8c8d" stroke-dasharray="3,3"/>
  <line x1="375" y1="55" x2="375" y2="158" stroke="#7f8c8d" stroke-dasharray="3,3"/>
  <text x="398" y="173" class="math">x</text>
  <text x="262" y="44" class="math">y</text>
  <text x="242" y="173" class="lbl">O</text>
  <text x="279" y="173" class="lbl">1</text>
  <text x="294" y="173" class="lbl">√2</text>
  <text x="371" y="173" class="lbl">4</text>
  <text x="315" y="112" class="lbl" fill="#c0392b">L = √15 - 1</text>
</svg>

- **【分步标准解答】**
  - **[1] アステロイドの長さ**：
    $x = a\cos^3 t,\; y = a\sin^3 t$ をそれぞれ $t$ で微分すると、
    $$\frac{dx}{dt} = -3a\cos^2 t \sin t, \qquad \frac{dy}{dt} = 3a\sin^2 t \cos t$$
    よって、
    $$\left(\frac{dx}{dt}\right)^2 + \left(\frac{dy}{dt}\right)^2 = 9a^2\sin^2 t \cos^2 t (\cos^2 t + \sin^2 t) = 9a^2\sin^2 t \cos^2 t$$
    この曲線は $x$ 軸、$y$ 軸に関して対称であるから、求める長さ $L$ は第 $1$ 象限部分（$0 \le t \le \dfrac{\pi}{2}$）の長さの $4$ 倍に等しい。
    $0 \le t \le \dfrac{\pi}{2}$ では $\sin t \ge 0,\; \cos t \ge 0$ であり、$a > 0$ より $\sqrt{9a^2\sin^2 t \cos^2 t} = 3a\sin t \cos t$ であるから、
    $$L = 4 \int_0^{\frac{\pi}{2}} 3a\sin t \cos t\,dt = 12a \left[\frac{1}{2}\sin^2 t\right]_0^{\frac{\pi}{2}} = 6a(1 - 0) = 6a$$
    > 💡 讲师批注：如果直接从 $0$ 积到 $2\pi$，千万别忘记 $\sqrt{\sin^2 t\cos^2 t} = |\sin t\cos t|$（不加绝对值会积出 $0$！）。利用四象限对称性只积 $[0, \frac{\pi}{2}]$ 再乘 $4$，既规范又绝对不出错！

  - **[2] $y = \log(x + \sqrt{x^2 - 1})$ の長さ**：
    $y$ を $x$ で微分すると、合成関数の微分法より、
    $$\frac{dy}{dx} = \frac{1 + \dfrac{2x}{2\sqrt{x^2 - 1}}}{x + \sqrt{x^2 - 1}} = \frac{\dfrac{\sqrt{x^2 - 1} + x}{\sqrt{x^2 - 1}}}{x + \sqrt{x^2 - 1}} = \frac{1}{\sqrt{x^2 - 1}}$$
    > 💡 讲师批注：分子通分后恰好与分母 $x + \sqrt{x^2 - 1}$ 完美约分！记住这个经典导数：$\left\{\log(x + \sqrt{x^2 \pm a^2})\right\}' = \dfrac{1}{\sqrt{x^2 \pm a^2}}$。

    したがって、$\sqrt{2} \le x \le 4$（$x > 0$）において、
    $$\sqrt{1 + \left(\frac{dy}{dx}\right)^2} = \sqrt{1 + \frac{1}{x^2 - 1}} = \sqrt{\frac{x^2}{x^2 - 1}} = \frac{x}{\sqrt{x^2 - 1}}$$
    よって、求める曲線の長さ $L$ は
    $$L = \int_{\sqrt{2}}^4 \frac{x}{\sqrt{x^2 - 1}}\,dx = \left[\sqrt{x^2 - 1}\right]_{\sqrt{2}}^4 = \sqrt{4^2 - 1} - \sqrt{(\sqrt{2})^2 - 1} = \sqrt{15} - 1$$
    （確認：$t = x^2 - 1$ とおけば $dt = 2x\,dx$、$\int_1^{15} \frac{1}{2\sqrt{t}}\,dt = [\sqrt{t}]_1^{15} = \sqrt{15} - 1$。）

- **【最终答案】**
  - **[1] $L = 6a$**
  - **[2] $L = \sqrt{15} - 1$**

---

### 第十二章 演習問題 1（順列・円順列・じゅず順列）

#### 演習問題 1-(1)
- **【原题重现与翻译】**
  - 原题：$0, 1, 2, 3, 4, 5$ の $6$ 個の数字から異なる $4$ 個の数字を取って並べて、$4$ 桁の整数を作るものとする。次のものは全部で何個できるか。
    - [1] 整数　　[2] $3$ の倍数　　[3] $6$ の倍数　　[4] $2400$ より大きい整数
  - 中文：从 $0, 1, 2, 3, 4, 5$ 这 $6$ 个数字中任取 $4$ 个不同的数字排成 $4$ 位数。下列情况各能组成多少个？
    - [1] 整数　　[2] $3$ 的倍数　　[3] $6$ 的倍数　　[4] 大于 $2400$ 的整数
- **【考点定位】**
  - 含 $0$ 的数字排列（首位不为 $0$）+ $3$ 的倍数与 $6$ 的倍数判定（各位数字之和为 $3$ 的倍数且末位为偶数）+ 大小比较分类计数。
- **【图解辅助（SVG 矢量图）】**

<svg viewBox="0 0 460 155" width="460" height="155" xmlns="http://www.w3.org/2000/svg" style="background:#fafafa;border:1px solid #e0e0e0;border-radius:6px;">
  <style>
    .box { fill: #eaf2f8; stroke: #2471a3; stroke-width: 1.5; rx: 4; }
    .box2 { fill: #fdedec; stroke: #c0392b; stroke-width: 1.5; rx: 4; }
    .lbl { font: 11.5px sans-serif; fill: #2c3e50; }
    .b { font: bold 12px sans-serif; fill: #1b4f72; }
  </style>
  <!-- Left: 4-digit slot structure -->
  <text x="15" y="22" class="lbl" font-weight="bold">[1] 4 桁の整数（千の位は 0 不可）</text>
  <rect x="18" y="34" width="44" height="36" class="box2"/>
  <rect x="68" y="34" width="44" height="36" class="box"/>
  <rect x="118" y="34" width="44" height="36" class="box"/>
  <rect x="168" y="34" width="44" height="36" class="box"/>
  <text x="29" y="57" class="b" fill="#c0392b">5通</text>
  <text x="79" y="57" class="b">5通</text>
  <text x="129" y="57" class="b">4通</text>
  <text x="179" y="57" class="b">3通</text>
  <text x="27" y="86" class="lbl">千位</text>
  <text x="77" y="86" class="lbl">百位</text>
  <text x="127" y="86" class="lbl">十位</text>
  <text x="177" y="86" class="lbl">个位</text>
  <text x="18" y="112" class="lbl">⇒ 5 × ₅P₃ = 5 × 60 = 300 個</text>
  <!-- Right: [2] Mod 3 grouping -->
  <text x="240" y="22" class="lbl" font-weight="bold">[2] 3 の倍数（总和 15 ⇒ 排除 2 数的和≡0）</text>
  <rect x="242" y="34" width="62" height="36" class="box"/>
  <rect x="312" y="34" width="62" height="36" class="box"/>
  <rect x="382" y="34" width="62" height="36" class="box"/>
  <text x="252" y="49" class="lbl">余 0</text><text x="250" y="64" class="b">{0, 3}</text>
  <text x="322" y="49" class="lbl">余 1</text><text x="320" y="64" class="b">{1, 4}</text>
  <text x="392" y="49" class="lbl">余 2</text><text x="390" y="64" class="b">{2, 5}</text>
  <text x="242" y="92" class="lbl">・排除 {0,3} ⇒ 选 {1,2,4,5}（不含0）：1組</text>
  <text x="242" y="112" class="lbl">・余1×余2 ⇒ 排除 {1,2},{1,5},{4,2},{4,5}</text>
  <text x="242" y="132" class="lbl">　⇒ 选出的 4 数均含 0：4組</text>
</svg>

- **【分步标准解答】**
  - **[1] $4$ 桁の整数**：
    千の位は $0$ 以外の $5$ 通り、残りの $3$ 桁は残り $5$ 個の数字から $3$ 個並べるから ${}_5\mathrm{P}_3$ 通り。
    $$5 \times {}_5\mathrm{P}_3 = 5 \times 5 \times 4 \times 3 = 300 \text{（個）}$$

  - **[2] $3$ の倍数**：
    $3$ の倍数となる条件は「各位の数字の和が $3$ の倍数」である。
    $6$ 個の数字の総和は $0 + 1 + 2 + 3 + 4 + 5 = 15$（$3$ の倍数）であるから、**選ぶ $4$ 個の和が $3$ の倍数 $\iff$ 選ばない $2$ 個の和が $3$ の倍数** となる。
    $6$ 個の数字を $3$ で割った余りで分類すると $\{0, 3\}$、$\{1, 4\}$、$\{2, 5\}$。和が $3$ の倍数になる $2$ 個の組は次の $5$ 通り：
    1. $\{0, 3\}$ を除く $\implies$ 使う数字は $\{1, 2, 4, 5\}$（$0$ を含まない）：$4! = 24$ 個
    2. $\{1, 2\}, \{1, 5\}, \{2, 4\}, \{4, 5\}$ のいずれかを除く（計 $4$ 組）$\implies$ 使う数字はそれぞれ $\{0, 3, 4, 5\},\; \{0, 2, 3, 4\},\; \{0, 1, 3, 5\},\; \{0, 1, 2, 3\}$（すべて $0$ を含む）：
       各組につき、千の位が $0$ 以外の $3$ 通り、残り $3$ 桁が $3!$ 通りなので $3 \times 3! = 18$ 個。
       $4$ 組合計で $4 \times 18 = 72$ 個。
    よって、合計 $24 + 72 = 96$ 個。
    > 💡 讲师批注：「选 4 个和是 3 的倍数」转化为「排除的 2 个和是 3 的倍数」，秒找全部 5 组，绝不遗漏！

  - **[3] $6$ の倍数**：
    $6$ の倍数 $\iff$「$3$ の倍数かつ偶数（一の位が $0, 2, 4$）」。[2] で求めた $5$ 組について個数を数える：
    - $\{1, 2, 4, 5\}$：一の位は $2, 4$ の $2$ 通り、残り $3$ 桁は $3!$ 通り $\implies 2 \times 6 = 12$ 個
    - $\{0, 3, 4, 5\}$：一の位が $0$ のとき $3! = 6$ 個；一の位が $4$ のとき千の位は $3, 5$ の $2$ 通り、残り $2$ 桁は $2!$ 通りで $2 \times 2 = 4$ 個 $\implies 6 + 4 = 10$ 個
    - $\{0, 2, 3, 4\}$：一の位が $0$ のとき $3! = 6$ 個；一の位が $2$ または $4$ のとき、一の位 $2$ 通り、千の位（$0$ 以外）$2$ 通り、残り $2!$ 通りで $2 \times 2 \times 2 = 8$ 個 $\implies 6 + 8 = 14$ 個
    - $\{0, 1, 3, 5\}$：偶数は $0$ のみ。一の位が $0$ で $3! = 6$ 個
    - $\{0, 1, 2, 3\}$：$\{0, 3, 4, 5\}$ と同様に、$6 + 4 = 10$ 個
    よって、合計 $12 + 10 + 14 + 6 + 10 = 52$ 個。
    > 💡 讲师批注：含 $0$ 求偶数时，**必须按「个位是否为 $0$」分类**！因为个位取 $0$ 时千位无限制，个位取非零偶数时千位不能取 $0$。

  - **[4] $2400$ より大きい整数**：
    千の位と百の位で場合分けする：
    1. 千の位が $3, 4, 5$ のとき：$3 \times {}_5\mathrm{P}_3 = 3 \times 60 = 180$ 個
    2. 千の位が $2$、百の位が $4$ または $5$ のとき（異なる数字を使うため最小でも $2401 > 2400$）：
       $1 \times 2 \times {}_4\mathrm{P}_2 = 2 \times 12 = 24$ 個
    よって、合計 $180 + 24 = 204$ 個。

- **【最终答案】**
  - **[1] $300$ 個　　[2] $96$ 個　　[3] $52$ 個　　[4] $204$ 個**

---

#### 演習問題 1-(2)
- **【原题重现与翻译】**
  - 原题：男子 $A, B, C$、女子 $D, E, F, G$ の $7$ 人が $1$ 列に並ぶとき、
    - [1] $A$ と $B$ が隣り合うような並び方は全部で何通りあるか。
    - [2] $A$ と $B$ が両端にくるような並び方は全部で何通りあるか。
    - [3] どの男子も隣り合わないような並び方は全部で何通りあるか。
  - 中文：男生 $A, B, C$ 与女生 $D, E, F, G$ 共 $7$ 人排成一列时：
    - [1] $A$ 与 $B$ 相邻的排法共有多少种？
    - [2] $A$ 与 $B$ 位于两端的排法共有多少种？
    - [3] 任意两名男生都不相邻的排法共有多少种？
- **【考点定位】**
  - 相邻问题（捆绑法）、特殊位置优先法、不相邻问题（插空法）。
- **【图解辅助（SVG 矢量图）】**

<svg viewBox="0 0 460 115" width="460" height="115" xmlns="http://www.w3.org/2000/svg" style="background:#fafafa;border:1px solid #e0e0e0;border-radius:6px;">
  <style>
    .girl { fill: #fadbd8; stroke: #c0392b; stroke-width: 1.5; }
    .gap { fill: #d6eaf8; stroke: #2471a3; stroke-width: 1.3; stroke-dasharray: 3,2; }
    .lbl { font: 11.5px sans-serif; fill: #2c3e50; }
    .b { font: bold 12px sans-serif; fill: #922b21; }
  </style>
  <text x="15" y="22" class="lbl" font-weight="bold">[3] 插空法示意图：先排 4 名女生（4!），产生 5 个空位插入 3 名男生（₅P₃）</text>
  <!-- 5 gaps and 4 girls -->
  <rect x="20" y="42" width="32" height="30" rx="4" class="gap"/><text x="30" y="61" class="lbl" fill="#2471a3">空1</text>
  <circle cx="80" cy="57" r="16" class="girl"/><text x="75" y="61" class="b">D</text>
  <rect x="108" y="42" width="32" height="30" rx="4" class="gap"/><text x="118" y="61" class="lbl" fill="#2471a3">空2</text>
  <circle cx="168" cy="57" r="16" class="girl"/><text x="163" y="61" class="b">E</text>
  <rect x="196" y="42" width="32" height="30" rx="4" class="gap"/><text x="206" y="61" class="lbl" fill="#2471a3">空3</text>
  <circle cx="256" cy="57" r="16" class="girl"/><text x="251" y="61" class="b">F</text>
  <rect x="284" y="42" width="32" height="30" rx="4" class="gap"/><text x="294" y="61" class="lbl" fill="#2471a3">空4</text>
  <circle cx="344" cy="57" r="16" class="girl"/><text x="339" y="61" class="b">G</text>
  <rect x="372" y="42" width="32" height="30" rx="4" class="gap"/><text x="382" y="61" class="lbl" fill="#2471a3">空5</text>
  <text x="20" y="100" class="lbl">⇒ 4! × ₅P₃ = 24 × 60 = 1440 通り</text>
</svg>

- **【分步标准解答】**
  - **[1] $A$ と $B$ が隣り合う**：
    $A$ と $B$ を $1$ 組（$1$ 人分）とみなして、残り $5$ 人と合わせた $6$ 個を $1$ 列に並べる方法は $6!$ 通り。
    さらに、組の中の $A$ と $B$ の並び方は $2!$ 通りあるから、
    $$6! \times 2! = 720 \times 2 = 1440 \text{（通り）}$$

  - **[2] $A$ と $B$ が両端にくる**：
    両端の $2$ か所に $A, B$ を並べる方法は $2!$ 通り。
    間の $5$ か所に残りの $5$ 人を並べる方法は $5!$ 通りであるから、
    $$2! \times 5! = 2 \times 120 = 240 \text{（通り）}$$

  - **[3] どの男子も隣り合わない**：
    まず女子 $4$ 人を $1$ 列に並べると $4!$ 通り。
    女子の両端と間には合計 $5$ か所のすき間ができる。この $5$ か所から $3$ か所を選んで男子 $3$ 人を並べればよいから ${}_5\mathrm{P}_3$ 通り。
    よって、
    $$4! \times {}_5\mathrm{P}_3 = 24 \times 60 = 1440 \text{（通り）}$$
    > 💡 讲师批注：3 人及以上不相邻时，**切勿用「总数减去全部相邻」**（因为还会漏减「恰好 2 人相邻」的情况），必须老老实实用**插空法**！

- **【最终答案】**
  - **[1] $1440$ 通り　　[2] $240$ 通り　　[3] $1440$ 通り**

---

#### 演習問題 1-(3)
- **【原题重现与翻译】**
  - 原题：$a, b, c, d, e$ の $5$ 文字を並べたものを、アルファベット順に、$1$ 番目 `abcde`、$2$ 番目 `abced`、$\cdots$、$120$ 番目 `edcba` と番号をつける。
    - [1] `cbeda` は何番目か。
    - [2] $40$ 番目は何か。
  - 中文：将 $a, b, c, d, e$ 这 $5$ 个字母的全排列按字母表顺序编号：第 $1$ 个为 `abcde`，第 $2$ 个为 `abced`，$\cdots$，第 $120$ 个为 `edcba`。
    - [1] `cbeda` 是第几个？
    - [2] 第 $40$ 个是什么？
- **【考点定位】**
  - 字典序排列（辞書式配列）的正向定位与逆向还原。
- **【图解辅助（SVG 矢量图）】**

<svg viewBox="0 0 460 110" width="460" height="110" xmlns="http://www.w3.org/2000/svg" style="background:#fafafa;border:1px solid #e0e0e0;border-radius:6px;">
  <style>
    .seg1 { fill: #d6eaf8; stroke: #2471a3; stroke-width: 1.2; }
    .seg2 { fill: #fdebd0; stroke: #d35400; stroke-width: 1.2; }
    .seg3 { fill: #fadbd8; stroke: #c0392b; stroke-width: 1.5; }
    .lbl { font: 11px sans-serif; fill: #2c3e50; }
  </style>
  <text x="14" y="20" class="lbl" font-weight="bold">字典序区间标尺（总计 5! = 120 个，每组首字母各占 4! = 24 个）</text>
  <rect x="15" y="34" width="84" height="30" class="seg1"/><text x="32" y="53" class="lbl">a**** (1-24)</text>
  <rect x="99" y="34" width="84" height="30" class="seg2"/><text x="112" y="53" class="lbl">b**** (25-48)</text>
  <rect x="183" y="34" width="84" height="30" class="seg3"/><text x="197" y="53" class="lbl">c**** (49-72)</text>
  <rect x="267" y="34" width="84" height="30" class="seg1"/><text x="281" y="53" class="lbl">d**** (73-96)</text>
  <rect x="351" y="34" width="92" height="30" class="seg1"/><text x="362" y="53" class="lbl">e**** (97-120)</text>
  <!-- Pointers -->
  <line x1="152" y1="64" x2="152" y2="84" stroke="#d35400" stroke-width="1.6"/>
  <text x="108" y="98" class="lbl" fill="#a04000" font-weight="bold">40番目: bdcea</text>
  <line x1="225" y1="64" x2="225" y2="84" stroke="#c0392b" stroke-width="1.6"/>
  <text x="195" y="98" class="lbl" fill="#c0392b" font-weight="bold">60番目: cbeda</text>
</svg>

- **【分步标准解答】**
  - **[1] `cbeda` の順番**：
    `cbeda` より前にくる文字列の個数を、先頭から順に固定して数える：
    - `a****` の形：$4! = 24$ 個
    - `b****` の形：$4! = 24$ 個
    - `ca***` の形：$3! = 6$ 個
    - `cba**` の形：$2! = 2$ 個
    - `cbd**` の形：$2! = 2$ 個
    - `cbe**` の形は残りが `a, d` なので、小さい順に `cbead`（$59$ 番目）、`cbeda`（$60$ 番目）。
    よって、`cbeda` は $24 + 24 + 6 + 2 + 2 + 2 = 60$ 番目である。
    > 💡 讲师批注：快检法——`cbeda` 是 `cb***` 中字典序**最大**的（剩余 `a, d, e` 逆序排列为 `eda`），而 `a****`、`b****`、`ca***`、`cb***` 共有 $24 + 24 + 6 + 6 = 60$ 个，故 `cbeda` 必为第 $60$ 个！

  - **[2] $40$ 番目の文字列**：
    先頭から順に範囲を絞り込む：
    - `a****`：$1 \sim 24$ 番目（$24$ 個）
    - `b****`：$25 \sim 48$ 番目（$40$ 番目はここ！残り $40 - 24 = 16$ 個目）
    - `ba***`：$25 \sim 30$ 番目（$3! = 6$ 個）
    - `bc***`：$31 \sim 36$ 番目（$3! = 6$ 個）
    - `bd***`：$37 \sim 42$ 番目（$40$ 番目はここ！）
    - `bda**`：$37 \sim 38$ 番目（$2! = 2$ 個）
    - `bdc**`：$39 \sim 40$ 番目。残りの文字は `a, e` なので、$39$ 番目が `bdcae`、$40$ 番目が `bdcea` である。

- **【最终答案】**
  - **[1] $60$ 番目**
  - **[2] `bdcea`**

---

#### 演習問題 1-(4)
- **【原题重现与翻译】**
  - 原题：ある領域が、右の図のように $6$ つの区画に分けられている。境界を接している区画は異なる色で塗ることにして、赤・青・黄・白の $4$ 色以内で領域を塗り分ける方法は何通りあるか。
  - 中文：某区域如右图所示被划分为 $6$ 个区块。规定有公共边界的区块必须涂不同颜色，用红、蓝、黄、白 $4$ 种以内的颜色为该区域涂色，共有多少种涂法？
- **【考点定位】**
  - 区域涂色问题（塗り分け）与乘法原理（積の法則）。
- **【图解辅助（SVG 矢量图）】**
  严格还原教材 `page_0420.jpg` 的 6 区画边界拓扑关系（注意：$D$ 与 $C$ 有公共边界，$B$ 与 $E$ 不相邻）：

<svg viewBox="0 0 420 200" width="420" height="200" xmlns="http://www.w3.org/2000/svg" style="background:#fafafa;border:1px solid #e0e0e0;border-radius:6px;">
  <style>
    .cell { stroke: #2c3e50; stroke-width: 1.8; }
    .lbl { font: 12px sans-serif; fill: #2c3e50; }
    .b { font: bold 14px sans-serif; fill: #2c3e50; }
  </style>
  <!-- Left: Exact 6-region map from page_0420.jpg -->
  <rect x="30" y="20" width="120" height="32" fill="#fadbd8" class="cell"/><text x="85" y="41" class="b">A</text>
  <rect x="30" y="52" width="60" height="36" fill="#d6eaf8" class="cell"/><text x="55" y="75" class="b">B</text>
  <rect x="90" y="52" width="60" height="62" fill="#fcf3cf" class="cell"/><text x="115" y="88" class="b">C</text>
  <rect x="30" y="88" width="60" height="62" fill="#d5f5e3" class="cell"/><text x="55" y="124" class="b">D</text>
  <rect x="90" y="114" width="60" height="36" fill="#ebdef0" class="cell"/><text x="115" y="137" class="b">E</text>
  <rect x="30" y="150" width="120" height="32" fill="#fdebd0" class="cell"/><text x="85" y="171" class="b">F</text>
  <!-- Highlight shared edge between C and D -->
  <line x1="90" y1="88" x2="90" y2="114" stroke="#c0392b" stroke-width="3.5"/>
  <!-- Right: Coloring order explanation -->
  <text x="175" y="38" class="lbl" font-weight="bold">关键观察：C 与 D 有公共边（红粗线）！</text>
  <text x="175" y="64" class="lbl">按 A → B → C → D → E → F 顺序涂色：</text>
  <text x="175" y="88" class="lbl">1. A：自由选 ⇒ 4 通り</text>
  <text x="175" y="108" class="lbl">2. B（≠A）：⇒ 3 通り</text>
  <text x="175" y="128" class="lbl">3. C（≠A, B）：A, B 必异色 ⇒ 2 通り</text>
  <text x="175" y="148" class="lbl">4. D（≠B, C）：B, C 必异色 ⇒ 2 通り</text>
  <text x="175" y="168" class="lbl">5. E（≠C, D）：C, D 必异色 ⇒ 2 通り</text>
  <text x="175" y="188" class="lbl">6. F（≠D, E）：D, E 必异色 ⇒ 2 通り</text>
</svg>

- **【分步标准解答】**
  図の境界の接し方を確認し、$A \to B \to C \to D \to E \to F$ の順に色を塗っていく。
  1. 区画 $A$ の塗り方：$4$ 色から自由に選べるから **$4$ 通り**。
  2. 区画 $B$ の塗り方：$A$ と接しているため $A$ 以外の **$3$ 通り**。
  3. 区画 $C$ の塗り方：$A$ と $B$ の両方に接しており、$A$ と $B$ はすでに異なる色であるから、残りの **$2$ 通り**。
  4. 区画 $D$ の塗り方：$B$ と $C$ の両方に接しており、$B$ と $C$ はすでに異なる色であるから、残りの **$2$ 通り**。
  5. 区画 $E$ の塗り方：$C$ と $D$ の両方に接しており、$C$ と $D$ はすでに異なる色であるから、残りの **$2$ 通り**。
  6. 区画 $F$ の塗り方：$D$ と $E$ の両方に接しており、$D$ と $E$ はすでに異なる色であるから、残りの **$2$ 通り**。

  よって、積の法則により、求める塗り分け方は
  $$4 \times 3 \times 2 \times 2 \times 2 \times 2 = 192 \text{（通り）}$$
  > 💡 讲师批注：本题无需分类讨论！核心原因在于每一步新涂的区域所邻接的「已涂区域」都是两个**彼此相邻**（因而必定异色）的区块（例如 $D$ 邻接已涂的 $B, C$，而 $B, C$ 彼此相邻）。另外注意题目说「$4$ 色以内」，意味着用 $3$ 色或 $4$ 色均可，以上乘法已自动包含所有合法情况。

- **【最终答案】**
  **$192$ 通り**

---

#### 演習問題 1-(5)
- **【原题重现与翻译】**
  - 原题：異なる $6$ 個の宝石がある。
    - [1] これらの宝石を机の上で円形に並べる方法は何通りあるか。
    - [2] これらの宝石で首飾りを作るとき、何種類の首飾りができるか。
    - [3] $6$ 個の宝石から $4$ 個を取り出し、机の上で円形に並べる方法は何通りあるか。
  - 中文：有 $6$ 颗不同的宝石。
    - [1] 将这些宝石在桌面上排成圆形，共有多少种排法？
    - [2] 用这些宝石做成项链，可以做成多少种不同的项链？
    - [3] 从 $6$ 颗宝石中取出 $4$ 颗在桌面上排成圆形，共有多少种排法？
- **【考点定位】**
  - 圆排列（円順列）、项链排列（じゅず順列）、选部分元素的圆排列。
- **【图解辅助（SVG 矢量图）】**

<svg viewBox="0 0 460 135" width="460" height="135" xmlns="http://www.w3.org/2000/svg" style="background:#fafafa;border:1px solid #e0e0e0;border-radius:6px;">
  <style>
    .ring { fill: none; stroke: #7f8c8d; stroke-width: 1.5; }
    .gem { fill: #d6eaf8; stroke: #2471a3; stroke-width: 1.5; }
    .fix { fill: #fadbd8; stroke: #c0392b; stroke-width: 1.8; }
    .lbl { font: 11px sans-serif; fill: #2c3e50; }
  </style>
  <!-- Left: Circular permutation -->
  <text x="15" y="18" class="lbl" font-weight="bold">[1] 円順列（固定 1 颗）</text>
  <circle cx="80" cy="75" r="35" class="ring"/>
  <circle cx="80" cy="40" r="9" class="fix"/><text x="76" y="44" class="lbl" fill="#c0392b">1</text>
  <circle cx="110" cy="57" r="8" class="gem"/><text x="107" y="61" class="lbl">2</text>
  <circle cx="110" cy="93" r="8" class="gem"/><text x="107" y="97" class="lbl">3</text>
  <circle cx="80" cy="110" r="8" class="gem"/><text x="77" y="114" class="lbl">4</text>
  <circle cx="50" cy="93" r="8" class="gem"/><text x="47" y="97" class="lbl">5</text>
  <circle cx="50" cy="57" r="8" class="gem"/><text x="47" y="61" class="lbl">6</text>
  <text x="38" y="128" class="lbl">(6-1)! = 120 通り</text>
  <!-- Middle: Necklace -->
  <text x="165" y="18" class="lbl" font-weight="bold">[2] じゅず順列（翻转重合 ÷2）</text>
  <circle cx="235" cy="75" r="35" class="ring"/>
  <line x1="235" y1="30" x2="235" y2="120" stroke="#c0392b" stroke-dasharray="3,2"/>
  <circle cx="235" cy="40" r="8" class="fix"/>
  <circle cx="265" cy="57" r="7" class="gem"/>
  <circle cx="265" cy="93" r="7" class="gem"/>
  <circle cx="235" cy="110" r="7" class="gem"/>
  <circle cx="205" cy="93" r="7" class="gem"/>
  <circle cx="205" cy="57" r="7" class="gem"/>
  <text x="192" y="128" class="lbl">120 ÷ 2 = 60 種類</text>
  <!-- Right: 4 of 6 circular -->
  <text x="330" y="18" class="lbl" font-weight="bold">[3] 6 选 4 圆排列</text>
  <circle cx="385" cy="75" r="30" class="ring"/>
  <circle cx="385" cy="45" r="8" class="gem"/>
  <circle cx="415" cy="75" r="8" class="gem"/>
  <circle cx="385" cy="105" r="8" class="gem"/>
  <circle cx="355" cy="75" r="8" class="gem"/>
  <text x="342" y="128" class="lbl">₆P₄ / 4 = 90 通り</text>
</svg>

- **【分步标准解答】**
  - **[1] 机の上での円順列**：
    異なる $6$ 個の円順列であるから、
    $$(6 - 1)! = 5! = 120 \text{（通り）}$$

  - **[2] 首飾り（じゅず順列）**：
    首飾りは空間で裏返すことができるため、回転して一致するものだけでなく、裏返して一致するものも同じ $1$ 種類とみなす。
    よって、[1] の円順列の総数を $2$ で割って、
    $$\frac{(6 - 1)!}{2} = \frac{120}{2} = 60 \text{（種類）}$$
    > 💡 讲师批注：区分「在桌上排成圆（不可翻转，円順列）」与「做成项链（可翻转，じゅず順列）」，前者不除以 $2$，后者必须除以 $2$！

  - **[3] $6$ 個から $4$ 個取り出して円形に並べる**：
    まず $6$ 個から $4$ 個を取り出して $1$ 列に並べる方法は ${}_6\mathrm{P}_4$ 通り。
    円形に並べると、回転によって $4$ 通りずつ同じ並びができるから、
    $$\frac{{}_6\mathrm{P}_4}{4} = \frac{6 \times 5 \times 4 \times 3}{4} = 90 \text{（通り）}$$
    > 💡 讲师批注：也可理解为「先从 6 颗中选 4 颗（${}_6\mathrm{C}_4 = 15$），再将这 4 颗做圆排列（$(4-1)! = 6$）」，得 $15 \times 6 = 90$ 通り，两种思路完全一致！

- **【最终答案】**
  - **[1] $120$ 通り　　[2] $60$ 種類　　[3] $90$ 通り**
