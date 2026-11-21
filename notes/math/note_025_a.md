# 《EJU 教材全解与备课讲义》数学 025-A（P361–P375 上）

> **对应源文件**：`work_math/ocr_md/ocr_025_p361-375.md`（第 15 章《不定積分》之「演習問題 13-(5)～(30)」全解析 + 第 16 章《定積分とその基本性質》之【16.1】～【16.7】）
> **视觉核对参考图**：`work_math/ref_imgs/page_0361.jpg` – `page_0375.jpg`（全 15 页均已逐字逐符号核对原图）
> **拆分说明**：本切片共含 26 个大题号、**41 道独立不定积分计算与证明题**，且涵盖定积分核心概念。为避免截断、保证每步推导零跳步，拆分为 `note_025_a.md`（知识点总览 + 词汇 + 演習問題 13-(5)～(17)）与 `note_025_b.md`（演習問題 13-(18)～(30) + 积分技巧速查表）。

---

## 一、国内高中基础知识点唤醒与 EJU 考纲差异对比

本切片前半部分（P361–P373）是对**不定积分（不定積分）**各类进阶技巧的集中高强度演练，涵盖**换元积分法、分部积分法、部分分式分解、分母有理化、三角函数恒等变形、循环分部积分、递推公式**；后半部分（P373–P375）正式开启**定积分及其基本性质（定積分とその基本性質）**。

### 1.1 不定积分核心策略决策图（SVG 矢量流程图）

面对一道复杂的不定积分题，学生在考场上最怕「不知道该换元还是分部」。教学时可直接给出以下决策树：

<svg viewBox="0 0 760 285" width="100%" xmlns="http://www.w3.org/2000/svg" style="background:#fafafa;border:1px solid #e2e8f0;border-radius:8px;margin:12px 0;">
  <defs>
    <marker id="arr" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#475569"/>
    </marker>
  </defs>
  <!-- Root -->
  <rect x="260" y="14" width="240" height="38" rx="8" fill="#1e3a8a"/>
  <text x="380" y="38" text-anchor="middle" fill="#ffffff" font-size="14" font-weight="bold">不定积分 ∫ f(x) dx 识别入口</text>
  <!-- Branches -->
  <line x1="300" y1="52" x2="115" y2="92" stroke="#475569" stroke-width="1.6" marker-end="url(#arr)"/>
  <line x1="355" y1="52" x2="295" y2="92" stroke="#475569" stroke-width="1.6" marker-end="url(#arr)"/>
  <line x1="405" y1="52" x2="465" y2="92" stroke="#475569" stroke-width="1.6" marker-end="url(#arr)"/>
  <line x1="460" y1="52" x2="645" y2="92" stroke="#475569" stroke-width="1.6" marker-end="url(#arr)"/>

  <!-- Col 1: Substitution -->
  <rect x="25" y="96" width="180" height="44" rx="6" fill="#dbeafe" stroke="#2563eb" stroke-width="1.4"/>
  <text x="115" y="115" text-anchor="middle" fill="#1e40af" font-size="13" font-weight="bold">① 换元积分法</text>
  <text x="115" y="132" text-anchor="middle" fill="#1e3a8a" font-size="11">f(g(x))g'(x) 或含根号</text>
  <line x1="115" y1="140" x2="115" y2="168" stroke="#2563eb" stroke-width="1.4" marker-end="url(#arr)"/>
  <rect x="20" y="172" width="190" height="96" rx="6" fill="#ffffff" stroke="#93c5fd" stroke-width="1.2"/>
  <text x="115" y="193" text-anchor="middle" fill="#334155" font-size="11.5">• 凑微分：f'(x)/f(x) → log|f|</text>
  <text x="115" y="213" text-anchor="middle" fill="#334155" font-size="11.5">• 根式代换：t = √(ax+b)</text>
  <text x="115" y="233" text-anchor="middle" fill="#334155" font-size="11.5">• 欧拉代换：t = x + √(x²+1)</text>
  <text x="115" y="253" text-anchor="middle" fill="#334155" font-size="11.5">• 三角代换：x = a tanθ / a sinθ</text>

  <!-- Col 2: Rational -->
  <rect x="215" y="96" width="160" height="44" rx="6" fill="#dcfce7" stroke="#16a34a" stroke-width="1.4"/>
  <text x="295" y="115" text-anchor="middle" fill="#166534" font-size="13" font-weight="bold">② 有理分式/根式化简</text>
  <text x="295" y="132" text-anchor="middle" fill="#14532d" font-size="11">分母可因式分解或含和差根式</text>
  <line x1="295" y1="140" x2="295" y2="168" stroke="#16a34a" stroke-width="1.4" marker-end="url(#arr)"/>
  <rect x="215" y="172" width="160" height="96" rx="6" fill="#ffffff" stroke="#86efac" stroke-width="1.2"/>
  <text x="295" y="193" text-anchor="middle" fill="#334155" font-size="11.5">• 真分式：部分分式分解</text>
  <text x="295" y="213" text-anchor="middle" fill="#334155" font-size="11.5">• 假分式：先多项式除法</text>
  <text x="295" y="233" text-anchor="middle" fill="#334155" font-size="11.5">• 分母含 √A ± √B：</text>
  <text x="295" y="251" text-anchor="middle" fill="#334155" font-size="11.5">  优先分母有理化！</text>

  <!-- Col 3: Trig -->
  <rect x="385" y="96" width="160" height="44" rx="6" fill="#fef3c7" stroke="#d97706" stroke-width="1.4"/>
  <text x="465" y="115" text-anchor="middle" fill="#92400e" font-size="13" font-weight="bold">③ 三角函数变形</text>
  <text x="465" y="132" text-anchor="middle" fill="#78350f" font-size="11">高次幂 / 异角乘积 / 倒数</text>
  <line x1="465" y1="140" x2="465" y2="168" stroke="#d97706" stroke-width="1.4" marker-end="url(#arr)"/>
  <rect x="385" y="172" width="160" height="96" rx="6" fill="#ffffff" stroke="#fcd34d" stroke-width="1.2"/>
  <text x="465" y="193" text-anchor="middle" fill="#334155" font-size="11.5">• 奇次幂：拆 1 次凑微分</text>
  <text x="465" y="213" text-anchor="middle" fill="#334155" font-size="11.5">• 偶次幂：半角降幂公式</text>
  <text x="465" y="233" text-anchor="middle" fill="#334155" font-size="11.5">• 异角乘积：积化和差</text>
  <text x="465" y="253" text-anchor="middle" fill="#334155" font-size="11.5">• 1/(sin+cos)：先合成</text>

  <!-- Col 4: Parts -->
  <rect x="555" y="96" width="185" height="44" rx="6" fill="#fce7f3" stroke="#db2777" stroke-width="1.4"/>
  <text x="647" y="115" text-anchor="middle" fill="#9d174d" font-size="13" font-weight="bold">④ 分部积分法</text>
  <text x="647" y="132" text-anchor="middle" fill="#831843" font-size="11">两类不同函数相乘 / 单 log</text>
  <line x1="647" y1="140" x2="647" y2="168" stroke="#db2777" stroke-width="1.4" marker-end="url(#arr)"/>
  <rect x="555" y="172" width="185" height="96" rx="6" fill="#ffffff" stroke="#f9a8d4" stroke-width="1.2"/>
  <text x="647" y="193" text-anchor="middle" fill="#334155" font-size="11.5">• 选微分侧优先级：</text>
  <text x="647" y="212" text-anchor="middle" fill="#be185d" font-size="11.5" font-weight="bold">反三角 &gt; 对数 &gt; 幂 &gt; 三角 ≈ 指数</text>
  <text x="647" y="233" text-anchor="middle" fill="#334155" font-size="11.5">• e^(ax)·sin/cos：两次循环</text>
  <text x="647" y="253" text-anchor="middle" fill="#334155" font-size="11.5">• sin^n x：构造递推式 I_n</text>
</svg>

### 1.2 定积分的定义与几何意义（【16.1】定積分）

- **定义**：设 $F'(x) = f(x)$，函数 $f(x)$ 在闭区间 $[a, b]$ 上连续，则称
  $$\int_a^b f(x)\,dx = \Big[F(x)\Big]_a^b = F(b) - F(a)$$
  为 $f(x)$ 在 $[a, b]$ 上的**定积分（定積分）**，其中 $a$ 称**下端（かたん）**，$b$ 称**上端（じょうたん）**。
