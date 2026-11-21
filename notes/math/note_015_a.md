# 《EJU 教材全解与备课讲义》数学 015-A（P211–P225 前半）

> **对应源文件**：`work_math/ocr_md/ocr_015_p211-225.md`（平面向量之内积综合应用、位置向量与图形、向量方程；空间坐标与空间向量开篇；教材印制页码 P210–P224）
> **视觉核对参考图**：`work_math/ref_imgs/page_0211.jpg`, `page_0212.jpg`, `page_0215.jpg`–`page_0221.jpg`, `page_0225.jpg`
> **分册说明**：本切片含 19 道综合演习题与大量几何证明，为保证推导绝对详尽不跳步，拆分为 `note_015_a.md`（知识点全景、词汇表及演習問題 3-(3)~(8)、4-(1)~(4)）与 `note_015_b.md`（演習問題 4-(5)~(8)、5-(1)~(4)、6-(1)）。

---

## 一、国内高中基础知识点唤醒与 EJU 考纲差异对比

本切片对应日本高中数学 **数学 C（ベクトル）**（旧课纲属数学 B）的绝对高频压轴板块，贯穿**平面向量的内积应用、位置向量与三角形四心、向量方程与终点存在范围**，并正式开启**空间坐标与空间向量**。

### 1.1 位置向量与图形（位置ベクトル、ベクトルと図形）

固定平面上一点 $O$，任意点 $P$ 的位置由 $\vec{p} = \overrightarrow{OP}$ 唯一确定，称 $\vec{p}$ 为点 $P$ 关于 $O$ 的**位置向量（位置ベクトル）**，记作 $P(\vec{p})$。
- **向量的分解（差公式 / 始点変換）**：$\overrightarrow{AB} = \overrightarrow{OB} - \overrightarrow{OA} = \vec{b} - \vec{a}$（**终点减起点**）。
- **内分点与外分点公式**：线段 $AB$ 按 $m:n$（$m>0, n>0$）内分的点 $P(\vec{p})$、外分的点 $Q(\vec{q})$（$m \neq n$）及中点 $M(\vec{m})$：
  $$\vec{p} = \frac{n\vec{a} + m\vec{b}}{m + n}, \qquad \vec{q} = \frac{-n\vec{a} + m\vec{b}}{m - n}, \qquad \vec{m} = \frac{\vec{a} + \vec{b}}{2}$$
- **三角形重心公式**：$\triangle ABC$ 重心 $G(\vec{g})$ 满足
  $$\vec{g} = \frac{\vec{a} + \vec{b} + \vec{c}}{3}$$
- **共线条件（共線条件）**：
  - 向量倍数法：点 $P$ 在直线 $AB$ 上 $\iff \overrightarrow{AP} = k\overrightarrow{AB}$（$k \in \mathbb{R}$）。
  - **系数和为 1 定理（EJU 最高频）**：点 $P$ 在直线 $AB$ 上 $\iff \vec{p} = s\vec{a} + t\vec{b}$ 且 $s + t = 1$（或 $\vec{p} = (1-t)\vec{a} + t\vec{b}$）。
- **共点条件（共点条件）**：三条直线 $l, m, n$ 交于一点 $\iff$ 直线 $l, m$ 的交点与 $m, n$ 的交点位置向量相等。

### 1.2 向量方程与终点存在范围（ベクトル方程式・終点の存在範囲）

设动点 $P(\vec{p})$，$s, t \in \mathbb{R}$：
1. **直线的向量方程**：
   - 过定点 $A(\vec{a})$、平行于非零方向向量 $\vec{d}$：$\vec{p} = \vec{a} + t\vec{d}$。
   - 过两定点 $A(\vec{a}), B(\vec{b})$：$\vec{p} = (1-t)\vec{a} + t\vec{b}$（或 $\vec{p} = s\vec{a} + t\vec{b},\; s+t=1$）。
   - 过定点 $A(\vec{a})$、垂直于非零法向量 $\vec{n}$：$\vec{n} \cdot (\vec{p} - \vec{a}) = 0$。
     - 特别地，直线 $ax + by + c = 0$ 的一个**法向量**为 $\vec{n} = (a, b)$。
2. **向量终点的存在范围（$\overrightarrow{OP} = s\vec{a} + t\vec{b}$，$\vec{a} \neq \vec{0}, \vec{b} \neq \vec{0}, \vec{a} \not\parallel \vec{b}$）**：
   - **直线 $AB$**：$s + t = 1$；**线段 $AB$**：$s + t = 1,\; s \ge 0,\; t \ge 0$。
   - **$\triangle OAB$ 的周界及内部**：$0 \le s + t \le 1,\; s \ge 0,\; t \ge 0$。
   - **平行四边形 $OACB$ 的周界及内部**：$0 \le s \le 1,\; 0 \le t \le 1$（$\overrightarrow{OC} = \overrightarrow{OA} + \overrightarrow{OB}$）。
   > ⚠️ **教材勘误提示**：原教材第 217 页（`page_0218.jpg`）[5.2] 条件误印为 $\vec{a} \parallel \vec{b}$，正确条件应为 **$\vec{a} \not\parallel \vec{b}$**（两向量不平行，线性无关）。

<svg viewBox="0 0 640 190" width="100%" style="max-width:640px;display:block;margin:12px auto;" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <marker id="arr15a" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#1e293b"/>
    </marker>
    <marker id="arr15b" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#2563eb"/>
    </marker>
  </defs>
  <!-- Panel 1: 线段 AB -->
  <rect x="6" y="6" width="200" height="178" rx="8" fill="#f8fafc" stroke="#cbd5e1"/>
  <text x="106" y="25" font-size="12" font-weight="bold" text-anchor="middle" fill="#0f172a">① 线段 AB (s+t=1, s≥0, t≥0)</text>
  <line x1="40" y1="145" x2="170" y2="145" stroke="#1e293b" stroke-width="1.5" marker-end="url(#arr15a)"/>
  <line x1="40" y1="145" x2="80" y2="65" stroke="#1e293b" stroke-width="1.5" marker-end="url(#arr15a)"/>
  <line x1="80" y1="65" x2="170" y2="145" stroke="#dc2626" stroke-width="3.5"/>
  <line x1="40" y1="145" x2="120" y2="100" stroke="#2563eb" stroke-width="1.5" stroke-dasharray="4,3" marker-end="url(#arr15b)"/>
  <circle cx="120" cy="100" r="3.5" fill="#2563eb"/>
  <text x="28" y="155" font-size="12" fill="#0f172a">O</text>
  <text x="175" y="155" font-size="12" fill="#0f172a">A</text>
  <text x="72" y="57" font-size="12" fill="#0f172a">B</text>
  <text x="128" y="96" font-size="12" font-weight="bold" fill="#2563eb">P</text>
  <text x="106" y="172" font-size="11" text-anchor="middle" fill="#dc2626">红粗线：P 的存在范围</text>

  <!-- Panel 2: 三角形 OAB -->
  <rect x="220" y="6" width="200" height="178" rx="8" fill="#f8fafc" stroke="#cbd5e1"/>
  <text x="320" y="25" font-size="12" font-weight="bold" text-anchor="middle" fill="#0f172a">② △OAB 内部 (0≤s+t≤1)</text>
  <polygon points="254,145 384,145 294,65" fill="#fecaca" fill-opacity="0.65" stroke="#dc2626" stroke-width="2"/>
  <line x1="254" y1="145" x2="384" y2="145" stroke="#1e293b" stroke-width="1.5" marker-end="url(#arr15a)"/>
  <line x1="254" y1="145" x2="294" y2="65" stroke="#1e293b" stroke-width="1.5" marker-end="url(#arr15a)"/>
  <circle cx="308" cy="116" r="3.5" fill="#2563eb"/>
  <text x="242" y="155" font-size="12" fill="#0f172a">O</text>
  <text x="389" y="155" font-size="12" fill="#0f172a">A</text>
  <text x="286" y="57" font-size="12" fill="#0f172a">B</text>
  <text x="315" y="120" font-size="12" font-weight="bold" fill="#2563eb">P</text>
  <text x="320" y="172" font-size="11" text-anchor="middle" fill="#dc2626">s≥0, t≥0 且 0≤s+t≤1</text>

  <!-- Panel 3: 平行四边形 OACB -->
  <rect x="434" y="6" width="200" height="178" rx="8" fill="#f8fafc" stroke="#cbd5e1"/>
  <text x="534" y="25" font-size="12" font-weight="bold" text-anchor="middle" fill="#0f172a">③ 平行四边形 (0≤s≤1, 0≤t≤1)</text>
  <polygon points="460,145 565,145 605,65 500,65" fill="#bfdbfe" fill-opacity="0.65" stroke="#2563eb" stroke-width="2"/>
  <line x1="460" y1="145" x2="565" y2="145" stroke="#1e293b" stroke-width="1.5" marker-end="url(#arr15a)"/>
  <line x1="460" y1="145" x2="500" y2="65" stroke="#1e293b" stroke-width="1.5" marker-end="url(#arr15a)"/>
  <circle cx="538" cy="105" r="3.5" fill="#dc2626"/>
  <text x="448" y="155" font-size="12" fill="#0f172a">O</text>
  <text x="570" y="155" font-size="12" fill="#0f172a">A</text>
  <text x="492" y="57" font-size="12" fill="#0f172a">B</text>
  <text x="610" y="68" font-size="12" fill="#0f172a">C</text>
  <text x="546" y="109" font-size="12" font-weight="bold" fill="#dc2626">P</text>
  <text x="534" y="172" font-size="11" text-anchor="middle" fill="#2563eb">OC = OA + OB</text>
