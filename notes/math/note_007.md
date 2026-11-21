# 《EJU 教材全解与备课讲义》数学 007（P91–P105）

> **对应源文件**：`work_math/ocr_md/ocr_007_p91-105.md`（第三章《図形と計量・図形の性質》之「三角比二次函数最值」「正弦定理と余弦定理」「三角比と図形の計量」「三角形の辺の比、五心」「チェバの定理、メネラウスの定理」「円に内接する四角形」）
> **视觉核对参考图**：`work_math/ref_imgs/page_0091.jpg`、`page_0093.jpg` – `page_0096.jpg`、`page_0099.jpg` – `page_0102.jpg`、`page_0104.jpg`、`page_0105.jpg`

---

## 一、国内高中基础知识点唤醒与 EJU 考纲差异对比

本切片横跨日本高中数学 **数学Ⅰ（図形と計量）** 与 **数学A（図形の性質）** 两大核心几何模块，涵盖 **正弦・余弦定理、三角形面积与内接/外接圆、三角形角平分线与四心（外心・垂心・内心・重心）、中线定理、切瓦定理与梅涅劳斯定理、圆周角与圆内接四边形（含托勒密定理）** 六大板块。

### 1.1 正弦定理与余弦定理（正弦定理と余弦定理）

设 $\triangle ABC$ 的三边长为 $a, b, c$，外接圆半径为 $R$：
- **正弦定理（正弦定理）**：
  $$\frac{a}{\sin A} = \frac{b}{\sin B} = \frac{c}{\sin C} = 2R$$
  - 推论（边角比例关系）：$a : b : c = \sin A : \sin B : \sin C$。
- **余弦定理（余弦定理）**：
  $$a^2 = b^2 + c^2 - 2bc\cos A, \qquad b^2 = c^2 + a^2 - 2ca\cos B, \qquad c^2 = a^2 + b^2 - 2ab\cos C$$
  - 求角变形公式：
    $$\cos A = \frac{b^2 + c^2 - a^2}{2bc}, \qquad \cos B = \frac{c^2 + a^2 - b^2}{2ca}, \qquad \cos C = \frac{a^2 + b^2 - c^2}{2ab}$$
- **三角形的成立条件**：$|b - c| < a < b + c$（两边之和大于第三边，两边之差小于第三边）。

### 1.2 三角比与图形的计量（三角比と図形の計量）

- **三角形面积公式**：
  $$S = \frac{1}{2}bc\sin A = \frac{1}{2}ca\sin B = \frac{1}{2}ab\sin C$$
- **海伦公式（ヘロンの公式）**：令 $s = \dfrac{a+b+c}{2}$（半周长，即 $2s = a+b+c$），则：
  $$S = \sqrt{s(s-a)(s-b)(s-c)}$$
  > 适用场景：已知三边长（特别是三边均为整数）求面积时极其高效。
- **三角形内切圆半径 $r$ 与面积**：
  $$S = \frac{1}{2}r(a+b+c) = rs$$
- **多边形面积**：通过连结对角线，分割为若干个三角形求和（尤其是圆内接四边形，利用对角互补 $\cos C = -\cos A,\; \sin C = \sin A$ 联立求解）。

### 1.3 三角形的边之比、五心与中线定理（三角形の辺の比、五心）

- **角平分线定理（角の二等分線と比）**：
  - **内角平分线定理**：$\angle A$ 的内角平分线交边 $BC$ 于 $P$，则 $BP : PC = AB : AC$（内分）。
  - **外角平分线定理**：当 $AB \neq AC$ 时，$\angle A$ 的外角平分线交边 $BC$ 的延长线于 $Q$，则 $BQ : QC = AB : AC$（外分）。
  > ⚠️ **教材勘误提示**：原教材第 95 页（`page_0096.jpg`）[5.1] 定理 2 将「辺 $BC$ を $AB:AC$ に**外分**する」误印为「**内分**する」，备课与授课时务必提醒学生修正为「外分」。
- **三角形的四大核心「心」**（本切片讲解外心・垂心・内心・重心；傍心为第五心）：
  1. **外心（外心，$O$）**：三边垂直平分线的交点，到三顶点等距（$OA = OB = OC = R$），为外接圆圆心。
  2. **垂心（垂心，$H$）**：三边高线（或其延长线）的交点。
  3. **内心（内心，$I$）**：三内角平分线的交点，到三边等距（距离为 $r$），为内切圆圆心。
  4. **重心（重心，$G$）**：三条中线的交点，将每条中线按 **$2:1$** 内分（顶点侧为 $2$，中点侧为 $1$）。
- **中线定理（中線定理 / パップスの定理 / Pappus 定理）**：
  设 $M$ 为 $\triangle ABC$ 边 $BC$ 的中点，则：
  $$AB^2 + AC^2 = 2(AM^2 + BM^2)$$

### 1.4 切瓦定理与梅涅劳斯定理（チェバの定理、メネラウスの定理）

- **切瓦定理（チェバの定理）**：$\triangle ABC$ 三顶点与点 $O$ 连线交对边（或延长线）于 $P, Q, R$，则：
  $$\frac{BP}{PC} \cdot \frac{CQ}{QA} \cdot \frac{AR}{RB} = 1$$
  - **逆定理**：边（或延长线）上三点 $P, Q, R$ 中有 1 个或 3 个在**边上**，且上述乘积为 $1$（并满足两直线相交），则三直线 $AP, BQ, CR$ 交于一点。
  > ⚠️ **教材勘误提示**：原教材第 101 页（`page_0102.jpg`）[6.2] 漏印「辺」字（「3個が（空白）上にある」应为「3個が**辺**上にある」）。
- **梅涅劳斯定理（メネラウスの定理）**：不过顶点的直线交 $\triangle ABC$ 三边（或延长线）于 $P, Q, R$，则：
  $$\frac{BP}{PC} \cdot \frac{CQ}{QA} \cdot \frac{AR}{RB} = 1$$
  - **逆定理**：三点中有 1 个或 3 个在**边的延长线上**，且上述乘积为 $1$，则 **三点 $P, Q, R$ 共线（1つの直線上にある）**。
  > ⚠️ **教材勘误提示**：原教材第 101 页（`page_0102.jpg`）[6.4] 梅涅劳斯逆定理存在严重复制粘贴错误，误印为「3直線 $AP, BQ, CR$ は1点で交わる」，正确结论应为「**3点 $P, Q, R$ は1つの直線上にある**」（与第 102 页解説证明一致）。

### 1.5 圆周角定理与圆内接四边形（円に内接する四角形）

- **圆周角定理（円周角の定理）**：同弧所对圆周角相等，且等于圆心角的一半；半圆所对圆周角为 $90^\circ$。
  > ⚠️ **教材勘误提示**：原教材第 104 页（`page_0105.jpg`）[7.1] 将「1つの**弧**に対する円周角」误印为「1つの**弧度**に対する円周角」；[7.3] 标题「円周に内接する四角形」应为「円に内接する四角形」。
- **圆内接四边形的性质与判定**：
  - ① 对角互补（和为 $180^\circ$）；② 任一内角等于其对角的外角。满足其一即共圆。
- **托勒密定理（トレミーの定理）**：圆内接四边形 $ABCD$ 满足：
  $$AB \cdot CD + AD \cdot BC = AC \cdot BD$$

### 1.6 国内高中 vs. 日本 EJU 考纲差异与符号习惯

| 对比维度 | 国内高中习惯 | 日本 EJU 习惯 | 备课/应试提醒 |
| :--- | :--- | :--- | :--- |
| **平面几何考查比重** | 高考弱化纯平面几何，侧重解析几何/向量 | **数学A 必考大题！** 切瓦、梅涅劳斯、五心、圆幂、圆内接四边形为高频压轴载体 | 必须训练纯几何「倒角・倒比例」与「切瓦/梅涅劳斯口诀速算」 |
| **勾股定理名称** | 勾股定理 | **三平方の定理（さんへいほうのていり）** | 日本考场绝不会写「勾股定理」，务必熟记 |
| **三角形中位线定理** | 中位线定理 | **中点連結定理（ちゅうてんれんけつていり）** | 证明平行与 2 倍关系时的标准理由用语 |
| **中线定理** | 选修/竞赛补充（极化恒等式替代） | **中線定理 / パップスの定理**，教科书明文收录 | 出现中点求平方和时，第一时间条件反射调用 |
| **切瓦・梅涅劳斯定理** | 高中竞赛内容，高考不要求 | **数学A 标准课内必考定理** | EJU 几乎每年在平面几何题中借此考线段比与面积比 |
| **托勒密定理** | 竞赛拓展 | EJU 备考常备提速工具（**トレミーの定理**） | 求圆内接四边形对角线长时可秒杀 |

---

## 二、日文核心词汇与公式假名注音

### 2.1 本切片日文核心词汇

- 正弦（せいげん / seigen） — 正弦（$\sin$）
- 余弦（よげん / yogen） — 余弦（$\cos$）
- 正接（せいせつ / seisetsu） — 正切（$\tan$）
- 正弦定理（せいげんていり / seigen teiri） — 正弦定理
- 余弦定理（よげんていり / yogen teiri） — 余弦定理
- 外接円（がいせつえん / gaisetsuen） — 外接圆
- 内接円（ないせつえん / naisetsuen） — 内接圆
- 半径（はんけい / hankei） — 半径
- 直径（ちょっけい / chokkei） — 直径
- 弧（こ / ko） — 弧
- 円周角（えんしゅうかく / enshuukaku） — 圆周角
- 中心角（ちゅうしんかく / chuushinkaku） — 圆心角
- 鋭角（えいかく / eikaku） — 锐角
- 直角（ちょっかく / chokkaku） — 直角
- 鈍角（どんかく / donkaku） — 钝角
- 内角（ないかく / naikaku） — 内角
- 外角（がいかく / gaikaku） — 外角
- 対角（たいかく / taikaku） — 对角
- 対辺（たいへん / taihen） — 对边
- 垂線（すいせん / suisen） — 垂线
- 三平方の定理（さんへいほうのていり / sanheihou no teiri） — 勾股定理
- ヘロンの公式（へろんのこうしき / heron no koushiki） — 海伦公式
- 多角形（たかっけい / takakkei） — 多边形
- 四角形（しかっけい / shikakkei） — 四边形
- 正三角形（せいさんかっけい / seisankakkei） — 等边三角形（正三角形）
- 平行四辺形（へいこうしへんけい / heikou shihenkei） — 平行四边形
- 内分（ないぶん / naibun） — 内分
- 外分（がいぶん / gaibun） — 外分
- 二等分線（にとうぶんせん / nitoubunsen） — 平分线
- 垂直二等分線（すいちょくにとうぶんせん / suichoku nitoubunsen） — 垂直平分线（中垂线）
- 外心（がいしん / gaishin） — 外心
- 内心（ないしん / naishin） — 内心
- 重心（じゅうしん / juushin） — 重心
- 垂心（すいしん / suishin） — 垂心
- 中線（ちゅうせん / chuusen） — 中线
- 中点（ちゅうてん / chuuten） — 中点
- 中点連結定理（ちゅうてんれんけつていり / chuuten renketsu teiri） — 三角形中位线定理
- 中線定理（ちゅうせんていり / chuusen teiri） — 中线定理（亦称 パップスの定理 / 帕普斯定理）
- 補助線（ほじょせん / hojosen） — 辅助线
- チェバの定理（ちぇばのていり / cheba no teiri） — 切瓦定理（塞瓦定理）
- メネラウスの定理（めねらうすのていり / menerausu no teiri） — 梅涅劳斯定理
- 円周角の定理（えんしゅうかくのていり / enshuukaku no teiri） — 圆周角定理
- トレミーの定理（とれみーのていり / toremii no teiri） — 托勒密定理

### 2.2 核心公式的日本课堂口语读法

1. **正弦定理** $\dfrac{a}{\sin A} = 2R$
   - 课堂读法：**サイン エー ぶんの スモールエー イコール にアール**
   - 备注：区分大小写字母时，小写读 **スモールエー**，大写读 **ラージエー**（或直接靠上下文区分）。
