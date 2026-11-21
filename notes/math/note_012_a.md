# 《EJU 教材全解与备课讲义》数学 012-A（P166–P180，上篇：知识梳理与不等式区域）

> **对应源文件**：`work_math/ocr_md/ocr_012_p166-180.md`（第七章《図形と方程式》之「不等式の表す領域」、以及《式と曲線（数学Ⅲ）》之「放物線」「楕円」「双曲線」「2次曲線と直線」）
> **视觉核对参考图**：`work_math/ref_imgs/page_0166.jpg` – `page_0180.jpg`（全 15 页均已完成逐字逐符号视觉核对）
> **分册说明**：本切片涵盖「不等式区域」与「二次曲线（圆锥曲线）」两大核心板块，题量较大（1 道例题 + 15 道大题 / 25 道独立小题）。为确保每道题推导详尽无跳步、SVG 图解完整清晰，拆分为 **上篇 `note_012_a.md`**（第一、二大板块全集 + 不等式区域全部例题与演習問題 7）与 **下篇 `note_012_b.md`**（演習問題 8 与演習問題 9 全部解析）。

---

## 一、国内高中基础知识点唤醒与 EJU 考纲差异对比

本切片横跨日本高中 **数学Ⅱ（図形と方程式：不等式の表す領域）** 与 **数学Ⅲ（式と曲線：2次曲線と直線）** 两大模块，是 EJU 理系数学**必考高频大题区**。

### 1.1 不等式所表示的平面区域（不等式の表す領域）

1. **曲线/直线与区域（[7.1]）**：
   - $y > f(x)$：曲线 $y = f(x)$ 的**上方部分**（不含边界线，作图时用虚线或文字注明「境界線を含まない」）。
   - $y < f(x)$：曲线 $y = f(x)$ 的**下方部分**。
   - 含等号（$\ge, \le$）时**包含边界线**（境界線を含む）。
   - 一般地，$f(x, y) > 0$ 称为 $f(x, y)$ 的**正区域（正領域）**，$f(x, y) < 0$ 称为**负区域（負領域）**。
2. **圆与区域（[7.2]）**：
   - 圆 $C: (x-a)^2 + (y-b)^2 = r^2$。
   - $(x-a)^2 + (y-b)^2 < r^2$ 表示圆 $C$ 的**内部**；$(x-a)^2 + (y-b)^2 > r^2$ 表示圆 $C$ 的**外部**。
3. **联立不等式与乘积型不等式（[7.3]）**：
   - 联立不等式表示各不等式区域的**公共部分（交集）**。
   - 乘积型 $A(x,y) \cdot B(x,y) > 0 \iff \{A>0 \text{ 且 } B>0\} \text{ 或 } \{A<0 \text{ 且 } B<0\}$（棋盘式交替涂色，过一条边界线变一次号）。
4. **区域与最值（线性规划思想，[7.4]）**：
   - 求目标式 $f(x, y)$ 在区域 $D$ 上的最值：令 $f(x, y) = k$，将 $k$ 转化为**直线截距、圆的半径平方、或两点斜率**等几何量，研究曲线 $f(x, y) = k$ 与区域 $D$ **有公共点（共有点をもつ）** 时 $k$ 的取值范围。
5. **区域与命题证明（[7.5]）**：
   - 设条件 $p, q$ 对应的点集（区域）为 $P, Q$，则：
     $$[p \Rightarrow q \text{ 为真}] \iff P \subset Q$$
   > ⚠️ **教材勘误提示**：原教材第 165 页（`page_0166.jpg`）中 `[7.5]` 的小节标题误印为「領域と最大・最小」，其正文实际讲解的是利用集合包含关系证明命题，正确标题应为「**領域と命題**」。

### 1.2 二次曲线（2次曲線：放物線・楕円・双曲線）标准形汇总

| 曲线类型 | 标准方程 | 焦点坐标 | 顶点 / 中心 / 准线 / 渐近线 | 对称性 | 几何定义（轨迹） |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **抛物线（$x$ 轴为轴）** | $y^2 = 4px\;(p \neq 0)$ | $(p, 0)$ | 顶点 $(0,0)$；准线 $x = -p$；轴：$x$ 轴 | 关于 $x$ 轴对称 | 到焦点与准线距离相等 |
| **抛物线（$y$ 轴为轴）** | $x^2 = 4py\;(p \neq 0)$ | $(0, p)$ | 顶点 $(0,0)$；准线 $y = -p$；轴：$y$ 轴 | 关于 $y$ 轴对称 | 到焦点与准线距离相等 |
| **椭圆（焦点在 $x$ 轴）** | $\dfrac{x^2}{a^2} + \dfrac{y^2}{b^2} = 1\;(a>b>0)$ | $(\pm\sqrt{a^2-b^2}, 0)$ | 中心 $(0,0)$；长轴長 $2a$，短轴長 $2b$ | $x$ 轴、$y$ 轴、原点对称 | 到两焦点距离之**和**为定值 $2a$ |
| **椭圆（焦点在 $y$ 轴）** | $\dfrac{x^2}{a^2} + \dfrac{y^2}{b^2} = 1\;(b>a>0)$ | $(0, \pm\sqrt{b^2-a^2})$ | 中心 $(0,0)$；长轴長 $2b$，短轴長 $2a$ | $x$ 轴、$y$ 轴、原点对称 | 到两焦点距离之**和**为定值 $2b$ |
| **双曲线（焦点在 $x$ 轴）** | $\dfrac{x^2}{a^2} - \dfrac{y^2}{b^2} = 1\;(a,b>0)$ | $(\pm\sqrt{a^2+b^2}, 0)$ | 中心 $(0,0)$；顶点 $(\pm a, 0)$；渐近线 $\dfrac{x}{a} \pm \dfrac{y}{b} = 0$ | $x$ 轴、$y$ 轴、原点对称 | 到两焦点距离之**差**的绝对值为定值 $2a$ |
| **双曲线（焦点在 $y$ 轴）** | $\dfrac{x^2}{a^2} - \dfrac{y^2}{b^2} = -1\;(a,b>0)$ | $(0, \pm\sqrt{a^2+b^2})$ | 中心 $(0,0)$；顶点 $(0, \pm b)$；渐近线 $\dfrac{x}{a} \pm \dfrac{y}{b} = 0$ | $x$ 轴、$y$ 轴、原点对称 | 到两焦点距离之**差**的绝对值为定值 $2b$ |

> ⚠️ **教材勘误提示**：原教材第 173 页（`page_0174.jpg`）的《放物線、楕円、双曲線 全部まとめ》汇总表中存在 **4 处明显印刷错误**，授课时务必提醒学生更正：
> 1. 抛物线 $x^2 = 4py$ 一行：准线误印为 `x = -p`，正确应为 **$y = -p$**。
> 2. 椭圆 $b > a > 0$ 一行：焦点坐标误印为 $(0, \pm\sqrt{a^2-b^2})$，正确应为 **$(0, \pm\sqrt{b^2-a^2})$**。
> 3. 双曲线（焦点在 $y$ 轴）一行：方程误印为 $\dfrac{x^2}{a^2} + \dfrac{y^2}{b^2} = -1$，正确应为 **$\dfrac{x^2}{a^2} - \dfrac{y^2}{b^2} = -1$**。
> 4. 双曲线两行的「曲線の点」列：均误印为「2つの焦点までの距離の**和**が $2a$（$2b$）」，正确应为「距離の**差**が $2a$（$2b$）」。

### 1.3 二次曲线的平移、与直线的位置关系及弦长公式（[11.1]–[11.3]）

1. **曲线平移**：曲线 $F(x, y) = 0$ 沿 $x$ 轴方向平移 $p$、沿 $y$ 轴方向平移 $q$，所得方程为 $F(x-p, y-q) = 0$（口诀：**左加右减、下加上减**）。
2. **与直线的公共点**：联立消去一个变量后，需**先判断最高次项系数是否为 $0$**：
   - 若降为**一次方程**（如直线平行于抛物线对称轴，或平行于双曲线渐近线）：仅有 $1$ 个交点（**交点而非切点**）或 $0$ 个交点。
   - 若为**二次方程**：由判别式 $D$ 判定，$D>0$（$2$ 个交点）、$D=0$（$1$ 个**切点**）、$D<0$（无公共点）。
   > ⚠️ **教材勘误提示**：原教材第 177 页（`page_0178.jpg`）中 `[11.3][1]` ② 将 $D=0$ 笼统写作「1点で交わる」，更严谨的表达应为「**1点で接する（相切）**」（教材在下一页的 `[11.3] 解説` 中已作补充说明）。
3. **弦长公式**：直线 $y = px + q$ 与二次曲线联立消去 $y$ 得 $ax^2 + bx + c = 0$（$a \neq 0, D = b^2 - 4ac > 0$），两交点横坐标 $\alpha, \beta$，则弦长为：
   $$L = \sqrt{1+p^2}\,|\beta - \alpha| = \frac{\sqrt{(1+p^2)(b^2-4ac)}}{|a|}$$

### 1.4 国内高中 vs. 日本 EJU 考纲差异与符号习惯

