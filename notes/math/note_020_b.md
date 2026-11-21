# 《EJU 教材全解与备课讲义》数学 020-B（P286–P300 下篇：无穷级数 & 函数极限）

> **对应源文件**：`work_math/ocr_md/ocr_020_p286-300.md`（数学Ⅲ《極限》之「無限級数」「関数の極限」演习题部分）
> **视觉核对参考图**：`work_math/ref_imgs/page_0290.jpg` – `page_0300.jpg`
> **上篇衔接**：全切片知识点总览、勘误汇总、核心词汇表及 演習問題 1（数列极限全 20 小题）详见同目录 [`note_020_a.md`](note_020_a.md)。

---

## 三、逐题深度解析（不可跳步）— 演習問題 2（無限級数）

---

### 演習問題 2-(1)（P292 / 原书 P291）

> **大题干**：次の無限級数の収束，発散について調べ，収束すればその和を求めよ。（判断下列无穷级数的收敛与发散，若收敛则求其和。）

---

#### 演習問題 2-(1)-[1]
- **【原题重现与翻译】**
  - 原题：$\displaystyle \sum_{n=1}^{\infty} \frac{1}{(2n + 1)(2n + 3)}$
  - 中文：判断无穷级数 $\displaystyle \sum_{n=1}^{\infty} \frac{1}{(2n + 1)(2n + 3)}$ 的敛散性，若收敛求其和。
- **【考点定位】**
  - 部分分式分解（裂项相消法）求部分和 $S_n$，再取极限 $\lim_{n\to\infty} S_n$。
- **【分步标准解答】**
  第 $n$ 項までの部分和を $S_n$ とする。一般項を部分分数に分解すると，
  $$\frac{1}{(2k + 1)(2k + 3)} = \frac{1}{2}\left(\frac{1}{2k + 1} - \frac{1}{2k + 3}\right)$$
  > 💡 讲师批注：裂项口诀「两项差为 $(2k+3)-(2k+1)=2$，故前面乘以 $\dfrac{1}{2}$」。通分反验：$\frac{1}{2}\cdot\frac{(2k+3)-(2k+1)}{(2k+1)(2k+3)} = \frac{1}{(2k+1)(2k+3)}$，准确！

  よって，
  $$S_n = \sum_{k=1}^{n} \frac{1}{2}\left(\frac{1}{2k + 1} - \frac{1}{2k + 3}\right)$$
  $$= \frac{1}{2}\left\{\left(\frac{1}{3} - \frac{1}{5}\right) + \left(\frac{1}{5} - \frac{1}{7}\right) + \dots + \left(\frac{1}{2n + 1} - \frac{1}{2n + 3}\right)\right\}$$
  $$= \frac{1}{2}\left(\frac{1}{3} - \frac{1}{2n + 3}\right)$$
  > 💡 讲师批注：代入 $n = 1$ 验算部分和：$S_1 = \frac{1}{2}\left(\frac{1}{3}-\frac{1}{5}\right) = \frac{1}{15} = \frac{1}{3\cdot 5}$，与原级数首项完全一致！

  したがって，
  $$\lim_{n\to\infty} S_n = \lim_{n\to\infty} \frac{1}{2}\left(\frac{1}{3} - \frac{1}{2n + 3}\right) = \frac{1}{2}\left(\frac{1}{3} - 0\right) = \frac{1}{6}$$
  よって，この無限級数は収束し，その和は $\dfrac{1}{6}$ である。
- **【最终答案】**
  **収束し，和は $\dfrac{1}{6}$**

---

#### 演習問題 2-(1)-[2]
- **【原题重现与翻译】**
  - 原题：$\dfrac{1}{\sqrt{1} + \sqrt{3}} + \dfrac{1}{\sqrt{2} + \sqrt{4}} + \dfrac{1}{\sqrt{3} + \sqrt{5}} + \dots$
  - 中文：判断无穷级数 $\dfrac{1}{\sqrt{1} + \sqrt{3}} + \dfrac{1}{\sqrt{2} + \sqrt{4}} + \dfrac{1}{\sqrt{3} + \sqrt{5}} + \dots$ 的敛散性，若收敛求其和。
- **【考点定位】**
  - 分母有理化 + 隔项裂项相消法求部分和 $S_n$。
