# 《EJU 教材全解与备课讲义》数学 016（P226–P240）

> **对应源文件**：`work_math/ocr_md/ocr_016_p226-240.md`（第八章《空間ベクトル》之「演習問題 6（続）」「空間ベクトルの内積」「位置ベクトル、ベクトルと図形」「空間座標の図形」；第九章《複素数》之「複素数・複素数の計算・負の数の平方根」）
> **视觉核对参考图**：`work_math/ref_imgs/page_0226.jpg` – `page_0240.jpg`（全 15 页已逐页核对）

---

## 一、国内高中基础知识点唤醒与 EJU 考纲差异对比

本切片横跨日本高中数学 **数学C（旧课纲数学B）《空間ベクトル》** 的后半核心内容，以及 **数学Ⅱ《複素数と方程式》** 的开篇基础，涵盖 **空间向量的内积与夹角、位置向量与共线/共点/共面条件、空间球面方程与球面向量方程、复数的四则运算与负数的平方根** 四大核心板块。

### 1.1 空间向量的内积与夹角（空間ベクトルの内積）

- **内积的定义**：当 $\vec{a} \neq \vec{0}, \; \vec{b} \neq \vec{0}$ 时，设 $\vec{a}$ 与 $\vec{b}$ 的夹角为 $\theta$（$0^\circ \le \theta \le 180^\circ$），则：
  $$\vec{a} \cdot \vec{b} = |\vec{a}||\vec{b}|\cos\theta$$
  当 $\vec{a} = \vec{0}$ **或** $\vec{b} = \vec{0}$ 时，规定 $\vec{a} \cdot \vec{b} = 0$。
  > ⚠️ **教材勘误提示**：原教材第 226 页（`page_0227.jpg`）[8.1]① 中写作「$\vec{a}=\vec{0}, \vec{b}=\vec{0}$ のとき」，严谨表述应为「$\vec{a}=\vec{0}$ **または** $\vec{b}=\vec{0}$ のとき」。此外，同页 [8.2]④ 中 $\vec{a}(k\vec{b})$ 漏印了内积点号，应为 $\vec{a}\cdot(k\vec{b})$。

- **内积的坐标（成分）表示**：设 $\vec{a} = (a_1, a_2, a_3), \; \vec{b} = (b_1, b_2, b_3)$，则：
  $$\vec{a} \cdot \vec{b} = a_1 b_1 + a_2 b_2 + a_3 b_3$$
- **夹角公式与垂直条件**（$\vec{a} \neq \vec{0}, \; \vec{b} \neq \vec{0}$）：
  $$\cos\theta = \frac{\vec{a}\cdot\vec{b}}{|\vec{a}||\vec{b}|} = \frac{a_1 b_1 + a_2 b_2 + a_3 b_3}{\sqrt{a_1^2 + a_2^2 + a_3^2}\sqrt{b_1^2 + b_2^2 + b_3^2}} \qquad (0^\circ \le \theta \le 180^\circ)$$
  $$\vec{a} \perp \vec{b} \iff \vec{a}\cdot\vec{b} = 0 \iff a_1 b_1 + a_2 b_2 + a_3 b_3 = 0$$
  > ⚠️ **教材勘误提示**：原教材第 226 页（`page_0227.jpg`）[8.3]① 分母误印为加号 $\sqrt{a_1^2+a_2^2+a_3^2} + \sqrt{b_1^2+b_2^2+b_3^2}$，**务必修正为乘积** $\sqrt{a_1^2+a_2^2+a_3^2}\sqrt{b_1^2+b_2^2+b_3^2}$！

### 1.2 位置向量与共线・共点・共面条件（位置ベクトル、ベクトルと図形）

- **线段分点与重心的位置向量**：设 $A(\vec{a}), B(\vec{b}), C(\vec{c})$：
  - 内分点 $P(\vec{p})$（$m:n$ 内分线段 $AB$）：$\vec{p} = \dfrac{n\vec{a} + m\vec{b}}{m+n}$
  - 外分点 $Q(\vec{q})$（$m:n$ 外分线段 $AB$）：$\vec{q} = \dfrac{-n\vec{a} + m\vec{b}}{m-n}$
    > ⚠️ **教材勘误提示**：原教材第 228 页（`page_0229.jpg`）[9.2]①[2]「外分点」说明文字误印为「$m:n$ に**内分**する点を $Q(\vec{q})$ とすると」，应为「$m:n$ に**外分**する点」。
  - 中点 $M(\vec{m})$：$\vec{m} = \dfrac{\vec{a}+\vec{b}}{2}$；$\triangle ABC$ 重心 $G(\vec{g})$：$\vec{g} = \dfrac{\vec{a}+\vec{b}+\vec{c}}{3}$。
- **三大位置关系条件**：
  1. **共线条件**：$A \neq B$ 时，点 $P$ 在直线 $AB$ 上 $\iff \overrightarrow{AP} = k\overrightarrow{AB} \iff \overrightarrow{OP} = (1-t)\overrightarrow{OA} + t\overrightarrow{OB}$（$\exists k, t \in \mathbb{R}$）。
  2. **共点条件**：三条直线 $l, m, n$ 交于一点 $\iff l$ 与 $m$ 的交点、$m$ 与 $n$ 的交点重合。
  3. **共面条件**：不共线的三点 $A(\vec{a}), B(\vec{b}), C(\vec{c})$ 确定平面 $ABC$，点 $P(\vec{p})$ 在平面 $ABC$ 上：
     $$\iff \overrightarrow{CP} = s\overrightarrow{CA} + t\overrightarrow{CB}\quad(\exists s, t \in \mathbb{R})$$
     $$\iff \vec{p} = s\vec{a} + t\vec{b} + u\vec{c} \;\text{ 且 }\; s + t + u = 1 \quad(\exists s, t, u \in \mathbb{R})$$
- **空间向量的分解唯一性（1次独立）**：若 $O, A, B, C$ 不共面，则空间中任意向量 $\vec{p}$ 均可唯一表示为 $\vec{p} = x\overrightarrow{OA} + y\overrightarrow{OB} + z\overrightarrow{OC}$，即系数对应相等。

### 1.3 空间坐标中的图形与球面方程（空間座標の図形）

- **垂直于坐标轴的平面方程**：过点 $P(a,b,c)$ 且垂直于 $x, y, z$ 轴的平面分别为 $x=a, \; y=b, \; z=c$。特别地，$xy, yz, zx$ 坐标平面的方程分别为 $z=0, \; x=0, \; y=0$。
  > ⚠️ **教材勘误提示**：原教材第 234 页（`page_0235.jpg`）[10.2] 中「各座標に垂直な平面」漏印「軸」字，应为「各座標軸に垂直な平面」。
- **球面方程**：
  - **标准形**：中心 $(a,b,c)$、半径 $r$：$(x-a)^2 + (y-b)^2 + (z-c)^2 = r^2$。
  - **一般形**：$x^2 + y^2 + z^2 + Ax + By + Cz + D = 0$（需满足 $A^2 + B^2 + C^2 - 4D > 0$）。
- **球面的向量方程**：
  - 中心 $C(\vec{c})$、半径 $r$：$|\vec{p} - \vec{c}| = r \iff (\vec{p}-\vec{c})\cdot(\vec{p}-\vec{c}) = r^2$。
  - 以线段 $AB$ 为直径：$(\vec{p}-\vec{a})\cdot(\vec{p}-\vec{b}) = 0$。

### 1.4 复数与负数的平方根（複素数）

- **复数的定义与分类**：设 $i^2 = -1$ 为虚数单位，$a, b \in \mathbb{R}$，称 $a + bi$ 为**复数**，$a$ 为**实部**，$b$ 为**虚部**。
  - $b = 0$ 时为**实数**；$b \neq 0$ 时为**虚数**；$a = 0$ 且 $b \neq 0$ 时为**纯虚数**。
- **复数相等**：$a,b,c,d \in \mathbb{R}$ 时，$a + bi = c + di \iff a = c \text{ 且 } b = d$。
- **共轭复数**：$a + bi$ 与 $a - bi$ 互为共轭复数（记作 $\overline{\alpha}$）。其和 $2a$ 与积 $a^2+b^2$ 均为实数；复数除法通过分子分母同乘分母的共轭复数实现「分母实数化」。
- **负数的平方根**：当 $a > 0$ 时，规定 $\sqrt{-a} = \sqrt{a}\,i$（特例 $\sqrt{-1} = i$）；负数 $-a$ 的平方根为 $\pm\sqrt{a}\,i$。
  - **铁律**：遇到 $\sqrt{-a}$（$a>0$）做乘除法时，**必须先化为 $\sqrt{a}\,i$ 再运算**，切忌直接套用实数公式 $\sqrt{-2}\sqrt{-3} = \sqrt{(-2)(-3)} = \sqrt{6}$（正确结果应为 $\sqrt{2}i \cdot \sqrt{3}i = -\sqrt{6}$）。

### 1.5 国内高中 vs. 日本 EJU 考纲差异与符号习惯

| 对比维度 | 国内高中习惯 | 日本 EJU 习惯 | 备课/应试提醒 |
| :--- | :--- | :--- | :--- |
| **空间直线与平面** | 高考大题重度依赖**建系 + 法向量 + 叉乘** | **不教叉乘（外積）**，常规做法是设垂直条件 $\vec{n}\cdot\vec{a}=0, \vec{n}\cdot\vec{b}=0$ 联立求解，且极重**纯基底向量法（四面体/平行六面体）** | 备课时既要教日本标准基底法（用于解答填空推导），也可补充叉乘作为草稿纸极速验算工具 |
| **球面方程** | 新高考课标已删减球面方程，仅保留空间两点距离 | **EJU 空间向量必考内容**，常考球面与坐标平面/平行平面的截圆半径、球面向量方程 | 牢记截圆勾股关系 $r_{\text{円}}^2 = R^2 - d^2$，以及球面与三坐标平面相切时中心为 $(\pm r, \pm r, \pm r)$ |
| **外分点公式** | 国内教材几乎不考定比分点/外分点公式 | 日本高中数学高频基础，常直接出现「$m:n$ に外分する点」 | 记口诀：「外分 = 内分公式把 $n$ 换成 $-n$」，即 $\dfrac{-n\vec{a}+m\vec{b}}{m-n}$ |
| **负数的平方根记号** | 国内严格避免书写 $\sqrt{-5}$，直接写作 $\sqrt{5}i$ | 日本数学Ⅱ正式定义 $\sqrt{-a} = \sqrt{a}i$（$a>0$），并高频作为易错陷阱考查 | 看到 $\sqrt{-a}$ 第一步立刻改写成 $\sqrt{a}i$，防止出现 $\sqrt{-5}\cdot\sqrt{-5} = \sqrt{25} = 5$ 的致命错误 |
| **复数相等前提** | 常口头省略“$a,b,c,d$ 为实数” | EJU 解答题中必须明确写出「$a, b, c, d$ は実数であるから」 | 若字母未声明为实数，不可直接比较实部虚部 |

---

## 二、日文核心词汇与公式假名注音

### 2.1 本切片日文核心词汇

- 空間ベクトル（くうかんべくとる / kuukan bekutoru） — 空间向量
- 内積（ないせき / naiseki） — 内积、数量积（点积）
- 成分表示（せいぶんひょうじ / seibun hyouji） — 坐标表示、分量表示（向量的成分表示）
- 単位ベクトル（たんいべくとる / tan'i bekutoru） — 单位向量
- 位置ベクトル（いちべくとる / ichi bekutoru） — 位置向量
- 分点（ぶんてん / bunten） — 分点（内分点与外分点的统称）
- 共線条件（きょうせんじょうけん / kyousen jouken） — 共线条件（三点共线条件）
- 共点条件（きょうてんじょうけん / kyouten jouken） — 共点条件（三线共点条件）
- 共面条件（きょうめんじょうけん / kyoumen jouken） — 共面条件（四点共面条件）
- 四面体（しめんたい / shimentai） — 四面体
- 平行六面体（へいこうろくめんたい / heikou rokumentai） — 平行六面体
- 1次独立（いちじどくりつ / ichiji dokuritsu） — 线性无关（空间基底分解唯一性）
- 空間座標（くうかんざひょう / kuukan zahyou） — 空间坐标（三维直角坐标）
- 座標軸（ざひょうじく / zahyoujiku） — 坐标轴
- 球面（きゅうめん / kyuumen） — 球面
- 球面の方程式（きゅうめんのほうていしき / kyuumen no houteishiki） — 球面方程
- ベクトル方程式（べくとるほうていしき / bekutoru houteishiki） — 向量方程
- 複素数（ふくそすう / fukusosuu） — 复数
- 虚数（きょすう / kyosuu） — 虚数
- 純虚数（じゅんきょすう / junkyosuu） — 纯虚数
- 虚数単位（きょすうたんい / kyosuu tan'i） — 虚数单位（$i$）
- 実部（じつぶ / jitsubu） — 实部
- 虚部（きょぶ / kyobu） — 虚部
- 複素数の相等（ふくそすうのそうとう / fukusosuu no soutou） — 复数相等
- 負の数の平方根（ふのかずのへいほうこん / fu no kazu no heihoukon） — 负数的平方根

### 2.2 核心公式的日本课堂口语读法

1. **向量内积定义** $\vec{a} \cdot \vec{b} = |\vec{a}||\vec{b}|\cos\theta$
   - 课堂读法：**ベクトル エー ドット ベクトル ビー イコール ぜったいち ベクトル エー、ぜったいち ベクトル ビー、コサイン シータ**
   - 备注：向量的模 $|\vec{a}|$ 在日本课堂常读作 **ベクトル エー の おおきさ**（大小）或 **ぜったいち ベクトル エー**；内积点号读作 **ドット** 或省略直接说 **ないせき**。
2. **共面条件** $\vec{p} = s\vec{a} + t\vec{b} + u\vec{c}, \; s+t+u=1$
   - 课堂读法：**ベクトル ピー イコール エス ベクトル エー たす ティー ベクトル ビー たす ユー ベクトル シー、ただし エス たす ティー たす ユー イコール いち**
   - 备注：口诀常称 **「けいすうの わ が いち（係数の和が 1）」**。
3. **直径式球面向量方程** $(\vec{p}-\vec{a})\cdot(\vec{p}-\vec{b}) = 0$
   - 课堂读法：**かっこ ベクトル ピー ひく ベクトル エー かっことじ ドット かっこ ベクトル ピー ひく ベクトル ビー かっことじ イコール ゼロ**