</svg>

3. **圆的向量方程**：
   - 圆心 $C(\vec{c})$、半径 $r$：$|\vec{p} - \vec{c}| = r$ 或 $(\vec{p} - \vec{c}) \cdot (\vec{p} - \vec{c}) = r^2$。
   - 以线段 $AB$ 为直径的圆：$(\vec{p} - \vec{a}) \cdot (\vec{p} - \vec{b}) = 0$。
   > ⚠️ **教材勘误提示**：原教材第 218 页（`page_0219.jpg`）[5.3] ② 将「直径」误印为「直線」（線分 $AB$ を**直線**とする円），正确表述应为「線分 $AB$ を**直径**とする円」。

### 1.3 空间坐标与空间向量（空間の座標・空間ベクトル）

- **两点间距离**：$A(x_1, y_1, z_1),\; B(x_2, y_2, z_2)$，
  $$AB = \sqrt{(x_2-x_1)^2 + (y_2-y_1)^2 + (z_2-z_1)^2}$$
- **空间向量基本定理（空间向量的分解）**：若不共面的四点 $O, A, B, C$ 确定 $\vec{a}=\overrightarrow{OA},\; \vec{b}=\overrightarrow{OB},\; \vec{c}=\overrightarrow{OC}$（线性无关 / 1 次独立），则空间任意向量 $\vec{p}$ 可**唯一**表示为
  $$\vec{p} = s\vec{a} + t\vec{b} + u\vec{c} \qquad (s, t, u \in \mathbb{R})$$
  特别地，$s\vec{a} + t\vec{b} + u\vec{c} = \vec{0} \iff s = t = u = 0$。
- **基本单位向量与分量表示**：$\vec{e}_1 = (1,0,0),\; \vec{e}_2 = (0,1,0),\; \vec{e}_3 = (0,0,1)$；任意向量 $\vec{a} = a_1\vec{e}_1 + a_2\vec{e}_2 + a_3\vec{e}_3 = (a_1, a_2, a_3)$，其模长为 $|\vec{a}| = \sqrt{a_1^2 + a_2^2 + a_3^2}$。

### 1.4 国内高中 vs. 日本 EJU 考纲差异对比

| 对比维度 | 国内高中习惯 | 日本 EJU 习惯 | 备课/应试提醒 |
| :--- | :--- | :--- | :--- |
| **向量记号** | 印刷体常写作粗体 $\boldsymbol{a}$，手写 $\vec{a}$ | 印刷与手写**统一带箭头** $\vec{a}, \overrightarrow{OA}$ | EJU 试卷中全部使用带箭头记号，零向量记作 $\vec{0}$ |
| **三角形四心向量** | 偶尔作为选填技巧出现 | **绝对压轴常客！** 垂心、内心、外心、欧拉线常以完整大题形式考查 | 必须熟练掌握通过内积（垂心、外心）与角平分线比（内心）推导位置向量 |
| **终点存在范围** | 较少系统以 $s, t$ 不等式出大题 | **日本高考/EJU 标志性题型**（如 $2s+3t=1$ 换元缩放） | 熟记三大基本模型，并掌握「变量代换还原为 $s'+t'=1$」的变形技巧 |
| **面积公式** | 常用行列式或 $\frac{1}{2}|x_1y_2-x_2y_1|$ | 教材从 $\frac{1}{2}\sqrt{|\vec{a}|^2|\vec{b}|^2 - (\vec{a}\cdot\vec{b})^2}$ 推导到 $\frac{1}{2}|a_1b_2-a_2b_1|$ | EJU 不考叉积（外積），但两者均为必背秒杀公式 |
| **基本单位向量** | 常用 $\vec{i}, \vec{j}, \vec{k}$ | 统一用 **$\vec{e}_1, \vec{e}_2, \vec{e}_3$** 称作「基本ベクトル」 | 注意符号差异，本质完全一致 |

---

## 二、日文核心词汇与公式假名注音

### 2.1 本切片日文核心词汇

- ベクトル（べくとる / bekutoru） — 向量、矢量
- 内積（ないせき / naiseki） — 内积（点积、数量积）
- 大きさ（おおきさ / ookisa） — 模、大小（向量的长度）
- 位置ベクトル（いちべくとる / ichi bekutoru） — 位置向量
- 分点（ぶんてん / bunten） — 分点（内分点与外分点的统称）
- 共線条件（きょうせんじょうけん / kyousen jouken） — 共线条件
- 共点条件（きょうてんじょうけん / kyouten jouken） — 共点条件
- 垂線の足（すいせんのあし / suisen no ashi） — 垂足
- オイラー線（おいらーせん / oiraa sen） — 欧拉线
- ベクトル方程式（べくとるほうていしき / bekutoru houteishiki） — 向量方程
- 方向ベクトル（ほうこうべくとる / houkou bekutoru） — 方向向量
- 法線ベクトル（ほうせんべくとる / housen bekutoru） — 法向量
- 終点の存在範囲（しゅうてんのそんざいはんい / shuuten no sonzai han'i） — 终点的存在范围
- 座標軸（ざひょうじく / zahyoujiku） — 坐标轴
- 直交座標軸（ちょっこうざひょうじく / chokkou zahyoujiku） — 直角坐标轴（正交坐标轴）
- 座標空間（ざひょうくうかん / zahyou kuukan） — 坐标空间
- 直方体（ちょくほうたい / chokuhoutai） — 长方体
- 空間ベクトル（くうかんべくとる / kuukan bekutoru） — 空间向量
- 逆ベクトル（ぎゃくべくとる / gyaku bekutoru） — 相反向量
- 零ベクトル（ぜろべくとる / zero bekutoru） — 零向量（亦读 れいべくとる）
- 実数倍（じっすうばい / jissuubai） — 数乘（向量的实数倍）
- 1次独立（いちじどくりつ / ichiji dokuritsu） — 线性无关（一次独立）
- 成分（せいぶん / seibun） — 分量、坐标分量
- 成分表示（せいぶんひょうじ / seibun hyouji） — 分量表示
- 単位ベクトル（たんいべくとる / tan'i bekutoru） — 单位向量
- 基本ベクトル（きほんべくとる / kihon bekutoru） — 基本单位向量

