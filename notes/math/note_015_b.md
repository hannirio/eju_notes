# 《EJU 教材全解与备课讲义》数学 015-B（P211–P225 后半）

> **对应源文件**：`work_math/ocr_md/ocr_015_p211-225.md`（续 `note_015_a.md`，涵盖演習問題 4-(5)~(8)、演習問題 5-(1)~(4)、演習問題 6-(1)）
> **视觉核对参考图**：`work_math/ref_imgs/page_0216.jpg`–`page_0221.jpg`, `page_0225.jpg`

---

## 三、逐题深度解析（续 `note_015_a.md`）

---

### 演習問題 4（位置ベクトル・ベクトルと図形・後半）

#### 演習問題 4-(5)
- **【原题重现与翻译】**
  - 原题：$\triangle ABC$ において、$AB = 8,\; BC = 7,\; CA = 5$ とし、内心を $I$ とする。$\overrightarrow{AI}$ を $\overrightarrow{AB}, \overrightarrow{AC}$ で表せ。
  - 中文：在 $\triangle ABC$ 中，已知 $AB = 8,\; BC = 7,\; CA = 5$，设其内心为 $I$。用 $\overrightarrow{AB}, \overrightarrow{AC}$ 表示 $\overrightarrow{AI}$。
- **【考点定位】**
  - **三角形内心（内心）的位置向量求法**：两次运用角平分线性质定理（内角の二等分線と比）。
- **【图解辅助（SVG 矢量图）】**

<svg viewBox="0 0 320 195" width="100%" style="max-width:320px;display:block;margin:12px auto;" xmlns="http://www.w3.org/2000/svg">
  <!-- A(115,30), B(40,165), C(260,165) schematic -->
  <!-- D divides BC in 8:5 -> (40*5 + 260*8)/13 = (2280/13, 165) = (175.4, 165) -->
  <!-- I divides AD in 13:7 -> A*7/20 + D*13/20 = (154.3, 117.75) -->
  <polygon points="115,30 40,165 260,165" fill="#f8fafc" stroke="#1e293b" stroke-width="2"/>
  <line x1="115" y1="30" x2="175.4" y2="165" stroke="#2563eb" stroke-width="1.6" stroke-dasharray="4,3"/>
  <line x1="40" y1="165" x2="154.3" y2="117.8" stroke="#16a34a" stroke-width="1.5" stroke-dasharray="4,3"/>
  <line x1="115" y1="30" x2="154.3" y2="117.8" stroke="#dc2626" stroke-width="2.2"/>
  <circle cx="115" cy="30" r="3.5" fill="#0f172a"/>
  <circle cx="40" cy="165" r="3.5" fill="#0f172a"/>
  <circle cx="260" cy="165" r="3.5" fill="#0f172a"/>
  <circle cx="175.4" cy="165" r="3.5" fill="#2563eb"/>
  <circle cx="154.3" cy="117.8" r="4" fill="#dc2626"/>
  <text x="110" y="21" font-size="13" font-weight="bold" fill="#0f172a">A</text>
  <text x="26" y="176" font-size="13" font-weight="bold" fill="#0f172a">B</text>
  <text x="266" y="176" font-size="13" font-weight="bold" fill="#0f172a">C</text>
  <text x="171" y="183" font-size="13" font-weight="bold" fill="#2563eb">D</text>
  <text x="163" y="116" font-size="13" font-weight="bold" fill="#dc2626">I</text>
  <text x="64" y="96" font-size="12" fill="#475569">8</text>
  <text x="200" y="96" font-size="12" fill="#475569">5</text>
  <text x="108" y="182" font-size="12" fill="#475569">BC = 7</text>
</svg>

- **【分步标准解答】**
  $\angle A$ の二等分線と辺 $BC$ との交点を $D$ とする。
  角の二等分線の性質より
  $$BD : DC = AB : AC = 8 : 5$$
  したがって、点 $D$ は辺 $BC$ を $8:5$ に内分するので
  $$\overrightarrow{AD} = \frac{5\overrightarrow{AB} + 8\overrightarrow{AC}}{8 + 5} = \frac{5\overrightarrow{AB} + 8\overrightarrow{AC}}{13}$$
  また、線分 $BD$ の長さは
  $$BD = BC \cdot \frac{8}{8 + 5} = 7 \cdot \frac{8}{13} = \frac{56}{13}$$
  > 💡 讲师批注：接下来聚焦 $\triangle ABD$！因为内心 $I$ 是三条角平分线的交点，所以 $BI$ 也是 $\triangle ABD$ 中 $\angle B$ 的平分线。

  次に、$\triangle ABD$ において $BI$ は $\angle ABD$ の二等分線であるから
  $$AI : ID = BA : BD = 8 : \frac{56}{13} = 13 : 7$$
  よって、点 $I$ は線分 $AD$ を $13:7$ に内分するので
  $$\overrightarrow{AI} = \frac{13}{13 + 7}\overrightarrow{AD} = \frac{13}{20} \cdot \frac{5\overrightarrow{AB} + 8\overrightarrow{AC}}{13} = \frac{5\overrightarrow{AB} + 8\overrightarrow{AC}}{20}$$
  $$= \frac{1}{4}\overrightarrow{AB} + \frac{2}{5}\overrightarrow{AC}$$
  > 💡 讲师批注：EJU 必背内心秒杀公式（选择/填空直接验算用）：设 $BC=a, CA=b, AB=c$，则 $\overrightarrow{OI} = \dfrac{a\overrightarrow{OA} + b\overrightarrow{OB} + c\overrightarrow{OC}}{a+b+c}$。令 $O=A$ 即得 $\overrightarrow{AI} = \dfrac{b\overrightarrow{AB} + c\overrightarrow{AC}}{a+b+c} = \dfrac{5\overrightarrow{AB}+8\overrightarrow{AC}}{7+5+8} = \dfrac{1}{4}\overrightarrow{AB} + \dfrac{2}{5}\overrightarrow{AC}$！
- **【最终答案】**
  **$\overrightarrow{AI} = \dfrac{1}{4}\overrightarrow{AB} + \dfrac{2}{5}\overrightarrow{AC}$**

