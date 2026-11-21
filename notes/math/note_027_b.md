# 《EJU 教材全解与备课讲义》数学 027-B（P391–P405 下篇）

> **对应源文件**：`work_math/ocr_md/ocr_027_p391-405.md`（面積〔演習問題 17 (5)–(12)〕，教材页码 P401–P404 / PDF 页码 P402–P405）
> **视觉核对参考图**：`work_math/ref_imgs/page_0402.jpg` – `page_0405.jpg`
> **衔接说明**：本切片的「一、国内高中基础知识点唤醒与 EJU 考纲差异对比」「二、日文核心词汇与公式假名注音」及演習問題 16 (1)–(5)、演習問題 17 (1)–(4) 详见上篇 [`note_027_a.md`](./note_027_a.md)；本下篇完整承接并解析 **演習問題 17 (5)–(12)**（共 8 大题 / 11 小问）。

---

## 三、逐题深度解析（不可跳步·续）

### 演習問題 17（面積·下半部分）

---

#### 演習問題 17-(5)
- **【原题重现与翻译】**
  - 原题：区間 $0 \le x \le 2\pi$ において、2つの曲線 $y = \sin x,\; y = \sin 2x$ で囲まれた図形の面積 $S$ を求めよ。
  - 中文：在区间 $0 \le x \le 2\pi$ 上，求两条曲线 $y = \sin x$ 与 $y = \sin 2x$ 围成的图形的面积 $S$。
- **【考点定位】**
  - 三角函数交点求解（二倍角公式因式分解）、图形中心对称性（点对称）简化定积分区间。
- **【图解辅助（SVG 矢量图）】**
<svg viewBox="0 0 420 220" width="420" height="220" xmlns="http://www.w3.org/2000/svg" style="background:#fff;border:1px solid #e2e8f0;border-radius:6px;">
  <!-- 坐标轴: x=0->40, x=2pi->380 (170px/pi); y=0->110 (70px/u) -->
  <line x1="20" y1="110" x2="402" y2="110" stroke="#1e293b" stroke-width="1.5"/>
  <polygon points="402,110 394,106 394,114" fill="#1e293b"/>
  <line x1="40" y1="205" x2="40" y2="15" stroke="#1e293b" stroke-width="1.5"/>
  <polygon points="40,15 36,23 44,23" fill="#1e293b"/>
  <text x="406" y="114" font-size="13" font-style="italic" fill="#1e293b">x</text>
  <text x="28" y="20" font-size="13" font-style="italic" fill="#1e293b">y</text>
  <text x="26" y="124" font-size="12" fill="#1e293b">O</text>
  <!-- 关键点: 0(40,110), pi/3(96.7,49.4), pi(210,110), 5pi/3(323.3,170.6), 2pi(380,110) -->
  <!-- 阴影区域 1: [0, pi/3] -->
  <path d="M 40 110 C 60 55, 80 35, 96.7 49.4 C 80 65, 60 85, 40 110 Z" fill="#bfdbfe" fill-opacity="0.75"/>
  <!-- 阴影区域 2: [pi/3, pi] -->
  <path d="M 96.7 49.4 C 125 32, 165 45, 210 110 C 175 185, 140 190, 125 110 C 115 72, 106 58, 96.7 49.4 Z" fill="#93c5fd" fill-opacity="0.7"/>
  <!-- 阴影区域 3: [pi, 5pi/3] -->
  <path d="M 210 110 C 245 35, 280 30, 295 110 C 305 148, 314 162, 323.3 170.6 C 295 188, 255 175, 210 110 Z" fill="#93c5fd" fill-opacity="0.7"/>
  <!-- 阴影区域 4: [5pi/3, 2pi] -->
  <path d="M 323.3 170.6 C 340 185, 360 165, 380 110 C 360 135, 340 155, 323.3 170.6 Z" fill="#bfdbfe" fill-opacity="0.75"/>
  <!-- 曲线 y = sin x (蓝) -->
  <path d="M 40 110 C 90 15, 160 15, 210 110 C 260 205, 330 205, 380 110" fill="none" stroke="#2563eb" stroke-width="2.2"/>
  <!-- 曲线 y = sin 2x (橙) -->
  <path d="M 40 110 C 65 15, 100 15, 125 110 C 150 205, 185 205, 210 110 C 235 15, 270 15, 295 110 C 320 205, 355 205, 380 110" fill="none" stroke="#ea580c" stroke-width="2.2"/>
  <!-- 交点标注与虚线 -->
  <line x1="96.7" y1="49.4" x2="96.7" y2="110" stroke="#64748b" stroke-width="1" stroke-dasharray="3,2"/>
  <line x1="323.3" y1="110" x2="323.3" y2="170.6" stroke="#64748b" stroke-width="1" stroke-dasharray="3,2"/>
  <circle cx="40" cy="110" r="3" fill="#dc2626"/>
  <circle cx="96.7" cy="49.4" r="3" fill="#dc2626"/>
  <circle cx="210" cy="110" r="3.5" fill="#dc2626"/>
  <circle cx="323.3" cy="170.6" r="3" fill="#dc2626"/>
  <circle cx="380" cy="110" r="3" fill="#dc2626"/>
  <!-- 刻度与图例 -->
  <text x="89" y="126" font-size="11" fill="#1e293b">π/3</text>
  <text x="205" y="126" font-size="11" fill="#1e293b">π</text>
  <text x="313" y="102" font-size="11" fill="#1e293b">5π/3</text>
  <text x="373" y="126" font-size="11" fill="#1e293b">2π</text>
  <text x="24" y="44" font-size="11" fill="#1e293b">1</text>
  <text x="20" y="183" font-size="11" fill="#1e293b">-1</text>
  <text x="145" y="34" font-size="12" fill="#2563eb" font-weight="bold">y = sin x</text>
  <text x="240" y="34" font-size="12" fill="#ea580c" font-weight="bold">y = sin 2x</text>
  <text x="152" y="102" font-size="13" font-style="italic" fill="#1e3a8a" font-weight="bold">S₂</text>
  <text x="255" y="102" font-size="13" font-style="italic" fill="#1e3a8a" font-weight="bold">S₂</text>
</svg>
- **【分步标准解答】**
  2つの曲線 $y = \sin x$ と $y = \sin 2x$ の交点の $x$ 座標を求める。
  $$\sin 2x = \sin x \iff 2\sin x\cos x - \sin x = 0 \iff \sin x(2\cos x - 1) = 0$$
  $0 \le x \le 2\pi$ において，$\sin x = 0$ または $\cos x = \dfrac{1}{2}$ より，
  $$x = 0,\; \frac{\pi}{3},\; \pi,\; \frac{5\pi}{3},\; 2\pi$$
  > 💡 讲师批注：解 $\sin 2x = \sin x$ 时切忌直接两边约去 $\sin x$（会丢掉 $x = 0, \pi, 2\pi$ 这三个交点！），必须移项提公因式。

  ここで，$f(x) = \sin 2x - \sin x$ とおくと，
  $$f(2\pi - x) = \sin(4\pi - 2x) - \sin(2\pi - x) = -\sin 2x + \sin x = -f(x)$$
  より，2つの曲線で囲まれた図形は点 $(\pi, 0)$ に関して対称である。したがって，求める面積 $S$ は区間 $0 \le x \le \pi$ の部分の面積の $2$ 倍となる。
  > 💡 讲师批注：发现关于 $(\pi, 0)$ 点对称后，积分段数立刻从 4 段减半为 2 段，大幅降低符号出错率！

  区間 $0 \le x \le \pi$ において $\sin x \ge 0$ であるから，$f(x) = \sin x(2\cos x - 1)$ の符号は：
  - $0 \le x \le \dfrac{\pi}{3}$ のとき，$\cos x \ge \dfrac{1}{2}$ より $\sin 2x \ge \sin x$
  - $\dfrac{\pi}{3} \le x \le \pi$ のとき，$\cos x \le \dfrac{1}{2}$ より $\sin x \ge \sin 2x$

  よって，
  $$S = 2\left\{\int_0^{\frac{\pi}{3}} (\sin 2x - \sin x)\,dx + \int_{\frac{\pi}{3}}^{\pi} (\sin x - \sin 2x)\,dx\right\}$$
  それぞれの定積分を計算する：
  $$\int_0^{\frac{\pi}{3}} (\sin 2x - \sin x)\,dx = \left[-\frac{1}{2}\cos 2x + \cos x\right]_0^{\frac{\pi}{3}} = \left\{\left(-\frac{1}{2}\right)\!\left(-\frac{1}{2}\right) + \frac{1}{2}\right\} - \left(-\frac{1}{2} + 1\right) = \frac{3}{4} - \frac{1}{2} = \frac{1}{4}$$
  $$\int_{\frac{\pi}{3}}^{\pi} (\sin x - \sin 2x)\,dx = \left[-\cos x + \frac{1}{2}\cos 2x\right]_{\frac{\pi}{3}}^{\pi} = \left(1 + \frac{1}{2}\right) - \left(-\frac{1}{2} - \frac{1}{4}\right) = \frac{3}{2} + \frac{3}{4} = \frac{9}{4}$$
  したがって，
  $$S = 2\left(\frac{1}{4} + \frac{9}{4}\right) = 2 \cdot \frac{10}{4} = 5$$
  > 💡 讲师批注：注意 $\int \sin 2x\,dx = -\dfrac{1}{2}\cos 2x$，别漏掉系数 $\dfrac{1}{2}$ 与负号。最终结果是一个非常干净的整数 $5$！