### 2.2 核心公式的日本课堂口语读法

1. **向量模与内积** $|\vec{a}|, \; \vec{a} \cdot \vec{b}$
   - 课堂读法：**ベクトル エー の おおきさ**（模）；**ベクトル エー と ベクトル ビー の ないせき**（或简读 **エー ドット ビー**）。
2. **向量垂直条件** $\vec{a} \perp \vec{b} \iff \vec{a} \cdot \vec{b} = 0$
   - 课堂读法：**ベクトル エー すいちょく ベクトル ビー どうち エー ドット ビー イコール ゼロ**。
3. **三角形面积向量公式** $S = \dfrac{1}{2}\sqrt{|\vec{a}|^2|\vec{b}|^2 - (\vec{a}\cdot\vec{b})^2}$
   - 课堂读法：**エス イコール にぶんのいち ルート、ベクトルエーのおおきさのにじょう かける ベクトルビーのおおきさのにじょう ひく、かっこ エー ドット ビー かっことじ の にじょう**。
4. **直线的法向量方程** $\vec{n} \cdot (\vec{p} - \vec{a}) = 0$
   - 课堂读法：**ベクトル エヌ ドット かっこ ベクトル ピー ひく ベクトル エー かっことじ イコール ゼロ**。
5. **空间向量唯一分解** $\vec{p} = s\vec{a} + t\vec{b} + u\vec{c}$
   - 课堂读法：**ベクトル ピー イコール エス ベクトルエー たす ティー ベクトルビー たす ユー ベクトルシー**。

---

## 三、逐题深度解析（不可跳步）

---

### 演習問題 3（ベクトルの内積とその応用）

#### 演習問題 3-(3)
- **【原题重现与翻译】**
  - 原题：等式 $|\vec{a} + \vec{b}|^2 + |\vec{a} - \vec{b}|^2 = 2\left(|\vec{a}|^2 + |\vec{b}|^2\right)$ を証明せよ。
  - 中文：证明等式 $|\vec{a} + \vec{b}|^2 + |\vec{a} - \vec{b}|^2 = 2\left(|\vec{a}|^2 + |\vec{b}|^2\right)$。
- **【考点定位】**
  - 向量模的平方与内积展开公式 $|\vec{a} \pm \vec{b}|^2 = |\vec{a}|^2 \pm 2\vec{a}\cdot\vec{b} + |\vec{b}|^2$（几何意义即平行四边形对角线定理 / 中线定理）。
- **【分步标准解答】**
  $$\text{左辺} = |\vec{a} + \vec{b}|^2 + |\vec{a} - \vec{b}|^2$$
  $$= \left(|\vec{a}|^2 + 2\vec{a}\cdot\vec{b} + |\vec{b}|^2\right) + \left(|\vec{a}|^2 - 2\vec{a}\cdot\vec{b} + |\vec{b}|^2\right)$$
  > 💡 讲师批注：利用 $|\vec{x}|^2 = \vec{x}\cdot\vec{x}$ 及内积的分配律与交换律展开。交叉项 $+2\vec{a}\cdot\vec{b}$ 与 $-2\vec{a}\cdot\vec{b}$ 恰好抵消。

  $$= 2|\vec{a}|^2 + 2|\vec{b}|^2 = 2\left(|\vec{a}|^2 + |\vec{b}|^2\right) = \text{右辺}$$
  よって、等式は成り立つ。（証明終）
  > 💡 讲师批注：该恒等式在几何上说明：**平行四边形两条对角线的平方和等于四条边的平方和**。在 EJU 中经常逆用它来求 $|\vec{a}+\vec{b}|$ 或 $|\vec{a}-\vec{b}|$。
- **【最终答案】**
  **証明済（左辺を展開すると内積の項 $2\vec{a}\cdot\vec{b}$ が打ち消し合い、右辺 $2(|\vec{a}|^2 + |\vec{b}|^2)$ に一致する）**

---

#### 演習問題 3-(4)
- **【原题重现与翻译】**
  - 原题：$|\vec{a}| = 2,\; |\vec{b}| = 1$ で、$\vec{a} - \vec{b}$ と $2\vec{a} + 5\vec{b}$ が垂直であるとき、$\vec{a}$ と $\vec{b}$ のなす角 $\theta$ を求めよ。
  - 中文：已知 $|\vec{a}| = 2,\; |\vec{b}| = 1$，且 $\vec{a} - \vec{b}$ 与 $2\vec{a} + 5\vec{b}$ 垂直，求 $\vec{a}$ 与 $\vec{b}$ 的夹角 $\theta$。
- **【考点定位】**
  - 向量垂直充要条件（内积为 $0$）+ 向量夹角余弦公式 $\cos\theta = \dfrac{\vec{a}\cdot\vec{b}}{|\vec{a}||\vec{b}|}$。
- **【分步标准解答】**
  $(\vec{a} - \vec{b}) \perp (2\vec{a} + 5\vec{b})$ より、内積は $0$ であるから
  $$(\vec{a} - \vec{b}) \cdot (2\vec{a} + 5\vec{b}) = 0$$
  左辺を展開すると
  $$2|\vec{a}|^2 + 5\vec{a}\cdot\vec{b} - 2\vec{b}\cdot\vec{a} - 5|\vec{b}|^2 = 0$$
  $$2|\vec{a}|^2 + 3\vec{a}\cdot\vec{b} - 5|\vec{b}|^2 = 0$$
  > 💡 讲师批注：内积满足交换律 $\vec{b}\cdot\vec{a} = \vec{a}\cdot\vec{b}$，合并同类项得 $+3\vec{a}\cdot\vec{b}$。

  $|\vec{a}| = 2,\; |\vec{b}| = 1$ を代入すると
  $$2 \cdot 2^2 + 3\vec{a}\cdot\vec{b} - 5 \cdot 1^2 = 0$$
  $$8 + 3\vec{a}\cdot\vec{b} - 5 = 0 \implies 3\vec{a}\cdot\vec{b} = -3 \implies \vec{a}\cdot\vec{b} = -1$$
  したがって、なす角 $\theta$ について
  $$\cos\theta = \frac{\vec{a}\cdot\vec{b}}{|\vec{a}||\vec{b}|} = \frac{-1}{2 \cdot 1} = -\frac{1}{2}$$
  $0^\circ \le \theta \le 180^\circ$ であるから、$\theta = 120^\circ$（弧度法では $\dfrac{2}{3}\pi$）。
  > 💡 讲师批注：写答案前务必注明向量夹角的定义范围 $0^\circ \le \theta \le 180^\circ$（或 $0 \le \theta \le \pi$），这是日本记述式考试的采分点。