---

#### 演習問題 4-(6)
- **【原题重现与翻译】**
  - 原题：$\triangle ABC$ において、$AB = 4,\; AC = 5,\; BC = 6$ とし、外心を $O$ とする。$\overrightarrow{AO}$ を $\overrightarrow{AB}, \overrightarrow{AC}$ で表せ。
  - 中文：在 $\triangle ABC$ 中，已知 $AB = 4,\; AC = 5,\; BC = 6$，设其外心为 $O$。用 $\overrightarrow{AB}, \overrightarrow{AC}$ 表示 $\overrightarrow{AO}$。
- **【考点定位】**
  - **三角形外心（外心）的位置向量求法**：利用「外心到三顶点等距」或「中垂线垂直条件」转化为两个内积方程。
- **【分步标准解答】**
  $\overrightarrow{AB} = \vec{b},\; \overrightarrow{AC} = \vec{c}$ とおくと、$|\vec{b}| = 4,\; |\vec{c}| = 5$ であり、$\overrightarrow{BC} = \vec{c} - \vec{b}$ より $|\vec{c} - \vec{b}| = 6$。
  まず内積 $\vec{b}\cdot\vec{c}$ を求める。$|\vec{c} - \vec{b}|^2 = 36$ より
  $$|\vec{c}|^2 - 2\vec{b}\cdot\vec{c} + |\vec{b}|^2 = 36$$
  $$5^2 - 2\vec{b}\cdot\vec{c} + 4^2 = 36 \implies 41 - 2\vec{b}\cdot\vec{c} = 36 \implies \vec{b}\cdot\vec{c} = \frac{5}{2}$$
  $\vec{b} \neq \vec{0},\; \vec{c} \neq \vec{0},\; \vec{b} \not\parallel \vec{c}$ より、実数 $s, t$ を用いて $\overrightarrow{AO} = s\vec{b} + t\vec{c}$ とおく。
  辺 $AB, AC$ の中点をそれぞれ $M, N$ とすると、外心 $O$ は各辺の垂直二等分線の交点であるから、$\overrightarrow{MO} \perp \overrightarrow{AB}$ かつ $\overrightarrow{NO} \perp \overrightarrow{AC}$ である。
  > 💡 讲师批注：这一步等价于一个极其好用的结论：**$\overrightarrow{AO} \cdot \overrightarrow{AB} = \dfrac{1}{2}|\overrightarrow{AB}|^2$**（因为 $\overrightarrow{AO}$ 在 $\overrightarrow{AB}$ 上的投影恰好是 $AB$ 的一半！）。

  ① $\overrightarrow{MO} \cdot \overrightarrow{AB} = 0$ より、$\left(\overrightarrow{AO} - \dfrac{1}{2}\vec{b}\right)\cdot\vec{b} = 0$、すなわち $\overrightarrow{AO}\cdot\vec{b} = \dfrac{1}{2}|\vec{b}|^2$：
  $$(s\vec{b} + t\vec{c})\cdot\vec{b} = \frac{1}{2} \cdot 4^2 \implies s|\vec{b}|^2 + t(\vec{b}\cdot\vec{c}) = 8$$
  $$16s + \frac{5}{2}t = 8 \implies 32s + 5t = 16 \qquad \cdots ①$$

  ② $\overrightarrow{NO} \cdot \overrightarrow{AC} = 0$ より、$\left(\overrightarrow{AO} - \dfrac{1}{2}\vec{c}\right)\cdot\vec{c} = 0$、すなわち $\overrightarrow{AO}\cdot\vec{c} = \dfrac{1}{2}|\vec{c}|^2$：
  $$(s\vec{b} + t\vec{c})\cdot\vec{c} = \frac{1}{2} \cdot 5^2 \implies s(\vec{b}\cdot\vec{c}) + t|\vec{c}|^2 = \frac{25}{2}$$
  $$\frac{5}{2}s + 25t = \frac{25}{2} \implies s + 10t = 5 \qquad \cdots ②$$

  ① $\times 2 -$ ② より
  $$(64s + 10t) - (s + 10t) = 32 - 5 \implies 63s = 27 \implies s = \frac{27}{63} = \frac{3}{7}$$
  ② に代入して
  $$10t = 5 - \frac{3}{7} = \frac{32}{7} \implies t = \frac{16}{35}$$
  よって
  $$\overrightarrow{AO} = \frac{3}{7}\overrightarrow{AB} + \frac{16}{35}\overrightarrow{AC}$$
  > 💡 讲师批注：把 $s = \frac{3}{7}, t = \frac{16}{35}$ 代回 ① 验算：$32\cdot\frac{3}{7} + 5\cdot\frac{16}{35} = \frac{96}{7} + \frac{16}{7} = \frac{112}{7} = 16$，完全正确！
- **【最终答案】**
  **$\overrightarrow{AO} = \dfrac{3}{7}\overrightarrow{AB} + \dfrac{16}{35}\overrightarrow{AC}$**

---

#### 演習問題 4-(7)
- **【原题重现与翻译】**
  - 原题：$\triangle ABC$ の重心を $G$、外接円の中心を $O$ とするとき、次のことを示せ。
    - [1] $\overrightarrow{OA} + \overrightarrow{OB} + \overrightarrow{OC} = \overrightarrow{OH}$ である点 $H$ をとると、$H$ は $\triangle ABC$ の垂心である。
    - [2] [1] の点 $H$ に対し、3 点 $O, G, H$ は一直線上にあり $GH = 2OG$。
  - 中文：设 $\triangle ABC$ 的重心为 $G$，外接圆圆心（外心）为 $O$，证明以下结论：
    - [1] 取满足 $\overrightarrow{OA} + \overrightarrow{OB} + \overrightarrow{OC} = \overrightarrow{OH}$ 的点 $H$，则 $H$ 是 $\triangle ABC$ 的垂心；
    - [2] 对于 [1] 中的点 $H$，$O, G, H$ 三点共线，且 $GH = 2OG$。
- **【考点定位】**
  - **欧拉线定理（オイラー線）**的经典向量证明（EJU 与日本名校二次试验的殿堂级常考证明题）。