- **【最终答案】**
  **$S = 5$**

---

#### 演習問題 17-(6)
- **【原题重现与翻译】**
  - 原题：連立不等式 $y \ge x^2,\; y \ge 2 - x,\; y \le x + 6$ の表す領域を図示せよ。またその領域の面積 $S$ を求めよ。
  - 中文：画出不等式组 $y \ge x^2,\; y \ge 2 - x,\; y \le x + 6$ 所表示的区域，并求该区域的面积 $S$。
- **【考点定位】**
  - 不等式组表示的平面区域（図形と方程式）、三线共点识别、分段定积分与 $\frac{1}{6}$ 面积公式做差速算。
- **【图解辅助（SVG 矢量图）】**
<svg viewBox="0 0 360 250" width="360" height="250" xmlns="http://www.w3.org/2000/svg" style="background:#fff;border:1px solid #e2e8f0;border-radius:6px;">
  <!-- 映射: x=0->155 (45px/u), y=0->220 (20px/u) -->
  <!-- 关键点: A(-2,4)->(65,140); B(1,1)->(200,200); C(3,9)->(290,40); (1,7)->(200,80) -->
  <line x1="25" y1="220" x2="340" y2="220" stroke="#1e293b" stroke-width="1.5"/>
  <polygon points="340,220 332,216 332,224" fill="#1e293b"/>
  <line x1="155" y1="240" x2="155" y2="15" stroke="#1e293b" stroke-width="1.5"/>
  <polygon points="155,15 151,23 159,23" fill="#1e293b"/>
  <text x="344" y="224" font-size="13" font-style="italic" fill="#1e293b">x</text>
  <text x="143" y="20" font-size="13" font-style="italic" fill="#1e293b">y</text>
  <text x="142" y="234" font-size="12" fill="#1e293b">O</text>
  <!-- 阴影区域: A(65,140) -> C(290,40) -> 沿抛物线到 B(200,200) -> 沿直线到 A(65,140) -->
  <path d="M 65 140 L 290 40 Q 245 160 200 200 L 65 140 Z" fill="#bfdbfe" fill-opacity="0.8"/>
  <!-- 抛物线 y = x^2 (蓝), x from -2.6 to 3.2 -->
  <path d="M 38 84.8 Q 155 355.2 299 15.2" fill="none" stroke="#2563eb" stroke-width="2.2"/>
  <!-- 直线 y = x + 6 (绿) -->
  <line x1="35" y1="153.3" x2="315" y2="28.9" stroke="#16a34a" stroke-width="2"/>
  <!-- 直线 y = 2 - x (橙) -->
  <line x1="40" y1="128.9" x2="265" y2="228.9" stroke="#ea580c" stroke-width="2"/>
  <!-- 辅助虚线 x = 1 -->
  <line x1="200" y1="80" x2="200" y2="220" stroke="#64748b" stroke-width="1" stroke-dasharray="3,2"/>
  <line x1="65" y1="140" x2="65" y2="220" stroke="#64748b" stroke-width="1" stroke-dasharray="3,2"/>
  <line x1="290" y1="40" x2="290" y2="220" stroke="#64748b" stroke-width="1" stroke-dasharray="3,2"/>
  <!-- 交点 -->
  <circle cx="65" cy="140" r="3.5" fill="#dc2626"/>
  <circle cx="200" cy="200" r="3.5" fill="#dc2626"/>
  <circle cx="290" cy="40" r="3.5" fill="#dc2626"/>
  <!-- 文字标注 -->
  <text x="58" y="234" font-size="11" fill="#1e293b">-2</text>
  <text x="197" y="234" font-size="11" fill="#1e293b">1</text>
  <text x="287" y="234" font-size="11" fill="#1e293b">3</text>
  <text x="16" y="138" font-size="11" fill="#dc2626" font-weight="bold">(-2, 4)</text>
  <text x="206" y="210" font-size="11" fill="#dc2626" font-weight="bold">(1, 1)</text>
  <text x="295" y="45" font-size="11" fill="#dc2626" font-weight="bold">(3, 9)</text>
  <text x="242" y="185" font-size="12" fill="#2563eb" font-weight="bold">y = x²</text>
  <text x="100" y="90" font-size="12" fill="#16a34a" font-weight="bold">y = x + 6</text>
  <text x="68" y="185" font-size="12" fill="#ea580c" font-weight="bold">y = 2 - x</text>
  <text x="180" y="142" font-size="15" font-style="italic" fill="#1e3a8a" font-weight="bold">S</text>
</svg>
- **【分步标准解答】**
  各境界線の交点を求める。
  1. $y = x^2$ と $y = 2 - x$ の交点：
     $$x^2 = 2 - x \iff x^2 + x - 2 = 0 \iff (x + 2)(x - 1) = 0 \implies x = -2,\; 1$$
     よって交点は $(-2, 4),\; (1, 1)$。
  2. $y = x^2$ と $y = x + 6$ の交点：
     $$x^2 = x + 6 \iff x^2 - x - 6 = 0 \iff (x + 2)(x - 3) = 0 \implies x = -2,\; 3$$
     よって交点は $(-2, 4),\; (3, 9)$。
  3. $y = 2 - x$ と $y = x + 6$ の交点：
     $$2 - x = x + 6 \implies x = -2,\; y = 4$$
     すなわち，3つの境界線はすべて点 $(-2, 4)$ を通る。

  以上より，連立不等式 $y \ge x^2,\; y \ge 2 - x,\; y \le x + 6$ の表す領域は上図の斜線部分（境界線を含む）である。
  > 💡 讲师批注：画图题（図示せよ）在日本考场中务必写明 **「境界線を含む（包含边界线）」**（不等号带等号 $\ge, \le$），并标出所有顶点坐标。

  **【解法 1：分段定积分（标准解法）】**
  区間 $-2 \le x \le 1$ では下側の境界が $y = 2 - x$，区間 $1 \le x \le 3$ では下側の境界が $y = x^2$ であるから，
  $$S = \int_{-2}^{1} \{(x + 6) - (2 - x)\}\,dx + \int_{1}^{3} \{(x + 6) - x^2\}\,dx$$
  $$= \int_{-2}^{1} (2x + 4)\,dx + \int_{1}^{3} (-x^2 + x + 6)\,dx$$
  $$= \left[x^2 + 4x\right]_{-2}^{1} + \left[-\frac{1}{3}x^3 + \frac{1}{2}x^2 + 6x\right]_{1}^{3}$$
  $$= \{(1 + 4) - (4 - 8)\} + \left\{\left(-9 + \frac{9}{2} + 18\right) - \left(-\frac{1}{3} + \frac{1}{2} + 6\right)\right\}$$
  $$= 9 + \left(\frac{27}{2} - \frac{37}{6}\right) = 9 + \frac{44}{6} = 9 + \frac{22}{3} = \frac{49}{3}$$

  **【解法 2：$\frac{1}{6}$ 公式做差（考场秒杀法）】**
  領域の面積 $S$ は，「放物線 $y = x^2$ と直線 $y = x + 6$ で囲まれた部分（$-2 \le x \le 3$）」から「放物線 $y = x^2$ と直線 $y = 2 - x$ で囲まれた部分（$-2 \le x \le 1$）」を引いたものに等しい。したがって $\frac{1}{6}$ 公式より直ちに，
  $$S = \frac{1}{6}\{3 - (-2)\}^3 - \frac{1}{6}\{1 - (-2)\}^3 = \frac{125}{6} - \frac{27}{6} = \frac{98}{6} = \frac{49}{3}$$
  > 💡 讲师批注：对比解法 1 与解法 2，用 $\frac{1}{6}$ 公式整体做差只需一步口算，完全避免分数通分失误！这也是 EJU 填空题最推荐的实战与验算策略。