- **【分步标准解答】**
  第 $k$ 項は $\dfrac{1}{\sqrt{k} + \sqrt{k + 2}}$ である。分母を有理化すると，
  $$\frac{1}{\sqrt{k} + \sqrt{k + 2}} = \frac{\sqrt{k + 2} - \sqrt{k}}{(\sqrt{k + 2} + \sqrt{k})(\sqrt{k + 2} - \sqrt{k})} = \frac{\sqrt{k + 2} - \sqrt{k}}{2}$$
  > 💡 讲师批注：把较大的 $\sqrt{k+2}$ 写在前面进行有理化，分母为 $(k+2)-k = 2 > 0$，可避免负号出错。

  第 $n$ 項までの部分和を $S_n$（$n \ge 2$）とすると，
  $$S_n = \frac{1}{2}\{(\sqrt{3} - \sqrt{1}) + (\sqrt{4} - \sqrt{2}) + (\sqrt{5} - \sqrt{3}) + \dots + (\sqrt{n + 1} - \sqrt{n - 1}) + (\sqrt{n + 2} - \sqrt{n})\}$$
  > 💡 讲师批注：本题是**隔项相消**（$k$ 与 $k+2$ 相差 $2$），消去中间项后，前面留最小的**两项**（$-\sqrt{1}, -\sqrt{2}$），后面留最大的**两项**（$+\sqrt{n+1}, +\sqrt{n+2}$）！

  $$= \frac{1}{2}(\sqrt{n + 1} + \sqrt{n + 2} - 1 - \sqrt{2})$$
  よって，
  $$\lim_{n\to\infty} S_n = \lim_{n\to\infty} \frac{1}{2}(\sqrt{n + 1} + \sqrt{n + 2} - 1 - \sqrt{2}) = \infty$$
  したがって，この無限級数は発散する。
- **【最终答案】**
  **発散する（正の無限大に発散）**

---

#### 演習問題 2-(1)-[3]
- **【原题重现与翻译】**
  - 原题：$\sqrt{3} + 3 + 3\sqrt{3} + \dots$
  - 中文：判断无穷等比级数 $\sqrt{3} + 3 + 3\sqrt{3} + \dots$ 的敛散性，若收敛求其和。
- **【考点定位】**
  - 无穷等比级数的收敛条件（$|r| < 1$）。
- **【分步标准解答】**
  この無限級数は，初項 $a = \sqrt{3}\; (\neq 0)$，公比 $r = \dfrac{3}{\sqrt{3}} = \sqrt{3}$ の無限等比級数である。
  $|r| = \sqrt{3} \ge 1$ であるから，この無限級数は発散する。
  > 💡 讲师批注：识别出初项 $a \neq 0$ 且 $|r| \ge 1$ 即可直接判定发散，无需计算部分和。
- **【最终答案】**
  **発散する**

---

#### 演習問題 2-(1)-[4]
- **【原题重现与翻译】**
  - 原题：$4 - 2\sqrt{3} + 3 - \dots$
  - 中文：判断无穷等比级数 $4 - 2\sqrt{3} + 3 - \dots$ 的敛散性，若收敛求其和。
- **【考点定位】**
  - 无穷等比级数求和公式 $S = \dfrac{a}{1-r}$ 与分母有理化。
- **【分步标准解答】**
  この無限級数は，初項 $a = 4$，公比 $r = \dfrac{-2\sqrt{3}}{4} = -\dfrac{\sqrt{3}}{2}$ の無限等比級数である。
  （検算：第 3 項は $4 \cdot \left(-\dfrac{\sqrt{3}}{2}\right)^2 = 4 \cdot \dfrac{3}{4} = 3$ となり一致する。）

  $|r| = \dfrac{\sqrt{3}}{2} < 1$ であるから，この無限級数は収束し，その和は
  $$S = \frac{4}{1 - \left(-\dfrac{\sqrt{3}}{2}\right)} = \frac{4}{1 + \dfrac{\sqrt{3}}{2}} = \frac{8}{2 + \sqrt{3}}$$
  > 💡 讲师批注：注意分母是 $1 - r$，而 $r$ 本身为负，故 $1 - \left(-\frac{\sqrt{3}}{2}\right) = 1 + \frac{\sqrt{3}}{2}$！别忘分子分母同乘 $2$ 去繁分数，再有理化。

  分母を有理化すると，
  $$S = \frac{8(2 - \sqrt{3})}{(2 + \sqrt{3})(2 - \sqrt{3})} = \frac{8(2 - \sqrt{3})}{4 - 3} = 16 - 8\sqrt{3}$$
- **【最终答案】**
  **収束し，和は $16 - 8\sqrt{3}$**

---

#### 演習問題 2-(1)-[5]
- **【原题重现与翻译】**
  - 原题：$\left(2 - \dfrac{1}{2}\right) + \left(\dfrac{2}{3} + \dfrac{1}{2^2}\right) + \left(\dfrac{2}{3^2} - \dfrac{1}{2^3}\right) + \dots + \left\{\dfrac{2}{3^{n-1}} + \dfrac{(-1)^n}{2^n}\right\} + \dots$
  - 中文：判断该无穷级数的敛散性，若收敛求其和。