- **【图解辅助（SVG 矢量图）】**

<svg viewBox="0 0 320 205" width="100%" style="max-width:320px;display:block;margin:12px auto;" xmlns="http://www.w3.org/2000/svg">
  <!-- Circumcircle centered at O(155, 110), R=85 -->
  <circle cx="155" cy="110" r="85" fill="#f8fafc" stroke="#94a3b8" stroke-width="1.4" stroke-dasharray="4,3"/>
  <!-- A(120, 32.5) [dx=-35, dy=-77.5, r=85], B(73, 132) [dx=-82, dy=22, r=84.9], C(238, 128) [dx=83, dy=18, r=84.9] -->
  <polygon points="120,32.5 73,132 238,128" fill="none" stroke="#1e293b" stroke-width="2"/>
  <!-- G = (A+B+C)/3 = (143.7, 97.5) -->
  <!-- H = O + (A-O)+(B-O)+(C-O) = (155 -35 -82 +83, 110 -77.5 +22 +18) = (121, 72.5) -->
  <!-- Euler line O-G-H -->
  <line x1="155" y1="110" x2="121" y2="72.5" stroke="#dc2626" stroke-width="2.4"/>
  <circle cx="120" cy="32.5" r="3" fill="#0f172a"/>
  <circle cx="73" cy="132" r="3" fill="#0f172a"/>
  <circle cx="238" cy="128" r="3" fill="#0f172a"/>
  <circle cx="155" cy="110" r="4" fill="#2563eb"/>
  <circle cx="143.7" cy="97.5" r="4" fill="#16a34a"/>
  <circle cx="121" cy="72.5" r="4" fill="#dc2626"/>
  <text x="115" y="24" font-size="13" font-weight="bold" fill="#0f172a">A</text>
  <text x="58" y="138" font-size="13" font-weight="bold" fill="#0f172a">B</text>
  <text x="244" y="135" font-size="13" font-weight="bold" fill="#0f172a">C</text>
  <text x="162" y="117" font-size="13" font-weight="bold" fill="#2563eb">O (外心)</text>
  <text x="150" y="96" font-size="12" font-weight="bold" fill="#16a34a">G (重心)</text>
  <text x="128" y="72" font-size="12" font-weight="bold" fill="#dc2626">H (垂心)</text>
  <text x="160" y="186" font-size="11" text-anchor="middle" fill="#dc2626">オイラー線：OG : GH = 1 : 2</text>
</svg>

- **【分步标准解答】**
  - **[1] $H$ が垂心であることの証明**：
    外接円の半径を $R$ とすると、$|\overrightarrow{OA}| = |\overrightarrow{OB}| = |\overrightarrow{OC}| = R$ である。
    条件 $\overrightarrow{OH} = \overrightarrow{OA} + \overrightarrow{OB} + \overrightarrow{OC}$ より
    $$\overrightarrow{AH} = \overrightarrow{OH} - \overrightarrow{OA} = \overrightarrow{OB} + \overrightarrow{OC}$$
    また、$\overrightarrow{BC} = \overrightarrow{OC} - \overrightarrow{OB}$ であるから、内積 $\overrightarrow{AH}\cdot\overrightarrow{BC}$ を計算すると
    $$\overrightarrow{AH}\cdot\overrightarrow{BC} = (\overrightarrow{OB} + \overrightarrow{OC})\cdot(\overrightarrow{OC} - \overrightarrow{OB}) = |\overrightarrow{OC}|^2 - |\overrightarrow{OB}|^2 = R^2 - R^2 = 0$$
    > 💡 讲师批注：平方差公式 $(\vec{c}+\vec{b})\cdot(\vec{c}-\vec{b}) = |\vec{c}|^2 - |\vec{b}|^2$ 一行秒杀！注意严谨性：若 $A$ 与 $H$ 重合（$\triangle ABC$ 是以 $A$ 为直角的直角三角形），$\overrightarrow{AH}=\vec{0}$ 时垂直表述需稍作说明。

    したがって、$\overrightarrow{AH} \neq \vec{0}$ のとき $AH \perp BC$ である（$\overrightarrow{AH} = \vec{0}$、すなわち $H$ が $A$ に一致するときは $\overrightarrow{OB} + \overrightarrow{OC} = \vec{0}$ より $BC$ が直径となり $\angle A = 90^\circ$ なので、$A$ 自身が垂心である）。
    同様にして
    $$\overrightarrow{BH}\cdot\overrightarrow{CA} = (\overrightarrow{OC} + \overrightarrow{OA})\cdot(\overrightarrow{OA} - \overrightarrow{OC}) = |\overrightarrow{OA}|^2 - |\overrightarrow{OC}|^2 = 0$$
    $$\overrightarrow{CH}\cdot\overrightarrow{AB} = (\overrightarrow{OA} + \overrightarrow{OB})\cdot(\overrightarrow{OB} - \overrightarrow{OA}) = |\overrightarrow{OB}|^2 - |\overrightarrow{OA}|^2 = 0$$
    ゆえに、点 $H$ は $\triangle ABC$ の垂心である。（証明終）

  - **[2] $O, G, H$ が一直線上にあり $GH = 2OG$ であることの証明**：
    点 $G$ は $\triangle ABC$ の重心であるから
    $$\overrightarrow{OG} = \frac{\overrightarrow{OA} + \overrightarrow{OB} + \overrightarrow{OC}}{3}$$
    条件 $\overrightarrow{OA} + \overrightarrow{OB} + \overrightarrow{OC} = \overrightarrow{OH}$ を代入すると
    $$\overrightarrow{OG} = \frac{1}{3}\overrightarrow{OH} \iff \overrightarrow{OH} = 3\overrightarrow{OG}$$
    よって、3 点 $O, G, H$ は一直線上にある（正三角形のときは 3 点が一致する）。
    さらに
    $$\overrightarrow{GH} = \overrightarrow{OH} - \overrightarrow{OG} = 3\overrightarrow{OG} - \overrightarrow{OG} = 2\overrightarrow{OG}$$
    両辺の大きさをとって
    $$GH = |\overrightarrow{GH}| = 2|\overrightarrow{OG}| = 2OG$$
    （証明終）