| 对比维度 | 国内高中习惯 | 日本 EJU 习惯 | 备课/应试提醒 |
| :--- | :--- | :--- | :--- |
| **抛物线标准式** | $y^2 = 2px$（焦点 $\left(\frac{p}{2}, 0\right)$，准线 $x = -\frac{p}{2}$） | **$y^2 = 4px$**（焦点 $(p, 0)$，准线 $x = -p$） | **最高频致命坑点！** 国内学生极易把 $4p$ 当 $2p$ 算错 $2$ 倍，务必记住日本教材系数是 $4p$！ |
| **椭圆焦点在 $y$ 轴的标准式** | $\dfrac{y^2}{a^2} + \dfrac{x^2}{b^2} = 1\;(a>b>0)$（$a$ 始终为半长轴） | **$\dfrac{x^2}{a^2} + \dfrac{y^2}{b^2} = 1\;(b>a>0)$**（$a$ 始终在 $x$ 下方，$b$ 在 $y$ 下方） | 日本习惯固定 $x^2$ 下为 $a^2$、$y^2$ 下为 $b^2$，通过比较 $a, b$ 大小定焦点轴，此时 $c = \sqrt{b^2-a^2}$ |
| **双曲线焦点在 $y$ 轴的标准式** | $\dfrac{y^2}{a^2} - \dfrac{x^2}{b^2} = 1$ | **$\dfrac{x^2}{a^2} - \dfrac{y^2}{b^2} = -1$** | 日本习惯右边写 $-1$，渐近线统一为 $\dfrac{x}{a} \pm \dfrac{y}{b} = 0$（即 $y = \pm \dfrac{b}{a}x$），不易搞混斜率！ |
| **离心率 $e$ 与第二定义** | 高考核心高频考点 | EJU 考纲基本**不考**离心率直接计算（偶在极坐标中出现） | 重点放在标准方程、定义轨迹、平移与直线联立判别式 |
| **区域边界表达** | 实线含边界、虚线不含边界 | 日本作图除虚实线外，**必须用文字注明**「境界線を含む / 境界線を含まない」 | 解答题（国公立二次試験）不写边界说明会扣分 |

---

## 二、日文核心词汇与公式假名注音

### 2.1 本切片日文核心词汇

- 領域（りょういき / ryouiki） — 区域（不等式所表示的平面区域）
- 正領域（せいりょういき / seiryouiki） — 正区域（$f(x,y) > 0$ 所表示的区域）
- 負領域（ふりょういき / furyouiki） — 负区域（$f(x,y) < 0$ 所表示的区域）
- 境界線（きょうかいせん / kyoukaisen） — 边界线（区域的边界曲线或直线）
- 斜線部分（しゃせんぶぶん / shasen bubun） — 阴影部分（斜线填充区域）
- 内部（ないぶ / naibu） — 内部（圆或封闭图形的内部）
- 外部（がいぶ / gaibu） — 外部（圆或封闭图形的外部）
- 線形計画法（せんけいけいかくほう / senkei keikakuhou） — 线性规划法
- 軌跡（きせき / kiseki） — 轨迹
- 2次曲線（にじきょくせん / niji kyokusen） — 二次曲线（圆锥曲线）
- 焦点（しょうてん / shouten） — 焦点
- 準線（じゅんせん / junsen） — 准线
- 標準形（ひょうじゅんけい / hyoujunkei） — 标准形、标准方程
- 楕円（だえん / daen） — 椭圆
- 長軸（ちょうじく / choujiku） — 长轴
- 短軸（たんじく / tanjiku） — 短轴
- 双曲線（そうきょくせん / soukyokusen） — 双曲线
- 主軸（しゅじく / shujiku） — 主轴（过双曲线两焦点的直线）
- 概形（がいけい / gaikei） — 草图、大致图形
- 図示する（ずしする / zushi suru） — 画图表示、图示

### 2.2 核心公式的日本课堂口语读法

1. **抛物线标准方程** $y^2 = 4px$
   - 课堂读法：**ワイのにじょう イコール よんピーエックス**
   - 备注：焦点 $(p, 0)$ 读作 **しょうてん かっこ ピー カンマ ゼロ**，准线 $x = -p$ 读作 **じゅんせん エックス イコール マイナス ピー**。
2. **椭圆标准方程** $\dfrac{x^2}{a^2} + \dfrac{y^2}{b^2} = 1$
   - 课堂读法：**エーのにじょうぶんの エックスのにじょう たす ビーのにじょうぶんの ワイのにじょう イコール いち**
3. **双曲线标准方程与渐近线** $\dfrac{x^2}{a^2} - \dfrac{y^2}{b^2} = 1,\; \dfrac{x}{a} \pm \dfrac{y}{b} = 0$
   - 课堂读法：**エーのにじょうぶんの エックスのにじょう ひく ビーのにじょうぶんの ワイのにじょう イコール いち**；渐近线读作 **ぜんきんせんは エーぶんのエックス プラスマイナス ビーぶんのワイ イコール ゼロ**。
4. **区域边界标准结束语**
   - 包含边界：**境界線を含む（きょうかいせんをふくむ / kyoukaisen o fukumu）**
   - 不含边界：**境界線を含まない（きょうかいせんをふくまない / kyoukaisen o fukumanai）**

---

## 三、逐题深度解析（上篇：不等式の表す領域）

---

### 例題（P167）

**【原题重现与翻译】**
> **日文原题**：連立不等式 $-2 \leqq 2x+y \leqq 2,\; -2 \leqq 2x-y \leqq 2$ の表す領域 $D$ における $x+y$ の最大値、最小値を求めよ。
> **中文翻译**：求在联立不等式 $-2 \le 2x+y \le 2,\; -2 \le 2x-y \le 2$ 所表示的区域 $D$ 上，$x+y$ 的最大值与最小值。

**【考点定位】**
二元一次不等式组区域作图 + 线性规划（利用直线斜率与 $y$ 截距求最值）。

**【图解辅助（SVG 矢量图）】**

```html
<svg viewBox="0 0 360 280" width="360" height="280" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <marker id="arr1" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#333"/>
    </marker>
    <pattern id="hatch1" width="8" height="8" patternTransform="rotate(45)" patternUnits="userSpaceOnUse">
      <line x1="0" y1="0" x2="0" y2="8" stroke="#2563eb" stroke-width="1.2" opacity="0.45"/>
    </pattern>
  </defs>
  <!-- 坐标轴: 原点(180,140), 1单位=45px -->
  <line x1="30" y1="140" x2="335" y2="140" stroke="#333" stroke-width="1.4" marker-end="url(#arr1)"/>
  <line x1="180" y1="265" x2="180" y2="18" stroke="#333" stroke-width="1.4" marker-end="url(#arr1)"/>
  <text x="338" y="144" font-size="13" font-style="italic" fill="#333">x</text>
  <text x="186" y="22" font-size="13" font-style="italic" fill="#333">y</text>
  <text x="166" y="154" font-size="12" fill="#333">O</text>
  <!-- 区域 D: 顶点 (1,0)->(225,140), (0,2)->(180,50), (-1,0)->(135,140), (0,-2)->(180,230) -->
  <polygon points="225,140 180,50 135,140 180,230" fill="url(#hatch1)" stroke="#1d4ed8" stroke-width="2"/>
  <!-- 边界延长线 -->
  <line x1="160" y1="10" x2="245" y2="180" stroke="#1d4ed8" stroke-width="1" stroke-dasharray="3,3"/>
  <line x1="115" y1="100" x2="200" y2="270" stroke="#1d4ed8" stroke-width="1" stroke-dasharray="3,3"/>
  <!-- 目标直线 x+y=k (斜率-1) -->
  <!-- x+y=2 过(0,2)->(180,50) 和 (2,0)->(270,140) -->
  <line x1="115" y1="-15" x2="295" y2="165" stroke="#dc2626" stroke-width="1.8" stroke-dasharray="6,3"/>
  <!-- x+y=-2 过(0,-2)->(180,230) 和 (-2,0)->(90,140) -->
  <line x1="65" y1="115" x2="245" y2="295" stroke="#dc2626" stroke-width="1.8" stroke-dasharray="6,3"/>
  <!-- 顶点标记 -->
  <circle cx="180" cy="50" r="3.5" fill="#dc2626"/>
  <circle cx="180" cy="230" r="3.5" fill="#dc2626"/>
  <circle cx="225" cy="140" r="3" fill="#1d4ed8"/>
  <circle cx="135" cy="140" r="3" fill="#1d4ed8"/>
  <!-- 标注 -->
  <text x="188" y="48" font-size="12" fill="#dc2626">(0, 2) 最大</text>
  <text x="188" y="242" font-size="12" fill="#dc2626">(0, -2) 最小</text>
  <text x="228" y="133" font-size="12" fill="#1d4ed8">1</text>
  <text x="118" y="133" font-size="12" fill="#1d4ed8">-1</text>
  <text x="187" y="132" font-size="13" font-weight="bold" fill="#1d4ed8">D</text>
  <text x="262" y="120" font-size="12" fill="#dc2626">x+y=2</text>
  <text x="48" y="108" font-size="12" fill="#dc2626">x+y=-2</text>
</svg>
```

**【分步标准解答】**

1. **整理不等式组并求顶点坐标**：
   - $-2 \le 2x+y \le 2 \iff -2x-2 \le y \le -2x+2$（斜率为 $-2$ 的两平行直线之间）。
   - $-2 \le 2x-y \le 2 \iff 2x-2 \le y \le 2x+2$（斜率为 $2$ 的两平行直线之间）。
   - 联立四条边界线，求得菱形区域 $D$ 的四个顶点为 $(1, 0),\; (0, 2),\; (-1, 0),\; (0, -2)$（含边界线）。
   > 💡 **讲师批注**：判断目标直线过哪个顶点取最值，**核心是比较目标直线与边界线的斜率**，绝不能凭草图目测乱猜！

