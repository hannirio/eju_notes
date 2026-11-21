# 《EJU 教材全解与备课讲义》数学 025-B（P361–P375 下）

> **对应源文件**：`work_math/ocr_md/ocr_025_p361-375.md`（第 15 章《不定積分》之「演習問題 13-(18)～(30)」全解析）
> **视觉核对参考图**：`work_math/ref_imgs/page_0367.jpg` – `page_0373.jpg`
> **前序章节**：知识点唤醒、定积分【16.1】–【16.7】、日文核心词汇及 演習問題 13-(5)～(17) 详见 [`note_025_a.md`](file:///Users/baohan/Desktop/EJU/notes_math/note_025_a.md)。

---

## 三、逐题深度解析（下：演習問題 13-(18) ～ 13-(30)）

---

### 演習問題 13-(18)（P367 / 教材 P366）

#### 演習問題 13-(18)[1]
- **【原题重现与翻译】**
  - 原题：次の不定積分を求めよ。$\displaystyle \int \frac{dx}{x\sqrt{x + 1}}$
  - 中文：求不定积分 $\displaystyle \int \frac{dx}{x\sqrt{x + 1}}$。
- **【考点定位】**
  - 无理函数换元积分（$t = \sqrt{x+1}$）+ 部分分式分解。
- **【分步标准解答】**
  $t = \sqrt{x + 1}\;(t > 0)$ とおくと，$t^2 = x + 1 \implies x = t^2 - 1$ であり，両辺を $t$ で微分して $dx = 2t\,dt$。
  $$\int \frac{dx}{x\sqrt{x + 1}} = \int \frac{2t\,dt}{(t^2 - 1)t} = \int \frac{2}{(t - 1)(t + 1)}\,dt$$
  > 💡 讲师批注：令 $t = \sqrt{x+1}$ 后，分子的 $t$ 与分母的 $t$ 立刻约掉，转化为最基础的有理分式 $\frac{2}{t^2-1}$！

  部分分数分解を用いて，
  $$= \int \left(\frac{1}{t - 1} - \frac{1}{t + 1}\right)dt = \log|t - 1| - \log|t + 1| + C = \log\left|\frac{t - 1}{t + 1}\right| + C$$
  $t = \sqrt{x + 1}$ を戻して，
  $$= \log\left|\frac{\sqrt{x + 1} - 1}{\sqrt{x + 1} + 1}\right| + C \quad (C \text{ は積分定数})$$
  > 💡 讲师批注：当 $-1 < x < 0$ 时 $\sqrt{x+1}-1 < 0$，故绝对值不可省。求导验算：$\frac{1}{2\sqrt{x+1}}\left(\frac{1}{\sqrt{x+1}-1}-\frac{1}{\sqrt{x+1}+1}\right) = \frac{1}{x\sqrt{x+1}}$。✓
- **【最终答案】**
  **$\log\left|\dfrac{\sqrt{x + 1} - 1}{\sqrt{x + 1} + 1}\right| + C$**（$C$ 为积分常数）

---

#### 演習問題 13-(18)[2]
- **【原题重现与翻译】**
  - 原题：次の不定積分を求めよ。$\displaystyle \int \frac{dx}{\sqrt{x^2 + 1}}$
  - 中文：求不定积分 $\displaystyle \int \frac{dx}{\sqrt{x^2 + 1}}$。
  > ⚠️ **教材勘误提示（P366 / `page_0367.jpg`）**：原教材印作 $\int \frac{dx}{\sqrt{x^2 + 1}}\,dx$，末尾多印了一个 $dx$，应修正为 $\int \frac{dx}{\sqrt{x^2 + 1}}$（即 $\int \frac{1}{\sqrt{x^2 + 1}}\,dx$）。
- **【考点定位】**
  - **日本数学Ⅲ最高频经典积分**（欧拉代换 $t = x + \sqrt{x^2 + 1}$）。
- **【分步标准解答】**
  $t = x + \sqrt{x^2 + 1}$ とおくと，すべての実数 $x$ に対して $\sqrt{x^2 + 1} > |x| \ge -x$ であるから $t > 0$。
  両辺を $x$ で微分すると，
  $$\frac{dt}{dx} = 1 + \frac{2x}{2\sqrt{x^2 + 1}} = 1 + \frac{x}{\sqrt{x^2 + 1}} = \frac{\sqrt{x^2 + 1} + x}{\sqrt{x^2 + 1}} = \frac{t}{\sqrt{x^2 + 1}}$$
  > 💡 讲师批注：**必背神级代换！** 这个导数化简极其优雅：$\frac{dt}{dx} = \frac{t}{\sqrt{x^2+1}} \iff \frac{dx}{\sqrt{x^2+1}} = \frac{dt}{t}$，瞬间一步到位！

  したがって，
  $$\int \frac{dx}{\sqrt{x^2 + 1}} = \int \frac{dt}{t} = \log|t| + C = \log\left(x + \sqrt{x^2 + 1}\right) + C \quad (C \text{ は積分定数})$$
  > 💡 讲师批注：因为 $x + \sqrt{x^2+1} > 0$ 恒成立，可去掉绝对值。一般形式 $\displaystyle \int \frac{dx}{\sqrt{x^2 + a}} = \log|x + \sqrt{x^2 + a}| + C$（$a \neq 0$）请务必烂熟于心！✓
- **【最终答案】**
  **$\log\left(x + \sqrt{x^2 + 1}\right) + C$**（$C$ 为积分常数）

---

### 演習問題 13-(19)（P367 / 教材 P366）

#### 演習問題 13-(19)[1]
- **【原题重现与翻译】**
  - 原题：次の不定積分を求めよ。$\displaystyle \int \sqrt{x^2 + 1}\,dx$
  - 中文：求不定积分 $\displaystyle \int \sqrt{x^2 + 1}\,dx$。
- **【考点定位】**
  - 分部积分法 + 方程思想（联动 13-(18)[2] 的结论）。
- **【分步标准解答】**
  $I = \displaystyle \int \sqrt{x^2 + 1}\,dx$ とおく。$1 = (x)'$ として部分積分法を適用すると，
  $$\begin{aligned}
  I &= \int (x)' \sqrt{x^2 + 1}\,dx \\
    &= x\sqrt{x^2 + 1} - \int x \cdot \frac{x}{\sqrt{x^2 + 1}}\,dx \\
    &= x\sqrt{x^2 + 1} - \int \frac{(x^2 + 1) - 1}{\sqrt{x^2 + 1}}\,dx \\
    &= x\sqrt{x^2 + 1} - \int \sqrt{x^2 + 1}\,dx + \int \frac{dx}{\sqrt{x^2 + 1}}
  \end{aligned}$$
  > 💡 讲师批注：把分子 $x^2$ 拆成 $(x^2+1)-1$ 是关键一步！这样右侧自动再现了原积分 $-I$ 与 13-(18)[2] 已求出的 $\int \frac{dx}{\sqrt{x^2+1}}$。

  演習問題 13-(18)[2] の結果 $\displaystyle \int \frac{dx}{\sqrt{x^2 + 1}} = \log\left(x + \sqrt{x^2 + 1}\right) + C_1$ を用いて，
  $$I = x\sqrt{x^2 + 1} - I + \log\left(x + \sqrt{x^2 + 1}\right) + C_1$$
  $I$ を左辺に移項して $2$ で割ると，
  $$2I = x\sqrt{x^2 + 1} + \log\left(x + \sqrt{x^2 + 1}\right) + C_1$$
  $$I = \frac{1}{2}\left\{ x\sqrt{x^2 + 1} + \log\left(x + \sqrt{x^2 + 1}\right) \right\} + C \quad (C \text{ は積分定数})$$
  > 💡 讲师批注：求导验算：$\frac{1}{2}\left(\sqrt{x^2+1} + \frac{x^2}{\sqrt{x^2+1}} + \frac{1}{\sqrt{x^2+1}}\right) = \frac{1}{2}\cdot 2\sqrt{x^2+1} = \sqrt{x^2+1}$。✓
- **【最终答案】**
  **$\dfrac{1}{2}\left\{ x\sqrt{x^2 + 1} + \log\left(x + \sqrt{x^2 + 1}\right) \right\} + C$**（$C$ 为积分常数）

---

### 演習問題 13-(20)（P368 / 教材 P367）

#### 演習問題 13-(20)[1]
- **【原题重现与翻译】**
  - 原题：次の不定積分を求めよ。$\displaystyle \int \frac{1}{x^3 + 1}\,dx$
  - 中文：求不定积分 $\displaystyle \int \frac{1}{x^3 + 1}\,dx$。
- **【考点定位】**
  - 三次有理函数积分（立方和分解 + 部分分式 + 配方 + $\tan^{-1}$ 积分），综合度极高。
- **【分步标准解答】**
  $x^3 + 1 = (x + 1)(x^2 - x + 1)$ であるから，
  $$\frac{1}{x^3 + 1} = \frac{A}{x + 1} + \frac{Bx + C}{x^2 - x + 1}$$
  とおいて両辺に $x^3 + 1$ を掛けると，
  $$1 = A(x^2 - x + 1) + (Bx + C)(x + 1) = (A + B)x^2 + (-A + B + C)x + (A + C)$$
  - $x = -1$ を代入して：$1 = 3A \implies A = \dfrac{1}{3}$
  - $x^2$ の係数比較：$A + B = 0 \implies B = -\dfrac{1}{3}$
  - 定数項の比較：$A + C = 1 \implies C = \dfrac{2}{3}$

  よって，
  $$\frac{1}{x^3 + 1} = \frac{1}{3} \cdot \frac{1}{x + 1} - \frac{1}{3} \cdot \frac{x - 2}{x^2 - x + 1}$$
  第2項の分子 $x - 2$ を，分母の導関数 $(x^2 - x + 1)' = 2x - 1$ を用いて分解する：
  $$x - 2 = \frac{1}{2}(2x - 1) - \frac{3}{2}$$
  > 💡 讲师批注：**万能拆分子法！** 对 $\frac{px+q}{x^2+bx+c}$，永远先凑出分母的导数 $2x+b$（这部分直接积成 $\log$），剩下的纯常数项通过分母配方积成 $\tan^{-1}$！

  したがって，
  $$\begin{aligned}
  \int \frac{1}{x^3 + 1}\,dx &= \frac{1}{3}\int \frac{dx}{x + 1} - \frac{1}{6}\int \frac{2x - 1}{x^2 - x + 1}\,dx + \frac{1}{2}\int \frac{dx}{x^2 - x + 1}
  \end{aligned}$$
  ここで，$x^2 - x + 1 = \left(x - \dfrac{1}{2}\right)^2 + \left(\dfrac{\sqrt{3}}{2}\right)^2 > 0$ であるから，公式 $\displaystyle \int \frac{du}{u^2 + a^2} = \frac{1}{a}\tan^{-1}\frac{u}{a} + C$（$u = x - \frac{1}{2},\; a = \frac{\sqrt{3}}{2}$）を用いて，
  $$\int \frac{dx}{x^2 - x + 1} = \frac{2}{\sqrt{3}}\tan^{-1}\left(\frac{x - \frac{1}{2}}{\frac{\sqrt{3}}{2}}\right) + C' = \frac{2}{\sqrt{3}}\tan^{-1}\left(\frac{2x - 1}{\sqrt{3}}\right) + C'$$
  ゆえに，
  $$\int \frac{1}{x^3 + 1}\,dx = \frac{1}{3}\log|x + 1| - \frac{1}{6}\log(x^2 - x + 1) + \frac{1}{\sqrt{3}}\tan^{-1}\left(\frac{2x - 1}{\sqrt{3}}\right) + C \quad (C \text{ は積分定数})$$
  > 💡 讲师批注：因 $x^2-x+1 > 0$ 恒成立，第二项省略绝对值。求导验算：$\frac{1}{3(x+1)} - \frac{2x-1}{6(x^2-x+1)} + \frac{1}{2(x^2-x+1)} = \frac{1}{x^3+1}$。✓
- **【最终答案】**
  **$\dfrac{1}{3}\log|x + 1| - \dfrac{1}{6}\log(x^2 - x + 1) + \dfrac{1}{\sqrt{3}}\tan^{-1}\left(\dfrac{2x - 1}{\sqrt{3}}\right) + C$**（$C$ 为积分常数）

---

### 演習問題 13-(21)（P368 / 教材 P367）

#### 演習問題 13-(21)[1]
- **【原题重现与翻译】**
  - 原题：次の不定積分を求めよ。$\displaystyle \int \cos^2 x\,dx$
  - 中文：求不定积分 $\displaystyle \int \cos^2 x\,dx$。
- **【考点定位】**
  - 三角函数偶次幂积分（半角/倍角降幂公式）。
- **【分步标准解答】**
  半角の公式 $\cos^2 x = \dfrac{1 + \cos 2x}{2}$ を用いると，
  $$\int \cos^2 x\,dx = \int \frac{1 + \cos 2x}{2}\,dx = \frac{1}{2}x + \frac{1}{4}\sin 2x + C \quad (C \text{ は積分定数})$$
  > 💡 讲师批注：求导验算：$\frac{1}{2} + \frac{1}{2}\cos 2x = \cos^2 x$。✓
- **【最终答案】**
  **$\dfrac{1}{2}x + \dfrac{1}{4}\sin 2x + C$**（$C$ 为积分常数）

---

#### 演習問題 13-(21)[2]
- **【原题重现与翻译】**
  - 原题：次の不定積分を求めよ。$\displaystyle \int \cos^3 x\,dx$
  - 中文：求不定积分 $\displaystyle \int \cos^3 x\,dx$。
- **【考点定位】**
  - 三角函数奇次幂积分（拆出一次 $\cos x\,dx = d(\sin x)$）。
- **【分步标准解答】**
  $$\int \cos^3 x\,dx = \int \cos^2 x \cdot \cos x\,dx = \int (1 - \sin^2 x)\cos x\,dx$$
  $t = \sin x$ とおくと $dt = \cos x\,dx$ であるから，
  $$= \int (1 - t^2)\,dt = t - \frac{1}{3}t^3 + C = \sin x - \frac{1}{3}\sin^3 x + C \quad (C \text{ は積分定数})$$
  > 💡 讲师批注：求导验算：$\cos x - \sin^2 x \cos x = \cos^3 x$。✓
- **【最终答案】**
  **$\sin x - \dfrac{1}{3}\sin^3 x + C$**（$C$ 为积分常数）

---

### 演習問題 13-(22)（P369 / 教材 P368）

#### 演習問題 13-(22)[1]
- **【原题重现与翻译】**
  - 原题：次の不定積分を求めよ。$\displaystyle \int \sin 2x \cos 3x\,dx$
  - 中文：求不定积分 $\displaystyle \int \sin 2x \cos 3x\,dx$。
- **【考点定位】**
  - 积化和差公式（積和の公式）在积分中的应用。
- **【分步标准解答】**
  積和の公式 $\sin\alpha \cos\beta = \dfrac{1}{2}\{\sin(\alpha + \beta) + \sin(\alpha - \beta)\}$ を用いると，
  $$\sin 2x \cos 3x = \frac{1}{2}\{\sin(2x + 3x) + \sin(2x - 3x)\} = \frac{1}{2}(\sin 5x - \sin x)$$
  > 💡 讲师批注：注意 $\sin(-x) = -\sin x$（正弦是奇函数），切勿漏掉负号！

  よって，
  $$\int \sin 2x \cos 3x\,dx = \frac{1}{2}\int (\sin 5x - \sin x)\,dx = \frac{1}{2}\left(-\frac{1}{5}\cos 5x + \cos x\right) + C$$
  $$= -\frac{1}{10}\cos 5x + \frac{1}{2}\cos x + C \quad (C \text{ は積分定数})$$
  > 💡 讲师批注：求导验算：$\frac{1}{2}\sin 5x - \frac{1}{2}\sin x = \sin 2x \cos 3x$。✓
- **【最终答案】**
  **$-\dfrac{1}{10}\cos 5x + \dfrac{1}{2}\cos x + C$**（$C$ 为积分常数）

---

#### 演習問題 13-(22)[2]
- **【原题重现与翻译】**
  - 原题：次の不定積分を求めよ。$\displaystyle \int \frac{\sin x - \sin^3 x}{1 + \cos x}\,dx$
  - 中文：求不定积分 $\displaystyle \int \frac{\sin x - \sin^3 x}{1 + \cos x}\,dx$。
- **【考点定位】**
  - 三角恒等变形 + 换元积分（$t = \cos x$）+ 假分式拆分。
- **【分步标准解答】**
  分子を整理すると，$\sin x - \sin^3 x = \sin x(1 - \sin^2 x) = \sin x \cos^2 x$。
  $t = \cos x$ とおくと，$dt = -\sin x\,dx$（すなわち $\sin x\,dx = -dt$）であるから，
  $$\int \frac{\sin x - \sin^3 x}{1 + \cos x}\,dx = \int \frac{\cos^2 x}{1 + \cos x} \sin x\,dx = -\int \frac{t^2}{t + 1}\,dt$$
  > 💡 讲师批注：假分式 $\frac{t^2}{t+1}$ 只需用平方差配凑：$t^2 = (t^2 - 1) + 1 = (t - 1)(t + 1) + 1$，比长除法更快！

  $$= -\int \frac{(t^2 - 1) + 1}{t + 1}\,dt = -\int \left(t - 1 + \frac{1}{t + 1}\right)dt$$
  $$= -\left(\frac{1}{2}t^2 - t + \log|t + 1|\right) + C = -\frac{1}{2}\cos^2 x + \cos x - \log(1 + \cos x) + C \quad (C \text{ は積分定数})$$
  > 💡 讲师批注：因分母 $1+\cos x \neq 0$ 且 $\cos x \ge -1$，故 $1+\cos x > 0$，可去掉绝对值符号。求导验算：$\cos x\sin x - \sin x + \frac{\sin x}{1+\cos x} = \frac{\sin x \cos^2 x}{1+\cos x}$。✓
- **【最终答案】**
  **$-\dfrac{1}{2}\cos^2 x + \cos x - \log(1 + \cos x) + C$**（$C$ 为积分常数）

---

### 演習問題 13-(23)（P369 / 教材 P368）

#### 演習問題 13-(23)[1]
- **【原题重现与翻译】**
  - 原题：次の不定積分を求めよ。$\displaystyle \int \sin x \cos(\cos x)\,dx$
  - 中文：求不定积分 $\displaystyle \int \sin x \cos(\cos x)\,dx$。
- **【考点定位】**
  - 换元积分法（复合三角函数凑微分）。
- **【分步标准解答】**
  $t = \cos x$ とおくと，$dt = -\sin x\,dx$ より $\sin x\,dx = -dt$。
  $$\int \sin x \cos(\cos x)\,dx = -\int \cos t\,dt = -\sin t + C = -\sin(\cos x) + C \quad (C \text{ は積分定数})$$
  > 💡 讲师批注：求导验算：$-\cos(\cos x)\cdot(-\sin x) = \sin x \cos(\cos x)$。✓
- **【最终答案】**
  **$-\sin(\cos x) + C$**（$C$ 为积分常数）

---

#### 演習問題 13-(23)[2]
- **【原题重现与翻译】**
  - 原题：次の不定積分を求めよ。$\displaystyle \int \frac{1}{\cos x}\,dx$
  - 中文：求不定积分 $\displaystyle \int \frac{1}{\cos x}\,dx$。
  > ⚠️ **教材勘误提示（P368 / `page_0369.jpg`）**：原教材分母印作 $\int \frac{1}{\cos}\,dx$，漏印了自变量 $x$，应修正为 $\int \frac{1}{\cos x}\,dx$。
- **【考点定位】**
  - **日本高考/EJU 必考经典技巧**：$\int \frac{1}{\cos x}\,dx$ 的分子分母同乘 $\cos x$ 换元法。
- **【分步标准解答】**
  分母・分子に $\cos x$ を掛けると，
  $$\int \frac{1}{\cos x}\,dx = \int \frac{\cos x}{\cos^2 x}\,dx = \int \frac{\cos x}{1 - \sin^2 x}\,dx$$
  $t = \sin x$ とおくと，$dt = \cos x\,dx$ であるから，
  $$= \int \frac{1}{1 - t^2}\,dt = \frac{1}{2}\int \left(\frac{1}{1 + t} + \frac{1}{1 - t}\right)dt$$
  $$= \frac{1}{2}\left(\log|1 + t| - \log|1 - t|\right) + C = \frac{1}{2}\log\left|\frac{1 + t}{1 - t}\right| + C$$
  > 💡 讲师批注：切记 $\int \frac{1}{1-t}\,dt = -\log|1-t| + C$（分母 $-t$ 的系数带来负号）！

  $\cos x \neq 0$ より $-1 < \sin x < 1$ なので $\dfrac{1 + \sin x}{1 - \sin x} > 0$。よって絶対値を外して，
  $$= \frac{1}{2}\log\frac{1 + \sin x}{1 - \sin x} + C \quad (C \text{ は積分定数})$$
  > 💡 讲师批注：等价变形说明：上下同乘 $(1+\sin x)$ 得 $\frac{1}{2}\log\frac{(1+\sin x)^2}{\cos^2 x} = \log\left|\frac{1+\sin x}{\cos x}\right| = \log|\sec x + \tan x|$，与国内大学高数教材公式完全一致！✓
- **【最终答案】**
  **$\dfrac{1}{2}\log\dfrac{1 + \sin x}{1 - \sin x} + C$**（亦等价于 $\log\left|\dfrac{1 + \sin x}{\cos x}\right| + C$，$C$ 为积分常数）

---

### 演習問題 13-(24)（P370 / 教材 P369）

#### 演習問題 13-(24)[1]
- **【原题重现与翻译】**
  - 原题：次の不定積分を求めよ。$\displaystyle \int \frac{1}{\sin x + \cos x}\,dx$
  - 中文：求不定积分 $\displaystyle \int \frac{1}{\sin x + \cos x}\,dx$。
- **【考点定位】**
  - 三角函数合成（辅助角公式）+ 联动 13-(23)[2] 结论。
- **【分步标准解答】**
  三角関数の合成により，
  $$\sin x + \cos x = \sqrt{2}\left(\cos x \cos\frac{\pi}{4} + \sin x \sin\frac{\pi}{4}\right) = \sqrt{2}\cos\left(x - \frac{\pi}{4}\right)$$
  > 💡 讲师批注：合成为 $\sqrt{2}\cos\left(x - \frac{\pi}{4}\right)$ 可以直接复用上一题 (23)[2] 的 $\int \frac{1}{\cos u}\,du$！若合成为 $\sqrt{2}\sin\left(x + \frac{\pi}{4}\right)$，同样只需分子分母同乘 $\sin u$。

  $u = x - \dfrac{\pi}{4}$ とおくと $du = dx$ であり，演習問題 13-(23)[2] の結果を用いて，
  $$\begin{aligned}
  \int \frac{1}{\sin x + \cos x}\,dx &= \frac{1}{\sqrt{2}}\int \frac{du}{\cos u} \\
  &= \frac{1}{2\sqrt{2}}\log\frac{1 + \sin u}{1 - \sin u} + C \\
  &= \frac{1}{2\sqrt{2}}\log\frac{1 + \sin\left(x - \frac{\pi}{4}\right)}{1 - \sin\left(x - \frac{\pi}{4}\right)} + C \quad (C \text{ は積分定数})
  \end{aligned}$$
  > 💡 讲师批注：若用 $\sin\left(x + \frac{\pi}{4}\right)$ 与万能代换 $\tan\frac{u}{2}$，答案等价写作 $\dfrac{1}{\sqrt{2}}\log\left|\tan\left(\dfrac{x}{2} + \dfrac{\pi}{8}\right)\right| + C$。求导验算两者导数均为 $\dfrac{1}{\sin x + \cos x}$。✓
- **【最终答案】**
  **$\dfrac{1}{2\sqrt{2}}\log\dfrac{1 + \sin\left(x - \frac{\pi}{4}\right)}{1 - \sin\left(x - \frac{\pi}{4}\right)} + C$**（或 $\dfrac{1}{\sqrt{2}}\log\left|\tan\left(\dfrac{x}{2} + \dfrac{\pi}{8}\right)\right| + C$，$C$ 为积分常数）

---

### 演習問題 13-(25)（P370 / 教材 P369）

#### 演習問題 13-(25)[1]
- **【原题重现与翻译】**
  - 原题：次の不定積分を求めよ。$\displaystyle \int x^4 e^x\,dx$
  - 中文：求不定积分 $\displaystyle \int x^4 e^x\,dx$。
- **【考点定位】**
  - 高次多项式 $\times$ 指数函数的多次分部积分（附「表格法 / DI 法」速算图解）。
- **【图解辅助（SVG 矢量图：表格法速算分部积分）】**

<svg viewBox="0 0 540 215" width="100%" xmlns="http://www.w3.org/2000/svg" style="background:#fafafa;border:1px solid #e2e8f0;border-radius:8px;margin:10px 0;">
  <defs>
    <marker id="ar2" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#2563eb"/>
    </marker>
  </defs>
  <text x="270" y="22" text-anchor="middle" fill="#1e293b" font-size="13" font-weight="bold">连续分部积分「表格法」速算 ∫ x⁴ eˣ dx</text>
  <!-- Headers -->
  <rect x="65" y="34" width="60" height="24" rx="4" fill="#e2e8f0"/>
  <text x="95" y="51" text-anchor="middle" fill="#334155" font-size="11.5" font-weight="bold">符号</text>
  <rect x="145" y="34" width="110" height="24" rx="4" fill="#dbeafe"/>
  <text x="200" y="51" text-anchor="middle" fill="#1e40af" font-size="11.5" font-weight="bold">求导列 (D)</text>
  <rect x="315" y="34" width="110" height="24" rx="4" fill="#dcfce7"/>
  <text x="370" y="51" text-anchor="middle" fill="#166534" font-size="11.5" font-weight="bold">积分列 (I)</text>

  <!-- Rows -->
  <text x="95" y="80" text-anchor="middle" fill="#16a34a" font-size="13" font-weight="bold">+</text>
  <text x="200" y="80" text-anchor="middle" fill="#1e293b" font-size="12.5">x⁴</text>
  <text x="370" y="80" text-anchor="middle" fill="#1e293b" font-size="12.5">eˣ</text>

  <text x="95" y="106" text-anchor="middle" fill="#dc2626" font-size="13" font-weight="bold">−</text>
  <text x="200" y="106" text-anchor="middle" fill="#1e293b" font-size="12.5">4x³</text>
  <text x="370" y="106" text-anchor="middle" fill="#1e293b" font-size="12.5">eˣ</text>

  <text x="95" y="132" text-anchor="middle" fill="#16a34a" font-size="13" font-weight="bold">+</text>
  <text x="200" y="132" text-anchor="middle" fill="#1e293b" font-size="12.5">12x²</text>
  <text x="370" y="132" text-anchor="middle" fill="#1e293b" font-size="12.5">eˣ</text>

  <text x="95" y="158" text-anchor="middle" fill="#dc2626" font-size="13" font-weight="bold">−</text>
  <text x="200" y="158" text-anchor="middle" fill="#1e293b" font-size="12.5">24x</text>
  <text x="370" y="158" text-anchor="middle" fill="#1e293b" font-size="12.5">eˣ</text>

  <text x="95" y="184" text-anchor="middle" fill="#16a34a" font-size="13" font-weight="bold">+</text>
  <text x="200" y="184" text-anchor="middle" fill="#1e293b" font-size="12.5">24</text>
  <text x="370" y="184" text-anchor="middle" fill="#1e293b" font-size="12.5">eˣ</text>

  <text x="200" y="206" text-anchor="middle" fill="#94a3b8" font-size="12">0 (停止)</text>
  <text x="370" y="206" text-anchor="middle" fill="#1e293b" font-size="12.5">eˣ</text>

  <!-- Diagonal arrows -->
  <line x1="230" y1="78" x2="345" y2="100" stroke="#2563eb" stroke-width="1.3" marker-end="url(#ar2)"/>
  <line x1="230" y1="104" x2="345" y2="126" stroke="#2563eb" stroke-width="1.3" marker-end="url(#ar2)"/>
  <line x1="230" y1="130" x2="345" y2="152" stroke="#2563eb" stroke-width="1.3" marker-end="url(#ar2)"/>
  <line x1="230" y1="156" x2="345" y2="178" stroke="#2563eb" stroke-width="1.3" marker-end="url(#ar2)"/>
  <line x1="230" y1="182" x2="345" y2="202" stroke="#2563eb" stroke-width="1.3" marker-end="url(#ar2)"/>
</svg>

- **【分步标准解答】**
  部分積分法を繰り返し適用する：
  $$\begin{aligned}
  \int x^4 e^x\,dx &= x^4 e^x - 4\int x^3 e^x\,dx \\
  &= x^4 e^x - 4\left(x^3 e^x - 3\int x^2 e^x\,dx\right) \\
  &= x^4 e^x - 4x^3 e^x + 12\left(x^2 e^x - 2\int x e^x\,dx\right) \\
  &= x^4 e^x - 4x^3 e^x + 12x^2 e^x - 24\left(x e^x - \int e^x\,dx\right) \\
  &= (x^4 - 4x^3 + 12x^2 - 24x + 24)e^x + C \quad (C \text{ は積分定数})
  \end{aligned}$$
  > 💡 讲师批注：考场上用上面的「表格法」3 秒即可心算验算：多项式 $P(x)$ 与 $e^x$ 相乘的积分公式为 $\int P(x)e^x\,dx = \{P(x) - P'(x) + P''(x) - P'''(x) + \cdots\}e^x + C$！求导验算：$[(4x^3-12x^2+24x-24)+(x^4-4x^3+12x^2-24x+24)]e^x = x^4 e^x$。✓
- **【最终答案】**
  **$(x^4 - 4x^3 + 12x^2 - 24x + 24)e^x + C$**（$C$ 为积分常数）

---

### 演習問題 13-(26)（P371 / 教材 P370）

#### 演習問題 13-(26)[1]
- **【原题重现与翻译】**
  - 原题：次の不定積分を求めよ。$\displaystyle \int e^x \sin x\,dx$
  - 中文：求不定积分 $\displaystyle \int e^x \sin x\,dx$。
- **【考点定位】**
  - 循环分部积分法（指数 $\times$ 三角函数，做两次还原自身）。
- **【分步标准解答】**
  $I = \displaystyle \int e^x \sin x\,dx$ とおく。部分積分法を2回適用する（毎回 $e^x$ を積分側、三角関数を微分側に統一する）：
  $$\begin{aligned}
  I &= \int (e^x)' \sin x\,dx \\
    &= e^x \sin x - \int e^x \cos x\,dx \\
    &= e^x \sin x - \left\{ e^x \cos x - \int e^x (-\sin x)\,dx \right\} \\
    &= e^x \sin x - e^x \cos x - \int e^x \sin x\,dx \\
    &= e^x(\sin x - \cos x) - I
  \end{aligned}$$
  > 💡 讲师批注：**切忌中途换角色！** 第一次选 $e^x$ 积分、第二次就必须继续选 $e^x$ 积分；如果第二次反过来选 $\cos x$ 积分，就会得到 $I = I$ 的恒等废话。

  $I$ を左辺に移項して（積分定数を補い），
  $$2I = e^x(\sin x - \cos x) + C' \implies I = \frac{1}{2}e^x(\sin x - \cos x) + C \quad (C \text{ は積分定数})$$
  > 💡 讲师批注：求导验算：$\frac{1}{2}e^x\{(\sin x - \cos x) + (\cos x + \sin x)\} = e^x \sin x$。✓
- **【最终答案】**
  **$\dfrac{1}{2}e^x(\sin x - \cos x) + C$**（$C$ 为积分常数）

---

### 演習問題 13-(27)（P371 / 教材 P370）

#### 演習問題 13-(27)[1]
- **【原题重现与翻译】**
  - 原题：次の不定積分を求めよ。$\displaystyle \int e^{ax} \cos bx\,dx$
  - 中文：求不定积分 $\displaystyle \int e^{ax} \cos bx\,dx$。
- **【考点定位】**
  - 含参循环分部积分法（13-(26)[1] 的一般化公式）。
- **【分步标准解答】**
  $a, b$ が同時に $0$ でない場合（$a^2 + b^2 \neq 0$）を考える。
  $I = \displaystyle \int e^{ax} \cos bx\,dx$ とおく。

  **（i）$a \neq 0$ のとき**：
  $$\begin{aligned}
  I &= \int \left(\frac{1}{a}e^{ax}\right)' \cos bx\,dx \\
    &= \frac{1}{a}e^{ax}\cos bx + \frac{b}{a}\int e^{ax}\sin bx\,dx \\
    &= \frac{1}{a}e^{ax}\cos bx + \frac{b}{a}\left\{ \frac{1}{a}e^{ax}\sin bx - \frac{b}{a}\int e^{ax}\cos bx\,dx \right\} \\
    &= \frac{e^{ax}}{a^2}(a\cos bx + b\sin bx) - \frac{b^2}{a^2}I
  \end{aligned}$$
  移項して整理すると，
  $$\frac{a^2 + b^2}{a^2}I = \frac{e^{ax}}{a^2}(a\cos bx + b\sin bx) + C'$$
  両辺に $\dfrac{a^2}{a^2 + b^2}$ を掛けて，
  $$I = \frac{e^{ax}}{a^2 + b^2}(a\cos bx + b\sin bx) + C \quad (C \text{ は積分定数})$$
  **（ii）$a = 0,\; b \neq 0$ のとき**：
  $\displaystyle \int \cos bx\,dx = \frac{1}{b}\sin bx + C$ であり，上の公式に $a = 0$ を代入した $\dfrac{1}{b^2}(b\sin bx) + C$ と一致する。
  **（iii）$a = b = 0$ のとき**：
  $\displaystyle \int 1\,dx = x + C$。
  > 💡 讲师批注：本题原题未注明 $a \neq 0, b \neq 0$，严谨解答应补齐 $a=0$ 与 $a=b=0$ 的讨论。同时建议背诵对称公式：
  > - $\displaystyle \int e^{ax}\cos bx\,dx = \frac{e^{ax}}{a^2+b^2}(a\cos bx + b\sin bx) + C$
  > - $\displaystyle \int e^{ax}\sin bx\,dx = \frac{e^{ax}}{a^2+b^2}(a\sin bx - b\cos bx) + C$
  >
  > 求导验算：$\frac{e^{ax}}{a^2+b^2}\{a(a\cos bx + b\sin bx) + (-ab\sin bx + b^2\cos bx)\} = e^{ax}\cos bx$。✓
- **【最终答案】**
  - **$a^2 + b^2 \neq 0$ 时：$\dfrac{e^{ax}}{a^2 + b^2}(a\cos bx + b\sin bx) + C$**
  - **$a = b = 0$ 时：$x + C$**（$C$ 为积分常数）

---

### 演習問題 13-(28)（P372 / 教材 P371）

#### 演習問題 13-(28)[1]
- **【原题重现与翻译】**
  - 原题：次の不定積分を求めよ。$\displaystyle \int \sin^4 x \cos^2 x\,dx$
  - 中文：求不定积分 $\displaystyle \int \sin^4 x \cos^2 x\,dx$。
- **【考点定位】**
  - 三角函数高次偶次幂积分（倍角公式 + 半角降幂综合变形）。
- **【分步标准解答】**
  倍角の公式 $\sin x \cos x = \dfrac{1}{2}\sin 2x$ および半角の公式 $\sin^2 x = \dfrac{1 - \cos 2x}{2}$ を用いて次数を下げる：
  $$\begin{aligned}
  \sin^4 x \cos^2 x &= (\sin x \cos x)^2 \cdot \sin^2 x \\
  &= \left(\frac{1}{2}\sin 2x\right)^2 \cdot \frac{1 - \cos 2x}{2} \\
  &= \frac{1}{8}\sin^2 2x (1 - \cos 2x) \\
  &= \frac{1}{8}\sin^2 2x - \frac{1}{8}\sin^2 2x \cos 2x
  \end{aligned}$$
  > 💡 讲师批注：**绝妙配对技巧！** 千万别把 $\sin^4 x$ 和 $\cos^2 x$ 各自硬展开成 $(1-\cos 2x)^2(1+\cos 2x)$ 再狂乘——先把 $\sin^2 x \cos^2 x$ 打包成 $\frac{1}{4}\sin^2 2x$，计算量直接减半！

  さらに第1項に半角の公式 $\sin^2 2x = \dfrac{1 - \cos 4x}{2}$ を用いると，
  $$\begin{aligned}
  \int \sin^4 x \cos^2 x\,dx &= \frac{1}{16}\int (1 - \cos 4x)\,dx - \frac{1}{8}\int \sin^2 2x \cos 2x\,dx
  \end{aligned}$$
  第2項は $t = \sin 2x$（$dt = 2\cos 2x\,dx$）より $\displaystyle \int \sin^2 2x \cos 2x\,dx = \frac{1}{2} \cdot \frac{1}{3}\sin^3 2x = \frac{1}{6}\sin^3 2x$ であるから，
  $$= \frac{1}{16}\left(x - \frac{1}{4}\sin 4x\right) - \frac{1}{8} \cdot \frac{1}{6}\sin^3 2x + C$$
  $$= \frac{1}{16}x - \frac{1}{64}\sin 4x - \frac{1}{48}\sin^3 2x + C \quad (C \text{ は積分定数})$$
  > 💡 讲师批注：求导验算：$\frac{1}{16} - \frac{1}{16}\cos 4x - \frac{1}{8}\sin^2 2x \cos 2x = \frac{1}{8}\sin^2 2x - \frac{1}{8}\sin^2 2x \cos 2x = \frac{1}{8}\sin^2 2x(1-\cos 2x) = \sin^4 x \cos^2 x$。✓
- **【最终答案】**
  **$\dfrac{1}{16}x - \dfrac{1}{64}\sin 4x - \dfrac{1}{48}\sin^3 2x + C$**（$C$ 为积分常数）

---

### 演習問題 13-(29)（P372 / 教材 P371）

#### 演習問題 13-(29)[1]
- **【原题重现与翻译】**
  - 原题：次の不定積分を求めよ。$\displaystyle \int x^3 (\log x)^2\,dx$
  - 中文：求不定积分 $\displaystyle \int x^3 (\log x)^2\,dx$。
- **【考点定位】**
  - 连续两次分部积分（幂函数 $\times$ 对数函数平方）。
- **【分步标准解答】**
  $x^3 = \left(\dfrac{1}{4}x^4\right)'$ とみなして部分積分法を用いる（対数関数を微分側に選ぶ）：
  $$\begin{aligned}
  \int x^3 (\log x)^2\,dx &= \frac{1}{4}x^4 (\log x)^2 - \int \frac{1}{4}x^4 \cdot 2(\log x) \cdot \frac{1}{x}\,dx \\
  &= \frac{1}{4}x^4 (\log x)^2 - \frac{1}{2}\int x^3 \log x\,dx
  \end{aligned}$$
  もう一度部分積分法を用いて，
  $$\begin{aligned}
  &= \frac{1}{4}x^4 (\log x)^2 - \frac{1}{2}\left\{ \frac{1}{4}x^4 \log x - \int \frac{1}{4}x^4 \cdot \frac{1}{x}\,dx \right\} \\
  &= \frac{1}{4}x^4 (\log x)^2 - \frac{1}{8}x^4 \log x + \frac{1}{8}\int x^3\,dx \\
  &= \frac{1}{4}x^4 (\log x)^2 - \frac{1}{8}x^4 \log x + \frac{1}{32}x^4 + C \\
  &= \frac{x^4}{32}\left\{ 8(\log x)^2 - 4\log x + 1 \right\} + C \quad (C \text{ は積分定数})
  \end{aligned}$$
  > 💡 讲师批注：切记「对数 > 幂函数」原则，把 $(\log x)^2$ 放在微分侧，求导一次降幂一次，两次即彻底消灭对数。求导验算：$\frac{x^3}{32}\{32(\log x)^2 - 16\log x + 4 + 16\log x - 4\} = x^3(\log x)^2$。✓
- **【最终答案】**
  **$\dfrac{x^4}{32}\left\{ 8(\log x)^2 - 4\log x + 1 \right\} + C$**（$C$ 为积分常数）

---

#### 演習問題 13-(29)[2]
- **【原题重现与翻译】**
  - 原题：次の不定積分を求めよ。$\displaystyle \int x \sin^{-1} x\,dx$
  - 中文：求不定积分 $\displaystyle \int x \arcsin x\,dx$。
- **【考点定位】**
  - 分部积分法（反三角函数优先放在微分侧）+ 三角代换 $x = \sin\theta$。
- **【图解辅助（SVG 矢量图：三角代换回代直角三角形）】**

<svg viewBox="0 0 460 145" width="100%" xmlns="http://www.w3.org/2000/svg" style="background:#fafafa;border:1px solid #e2e8f0;border-radius:8px;margin:10px 0;">
  <!-- Right triangle -->
  <polygon points="55,120 225,120 225,32" fill="#eff6ff" stroke="#1e40af" stroke-width="2"/>
  <!-- Right angle mark -->
  <polyline points="212,120 212,107 225,107" fill="none" stroke="#1e40af" stroke-width="1.4"/>
  <!-- Angle theta arc -->
  <path d="M 92 120 A 37 37 0 0 0 88 103" fill="none" stroke="#dc2626" stroke-width="1.6"/>
  <text x="100" y="113" fill="#dc2626" font-size="12.5" font-style="italic">θ</text>
  <!-- Side labels -->
  <text x="130" y="68" fill="#1e40af" font-size="12.5" font-weight="bold">1</text>
  <text x="235" y="80" fill="#1e40af" font-size="12.5" font-weight="bold">x</text>
  <text x="140" y="136" text-anchor="middle" fill="#1e40af" font-size="12" font-weight="bold">√(1 − x²)</text>
  <!-- Formulas on right -->
  <text x="285" y="45" fill="#1e293b" font-size="12" font-weight="bold">令 x = sin θ (−π/2 ≤ θ ≤ π/2)</text>
  <text x="285" y="70" fill="#334155" font-size="11.5">• θ = sin⁻¹ x</text>
  <text x="285" y="92" fill="#334155" font-size="11.5">• cos θ = √(1 − x²) ≥ 0</text>
  <text x="285" y="114" fill="#334155" font-size="11.5">• sin 2θ = 2 sin θ cos θ = 2x√(1 − x²)</text>
</svg>

- **【分步标准解答】**
  $(\sin^{-1} x)' = \dfrac{1}{\sqrt{1 - x^2}}$ である。$\sin^{-1} x$ を微分側，$x = \left(\dfrac{1}{2}x^2\right)'$ を積分側として部分積分法を適用する：
  $$\int x \sin^{-1} x\,dx = \frac{1}{2}x^2 \sin^{-1} x - \frac{1}{2}\int \frac{x^2}{\sqrt{1 - x^2}}\,dx$$
  第2項について，$x = \sin\theta\;\left(-\dfrac{\pi}{2} \le \theta \le \dfrac{\pi}{2}\right)$ とおくと，$dx = \cos\theta\,d\theta$，$\sqrt{1 - x^2} = \cos\theta \ge 0$ より，
  $$\begin{aligned}
  \int \frac{x^2}{\sqrt{1 - x^2}}\,dx &= \int \frac{\sin^2\theta}{\cos\theta} \cdot \cos\theta\,d\theta = \int \sin^2\theta\,d\theta \\
  &= \int \frac{1 - \cos 2\theta}{2}\,d\theta = \frac{1}{2}\theta - \frac{1}{4}\sin 2\theta + C' \\
  &= \frac{1}{2}\theta - \frac{1}{2}\sin\theta \cos\theta + C' \\
  &= \frac{1}{2}\sin^{-1} x - \frac{1}{2}x\sqrt{1 - x^2} + C'
  \end{aligned}$$
  > 💡 讲师批注：因为 $-\frac{\pi}{2} \le \theta \le \frac{\pi}{2}$，所以 $\cos\theta \ge 0$，$\sqrt{1-\sin^2\theta} = \cos\theta$ 无需加绝对值。回代时 $\sin 2\theta = 2\sin\theta\cos\theta = 2x\sqrt{1-x^2}$。

  これを元の式に代入して整理すると，
  $$\begin{aligned}
  \int x \sin^{-1} x\,dx &= \frac{1}{2}x^2 \sin^{-1} x - \frac{1}{2}\left(\frac{1}{2}\sin^{-1} x - \frac{1}{2}x\sqrt{1 - x^2}\right) + C \\
  &= \frac{2x^2 - 1}{4}\sin^{-1} x + \frac{1}{4}x\sqrt{1 - x^2} + C \quad (C \text{ は積分定数})
  \end{aligned}$$
  > 💡 讲师批注：求导验算：$x\sin^{-1} x + \frac{2x^2-1}{4\sqrt{1-x^2}} + \frac{1}{4}\sqrt{1-x^2} - \frac{x^2}{4\sqrt{1-x^2}} = x\sin^{-1} x + \frac{2x^2-1+1-x^2-x^2}{4\sqrt{1-x^2}} = x\sin^{-1} x$。✓
- **【最终答案】**
  **$\dfrac{2x^2 - 1}{4}\sin^{-1} x + \dfrac{1}{4}x\sqrt{1 - x^2} + C$**（$C$ 为积分常数）

---

### 演習問題 13-(30)（P373 / 教材 P372）

- **【原题重现与翻译】**
  - 原题：$n$ は整数とし、$I_n = \displaystyle \int \sin^n x\,dx$ とする。このとき、次の等式が成り立つことを証明せよ。ただし、$\sin^0 x = 1$ である。
    $$n \ge 2 \text{ のとき} \qquad I_n = \frac{1}{n}\left\{-\sin^{n-1} x \cos x + (n - 1)I_{n-2}\right\}$$
  - 中文：设 $n$ 为整数，$I_n = \displaystyle \int \sin^n x\,dx$。证明：当 $n \ge 2$ 时，下式成立（规定 $\sin^0 x = 1$）：
    $$I_n = \frac{1}{n}\left\{-\sin^{n-1} x \cos x + (n - 1)I_{n-2}\right\}$$
  > ⚠️ **教材勘误提示（P372 / `page_0373.jpg`）**：原题题干「ただし、$\sin^0 = 1$ である」漏印了自变量 $x$，应为 $\sin^0 x = 1$。
- **【考点定位】**
  - 积分递推公式（漸化式）的推导——**ウォリス積分（Wallis 积分）的核心预备定理**。
- **【分步标准解答】**
  $n \ge 2$ のとき，$\sin^n x = \sin^{n-1} x \cdot \sin x = \sin^{n-1} x \cdot (-\cos x)'$ とみなして部分積分法を適用する：
  $$\begin{aligned}
  I_n &= \int \sin^{n-1} x \cdot (-\cos x)'\,dx \\
      &= -\sin^{n-1} x \cos x - \int (n - 1)\sin^{n-2} x \cos x \cdot (-\cos x)\,dx \\
      &= -\sin^{n-1} x \cos x + (n - 1)\int \sin^{n-2} x \cos^2 x\,dx
  \end{aligned}$$
  > 💡 讲师批注：把 $\sin^n x$ 拆出**一个** $\sin x$ 作为积分侧 $(-\cos x)'$，其余 $\sin^{n-1} x$ 作为微分侧，这是推导三角幂递推公式的标准起手式。

  ここで，$\cos^2 x = 1 - \sin^2 x$ を代入すると，
  $$\begin{aligned}
  I_n &= -\sin^{n-1} x \cos x + (n - 1)\int \sin^{n-2} x (1 - \sin^2 x)\,dx \\
      &= -\sin^{n-1} x \cos x + (n - 1)\int \sin^{n-2} x\,dx - (n - 1)\int \sin^n x\,dx \\
      &= -\sin^{n-1} x \cos x + (n - 1)I_{n-2} - (n - 1)I_n
  \end{aligned}$$
  右辺の $-(n - 1)I_n$ を左辺に移項すると，
  $$\{1 + (n - 1)\}I_n = -\sin^{n-1} x \cos x + (n - 1)I_{n-2}$$
  $$n I_n = -\sin^{n-1} x \cos x + (n - 1)I_{n-2}$$
  $n \ge 2 > 0$ より両辺を $n$ で割って，
  $$I_n = \frac{1}{n}\left\{-\sin^{n-1} x \cos x + (n - 1)I_{n-2}\right\}$$
  （証明終）
  > 💡 讲师批注：将此式两边取定积分 $[0, \frac{\pi}{2}]$，由于 $\Big[-\sin^{n-1}x\cos x\Big]_0^{\pi/2} = 0$，立刻得到日本大学入试大名鼎鼎的 **Wallis 递推公式**：$J_n = \dfrac{n-1}{n}J_{n-2}$，下一切片定积分中将频繁亮相！✓
- **【最终答案】**
  **如上分步推导，等式得证（Q.E.D.）。**

---

## 四、本切片高频经典不定积分速查表（考前必背）

| 题型特征 | 代表题号 | 必杀技 / 结论速记 |
| :--- | :--- | :--- |
| 分母含 $\sqrt{A} \pm \sqrt{B}$ | 13-(14)[2], 13-(17)[1] | **优先分母有理化**，往往直接消去分母！ |
| $\displaystyle \int \frac{dx}{\sqrt{x^2 + a}}$ | 13-(18)[2] | 欧拉代换 $t = x + \sqrt{x^2 + a}$ $\implies \log\big|x + \sqrt{x^2 + a}\big| + C$ |
| $\displaystyle \int \sqrt{x^2 + 1}\,dx$ | 13-(19)[1] | 分部积分产生 $-I$ 移项 $\implies \dfrac{1}{2}\left\{x\sqrt{x^2+1} + \log(x+\sqrt{x^2+1})\right\} + C$ |
| $\displaystyle \int \frac{dx}{x^2 + a^2}$ | 13-(15)[2], 13-(20)[1] | 令 $x = a\tan\theta$ $\implies \dfrac{1}{a}\tan^{-1}\dfrac{x}{a} + C$ |
| $\displaystyle \int \frac{dx}{\cos x}$ | 13-(23)[2], 13-(24)[1] | 上下同乘 $\cos x$ 换元 $t = \sin x$ $\implies \dfrac{1}{2}\log\dfrac{1+\sin x}{1-\sin x} + C$ |
| $\displaystyle \int e^{ax}\cos bx\,dx$ | 13-(26)[1], 13-(27)[1] | 两次循环分部积分 $\implies \dfrac{e^{ax}}{a^2+b^2}(a\cos bx + b\sin bx) + C$ |
| $\displaystyle \int \sin^n x\,dx$ | 13-(30) | 拆出 $\sin x = (-\cos x)'$ 分部积分 $\implies I_n = \dfrac{1}{n}\{-\sin^{n-1}x\cos x + (n-1)I_{n-2}\}$ |