4. **复数标准形与共轭复数** $\alpha = a + bi, \; \overline{\alpha} = a - bi$
   - 课堂读法：**アルファ イコール エー たす ビー アイ、アルファ バー イコール エー ひく ビー アイ**
   - 备注：共轭符号 $\overline{\alpha}$ 读作 **アルファ バー（$\alpha$ bar）**。
5. **负数的平方根** $\sqrt{-a} = \sqrt{a}\,i \;\; (a>0)$
   - 课堂读法：**ルート マイナス エー イコール ルート エー アイ**

---

## 三、逐题深度解析（不可跳步）

---

### 第八章 演習問題 6（続き：空間ベクトルの成分と大きさ）

#### 演習問題 6-(2)
- **【原题重现与翻译】**
  - 原题：4点 $A(1, 0, -3), \; B(-1, 2, 2), \; D(2, 3, -1), \; E(6, a, b)$ がある。
    - `[1]` $AB \parallel DE$ であるとき、$a, b$ の値を求めよ。
    - `[2]` 四角形 $ABCD$ が平行四辺形であるとき、点 $C$ の座標を求めよ。
  - 中文：已知 4 点 $A(1, 0, -3), \; B(-1, 2, 2), \; D(2, 3, -1), \; E(6, a, b)$。
    - `[1]` 当 $AB \parallel DE$ 时，求 $a, b$ 的值。
    - `[2]` 当四边形 $ABCD$ 为平行四边形时，求点 $C$ 的坐标。
- **【考点定位】**
  - 空间向量的坐标计算（终点减起点）、向量平行条件（$\vec{b} = k\vec{a}$）、平行四边形的向量判定（$\overrightarrow{AB} = \overrightarrow{DC}$）。
- **【分步标准解答】**
  - **`[1]` の解答**：
    $$\overrightarrow{AB} = (-1 - 1, \; 2 - 0, \; 2 - (-3)) = (-2, \; 2, \; 5)$$
    $$\overrightarrow{DE} = (6 - 2, \; a - 3, \; b - (-1)) = (4, \; a - 3, \; b + 1)$$
    > 💡 讲师批注：求向量坐标一律遵循「终点坐标 $-$ 起点坐标」，特别注意减负数时的变号（如 $2 - (-3) = 5$）。

    $\overrightarrow{AB} \neq \vec{0}$ であるから、$AB \parallel DE$ の条件は、$\overrightarrow{DE} = k\overrightarrow{AB}$ となる実数 $k$ が存在することである。
    $$(4, \; a - 3, \; b + 1) = k(-2, \; 2, \; 5) = (-2k, \; 2k, \; 5k)$$
    成分を比較すると：
    $$4 = -2k, \qquad a - 3 = 2k, \qquad b + 1 = 5k$$
    > 💡 讲师批注：先由不含参数的 $x$ 分量求出比例系数 $k$，再分别代入 $y, z$ 分量。

    第 1 式より $k = -2$。これを第 2 式・第 3 式に代入すると：
    $$a - 3 = 2(-2) = -4 \implies a = -1$$
    $$b + 1 = 5(-2) = -10 \implies b = -11$$
    > 💡 讲师批注：验算 $\overrightarrow{DE} = (4, -4, -10) = -2(-2, 2, 5) = -2\overrightarrow{AB}$，完全正确。

  - **`[2]` の解答**：
    点 $C$ の座標を $(x, y, z)$ とおく。四角形 $ABCD$ が平行四辺形であるための条件は $\overrightarrow{AB} = \overrightarrow{DC}$ である。
    > 💡 讲师批注：**极易踩坑点！** 四边形按顶点顺次记作 $ABCD$，因此 $AB$ 的对边向量是 $\overrightarrow{DC}$（而不是 $\overrightarrow{CD}$！）。也可等价写作 $\overrightarrow{AD} = \overrightarrow{BC}$ 或利用对角线中点重合 $A+C = B+D$。

    $$\overrightarrow{DC} = (x - 2, \; y - 3, \; z - (-1)) = (x - 2, \; y - 3, \; z + 1)$$
    $\overrightarrow{AB} = \overrightarrow{DC}$ より：
    $$(-2, \; 2, \; 5) = (x - 2, \; y - 3, \; z + 1)$$
    各成分を比較すると：
    $$x - 2 = -2 \implies x = 0, \qquad y - 3 = 2 \implies y = 5, \qquad z + 1 = 5 \implies z = 4$$
    よって、点 $C$ の座標は $(0, 5, 4)$ である。
    > 💡 讲师批注：用对角线中点验算：$AC$ 中点为 $(\frac{1+0}{2}, \frac{0+5}{2}, \frac{-3+4}{2}) = (\frac{1}{2}, \frac{5}{2}, \frac{1}{2})$，$BD$ 中点为 $(\frac{-1+2}{2}, \frac{2+3}{2}, \frac{2-1}{2}) = (\frac{1}{2}, \frac{5}{2}, \frac{1}{2})$，完全一致！
- **【最终答案】**
  - **`[1]` $a = -1, \quad b = -11$**
  - **`[2]` $C(0, \; 5, \; 4)$**

---

#### 演習問題 6-(3)
- **【原题重现与翻译】**
  - 原题：$\vec{a} = (2, 1, 1), \; \vec{b} = (1, 2, -1)$ とする。ベクトル $\vec{a} + t\vec{b}$ の大きさが最小になるときの実数 $t$ の値と、その時の大きさを求めよ。
  - 中文：设 $\vec{a} = (2, 1, 1), \; \vec{b} = (1, 2, -1)$。求使向量 $\vec{a} + t\vec{b}$ 的模取得最小值时的实数 $t$ 的值，以及此时的模长。
- **【考点定位】**
  - 空间向量模长的平方与二次函数配方求最值。
- **【分步标准解答】**
  $$\vec{a} + t\vec{b} = (2, 1, 1) + t(1, 2, -1) = (2 + t, \; 1 + 2t, \; 1 - t)$$
  大きさを 2 乗すると：
  $$|\vec{a} + t\vec{b}|^2 = (2 + t)^2 + (1 + 2t)^2 + (1 - t)^2$$
  $$= (t^2 + 4t + 4) + (4t^2 + 4t + 1) + (t^2 - 2t + 1)$$
  $$= 6t^2 + 6t + 6$$
  > 💡 讲师批注：因为 $|\vec{a}+t\vec{b}| \ge 0$，求模长最小等价于求模长的平方 $|\vec{a}+t\vec{b}|^2$ 最小，从而消去根号，转化为关于 $t$ 的二次函数最值问题。

  平方完成すると：
  $$|\vec{a} + t\vec{b}|^2 = 6(t^2 + t) + 6 = 6\left(t + \frac{1}{2}\right)^2 - 6 \cdot \frac{1}{4} + 6 = 6\left(t + \frac{1}{2}\right)^2 + \frac{9}{2}$$
  > 💡 讲师批注：配方时切记括号内多出的 $\left(\frac{1}{2}\right)^2 = \frac{1}{4}$ 要乘以括号外的系数 $6$ 再减去：$6 - \frac{3}{2} = \frac{9}{2}$。

  したがって、$t = -\dfrac{1}{2}$ のとき、$|\vec{a} + t\vec{b}|^2$ は最小値 $\dfrac{9}{2}$ をとる。
  $|\vec{a} + t\vec{b}| \ge 0$ であるから、求める最小の大きさは：
  $$\sqrt{\frac{9}{2}} = \frac{3}{\sqrt{2}} = \frac{3\sqrt{2}}{2}$$
  > 💡 讲师批注：**几何意义验算**：模长最小时，$\vec{a}+t\vec{b}$ 必垂直于 $\vec{b}$。将 $t = -\frac{1}{2}$ 代入得 $\vec{a} - \frac{1}{2}\vec{b} = \left(\frac{3}{2}, 0, \frac{3}{2}\right)$，其与 $\vec{b}=(1,2,-1)$ 的内积为 $\frac{3}{2} + 0 - \frac{3}{2} = 0$，且模长为 $\sqrt{\frac{9}{4} + \frac{9}{4}} = \frac{3\sqrt{2}}{2}$，100% 吻合！
- **【最终答案】**
  **$t = -\dfrac{1}{2}$ のとき、最小値 $\dfrac{3\sqrt{2}}{2}$**

---

#### 演習問題 6-(4)
- **【原题重现与翻译】**
  - 原题：定点 $A(2, 0, 3), \; B(1, 2, 1)$ と、$xy$ 平面上を動く点 $P$ に対し、$AP + PB$ の最小値を求めよ。
  - 中文：已知定点 $A(2, 0, 3), \; B(1, 2, 1)$ 以及在 $xy$ 平面上运动的动点 $P$，求 $AP + PB$ 的最小值。
- **【考点定位】**
  - 空间对称点（关于 $xy$ 平面的对称）、将军饮马模型在三维空间的推广、空间两点间距离公式。
- **【图解辅助（SVG 矢量图）】**

<svg viewBox="0 0 460 250" width="460" height="250" xmlns="http://www.w3.org/2000/svg" style="background:#fafafa;border:1px solid #e0e0e0;border-radius:8px;display:block;margin:12px auto;">
  <defs>
    <marker id="arr1" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#64748b"/>
    </marker>
  </defs>
  <!-- xy-plane parallelogram -->
  <polygon points="50,155 340,155 410,105 120,105" fill="#e0f2fe" fill-opacity="0.65" stroke="#0284c7" stroke-width="1.5"/>
  <text x="342" y="148" font-size="12" fill="#0369a1" font-weight="bold">xy 平面 (z=0)</text>

  <!-- Point A(2,0,3) -->
  <circle cx="135" cy="40" r="4.5" fill="#dc2626"/>
  <text x="72" y="36" font-size="13" fill="#dc2626" font-weight="bold">A(2, 0, 3)</text>

  <!-- Point B(1,2,1) -->
  <circle cx="315" cy="80" r="4.5" fill="#2563eb"/>
  <text x="325" y="82" font-size="13" fill="#2563eb" font-weight="bold">B(1, 2, 1)</text>

  <!-- Foot of B on xy plane -->
  <circle cx="315" cy="130" r="3" fill="#64748b"/>
  <!-- Point B'(1,2,-1) symmetric -->
  <circle cx="315" cy="180" r="4.5" fill="#7c3aed"/>
  <text x="325" y="185" font-size="13" fill="#7c3aed" font-weight="bold">B'(1, 2, -1)</text>

  <!-- Vertical line B-B' -->
  <line x1="315" y1="80" x2="315" y2="180" stroke="#64748b" stroke-width="1.3" stroke-dasharray="4,3"/>
  <!-- Right angle mark -->
  <polyline points="305,130 305,120 315,120" fill="none" stroke="#64748b" stroke-width="1.2"/>

  <!-- Optimal P on AB' intersection with xy-plane -->
  <!-- Line A(135,40) to B'(315,180): at y=130, t=(130-40)/140=9/14, x=135+180*9/14=250.7 -->
  <circle cx="251" cy="130" r="4.5" fill="#059669"/>
  <text x="234" y="150" font-size="13" fill="#059669" font-weight="bold">P (最小点)</text>

  <!-- Segment A-P-B' (straight line) -->
  <line x1="135" y1="40" x2="251" y2="130" stroke="#dc2626" stroke-width="2"/>
  <line x1="251" y1="130" x2="315" y2="180" stroke="#7c3aed" stroke-width="2" stroke-dasharray="5,3"/>

  <!-- Segment P-B -->
  <line x1="251" y1="130" x2="315" y2="80" stroke="#2563eb" stroke-width="2"/>

  <!-- Equal ticks PB = PB' -->
  <text x="268" y="99" font-size="12" fill="#2563eb">PB</text>
  <text x="264" y="170" font-size="12" fill="#7c3aed">PB'</text>
  <text x="20" y="232" font-size="12" fill="#334155">关于 xy 平面作对称点 B'：AP + PB = AP + PB' ≥ AB'（三点共线时取等）</text>
</svg>

- **【分步标准解答】**
  2点 $A(2, 0, 3), \; B(1, 2, 1)$ の $z$ 座標はともに正であるから、2点 $A, B$ は $xy$ 平面に関して同じ側にある。
  > 💡 讲师批注：使用镜像对称法前，必须先确认两定点的 $z$ 坐标同号（位于 $xy$ 平面同侧）；若异号则线段 $AB$ 本身就穿过 $xy$ 平面，最小值为 $AB$。

  $xy$ 平面に関して点 $B(1, 2, 1)$ と対称な点を $B'$ とすると、$z$ 座標の符号のみが反転して：
  $$B'(1, \; 2, \; -1)$$
  > 💡 讲师批注：关于 $xy$ 平面对称时，$(x, y, z) \mapsto (x, y, -z)$，横纵坐标不变、竖坐标取相反数。

  点 $P$ は $xy$ 平面上にあるから、対称性より $PB = PB'$ が成り立つ。よって：
  $$AP + PB = AP + PB' \ge AB'$$
  等号は、点 $P$ が線分 $AB'$ と $xy$ 平面の交点に一致するときに成り立つ（$A, B'$ の $z$ 座標は異符号なので交点は必ず線分 $AB'$ 上に存在する）。
  したがって、$AP + PB$ の最小値は線分 $AB'$ の長さである：
  $$AB' = \sqrt{(1 - 2)^2 + (2 - 0)^2 + (-1 - 3)^2} = \sqrt{(-1)^2 + 2^2 + (-4)^2} = \sqrt{1 + 4 + 16} = \sqrt{21}$$
  > 💡 讲师批注：若改为作 $A$ 关于 $xy$ 平面的对称点 $A'(2, 0, -3)$，则 $A'B = \sqrt{(1-2)^2 + (2-0)^2 + (1-(-3))^2} = \sqrt{1+4+16} = \sqrt{21}$，结果完全一致。
- **【最终答案】**
  **$\sqrt{21}$**

---

### 第八章 演習問題 7（空間ベクトルの内積）

#### 演習問題 7-(1)
- **【原题重现与翻译】**
  - 原题：$\vec{a} = (0, 0, 2), \; \vec{b} = (1, \sqrt{2}, 3)$ の内積とそのなす角 $\theta$ を求めよ。
  - 中文：求 $\vec{a} = (0, 0, 2), \; \vec{b} = (1, \sqrt{2}, 3)$ 的内积以及它们的夹角 $\theta$。
- **【考点定位】**
  - 空间向量内积的坐标公式与夹角余弦公式。