- **【考点定位】**
  - 无穷级数的线性性质：拆分为两个**各自收敛**的无穷等比级数之和。
- **【分步标准解答】**
  与えられた無限級数を 2 つの無限等比級数に分けて考える。
  1. $\displaystyle \sum_{n=1}^{\infty} \frac{2}{3^{n-1}}$ は初項 $2$，公比 $\dfrac{1}{3}$ の無限等比級数であり，$\left|\dfrac{1}{3}\right| < 1$ より収束して，その和は
     $$\frac{2}{1 - \dfrac{1}{3}} = \frac{2}{\dfrac{2}{3}} = 3$$
  2. $\displaystyle \sum_{n=1}^{\infty} \frac{(-1)^n}{2^n} = \sum_{n=1}^{\infty} \left(-\frac{1}{2}\right)^n$ は初項 $-\dfrac{1}{2}$，公比 $-\dfrac{1}{2}$ の無限等比級数であり，$\left|-\dfrac{1}{2}\right| < 1$ より収束して，その和は
     $$\frac{-\dfrac{1}{2}}{1 - \left(-\dfrac{1}{2}\right)} = \frac{-\dfrac{1}{2}}{\dfrac{3}{2}} = -\frac{1}{3}$$
  > 💡 讲师批注：**严守逻辑顺序！** 只有在确认拆分后的**两个无穷级数各自收敛**之后，才能使用线性性质 $\sum(a_n+b_n) = \sum a_n + \sum b_n$！另外注意第二个级数初项是 $n=1$ 时的 $-\frac{1}{2}$，不是 $1$。

  2 つの無限級数がともに収束するので，もとの無限級数も収束し，その和は
  $$3 + \left(-\frac{1}{3}\right) = \frac{8}{3}$$
- **【最终答案】**
  **収束し，和は $\dfrac{8}{3}$**

---

### 演習問題 2-(2)（P294 / 原书 P293）

> **大题干**：次の無限級数は発散することを示せ。（证明下列无穷级数发散。）

---

#### 演習問題 2-(2)-[1]
- **【原题重现与翻译】**
  - 原题：$\dfrac{1}{2} + \dfrac{4}{3} + \dfrac{7}{4} + \dfrac{10}{5} + \dots$
  - 中文：证明无穷级数 $\dfrac{1}{2} + \dfrac{4}{3} + \dfrac{7}{4} + \dfrac{10}{5} + \dots$ 发散。
- **【考点定位】**
  - 发散判定法（收敛必要条件的逆否命题）：$\lim_{n\to\infty} a_n \neq 0 \implies$ 级数发散。
- **【分步标准解答】**
  この無限級数の第 $n$ 項 $a_n$ は，分子が初項 $1$・公差 $3$ の等差数列 $3n - 2$，分母が $n + 1$ であるから，
  $$a_n = \frac{3n - 2}{n + 1}$$
  > 💡 讲师批注：核对前 4 项：$n=1 \implies \frac{1}{2}$，$n=2 \implies \frac{4}{3}$，$n=3 \implies \frac{7}{4}$，$n=4 \implies \frac{10}{5}$，完全吻合。

  第 $n$ 項の極限を求めると，
  $$\lim_{n\to\infty} a_n = \lim_{n\to\infty} \frac{3n - 2}{n + 1} = \lim_{n\to\infty} \frac{3 - \dfrac{2}{n}}{1 + \dfrac{1}{n}} = 3 \neq 0$$
  $\lim_{n\to\infty} a_n \neq 0$ であるから，この無限級数は発散する。
- **【最终答案】**
  **$\lim_{n\to\infty} a_n = 3 \neq 0$ より，発散する。（証明終）**

---

#### 演習問題 2-(2)-[2]
- **【原题重现与翻译】**
  - 原题：$\cos\pi + \cos 2\pi + \cos 3\pi + \dots$
  - 中文：证明无穷级数 $\cos\pi + \cos 2\pi + \cos 3\pi + \dots$ 发散。
  > ⚠️ **教材勘误提示（P293 / `page_0294.jpg`）**：原教材误印为 $\cos\pi + \cos 2\pi \cos 3\pi + \dots$（漏印了第 2 项与第 3 项之间的加号 `+`），正确应为 **$\cos\pi + \cos 2\pi + \cos 3\pi + \dots$**。
- **【考点定位】**
  - 发散判定法：通项震荡不收敛于 $0$。