2. **设目标函数并利用斜率比较**：
   - 令 $x + y = k$，变形为 $y = -x + k$。这是斜率为 $-1$、$y$ 截距为 $k$ 的直线。
   - 比较斜率：边界线斜率为 $-2$ 与 $2$，而目标直线斜率 $-1$ 满足：
     $$-2 < -1 < 2$$
   - 当直线 $y = -x + k$ 平行移动且与区域 $D$ 有公共点时：
     - 经过最上方顶点 $(0, 2)$ 时，$y$ 截距 $k$ 最大：$k = 0 + 2 = 2$。
     - 经过最下方顶点 $(0, -2)$ 时，$y$ 截距 $k$ 最小：$k = 0 + (-2) = -2$。
   > 💡 **讲师批注**：验算四顶点处 $x+y$ 的值：$(1,0)\to 1$，$(0,2)\to 2$，$(-1,0)\to -1$，$(0,-2)\to -2$，确实在 $(0,2)$ 取最大、$(0,-2)$ 取最小。

**【最终答案】**
**$x = 0,\; y = 2$ のとき最大値 $2$；$x = 0,\; y = -2$ のとき最小値 $-2$。**

---

### 演習問題 7（1）次の不等式の表す領域を図示せよ。（P168）

#### [1] $y \ge x^2 - 3x + 2$

**【原题重现与翻译】**
> **日文原题**：次の不等式の表す領域を図示せよ。`[1]` $y \ge x^2 - 3x + 2$
> **中文翻译**：画出下列不等式所表示的平面区域：`[1]` $y \ge x^2 - 3x + 2$。

**【考点定位】** 抛物线与平面区域（$y \ge f(x)$ 表示曲线上方含边界）。

**【图解辅助（SVG 矢量图）】**

```html
<svg viewBox="0 0 320 240" width="320" height="240" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <marker id="arr711" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#333"/>
    </marker>
    <pattern id="h711" width="7" height="7" patternTransform="rotate(45)" patternUnits="userSpaceOnUse">
      <line x1="0" y1="0" x2="0" y2="7" stroke="#2563eb" stroke-width="1.2" opacity="0.45"/>
    </pattern>
  </defs>
  <!-- 原点(90,170), 1单位=50px -->
  <!-- 顶点(1.5, -0.25) -> (165, 182.5), x=0 -> (90, 70), x=3 -> (240, 70), x=1 -> (140,170), x=2 -> (190,170) -->
  <!-- 抛物线内部填充: 用二次贝塞尔曲线 Q 控制点 (165, 295) 可精确拟合过(90,70),(165,182.5),(240,70) -->
  <path d="M 75,20 Q 165,345 255,20 Z" fill="url(#h711)"/>
  <line x1="25" y1="170" x2="300" y2="170" stroke="#333" stroke-width="1.4" marker-end="url(#arr711)"/>
  <line x1="90" y1="225" x2="90" y2="15" stroke="#333" stroke-width="1.4" marker-end="url(#arr711)"/>
  <text x="303" y="174" font-size="13" font-style="italic" fill="#333">x</text>
  <text x="96" y="20" font-size="13" font-style="italic" fill="#333">y</text>
  <text x="76" y="184" font-size="12" fill="#333">O</text>
  <path d="M 75,20 Q 165,345 255,20" fill="none" stroke="#1d4ed8" stroke-width="2.2"/>
  <circle cx="140" cy="170" r="3" fill="#1d4ed8"/>
  <circle cx="190" cy="170" r="3" fill="#1d4ed8"/>
  <circle cx="90" cy="70" r="3" fill="#1d4ed8"/>
  <circle cx="165" cy="182.5" r="3" fill="#dc2626"/>
  <text x="132" y="162" font-size="12" fill="#333">1</text>
  <text x="192" y="162" font-size="12" fill="#333">2</text>
  <text x="76" y="74" font-size="12" fill="#333">2</text>
  <text x="148" y="202" font-size="11" fill="#dc2626">(3/2, -1/4)</text>
  <text x="198" y="45" font-size="12" fill="#1d4ed8">y = x²-3x+2</text>
</svg>
```

**【分步标准解答】**
1. 边界线为抛物线 $y = x^2 - 3x + 2$。
2. 因式分解与配方以确定关键点：
   $$y = (x-1)(x-2) = \left(x - \frac{3}{2}\right)^2 - \frac{1}{4}$$
   - 顶点：$\left(\dfrac{3}{2},\; -\dfrac{1}{4}\right)$；与 $x$ 轴交点：$(1, 0),\; (2, 0)$；与 $y$ 轴交点：$(0, 2)$。
3. 由于不等号为 $\ge$，所求区域为该抛物线的**上方部分**，且**包含边界线**。
   > 💡 **讲师批注**：作抛物线区域图时，务必标出**顶点、与坐标轴交点**，并注意 $y \ge f(x)$ 是抛物线开口“内部”（即上方）。

**【最终答案】**
**放物線 $y = x^2 - 3x + 2$ の上側の部分（図の斜線部分、境界線を含む）。**

---

#### [2] $(x-2)^2 + y^2 \ge 4$

**【原题重现与翻译】**
> **日文原题**：`[2]` $(x-2)^2 + y^2 \ge 4$
> **中文翻译**：画出不等式 $(x-2)^2 + y^2 \ge 4$ 所表示的平面区域。

**【考点定位】** 圆的外部区域（含边界）。

**【图解辅助（SVG 矢量图）】**

```html
<svg viewBox="0 0 320 220" width="320" height="220" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <marker id="arr712" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#333"/>
    </marker>
    <pattern id="h712" width="8" height="8" patternTransform="rotate(45)" patternUnits="userSpaceOnUse">
      <line x1="0" y1="0" x2="0" y2="8" stroke="#2563eb" stroke-width="1.2" opacity="0.4"/>
    </pattern>
    <mask id="outCircle712">
      <rect x="20" y="15" width="280" height="190" fill="white"/>
      <circle cx="170" cy="110" r="60" fill="black"/>
    </mask>
  </defs>
  <!-- 外部斜线填充 -->
  <rect x="20" y="15" width="280" height="190" fill="url(#h712)" mask="url(#outCircle712)"/>
  <!-- 原点(110,110), 1单位=30px, 圆心(2,0)->(170,110), r=2->60px -->
  <line x1="20" y1="110" x2="305" y2="110" stroke="#333" stroke-width="1.4" marker-end="url(#arr712)"/>
  <line x1="110" y1="210" x2="110" y2="12" stroke="#333" stroke-width="1.4" marker-end="url(#arr712)"/>
  <text x="307" y="114" font-size="13" font-style="italic" fill="#333">x</text>
  <text x="116" y="18" font-size="13" font-style="italic" fill="#333">y</text>
  <text x="96" y="124" font-size="12" fill="#333">O</text>
  <circle cx="170" cy="110" r="60" fill="none" stroke="#1d4ed8" stroke-width="2.2"/>
  <circle cx="170" cy="110" r="3" fill="#dc2626"/>
  <text x="166" y="126" font-size="12" fill="#dc2626">2</text>
  <text x="234" y="124" font-size="12" fill="#333">4</text>
  <text x="180" y="42" font-size="12" fill="#1d4ed8">(x-2)²+y²=4</text>
</svg>
```

**【分步标准解答】**
1. 边界线为圆 $(x-2)^2 + y^2 = 2^2$，其圆心为 $(2, 0)$，半径为 $2$（与 $y$ 轴相切于原点 $O$，过点 $(4, 0)$）。
2. 由于不等号为 $\ge$，所求区域为该圆的**外部**，且**包含圆周（边界线）**。

**【最终答案】**
**中心 $(2, 0)$、半径 $2$ の円の外部（図の斜線部分、境界線を含む）。**

---

#### [3] $|x + 2y| \le 6$

**【原题重现与翻译】**
> **日文原题**：`[3]` $|x + 2y| \le 6$
> **中文翻译**：画出不等式 $|x + 2y| \le 6$ 所表示的平面区域。

**【考点定位】** 含绝对值的线性不等式（等价转化为两平行直线间的带状区域）。

**【图解辅助（SVG 矢量图）】**

```html
<svg viewBox="0 0 340 240" width="340" height="240" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <marker id="arr713" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#333"/>
    </marker>
    <pattern id="h713" width="8" height="8" patternTransform="rotate(45)" patternUnits="userSpaceOnUse">
      <line x1="0" y1="0" x2="0" y2="8" stroke="#2563eb" stroke-width="1.2" opacity="0.45"/>
    </pattern>
  </defs>
  <!-- 原点(170,120), 1单位=20px -->
  <!-- 直线1: y = -0.5x + 3 -> x=-8:(10,20), x=8:(330,140) -> 修正: y=3-0.5x, x=-8时y=7(超出), 用x=-6:(50,0), x=8:(330,140) -->
  <!-- 直线2: y = -0.5x - 3 -> x=-8:(10,100), x=6:(290,240) -->
  <polygon points="50,0 330,140 290,240 10,100" fill="url(#h713)"/>
  <line x1="15" y1="120" x2="325" y2="120" stroke="#333" stroke-width="1.4" marker-end="url(#arr713)"/>
  <line x1="170" y1="230" x2="170" y2="12" stroke="#333" stroke-width="1.4" marker-end="url(#arr713)"/>
  <text x="328" y="124" font-size="13" font-style="italic" fill="#333">x</text>
  <text x="176" y="18" font-size="13" font-style="italic" fill="#333">y</text>
  <text x="156" y="134" font-size="12" fill="#333">O</text>
  <!-- 两条边界线 -->
  <line x1="50" y1="0" x2="330" y2="140" stroke="#1d4ed8" stroke-width="2"/>
  <line x1="10" y1="100" x2="290" y2="240" stroke="#1d4ed8" stroke-width="2"/>
  <!-- 截距点: (0,3)->(170,60), (6,0)->(290,120), (0,-3)->(170,180), (-6,0)->(50,120) -->
  <circle cx="170" cy="60" r="3" fill="#1d4ed8"/>
  <circle cx="290" cy="120" r="3" fill="#1d4ed8"/>
  <circle cx="170" cy="180" r="3" fill="#1d4ed8"/>
  <circle cx="50" cy="120" r="3" fill="#1d4ed8"/>
  <text x="176" y="58" font-size="12" fill="#333">3</text>
  <text x="292" y="114" font-size="12" fill="#333">6</text>
  <text x="148" y="185" font-size="12" fill="#333">-3</text>
  <text x="36" y="134" font-size="12" fill="#333">-6</text>
  <text x="225" y="72" font-size="12" fill="#1d4ed8">x+2y=6</text>
  <text x="28" y="175" font-size="12" fill="#1d4ed8">x+2y=-6</text>
</svg>
```

