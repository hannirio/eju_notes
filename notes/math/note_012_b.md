# 《EJU 教材全解与备课讲义》数学 012-B（P166–P180，下篇：二次曲线与直线）

> **对应源文件**：`work_math/ocr_md/ocr_012_p166-180.md`（P171–P180：放物線・楕円・双曲線・2次曲線と直線）
> **视觉核对参考图**：`work_math/ref_imgs/page_0171.jpg` – `page_0180.jpg`
> **前篇导引**：本切片的「知识点唤醒与考纲差异对比」「日文核心词汇与口语读法」及「不等式の表す領域（例题 + 演習問題 7）」请见上篇 [`note_012_a.md`](file:///Users/baohan/Desktop/EJU/notes_math/note_012_a.md)。

---

## 三、逐题深度解析（下篇：2次曲線と直線）

---

### 演習問題 8（1）（P175）

**【原题重现与翻译】**
> **日文原题**：焦点が点 $(2, 0)$、準線が直線 $x = -2$ である放物線の方程式を求めよ。また、その概形をかけ。
> **中文翻译**：求焦点为 $(2, 0)$、准线为直线 $x = -2$ 的抛物线方程，并画出其草图。

**【考点定位】** 抛物线标准方程 $y^2 = 4px$ 的基本应用。

**【图解辅助（SVG 矢量图）】**

```html
<svg viewBox="0 0 320 220" width="320" height="220" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <marker id="arr81" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#333"/>
    </marker>
  </defs>
  <!-- 原点(130,110), 1单位=20px -->
  <!-- y^2=8x: x=2->y=±4 (170,30)/(170,190), 顶点(130,110) => Q(90,110) -->
  <line x1="25" y1="110" x2="300" y2="110" stroke="#333" stroke-width="1.4" marker-end="url(#arr81)"/>
  <line x1="130" y1="210" x2="130" y2="12" stroke="#333" stroke-width="1.4" marker-end="url(#arr81)"/>
  <text x="303" y="114" font-size="13" font-style="italic" fill="#333">x</text>
  <text x="136" y="18" font-size="13" font-style="italic" fill="#333">y</text>
  <text x="116" y="124" font-size="12" fill="#333">O</text>
  <!-- 准线 x=-2 -> x=90 -->
  <line x1="90" y1="20" x2="90" y2="200" stroke="#dc2626" stroke-width="1.6" stroke-dasharray="5,3"/>
  <!-- 抛物线 y^2=8x: x=4.5->y=±6 -> (220,-10) 太高, 用 x=3.125->y=±5 -> (192.5,10)/(192.5,210), Q(67.5,110) -->
  <path d="M 192.5,10 Q 67.5,110 192.5,210" fill="none" stroke="#1d4ed8" stroke-width="2.2"/>
  <circle cx="170" cy="110" r="3.5" fill="#dc2626"/>
  <circle cx="170" cy="30" r="3" fill="#1d4ed8"/>
  <circle cx="170" cy="190" r="3" fill="#1d4ed8"/>
  <line x1="170" y1="30" x2="170" y2="190" stroke="#999" stroke-width="1" stroke-dasharray="3,3"/>
  <text x="175" y="124" font-size="12" fill="#dc2626">F(2, 0)</text>
  <text x="48" y="34" font-size="12" fill="#dc2626">x = -2</text>
  <text x="176" y="34" font-size="11" fill="#1d4ed8">(2, 4)</text>
  <text x="176" y="194" font-size="11" fill="#1d4ed8">(2, -4)</text>
  <text x="208" y="45" font-size="12" fill="#1d4ed8">y² = 8x</text>
</svg>
```

**【分步标准解答】**
1. 焦点 $(p, 0) = (2, 0)$，准线 $x = -p = -2$，故 $p = 2$。
2. 代入日本标准形 $y^2 = 4px$：
   $$y^2 = 4 \cdot 2 \cdot x = 8x$$
3. 取特征点 $(2, \pm 4)$（通径端点）辅助画图，开口向右。
   > 💡 **讲师批注**：国内学生切勿错用 $y^2=2px$ 算出 $y^2=4x$！日本标准形系数固定为 $4p$，可直接用定义验算：点 $(2,4)$ 到焦点 $(2,0)$ 距离为 $4$，到准线 $x=-2$ 距离为 $2-(-2)=4$，相等！

**【最终答案】**
**方程式：$y^2 = 8x$（概形は上図の通り）。**

---

### 演習問題 8（2）（P175）

**【原题重现与翻译】**
> **日文原题**：次の放物線の焦点と準線を求め、その概形をかけ。`[1]` $y^2 = -3x$、`[2]` $y = 2x^2$
> **中文翻译**：求下列抛物线的焦点与准线，并画出其草图。`[1]` $y^2 = -3x$、`[2]` $y = 2x^2$。

**【考点定位】** 将一般抛物线方程化为 $y^2 = 4px$ 或 $x^2 = 4py$ 的标准形。

**【图解辅助（SVG 矢量图）】**

```html
<svg viewBox="0 0 420 210" width="420" height="210" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <marker id="arr82" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#333"/>
    </marker>
  </defs>
  <!-- 左图 [1] y^2 = -3x: 原点(130,105), 1单位=30px -->
  <line x1="15" y1="105" x2="195" y2="105" stroke="#333" stroke-width="1.3" marker-end="url(#arr82)"/>
  <line x1="130" y1="195" x2="130" y2="15" stroke="#333" stroke-width="1.3" marker-end="url(#arr82)"/>
  <text x="197" y="109" font-size="12" font-style="italic">x</text>
  <text x="135" y="20" font-size="12" font-style="italic">y</text>
  <text x="134" y="118" font-size="11">O</text>
  <!-- 准线 x=3/4 -> 130+22.5=152.5 -->
  <line x1="152.5" y1="25" x2="152.5" y2="185" stroke="#dc2626" stroke-width="1.5" stroke-dasharray="4,3"/>
  <!-- 抛物线: x=-3->y=±3 -> (40,15)/(40,195), 顶点(130,105) => Q(220,105) -->
  <path d="M 40,15 Q 220,105 40,195" fill="none" stroke="#1d4ed8" stroke-width="2"/>
  <circle cx="107.5" cy="105" r="3" fill="#dc2626"/>
  <text x="72" y="122" font-size="11" fill="#dc2626">F(-3/4, 0)</text>
  <text x="156" y="42" font-size="11" fill="#dc2626">x=3/4</text>
  <text x="20" y="28" font-size="12" font-weight="bold" fill="#1d4ed8">[1] y²=-3x</text>

  <!-- 右图 [2] y = 2x^2 (x^2 = y/2): 原点(315,155), 1单位=120px? 用比例缩放: x=±0.5->y=0.5 -->
  <!-- 设原点(315,155), 1单位=80px: 焦点(0,1/8)->(315,145), 准线y=-1/8->y=165 -->
  <!-- x=±0.8 -> y=1.28 -> (251, 52.6)/(379, 52.6), 顶点(315,155) => Q(315,257.4) -->
  <line x1="225" y1="155" x2="405" y2="155" stroke="#333" stroke-width="1.3" marker-end="url(#arr82)"/>
  <line x1="315" y1="198" x2="315" y2="15" stroke="#333" stroke-width="1.3" marker-end="url(#arr82)"/>
  <text x="407" y="159" font-size="12" font-style="italic">x</text>
  <text x="320" y="20" font-size="12" font-style="italic">y</text>
  <text x="303" y="168" font-size="11">O</text>
  <line x1="240" y1="165" x2="390" y2="165" stroke="#dc2626" stroke-width="1.5" stroke-dasharray="4,3"/>
  <path d="M 251,52.6 Q 315,257.4 379,52.6" fill="none" stroke="#1d4ed8" stroke-width="2"/>
  <circle cx="315" cy="145" r="3" fill="#dc2626"/>
  <text x="322" y="143" font-size="11" fill="#dc2626">F(0, 1/8)</text>
  <text x="352" y="180" font-size="11" fill="#dc2626">y=-1/8</text>
  <text x="225" y="28" font-size="12" font-weight="bold" fill="#1d4ed8">[2] y=2x²</text>
</svg>
```

**【分步标准解答】**
- **`[1]` $y^2 = -3x$**：
  1. 改写为标准形 $y^2 = 4\left(-\dfrac{3}{4}\right)x$，得 $p = -\dfrac{3}{4}$。
  2. 故焦点为 $\left(-\dfrac{3}{4},\; 0\right)$，准线为直线 $x = \dfrac{3}{4}$，开口向左。
- **`[2]` $y = 2x^2$**：
  1. 改写为标准形 $x^2 = \dfrac{1}{2}y = 4\left(\dfrac{1}{8}\right)y$，得 $p = \dfrac{1}{8}$。
  2. 故焦点为 $\left(0,\; \dfrac{1}{8}\right)$，准线为直线 $y = -\dfrac{1}{8}$，开口向上。
  > 💡 **讲师批注**：对于初中/高一熟悉的二次函数 $y = ax^2$，可直接记忆其焦点为 $\left(0, \dfrac{1}{4a}\right)$、准线为 $y = -\dfrac{1}{4a}$。

**【最终答案】**
**`[1]` 焦点 $\left(-\dfrac{3}{4},\; 0\right)$、準線 $x = \dfrac{3}{4}$；`[2]` 焦点 $\left(0,\; \dfrac{1}{8}\right)$、準線 $y = -\dfrac{1}{8}$（概形は上図の通り）。**

---

### 演習問題 8（3）（P175）

**【原题重现与翻译】**
> **日文原题**：円 $(x-4)^2 + y^2 = 1$ と直線 $x = -3$ の両方に接する円の中心 $P$ の軌跡を求めよ。
> **中文翻译**：求与圆 $(x-4)^2 + y^2 = 1$ 和直线 $x = -3$ 都相切的圆的圆心 $P$ 的轨迹。

**【考点定位】** 抛物线定义的几何应用（**高频易错点：动圆与定圆有「外切」和「内切」两种相切情况！**）。

**【图解辅助（SVG 矢量图）】**

```html
<svg viewBox="0 0 380 250" width="380" height="250" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <marker id="arr83" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#333"/>
    </marker>
  </defs>
  <!-- 原点(160,125), 1单位=22px -->
  <!-- x=-4 -> 72; x=-3 -> 94; x=-2 -> 116; 顶点(1,0)->182; 定圆心 A(4,0)->248, r=22 -->
  <line x1="20" y1="125" x2="365" y2="125" stroke="#333" stroke-width="1.3" marker-end="url(#arr83)"/>
  <line x1="160" y1="240" x2="160" y2="12" stroke="#333" stroke-width="1.3" marker-end="url(#arr83)"/>
  <text x="367" y="129" font-size="12" font-style="italic">x</text>
  <text x="165" y="18" font-size="12" font-style="italic">y</text>
  <text x="148" y="138" font-size="11">O</text>
  <!-- 直线 x=-3 (给定直线) -->
  <line x1="94" y1="15" x2="94" y2="235" stroke="#111" stroke-width="1.8"/>
  <!-- 两条准线 x=-4 (蓝虚线), x=-2 (红虚线) -->
  <line x1="72" y1="20" x2="72" y2="230" stroke="#1d4ed8" stroke-width="1.2" stroke-dasharray="4,3"/>
  <line x1="116" y1="20" x2="116" y2="230" stroke="#dc2626" stroke-width="1.2" stroke-dasharray="4,3"/>
  <!-- 定圆 (x-4)^2+y^2=1 -->
  <circle cx="248" cy="125" r="22" fill="#e5e7eb" fill-opacity="0.5" stroke="#111" stroke-width="1.8"/>
  <circle cx="248" cy="125" r="3" fill="#111"/>
  <!-- 轨迹1 (外切): y^2 = 16x -> x=1.5625, y=±5 -> (194.4,15)/(194.4,235), 顶点(160,125) => Q(125.6,125) -->
  <!-- 用 x=2.25, y=±6 (超边界), 用 x=1.5625->(194.4, 15) 太窄, 用 x=3 -> y=±sqrt(48)=±6.93 -->
  <!-- 准确画到 y=±5 -> x=25/16=1.5625 -> (194.4,15); 为了视觉舒展，改1单位=18px? 直接取 y=±5.2 -> x=1.69 -> (197.2,10.6)/(197.2,239.4), Q(122.8,125) -->
  <path d="M 215,0 Q 105,125 215,250" fill="none" stroke="#1d4ed8" stroke-width="2.2"/>
  <!-- 轨迹2 (内切): y^2 = 12(x-1) -> 顶点(182,125); y=±5.68 -> x=1+32.3/12=3.69 -> (241.2,0)/(241.2,250), Q(122.8,125) -->
  <path d="M 241.2,0 Q 122.8,125 241.2,250" fill="none" stroke="#dc2626" stroke-width="2.2"/>
  <circle cx="160" cy="125" r="3" fill="#1d4ed8"/>
  <circle cx="182" cy="125" r="3" fill="#dc2626"/>
  <text x="234" y="142" font-size="11" fill="#111">A(4,0)</text>
  <text x="184" y="140" font-size="11" fill="#dc2626">1</text>
  <text x="38" y="34" font-size="11" fill="#1d4ed8">x=-4</text>
  <text x="82" y="246" font-size="11" fill="#111">x=-3</text>
  <text x="119" y="34" font-size="11" fill="#dc2626">x=-2</text>
  <text x="245" y="24" font-size="11" fill="#1d4ed8">外切: y²=16x</text>
  <text x="248" y="42" font-size="11" fill="#dc2626">内切: y²=12(x-1)</text>
</svg>
```

**【分步标准解答】**
1. **分析几何位置关系**：
   - 定圆圆心为 $A(4, 0)$，半径 $r_0 = 1$。圆心 $A$ 到定直线 $x = -3$ 的距离为 $4 - (-3) = 7 > 1$，故定圆完全位于直线 $x = -3$ 的右侧。
   - 设动圆圆心为 $P(x, y)$，半径为 $R$（$R > 0$）。动圆与定圆相切且与直线 $x = -3$ 相切，故动圆必位于直线 $x = -3$ 的右侧，即 $x > -3$，且半径为：
     $$R = x - (-3) = x + 3$$
2. **分两种相切情况讨论**：
   - **情况 ①：动圆与定圆外切（外接）**
     $$PA = R + 1 = (x + 3) + 1 = x + 4$$
     这意味着点 $P(x, y)$ 到定点 $A(4, 0)$ 的距离等于到定直线 $x = -4$ 的距离！
     由抛物线定义（或平方整理 $\sqrt{(x-4)^2+y^2} = x+4$），得：
     $$(x-4)^2 + y^2 = (x+4)^2 \iff y^2 = 16x$$
     此时 $x = \dfrac{y^2}{16} \ge 0 > -3$，轨迹上所有点均满足条件。
   - **情况 ②：动圆与定圆内切（内接，动圆包含定圆）**
     $$PA = R - 1 = (x + 3) - 1 = x + 2$$
     这意味着点 $P(x, y)$ 到定点 $A(4, 0)$ 的距离等于到定直线 $x = -2$ 的距离！
     两边平方整理 $\sqrt{(x-4)^2+y^2} = x+2$（注意 $x+2 > 0$）：
     $$(x-4)^2 + y^2 = (x+2)^2 \iff y^2 = 12x - 12 = 12(x-1)$$
     此时 $x = 1 + \dfrac{y^2}{12} \ge 1$，故 $R = x + 3 \ge 4 > 1$，所有点均满足内切条件。
   > 💡 **讲师批注**：本题是日本数学Ⅲ经典陷阱题！题干只说「接する（相切）」，未限定「外接（外切）」，因此必须同时考虑**动圆包住定圆的内切情况**！特值检验：取内切抛物线顶点 $P(1,0)$，半径 $R=4$，圆为 $(x-1)^2+y^2=16$，左端切 $x=-3$，右端 $(5,0)$ 恰与定圆 $(x-4)^2+y^2=1$ 内切！

**【最终答案】**
**2 つの放物線 $y^2 = 16x$ と $y^2 = 12(x-1)$。**

---

### 演習問題 8（4）（P176）

**【原题重现与翻译】**
> **日文原题**：次の楕円の長軸・短軸の長さ、焦点を求めよ。また、その概形をかけ。`[1]` $\dfrac{x^2}{16} + \dfrac{y^2}{9} = 1$、`[2]` $25x^2 + 16y^2 = 1$
> **中文翻译**：求下列椭圆的长轴长、短轴长与焦点，并画出其草图。`[1]` $\dfrac{x^2}{16} + \dfrac{y^2}{9} = 1$、`[2]` $25x^2 + 16y^2 = 1$。

**【考点定位】** 椭圆标准方程识别（区分横椭圆 $a>b$ 与竖椭圆 $b>a$）。

**【图解辅助（SVG 矢量图）】**

```html
<svg viewBox="0 0 420 210" width="420" height="210" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <marker id="arr84" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#333"/>
    </marker>
  </defs>
  <!-- 左图 [1]: 中心(105,110), a=4->72px, b=3->54px, c=sqrt(7)≈2.646->47.6px -->
  <line x1="15" y1="110" x2="198" y2="110" stroke="#333" stroke-width="1.3" marker-end="url(#arr84)"/>
  <line x1="105" y1="190" x2="105" y2="25" stroke="#333" stroke-width="1.3" marker-end="url(#arr84)"/>
  <text x="200" y="114" font-size="12" font-style="italic">x</text>
  <text x="110" y="30" font-size="12" font-style="italic">y</text>
  <ellipse cx="105" cy="110" rx="72" ry="54" fill="none" stroke="#1d4ed8" stroke-width="2"/>
  <circle cx="152.6" cy="110" r="3" fill="#dc2626"/>
  <circle cx="57.4" cy="110" r="3" fill="#dc2626"/>
  <text x="179" y="124" font-size="11">4</text>
  <text x="20" y="124" font-size="11">-4</text>
  <text x="110" y="52" font-size="11">3</text>
  <text x="110" y="175" font-size="11">-3</text>
  <text x="142" y="102" font-size="10" fill="#dc2626">√7</text>
  <text x="44" y="102" font-size="10" fill="#dc2626">-√7</text>
  <text x="18" y="22" font-size="12" font-weight="bold" fill="#1d4ed8">[1] x²/16 + y²/9 = 1</text>

  <!-- 右图 [2]: 中心(315,110), a=1/5->56px, b=1/4->70px, c=3/20->42px -->
  <line x1="230" y1="110" x2="400" y2="110" stroke="#333" stroke-width="1.3" marker-end="url(#arr84)"/>
  <line x1="315" y1="198" x2="315" y2="20" stroke="#333" stroke-width="1.3" marker-end="url(#arr84)"/>
  <text x="402" y="114" font-size="12" font-style="italic">x</text>
  <text x="320" y="25" font-size="12" font-style="italic">y</text>
  <ellipse cx="315" cy="110" rx="56" ry="70" fill="none" stroke="#1d4ed8" stroke-width="2"/>
  <circle cx="315" cy="68" r="3" fill="#dc2626"/>
  <circle cx="315" cy="152" r="3" fill="#dc2626"/>
  <text x="374" y="124" font-size="11">1/5</text>
  <text x="234" y="124" font-size="11">-1/5</text>
  <text x="321" y="38" font-size="11">1/4</text>
  <text x="321" y="191" font-size="11">-1/4</text>
  <text x="321" y="72" font-size="10" fill="#dc2626">3/20</text>
  <text x="321" y="156" font-size="10" fill="#dc2626">-3/20</text>
  <text x="230" y="22" font-size="12" font-weight="bold" fill="#1d4ed8">[2] 25x² + 16y² = 1</text>
</svg>
```

**【分步标准解答】**
- **`[1]` $\dfrac{x^2}{16} + \dfrac{y^2}{9} = 1$**：
  - $a = 4,\; b = 3$（$a > b > 0$，焦点在 $x$ 轴上）。
  - 长轴长：$2a = 8$；短轴长：$2b = 6$。
  - $c = \sqrt{a^2 - b^2} = \sqrt{16 - 9} = \sqrt{7}$，故焦点为 $(\sqrt{7}, 0),\; (-\sqrt{7}, 0)$。
- **`[2]` $25x^2 + 16y^2 = 1$**：
  - 改写为标准形：$\dfrac{x^2}{\left(\frac{1}{5}\right)^2} + \dfrac{y^2}{\left(\frac{1}{4}\right)^2} = 1$。
  - $a = \dfrac{1}{5},\; b = \dfrac{1}{4}$（注意 $\dfrac{1}{4} > \dfrac{1}{5}$，即 $b > a > 0$，**焦点在 $y$ 轴上**！）。
  - 长轴长：$2b = \dfrac{1}{2}$；短轴长：$2a = \dfrac{2}{5}$。
  - $c = \sqrt{b^2 - a^2} = \sqrt{\dfrac{1}{16} - \dfrac{1}{25}} = \sqrt{\dfrac{9}{400}} = \dfrac{3}{20}$，故焦点为 $\left(0, \dfrac{3}{20}\right),\; \left(0, -\dfrac{3}{20}\right)$。
  > 💡 **讲师批注**：`[2]` 极易看错系数大小——$25 > 16$，但倒数之后 $\frac{1}{25} < \frac{1}{16}$，所以长轴在 $y$ 轴上！

**【最终答案】**
**`[1]` 長軸の長さ $8$、短軸の長さ $6$、焦点 $(\sqrt{7}, 0),\; (-\sqrt{7}, 0)$；**
**`[2]` 長軸の長さ $\dfrac{1}{2}$、短軸の長さ $\dfrac{2}{5}$、焦点 $\left(0, \dfrac{3}{20}\right),\; \left(0, -\dfrac{3}{20}\right)$（概形は上図の通り）。**

---

### 演習問題 8（5）（P176）

**【原题重现与翻译】**
> **日文原题**：焦点 $F(3, 0),\; F'(-3, 0)$ で点 $A(-4, 0)$ を通る楕円の方程式を求めよ。
> **中文翻译**：求焦点为 $F(3, 0),\; F'(-3, 0)$ 且经过点 $A(-4, 0)$ 的椭圆方程。

**【考点定位】** 待定系数法求椭圆标准方程。

**【分步标准解答】**
1. 焦点在 $x$ 轴上且关于原点对称，故设椭圆方程为：
   $$\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1 \qquad (a > b > 0)$$
2. 椭圆过点 $A(-4, 0)$，代入方程得：
   $$\frac{(-4)^2}{a^2} + 0 = 1 \implies a^2 = 16 \quad (a = 4)$$
3. 又由焦点坐标 $(\pm 3, 0)$ 知 $c = 3$，故：
   $$b^2 = a^2 - c^2 = 16 - 9 = 7$$
4. 从而所求椭圆方程为 $\dfrac{x^2}{16} + \dfrac{y^2}{7} = 1$。
   > 💡 **讲师批注**：也可用椭圆定义验证：$AF + AF' = |{-4}-3| + |{-4}-(-3)| = 7 + 1 = 8 = 2a \Rightarrow a = 4$，完全一致！

**【最终答案】**
**$\dfrac{x^2}{16} + \dfrac{y^2}{7} = 1$**

---

### 演習問題 8（6）（P177）

> ⚠️ **教材勘误提示**：原教材第 176 页（`page_0177.jpg`）中演習問題 8 (6) 的题干存在明显复制粘贴错误，误印为「次の**楕円**の**長軸・短軸の長さ**、焦点を求めよ。また、その概形をかけ。」但下方 `[1]` $x^2 - \dfrac{y^2}{4} = 1$ 与 `[2]` $9x^2 - 25y^2 = -225$ 均为**双曲线**！正确题干应为「次の**双曲線**の**頂点・焦点・漸近線**を求めよ。また、その概形をかけ。」以下按修正后的双曲线题干完整解析。

**【原题重现与翻译（已勘误）】**
> **日文原题（修正後）**：次の双曲線の頂点、焦点、漸近線を求めよ。また、その概形をかけ。`[1]` $x^2 - \dfrac{y^2}{4} = 1$、`[2]` $9x^2 - 25y^2 = -225$
> **中文翻译**：求下列双曲线的顶点、焦点与渐近线，并画出其草图。`[1]` $x^2 - \dfrac{y^2}{4} = 1$、`[2]` $9x^2 - 25y^2 = -225$。

**【考点定位】** 双曲线标准方程（右边为 $1$ 与右边为 $-1$ 的两种形态）及渐近线作图法。

**【图解辅助（SVG 矢量图）】**

```html
<svg viewBox="0 0 420 220" width="420" height="220" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <marker id="arr86" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#333"/>
    </marker>
  </defs>
  <!-- 左图 [1]: x^2 - y^2/4 = 1, 原点(105,115), 1单位=20px, a=1->20, b=2->40, c=sqrt(5)≈2.24->44.7 -->
  <line x1="15" y1="115" x2="195" y2="115" stroke="#333" stroke-width="1.3" marker-end="url(#arr86)"/>
  <line x1="105" y1="205" x2="105" y2="25" stroke="#333" stroke-width="1.3" marker-end="url(#arr86)"/>
  <text x="197" y="119" font-size="12" font-style="italic">x</text>
  <text x="110" y="30" font-size="12" font-style="italic">y</text>
  <!-- 渐近线 y=±2x -->
  <line x1="65" y1="195" x2="145" y2="35" stroke="#999" stroke-width="1.2" stroke-dasharray="4,3"/>
  <line x1="65" y1="35" x2="145" y2="195" stroke="#999" stroke-width="1.2" stroke-dasharray="4,3"/>
  <!-- 双曲线左右支 -->
  <path d="M 150,32 Q 105,115 150,198" fill="none" stroke="#1d4ed8" stroke-width="2"/>
  <path d="M 60,32 Q 105,115 60,198" fill="none" stroke="#1d4ed8" stroke-width="2"/>
  <circle cx="125" cy="115" r="2.8" fill="#1d4ed8"/>
  <circle cx="85" cy="115" r="2.8" fill="#1d4ed8"/>
  <circle cx="149.7" cy="115" r="3" fill="#dc2626"/>
  <circle cx="60.3" cy="115" r="3" fill="#dc2626"/>
  <text x="122" y="130" font-size="10" fill="#1d4ed8">1</text>
  <text x="76" y="130" font-size="10" fill="#1d4ed8">-1</text>
  <text x="148" y="130" font-size="10" fill="#dc2626">√5</text>
  <text x="42" y="130" font-size="10" fill="#dc2626">-√5</text>
  <text x="148" y="48" font-size="10" fill="#666">y=2x</text>
  <text x="15" y="20" font-size="12" font-weight="bold" fill="#1d4ed8">[1] x² - y²/4 = 1</text>

  <!-- 右图 [2]: x^2/25 - y^2/9 = -1, 原点(315,115), 1单位=11px, a=5->55, b=3->33, c=sqrt(34)≈5.83->64 -->
  <line x1="225" y1="115" x2="405" y2="115" stroke="#333" stroke-width="1.3" marker-end="url(#arr86)"/>
  <line x1="315" y1="208" x2="315" y2="22" stroke="#333" stroke-width="1.3" marker-end="url(#arr86)"/>
  <text x="407" y="119" font-size="12" font-style="italic">x</text>
  <text x="320" y="27" font-size="12" font-style="italic">y</text>
  <!-- 渐近线 y=±(3/5)x -->
  <line x1="230" y1="166" x2="400" y2="64" stroke="#999" stroke-width="1.2" stroke-dasharray="4,3"/>
  <line x1="230" y1="64" x2="400" y2="166" stroke="#999" stroke-width="1.2" stroke-dasharray="4,3"/>
  <!-- 双曲线上下支: 顶点(315,82)与(315,148) -->
  <path d="M 240,58 Q 315,106 390,58" fill="none" stroke="#1d4ed8" stroke-width="2"/>
  <path d="M 240,172 Q 315,124 390,172" fill="none" stroke="#1d4ed8" stroke-width="2"/>
  <circle cx="315" cy="82" r="2.8" fill="#1d4ed8"/>
  <circle cx="315" cy="148" r="2.8" fill="#1d4ed8"/>
  <circle cx="315" cy="51" r="3" fill="#dc2626"/>
  <circle cx="315" cy="179" r="3" fill="#dc2626"/>
  <text x="320" y="88" font-size="10" fill="#1d4ed8">3</text>
  <text x="320" y="154" font-size="10" fill="#1d4ed8">-3</text>
  <text x="320" y="54" font-size="10" fill="#dc2626">√34</text>
  <text x="320" y="185" font-size="10" fill="#dc2626">-√34</text>
  <text x="360" y="85" font-size="10" fill="#666">y=3x/5</text>
  <text x="225" y="20" font-size="12" font-weight="bold" fill="#1d4ed8">[2] x²/25 - y²/9 = -1</text>
</svg>
```

**【分步标准解答】**
- **`[1]` $x^2 - \dfrac{y^2}{4} = 1$**：
  - 标准形 $\dfrac{x^2}{1^2} - \dfrac{y^2}{2^2} = 1$，得 $a = 1,\; b = 2$（右边为 $1$，焦点在 $x$ 轴上）。
  - 顶点：$(1, 0),\; (-1, 0)$。
  - $c = \sqrt{a^2 + b^2} = \sqrt{1 + 4} = \sqrt{5}$，故焦点为 $(\sqrt{5}, 0),\; (-\sqrt{5}, 0)$。
  - 渐近线：$\dfrac{x}{1} \pm \dfrac{y}{2} = 0 \iff y = \pm 2x$。
- **`[2]` $9x^2 - 25y^2 = -225$**：
  - 两边同除以 $225$，化为日本标准形：
    $$\frac{x^2}{25} - \frac{y^2}{9} = -1 \quad \left(\frac{x^2}{5^2} - \frac{y^2}{3^2} = -1\right)$$
  - 得 $a = 5,\; b = 3$（右边为 $-1$，焦点在 $y$ 轴上）。
  - 顶点：$(0, 3),\; (0, -3)$。
  - $c = \sqrt{a^2 + b^2} = \sqrt{25 + 9} = \sqrt{34}$，故焦点为 $(0, \sqrt{34}),\; (0, -\sqrt{34})$。
  - 渐近线：$\dfrac{x}{5} \pm \dfrac{y}{3} = 0 \iff y = \pm \dfrac{3}{5}x$。

**【最终答案】**
**`[1]` 頂点 $(\pm 1, 0)$、焦点 $(\pm\sqrt{5}, 0)$、漸近線 $y = \pm 2x$；**
**`[2]` 頂点 $(0, \pm 3)$、焦点 $(0, \pm\sqrt{34})$、漸近線 $y = \pm \dfrac{3}{5}x$（概形は上図の通り）。**

---

### 演習問題 8（7）（P177）

**【原题重现与翻译】**
> **日文原题**：次のような双曲線の方程式を求めよ。
> `[1]` 2 点 $(5, 0),\; (-5, 0)$ を焦点とし、焦点から距離の差が $8$ である。
> `[2]` 焦点が 2 点 $(0, 4),\; (0, -4)$ で、漸近線が直線 $y = \pm \dfrac{1}{\sqrt{3}}x$ である。
> **中文翻译**：求满足下列条件的双曲线方程。
> `[1]` 以两点 $(5, 0),\; (-5, 0)$ 为焦点，到两焦点距离之差为 $8$。
> `[2]` 焦点为两点 $(0, 4),\; (0, -4)$，渐近线为直线 $y = \pm \dfrac{1}{\sqrt{3}}x$。

**【考点定位】** 由几何条件（焦点、距离差、渐近线）反求双曲线标准方程。

**【分步标准解答】**
- **`[1]`**：
  1. 焦点在 $x$ 轴上，设方程为 $\dfrac{x^2}{a^2} - \dfrac{y^2}{b^2} = 1$（$a>0, b>0$）。
  2. 由距离之差为 $8$，得 $2a = 8 \implies a = 4$（$a^2 = 16$）。
  3. 由焦点 $(\pm 5, 0)$ 得 $c = 5$，利用 $c^2 = a^2 + b^2$：
     $$b^2 = c^2 - a^2 = 25 - 16 = 9$$
  4. 故所求双曲线方程为 $\dfrac{x^2}{16} - \dfrac{y^2}{9} = 1$。

- **`[2]`**：
  1. 焦点在 $y$ 轴上，设方程为 $\dfrac{x^2}{a^2} - \dfrac{y^2}{b^2} = -1$（$a>0, b>0$）。
  2. 渐近线方程为 $y = \pm \dfrac{b}{a}x$，与 $y = \pm \dfrac{1}{\sqrt{3}}x$ 对比得：
     $$\frac{b}{a} = \frac{1}{\sqrt{3}} \implies a = \sqrt{3}\,b$$
  3. 又由焦点 $(0, \pm 4)$ 得 $c = 4$，代入 $a^2 + b^2 = c^2$：
     $$(\sqrt{3}\,b)^2 + b^2 = 4^2 \iff 4b^2 = 16 \implies b^2 = 4,\quad a^2 = 3b^2 = 12$$
  4. 故所求双曲线方程为 $\dfrac{x^2}{12} - \dfrac{y^2}{4} = -1$。
  > 💡 **讲师批注**：验算 `[2]`：渐近线 $\frac{x}{\sqrt{12}} \pm \frac{y}{2} = 0 \Rightarrow y = \pm \frac{2}{2\sqrt{3}}x = \pm \frac{1}{\sqrt{3}}x$；焦点 $c = \sqrt{12+4} = 4$，完全吻合！

**【最终答案】**
**`[1]` $\dfrac{x^2}{16} - \dfrac{y^2}{9} = 1$；　`[2]` $\dfrac{x^2}{12} - \dfrac{y^2}{4} = -1$。**

---

### 演習問題 9（1）（P180）

**【原题重现与翻译】**
> **日文原题**：次の曲線と直線の共有点の個数を求めよ。ただし、$k, m$ は定数とする。
> `[1]` $x^2 + 4y^2 = 20,\; y = x + k$　　　`[2]` $4x^2 - y^2 = 4,\; y = mx$
> **中文翻译**：求下列曲线与直线的公共点个数（其中 $k, m$ 为常数）。
> `[1]` $x^2 + 4y^2 = 20,\; y = x + k$　　　`[2]` $4x^2 - y^2 = 4,\; y = mx$。

**【考点定位】** 二次曲线与直线公共点个数分类讨论（`[2]` 重点考察**二次项系数为 $0$**即与渐近线重合的特殊情形！）。

**【图解辅助（SVG 矢量图）】**

```html
<svg viewBox="0 0 420 200" width="420" height="200" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <marker id="arr91" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#333"/>
    </marker>
  </defs>
  <!-- 左图 [1]: 椭圆 x^2/20 + y^2/5 = 1, 中心(105,105), rx=67, ry=33.5 -->
  <line x1="15" y1="105" x2="195" y2="105" stroke="#333" stroke-width="1.2" marker-end="url(#arr91)"/>
  <line x1="105" y1="185" x2="105" y2="25" stroke="#333" stroke-width="1.2" marker-end="url(#arr91)"/>
  <ellipse cx="105" cy="105" rx="67" ry="33.5" fill="none" stroke="#1d4ed8" stroke-width="2"/>
  <!-- 切线 y=x+5 与 y=x-5 (斜率1) -->
  <line x1="40" y1="95" x2="130" y2="5" stroke="#dc2626" stroke-width="1.5" stroke-dasharray="4,3"/>
  <line x1="80" y1="205" x2="170" y2="115" stroke="#dc2626" stroke-width="1.5" stroke-dasharray="4,3"/>
  <line x1="55" y1="155" x2="155" y2="55" stroke="#16a34a" stroke-width="1.5"/>
  <text x="15" y="20" font-size="11" font-weight="bold" fill="#1d4ed8">[1] x²+4y²=20, y=x+k</text>
  <text x="128" y="34" font-size="10" fill="#dc2626">k=5 (1点)</text>
  <text x="148" y="160" font-size="10" fill="#dc2626">k=-5 (1点)</text>

  <!-- 右图 [2]: 双曲线 x^2 - y^2/4 = 1, y=mx -->
  <line x1="225" y1="105" x2="405" y2="105" stroke="#333" stroke-width="1.2" marker-end="url(#arr91)"/>
  <line x1="315" y1="188" x2="315" y2="25" stroke="#333" stroke-width="1.2" marker-end="url(#arr91)"/>
  <!-- 渐近线 y=±2x (m=±2) -->
  <line x1="275" y1="185" x2="355" y2="25" stroke="#dc2626" stroke-width="1.4" stroke-dasharray="4,3"/>
  <line x1="275" y1="25" x2="355" y2="185" stroke="#dc2626" stroke-width="1.4" stroke-dasharray="4,3"/>
  <!-- 双曲线 -->
  <path d="M 358,28 Q 315,105 358,182" fill="none" stroke="#1d4ed8" stroke-width="2"/>
  <path d="M 272,28 Q 315,105 272,182" fill="none" stroke="#1d4ed8" stroke-width="2"/>
  <!-- 交2点的直线 (|m|<2) -->
  <line x1="235" y1="138" x2="395" y2="72" stroke="#16a34a" stroke-width="1.6"/>
  <text x="225" y="20" font-size="11" font-weight="bold" fill="#1d4ed8">[2] 4x²-y²=4, y=mx</text>
  <text x="358" y="42" font-size="10" fill="#dc2626">m=±2 (0点)</text>
  <text x="362" y="70" font-size="10" fill="#16a34a">|m|&lt;2 (2点)</text>
</svg>
```

**【分步标准解答】**
- **`[1]` $x^2 + 4y^2 = 20,\; y = x + k$**：
  1. 将 $y = x + k$ 代入 $x^2 + 4y^2 = 20$，消去 $y$：
     $$x^2 + 4(x + k)^2 = 20 \iff 5x^2 + 8kx + 4k^2 - 20 = 0$$
  2. 设该二次方程的判别式为 $D$：
     $$\frac{D}{4} = (4k)^2 - 5(4k^2 - 20) = 16k^2 - 20k^2 + 100 = -4(k^2 - 25) = -4(k+5)(k-5)$$
  3. 按 $D$ 的符号分类：
     - $D > 0 \iff -5 < k < 5$ 时：共有点 **$2$ 個**；
     - $D = 0 \iff k = \pm 5$ 时：共有点 **$1$ 個**（相切）；
     - $D < 0 \iff k < -5,\; 5 < k$ 时：共有点 **$0$ 個**。

- **`[2]` $4x^2 - y^2 = 4,\; y = mx$**：
  1. 将 $y = mx$ 代入 $4x^2 - y^2 = 4$，消去 $y$：
     $$4x^2 - m^2 x^2 = 4 \iff (4 - m^2)x^2 = 4 \quad \cdots\text{①}$$
  2. **关键步骤：对 $x^2$ 的系数 $4 - m^2$ 分情况讨论**：
     - **① $4 - m^2 = 0$（即 $m = \pm 2$）时**：方程化为 $0 \cdot x^2 = 4$，无解 $\implies$ 共有点 **$0$ 個**（此时直线恰为双曲线的渐近线 $y = \pm 2x$）。
     - **② $4 - m^2 > 0$（即 $-2 < m < 2$）时**：$x^2 = \dfrac{4}{4 - m^2} > 0$，有两个不同实数解 $x = \pm \dfrac{2}{\sqrt{4-m^2}}$ $\implies$ 共有点 **$2$ 個**。
     - **③ $4 - m^2 < 0$（即 $m < -2,\; 2 < m$）时**：$x^2 = \dfrac{4}{4 - m^2} < 0$，无实数解 $\implies$ 共有点 **$0$ 個**。
  3. 合并 $0$ 个的情况，得最终分类结果。
  > 💡 **讲师批注**：`[2]` 千万不要盲目套判别式 $D = -4(4-m^2)(-4) = 16(4-m^2)$ 然后误判「$D=0 \Rightarrow m=\pm 2$ 时有 $1$ 个交点」！**判别式只适用于二次项系数非零的二次方程**，当 $m=\pm 2$ 时二次项消失，绝无交点！

**【最终答案】**
**`[1]` $-5 < k < 5$ のとき $2$ 個、$k = \pm 5$ のとき $1$ 個、$k < -5,\; 5 < k$ のとき $0$ 個；**
**`[2]` $-2 < m < 2$ のとき $2$ 個、$m \le -2,\; 2 \le m$ のとき $0$ 個。**

---

### 演習問題 9（2）（P180）

**【原题重现与翻译】**
> **日文原题**：直線 $y = 4x + 1$ と楕円 $4x^2 + y^2 = 4$ が交わってできる弦の中点の座標、及び長さを求めよ。
> **中文翻译**：求直线 $y = 4x + 1$ 与椭圆 $4x^2 + y^2 = 4$ 相交所得弦的中点坐标及弦长。

**【考点定位】** 韦达定理（解と係数の関係）求弦中点坐标与弦长公式 $L = \sqrt{1+p^2}\,|\beta - \alpha|$。

**【图解辅助（SVG 矢量图）】**

```html
<svg viewBox="0 0 300 240" width="300" height="240" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <marker id="arr92" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#333"/>
    </marker>
  </defs>
  <!-- 原点(150,120), 1单位=45px -->
  <!-- 椭圆 x^2 + y^2/4 = 1: rx=45, ry=90 -->
  <line x1="30" y1="120" x2="275" y2="120" stroke="#333" stroke-width="1.3" marker-end="url(#arr92)"/>
  <line x1="150" y1="230" x2="150" y2="12" stroke="#333" stroke-width="1.3" marker-end="url(#arr92)"/>
  <text x="278" y="124" font-size="12" font-style="italic">x</text>
  <text x="155" y="18" font-size="12" font-style="italic">y</text>
  <text x="137" y="134" font-size="11">O</text>
  <ellipse cx="150" cy="120" rx="45" ry="90" fill="none" stroke="#1d4ed8" stroke-width="2"/>
  <!-- 直线 y=4x+1: x=-0.8->y=-2.2 ->(114,219); x=0.35->y=2.4 ->(165.75,12) -->
  <line x1="114" y1="219" x2="165.75" y2="12" stroke="#dc2626" stroke-width="1.8"/>
  <!-- 交点: x=(-2±sqrt(19))/10 ≈ 0.236, -0.636; y ≈ 1.944, -1.544 -->
  <!-- P1(0.236, 1.944)->(160.6, 32.5); P2(-0.636, -1.544)->(121.4, 189.5) -->
  <!-- 中点 M(-0.2, 0.2)->(141, 111) -->
  <circle cx="160.6" cy="32.5" r="3" fill="#dc2626"/>
  <circle cx="121.4" cy="189.5" r="3" fill="#dc2626"/>
  <circle cx="141" cy="111" r="3.5" fill="#16a34a"/>
  <text x="198" y="134" font-size="11" fill="#1d4ed8">1</text>
  <text x="155" y="28" font-size="11" fill="#1d4ed8">2</text>
  <text x="58" y="110" font-size="11" fill="#16a34a">M(-1/5, 1/5)</text>
  <text x="172" y="42" font-size="11" fill="#dc2626">y=4x+1</text>
  <text x="198" y="65" font-size="11" fill="#1d4ed8">4x²+y²=4</text>
</svg>
```

**【分步标准解答】**
1. **联立方程消去 $y$**：
   将 $y = 4x + 1$ 代入 $4x^2 + y^2 = 4$：
   $$4x^2 + (4x + 1)^2 = 4 \iff 4x^2 + 16x^2 + 8x + 1 - 4 = 0 \iff 20x^2 + 8x - 3 = 0 \quad \cdots\text{①}$$
   判别式 $\dfrac{D}{4} = 4^2 - 20(-3) = 76 > 0$，故直线与椭圆交于不同的两点。
2. **利用根与系数的关系（解と係数の関係）**：
   设两个交点的横坐标为 $\alpha, \beta$（即方程 ① 的两实根），则：
   $$\alpha + \beta = -\frac{8}{20} = -\frac{2}{5}, \qquad \alpha\beta = -\frac{3}{20}$$
3. **求弦的中点 $M(x_M, y_M)$ 坐标**：
   - 中点横坐标：
     $$x_M = \frac{\alpha + \beta}{2} = -\frac{1}{5}$$
   - 因为中点 $M$ 在直线 $y = 4x + 1$ 上，代入得纵坐标：
     $$y_M = 4\left(-\frac{1}{5}\right) + 1 = \frac{1}{5}$$
   故中点坐标为 $\left(-\dfrac{1}{5},\; \dfrac{1}{5}\right)$。
4. **求弦长 $L$**：
   - 先求 $|\beta - \alpha|$：
     $$(\beta - \alpha)^2 = (\alpha + \beta)^2 - 4\alpha\beta = \left(-\frac{2}{5}\right)^2 - 4\left(-\frac{3}{20}\right) = \frac{4}{25} + \frac{15}{25} = \frac{19}{25}$$
     $$|\beta - \alpha| = \frac{\sqrt{19}}{5}$$
   - 代入斜率 $p = 4$ 的弦长公式 $L = \sqrt{1 + p^2}\,|\beta - \alpha|$：
     $$L = \sqrt{1 + 4^2} \cdot \frac{\sqrt{19}}{5} = \sqrt{17} \cdot \frac{\sqrt{19}}{5} = \frac{\sqrt{323}}{5}$$
   > 💡 **讲师批注**：切记**不要硬解求根公式**算两个交点坐标再套两点距离公式，那样计算量爆炸且极易算错！用韦达定理求中点与弦长只需 4 行即可稳准快拿下。另注：$17 \times 19 = (18-1)(18+1) = 324 - 1 = 323$，平方差口算秒验！

**【最终答案】**
**中点の座標：$\left(-\dfrac{1}{5},\; \dfrac{1}{5}\right)$、弦の長さ：$\dfrac{\sqrt{323}}{5}$。**