- **【分步标准解答】**
  この無限級数の第 $n$ 項を $a_n$ とすると，
  $$a_n = \cos n\pi = (-1)^n$$
  数列 $\{a_n\}$ は $-1,\; 1,\; -1,\; 1,\; \dots$ と振動するため，$0$ に収束しない。
  よって，この無限級数は発散する。
  > 💡 讲师批注：规范表述写「数列 $\{a_n\}$ は $0$ に収束しない」（因为 $\lim a_n$ 本身不存在，比直接写 $\lim a_n \neq 0$ 更严谨）。
- **【最终答案】**
  **一般項 $a_n = \cos n\pi = (-1)^n$ は $0$ に収束しないため，発散する。（証明終）**

---

### 演習問題 2-(3)（P294 / 原书 P293）
- **【原题重现与翻译】**
  - 原题：無限級数 $\displaystyle \sum_{n=1}^{\infty} \left(\frac{1}{3}\right)^n \sin\frac{n\pi}{2}$ の和を求めよ。
  - 中文：求无穷级数 $\displaystyle \sum_{n=1}^{\infty} \left(\frac{1}{3}\right)^n \sin\frac{n\pi}{2}$ 的和。
- **【考点定位】**
  - 含周期性零项的无穷级数：通过奇偶项部分和 $S_{2m-1}, S_{2m}$ 严格求极限。
- **【分步标准解答】**
  $n = 1, 2, 3, 4, \dots$ に対して，$\sin\dfrac{n\pi}{2}$ の値は $1,\; 0,\; -1,\; 0,\; 1,\; 0,\; \dots$ と周期 $4$ で繰り返される。
  したがって，与えられた級数の各項を書き出すと，
  $$\frac{1}{3} + 0 - \frac{1}{3^3} + 0 + \frac{1}{3^5} + 0 - \frac{1}{3^7} + \dots$$
  > 💡 讲师批注：**日本考场满分严谨写法**：无穷级数不能随意“直接删除 0 项”（虽然有限个 0 项不影响部分和），最规范的写法是直接考察奇数项部分和 $S_{2m-1}$ 与偶数项部分和 $S_{2m}$！

  第 $n$ 項までの部分和を $S_n$ とする。任意の自然数 $m$ に対して，第 $2m$ 項は $0$ であるから $S_{2m} = S_{2m-1}$ が成り立ち，
  $$S_{2m-1} = S_{2m} = \frac{1}{3} - \frac{1}{3^3} + \frac{1}{3^5} - \dots + \frac{(-1)^{m-1}}{3^{2m-1}}$$
  これは初項 $\dfrac{1}{3}$，公比 $-\dfrac{1}{9}$，項数 $m$ の等比数列の和であるから，
  $$S_{2m-1} = S_{2m} = \frac{\dfrac{1}{3}\left\{1 - \left(-\dfrac{1}{9}\right)^m\right\}}{1 - \left(-\dfrac{1}{9}\right)} = \frac{\dfrac{1}{3}}{\dfrac{10}{9}}\left\{1 - \left(-\frac{1}{9}\right)^m\right\} = \frac{3}{10}\left\{1 - \left(-\frac{1}{9}\right)^m\right\}$$
  $m \to \infty$ のとき，$\left(-\dfrac{1}{9}\right)^m \to 0$ であるから，
  $$\lim_{m\to\infty} S_{2m-1} = \lim_{m\to\infty} S_{2m} = \frac{3}{10}$$
  よって，$\lim_{n\to\infty} S_n = \dfrac{3}{10}$ となり，求める和は $\dfrac{3}{10}$ である。
- **【最终答案】**
  **$\dfrac{3}{10}$**

---

### 演習問題 2-(4)（P295 / 原书 P294）
- **【原题重现与翻译】**
  - 原题：無限級数 $(x - 4) + \dfrac{x(x - 4)}{2x - 4} + \dfrac{x^2(x - 4)}{(2x - 4)^2} + \dots \quad (x \neq 2)$ について
    - [1] 無限級数が収束するときの実数 $x$ の値の範囲を求めよ。
    - [2] 無限級数の和 $S$ を求めよ。
  - 中文：关于无穷级数 $(x - 4) + \dfrac{x(x - 4)}{2x - 4} + \dfrac{x^2(x - 4)}{(2x - 4)^2} + \dots \quad (x \neq 2)$：
    - [1] 求使该无穷级数收敛的实数 $x$ 的取值范围。
    - [2] 求该无穷级数的和 $S$。
- **【考点定位】**
  - 含参数无穷等比级数的收敛条件（**切勿遗漏「初项 $a = 0$」**！）与分段求和。
- **【图解辅助（SVG 矢量图）】**