**【分步标准解答】**
1. 去掉绝对值符号：
   $$|x + 2y| \le 6 \iff -6 \le x + 2y \le 6$$
2. 变形为关于 $y$ 的不等式：
   $$-\frac{1}{2}x - 3 \le y \le -\frac{1}{2}x + 3$$
3. 因此，所求区域为两条平行直线 $x + 2y = 6$（过 $(6,0),(0,3)$）与 $x + 2y = -6$（过 $(-6,0),(0,-3)$）所夹的带状区域（含边界线）。

**【最终答案】**
**2 直線 $x+2y=6$ と $x+2y=-6$ に挟まれた部分（図の斜線部分、境界線を含む）。**

---

#### [4] $|x| + |y + 1| \le 2$

**【原题重现与翻译】**
> **日文原题**：`[4]` $|x| + |y + 1| \le 2$
> **中文翻译**：画出不等式 $|x| + |y + 1| \le 2$ 所表示的平面区域。

**【考点定位】** 双绝对值区域作图（分类讨论或平移法）。

**【图解辅助（SVG 矢量图）】**

```html
<svg viewBox="0 0 320 250" width="320" height="250" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <marker id="arr714" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#333"/>
    </marker>
    <pattern id="h714" width="7" height="7" patternTransform="rotate(45)" patternUnits="userSpaceOnUse">
      <line x1="0" y1="0" x2="0" y2="7" stroke="#2563eb" stroke-width="1.2" opacity="0.45"/>
    </pattern>
  </defs>
  <!-- 原点(160,85), 1单位=42px -->
  <!-- 顶点: (0,1)->(160,43), (2,-1)->(244,127), (0,-3)->(160,211), (-2,-1)->(76,127) -->
  <polygon points="160,43 244,127 160,211 76,127" fill="url(#h714)" stroke="#1d4ed8" stroke-width="2.2"/>
  <line x1="25" y1="85" x2="295" y2="85" stroke="#333" stroke-width="1.4" marker-end="url(#arr714)"/>
  <line x1="160" y1="240" x2="160" y2="14" stroke="#333" stroke-width="1.4" marker-end="url(#arr714)"/>
  <text x="298" y="89" font-size="13" font-style="italic" fill="#333">x</text>
  <text x="166" y="20" font-size="13" font-style="italic" fill="#333">y</text>
  <text x="146" y="99" font-size="12" fill="#333">O</text>
  <!-- 中心虚线 y=-1 -->
  <line x1="76" y1="127" x2="244" y2="127" stroke="#dc2626" stroke-width="1" stroke-dasharray="4,3"/>
  <circle cx="160" cy="127" r="3" fill="#dc2626"/>
  <circle cx="160" cy="43" r="3" fill="#1d4ed8"/>
  <circle cx="244" cy="127" r="3" fill="#1d4ed8"/>
  <circle cx="160" cy="211" r="3" fill="#1d4ed8"/>
  <circle cx="76" cy="127" r="3" fill="#1d4ed8"/>
  <text x="167" y="42" font-size="12" fill="#1d4ed8">(0, 1)</text>
  <text x="249" y="131" font-size="12" fill="#1d4ed8">(2, -1)</text>
  <text x="167" y="218" font-size="12" fill="#1d4ed8">(0, -3)</text>
  <text x="25" y="131" font-size="12" fill="#1d4ed8">(-2, -1)</text>
  <text x="165" y="122" font-size="11" fill="#dc2626">(0,-1)</text>
</svg>
```

**【分步标准解答】**
- **方法一（平移法，推荐考场秒杀）**：
  1. 先考虑基本图形 $|x| + |y| \le 2$：它表示以 $(2,0),(0,2),(-2,0),(0,-2)$ 为顶点的正方形（旋转 $45^\circ$）的内部及边界。
  2. 将 $y$ 替换为 $y+1$，即将上述正方形沿 $y$ 轴负方向平移 $1$ 个单位，得到中心在 $(0, -1)$、四个顶点分别为 $(2, -1),\; (0, 1),\; (-2, -1),\; (0, -3)$ 的正方形内部及边界。
- **方法二（分类讨论法，日本教材标准写法）**：
  - ① $x \ge 0,\; y \ge -1$ 时：$x + (y+1) \le 2 \iff y \le -x + 1$；
  - ② $x \ge 0,\; y < -1$ 时：$x - (y+1) \le 2 \iff y \ge x - 3$；
  - ③ $x < 0,\; y \ge -1$ 时：$-x + (y+1) \le 2 \iff y \le x + 1$；
  - ④ $x < 0,\; y < -1$ 时：$-x - (y+1) \le 2 \iff y \ge -x - 3$。
  > 💡 **讲师批注**：验算四个顶点：代入 $(0,1)\to 0+2=2$；$(2,-1)\to 2+0=2$；$(0,-3)\to 0+|-2|=2$；$(-2,-1)\to 2+0=2$，全部满足等号！

**【最终答案】**
**4 点 $(0, 1),\; (2, -1),\; (0, -3),\; (-2, -1)$ を頂点とする正方形の周および内部（図の斜線部分、境界線を含む）。**

---

#### [5] $(x + y - 2)(y - x^2) > 0$

**【原题重现与翻译】**
> **日文原题**：`[5]` $(x + y - 2)(y - x^2) > 0$
> **中文翻译**：画出不等式 $(x + y - 2)(y - x^2) > 0$ 所表示的平面区域。

**【考点定位】** 乘积型不等式（$AB > 0$ 等价转化为两个不等式组的并集，不含边界）。

**【图解辅助（SVG 矢量图）】**

```html
<svg viewBox="0 0 340 260" width="340" height="260" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <marker id="arr715" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#333"/>
    </marker>
    <pattern id="h715" width="7" height="7" patternTransform="rotate(45)" patternUnits="userSpaceOnUse">
      <line x1="0" y1="0" x2="0" y2="7" stroke="#2563eb" stroke-width="1.2" opacity="0.5"/>
    </pattern>
    <!-- 裁剪出 y>x^2 且 y>-x+2 (上方公共区) -->
    <clipPath id="aboveParab">
      <path d="M 85,10 Q 190,410 295,10 Z"/>
    </clipPath>
    <clipPath id="belowParab">
      <path d="M 0,0 L 340,0 L 340,260 L 0,260 Z M 85,10 Q 190,410 295,10 Z" clip-rule="evenodd"/>
    </clipPath>
  </defs>
  <!-- 原点(190,210), 1单位=40px -->
  <!-- 抛物线 y=x^2: x=0->(190,210), x=1->(230,170), x=-2->(110,50), x=2->(270,50), x=±2.23->(100,10)/(280,10) -->
  <!-- 修正贝塞尔拟合 y=x^2: 端点(-2.236,5)->(100.6,10), (2.236,5)->(279.4,10), 顶点(190,210) => Q(190,410) -->
  <!-- 直线 y=-x+2: x=-2->(110,50), x=1->(230,170), x=2->(270,210), x=3->(310,250), x=-3->(70,10) -->
  <!-- 区域1: 抛物线上方且直线上方 -->
  <polygon points="70,10 340,10 340,260 310,250" fill="url(#h715)" clip-path="url(#aboveParab)"/>
  <!-- 区域2: 抛物线下方且直线下方 -->
  <polygon points="0,10 70,10 310,250 310,260 0,260" fill="url(#h715)" clip-path="url(#belowParab)"/>
  <!-- 坐标轴 -->
  <line x1="20" y1="210" x2="325" y2="210" stroke="#333" stroke-width="1.4" marker-end="url(#arr715)"/>
  <line x1="190" y1="250" x2="190" y2="12" stroke="#333" stroke-width="1.4" marker-end="url(#arr715)"/>
  <text x="328" y="214" font-size="13" font-style="italic" fill="#333">x</text>
  <text x="196" y="18" font-size="13" font-style="italic" fill="#333">y</text>
  <text x="176" y="224" font-size="12" fill="#333">O</text>
  <!-- 虚线边界 -->
  <path d="M 100.6,10 Q 190,410 279.4,10" fill="none" stroke="#1d4ed8" stroke-width="2" stroke-dasharray="5,4"/>
  <line x1="70" y1="10" x2="310" y2="250" stroke="#dc2626" stroke-width="2" stroke-dasharray="5,4"/>
  <!-- 交点 (空心圆) -->
  <circle cx="110" cy="50" r="4" fill="white" stroke="#111" stroke-width="1.6"/>
  <circle cx="230" cy="170" r="4" fill="white" stroke="#111" stroke-width="1.6"/>
  <text x="45" y="54" font-size="12" fill="#111">(-2, 4)</text>
  <text x="237" y="168" font-size="12" fill="#111">(1, 1)</text>
  <text x="196" y="130" font-size="12" fill="#dc2626">2</text>
  <text x="272" y="224" font-size="12" fill="#dc2626">2</text>
  <text x="278" y="34" font-size="12" fill="#1d4ed8">y=x²</text>
  <text x="258" y="242" font-size="12" fill="#dc2626">x+y=2</text>
</svg>
```

**【分步标准解答】**
1. 化为同号条件：
   $$(x+y-2)(y-x^2) > 0 \iff \begin{cases} y > -x+2 \\ y > x^2 \end{cases} \quad \text{または} \quad \begin{cases} y < -x+2 \\ y < x^2 \end{cases}$$
