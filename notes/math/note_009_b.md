# 《EJU 教材全解与备课讲义》数学 009-B（P130–P135）

> **对应源文件**：`work_math/ocr_md/ocr_009_p121-135.md`（本册承接 `note_009_a.md`，覆盖 P130–P135「加法定理とその応用」之公式推导与演習問題 4 全部 7 大题）
> **视觉核对参考图**：`work_math/ref_imgs/page_0130.jpg` – `page_0135.jpg`

---

## 一、核心定理证明脉络速览（P130–P132）

> 本切片完整知识梳理、国内 vs EJU 考纲对比及日文核心词汇与口语读法见 [note_009_a.md](file:///Users/baohan/Desktop/EJU/notes_math/note_009_a.md)。此处提炼 P130–P132 的核心推导脉络，便于课堂板书串讲：

1. **加法定理母公式 $\cos(\alpha - \beta) = \cos\alpha\cos\beta + \sin\alpha\sin\beta$ 的证明（P131）**：
   在单位圆上取两点 $A(\cos\alpha, \sin\alpha)$ 与 $B(\cos\beta, \sin\beta)$，分别用**两点间距离公式**与**余弦定理**表示 $AB^2$：
   $$(\cos\beta - \cos\alpha)^2 + (\sin\beta - \sin\alpha)^2 = 1^2 + 1^2 - 2\cdot 1 \cdot 1 \cdot \cos(\alpha - \beta)$$
   展开左边得 $2 - 2(\cos\alpha\cos\beta + \sin\alpha\sin\beta) = 2 - 2\cos(\alpha - \beta)$，消去 $2$ 与 $-2$ 即证！
2. **由加法定理一键派生三大公式簇**：
   - **2 倍角公式**：令 $\beta = \alpha$ 即得 $\sin 2\alpha,\; \cos 2\alpha,\; \tan 2\alpha$。
   - **半角公式**：由 $\cos 2\alpha = 1 - 2\sin^2\alpha = 2\cos^2\alpha - 1$ 反解降幂，再将 $\alpha \to \dfrac{\alpha}{2}$ 即得。
   - **3 倍角公式**：将 $3\alpha = 2\alpha + \alpha$ 展开后统一为单函数即得。
3. **两直线夹锐角公式的几何推导（P132）**：
   将两直线平移至过原点 $y = m_1 x,\; y = m_2 x$，倾斜角分别为 $\alpha, \beta$（$0 \le \beta < \alpha < \pi$），则 $\tan\alpha = m_1,\; \tan\beta = m_2$。
   令 $\theta' = \alpha - \beta \in (0, \pi)$，由 $\tan\theta' = \dfrac{m_1 - m_2}{1 + m_1 m_2}$：
   - 若右式 $> 0$，则 $\theta'$ 为锐角，$\tan\theta = \tan\theta'$；
   - 若右式 $< 0$，则 $\theta'$ 为钝角，其补角 $\theta = \pi - \theta'$ 为锐角，$\tan\theta = -\tan\theta'$；
   综合两种情况即得 $\tan\theta = \left|\dfrac{m_1 - m_2}{1 + m_1 m_2}\right|$。

---

## 三、逐题深度解析（下：演習問題 4）

### 演習問題 4（P132–P135）

#### 演習問題 4 (1)（P132）

**【原题重现与翻译】**
> **日文原题**：加法定理を用いて、次の値を求めよ。
> `[1]` $\sin 15^\circ$　　`[2]` $\tan 75^\circ$　　`[3]` $\cos\dfrac{\pi}{12}$
> `[4]` $\sin 105^\circ$　　`[5]` $\cos 165^\circ$　　`[6]` $\tan\dfrac{7\pi}{12}$
>
> **中文翻译**：利用加法定理，求下列各式的值。

> ⚠️ **教材勘误提示**：原教材第 131 页（`page_0132.jpg`）题干助词误印为「加法定理**と**用いて」，正确日文应为「加法定理**を**用いて」。

**【考点定位】**
将非特殊角（$15^\circ$ 的奇数倍 / $\frac{\pi}{12}$ 的奇数倍）拆分为 $30^\circ, 45^\circ, 60^\circ, 120^\circ$ 等特殊角的和或差，套用加法定理并化简分母有理化。

**【分步标准解答】**

- **`[1]`** $\sin 15^\circ$
  $$\sin 15^\circ = \sin(45^\circ - 30^\circ) = \sin 45^\circ\cos 30^\circ - \cos 45^\circ\sin 30^\circ$$
  $$= \frac{\sqrt{2}}{2}\cdot\frac{\sqrt{3}}{2} - \frac{\sqrt{2}}{2}\cdot\frac{1}{2} = \frac{\sqrt{6} - \sqrt{2}}{4}$$
  > 💡 讲师批注：$15^\circ$ 与 $75^\circ$ 的正余弦值是 EJU 高频常客，建议直接背熟：$\sin 15^\circ = \cos 75^\circ = \dfrac{\sqrt{6}-\sqrt{2}}{4}$，$\cos 15^\circ = \sin 75^\circ = \dfrac{\sqrt{6}+\sqrt{2}}{4}$。

- **`[2]`** $\tan 75^\circ$
  $$\tan 75^\circ = \tan(45^\circ + 30^\circ) = \frac{\tan 45^\circ + \tan 30^\circ}{1 - \tan 45^\circ\tan 30^\circ} = \frac{1 + \frac{1}{\sqrt{3}}}{1 - 1\cdot\frac{1}{\sqrt{3}}} = \frac{\sqrt{3} + 1}{\sqrt{3} - 1}$$
  分母を有理化すると、
  $$\frac{(\sqrt{3} + 1)^2}{(\sqrt{3} - 1)(\sqrt{3} + 1)} = \frac{3 + 2\sqrt{3} + 1}{3 - 1} = \frac{4 + 2\sqrt{3}}{2} = 2 + \sqrt{3}$$

- **`[3]`** $\cos\dfrac{\pi}{12}$
  $\dfrac{\pi}{12} = \dfrac{\pi}{3} - \dfrac{\pi}{4}$（または $\dfrac{\pi}{4} - \dfrac{\pi}{6}$）であるから、
  $$\cos\frac{\pi}{12} = \cos\left(\frac{\pi}{3} - \frac{\pi}{4}\right) = \cos\frac{\pi}{3}\cos\frac{\pi}{4} + \sin\frac{\pi}{3}\sin\frac{\pi}{4}$$
  $$= \frac{1}{2}\cdot\frac{\sqrt{2}}{2} + \frac{\sqrt{3}}{2}\cdot\frac{\sqrt{2}}{2} = \frac{\sqrt{6} + \sqrt{2}}{4}$$

- **`[4]`** $\sin 105^\circ$
  $$\sin 105^\circ = \sin(60^\circ + 45^\circ) = \sin 60^\circ\cos 45^\circ + \cos 60^\circ\sin 45^\circ$$
  $$= \frac{\sqrt{3}}{2}\cdot\frac{\sqrt{2}}{2} + \frac{1}{2}\cdot\frac{\sqrt{2}}{2} = \frac{\sqrt{6} + \sqrt{2}}{4}$$
  > 💡 讲师批注：验算技巧：$\sin 105^\circ = \sin(180^\circ - 75^\circ) = \sin 75^\circ = \cos 15^\circ = \dfrac{\sqrt{6}+\sqrt{2}}{4}$，与 `[3]` 完全一致！

- **`[5]`** $\cos 165^\circ$
  $$\cos 165^\circ = \cos(120^\circ + 45^\circ) = \cos 120^\circ\cos 45^\circ - \sin 120^\circ\sin 45^\circ$$
  $$= \left(-\frac{1}{2}\right)\cdot\frac{\sqrt{2}}{2} - \frac{\sqrt{3}}{2}\cdot\frac{\sqrt{2}}{2} = -\frac{\sqrt{6} + \sqrt{2}}{4}$$
  > 💡 讲师批注：验算：$165^\circ$ 在第二象限，余弦值必为负，且 $\cos 165^\circ = -\cos 15^\circ = -\dfrac{\sqrt{6}+\sqrt{2}}{4}$。

- **`[6]`** $\tan\dfrac{7\pi}{12}$
  $\dfrac{7\pi}{12} = \dfrac{\pi}{3} + \dfrac{\pi}{4}$ であるから、
  $$\tan\frac{7\pi}{12} = \tan\left(\frac{\pi}{3} + \frac{\pi}{4}\right) = \frac{\tan\frac{\pi}{3} + \tan\frac{\pi}{4}}{1 - \tan\frac{\pi}{3}\tan\frac{\pi}{4}} = \frac{\sqrt{3} + 1}{1 - \sqrt{3}}$$
  分母を有理化すると、
  $$\frac{(\sqrt{3} + 1)(1 + \sqrt{3})}{(1 - \sqrt{3})(1 + \sqrt{3})} = \frac{4 + 2\sqrt{3}}{1 - 3} = -2 - \sqrt{3}$$
  > 💡 讲师批注：验算：$\frac{7\pi}{12} = 105^\circ = 180^\circ - 75^\circ$，故 $\tan 105^\circ = -\tan 75^\circ = -(2+\sqrt{3}) = -2-\sqrt{3}$！

**【最终答案】**
- **`[1]` $\dfrac{\sqrt{6} - \sqrt{2}}{4}$　　`[2]` $2 + \sqrt{3}$　　`[3]` $\dfrac{\sqrt{6} + \sqrt{2}}{4}$**
- **`[4]` $\dfrac{\sqrt{6} + \sqrt{2}}{4}$　　`[5]` $-\dfrac{\sqrt{6} + \sqrt{2}}{4}$　　`[6]` $-2 - \sqrt{3}$**

---

#### 演習問題 4 (2)（P133）

**【原题重现与翻译】**
> **日文原题**：$0 \le \theta < 2\pi$ のとき、次の方程式、不等式を求めよ。
> `[1]` $\sin 2\theta = \cos\theta$
> `[2]` $\cos 2\theta - 3\cos\theta + 2 \ge 0$
> `[3]` $\sin 2\theta - \sqrt{2}\sin\theta = 0$
> `[4]` $\cos 2\theta - \sin\theta \le 0$
>
> **中文翻译**：当 $0 \le \theta < 2\pi$ 时，解下列方程与不等式。

**【考点定位】**
二倍角公式统一角度（$2\theta \to \theta$）与函数名、因式分解求解；**特别注意带等号不等式中的孤立点解！**

**【分步标准解答】**

- **`[1]`** $\sin 2\theta = \cos\theta$
  $\sin 2\theta = 2\sin\theta\cos\theta$ を用いると、
  $$2\sin\theta\cos\theta - \cos\theta = 0 \iff \cos\theta(2\sin\theta - 1) = 0$$
  ゆえに $\cos\theta = 0$ または $\sin\theta = \dfrac{1}{2}$。
  $0 \le \theta < 2\pi$ の範囲で解くと、
  - $\cos\theta = 0$ より $\theta = \dfrac{\pi}{2},\; \dfrac{3}{2}\pi$
  - $\sin\theta = \dfrac{1}{2}$ より $\theta = \dfrac{\pi}{6},\; \dfrac{5}{6}\pi$
  > 💡 讲师批注：**严禁两边同除以 $\cos\theta$！** 否则会丢失 $\cos\theta = 0$ 对应的两个解 $\frac{\pi}{2}, \frac{3}{2}\pi$。必须移项提取公因式！

- **`[2]`** $\cos 2\theta - 3\cos\theta + 2 \ge 0$
  $\cos 2\theta = 2\cos^2\theta - 1$ を代入して $\cos\theta$ に統一すると、
  $$(2\cos^2\theta - 1) - 3\cos\theta + 2 \ge 0$$
  $$2\cos^2\theta - 3\cos\theta + 1 \ge 0$$
  $$(2\cos\theta - 1)(\cos\theta - 1) \ge 0$$
  よって、$\cos\theta \le \dfrac{1}{2}$ または $\cos\theta \ge 1$。
  ここで $-1 \le \cos\theta \le 1$ より、$\cos\theta \ge 1$ は **$\cos\theta = 1$** のみ成り立つ！
  $0 \le \theta < 2\pi$ の範囲で解くと、
  - $\cos\theta = 1$ より $\theta = 0$
  - $\cos\theta \le \dfrac{1}{2}$ より $\dfrac{\pi}{3} \le \theta \le \dfrac{5}{3}\pi$
  > 💡 讲师批注：**经典“孤立点”杀手题！** 80% 的同学会把 $\cos\theta - 1 \le 0$ 误认为严格小于 $0$ 而直接消去，从而漏掉 **$\theta = 0$** 这个孤立解！代入验算：$\theta = 0$ 时 $\cos 0 - 3\cos 0 + 2 = 1 - 3 + 2 = 0 \ge 0$，确实成立！

- **`[3]`** $\sin 2\theta - \sqrt{2}\sin\theta = 0$
  $$2\sin\theta\cos\theta - \sqrt{2}\sin\theta = 0 \iff \sin\theta(2\cos\theta - \sqrt{2}) = 0$$
  ゆえに $\sin\theta = 0$ または $\cos\theta = \dfrac{\sqrt{2}}{2}$。
  $0 \le \theta < 2\pi$ の範囲で解くと、
  - $\sin\theta = 0$ より $\theta = 0,\; \pi$
  - $\cos\theta = \dfrac{\sqrt{2}}{2}$ より $\theta = \dfrac{\pi}{4},\; \dfrac{7}{4}\pi$

- **`[4]`** $\cos 2\theta - \sin\theta \le 0$
  $\cos 2\theta = 1 - 2\sin^2\theta$ を代入して $\sin\theta$ に統一すると、
  $$(1 - 2\sin^2\theta) - \sin\theta \le 0$$
  $$2\sin^2\theta + \sin\theta - 1 \ge 0$$
  $$(2\sin\theta - 1)(\sin\theta + 1) \ge 0$$
  よって、$\sin\theta \le -1$ または $\sin\theta \ge \dfrac{1}{2}$。
  ここで $-1 \le \sin\theta \le 1$ より、$\sin\theta \le -1$ は **$\sin\theta = -1$** のみ成り立つ！
  $0 \le \theta < 2\pi$ の範囲で解くと、
  - $\sin\theta \ge \dfrac{1}{2}$ より $\dfrac{\pi}{6} \le \theta \le \dfrac{5}{6}\pi$
  - $\sin\theta = -1$ より $\theta = \dfrac{3}{2}\pi$
  > 💡 讲师批注：与 `[2]` 同款“孤立点”陷阱！千万别漏掉 $\theta = \frac{3}{2}\pi$（代入验算：$\cos 3\pi - \sin\frac{3\pi}{2} = -1 - (-1) = 0 \le 0$ 成立）。

**【最终答案】**
- **`[1]` $\theta = \dfrac{\pi}{6},\; \dfrac{\pi}{2},\; \dfrac{5}{6}\pi,\; \dfrac{3}{2}\pi$**
- **`[2]` $\theta = 0,\; \dfrac{\pi}{3} \le \theta \le \dfrac{5}{3}\pi$**
- **`[3]` $\theta = 0,\; \dfrac{\pi}{4},\; \pi,\; \dfrac{7}{4}\pi$**
- **`[4]` $\dfrac{\pi}{6} \le \theta \le \dfrac{5}{6}\pi,\; \theta = \dfrac{3}{2}\pi$**

---

#### 演習問題 4 (3)（P134）

**【原题重现与翻译】**
> **日文原题**：$0 < \alpha < \dfrac{\pi}{2},\; \dfrac{\pi}{2} < \beta < \pi,\; \sin\alpha = \dfrac{4}{5},\; \sin\beta = \dfrac{12}{13}$ のとき、$\sin(\alpha + \beta),\; \cos(\alpha - \beta),\; \tan(\alpha - \beta)$ の値をそれぞれ求めよ。
>
> **中文翻译**：当 $0 < \alpha < \dfrac{\pi}{2},\; \dfrac{\pi}{2} < \beta < \pi,\; \sin\alpha = \dfrac{4}{5},\; \sin\beta = \dfrac{12}{13}$ 时，分别求 $\sin(\alpha + \beta),\; \cos(\alpha - \beta),\; \tan(\alpha - \beta)$ 的值。

> ⚠️ **教材勘误提示**：原教材第 133 页（`page_0134.jpg`）将第二个角范围误印为「$\dfrac{\pi}{2} < \alpha < \pi$」（与前文 $0 < \alpha < \frac{\pi}{2}$ 矛盾），显然应为 **$\dfrac{\pi}{2} < \beta < \pi$**。

**【考点定位】**
由象限确定同角三角函数符号 + 加法定理直接求值。

**【分步标准解答】**
- $0 < \alpha < \dfrac{\pi}{2}$（第 1 象限）より $\cos\alpha > 0$ であるから、
  $$\cos\alpha = \sqrt{1 - \sin^2\alpha} = \sqrt{1 - \left(\frac{4}{5}\right)^2} = \frac{3}{5}, \qquad \tan\alpha = \frac{\sin\alpha}{\cos\alpha} = \frac{4}{3}$$
- $\dfrac{\pi}{2} < \beta < \pi$（第 2 象限）より $\cos\beta < 0$ であるから、
  $$\cos\beta = -\sqrt{1 - \sin^2\beta} = -\sqrt{1 - \left(\frac{12}{13}\right)^2} = -\frac{5}{13}, \qquad \tan\beta = \frac{\sin\beta}{\cos\beta} = -\frac{12}{5}$$
  > 💡 讲师批注：勾股数 $(3, 4, 5)$ 和 $(5, 12, 13)$ 可瞬间心算出绝对值，**唯一易错点是 $\beta$ 在第二象限，故 $\cos\beta$ 与 $\tan\beta$ 均带负号！**

加法定理より：
1. $\sin(\alpha + \beta) = \sin\alpha\cos\beta + \cos\alpha\sin\beta = \dfrac{4}{5}\left(-\dfrac{5}{13}\right) + \dfrac{3}{5}\cdot\dfrac{12}{13} = \dfrac{-20 + 36}{65} = \dfrac{16}{65}$
2. $\cos(\alpha - \beta) = \cos\alpha\cos\beta + \sin\alpha\sin\beta = \dfrac{3}{5}\left(-\dfrac{5}{13}\right) + \dfrac{4}{5}\cdot\dfrac{12}{13} = \dfrac{-15 + 48}{65} = \dfrac{33}{65}$
3. $\tan(\alpha - \beta) = \dfrac{\tan\alpha - \tan\beta}{1 + \tan\alpha\tan\beta} = \dfrac{\frac{4}{3} - \left(-\frac{12}{5}\right)}{1 + \frac{4}{3}\left(-\frac{12}{5}\right)} = \dfrac{\frac{20 + 36}{15}}{1 - \frac{48}{15}} = \dfrac{56}{15 - 48} = -\dfrac{56}{33}$
   > 💡 讲师批注：交叉验算：算出 $\sin(\alpha-\beta) = \frac{4}{5}(-\frac{5}{13}) - \frac{3}{5}\cdot\frac{12}{13} = -\frac{56}{65}$，则 $\frac{\sin(\alpha-\beta)}{\cos(\alpha-\beta)} = -\frac{56}{33}$，且 $33^2 + 56^2 = 1089 + 3136 = 4225 = 65^2$，100% 精确！

**【最终答案】**
- **$\sin(\alpha + \beta) = \dfrac{16}{65},\quad \cos(\alpha - \beta) = \dfrac{33}{65},\quad \tan(\alpha - \beta) = -\dfrac{56}{33}$**

---

#### 演習問題 4 (4)（P134）

**【原题重现与翻译】**
> **日文原题**：$\sin\alpha - \sin\beta = \dfrac{5}{4},\; \cos\alpha + \cos\beta = \dfrac{5}{4}$ のとき、$\cos(\alpha + \beta)$ の値をそれぞれ求めよ。
>
> **中文翻译**：当 $\sin\alpha - \sin\beta = \dfrac{5}{4},\; \cos\alpha + \cos\beta = \dfrac{5}{4}$ 时，求 $\cos(\alpha + \beta)$ 的值。

**【考点定位】**
两式分别平方后相加，利用 $\sin^2 x + \cos^2 x = 1$ 与余弦加法定理整体求值（EJU 经典技巧题）。

**【分步标准解答】**
与えられた 2 式の両辺をそれぞれ 2 乗すると、
$$\sin^2\alpha - 2\sin\alpha\sin\beta + \sin^2\beta = \frac{25}{16} \quad \cdots \text{①}$$
$$\cos^2\alpha + 2\cos\alpha\cos\beta + \cos^2\beta = \frac{25}{16} \quad \cdots \text{②}$$
① と ② の辺々を加えると、$\sin^2\alpha + \cos^2\alpha = 1,\; \sin^2\beta + \cos^2\beta = 1$ より、
$$(\sin^2\alpha + \cos^2\alpha) + (\sin^2\beta + \cos^2\beta) + 2(\cos\alpha\cos\beta - \sin\alpha\sin\beta) = \frac{25}{16} + \frac{25}{16}$$
$$1 + 1 + 2\cos(\alpha + \beta) = \frac{50}{16} = \frac{25}{8}$$
> 💡 讲师批注：注意观察符号！① 中交叉项是 **$-2\sin\alpha\sin\beta$**，② 中交叉项是 **$+2\cos\alpha\cos\beta$**，两者相加恰好凑出 $2(\cos\alpha\cos\beta - \sin\alpha\sin\beta) = 2\cos(\alpha + \beta)$！如果两式都是减号，则凑出的是 $\cos(\alpha - \beta)$。

よって、
$$2\cos(\alpha + \beta) = \frac{25}{8} - 2 = \frac{9}{8} \implies \cos(\alpha + \beta) = \frac{9}{16}$$

**【最终答案】**
- **$\cos(\alpha + \beta) = \dfrac{9}{16}$**

---

#### 演習問題 4 (5)（P135）

**【原题重现与翻译】**
> **日文原题**：2 直線 $\sqrt{3}x - 2y + 2 = 0,\; 3\sqrt{3}x + y - 1 = 0$ のなす鋭角 $\theta$ を求めよ。
>
> **中文翻译**：求两条直线 $\sqrt{3}x - 2y + 2 = 0$ 与 $3\sqrt{3}x + y - 1 = 0$ 所成的锐角 $\theta$。

**【考点定位】**
两直线的夹锐角公式 $\tan\theta = \left|\dfrac{m_1 - m_2}{1 + m_1 m_2}\right|$。

**【图解辅助（SVG 矢量图）】**

<svg viewBox="0 0 380 230" width="60%" xmlns="http://www.w3.org/2000/svg" style="background:#fafafa;border:1px solid #e0e0e0;border-radius:8px;margin:8px 0;">
  <rect x="0" y="0" width="380" height="230" fill="#fff" rx="6"/>
  <!-- axes: origin (170, 145) -->
  <line x1="25" y1="145" x2="355" y2="145" stroke="#6b7280" stroke-width="1.2"/>
  <line x1="170" y1="15" x2="170" y2="215" stroke="#6b7280" stroke-width="1.2"/>
  <text x="358" y="149" font-size="11" fill="#374151">x</text>
  <text x="175" y="23" font-size="11" fill="#374151">y</text>
  <text x="157" y="158" font-size="10" fill="#374151">O</text>
  <!-- scale: 1 unit = 45px -->
  <!-- Line 1: y = (√3/2)x + 1 -> x=-2(-90)->y=-0.73(33px down)->(80,178); x=2(90)->y=2.73(123px up)->(260,22) -->
  <line x1="65" y1="191" x2="275" y2="9" stroke="#2563eb" stroke-width="2"/>
  <text x="278" y="26" font-size="10.5" fill="#2563eb">ℓ₁: y = (√3/2)x + 1</text>
  <!-- Line 2: y = -3√3 x + 1 -> passes (0,1)=(170,100), slope -5.196 -> x=-0.35(-16)->y=2.82(127px up)->(154,18); x=0.45(20)->y=-1.34(60px down)->(190,205) -->
  <line x1="154" y1="17" x2="191" y2="210" stroke="#dc2626" stroke-width="2"/>
  <text x="200" y="205" font-size="10.5" fill="#dc2626">ℓ₂: y = -3√3 x + 1</text>
  <!-- Intersection point (0, 1) = (170, 100) -->
  <circle cx="170" cy="100" r="3.8" fill="#111827"/>
  <text x="176" y="96" font-size="10" fill="#111827">(0, 1)</text>
  <!-- Acute angle arc θ = 60° between rays going up-right (40.9°) and up-left (100.9°) -->
  <path d="M 192.6,80.4 A 30,30 0 0 0 164.3,70.5" fill="none" stroke="#059669" stroke-width="2.2"/>
  <text x="180" y="65" font-size="11.5" font-weight="bold" fill="#059669">θ = π/3 (60°)</text>
</svg>

**【分步标准解答】**
2 直線の方程式を $y = mx + n$ の形に直すと、
$$y = \frac{\sqrt{3}}{2}x + 1, \qquad y = -3\sqrt{3}x + 1$$
よって、2 直線の傾きはそれぞれ $m_1 = \dfrac{\sqrt{3}}{2},\; m_2 = -3\sqrt{3}$ である。
$m_1 m_2 = \dfrac{\sqrt{3}}{2}(-3\sqrt{3}) = -\dfrac{9}{2} \neq -1$ より、2 直線は垂直ではない。

2 直線のなす鋭角を $\theta\;\left(0 < \theta < \dfrac{\pi}{2}\right)$ とすると、
$$\tan\theta = \left|\frac{m_1 - m_2}{1 + m_1 m_2}\right| = \left|\frac{\frac{\sqrt{3}}{2} - (-3\sqrt{3})}{1 + \frac{\sqrt{3}}{2}\cdot(-3\sqrt{3})}\right| = \left|\frac{\frac{7\sqrt{3}}{2}}{1 - \frac{9}{2}}\right| = \left|\frac{\frac{7\sqrt{3}}{2}}{-\frac{7}{2}}\right| = \sqrt{3}$$
> 💡 讲师批注：分子分母同乘 $2$ 可瞬间消去繁分数：$\left|\dfrac{\sqrt{3} + 6\sqrt{3}}{2 - 9}\right| = \left|\dfrac{7\sqrt{3}}{-7}\right| = \sqrt{3}$！也可用法向量 $\vec{n}_1 = (\sqrt{3}, -2),\; \vec{n}_2 = (3\sqrt{3}, 1)$ 验算：$\cos\theta = \dfrac{|9 - 2|}{\sqrt{7}\cdot 2\sqrt{7}} = \dfrac{1}{2} \Rightarrow \theta = \dfrac{\pi}{3}$，完全一致！

$0 < \theta < \dfrac{\pi}{2}$ より、$\theta = \dfrac{\pi}{3}$。

**【最终答案】**
- **$\theta = \dfrac{\pi}{3}$（または $60^\circ$）**

---

#### 演習問題 4 (6)（P135）

**【原题重现与翻译】**
> **日文原题**：直線 $y = 2x - 1$ と $\dfrac{\pi}{4}$ の角をなす直線の傾きを求めよ。
>
> **中文翻译**：求与直线 $y = 2x - 1$ 成 $\dfrac{\pi}{4}$ 角的直线的斜率。

**【考点定位】**
两直线夹角公式的逆用（含绝对值方程，注意必然有**两条**互相垂直的直线）。

**【图解辅助（SVG 矢量图）】**

<svg viewBox="0 0 380 230" width="60%" xmlns="http://www.w3.org/2000/svg" style="background:#fafafa;border:1px solid #e0e0e0;border-radius:8px;margin:8px 0;">
  <rect x="0" y="0" width="380" height="230" fill="#fff" rx="6"/>
  <!-- origin (180, 125) -->
  <line x1="25" y1="125" x2="355" y2="125" stroke="#6b7280" stroke-width="1.2"/>
  <line x1="180" y1="15" x2="180" y2="215" stroke="#6b7280" stroke-width="1.2"/>
  <text x="358" y="129" font-size="11" fill="#374151">x</text>
  <text x="185" y="23" font-size="11" fill="#374151">y</text>
  <!-- reference line y = 2x (parallel to y=2x-1) through origin -->
  <line x1="135" y1="215" x2="230" y2="25" stroke="#111827" stroke-width="2.2"/>
  <text x="234" y="34" font-size="10.5" font-weight="bold" fill="#111827">基准斜率 m₁ = 2</text>
  <!-- m = 1/3 line -->
  <line x1="45" y1="170" x2="330" y2="75" stroke="#2563eb" stroke-width="2"/>
  <text x="260" y="72" font-size="10.5" fill="#2563eb">m = 1/3 (顺时针 45°)</text>
  <!-- m = -3 line -->
  <line x1="150" y1="35" x2="210" y2="215" stroke="#dc2626" stroke-width="2"/>
  <text x="48" y="45" font-size="10.5" fill="#dc2626">m = -3 (逆时针 45°)</text>
  <!-- 45 deg arcs -->
  <path d="M 218,112 A 40,40 0 0 0 198,89" fill="none" stroke="#2563eb" stroke-width="1.6"/>
  <text x="218" y="102" font-size="9.5" fill="#2563eb">π/4</text>
  <path d="M 198,89 A 40,40 0 0 0 167,87" fill="none" stroke="#dc2626" stroke-width="1.6"/>
  <text x="172" y="79" font-size="9.5" fill="#dc2626">π/4</text>
</svg>

**【分步标准解答】**
求める直線の傾きを $m$ とする。直線 $y = 2x - 1$ の傾きは $2$ である。
2 直線のなす角が $\dfrac{\pi}{4}$ であるから、2 直線は垂直ではない（すなわち $1 + 2m \neq 0$）。
よって、2 直線のなす角の公式より、
$$\tan\frac{\pi}{4} = \left|\frac{m - 2}{1 + 2m}\right|$$
$\tan\dfrac{\pi}{4} = 1$ であるから、
$$\left|\frac{m - 2}{1 + 2m}\right| = 1 \iff |m - 2| = |1 + 2m|$$
したがって、$m - 2 = \pm(1 + 2m)$：
- **① $m - 2 = 1 + 2m$ のとき**：$m = -3$
- **② $m - 2 = -(1 + 2m)$ のとき**：$m - 2 = -1 - 2m \implies 3m = 1 \implies m = \dfrac{1}{3}$

いずれの値も $1 + 2m \neq 0$ を満たす。
> 💡 讲师批注：**绝妙的几何验算！** 与基准直线分别顺时针转 $\frac{\pi}{4}$ 和逆时针转 $\frac{\pi}{4}$ 的两条直线，它们彼此之间的夹角必然是 $\frac{\pi}{4} + \frac{\pi}{4} = \frac{\pi}{2}$（互相垂直）！检查斜率乘积：$(-3) \times \dfrac{1}{3} = -1$，完美验证！

**【最终答案】**
- **$-3,\; \dfrac{1}{3}$**

---

#### 演習問題 4 (7)（P135）

**【原题重现与翻译】**
> **日文原题**：$\dfrac{\pi}{2} < \theta < \pi,\; \sin\theta = \dfrac{3}{5}$ のとき、$\sin 2\theta,\; \cos 2\theta,\; \tan\dfrac{\theta}{2}$ の値を求めよ。
>
> **中文翻译**：当 $\dfrac{\pi}{2} < \theta < \pi,\; \sin\theta = \dfrac{3}{5}$ 时，求 $\sin 2\theta,\; \cos 2\theta,\; \tan\dfrac{\theta}{2}$ 的值。

**【考点定位】**
二倍角公式与半角公式的综合求值；**半角开方时的象限符号判定**。

**【分步标准解答】**
$\dfrac{\pi}{2} < \theta < \pi$（第 2 象限）より $\cos\theta < 0$ であるから、
$$\cos\theta = -\sqrt{1 - \sin^2\theta} = -\sqrt{1 - \left(\frac{3}{5}\right)^2} = -\frac{4}{5}$$

1. **$\sin 2\theta$（2 倍角の公式）**：
   $$\sin 2\theta = 2\sin\theta\cos\theta = 2\cdot\frac{3}{5}\cdot\left(-\frac{4}{5}\right) = -\frac{24}{25}$$

2. **$\cos 2\theta$（2 倍角の公式）**：
   $$\cos 2\theta = 1 - 2\sin^2\theta = 1 - 2\cdot\left(\frac{3}{5}\right)^2 = 1 - \frac{18}{25} = \frac{7}{25}$$
   > 💡 讲师批注：验算 $\sin^2 2\theta + \cos^2 2\theta = \left(-\frac{24}{25}\right)^2 + \left(\frac{7}{25}\right)^2 = \frac{576 + 49}{625} = 1$，完全正确！

3. **$\tan\dfrac{\theta}{2}$（半角の公式）**：
   半角の公式より、
   $$\tan^2\frac{\theta}{2} = \frac{1 - \cos\theta}{1 + \cos\theta} = \frac{1 - \left(-\frac{4}{5}\right)}{1 + \left(-\frac{4}{5}\right)} = \frac{\frac{9}{5}}{\frac{1}{5}} = 9$$
   ここで、$\dfrac{\pi}{2} < \theta < \pi$ の各辺を $2$ で割ると、
   $$\frac{\pi}{4} < \frac{\theta}{2} < \frac{\pi}{2}$$
   $\dfrac{\theta}{2}$ は第 1 象限の角であるから $\tan\dfrac{\theta}{2} > 0$。よって、
   $$\tan\frac{\theta}{2} = \sqrt{9} = 3$$
   > 💡 讲师批注：用半角公式开方前，**必须先把 $\theta$ 的范围除以 $2$** 写出 $\frac{\pi}{4} < \frac{\theta}{2} < \frac{\pi}{2}$，据此确定符号为正！另附无平方速算技巧：$\tan\dfrac{\theta}{2} = \dfrac{1 - \cos\theta}{\sin\theta} = \dfrac{1 - (-4/5)}{3/5} = \dfrac{9/5}{3/5} = 3$，一步出结果且自带符号，考场验算极佳！

**【最终答案】**
- **$\sin 2\theta = -\dfrac{24}{25},\quad \cos 2\theta = \dfrac{7}{25},\quad \tan\dfrac{\theta}{2} = 3$**