- **【最终答案】**
  **[1]・[2] ともに証明済（$\overrightarrow{OH} = 3\overrightarrow{OG}$ より、外心 $O$・重心 $G$・垂心 $H$ は同一直線「オイラー線」上にあり、$OG:GH = 1:2$）**

---

#### 演習問題 4-(8)
- **【原题重现与翻译】**
  - 原题：鋭角三角形 $ABC$ の外心 $O$ から直線 $BC, CA, AB$ に下ろした垂線の足を、それぞれ $P, Q, R$ とするとき、$\overrightarrow{OP} + 2\overrightarrow{OQ} + 3\overrightarrow{OR} = \vec{0}$ が成立しているとする。
    - [1] $5\overrightarrow{OA} + 4\overrightarrow{OB} + 3\overrightarrow{OC} = \vec{0}$ が成り立つことを示せ。
    - [2] 内積 $\overrightarrow{OB}\cdot\overrightarrow{OC}$ を求めよ。
    - [3] $\angle A$ の大きさを求めよ。
  - 中文：从锐角三角形 $ABC$ 的外心 $O$ 分别向直线 $BC, CA, AB$ 作垂线，垂足分别为 $P, Q, R$，已知 $\overrightarrow{OP} + 2\overrightarrow{OQ} + 3\overrightarrow{OR} = \vec{0}$。
    - [1] 证明 $5\overrightarrow{OA} + 4\overrightarrow{OB} + 3\overrightarrow{OC} = \vec{0}$；
    - [2] 求内积 $\overrightarrow{OB}\cdot\overrightarrow{OC}$；
    - [3] 求 $\angle A$ 的大小。
- **【考点定位】**
  - 外心的几何性质（垂足即各边中点）+ 向量移项平方技巧（利用勾股数 $3^2+4^2=5^2$ 消去外接圆半径 $R$）+ 圆周角定理。
- **【分步标准解答】**
  - **[1] $5\overrightarrow{OA} + 4\overrightarrow{OB} + 3\overrightarrow{OC} = \vec{0}$ の証明**：
    外心 $O$ は各辺の垂直二等分線の交点であるから、$O$ から辺 $BC, CA, AB$ に下ろした垂線の足 $P, Q, R$ は、それぞれ辺 $BC, CA, AB$ の**中点**である。
    > 💡 讲师批注：破题第一眼！外心向各边作垂线，垂足必然是各边中点（因为 $OB=OC$ 等腰三角形三线合一）。

    したがって、中点の位置ベクトル公式より
    $$\overrightarrow{OP} = \frac{\overrightarrow{OB} + \overrightarrow{OC}}{2}, \qquad \overrightarrow{OQ} = \frac{\overrightarrow{OC} + \overrightarrow{OA}}{2}, \qquad \overrightarrow{OR} = \frac{\overrightarrow{OA} + \overrightarrow{OB}}{2}$$
    これらを条件式 $\overrightarrow{OP} + 2\overrightarrow{OQ} + 3\overrightarrow{OR} = \vec{0}$ に代入すると
    $$\frac{\overrightarrow{OB} + \overrightarrow{OC}}{2} + 2 \cdot \frac{\overrightarrow{OC} + \overrightarrow{OA}}{2} + 3 \cdot \frac{\overrightarrow{OA} + \overrightarrow{OB}}{2} = \vec{0}$$
    両辺に $2$ を掛けて整理すると
    $$(\overrightarrow{OB} + \overrightarrow{OC}) + 2(\overrightarrow{OC} + \overrightarrow{OA}) + 3(\overrightarrow{OA} + \overrightarrow{OB}) = \vec{0}$$
    $$5\overrightarrow{OA} + 4\overrightarrow{OB} + 3\overrightarrow{OC} = \vec{0} \qquad \text{（証明終）}$$

  - **[2] 内積 $\overrightarrow{OB}\cdot\overrightarrow{OC}$ を求める**：
    外接円の半径を $r$ とすると、$|\overrightarrow{OA}| = |\overrightarrow{OB}| = |\overrightarrow{OC}| = r$（$r > 0$）である。
    [1] の等式を変形して $\overrightarrow{OA}$ を孤立させる：
    $$4\overrightarrow{OB} + 3\overrightarrow{OC} = -5\overrightarrow{OA}$$
    両辺の大きさの 2 乗をとると
    $$|4\overrightarrow{OB} + 3\overrightarrow{OC}|^2 = |-5\overrightarrow{OA}|^2$$
    $$16|\overrightarrow{OB}|^2 + 24\overrightarrow{OB}\cdot\overrightarrow{OC} + 9|\overrightarrow{OC}|^2 = 25|\overrightarrow{OA}|^2$$
    > 💡 讲师批注：把要求内积的两个向量（$\overrightarrow{OB}, \overrightarrow{OC}$）留在同一侧，第三个向量移到另一侧再平方——这是 EJU 处理 $p\overrightarrow{OA}+q\overrightarrow{OB}+r\overrightarrow{OC}=\vec{0}$ 题型的**万能通法**！

    $|\overrightarrow{OA}| = |\overrightarrow{OB}| = |\overrightarrow{OC}| = r$ を代入すると
    $$16r^2 + 24\overrightarrow{OB}\cdot\overrightarrow{OC} + 9r^2 = 25r^2$$
    $$25r^2 + 24\overrightarrow{OB}\cdot\overrightarrow{OC} = 25r^2 \implies 24\overrightarrow{OB}\cdot\overrightarrow{OC} = 0$$
    よって
    $$\overrightarrow{OB}\cdot\overrightarrow{OC} = 0$$
    > 💡 讲师批注：因为 $3^2 + 4^2 = 5^2$，$r^2$ 完美抵消！所以即使题干未给出外接圆半径，依然可以精准算出内积为 $0$。

  - **[3] $\angle A$ の大きさを求める**：
    [2] より $\overrightarrow{OB}\cdot\overrightarrow{OC} = 0$ であり、$\overrightarrow{OB} \neq \vec{0},\; \overrightarrow{OC} \neq \vec{0}$ であるから
    $$\overrightarrow{OB} \perp \overrightarrow{OC} \implies \angle BOC = 90^\circ$$
    $\triangle ABC$ は**鋭角三角形**であるから、外心 $O$ は $\triangle ABC$ の内部にあり、$\angle A$ は劣弧 $BC$ に対する円周角である。
    円周角の定理より
    $$\angle A = \frac{1}{2}\angle BOC = \frac{1}{2} \cdot 90^\circ = 45^\circ$$
    > 💡 讲师批注：注意题干中「**鋭角三角形**」四个字绝非废话！若无此条件，圆周角也可能是优弧所对的 $135^\circ$（钝角三角形）。