- **【最终答案】**
  **$\theta = 120^\circ$**（または $\dfrac{2}{3}\pi$）

---

#### 演習問題 3-(5)
- **【原题重现与翻译】**
  - 原题：ベクトル $\vec{a}, \vec{b}$ について $|\vec{a}| = \sqrt{3},\; |\vec{b}| = 2,\; |\vec{a} - \vec{b}| = \sqrt{5}$ とするとき
    - [1] 内積 $\vec{a}\cdot\vec{b}$ の値を求めよ。
    - [2] ベクトル $2\vec{a} - 3\vec{b}$ の大きさを求めよ。
    - [3] ベクトル $\vec{a} + t\vec{b}$ の大きさが最小となるように実数 $t$ の値を定め、その時の最小値を求めよ。
  - 中文：已知向量 $\vec{a}, \vec{b}$ 满足 $|\vec{a}| = \sqrt{3},\; |\vec{b}| = 2,\; |\vec{a} - \vec{b}| = \sqrt{5}$：
    - [1] 求内积 $\vec{a}\cdot\vec{b}$ 的值；
    - [2] 求向量 $2\vec{a} - 3\vec{b}$ 的模；
    - [3] 确定使向量 $\vec{a} + t\vec{b}$ 的模取得最小值的实数 $t$，并求此时的最小值。
- **【考点定位】**
  - 「见模平方」核心技巧 + 二次函数配方求向量模的最小值。
- **【分步标准解答】**
  - **[1] $\vec{a}\cdot\vec{b}$ の値**：
    $|\vec{a} - \vec{b}| = \sqrt{5}$ の両辺を 2 乗すると
    $$|\vec{a} - \vec{b}|^2 = 5$$
    $$|\vec{a}|^2 - 2\vec{a}\cdot\vec{b} + |\vec{b}|^2 = 5$$
    $|\vec{a}| = \sqrt{3},\; |\vec{b}| = 2$ を代入して
    $$(\sqrt{3})^2 - 2\vec{a}\cdot\vec{b} + 2^2 = 5 \implies 3 - 2\vec{a}\cdot\vec{b} + 4 = 5$$
    $$2\vec{a}\cdot\vec{b} = 2 \implies \vec{a}\cdot\vec{b} = 1$$
    > 💡 讲师批注：处理向量模长条件的铁律就是**先平方转化成内积**。

  - **[2] $|2\vec{a} - 3\vec{b}|$ の値**：
    $$|2\vec{a} - 3\vec{b}|^2 = 4|\vec{a}|^2 - 12\vec{a}\cdot\vec{b} + 9|\vec{b}|^2$$
    $$= 4(\sqrt{3})^2 - 12(1) + 9(2)^2 = 12 - 12 + 36 = 36$$
    $|2\vec{a} - 3\vec{b}| \ge 0$ より
    $$|2\vec{a} - 3\vec{b}| = \sqrt{36} = 6$$
    > 💡 讲师批注：开方前务必写上 $|2\vec{a} - 3\vec{b}| \ge 0$，避免遗漏非负性说明。

  - **[3] $|\vec{a} + t\vec{b}|$ の最小値**：
    $|\vec{a} + t\vec{b}| \ge 0$ より、$|\vec{a} + t\vec{b}|$ が最小となるのは $|\vec{a} + t\vec{b}|^2$ が最小となるときである。
    $$|\vec{a} + t\vec{b}|^2 = |\vec{a}|^2 + 2t(\vec{a}\cdot\vec{b}) + t^2|\vec{b}|^2$$
    $$= 4t^2 + 2t + 3$$
    $$= 4\left(t^2 + \frac{1}{2}t\right) + 3 = 4\left(t + \frac{1}{4}\right)^2 - 4\cdot\frac{1}{16} + 3$$
    $$= 4\left(t + \frac{1}{4}\right)^2 + \frac{11}{4}$$
    > 💡 讲师批注：转化为关于实数 $t$ 的一元二次函数后，用平方完成（配方）即可瞬间锁定最小值。几何意义上，此时 $(\vec{a} + t\vec{b}) \perp \vec{b}$，可用 $(\vec{a}+t\vec{b})\cdot\vec{b} = 1 + 4t = 0 \implies t = -\frac{1}{4}$ 快速验算！

    よって、$t = -\dfrac{1}{4}$ のとき $|\vec{a} + t\vec{b}|^2$ は最小値 $\dfrac{11}{4}$ をとる。
    したがって、$|\vec{a} + t\vec{b}|$ の最小値は
    $$\sqrt{\frac{11}{4}} = \frac{\sqrt{11}}{2}$$
- **【最终答案】**
  **[1] $\vec{a}\cdot\vec{b} = 1$　　[2] $6$　　[3] $t = -\dfrac{1}{4}$ のとき、最小値 $\dfrac{\sqrt{11}}{2}$**

---

#### 演習問題 3-(6)
- **【原题重现与翻译】**
  - 原题：$k$ は実数とする。$|\vec{a}| = 2,\; |\vec{b}| = 3,\; |\vec{a} - \vec{b}| = \sqrt{7}$ とするとき、$|k\vec{a} + t\vec{b}| > \sqrt{3}$ がすべての実数 $t$ に対して成り立つような $k$ の値の範囲を求めよ。
  - 中文：设 $k$ 为实数。已知 $|\vec{a}| = 2,\; |\vec{b}| = 3,\; |\vec{a} - \vec{b}| = \sqrt{7}$，求使 $|k\vec{a} + t\vec{b}| > \sqrt{3}$ 对所有实数 $t$ 恒成立的 $k$ 的取值范围。
- **【考点定位】**
  - 向量内积 + 一元二次绝对不等式（恒成立条件 $D < 0$）。
- **【分步标准解答】**
  まず $|\vec{a} - \vec{b}| = \sqrt{7}$ の両辺を 2 乗して
  $$|\vec{a}|^2 - 2\vec{a}\cdot\vec{b} + |\vec{b}|^2 = 7$$
  $$2^2 - 2\vec{a}\cdot\vec{b} + 3^2 = 7 \implies 13 - 2\vec{a}\cdot\vec{b} = 7 \implies \vec{a}\cdot\vec{b} = 3$$
  次に、不等式 $|k\vec{a} + t\vec{b}| > \sqrt{3}$ の両辺はともに正（または非負）であるから、両辺を 2 乗した不等式と同値である：
  $$|k\vec{a} + t\vec{b}|^2 > 3$$
  $$k^2|\vec{a}|^2 + 2kt(\vec{a}\cdot\vec{b}) + t^2|\vec{b}|^2 > 3$$
  $|\vec{a}| = 2,\; |\vec{b}| = 3,\; \vec{a}\cdot\vec{b} = 3$ を代入すると
  $$4k^2 + 6kt + 9t^2 > 3$$
  $t$ について整理すると
  $$9t^2 + 6kt + (4k^2 - 3) > 0 \qquad \cdots ①$$
  > 💡 讲师批注：看清主元！题目要求「对所有实数 $t$ 恒成立」，因此把不等式整理成关于 $t$ 的二次不等式，此时二次项系数 $9 > 0$（开口向上）。

  ① がすべての実数 $t$ に対して成り立つための必要十分条件は、$t$ の 2 次方程式 $9t^2 + 6kt + (4k^2 - 3) = 0$ の判別式 $D$ が $D < 0$ となることである。
  $$\frac{D}{4} = (3k)^2 - 9(4k^2 - 3) < 0$$
  $$9k^2 - 36k^2 + 27 < 0$$
  $$-27k^2 + 27 < 0 \implies k^2 - 1 > 0$$
  $$(k + 1)(k - 1) > 0 \implies k < -1,\; 1 < k$$
  > 💡 讲师批注：也可用配方法直接验证：$9t^2 + 6kt + 4k^2 - 3 = 9\left(t + \frac{k}{3}\right)^2 + 3k^2 - 3 > 0$ 对任意 $t$ 恒成立 $\iff 3k^2 - 3 > 0 \iff k < -1$ 或 $k > 1$。