- **【分步标准解答】**
  内積 $\vec{a} \cdot \vec{b}$ は：
  $$\vec{a} \cdot \vec{b} = 0 \cdot 1 + 0 \cdot \sqrt{2} + 2 \cdot 3 = 6$$
  それぞれの大きさは：
  $$|\vec{a}| = \sqrt{0^2 + 0^2 + 2^2} = 2$$
  $$|\vec{b}| = \sqrt{1^2 + (\sqrt{2})^2 + 3^2} = \sqrt{1 + 2 + 9} = \sqrt{12} = 2\sqrt{3}$$
  > 💡 讲师批注：计算 $|\vec{b}|$ 时切勿把 $(\sqrt{2})^2$ 算成 $4$，应为 $2$。

  よって、なす角 $\theta$ について：
  $$\cos\theta = \frac{\vec{a}\cdot\vec{b}}{|\vec{a}||\vec{b}|} = \frac{6}{2 \cdot 2\sqrt{3}} = \frac{6}{4\sqrt{3}} = \frac{3}{2\sqrt{3}} = \frac{\sqrt{3}}{2}$$
  $0^\circ \le \theta \le 180^\circ$ であるから、$\theta = 30^\circ$。
  > 💡 讲师批注：回答夹角时务必写出范围条件 $0^\circ \le \theta \le 180^\circ$，以此保证 $\cos\theta = \frac{\sqrt{3}}{2}$ 唯一确定 $\theta = 30^\circ$。
- **【最终答案】**
  **内積：$6$、なす角：$\theta = 30^\circ$**

---

#### 演習問題 7-(2)
- **【原题重现与翻译】**
  - 原题：2つのベクトル $\vec{a} = (2, 1, 3), \; \vec{b} = (1, -1, 0)$ の両方に垂直な単位ベクトルを求めよ。
  - 中文：求同时垂直于两个向量 $\vec{a} = (2, 1, 3)$ 与 $\vec{b} = (1, -1, 0)$ 的单位向量。
- **【考点定位】**
  - 空间向量垂直条件（$\vec{a}\cdot\vec{e}=0, \vec{b}\cdot\vec{e}=0$）与单位向量条件（$|\vec{e}|=1$）。
- **【分步标准解答】**
  求める単位ベクトルを $\vec{e} = (x, y, z)$ とおく。
  $\vec{e} \perp \vec{a}, \; \vec{e} \perp \vec{b}$ かつ $|\vec{e}| = 1$ であるから：
  $$\begin{cases} \vec{a}\cdot\vec{e} = 2x + y + 3z = 0 & \cdots ① \\ \vec{b}\cdot\vec{e} = x - y = 0 & \cdots ② \\ |\vec{e}|^2 = x^2 + y^2 + z^2 = 1 & \cdots ③ \end{cases}$$
  > 💡 讲师批注：求公垂单位向量共有 3 个未知数，恰好由 2 个垂直方程 + 1 个模长为 1 的方程构成完备方程组。

  ② より $y = x$。これを ① に代入すると：
  $$2x + x + 3z = 0 \implies 3x + 3z = 0 \implies z = -x$$
  $y = x, \; z = -x$ を ③ に代入すると：
  $$x^2 + x^2 + (-x)^2 = 1 \implies 3x^2 = 1 \implies x = \pm\frac{1}{\sqrt{3}} = \pm\frac{\sqrt{3}}{3}$$
  > 💡 讲师批注：**最高频漏解点！** 空间中同时垂直于两个不共线向量的单位向量必定有**方向相反的一对（正负两个）**，切勿漏掉负号！

  したがって、求める単位ベクトルは：
  - $x = \dfrac{\sqrt{3}}{3}$ のとき：$\vec{e} = \left(\dfrac{\sqrt{3}}{3}, \; \dfrac{\sqrt{3}}{3}, \; -\dfrac{\sqrt{3}}{3}\right)$
  - $x = -\dfrac{\sqrt{3}}{3}$ のとき：$\vec{e} = \left(-\dfrac{\sqrt{3}}{3}, \; -\dfrac{\sqrt{3}}{3}, \; \dfrac{\sqrt{3}}{3}\right)$
  > 💡 讲师批注：草稿纸可用外积（叉乘）秒验：$\vec{a}\times\vec{b} = (1\cdot 0 - 3(-1), \; 3\cdot 1 - 2\cdot 0, \; 2(-1)-1\cdot 1) = (3, 3, -3) \parallel (1, 1, -1)$，单位化后即 $\pm\frac{1}{\sqrt{3}}(1,1,-1)$，完全一致！
- **【最终答案】**
  **$\left(\dfrac{\sqrt{3}}{3}, \; \dfrac{\sqrt{3}}{3}, \; -\dfrac{\sqrt{3}}{3}\right), \quad \left(-\dfrac{\sqrt{3}}{3}, \; -\dfrac{\sqrt{3}}{3}, \; \dfrac{\sqrt{3}}{3}\right)$**

---

#### 演習問題 7-(3)
- **【原题重现与翻译】**
  - 原题：$A(-2, 1, 3), \; B(-3, 1, 4), \; C(-3, 3, 5)$ とする。
    - `[1]` 2つのベクトル $\overrightarrow{AB}, \; \overrightarrow{AC}$ のなす角を求めよ。
    - `[2]` 3点 $A, B, C$ で定める $\triangle ABC$ の面積 $S$ を求めよ。
  - 中文：已知 $A(-2, 1, 3), \; B(-3, 1, 4), \; C(-3, 3, 5)$。
    - `[1]` 求两个向量 $\overrightarrow{AB}, \; \overrightarrow{AC}$ 的夹角。
    - `[2]` 求三点 $A, B, C$ 所确定的 $\triangle ABC$ 的面积 $S$。
- **【考点定位】**
  - 空间向量夹角计算、利用内积求空间三角形面积。
- **【分步标准解答】**
  - **`[1]` の解答**：
    $$\overrightarrow{AB} = (-3 - (-2), \; 1 - 1, \; 4 - 3) = (-1, \; 0, \; 1)$$
    $$\overrightarrow{AC} = (-3 - (-2), \; 3 - 1, \; 5 - 3) = (-1, \; 2, \; 2)$$
    それぞれの大きさと内積を計算すると：
    $$|\overrightarrow{AB}| = \sqrt{(-1)^2 + 0^2 + 1^2} = \sqrt{2}$$
    $$|\overrightarrow{AC}| = \sqrt{(-1)^2 + 2^2 + 2^2} = \sqrt{1 + 4 + 4} = 3$$
    $$\overrightarrow{AB} \cdot \overrightarrow{AC} = (-1)(-1) + 0 \cdot 2 + 1 \cdot 2 = 1 + 0 + 2 = 3$$
    > 💡 讲师批注：求 $\triangle ABC$ 的内角 $\angle A$ 时，两向量必须**共起点 $A$**（即 $\overrightarrow{AB}$ 与 $\overrightarrow{AC}$）。

    なす角を $\theta$（$0^\circ \le \theta \le 180^\circ$）とすると：
    $$\cos\theta = \frac{\overrightarrow{AB}\cdot\overrightarrow{AC}}{|\overrightarrow{AB}||\overrightarrow{AC}|} = \frac{3}{\sqrt{2} \cdot 3} = \frac{1}{\sqrt{2}}$$
    よって、$\theta = 45^\circ$。

  - **`[2]` の解答**：
    `[1]` の結果より $\sin\theta = \sin 45^\circ = \dfrac{1}{\sqrt{2}}$ であるから：
    $$S = \frac{1}{2}|\overrightarrow{AB}||\overrightarrow{AC}|\sin\theta = \frac{1}{2} \cdot \sqrt{2} \cdot 3 \cdot \frac{1}{\sqrt{2}} = \frac{3}{2}$$
    > 💡 讲师批注：也可用免角度公式直接验算：$S = \dfrac{1}{2}\sqrt{|\overrightarrow{AB}|^2|\overrightarrow{AC}|^2 - (\overrightarrow{AB}\cdot\overrightarrow{AC})^2} = \dfrac{1}{2}\sqrt{2\cdot 9 - 3^2} = \dfrac{1}{2}\sqrt{9} = \dfrac{3}{2}$，完全吻合。
- **【最终答案】**
  - **`[1]` $45^\circ$**
  - **`[2]` $S = \dfrac{3}{2}$**

---

#### 演習問題 7-(4)
- **【原题重现与翻译】**
  - 原题：空間において、大きさが $4$ で、$x$ 軸の正の向きとなす角が $60^\circ$、$z$ 軸の正の向きとなす角が $45^\circ$ であるようなベクトル $\vec{p}$ を求めよ。また、$\vec{p}$ が $y$ 軸の正の向きとなす角 $\theta$ を求めよ。
  - 中文：在空间中，求模长为 $4$、与 $x$ 轴正方向夹角为 $60^\circ$、与 $z$ 轴正方向夹角为 $45^\circ$ 的向量 $\vec{p}$。并求 $\vec{p}$ 与 $y$ 轴正方向的夹角 $\theta$。
- **【考点定位】**
  - 空间向量与坐标轴正方向的夹角（方向余弦）、单位坐标基向量内积。
- **【分步标准解答】**
  求めるベクトルを $\vec{p} = (x, y, z)$ とおく。$x$ 軸、$y$ 軸、$z$ 軸の正の向きの単位ベクトルをそれぞれ $\vec{e}_1 = (1, 0, 0), \; \vec{e}_2 = (0, 1, 0), \; \vec{e}_3 = (0, 0, 1)$ とする。
  > 💡 讲师批注：向量 $\vec{p}=(x,y,z)$ 与坐标轴正方向的夹角，本质上就是 $\vec{p}$ 与对应坐标轴单位基向量的夹角，因此有直接结论 $x = |\vec{p}|\cos\alpha, \; y = |\vec{p}|\cos\beta, \; z = |\vec{p}|\cos\gamma$。

  条件 $|\vec{p}| = 4$ より：
  $$x = \vec{p}\cdot\vec{e}_1 = |\vec{p}||\vec{e}_1|\cos 60^\circ = 4 \cdot 1 \cdot \frac{1}{2} = 2$$
  $$z = \vec{p}\cdot\vec{e}_3 = |\vec{p}||\vec{e}_3|\cos 45^\circ = 4 \cdot 1 \cdot \frac{\sqrt{2}}{2} = 2\sqrt{2}$$
  また、$|\vec{p}|^2 = x^2 + y^2 + z^2 = 4^2 = 16$ であるから：
  $$2^2 + y^2 + (2\sqrt{2})^2 = 16 \implies 4 + y^2 + 8 = 16 \implies y^2 = 4 \implies y = \pm 2$$
  > 💡 讲师批注：开方得到 $y = \pm 2$ 对应两个不同的向量，分别与 $y$ 轴正方向成锐角与钝角，必须分类写出对应的 $\theta$！

  さらに、$\cos\theta = \dfrac{\vec{p}\cdot\vec{e}_2}{|\vec{p}||\vec{e}_2|} = \dfrac{y}{4}$（$0^\circ \le \theta \le 180^\circ$）より：
  - $y = 2$ のとき：$\vec{p} = (2, 2, 2\sqrt{2})$、$\cos\theta = \dfrac{2}{4} = \dfrac{1}{2}$ より $\theta = 60^\circ$。
  - $y = -2$ のとき：$\vec{p} = (2, -2, 2\sqrt{2})$、$\cos\theta = \dfrac{-2}{4} = -\dfrac{1}{2}$ より $\theta = 120^\circ$。
  > 💡 讲师批注：用方向余弦恒等式 $\cos^2\alpha + \cos^2\beta + \cos^2\gamma = 1$ 验算：$\cos^2 60^\circ + \cos^2\theta + \cos^2 45^\circ = \frac{1}{4} + \frac{1}{4} + \frac{1}{2} = 1$，完美验证。
- **【最终答案】**
  **$\vec{p} = (2, \; 2, \; 2\sqrt{2})$ のとき $\theta = 60^\circ$；$\vec{p} = (2, \; -2, \; 2\sqrt{2})$ のとき $\theta = 120^\circ$**

---

### 第八章 演習問題 8（位置ベクトル、ベクトルと図形）

#### 演習問題 8-(1)
- **【原题重现与翻译】**
  - 原题：四面体 $ABCD$ において、$\triangle BCD, \; \triangle ACD, \; \triangle ABD, \; \triangle ABC$ の重心をそれぞれ $G_a, \; G_b, \; G_c, \; G_d$ とする。線分 $AG_a, \; BG_b, \; CG_c, \; DG_d$ をそれぞれ $3:1$ に内分する点は一致することを示せ。
  - 中文：在四面体 $ABCD$ 中，设 $\triangle BCD, \; \triangle ACD, \; \triangle ABD, \; \triangle ABC$ 的重心分别为 $G_a, \; G_b, \; G_c, \; G_d$。证明：将线段 $AG_a, \; BG_b, \; CG_c, \; DG_d$ 各自按 $3:1$ 内分的四个点重合。
- **【考点定位】**
  - 位置向量、三角形重心公式、内分点公式与四面体（空间）重心性质。
- **【分步标准解答】**
  空間の基準点 $O$ に関する 4 点 $A, B, C, D$ の位置ベクトルをそれぞれ $\vec{a}, \vec{b}, \vec{c}, \vec{d}$ とする。
  $G_a$ は $\triangle BCD$ の重心であるから、その位置ベクトル $\vec{g}_a$ は：
  $$\vec{g}_a = \frac{\vec{b} + \vec{c} + \vec{d}}{3}$$
  線分 $AG_a$ を $3:1$ に内分する点 $P_a$ の位置ベクトル $\vec{p}_a$ は、内分点の公式より：
  $$\vec{p}_a = \frac{1 \cdot \vec{a} + 3 \cdot \vec{g}_a}{3 + 1} = \frac{\vec{a} + 3 \cdot \dfrac{\vec{b} + \vec{c} + \vec{d}}{3}}{4} = \frac{\vec{a} + \vec{b} + \vec{c} + \vec{d}}{4}$$
  > 💡 讲师批注：内分点公式为「交叉相乘除以比例和」：$AG_a$ 按 $3:1$ 内分时，靠近 $G_a$，因此 $A$ 乘以 $1$、$G_a$ 乘以 $3$，恰好与 $\vec{g}_a$ 的分母 $3$ 约分！

  同様にして、線分 $BG_b, \; CG_c, \; DG_d$ をそれぞれ $3:1$ に内分する点 $P_b, P_c, P_d$ の位置ベクトルを求めると、対称性よりすべて：
  $$\vec{p}_b = \vec{p}_c = \vec{p}_d = \frac{\vec{a} + \vec{b} + \vec{c} + \vec{d}}{4}$$
  となる。位置ベクトルが一致するから、これら 4 つの内分点はすべて一致する。（証明終）
  > 💡 讲师批注：这个公共点 $G\left(\dfrac{\vec{a}+\vec{b}+\vec{c}+\vec{d}}{4}\right)$ 称为**四面体的重心（四面体の重心）**。注意它恰好也是任意一对对棱中点连线（如 $AB$ 中点与 $CD$ 中点连线）的中点，下一题 8-(2) 就会直接用到！