- **【最终答案】**
  - **区域图**：见上方 SVG 矢量图（**含边界线**，顶点为 $(-2, 4),\; (1, 1),\; (3, 9)$）。
  - **面积**：**$S = \dfrac{49}{3}$**

---

#### 演習問題 17-(7)
- **【原题重现与翻译】**
  - 原题：放物線 $C: y = x^2 - 4x + 3$ 上の点 $P(0, 3),\; Q(6, 15)$ における接線を、それぞれ $l,\; m$ とする。この2つの接線と放物線で囲まれた図形の面積 $S$ を求めよ。
  - 中文：设抛物线 $C: y = x^2 - 4x + 3$ 上点 $P(0, 3)$ 与 $Q(6, 15)$ 处的切线分别为 $l, m$，求这两条切线与抛物线围成的图形面积 $S$。
- **【考点定位】**
  - 抛物线与两条切线围成的面积（補足 1 ②：两切线交点在中点 $x = \dfrac{\alpha + \beta}{2}$ 处，且满足 $\frac{1}{12}$ 面积公式）。
- **【图解辅助（SVG 矢量图）】**
<svg viewBox="0 0 360 250" width="360" height="250" xmlns="http://www.w3.org/2000/svg" style="background:#fff;border:1px solid #e2e8f0;border-radius:6px;">
  <!-- 映射: x=0->80 (35px/u), y=0->155 (7.5px/u) -->
  <!-- 关键点: P(0,3)->(80,132.5); 顶点(2,-1)->(150,162.5); Q(6,15)->(290,42.5); R(3,-9)->(185,222.5) -->
  <line x1="25" y1="155" x2="342" y2="155" stroke="#1e293b" stroke-width="1.5"/>
  <polygon points="342,155 334,151 334,159" fill="#1e293b"/>
  <line x1="80" y1="240" x2="80" y2="15" stroke="#1e293b" stroke-width="1.5"/>
  <polygon points="80,15 76,23 84,23" fill="#1e293b"/>
  <text x="346" y="159" font-size="13" font-style="italic" fill="#1e293b">x</text>
  <text x="68" y="20" font-size="13" font-style="italic" fill="#1e293b">y</text>
  <text x="67" y="168" font-size="12" fill="#1e293b">O</text>
  <!-- 阴影区域: P(80,132.5) 沿抛物线到 Q(290,42.5) -> R(185,222.5) -> P -->
  <path d="M 80 132.5 Q 185 222.5 290 42.5 L 185 222.5 Z" fill="#bfdbfe" fill-opacity="0.8"/>
  <!-- 抛物线 C: y = x^2 - 4x + 3 (精确二次贝塞尔: P=(80,132.5), Q=(290,42.5), 控制点恰为切线交点 R=(185,222.5)!) -->
  <path d="M 45 95 Q 150 230 307.5 16.25" fill="none" stroke="#2563eb" stroke-width="2.2"/>
  <!-- 切线 l: y = -4x + 3 (绿) -->
  <line x1="55" y1="111.1" x2="205" y2="239.6" stroke="#16a34a" stroke-width="1.8"/>
  <!-- 切线 m: y = 8x - 33 (橙) -->
  <line x1="175" y1="239.6" x2="305" y2="16.8" stroke="#ea580c" stroke-width="1.8"/>
  <!-- 中点竖线 x = 3 -->
  <line x1="185" y1="155" x2="185" y2="222.5" stroke="#64748b" stroke-width="1.2" stroke-dasharray="3,2"/>
  <!-- 点标注 -->
  <circle cx="80" cy="132.5" r="3.5" fill="#dc2626"/>
  <circle cx="290" cy="42.5" r="3.5" fill="#dc2626"/>
  <circle cx="185" cy="222.5" r="3.5" fill="#dc2626"/>
  <text x="26" y="136" font-size="11" fill="#dc2626" font-weight="bold">P(0, 3)</text>
  <text x="296" y="47" font-size="11" fill="#dc2626" font-weight="bold">Q(6, 15)</text>
  <text x="193" y="232" font-size="11" fill="#dc2626" font-weight="bold">R(3, -9)</text>
  <text x="181" y="148" font-size="11" fill="#64748b">3</text>
  <text x="108" y="195" font-size="12" fill="#16a34a" font-weight="bold">l</text>
  <text x="260" y="128" font-size="12" fill="#ea580c" font-weight="bold">m</text>
  <text x="232" y="55" font-size="12" fill="#2563eb" font-weight="bold">C</text>
  <text x="179" y="185" font-size="14" font-style="italic" fill="#1e3a8a" font-weight="bold">S</text>
</svg>
- **【分步标准解答】**
  $y = x^2 - 4x + 3$ を微分すると，$y' = 2x - 4$。
  - 点 $P(0, 3)$ における接線 $l$ の傾きは $y'(0) = -4$ であるから，$l$ の方程式は，
    $$y = -4x + 3$$
  - 点 $Q(6, 15)$ における接線 $m$ の傾きは $y'(6) = 2 \cdot 6 - 4 = 8$ であるから，$m$ の方程式は，
    $$y - 15 = 8(x - 6) \implies y = 8x - 33$$

  2つの接線 $l, m$ の交点 $R$ の $x$ 座標を求める。
  $$-4x + 3 = 8x - 33 \iff 12x = 36 \implies x = 3$$
  このとき $y = -4 \cdot 3 + 3 = -9$ より，$R(3, -9)$ である。
  > 💡 讲师批注：交点横坐标 $x = 3$ 恰好是两切点横坐标 $0$ 与 $6$ 的中点 $\dfrac{0+6}{2} = 3$，可立即用来检验两条切线方程是否求错！

  区間 $0 \le x \le 3$ では $l$ が下側，区間 $3 \le x \le 6$ では $m$ が下側にあるから，求める面積 $S$ は，
  $$S = \int_0^3 \{(x^2 - 4x + 3) - (-4x + 3)\}\,dx + \int_3^6 \{(x^2 - 4x + 3) - (8x - 33)\}\,dx$$
  $$= \int_0^3 x^2\,dx + \int_3^6 (x^2 - 12x + 36)\,dx = \int_0^3 x^2\,dx + \int_3^6 (x - 6)^2\,dx$$
  $$= \left[\frac{1}{3}x^3\right]_0^3 + \left[\frac{1}{3}(x - 6)^3\right]_3^6 = (9 - 0) + \{0 - (-9)\} = 18$$
  > 💡 讲师批注：
  > 1. 抛物线减切线的被积式必然是完全平方式 $a(x - \alpha)^2$，利用 $\int (x - 6)^2\,dx = \dfrac{1}{3}(x - 6)^3$ 可避免展开成三项分别代上下限的繁琐计算！
  > 2. 用補足 1 ②的 **$\frac{1}{12}$ 公式** 验算：$S = \dfrac{|a|}{12}(\beta - \alpha)^3 = \dfrac{1}{12}(6 - 0)^3 = \dfrac{216}{12} = 18$，秒杀且完全一致！
- **【最终答案】**
  **$S = 18$**

---

#### 演習問題 17-(8)
- **【原题重现与翻译】**
  - 原题：2つの放物線 $C_1: y = x^2,\; C_2: y = x^2 - 8x + 8$ を考える。
    - `[1]` $C_1$ と $C_2$ の両方に接する直線 $l$ の方程式を求めよ。
    - `[2]` 2つの放物線 $C_1,\; C_2$ と直線 $l$ で囲まれた図形の面積 $S$ を求めよ。
  - 中文：考虑两条抛物线 $C_1: y = x^2$ 与 $C_2: y = x^2 - 8x + 8$。
    - `[1]` 求同时与 $C_1$ 和 $C_2$ 相切的直线 $l$ 的方程。
    - `[2]` 求两条抛物线 $C_1, C_2$ 与直线 $l$ 围成的图形面积 $S$。
- **【考点定位】**
  - 两抛物线的公切线（共通接線）求法、同开口抛物线与公切线围成面积（補足 1 ③与 $\frac{1}{12}$ 公式）。