- **几何意义（带符号面积）**：曲线 $y = f(x)$ 与直线 $x=a$、$x=b$ 及 $x$ 轴所围成的面积，在 **$x$ 轴上方记为正（$+$），在 $x$ 轴下方记为负（$-$）**。
- **上下限约定**：
  - 当 $a > b$ 时：$\displaystyle \int_a^b f(x)\,dx = -\int_b^a f(x)\,dx$
  - 当 $a = b$ 时：$\displaystyle \int_a^a f(x)\,dx = 0$

<svg viewBox="0 0 680 210" width="100%" xmlns="http://www.w3.org/2000/svg" style="background:#fafafa;border:1px solid #e2e8f0;border-radius:8px;margin:12px 0;">
  <!-- Left panel: Signed area [16.1] -->
  <text x="170" y="22" text-anchor="middle" fill="#1e293b" font-size="13" font-weight="bold">【16.1】定积分的带符号面积</text>
  <!-- x-axis -->
  <line x1="25" y1="115" x2="315" y2="115" stroke="#334155" stroke-width="1.5"/>
  <polygon points="315,115 307,111 307,119" fill="#334155"/>
  <text x="322" y="119" fill="#334155" font-size="12" font-style="italic">x</text>
  <!-- Shaded regions -->
  <!-- Negative left -->
  <path d="M 55 115 L 55 142 Q 70 148 88 115 Z" fill="#fecaca" opacity="0.8"/>
  <!-- Positive middle -->
  <path d="M 88 115 Q 135 35 182 115 Z" fill="#bbf7d0" opacity="0.8"/>
  <!-- Negative right-mid -->
  <path d="M 182 115 Q 222 185 256 115 Z" fill="#fecaca" opacity="0.8"/>
  <!-- Positive far right -->
  <path d="M 256 115 Q 275 82 288 86 L 288 115 Z" fill="#bbf7d0" opacity="0.8"/>
  <!-- Curve y=f(x) -->
  <path d="M 42 125 Q 58 158 88 115 Q 135 35 182 115 Q 222 185 256 115 Q 278 74 300 98" fill="none" stroke="#1e40af" stroke-width="2.2"/>
  <!-- Vertical lines x=a, x=b -->
  <line x1="55" y1="42" x2="55" y2="175" stroke="#475569" stroke-width="1.4" stroke-dasharray="4,3"/>
  <line x1="288" y1="42" x2="288" y2="175" stroke="#475569" stroke-width="1.4" stroke-dasharray="4,3"/>
  <text x="55" y="38" text-anchor="middle" fill="#475569" font-size="11.5">x = a</text>
  <text x="288" y="38" text-anchor="middle" fill="#475569" font-size="11.5">x = b</text>
  <text x="64" y="109" fill="#1e293b" font-size="11.5" font-style="italic">a</text>
  <text x="276" y="130" fill="#1e293b" font-size="11.5" font-style="italic">b</text>
  <text x="180" y="65" fill="#1e40af" font-size="12" font-style="italic">y = f(x)</text>
  <!-- Signs -->
  <circle cx="68" cy="128" r="8" fill="#ffffff" stroke="#dc2626" stroke-width="1.2"/>
  <text x="68" y="132" text-anchor="middle" fill="#dc2626" font-size="12" font-weight="bold">−</text>
  <circle cx="135" cy="94" r="9" fill="#ffffff" stroke="#16a34a" stroke-width="1.2"/>
  <text x="135" y="98" text-anchor="middle" fill="#16a34a" font-size="12" font-weight="bold">+</text>
  <circle cx="220" cy="136" r="9" fill="#ffffff" stroke="#dc2626" stroke-width="1.2"/>
  <text x="220" y="140" text-anchor="middle" fill="#dc2626" font-size="12" font-weight="bold">−</text>
  <circle cx="274" cy="103" r="8" fill="#ffffff" stroke="#16a34a" stroke-width="1.2"/>
  <text x="274" y="107" text-anchor="middle" fill="#16a34a" font-size="12" font-weight="bold">+</text>

  <!-- Divider -->
  <line x1="348" y1="18" x2="348" y2="192" stroke="#cbd5e1" stroke-width="1.2"/>

  <!-- Right panel: Absolute value [16.3] -->
  <text x="515" y="22" text-anchor="middle" fill="#1e293b" font-size="13" font-weight="bold">【16.3】绝对值函数的定积分</text>
  <!-- Axes -->
  <line x1="375" y1="135" x2="650" y2="135" stroke="#334155" stroke-width="1.5"/>
  <polygon points="650,135 642,131 642,139" fill="#334155"/>
  <text x="656" y="139" fill="#334155" font-size="12" font-style="italic">x</text>
  <line x1="415" y1="185" x2="415" y2="42" stroke="#334155" stroke-width="1.5"/>
  <polygon points="415,42 411,50 419,50" fill="#334155"/>
  <text x="403" y="48" fill="#334155" font-size="12" font-style="italic">y</text>
  <text x="404" y="149" fill="#334155" font-size="11.5">O</text>
  <!-- Shaded area under y=|f(x)| -->
  <path d="M 440 135 L 440 100 Q 470 122 495 135 Z" fill="#dbeafe" opacity="0.85"/>
  <path d="M 495 135 Q 545 108 605 95 L 605 135 Z" fill="#fef3c7" opacity="0.9"/>
  <!-- Original curve y=f(x) below x-axis (dashed) -->
  <path d="M 495 135 Q 545 162 630 180" fill="none" stroke="#64748b" stroke-width="1.6" stroke-dasharray="5,4"/>
  <!-- Curve y=|f(x)| solid -->
  <path d="M 385 52 Q 435 104 495 135 Q 545 108 630 90" fill="none" stroke="#1e40af" stroke-width="2.2"/>
  <!-- Vertical lines a, b -->
  <line x1="440" y1="100" x2="440" y2="135" stroke="#2563eb" stroke-width="1.4"/>
  <line x1="605" y1="95" x2="605" y2="135" stroke="#d97706" stroke-width="1.4"/>
  <text x="440" y="150" text-anchor="middle" fill="#1e293b" font-size="11.5" font-style="italic">a</text>
  <text x="495" y="150" text-anchor="middle" fill="#1e293b" font-size="11.5" font-style="italic">c</text>
  <text x="605" y="150" text-anchor="middle" fill="#1e293b" font-size="11.5" font-style="italic">b</text>
  <text x="580" y="78" fill="#1e40af" font-size="12" font-weight="bold">y = |f(x)|</text>
  <text x="585" y="190" fill="#64748b" font-size="11.5" font-style="italic">y = f(x)</text>
  <text x="462" y="128" text-anchor="middle" fill="#1e40af" font-size="10.5">+f(x)</text>
  <text x="556" y="124" text-anchor="middle" fill="#b45309" font-size="10.5">−f(x)</text>
</svg>

### 1.3 定积分的基本性质与计算公式（【16.2】–【16.7】）

1. **基本性质（【16.2】）**（$k, l$ 为常数）：
   - `[1]` 积分变量无关性：$\displaystyle \int_a^b f(x)\,dx = \int_a^b f(t)\,dt$
   - `[2]` 常数倍提取：$\displaystyle \int_a^b k f(x)\,dx = k\int_a^b f(x)\,dx$
   - `[3]` 可加性：$\displaystyle \int_a^b \{f(x)+g(x)\}\,dx = \int_a^b f(x)\,dx + \int_a^b g(x)\,dx$
   - `[4]` 线性性：$\displaystyle \int_a^b \{k f(x) + l g(x)\}\,dx = k\int_a^b f(x)\,dx + l\int_a^b g(x)\,dx$
   - `[5]` 上下限互换变号：$\displaystyle \int_a^b f(x)\,dx = -\int_b^a f(x)\,dx$，特别地 $\displaystyle \int_a^a f(x)\,dx = 0$
   - `[6]` 积分区间可拆性：$\displaystyle \int_a^b f(x)\,dx = \int_a^c f(x)\,dx + \int_c^b f(x)\,dx$
   > ⚠️ **教材勘误提示（P373 / `page_0374.jpg`）**：
   > - 原教材【16.2】`[5]` 右侧误印为 $-\int_a^b f(x)\,dx$（上下限未互换），正确应为 $-\int_b^a f(x)\,dx$。
   > - 原教材【16.2】`[6]` 末项误印为 $\int_c^b f(x)\,dt$（微分变量误作 $dt$），正确应为 $\int_c^b f(x)\,dx$。
   > - 另外，P374（`page_0375.jpg`）页眉虽标「定積分とその基本性質」，但底部【16.1】【16.2】解説框内实际错植了「不定積分」与「不定積分の性質」的说明文字，备课时需向学生说明。