- **【最终答案】**
  **[1] 証明済　　[2] $\overrightarrow{OB}\cdot\overrightarrow{OC} = 0$　　[3] $\angle A = 45^\circ$**（または $\dfrac{\pi}{4}$）

---

### 演習問題 5（ベクトル方程式）

#### 演習問題 5-(1)
- **【原题重现与翻译】**
  - 原题：点 $(3, -4)$ を通り、直線 $l : 2x - 3y + 6 = 0$ に平行な直線を $g$ とする。直線 $g$ の方程式を求めよ。
  - 中文：设过点 $(3, -4)$ 且平行于直线 $l : 2x - 3y + 6 = 0$ 的直线为 $g$，求直线 $g$ 的方程。
- **【考点定位】**
  - 直线的法向量方程 $\vec{n}\cdot(\vec{p} - \vec{a}) = 0$（直线 $ax+by+c=0$ 的法向量为 $\vec{n}=(a,b)$）。
- **【分步标准解答】**
  直線 $l : 2x - 3y + 6 = 0$ の法線ベクトルの 1 つは $\vec{n} = (2, -3)$ である。
  直線 $g$ は直線 $l$ に平行であるから、$\vec{n} = (2, -3)$ は直線 $g$ の法線ベクトルでもある。
  直線 $g$ 上の任意の点を $P(x, y)$、定点を $A(3, -4)$ とすると、$\overrightarrow{AP} = (x - 3,\; y + 4)$ であり、法線ベクトル方程式 $\vec{n}\cdot\overrightarrow{AP} = 0$ より
  $$2(x - 3) - 3(y + 4) = 0$$
  $$2x - 6 - 3y - 12 = 0$$
  $$2x - 3y - 18 = 0$$
  > 💡 讲师批注：代入点 $(3, -4)$ 验算：$2(3) - 3(-4) - 18 = 6 + 12 - 18 = 0$，且法向量均为 $(2, -3)$，正确！
- **【最终答案】**
  **$2x - 3y - 18 = 0$**

---

#### 演習問題 5-(2)
- **【原题重现与翻译】**
  - 原题：2 直線 $2x + y - 6 = 0,\; x + 3y - 5 = 0$ のなす鋭角を求めよ。
  - 中文：求两条直线 $2x + y - 6 = 0$ 与 $x + 3y - 5 = 0$ 所成的锐角。
- **【考点定位】**
  - 利用两直线法向量的内积求直线夹角：$\cos\theta = \dfrac{|\vec{n}_1 \cdot \vec{n}_2|}{|\vec{n}_1||\vec{n}_2|}$。
- **【分步标准解答】**
  2 直線 $2x + y - 6 = 0,\; x + 3y - 5 = 0$ の法線ベクトルをそれぞれ $\vec{n}_1 = (2, 1),\; \vec{n}_2 = (1, 3)$ とする。
  2 直線のなす鋭角を $\theta$（$0^\circ < \theta < 90^\circ$）とすると、$\theta$ は 2 つの法線ベクトル $\vec{n}_1, \vec{n}_2$ のなす角（またはその補角）に等しいので
  $$\cos\theta = \frac{|\vec{n}_1 \cdot \vec{n}_2|}{|\vec{n}_1||\vec{n}_2|}$$
  > 💡 讲师批注：求两直线夹角（**鋭角**）时，分子**务必加绝对值**，保证 $\cos\theta > 0$，从而直接得出锐角 $\theta$！

  各値を計算すると
  $$\vec{n}_1 \cdot \vec{n}_2 = 2 \cdot 1 + 1 \cdot 3 = 5$$
  $$|\vec{n}_1| = \sqrt{2^2 + 1^2} = \sqrt{5}, \qquad |\vec{n}_2| = \sqrt{1^2 + 3^2} = \sqrt{10}$$
  したがって
  $$\cos\theta = \frac{|5|}{\sqrt{5}\cdot\sqrt{10}} = \frac{5}{5\sqrt{2}} = \frac{1}{\sqrt{2}}$$
  $0^\circ < \theta < 90^\circ$ より、$\theta = 45^\circ$（$\dfrac{\pi}{4}$）。
- **【最终答案】**
  **$45^\circ$**（または $\dfrac{\pi}{4}$）

---

#### 演習問題 5-(3)
- **【原题重现与翻译】**
  - 原题：点 $A(4, 5)$ から直線 $l : x + 2y - 6 = 0$ に垂線を引き、$l$ との交点を $H$ とする。
    - [1] 点 $H$ の座標を、ベクトルを用いて求めよ。
    - [2] 線分 $AH$ の長さを求めよ。
  - 中文：从点 $A(4, 5)$ 向直线 $l : x + 2y - 6 = 0$ 作垂线，与 $l$ 的交点记为 $H$。
    - [1] 用向量法求点 $H$ 的坐标；
    - [2] 求线段 $AH$ 的长度。
  > ⚠️ **教材勘误提示**：原教材第 220 页（`page_0221.jpg`）题干仅写「点 $(4,5)$ から…」，漏印了点名 $A$，但在 [2] 中直接问「線分 $AH$ の長さ」。此处已自动补全为「点 $A(4,5)$」。
- **【考点定位】**
  - 利用直线法向量求垂足坐标 + 向量模求点到直线的距离（日本教材推导点到直线距离公式的标准向量法）。
- **【图解辅助（SVG 矢量图）】**