- **【图解辅助（SVG 矢量图）】**
<svg viewBox="0 0 360 250" width="360" height="250" xmlns="http://www.w3.org/2000/svg" style="background:#fff;border:1px solid #e2e8f0;border-radius:6px;">
  <!-- 映射: x=0->110 (35px/u), y=0->130 (11px/u) -->
  <!-- 关键点: C1切点(-1,1)->(75,119); 交点(1,1)->(145,119); C2切点(3,-7)->(215,207); C2顶点(4,-8)->(250,218) -->
  <line x1="20" y1="130" x2="342" y2="130" stroke="#1e293b" stroke-width="1.5"/>
  <polygon points="342,130 334,126 334,134" fill="#1e293b"/>
  <line x1="110" y1="240" x2="110" y2="15" stroke="#1e293b" stroke-width="1.5"/>
  <polygon points="110,15 106,23 114,23" fill="#1e293b"/>
  <text x="346" y="134" font-size="13" font-style="italic" fill="#1e293b">x</text>
  <text x="98" y="20" font-size="13" font-style="italic" fill="#1e293b">y</text>
  <text x="97" y="144" font-size="12" fill="#1e293b">O</text>
  <!-- 阴影区域: (-1,1)沿C1到(1,1) -> 沿C2到(3,-7) -> 沿l回(-1,1) -->
  <path d="M 75 119 Q 110 141 145 119 Q 180 185 215 207 L 75 119 Z" fill="#bfdbfe" fill-opacity="0.8"/>
  <!-- 抛物线 C1: y = x^2 (蓝), x in [-2.8, 2.8] -->
  <path d="M 12 43.8 Q 110 216.2 208 43.8" fill="none" stroke="#2563eb" stroke-width="2.2"/>
  <!-- 抛物线 C2: y = (x-4)^2 - 8 (紫), x in [0.5, 7.2] -->
  <path d="M 127.5 83.25 Q 250 352.75 362 105.4" fill="none" stroke="#9333ea" stroke-width="2.2"/>
  <!-- 公切线 l: y = -2x - 1 (橙) -->
  <line x1="35" y1="93.9" x2="260" y2="235.3" stroke="#ea580c" stroke-width="2"/>
  <!-- 辅助虚线 x = 1 -->
  <line x1="145" y1="119" x2="145" y2="163" stroke="#64748b" stroke-width="1.2" stroke-dasharray="3,2"/>
  <!-- 关键点 -->
  <circle cx="75" cy="119" r="3.5" fill="#dc2626"/>
  <circle cx="145" cy="119" r="3.5" fill="#dc2626"/>
  <circle cx="215" cy="207" r="3.5" fill="#dc2626"/>
  <text x="26" y="116" font-size="11" fill="#dc2626" font-weight="bold">(-1, 1)</text>
  <text x="148" y="114" font-size="11" fill="#dc2626" font-weight="bold">(1, 1)</text>
  <text x="220" y="218" font-size="11" fill="#dc2626" font-weight="bold">(3, -7)</text>
  <text x="180" y="42" font-size="12" fill="#2563eb" font-weight="bold">C₁</text>
  <text x="315" y="95" font-size="12" fill="#9333ea" font-weight="bold">C₂</text>
  <text x="255" y="244" font-size="12" fill="#ea580c" font-weight="bold">l: y = -2x - 1</text>
  <text x="150" y="156" font-size="14" font-style="italic" fill="#1e3a8a" font-weight="bold">S</text>
</svg>
- **【分步标准解答】**
  **`[1]` 共通接線 $l$ の方程式**
  $C_1: y = x^2$ 上の点 $(s, s^2)$ における接線 $l$ の方程式は，$y' = 2x$ より，
  $$y - s^2 = 2s(x - s) \iff y = 2sx - s^2 \quad \cdots \text{①}$$
  この直線 $l$ が $C_2: y = x^2 - 8x + 8$ にも接するとき，2つの式から $y$ を消去した2次方程式
  $$x^2 - 8x + 8 = 2sx - s^2 \iff x^2 - 2(s + 4)x + (s^2 + 8) = 0 \quad \cdots \text{②}$$
  が重解をもつ。したがって，判別式を $D$ とすると，
  $$\frac{D}{4} = (s + 4)^2 - (s^2 + 8) = 0$$
  $$s^2 + 8s + 16 - s^2 - 8 = 0 \iff 8s + 8 = 0 \implies s = -1$$
  これを ① に代入して，求める共通接線 $l$ の方程式は，
  $$y = -2x - 1$$
  また，このとき $l$ と $C_1$ の接点の $x$ 座標は $s = -1$，$l$ と $C_2$ の接点の $x$ 座標は ② の重解より $x = s + 4 = 3$ である。
  > 💡 讲师批注：求两抛物线公切线的标准套路是「设其中一条的切线（单参数 $s$）→ 与另一条联立令判别式 $D = 0$」，比设两个切点联立系数更省事！

  **`[2]` 囲まれた図形の面積 $S$**
  $C_1$ と $C_2$ の交点の $x$ 座標を求める。
  $$x^2 = x^2 - 8x + 8 \implies 8x = 8 \implies x = 1$$
  （これは2つの接点の $x$ 座標 $-1$ と $3$ の中点 $\dfrac{-1 + 3}{2} = 1$ に一致する。）
  区間 $-1 \le x \le 1$ では $C_1$ が上側，区間 $1 \le x \le 3$ では $C_2$ が上側にあるから，
  $$S = \int_{-1}^{1} \{x^2 - (-2x - 1)\}\,dx + \int_{1}^{3} \{(x^2 - 8x + 8) - (-2x - 1)\}\,dx$$
  $$= \int_{-1}^{1} (x + 1)^2\,dx + \int_{1}^{3} (x - 3)^2\,dx$$
  $$= \left[\frac{1}{3}(x + 1)^3\right]_{-1}^{1} + \left[\frac{1}{3}(x - 3)^3\right]_{1}^{3}$$
  $$= \left(\frac{8}{3} - 0\right) + \left\{0 - \left(-\frac{8}{3}\right)\right\} = \frac{16}{3}$$
  > 💡 讲师批注：用補足 1 ③的 **$\frac{1}{12}$ 公式** 验算：$S = \dfrac{|a|}{12}(\beta - \alpha)^3 = \dfrac{1}{12}\{3 - (-1)\}^3 = \dfrac{64}{12} = \dfrac{16}{3}$，完全一致！
- **【最终答案】**
  - **`[1]` $y = -2x - 1$**
  - **`[2]` $S = \dfrac{16}{3}$**

---

#### 演習問題 17-(9)
- **【原题重现与翻译】**
  - 原题：曲線 $y = x^3 - 5x^2 + 2x + 6$ とその曲線上の点 $(3, -6)$ における接線で囲まれた図形の面積 $S$ を求めよ。
  - 中文：求曲线 $y = x^3 - 5x^2 + 2x + 6$ 与其上点 $(3, -6)$ 处的切线围成的图形面积 $S$。
- **【考点定位】**
  - 三次函数与切线围成的面积（補足 1 ④：重根因式分解与三次函数 $\frac{1}{12}$ 面积公式 $\dfrac{|a|}{12}(\beta - \alpha)^4$）。
- **【图解辅助（SVG 矢量图）】**
<svg viewBox="0 0 360 230" width="360" height="230" xmlns="http://www.w3.org/2000/svg" style="background:#fff;border:1px solid #e2e8f0;border-radius:6px;">
  <!-- 映射: x=0->110 (50px/u), y=0->125 (10px/u) -->
  <!-- 关键点: (-1,-2)->(60,145); (0,6)->(110,65); (0.21,6.21)->(120.5,62.9); (3,-6)->(260,185); (3.12,-6.05)->(266,185.5); (4, -2)->(310,145) -->
  <line x1="20" y1="125" x2="342" y2="125" stroke="#1e293b" stroke-width="1.5"/>
  <polygon points="342,125 334,121 334,129" fill="#1e293b"/>
  <line x1="110" y1="215" x2="110" y2="15" stroke="#1e293b" stroke-width="1.5"/>
  <polygon points="110,15 106,23 114,23" fill="#1e293b"/>
  <text x="346" y="129" font-size="13" font-style="italic" fill="#1e293b">x</text>
  <text x="98" y="20" font-size="13" font-style="italic" fill="#1e293b">y</text>
  <text x="97" y="139" font-size="12" fill="#1e293b">O</text>
  <!-- 阴影区域: (-1,-2)沿曲线经(0.2,6.2)到(3,-6), 再沿切线回(-1,-2) -->
  <path d="M 60 145 C 95 45, 130 40, 175 105 C 210 155, 235 182, 260 185 L 60 145 Z" fill="#bfdbfe" fill-opacity="0.8"/>
  <!-- 三次曲线 (蓝) -->
  <path d="M 45 205 C 80 50, 125 35, 175 105 C 220 170, 265 205, 290 175 C 308 153, 320 110, 330 55" fill="none" stroke="#2563eb" stroke-width="2.2"/>
  <!-- 切线 y = -x - 3 (橙) -->
  <line x1="35" y1="140" x2="315" y2="196" stroke="#ea580c" stroke-width="2"/>
  <!-- 辅助虚线 -->
  <line x1="60" y1="125" x2="60" y2="145" stroke="#64748b" stroke-width="1" stroke-dasharray="3,2"/>
  <line x1="260" y1="125" x2="260" y2="185" stroke="#64748b" stroke-width="1" stroke-dasharray="3,2"/>
  <!-- 交点与切点 -->
  <circle cx="60" cy="145" r="3.5" fill="#dc2626"/>
  <circle cx="260" cy="185" r="3.5" fill="#dc2626"/>
  <text x="53" y="118" font-size="11" fill="#1e293b">-1</text>
  <text x="257" y="118" font-size="11" fill="#1e293b">3</text>
  <text x="12" y="160" font-size="11" fill="#dc2626" font-weight="bold">(-1, -2)</text>
  <text x="245" y="207" font-size="11" fill="#dc2626" font-weight="bold">(3, -6)</text>
  <text x="148" y="45" font-size="12" fill="#2563eb" font-weight="bold">y = x³ - 5x² + 2x + 6</text>
  <text x="120" y="176" font-size="12" fill="#ea580c" font-weight="bold">y = -x - 3</text>
  <text x="135" y="112" font-size="15" font-style="italic" fill="#1e3a8a" font-weight="bold">S</text>