<svg viewBox="0 0 500 105" width="500" height="105" xmlns="http://www.w3.org/2000/svg">
  <rect x="0" y="0" width="500" height="105" fill="#f8fafc" rx="8"/>
  <text x="16" y="22" font-size="12" font-weight="bold" fill="#1e293b">收敛范围数轴：x &lt; 4/3 或 x ≥ 4（注意 x = 4 是由初项 a = 0 补入的实心点！）</text>
  <!-- 数轴 -->
  <line x1="30" y1="68" x2="470" y2="68" stroke="#334155" stroke-width="2"/>
  <polygon points="470,68 462,64 462,72" fill="#334155"/>
  <text x="478" y="72" font-size="12" font-style="italic" fill="#334155">x</text>
  <!-- 区间线：x < 4/3 (x=30..180) 与 x >= 4 (x=340..455) -->
  <line x1="30" y1="48" x2="180" y2="48" stroke="#2563eb" stroke-width="3.5"/>
  <line x1="340" y1="48" x2="455" y2="48" stroke="#2563eb" stroke-width="3.5"/>
  <line x1="180" y1="48" x2="180" y2="68" stroke="#64748b" stroke-width="1" stroke-dasharray="3,2"/>
  <line x1="340" y1="48" x2="340" y2="68" stroke="#64748b" stroke-width="1" stroke-dasharray="3,2"/>
  <!-- x = 4/3 空心点 -->
  <circle cx="180" cy="48" r="5" fill="#ffffff" stroke="#2563eb" stroke-width="2.5"/>
  <text x="168" y="88" font-size="12" fill="#1e293b">4/3</text>
  <!-- x = 2 标记（分母为0） -->
  <line x1="230" y1="63" x2="230" y2="73" stroke="#dc2626" stroke-width="2"/>
  <text x="225" y="88" font-size="11" fill="#dc2626">2 (除外)</text>
  <!-- x = 4 实心点 -->
  <circle cx="340" cy="48" r="5" fill="#10b981" stroke="#047857" stroke-width="2"/>
  <text x="336" y="88" font-size="12" fill="#059669" font-weight="bold">4</text>
  <!-- 文字说明 -->
  <text x="58" y="40" font-size="11" fill="#2563eb">S = 2x - 4</text>
  <text x="372" y="40" font-size="11" fill="#2563eb">S = 2x - 4</text>
  <text x="295" y="100" font-size="10.5" fill="#059669">x = 4 时 S = 0</text>
</svg>

- **【分步标准解答】**
  この無限級数は，初項 $a = x - 4$，公比 $r = \dfrac{x}{2x - 4}\; (x \neq 2)$ の無限等比級数である。

  **[1] 収束する $x$ の範囲**
  無限等比級数が収束するための条件は，「$a = 0$」または「$|r| < 1$」である。
  - **ケース 1（初項 $= 0$）**：$x - 4 = 0 \implies x = 4$（$x \neq 2$ を満たす）。
  - **ケース 2（$|r| < 1$）**：
    $$\left|\frac{x}{2x - 4}\right| < 1 \iff |x| < |2x - 4|$$
    両辺は $0$ 以上であるから，2 乗しても同値：
    $$x^2 < (2x - 4)^2 \iff x^2 < 4x^2 - 16x + 16$$
    $$\iff 3x^2 - 16x + 16 > 0 \iff (3x - 4)(x - 4) > 0$$
    $$\iff x < \frac{4}{3},\; x > 4$$
    （この範囲は自動的に $x \neq 2$ を満たしている。）
  > 💡 讲师批注：**EJU 最高频失分坑！** 90% 的失分都是漏掉了「初项 $a = 0 \implies x = 4$」，只写了 $x < \frac{4}{3},\; x > 4$！合并两个条件后，$x = 4$ 处的空心点变为**实心点**，得 $x < \dfrac{4}{3}$ または $x \ge 4$！

  **[2] 無限級数の和 $S$**
  - $x = 4$ のとき：すべての項が $0$ であるから，$S = 0$。
  - $x < \dfrac{4}{3},\; x > 4$ のとき（$x \neq 4$）：
    $$S = \frac{a}{1 - r} = \frac{x - 4}{1 - \dfrac{x}{2x - 4}} = \frac{(x - 4)(2x - 4)}{(2x - 4) - x} = \frac{(x - 4)(2x - 4)}{x - 4} = 2x - 4$$
  > 💡 讲师批注：**第二大易错坑！** 约去 $(x-4)$ 得到的 $S = 2x - 4$ 在 $x = 4$ 时等于 $4 \neq 0$！因此 $[2]$ 的答案**必须分类书写**，绝不可把 $x = 4$ 混入 $S = 2x - 4$ 中！