<svg viewBox="0 0 300 185" width="100%" style="max-width:300px;display:block;margin:12px auto;" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <marker id="arr15n" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#2563eb"/>
    </marker>
  </defs>
  <!-- Line l: x + 2y - 6 = 0. Schematic: tilt -26.5 deg -->
  <line x1="25" y1="85" x2="275" y2="160" stroke="#1e293b" stroke-width="2"/>
  <!-- H(135, 118), A(165, 38) roughly perpendicular to (250, 75) -> perp is (75, -250) -> (30, -100) -->
  <!-- Wait: vector along line = (250, 75) = 25*(10, 3). Perp = (3, -10). From H(135,118) + 8*(3,-10) = A(159, 38) -->
  <line x1="159" y1="38" x2="135" y2="118" stroke="#dc2626" stroke-width="2" stroke-dasharray="4,3"/>
  <!-- Normal vector n from H -->
  <line x1="205" y1="139" x2="220" y2="89" stroke="#2563eb" stroke-width="2" marker-end="url(#arr15n)"/>
  <!-- Right angle mark at H -->
  <polyline points="145,121 148,111 138,108" fill="none" stroke="#dc2626" stroke-width="1.3"/>
  <circle cx="159" cy="38" r="4" fill="#dc2626"/>
  <circle cx="135" cy="118" r="4" fill="#0f172a"/>
  <text x="167" y="40" font-size="13" font-weight="bold" fill="#dc2626">A(4, 5)</text>
  <text x="115" y="138" font-size="13" font-weight="bold" fill="#0f172a">H(12/5, 9/5)</text>
  <text x="225" y="92" font-size="12" font-weight="bold" fill="#2563eb">n = (1, 2)</text>
  <text x="200" y="168" font-size="12" fill="#1e293b">l : x + 2y - 6 = 0</text>
</svg>

- **【分步标准解答】**
  - **[1] 点 $H$ の座標を求める**：
    直線 $l : x + 2y - 6 = 0$ の法線ベクトルの 1 つは $\vec{n} = (1, 2)$ である。
    $AH \perp l$ より $\overrightarrow{AH} \parallel \vec{n}$（または $\overrightarrow{AH} = \vec{0}$）であるから、実数 $t$ を用いて
    $$\overrightarrow{AH} = t\vec{n} = t(1, 2) = (t, 2t)$$
    点 $H$ の座標を $(x, y)$ とすると、$\overrightarrow{AH} = (x - 4,\; y - 5)$ であるから
    $$(x - 4,\; y - 5) = (t, 2t) \implies x = 4 + t,\quad y = 5 + 2t$$
    点 $H$ は直線 $l$ 上にあるので、$x + 2y - 6 = 0$ に代入すると
    $$(4 + t) + 2(5 + 2t) - 6 = 0$$
    $$4 + t + 10 + 4t - 6 = 0 \implies 5t + 8 = 0 \implies t = -\frac{8}{5}$$
    よって、点 $H$ の座標は
    $$x = 4 - \frac{8}{5} = \frac{12}{5}, \qquad y = 5 + 2\left(-\frac{8}{5}\right) = \frac{9}{5}$$
    すなわち $H\left(\dfrac{12}{5},\; \dfrac{9}{5}\right)$。
    > 💡 讲师批注：把 $H\left(\frac{12}{5}, \frac{9}{5}\right)$ 代入直线 $l$ 验算：$\frac{12}{5} + 2\cdot\frac{9}{5} - 6 = \frac{30}{5} - 6 = 0$，无误！

  - **[2] 線分 $AH$ の長さを求める**：
    [1] より $\overrightarrow{AH} = t\vec{n} = -\dfrac{8}{5}(1, 2)$ であるから
    $$AH = |\overrightarrow{AH}| = \left|-\frac{8}{5}\right| |\vec{n}| = \frac{8}{5}\sqrt{1^2 + 2^2} = \frac{8\sqrt{5}}{5}$$
    > 💡 讲师批注：用点到直线距离公式验算：$d = \dfrac{|4 + 2\cdot 5 - 6|}{\sqrt{1^2 + 2^2}} = \dfrac{8}{\sqrt{5}} = \dfrac{8\sqrt{5}}{5}$，完美吻合！
- **【最终答案】**
  **[1] $H\left(\dfrac{12}{5},\; \dfrac{9}{5}\right)$　　[2] $AH = \dfrac{8\sqrt{5}}{5}$**

---

#### 演習問題 5-(4)
- **【原题重现与翻译】**
  - 原题：平行四辺形 $ABCD$ において、辺 $AB$ の中点を $M$、辺 $BC$ を $1:2$ に内分する点を $E$、辺 $CD$ を $3:1$ に内分する点を $F$ とする。$\overrightarrow{AB} = \vec{b},\; \overrightarrow{AD} = \vec{d}$ とするとき
    - [1] 線分 $CM$ と $FE$ の交点を $P$ とするとき、$\overrightarrow{AP}$ を $\vec{b}, \vec{d}$ で表せ。
    - [2] 直線 $AP$ と対角線 $BD$ の交点を $Q$ とするとき、$\overrightarrow{AQ}$ を $\vec{b}, \vec{d}$ で表せ。
  - 中文：在平行四边形 $ABCD$ 中，设 $M$ 为边 $AB$ 的中点，$E$ 将边 $BC$ 按 $1:2$ 内分，$F$ 将边 $CD$ 按 $3:1$ 内分，且 $\overrightarrow{AB} = \vec{b},\; \overrightarrow{AD} = \vec{d}$。
    - [1] 设线段 $CM$ 与 $FE$ 交于点 $P$，用 $\vec{b}, \vec{d}$ 表示 $\overrightarrow{AP}$；
    - [2] 设直线 $AP$ 与对角线 $BD$ 交于点 $Q$，用 $\vec{b}, \vec{d}$ 表示 $\overrightarrow{AQ}$。
- **【考点定位】**
  - 平行四边形中的直线的向量方程（共线参数表示 + 线性无关比较系数）。
- **【图解辅助（SVG 矢量图）】**