2. **含绝对值函数的定积分（【16.3】）**：
   若 $a \le x \le c$ 时 $f(x) \ge 0$，$c \le x \le b$ 时 $f(x) \le 0$，则以零点 $c$ 为界拆分区间去绝对值：
   $$\int_a^b |f(x)|\,dx = \int_a^c f(x)\,dx + \int_c^b \{-f(x)\}\,dx$$

3. **定积分的换元积分法（【16.4】）**（**切记同步更换上下限！**）：
   - 形式 `[1]`：令 $x = g(t)$，当 $t: \alpha \to \beta$ 时 $x: a \to b$（即 $a = g(\alpha),\; b = g(\beta)$），则
     $$\int_a^b f(x)\,dx = \int_\alpha^\beta f(g(t)) g'(t)\,dt$$
   - 形式 `[2]`：令 $t = g(x)$，当 $x: a \to b$ 时 $t: \alpha \to \beta$（即 $\alpha = g(a),\; \beta = g(b)$），则
     $$\int_a^b f(g(x)) g'(x)\,dx = \int_\alpha^\beta f(t)\,dt$$

4. **偶函数、奇函数在对称区间 $[-\alpha, \alpha]$ 上的定积分（【16.5】）**：
   - 偶函数（$f(-x) = f(x)$）：$\displaystyle \int_{-\alpha}^\alpha f(x)\,dx = 2\int_0^\alpha f(x)\,dx$
   - 奇函数（$f(-x) = -f(x)$）：$\displaystyle \int_{-\alpha}^\alpha f(x)\,dx = 0$

5. **定积分的分部积分法（【16.6】）**：
   $$\int_a^b f(x) g'(x)\,dx = \Big[f(x) g(x)\Big]_a^b - \int_a^b f'(x) g(x)\,dx$$
   特别地，取 $g'(x) = 1 \implies g(x) = x$ 时：
   $$\int_a^b f(x)\,dx = \Big[x f(x)\Big]_a^b - \int_a^b x f'(x)\,dx$$

6. **定积分与递推公式（【16.7】）**：
   对含整数参数 $n$ 的积分（如 $\int \sin^n x\,dx$、$\int_0^{\pi/2} \sin^n x\,dx$），利用分部积分法建立 $I_n$ 与 $I_{n-2}$（或 $I_{n-1}$）的递推关系（漸化式），详见演習問題 13-(30)。

### 1.4 国内高中 vs. 日本 EJU 考纲差异对比

| 对比维度 | 国内高中（新高考） | 日本 EJU（数学Ⅲ・课程2） | 备课/应试提醒 |
| :--- | :--- | :--- | :--- |
| **微积分深度** | 新高考已大幅删减定积分，仅保留导数基础；换元积分、分部积分属于大学高数内容 | **必考核心压轴板块！** 涵盖几乎全部大学高数一元积分技巧 | 国内转轨学生必须把本切片 41 题作为肌肉记忆反复刷透 |
| **自然对数记号** | 写作 $\ln x$ | **无底数 $\log x$ 即表示自然对数 $\log_e x$** | 切勿误认为常用对数 $\log_{10} x$！ |
| **反三角函数记号** | 写作 $\arcsin x,\; \arctan x$ | 日本教材与考卷普遍写作 **$\sin^{-1} x,\; \tan^{-1} x$** | 注意 $\sin^{-1} x$ 是反函数，**绝不是** $\frac{1}{\sin x}$！ |
| **牛顿-莱布尼茨括号** | 常写作 $F(x)\Big|_a^b$ | 日本统一用方括号 **$\Big[F(x)\Big]_a^b$** | 考场书写与阅卷均以方括号为准 |
| **积分常数书写** | 写 $+C$ 即可 | 日本标准答案须注明 **「$C$ は積分定数」**（$C$ 为积分常数） | 养成每题末尾标注的习惯 |

---

## 二、日文核心词汇与公式假名注音

### 2.1 本切片日文核心词汇

- 不定積分（ふていせきぶん / futei sekibun） — 不定积分
- 原始関数（げんしかんすう / genshi kansuu） — 原函数
- 被積分関数（ひせきぶんかんすう / hisekibun kansuu） — 被积函数
- 積分変数（せきぶんへんすう / sekibun hensuu） — 积分变量
- 積分定数（せきぶんていすう / sekibun teisuu） — 积分常数
- 積分する（せきぶんする / sekibun suru） — 求积分、积分
- 置換積分法（ちかんせきぶんほう / chikan sekibunhou） — 换元积分法
- 部分積分法（ぶぶんせきぶんほう / bubun sekibunhou） — 分部积分法
- 定積分（ていせきぶん / tei sekibun） — 定积分
- 上端（じょうたん / joutan） — 积分上限（上端）
- 下端（かたん / katan） — 积分下限（下端）
- 積分区間（せきぶんくかん / sekibun kukan） — 积分区间
- 逆三角関数（ぎゃくさんかくかんすう / gyaku sankaku kansuu） — 反三角函数
- 勘定する（かんじょうする / kanjou suru） — 计算、计入（按正负号计入面积）

### 2.2 核心公式的日本课堂口语读法

1. **不定积分定义** $\displaystyle \int f(x)\,dx = F(x) + C$
   - 课堂读法：**インテグラル エフ・エックス ディーエックス イコール ラージエフ・エックス たす シー**
   - 备注：积分号 $\int$ 读作 **インテグラル（integral）**，大写字母 $F$ 读作 **ラージエフ（large F）**。
2. **定积分定义** $\displaystyle \int_a^b f(x)\,dx = \Big[F(x)\Big]_a^b = F(b) - F(a)$
   - 课堂读法：**インテグラル エーからビーまでの エフ・エックス ディーエックス イコール だいかっこ ラージエフ・エックス エーからビーまで イコール ラージエフ・ビー ひく ラージエフ・エー**
