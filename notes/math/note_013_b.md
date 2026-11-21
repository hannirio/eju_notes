# 《EJU 教材全解与备课讲义》数学 013（P181–P195）·下篇

> **对应源文件**：`work_math/ocr_md/ocr_013_p181-195.md`（原书 P188–P194：演習問題 11［2次曲線の性質・離心率・領域］、演習問題 12［媒介変数表示］）
> **视觉核对参考图**：`work_math/ref_imgs/page_0186.jpg` – `page_0195.jpg`
> **前篇链接**：知识点梳理、词汇表、口语读法及演習問題 9–10 详见 [`note_013_a.md`](./note_013_a.md)。

---

## 三、逐题深度解析（不可跳步）·下篇（演習問題 11–12）

---

### 演習問題 11（2次曲線の性質・離心率・領域）

#### 演習問題 11-(1)
- **【原题重现与翻译】**
  - 原题：$a > 0,\; a \neq 1$ とする。点 $A(a, 0)$ からの距離と直線 $x = \dfrac{1}{a}$ からの距離の比が $a : 1$ である点 $P$ の軌跡を求めよ。
  - 中文：设 $a > 0,\; a \neq 1$。求到点 $A(a, 0)$ 的距离与到直线 $x = \dfrac{1}{a}$ 的距离之比为 $a : 1$ 的点 $P$ 的轨迹。
- **【考点定位】**
  - 二次曲线的统一定义（焦点、准线、离心率 $e = a$）、**按参数范围分类讨论（場合分け）**。
- **【图解辅助（SVG 矢量图）】**