2. 求直线 $y = -x + 2$ 与抛物线 $y = x^2$ 的交点：
   $$x^2 = -x + 2 \iff x^2 + x - 2 = 0 \iff (x+2)(x-1) = 0 \implies x = -2,\; 1$$
   故两交点为 $(-2, 4)$ 与 $(1, 1)$。
3. 因为不等号不含等号（$>$），边界线均为虚线，交点为空心点，**不包含边界线**。
   > 💡 **讲师批注**：快速验算涂色区域的方法是**代特值法**：取点 $(0, 3)$，$(0+3-2)(3-0) = 3 > 0$（涂色）；取点 $(0, 1)$，$(0+1-2)(1-0) = -1 < 0$（不涂）；取点 $(0, -1)$，$(-3)(-1) = 3 > 0$（涂色）。

**【最终答案】**
**直線 $x+y=2$ と放物線 $y=x^2$ で分けられる領域のうち、両者の上側にある部分と、両者の下側にある部分（図の斜線部分、境界線を含まない）。**

---

#### [6] $(x^2 + y^2 - 4)(x^2 + y^2 + 4x - 5) \le 0$

**【原题重现与翻译】**
> **日文原题**：`[6]` $(x^2 + y^2 - 4)(x^2 + y^2 + 4x - 5) \le 0$
> **中文翻译**：画出不等式 $(x^2 + y^2 - 4)(x^2 + y^2 + 4x - 5) \le 0$ 所表示的平面区域。

**【考点定位】** 两圆乘积型不等式（先配方判定两圆位置关系，再取异号区域）。

**【图解辅助（SVG 矢量图）】**

```html
<svg viewBox="0 0 360 250" width="360" height="250" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <marker id="arr716" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#333"/>
    </marker>
    <pattern id="h716" width="7" height="7" patternTransform="rotate(45)" patternUnits="userSpaceOnUse">
      <line x1="0" y1="0" x2="0" y2="7" stroke="#2563eb" stroke-width="1.2" opacity="0.5"/>
    </pattern>
    <!-- C1: 圆心(220,125), r=60 (1单位=30px); C2: 圆心(160,125), r=90 -->
    <mask id="m716a">
      <rect x="0" y="0" width="360" height="250" fill="black"/>
      <circle cx="220" cy="125" r="60" fill="white"/>
      <circle cx="160" cy="125" r="90" fill="black"/>
    </mask>
    <mask id="m716b">
      <rect x="0" y="0" width="360" height="250" fill="black"/>
      <circle cx="160" cy="125" r="90" fill="white"/>
      <circle cx="220" cy="125" r="60" fill="black"/>
    </mask>
  </defs>
  <!-- 涂色区域: C1内且C2外 + C2内且C1外 -->
  <rect x="0" y="0" width="360" height="250" fill="url(#h716)" mask="url(#m716a)"/>
  <rect x="0" y="0" width="360" height="250" fill="url(#h716)" mask="url(#m716b)"/>
  <!-- 坐标轴 -->
  <line x1="20" y1="125" x2="340" y2="125" stroke="#333" stroke-width="1.4" marker-end="url(#arr716)"/>
  <line x1="220" y1="240" x2="220" y2="12" stroke="#333" stroke-width="1.4" marker-end="url(#arr716)"/>
  <text x="342" y="129" font-size="13" font-style="italic" fill="#333">x</text>
  <text x="226" y="18" font-size="13" font-style="italic" fill="#333">y</text>
  <text x="206" y="139" font-size="12" fill="#333">O</text>
  <!-- 两圆边界 -->
  <circle cx="220" cy="125" r="60" fill="none" stroke="#1d4ed8" stroke-width="2"/>
  <circle cx="160" cy="125" r="90" fill="none" stroke="#dc2626" stroke-width="2"/>
  <!-- 关键点标注 -->
  <circle cx="160" cy="125" r="2.8" fill="#dc2626"/>
  <text x="150" y="140" font-size="11" fill="#dc2626">-2</text>
  <text x="64" y="140" font-size="11" fill="#dc2626">-5</text>
  <text x="252" y="140" font-size="11" fill="#dc2626">1</text>
  <text x="283" y="140" font-size="11" fill="#1d4ed8">2</text>
  <text x="224" y="61" font-size="11" fill="#1d4ed8">2</text>
  <text x="145" y="29" font-size="12" fill="#dc2626">C₂: (x+2)²+y²=9</text>
  <text x="255" y="58" font-size="12" fill="#1d4ed8">C₁: x²+y²=4</text>
</svg>
```

**【分步标准解答】**
1. 配方确定两个边界圆：
   - 圆 $C_1$: $x^2 + y^2 = 4$（圆心 $(0, 0)$，半径 $r_1 = 2$）。
   - 圆 $C_2$: $(x+2)^2 + y^2 = 9$（圆心 $(-2, 0)$，半径 $r_2 = 3$）。
2. 判断两圆位置关系：圆心距 $d = 2$，满足 $r_2 - r_1 = 1 < d = 2 < r_1 + r_2 = 5$，故两圆**相交于两点**（由两式相减 $4x-5=-4 \Rightarrow x = \frac{1}{4}$，$y = \pm \frac{3\sqrt{7}}{4}$）。
3. 异号条件：
   $$(x^2+y^2-4)\{(x+2)^2+y^2-9\} \le 0 \iff \begin{cases} C_1 \text{ の外部(周を含む)} \\ C_2 \text{ の内部(周を含む)} \end{cases} \text{ または } \begin{cases} C_1 \text{ の内部(周を含む)} \\ C_2 \text{ の外部(周を含む)} \end{cases}$$
   > 💡 **讲师批注**：取原点 $(0,0)$ 检验：$(-4)(-5) = 20 > 0$，所以两圆重叠的中间部分**不涂色**！只涂左右两个月牙形区域（含边界线）。

**【最终答案】**
**円 $C_1: x^2+y^2=4$ と円 $C_2: (x+2)^2+y^2=9$ の一方の内部で他方の外部にある部分（図の斜線部分、境界線を含む）。**

---

### 演習問題 7（2）（P169）

**【原题重现与翻译】**
> **日文原题**：$x, y$ が 3 つの不等式 $3x-5y \ge -16,\; 3x-y \le 4,\; x+y \ge 0$ を満たすとき、$2x+5y$ の最大値及び最小値を求めよ。
> **中文翻译**：当 $x, y$ 满足 3 个不等式 $3x-5y \ge -16,\; 3x-y \le 4,\; x+y \ge 0$ 时，求 $2x+5y$ 的最大值与最小值。

**【考点定位】** 三角形可行域上的线性规划最值问题。

**【图解辅助（SVG 矢量图）】**

```html
<svg viewBox="0 0 360 280" width="360" height="280" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <marker id="arr72" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#333"/>
    </marker>
    <pattern id="h72" width="7" height="7" patternTransform="rotate(45)" patternUnits="userSpaceOnUse">
      <line x1="0" y1="0" x2="0" y2="7" stroke="#2563eb" stroke-width="1.2" opacity="0.45"/>
    </pattern>
  </defs>
  <!-- 原点(140,200), 1单位=32px -->
  <!-- A(3,5)->(236,40), B(-2,2)->(76,136), C(1,-1)->(172,232) -->
  <polygon points="236,40 76,136 172,232" fill="url(#h72)" stroke="#1d4ed8" stroke-width="2"/>
  <line x1="25" y1="200" x2="335" y2="200" stroke="#333" stroke-width="1.4" marker-end="url(#arr72)"/>
  <line x1="140" y1="265" x2="140" y2="15" stroke="#333" stroke-width="1.4" marker-end="url(#arr72)"/>
  <text x="338" y="204" font-size="13" font-style="italic" fill="#333">x</text>
  <text x="146" y="20" font-size="13" font-style="italic" fill="#333">y</text>
  <text x="126" y="214" font-size="12" fill="#333">O</text>
  <!-- 目标直线 2x+5y=k (斜率 -2/5 = -0.4) -->
  <!-- 过 A(3,5)->(236,40): dx=100, dy=+40 -> (136,0) to (336,80) -->
  <line x1="156" y1="8" x2="326" y2="76" stroke="#dc2626" stroke-width="1.8" stroke-dasharray="6,3"/>
  <!-- 过 C(1,-1)->(172,232): (72,192) to (272,272) -->
  <line x1="72" y1="192" x2="262" y2="268" stroke="#dc2626" stroke-width="1.8" stroke-dasharray="6,3"/>
  <circle cx="236" cy="40" r="3.5" fill="#dc2626"/>
  <circle cx="76" cy="136" r="3" fill="#1d4ed8"/>
  <circle cx="172" cy="232" r="3.5" fill="#dc2626"/>
  <text x="242" y="38" font-size="12" fill="#dc2626">A(3, 5) 最大</text>
  <text x="26" y="132" font-size="12" fill="#1d4ed8">B(-2, 2)</text>
  <text x="178" y="236" font-size="12" fill="#dc2626">C(1, -1) 最小</text>
  <text x="265" y="74" font-size="11" fill="#dc2626">2x+5y=31</text>
  <text x="220" y="266" font-size="11" fill="#dc2626">2x+5y=-3</text>
</svg>
```

**【分步标准解答】**
1. **将 3 个不等式改写为关于 $y$ 的形式**：
   - $3x - 5y \ge -16 \iff y \le \dfrac{3}{5}x + \dfrac{16}{5} \quad \cdots\text{①}$
   - $3x - y \le 4 \iff y \ge 3x - 4 \quad \cdots\text{②}$
   - $x + y \ge 0 \iff y \ge -x \quad \cdots\text{③}$