</svg>
- **【分步标准解答】**
  $f(x) = x^3 - 5x^2 + 2x + 6$ とおくと，$f'(x) = 3x^2 - 10x + 2$。
  点 $(3, -6)$ における接線の傾きは，
  $$f'(3) = 3 \cdot 3^2 - 10 \cdot 3 + 2 = 27 - 30 + 2 = -1$$
  よって，接線の方程式は，
  $$y - (-6) = -1(x - 3) \implies y = -x - 3$$

  曲線と接線の共有点の $x$ 座標を求める。
  $$x^3 - 5x^2 + 2x + 6 = -x - 3 \iff x^3 - 5x^2 + 3x + 9 = 0$$
  $x = 3$ が重解であることに注意して因数分解すると，
  $$(x - 3)^2(x + 1) = 0 \implies x = -1,\; 3$$
  > 💡 讲师批注：求三次方程的另一根完全不需要猜根或做长除法！已知切点 $x=3$ 是二重根，直接写出 $(x-3)^2(x - \alpha) = (x^2 - 6x + 9)(x - \alpha)$，对比常数项 $9(-\alpha) = 9 \implies \alpha = -1$（或用韦达定理 $3 + 3 + \alpha = 5 \implies \alpha = -1$），1 秒出答案！

  区間 $-1 \le x \le 3$ において，$(x - 3)^2(x + 1) \ge 0$ であるから，曲線は接線の上側にある。したがって，求める面積 $S$ は，
  $$S = \int_{-1}^{3} \{(x^3 - 5x^2 + 2x + 6) - (-x - 3)\}\,dx = \int_{-1}^{3} (x - 3)^2(x + 1)\,dx$$
  ここで，$x + 1 = (x - 3) + 4$ と変形して積分すると，
  $$S = \int_{-1}^{3} (x - 3)^2\{(x - 3) + 4\}\,dx = \int_{-1}^{3} \{(x - 3)^3 + 4(x - 3)^2\}\,dx$$
  $$= \left[\frac{1}{4}(x - 3)^4 + \frac{4}{3}(x - 3)^3\right]_{-1}^{3} = 0 - \left\{\frac{1}{4}(-4)^4 + \frac{4}{3}(-4)^3\right\} = -\left(64 - \frac{256}{3}\right) = \frac{64}{3}$$
  > 💡 讲师批注：
  > 1. 将 $(x+1)$ 改写为 $(x-3)+4$ 是補足 1 ④展示的「以 $(x-3)$ 为整体的凑微分技巧」，代入上限 $3$ 时直接归零，计算量减少一半！
  > 2. 用三次函数 **$\frac{1}{12}$ 公式** 验算：$S = \dfrac{|a|}{12}(\beta - \alpha)^4 = \dfrac{1}{12}\{3 - (-1)\}^4 = \dfrac{256}{12} = \dfrac{64}{3}$，完全一致！
- **【最终答案】**
  **$S = \dfrac{64}{3}$**

---

#### 演習問題 17-(10)
- **【原题重现与翻译】**
  - 原题：曲線 $y = \log x$ が曲線 $y = ax^2$ と接するように正の定数 $a$ の値を定めよ。また、そのとき、これらの曲線と $x$ 軸で囲まれた図形の面積を求めよ。
  - 中文：确定正定数 $a$ 的值，使曲线 $y = \log x$ 与曲线 $y = ax^2$ 相切。并求此时这两条曲线与 $x$ 轴围成的图形的面积。
- **【考点定位】**
  - 两曲线相切的充要条件（切点处函数值与导数值同时相等）、对数函数的积分（$\int \log x\,dx = x\log x - x + C$）与区域面积分割（亦可转为对 $y$ 积分）。
- **【图解辅助（SVG 矢量图）】**
<svg viewBox="0 0 360 220" width="360" height="220" xmlns="http://www.w3.org/2000/svg" style="background:#fff;border:1px solid #e2e8f0;border-radius:6px;">
  <!-- 映射: x=0->50 (120px/u), y=0->155 (140px/u) -->
  <!-- 关键点: (0,0)->(50,155); (1,0)->(170,155); 切点(sqrt(e)=1.649, 0.5)->(247.8, 85) -->
  <line x1="20" y1="155" x2="342" y2="155" stroke="#1e293b" stroke-width="1.5"/>
  <polygon points="342,155 334,151 334,159" fill="#1e293b"/>
  <line x1="50" y1="210" x2="50" y2="15" stroke="#1e293b" stroke-width="1.5"/>
  <polygon points="50,15 46,23 54,23" fill="#1e293b"/>
  <text x="346" y="159" font-size="13" font-style="italic" fill="#1e293b">x</text>
  <text x="38" y="20" font-size="13" font-style="italic" fill="#1e293b">y</text>
  <text x="37" y="169" font-size="12" fill="#1e293b">O</text>
  <!-- 阴影区域: (0,0)沿抛物线到(sqrt(e),0.5) -> 沿log x到(1,0) -> 沿x轴回(0,0) -->
  <path d="M 50 155 Q 148.9 155 247.8 85 C 215 106, 188 130, 170 155 L 50 155 Z" fill="#bfdbfe" fill-opacity="0.85"/>
  <!-- 抛物线 y = x^2/(2e) (蓝), x in [0, 2.2] -->
  <path d="M 50 155 Q 182 155 314 30.3" fill="none" stroke="#2563eb" stroke-width="2.2"/>
  <!-- 对数曲线 y = log x (绿), x in [0.65, 2.3] -->
  <path d="M 128 215 C 145 182, 160 165, 170 155 C 195 128, 222 102, 247.8 85 C 275 68, 300 54, 326 38.4" fill="none" stroke="#16a34a" stroke-width="2.2"/>
  <!-- 辅助虚线 -->
  <line x1="247.8" y1="85" x2="247.8" y2="155" stroke="#64748b" stroke-width="1" stroke-dasharray="3,2"/>
  <line x1="50" y1="85" x2="247.8" y2="85" stroke="#64748b" stroke-width="1" stroke-dasharray="3,2"/>
  <!-- 关键点 -->
  <circle cx="170" cy="155" r="3" fill="#1e293b"/>
  <circle cx="247.8" cy="85" r="3.5" fill="#dc2626"/>
  <text x="167" y="170" font-size="11" fill="#1e293b">1</text>
  <text x="239" y="170" font-size="11" fill="#1e293b">√e</text>
  <text x="26" y="89" font-size="11" fill="#1e293b">1/2</text>
  <text x="192" y="74" font-size="11" fill="#dc2626" font-weight="bold">(√e, 1/2)</text>
  <text x="242" y="34" font-size="12" fill="#2563eb" font-weight="bold">y = x²/(2e)</text>
  <text x="278" y="80" font-size="12" fill="#16a34a" font-weight="bold">y = log x</text>
  <text x="160" y="138" font-size="14" font-style="italic" fill="#1e3a8a" font-weight="bold">S</text>