2. **余弦定理** $a^2 = b^2 + c^2 - 2bc\cos A$
   - 课堂读法：**エーのにじょう イコール ビーのにじょう たす シーのにじょう ひく にビーシー コサイン エー**
3. **三角形面积与内切圆** $S = \dfrac{1}{2}bc\sin A = \dfrac{1}{2}r(a+b+c)$
   - 课堂读法：**エス イコール にぶんのいち ビーシー サイン エー イコール にぶんのいち アール かっこ エー たす ビー たす シー かっことじ**
4. **切瓦 / 梅涅劳斯定理** $\dfrac{BP}{PC} \cdot \dfrac{CQ}{QA} \cdot \dfrac{AR}{RB} = 1$
   - 课堂读法：**ピーシー ぶんの ビーピー かける キューエー ぶんの シーキュー かける アールビー ぶんの エーアール イコール いち**
   - 课堂记忆口诀：**「頂点 → 分点 → 頂点 → 分点 → 頂点 → 分点」**（绕三角形一圈，分子分母交替推进！）。
5. **中线定理** $AB^2 + AC^2 = 2(AM^2 + BM^2)$
   - 课堂读法：**エービーのにじょう たす エーシーのにじょう イコール に かっこ エーエムのにじょう たす ビーエムのにじょう かっことじ**

---

## 三、逐题深度解析（不可跳步）

---

### 演習問題 2（三角比を含む 2 次関数の最大・最小）

#### 演習問題 2-(7)
- **【原题重现与翻译】**
  - 原题：$30^\circ \le \theta \le 90^\circ$ のとき、関数 $y = \sin^2\theta + \cos\theta + 1$ の最大値、最小値を求めよ。また、その時の $\theta$ の値も求めよ。
  - 中文：当 $30^\circ \le \theta \le 90^\circ$ 时，求函数 $y = \sin^2\theta + \cos\theta + 1$ 的最大值与最小值，并求此时对应的 $\theta$ 的值。
- **【考点定位】**
  - 同角三角比关系（$\sin^2\theta + \cos^2\theta = 1$）消元换元；二次函数在闭区间上的最值（轴动/定轴定区间）。
- **【图解辅助（SVG 矢量图）】**

<svg viewBox="0 0 460 220" width="100%" xmlns="http://www.w3.org/2000/svg" style="max-width:460px;display:block;margin:12px auto;background:#fafbfc;border:1px solid #e1e4e8;border-radius:8px;">
  <defs>
    <marker id="arr7" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#333"/>
    </marker>
  </defs>
  <!-- 坐标轴 -->
  <line x1="60" y1="185" x2="410" y2="185" stroke="#333" stroke-width="1.5" marker-end="url(#arr7)"/>
  <line x1="90" y1="205" x2="90" y2="20" stroke="#333" stroke-width="1.5" marker-end="url(#arr7)"/>
  <text x="415" y="189" font-size="13" fill="#333" font-style="italic">t</text>
  <text x="85" y="15" font-size="13" fill="#333" font-style="italic">y</text>
  <text x="74" y="200" font-size="12" fill="#333">O</text>

  <!-- 抛物线虚线部分 y = -(t-0.5)^2 + 2.25; 映射: t=0->x=90, t=1->x=330 (scale 240); y=0->185, y=2.5->35 (scale 60) -->
  <!-- t=-0.2 -> x=42, y=1.76 -> 79.4; t=0 -> x=90, y=2 -> 65; t=0.5 -> x=210, y=2.25 -> 50; t=0.866 -> x=297.8, y=2.116 -> 58; t=1.2 -> x=378, y=1.76 -> 79.4 -->
  <path d="M 42 79.4 Q 66 71 90 65" fill="none" stroke="#aaa" stroke-width="1.5" stroke-dasharray="4,4"/>
  <path d="M 297.8 58 Q 338 68 378 79.4" fill="none" stroke="#aaa" stroke-width="1.5" stroke-dasharray="4,4"/>

  <!-- 有效区间实线部分 0 <= t <= sqrt(3)/2 -->
  <!-- 用二次贝塞尔精准拟合抛物线: 控制点在 x=(90+297.8)/2=193.9? 拆成两段 [0,0.5] 和 [0.5, 0.866] -->
  <!-- 段1 [0, 0.5]: P0=(90,65), P2=(210,50). 切线在t=0斜率dy/dt=1 -> dy/dx = -60/240 = -0.25 -> 控制点(150, 50) -->
  <!-- 段2 [0.5, 0.866]: P0=(210,50), P2=(297.8,58). 切线在t=0.5水平 -> 控制点(253.9, 50) -->
  <path d="M 90 65 Q 150 50 210 50 Q 253.9 50 297.8 58" fill="none" stroke="#d93025" stroke-width="3"/>

  <!-- 对称轴与辅助线 -->
  <line x1="210" y1="35" x2="210" y2="185" stroke="#1a73e8" stroke-width="1.2" stroke-dasharray="4,3"/>
  <line x1="90" y1="50" x2="210" y2="50" stroke="#1a73e8" stroke-width="1.2" stroke-dasharray="4,3"/>
  <line x1="297.8" y1="58" x2="297.8" y2="185" stroke="#666" stroke-width="1.2" stroke-dasharray="3,3"/>

  <!-- 关键点 -->
  <circle cx="90" cy="65" r="4.5" fill="#188038"/>
  <circle cx="210" cy="50" r="4.5" fill="#d93025"/>
  <circle cx="297.8" cy="58" r="4.5" fill="#555"/>

  <!-- 标注 -->
  <text x="68" y="69" font-size="12" fill="#188038" font-weight="bold">2</text>
  <text x="58" y="52" font-size="12" fill="#d93025" font-weight="bold">9/4</text>
  <text x="200" y="202" font-size="12" fill="#1a73e8" font-weight="bold">1/2</text>
  <text x="282" y="202" font-size="12" fill="#333">√3/2</text>
  <text x="195" y="34" font-size="12" fill="#d93025" font-weight="bold">最大値 9/4 (t=1/2)</text>
  <text x="102" y="88" font-size="12" fill="#188038" font-weight="bold">最小値 2 (t=0)</text>
  <text x="305" y="54" font-size="11" fill="#555">(5+2√3)/4 ≈ 2.12</text>
</svg>

- **【分步标准解答】**
  $\sin^2\theta = 1 - \cos^2\theta$ を用いて式を $\cos\theta$ だけで表すと、
  $$y = (1 - \cos^2\theta) + \cos\theta + 1 = -\cos^2\theta + \cos\theta + 2$$
  > 💡 讲师批注：三角比二次函数求最值的第一步永远是**「统一函数名」**——一次项是 $\cos\theta$，因此必须把二次项 $\sin^2\theta$ 转化为 $1 - \cos^2\theta$。

  ここで、$t = \cos\theta$ とおく。
  $30^\circ \le \theta \le 90^\circ$ の範囲で $\cos\theta$ は単調減少するから、$\cos 90^\circ \le \cos\theta \le \cos 30^\circ$ すなわち
  $$0 \le t \le \frac{\sqrt{3}}{2}$$
  > 💡 讲师批注：换元后**必须立即确定新变量 $t$ 的定义域**！注意 $\cos\theta$ 在 $[0^\circ, 180^\circ]$ 上单调递减，千万不要把左右端点写反。

  $y$ を $t$ の 2 次関数として平方完成すると、
  $$y = -t^2 + t + 2 = -\left(t - \frac{1}{2}\right)^2 + \frac{9}{4}$$
  > 💡 讲师批注：配方结果表示开口向下的抛物线，顶点为 $\left(\frac{1}{2},\; \frac{9}{4}\right)$。比较轴与区间端点：$\frac{\sqrt{3}}{2} \approx 0.866 > 0.5$，故对称轴 $t = \frac{1}{2}$ 落在定义域内部。

  したがって、$0 \le t \le \dfrac{\sqrt{3}}{2}$ において：
  - $t = \dfrac{1}{2}$ のとき、**最大値 $\dfrac{9}{4}$** をとる。このとき $\cos\theta = \dfrac{1}{2}$（$30^\circ \le \theta \le 90^\circ$）より $\theta = 60^\circ$。
  - 軸 $t = \dfrac{1}{2}$ からより遠い端点 $t = 0$（距離 $0.5 > \frac{\sqrt{3}}{2} - 0.5 \approx 0.366$）で最小となる。実際に端点の値を比べると：
    - $t = 0$ のとき $y = 2$
    - $t = \dfrac{\sqrt{3}}{2}$ のとき $y = -\dfrac{3}{4} + \dfrac{\sqrt{3}}{2} + 2 = \dfrac{5 + 2\sqrt{3}}{4} > 2$
    よって $t = 0$ のとき、**最小値 $2$** をとる。このとき $\cos\theta = 0$ より $\theta = 90^\circ$。
  > 💡 讲师批注：考场上判断哪一端离对称轴更远，只需比较 $\frac{1}{2} - 0 = \frac{1}{2}$ 与 $\frac{\sqrt{3}}{2} - \frac{1}{2}$：由于 $\sqrt{3} < 2$，显然 $\frac{\sqrt{3}}{2} - \frac{1}{2} < \frac{2}{2} - \frac{1}{2} = \frac{1}{2}$，故 $t=0$ 更远！
- **【最终答案】**
  **最大値：$\dfrac{9}{4}$（$\theta = 60^\circ$ のとき）、最小値：$2$（$\theta = 90^\circ$ のとき）**

---

### 演習問題 3（正弦定理と余弦定理）

#### 演習問題 3-(1)
- **【原题重现与翻译】**
  - 原题：$\triangle ABC$ において、$a = \sqrt{2},\; b = 2,\; A = 30^\circ$ のとき、$c,\; B,\; C$ を求めよ。
  - 中文：在 $\triangle ABC$ 中，已知 $a = \sqrt{2},\; b = 2,\; A = 30^\circ$，求边 $c$ 以及角 $B, C$。
- **【考点定位】**
  - 已知两边及其中一边的对角（SSA 情形）解三角形；正弦定理的多解检验与余弦定理求第三边。
- **【图解辅助（SVG 矢量图）】**

<svg viewBox="0 0 440 190" width="100%" xmlns="http://www.w3.org/2000/svg" style="max-width:440px;display:block;margin:12px auto;background:#fafbfc;border:1px solid #e1e4e8;border-radius:8px;">
  <!-- 射线 AB 水平向右，A在(50,150)，b=2(放大75倍->150)，A=30° -> C=(50+150*cos30, 150-150*sin30) = (179.9, 75) -->
  <!-- 以C为圆心，a=sqrt(2)*75=106.07画弧，交水平线y=150于 x = 179.9 ± sqrt(106.07^2 - 75^2) = 179.9 ± 75 = 104.9 和 254.9 -->
  <!-- 辅助圆弧 -->
  <path d="M 86 125 A 106.1 106.1 0 0 0 274 125" fill="none" stroke="#aaa" stroke-width="1.2" stroke-dasharray="4,3"/>
  <!-- 射线 -->
  <line x1="50" y1="150" x2="310" y2="150" stroke="#888" stroke-width="1.2"/>
  <!-- 两个三角形 -->
  <polygon points="50,150 254.9,150 179.9,75" fill="rgba(26,115,232,0.08)" stroke="#1a73e8" stroke-width="2"/>
  <line x1="179.9" y1="75" x2="104.9" y2="150" stroke="#d93025" stroke-width="2" stroke-dasharray="5,3"/>

  <!-- 点与标注 -->
  <circle cx="50" cy="150" r="3.5" fill="#333"/>
  <circle cx="179.9" cy="75" r="3.5" fill="#333"/>
  <circle cx="104.9" cy="150" r="3.5" fill="#d93025"/>
  <circle cx="254.9" cy="150" r="3.5" fill="#1a73e8"/>

  <text x="35" y="155" font-size="13" font-weight="bold" fill="#333">A</text>
  <text x="72" y="144" font-size="11" fill="#333">30°</text>
  <text x="176" y="65" font-size="13" font-weight="bold" fill="#333">C</text>
  <text x="95" y="168" font-size="13" font-weight="bold" fill="#d93025">B₂ (135°)</text>
  <text x="242" y="168" font-size="13" font-weight="bold" fill="#1a73e8">B₁ (45°)</text>

  <text x="100" y="106" font-size="12" fill="#333">b = 2</text>
  <text x="225" y="108" font-size="12" fill="#1a73e8">a = √2</text>
  <text x="148" y="122" font-size="12" fill="#d93025">a = √2</text>

  <!-- 说明 -->
  <text x="295" y="45" font-size="11.5" fill="#1a73e8">[1] B₁=45°, c=√3+1</text>
  <text x="295" y="66" font-size="11.5" fill="#d93025">[2] B₂=135°, c=√3-1</text>