- **【最终答案】**
  **[1] $x < \dfrac{4}{3}$ または $x \ge 4$**
  **[2] $x = 4$ のとき $S = 0$；$x < \dfrac{4}{3},\; x > 4$ のとき $S = 2x - 4$**

---

### 演習問題 2-(5)（P295 / 原书 P294）
- **【原题重现与翻译】**
  - 原题：数列の和 $S_n = \displaystyle \sum_{k=1}^{n} k\left(\frac{1}{3}\right)^{k-1}$ を求め，また $\lim_{n\to\infty} S_n$ を求めよ。
  - 中文：求数列前 $n$ 项和 $S_n = \displaystyle \sum_{k=1}^{n} k\left(\frac{1}{3}\right)^{k-1}$，并求 $\lim_{n\to\infty} S_n$。
  > ⚠️ **教材勘误提示（P294 / `page_0295.jpg`）**：原教材误印为 $S_n = \displaystyle \sum_{n=1}^{\infty} k\left(\frac{1}{3}\right)^{k-1}$（下限变量误印为 $n=1$，上限误印为 $\infty$），正确应为 **$S_n = \displaystyle \sum_{k=1}^{n} k\left(\frac{1}{3}\right)^{k-1}$**。
- **【考点定位】**
  - 「等差 $\times$ 等比」型数列求和（错位相减法）+ 利用二项式定理与夹逼原理证明 $\lim_{n\to\infty} \dfrac{n}{3^n} = 0$。
- **【分步标准解答】**
  $S_n$ と $\dfrac{1}{3}S_n$ を並べて引き算する（公比倍してずらして引く）：
  $$\begin{aligned}
  S_n &= 1 + 2 \cdot \frac{1}{3} + 3 \cdot \left(\frac{1}{3}\right)^2 + \dots + n \cdot \left(\frac{1}{3}\right)^{n-1} \\
  -\big)\;\frac{1}{3}S_n &= \phantom{1 + {}} 1 \cdot \frac{1}{3} + 2 \cdot \left(\frac{1}{3}\right)^2 + \dots + (n - 1)\left(\frac{1}{3}\right)^{n-1} + n \cdot \left(\frac{1}{3}\right)^n
  \end{aligned}$$
  辺々を引くと，
  $$\frac{2}{3}S_n = \left\{1 + \frac{1}{3} + \left(\frac{1}{3}\right)^2 + \dots + \left(\frac{1}{3}\right)^{n-1}\right\} - n\left(\frac{1}{3}\right)^n$$
  > 💡 讲师批注：括号内为初项 $1$、公比 $\frac{1}{3}$、项数 $n$ 的等比数列之和；特别注意最后一项 $-n\left(\frac{1}{3}\right)^n$ 前面是**减号**！

  $$\frac{2}{3}S_n = \frac{1 - \left(\dfrac{1}{3}\right)^n}{1 - \dfrac{1}{3}} - n\left(\frac{1}{3}\right)^n = \frac{3}{2}\left\{1 - \left(\frac{1}{3}\right)^n\right\} - n\left(\frac{1}{3}\right)^n$$
  両辺に $\dfrac{3}{2}$ を掛けて，
  $$S_n = \frac{9}{4}\left\{1 - \left(\frac{1}{3}\right)^n\right\} - \frac{3n}{2}\left(\frac{1}{3}\right)^n = \frac{9}{4} - \frac{2n + 3}{4 \cdot 3^{n-1}}$$
  > 💡 讲师批注：特值验算——$n=1$ 时 $S_1 = \frac{9}{4} - \frac{5}{4} = 1$；$n=2$ 时 $S_2 = \frac{9}{4} - \frac{7}{12} = \frac{20}{12} = \frac{5}{3}$，而直接算 $1 + 2\cdot\frac{1}{3} = \frac{5}{3}$，100% 准确！

  次に $\lim_{n\to\infty} S_n$ を求める。ここで $n \ge 2$ のとき，二項定理より
  $$3^n = (1 + 2)^n > {}_n\mathrm{C}_2 \cdot 2^2 = \frac{n(n - 1)}{2} \cdot 4 = 2n(n - 1)$$
  よって，$0 < \dfrac{n}{3^n} < \dfrac{n}{2n(n - 1)} = \dfrac{1}{2(n - 1)}$。
  $\lim_{n\to\infty} \dfrac{1}{2(n - 1)} = 0$ より，はさみうちの原理から $\lim_{n\to\infty} \dfrac{n}{3^n} = 0$（よって $\lim_{n\to\infty} \dfrac{n}{3^{n-1}} = 0$）。
  > 💡 讲师批注：**日本二次考与 EJU 记述题加分点**：$\lim_{n\to\infty} \frac{n}{r^n} = 0\;(r>1)$ 是 $\frac{\infty}{\infty}$ 不定形，用二项式定理取二次项 ${}_n\mathrm{C}_2$ 放缩夹逼是最经典的满分证明！

  したがって，
  $$\lim_{n\to\infty} S_n = \lim_{n\to\infty} \left(\frac{9}{4} - \frac{2n + 3}{4 \cdot 3^{n-1}}\right) = \frac{9}{4} - 0 = \frac{9}{4}$$