</svg>
- **【分步标准解答】**
  2つの曲線 $y = \log x$ と $y = ax^2$ の接点の $x$ 座標を $t\;(t > 0)$ とする。
  それぞれの導関数は，
  $$(\log x)' = \frac{1}{x},\qquad (ax^2)' = 2ax$$
  接点において $y$ 座標と接線の傾きがともに一致するから，
  $$\begin{cases} \log t = at^2 & \cdots \text{①} \\ \dfrac{1}{t} = 2at & \cdots \text{②} \end{cases}$$
  ② より $at^2 = \dfrac{1}{2}$ であるから，これを ① に代入して，
  $$\log t = \frac{1}{2} \implies t = e^{\frac{1}{2}} = \sqrt{e}$$
  再び $at^2 = \dfrac{1}{2}$ に代入すると，$a \cdot e = \dfrac{1}{2}$ より，
  $$a = \frac{1}{2e}$$
  これは $a > 0$ を満たす。また，接点の座標は $\left(\sqrt{e},\; \dfrac{1}{2}\right)$ である。
  > 💡 讲师批注：解方程组 ①② 时，不要急着把 $a = \dfrac{1}{2t^2}$ 硬代，直接观察到 ② 等价于 $at^2 = \dfrac{1}{2}$，整体代入 ① 瞬间得 $\log t = \dfrac{1}{2}$！

  次に，2つの曲線 $y = \dfrac{1}{2e}x^2,\; y = \log x$ と $x$ 軸で囲まれた図形の面積 $S$ を求める。
  曲線 $y = \log x$ と $x$ 軸の交点は $(1, 0)$ である。上図より，求める面積 $S$ は「区間 $0 \le x \le \sqrt{e}$ における $y = \dfrac{1}{2e}x^2$ と $x$ 軸の間の面積」から「区間 $1 \le x \le \sqrt{e}$ における $y = \log x$ と $x$ 軸の間の面積」を引いたものに等しい。
  $$S = \int_0^{\sqrt{e}} \frac{1}{2e}x^2\,dx - \int_1^{\sqrt{e}} \log x\,dx$$
  $$= \left[\frac{1}{6e}x^3\right]_0^{\sqrt{e}} - \left[x\log x - x\right]_1^{\sqrt{e}}$$
  $$= \frac{e\sqrt{e}}{6e} - \left\{\left(\sqrt{e}\cdot\frac{1}{2} - \sqrt{e}\right) - (1 \cdot 0 - 1)\right\}$$
  $$= \frac{\sqrt{e}}{6} - \left(1 - \frac{\sqrt{e}}{2}\right) = \frac{\sqrt{e}}{6} + \frac{3\sqrt{e}}{6} - 1 = \frac{2\sqrt{e}}{3} - 1$$
  > 💡 讲师批注：
  > - 公式 $\int \log x\,dx = x\log x - x + C$ 必须烂熟于心（由分部积分 $\int 1 \cdot \log x\,dx = x\log x - \int x \cdot \frac{1}{x}\,dx$ 得到）。
  > - **对 $y$ 积分验算**：区间 $0 \le y \le \frac{1}{2}$，右边界 $x = e^y$，左边界 $x = \sqrt{2ey}$，于是
  >   $$S = \int_0^{\frac{1}{2}} \left(e^y - \sqrt{2e}\,y^{\frac{1}{2}}\right)dy = \left[e^y - \frac{2\sqrt{2e}}{3}y^{\frac{3}{2}}\right]_0^{\frac{1}{2}} = \left(\sqrt{e} - \frac{\sqrt{e}}{3}\right) - 1 = \frac{2\sqrt{e}}{3} - 1$$
  >   完全一致！
- **【最终答案】**
  **$a = \dfrac{1}{2e}$，面積 $S = \dfrac{2\sqrt{e}}{3} - 1$**

---

#### 演習問題 17-(11)
- **【原题重现与翻译】**
  - 原题：放物線 $L: y = x^2$ と点 $R\left(0, \dfrac{5}{4}\right)$ を中心とする円 $C$ が異なる2点で接するとき
    - `[1]` 2つの接点の座標を求めよ。
    - `[2]` 2つ接点を両端とする円 $C$ の短い方の弧と $L$ とで囲まれた図形の面積 $S$ を求めよ。
  - 中文：当抛物线 $L: y = x^2$ 与以点 $R\left(0, \dfrac{5}{4}\right)$ 为圆心的圆 $C$ 在不同的 2 点相切时，
    - `[1]` 求这两个切点的坐标。
    - `[2]` 求以这两个切点为端点的圆 $C$ 的劣弧（较短的弧）与抛物线 $L$ 围成的图形面积 $S$。
- **【考点定位】**
  - 抛物线与圆相切（二次方程重根法 / 法线过圆心法）、**補足 2 核心策略**（用「抛物线与弦的 $\frac{1}{6}$ 公式」减去「扇形与三角形之差（弓形）」，彻底避开根式积分 $\int \sqrt{1-x^2}\,dx$！）。
- **【图解辅助（SVG 矢量图）】**
<svg viewBox="0 0 360 270" width="360" height="270" xmlns="http://www.w3.org/2000/svg" style="background:#fff;border:1px solid #e2e8f0;border-radius:6px;">
  <!-- 映射: x=0->180 (90px/u), y=0->230 (90px/u) -->
  <!-- 关键点: R(0, 1.25)->(180, 117.5), r=90px -->
  <!-- A(-sqrt(3)/2, 0.75)->(102.06, 162.5); B(sqrt(3)/2, 0.75)->(257.94, 162.5); H(0,0.75)->(180,162.5) -->
  <!-- 底部圆弧最低点 (0, 0.25)->(180, 207.5) -->
  <line x1="25" y1="230" x2="340" y2="230" stroke="#1e293b" stroke-width="1.5"/>
  <polygon points="340,230 332,226 332,234" fill="#1e293b"/>
  <line x1="180" y1="260" x2="180" y2="12" stroke="#1e293b" stroke-width="1.5"/>
  <polygon points="180,12 176,20 184,20" fill="#1e293b"/>
  <text x="344" y="234" font-size="13" font-style="italic" fill="#1e293b">x</text>
  <text x="168" y="18" font-size="13" font-style="italic" fill="#1e293b">y</text>
  <text x="166" y="244" font-size="12" fill="#1e293b">O</text>
  <!-- 扇形 RAB 浅橙色辅助示意 -->
  <path d="M 180 117.5 L 102.06 162.5 A 90 90 0 0 0 257.94 162.5 Z" fill="#fef3c7" fill-opacity="0.7"/>
  <!-- 所求月牙区域 S: A沿抛物线到B, 再沿圆劣弧回A -->
  <path d="M 102.06 162.5 Q 180 297.5 257.94 162.5 A 90 90 0 0 1 102.06 162.5 Z" fill="#93c5fd" fill-opacity="0.85"/>
  <!-- 圆 C (橙) -->
  <circle cx="180" cy="117.5" r="90" fill="none" stroke="#ea580c" stroke-width="2"/>
  <!-- 抛物线 L: y = x^2 (蓝), x in [-1.5, 1.5] -> y=2.25 -> py=27.5 -->
  <path d="M 45 27.5 Q 180 432.5 315 27.5" fill="none" stroke="#2563eb" stroke-width="2.2"/>
  <!-- 弦 AB 与半径 RA, RB -->
  <line x1="102.06" y1="162.5" x2="257.94" y2="162.5" stroke="#16a34a" stroke-width="1.5" stroke-dasharray="4,2"/>
  <line x1="180" y1="117.5" x2="102.06" y2="162.5" stroke="#64748b" stroke-width="1.2" stroke-dasharray="3,2"/>
  <line x1="180" y1="117.5" x2="257.94" y2="162.5" stroke="#64748b" stroke-width="1.2" stroke-dasharray="3,2"/>
  <!-- 关键点 -->
  <circle cx="180" cy="117.5" r="3.5" fill="#ea580c"/>
  <circle cx="102.06" cy="162.5" r="3.5" fill="#dc2626"/>
  <circle cx="257.94" cy="162.5" r="3.5" fill="#dc2626"/>
  <text x="186" y="114" font-size="11" fill="#ea580c" font-weight="bold">R(0, 5/4)</text>
  <text x="16" y="166" font-size="11" fill="#dc2626" font-weight="bold">A(-√3/2, 3/4)</text>
  <text x="263" y="166" font-size="11" fill="#dc2626" font-weight="bold">B(√3/2, 3/4)</text>
  <text x="164" y="142" font-size="11" fill="#92400e">2π/3</text>
  <text x="275" y="65" font-size="12" fill="#2563eb" font-weight="bold">L: y = x²</text>
  <text x="248" y="45" font-size="12" fill="#ea580c" font-weight="bold">C (r = 1)</text>
  <text x="185" y="222" font-size="13" font-style="italic" fill="#1e3a8a" font-weight="bold">S</text>