- **【最终答案】**
  **4 つの内分点の位置ベクトルはいずれも $\dfrac{\vec{a} + \vec{b} + \vec{c} + \vec{d}}{4}$ となり一致する（証明完了）。**

---

#### 演習問題 8-(2)
- **【原题重现与翻译】**
  - 原题：1辺の長さが $a$ の正四面体 $ABCD$ において、$\overrightarrow{AB} = \vec{b}, \; \overrightarrow{AC} = \vec{c}, \; \overrightarrow{AD} = \vec{d}$ とする。辺 $AB, CD$ の中点をそれぞれ $M, N$ とし、線分 $MN$ の中点を $G$、$\angle AGB = \theta$ とする。
    - `[1]` $\overrightarrow{AN}, \; \overrightarrow{AG}, \; \overrightarrow{BG}$ をそれぞれ $\vec{b}, \vec{c}, \vec{d}$ で表せ。
    - `[2]` $|\overrightarrow{GA}|^2, \; \overrightarrow{GA}\cdot\overrightarrow{GB}$ をそれぞれ $a$ を用いて表せ。
    - `[3]` $\cos\theta$ の値を求めよ。
  - 中文：在棱长为 $a$ 的正四面体 $ABCD$ 中，设 $\overrightarrow{AB} = \vec{b}, \; \overrightarrow{AC} = \vec{c}, \; \overrightarrow{AD} = \vec{d}$。边 $AB, CD$ 的中点分别为 $M, N$，线段 $MN$ 的中点为 $G$，且 $\angle AGB = \theta$。
    - `[1]` 分别用 $\vec{b}, \vec{c}, \vec{d}$ 表示 $\overrightarrow{AN}, \; \overrightarrow{AG}, \; \overrightarrow{BG}$。
    - `[2]` 分别用 $a$ 表示 $|\overrightarrow{GA}|^2$ 和 $\overrightarrow{GA}\cdot\overrightarrow{GB}$。
    - `[3]` 求 $\cos\theta$ 的值。
  > ⚠️ **教材勘误提示**：原教材第 231 页（`page_0232.jpg`）题干中「$\overrightarrow{AD}=\vec{d}$ とする辺 $AB, CD$」在「とする」后漏印句号「。」。
- **【考点定位】**
  - 正四面体的基底向量表示、空间向量内积展开与夹角余弦计算（甲烷 $\mathrm{CH}_4$ 键角模型）。
- **【图解辅助（SVG 矢量图）】**

<svg viewBox="0 0 420 260" width="420" height="260" xmlns="http://www.w3.org/2000/svg" style="background:#fafafa;border:1px solid #e0e0e0;border-radius:8px;display:block;margin:12px auto;">
  <!-- Vertices: A(210,35), B(90,210), C(245,225), D(340,165) -->
  <!-- Hidden edge BD -->
  <line x1="90" y1="210" x2="340" y2="165" stroke="#94a3b8" stroke-width="1.4" stroke-dasharray="5,4"/>
  <!-- Visible edges -->
  <line x1="210" y1="35" x2="90" y2="210" stroke="#1e293b" stroke-width="1.8"/>
  <line x1="210" y1="35" x2="245" y2="225" stroke="#1e293b" stroke-width="1.8"/>
  <line x1="210" y1="35" x2="340" y2="165" stroke="#1e293b" stroke-width="1.8"/>
  <line x1="90" y1="210" x2="245" y2="225" stroke="#1e293b" stroke-width="1.8"/>
  <line x1="245" y1="225" x2="340" y2="165" stroke="#1e293b" stroke-width="1.8"/>

  <!-- Midpoint M of AB: (150, 122.5) -->
  <!-- Midpoint N of CD: (292.5, 195) -->
  <!-- Midpoint G of MN: (221.25, 158.75) -->
  <line x1="150" y1="122.5" x2="292.5" y2="195" stroke="#0284c7" stroke-width="1.6" stroke-dasharray="4,3"/>
  <line x1="210" y1="35" x2="221.25" y2="158.75" stroke="#dc2626" stroke-width="2"/>
  <line x1="90" y1="210" x2="221.25" y2="158.75" stroke="#dc2626" stroke-width="2"/>

  <!-- Angle arc at G between GA and GB -->
  <path d="M 218.5,134 A 25,25 0 0 0 198,167" fill="none" stroke="#ea580c" stroke-width="1.8"/>
  <text x="193" y="146" font-size="13" fill="#ea580c" font-weight="bold">θ</text>

  <!-- Points -->
  <circle cx="210" cy="35" r="4" fill="#1e293b"/>
  <text x="205" y="24" font-size="14" font-weight="bold" fill="#1e293b">A</text>
  <circle cx="90" cy="210" r="4" fill="#1e293b"/>
  <text x="72" y="218" font-size="14" font-weight="bold" fill="#1e293b">B</text>
  <circle cx="245" cy="225" r="4" fill="#1e293b"/>
  <text x="242" y="244" font-size="14" font-weight="bold" fill="#1e293b">C</text>
  <circle cx="340" cy="165" r="4" fill="#1e293b"/>
  <text x="348" y="168" font-size="14" font-weight="bold" fill="#1e293b">D</text>

  <circle cx="150" cy="122.5" r="3.5" fill="#0284c7"/>
  <text x="130" y="122" font-size="13" font-weight="bold" fill="#0284c7">M</text>
  <circle cx="292.5" cy="195" r="3.5" fill="#0284c7"/>
  <text x="298" y="210" font-size="13" font-weight="bold" fill="#0284c7">N</text>
  <circle cx="221.25" cy="158.75" r="4.5" fill="#dc2626"/>
  <text x="229" y="156" font-size="13" font-weight="bold" fill="#dc2626">G</text>

  <!-- Basis labels -->
  <text x="122" y="88" font-size="12" fill="#475569">b (AB)</text>
  <text x="234" y="118" font-size="12" fill="#475569">c (AC)</text>
  <text x="284" y="92" font-size="12" fill="#475569">d (AD)</text>
</svg>

- **【分步标准解答】**
  - **`[1]` の解答**：
    $N$ は辺 $CD$ の中点であるから：
    $$\overrightarrow{AN} = \frac{\overrightarrow{AC} + \overrightarrow{AD}}{2} = \frac{\vec{c} + \vec{d}}{2}$$
    $M$ は辺 $AB$ の中点であるから $\overrightarrow{AM} = \dfrac{1}{2}\vec{b}$。
    $G$ は線分 $MN$ の中点であるから：
    $$\overrightarrow{AG} = \frac{\overrightarrow{AM} + \overrightarrow{AN}}{2} = \frac{\dfrac{1}{2}\vec{b} + \dfrac{\vec{c} + \vec{d}}{2}}{2} = \frac{\vec{b} + \vec{c} + \vec{d}}{4}$$
    > 💡 讲师批注：把顶点 $A$ 当作位置向量原点（$\vec{a} = \vec{0}$），$\overrightarrow{AG} = \frac{\vec{0}+\vec{b}+\vec{c}+\vec{d}}{4}$ 正好就是 8-(1) 中证明的四面体重心公式！

    また、始点の変換（$\overrightarrow{BG} = \overrightarrow{AG} - \overrightarrow{AB}$）より：
    $$\overrightarrow{BG} = \frac{\vec{b} + \vec{c} + \vec{d}}{4} - \vec{b} = \frac{-3\vec{b} + \vec{c} + \vec{d}}{4}$$

  - **`[2]` の解答**：
    正四面体 $ABCD$ の 1 辺の長さは $a$ で、各面は正三角形であるから、すべての辺のなす角は $60^\circ$ である。したがって：
    $$|\vec{b}| = |\vec{c}| = |\vec{d}| = a$$
    $$\vec{b}\cdot\vec{c} = \vec{c}\cdot\vec{d} = \vec{d}\cdot\vec{b} = a \cdot a \cos 60^\circ = \frac{1}{2}a^2$$
    > 💡 讲师批注：**正四面体解题起手式**：一上来立刻列出「三模长均为 $a$、三两两内积均为 $\frac{1}{2}a^2$」，后续所有内积展开只需直接代换，几乎不会算错。

    $\overrightarrow{GA} = -\overrightarrow{AG}$ であるから：
    $$|\overrightarrow{GA}|^2 = |\overrightarrow{AG}|^2 = \left|\frac{\vec{b} + \vec{c} + \vec{d}}{4}\right|^2 = \frac{1}{16}\left(|\vec{b}|^2 + |\vec{c}|^2 + |\vec{d}|^2 + 2\vec{b}\cdot\vec{c} + 2\vec{c}\cdot\vec{d} + 2\vec{d}\cdot\vec{b}\right)$$
    $$= \frac{1}{16}\left(a^2 + a^2 + a^2 + 2\cdot\frac{1}{2}a^2 + 2\cdot\frac{1}{2}a^2 + 2\cdot\frac{1}{2}a^2\right) = \frac{6a^2}{16} = \frac{3}{8}a^2$$
    次に、$\overrightarrow{GA} = -\overrightarrow{AG}, \; \overrightarrow{GB} = -\overrightarrow{BG}$ より $\overrightarrow{GA}\cdot\overrightarrow{GB} = \overrightarrow{AG}\cdot\overrightarrow{BG}$ であるから：
    $$\overrightarrow{GA}\cdot\overrightarrow{GB} = \frac{1}{4}(\vec{b} + \vec{c} + \vec{d})\cdot\frac{1}{4}(-3\vec{b} + \vec{c} + \vec{d})$$
    $$= \frac{1}{16}\left(-3|\vec{b}|^2 + |\vec{c}|^2 + |\vec{d}|^2 + (1-3)\vec{b}\cdot\vec{c} + (1-3)\vec{b}\cdot\vec{d} + 2\vec{c}\cdot\vec{d}\right)$$
    $$= \frac{1}{16}\left(-3a^2 + a^2 + a^2 - 2\cdot\frac{1}{2}a^2 - 2\cdot\frac{1}{2}a^2 + 2\cdot\frac{1}{2}a^2\right)$$
    $$= \frac{1}{16}(-3a^2 + a^2 + a^2 - a^2 - a^2 + a^2) = \frac{-2a^2}{16} = -\frac{1}{8}a^2$$
    > 💡 讲师批注：展开 $(\vec{b}+\vec{c}+\vec{d})\cdot(-3\vec{b}+\vec{c}+\vec{d})$ 时，可将 $\vec{c}+\vec{d}$ 视作整体 $\vec{u}$，写成 $(\vec{b}+\vec{u})\cdot(-3\vec{b}+\vec{u}) = -3|\vec{b}|^2 - 2\vec{b}\cdot\vec{u} + |\vec{u}|^2$，既快又不易漏项！

  - **`[3]` の解答**：
    正四面体の対称性より（$G$ は重心であり 4 頂点から等距離にあるため）、$|\overrightarrow{GB}| = |\overrightarrow{GA}| = \sqrt{\dfrac{3}{8}}a$ である。
    （直接計算でも $|\overrightarrow{GB}|^2 = \dfrac{1}{16}(9a^2 + a^2 + a^2 - 3a^2 - 3a^2 + a^2) = \dfrac{6}{16}a^2 = \dfrac{3}{8}a^2$ となり一致する。）
    したがって：
    $$\cos\theta = \frac{\overrightarrow{GA}\cdot\overrightarrow{GB}}{|\overrightarrow{GA}||\overrightarrow{GB}|} = \frac{-\dfrac{1}{8}a^2}{\dfrac{3}{8}a^2} = -\frac{1}{3}$$
    > 💡 讲师批注：$\cos\theta = -\frac{1}{3}$（约 $109.5^\circ$）是化学中正四面体分子（如甲烷 $\mathrm{CH}_4$）的著名键角余弦值，记忆这个常识可以直接秒验答案！
- **【最终答案】**
  - **`[1]` $\overrightarrow{AN} = \dfrac{\vec{c} + \vec{d}}{2}, \quad \overrightarrow{AG} = \dfrac{\vec{b} + \vec{c} + \vec{d}}{4}, \quad \overrightarrow{BG} = \dfrac{-3\vec{b} + \vec{c} + \vec{d}}{4}$**
  - **`[2]` $|\overrightarrow{GA}|^2 = \dfrac{3}{8}a^2, \quad \overrightarrow{GA}\cdot\overrightarrow{GB} = -\dfrac{1}{8}a^2$**
  - **`[3]` $\cos\theta = -\dfrac{1}{3}$**

---

#### 演習問題 8-(3)
- **【原题重现与翻译】**
  - 原题：平行六面体 $ABCD-EFGH$ において、辺 $AB, AD$ を $2:1$ に内分する点をそれぞれ $P, Q$ とし、平行四辺形 $EFGH$ の対角線 $EG$ を $1:2$ に内分する点を $R$ とするとき、平行六面体の対角線 $AG$ は $\triangle PQR$ の重心 $K$ を通ることを証明せよ。
  - 中文：在平行六面体 $ABCD-EFGH$ 中，设按 $2:1$ 内分边 $AB, AD$ 的点分别为 $P, Q$，按 $1:2$ 内分平行四边形 $EFGH$ 的对角线 $EG$ 的点为 $R$。证明：平行六面体的对角线 $AG$ 经过 $\triangle PQR$ 的重心 $K$。
- **【考点定位】**
  - 平行六面体的三棱基底向量表示、共线条件（$\overrightarrow{AK} = k\overrightarrow{AG}$ 且 $0 < k < 1$）。
- **【图解辅助（SVG 矢量图）】**