2. **求边界直线的 3 个交点（三角形顶点）**：
   - ①②联立：$(3x - 5y) - (3x - y) = -16 - 4 \Rightarrow -4y = -20 \Rightarrow y = 5,\; x = 3$，得 $A(3, 5)$。
   - ①③联立：代入 $y = -x$ 得 $3x + 5x = -16 \Rightarrow x = -2,\; y = 2$，得 $B(-2, 2)$。
   - ②③联立：代入 $y = -x$ 得 $3x + x = 4 \Rightarrow x = 1,\; y = -1$，得 $C(1, -1)$。
   故所给不等式组表示以 $A, B, C$ 为顶点的三角形周界及内部（区域 $D$）。
3. **设目标函数并比较斜率**：
   - 令 $2x + 5y = k$，变形为 $y = -\dfrac{2}{5}x + \dfrac{k}{5}$（斜率为 $-\dfrac{2}{5}$，$y$ 截距为 $\dfrac{k}{5}$）。
   - 因为 $k$ 与 $y$ 截距 $\dfrac{k}{5}$ 成正比，且目标直线斜率 $-\dfrac{2}{5}$ 满足：
     $$-1 < -\frac{2}{5} < \frac{3}{5} < 3$$
   - 由图可知，当直线 $y = -\dfrac{2}{5}x + \dfrac{k}{5}$ 与区域 $D$ 有公共点时：
     - 过点 $A(3, 5)$ 时 $k$ 最大：$k = 2(3) + 5(5) = 31$；
     - 过点 $C(1, -1)$ 时 $k$ 最小：$k = 2(1) + 5(-1) = -3$。
   > 💡 **讲师批注**：在 $B(-2,2)$ 处，$2(-2)+5(2)=6$，确实介于 $-3$ 与 $31$ 之间，验算无误！

**【最终答案】**
**最大値 $31$（$x=3,\; y=5$ のとき）、最小値 $-3$（$x=1,\; y=-1$ のとき）。**

---

### 演習問題 7（3）（P169）

**【原题重现与翻译】**
> **日文原题**：$x, y$ が 2 つの不等式 $x^2 + y^2 \le 10,\; y \ge -2x + 5$ を満たすとき、$x + y$ の最大値及び最小値を求めよ。
> **中文翻译**：当 $x, y$ 满足 2 个不等式 $x^2 + y^2 \le 10,\; y \ge -2x + 5$ 时，求 $x + y$ 的最大值与最小值。

**【考点定位】** 圆与直线围成的弓形区域上的线性最值（相切取最大 + 端点取最小）。

**【图解辅助（SVG 矢量图）】**

```html
<svg viewBox="0 0 340 260" width="340" height="260" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <marker id="arr73" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#333"/>
    </marker>
    <pattern id="h73" width="6" height="6" patternTransform="rotate(45)" patternUnits="userSpaceOnUse">
      <line x1="0" y1="0" x2="0" y2="6" stroke="#2563eb" stroke-width="1.2" opacity="0.5"/>
    </pattern>
    <clipPath id="inCirc73">
      <circle cx="150" cy="140" r="94.87"/>
    </clipPath>
  </defs>
  <!-- 原点(150,140), 1单位=30px, r=sqrt(10)*30=94.87 -->
  <!-- 交点 A(1,3)->(180,50), B(3,-1)->(240,170) -->
  <!-- 弓形区域: 直线 y=-2x+5 上方且在圆内 -->
  <polygon points="160,10 320,10 320,250 280,250" fill="url(#h73)" clip-path="url(#inCirc73)"/>
  <line x1="25" y1="140" x2="320" y2="140" stroke="#333" stroke-width="1.4" marker-end="url(#arr73)"/>
  <line x1="150" y1="250" x2="150" y2="12" stroke="#333" stroke-width="1.4" marker-end="url(#arr73)"/>
  <text x="323" y="144" font-size="13" font-style="italic" fill="#333">x</text>
  <text x="156" y="18" font-size="13" font-style="italic" fill="#333">y</text>
  <text x="136" y="154" font-size="12" fill="#333">O</text>
  <!-- 圆与割线 -->
  <circle cx="150" cy="140" r="94.87" fill="none" stroke="#1d4ed8" stroke-width="2"/>
  <line x1="165" y1="20" x2="265" y2="220" stroke="#1d4ed8" stroke-width="2"/>
  <!-- 切线 x+y=2sqrt(5) ≈ 4.472 -> 切点(sqrt(5), sqrt(5)) -> (217.1, 72.9) -->
  <line x1="155" y1="10.8" x2="290" y2="145.8" stroke="#dc2626" stroke-width="1.8" stroke-dasharray="6,3"/>
  <!-- 过 B(3,-1) 的最小线 x+y=2 -> (240,170) -->
  <line x1="160" y1="90" x2="275" y2="205" stroke="#dc2626" stroke-width="1.8" stroke-dasharray="6,3"/>
  <circle cx="180" cy="50" r="3" fill="#1d4ed8"/>
  <circle cx="240" cy="170" r="3.5" fill="#dc2626"/>
  <circle cx="217.1" cy="72.9" r="3.5" fill="#dc2626"/>
  <text x="184" y="46" font-size="11" fill="#1d4ed8">A(1,3)</text>
  <text x="247" y="176" font-size="11" fill="#dc2626">B(3,-1) 最小</text>
  <text x="224" y="72" font-size="11" fill="#dc2626">(√5, √5) 最大</text>
  <text x="260" y="122" font-size="11" fill="#dc2626">x+y=2√5</text>
  <text x="252" y="218" font-size="11" fill="#dc2626">x+y=2</text>
</svg>
```

**【分步标准解答】**
1. **求圆 $x^2 + y^2 = 10$ 与直线 $y = -2x + 5$ 的交点**：
   $$x^2 + (-2x + 5)^2 = 10 \iff 5x^2 - 20x + 15 = 0 \iff (x-1)(x-3) = 0 \implies x = 1,\; 3$$
   对应交点为 $A(1, 3)$ 与 $B(3, -1)$。所给不等式组表示直线 $AB$ 上方的弓形区域 $D$（含边界）。
2. **令 $x + y = k$（即 $y = -x + k$，斜率为 $-1$）**：
   - **求最大值（相切检验）**：直线 $x + y - k = 0$ 与圆 $x^2 + y^2 = 10$ 相切的条件为圆心 $(0,0)$ 到直线的距离等于半径 $\sqrt{10}$：
     $$\frac{|k|}{\sqrt{1^2 + 1^2}} = \sqrt{10} \iff |k| = 2\sqrt{5} \implies k = \pm 2\sqrt{5}$$
     取 $k = 2\sqrt{5}$ 时，切点满足 $x = y$ 且 $x+y = 2\sqrt{5}$，解得切点 $(\sqrt{5}, \sqrt{5})$。
     **检验切点是否在区域 $D$ 内**：$2(\sqrt{5}) + \sqrt{5} = 3\sqrt{5} = \sqrt{45} > \sqrt{25} = 5$，满足 $y \ge -2x + 5$！故切点在区域 $D$ 内，最大值为 $2\sqrt{5}$。
   - **求最小值（比较斜率找端点）**：边界弦 $AB$ 的斜率为 $-2$，目标直线斜率为 $-1$（$-2 < -1$）。向下平移直线，最后离开弓形的点是右下方交点 $B(3, -1)$。
     此时 $k = 3 + (-1) = 2$。
   > 💡 **讲师批注**：圆弧区域求最值时，**切点一定要检验是否落在有效圆弧上**！如果不验证直接写 $2\sqrt{5}$，在切点落在无效弧段的变式题中就会掉坑。

**【最终答案】**
**最大値 $2\sqrt{5}$（$x=\sqrt{5},\; y=\sqrt{5}$ のとき）、最小値 $2$（$x=3,\; y=-1$ のとき）。**

---

### 演習問題 7（4）（P170）

**【原题重现与翻译】**
> **日文原题**：連立不等式 $2x-3y \ge -12,\; 5x-y \le 9,\; x+5y \ge 7$ の表す領域を $A$ とする。点 $(x, y)$ が領域 $A$ 上を動くとき、$x^2+y^2$ の最大値と最小値、及びその時の $x, y$ の値を求めよ。
> **中文翻译**：设联立不等式 $2x-3y \ge -12,\; 5x-y \le 9,\; x+5y \ge 7$ 所表示的区域为 $A$。当点 $(x, y)$ 在区域 $A$ 上运动时，求 $x^2+y^2$ 的最大值与最小值，以及此时 $x, y$ 的值。

**【考点定位】** 非线性目标函数 $x^2+y^2$（转化为动点到原点距离的平方，注意垂足是否落在线段上）。

**【图解辅助（SVG 矢量图）】**