- **【最终答案】**
  **$k < -1,\; 1 < k$**

---

#### 演習問題 3-(7)
- **【原题重现与翻译】**
  - 原题：$\triangle OAB$ において、$\overrightarrow{OA} = \vec{a},\; \overrightarrow{OB} = \vec{b}$ のとき、$\triangle OAB$ の面積 $S$ を $\vec{a}, \vec{b}$ で表せ。
  - 中文：在 $\triangle OAB$ 中，设 $\overrightarrow{OA} = \vec{a},\; \overrightarrow{OB} = \vec{b}$，用 $\vec{a}, \vec{b}$ 表示 $\triangle OAB$ 的面积 $S$。
- **【考点定位】**
  - 三角形面积公式 $S = \frac{1}{2}ab\sin\theta$ 与向量内积的综合推导。
- **【分步标准解答】**
  $\angle AOB = \theta$ とすると、$0^\circ < \theta < 180^\circ$ より $\sin\theta > 0$ であるから
  $$\sin\theta = \sqrt{1 - \cos^2\theta}$$
  また、内積の定義より $\cos\theta = \dfrac{\vec{a}\cdot\vec{b}}{|\vec{a}||\vec{b}|}$ である。
  したがって、$\triangle OAB$ の面積 $S$ は
  $$S = \frac{1}{2}|\vec{a}||\vec{b}|\sin\theta = \frac{1}{2}|\vec{a}||\vec{b}|\sqrt{1 - \cos^2\theta}$$
  $$= \frac{1}{2}|\vec{a}||\vec{b}|\sqrt{1 - \left(\frac{\vec{a}\cdot\vec{b}}{|\vec{a}||\vec{b}|}\right)^2}$$
  > 💡 讲师批注：把外面的正数 $|\vec{a}||\vec{b}|$ 放进根号内（变为 $|\vec{a}|^2|\vec{b}|^2$）即可消去分母，得到极其对称的向量面积公式。

  $$= \frac{1}{2}\sqrt{|\vec{a}|^2|\vec{b}|^2 - (\vec{a}\cdot\vec{b})^2}$$
- **【最终答案】**
  **$S = \dfrac{1}{2}\sqrt{|\vec{a}|^2|\vec{b}|^2 - (\vec{a}\cdot\vec{b})^2}$**

---

#### 演習問題 3-(8)
- **【原题重现与翻译】**
  - 原题：(7) を利用して、3 点 $O(0,0),\; A(a_1, a_2),\; B(b_1, b_2)$ を頂点とする $\triangle OAB$ の面積 $S$ を $a_1, a_2, b_1, b_2$ を用いて表せ。
  - 中文：利用 (7) 的结论，用 $a_1, a_2, b_1, b_2$ 表示以 $O(0,0),\; A(a_1, a_2),\; B(b_1, b_2)$ 为顶点的 $\triangle OAB$ 的面积 $S$。
- **【考点定位】**
  - 坐标平面上过原点的三角形面积公式（行列式面积公式）。
- **【分步标准解答】**
  $\vec{a} = \overrightarrow{OA} = (a_1, a_2),\; \vec{b} = \overrightarrow{OB} = (b_1, b_2)$ より
  $$|\vec{a}|^2 = a_1^2 + a_2^2, \qquad |\vec{b}|^2 = b_1^2 + b_2^2, \qquad \vec{a}\cdot\vec{b} = a_1 b_1 + a_2 b_2$$
  これらを (7) の公式の根号内に代入すると
  $$|\vec{a}|^2|\vec{b}|^2 - (\vec{a}\cdot\vec{b})^2 = (a_1^2 + a_2^2)(b_1^2 + b_2^2) - (a_1 b_1 + a_2 b_2)^2$$
  $$= (a_1^2 b_1^2 + a_1^2 b_2^2 + a_2^2 b_1^2 + a_2^2 b_2^2) - (a_1^2 b_1^2 + 2a_1 a_2 b_1 b_2 + a_2^2 b_2^2)$$
  $$= a_1^2 b_2^2 - 2a_1 a_2 b_1 b_2 + a_2^2 b_1^2 = (a_1 b_2 - a_2 b_1)^2$$
  > 💡 讲师批注：这是经典的**拉格朗日恒等式**！注意 $\sqrt{X^2} = |X|$，绝对不能漏掉绝对值符号！

  よって
  $$S = \frac{1}{2}\sqrt{(a_1 b_2 - a_2 b_1)^2} = \frac{1}{2}|a_1 b_2 - a_2 b_1|$$
  > 💡 讲师批注：若三角形三个顶点都不在原点（如 $A, B, C$），只需先平移令其中一个顶点为原点（取 $\overrightarrow{AB} = (x_1, y_1),\; \overrightarrow{AC} = (x_2, y_2)$），同样可用 $S = \frac{1}{2}|x_1 y_2 - x_2 y_1|$ 秒杀。
- **【最终答案】**
  **$S = \dfrac{1}{2}|a_1 b_2 - a_2 b_1|$**

---

### 演習問題 4（位置ベクトル・ベクトルと図形）

#### 演習問題 4-(1)
- **【原题重现与翻译】**
  - 原题：平行四辺形 $ABCD$ において、辺 $CD$ を $2:3$ に内分する点を $E$、対角線 $BD$ を $5:3$ に内分する点を $F$ とする。3 点 $A, F, E$ は一直線上にあることを証明せよ。
  - 中文：在平行四边形 $ABCD$ 中，设点 $E$ 将边 $CD$ 按 $2:3$ 内分，点 $F$ 将对角线 $BD$ 按 $5:3$ 内分。证明 $A, F, E$ 三点共线。
- **【考点定位】**
  - 基底选择 + 内分点公式 + 三点共线条件（$\overrightarrow{AF} = k\overrightarrow{AE}$）。
- **【图解辅助（SVG 矢量图）】**