</svg>

- **【分步标准解答】**
  正弦定理 $\dfrac{a}{\sin A} = \dfrac{b}{\sin B}$ より、
  $$\frac{\sqrt{2}}{\sin 30^\circ} = \frac{2}{\sin B}$$
  $$\sin B = \frac{2 \sin 30^\circ}{\sqrt{2}} = \frac{2 \cdot \frac{1}{2}}{\sqrt{2}} = \frac{1}{\sqrt{2}}$$
  > 💡 讲师批注：由 $\sin B = \frac{1}{\sqrt{2}}$ 反求角 $B$ 时，**千万不能只写 $45^\circ$！** 必须结合三角形内角和 $A + B < 180^\circ$（即 $0^\circ < B < 150^\circ$）检验钝角解是否成立。

  $A = 30^\circ$ より $0^\circ < B < 150^\circ$ であるから、
  $$B = 45^\circ \quad \text{または} \quad B = 135^\circ$$

  また、余弦定理 $a^2 = b^2 + c^2 - 2bc\cos A$ に $a = \sqrt{2},\; b = 2,\; A = 30^\circ$ を代入すると、
  $$(\sqrt{2})^2 = 2^2 + c^2 - 2 \cdot 2 \cdot c \cdot \cos 30^\circ$$
  $$2 = 4 + c^2 - 4c \cdot \frac{\sqrt{3}}{2}$$
  $$c^2 - 2\sqrt{3}c + 2 = 0$$
  2次方程式の解の公式より、
  $$c = \sqrt{3} \pm \sqrt{(\sqrt{3})^2 - 2} = \sqrt{3} \pm 1$$
  > 💡 讲师批注：由于数学Ⅰ阶段尚未学习 $\sin 105^\circ$ 与 $\sin 15^\circ$ 的加法定理，利用**余弦定理列出关于 $c$ 的一元二次方程**来求 $c$ 是最标准、最安全的做法！

  ここで、三角形の「大辺対大角」の性質（あるいは $B$ の値との対応）により場合分けする：
  - **[1] $B = 45^\circ$ のとき**：
    $C = 180^\circ - (30^\circ + 45^\circ) = 105^\circ$。
    $C > B$ より $c > b = 2$ であるから、$c = \sqrt{3} + 1$（$\approx 2.732 > 2$）。
  - **[2] $B = 135^\circ$ のとき**：
    $C = 180^\circ - (30^\circ + 135^\circ) = 15^\circ$。
    $C < A$ より $c < a = \sqrt{2}$ であるから、$c = \sqrt{3} - 1$（$\approx 0.732 < 1.414$）。
- **【最终答案】**
  **$c = \sqrt{3}+1,\; B = 45^\circ,\; C = 105^\circ$ または $c = \sqrt{3}-1,\; B = 135^\circ,\; C = 15^\circ$**

---

#### 演習問題 3-(2)
- **【原题重现与翻译】**
  - 原题：$\triangle ABC$ において、$\dfrac{\sin A}{\sqrt{7}} = \dfrac{\sin B}{\sqrt{3}} = \sin C$ が成り立つとき
    - [1] $\triangle ABC$ の内角のうち、最も大きい角の大きさを求めよ。
    - [2] $\triangle ABC$ の内角のうち、2番目に大きい角の正接を求めよ。
  - 中文：在 $\triangle ABC$ 中，已知 $\dfrac{\sin A}{\sqrt{7}} = \dfrac{\sin B}{\sqrt{3}} = \sin C$ 成立，求：
    - [1] $\triangle ABC$ 的内角中最大角的度数。
    - [2] $\triangle ABC$ 的内角中第二大角的正切值。
- **【考点定位】**
  - 正弦定理推论（$a:b:c = \sin A : \sin B : \sin C$）；余弦定理求角；大边对大角；同角三角比求 $\tan B$。
- **【分步标准解答】**
  与えられた連比式 $\dfrac{\sin A}{\sqrt{7}} = \dfrac{\sin B}{\sqrt{3}} = \dfrac{\sin C}{1}$ より、
  $$\sin A : \sin B : \sin C = \sqrt{7} : \sqrt{3} : 1$$
  正弦定理により $a : b : c = \sin A : \sin B : \sin C$ であるから、
  $$a : b : c = \sqrt{7} : \sqrt{3} : 1$$
  よって、正の数 $k\;(k > 0)$ を用いて
  $$a = \sqrt{7}k, \qquad b = \sqrt{3}k, \qquad c = k$$
  とおける。
  > 💡 讲师批注：在规范解答中，切忌直接写「设 $a = \sqrt{7}, b = \sqrt{3}, c = 1$」，因为题干只给了比例关系。引入正比例常数 $k > 0$，后续代入余弦定理时 $k^2$ 会自动约去，逻辑滴水不漏。

  **[1]** $\sqrt{7} > \sqrt{3} > 1$ より $a > b > c$ であるから、最も大きい角は $A$ である。
  余弦定理より、
  $$\cos A = \frac{b^2 + c^2 - a^2}{2bc} = \frac{(\sqrt{3}k)^2 + k^2 - (\sqrt{7}k)^2}{2 \cdot \sqrt{3}k \cdot k} = \frac{3k^2 + k^2 - 7k^2}{2\sqrt{3}k^2} = \frac{-3}{2\sqrt{3}} = -\frac{\sqrt{3}}{2}$$
  $0^\circ < A < 180^\circ$ であるから、
  $$A = 150^\circ$$

  **[2]** 2番目に大きい角は $B$ である。
  余弦定理より、
  $$\cos B = \frac{c^2 + a^2 - b^2}{2ca} = \frac{k^2 + 7k^2 - 3k^2}{2 \cdot k \cdot \sqrt{7}k} = \frac{5}{2\sqrt{7}}$$
  $0^\circ < B < 180^\circ$ より $\sin B > 0$ であるから、
  $$\sin B = \sqrt{1 - \cos^2 B} = \sqrt{1 - \frac{25}{28}} = \sqrt{\frac{3}{28}} = \frac{\sqrt{3}}{2\sqrt{7}}$$
  > 💡 讲师批注：求 $\sin B$ 也可以直接利用原条件 $\frac{\sin B}{\sqrt{3}} = \frac{\sin A}{\sqrt{7}} = \frac{\sin 150^\circ}{\sqrt{7}} = \frac{1}{2\sqrt{7}}$，瞬间得 $\sin B = \frac{\sqrt{3}}{2\sqrt{7}}$，计算量更小！

  したがって、正接 $\tan B$ は
  $$\tan B = \frac{\sin B}{\cos B} = \frac{\dfrac{\sqrt{3}}{2\sqrt{7}}}{\dfrac{5}{2\sqrt{7}}} = \frac{\sqrt{3}}{5}$$
- **【最终答案】**
  **[1] $150^\circ$　　[2] $\dfrac{\sqrt{3}}{5}$**

---

#### 演習問題 3-(3)
- **【原题重现与翻译】**
  - 原题：$\triangle ABC$ において、次の等式が成り立つことを証明せよ。
    $$a\sin A - b\sin B = c(\sin A\cos B - \cos A\sin B)$$
  - 中文：在 $\triangle ABC$ 中，证明等式 $a\sin A - b\sin B = c(\sin A\cos B - \cos A\sin B)$ 成立。
- **【考点定位】**
  - 利用正弦定理与余弦定理进行「角化边」证明三角形恒等式。
- **【分步标准解答】**
  $\triangle ABC$ の外接円の半径を $R$ とする。
  正弦定理より、
  $$\sin A = \frac{a}{2R}, \qquad \sin B = \frac{b}{2R}$$
  余弦定理より、
  $$\cos A = \frac{b^2 + c^2 - a^2}{2bc}, \qquad \cos B = \frac{c^2 + a^2 - b^2}{2ca}$$
  > 💡 讲师批注：三角形恒等式证明的通用王道策略——**「全部化为边 $a, b, c$ 与 $R$」**！只需把 $\sin$ 用正弦定理替换、$\cos$ 用余弦定理替换，化简左右两边必然相等。

  まず、左辺を計算すると、
  $$(\text{左辺}) = a \cdot \frac{a}{2R} - b \cdot \frac{b}{2R} = \frac{a^2 - b^2}{2R}$$

  次に、右辺を計算すると、
  $$(\text{右辺}) = c\left(\frac{a}{2R} \cdot \frac{c^2 + a^2 - b^2}{2ca} - \frac{b^2 + c^2 - a^2}{2bc} \cdot \frac{b}{2R}\right)$$
  $$= c\left(\frac{c^2 + a^2 - b^2}{4Rc} - \frac{b^2 + c^2 - a^2}{4Rc}\right)$$
  $$= \frac{(c^2 + a^2 - b^2) - (b^2 + c^2 - a^2)}{4R}$$
  $$= \frac{2a^2 - 2b^2}{4R} = \frac{a^2 - b^2}{2R}$$
  > 💡 讲师批注：注意约分时 $a$ 与 $a$ 约去、$b$ 与 $b$ 约去，最后外层的 $c$ 与分母的 $c$ 恰好全部消掉，括号内展开时注意第二项前面的负号要逐项变号！

  よって $(\text{左辺}) = (\text{右辺})$ となり、等式は成り立つ。（証明終）
- **【最终答案】**
  **証明完了（左右两边均化简为 $\dfrac{a^2 - b^2}{2R}$）**

---

### 演習問題 4（三角比と図形の計量）

#### 演習問題 4-(1)
- **【原题重现与翻译】**
  - 原题：$\triangle ABC$ において、$a = 2,\; b = \sqrt{2},\; c = 1$ とする。次のものを求めよ。
    - [1] $\cos B,\; \sin B$　　[2] $\triangle ABC$ の面積 $S$
    - [3] $\triangle ABC$ の内接円の半径 $r$　　[4] $\triangle ABC$ の外接円の半径 $R$
  - 中文：在 $\triangle ABC$ 中，已知 $a = 2,\; b = \sqrt{2},\; c = 1$，求：[1] $\cos B, \sin B$；[2] 面积 $S$；[3] 内切圆半径 $r$；[4] 外接圆半径 $R$。
- **【考点定位】**
  - 已知三边求角、面积、内切圆半径与外接圆半径（EJU 数学Ⅰ「解三角形四件套」必考经典流程）。
- **【图解辅助（SVG 矢量图）】**