</svg>
- **【分步标准解答】**
  **`[1]` 2つの接点の座標**
  円 $C$ の半径を $r\;(r > 0)$ とすると，円 $C$ の方程式は，
  $$x^2 + \left(y - \frac{5}{4}\right)^2 = r^2$$
  これと放物線 $L: y = x^2$ から $x^2$ を消去すると，
  $$y + \left(y - \frac{5}{4}\right)^2 = r^2 \iff y^2 - \frac{3}{2}y + \frac{25}{16} - r^2 = 0 \quad \cdots \text{①}$$
  放物線 $L$ と円 $C$ はともに $y$ 軸に関して対称であるから，異なる2点で接するとき，2つの接点の $y$ 座標は等しく，かつ正（$y > 0$）でなければならない。すなわち，$y$ の2次方程式 ① が正の重解をもつ。
  判別式を $D$ とすると，
  $$D = \left(-\frac{3}{2}\right)^2 - 4\left(\frac{25}{16} - r^2\right) = 0$$
  $$\frac{9}{4} - \frac{25}{4} + 4r^2 = 0 \iff 4r^2 = 4 \implies r = 1 \quad (r > 0)$$
  このとき，① の重解は $y = \dfrac{3}{4} > 0$ であり，$x^2 = \dfrac{3}{4}$ より $x = \pm\dfrac{\sqrt{3}}{2}$。
  したがって，2つの接点の座標は，
  $$\left(-\frac{\sqrt{3}}{2},\; \frac{3}{4}\right),\qquad \left(\frac{\sqrt{3}}{2},\; \frac{3}{4}\right)$$
  > 💡 讲师批注：**法线法秒杀 `[1]`**：设切点 $(t, t^2)\;(t \ne 0)$，此处抛物线切线斜率为 $2t$，故法线斜率为 $-\dfrac{1}{2t}$。因圆与抛物线相切，法线必过圆心 $R\left(0, \frac{5}{4}\right)$，于是
  > $$\frac{t^2 - \frac{5}{4}}{t - 0} = -\frac{1}{2t} \implies t^2 - \frac{5}{4} = -\frac{1}{2} \implies t^2 = \frac{3}{4} \implies t = \pm\frac{\sqrt{3}}{2}$$
  > 无需引入半径 $r$ 就能瞬间求出切点坐标！

  **`[2]` 囲まれた図形の面積 $S$**
  2つの接点を $A\left(-\dfrac{\sqrt{3}}{2}, \dfrac{3}{4}\right),\; B\left(\dfrac{\sqrt{3}}{2}, \dfrac{3}{4}\right)$ とし，弦 $AB$ の中点を $H\left(0, \dfrac{3}{4}\right)$ とする。
  円 $C$ の半径は $r = 1$ であり，$RH = \dfrac{5}{4} - \dfrac{3}{4} = \dfrac{1}{2},\; HB = \dfrac{\sqrt{3}}{2}$ であるから，直角三角形 $RHB$ において，
  $$\sin\angle HRB = \frac{HB}{RB} = \frac{\sqrt{3}}{2} \implies \angle HRB = \frac{\pi}{3}$$
  よって，中心角は $\angle ARB = \dfrac{2\pi}{3}$ である。

  求める面積 $S$ は，「放物線 $L$ と弦 $AB\;(y = \frac{3}{4})$ で囲まれた部分の面積 $S_1$」から「弦 $AB$ と円 $C$ の短い方の弧で囲まれた弓形の面積 $S_2$」を引いたものに等しい。
  1. $S_1$ は $\frac{1}{6}$ 公式より，
     $$S_1 = \int_{-\frac{\sqrt{3}}{2}}^{\frac{\sqrt{3}}{2}} \left(\frac{3}{4} - x^2\right)dx = \frac{1}{6}\left\{\frac{\sqrt{3}}{2} - \left(-\frac{\sqrt{3}}{2}\right)\right\}^3 = \frac{1}{6}(\sqrt{3})^3 = \frac{\sqrt{3}}{2}$$
  2. $S_2$ は（扇形 $RAB$ の面積）$-$（$\triangle RAB$ の面積）より，
     $$S_2 = \frac{1}{2} \cdot 1^2 \cdot \frac{2\pi}{3} - \frac{1}{2} \cdot \sqrt{3} \cdot \frac{1}{2} = \frac{\pi}{3} - \frac{\sqrt{3}}{4}$$
  したがって，
  $$S = S_1 - S_2 = \frac{\sqrt{3}}{2} - \left(\frac{\pi}{3} - \frac{\sqrt{3}}{4}\right) = \frac{3\sqrt{3}}{4} - \frac{\pi}{3}$$
  > 💡 讲师批注：这道题是教材 **補足 2（用初等几何避开积分）** 的典范！若硬算 $2\int_0^{\frac{\sqrt{3}}{2}} \left(\frac{5}{4} - \sqrt{1-x^2} - x^2\right)dx$ 需要三角换元 $x = \sin\theta$，耗时至少 3 倍；而用「$\frac{1}{6}$ 公式 $-$ 弓形面积」，全程几乎零积分！
- **【最终答案】**
  - **`[1]` $\left(-\dfrac{\sqrt{3}}{2},\; \dfrac{3}{4}\right),\quad \left(\dfrac{\sqrt{3}}{2},\; \dfrac{3}{4}\right)$**
  - **`[2]` $S = \dfrac{3\sqrt{3}}{4} - \dfrac{\pi}{3}$**

---

#### 演習問題 17-(12)
- **【原题重现与翻译】**
  - 原题：2つの楕円 $x^2 + 3y^2 = 4 \cdots \text{①},\quad 3x^2 + y^2 = 4 \cdots \text{②}$ がある。
    - `[1]` 2つ楕円の4つの交点の座標を求めよ。
    - `[2]` 2つ楕円の内部の重なった部分の面積を求めよ。
  - 中文：已知两个椭圆 $x^2 + 3y^2 = 4 \cdots \text{①}$ 与 $3x^2 + y^2 = 4 \cdots \text{②}$。
    - `[1]` 求两个椭圆的 4 个交点的坐标。
    - `[2]` 求两个椭圆内部重叠部分的面积。
- **【考点定位】**
  - 二次曲线交点、多重对称性（关于 $x$ 轴、$y$ 轴、$y = \pm x$ 的 **8 重对称性**）、圆弧型根式定积分 $\int_0^1 \sqrt{4 - x^2}\,dx$（三角换元或几何扇形法）。
- **【图解辅助（SVG 矢量图）】**
<svg viewBox="0 0 360 300" width="360" height="300" xmlns="http://www.w3.org/2000/svg" style="background:#fff;border:1px solid #e2e8f0;border-radius:6px;">
  <!-- 映射: x=0->180 (60px/u), y=0->150 (60px/u) -->
  <!-- 椭圆1: rx=2*60=120, ry=(2/sqrt(3))*60=69.28 -->
  <!-- 椭圆2: rx=69.28, ry=120 -->
  <!-- 交点: (±1, ±1) -> (240, 90), (240, 210), (120, 90), (120, 210) -->
  <defs>
    <clipPath id="clip-e1">
      <ellipse cx="180" cy="150" rx="120" ry="69.28"/>
    </clipPath>
  </defs>
  <!-- 重叠部分浅蓝填充 -->
  <ellipse cx="180" cy="150" rx="69.28" ry="120" fill="#dbeafe" clip-path="url(#clip-e1)"/>
  <!-- 第一象限 1/8 典型区域高亮 (0<=x<=1, x<=y<=sqrt((4-x^2)/3)) -->
  <path d="M 180 150 L 180 80.72 Q 212 80.72 240 90 L 180 150 Z" fill="#60a5fa" fill-opacity="0.75"/>
  <!-- 坐标轴 -->
  <line x1="25" y1="150" x2="338" y2="150" stroke="#1e293b" stroke-width="1.5"/>
  <polygon points="338,150 330,146 330,154" fill="#1e293b"/>
  <line x1="180" y1="288" x2="180" y2="12" stroke="#1e293b" stroke-width="1.5"/>
  <polygon points="180,12 176,20 184,20" fill="#1e293b"/>
  <text x="342" y="154" font-size="13" font-style="italic" fill="#1e293b">x</text>
  <text x="168" y="18" font-size="13" font-style="italic" fill="#1e293b">y</text>
  <text x="166" y="164" font-size="12" fill="#1e293b">O</text>
  <!-- 两椭圆边框 -->
  <ellipse cx="180" cy="150" rx="120" ry="69.28" fill="none" stroke="#2563eb" stroke-width="2.2"/>
  <ellipse cx="180" cy="150" rx="69.28" ry="120" fill="none" stroke="#ea580c" stroke-width="2.2"/>
  <!-- 对称轴 y = x -->
  <line x1="90" y1="240" x2="275" y2="55" stroke="#16a34a" stroke-width="1.4" stroke-dasharray="4,2"/>
  <!-- 4个交点 -->
  <circle cx="240" cy="90" r="3.5" fill="#dc2626"/>
  <circle cx="120" cy="90" r="3.5" fill="#dc2626"/>
  <circle cx="120" cy="210" r="3.5" fill="#dc2626"/>
  <circle cx="240" cy="210" r="3.5" fill="#dc2626"/>
  <!-- 标注 -->
  <text x="247" y="88" font-size="11" fill="#dc2626" font-weight="bold">(1, 1)</text>
  <text x="72" y="88" font-size="11" fill="#dc2626" font-weight="bold">(-1, 1)</text>
  <text x="68" y="222" font-size="11" fill="#dc2626" font-weight="bold">(-1, -1)</text>
  <text x="246" y="222" font-size="11" fill="#dc2626" font-weight="bold">(1, -1)</text>
  <text x="298" y="166" font-size="11" fill="#2563eb">2</text>
  <text x="185" y="34" font-size="11" fill="#ea580c">2</text>
  <text x="280" y="122" font-size="11" fill="#2563eb" font-weight="bold">①</text>
  <text x="215" y="45" font-size="11" fill="#ea580c" font-weight="bold">②</text>
  <text x="268" y="52" font-size="11" fill="#16a34a" font-weight="bold">y = x</text>
  <text x="196" y="110" font-size="12" fill="#1e3a8a" font-weight="bold">S/8</text>