<svg viewBox="0 0 430 270" width="430" height="270" xmlns="http://www.w3.org/2000/svg" style="background:#fafafa;border:1px solid #e0e0e0;border-radius:8px;display:block;margin:12px auto;">
  <!-- Top face ABCD: A(115,65), B(275,65), C(345,25), D(185,25) -->
  <!-- Bottom face EFGH: E(75,215), F(235,215), G(305,175), H(145,175) -->
  <!-- Hidden edges: DH, EH, GH -->
  <line x1="185" y1="25" x2="145" y2="175" stroke="#94a3b8" stroke-width="1.3" stroke-dasharray="4,4"/>
  <line x1="75" y1="215" x2="145" y2="175" stroke="#94a3b8" stroke-width="1.3" stroke-dasharray="4,4"/>
  <line x1="145" y1="175" x2="305" y2="175" stroke="#94a3b8" stroke-width="1.3" stroke-dasharray="4,4"/>

  <!-- Visible edges -->
  <polygon points="115,65 275,65 345,25 185,25" fill="none" stroke="#1e293b" stroke-width="1.7"/>
  <line x1="115" y1="65" x2="75" y2="215" stroke="#1e293b" stroke-width="1.7"/>
  <line x1="275" y1="65" x2="235" y2="215" stroke="#1e293b" stroke-width="1.7"/>
  <line x1="345" y1="25" x2="305" y2="175" stroke="#1e293b" stroke-width="1.7"/>
  <line x1="75" y1="215" x2="235" y2="215" stroke="#1e293b" stroke-width="1.7"/>
  <line x1="235" y1="215" x2="305" y2="175" stroke="#1e293b" stroke-width="1.7"/>

  <!-- Diagonal EG -->
  <line x1="75" y1="215" x2="305" y2="175" stroke="#64748b" stroke-width="1.4" stroke-dasharray="3,3"/>

  <!-- P = A + 2/3(B-A) = (221.7, 65) -->
  <!-- Q = A + 2/3(D-A) = (161.7, 38.3) -->
  <!-- R = E + 1/3(G-E) = (151.7, 201.7) -->
  <!-- K = (P+Q+R)/3 = (178.3, 101.7) -->
  <!-- Check A + 1/3(G-A) = (115+63.3, 65+36.7) = (178.3, 101.7)! Exact! -->

  <!-- Triangle PQR -->
  <polygon points="221.7,65 161.7,38.3 151.7,201.7" fill="#fef3c7" fill-opacity="0.55" stroke="#d97706" stroke-width="1.7"/>

  <!-- Diagonal AG -->
  <line x1="115" y1="65" x2="305" y2="175" stroke="#dc2626" stroke-width="2"/>

  <!-- Vertices -->
  <text x="97" y="65" font-size="13" font-weight="bold" fill="#1e293b">A</text>
  <text x="282" y="70" font-size="13" font-weight="bold" fill="#1e293b">B</text>
  <text x="352" y="28" font-size="13" font-weight="bold" fill="#1e293b">C</text>
  <text x="176" y="18" font-size="13" font-weight="bold" fill="#1e293b">D</text>
  <text x="58" y="223" font-size="13" font-weight="bold" fill="#1e293b">E</text>
  <text x="240" y="232" font-size="13" font-weight="bold" fill="#1e293b">F</text>
  <text x="313" y="182" font-size="13" font-weight="bold" fill="#1e293b">G</text>
  <text x="134" y="170" font-size="13" font-weight="bold" fill="#64748b">H</text>

  <!-- Special points -->
  <circle cx="221.7" cy="65" r="4" fill="#d97706"/>
  <text x="225" y="57" font-size="13" font-weight="bold" fill="#b45309">P</text>
  <circle cx="161.7" cy="38.3" r="4" fill="#d97706"/>
  <text x="145" y="34" font-size="13" font-weight="bold" fill="#b45309">Q</text>
  <circle cx="151.7" cy="201.7" r="4" fill="#d97706"/>
  <text x="148" y="220" font-size="13" font-weight="bold" fill="#b45309">R</text>
  <circle cx="178.3" cy="101.7" r="4.5" fill="#dc2626"/>
  <text x="186" y="100" font-size="13" font-weight="bold" fill="#dc2626">K (AK = 1/3 AG)</text>

  <text x="20" y="255" font-size="12" fill="#334155">注：平行六面体中 AG = AB + AD + AE，AK = (AP + AQ + AR)/3 = (1/3)AG</text>
</svg>

- **【分步标准解答】**
  $\overrightarrow{AB} = \vec{b}, \; \overrightarrow{AD} = \vec{d}, \; \overrightarrow{AE} = \vec{e}$ とおく。
  平行六面体の性質より、対角線ベクトル $\overrightarrow{AG}$ は：
  $$\overrightarrow{AG} = \vec{b} + \vec{d} + \vec{e}$$
  > 💡 讲师批注：在平行六面体 $ABCD-EFGH$ 中，顶面 $ABCD$ 与底面 $EFGH$ 对应顶点一一垂直/平行对应（$A\leftrightarrow E, \; B\leftrightarrow F, \; C\leftrightarrow G, \; D\leftrightarrow H$），因此 $\overrightarrow{EG} = \overrightarrow{AC} = \vec{b}+\vec{d}$，$\overrightarrow{AG} = \overrightarrow{AE}+\overrightarrow{EG} = \vec{b}+\vec{d}+\vec{e}$。

  次に、3 点 $P, Q, R$ の $A$ を始点とする位置ベクトルを求める：
  - $P$ は辺 $AB$ を $2:1$ に内分する点だから：$\overrightarrow{AP} = \dfrac{2}{3}\vec{b}$
  - $Q$ は辺 $AD$ を $2:1$ に内分する点だから：$\overrightarrow{AQ} = \dfrac{2}{3}\vec{d}$
  - $R$ は対角線 $EG$ を $1:2$ に内分する点だから：
    $$\overrightarrow{AR} = \frac{2\overrightarrow{AE} + 1\overrightarrow{AG}}{1 + 2} = \frac{2\vec{e} + (\vec{b} + \vec{d} + \vec{e})}{3} = \frac{1}{3}\vec{b} + \frac{1}{3}\vec{d} + \vec{e}$$
  > 💡 讲师批注：求 $\overrightarrow{AR}$ 时也可以写成 $\overrightarrow{AE} + \frac{1}{3}\overrightarrow{EG} = \vec{e} + \frac{1}{3}(\vec{b}+\vec{d})$，结果完全一样，而且更直观！

  $K$ は $\triangle PQR$ の重心であるから：
  $$\overrightarrow{AK} = \frac{\overrightarrow{AP} + \overrightarrow{AQ} + \overrightarrow{AR}}{3} = \frac{\dfrac{2}{3}\vec{b} + \dfrac{2}{3}\vec{d} + \left(\dfrac{1}{3}\vec{b} + \dfrac{1}{3}\vec{d} + \vec{e}\right)}{3} = \frac{\vec{b} + \vec{d} + \vec{e}}{3} = \frac{1}{3}\overrightarrow{AG}$$
  $\overrightarrow{AK} = \dfrac{1}{3}\overrightarrow{AG}$ より、点 $K$ は線分 $AG$ を $1:2$ に内分する点である。
  したがって、対角線 $AG$ は $\triangle PQR$ の重心 $K$ を通る。（証明終）
  > 💡 讲师批注：注意题目问的是「対角線 $AG$（线段）を通る」，因为比例系数 $\frac{1}{3}$ 满足 $0 < \frac{1}{3} < 1$，不仅三点 $A, K, G$ 共线，而且 $K$ 严格落在线段 $AG$ 的内部，证明无懈可击！
- **【最终答案】**
  **$\overrightarrow{AK} = \dfrac{1}{3}\overrightarrow{AG}$ が成り立つため、対角線 $AG$ は重心 $K$ を通る（証明完了）。**

---

#### 演習問題 8-(4)
- **【原题重现与翻译】**
  - 原题：四面体 $OABC$ の辺 $OA$ の中点を $P$、辺 $BC$ を $2:1$ に内分する点を $Q$、辺 $OC$ を $1:3$ に内分する点を $R$、辺 $AB$ を $1:6$ に内分する点を $S$ とする。$\overrightarrow{OA} = \vec{a}, \; \overrightarrow{OB} = \vec{b}, \; \overrightarrow{OC} = \vec{c}$ とするとき
    - `[1]` $\overrightarrow{PQ}$ を $\vec{a}, \vec{b}, \vec{c}$ で表せ。
    - `[2]` $\overrightarrow{RS}$ を $\vec{a}, \vec{b}, \vec{c}$ で表せ。
    - `[3]` 直線 $PQ$ と直線 $RS$ は交わり、その交点を $T$ とするとき、$\overrightarrow{OT}$ を $\vec{a}, \vec{b}, \vec{c}$ で表せ。
  - 中文：设四面体 $OABC$ 中，边 $OA$ 的中点为 $P$，按 $2:1$ 内分边 $BC$ 的点为 $Q$，按 $1:3$ 内分边 $OC$ 的点为 $R$，按 $1:6$ 内分边 $AB$ 的点为 $S$。令 $\overrightarrow{OA} = \vec{a}, \; \overrightarrow{OB} = \vec{b}, \; \overrightarrow{OC} = \vec{c}$：
    - `[1]` 用 $\vec{a}, \vec{b}, \vec{c}$ 表示 $\overrightarrow{PQ}$。
    - `[2]` 用 $\vec{a}, \vec{b}, \vec{c}$ 表示 $\overrightarrow{RS}$。
    - `[3]` 直线 $PQ$ 与直线 $RS$ 相交，设交点为 $T$，用 $\vec{a}, \vec{b}, \vec{c}$ 表示 $\overrightarrow{OT}$。
  > ⚠️ **教材勘误提示**：原教材第 232 页（`page_0233.jpg`）小问 `[2]` 误多印了一个助词「を」（「$\overrightarrow{RS}$ をを $\vec{a}, \vec{b}, \vec{c}$ で表せ」）。
- **【考点定位】**
  - 空间四面体基底分解、直线交点求法（双路径表示 + 空间向量 1 次独立系数比较）。
- **【分步标准解答】**
  まず、各点の位置ベクトルを $\vec{a}, \vec{b}, \vec{c}$ で表す：
  $$\overrightarrow{OP} = \frac{1}{2}\vec{a}, \qquad \overrightarrow{OQ} = \frac{\vec{b} + 2\vec{c}}{3}, \qquad \overrightarrow{OR} = \frac{1}{4}\vec{c}, \qquad \overrightarrow{OS} = \frac{6\vec{a} + \vec{b}}{7}$$
  - **`[1]` の解答**：
    $$\overrightarrow{PQ} = \overrightarrow{OQ} - \overrightarrow{OP} = \frac{\vec{b} + 2\vec{c}}{3} - \frac{1}{2}\vec{a} = -\frac{1}{2}\vec{a} + \frac{1}{3}\vec{b} + \frac{2}{3}\vec{c}$$
  - **`[2]` の解答**：
    $$\overrightarrow{RS} = \overrightarrow{OS} - \overrightarrow{OR} = \frac{6\vec{a} + \vec{b}}{7} - \frac{1}{4}\vec{c} = \frac{6}{7}\vec{a} + \frac{1}{7}\vec{b} - \frac{1}{4}\vec{c}$$
  - **`[3]` の解答**：
    点 $T$ は直線 $PQ$ 上にあるから、実数 $s$ を用いて：
    $$\overrightarrow{OT} = \overrightarrow{OP} + s\overrightarrow{PQ} = \frac{1}{2}\vec{a} + s\left(-\frac{1}{2}\vec{a} + \frac{1}{3}\vec{b} + \frac{2}{3}\vec{c}\right) = \frac{1 - s}{2}\vec{a} + \frac{s}{3}\vec{b} + \frac{2s}{3}\vec{c} \qquad \cdots ①$$
    また、点 $T$ は直線 $RS$ 上にあるから、実数 $t$ を用いて：
    $$\overrightarrow{OT} = \overrightarrow{OR} + t\overrightarrow{RS} = \frac{1}{4}\vec{c} + t\left(\frac{6}{7}\vec{a} + \frac{1}{7}\vec{b} - \frac{1}{4}\vec{c}\right) = \frac{6t}{7}\vec{a} + \frac{t}{7}\vec{b} + \frac{1 - t}{4}\vec{c} \qquad \cdots ②$$
    > 💡 讲师批注：求空间两直线的交点，最标准的日本考场套路就是**用两条直线各自的参数方程写出 $\overrightarrow{OT}$**，再利用 1 次独立（基底分解唯一性）联立三个方程！

    4点 $O, A, B, C$ は同じ平面上にない（$\vec{a}, \vec{b}, \vec{c}$ は 1 次独立である）から、①・② の各係数を比較すると：
    $$\begin{cases} \dfrac{1 - s}{2} = \dfrac{6t}{7} & \cdots (a) \\[6pt] \dfrac{s}{3} = \dfrac{t}{7} & \cdots (b) \\[6pt] \dfrac{2s}{3} = \dfrac{1 - t}{4} & \cdots (c) \end{cases}$$
    $(b)$ より $t = \dfrac{7}{3}s$。これを $(a)$ に代入すると：
    $$\frac{1 - s}{2} = \frac{6}{7}\cdot\frac{7}{3}s = 2s \implies 1 - s = 4s \implies 5s = 1 \implies s = \frac{1}{5}$$
    よって $t = \dfrac{7}{3}\cdot\dfrac{1}{5} = \dfrac{7}{15}$。
    これらを $(c)$ に代入して検算すると：
    $$\text{左辺} = \frac{2}{3}\cdot\frac{1}{5} = \frac{2}{15}, \qquad \text{右辺} = \frac{1 - \frac{7}{15}}{4} = \frac{\frac{8}{15}}{4} = \frac{2}{15}$$
    となり $(c)$ も満たされる。
    > 💡 讲师批注：3 个方程 2 个未知数时，由前两式解出 $s, t$ 后**必须代入第 3 式验证相容性**——这既是检验计算是否出错的最佳手段，也是两直线确实相交（而非异面）的严格证明！

    $s = \dfrac{1}{5}$ を ① に代入すると：
    $$\overrightarrow{OT} = \frac{1 - \frac{1}{5}}{2}\vec{a} + \frac{\frac{1}{5}}{3}\vec{b} + \frac{\frac{2}{5}}{3}\vec{c} = \frac{2}{5}\vec{a} + \frac{1}{15}\vec{b} + \frac{2}{15}\vec{c}$$