<svg viewBox="0 0 380 200" width="100%" xmlns="http://www.w3.org/2000/svg" style="max-width:380px;display:block;margin:12px auto;background:#fafbfc;border:1px solid #e1e4e8;border-radius:8px;">
  <!-- 示意图: B在左下(80,155), C在右下(280,155), a=BC=2(scale 100), c=AB=1 -> cosB=3/4, sinB=sqrt(7)/4 -->
  <!-- A = (80 + 100*0.75, 155 - 100*0.6614) = (155, 88.9) -->
  <!-- 外心O: 垂直平分BC在x=180; R = 2sqrt(14)/7 * 100 ≈ 106.9; y_O = 155 - sqrt(106.9^2 - 100^2) = 155 - 37.8 = 117.2 -->
  <!-- 内心I: r = (3sqrt(7)-sqrt(14))/14 * 100 ≈ 30.0; x_I = (a*xA + b*xB + c*xC)/(a+b+c) = (2*155+1.414*80+1*280)/4.414 = 159.3; y_I = 155 - 30.0 = 125.0 -->
  <circle cx="180" cy="117.2" r="106.9" fill="none" stroke="#1a73e8" stroke-width="1.3" stroke-dasharray="4,3"/>
  <circle cx="159.3" cy="125.0" r="30.0" fill="rgba(24,128,56,0.08)" stroke="#188038" stroke-width="1.5"/>
  <polygon points="155,88.9 80,155 280,155" fill="none" stroke="#222" stroke-width="2"/>

  <!-- 半径线 -->
  <line x1="159.3" y1="125.0" x2="159.3" y2="155" stroke="#188038" stroke-width="1.3"/>
  <line x1="180" y1="117.2" x2="280" y2="155" stroke="#1a73e8" stroke-width="1.3" stroke-dasharray="3,2"/>

  <circle cx="159.3" cy="125.0" r="2.5" fill="#188038"/>
  <circle cx="180" cy="117.2" r="2.5" fill="#1a73e8"/>

  <!-- 标注 -->
  <text x="150" y="79" font-size="13" font-weight="bold" fill="#222">A</text>
  <text x="64" y="162" font-size="13" font-weight="bold" fill="#222">B</text>
  <text x="286" y="162" font-size="13" font-weight="bold" fill="#222">C</text>
  <text x="103" y="114" font-size="12" fill="#222">c=1</text>
  <text x="220" y="113" font-size="12" fill="#222">b=√2</text>
  <text x="175" y="172" font-size="12" fill="#222">a=2</text>
  <text x="148" y="143" font-size="11" fill="#188038" font-weight="bold">r</text>
  <text x="232" y="136" font-size="11" fill="#1a73e8" font-weight="bold">R</text>
</svg>

- **【分步标准解答】**
  **[1]** 余弦定理より、
  $$\cos B = \frac{c^2 + a^2 - b^2}{2ca} = \frac{1^2 + 2^2 - (\sqrt{2})^2}{2 \cdot 1 \cdot 2} = \frac{1 + 4 - 2}{4} = \frac{3}{4}$$
  $0^\circ < B < 180^\circ$ より $\sin B > 0$ であるから、
  $$\sin B = \sqrt{1 - \cos^2 B} = \sqrt{1 - \left(\frac{3}{4}\right)^2} = \sqrt{\frac{7}{16}} = \frac{\sqrt{7}}{4}$$

  **[2]** 三角形の面積公式 $S = \dfrac{1}{2}ca\sin B$ より、
  $$S = \frac{1}{2} \cdot 1 \cdot 2 \cdot \frac{\sqrt{7}}{4} = \frac{\sqrt{7}}{4}$$

  **[3]** 内接円の半径 $r$ と面積の関係式 $S = \dfrac{1}{2}r(a+b+c)$ より、
  $$\frac{\sqrt{7}}{4} = \frac{1}{2} r (2 + \sqrt{2} + 1) = \frac{3 + \sqrt{2}}{2} r$$
  よって、分母を有理化して、
  $$r = \frac{\sqrt{7}}{2(3 + \sqrt{2})} = \frac{\sqrt{7}(3 - \sqrt{2})}{2(3 + \sqrt{2})(3 - \sqrt{2})} = \frac{\sqrt{7}(3 - \sqrt{2})}{2(9 - 2)} = \frac{3\sqrt{7} - \sqrt{14}}{14}$$
  > 💡 讲师批注：求内切圆半径 $r$ 时，遇到含根号的周长 $3 + \sqrt{2}$ 务必进行**分母有理化**（分子分母同乘 $3 - \sqrt{2}$），这是日本 EJU 填空的标准形式。

  **[4]** 正弦定理 $\dfrac{b}{\sin B} = 2R$ より、
  $$2R = \frac{\sqrt{2}}{\dfrac{\sqrt{7}}{4}} = \frac{4\sqrt{2}}{\sqrt{7}}$$
  $$R = \frac{2\sqrt{2}}{\sqrt{7}} = \frac{2\sqrt{14}}{7}$$
  > 💡 讲师批注：验算技巧——利用恒等式 $R = \dfrac{abc}{4S} = \dfrac{2 \cdot \sqrt{2} \cdot 1}{4 \cdot \frac{\sqrt{7}}{4}} = \dfrac{2\sqrt{2}}{\sqrt{7}} = \dfrac{2\sqrt{14}}{7}$，结果完全一致！
- **【最终答案】**
  **[1] $\cos B = \dfrac{3}{4},\; \sin B = \dfrac{\sqrt{7}}{4}$　　[2] $S = \dfrac{\sqrt{7}}{4}$　　[3] $r = \dfrac{3\sqrt{7} - \sqrt{14}}{14}$　　[4] $R = \dfrac{2\sqrt{14}}{7}$**

---

#### 演習問題 4-(2)
- **【原题重现与翻译】**
  - 原题：円に内接する四角形 $ABCD$ がある。$AB = 4,\; BC = 5,\; CD = 7,\; DA = 10$ のとき
    - [1] $\cos A$ の値を求めよ。
    - [2] 四角形 $ABCD$ の面積を求めよ。
  - 中文：已知圆内接四边形 $ABCD$ 满足 $AB = 4,\; BC = 5,\; CD = 7,\; DA = 10$，求：[1] $\cos A$ 的值；[2] 四边形 $ABCD$ 的面积。
- **【考点定位】**
  - 圆内接四边形对角互补（$A + C = 180^\circ$）；公共对角线双用余弦定理；多边形分割求面积。
- **【图解辅助（SVG 矢量图）】**

<svg viewBox="0 0 360 220" width="100%" xmlns="http://www.w3.org/2000/svg" style="max-width:360px;display:block;margin:12px auto;background:#fafbfc;border:1px solid #e1e4e8;border-radius:8px;">
  <!-- 圆心(170,110), 半径85 -->
  <circle cx="170" cy="110" r="85" fill="none" stroke="#1a73e8" stroke-width="1.5"/>
  <!-- 示意图四点在圆上: A左上, B左下, C右下, D右上 -->
  <!-- A: 145 deg -> (170-69.6, 110-48.8) = (100.4, 61.2) -->
  <!-- B: 205 deg -> (170-77.0, 110+35.9) = (93.0, 145.9) -->
  <!-- C: 280 deg -> (170+14.8, 110+83.7) = (184.8, 193.7) -->
  <!-- D: 20 deg  -> (170+79.9, 110-29.1) = (249.9, 80.9) -->
  <polygon points="100.4,61.2 93.0,145.9 184.8,193.7 249.9,80.9" fill="rgba(26,115,232,0.06)" stroke="#222" stroke-width="2"/>
  <line x1="93.0" y1="145.9" x2="249.9" y2="80.9" stroke="#d93025" stroke-width="1.8" stroke-dasharray="5,3"/>

  <text x="84" y="57" font-size="13" font-weight="bold" fill="#222">A</text>
  <text x="77" y="154" font-size="13" font-weight="bold" fill="#222">B</text>
  <text x="183" y="210" font-size="13" font-weight="bold" fill="#222">C (180°-A)</text>
  <text x="256" y="83" font-size="13" font-weight="bold" fill="#222">D</text>

  <text x="72" y="108" font-size="12" fill="#222">4</text>
  <text x="125" y="182" font-size="12" fill="#222">5</text>
  <text x="225" y="148" font-size="12" fill="#222">7</text>
  <text x="175" y="64" font-size="12" fill="#222">10</text>
  <text x="160" y="110" font-size="11.5" fill="#d93025" font-weight="bold">対角線 BD</text>
</svg>

- **【分步标准解答】**
  **[1]** 対角線 $BD$ を引く。
  四角形 $ABCD$ は円に内接するから、対角の和は $180^\circ$ である。すなわち
  $$C = 180^\circ - A$$
  よって、$\cos C = \cos(180^\circ - A) = -\cos A$ である。

  $\triangle ABD$ において、余弦定理より
  $$BD^2 = AB^2 + DA^2 - 2 \cdot AB \cdot DA \cos A = 4^2 + 10^2 - 2 \cdot 4 \cdot 10 \cos A = 116 - 80\cos A \quad \cdots \text{①}$$
  $\triangle CBD$ において、余弦定理より
  $$BD^2 = BC^2 + CD^2 - 2 \cdot BC \cdot CD \cos C = 5^2 + 7^2 - 2 \cdot 5 \cdot 7 (-\cos A) = 74 + 70\cos A \quad \cdots \text{②}$$
  > 💡 讲师批注：求 $\cos A$ 就必须连结**不含 $A$ 的对角线 $BD$**，把四边形拆成 $\triangle ABD$ 与 $\triangle CBD$，通过公共边 $BD^2$ 建立方程！

  ①，② より $BD^2$ を消去すると、
  $$116 - 80\cos A = 74 + 70\cos A$$
  $$150\cos A = 42$$
  $$\cos A = \frac{42}{150} = \frac{7}{25}$$

  **[2]** $0^\circ < A < 180^\circ$ より $\sin A > 0$ であるから、
  $$\sin A = \sqrt{1 - \cos^2 A} = \sqrt{1 - \left(\frac{7}{25}\right)^2} = \sqrt{\frac{625 - 49}{625}} = \sqrt{\frac{576}{625}} = \frac{24}{25}$$
  また、$\sin C = \sin(180^\circ - A) = \sin A = \dfrac{24}{25}$ である。

  よって、四角形 $ABCD$ の面積 $S$ は
  $$S = \triangle ABD + \triangle CBD = \frac{1}{2} \cdot AB \cdot DA \sin A + \frac{1}{2} \cdot BC \cdot CD \sin C$$
  $$= \frac{1}{2}(4 \cdot 10 + 5 \cdot 7) \cdot \frac{24}{25} = \frac{1}{2} \cdot 75 \cdot \frac{24}{25} = 3 \cdot 12 = 36$$
  > 💡 讲师批注：验算神器——圆内接四边形面积的**婆罗摩笈多公式（ブラーマグプタの公式）**：$s = \frac{4+5+7+10}{2} = 13$，$S = \sqrt{(13-4)(13-5)(13-7)(13-10)} = \sqrt{9 \cdot 8 \cdot 6 \cdot 3} = \sqrt{1296} = 36$，秒速验证无误！
- **【最终答案】**
  **[1] $\cos A = \dfrac{7}{25}$　　[2] $36$**

---

### 演習問題 5（三角形の辺の比・五心・中線定理）

#### 演習問題 5-(1)
- **【原题重现与翻译】**
  - 原题：$\triangle ABC$ の内心を $I$ とするとき、右の図の角 $\alpha, \beta$ を求めよ。ただし、点 $D$ は $AI$ と $BC$ の交点である。（图：$\angle BAI = 35^\circ,\; \angle ICA = 30^\circ,\; \beta = \angle BDI,\; \alpha = \angle CDI$）
  - 中文：设 $I$ 为 $\triangle ABC$ 的内心，点 $D$ 为 $AI$ 与 $BC$ 的交点。求如图所示的角 $\alpha, \beta$。
- **【考点定位】**
  - 三角形内心的定义（三条内角平分线的交点）；三角形内角和与外角定理。
- **【图解辅助（SVG 矢量图）】**

<svg viewBox="0 0 360 210" width="100%" xmlns="http://www.w3.org/2000/svg" style="max-width:360px;display:block;margin:12px auto;background:#fafbfc;border:1px solid #e1e4e8;border-radius:8px;">
  <!-- A(185, 25), B(75, 180), C(285, 180) -->
  <!-- 内心 I 约在 (180, 130); AI 延长交 BC 于 D(177.8, 180) -->
  <polygon points="185,25 75,180 285,180" fill="none" stroke="#222" stroke-width="2"/>
  <line x1="185" y1="25" x2="177.8" y2="180" stroke="#1a73e8" stroke-width="1.6"/>
  <line x1="75" y1="180" x2="180" y2="130" stroke="#188038" stroke-width="1.4" stroke-dasharray="4,2"/>
  <line x1="285" y1="180" x2="180" y2="130" stroke="#188038" stroke-width="1.4"/>

  <circle cx="180" cy="130" r="3.2" fill="#d93025"/>
  <circle cx="177.8" cy="180" r="3" fill="#1a73e8"/>

  <!-- 顶点与角度标注 -->
  <text x="180" y="18" font-size="13" font-weight="bold" fill="#222">A</text>
  <text x="58" y="188" font-size="13" font-weight="bold" fill="#222">B</text>
  <text x="292" y="188" font-size="13" font-weight="bold" fill="#222">C</text>
  <text x="187" y="131" font-size="13" font-weight="bold" fill="#d93025">I</text>
  <text x="173" y="198" font-size="13" font-weight="bold" fill="#1a73e8">D</text>

  <text x="150" y="85" font-size="12" fill="#1a73e8" font-weight="bold">35°</text>
  <text x="233" y="142" font-size="12" fill="#188038" font-weight="bold">30°</text>
  <text x="154" y="172" font-size="13" fill="#d93025" font-weight="bold">β</text>
  <text x="188" y="172" font-size="13" fill="#d93025" font-weight="bold">α</text>