3. **对数型积分公式** $\displaystyle \int \frac{f'(x)}{f(x)}\,dx = \log|f(x)| + C$
   - 课堂读法：**インテグラル エフ・エックス ぶんの エフダッシュ・エックス ディーエックス イコール ログ ぜったいち エフ・エックス たす シー**
4. **反三角函数** $\sin^{-1} x,\; \tan^{-1} x$
   - 课堂读法：**アークサイン エックス**（或 **サインインバース エックス**）、**アークタンジェント エックス**（或 **タンジェントインバース エックス**）。

---

## 三、逐题深度解析（上：演習問題 13-(5) ～ 13-(17)）

---

### 演習問題 13-(5)（P361 / 教材 P360）

- **【原题重现与翻译】**
  - 原题：$f'(x) = 3x^2 - 2x,\; f(2) = 0$ を満たす関数 $f(x)$ を求めよ。
  - 中文：求满足 $f'(x) = 3x^2 - 2x$ 且 $f(2) = 0$ 的函数 $f(x)$。
- **【考点定位】**
  - 多项式的不定积分 + 利用初始条件确定积分常数 $C$。
- **【分步标准解答】**
  $$f(x) = \int (3x^2 - 2x)\,dx = 3 \cdot \frac{1}{3}x^3 - 2 \cdot \frac{1}{2}x^2 + C = x^3 - x^2 + C \quad (C \text{ は積分定数})$$
  > 💡 讲师批注：由 $f'(x)$ 反推 $f(x)$ 即求不定积分，切忌漏写积分常数 $C$。

  $f(2) = 0$ より，
  $$2^3 - 2^2 + C = 0 \iff 8 - 4 + C = 0 \iff C = -4$$
  > 💡 讲师批注：将 $x=2$ 代入解得 $C=-4$，最后口算验算 $f'(x)=3x^2-2x$ 且 $f(2)=8-4-4=0$。
- **【最终答案】**
  **$f(x) = x^3 - x^2 - 4$**

---

### 演習問題 13-(6)（P361 / 教材 P360）

- **【原题重现与翻译】**
  - 原题：曲線 $y = f(x)$ が点 $(1, 0)$ を通り、更に点 $(x, f(x))$ における接線の傾きが $x^2 - 1$ であるとき、$f(x)$ を求めよ。
  - 中文：曲线 $y = f(x)$ 经过点 $(1, 0)$，且在点 $(x, f(x))$ 处的切线斜率为 $x^2 - 1$，求 $f(x)$。
- **【考点定位】**
  - 导数的几何意义（切线斜率 $= f'(x)$）+ 不定积分求原函数。
- **【分步标准解答】**
  点 $(x, f(x))$ における接線の傾きが $x^2 - 1$ であるから，
  $$f'(x) = x^2 - 1$$
  > 💡 讲师批注：将几何条件「接線の傾き」翻译为解析条件 $f'(x) = x^2 - 1$，将「点 $(1,0)$ を通る」翻译为 $f(1) = 0$。

  よって，
  $$f(x) = \int (x^2 - 1)\,dx = \frac{1}{3}x^3 - x + C \quad (C \text{ は積分定数})$$
  曲線は点 $(1, 0)$ を通るから，$f(1) = 0$ より，
  $$\frac{1}{3} \cdot 1^3 - 1 + C = 0 \iff -\frac{2}{3} + C = 0 \iff C = \frac{2}{3}$$
  > 💡 讲师批注：验算：$f'(x) = x^2 - 1$，$f(1) = \frac{1}{3} - 1 + \frac{2}{3} = 0$，完全吻合。
- **【最终答案】**
  **$f(x) = \dfrac{1}{3}x^3 - x + \dfrac{2}{3}$**

---

### 演習問題 13-(7)（P361 / 教材 P360）

- **【原题重现与翻译】**
  - 原题：微分可能な関数 $f(x)$ が $f'(x) = |e^x - 1|$ を満たし、$f(1) = e$ であるとき、$f(x)$ を求めよ。
  - 中文：可微函数 $f(x)$ 满足 $f'(x) = |e^x - 1|$，且 $f(1) = e$，求 $f(x)$。
- **【考点定位】**
  - 含绝对值导函数的分段积分 + 利用「可微必连续」在分界点 $x=0$ 处拼接两段积分常数。
- **【图解辅助（SVG 矢量图）】**

<svg viewBox="0 0 560 200" width="100%" xmlns="http://www.w3.org/2000/svg" style="background:#fafafa;border:1px solid #e2e8f0;border-radius:8px;margin:10px 0;">
  <!-- Left: y = f'(x) = |e^x - 1| -->
  <text x="135" y="20" text-anchor="middle" fill="#1e293b" font-size="12.5" font-weight="bold">导函数 f'(x) = |eˣ − 1|</text>
  <line x1="25" y1="155" x2="250" y2="155" stroke="#334155" stroke-width="1.3"/>
  <line x1="130" y1="175" x2="130" y2="35" stroke="#334155" stroke-width="1.3"/>
  <text x="255" y="159" fill="#334155" font-size="11.5" font-style="italic">x</text>
  <text x="120" y="42" fill="#334155" font-size="11.5" font-style="italic">y</text>
  <text x="120" y="168" fill="#334155" font-size="11">O</text>
  <!-- y=1-e^x for x<0 -->
  <path d="M 35 110 Q 85 116 130 155" fill="none" stroke="#db2777" stroke-width="2"/>
  <line x1="25" y1="105" x2="130" y2="105" stroke="#94a3b8" stroke-width="1" stroke-dasharray="3,3"/>
  <text x="135" y="108" fill="#64748b" font-size="10.5">1</text>
  <!-- y=e^x-1 for x>=0 -->
  <path d="M 130 155 Q 175 140 215 48" fill="none" stroke="#2563eb" stroke-width="2"/>
  <text x="68" y="95" fill="#db2777" font-size="11">1 − eˣ (x&lt;0)</text>
  <text x="195" y="88" fill="#2563eb" font-size="11">eˣ − 1 (x≥0)</text>

  <!-- Divider -->
  <line x1="280" y1="16" x2="280" y2="184" stroke="#cbd5e1" stroke-width="1.2"/>

  <!-- Right: y = f(x) continuous & smooth at x=0 -->
  <text x="420" y="20" text-anchor="middle" fill="#1e293b" font-size="12.5" font-weight="bold">原函数 f(x) 在 x=0 处光滑拼接</text>
  <line x1="305" y1="160" x2="535" y2="160" stroke="#334155" stroke-width="1.3"/>
  <line x1="415" y1="180" x2="415" y2="35" stroke="#334155" stroke-width="1.3"/>
  <text x="540" y="164" fill="#334155" font-size="11.5" font-style="italic">x</text>
  <text x="404" y="42" fill="#334155" font-size="11.5" font-style="italic">y</text>
  <text x="404" y="173" fill="#334155" font-size="11">O</text>
  <!-- x<0: x - e^x + 3 (at x=0, y=2, slope=0; x=-1, y=2-1/e≈1.63; x=-2, y=1-e^-2≈0.86) -->
  <path d="M 325 145 Q 370 112 415 108" fill="none" stroke="#db2777" stroke-width="2.2"/>
  <!-- x>=0: e^x - x + 1 (at x=0, y=2; x=1, y=e≈2.72) -->
  <path d="M 415 108 Q 465 104 510 52" fill="none" stroke="#2563eb" stroke-width="2.2"/>
  <circle cx="415" cy="108" r="4" fill="#16a34a"/>
  <text x="424" y="122" fill="#16a34a" font-size="11" font-weight="bold">(0, 2) 连续拼接</text>
  <circle cx="475" cy="86" r="3.5" fill="#2563eb"/>
  <text x="482" y="90" fill="#2563eb" font-size="11">(1, e)</text>
</svg>

- **【分步标准解答】**
  $e^x - 1 = 0 \iff x = 0$ であるから，$x$ の符号によって場合分けする。
  - $x \ge 0$ のとき，$e^x - 1 \ge 0$ より $f'(x) = e^x - 1$。積分して，
    $$f(x) = \int (e^x - 1)\,dx = e^x - x + C_1 \quad (C_1 \text{ は積分定数})$$
  - $x < 0$ のとき，$e^x - 1 < 0$ より $f'(x) = -(e^x - 1) = 1 - e^x$。積分して，
    $$f(x) = \int (1 - e^x)\,dx = x - e^x + C_2 \quad (C_2 \text{ は積分定数})$$
  > 💡 讲师批注：**极易错点！** 分段区间各自积分时，**两段的积分常数 $C_1, C_2$ 一般不相等**，必须用不同的字母标记！

  条件 $f(1) = e$（$1 \ge 0$ なので第1式を用いる）より，
  $$e^1 - 1 + C_1 = e \implies C_1 = 1$$
  よって，$x \ge 0$ のとき $f(x) = e^x - x + 1$。特に $f(0) = e^0 - 0 + 1 = 2$。

  また，$f(x)$ はすべての実数で微分可能であるから，$x = 0$ で連続である。したがって，
  $$\lim_{x \to -0} f(x) = f(0)$$
  $$\lim_{x \to -0} (x - e^x + C_2) = 2 \implies 0 - 1 + C_2 = 2 \implies C_2 = 3$$
  > 💡 讲师批注：由于 $x=0$ 处左右导数均为 $0$（$e^0-1 = 1-e^0 = 0$），只要 $x=0$ 处连续，函数就在 $x=0$ 处可微。
- **【最终答案】**
  **$f(x) = \begin{cases} e^x - x + 1 & (x \ge 0) \\ x - e^x + 3 & (x < 0) \end{cases}$**

---

### 演習問題 13-(8)（P362 / 教材 P361）

#### 演習問題 13-(8)[1]
- **【原题重现与翻译】**
  - 原题：次の不定積分を求めよ。$\displaystyle \int (2x + 1)\sqrt{x + 2}\,dx$
  - 中文：求不定积分 $\displaystyle \int (2x + 1)\sqrt{x + 2}\,dx$。
- **【考点定位】**
  - 换元积分法（一次根式代换 $t = x + 2$）。
- **【分步标准解答】**
  $t = x + 2$ とおくと，$x = t - 2,\; dx = dt$ であり，$2x + 1 = 2(t - 2) + 1 = 2t - 3$ となる。
  $$\int (2x + 1)\sqrt{x + 2}\,dx = \int (2t - 3) t^{\frac{1}{2}}\,dt = \int \left(2t^{\frac{3}{2}} - 3t^{\frac{1}{2}}\right)dt$$
  > 💡 讲师批注：对于 $(ax+b)\sqrt{cx+d}$ 型，令根号内部 $t = x+2$（或直接令 $u = \sqrt{x+2}$）即可将根号外的一次式化为关于 $t$ 的多项式，逐项套用幂函数积分公式。

  $$= 2 \cdot \frac{2}{5}t^{\frac{5}{2}} - 3 \cdot \frac{2}{3}t^{\frac{3}{2}} + C = \frac{4}{5}t^{\frac{5}{2}} - 2t^{\frac{3}{2}} + C$$
  $$= \frac{2}{5}t^{\frac{3}{2}}(2t - 5) + C = \frac{2}{5}(x + 2)\sqrt{x + 2}\,(2x - 1) + C \quad (C \text{ は積分定数})$$
  > 💡 讲师批注：最后一步提取公因式 $\frac{2}{5}t^{\frac{3}{2}}$ 是日本标准解答的规范整理形式（$2t - 5 = 2(x+2)-5 = 2x-1$）。求导验算：$\frac{2}{5}[\frac{3}{2}\sqrt{x+2}(2x-1) + 2(x+2)\sqrt{x+2}] = (2x+1)\sqrt{x+2}$。✓
- **【最终答案】**
  **$\dfrac{2}{5}(2x - 1)(x + 2)\sqrt{x + 2} + C$**（$C$ 为积分常数）

---

#### 演習問題 13-(8)[2]
- **【原题重现与翻译】**
  - 原题：次の不定積分を求めよ。$\displaystyle \int \frac{e^{2x}}{(e^x + 1)^2}\,dx$
  - 中文：求不定积分 $\displaystyle \int \frac{e^{2x}}{(e^x + 1)^2}\,dx$。
- **【考点定位】**
  - 换元积分法（指数函数代换 $t = e^x + 1$）。
- **【分步标准解答】**
  $t = e^x + 1$ とおくと，$e^x = t - 1$，$dt = e^x\,dx$ である。
  $$\int \frac{e^{2x}}{(e^x + 1)^2}\,dx = \int \frac{e^x}{(e^x + 1)^2} \cdot e^x\,dx = \int \frac{t - 1}{t^2}\,dt$$
  > 💡 讲师批注：把分子的 $e^{2x}$ 拆成 $e^x \cdot e^x$，其中一份正好与 $dx$ 配成 $dt = e^x\,dx$。

  $$= \int \left(\frac{1}{t} - t^{-2}\right)dt = \log|t| + \frac{1}{t} + C$$
  $t = e^x + 1 > 0$ より絶対値記号を外して，
  $$= \log(e^x + 1) + \frac{1}{e^x + 1} + C \quad (C \text{ は積分定数})$$
  > 💡 讲师批注：因为 $e^x + 1$ 恒大于 $0$，日本考场习惯去掉 $\log$ 内的绝对值符号。求导验算：$\frac{e^x}{e^x+1} - \frac{e^x}{(e^x+1)^2} = \frac{e^{2x}}{(e^x+1)^2}$。✓
- **【最终答案】**
  **$\log(e^x + 1) + \dfrac{1}{e^x + 1} + C$**（$C$ 为积分常数）

---

### 演習問題 13-(9)（P362 / 教材 P361）

#### 演習問題 13-(9)[1]
- **【原题重现与翻译】**
  - 原题：次の不定積分を求めよ。$\displaystyle \int x e^{-\frac{x^2}{2}}\,dx$
  - 中文：求不定积分 $\displaystyle \int x e^{-\frac{x^2}{2}}\,dx$。
- **【考点定位】**
  - 换元积分法（凑微分型 $\int f(g(x))g'(x)\,dx$）。
- **【分步标准解答】**
  $t = -\dfrac{x^2}{2}$ とおくと，$\dfrac{dt}{dx} = -x$ より $x\,dx = -dt$。
  $$\int x e^{-\frac{x^2}{2}}\,dx = \int e^t (-dt) = -\int e^t\,dt = -e^t + C = -e^{-\frac{x^2}{2}} + C \quad (C \text{ は積分定数})$$
  > 💡 讲师批注：看到指数上有 $x^2$ 而外面乘了 $x$，立刻敏锐识别出 $(-\frac{x^2}{2})' = -x$。求导验算：$-e^{-x^2/2}\cdot(-x) = x e^{-x^2/2}$。✓
- **【最终答案】**
  **$-e^{-\frac{x^2}{2}} + C$**（$C$ 为积分常数）

---

#### 演習問題 13-(9)[2]
- **【原题重现与翻译】**
  - 原题：次の不定積分を求めよ。$\displaystyle \int \sin^3 x \cos x\,dx$
  - 中文：求不定积分 $\displaystyle \int \sin^3 x \cos x\,dx$。
- **【考点定位】**
  - 换元积分法（三角函数凑微分）。
- **【分步标准解答】**
  $t = \sin x$ とおくと，$dt = \cos x\,dx$ であるから，
  $$\int \sin^3 x \cos x\,dx = \int t^3\,dt = \frac{1}{4}t^4 + C = \frac{1}{4}\sin^4 x + C \quad (C \text{ は積分定数})$$
  > 💡 讲师批注：直接利用 $\int \{f(x)\}^\alpha f'(x)\,dx = \frac{1}{\alpha+1}\{f(x)\}^{\alpha+1} + C$ 也可一步写出答案。✓
- **【最终答案】**
  **$\dfrac{1}{4}\sin^4 x + C$**（$C$ 为积分常数）

---

### 演習問題 13-(10)（P363 / 教材 P362）

#### 演習問題 13-(10)[1]
- **【原题重现与翻译】**
  - 原题：次の不定積分を求めよ。$\displaystyle \int \frac{x + 1}{x^2 + 2x - 1}\,dx$
  - 中文：求不定积分 $\displaystyle \int \frac{x + 1}{x^2 + 2x - 1}\,dx$。
- **【考点定位】**
  - 对数型积分公式：$\displaystyle \int \frac{f'(x)}{f(x)}\,dx = \log|f(x)| + C$。
- **【分步标准解答】**
  分母を微分すると $(x^2 + 2x - 1)' = 2x + 2 = 2(x + 1)$ であるから，
  $$\int \frac{x + 1}{x^2 + 2x - 1}\,dx = \frac{1}{2}\int \frac{(x^2 + 2x - 1)'}{x^2 + 2x - 1}\,dx = \frac{1}{2}\log|x^2 + 2x - 1| + C \quad (C \text{ は積分定数})$$
  > 💡 讲师批注：遇到分式积分，**第一反应永远是先看分母的导数是否与分子成常数倍关系**！本题分母可取正也可取负，**绝对值符号绝不可省**。✓
- **【最终答案】**
  **$\dfrac{1}{2}\log|x^2 + 2x - 1| + C$**（$C$ 为积分常数）

---

#### 演習問題 13-(10)[2]
- **【原题重现与翻译】**
  - 原题：次の不定積分を求めよ。$\displaystyle \int x e^{2x}\,dx$
  - 中文：求不定积分 $\displaystyle \int x e^{2x}\,dx$。
- **【考点定位】**
  - 分部积分法（多项式 $\times$ 指数函数）。
- **【分步标准解答】**
  $$\int x e^{2x}\,dx = \int x \left(\frac{1}{2}e^{2x}\right)' dx$$
  > 💡 讲师批注：按「微分侧优先」原则，选多项式 $x$ 求导（降次为 $1$），选 $e^{2x}$ 积分（得 $\frac{1}{2}e^{2x}$，注意别漏系数 $\frac{1}{2}$）。

  $$= x \cdot \frac{1}{2}e^{2x} - \int 1 \cdot \frac{1}{2}e^{2x}\,dx = \frac{1}{2}x e^{2x} - \frac{1}{2} \cdot \frac{1}{2}e^{2x} + C$$
  $$= \frac{1}{4}(2x - 1)e^{2x} + C \quad (C \text{ は積分定数})$$
  > 💡 讲师批注：求导验算：$\frac{1}{4}\{2e^{2x} + (2x-1)\cdot 2e^{2x}\} = x e^{2x}$。✓
- **【最终答案】**
  **$\dfrac{1}{4}(2x - 1)e^{2x} + C$**（$C$ 为积分常数）

---

### 演習問題 13-(11)（P363 / 教材 P362）

#### 演習問題 13-(11)[1]
- **【原题重现与翻译】**
  - 原题：次の不定積分を求めよ。$\displaystyle \int x \cos 2x\,dx$
  - 中文：求不定积分 $\displaystyle \int x \cos 2x\,dx$。
- **【考点定位】**
  - 分部积分法（多项式 $\times$ 三角函数）。
- **【分步标准解答】**
  $$\int x \cos 2x\,dx = \int x \left(\frac{1}{2}\sin 2x\right)' dx$$
  $$= \frac{1}{2}x \sin 2x - \int 1 \cdot \frac{1}{2}\sin 2x\,dx$$
  > 💡 讲师批注：$\int \sin 2x\,dx = -\frac{1}{2}\cos 2x + C$，注意与前面的负号相乘变为正号！

  $$= \frac{1}{2}x \sin 2x + \frac{1}{4}\cos 2x + C \quad (C \text{ は積分定数})$$
  > 💡 讲师批注：求导验算：$\frac{1}{2}\sin 2x + x\cos 2x - \frac{1}{2}\sin 2x = x\cos 2x$。✓
- **【最终答案】**
  **$\dfrac{1}{2}x \sin 2x + \dfrac{1}{4}\cos 2x + C$**（$C$ 为积分常数）

---

#### 演習問題 13-(11)[2]
- **【原题重现与翻译】**
  - 原题：次の不定積分を求めよ。$\displaystyle \int \log(x + 1)\,dx$
  - 中文：求不定积分 $\displaystyle \int \log(x + 1)\,dx$。
- **【考点定位】**
  - 分部积分法（对数函数积分的「巧选原函数」技巧）。
- **【分步标准解答】**
  $1 = (x + 1)'$ とみなして部分積分法を用いると，
  $$\int \log(x + 1)\,dx = \int (x + 1)' \log(x + 1)\,dx$$
  > 💡 讲师批注：**黄金提速技巧！** 通常写 $1 = x'$ 会产生 $\int \frac{x}{x+1}\,dx$ 还需拆分；而直接把 $1$ 看作 $(x+1)'$，下一步就能直接约分掉分母 $x+1$！

  $$= (x + 1)\log(x + 1) - \int (x + 1) \cdot \frac{1}{x + 1}\,dx$$
  $$= (x + 1)\log(x + 1) - \int 1\,dx = (x + 1)\log(x + 1) - x + C \quad (C \text{ は積分定数})$$
  > 💡 讲师批注：求导验算：$\log(x+1) + (x+1)\cdot\frac{1}{x+1} - 1 = \log(x+1)$。✓
- **【最终答案】**
  **$(x + 1)\log(x + 1) - x + C$**（$C$ 为积分常数）

---

### 演習問題 13-(12)（P364 / 教材 P363）

#### 演習問題 13-(12)[1]
- **【原题重现与翻译】**
  - 原题：次の不定積分を求めよ。$\displaystyle \int \frac{x}{\sqrt{1 - 4x^2}}\,dx$
  - 中文：求不定积分 $\displaystyle \int \frac{x}{\sqrt{1 - 4x^2}}\,dx$。
- **【考点定位】**
  - 换元积分法（根号内二次式导数与分子匹配）。
- **【分步标准解答】**
  $t = 1 - 4x^2$ とおくと，$dt = -8x\,dx$ より $x\,dx = -\dfrac{1}{8}\,dt$。
  $$\int \frac{x}{\sqrt{1 - 4x^2}}\,dx = \int \frac{1}{\sqrt{t}}\left(-\frac{1}{8}\,dt\right) = -\frac{1}{8}\int t^{-\frac{1}{2}}\,dt$$
  > 💡 讲师批注：别看到 $\sqrt{1-4x^2}$ 就条件反射去做三角代换！因为分子上有一个 $x$，正好是 $1-4x^2$ 导数的常数倍，直接代数换元一步出答案。

  $$= -\frac{1}{8} \cdot 2 t^{\frac{1}{2}} + C = -\frac{1}{4}\sqrt{1 - 4x^2} + C \quad (C \text{ は積分定数})$$
  > 💡 讲师批注：求导验算：$-\frac{1}{4}\cdot\frac{-8x}{2\sqrt{1-4x^2}} = \frac{x}{\sqrt{1-4x^2}}$。✓
- **【最终答案】**
  **$-\dfrac{1}{4}\sqrt{1 - 4x^2} + C$**（$C$ 为积分常数）

---

#### 演習問題 13-(12)[2]
- **【原题重现与翻译】**
  - 原题：次の不定積分を求めよ。$\displaystyle \int x^3 \cos(x^4 + 2)\,dx$
  - 中文：求不定积分 $\displaystyle \int x^3 \cos(x^4 + 2)\,dx$。
- **【考点定位】**
  - 换元积分法（凑微分型）。
- **【分步标准解答】**
  $t = x^4 + 2$ とおくと，$dt = 4x^3\,dx$ より $x^3\,dx = \dfrac{1}{4}\,dt$。
  $$\int x^3 \cos(x^4 + 2)\,dx = \frac{1}{4}\int \cos t\,dt = \frac{1}{4}\sin t + C = \frac{1}{4}\sin(x^4 + 2) + C \quad (C \text{ は積分定数})$$
  > 💡 讲师批注：求导验算：$\frac{1}{4}\cos(x^4+2)\cdot 4x^3 = x^3\cos(x^4+2)$。✓
- **【最终答案】**
  **$\dfrac{1}{4}\sin(x^4 + 2) + C$**（$C$ 为积分常数）

---

### 演習問題 13-(13)（P364 / 教材 P363）

#### 演習問題 13-(13)[1]
- **【原题重现与翻译】**
  - 原题：次の不定積分を求めよ。$\displaystyle \int (\log x)^2\,dx$
  - 中文：求不定积分 $\displaystyle \int (\log x)^2\,dx$。
- **【考点定位】**
  - 连续分部积分法（对数幂次积分）。
- **【分步标准解答】**
  $$\int (\log x)^2\,dx = \int (x)' (\log x)^2\,dx$$
  $$= x(\log x)^2 - \int x \cdot 2(\log x) \cdot \frac{1}{x}\,dx = x(\log x)^2 - 2\int \log x\,dx$$
  > 💡 讲师批注：对 $(\log x)^2$ 求导时切记用复合函数链式法则：$\{(\log x)^2\}' = 2\log x \cdot \frac{1}{x}$。

  さらに $\displaystyle \int \log x\,dx = \int (x)' \log x\,dx = x\log x - \int x \cdot \frac{1}{x}\,dx = x\log x - x + C'$ を用いて，
  $$= x(\log x)^2 - 2(x\log x - x) + C = x(\log x)^2 - 2x\log x + 2x + C \quad (C \text{ は積分定数})$$
  > 💡 讲师批注：$\int \log x\,dx = x\log x - x + C$ 建议学生当作二级结论直接熟记。求导验算：$(\log x)^2 + 2\log x - 2\log x - 2 + 2 = (\log x)^2$。✓
- **【最终答案】**
  **$x(\log x)^2 - 2x\log x + 2x + C$**（$C$ 为积分常数）

---

#### 演習問題 13-(13)[2]
- **【原题重现与翻译】**
  - 原题：次の不定積分を求めよ。$\displaystyle \int x^2 e^{2x}\,dx$
  - 中文：求不定积分 $\displaystyle \int x^2 e^{2x}\,dx$。
- **【考点定位】**
  - 连续两次分部积分（二次多项式 $\times$ 指数函数）。
- **【分步标准解答】**
  $$\int x^2 e^{2x}\,dx = \int x^2 \left(\frac{1}{2}e^{2x}\right)' dx = \frac{1}{2}x^2 e^{2x} - \int 2x \cdot \frac{1}{2}e^{2x}\,dx$$
  $$= \frac{1}{2}x^2 e^{2x} - \int x e^{2x}\,dx$$
  さらに部分積分法をもう一度適用する（演習問題 13-(10)[2] の結果と同じ）：
  $$= \frac{1}{2}x^2 e^{2x} - \left\{ \frac{1}{2}x e^{2x} - \int \frac{1}{2}e^{2x}\,dx \right\}$$
  $$= \frac{1}{2}x^2 e^{2x} - \frac{1}{2}x e^{2x} + \frac{1}{4}e^{2x} + C = \frac{1}{4}(2x^2 - 2x + 1)e^{2x} + C \quad (C \text{ は積分定数})$$
  > 💡 讲师批注：连续分部积分时最容易在第二次去括号时搞错正负号，务必先保留大括号 `{ ... }` 再去括号。求导验算：$\frac{1}{4}\{(4x-2) + 2(2x^2-2x+1)\}e^{2x} = x^2 e^{2x}$。✓
- **【最终答案】**
  **$\dfrac{1}{4}(2x^2 - 2x + 1)e^{2x} + C$**（$C$ 为积分常数）

---

### 演習問題 13-(14)（P365 / 教材 P364）

#### 演習問題 13-(14)[1]
- **【原题重现与翻译】**
  - 原题：次の不定積分を求めよ。$\displaystyle \int \frac{\sin(3\log x)}{x}\,dx$
  - 中文：求不定积分 $\displaystyle \int \frac{\sin(3\log x)}{x}\,dx$。
- **【考点定位】**
  - 换元积分法（对数函数凑微分）。
- **【分步标准解答】**
  $t = 3\log x$ とおくと，$dt = \dfrac{3}{x}\,dx$ より $\dfrac{dx}{x} = \dfrac{1}{3}\,dt$。
  $$\int \frac{\sin(3\log x)}{x}\,dx = \frac{1}{3}\int \sin t\,dt = -\frac{1}{3}\cos t + C = -\frac{1}{3}\cos(3\log x) + C \quad (C \text{ は積分定数})$$
  > 💡 讲师批注：看到被积函数里同时出现 $\log x$ 与 $\frac{1}{x}$，立刻联想 $(\log x)' = \frac{1}{x}$。求导验算：$\frac{1}{3}\sin(3\log x)\cdot\frac{3}{x} = \frac{\sin(3\log x)}{x}$。✓
- **【最终答案】**
  **$-\dfrac{1}{3}\cos(3\log x) + C$**（$C$ 为积分常数）

---

#### 演習問題 13-(14)[2]
- **【原题重现与翻译】**
  - 原题：次の不定積分を求めよ。$\displaystyle \int \frac{x}{x + \sqrt{x^2 + 1}}\,dx$
  - 中文：求不定积分 $\displaystyle \int \frac{x}{x + \sqrt{x^2 + 1}}\,dx$。
- **【考点定位】**
  - 分母有理化（共轭根式消元）+ 换元积分法。
- **【分步标准解答】**
  被積分関数の分母を有理化すると，
  $$\frac{x}{x + \sqrt{x^2 + 1}} = \frac{x\left(\sqrt{x^2 + 1} - x\right)}{\left(\sqrt{x^2 + 1} + x\right)\left(\sqrt{x^2 + 1} - x\right)} = \frac{x\left(\sqrt{x^2 + 1} - x\right)}{(x^2 + 1) - x^2} = x\sqrt{x^2 + 1} - x^2$$
  > 💡 讲师批注：**神来之笔！** 分母平方差后 $x^2$ 完美抵消为 $1$，瞬间把一道看似棘手的无理分式题秒变成送分题！

  よって，
  $$\int \frac{x}{x + \sqrt{x^2 + 1}}\,dx = \int x\sqrt{x^2 + 1}\,dx - \int x^2\,dx$$
  第1項について $t = x^2 + 1$ とおくと $dt = 2x\,dx$ より，
  $$\int x\sqrt{x^2 + 1}\,dx = \frac{1}{2}\int t^{\frac{1}{2}}\,dt = \frac{1}{2} \cdot \frac{2}{3}t^{\frac{3}{2}} + C_1 = \frac{1}{3}(x^2 + 1)\sqrt{x^2 + 1} + C_1$$
  したがって，
  $$\int \frac{x}{x + \sqrt{x^2 + 1}}\,dx = \frac{1}{3}(x^2 + 1)\sqrt{x^2 + 1} - \frac{1}{3}x^3 + C \quad (C \text{ は積分定数})$$
  > 💡 讲师批注：求导验算：$\frac{1}{3}\cdot\frac{3}{2}(x^2+1)^{1/2}\cdot 2x - x^2 = x\sqrt{x^2+1} - x^2 = \frac{x}{x+\sqrt{x^2+1}}$。✓
- **【最终答案】**
  **$\dfrac{1}{3}(x^2 + 1)\sqrt{x^2 + 1} - \dfrac{1}{3}x^3 + C$**（$C$ 为积分常数）

---

### 演習問題 13-(15)（P365 / 教材 P364）

#### 演習問題 13-(15)[1]
- **【原题重现与翻译】**
  - 原题：次の不定積分を求めよ。$\displaystyle \int \frac{5x - 3}{(x + 1)(x - 3)}\,dx$
  - 中文：求不定积分 $\displaystyle \int \frac{5x - 3}{(x + 1)(x - 3)}\,dx$。
- **【考点定位】**
  - 有理函数积分（部分分式分解：分母为互异一次因式乘积）。
- **【分步标准解答】**
  部分分数分解を行う。
  $$\frac{5x - 3}{(x + 1)(x - 3)} = \frac{A}{x + 1} + \frac{B}{x - 3}$$
  とおいて両辺に $(x + 1)(x - 3)$ を掛けると，
  $$5x - 3 = A(x - 3) + B(x + 1)$$
  - $x = -1$ を代入して：$-8 = -4A \implies A = 2$
  - $x = 3$ を代入して：$12 = 4B \implies B = 3$
  > 💡 讲师批注：数值代入法（Heaviside 盖住法）求待定系数比展开比较系数快得多。代入后心算通分验算：$2(x-3)+3(x+1) = 5x-3$。✓

  よって，
  $$\int \frac{5x - 3}{(x + 1)(x - 3)}\,dx = \int \left(\frac{2}{x + 1} + \frac{3}{x - 3}\right)dx = 2\log|x + 1| + 3\log|x - 3| + C \quad (C \text{ は積分定数})$$
- **【最终答案】**
  **$2\log|x + 1| + 3\log|x - 3| + C$**（也可写为 $\log\big|(x+1)^2(x-3)^3\big| + C$，$C$ 为积分常数）

---

#### 演習問題 13-(15)[2]
- **【原题重现与翻译】**
  - 原题：次の不定積分を求めよ。$\displaystyle \int \frac{2x^2 - x + 4}{x^3 + 4x}\,dx$
  - 中文：求不定积分 $\displaystyle \int \frac{2x^2 - x + 4}{x^3 + 4x}\,dx$。
- **【考点定位】**
  - 有理函数积分（含不可约二次因式 $x^2+4$ 的部分分式分解 + 三角代换 / 反三角函数 $\tan^{-1}$）。
- **【分步标准解答】**
  分母を因数分解すると $x^3 + 4x = x(x^2 + 4)$ であるから，
  $$\frac{2x^2 - x + 4}{x(x^2 + 4)} = \frac{A}{x} + \frac{Bx + C}{x^2 + 4}$$
  とおいて両辺に $x(x^2 + 4)$ を掛けると，
  $$2x^2 - x + 4 = A(x^2 + 4) + (Bx + C)x = (A + B)x^2 + Cx + 4A$$
  両辺の係数を比較して，
  $$4A = 4,\quad A + B = 2,\quad C = -1 \implies A = 1,\; B = 1,\; C = -1$$
  > 💡 讲师批注：分母出现实数域内不可分解的二次因式 $x^2 + 4$ 时，其对应分子必须设为一次式 $Bx + C$。

  したがって，
  $$\int \frac{2x^2 - x + 4}{x^3 + 4x}\,dx = \int \left(\frac{1}{x} + \frac{x - 1}{x^2 + 4}\right)dx = \int \frac{1}{x}\,dx + \frac{1}{2}\int \frac{2x}{x^2 + 4}\,dx - \int \frac{1}{x^2 + 4}\,dx$$
  第3項について，$x = 2\tan\theta\;\left(-\dfrac{\pi}{2} < \theta < \dfrac{\pi}{2}\right)$ とおくと，$dx = \dfrac{2}{\cos^2\theta}\,d\theta$ かつ $x^2 + 4 = 4(1 + \tan^2\theta) = \dfrac{4}{\cos^2\theta}$ より，
  $$\int \frac{1}{x^2 + 4}\,dx = \int \frac{\cos^2\theta}{4} \cdot \frac{2}{\cos^2\theta}\,d\theta = \frac{1}{2}\int d\theta = \frac{1}{2}\theta + C' = \frac{1}{2}\tan^{-1}\frac{x}{2} + C'$$
  > 💡 讲师批注：**必背标准公式！** $\displaystyle \int \frac{dx}{x^2 + a^2} = \frac{1}{a}\tan^{-1}\frac{x}{a} + C$（即 $\frac{1}{a}\arctan\frac{x}{a} + C$）。本题 $a=2$，直接写出 $\frac{1}{2}\tan^{-1}\frac{x}{2}$。

  以上より，
  $$\int \frac{2x^2 - x + 4}{x^3 + 4x}\,dx = \log|x| + \frac{1}{2}\log(x^2 + 4) - \frac{1}{2}\tan^{-1}\frac{x}{2} + C \quad (C \text{ は積分定数})$$
  > 💡 讲师批注：因 $x^2+4 > 0$ 恒成立，第二项可去绝对值。求导验算：$\frac{1}{x} + \frac{x}{x^2+4} - \frac{1}{x^2+4} = \frac{2x^2-x+4}{x(x^2+4)}$。✓
- **【最终答案】**
  **$\log|x| + \dfrac{1}{2}\log(x^2 + 4) - \dfrac{1}{2}\tan^{-1}\dfrac{x}{2} + C$**（$C$ 为积分常数）

---

### 演習問題 13-(16)（P366 / 教材 P365）

#### 演習問題 13-(16)[1]
- **【原题重现与翻译】**
  - 原题：次の不定積分を求めよ。$\displaystyle \int \frac{x + 5}{x^2 + x - 2}\,dx$
  - 中文：求不定积分 $\displaystyle \int \frac{x + 5}{x^2 + x - 2}\,dx$。
- **【考点定位】**
  - 有理函数积分（因式分解 + 部分分式分解）。
- **【分步标准解答】**
  $x^2 + x - 2 = (x + 2)(x - 1)$ であるから，
  $$\frac{x + 5}{(x + 2)(x - 1)} = \frac{A}{x + 2} + \frac{B}{x - 1}$$
  とおくと，$x + 5 = A(x - 1) + B(x + 2)$。
  - $x = -2$ を代入して：$3 = -3A \implies A = -1$
  - $x = 1$ を代入して：$6 = 3B \implies B = 2$

  よって，
  $$\int \frac{x + 5}{x^2 + x - 2}\,dx = \int \left(-\frac{1}{x + 2} + \frac{2}{x - 1}\right)dx = 2\log|x - 1| - \log|x + 2| + C \quad (C \text{ は積分定数})$$
  > 💡 讲师批注：也可利用对数性质合并为 $\log\left|\dfrac{(x-1)^2}{x+2}\right| + C$，两种写法在 EJU 中均正确。✓
- **【最终答案】**
  **$2\log|x - 1| - \log|x + 2| + C$**（或 $\log\left|\dfrac{(x-1)^2}{x+2}\right| + C$，$C$ 为积分常数）

---

#### 演習問題 13-(16)[2]
- **【原题重现与翻译】**
  - 原题：次の不定積分を求めよ。$\displaystyle \int \frac{x}{(2x - 1)^4}\,dx$
  - 中文：求不定积分 $\displaystyle \int \frac{x}{(2x - 1)^4}\,dx$。
- **【考点定位】**
  - 换元积分法（高次分母一次式代换 $t = 2x - 1$）。
- **【分步标准解答】**
  $t = 2x - 1$ とおくと，$x = \dfrac{t + 1}{2}$，$dx = \dfrac{1}{2}\,dt$ である。
  $$\int \frac{x}{(2x - 1)^4}\,dx = \int \frac{\frac{t + 1}{2}}{t^4} \cdot \frac{1}{2}\,dt = \frac{1}{4}\int (t^{-3} + t^{-4})\,dt$$
  > 💡 讲师批注：也可以不换元，直接把分子写成 $x = \frac{1}{2}\{(2x-1)+1\}$ 再拆项，本质完全相同。

  $$= \frac{1}{4}\left(-\frac{1}{2}t^{-2} - \frac{1}{3}t^{-3}\right) + C = -\frac{1}{8(2x - 1)^2} - \frac{1}{12(2x - 1)^3} + C$$
  通分して整理すると，
  $$= -\frac{3(2x - 1) + 2}{24(2x - 1)^3} + C = -\frac{6x - 1}{24(2x - 1)^3} + C \quad (C \text{ は積分定数})$$
  > 💡 讲师批注：求导验算：$\left(-\frac{1}{8}(2x-1)^{-2} - \frac{1}{12}(2x-1)^{-3}\right)' = \frac{1}{2}(2x-1)^{-3} + \frac{1}{2}(2x-1)^{-4} = \frac{2x-1+1}{2(2x-1)^4} = \frac{x}{(2x-1)^4}$。✓
- **【最终答案】**
  **$-\dfrac{6x - 1}{24(2x - 1)^3} + C$**（或 $-\dfrac{1}{8(2x-1)^2} - \dfrac{1}{12(2x-1)^3} + C$，$C$ 为积分常数）

---

### 演習問題 13-(17)（P366 / 教材 P365）

#### 演習問題 13-(17)[1]
- **【原题重现与翻译】**
  - 原题：次の不定積分を求めよ。$\displaystyle \int \frac{x}{\sqrt{x + 9} + 3}\,dx$
  - 中文：求不定积分 $\displaystyle \int \frac{x}{\sqrt{x + 9} + 3}\,dx$。
- **【考点定位】**
  - 分母有理化 + 幂函数不定积分。
- **【分步标准解答】**
  分母を有理化すると（$x \neq 0$ にて，また $x = 0$ でも連続），
  $$\frac{x}{\sqrt{x + 9} + 3} = \frac{x\left(\sqrt{x + 9} - 3\right)}{(x + 9) - 9} = \frac{x\left(\sqrt{x + 9} - 3\right)}{x} = \sqrt{x + 9} - 3$$
  > 💡 讲师批注：与 (14)[2] 异曲同工！有理化后分母正好变成 $x$，与分子 $x$ 约分消去，直接降维打击！

  よって，
  $$\int \frac{x}{\sqrt{x + 9} + 3}\,dx = \int \left\{(x + 9)^{\frac{1}{2}} - 3\right\}dx = \frac{2}{3}(x + 9)\sqrt{x + 9} - 3x + C \quad (C \text{ は積分定数})$$
  > 💡 讲师批注：求导验算：$\sqrt{x+9} - 3 = \frac{(x+9)-9}{\sqrt{x+9}+3} = \frac{x}{\sqrt{x+9}+3}$。✓
- **【最终答案】**
  **$\dfrac{2}{3}(x + 9)\sqrt{x + 9} - 3x + C$**（$C$ 为积分常数）

---

#### 演習問題 13-(17)[2]
- **【原题重现与翻译】**
  - 原题：次の不定積分を求めよ。$\displaystyle \int x^3 \sqrt{x + 3}\,dx$
  - 中文：求不定积分 $\displaystyle \int x^3 \sqrt{x + 3}\,dx$。
- **【考点定位】**
  - 换元积分法（高次多项式 $\times$ 一次根式，大计算量细心度检验）。
- **【分步标准解答】**
  $t = x + 3$ とおくと，$x = t - 3$，$dx = dt$ であり，
  $$x^3 = (t - 3)^3 = t^3 - 9t^2 + 27t - 27$$
  よって，
  $$\int x^3 \sqrt{x + 3}\,dx = \int (t^3 - 9t^2 + 27t - 27)t^{\frac{1}{2}}\,dt = \int \left(t^{\frac{7}{2}} - 9t^{\frac{5}{2}} + 27t^{\frac{3}{2}} - 27t^{\frac{1}{2}}\right)dt$$
  > 💡 讲师批注：利用 $(a-b)^3 = a^3 - 3a^2b + 3ab^2 - b^3$ 展开时，务必检查正负号交替（$+,-,+,-$）与系数 $1, 9, 27, 27$。

  各項を積分して，
  $$= \frac{2}{9}t^{\frac{9}{2}} - 9 \cdot \frac{2}{7}t^{\frac{7}{2}} + 27 \cdot \frac{2}{5}t^{\frac{5}{2}} - 27 \cdot \frac{2}{3}t^{\frac{3}{2}} + C$$
  $$= \frac{2}{9}t^{\frac{9}{2}} - \frac{18}{7}t^{\frac{7}{2}} + \frac{54}{5}t^{\frac{5}{2}} - 18t^{\frac{3}{2}} + C$$
  分母 $9, 7, 5$ の最小公倍数 $315$ で通分し，$\dfrac{2}{315}t^{\frac{3}{2}}$ をくくり出すと，
  $$= \frac{2}{315}t^{\frac{3}{2}}\left(35t^3 - 405t^2 + 1701t - 2835\right) + C$$
  $t = x + 3$ を戻して括弧内を整理する：
  $$\begin{aligned}
  &35(x+3)^3 - 405(x+3)^2 + 1701(x+3) - 2835 \\
  &= 35(x^3 + 9x^2 + 27x + 27) - 405(x^2 + 6x + 9) + 1701(x + 3) - 2835 \\
  &= (35x^3 + 315x^2 + 945x + 945) - (405x^2 + 2430x + 3645) + (1701x + 5103) - 2835 \\
  &= 35x^3 - 90x^2 + 216x - 432
  \end{aligned}$$
  したがって，
  $$\int x^3 \sqrt{x + 3}\,dx = \frac{2}{315}(35x^3 - 90x^2 + 216x - 432)(x + 3)\sqrt{x + 3} + C \quad (C \text{ は積分定数})$$
  > 💡 讲师批注：这种大系数题**必须求导验算**：
  > 分子 $= 3(35x^3-90x^2+216x-432) + 2(x+3)(105x^2-180x+216) = 315x^3$，除以 $315$ 恰好还原为 $x^3\sqrt{x+3}$！若考试时间紧张，也可以保留未展开的 $t=x+3$ 形式：$\frac{2}{9}(x+3)^{9/2} - \frac{18}{7}(x+3)^{7/2} + \frac{54}{5}(x+3)^{5/2} - 18(x+3)^{3/2} + C$。✓
- **【最终答案】**
  **$\dfrac{2}{315}(35x^3 - 90x^2 + 216x - 432)(x + 3)\sqrt{x + 3} + C$**（$C$ 为积分常数）

---

> 👉 **接续阅读**：演習問題 13-(18) ～ 13-(30) 的逐题深度解析，请继续阅读 [`note_025_b.md`](file:///Users/baohan/Desktop/EJU/notes_math/note_025_b.md)。