- **【最终答案】**
  **$S_n = \dfrac{9}{4} - \dfrac{2n + 3}{4 \cdot 3^{n-1}}$，$\quad \lim_{n\to\infty} S_n = \dfrac{9}{4}$**

---

## 三（续）、逐题深度解析（不可跳步）— 演習問題 3（関数の極限）

---

### 演習問題 3-(1)（P300 / 原书 P299）

> **大题干**：次の極限値を求めよ。（求下列极限值。）

---

#### 演習問題 3-(1)-[1]
- **【原题重现与翻译】**
  - 原题：$\displaystyle \lim_{x \to 2} \frac{x^3 - 3x - 2}{x^3 - 3x + 2}$
  - 中文：求极限值 $\displaystyle \lim_{x \to 2} \frac{x^3 - 3x - 2}{x^3 - 3x + 2}$。
- **【考点定位】**
  - 函数极限的第一步原则：**先直接代入检验是否为不定形**（非不定形直接得值）。
- **【分步标准解答】**
  $x = 2$ を分母・分子にそれぞれ代入すると，
  - 分子：$2^3 - 3 \cdot 2 - 2 = 8 - 6 - 2 = 0$
  - 分母：$2^3 - 3 \cdot 2 + 2 = 8 - 6 + 2 = 4 \neq 0$
  > 💡 讲师批注：**极佳的反套路检验题！** 很多学生一看到三次分式就不假思索地因式分解，其实求函数极限的**第一铁律**永远是「先代入看分母是否为 $0$」！本题分母趋于 $4 \neq 0$，并非 $\frac{0}{0}$ 不定形，直接得 $\frac{0}{4} = 0$！

  分母は $0$ に収束しないため，そのまま極限値を求められて，
  $$\lim_{x \to 2} \frac{x^3 - 3x - 2}{x^3 - 3x + 2} = \frac{2^3 - 3 \cdot 2 - 2}{2^3 - 3 \cdot 2 + 2} = \frac{0}{4} = 0$$
- **【最终答案】**
  **$0$**

---

#### 演習問題 3-(1)-[2]
- **【原题重现与翻译】**
  - 原题：$\displaystyle \lim_{x \to 0} \frac{1}{x}\left(\frac{3}{x + 3} - 1\right)$
  - 中文：求极限值 $\displaystyle \lim_{x \to 0} \frac{1}{x}\left(\frac{3}{x + 3} - 1\right)$。
- **【考点定位】**
  - $\infty \times 0$ 型不定式：通分后约去零因子 $x$。
- **【分步标准解答】**
  かっこ内を通分して整理すると（$x \neq 0$），
  $$\frac{1}{x}\left(\frac{3}{x + 3} - 1\right) = \frac{1}{x} \cdot \frac{3 - (x + 3)}{x + 3} = \frac{1}{x} \cdot \frac{-x}{x + 3} = -\frac{1}{x + 3}$$
  > 💡 讲师批注：求 $\lim_{x\to 0}$ 时 $x$ 无限趋近于 $0$ 但**不等于 $0$**（$x \neq 0$），故可合法约去分子分母的公因子 $x$。

  よって，
  $$\lim_{x \to 0} \frac{1}{x}\left(\frac{3}{x + 3} - 1\right) = \lim_{x \to 0} \left(-\frac{1}{x + 3}\right) = -\frac{1}{0 + 3} = -\frac{1}{3}$$
- **【最终答案】**
  **$-\dfrac{1}{3}$**

---

#### 演習問題 3-(1)-[3]
- **【原题重现与翻译】**
  - 原题：$\displaystyle \lim_{x \to 4} \frac{\sqrt{x + 5} - 3}{x - 4}$
  - 中文：求极限值 $\displaystyle \lim_{x \to 4} \frac{\sqrt{x + 5} - 3}{x - 4}$。
- **【考点定位】**
  - 含根号的 $\dfrac{0}{0}$ 型不定式：分子有理化并约去零因子 $(x - 4)$。