<svg viewBox="0 0 360 190" width="100%" style="max-width:360px;display:block;margin:12px auto;" xmlns="http://www.w3.org/2000/svg">
  <!-- Parallelogram ABCD: A(40,150), B(220,150), C(310,40), D(130,40) -->
  <polygon points="40,150 220,150 310,40 130,40" fill="#f8fafc" stroke="#1e293b" stroke-width="2"/>
  <!-- Diagonal BD -->
  <line x1="220" y1="150" x2="130" y2="40" stroke="#64748b" stroke-width="1.5" stroke-dasharray="5,3"/>
  <!-- E divides CD in 2:3 -> C(310,40) to D(130,40): E = (310*3 + 130*2)/5 = (238, 40) -->
  <!-- F divides BD in 5:3 -> B(220,150) to D(130,40): F = (220*3 + 130*5)/8 = (163.75, 81.25) -->
  <!-- Line A-F-E -->
  <line x1="40" y1="150" x2="238" y2="40" stroke="#dc2626" stroke-width="2.2"/>
  <circle cx="40" cy="150" r="3.5" fill="#0f172a"/>
  <circle cx="220" cy="150" r="3.5" fill="#0f172a"/>
  <circle cx="310" cy="40" r="3.5" fill="#0f172a"/>
  <circle cx="130" cy="40" r="3.5" fill="#0f172a"/>
  <circle cx="238" cy="40" r="4" fill="#dc2626"/>
  <circle cx="163.75" cy="81.25" r="4" fill="#2563eb"/>
  <!-- Labels -->
  <text x="24" y="164" font-size="13" font-weight="bold" fill="#0f172a">A</text>
  <text x="224" y="166" font-size="13" font-weight="bold" fill="#0f172a">B</text>
  <text x="316" y="38" font-size="13" font-weight="bold" fill="#0f172a">C</text>
  <text x="116" y="36" font-size="13" font-weight="bold" fill="#0f172a">D</text>
  <text x="234" y="28" font-size="13" font-weight="bold" fill="#dc2626">E</text>
  <text x="171" y="96" font-size="13" font-weight="bold" fill="#2563eb">F</text>
  <!-- Ratio labels -->
  <text x="274" y="32" font-size="11" fill="#475569">2</text>
  <text x="180" y="32" font-size="11" fill="#475569">3</text>
  <text x="196" y="124" font-size="11" fill="#475569">5</text>
  <text x="142" y="64" font-size="11" fill="#475569">3</text>
</svg>

- **【分步标准解答】**
  $\overrightarrow{AB} = \vec{b},\; \overrightarrow{AD} = \vec{d}$ とおく。
  平行四辺形 $ABCD$ より、$\overrightarrow{DC} = \overrightarrow{AB} = \vec{b}$ である。
  点 $E$ は辺 $CD$ を $2:3$ に内分するから、$DE:EC = 3:2$ であり、$\overrightarrow{DE} = \dfrac{3}{5}\overrightarrow{DC} = \dfrac{3}{5}\vec{b}$。
  よって
  $$\overrightarrow{AE} = \overrightarrow{AD} + \overrightarrow{DE} = \vec{d} + \frac{3}{5}\vec{b} = \frac{3}{5}\vec{b} + \vec{d} \qquad \cdots ①$$
  > 💡 讲师批注：务必注意比例顺序！题目说「辺 $CD$ を $2:3$ に内分する」，意思是 $CE : ED = 2 : 3$，千万不要看反成 $DE : EC = 2 : 3$！

  また、点 $F$ は対角線 $BD$ を $5:3$ に内分するから、内分点の公式より
  $$\overrightarrow{AF} = \frac{3\overrightarrow{AB} + 5\overrightarrow{AD}}{5 + 3} = \frac{3\vec{b} + 5\vec{d}}{8} = \frac{3}{8}\vec{b} + \frac{5}{8}\vec{d} \qquad \cdots ②$$
  ①、② を比較すると
  $$\overrightarrow{AF} = \frac{5}{8}\left(\frac{3}{5}\vec{b} + \vec{d}\right) = \frac{5}{8}\overrightarrow{AE}$$
  したがって、$\overrightarrow{AF} = \dfrac{5}{8}\overrightarrow{AE}$ が成り立つので、3 点 $A, F, E$ は一直線上にある。（証明終）
  > 💡 讲师批注：不仅证出了三点共线，还顺带得到了比例关系 $AF : FE = 5 : 3$。
- **【最终答案】**
  **証明済（$\overrightarrow{AF} = \dfrac{5}{8}\overrightarrow{AE}$ より、3 点 $A, F, E$ は一直線上にある）**

---

#### 演習問題 4-(2)
- **【原题重现与翻译】**
  - 原题：$\triangle ABC$ の辺 $BC, CA, AB$ をそれぞれ $m:n$（$m > 0,\; n > 0$）に内分する点を $P, Q, R$ とするとき、$\triangle ABC$ と $\triangle PQR$ の重心は一致することを示せ。
  - 中文：设点 $P, Q, R$ 分别将 $\triangle ABC$ 的边 $BC, CA, AB$ 按 $m:n$（$m>0, n>0$）内分，证明 $\triangle ABC$ 与 $\triangle PQR$ 的重心重合。
- **【考点定位】**
  - 位置向量 + 内分点公式 + 三角形重心公式。