- **【最终答案】**
  - **`[1]` $\overrightarrow{PQ} = -\dfrac{1}{2}\vec{a} + \dfrac{1}{3}\vec{b} + \dfrac{2}{3}\vec{c}$**
  - **`[2]` $\overrightarrow{RS} = \dfrac{6}{7}\vec{a} + \dfrac{1}{7}\vec{b} - \dfrac{1}{4}\vec{c}$**
  - **`[3]` $\overrightarrow{OT} = \dfrac{2}{5}\vec{a} + \dfrac{1}{15}\vec{b} + \dfrac{2}{15}\vec{c}$**（または $\dfrac{6\vec{a} + \vec{b} + 2\vec{c}}{15}$）

---

#### 演習問題 8-(5)
- **【原题重现与翻译】**
  - 原题：3点 $A(2, 0, 0), \; B(0, -1, 0), \; C(0, 0, 2)$ と、2つのベクトル $\vec{u} = (0, 1, 2), \; \vec{v} = (1, 1, 1)$ がある。
    - `[1]` $\overrightarrow{AP}$ と $\vec{u}$ が平行、かつ $\overrightarrow{BP}$ と $\vec{v}$ が平行となるような点 $P$ の座標を求めよ。
    - `[2]` `[1]` で求めた点 $P$ は 3点 $A, B, C$ の定める平面上にあることを示せ。
  - 中文：已知三点 $A(2, 0, 0), \; B(0, -1, 0), \; C(0, 0, 2)$ 以及两个向量 $\vec{u} = (0, 1, 2), \; \vec{v} = (1, 1, 1)$。
    - `[1]` 求满足 $\overrightarrow{AP} \parallel \vec{u}$ 且 $\overrightarrow{BP} \parallel \vec{v}$ 的点 $P$ 的坐标。
    - `[2]` 证明 `[1]` 中求得的点 $P$ 位于三点 $A, B, C$ 所确定的平面上。
- **【考点定位】**
  - 空间直线的参数表示与交点、四点共面条件（$\overrightarrow{AP} = p\overrightarrow{AB} + q\overrightarrow{AC}$）。
- **【分步标准解答】**
  - **`[1]` の解答**：
    $\overrightarrow{AP} \parallel \vec{u}$ より $\overrightarrow{AP} = s\vec{u}$ となる実数 $s$ が存在し、点 $P$ の座標は：
    $$\overrightarrow{OP} = \overrightarrow{OA} + s\vec{u} = (2, 0, 0) + s(0, 1, 2) = (2, \; s, \; 2s)$$
    また、$\overrightarrow{BP} \parallel \vec{v}$ より $\overrightarrow{BP} = t\vec{v}$ となる実数 $t$ が存在し、点 $P$ の座標は：
    $$\overrightarrow{OP} = \overrightarrow{OB} + t\vec{v} = (0, -1, 0) + t(1, 1, 1) = (t, \; -1 + t, \; t)$$
    各成分を比較すると：
    $$\begin{cases} 2 = t \\ s = -1 + t \\ 2s = t \end{cases}$$
    第 1 式より $t = 2$、第 2 式より $s = -1 + 2 = 1$。これらは第 3 式 $2(1) = 2$ も満たす。
    よって、求める点 $P$ の座標は $(2, 1, 2)$ である。

  - **`[2]` の解答**：
    まず、3点 $A, B, C$ が一直線上にないことを確認する：
    $$\overrightarrow{AB} = (-2, -1, 0), \qquad \overrightarrow{AC} = (-2, 0, 2)$$
    $\overrightarrow{AB}$ と $\overrightarrow{AC}$ は平行でないから、3点 $A, B, C$ は 1 つの平面を定める。
    ここで $\overrightarrow{AP} = (2 - 2, \; 1 - 0, \; 2 - 0) = (0, 1, 2)$ に対し、$\overrightarrow{AP} = p\overrightarrow{AB} + q\overrightarrow{AC}$ を満たす実数 $p, q$ の存在を調べる：
    $$(0, 1, 2) = p(-2, -1, 0) + q(-2, 0, 2) = (-2p - 2q, \; -p, \; 2q)$$
    各成分を比較すると：
    $$\begin{cases} -2p - 2q = 0 \\ -p = 1 \\ 2q = 2 \end{cases}$$
    第 2 式より $p = -1$、第 3 式より $q = 1$。これを第 1 式に代入すると $-2(-1) - 2(1) = 2 - 2 = 0$ となり成り立つ。
    よって $\overrightarrow{AP} = -\overrightarrow{AB} + \overrightarrow{AC}$ を満たす実数 $p = -1, \; q = 1$ が存在するから、点 $P$ は平面 $ABC$ 上にある。（証明終）
    > 💡 讲师批注：本题用平面截距式方程秒验也很爽：$A(2,0,0), B(0,-1,0), C(0,0,2)$ 确定的平面方程为 $\frac{x}{2} + \frac{y}{-1} + \frac{z}{2} = 1$，代入 $P(2,1,2)$ 得 $1 - 1 + 1 = 1$，立刻确认 $P$ 在平面 $ABC$ 上！
- **【最终答案】**
  - **`[1]` $P(2, \; 1, \; 2)$**
  - **`[2]` $\overrightarrow{AP} = -\overrightarrow{AB} + \overrightarrow{AC}$ が成り立つため、点 $P$ は平面 $ABC$ 上にある（証明完了）。**

---

#### 演習問題 8-(6)
- **【原题重现与翻译】**
  - 原题：四面体 $OABC$ において、$P$ を辺 $OA$ の中点、$Q$ を辺 $OB$ を $2:1$ に内分する点、$R$ を辺 $BC$ の中点とする。$P, Q, R$ を通る平面と辺 $AC$ の交点を $S$ とする。$\overrightarrow{OA} = \vec{a}, \; \overrightarrow{OB} = \vec{b}, \; \overrightarrow{OC} = \vec{c}$ とおく。
    - `[1]` $\overrightarrow{PQ}, \; \overrightarrow{PR}$ をそれぞれ $\vec{a}, \vec{b}, \vec{c}$ を用いて表せ。
    - `[2]` $|\overrightarrow{AS}| : |\overrightarrow{SC}|$ を求めよ。
  - 中文：在四面体 $OABC$ 中，设 $P$ 为边 $OA$ 的中点，$Q$ 为按 $2:1$ 内分边 $OB$ 的点，$R$ 为边 $BC$ 的中点。过 $P, Q, R$ 的平面与边 $AC$ 的交点记为 $S$。令 $\overrightarrow{OA} = \vec{a}, \; \overrightarrow{OB} = \vec{b}, \; \overrightarrow{OC} = \vec{c}$：
    - `[1]` 分别用 $\vec{a}, \vec{b}, \vec{c}$ 表示 $\overrightarrow{PQ}, \; \overrightarrow{PR}$。
    - `[2]` 求 $|\overrightarrow{AS}| : |\overrightarrow{SC}|$。
- **【考点定位】**
  - 空间平面与棱的交点问题（EJU 超高频经典题型：共面条件 + 共线条件 + 1 次独立）。
- **【图解辅助（SVG 矢量图）】**

<svg viewBox="0 0 420 250" width="420" height="250" xmlns="http://www.w3.org/2000/svg" style="background:#fafafa;border:1px solid #e0e0e0;border-radius:8px;display:block;margin:12px auto;">
  <!-- O(205,30), A(85,200), B(235,220), C(345,155) -->
  <!-- Hidden edge AC -->
  <line x1="85" y1="200" x2="345" y2="155" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="5,4"/>
  <!-- Visible edges -->
  <line x1="205" y1="30" x2="85" y2="200" stroke="#1e293b" stroke-width="1.8"/>
  <line x1="205" y1="30" x2="235" y2="220" stroke="#1e293b" stroke-width="1.8"/>
  <line x1="205" y1="30" x2="345" y2="155" stroke="#1e293b" stroke-width="1.8"/>
  <line x1="85" y1="200" x2="235" y2="220" stroke="#1e293b" stroke-width="1.8"/>
  <line x1="235" y1="220" x2="345" y2="155" stroke="#1e293b" stroke-width="1.8"/>

  <!-- P: midpoint OA = (145, 115) -->
  <!-- Q: 2:1 on OB = (205 + 2/3*30, 30 + 2/3*190) = (225, 156.7) -->
  <!-- R: midpoint BC = (290, 187.5) -->
  <!-- S: 2:1 on AC = (85 + 2/3*260, 200 - 2/3*45) = (258.3, 170) -->

  <!-- Cross-section quadrilateral PQRS -->
  <polygon points="145,115 225,156.7 290,187.5 258.3,170" fill="#dbeafe" fill-opacity="0.55" stroke="#2563eb" stroke-width="1.7"/>
  <line x1="145" y1="115" x2="258.3" y2="170" stroke="#2563eb" stroke-width="1.4" stroke-dasharray="4,3"/>

  <!-- Vertices -->
  <circle cx="205" cy="30" r="4" fill="#1e293b"/>
  <text x="199" y="20" font-size="14" font-weight="bold" fill="#1e293b">O</text>
  <circle cx="85" cy="200" r="4" fill="#1e293b"/>
  <text x="68" y="208" font-size="14" font-weight="bold" fill="#1e293b">A</text>
  <circle cx="235" cy="220" r="4" fill="#1e293b"/>
  <text x="232" y="238" font-size="14" font-weight="bold" fill="#1e293b">B</text>
  <circle cx="345" cy="155" r="4" fill="#1e293b"/>
  <text x="354" y="158" font-size="14" font-weight="bold" fill="#1e293b">C</text>

  <!-- Points P, Q, R, S -->
  <circle cx="145" cy="115" r="4" fill="#2563eb"/>
  <text x="125" y="115" font-size="13" font-weight="bold" fill="#2563eb">P</text>
  <circle cx="225" cy="156.7" r="4" fill="#2563eb"/>
  <text x="206" y="164" font-size="13" font-weight="bold" fill="#2563eb">Q</text>
  <circle cx="290" cy="187.5" r="4" fill="#2563eb"/>
  <text x="296" y="202" font-size="13" font-weight="bold" fill="#2563eb">R</text>
  <circle cx="258.3" cy="170" r="4.5" fill="#dc2626"/>
  <text x="260" y="161" font-size="13" font-weight="bold" fill="#dc2626">S (AS:SC = 2:1)</text>
</svg>

- **【分步标准解答】**
  - **`[1]` の解答**：
    条件より、各点の位置ベクトルは次の通り：
    $$\overrightarrow{OP} = \frac{1}{2}\vec{a}, \qquad \overrightarrow{OQ} = \frac{2}{3}\vec{b}, \qquad \overrightarrow{OR} = \frac{\vec{b} + \vec{c}}{2}$$
    したがって：
    $$\overrightarrow{PQ} = \overrightarrow{OQ} - \overrightarrow{OP} = -\frac{1}{2}\vec{a} + \frac{2}{3}\vec{b}$$
    $$\overrightarrow{PR} = \overrightarrow{OR} - \overrightarrow{OP} = -\frac{1}{2}\vec{a} + \frac{1}{2}\vec{b} + \frac{1}{2}\vec{c}$$

  - **`[2]` の解答**：
    点 $S$ は平面 $PQR$ 上にあるから、実数 $s, t$ を用いて $\overrightarrow{PS} = s\overrightarrow{PQ} + t\overrightarrow{PR}$ と表せる。
    よって：
    $$\overrightarrow{OS} = \overrightarrow{OP} + s\overrightarrow{PQ} + t\overrightarrow{PR}$$
    $$= \frac{1}{2}\vec{a} + s\left(-\frac{1}{2}\vec{a} + \frac{2}{3}\vec{b}\right) + t\left(-\frac{1}{2}\vec{a} + \frac{1}{2}\vec{b} + \frac{1}{2}\vec{c}\right)$$
    $$= \frac{1 - s - t}{2}\vec{a} + \left(\frac{2}{3}s + \frac{1}{2}t\right)\vec{b} + \frac{1}{2}t\vec{c} \qquad \cdots ①$$
    > 💡 讲师批注：把「$S$ 在平面 $PQR$ 上」写成 $\overrightarrow{OS} = \overrightarrow{OP} + s\overrightarrow{PQ} + t\overrightarrow{PR}$ 并按基底 $\vec{a}, \vec{b}, \vec{c}$ 合并同类项，可直接衔接第 `[1]` 问结果。

    一方、点 $S$ は辺 $AC$ 上にあるから、実数 $k$ を用いて $\overrightarrow{OS} = (1 - k)\vec{a} + k\vec{c}$ と表せる。
    すなわち、$\vec{b}$ の係数は $0$ であり、$\vec{a}$ と $\vec{c}$ の係数の和は $1$ である。
    $\vec{a}, \vec{b}, \vec{c}$ は 1 次独立であるから、① と比較して：
    $$\begin{cases} \dfrac{2}{3}s + \dfrac{1}{2}t = 0 & \cdots ② \\[6pt] \dfrac{1 - s - t}{2} + \dfrac{1}{2}t = 1 & \cdots ③ \end{cases}$$
    > 💡 讲师批注：**神来之笔！** 看第 ③ 式中 $-\frac{t}{2}$ 与 $+\frac{t}{2}$ 恰好直接抵消！不用设多余变量 $k$ 就能瞬间解出 $s$！

    ③ より：
    $$\frac{1 - s}{2} = 1 \implies 1 - s = 2 \implies s = -1$$
    これを ② に代入すると：
    $$-\frac{2}{3} + \frac{1}{2}t = 0 \implies \frac{1}{2}t = \frac{2}{3} \implies t = \frac{4}{3}$$
    $s = -1, \; t = \dfrac{4}{3}$ を ① に代入すると：
    $$\overrightarrow{OS} = \frac{1 - (-1) - \frac{4}{3}}{2}\vec{a} + 0\cdot\vec{b} + \frac{1}{2}\cdot\frac{4}{3}\vec{c} = \frac{1}{3}\vec{a} + \frac{2}{3}\vec{c} = \frac{1\cdot\vec{a} + 2\cdot\vec{c}}{2 + 1}$$
    したがって、点 $S$ は辺 $AC$ を $2:1$ に内分する点であるから：
    $$|\overrightarrow{AS}| : |\overrightarrow{SC}| = 2 : 1$$
    > 💡 讲师批注：**警惕比例写反！** $\overrightarrow{OS} = \frac{1\cdot\vec{a} + 2\cdot\vec{c}}{2+1}$ 表示 $S$ 靠近 $C$（因为 $\vec{c}$ 的权重更大），所以 $AS : SC = 2 : 1$，切勿粗心写成 $1 : 2$！