- **【分步标准解答】**
  $x \to 4$ のとき分母・分子ともに $0$ となる $\dfrac{0}{0}$ の不定形である。分子を有理化すると（$x \neq 4$），
  $$\frac{\sqrt{x + 5} - 3}{x - 4} = \frac{(\sqrt{x + 5} - 3)(\sqrt{x + 5} + 3)}{(x - 4)(\sqrt{x + 5} + 3)}$$
  $$= \frac{(x + 5) - 9}{(x - 4)(\sqrt{x + 5} + 3)} = \frac{x - 4}{(x - 4)(\sqrt{x + 5} + 3)} = \frac{1}{\sqrt{x + 5} + 3}$$
  > 💡 讲师批注：分子有理化后刚好出现与分母相同的零因子 $(x - 4)$，约分即可消除不定形！

  よって，
  $$\lim_{x \to 4} \frac{\sqrt{x + 5} - 3}{x - 4} = \lim_{x \to 4} \frac{1}{\sqrt{x + 5} + 3} = \frac{1}{\sqrt{4 + 5} + 3} = \frac{1}{3 + 3} = \frac{1}{6}$$
  > 💡 讲师批注：验算技巧——原式即 $f(x) = \sqrt{x+5}$ 在 $x=4$ 处的导数 $f'(4) = \frac{1}{2\sqrt{4+5}} = \frac{1}{6}$，完全一致！
- **【最终答案】**
  **$\dfrac{1}{6}$**

---

### 演習問題 3-(2)（P300 / 原书 P299）
- **【原题重现与翻译】**
  - 原题：次の等式が成り立つように，定数 $a, b$ の値を定めよ。
    $$\lim_{x \to 1} \frac{a\sqrt{x + 1} - b}{x - 1} = \sqrt{2}$$
  - 中文：确定常数 $a, b$ 的值，使等式 $\displaystyle \lim_{x \to 1} \frac{a\sqrt{x + 1} - b}{x - 1} = \sqrt{2}$ 成立。
- **【考点定位】**
  - 已知分式极限反求参数（待定系数法）：分母趋于 $0$ 且极限为有限值 $\implies$ **分子必趋于 $0$（必要条件）**，代回消元后求极限（充分性验证）。
- **【分步标准解答】**
  $x \to 1$ のとき，（分母）$= x - 1 \to 0$ であり，極限値が有限な値 $\sqrt{2}$ として存在するためには，（分子）$\to 0$ でなければならない。
  $$\lim_{x \to 1} (a\sqrt{x + 1} - b) = 0 \implies \sqrt{2}a - b = 0 \implies b = \sqrt{2}a \quad \cdots \text{①}$$
  > 💡 讲师批注：**标准必写逻辑链**：分母 $\to 0$ 且极限存在 $\implies$ 分子 $\to 0$（注意这只是**必要条件**，必须将 $b = \sqrt{2}a$ 代回原式计算极限，既求出 $a$ 又验证了充分性）。

  ① をもとの式の左辺に代入して，分子を有理化すると，
  $$\lim_{x \to 1} \frac{a\sqrt{x + 1} - \sqrt{2}a}{x - 1} = \lim_{x \to 1} \frac{a(\sqrt{x + 1} - \sqrt{2})}{x - 1}$$
  $$= \lim_{x \to 1} \frac{a(\sqrt{x + 1} - \sqrt{2})(\sqrt{x + 1} + \sqrt{2})}{(x - 1)(\sqrt{x + 1} + \sqrt{2})}$$
  $$= \lim_{x \to 1} \frac{a\{(x + 1) - 2\}}{(x - 1)(\sqrt{x + 1} + \sqrt{2})} = \lim_{x \to 1} \frac{a(x - 1)}{(x - 1)(\sqrt{x + 1} + \sqrt{2})}$$
  $$= \lim_{x \to 1} \frac{a}{\sqrt{x + 1} + \sqrt{2}} = \frac{a}{\sqrt{2} + \sqrt{2}} = \frac{a}{2\sqrt{2}}$$
  > 💡 讲师批注：把公因式 $a$ 先提出来再有理化，计算量减半、不易出错。

  条件より，$\dfrac{a}{2\sqrt{2}} = \sqrt{2}$ であるから，
  $$a = \sqrt{2} \cdot 2\sqrt{2} = 4$$
  ① に代入して，
  $$b = \sqrt{2} \cdot 4 = 4\sqrt{2}$$
  （検算：$a=4,\; b=4\sqrt{2}$ のとき，$\lim_{x\to 1} \frac{4\sqrt{x+1}-4\sqrt{2}}{x-1} = \frac{4}{2\sqrt{2}} = \sqrt{2}$ となり確かに成り立つ。）
- **【最终答案】**
  **$a = 4,\quad b = 4\sqrt{2}$**