- **【分步标准解答】**
  3 点 $A, B, C$ の位置ベクトルをそれぞれ $\vec{a}, \vec{b}, \vec{c}$ とし、点 $P, Q, R$ の位置ベクトルをそれぞれ $\vec{p}, \vec{q}, \vec{r}$ とする。
  点 $P, Q, R$ はそれぞれ辺 $BC, CA, AB$ を $m:n$ に内分するので、内分点の公式より
  $$\vec{p} = \frac{n\vec{b} + m\vec{c}}{m + n}, \qquad \vec{q} = \frac{n\vec{c} + m\vec{a}}{m + n}, \qquad \vec{r} = \frac{n\vec{a} + m\vec{b}}{m + n}$$
  > 💡 讲师批注：轮换对称结构！写完 $\vec{p}$ 后，按 $A \to B \to C \to A$ 轮换即可写出 $\vec{q}, \vec{r}$，绝对不会出错。

  $\triangle PQR$ の重心 $G'$ の位置ベクトルを $\vec{g'}$ とすると
  $$\vec{g'} = \frac{\vec{p} + \vec{q} + \vec{r}}{3} = \frac{1}{3}\left(\frac{n\vec{b} + m\vec{c}}{m + n} + \frac{n\vec{c} + m\vec{a}}{m + n} + \frac{n\vec{a} + m\vec{b}}{m + n}\right)$$
  $$= \frac{1}{3} \cdot \frac{(m + n)\vec{a} + (m + n)\vec{b} + (m + n)\vec{c}}{m + n}$$
  $m + n > 0$ より分子・分母を $(m + n)$ で約分すると
  $$\vec{g'} = \frac{\vec{a} + \vec{b} + \vec{c}}{3}$$
  これは $\triangle ABC$ の重心 $G$ の位置ベクトル $\vec{g} = \dfrac{\vec{a} + \vec{b} + \vec{c}}{3}$ に等しい。
  よって、$\triangle ABC$ と $\triangle PQR$ の重心は一致する。（証明終）
- **【最终答案】**
  **証明済（$\vec{g'} = \dfrac{\vec{p}+\vec{q}+\vec{r}}{3} = \dfrac{\vec{a}+\vec{b}+\vec{c}}{3} = \vec{g}$ より、重心は一致する）**

---

#### 演習問題 4-(3)
- **【原题重现与翻译】**
  - 原题：$\triangle OAB$ において、$\overrightarrow{OA} = \vec{a},\; \overrightarrow{OB} = \vec{b}$ とする。辺 $OA$ を $3:2$ に内分する点を $C$、辺 $OB$ を $3:4$ に内分する点を $D$、線分 $AD$ と $BC$ との交点を $P$ とし、直線 $OP$ と辺 $AB$ との交点を $Q$ とする。次のベクトルを $\vec{a}, \vec{b}$ を用いて表せ。
    - [1] $\overrightarrow{OP}$　　　[2] $\overrightarrow{OQ}$
  - 中文：在 $\triangle OAB$ 中，设 $\overrightarrow{OA} = \vec{a},\; \overrightarrow{OB} = \vec{b}$。点 $C$ 将边 $OA$ 按 $3:2$ 内分，点 $D$ 将边 $OB$ 按 $3:4$ 内分，线段 $AD$ 与 $BC$ 交于点 $P$，直线 $OP$ 与边 $AB$ 交于点 $Q$。用 $\vec{a}, \vec{b}$ 表示下列向量：[1] $\overrightarrow{OP}$；[2] $\overrightarrow{OQ}$。
- **【考点定位】**
  - EJU 向量最经典母题：**交点位置向量的「双途径表示 + 比较系数法」**（一次独立性の利用）。
- **【图解辅助（SVG 矢量图）】**

<svg viewBox="0 0 320 220" width="100%" style="max-width:320px;display:block;margin:12px auto;" xmlns="http://www.w3.org/2000/svg">
  <!-- O(140,25), A(40,195), B(280,195) -->
  <!-- C divides OA 3:2 -> O*2/5 + A*3/5 = (80, 127) -->
  <!-- D divides OB 3:4 -> O*4/7 + B*3/7 = (200, 97.86) -->
  <!-- P = 6/13 a + 3/13 b -> O + 6/13(-100,170) + 3/13(140,170) = (140 - 46.15 + 32.31, 25 + 78.46 + 39.23) = (126.15, 142.69) -->
  <!-- Q = 2/3 a + 1/3 b -> (120, 195) -->
  <polygon points="140,25 40,195 280,195" fill="#f8fafc" stroke="#1e293b" stroke-width="2"/>
  <line x1="40" y1="195" x2="200" y2="97.86" stroke="#2563eb" stroke-width="1.6"/>
  <line x1="280" y1="195" x2="80" y2="127" stroke="#2563eb" stroke-width="1.6"/>
  <line x1="140" y1="25" x2="120" y2="195" stroke="#dc2626" stroke-width="1.8" stroke-dasharray="5,3"/>
  <circle cx="140" cy="25" r="3.5" fill="#0f172a"/>
  <circle cx="40" cy="195" r="3.5" fill="#0f172a"/>
  <circle cx="280" cy="195" r="3.5" fill="#0f172a"/>
  <circle cx="80" cy="127" r="3.5" fill="#2563eb"/>
  <circle cx="200" cy="97.86" r="3.5" fill="#2563eb"/>
  <circle cx="126.15" cy="142.69" r="4" fill="#dc2626"/>
  <circle cx="120" cy="195" r="4" fill="#dc2626"/>
  <text x="136" y="17" font-size="13" font-weight="bold" fill="#0f172a">O</text>
  <text x="26" y="205" font-size="13" font-weight="bold" fill="#0f172a">A</text>
  <text x="285" y="205" font-size="13" font-weight="bold" fill="#0f172a">B</text>
  <text x="64" y="128" font-size="13" font-weight="bold" fill="#2563eb">C</text>
  <text x="208" y="96" font-size="13" font-weight="bold" fill="#2563eb">D</text>
  <text x="135" y="140" font-size="13" font-weight="bold" fill="#dc2626">P</text>
  <text x="115" y="213" font-size="13" font-weight="bold" fill="#dc2626">Q</text>
  <text x="98" y="75" font-size="11" fill="#475569">3</text>
  <text x="50" y="165" font-size="11" fill="#475569">2</text>
  <text x="176" y="60" font-size="11" fill="#475569">3</text>
  <text x="246" y="146" font-size="11" fill="#475569">4</text>
</svg>

- **【分步标准解答】**
  - **[1] $\overrightarrow{OP}$ を求める**：
    条件より $\overrightarrow{OC} = \dfrac{3}{5}\vec{a},\; \overrightarrow{OD} = \dfrac{3}{7}\vec{b}$ である。
    点 $P$ は線分 $AD$ 上にあるから、実数 $s$ を用いて
    $$\overrightarrow{OP} = (1 - s)\overrightarrow{OA} + s\overrightarrow{OD} = (1 - s)\vec{a} + \frac{3}{7}s\vec{b} \qquad \cdots ①$$
    また、点 $P$ は線分 $BC$ 上にあるから、実数 $t$ を用いて
    $$\overrightarrow{OP} = t\overrightarrow{OC} + (1 - t)\overrightarrow{OB} = \frac{3}{5}t\vec{a} + (1 - t)\vec{b} \qquad \cdots ②$$
    $\vec{a} \neq \vec{0},\; \vec{b} \neq \vec{0}$ かつ $\vec{a} \not\parallel \vec{b}$ であるから、①、② の係数を比較して
    $$\begin{cases} 1 - s = \dfrac{3}{5}t & \cdots ③ \\ \dfrac{3}{7}s = 1 - t & \cdots ④ \end{cases}$$
    > 💡 讲师批注：日本记述式考场中，比较系数前**必须写明「$\vec{a} \neq \vec{0},\; \vec{b} \neq \vec{0}$ かつ $\vec{a} \not\parallel \vec{b}$」（线性无关）**，否则会被扣 1–2 分！

    ④ より $t = 1 - \dfrac{3}{7}s$。これを ③ に代入すると
    $$1 - s = \frac{3}{5}\left(1 - \frac{3}{7}s\right) = \frac{3}{5} - \frac{9}{35}s$$
    両辺に $35$ を掛けて整理すると
    $$35 - 35s = 21 - 9s \implies 26s = 14 \implies s = \frac{7}{13}$$
    これを ① に代入すると
    $$1 - s = \frac{6}{13}, \qquad \frac{3}{7}s = \frac{3}{13}$$
    よって
    $$\overrightarrow{OP} = \frac{6}{13}\vec{a} + \frac{3}{13}\vec{b}$$

  - **[2] $\overrightarrow{OQ}$ を求める**：
    点 $Q$ は直線 $OP$ 上にあるから、実数 $k$ を用いて
    $$\overrightarrow{OQ} = k\overrightarrow{OP} = \frac{6}{13}k\vec{a} + \frac{3}{13}k\vec{b}$$
    さらに点 $Q$ は辺 $AB$ 上にあるから、$\vec{a}, \vec{b}$ の係数の和が $1$ である：
    $$\frac{6}{13}k + \frac{3}{13}k = 1 \implies \frac{9}{13}k = 1 \implies k = \frac{13}{9}$$
    したがって
    $$\overrightarrow{OQ} = \frac{6}{13}\cdot\frac{13}{9}\vec{a} + \frac{3}{13}\cdot\frac{13}{9}\vec{b} = \frac{2}{3}\vec{a} + \frac{1}{3}\vec{b}$$
    > 💡 讲师批注：用**塞瓦定理（チェバの定理）**秒速验算：$\dfrac{OC}{CA}\cdot\dfrac{AQ}{QB}\cdot\dfrac{BD}{DO} = 1 \implies \dfrac{3}{2}\cdot\dfrac{AQ}{QB}\cdot\dfrac{4}{3} = 1 \implies \dfrac{AQ}{QB} = \dfrac{1}{2}$，所以 $Q$ 内分 $AB$ 为 $1:2$，$\overrightarrow{OQ} = \dfrac{2\vec{a}+\vec{b}}{3}$。100% 吻合！
- **【最终答案】**
  **[1] $\overrightarrow{OP} = \dfrac{6}{13}\vec{a} + \dfrac{3}{13}\vec{b}$　　[2] $\overrightarrow{OQ} = \dfrac{2}{3}\vec{a} + \dfrac{1}{3}\vec{b}$**

---

#### 演習問題 4-(4)
- **【原题重现与翻译】**
  - 原题：平面上に $\triangle OAB$ があり、$OA = 5,\; OB = 6,\; AB = 7$ とする。また、$\triangle OAB$ の垂心を $H$ とする。
    - [1] $\cos\angle AOB$ を求めよ。
    - [2] $\overrightarrow{OA} = \vec{a},\; \overrightarrow{OB} = \vec{b}$ とするとき、$\overrightarrow{OH}$ を $\vec{a}, \vec{b}$ を用いて表せ。
  - 中文：平面上有 $\triangle OAB$，满足 $OA = 5,\; OB = 6,\; AB = 7$，设其垂心为 $H$。
    - [1] 求 $\cos\angle AOB$；
    - [2] 设 $\overrightarrow{OA} = \vec{a},\; \overrightarrow{OB} = \vec{b}$，用 $\vec{a}, \vec{b}$ 表示 $\overrightarrow{OH}$。
- **【考点定位】**
  - 余弦定理 + **三角形垂心（垂心）的位置向量求法**（利用两条高线垂直的内积方程组）。
- **【图解辅助（SVG 矢量图）】**

<svg viewBox="0 0 320 200" width="100%" style="max-width:320px;display:block;margin:12px auto;" xmlns="http://www.w3.org/2000/svg">
  <!-- O(60,170), B(260,170) [OB=6 -> scale 33.33 -> 200px] -->
  <!-- OA=5 -> 166.67px, cos O = 1/5, sin O = 2sqrt(6)/5 = 0.9798 -> A(60+33.33, 170-163.3) = (93.33, 6.7) -->
  <!-- Wait, adjust scale to 25px/unit: O(60,175), B(210,175) [150px], A(60+25, 175-122.5)=(85,52.5) -->
  <!-- H = 5/24 a + 19/144 b = (60 + 5/24*25 + 19/144*150, 175 - 5/24*122.5) = (60+5.21+19.79, 175-25.52) = (85, 149.48) -->
  <polygon points="60,175 210,175 85,52.5" fill="#f8fafc" stroke="#1e293b" stroke-width="2"/>
  <!-- Altitude from A to OB (x=85) -->
  <line x1="85" y1="52.5" x2="85" y2="175" stroke="#2563eb" stroke-width="1.4" stroke-dasharray="4,3"/>
  <!-- Altitude from B to OA: foot on OA -->
  <!-- OA vector = (25, -122.5), OB = (150, 0), proj = (150*25)/(625+15006.25) = 3750/15631.25 = 0.24 -> foot (66, 145.6) -->
  <line x1="210" y1="175" x2="66" y2="145.6" stroke="#2563eb" stroke-width="1.4" stroke-dasharray="4,3"/>
  <!-- Vector OH -->
  <line x1="60" y1="175" x2="85" y2="149.5" stroke="#dc2626" stroke-width="2"/>
  <!-- Right angle mark at (85,175) -->
  <polyline points="85,165 95,165 95,175" fill="none" stroke="#2563eb" stroke-width="1.2"/>
  <circle cx="60" cy="175" r="3.5" fill="#0f172a"/>
  <circle cx="210" cy="175" r="3.5" fill="#0f172a"/>
  <circle cx="85" cy="52.5" r="3.5" fill="#0f172a"/>
  <circle cx="85" cy="149.5" r="4" fill="#dc2626"/>
  <text x="44" y="185" font-size="13" font-weight="bold" fill="#0f172a">O</text>
  <text x="216" y="185" font-size="13" font-weight="bold" fill="#0f172a">B</text>
  <text x="80" y="42" font-size="13" font-weight="bold" fill="#0f172a">A</text>
  <text x="92" y="146" font-size="13" font-weight="bold" fill="#dc2626">H</text>
  <text x="58" y="112" font-size="12" fill="#475569">5</text>
  <text x="132" y="192" font-size="12" fill="#475569">6</text>
  <text x="155" y="106" font-size="12" fill="#475569">7</text>
</svg>

- **【分步标准解答】**
  - **[1] $\cos\angle AOB$ を求める**：
    $\triangle OAB$ に余弦定理を用いると
    $$\cos\angle AOB = \frac{OA^2 + OB^2 - AB^2}{2 \cdot OA \cdot OB} = \frac{5^2 + 6^2 - 7^2}{2 \cdot 5 \cdot 6} = \frac{25 + 36 - 49}{60} = \frac{12}{60} = \frac{1}{5}$$

  - **[2] $\overrightarrow{OH}$ を求める**：
    [1] の結果より、内積 $\vec{a}\cdot\vec{b}$ は
    $$\vec{a}\cdot\vec{b} = |\vec{a}||\vec{b}|\cos\angle AOB = 5 \cdot 6 \cdot \frac{1}{5} = 6$$
    また $|\vec{a}|^2 = 25,\; |\vec{b}|^2 = 36$ である。
    $\vec{a} \neq \vec{0},\; \vec{b} \neq \vec{0},\; \vec{a} \not\parallel \vec{b}$ より、実数 $s, t$ を用いて $\overrightarrow{OH} = s\vec{a} + t\vec{b}$ とおく。
    点 $H$ は $\triangle OAB$ の垂心であるから、$\overrightarrow{AH} \perp \overrightarrow{OB}$ かつ $\overrightarrow{BH} \perp \overrightarrow{OA}$ が成り立つ。
    > 💡 讲师批注：垂心有三条垂直关系，选取以 $O$ 为端点的两条边（$\overrightarrow{AH}\perp\vec{b}$ 和 $\overrightarrow{BH}\perp\vec{a}$）列内积为 $0$ 最简洁！第三条 $\overrightarrow{OH}\perp\overrightarrow{AB}$ 可留作验算。

    ① $\overrightarrow{AH} \cdot \overrightarrow{OB} = 0$ より
    $$(\overrightarrow{OH} - \vec{a})\cdot\vec{b} = 0 \implies \{(s - 1)\vec{a} + t\vec{b}\}\cdot\vec{b} = 0$$
    $$(s - 1)(\vec{a}\cdot\vec{b}) + t|\vec{b}|^2 = 0 \implies 6(s - 1) + 36t = 0$$
    両辺を $6$ で割ると
    $$s + 6t = 1 \qquad \cdots ①$$

    ② $\overrightarrow{BH} \cdot \overrightarrow{OA} = 0$ より
    $$(\overrightarrow{OH} - \vec{b})\cdot\vec{a} = 0 \implies \{s\vec{a} + (t - 1)\vec{b}\}\cdot\vec{a} = 0$$
    $$s|\vec{a}|^2 + (t - 1)(\vec{a}\cdot\vec{b}) = 0 \implies 25s + 6(t - 1) = 0$$
    $$25s + 6t = 6 \qquad \cdots ②$$

    ② $-$ ① より
    $$24s = 5 \implies s = \frac{5}{24}$$
    ① に代入して
    $$6t = 1 - \frac{5}{24} = \frac{19}{24} \implies t = \frac{19}{144}$$
    したがって
    $$\overrightarrow{OH} = \frac{5}{24}\vec{a} + \frac{19}{144}\vec{b}$$
    > 💡 讲师批注：用第三条垂直关系验算：$\overrightarrow{OH}\cdot(\vec{b}-\vec{a}) = \frac{5}{24}(6-25) + \frac{19}{144}(36-6) = -\frac{95}{24} + \frac{95}{24} = 0$，绝对无误！
- **【最终答案】**
  **[1] $\cos\angle AOB = \dfrac{1}{5}$　　[2] $\overrightarrow{OH} = \dfrac{5}{24}\vec{a} + \dfrac{19}{144}\vec{b}$**

---

> 👉 接续本切片后半部分（演習問題 4-(5)~(8)、演習問題 5-(1)~(4)、演習問題 6-(1)），请见 **`note_015_b.md`**。