- **【最终答案】**
  - **`[1]` $\overrightarrow{PQ} = -\dfrac{1}{2}\vec{a} + \dfrac{2}{3}\vec{b}, \quad \overrightarrow{PR} = -\dfrac{1}{2}\vec{a} + \dfrac{1}{2}\vec{b} + \dfrac{1}{2}\vec{c}$**
  - **`[2]` $|\overrightarrow{AS}| : |\overrightarrow{SC}| = 2 : 1$**

---

#### 演習問題 8-(7)
- **【原题重现与翻译】**
  - 原题：空間において、3点 $A(5, 0, 1), \; B(4, 2, 0), \; C(0, 1, 5)$ を頂点とする三角形 $ABC$ がある。原点 $O(0, 0, 0)$ から平面 $ABC$ に垂線を下ろし、平面 $ABC$ との交点を $H$ とするとき、$H$ の座標を求めよ。
  - 中文：在空间中，已知以三点 $A(5, 0, 1), \; B(4, 2, 0), \; C(0, 1, 5)$ 为顶点的三角形 $ABC$。从原点 $O(0, 0, 0)$ 向平面 $ABC$ 作垂线，设垂足（与平面 $ABC$ 的交点）为 $H$，求 $H$ 的坐标。
- **【考点定位】**
  - 空间点向平面作垂线求垂足坐标（EJU 压轴高频：共面条件 + 线面垂直 $\iff$ 与平面内两不共线向量垂直）。
- **【图解辅助（SVG 矢量图）】**

<svg viewBox="0 0 420 220" width="420" height="220" xmlns="http://www.w3.org/2000/svg" style="background:#fafafa;border:1px solid #e0e0e0;border-radius:8px;display:block;margin:12px auto;">
  <!-- Plane ABC -->
  <polygon points="40,185 330,185 390,105 100,105" fill="#f0fdf4" stroke="#16a34a" stroke-width="1.5"/>
  <text x="302" y="177" font-size="12" fill="#15803d" font-weight="bold">平面 ABC</text>

  <!-- Triangle ABC inside plane -->
  <polygon points="115,165 270,170 230,120" fill="#dcfce7" fill-opacity="0.7" stroke="#15803d" stroke-width="1.5"/>
  <circle cx="115" cy="165" r="3.5" fill="#15803d"/>
  <text x="95" y="170" font-size="13" font-weight="bold" fill="#15803d">A</text>
  <circle cx="270" cy="170" r="3.5" fill="#15803d"/>
  <text x="276" y="174" font-size="13" font-weight="bold" fill="#15803d">B</text>
  <circle cx="230" cy="120" r="3.5" fill="#15803d"/>
  <text x="236" y="122" font-size="13" font-weight="bold" fill="#15803d">C</text>

  <!-- Origin O above plane -->
  <circle cx="200" cy="35" r="4.5" fill="#dc2626"/>
  <text x="208" y="39" font-size="13" font-weight="bold" fill="#dc2626">O(0, 0, 0)</text>

  <!-- Foot H on plane -->
  <circle cx="200" cy="148" r="4.5" fill="#2563eb"/>
  <text x="208" y="156" font-size="13" font-weight="bold" fill="#2563eb">H(2, 2, 2)</text>

  <!-- Perpendicular OH -->
  <line x1="200" y1="35" x2="200" y2="148" stroke="#dc2626" stroke-width="2"/>
  <!-- Right angle mark -->
  <polyline points="200,136 212,136 212,148" fill="none" stroke="#dc2626" stroke-width="1.4"/>

  <text x="22" y="208" font-size="12" fill="#334155">两大条件：① H ∈ 平面 ABC（OH = OA + sAB + tAC）；② OH ⊥ AB 且 OH ⊥ AC</text>
</svg>

- **【分步标准解答】**
  $$\overrightarrow{AB} = (4 - 5, \; 2 - 0, \; 0 - 1) = (-1, \; 2, \; -1)$$
  $$\overrightarrow{AC} = (0 - 5, \; 1 - 0, \; 5 - 1) = (-5, \; 1, \; 4)$$
  点 $H$ は平面 $ABC$ 上にあるから、実数 $s, t$ を用いて $\overrightarrow{OH} = \overrightarrow{OA} + s\overrightarrow{AB} + t\overrightarrow{AC}$ と表せる：
  $$\overrightarrow{OH} = (5, 0, 1) + s(-1, 2, -1) + t(-5, 1, 4) = (5 - s - 5t, \; 2s + t, \; 1 - s + 4t)$$
  > 💡 讲师批注：这是日本 EJU 考场最规范的标准解法（不依赖法向量概念），只需设出 2 个实参数 $s, t$，再由 2 个垂直内积方程解出即可。

  $\overrightarrow{OH} \perp \text{平面 } ABC$ であるから、$\overrightarrow{OH} \perp \overrightarrow{AB}$ かつ $\overrightarrow{OH} \perp \overrightarrow{AC}$ すなわち：
  $$\overrightarrow{OH}\cdot\overrightarrow{AB} = 0 \quad \text{かつ} \quad \overrightarrow{OH}\cdot\overrightarrow{AC} = 0$$
  成分で計算すると：
  1. $\overrightarrow{OH}\cdot\overrightarrow{AB} = 0$ より：
     $$(-1)(5 - s - 5t) + 2(2s + t) + (-1)(1 - s + 4t) = 0$$
     $$(-5 + s + 5t) + (4s + 2t) + (-1 + s - 4t) = 0$$
     $$6s + 3t - 6 = 0 \implies 2s + t = 2 \qquad \cdots ①$$
  2. $\overrightarrow{OH}\cdot\overrightarrow{AC} = 0$ より：
     $$(-5)(5 - s - 5t) + 1(2s + t) + 4(1 - s + 4t) = 0$$
     $$(-25 + 5s + 25t) + (2s + t) + (4 - 4s + 16t) = 0$$
     $$3s + 42t - 21 = 0 \implies s + 14t = 7 \qquad \cdots ②$$
  ① より $t = 2 - 2s$。これを ② に代入すると：
  $$s + 14(2 - 2s) = 7 \implies -27s = -21 \implies s = \frac{7}{9}$$
  よって $t = 2 - 2\cdot\dfrac{7}{9} = \dfrac{4}{9}$。
  これらを $\overrightarrow{OH}$ に代入すると：
  $$x = 5 - \frac{7}{9} - 5\cdot\frac{4}{9} = 5 - \frac{27}{9} = 2$$
  $$y = 2\cdot\frac{7}{9} + \frac{4}{9} = \frac{18}{9} = 2$$
  $$z = 1 - \frac{7}{9} + 4\cdot\frac{4}{9} = 1 + \frac{9}{9} = 2$$
  したがって、求める垂足 $H$ の座標は $(2, 2, 2)$ である。
  > 💡 讲师批注：**国内法向量极速验算法**：草稿纸上用叉乘算出法向量 $\overrightarrow{AB}\times\overrightarrow{AC} = (9, 9, 9) \parallel (1, 1, 1)$，于是平面 $ABC$ 方程为 $x + y + z = 5 + 0 + 1 = 6$（代入 $B, C$ 均满足 $6$）。因为 $\overrightarrow{OH} \parallel (1, 1, 1)$，设 $H(k, k, k)$ 代入 $3k = 6 \implies k = 2 \implies H(2, 2, 2)$，3 秒完成验算！
- **【最终答案】**
  **$H(2, \; 2, \; 2)$**

---

### 第八章 演習問題 9（空間座標の図形・球面の方程式）

#### 演習問題 9-(1)
- **【原题重现与翻译】**
  - 原题：次の条件を満たす球面の方程式を求めよ。
    - `[1]` 2点 $A(1, 2, 4), \; B(-5, 8, -2)$ を直径の両端とする。
    - `[2]` 点 $(5, 1, 4)$ を通り、3つの座標平面に接する。
  - 中文：求满足下列条件的球面方程：
    - `[1]` 以两点 $A(1, 2, 4), \; B(-5, 8, -2)$ 为直径的两端点。
    - `[2]` 经过点 $(5, 1, 4)$，且与三个坐标平面都相切。
- **【考点定位】**
  - 球面的标准方程、直径端点确定球心与半径、球面与三坐标平面相切的几何特征。
- **【分步标准解答】**
  - **`[1]` の解答**：
    球面の中心 $C$ は線分 $AB$ の中点であるから：
    $$C\left(\frac{1 + (-5)}{2}, \; \frac{2 + 8}{2}, \; \frac{4 + (-2)}{2}\right) = C(-2, \; 5, \; 1)$$
    半径 $r$ は線分 $CA$ の長さであるから：
    $$r^2 = CA^2 = (1 - (-2))^2 + (2 - 5)^2 + (4 - 1)^2 = 3^2 + (-3)^2 + 3^2 = 9 + 9 + 9 = 27$$
    よって、求める球面の方程式は：
    $$(x + 2)^2 + (y - 5)^2 + (z - 1)^2 = 27$$
    > 💡 讲师批注：本题也可用球面直径式向量方程 $(\vec{p}-\vec{a})\cdot(\vec{p}-\vec{b}) = 0$ 直接展开：$(x-1)(x+5) + (y-2)(y-8) + (z-4)(z+2) = 0$，配方后同样得 $(x+2)^2+(y-5)^2+(z-1)^2 = 27$。

  - **`[2]` の解答**：
    球面が 3 つの座標平面（$xy$ 平面、$yz$ 平面、$zx$ 平面）のすべてに接し、かつ $x > 0, \; y > 0, \; z > 0$ の領域にある点 $(5, 1, 4)$ を通るから、球面全体が第 1 象限（$x \ge 0, \; y \ge 0, \; z \ge 0$）に含まれる。
    > 💡 讲师批注：**关键推理不可跳过！** 与三坐标平面相切的球面共有 8 个卦限方向，中心一般为 $(\pm r, \pm r, \pm r)$；正因为经过点 $(5,1,4)$（三个坐标全为正），才唯一确定球心在第一卦限 $(r, r, r)$（$r > 0$）。

    したがって、半径を $r$（$r > 0$）とすると、中心の座標は $(r, r, r)$ であり、球面の方程式は：
    $$(x - r)^2 + (y - r)^2 + (z - r)^2 = r^2$$
    この球面が点 $(5, 1, 4)$ を通るから、$x = 5, \; y = 1, \; z = 4$ を代入すると：
    $$(5 - r)^2 + (1 - r)^2 + (4 - r)^2 = r^2$$
    $$(25 - 10r + r^2) + (1 - 2r + r^2) + (16 - 8r + r^2) = r^2$$
    $$2r^2 - 20r + 42 = 0 \implies r^2 - 10r + 21 = 0 \implies (r - 3)(r - 7) = 0$$
    よって $r = 3, \; 7$（ともに $r > 0$ を満たす）。
    したがって、求める球面の方程式は次の 2 つである：
    $$(x - 3)^2 + (y - 3)^2 + (z - 3)^2 = 9, \qquad (x - 7)^2 + (y - 7)^2 + (z - 7)^2 = 49$$
    > 💡 讲师批注：两个解各有几何意义：一个较小（$r=3$，点 $(5,1,4)$ 在球面外上方偏外侧），一个较大（$r=7$，点 $(5,1,4)$ 在球面靠近原点一侧）。代入 $(5,1,4)$ 验算：$2^2+(-2)^2+1^2=9$；$(-2)^2+(-6)^2+(-3)^2=49$，均成立！
- **【最终答案】**
  - **`[1]` $(x + 2)^2 + (y - 5)^2 + (z - 1)^2 = 27$**
  - **`[2]` $(x - 3)^2 + (y - 3)^2 + (z - 3)^2 = 9, \quad (x - 7)^2 + (y - 7)^2 + (z - 7)^2 = 49$**

---

#### 演習問題 9-(2)
- **【原题重现与翻译】**
  - 原题：中心が点 $(1, -3, 2)$ で、原点を通る球面を $S$ とする。
    - `[1]` $S$ と $yz$ 平面の交わりは円になる。この円の中心と半径を求めよ。
    - `[2]` $S$ と平面 $z = k$ の交わりが半径 $\sqrt{5}$ の円になるという。$k$ の値を求めよ。
  - 中文：设中心为点 $(1, -3, 2)$ 且经过原点的球面为 $S$。
    - `[1]` $S$ 与 $yz$ 平面的交线是一个圆。求这个圆的圆心和半径。
    - `[2]` 已知 $S$ 与平面 $z = k$ 的交线是一个半径为 $\sqrt{5}$ 的圆。求 $k$ 的值。
- **【考点定位】**
  - 球面方程的建立、球面与坐标平面（或平行平面）截圆的圆心坐标与半径计算。
- **【图解辅助（SVG 矢量图）】**

<svg viewBox="0 0 420 220" width="420" height="220" xmlns="http://www.w3.org/2000/svg" style="background:#fafafa;border:1px solid #e0e0e0;border-radius:8px;display:block;margin:12px auto;">
  <!-- Sphere outer circle -->
  <circle cx="170" cy="110" r="82" fill="#eff6ff" stroke="#2563eb" stroke-width="1.8"/>
  <!-- Equator dashed ellipse -->
  <ellipse cx="170" cy="110" rx="82" ry="22" fill="none" stroke="#93c5fd" stroke-width="1.2" stroke-dasharray="4,3"/>

  <!-- Cutting plane z=k (horizontal slice above center) -->
  <!-- At y = 110 - 52 = 58, half-width = sqrt(82^2 - 52^2) = sqrt(6724 - 2704) = 63.4 -->
  <ellipse cx="170" cy="58" rx="63.4" ry="15" fill="#fef3c7" fill-opacity="0.7" stroke="#d97706" stroke-width="1.8"/>

  <!-- Sphere center C(1,-3,2) -->
  <circle cx="170" cy="110" r="3.5" fill="#1e293b"/>
  <text x="112" y="128" font-size="12" font-weight="bold" fill="#1e293b">C(1, -3, 2)</text>

  <!-- Slice circle center M -->
  <circle cx="170" cy="58" r="3.5" fill="#d97706"/>
  <text x="148" y="47" font-size="12" font-weight="bold" fill="#b45309">M(1, -3, k)</text>

  <!-- Right triangle C - M - edgePoint(233.4, 58) -->
  <line x1="170" y1="110" x2="170" y2="58" stroke="#dc2626" stroke-width="1.8"/>
  <line x1="170" y1="58" x2="233.4" y2="58" stroke="#d97706" stroke-width="1.8"/>
  <line x1="170" y1="110" x2="233.4" y2="58" stroke="#2563eb" stroke-width="1.8"/>
  <!-- Right angle mark -->
  <polyline points="170,68 180,68 180,58" fill="none" stroke="#dc2626" stroke-width="1.3"/>

  <!-- Labels on triangle -->
  <text x="174" y="88" font-size="12" fill="#dc2626" font-weight="bold">d = |k-2|</text>
  <text x="193" y="53" font-size="12" fill="#b45309" font-weight="bold">r' = √5</text>
  <text x="206" y="95" font-size="12" fill="#2563eb" font-weight="bold">R = √14</text>

  <!-- Formula box on the right -->
  <rect x="274" y="62" width="132" height="96" rx="6" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.2"/>
  <text x="284" y="84" font-size="12" font-weight="bold" fill="#1e293b">截圆勾股关系</text>
  <text x="284" y="106" font-size="12" fill="#334155">d² + r'² = R²</text>
  <text x="284" y="126" font-size="12" fill="#334155">(k-2)² + 5 = 14</text>
  <text x="284" y="146" font-size="12" fill="#dc2626" font-weight="bold">⇒ k = -1, 5</text>