</svg>

- **【分步标准解答】**
  点 $I$ は $\triangle ABC$ の内心であるから、直線 $AI, BI, CI$ はそれぞれ $\angle A, \angle B, \angle C$ の二等分線である。
  したがって、
  $$\angle BAD = \angle CAD = 35^\circ \implies \angle A = 2 \times 35^\circ = 70^\circ$$
  $$\angle ACI = \angle BCI = 30^\circ \implies \angle C = 2 \times 30^\circ = 60^\circ$$

  $\triangle ADC$ の内角の和は $180^\circ$ であるから、
  $$\alpha = \angle ADC = 180^\circ - (\angle CAD + \angle C) = 180^\circ - (35^\circ + 60^\circ) = 85^\circ$$
  > 💡 讲师批注：直接锁定右侧的 $\triangle ADC$，不需要先算 $\angle B$ 就能一步求出 $\alpha = 85^\circ$！

  また、$\alpha$ と $\beta$ は直線 $BC$ 上の補角（隣り合う角）であるから、
  $$\beta = 180^\circ - \alpha = 180^\circ - 85^\circ = 95^\circ$$
  > 💡 讲师批注：也可以利用 $\triangle ADC$ 的外角定理直接得 $\beta = \angle CAD + \angle C = 35^\circ + 60^\circ = 95^\circ$，验算 $\alpha + \beta = 85^\circ + 95^\circ = 180^\circ$，完全无误！
- **【最终答案】**
  **$\alpha = 85^\circ,\quad \beta = 95^\circ$**

---

#### 演習問題 5-(2)
- **【原题重现与翻译】**
  - 原题：$\triangle ABC$ の内心を $I$ とし、直線 $AI$ と辺 $BC$ の交点を $D$ とする。$AB = 8,\; BC = 7,\; AC = 4$ であるとき、$AI : ID$ を求めよ。
  - 中文：设 $I$ 为 $\triangle ABC$ 的内心，直线 $AI$ 与边 $BC$ 的交点为 $D$。已知 $AB = 8,\; BC = 7,\; AC = 4$，求比值 $AI : ID$。
- **【考点定位】**
  - 连续两次应用「内角平分线定理」（先在大三角形 $\triangle ABC$ 求 $BD$，再在小三角形 $\triangle ABD$ 求 $AI : ID$）。
- **【图解辅助（SVG 矢量图）】**

<svg viewBox="0 0 360 200" width="100%" xmlns="http://www.w3.org/2000/svg" style="max-width:360px;display:block;margin:12px auto;background:#fafbfc;border:1px solid #e1e4e8;border-radius:8px;">
  <!-- 比例图: B(60,165), C(270,165) (BC=7 -> 210, scale 30) -->
  <!-- AB=8->240, AC=4->120. cosB = (64+49-16)/(112) = 97/112 = 0.866; sinB = 0.500 -->
  <!-- A = (60 + 240*0.866, 165 - 240*0.5) = (267.8, 45) -->
  <!-- BD:DC = 2:1 -> D = (60 + 140, 165) = (200, 165) -->
  <!-- AI:ID = 12:7 -> I = ((7*267.8+12*200)/19, (7*45+12*165)/19) = (225.0, 120.8) -->
  <polygon points="267.8,45 60,165 270,165" fill="none" stroke="#222" stroke-width="2"/>
  <line x1="267.8" y1="45" x2="200" y2="165" stroke="#1a73e8" stroke-width="1.8"/>
  <line x1="60" y1="165" x2="225.0" y2="120.8" stroke="#d93025" stroke-width="1.6" stroke-dasharray="4,2"/>

  <circle cx="225.0" cy="120.8" r="3.5" fill="#d93025"/>
  <circle cx="200" cy="165" r="3" fill="#1a73e8"/>

  <text x="266" y="36" font-size="13" font-weight="bold" fill="#222">A</text>
  <text x="44" y="172" font-size="13" font-weight="bold" fill="#222">B</text>
  <text x="278" y="172" font-size="13" font-weight="bold" fill="#222">C</text>
  <text x="195" y="184" font-size="13" font-weight="bold" fill="#1a73e8">D</text>
  <text x="233" y="123" font-size="13" font-weight="bold" fill="#d93025">I</text>

  <text x="145" y="96" font-size="12" fill="#222">AB = 8</text>
  <text x="276" y="108" font-size="12" fill="#222">AC = 4</text>
  <text x="115" y="182" font-size="11.5" fill="#1a73e8">BD = 14/3</text>
  <text x="225" y="182" font-size="11.5" fill="#555">DC = 7/3</text>
</svg>

- **【分步标准解答】**
  点 $I$ は $\triangle ABC$ の内心であるから、線分 $AD$ は $\angle A$ の二等分線である。
  内角の二等分線の定理より、
  $$BD : DC = AB : AC = 8 : 4 = 2 : 1$$
  したがって、$BC = 7$ より線分 $BD$ の長さは
  $$BD = \frac{2}{2 + 1} BC = \frac{2}{3} \times 7 = \frac{14}{3}$$
  > 💡 讲师批注：第一步先在 $\triangle ABC$ 中求出 $BD$ 的具体长度。

  次に、$\triangle ABD$ に着目すると、線分 $BI$ は $\angle B$ の二等分線である。
  再び内角の二等分線の定理より、
  $$AI : ID = BA : BD = 8 : \frac{14}{3}$$
  両辺に $3$ を掛けて整数比に直すと、
  $$AI : ID = 24 : 14 = 12 : 7$$
  > 💡 讲师批注：EJU 高频二级结论（选择题/填空题秒杀公式）：若 $I$ 为内心，$AI$ 交 $BC$ 于 $D$，则恒有 $AI : ID = (AB + AC) : BC$！代入本题：$(8 + 4) : 7 = 12 : 7$，一秒验算！
- **【最终答案】**
  **$AI : ID = 12 : 7$**

---

#### 演習問題 5-(3)
- **【原题重现与翻译】**
  - 原题：右の図の $\triangle ABC$ で、点 $D, E$ はそれぞれ辺 $BC, CA$ の中点（※原教材误印为「中心」）である。また、$AD$ と $BE$ の交点を $F$、線分 $AF$ の中点を $G$、$CG$ と $BE$ の交点を $H$ とする。$BE = 9$ のとき
    - [1] 線分 $FH$ の長さを求めよ。
    - [2] 面積について、$\triangle EBC = \square \triangle FBD$ である。
  - 中文：在如图所示的 $\triangle ABC$ 中，点 $D, E$ 分别为边 $BC, CA$ 的中点。设 $AD$ 与 $BE$ 的交点为 $F$，线段 $AF$ 的中点为 $G$，$CG$ 与 $BE$ 的交点为 $H$。当 $BE = 9$ 时，求：[1] 线段 $FH$ 的长；[2] 面积关系 $\triangle EBC = \square \triangle FBD$ 中的系数。
  > ⚠️ **教材勘误提示**：原教材第 99 页（`page_0100.jpg`）题干将「辺 $BC, CA$ の**中点**である」误印为「辺 $BC, CA$ の**中心**である」，应修正为「中点」。
- **【考点定位】**
  - 三角形重心的识别与性质（中线 $2:1$ 分割）的**嵌套应用**（大三角形重心 $F$ + 局部三角形重心 $H$）；三角形面积比。
- **【图解辅助（SVG 矢量图）】**

<svg viewBox="0 0 360 220" width="100%" xmlns="http://www.w3.org/2000/svg" style="max-width:360px;display:block;margin:12px auto;background:#fafbfc;border:1px solid #e1e4e8;border-radius:8px;">
  <!-- A(185, 25), B(75, 190), C(285, 190) -->
  <!-- D=(180, 190), E=(235, 107.5) -->
  <!-- 重心 F = ((185+75+285)/3, (25+190+190)/3) = (181.7, 135) -->
  <!-- AF 中点 G = (183.3, 80) -->
  <!-- △AFC 的重心 H = ((185+181.7+285)/3, (25+135+190)/3) = (217.2, 116.7) -->
  <!-- 高亮 △AFC -->
  <polygon points="185,25 181.7,135 285,190" fill="rgba(26,115,232,0.08)" stroke="none"/>
  <polygon points="185,25 75,190 285,190" fill="none" stroke="#222" stroke-width="2"/>

  <!-- 线段 -->
  <line x1="185" y1="25" x2="180" y2="190" stroke="#222" stroke-width="1.5"/>
  <line x1="75" y1="190" x2="235" y2="107.5" stroke="#1a73e8" stroke-width="1.8"/>
  <line x1="285" y1="190" x2="183.3" y2="80" stroke="#d93025" stroke-width="1.6"/>
  <line x1="181.7" y1="135" x2="285" y2="190" stroke="#888" stroke-width="1.2" stroke-dasharray="4,3"/>

  <!-- 关键点 -->
  <circle cx="181.7" cy="135" r="3.5" fill="#1a73e8"/>
  <circle cx="183.3" cy="80" r="3.2" fill="#d93025"/>
  <circle cx="217.2" cy="116.7" r="3.5" fill="#d93025"/>

  <!-- 标注 -->
  <text x="180" y="18" font-size="13" font-weight="bold" fill="#222">A</text>
  <text x="58" y="196" font-size="13" font-weight="bold" fill="#222">B</text>
  <text x="292" y="196" font-size="13" font-weight="bold" fill="#222">C</text>
  <text x="175" y="208" font-size="13" font-weight="bold" fill="#222">D</text>
  <text x="242" y="108" font-size="13" font-weight="bold" fill="#222">E</text>
  <text x="166" y="136" font-size="13" font-weight="bold" fill="#1a73e8">F</text>
  <text x="167" y="83" font-size="13" font-weight="bold" fill="#d93025">G</text>
  <text x="218" y="135" font-size="13" font-weight="bold" fill="#d93025">H</text>

  <text x="16" y="34" font-size="11.5" fill="#1a73e8">F = △ABC の重心</text>
  <text x="16" y="52" font-size="11.5" fill="#d93025">H = △AFC の重心</text>
</svg>