```html
<svg viewBox="0 0 360 280" width="360" height="280" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <marker id="arr74" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#333"/>
    </marker>
    <pattern id="h74" width="7" height="7" patternTransform="rotate(45)" patternUnits="userSpaceOnUse">
      <line x1="0" y1="0" x2="0" y2="7" stroke="#2563eb" stroke-width="1.2" opacity="0.45"/>
    </pattern>
  </defs>
  <!-- 原点(160,230), 1单位=30px -->
  <!-- P(3,6)->(250,50), Q(-3,2)->(70,170), R(2,1)->(220,200) -->
  <!-- 垂足 H(7/26, 35/26) ≈ (0.27, 1.35) -> (168.1, 189.6) -->
  <polygon points="250,50 70,170 220,200" fill="url(#h74)" stroke="#1d4ed8" stroke-width="2"/>
  <line x1="25" y1="230" x2="335" y2="230" stroke="#333" stroke-width="1.4" marker-end="url(#arr74)"/>
  <line x1="160" y1="270" x2="160" y2="12" stroke="#333" stroke-width="1.4" marker-end="url(#arr74)"/>
  <text x="338" y="234" font-size="13" font-style="italic" fill="#333">x</text>
  <text x="166" y="18" font-size="13" font-style="italic" fill="#333">y</text>
  <text x="146" y="244" font-size="12" fill="#333">O</text>
  <!-- 最小圆 (r=7/sqrt(26)*30 ≈ 41.18) -->
  <circle cx="160" cy="230" r="41.18" fill="none" stroke="#dc2626" stroke-width="1.6" stroke-dasharray="5,3"/>
  <!-- 最大圆弧 (r=sqrt(45)*30 ≈ 201.25) -->
  <path d="M 160,28.75 A 201.25,201.25 0 0,1 305,90" fill="none" stroke="#dc2626" stroke-width="1.6" stroke-dasharray="5,3"/>
  <!-- 垂线段 OH -->
  <line x1="160" y1="230" x2="168.1" y2="189.6" stroke="#dc2626" stroke-width="1.8"/>
  <circle cx="250" cy="50" r="3.5" fill="#dc2626"/>
  <circle cx="70" cy="170" r="3" fill="#1d4ed8"/>
  <circle cx="220" cy="200" r="3" fill="#1d4ed8"/>
  <circle cx="168.1" cy="189.6" r="3.5" fill="#dc2626"/>
  <text x="256" y="48" font-size="12" fill="#dc2626">P(3, 6) 最大</text>
  <text x="20" y="168" font-size="12" fill="#1d4ed8">Q(-3, 2)</text>
  <text x="226" y="206" font-size="12" fill="#1d4ed8">R(2, 1)</text>
  <text x="174" y="186" font-size="11" fill="#dc2626">H(7/26, 35/26)</text>
  <text x="155" y="145" font-size="13" font-weight="bold" fill="#1d4ed8">A</text>
</svg>
```

**【分步标准解答】**
1. **确定区域 $A$ 的三个顶点**：
   - $l_1: 2x - 3y = -12$（$y \le \frac{2}{3}x + 4$）
   - $l_2: 5x - y = 9$（$y \ge 5x - 9$）
   - $l_3: x + 5y = 7$（$y \ge -\frac{1}{5}x + \frac{7}{5}$）
   - 联立求交点：
     - $l_1 \cap l_2$：$2x - 3(5x-9) = -12 \Rightarrow -13x = -39 \Rightarrow P(3, 6)$。
     - $l_1 \cap l_3$：$2(7-5y) - 3y = -12 \Rightarrow 13y = 26 \Rightarrow Q(-3, 2)$。
     - $l_2 \cap l_3$：$x + 5(5x-9) = 7 \Rightarrow 26x = 52 \Rightarrow R(2, 1)$。
2. **转化目标函数**：令 $x^2 + y^2 = r^2$（$r > 0$），即动点 $(x,y)$ 到原点 $O(0,0)$ 距离的平方（以原点为圆心、半径为 $r$ 的圆与区域 $A$ 有公共点）。
3. **求最大值**：原点到多边形区域的最远点必在顶点处，分别计算：
   $$OP^2 = 3^2 + 6^2 = 45, \qquad OQ^2 = (-3)^2 + 2^2 = 13, \qquad OR^2 = 2^2 + 1^2 = 5$$
   故在 $P(3, 6)$ 处取得最大值 $45$。
4. **求最小值**：从原点 $O$ 向边 $QR$（直线 $l_3: x + 5y - 7 = 0$）作垂线，垂足记为 $H$。
   - 过原点垂直于 $l_3$ 的直线方程为 $y = 5x$。
   - 联立 $x + 5y = 7$ 与 $y = 5x$，得 $26x = 7 \Rightarrow x = \dfrac{7}{26},\; y = \dfrac{35}{26}$。
   - **检验垂足是否落在线段 $QR$ 上**：因为 $-3 < \dfrac{7}{26} < 2$，垂足 $H\left(\dfrac{7}{26}, \dfrac{35}{26}\right)$ 确实在线段 $QR$ 上！
   - 此时距离平方为：
     $$OH^2 = \left(\frac{|0 + 0 - 7|}{\sqrt{1^2 + 5^2}}\right)^2 = \frac{49}{26}$$
   > 💡 **讲师批注**：切记不要只算三个顶点的 $x^2+y^2$ 就以为最小值是 $OR^2 = 5$！原点到三角形的最近点常常是**垂足**，且必须验证垂足的 $x$ 坐标确实夹在两端点 $x$ 坐标之间。

**【最终答案】**
**最大値 $45$（$x=3,\; y=6$ のとき）、最小値 $\dfrac{49}{26}$（$x=\dfrac{7}{26},\; y=\dfrac{35}{26}$ のとき）。**

---

### 演習問題 7（5）（P170）

**【原题重现与翻译】**
> **日文原题**：実数 $x, y$ が $x^2 + y^2 \le 1$ を満たしながら変わるとき、点 $(x+y,\; xy)$ の動く領域を図示せよ。
> **中文翻译**：当实数 $x, y$ 满足 $x^2 + y^2 \le 1$ 变化时，画出点 $(x+y,\; xy)$ 的运动区域。

**【考点定位】** 逆像法 / 基本对称式换元 + 实数解存在条件（判别式 $D \ge 0$）！EJU 压轴高频经典题！

**【图解辅助（SVG 矢量图）】**

```html
<svg viewBox="0 0 340 240" width="340" height="240" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <marker id="arr75" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#333"/>
    </marker>
    <pattern id="h75" width="7" height="7" patternTransform="rotate(45)" patternUnits="userSpaceOnUse">
      <line x1="0" y1="0" x2="0" y2="7" stroke="#2563eb" stroke-width="1.2" opacity="0.5"/>
    </pattern>
  </defs>
  <!-- 原点(170,130), X轴 1单位=70px, Y轴 1单位=120px -->
  <!-- 交点 (-sqrt(2), 0.5) -> (71, 70); (sqrt(2), 0.5) -> (269, 70) -->
  <!-- 上边界 Y=X^2/4: 顶点(170,130) => Q(170, 190) -->
  <!-- 下边界 Y=X^2/2 - 0.5: 顶点(170,190) => Q(170, 310) -->
  <path d="M 71,70 Q 170,190 269,70 Q 170,310 71,70 Z" fill="url(#h75)"/>
  <!-- 坐标轴 -->
  <line x1="25" y1="130" x2="320" y2="130" stroke="#333" stroke-width="1.4" marker-end="url(#arr75)"/>
  <line x1="170" y1="225" x2="170" y2="15" stroke="#333" stroke-width="1.4" marker-end="url(#arr75)"/>
  <text x="322" y="134" font-size="13" font-style="italic" fill="#333">X</text>
  <text x="176" y="20" font-size="13" font-style="italic" fill="#333">Y</text>
  <text x="156" y="143" font-size="12" fill="#333">O</text>
  <!-- 两条抛物线边界 -->
  <path d="M 71,70 Q 170,190 269,70" fill="none" stroke="#1d4ed8" stroke-width="2.2"/>
  <path d="M 71,70 Q 170,310 269,70" fill="none" stroke="#dc2626" stroke-width="2.2"/>
  <!-- 辅助虚线 -->
  <line x1="71" y1="70" x2="71" y2="130" stroke="#666" stroke-width="1" stroke-dasharray="3,3"/>
  <line x1="269" y1="70" x2="269" y2="130" stroke="#666" stroke-width="1" stroke-dasharray="3,3"/>
  <line x1="71" y1="70" x2="269" y2="70" stroke="#666" stroke-width="1" stroke-dasharray="3,3"/>
  <circle cx="71" cy="70" r="3.5" fill="#111"/>
  <circle cx="269" cy="70" r="3.5" fill="#111"/>
  <circle cx="170" cy="190" r="3" fill="#dc2626"/>
  <text x="54" y="145" font-size="12" fill="#333">-√2</text>
  <text x="260" y="145" font-size="12" fill="#333">√2</text>
  <text x="176" y="66" font-size="11" fill="#333">1/2</text>
  <text x="176" y="198" font-size="11" fill="#dc2626">-1/2</text>
  <text x="225" y="48" font-size="12" fill="#1d4ed8">Y = X²/4</text>
  <text x="235" y="182" font-size="12" fill="#dc2626">Y = X²/2 - 1/2</text>
</svg>
```

**【分步标准解答】**
1. **换元**：设 $X = x + y,\; Y = xy$。
2. **列出存在实数 $x, y$ 的充要条件**：
   - **条件 ①（实数存在条件）**：$x, y$ 是关于 $t$ 的一元二次方程 $t^2 - Xt + Y = 0$ 的两个实数解，故其判别式 $D \ge 0$：
     $$X^2 - 4Y \ge 0 \iff Y \le \frac{1}{4}X^2$$
   - **条件 ②（给定约束转化）**：
     $$x^2 + y^2 \le 1 \iff (x+y)^2 - 2xy \le 1 \iff X^2 - 2Y \le 1 \iff Y \ge \frac{1}{2}X^2 - \frac{1}{2}$$
   > 💡 **讲师批注**：**90% 的学生都会漏掉条件 ①（$X^2 - 4Y \ge 0$）！** 凡是看到对称式 $(x+y, xy)$，必须条件反射立刻写出二次方程 $t^2 - Xt + Y = 0$ 的判别式 $D \ge 0$。
3. **求两条边界抛物线的交点**：
   $$\frac{1}{4}X^2 = \frac{1}{2}X^2 - \frac{1}{2} \iff \frac{1}{4}X^2 = \frac{1}{2} \iff X^2 = 2 \implies X = \pm\sqrt{2},\; Y = \frac{1}{2}$$