<svg viewBox="0 0 540 240" width="540" height="240" xmlns="http://www.w3.org/2000/svg" style="background:#fafafa;border:1px solid #e0e0e0;border-radius:6px;">
  <style>
    .axis { stroke:#333; stroke-width:1.3; }
    .dir { stroke:#e74c3c; stroke-width:1.4; stroke-dasharray:4,3; }
    .curve { stroke:#2980b9; stroke-width:2; fill:none; }
    .txt { font: 11px sans-serif; fill:#2c3e50; }
    .title { font: bold 12px sans-serif; fill:#2c3e50; }
    .lbl { font: bold 11px sans-serif; fill:#c0392b; }
  </style>
  <!-- Left panel: 0 < a < 1 (Ellipse, e.g. a=0.6) -->
  <text x="18" y="22" class="title">(i) 0 &lt; a &lt; 1 のとき：楕円</text>
  <!-- Origin (120, 130), scale 1 unit = 55px -->
  <line x1="20" y1="130" x2="255" y2="130" class="axis"/>
  <line x1="120" y1="40" x2="120" y2="220" class="axis"/>
  <text x="246" y="144" class="txt">x</text>
  <text x="126" y="48" class="txt">y</text>
  <text x="108" y="143" class="txt">O</text>
  <!-- Ellipse rx=55 (1), ry=44 (sqrt(1-0.36)=0.8) -->
  <ellipse cx="120" cy="130" rx="55" ry="44" class="curve"/>
  <!-- Focus A(0.6,0)=(153,130), Directrix x=1/0.6=1.67 -> x=120+91.7=211.7 -->
  <line x1="212" y1="45" x2="212" y2="215" class="dir"/>
  <circle cx="153" cy="130" r="3" fill="#e74c3c"/>
  <text x="148" y="146" class="lbl">A(a,0)</text>
  <text x="195" y="60" class="lbl">x = 1/a</text>
  <text x="178" y="125" class="txt">1</text>
  <text x="52" y="125" class="txt">-1</text>
  <text x="48" y="215" class="txt" fill="#2980b9">x² + y²/(1-a²) = 1</text>
  <!-- Divider -->
  <line x1="270" y1="15" x2="270" y2="225" stroke="#ddd" stroke-width="1"/>
  <!-- Right panel: a > 1 (Hyperbola, e.g. a=1.5) -->
  <text x="288" y="22" class="title">(ii) a &gt; 1 のとき：双曲線</text>
  <!-- Origin (400, 130), scale 1 unit = 45px -->
  <line x1="285" y1="130" x2="525" y2="130" class="axis"/>
  <line x1="400" y1="40" x2="400" y2="220" class="axis"/>
  <text x="515" y="144" class="txt">x</text>
  <text x="406" y="48" class="txt">y</text>
  <text x="388" y="143" class="txt">O</text>
  <!-- Hyperbola vertices (±1,0) -> (355,130), (445,130) -->
  <path d="M 505,48 Q 445,102 445,130 Q 445,158 505,212" class="curve"/>
  <path d="M 295,48 Q 355,102 355,130 Q 355,158 295,212" class="curve"/>
  <!-- Focus A(1.5,0)=(467.5,130), Directrix x=1/1.5=0.67 -> 430 -->
  <line x1="430" y1="45" x2="430" y2="215" class="dir"/>
  <circle cx="468" cy="130" r="3" fill="#e74c3c"/>
  <text x="462" y="146" class="lbl">A(a,0)</text>
  <text x="414" y="60" class="lbl">x=1/a</text>
  <text x="330" y="215" class="txt" fill="#2980b9">x² - y²/(a²-1) = 1</text>
</svg>

- **【分步标准解答】**
  点 $P$ の座標を $(x, y)$ とし、点 $P$ から直線 $x = \dfrac{1}{a}$ に下ろした垂線を $PH$ とする。
  条件 $PA : PH = a : 1$ より、$PA = a \cdot PH$ であるから、
  $$\sqrt{(x - a)^2 + y^2} = a \left|x - \frac{1}{a}\right| = |ax - 1|$$
  両辺はともに $0$ 以上であるから、両辺を 2 乗しても同値であり、
  $$(x - a)^2 + y^2 = (ax - 1)^2$$
  展開して整理すると、
  $$x^2 - 2ax + a^2 + y^2 = a^2 x^2 - 2ax + 1$$
  $$(1 - a^2)x^2 + y^2 = 1 - a^2$$
  > 💡 讲师批注：展开后两边的 $-2ax$ 恰好消去！这正是因为原点恰好是轨迹的对称中心（离心率 $e = a$，半实/长轴长为 $1$，焦点 $(e, 0) = (a, 0)$，准线 $x = \frac{1}{e} = \frac{1}{a}$）。

  条件 $a > 0,\; a \neq 1$ より $1 - a^2 \neq 0$ であるから、両辺を $1 - a^2$ で割ると、
  $$x^2 + \frac{y^2}{1 - a^2} = 1$$
  ここで、$1 - a^2$ の符号によって場合分けする：
  - **$0 < a < 1$ のとき**：$1 - a^2 > 0$ であるから、軌跡は**楕円** $x^2 + \dfrac{y^2}{1 - a^2} = 1$。
  - **$a > 1$ のとき**：$a^2 - 1 > 0$ であるから、軌跡は**双曲線** $x^2 - \dfrac{y^2}{a^2 - 1} = 1$。
  > 💡 讲师批注：写出轨迹方程的同时，日本 EJU 习惯明确指出图形名称（楕円 / 双曲線），并将分母整理为正数形式（$a > 1$ 时写成 $x^2 - \frac{y^2}{a^2 - 1} = 1$）。

- **【最终答案】**
  - **$0 < a < 1$ のとき：楕円 $x^2 + \dfrac{y^2}{1 - a^2} = 1$**
  - **$a > 1$ のとき：双曲線 $x^2 - \dfrac{y^2}{a^2 - 1} = 1$**

---

#### 演習問題 11-(2)
- **【原题重现与翻译】**
  - 原题：楕円上にあって長軸、短軸上にない点 $P$ と短軸の両端を結ぶ 2 つの直線が、長軸またはその延長と交わる点をそれぞれ $Q, R$ とする。楕円の中心を $O$ とすると、線分 $OQ, OR$ の長さの積は一定であることを証明せよ。
  - 中文：设 $P$ 为椭圆上不在长轴、短轴上的一点，将点 $P$ 与短轴两端点相连的两条直线分别交长轴或其延长线于 $Q, R$。设椭圆的中心为 $O$，证明线段 $OQ, OR$ 的长度之积为定值。
- **【考点定位】**
  - 坐标法（解析几何）证明椭圆几何定值问题。
- **【图解辅助（SVG 矢量图）】**

<svg viewBox="0 0 460 250" width="460" height="250" xmlns="http://www.w3.org/2000/svg" style="background:#fafafa;border:1px solid #e0e0e0;border-radius:6px;">
  <style>
    .axis { stroke:#333; stroke-width:1.4; }
    .ell { stroke:#2980b9; stroke-width:2.2; fill:none; }
    .line { stroke:#e74c3c; stroke-width:1.6; }
    .txt { font: 12px sans-serif; fill:#2c3e50; }
    .lbl { font: bold 12px sans-serif; fill:#c0392b; }
  </style>
  <!-- Origin (180, 125), rx=100 (a=2 -> 50px/unit), ry=50 (b=1) -->
  <!-- P(sqrt2, 1/sqrt2) = (180+70.7, 125-35.4) = (250.7, 89.6) -->
  <!-- B(0,1)=(180,75), B'(0,-1)=(180,175) -->
  <!-- Q = (2(sqrt2+1), 0) ≈ (4.83, 0) -> x = 180 + 241.4 = 421.4 -->
  <!-- R = (2(sqrt2-1), 0) ≈ (0.83, 0) -> x = 180 + 41.4 = 221.4 -->
  <line x1="30" y1="125" x2="445" y2="125" class="axis"/>
  <line x1="180" y1="20" x2="180" y2="230" class="axis"/>
  <polygon points="445,125 437,121 437,129" fill="#333"/>
  <polygon points="180,20 176,28 184,28" fill="#333"/>
  <text x="435" y="143" class="txt">x</text>
  <text x="188" y="30" class="txt">y</text>
  <text x="165" y="142" class="txt">O</text>
  <ellipse cx="180" cy="125" rx="100" ry="50" class="ell"/>
  <!-- Line PBQ -->
  <line x1="180" y1="75" x2="421.4" y2="125" class="line"/>
  <!-- Line PB'R -->
  <line x1="180" y1="175" x2="250.7" y2="89.6" class="line"/>
  <circle cx="180" cy="75" r="3.5" fill="#2c3e50"/>
  <circle cx="180" cy="175" r="3.5" fill="#2c3e50"/>
  <circle cx="250.7" cy="89.6" r="4" fill="#e74c3c"/>
  <circle cx="421.4" cy="125" r="4" fill="#e74c3c"/>
  <circle cx="221.4" cy="125" r="4" fill="#e74c3c"/>
  <text x="142" y="72" class="txt">B(0, b)</text>
  <text x="135" y="190" class="txt">B'(0, -b)</text>
  <text x="255" y="82" class="lbl">P(x₀, y₀)</text>
  <text x="224" y="143" class="lbl">R</text>
  <text x="415" y="143" class="lbl">Q</text>
  <text x="282" y="142" class="txt">a</text>
  <text x="64" y="142" class="txt">-a</text>
  <text x="285" y="205" class="lbl">OQ · OR = a² (一定)</text>
</svg>

- **【分步标准解答】**
  **［証明］**
  座標平面上で、楕円の中心 $O$ を原点、長軸を $x$ 軸、短軸を $y$ 軸にとると、楕円の方程式は
  $$\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1 \qquad (a > b > 0)$$
  と表される。このとき、短軸の両端は $B(0, b),\; B'(0, -b)$ である。
  楕円上の点 $P$ の座標を $(x_0, y_0)$ とすると、点 $P$ は長軸・短軸上にないので $x_0 \neq 0,\; y_0 \neq 0$（したがって $y_0 \neq \pm b$）であり、
  $$\frac{x_0^2}{a^2} + \frac{y_0^2}{b^2} = 1 \qquad \cdots \text{①}$$
  > 💡 讲师批注：由于 $P$ 不在短轴（$y$ 轴）上，故 $x_0 \neq 0$，这保证了直线 $PB, PB'$ 的斜率均存在；且 $y_0 \neq \pm b$，保证了直线 $PB, PB'$ 均不平行于 $x$ 轴，必与 $x$ 轴相交！

  1. **直線 $PB$ と $x$ 軸との交点 $Q$**：
     直線 $PB$ は 2 点 $(0, b),\; (x_0, y_0)$ を通るから、その方程式は
     $$y = \frac{y_0 - b}{x_0}x + b$$
     $y = 0$ を代入すると、$Q$ の $x$ 座標 $x_Q$ は
     $$0 = \frac{y_0 - b}{x_0}x_Q + b \implies x_Q = -\frac{bx_0}{y_0 - b} = \frac{bx_0}{b - y_0}$$
  2. **直線 $PB'$ と $x$ 軸との交点 $R$**：
     直線 $PB'$ は 2 点 $(0, -b),\; (x_0, y_0)$ を通るから、その方程式は
     $$y = \frac{y_0 + b}{x_0}x - b$$
     $y = 0$ を代入すると、$R$ の $x$ 座標 $x_R$ は
     $$0 = \frac{y_0 + b}{x_0}x_R - b \implies x_R = \frac{bx_0}{y_0 + b}$$

  したがって、線分 $OQ, OR$ の長さの積 $OQ \cdot OR$ は
  $$OQ \cdot OR = |x_Q| \cdot |x_R| = |x_Q x_R| = \left|\frac{bx_0}{b - y_0} \cdot \frac{bx_0}{y_0 + b}\right| = \left|\frac{b^2 x_0^2}{b^2 - y_0^2}\right|$$
  ここで、① より $\dfrac{y_0^2}{b^2} = 1 - \dfrac{x_0^2}{a^2}$ であるから、両辺に $b^2$ を掛けて
  $$b^2 - y_0^2 = \frac{b^2}{a^2}x_0^2$$
  これを上式に代入すると（$x_0 \neq 0$ より約分できて）、
  $$OQ \cdot OR = \left|\frac{b^2 x_0^2}{\dfrac{b^2}{a^2}x_0^2}\right| = a^2$$
  $a^2$ は点 $P$ の位置によらない定数であるから、線分 $OQ, OR$ の長さの積は一定である。　（証明終）
  > 💡 讲师批注：**巧用参数方程的另解**：令 $P(a\cos\theta, b\sin\theta)$，则 $x_Q = \frac{a\cos\theta}{1 - \sin\theta}$，$x_R = \frac{a\cos\theta}{1 + \sin\theta}$，瞬间得出 $OQ \cdot OR = \left|\frac{a^2\cos^2\theta}{1 - \sin^2\theta}\right| = a^2$！在 EJU 填空题中参数法极快。

- **【最终答案】**
  **$OQ \cdot OR = a^2$（長軸の半分の長さの 2 乗で一定、証明完了）**

---

#### 演習問題 11-(3)
- **【原题重现与翻译】**
  - 原题：実数 $x, y$ が 2 つの不等式 $y \le x + 1,\; x^2 + 4y^2 \le 4$ を満たすとき、$y - 2x$ の最大値、最小値を求めよ。
  - 中文：当实数 $x, y$ 满足两个不等式 $y \le x + 1$ 与 $x^2 + 4y^2 \le 4$ 时，求 $y - 2x$ 的最大值与最小值。
- **【考点定位】**
  - 椭圆与直线围成的平面区域（領域）上的线性规划最值问题、**切点是否在可行域内的检验（高频易错点）**。
- **【图解辅助（SVG 矢量图）】**

<svg viewBox="0 0 460 280" width="460" height="280" xmlns="http://www.w3.org/2000/svg" style="background:#fafafa;border:1px solid #e0e0e0;border-radius:6px;">
  <style>
    .axis { stroke:#333; stroke-width:1.4; }
    .ell { stroke:#2980b9; stroke-width:2; fill:none; }
    .line1 { stroke:#27ae60; stroke-width:1.8; }
    .kline { stroke:#e74c3c; stroke-width:1.6; stroke-dasharray:5,3; }
    .txt { font: 12px sans-serif; fill:#2c3e50; }
    .lbl { font: bold 12px sans-serif; fill:#c0392b; }
  </style>
  <defs>
    <!-- Clip path for region y <= x + 1 -->
    <!-- Origin (230, 140), scale 1 unit = 55px -->
    <!-- Line y = x + 1 passes (-2.5, -1.5) = (92.5, 222.5) and (1.5, 2.5) = (312.5, 2.5) -->
    <clipPath id="belowLine">
      <polygon points="92.5,222.5 312.5,2.5 460,2.5 460,280 92.5,280"/>
    </clipPath>
  </defs>
  <!-- Shaded feasible region D -->
  <ellipse cx="230" cy="140" rx="110" ry="55" fill="#d6eaf8" clip-path="url(#belowLine)"/>
  <!-- Axes -->
  <line x1="50" y1="140" x2="410" y2="140" class="axis"/>
  <line x1="230" y1="15" x2="230" y2="265" class="axis"/>
  <polygon points="410,140 402,136 402,144" fill="#333"/>
  <polygon points="230,15 226,23 234,23" fill="#333"/>
  <text x="398" y="158" class="txt">x</text>
  <text x="238" y="26" class="txt">y</text>
  <text x="215" y="156" class="txt">O</text>
  <!-- Ellipse x^2/4 + y^2/1 = 1 -->
  <ellipse cx="230" cy="140" rx="110" ry="55" class="ell"/>
  <!-- Line y = x + 1 -->
  <line x1="92.5" y1="222.5" x2="290" y2="25" class="line1"/>
  <!-- Intersections A(0,1)=(230,85), B(-1.6, -0.6)=(142, 173) -->
  <circle cx="230" cy="85" r="3.5" fill="#27ae60"/>
  <circle cx="142" cy="173" r="4" fill="#e74c3c"/>
  <!-- Max line y = 2x + 13/5 through B(-1.6, -0.6)=(142,173): slope 2 -> (-2.1,-1.6)=(114.5,228) to (-0.6,1.4)=(197,63) -->
  <line x1="114.5" y1="228" x2="197" y2="63" class="kline"/>
  <!-- Min line y = 2x - sqrt17 (≈-4.123) tangent at (8/sqrt17, -1/sqrt17) ≈ (1.94, -0.243) = (336.7, 153.3) -->
  <!-- Passes (1.3, -1.52)=(301.5, 223.8) to (2.4, 0.68)=(362, 102.8) -->
  <line x1="301.5" y1="223.8" x2="362" y2="102.8" class="kline"/>
  <circle cx="336.7" cy="153.3" r="4" fill="#e74c3c"/>
  <text x="236" y="80" class="txt">A(0, 1)</text>
  <text x="48" y="168" class="lbl">B(-8/5, -3/5)</text>
  <text x="125" y="55" class="lbl">最大 k = 13/5</text>
  <text x="342" y="168" class="lbl">T(8/√17, -1/√17)</text>
  <text x="325" y="95" class="lbl">最小 k = -√17</text>
  <text x="275" y="42" class="txt" fill="#27ae60">y = x + 1</text>
  <text x="260" y="170" class="txt" fill="#2980b9">領域 D</text>
</svg>

- **【分步标准解答】**
  連立不等式 $y \le x + 1,\; \dfrac{x^2}{4} + \dfrac{y^2}{1} \le 1$ の表す領域を $D$ とする。
  まず、直線 $y = x + 1$ と楕円 $x^2 + 4y^2 = 4$ の交点を求める。$y = x + 1$ を代入すると、
  $$x^2 + 4(x + 1)^2 = 4 \iff 5x^2 + 8x = 0 \iff x(5x + 8) = 0$$
  よって $x = 0,\; -\dfrac{8}{5}$ であり、交点は $A(0, 1),\; B\left(-\dfrac{8}{5},\; -\dfrac{3}{5}\right)$ である。領域 $D$ は上図の着色部分（境界を含む）。

  $y - 2x = k$ とおくと、
  $$y = 2x + k \qquad \cdots \text{①}$$
  これは傾き $2$、$y$ 切片 $k$ の直線を表す。直線 ① が領域 $D$ と共有点をもつときの $k$ の最大値・最小値を求める。

  まず、直線 ① が楕円 $x^2 + 4y^2 = 4$ に接するときの $k$ と接点を求める。① を楕円に代入して
  $$x^2 + 4(2x + k)^2 = 4 \iff 17x^2 + 16kx + 4k^2 - 4 = 0 \qquad \cdots \text{②}$$
  ② の判別式を $D_1$ とすると、接する条件 $D_1 = 0$ より
  $$\frac{D_1}{4} = (8k)^2 - 17(4k^2 - 4) = 64k^2 - 68k^2 + 68 = -4k^2 + 68 = 0$$
  $$k^2 = 17 \implies k = \pm \sqrt{17}$$
  このとき、② の重解（接点の $x$ 座標）は $x = -\dfrac{8k}{17}$ である：
  - **$k = -\sqrt{17}$ のとき**：接点は $x = \dfrac{8\sqrt{17}}{17},\; y = 2 \cdot \dfrac{8\sqrt{17}}{17} - \sqrt{17} = -\dfrac{\sqrt{17}}{17}$。
    ここで $x + 1 = \dfrac{8\sqrt{17}}{17} + 1 > 0 > -\dfrac{\sqrt{17}}{17} = y$ であるから、この接点は**領域 $D$ 内に含まれる**。
    したがって、最小値は $-\sqrt{17}$ である。
  - **$k = \sqrt{17}$ のとき**：接点は $x = -\dfrac{8\sqrt{17}}{17},\; y = \dfrac{\sqrt{17}}{17}$。
    ここで $x + 1 = 1 - \dfrac{8}{\sqrt{17}} < 0 < \dfrac{1}{\sqrt{17}} = y$（$\because \sqrt{17} < 8$）であるから、この接点は $y \le x + 1$ を満たさず、**領域 $D$ 外にある**！
  > 💡 讲师批注：**本题最大陷阱！** 千万不要看到 $k = \pm \sqrt{17}$ 就直接写最大值为 $\sqrt{17}$！必须代入 $y \le x + 1$ 检验切点是否在可行域 $D$ 内！

  上図より、直線 ①（傾き $2$）は境界直線 $y = x + 1$（傾き $1$）よりも傾きが大きいため、領域 $D$ 内で $k$ が最大となるのは、直線 ① が交点 $B\left(-\dfrac{8}{5},\; -\dfrac{3}{5}\right)$ を通るときである。
  > 💡 讲师批注：严谨确认：椭圆在点 $B\left(-\frac{8}{5}, -\frac{3}{5}\right)$ 处的切线为 $-\frac{8}{5}x - \frac{12}{5}y = 4$，其斜率为 $-\frac{2}{3} < 2$，故直线 ① 过 $B$ 点时不会再次切入 $B$ 点左下方的椭圆内部，因此 $B$ 确为最大值点！

  点 $B\left(-\dfrac{8}{5},\; -\dfrac{3}{5}\right)$ を $k = y - 2x$ に代入すると、
  $$k = -\frac{3}{5} - 2\left(-\frac{8}{5}\right) = \frac{-3 + 16}{5} = \frac{13}{5}$$

- **【最终答案】**
  - **最大値：$\dfrac{13}{5}$**（$x = -\dfrac{8}{5},\; y = -\dfrac{3}{5}$ のとき）
  - **最小値：$-\sqrt{17}$**（$x = \dfrac{8\sqrt{17}}{17},\; y = -\dfrac{\sqrt{17}}{17}$ のとき）

---

#### 演習問題 11-(4)
- **【原题重现与翻译】**
  - 原题：連立不等式 $x - 2y + 3 \ge 0,\; 2x - y \le 0,\; x + y \ge 0$ の表す領域を $A$ とする。点 $(x, y)$ が領域 $A$ を動くとき、$y^2 - 4x$ の最小値と、その時の $x, y$ の値を求めよ。
  - 中文：设联立不等式 $x - 2y + 3 \ge 0,\; 2x - y \le 0,\; x + y \ge 0$ 所表示的区域为 $A$。当点 $(x, y)$ 在区域 $A$ 内移动时，求 $y^2 - 4x$ 的最小值以及此时 $x, y$ 的值。
- **【考点定位】**
  - 非线性目标函数（**抛物线族** $y^2 - 4x = k$）在多边形区域上的最值问题。
- **【图解辅助（SVG 矢量图）】**

<svg viewBox="0 0 460 270" width="460" height="270" xmlns="http://www.w3.org/2000/svg" style="background:#fafafa;border:1px solid #e0e0e0;border-radius:6px;">
  <style>
    .axis { stroke:#333; stroke-width:1.4; }
    .tri { fill:#d5f5e3; stroke:#27ae60; stroke-width:2; }
    .par { stroke:#e74c3c; stroke-width:2; fill:none; }
    .par0 { stroke:#95a5a6; stroke-width:1.2; stroke-dasharray:4,3; fill:none; }
    .txt { font: 12px sans-serif; fill:#2c3e50; }
    .lbl { font: bold 12px sans-serif; fill:#c0392b; }
  </style>
  <!-- Origin (200, 210), scale: 1 unit = 75px -->
  <!-- Vertices: O(0,0)=(200,210), P(1,2)=(275,60), Q(-1,1)=(125,135) -->
  <line x1="40" y1="210" x2="420" y2="210" class="axis"/>
  <line x1="200" y1="20" x2="200" y2="255" class="axis"/>
  <polygon points="420,210 412,206 412,214" fill="#333"/>
  <polygon points="200,20 196,28 204,28" fill="#333"/>
  <text x="408" y="226" class="txt">x</text>
  <text x="208" y="30" class="txt">y</text>
  <text x="184" y="226" class="txt">O</text>
  <!-- Triangle A -->
  <polygon points="200,210 275,60 125,135" class="tri"/>
  <!-- Parabola k=0: x = y^2/4 -> (0,0)=(200,210), (1,2)=(275,60), (1,-2) -->
  <path d="M 310,30 Q 200,140 200,210 Q 200,235 235,255" class="par0"/>
  <!-- Optimal parabola k=-1: x = y^2/4 + 1/4, vertex (0.25, 0)=(218.75, 210), tangent at (0.5, 1)=(237.5, 135) -->
  <!-- At y=2: x=1.25 -> (293.75, 60); At y=2.2: x=1.46 -> (309.5, 45); At y=-0.6: x=0.34 -> (225.5, 255) -->
  <path d="M 310,45 Q 218.75,135 218.75,210 Q 218.75,235 245,255" class="par"/>
  <circle cx="200" cy="210" r="3.5" fill="#27ae60"/>
  <circle cx="275" cy="60" r="3.5" fill="#27ae60"/>
  <circle cx="125" cy="135" r="3.5" fill="#27ae60"/>
  <circle cx="237.5" cy="135" r="4.5" fill="#e74c3c"/>
  <text x="282" y="62" class="txt">P(1, 2)</text>
  <text x="68" y="138" class="txt">Q(-1, 1)</text>
  <text x="172" y="148" class="txt" fill="#27ae60" font-weight="bold">領域 A</text>
  <text x="246" y="142" class="lbl">接点 (1/2, 1)</text>
  <text x="215" y="232" class="lbl">頂点 (1/4, 0)</text>
  <text x="315" y="52" class="lbl">y² - 4x = -1</text>
</svg>

- **【分步标准解答】**
  与えられた 3 つの不等式をそれぞれ $y$ について整理すると、
  $$y \le \frac{1}{2}x + \frac{3}{2}, \qquad y \ge 2x, \qquad y \ge -x$$
  3 直線の交点をそれぞれ求めると、
  - $y = 2x$ と $y = -x$ の交点：$O(0, 0)$
  - $y = \dfrac{1}{2}x + \dfrac{3}{2}$ と $y = 2x$ の交点：$2x = \dfrac{1}{2}x + \dfrac{3}{2} \implies x = 1,\; y = 2$、よって $P(1, 2)$
  - $y = \dfrac{1}{2}x + \dfrac{3}{2}$ と $y = -x$ の交点：$-x = \dfrac{1}{2}x + \dfrac{3}{2} \implies x = -1,\; y = 1$、よって $Q(-1, 1)$

  したがって、領域 $A$ は 3 点 $O(0, 0),\; P(1, 2),\; Q(-1, 1)$ を頂点とする三角形の周および内部である。

  ここで、$y^2 - 4x = k$ とおくと、
  $$x = \frac{1}{4}y^2 - \frac{k}{4} \qquad \cdots \text{①}$$
  これは頂点が $\left(-\dfrac{k}{4},\; 0\right)$、軸が $x$ 軸、右に開いた放物線を表す。
  $k$ が最小となるのは、頂点の $x$ 座標 $-\dfrac{k}{4}$ が**最大**になるとき、すなわち放物線 ① が領域 $A$ と共有点をもちながら**最も右側**にくるときである。
  > 💡 讲师批注：把目标函数改写成 $x = \frac{1}{4}y^2 - \frac{k}{4}$ 是破题关键！因为 $k$ 前面带负号，所以「$k$ 最小 $\iff$ 抛物线顶点 $-\frac{k}{4}$ 最靠右」。

  上図より、放物線 ① が最も右側で領域 $A$ と共有点をもつのは、放物線 ① が領域 $A$ の右端の境界である線分 $OP$（直線 $y = 2x$ 上の $0 \le x \le 1$ の部分）に接するときである。
  直線 $y = 2x$（すなわち $x = \dfrac{y}{2}$）を $y^2 - 4x = k$ に代入すると、
  $$y^2 - 2y - k = 0 \qquad \cdots \text{②}$$
  接する条件（判別式 $D = 0$）より、
  $$\frac{D}{4} = (-1)^2 - 1 \cdot (-k) = 1 + k = 0 \implies k = -1$$
  このとき、② の重解は $y = 1$ であり、$x = \dfrac{y}{2} = \dfrac{1}{2}$。
  点 $\left(\dfrac{1}{2},\; 1\right)$ は $0 \le \dfrac{1}{2} \le 1$ を満たすため、確かに線分 $OP$ 上（領域 $A$ 内）にある！
  > 💡 讲师批注：代数秒杀验算：在区域 $A$ 中恒有 $2x \le y$，即 $4x \le 2y$，所以 $y^2 - 4x \ge y^2 - 2y = (y - 1)^2 - 1 \ge -1$！等号成立当且仅当 $y = 1$ 且 $4x = 2y \iff x = \frac{1}{2}$，检验该点满足 $x - 2y + 3 = \frac{3}{2} \ge 0$ 与 $x + y = \frac{3}{2} \ge 0$，确实在区域 $A$ 内！几行就完成绝对严谨的验算。

- **【最终答案】**
  **$x = \dfrac{1}{2},\; y = 1$ のとき、最小値 $-1$**

---

### 演習問題 12（媒介変数表示）

#### 演習問題 12-(1)
- **【原题重现与翻译】**
  - 原题：放物線 $y = x^2 - 2(t + 1)x + 2t^2 - t$ の頂点は、$t$ の値が変化するとき、どんな曲線上を動くか。
  - 中文：当 $t$ 的值变化时，抛物线 $y = x^2 - 2(t + 1)x + 2t^2 - t$ 的顶点在怎样的曲线上移动？
- **【考点定位】**
  - 配方法（平方完成）求含参抛物线顶点坐标、消去参数 $t$ 求轨迹。
- **【分步标准解答】**
  与えられた放物線の方程式を平方完成すると、
  $$y = \{x - (t + 1)\}^2 - (t + 1)^2 + 2t^2 - t$$
  $$= \{x - (t + 1)\}^2 - (t^2 + 2t + 1) + 2t^2 - t$$
  $$= \{x - (t + 1)\}^2 + t^2 - 3t - 1$$
  したがって、頂点の座標を $(X, Y)$ とすると、
  $$X = t + 1 \quad \cdots \text{①}, \qquad Y = t^2 - 3t - 1 \quad \cdots \text{②}$$
  ① より $t = X - 1$。これを ② に代入して $t$ を消去すると、
  $$Y = (X - 1)^2 - 3(X - 1) - 1$$
  $$= (X^2 - 2X + 1) - 3X + 3 - 1$$
  $$= X^2 - 5X + 3$$
  ここで、$t$ がすべての実数値をとって変化するとき、① より $X = t + 1$ すべての実数値をとる。
  よって、頂点は放物線 $y = x^2 - 5x + 3$ の全体の上を動く。
  > 💡 讲师批注：验算：取 $t = 0$，原抛物线 $y = x^2 - 2x = (x-1)^2 - 1$，顶点 $(1, -1)$，代入 $y = x^2 - 5x + 3$：$1 - 5 + 3 = -1$，吻合！取 $t = 1$，原抛物线 $y = x^2 - 4x + 1 = (x-2)^2 - 3$，顶点 $(2, -3)$，代入 $4 - 10 + 3 = -3$，吻合！

- **【最终答案】**
  **放物線 $y = x^2 - 5x + 3$**

---

#### 演習問題 12-(2)
- **【原题重现与翻译】**
  - 原题：定円 $x^2 + y^2 = r^2$ の周上を点 $P(x, y)$ が動くとき、座標が $(y^2 - x^2,\; 2xy)$ で表される点 $Q$ はどんな曲線上を動くか。
  - 中文：当点 $P(x, y)$ 在定圆 $x^2 + y^2 = r^2$ 的圆周上运动时，坐标为 $(y^2 - x^2,\; 2xy)$ 的点 $Q$ 在怎样的曲线上移动？
- **【考点定位】**
  - 圆的参数方程表示（$x = r\cos\theta,\; y = r\sin\theta$）与三角函数二倍角公式。
- **【分步标准解答】**
  定円 $x^2 + y^2 = r^2$（$r > 0$ とする）の周上を動く点 $P(x, y)$ は、媒介変数 $\theta\ (0 \le \theta < 2\pi)$ を用いて
  $$x = r\cos\theta, \qquad y = r\sin\theta$$
  と表される。点 $Q$ の座標を $(X, Y)$ とすると、2 倍角の公式より
  $$X = y^2 - x^2 = r^2\sin^2\theta - r^2\cos^2\theta = -r^2(\cos^2\theta - \sin^2\theta) = -r^2\cos 2\theta$$
  $$Y = 2xy = 2r^2\sin\theta\cos\theta = r^2\sin 2\theta$$
  > 💡 讲师批注：注意 $y^2 - x^2$ 与 $\cos 2\theta = \cos^2\theta - \sin^2\theta$ 恰好差一个负号，因此 $X = -r^2\cos 2\theta$。

  両式を 2 乗して加えると、
  $$X^2 + Y^2 = (-r^2\cos 2\theta)^2 + (r^2\sin 2\theta)^2 = r^4(\cos^2 2\theta + \sin^2 2\theta) = r^4$$
  ここで、$\theta$ が $0 \le \theta < 2\pi$ の範囲を動くとき、$2\theta$ は $0 \le 2\theta < 4\pi$ の範囲を動くから、点 $Q(X, Y)$ は円 $X^2 + Y^2 = r^4$ の周上をちょうど 2 周し、円周全体を描く。
  したがって、点 $Q$ は原点を中心とし半径 $r^2$ の円 $x^2 + y^2 = r^4$ 上を動く。
  > 💡 讲师批注：若不用参数法而直接算 $(y^2 - x^2)^2 + (2xy)^2 = (x^2 + y^2)^2 = r^4$，虽然能很快得到方程，但较难说明「$Q$ 能否取遍整个圆周（是否存在除外点）」。用参数方程 $\theta$ 配合二倍角公式，一步到位证明了 $Q$ 绕圆周两周、无任何除外点！

- **【最终答案】**
  **円 $x^2 + y^2 = r^4$**（原点を中心とし、半径 $r^2$ の円）

---

#### 演習問題 12-(3)
- **【原题重现与翻译】**
  - 原题：双曲線 $x^2 - y^2 = 1$ と直線 $y = -x + t$ との交点を考えて、この曲線を媒介変数 $t$ を用いて表せ。
  - 中文：考虑双曲线 $x^2 - y^2 = 1$ 与直线 $y = -x + t$ 的交点，用参数 $t$ 表示该双曲线。
- **【考点定位】**
  - 利用直线族（直線群）交点求双曲线的有理参数方程、**参数定义域限制（$t \neq 0$）**。
- **【图解辅助（SVG 矢量图）】**

<svg viewBox="0 0 440 250" width="440" height="250" xmlns="http://www.w3.org/2000/svg" style="background:#fafafa;border:1px solid #e0e0e0;border-radius:6px;">
  <style>
    .axis { stroke:#333; stroke-width:1.4; }
    .asym { stroke:#95a5a6; stroke-width:1.2; stroke-dasharray:4,3; }
    .curve { stroke:#2980b9; stroke-width:2.2; fill:none; }
    .line { stroke:#e74c3c; stroke-width:1.6; }
    .txt { font: 12px sans-serif; fill:#2c3e50; }
    .lbl { font: bold 12px sans-serif; fill:#c0392b; }
  </style>
  <!-- Origin (220, 125), scale 1 unit = 40px -->
  <line x1="40" y1="125" x2="400" y2="125" class="axis"/>
  <line x1="220" y1="15" x2="220" y2="235" class="axis"/>
  <polygon points="400,125 392,121 392,129" fill="#333"/>
  <polygon points="220,15 216,23 224,23" fill="#333"/>
  <text x="390" y="142" class="txt">x</text>
  <text x="228" y="25" class="txt">y</text>
  <text x="206" y="140" class="txt">O</text>
  <!-- Asymptotes y = ±x -->
  <line x1="115" y1="230" x2="325" y2="20" class="asym"/>
  <line x1="115" y1="20" x2="325" y2="230" class="asym"/>
  <!-- Hyperbola x^2 - y^2 = 1 -->
  <path d="M 325,30 Q 260,92 260,125 Q 260,158 325,220" class="curve"/>
  <path d="M 115,30 Q 180,92 180,125 Q 180,158 115,220" class="curve"/>
  <!-- Line y = -x + t (t=2): passes (220,45) and (300,125), intersects at (1.25, 0.75) = (270, 95) -->
  <line x1="200" y1="25" x2="355" y2="180" class="line"/>
  <circle cx="270" cy="95" r="4" fill="#e74c3c"/>
  <text x="278" y="92" class="lbl">P(x, y)</text>
  <text x="328" y="176" class="lbl">y = -x + t (t≠0)</text>
  <text x="80" y="220" class="txt" fill="#7f8c8d">t=0: y=-x (漸近線・交点なし)</text>
  <text x="330" y="42" class="txt" fill="#2980b9">x² - y² = 1</text>
</svg>

- **【分步标准解答】**
  双曲線 $x^2 - y^2 = 1$ を因数分解すると、
  $$(x + y)(x - y) = 1 \qquad \cdots \text{①}$$
  一方、直線 $y = -x + t$ より、
  $$x + y = t \qquad \cdots \text{②}$$
  ② を ① に代入すると、
  $$t(x - y) = 1$$
  ここで、$t = 0$ のときは $0 = 1$ となり不合理（幾何学的には、直線 $y = -x$ は双曲線の漸近線であり交点をもたない）。
  したがって $t \neq 0$ であり、両辺を $t$ で割って
  $$x - y = \frac{1}{t} \qquad \cdots \text{③}$$
  ② と ③ を連立して解く：
  - ② $+$ ③ より：$2x = t + \dfrac{1}{t} \implies x = \dfrac{1}{2}\left(t + \dfrac{1}{t}\right) = \dfrac{t^2 + 1}{2t}$
  - ② $-$ ③ より：$2y = t - \dfrac{1}{t} \implies y = \dfrac{1}{2}\left(t - \dfrac{1}{t}\right) = \dfrac{t^2 - 1}{2t}$

  逆に、双曲線 $x^2 - y^2 = 1$ 上の任意の点 $(x, y)$ に対し $t = x + y$ とおけば、$(x + y)(x - y) = 1$ より $t \neq 0$ であり、上の表示で双曲線全体が過不足なく表される。
  > 💡 讲师批注：**千万不要漏写 $t \neq 0$！** 并且顺带观察：当 $t > 0$ 时对应双曲线右支（$x = \frac{1}{2}(t + \frac{1}{t}) \ge 1$），当 $t < 0$ 时对应双曲线左支（$x \le -1$）。

- **【最终答案】**
  **$x = \dfrac{1}{2}\left(t + \dfrac{1}{t}\right),\quad y = \dfrac{1}{2}\left(t - \dfrac{1}{t}\right)\quad (t \neq 0)$**（または $x = \dfrac{t^2 + 1}{2t},\; y = \dfrac{t^2 - 1}{2t}\ (t \neq 0)$）

---

#### 演習問題 12-(4)
- **【原题重现与翻译】**
  - 原题：曲線 $x = \dfrac{3}{1 + t^2},\; y = \dfrac{3t}{1 + t^2}$ は、どのような図形か（$t$ は媒介変数）。
  - 中文：曲线 $x = \dfrac{3}{1 + t^2},\; y = \dfrac{3t}{1 + t^2}$（$t$ 为参数）是什么图形？
- **【考点定位】**
  - 有理参数方程消参、**除外点（除く点）的严格识别**。
- **【图解辅助（SVG 矢量图）】**

<svg viewBox="0 0 400 230" width="400" height="230" xmlns="http://www.w3.org/2000/svg" style="background:#fafafa;border:1px solid #e0e0e0;border-radius:6px;">
  <style>
    .axis { stroke:#333; stroke-width:1.4; }
    .cir { stroke:#2980b9; stroke-width:2.2; fill:none; }
    .txt { font: 12px sans-serif; fill:#2c3e50; }
    .lbl { font: bold 12px sans-serif; fill:#c0392b; }
  </style>
  <!-- Origin (120, 115), scale 1 unit = 50px -->
  <!-- Circle center (1.5, 0) = (195, 115), radius 1.5 = 75px -->
  <line x1="40" y1="115" x2="360" y2="115" class="axis"/>
  <line x1="120" y1="20" x2="120" y2="210" class="axis"/>
  <polygon points="360,115 352,111 352,119" fill="#333"/>
  <polygon points="120,20 116,28 124,28" fill="#333"/>
  <text x="350" y="132" class="txt">x</text>
  <text x="128" y="30" class="txt">y</text>
  <circle cx="195" cy="115" r="75" class="cir"/>
  <!-- Center dot -->
  <circle cx="195" cy="115" r="3" fill="#2c3e50"/>
  <!-- Excluded origin (hollow circle) -->
  <circle cx="120" cy="115" r="4.5" fill="#fff" stroke="#e74c3c" stroke-width="2"/>
  <text x="184" y="135" class="txt">(3/2, 0)</text>
  <text x="276" y="132" class="txt">3</text>
  <text x="48" y="136" class="lbl">O(0, 0) を除く</text>
  <text x="242" y="52" class="txt" fill="#2980b9">(x - 3/2)² + y² = 9/4</text>
</svg>

- **【分步标准解答】**
  $1 + t^2 \ge 1 > 0$ であるから、すべての実数 $t$ に対して
  $$x = \frac{3}{1 + t^2} > 0 \qquad \text{（すなわち } x \neq 0 \text{）}$$
  である。$y = \dfrac{3t}{1 + t^2} = t \cdot \dfrac{3}{1 + t^2} = tx$ であるから、$x \neq 0$ より
  $$t = \frac{y}{x} \qquad \cdots \text{①}$$
  ① を $x = \dfrac{3}{1 + t^2}$ に代入して $t$ を消去すると、
  $$x = \frac{3}{1 + \dfrac{y^2}{x^2}} = \frac{3x^2}{x^2 + y^2}$$
  $x \neq 0$ より両辺を $x$ で割り、分母を払うと、
  $$x^2 + y^2 = 3x$$
  平方完成して整理すると、
  $$\left(x - \frac{3}{2}\right)^2 + y^2 = \left(\frac{3}{2}\right)^2 \qquad \cdots \text{②}$$
  > 💡 讲师批注：也可以直接由 $x^2 + y^2 = \frac{9 + 9t^2}{(1+t^2)^2} = \frac{9}{1+t^2} = 3x$ 一秒消参！但无论用哪种方法，都必须检查**是否存在无法取到的点**。

  逆に、円 ② 上の点 $(x, y)$ のうち、原点 $(0, 0)$ 以外の任意の点は $x > 0$ を満たすから、$t = \dfrac{y}{x}$ とおくと、$x^2 + y^2 = 3x$ より
  $$\frac{3}{1 + t^2} = \frac{3}{1 + \dfrac{y^2}{x^2}} = \frac{3x^2}{x^2 + y^2} = \frac{3x^2}{3x} = x, \qquad \frac{3t}{1 + t^2} = tx = y$$
  となり、すべて与えられた媒介変数表示で表される。一方、原点 $(0, 0)$ は $x = \dfrac{3}{1 + t^2} > 0$ より決してとることができない。
  したがって、求める図形は「中心 $\left(\dfrac{3}{2},\; 0\right)$、半径 $\dfrac{3}{2}$ の円から原点 $(0, 0)$ を除いた図形」である。
  > 💡 讲师批注：本题与教材 [14.4] 中的有理参数圆同源！当 $t \to \pm\infty$ 时点无限趋近于原点 $(0, 0)$，但任何有限实数 $t$ 都无法取到原点，因此必须明确写出「**ただし、原点 $(0, 0)$ を除く**」！

- **【最终答案】**
  **中心 $\left(\dfrac{3}{2},\; 0\right)$、半径 $\dfrac{3}{2}$ の円 $\left(x - \dfrac{3}{2}\right)^2 + y^2 = \dfrac{9}{4}$。ただし、原点 $(0, 0)$ を除く。**

---

#### 演習問題 12-(5)
- **【原题重现与翻译】**
  - 原题：楕円 $\dfrac{x^2}{a^2} + \dfrac{y^2}{b^2} = 1\ (0 < b < a)$ の第一象限の部分上にある点 $P$ における楕円の法線が、$x$ 軸、$y$ 軸と交わる点をそれぞれ $Q, R$ とする。このとき、$\triangle OQR$（$O$ は原点）の面積 $S$ の取りうる値の範囲を求めよ。
  - 中文：过椭圆 $\dfrac{x^2}{a^2} + \dfrac{y^2}{b^2} = 1\ (0 < b < a)$ 位于第一象限部分上的一点 $P$ 作椭圆的法线，分别交 $x$ 轴、$y$ 轴于 $Q, R$ 两点。求 $\triangle OQR$（$O$ 为原点）的面积 $S$ 的取值范围。
- **【考点定位】**
  - 椭圆的参数方程（$x = a\cos\theta,\; y = b\sin\theta$）、切线与**法线（法線）**方程、三角函数二倍角公式求最值与取值范围。
- **【图解辅助（SVG 矢量图）】**

<svg viewBox="0 0 460 280" width="460" height="280" xmlns="http://www.w3.org/2000/svg" style="background:#fafafa;border:1px solid #e0e0e0;border-radius:6px;">
  <style>
    .axis { stroke:#333; stroke-width:1.4; }
    .ell { stroke:#2980b9; stroke-width:2.2; fill:none; }
    .tan { stroke:#7f8c8d; stroke-width:1.4; stroke-dasharray:4,3; }
    .nor { stroke:#e74c3c; stroke-width:2; }
    .tri { fill:#fadbd8; opacity:0.65; }
    .txt { font: 12px sans-serif; fill:#2c3e50; }
    .lbl { font: bold 12px sans-serif; fill:#c0392b; }
  </style>
  <!-- Origin (200, 140), scale: a=2 -> 120px (60px/unit), b=1 -> 60px -->
  <!-- P at theta = pi/4: P(sqrt2, sqrt2/2) = (200+84.9, 140-42.4) = (284.9, 97.6) -->
  <!-- Normal slope = 2: passes Q(3sqrt2/4, 0) ≈ (1.06, 0) = (263.6, 140), R(0, -3sqrt2/2) ≈ (0, -2.12) = (200, 267.3)? Wait rescale to 45px/unit! -->
  <!-- Scale 45px/unit: a=2 -> rx=90, b=1 -> ry=45 -->
  <!-- Origin (210, 130) -->
  <!-- P(1.414, 0.707) = (273.6, 98.2) -->
  <!-- Q(1.061, 0) = (257.7, 130) -->
  <!-- R(0, -2.121) = (210, 225.5) -->
  <!-- Shaded triangle OQR -->
  <polygon points="210,130 257.7,130 210,225.5" class="tri"/>
  <line x1="60" y1="130" x2="390" y2="130" class="axis"/>
  <line x1="210" y1="20" x2="210" y2="260" class="axis"/>
  <polygon points="390,130 382,126 382,134" fill="#333"/>
  <polygon points="210,20 206,28 214,28" fill="#333"/>
  <text x="380" y="146" class="txt">x</text>
  <text x="218" y="30" class="txt">y</text>
  <text x="195" y="145" class="txt">O</text>
  <ellipse cx="210" cy="130" rx="90" ry="45" class="ell"/>
  <!-- Tangent at P: slope -0.5 -> from (210, 66.4) to (337.2, 130) -->
  <line x1="200" y1="61.4" x2="345" y2="133.9" class="tan"/>
  <!-- Normal at P: slope 2 -> from (295, 55.5) through P(273.6, 98.2), Q(257.7, 130), R(210, 225.5) to (198, 249.5) -->
  <line x1="295" y1="55.5" x2="198" y2="249.5" class="nor"/>
  <circle cx="273.6" cy="98.2" r="4" fill="#e74c3c"/>
  <circle cx="257.7" cy="130" r="3.5" fill="#e74c3c"/>
  <circle cx="210" cy="225.5" r="3.5" fill="#e74c3c"/>
  <text x="285" y="96" class="lbl">P(a cosθ, b sinθ)</text>
  <text x="262" y="146" class="lbl">Q</text>
  <text x="188" y="232" class="lbl">R</text>
  <text x="220" y="170" class="lbl">S</text>
  <text x="305" y="65" class="lbl">法線</text>
  <text x="330" y="118" class="txt" fill="#7f8c8d">接線</text>
  <text x="102" y="102" class="txt" fill="#2980b9">x²/a² + y²/b² = 1</text>
</svg>

- **【分步标准解答】**
  点 $P$ は楕円 $\dfrac{x^2}{a^2} + \dfrac{y^2}{b^2} = 1$ の第一象限の部分上にあるから、媒介変数 $\theta$ を用いて
  $$P(a\cos\theta,\; b\sin\theta) \qquad \left(0 < \theta < \frac{\pi}{2}\right)$$
  とおくことができる。このとき、$\cos\theta > 0,\; \sin\theta > 0$ である。
  > 💡 讲师批注：本题用 $(x_1, y_1)$ 也能做，但用参数方程 $P(a\cos\theta, b\sin\theta)$ 能直接将面积 $S$ 化为单一变量 $\sin 2\theta$ 的函数，轻松得出精确取值范围！

  点 $P$ における楕円の接線の方程式は
  $$\frac{(a\cos\theta)x}{a^2} + \frac{(b\sin\theta)y}{b^2} = 1 \iff \frac{\cos\theta}{a}x + \frac{\sin\theta}{b}y = 1$$
  $\sin\theta > 0$ より、この接線の傾きは $-\dfrac{b\cos\theta}{a\sin\theta}$ である。
  法線は点 $P$ を通り接線に垂直な直線であるから、法線の傾きは $\dfrac{a\sin\theta}{b\cos\theta}$ となり、法線の方程式は
  $$y - b\sin\theta = \frac{a\sin\theta}{b\cos\theta}(x - a\cos\theta) \qquad \cdots \text{①}$$
  > 💡 讲师批注：法线斜率与切线斜率乘积为 $-1$；因 $0 < \theta < \frac{\pi}{2}$，$\cos\theta \neq 0$ 且 $\sin\theta \neq 0$，无需担心分母为 $0$。

  1. **$x$ 軸との交点 $Q$ の $x$ 座標**：① に $y = 0$ を代入して
     $$-b\sin\theta = \frac{a\sin\theta}{b\cos\theta}(x - a\cos\theta)$$
     両辺を $\sin\theta\ (> 0)$ で割って整理すると、
     $$-\frac{b^2\cos\theta}{a} = x - a\cos\theta \implies x = a\cos\theta - \frac{b^2\cos\theta}{a} = \frac{a^2 - b^2}{a}\cos\theta$$
     よって、$Q\left(\dfrac{a^2 - b^2}{a}\cos\theta,\; 0\right)$。
     $0 < b < a$ および $\cos\theta > 0$ より、$OQ = \dfrac{a^2 - b^2}{a}\cos\theta > 0$。

  2. **$y$ 軸との交点 $R$ の $y$ 座標**：① に $x = 0$ を代入して
     $$y - b\sin\theta = \frac{a\sin\theta}{b\cos\theta}(-a\cos\theta) = -\frac{a^2}{b}\sin\theta$$
     $$y = b\sin\theta - \frac{a^2}{b}\sin\theta = -\frac{a^2 - b^2}{b}\sin\theta$$
     よって、$R\left(0,\; -\dfrac{a^2 - b^2}{b}\sin\theta\right)$。
     $0 < b < a$ および $\sin\theta > 0$ より、$y$ 座標は負であるから、$OR = \dfrac{a^2 - b^2}{b}\sin\theta > 0$。

  したがって、$\triangle OQR$ の面積 $S$ は
  $$S = \frac{1}{2} \cdot OQ \cdot OR = \frac{1}{2} \cdot \frac{a^2 - b^2}{a}\cos\theta \cdot \frac{a^2 - b^2}{b}\sin\theta$$
  $$= \frac{(a^2 - b^2)^2}{2ab}\sin\theta\cos\theta = \frac{(a^2 - b^2)^2}{4ab}\sin 2\theta$$
  > 💡 讲师批注：逆用正弦二倍角公式 $\sin\theta\cos\theta = \frac{1}{2}\sin 2\theta$，瞬间化简完毕！

  ここで、$0 < \theta < \dfrac{\pi}{2}$ より $0 < 2\theta < \pi$ であるから、
  $$0 < \sin 2\theta \le 1$$
  （等号成立は $2\theta = \dfrac{\pi}{2}$ すなわち $\theta = \dfrac{\pi}{4}$ のとき）。
  $\dfrac{(a^2 - b^2)^2}{4ab} > 0$ を掛けて、求める $S$ の取りうる値の範囲は
  $$0 < S \le \frac{(a^2 - b^2)^2}{4ab}$$
  > 💡 讲师批注：注意区间的开闭性！点 $P$ 在第一象限（不含坐标轴），故 $0 < \theta < \frac{\pi}{2}$，下界 $0$ **不可取等**（开区间），而上界在 $\theta = \frac{\pi}{4} \in \left(0, \frac{\pi}{2}\right)$ 处**可取等**（闭区间）。

- **【最终答案】**
  **$0 < S \le \dfrac{(a^2 - b^2)^2}{4ab}$**