- **【分步标准解答】**
  **[1]** 点 $D, E$ はそれぞれ辺 $BC, CA$ の中点であるから、線分 $AD, BE$ は $\triangle ABC$ の中線である。
  したがって、その交点 $F$ は **$\triangle ABC$ の重心** であり、
  $$BF : FE = 2 : 1$$
  $BE = 9$ であるから、
  $$FE = \frac{1}{2 + 1} BE = \frac{1}{3} \times 9 = 3$$

  次に、**$\triangle AFC$**（図の薄青色部分）に着目する。
  - 点 $E$ は辺 $CA$ の中点であるから、線分 $FE$ は $\triangle AFC$ の中線である。
  - 点 $G$ は辺 $AF$ の中点であるから、線分 $CG$ も $\triangle AFC$ の中線である。
  よって、その交点 $H$ は **$\triangle AFC$ の重心** である！
  > 💡 讲师批注：本题最惊艳的几何洞察在于连结辅助线 $FC$ 后，立刻看出 **$H$ 正是 $\triangle AFC$ 的重心**！如果没看出来，也可以对 $\triangle AFE$ 和截线 $C$-$H$-$G$ 使用梅涅劳斯定理：$\frac{AG}{GF}\cdot\frac{FH}{HE}\cdot\frac{EC}{CA} = 1 \Rightarrow 1 \cdot \frac{FH}{HE}\cdot \frac{1}{2} = 1 \Rightarrow FH:HE = 2:1$，同样轻松得出结论。

  重心の性質より $FH : HE = 2 : 1$ であるから、
  $$FH = \frac{2}{2 + 1} FE = \frac{2}{3} \times 3 = 2$$

  **[2]** $\triangle ABC$ の面積を $S$ とおく。
  - 点 $E$ は辺 $AC$ の中点であるから、底辺の比 $CE : CA = 1 : 2$ より
    $$\triangle EBC = \frac{1}{2} S$$
  - 点 $D$ は辺 $BC$ の中点であるから、$\triangle ABD = \dfrac{1}{2} S$。さらに重心 $F$ は中線 $AD$ を $AF : FD = 2 : 1$ に内分するので、$FD : AD = 1 : 3$ より
    $$\triangle FBD = \frac{1}{3} \triangle ABD = \frac{1}{3} \cdot \frac{1}{2} S = \frac{1}{6} S$$
  したがって、
  $$\frac{\triangle EBC}{\triangle FBD} = \frac{\frac{1}{2}S}{\frac{1}{6}S} = 3 \implies \triangle EBC = 3 \triangle FBD$$
- **【最终答案】**
  **[1] $FH = 2$　　[2] $3$**

---

#### 演習問題 5-(4)
- **【原题重现与翻译】**
  - 原题：鋭角三角形 $ABC$ の外心を $O$、垂心を $H$ とし、$O$ から辺 $BC$ に下ろした垂線を $OM$ とする。また、$\triangle ABC$ の外接円の周上に点 $D$ をとり、線分 $CD$ が円の直径になるようにする。この時、次のことを証明せよ。
    - [1] $DB = 2OM$
    - [2] 四角形 $ADBH$ は平行四辺形である。
    - [3] $AH = 2OM$
  - 中文：设锐角三角形 $ABC$ 的外心为 $O$、垂心为 $H$，由 $O$ 向边 $BC$ 作垂线 $OM$。在 $\triangle ABC$ 的外接圆周上取点 $D$，使线段 $CD$ 为圆的直径。此时证明：
    - [1] $DB = 2OM$；[2] 四边形 $ADBH$ 是平行四边形；[3] $AH = 2OM$。
- **【考点定位】**
  - 欧拉线（オイラー線）证明的前置核心定理（$AH = 2OM$）；外心・垂心定义、圆周角定理（半圆所对圆周角为 $90^\circ$）、中点连结定理（中位线定理）。
- **【图解辅助（SVG 矢量图）】**

<svg viewBox="0 0 360 240" width="100%" xmlns="http://www.w3.org/2000/svg" style="max-width:360px;display:block;margin:12px auto;background:#fafbfc;border:1px solid #e1e4e8;border-radius:8px;">
  <!-- 外接圆心 O(180, 120), 半径 R=95 -->
  <circle cx="180" cy="120" r="95" fill="none" stroke="#999" stroke-width="1.3"/>
  <!-- A: 112 deg -> (180-35.6, 120-88.1) = (144.4, 31.9) -->
  <!-- B: 215 deg -> (180-77.8, 120+54.5) = (102.2, 174.5) -->
  <!-- C: 325 deg -> (180+77.8, 120+54.5) = (257.8, 174.5) -->
  <!-- 直径 CD -> D = 145 deg -> (180-77.8, 120-54.5) = (102.2, 65.5) -->
  <!-- BC 中点 M = (180, 174.5) -->
  <!-- 垂心 H: x_H = x_A = 144.4; 且 AH = 2*OM = 2*(174.5-120) = 109.0 -> y_H = 31.9 + 109.0 = 140.9 -->
  <!-- 平行四边形 ADBH 高亮 -->
  <polygon points="144.4,31.9 102.2,65.5 102.2,174.5 144.4,140.9" fill="rgba(26,115,232,0.10)" stroke="#1a73e8" stroke-width="1.8"/>
  <!-- △ABC -->
  <polygon points="144.4,31.9 102.2,174.5 257.8,174.5" fill="none" stroke="#222" stroke-width="2"/>
  <!-- 直径 CD -->
  <line x1="257.8" y1="174.5" x2="102.2" y2="65.5" stroke="#d93025" stroke-width="1.5" stroke-dasharray="5,3"/>
  <!-- OM -->
  <line x1="180" y1="120" x2="180" y2="174.5" stroke="#188038" stroke-width="1.8"/>
  <!-- 高线 AH 延长到 BC -->
  <line x1="144.4" y1="140.9" x2="144.4" y2="174.5" stroke="#888" stroke-width="1.2" stroke-dasharray="3,3"/>

  <!-- 点 -->
  <circle cx="180" cy="120" r="3" fill="#188038"/>
  <circle cx="144.4" cy="140.9" r="3" fill="#1a73e8"/>
  <circle cx="180" cy="174.5" r="2.8" fill="#188038"/>

  <!-- 标注 -->
  <text x="140" y="23" font-size="13" font-weight="bold" fill="#222">A</text>
  <text x="86" y="182" font-size="13" font-weight="bold" fill="#222">B</text>
  <text x="263" y="182" font-size="13" font-weight="bold" fill="#222">C</text>
  <text x="86" y="64" font-size="13" font-weight="bold" fill="#d93025">D</text>
  <text x="187" y="122" font-size="13" font-weight="bold" fill="#188038">O</text>
  <text x="176" y="191" font-size="13" font-weight="bold" fill="#188038">M</text>
  <text x="150" y="146" font-size="13" font-weight="bold" fill="#1a73e8">H</text>
</svg>

- **【分步标准解答】**
  **[1]** $O$ は $\triangle ABC$ の外心であるから、$OB = OC$ である。
  よって $\triangle OBC$ は二等辺三角形であり、頂点 $O$ から底辺 $BC$ に下ろした垂線 $OM$ の足 $M$ は、辺 $BC$ の中点である（$BM = MC$）。
  また、線分 $CD$ は外接円の直径であるから、円の中心 $O$ は線分 $CD$ の中点である（$CO = OD$）。
  したがって、$\triangle CDB$ において、中点連結定理より
  $$OM \parallel DB \quad \text{かつ} \quad OM = \frac{1}{2} DB$$
  ゆえに、$DB = 2OM$ が成り立つ。

  **[2]** 線分 $CD$ は外接円の直径であるから、半円の弧に対する円周角は $90^\circ$ であり、
  $$\angle CAD = 90^\circ \implies DA \perp AC$$
  $$\angle CBD = 90^\circ \implies DB \perp BC$$
  一方、点 $H$ は $\triangle ABC$ の垂心であるから、
  $$AH \perp BC, \qquad BH \perp AC$$
  したがって、
  - $AH \perp BC$ かつ $DB \perp BC$ より、$AH \parallel DB$
  - $BH \perp AC$ かつ $DA \perp AC$ より、$BH \parallel DA$
  2組の対辺がそれぞれ平行であるから、四角形 $ADBH$ は平行四辺形である。
  > 💡 讲师批注：证明四边形为平行四边形的标准套路之一——「分别垂直于同一条直线的两条直线互相平行」，从而得到两组对边分别平行！

  **[3]** [2] より、四角形 $ADBH$ は平行四辺形であるから、対辺の長さは等しく
  $$AH = DB$$
  これと [1] の結果 $DB = 2OM$ を合わせると、
  $$AH = 2OM$$
  が成り立つ。（証明終）
- **【最终答案】**
  **証明完了（$AH = DB = 2OM$，此即著名的欧拉线核心关系）**

---

#### 演習問題 5-(5)
- **【原题重现与翻译】**
  - 原题：$\triangle ABC$ において、辺 $BC$ の中点を $M$、線分 $BM$ の中点を $D$ とするとき、
    $$3AB^2 + AC^2 = 4AD^2 + 12BD^2$$
    が成り立つことを示せ。
  - 中文：在 $\triangle ABC$ 中，设边 $BC$ 的中点为 $M$，线段 $BM$ 的中点为 $D$，证明 $3AB^2 + AC^2 = 4AD^2 + 12BD^2$ 成立。
- **【考点定位】**
  - 中线定理（パップスの定理）的二次嵌套与消元（消去中间量 $AM^2$）。
- **【图解辅助（SVG 矢量图）】**

<svg viewBox="0 0 360 180" width="100%" xmlns="http://www.w3.org/2000/svg" style="max-width:360px;display:block;margin:12px auto;background:#fafbfc;border:1px solid #e1e4e8;border-radius:8px;">
  <!-- B(50,145), C(310,145) -> M(180,145), D(115,145); A(155,35) -->
  <polygon points="155,35 50,145 310,145" fill="none" stroke="#222" stroke-width="2"/>
  <line x1="155" y1="35" x2="180" y2="145" stroke="#1a73e8" stroke-width="1.6"/>
  <line x1="155" y1="35" x2="115" y2="145" stroke="#d93025" stroke-width="1.8"/>

  <circle cx="115" cy="145" r="3" fill="#d93025"/>
  <circle cx="180" cy="145" r="3" fill="#1a73e8"/>

  <text x="150" y="26" font-size="13" font-weight="bold" fill="#222">A</text>
  <text x="38" y="152" font-size="13" font-weight="bold" fill="#222">B</text>
  <text x="316" y="152" font-size="13" font-weight="bold" fill="#222">C</text>
  <text x="110" y="164" font-size="13" font-weight="bold" fill="#d93025">D</text>
  <text x="174" y="164" font-size="13" font-weight="bold" fill="#1a73e8">M</text>

  <text x="76" y="139" font-size="11" fill="#555">x</text>
  <text x="142" y="139" font-size="11" fill="#555">x</text>
  <text x="238" y="139" font-size="11" fill="#555">2x</text>
</svg>

- **【分步标准解答】**
  まず、$\triangle ABC$ において、点 $M$ は辺 $BC$ の中点であるから、中線定理より
  $$AB^2 + AC^2 = 2(AM^2 + BM^2) \quad \cdots \text{①}$$
  次に、$\triangle ABM$ において、点 $D$ は辺 $BM$ の中点であるから、中線定理より
  $$AB^2 + AM^2 = 2(AD^2 + BD^2) \quad \cdots \text{②}$$
  > 💡 讲师批注：观察目标等式 $3AB^2 + AC^2 = 4AD^2 + 12BD^2$，里面**不含 $AM$ 也不含 $BM$**！所以思路极其明确：把 ② 式变形解出 $2AM^2$，并利用 $BM = 2BD$，一起代入 ① 式消去 $AM^2$ 与 $BM^2$！

  ② より、
  $$AM^2 = 2AD^2 + 2BD^2 - AB^2 \implies 2AM^2 = 4AD^2 + 4BD^2 - 2AB^2$$
  また、点 $D$ は線分 $BM$ の中点であるから $BM = 2BD$ であり、
  $$BM^2 = (2BD)^2 = 4BD^2$$
  これらを ① に代入すると、
  $$AB^2 + AC^2 = (4AD^2 + 4BD^2 - 2AB^2) + 2(4BD^2)$$
  $$AB^2 + AC^2 = 4AD^2 + 12BD^2 - 2AB^2$$
  $-2AB^2$ を左辺に移項して整理すると、
  $$3AB^2 + AC^2 = 4AD^2 + 12BD^2$$
  よって、等式は成り立つ。（証明終）
- **【最终答案】**
  **証明完了（对 $\triangle ABC$ 与 $\triangle ABM$ 两次应用中线定理并消去 $AM^2$）**

---

#### 演習問題 5-(6)
- **【原题重现与翻译】**
  - 原题：$\triangle ABC$ の3つの中線を $AD, BE, CF$ とするとき、
    - [1] $2AD < AB + AC$ が成り立つことを証明せよ。
    - [2] $AD + BE + CF < AB + BC + CA$ が成り立つことを証明せよ。（※原教材误印为 `AB + +BC + CA`）
  - 中文：设 $\triangle ABC$ 的三条中线为 $AD, BE, CF$，证明：
    - [1] $2AD < AB + AC$；[2] $AD + BE + CF < AB + BC + CA$。
  > ⚠️ **教材勘误提示**：原教材第 100 页（`page_0101.jpg`）[2] 题干多印了一个加号（`AB + +BC + CA`），应为 `AB + BC + CA`。