4. 综合条件 ① 与 ②，点 $(X, Y)$ 的运动区域为两条抛物线 $Y = \dfrac{1}{4}X^2$ 与 $Y = \dfrac{1}{2}X^2 - \dfrac{1}{2}$ 所围成的封闭区域（含边界线）。

**【最终答案】**
**2 つの放物線 $Y = \dfrac{1}{4}X^2$ と $Y = \dfrac{1}{2}X^2 - \dfrac{1}{2}$ で囲まれた部分（図の斜線部分、境界線を含む。交点は $(-\sqrt{2}, \frac{1}{2}),\; (\sqrt{2}, \frac{1}{2})$）。**

---

### 演習問題 7（6）（P171）

#### [1] $x^2 + y^2 + 2x < 3$ ならば $x^2 + y^2 - 2x < 15$ であることを証明せよ。

**【原题重现与翻译】**
> **日文原题**：$x, y$ は実数とする。`[1]` $x^2 + y^2 + 2x < 3$ ならば $x^2 + y^2 - 2x < 15$ であることを証明せよ。
> **中文翻译**：设 $x, y$ 为实数。证明：若 $x^2 + y^2 + 2x < 3$，则 $x^2 + y^2 - 2x < 15$。

**【考点定位】** 利用平面区域的包含关系（$P \subset Q$）证明命题。

**【图解辅助（SVG 矢量图）】**

```html
<svg viewBox="0 0 340 240" width="340" height="240" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <marker id="arr761" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#333"/>
    </marker>
    <pattern id="h761" width="6" height="6" patternTransform="rotate(45)" patternUnits="userSpaceOnUse">
      <line x1="0" y1="0" x2="0" y2="6" stroke="#2563eb" stroke-width="1.2" opacity="0.5"/>
    </pattern>
  </defs>
  <!-- 原点(150,120), 1单位=24px -->
  <!-- 圆 Q: 圆心(1,0)->(174,120), r=4->96px (左端 x=-3 -> 78, 右端 x=5 -> 270) -->
  <!-- 圆 P: 圆心(-1,0)->(126,120), r=2->48px (左端 x=-3 -> 78, 右端 x=1 -> 174) -->
  <circle cx="174" cy="120" r="96" fill="#fef2f2" stroke="#dc2626" stroke-width="2" stroke-dasharray="5,4"/>
  <circle cx="126" cy="120" r="48" fill="url(#h761)" stroke="#1d4ed8" stroke-width="2" stroke-dasharray="5,4"/>
  <line x1="25" y1="120" x2="315" y2="120" stroke="#333" stroke-width="1.4" marker-end="url(#arr761)"/>
  <line x1="150" y1="230" x2="150" y2="14" stroke="#333" stroke-width="1.4" marker-end="url(#arr761)"/>
  <text x="318" y="124" font-size="13" font-style="italic" fill="#333">x</text>
  <text x="156" y="18" font-size="13" font-style="italic" fill="#333">y</text>
  <text x="136" y="134" font-size="12" fill="#333">O</text>
  <circle cx="126" cy="120" r="2.8" fill="#1d4ed8"/>
  <circle cx="174" cy="120" r="2.8" fill="#dc2626"/>
  <circle cx="78" cy="120" r="3" fill="#111"/>
  <text x="116" y="135" font-size="11" fill="#1d4ed8">-1</text>
  <text x="172" y="135" font-size="11" fill="#dc2626">1</text>
  <text x="64" y="135" font-size="11" fill="#111">-3</text>
  <text x="274" y="135" font-size="11" fill="#dc2626">5</text>
  <text x="110" y="96" font-size="13" font-weight="bold" fill="#1d4ed8">P</text>
  <text x="210" y="66" font-size="13" font-weight="bold" fill="#dc2626">Q (P ⊂ Q)</text>
</svg>
```

**【分步标准解答】**
1. 将两个不等式配方，分别记其所表示的区域为 $P, Q$：
   - $P: (x+1)^2 + y^2 < 2^2$（以 $A(-1, 0)$ 为圆心、半径 $r_1 = 2$ 的圆内部）。
   - $Q: (x-1)^2 + y^2 < 4^2$（以 $B(1, 0)$ 为圆心、半径 $r_2 = 4$ 的圆内部）。
2. 计算两圆心之间的距离 $AB$：
   $$AB = 1 - (-1) = 2 = 4 - 2 = r_2 - r_1$$
   故圆 $A$ 内切于圆 $B$（切点为 $(-3, 0)$）。
3. 因此，圆 $A$ 的内部完全包含于圆 $B$ 的内部，即 $P \subset Q$ 成立。
   よって、命題「$x^2+y^2+2x<3 \implies x^2+y^2-2x<15$」は真である。（証明終）
   > 💡 **讲师批注**：也可以用纯代数法验算：由 $(x+1)^2 + y^2 < 4$ 得 $|x+1|<2 \Rightarrow x>-3 \Rightarrow -4x < 12$，故 $x^2+y^2-2x = (x^2+y^2+2x) - 4x < 3 + 12 = 15$。

**【最终答案】**
**領域 $P \subset Q$（2 円が点 $(-3, 0)$ で内接）より、題意は証明された。**

---

#### [2] $x^2 + y^2 \le 5$ が $2x + y \ge k$ の十分条件となる定数 $k$ の値の範囲を求めよ。

**【原题重现与翻译】**
> **日文原题**：`[2]` $x^2 + y^2 \le 5$ が $2x + y \ge k$ の十分条件となる定数 $k$ の値の範囲を求めよ。
> **中文翻译**：求使 $x^2 + y^2 \le 5$ 成为 $2x + y \ge k$ 的充分条件的常数 $k$ 的取值范围。

**【考点定位】** 充分条件与区域包含（圆盘完全包含于半平面内的条件）。

**【图解辅助（SVG 矢量图）】**

```html
<svg viewBox="0 0 320 240" width="320" height="240" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <marker id="arr762" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#333"/>
    </marker>
    <pattern id="h762" width="7" height="7" patternTransform="rotate(45)" patternUnits="userSpaceOnUse">
      <line x1="0" y1="0" x2="0" y2="7" stroke="#2563eb" stroke-width="1.2" opacity="0.45"/>
    </pattern>
  </defs>
  <!-- 原点(160,115), 1单位=28px, r=sqrt(5)*28 ≈ 62.6 -->
  <circle cx="160" cy="115" r="62.6" fill="url(#h762)" stroke="#1d4ed8" stroke-width="2"/>
  <line x1="25" y1="115" x2="295" y2="115" stroke="#333" stroke-width="1.4" marker-end="url(#arr762)"/>
  <line x1="160" y1="230" x2="160" y2="12" stroke="#333" stroke-width="1.4" marker-end="url(#arr762)"/>
  <text x="298" y="119" font-size="13" font-style="italic" fill="#333">x</text>
  <text x="166" y="18" font-size="13" font-style="italic" fill="#333">y</text>
  <text x="146" y="129" font-size="12" fill="#333">O</text>
  <!-- 切线 2x+y=-5: 切点(-2,-1)->(104,143); x=-3.5,y=2 ->(62,59); x=-0.5,y=-4 ->(146,227) -->
  <line x1="62" y1="59" x2="146" y2="227" stroke="#dc2626" stroke-width="2"/>
  <!-- 更下方的允许直线 2x+y=k (k<-5) -->
  <line x1="42" y1="75" x2="120" y2="231" stroke="#dc2626" stroke-width="1.5" stroke-dasharray="5,3"/>
  <circle cx="104" cy="143" r="3.5" fill="#dc2626"/>
  <text x="172" y="92" font-size="13" font-weight="bold" fill="#1d4ed8">P</text>
  <text x="24" y="152" font-size="11" fill="#dc2626">(-2,-1)</text>
  <text x="148" y="220" font-size="11" fill="#dc2626">2x+y=-5</text>
  <text x="200" y="195" font-size="12" fill="#dc2626">Q: 2x+y ≥ k</text>
</svg>
```

**【分步标准解答】**
1. 设区域 $P: x^2 + y^2 \le 5$（圆心原点、半径 $\sqrt{5}$ 的圆盘），区域 $Q: 2x + y \ge k$（直线 $y = -2x + k$ 及其上方区域）。
2. 「$P$ 是 $Q$ 的充分条件」等价于 $P \subset Q$，即圆盘 $P$ 必须完全位于直线 $y = -2x + k$ 的上方（允许相切）。
3. 求直线 $2x + y - k = 0$ 与圆 $x^2 + y^2 = 5$ 相切时的 $k$ 值：
   $$\frac{|k|}{\sqrt{2^2 + 1^2}} = \sqrt{5} \iff \frac{|k|}{\sqrt{5}} = \sqrt{5} \iff |k| = 5 \implies k = \pm 5$$
4. 要使圆盘在直线上方，直线需在圆的**左下方**，其临界位置为下方切线 $2x + y = -5$（切点 $(-2, -1)$）。当直线继续向下平移（$y$ 截距 $k$ 变小）时仍满足 $P \subset Q$，故：
   $$k \le -5$$
   > 💡 **讲师批注**：也可用柯西不等式验算：$(2x+y)^2 \le (2^2+1^2)(x^2+y^2) \le 5 \times 5 = 25 \Rightarrow -5 \le 2x+y \le 5$，要使 $2x+y \ge k$ 恒成立，必有 $k \le \min(2x+y) = -5$。

**【最终答案】**
**$k \le -5$**

---

> 👉 **续篇导引**：本切片的「2次曲線（放物線・楕円・双曲線）」与「2次曲線と直線」（演習問題 8 与演習問題 9 全解）请见下篇 [`note_012_b.md`](file:///Users/baohan/Desktop/EJU/notes_math/note_012_b.md)。