<svg viewBox="0 0 360 200" width="100%" style="max-width:360px;display:block;margin:12px auto;" xmlns="http://www.w3.org/2000/svg">
  <!-- A(40,165), B(220,165), C(310,45), D(130,45) -->
  <!-- M = (130, 165) -->
  <!-- E divides BC 1:2 -> (220*2 + 310)/3 = (250, 125) -->
  <!-- F divides CD 3:1 -> (310 + 130*3)/4 = (175, 45) -->
  <!-- P = 10/13 b + 7/13 d = (40 + 1800/13 + 630/13, 165 - 840/13) = (226.9, 100.4) -->
  <!-- Q = 10/17 b + 7/17 d = (40 + 1800/17 + 630/17, 165 - 840/17) = (182.9, 115.6) -->
  <polygon points="40,165 220,165 310,45 130,45" fill="#f8fafc" stroke="#1e293b" stroke-width="2"/>
  <line x1="310" y1="45" x2="130" y2="165" stroke="#2563eb" stroke-width="1.6"/>
  <line x1="175" y1="45" x2="250" y2="125" stroke="#2563eb" stroke-width="1.6"/>
  <line x1="220" y1="165" x2="130" y2="45" stroke="#64748b" stroke-width="1.4" stroke-dasharray="4,3"/>
  <line x1="40" y1="165" x2="226.9" y2="100.4" stroke="#dc2626" stroke-width="1.8" stroke-dasharray="5,3"/>
  <circle cx="40" cy="165" r="3.5" fill="#0f172a"/>
  <circle cx="220" cy="165" r="3.5" fill="#0f172a"/>
  <circle cx="310" cy="45" r="3.5" fill="#0f172a"/>
  <circle cx="130" cy="45" r="3.5" fill="#0f172a"/>
  <circle cx="130" cy="165" r="3.5" fill="#2563eb"/>
  <circle cx="250" cy="125" r="3.5" fill="#2563eb"/>
  <circle cx="175" cy="45" r="3.5" fill="#2563eb"/>
  <circle cx="226.9" cy="100.4" r="4" fill="#dc2626"/>
  <circle cx="182.9" cy="115.6" r="4" fill="#16a34a"/>
  <text x="24" y="176" font-size="13" font-weight="bold" fill="#0f172a">A</text>
  <text x="225" y="178" font-size="13" font-weight="bold" fill="#0f172a">B</text>
  <text x="316" y="44" font-size="13" font-weight="bold" fill="#0f172a">C</text>
  <text x="115" y="42" font-size="13" font-weight="bold" fill="#0f172a">D</text>
  <text x="125" y="182" font-size="12" font-weight="bold" fill="#2563eb">M</text>
  <text x="258" y="130" font-size="12" font-weight="bold" fill="#2563eb">E</text>
  <text x="171" y="34" font-size="12" font-weight="bold" fill="#2563eb">F</text>
  <text x="234" y="99" font-size="13" font-weight="bold" fill="#dc2626">P</text>
  <text x="178" y="106" font-size="13" font-weight="bold" fill="#16a34a">Q</text>
</svg>

- **【分步标准解答】**
  - **[1] $\overrightarrow{AP}$ を求める**：
    まず各点の位置ベクトルを $\vec{b}, \vec{d}$ で表す：
    $$\overrightarrow{AM} = \frac{1}{2}\vec{b}, \qquad \overrightarrow{AC} = \vec{b} + \vec{d}$$
    $$\overrightarrow{AE} = \overrightarrow{AB} + \frac{1}{3}\overrightarrow{BC} = \vec{b} + \frac{1}{3}\vec{d}$$
    $$\overrightarrow{AF} = \overrightarrow{AD} + \frac{1}{4}\overrightarrow{DC} = \frac{1}{4}\vec{b} + \vec{d}$$
    > 💡 讲师批注：再次核对比例方向：$E$ 内分 $BC$ 为 $1:2 \implies BE:EC = 1:2$；$F$ 内分 $CD$ 为 $3:1 \implies CF:FD = 3:1 \implies \overrightarrow{DF} = \frac{1}{4}\overrightarrow{DC} = \frac{1}{4}\vec{b}$。

    点 $P$ は線分 $CM$ 上にあるから、実数 $s$ を用いて
    $$\overrightarrow{AP} = (1 - s)\overrightarrow{AM} + s\overrightarrow{AC} = (1 - s)\cdot\frac{1}{2}\vec{b} + s(\vec{b} + \vec{d}) = \frac{1 + s}{2}\vec{b} + s\vec{d} \qquad \cdots ①$$
    また、点 $P$ は線分 $FE$ 上にあるから、実数 $t$ を用いて
    $$\overrightarrow{AP} = (1 - t)\overrightarrow{AF} + t\overrightarrow{AE} = (1 - t)\left(\frac{1}{4}\vec{b} + \vec{d}\right) + t\left(\vec{b} + \frac{1}{3}\vec{d}\right)$$
    $$= \frac{1 + 3t}{4}\vec{b} + \frac{3 - 2t}{3}\vec{d} \qquad \cdots ②$$
    $\vec{b} \neq \vec{0},\; \vec{d} \neq \vec{0},\; \vec{b} \not\parallel \vec{d}$ より、①、② の係数を比較して
    $$\begin{cases} \dfrac{1 + s}{2} = \dfrac{1 + 3t}{4} & \implies 2s - 3t = -1 \quad \cdots ③ \\ s = \dfrac{3 - 2t}{3} & \implies 3s + 2t = 3 \quad \cdots ④ \end{cases}$$
    ③ $\times 2 +$ ④ $\times 3$ より
    $$(4s - 6t) + (9s + 6t) = -2 + 9 \implies 13s = 7 \implies s = \frac{7}{13}$$
    これを ① に代入すると
    $$\frac{1 + s}{2} = \frac{1 + \frac{7}{13}}{2} = \frac{10}{13}$$
    よって
    $$\overrightarrow{AP} = \frac{10}{13}\vec{b} + \frac{7}{13}\vec{d}$$
    > 💡 讲师批注：把 $s = \frac{7}{13}$ 代入 ④ 得 $t = \frac{9}{13}$，再代入 ② 验算：$\frac{1+27/13}{4} = \frac{10}{13}$，$\frac{3-18/13}{3} = \frac{7}{13}$，两式完全一致！

  - **[2] $\overrightarrow{AQ}$ を求める**：
    点 $Q$ は直線 $AP$ 上にあるから、実数 $k$ を用いて
    $$\overrightarrow{AQ} = k\overrightarrow{AP} = \frac{10}{13}k\vec{b} + \frac{7}{13}k\vec{d}$$
    点 $Q$ は対角線 $BD$ 上にあるから、$\vec{b}, \vec{d}$ の係数の和が $1$ である：
    $$\frac{10}{13}k + \frac{7}{13}k = 1 \implies \frac{17}{13}k = 1 \implies k = \frac{13}{17}$$
    したがって
    $$\overrightarrow{AQ} = \frac{10}{17}\vec{b} + \frac{7}{17}\vec{d}$$