- **【考点定位】**
  - 几何辅助线经典技法「倍长中线法」；三角形三边不等关系（两边之和大于第三边）；轮换对称求和。
- **【图解辅助（SVG 矢量图）】**

<svg viewBox="0 0 360 220" width="100%" xmlns="http://www.w3.org/2000/svg" style="max-width:360px;display:block;margin:12px auto;background:#fafbfc;border:1px solid #e1e4e8;border-radius:8px;">
  <!-- A(155, 25), B(75, 115), C(255, 115) -> D(165, 115) -->
  <!-- 倍长 AD 至 G: G = 2D - A = (175, 205) -->
  <polygon points="155,25 75,115 255,115" fill="rgba(26,115,232,0.06)" stroke="#222" stroke-width="2"/>
  <line x1="155" y1="25" x2="165" y2="115" stroke="#1a73e8" stroke-width="1.8"/>
  <!-- 辅助线延长及连线 -->
  <line x1="165" y1="115" x2="175" y2="205" stroke="#d93025" stroke-width="1.8" stroke-dasharray="5,3"/>
  <line x1="75" y1="115" x2="175" y2="205" stroke="#d93025" stroke-width="1.6" stroke-dasharray="5,3"/>
  <line x1="255" y1="115" x2="175" y2="205" stroke="#aaa" stroke-width="1.2" stroke-dasharray="4,3"/>

  <circle cx="165" cy="115" r="3" fill="#1a73e8"/>
  <circle cx="175" cy="205" r="3" fill="#d93025"/>

  <text x="150" y="18" font-size="13" font-weight="bold" fill="#222">A</text>
  <text x="58" y="120" font-size="13" font-weight="bold" fill="#222">B</text>
  <text x="262" y="120" font-size="13" font-weight="bold" fill="#222">C</text>
  <text x="172" y="110" font-size="13" font-weight="bold" fill="#1a73e8">D</text>
  <text x="182" y="210" font-size="13" font-weight="bold" fill="#d93025">G (AD = DG)</text>
  <text x="86" y="175" font-size="12" fill="#d93025" font-weight="bold">BG = AC</text>
</svg>

- **【分步标准解答】**
  **[1]** 中線 $AD$ を $D$ の方に延長し、$AD = DG$ となる点 $G$ をとり、線分 $BG, CG$ を結ぶ。
  四角形 $ABGC$ において、対角線 $BC$ と $AG$ はそれぞれの中点 $D$ で交わる（$BD = DC,\; AD = DG$）から、四角形 $ABGC$ は平行四辺形である。
  したがって、対辺の長さは等しく、
  $$BG = AC$$
  ここで、$\triangle ABG$ に着目すると、三角形の 3 辺の大小関係（2 辺の和は他の 1 辺より大きい）より、
  $$AG < AB + BG$$
  $AG = 2AD$ および $BG = AC$ を代入すると、
  $$2AD < AB + AC$$
  が成り立つ。
  > 💡 讲师批注：「见到中线要证 $2AD < AB + AC$」，**倍长中线构造平行四边形**是平面几何最经典的破局辅助线，直接把 $2AD$ 和 $AC$ 搬进同一个三角形 $\triangle ABG$ 中！

  **[2]** [1] と全く同様にして、他の2つの中線 $BE, CF$ についても次の不等式が成り立つ：
  $$2BE < BC + BA$$
  $$2CF < CA + CB$$
  [1] の結果と合わせた 3 つの不等式の辺々を足し合わせると、
  $$2AD + 2BE + 2CF < (AB + AC) + (BC + BA) + (CA + CB)$$
  $$2(AD + BE + CF) < 2(AB + BC + CA)$$
  両辺を $2$ で割ると、
  $$AD + BE + CF < AB + BC + CA$$
  が成り立つ。（証明終）
- **【最终答案】**
  **証明完了（[1] 倍长中线法 + 三角形三边关系；[2] 轮换三式相加除以 2）**

---

### 演習問題 6（チェバの定理・メネラウスの定理）

#### 演習問題 6-(1)
- **【原题重现与翻译】**
  - 原题：1辺の長さが $7$ の正三角形 $ABC$ がある。辺 $AB, AC$ 上に $AD = 3,\; AE = 6$ となるように 2 点 $D, E$ をとる。この時、$BE, CD$ の交点を $F$、直線 $AF$ と $BC$ との交点を $G$ とする。線分 $CG$ の長さを求めよ。
  - 中文：已知边长为 $7$ 的等边三角形 $ABC$，在边 $AB, AC$ 上分别取点 $D, E$ 使 $AD = 3,\; AE = 6$。设 $BE$ 与 $CD$ 的交点为 $F$，直线 $AF$ 与 $BC$ 的交点为 $G$，求线段 $CG$ 的长。
- **【考点定位】**
  - 切瓦定理（チェバの定理）的直接应用求线段比与线段长。
- **【图解辅助（SVG 矢量图）】**

<svg viewBox="0 0 360 220" width="100%" xmlns="http://www.w3.org/2000/svg" style="max-width:360px;display:block;margin:12px auto;background:#fafbfc;border:1px solid #e1e4e8;border-radius:8px;">
  <!-- 等边三角形 A(180,25), B(80,198), C(280,198) 边长200 -->
  <!-- AD:DB = 3:4 -> D = (180 - 100*3/7, 25 + 173*3/7) = (137.1, 99.1) -->
  <!-- AE:EC = 6:1 -> E = (180 + 100*6/7, 25 + 173*6/7) = (265.7, 173.3) -->
  <!-- BG:GC = 8:1 -> G = (80 + 200*8/9, 198) = (257.8, 198) -->
  <!-- 交点 F: 由 BE 与 CD 求交, 或用重心坐标权重: A:1, B:3/4? 实际 A:3, B:4(不对: AD:DB=3:4 -> wA:wB=4:3; AE:EC=6:1 -> wA:wC=1:6 -> 统一 wA=4, wB=3, wC=24; 校验 BG:GC = wC:wB = 24:3 = 8:1!) -->
  <!-- F = (4*A + 3*B + 24*C)/31 = ((720+240+6720)/31, (100+594+4752)/31) = (247.7, 175.7) -->
  <polygon points="180,25 80,198 280,198" fill="none" stroke="#222" stroke-width="2"/>
  <line x1="80" y1="198" x2="265.7" y2="173.3" stroke="#1a73e8" stroke-width="1.5"/>
  <line x1="280" y1="198" x2="137.1" y2="99.1" stroke="#1a73e8" stroke-width="1.5"/>
  <line x1="180" y1="25" x2="257.8" y2="198" stroke="#d93025" stroke-width="1.8"/>

  <circle cx="247.7" cy="175.7" r="3.2" fill="#d93025"/>
  <circle cx="257.8" cy="198" r="3" fill="#d93025"/>

  <text x="175" y="18" font-size="13" font-weight="bold" fill="#222">A</text>
  <text x="64" y="205" font-size="13" font-weight="bold" fill="#222">B</text>
  <text x="287" y="205" font-size="13" font-weight="bold" fill="#222">C</text>
  <text x="120" y="96" font-size="13" font-weight="bold" fill="#1a73e8">D</text>
  <text x="274" y="175" font-size="13" font-weight="bold" fill="#1a73e8">E</text>
  <text x="234" y="168" font-size="13" font-weight="bold" fill="#d93025">F</text>
  <text x="252" y="214" font-size="13" font-weight="bold" fill="#d93025">G</text>

  <text x="145" y="58" font-size="11.5" fill="#333">3</text>
  <text x="98" y="152" font-size="11.5" fill="#333">4</text>
  <text x="230" y="102" font-size="11.5" fill="#333">6</text>
  <text x="282" y="191" font-size="11" fill="#333">1</text>
  <text x="165" y="213" font-size="11.5" fill="#d93025">BG : GC = 8 : 1</text>
</svg>

- **【分步标准解答】**
  $\triangle ABC$ は 1 辺の長さが $7$ の正三角形であるから、
  $$DB = AB - AD = 7 - 3 = 4$$
  $$EC = AC - AE = 7 - 6 = 1$$

  $\triangle ABC$ と内部の点 $F$ に対して、チェバの定理を適用すると、
  $$\frac{BG}{GC} \cdot \frac{CE}{EA} \cdot \frac{AD}{DB} = 1$$
  各線分の長さを代入すると、
  $$\frac{BG}{GC} \cdot \frac{1}{6} \cdot \frac{3}{4} = 1$$
  $$\frac{BG}{GC} \cdot \frac{1}{8} = 1 \implies \frac{BG}{GC} = 8$$
  すなわち、$BG : GC = 8 : 1$ である。
  > 💡 讲师批注：切瓦定理书写时一定要按「$B \to G \to C \to E \to A \to D \to B$」绕三角形一圈首尾相连，绝不会写反分子分母！

  したがって、$BC = 7$ より線分 $CG$ の長さは
  $$CG = \frac{1}{8 + 1} BC = \frac{1}{9} \times 7 = \frac{7}{9}$$
- **【最终答案】**
  **$CG = \dfrac{7}{9}$**

---

#### 演習問題 6-(2)
- **【原题重现与翻译】**
  - 原题：$\triangle ABC$ において、辺 $AB$ 上と辺 $AC$ の延長上にそれぞれ点 $E, F$ をとり、$AE : EB = 1 : 2,\; AF : FC = 3 : 1$ とする。直線 $EF$ と直線 $BC$ との交点を $D$ とするとき、$BD : DC,\; ED : DF$ をそれぞれ求めよ。
  - 中文：在 $\triangle ABC$ 中，在边 $AB$ 上和边 $AC$ 的延长线上分别取点 $E, F$，使 $AE : EB = 1 : 2,\; AF : FC = 3 : 1$。设直线 $EF$ 与直线 $BC$ 的交点为 $D$，分别求 $BD : DC$ 与 $ED : DF$。
- **【考点定位】**
  - 梅涅劳斯定理（メネラウスの定理）的**双重视角切换**（求 $BD : DC$ 时把 $\triangle ABC$ 作为主体三角形；求 $ED : DF$ 时把 $\triangle AEF$ 作为主体三角形！）。
- **【图解辅助（SVG 矢量图）】**

<svg viewBox="0 0 380 230" width="100%" xmlns="http://www.w3.org/2000/svg" style="max-width:380px;display:block;margin:12px auto;background:#fafbfc;border:1px solid #e1e4e8;border-radius:8px;">
  <!-- 精确坐标映射: A(70, 35), B(310, 155) [向量(240,120)], C(120, 145) [向量(50,110)] -->
  <!-- E 在 AB 上 AE:EB=1:2 -> E = (70+80, 35+40) = (150, 75) -->
  <!-- F 在 AC 延长线上 AF:FC=3:1 -> AC:CF=2:1 -> F = A + 1.5*(C-A) = (70+75, 35+165) = (145, 200) -->
  <!-- 交点 D 在 BC 上 BD:DC=6:1 -> D = (1*B + 6*C)/7 = ((310+720)/7, (155+870)/7) = (147.1, 146.4) -->
  <!-- 校验 D 在 EF 上: E(150,75), F(145,200), ED:DF=4:3 -> (3*150+4*145)/7 = 147.1, (3*75+4*200)/7 = 146.4! 完美精确! -->
  <polygon points="70,35 310,155 120,145" fill="rgba(26,115,232,0.06)" stroke="#222" stroke-width="2"/>
  <!-- 延长 AC 至 F -->
  <line x1="120" y1="145" x2="145" y2="200" stroke="#222" stroke-width="1.6" stroke-dasharray="4,3"/>
  <!-- 截线 E-D-F -->
  <line x1="150" y1="75" x2="145" y2="200" stroke="#d93025" stroke-width="2"/>

  <circle cx="150" cy="75" r="3.2" fill="#d93025"/>
  <circle cx="145" cy="200" r="3.2" fill="#d93025"/>
  <circle cx="147.1" cy="146.4" r="3.5" fill="#188038"/>

  <text x="54" y="34" font-size="13" font-weight="bold" fill="#222">A</text>
  <text x="317" y="160" font-size="13" font-weight="bold" fill="#222">B</text>
  <text x="103" y="152" font-size="13" font-weight="bold" fill="#222">C</text>
  <text x="157" y="70" font-size="13" font-weight="bold" fill="#d93025">E</text>
  <text x="153" y="207" font-size="13" font-weight="bold" fill="#d93025">F</text>
  <text x="156" y="142" font-size="13" font-weight="bold" fill="#188038">D</text>

  <!-- 比例提示 -->
  <text x="105" y="49" font-size="11.5" fill="#1a73e8">1</text>
  <text x="235" y="110" font-size="11.5" fill="#1a73e8">2</text>
  <text x="80" y="96" font-size="11.5" fill="#555">AC:CF = 2:1</text>
  <text x="210" y="38" font-size="11.5" fill="#d93025">① △ABC + 截線 EF → BD:DC</text>
  <text x="210" y="56" font-size="11.5" fill="#188038">② △AEF + 截線 BC → ED:DF</text>