</svg>

- **【分步标准解答】**
  まず、球面 $S$ の方程式を求める。中心 $C(1, -3, 2)$ から原点 $O(0, 0, 0)$ までの距離が半径 $R$ であるから：
  $$R^2 = OC^2 = 1^2 + (-3)^2 + 2^2 = 1 + 9 + 4 = 14$$
  よって、球面 $S$ の方程式は：
  $$(x - 1)^2 + (y + 3)^2 + (z - 2)^2 = 14 \qquad \cdots ①$$

  - **`[1]` の解答**：
    $yz$ 平面の方程式は $x = 0$ であるから、これを ① に代入すると：
    $$(0 - 1)^2 + (y + 3)^2 + (z - 2)^2 = 14$$
    $$(y + 3)^2 + (z - 2)^2 = 13 \qquad (\text{かつ } x = 0)$$
    したがって、交わりの円の中心は $(0, -3, 2)$、半径は $\sqrt{13}$ である。
    > 💡 讲师批注：**极易失分细节！** 空间中交圆的圆心坐标必须写成**三维坐标 $(0, -3, 2)$**，切勿因为令 $x=0$ 就漏掉 $x$ 坐标而误写成二维坐标 $(-3, 2)$！

  - **`[2]` の解答**：
    ① に $z = k$ を代入すると：
    $$(x - 1)^2 + (y + 3)^2 + (k - 2)^2 = 14$$
    $$(x - 1)^2 + (y + 3)^2 = 14 - (k - 2)^2$$
    この円（平面 $z = k$ 上）の半径が $\sqrt{5}$ であるから：
    $$14 - (k - 2)^2 = (\sqrt{5})^2 = 5$$
    $$(k - 2)^2 = 9 \implies k - 2 = \pm 3 \implies k = 2 \pm 3$$
    よって、$k = -1, \; 5$。
    > 💡 讲师批注：注意平面 $z=k$ 在球心 $z=2$ 上方和下方各截得一个半径为 $\sqrt{5}$ 的圆，因此必有两个对称解 $k=2+3=5$ 与 $k=2-3=-1$。
- **【最终答案】**
  - **`[1]` 中心 $(0, \; -3, \; 2)$、半径 $\sqrt{13}$**
  - **`[2]` $k = -1, \; 5$**

---

#### 演習問題 9-(3)
- **【原题重现与翻译】**
  - 原题：空間において、点 $A(0, 6, 0)$ を中心とする半径 $3$ の球面上を動く点 $Q$ を考える。更に、原点を $O$、線分 $OQ$ の中点を $P$ とし、点 $A, Q, P$ の位置ベクトルをそれぞれ $\vec{a}, \vec{q}, \vec{p}$ とする。このとき、点 $P$ が満たすベクトル方程式を求めよ。また、点 $P(x, y, z)$ が描く方程式を $x, y, z$ を用いて表せ。
  - 中文：在空间中，考虑在以点 $A(0, 6, 0)$ 为中心、半径为 $3$ 的球面上运动的动点 $Q$。此外，设原点为 $O$，线段 $OQ$ 的中点为 $P$，点 $A, Q, P$ 的位置向量分别为 $\vec{a}, \vec{q}, \vec{p}$。求点 $P$ 满足的向量方程，并用 $x, y, z$ 表示点 $P(x, y, z)$ 所描绘图形的方程。
- **【考点定位】**
  - 球面的向量方程、空间轨迹（联动点/位似缩放）的向量求法与坐标转化。
- **【图解辅助（SVG 矢量图）】**

<svg viewBox="0 0 430 220" width="430" height="220" xmlns="http://www.w3.org/2000/svg" style="background:#fafafa;border:1px solid #e0e0e0;border-radius:8px;display:block;margin:12px auto;">
  <!-- Origin O -->
  <circle cx="55" cy="115" r="4" fill="#1e293b"/>
  <text x="38" y="132" font-size="13" font-weight="bold" fill="#1e293b">O</text>

  <!-- Large sphere centered at A(295,115), radius 75 (represents center (0,6,0), R=3) -->
  <circle cx="295" cy="115" r="75" fill="#eff6ff" fill-opacity="0.5" stroke="#2563eb" stroke-width="1.8"/>
  <circle cx="295" cy="115" r="3.5" fill="#2563eb"/>
  <text x="298" y="132" font-size="12" font-weight="bold" fill="#2563eb">A(0, 6, 0)</text>

  <!-- Small locus sphere centered at M(175,115), radius 37.5 (represents (0,3,0), R=3/2) -->
  <circle cx="175" cy="115" r="37.5" fill="#fef3c7" fill-opacity="0.6" stroke="#d97706" stroke-width="1.8"/>
  <circle cx="175" cy="115" r="3.5" fill="#d97706"/>
  <text x="160" y="133" font-size="12" font-weight="bold" fill="#b45309">(0, 3, 0)</text>

  <!-- Axis O - A -->
  <line x1="55" y1="115" x2="385" y2="115" stroke="#94a3b8" stroke-width="1.2" stroke-dasharray="4,3"/>

  <!-- Sample point Q on large sphere: angle -45deg from A => (295+53, 115-53) = (348, 62) -->
  <!-- Midpoint P of OQ: ((55+348)/2, (115+62)/2) = (201.5, 88.5) -->
  <line x1="55" y1="115" x2="348" y2="62" stroke="#dc2626" stroke-width="1.6"/>
  <line x1="295" y1="115" x2="348" y2="62" stroke="#2563eb" stroke-width="1.3" stroke-dasharray="3,3"/>
  <line x1="175" y1="115" x2="201.5" y2="88.5" stroke="#d97706" stroke-width="1.3" stroke-dasharray="3,3"/>

  <circle cx="348" cy="62" r="4" fill="#2563eb"/>
  <text x="355" y="59" font-size="13" font-weight="bold" fill="#2563eb">Q</text>
  <circle cx="201.5" cy="88.5" r="4" fill="#dc2626"/>
  <text x="196" y="77" font-size="13" font-weight="bold" fill="#dc2626">P (OQ中点)</text>

  <text x="20" y="205" font-size="12" fill="#334155">以原点 O 为中心缩小至 1/2：球心 (0,6,0) → (0,3,0)，半径 3 → 3/2</text>
</svg>

- **【分步标准解答】**
  点 $Q(\vec{q})$ は点 $A(\vec{a})$ を中心とする半径 $3$ の球面上にあるから、$\vec{q}$ が満たすベクトル方程式は：
  $$|\vec{q} - \vec{a}| = 3 \qquad \cdots ①$$
  また、点 $P(\vec{p})$ は線分 $OQ$ の中点であるから：
  $$\vec{p} = \frac{1}{2}\vec{q} \iff \vec{q} = 2\vec{p} \qquad \cdots ②$$
  > 💡 讲师批注：求从动点 $P$ 的轨迹方程（联动轨迹法）：用**所求点 $\vec{p}$ 表示主动点 $\vec{q}$**（即 $\vec{q} = 2\vec{p}$），再代入主动点满足的方程 ① 消去 $\vec{q}$！

  ② を ① に代入すると：
  $$|2\vec{p} - \vec{a}| = 3$$
  両辺を $2$ で割って整理すると、点 $P$ が満たす球面のベクトル方程式は：
  $$\left|\vec{p} - \frac{1}{2}\vec{a}\right| = \frac{3}{2}$$
  > 💡 讲师批注：把 $|2\vec{p}-\vec{a}|=3$ 整理为标准形式 $\left|\vec{p}-\frac{1}{2}\vec{a}\right| = \frac{3}{2}$ 后，几何意义一目了然：这是一个以 $\frac{1}{2}\vec{a}$ 为球心、半径为 $\frac{3}{2}$ 的球面。

  次に、これを座標で表す。$\vec{p} = (x, y, z), \; \vec{a} = (0, 6, 0)$ であるから $\dfrac{1}{2}\vec{a} = (0, 3, 0)$。
  よって、$\vec{p} - \dfrac{1}{2}\vec{a} = (x, \; y - 3, \; z)$ となり、両辺を 2 乗すると：
  $$x^2 + (y - 3)^2 + z^2 = \left(\frac{3}{2}\right)^2 = \frac{9}{4}$$
- **【最终答案】**
  - **ベクトル方程式：$\left|\vec{p} - \dfrac{1}{2}\vec{a}\right| = \dfrac{3}{2}$**（または $|2\vec{p} - \vec{a}| = 3$）
  - **座標の方程式：$x^2 + (y - 3)^2 + z^2 = \dfrac{9}{4}$**

---

### 第九章 演習問題 1（複素数の計算）

#### 演習問題 1-(1)
- **【原题重现与翻译】**
  - 原题：次の計算をせよ。
    - `[1]` $(4 + 5i) - (3 - 2i)$
    - `[2]` $(2 + i)^2$
    - `[3]` $(2 + \sqrt{-5})(3 - \sqrt{-5})$
    - `[4]` $\dfrac{2 + 5i}{3 - 2i}$
    - `[5]` $\dfrac{3 + 2i}{2 + i} - \dfrac{i}{1 - 2i}$
  - 中文：计算下列各式。
- **【考点定位】**
  - 复数的加减乘除四则运算、虚数单位性质 $i^2 = -1$、负数的平方根 $\sqrt{-a} = \sqrt{a}i$、分母实数化（共轭复数乘法）。
- **【分步标准解答】**
  - **`[1]` の解答**：
    $$(4 + 5i) - (3 - 2i) = (4 - 3) + (5 + 2)i = 1 + 7i$$
    > 💡 讲师批注：去括号时注意 $-(-2i) = +2i$，实部与实部相加减、虚部与虚部相加减。

  - **`[2]` の解答**：
    $$(2 + i)^2 = 2^2 + 2\cdot 2\cdot i + i^2 = 4 + 4i + (-1) = 3 + 4i$$
    > 💡 讲师批注：切记 $i^2 = -1$，因此 $(a+bi)^2 = (a^2 - b^2) + 2abi$。

  - **`[3]` の解答**：
    まず負の数の平方根を $\sqrt{-5} = \sqrt{5}\,i$ と書き換える：
    $$(2 + \sqrt{-5})(3 - \sqrt{-5}) = (2 + \sqrt{5}\,i)(3 - \sqrt{5}\,i)$$
    $$= 6 - 2\sqrt{5}\,i + 3\sqrt{5}\,i - (\sqrt{5}\,i)^2$$
    $$= 6 + \sqrt{5}\,i - 5i^2 = 6 + \sqrt{5}\,i - 5(-1) = 11 + \sqrt{5}\,i$$
    > 💡 讲师批注：**铁律提醒！** 遇到 $\sqrt{-5}$ 务必第一时间化为 $\sqrt{5}i$，于是 $-(\sqrt{5}i)^2 = -(-5) = +5$；绝不可直接写成 $-\sqrt{(-5)(-5)} = -5$！

  - **`[4]` の解答**：
    分母 $3 - 2i$ と共役な複素数 $3 + 2i$ を分母・分子に掛ける（分母の実数化）：
    $$\frac{2 + 5i}{3 - 2i} = \frac{(2 + 5i)(3 + 2i)}{(3 - 2i)(3 + 2i)} = \frac{6 + 4i + 15i + 10i^2}{3^2 - (2i)^2}$$
    $$= \frac{6 + 19i - 10}{9 + 4} = \frac{-4 + 19i}{13} = -\frac{4}{13} + \frac{19}{13}i$$
    > 💡 讲师批注：分母 $(a-bi)(a+bi) = a^2 + b^2$ 必为正实数（这里 $3^2 + 2^2 = 13$）。最终结果按日本教材规范拆成 $a + bi$ 的标准形式 $-\frac{4}{13} + \frac{19}{13}i$。

  - **`[5]` の解答**：
    それぞれの分数の分母を実数化する：
    - 第 1 項：
      $$\frac{3 + 2i}{2 + i} = \frac{(3 + 2i)(2 - i)}{(2 + i)(2 - i)} = \frac{6 - 3i + 4i - 2i^2}{2^2 + 1^2} = \frac{6 + i + 2}{5} = \frac{8 + i}{5}$$
    - 第 2 項：
      $$\frac{i}{1 - 2i} = \frac{i(1 + 2i)}{(1 - 2i)(1 + 2i)} = \frac{i + 2i^2}{1^2 + 2^2} = \frac{-2 + i}{5}$$
    よって、両者の差を計算すると：
    $$\frac{3 + 2i}{2 + i} - \frac{i}{1 - 2i} = \frac{8 + i}{5} - \frac{-2 + i}{5} = \frac{(8 + i) - (-2 + i)}{5} = \frac{10}{5} = 2$$
    > 💡 讲师批注：观察两个分母的模长平方都是 $2^2+1^2 = 1^2+2^2 = 5$，分别实数化后天然同分母，比先通分再实数化省力得多！虚部 $\frac{i}{5} - \frac{i}{5}$ 恰好完全抵消，结果是纯实数 $2$。
- **【最终答案】**
  - **`[1]` $1 + 7i$**
  - **`[2]` $3 + 4i$**
  - **`[3]` $11 + \sqrt{5}\,i$**
  - **`[4]` $-\dfrac{4}{13} + \dfrac{19}{13}i$**
  - **`[5]` $2$**