- **【最终答案】**
  **[1] $\overrightarrow{AP} = \dfrac{10}{13}\vec{b} + \dfrac{7}{13}\vec{d}$　　[2] $\overrightarrow{AQ} = \dfrac{10}{17}\vec{b} + \dfrac{7}{17}\vec{d}$**

---

### 演習問題 6（空間ベクトル・ベクトルの成分）

#### 演習問題 6-(1)
- **【原题重现与翻译】**
  - 原题：$\vec{a} = (-2, 0, 1),\; \vec{b} = (0, 2, 0),\; \vec{c} = (2, 1, 1)$ とし、$s, t, u$ は実数とする。
    - [1] $3\vec{a} + 4\vec{b} - \vec{c}$ を成分で表せ。また、その大きさを求めよ。
    - [2] $s\vec{a} + t\vec{b} + u\vec{c} = \vec{0}$ ならば $s = t = u = 0$ であることを示せ。
    - [3] $\vec{p} = (2, -7, 5)$ を $s\vec{a} + t\vec{b} + u\vec{c}$ の形に表せ。
  - 中文：设 $\vec{a} = (-2, 0, 1),\; \vec{b} = (0, 2, 0),\; \vec{c} = (2, 1, 1)$，$s, t, u$ 为实数。
    - [1] 用分量表示 $3\vec{a} + 4\vec{b} - \vec{c}$，并求其模长；
    - [2] 证明：若 $s\vec{a} + t\vec{b} + u\vec{c} = \vec{0}$，则 $s = t = u = 0$；
    - [3] 将 $\vec{p} = (2, -7, 5)$ 表示为 $s\vec{a} + t\vec{b} + u\vec{c}$ 的形式。
- **【考点定位】**
  - 空间向量的坐标分量运算、模长公式、三维向量的线性无关（1 次独立）判定与唯一分解。
- **【分步标准解答】**
  - **[1] $3\vec{a} + 4\vec{b} - \vec{c}$ の成分と大きさ**：
    $$3\vec{a} + 4\vec{b} - \vec{c} = 3(-2, 0, 1) + 4(0, 2, 0) - (2, 1, 1)$$
    $$= (-6, 0, 3) + (0, 8, 0) - (2, 1, 1)$$
    $$= (-6 + 0 - 2,\; 0 + 8 - 1,\; 3 + 0 - 1) = (-8, 7, 2)$$
    その大きさは
    $$|3\vec{a} + 4\vec{b} - \vec{c}| = \sqrt{(-8)^2 + 7^2 + 2^2} = \sqrt{64 + 49 + 4} = \sqrt{117} = 3\sqrt{13}$$
    > 💡 讲师批注：$\sqrt{117} = \sqrt{9 \times 13} = 3\sqrt{13}$，记得化简最简二次根式！

  - **[2] $s\vec{a} + t\vec{b} + u\vec{c} = \vec{0} \implies s = t = u = 0$ の証明**：
    左辺を成分で表すと
    $$s\vec{a} + t\vec{b} + u\vec{c} = s(-2, 0, 1) + t(0, 2, 0) + u(2, 1, 1) = (-2s + 2u,\; 2t + u,\; s + u)$$
    これが $\vec{0} = (0, 0, 0)$ に等しいから、各成分を比較して
    $$\begin{cases} -2s + 2u = 0 & \cdots ① \\ 2t + u = 0 & \cdots ② \\ s + u = 0 & \cdots ③ \end{cases}$$
    ① より $s = u$。これを ③ に代入すると $2u = 0 \implies u = 0$、よって $s = 0$。
    さらに $u = 0$ を ② に代入すると $2t = 0 \implies t = 0$。
    したがって、$s = t = u = 0$ である。（証明終）
    > 💡 讲师批注：这正是证明三个空间向量 $\vec{a}, \vec{b}, \vec{c}$ **线性无关（1 次独立 / 不共面）**的标准步骤。

  - **[3] $\vec{p} = (2, -7, 5)$ を $s\vec{a} + t\vec{b} + u\vec{c}$ の形に表す**：
    [2] の計算と同様に成分を比較すると
    $$(-2s + 2u,\; 2t + u,\; s + u) = (2, -7, 5)$$
    よって連立方程式
    $$\begin{cases} -2s + 2u = 2 & \implies -s + u = 1 \quad \cdots ④ \\ 2t + u = -7 & \cdots ⑤ \\ s + u = 5 & \cdots ⑥ \end{cases}$$
    ④ $+$ ⑥ より
    $$2u = 6 \implies u = 3$$
    ⑥ に代入して $s = 5 - 3 = 2$。
    ⑤ に代入して $2t + 3 = -7 \implies 2t = -10 \implies t = -5$。
    したがって
    $$\vec{p} = 2\vec{a} - 5\vec{b} + 3\vec{c}$$
    > 💡 讲师批注：反代验算：$2(-2,0,1) - 5(0,2,0) + 3(2,1,1) = (-4+0+6,\; 0-10+3,\; 2+0+3) = (2, -7, 5) = \vec{p}$，100% 准确！
- **【最终答案】**
  **[1] 成分：$(-8, 7, 2)$、大きさ：$3\sqrt{13}$　　[2] 証明済　　[3] $\vec{p} = 2\vec{a} - 5\vec{b} + 3\vec{c}$**