</svg>

- **【分步标准解答】**
  点 $F$ は辺 $AC$ の延長上にあり、$AF : FC = 3 : 1$ であるから、$AF > FC$ より点 $F$ は辺 $AC$ の点 $C$ の側の延長上にある。
  したがって、$AC : CF = (3 - 1) : 1 = 2 : 1$ である。
  > 💡 讲师批注：画图前务必先确认点 $F$ 在哪一侧延长线上！因为 $AF : FC = 3 : 1$（即 $AF > FC$），点 $F$ 只能在 $C$ 侧延长线上（若在 $A$ 侧则必有 $AF < FC$，矛盾）。

  **① $BD : DC$ を求める**：
  **$\triangle ABC$ と直線 $EF$** について、メネラウスの定理を適用すると、
  $$\frac{BD}{DC} \cdot \frac{CF}{FA} \cdot \frac{AE}{EB} = 1$$
  $CF : FA = 1 : 3$、$AE : EB = 1 : 2$ を代入して、
  $$\frac{BD}{DC} \cdot \frac{1}{3} \cdot \frac{1}{2} = 1 \implies \frac{BD}{DC} = 6$$
  よって、
  $$BD : DC = 6 : 1$$

  **② $ED : DF$ を求める**：
  視点を切り替え、**$\triangle AEF$ と直線 $BC$**（辺 $AE$ の延長上に点 $B$、辺 $EF$ 上に点 $D$、辺 $FA$ 上に点 $C$ がある）について、メネラウスの定理を適用すると、
  $$\frac{AB}{BE} \cdot \frac{ED}{DF} \cdot \frac{FC}{CA} = 1$$
  ここで、
  - $AE : EB = 1 : 2$ より $AB : BE = (1 + 2) : 2 = 3 : 2$
  - $AC : CF = 2 : 1$ より $FC : CA = 1 : 2$
  これらを代入すると、
  $$\frac{3}{2} \cdot \frac{ED}{DF} \cdot \frac{1}{2} = 1 \implies \frac{ED}{DF} = \frac{4}{3}$$
  よって、
  $$ED : DF = 4 : 3$$
  > 💡 讲师批注：梅涅劳斯定理中「一个三角形 + 一条截线」一共构成 4 条直线（完全四边形），**任选其中 3 条直线作为三角形，剩下 1 条作为截线**，可以写出 4 个不同的梅涅劳斯等式！要哪条线段上的比例，就把哪条线段选为三角形的边！
- **【最终答案】**
  **$BD : DC = 6 : 1,\qquad ED : DF = 4 : 3$**

---

#### 演習問題 6-(3)
- **【原题重现与翻译】**
  - 原题：面積が $1$ に等しい $\triangle ABC$ において、辺 $BC, CA, AB$ を $2 : 1$ に内分する点をそれぞれ $L, M, N$ とし、線分 $AL$ と $BM$、$BM$ と $CN$、$CN$ と $AL$ の交点をそれぞれ $P, Q, R$ とするとき
    - [1] $AP : PR : RL = \square : \square : 1$ である。
    - [2] $\triangle PQR$ の面積は $\square$ である。
  - 中文：在面积为 $1$ 的 $\triangle ABC$ 中，将边 $BC, CA, AB$ 均按 $2 : 1$ 内分的点分别记为 $L, M, N$，线段 $AL$ 与 $BM$、$BM$ 与 $CN$、$CN$ 与 $AL$ 的交点分别记为 $P, Q, R$。求：
    - [1] $AP : PR : RL = \square : \square : 1$；
    - [2] $\triangle PQR$ 的面积。
- **【考点定位】**
  - 梅涅劳斯定理求连比（同一线段上两次定位分点）；对称性割补求面积（经典劳斯定理 Routh's Theorem 特例，EJU 极高频压轴母题）。
- **【图解辅助（SVG 矢量图）】**

<svg viewBox="0 0 380 230" width="100%" xmlns="http://www.w3.org/2000/svg" style="max-width:380px;display:block;margin:12px auto;background:#fafbfc;border:1px solid #e1e4e8;border-radius:8px;">
  <!-- 等边三角形便于对称展示: A(190,25), B(80,205), C(300,205) -->
  <!-- L 分 BC 为 2:1 -> L = (80 + 220*2/3, 205) = (226.7, 205) -->
  <!-- M 分 CA 为 2:1 -> M = (300 - 110*2/3, 205 - 180*2/3) = (226.7, 85) -->
  <!-- N 分 AB 为 2:1 -> N = (190 - 110*2/3, 25 + 180*2/3) = (116.7, 145) -->
  <!-- P = AL ∩ BM: AP:PL = 3:4 -> P = (4*A + 3*L)/7 = ((760+680)/7, (100+615)/7) = (205.7, 102.1) -->
  <!-- Q = BM ∩ CN: BQ:QM = 3:4 -> Q = (4*B + 3*M)/7 = ((320+680)/7, (820+255)/7) = (142.9, 153.6) -->
  <!-- R = CN ∩ AL: CR:RN = 3:4 -> R = (4*C + 3*N)/7 = ((1200+350)/7, (820+435)/7) = (221.4, 179.3) -->
  <!-- 中央 △PQR 高亮 -->
  <polygon points="205.7,102.1 142.9,153.6 221.4,179.3" fill="rgba(217,48,37,0.16)" stroke="#d93025" stroke-width="2"/>
  <polygon points="190,25 80,205 300,205" fill="none" stroke="#222" stroke-width="2"/>

  <line x1="190" y1="25" x2="226.7" y2="205" stroke="#1a73e8" stroke-width="1.6"/>
  <line x1="80" y1="205" x2="226.7" y2="85" stroke="#188038" stroke-width="1.5"/>
  <line x1="300" y1="205" x2="116.7" y2="145" stroke="#555" stroke-width="1.5"/>

  <circle cx="205.7" cy="102.1" r="3" fill="#d93025"/>
  <circle cx="142.9" cy="153.6" r="3" fill="#d93025"/>
  <circle cx="221.4" cy="179.3" r="3" fill="#d93025"/>

  <text x="185" y="18" font-size="13" font-weight="bold" fill="#222">A</text>
  <text x="64" y="212" font-size="13" font-weight="bold" fill="#222">B</text>
  <text x="307" y="212" font-size="13" font-weight="bold" fill="#222">C</text>
  <text x="223" y="222" font-size="13" font-weight="bold" fill="#1a73e8">L</text>
  <text x="234" y="84" font-size="13" font-weight="bold" fill="#188038">M</text>
  <text x="100" y="146" font-size="13" font-weight="bold" fill="#555">N</text>

  <text x="188" y="106" font-size="12.5" font-weight="bold" fill="#d93025">P</text>
  <text x="148" y="168" font-size="12.5" font-weight="bold" fill="#d93025">Q</text>
  <text x="228" y="177" font-size="12.5" font-weight="bold" fill="#d93025">R</text>

  <text x="15" y="42" font-size="11.5" fill="#1a73e8">AP : PR : RL = 3 : 3 : 1</text>
  <text x="15" y="60" font-size="11.5" fill="#d93025">△PQR = 1 - 3×(2/7) = 1/7</text>
</svg>

- **【分步标准解答】**
  **[1]** 辺 $BC, CA, AB$ を $2 : 1$ に内分する点が $L, M, N$ であるから、
  $$BL : LC = 2 : 1, \qquad CM : MA = 2 : 1, \qquad AN : NB = 2 : 1$$

  まず、**$\triangle ALC$ と直線 $BM$** にメネラウスの定理を適用すると、
  $$\frac{AP}{PL} \cdot \frac{LB}{BC} \cdot \frac{CM}{MA} = 1$$
  $LB : BC = 2 : (2+1) = 2 : 3$、$CM : MA = 2 : 1$ を代入すると、
  $$\frac{AP}{PL} \cdot \frac{2}{3} \cdot \frac{2}{1} = 1 \implies \frac{AP}{PL} = \frac{3}{4}$$
  よって、線分 $AL$ 全体を $3 + 4 = 7$ とすると、
  $$AP = \frac{3}{7} AL \quad \cdots \text{①}$$

  次に、**$\triangle ALB$ と直線 $CN$** にメネラウスの定理を適用すると、
  $$\frac{AR}{RL} \cdot \frac{LC}{CB} \cdot \frac{BN}{NA} = 1$$
  $LC : CB = 1 : 3$、$BN : NA = 1 : 2$ を代入すると、
  $$\frac{AR}{RL} \cdot \frac{1}{3} \cdot \frac{1}{2} = 1 \implies \frac{AR}{RL} = 6$$
  よって、線分 $AL$ 全体を $6 + 1 = 7$ とすると、
  $$RL = \frac{1}{7} AL \quad \cdots \text{②}$$
  > 💡 讲师批注：两条梅涅劳斯定理得到的总份数恰好都是 $3+4 = 7$ 和 $6+1 = 7$，连通分都省了！立刻可得中段 $PR = 7 - 3 - 1 = 3$ 份！

  ①，② より、$PR = AL - AP - RL = \left(1 - \dfrac{3}{7} - \dfrac{1}{7}\right) AL = \dfrac{3}{7} AL$ であるから、
  $$AP : PR : RL = \frac{3}{7} : \frac{3}{7} : \frac{1}{7} = 3 : 3 : 1$$

  **[2]** まず、$\triangle ABP$ の面積を求める。
  - $BL : BC = 2 : 3$ より、
    $$\triangle ABL = \frac{2}{3} \triangle ABC = \frac{2}{3} \times 1 = \frac{2}{3}$$
  - [1] より $AP : AL = 3 : 7$ であるから、
    $$\triangle ABP = \frac{3}{7} \triangle ABL = \frac{3}{7} \times \frac{2}{3} = \frac{2}{7}$$

  対称性より、全く同様にして $\triangle BCQ$ および $\triangle CAR$ の面積も等しく、
  $$\triangle ABP = \triangle BCQ = \triangle CAR = \frac{2}{7}$$
  図より、$\triangle ABC$ から周囲の 3 つの三角形 $\triangle ABP, \triangle BCQ, \triangle CAR$ を除いた部分がちょうど $\triangle PQR$ であるから、
  $$\triangle PQR = \triangle ABC - (\triangle ABP + \triangle BCQ + \triangle CAR) = 1 - 3 \times \frac{2}{7} = 1 - \frac{6}{7} = \frac{1}{7}$$
  > 💡 讲师批注：记住这个「$\frac{1}{7}$ 黄金结论」！（劳斯定理通式：三边均按 $k:1$ 内分时，中央小三角形面积占原三角形的 $\dfrac{(k-1)^2}{k^2+k+1}$；当 $k=2$ 时即 $\dfrac{1}{7}$，当 $k=3$ 时即 $\dfrac{4}{13}$。）在 EJU 考试中遇到此图形可瞬间核对答案！
- **【最终答案】**
  **[1] $AP : PR : RL = 3 : 3 : 1$　　[2] $\dfrac{1}{7}$**