</svg>
- **【分步标准解答】**
  **`[1]` 4つの交点の座標**
  ① + ② より，
  $$4x^2 + 4y^2 = 8 \implies x^2 + y^2 = 2 \quad \cdots \text{③}$$
  ① $-$ ③ より，$2y^2 = 2 \implies y^2 = 1 \implies y = \pm 1$。
  ③ に代入して，$x^2 = 1 \implies x = \pm 1$。
  したがって，4つの交点の座標は，
  $$(1, 1),\quad (1, -1),\quad (-1, 1),\quad (-1, -1)$$

  **`[2]` 重なった部分の面積 $S$**
  2つの楕円 ①，② はともに $x$ 軸，$y$ 軸に関して対称であり，さらに ① の $x$ と $y$ を入れ替えると ② になるから，2つの楕円は直線 $y = x$ に関しても対称である。
  よって，重なった部分の図形は $x$ 軸，$y$ 軸，直線 $y = x,\; y = -x$ によって合同な **8つの部分** に分けられる。
  > 💡 讲师批注：抓住 **「关于 $y = x$ 互相对称」** 这一神级洞察，直接将整个面积压缩为第一象限中 $0 \le x \le 1$ 上方一块（图中的 $S/8$）的 **8 倍**，免去了分别对两个椭圆做两次根式积分的麻烦！

  第1象限の直線 $y = x$ より上側かつ $0 \le x \le 1$ の部分（面積 $\dfrac{S}{8}$）を考える。
  $0 \le x \le 1$ において，① より $y = \sqrt{\dfrac{4 - x^2}{3}}$，② より $y = \sqrt{4 - 3x^2}$ であり，
  $$(4 - 3x^2) - \frac{4 - x^2}{3} = \frac{8(1 - x^2)}{3} \ge 0$$
  なので，① の方が下側（重なった部分の上側の境界）になる。よって，
  $$S = 8 \int_0^1 \left(\sqrt{\frac{4 - x^2}{3}} - x\right)dx = \frac{8}{\sqrt{3}}\int_0^1 \sqrt{4 - x^2}\,dx - 8\int_0^1 x\,dx$$
  ここで，$I = \displaystyle\int_0^1 \sqrt{4 - x^2}\,dx$ を求める。$x = 2\sin\theta\;\left(0 \le \theta \le \dfrac{\pi}{6}\right)$ とおくと，$dx = 2\cos\theta\,d\theta$ であり，$\cos\theta \ge 0$ より $\sqrt{4 - x^2} = 2\cos\theta$。したがって，
  $$I = \int_0^{\frac{\pi}{6}} 2\cos\theta \cdot 2\cos\theta\,d\theta = 2\int_0^{\frac{\pi}{6}} (1 + \cos 2\theta)\,d\theta = \left[2\theta + \sin 2\theta\right]_0^{\frac{\pi}{6}} = \frac{\pi}{3} + \frac{\sqrt{3}}{2}$$
  > 💡 讲师批注：**初等几何秒算 $I$**：$\int_0^1 \sqrt{4 - x^2}\,dx$ 表示半径为 $2$ 的圆在 $0 \le x \le 1$ 内的曲边梯形面积 =（圆心角 $\frac{\pi}{6}$ 的扇形面积 $\frac{1}{2}\cdot 2^2 \cdot \frac{\pi}{6} = \frac{\pi}{3}$）$+$（直角边 $1, \sqrt{3}$ 的直角三角形面积 $\frac{\sqrt{3}}{2}$），与换元结果完全一致！

  また，$\displaystyle\int_0^1 x\,dx = \left[\frac{1}{2}x^2\right]_0^1 = \frac{1}{2}$ であるから，
  $$S = \frac{8}{\sqrt{3}}\left(\frac{\pi}{3} + \frac{\sqrt{3}}{2}\right) - 8 \cdot \frac{1}{2} = \frac{8\pi}{3\sqrt{3}} + 4 - 4 = \frac{8\sqrt{3}}{9}\pi$$
  > 💡 讲师批注：常数项 $+4$ 与 $-4$ 竟然完美抵消！量级验算：单个椭圆面积为 $\pi \cdot 2 \cdot \frac{2}{\sqrt{3}} = \frac{4\sqrt{3}}{3}\pi \approx 7.26$，重叠部分面积 $\frac{8\sqrt{3}}{9}\pi \approx 4.84$，恰好为单个椭圆面积的 $\dfrac{2}{3}$，且大于四个交点组成的正方形面积 $4$，100% 合理！
- **【最终答案】**
  - **`[1]` $(1, 1),\; (1, -1),\; (-1, 1),\; (-1, -1)$**
  - **`[2]` $S = \dfrac{8\sqrt{3}}{9}\pi$**

---

## 附：下篇题型速查与考场提速策略小结

| 题号 | 核心图形 / 函数 | 必杀提速技巧 | 最终答案 |
| :--- | :--- | :--- | :--- |
| **17-(5)** | $y=\sin x,\; y=\sin 2x$ | 关于 $(\pi, 0)$ 点对称，积分段数减半 | $5$ |
| **17-(6)** | 抛物线 + 两直线（连立不等式） | 三线共点 $(-2,4)$，两次 $\frac{1}{6}$ 公式直接做差 | $\dfrac{49}{3}$ |
| **17-(7)** | 抛物线 + 两条切线 | 交点在中点 $x=3$，直接用 $\frac{1}{12}$ 公式 | $18$ |
| **17-(8)** | 两同开口抛物线 + 公切线 | 联立 $D=0$ 求公切线，再用 $\frac{1}{12}$ 公式 | $y=-2x-1$；$\dfrac{16}{3}$ |
| **17-(9)** | 三次函数 + 切线 | 切点二重根秒求另一根，用三次 $\frac{1}{12}$ 公式 | $\dfrac{64}{3}$ |
| **17-(10)** | $y=\log x$ 与 $y=ax^2$ 相切 | 整体代换 $at^2 = \frac{1}{2}$；可用对 $y$ 积分验算 | $a=\dfrac{1}{2e}$；$\dfrac{2\sqrt{e}}{3}-1$ |
| **17-(11)** | 抛物线 + 相切圆劣弧 | 法线过圆心求切点；$\frac{1}{6}$ 公式 $-$ 弓形面积 | $\left(\pm\dfrac{\sqrt{3}}{2}, \dfrac{3}{4}\right)$；$\dfrac{3\sqrt{3}}{4}-\dfrac{\pi}{3}$ |
| **17-(12)** | 两正交椭圆重叠面积 | 关于 $y=x$ 的 **8 重对称性** + 圆弧几何面积 | $(\pm 1, \pm 1)$；$\dfrac{8\sqrt{3}}{9}\pi$ |
