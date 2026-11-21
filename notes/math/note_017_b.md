# 《EJU 教材全解与备课讲义》数学 017-B（P250–P255）

> **对应源文件**：`work_math/ocr_md/ocr_017_p241-255.md`（第九章《複素数平面》之「ド・モアブルの定理」「1 の $n$ 乗根」；第十章《数列》之「等差数列」「調和数列」）
> **视觉核对参考图**：`work_math/ref_imgs/page_0250.jpg`、`page_0251.jpg`、`page_0252.jpg`、`page_0255.jpg`
> **本切片分册说明**：接续 `note_017_a.md`（P241–P249），本分册完整覆盖 P250–P255 全部知识点与例题解析。

---

## 一、国内高中基础知识点唤醒与 EJU 考纲差异对比

本分册横跨两大高频考点板块：**数学Ⅲ/C《ド・モアブルの定理と 1 の $n$ 乗根》**（复数高次幂与复数方程求解）与 **数学B《等差数列・調和数列》**（数列开篇基础）。

### 1.1 棣莫弗定理与 1 的 $n$ 次单位根（ド・モアブルの定理と 1 の $n$ 乗根）

- **棣莫弗定理（ド・モアブルの定理）**：
  对任意**整数 $n$**（包含正整数、$0$ 与负整数）：
  $$(\cos\theta + i\sin\theta)^n = \cos n\theta + i\sin n\theta$$
  - 若 $z = r(\cos\theta + i\sin\theta)$（$r > 0$），则 $z^n = r^n(\cos n\theta + i\sin n\theta)$。
  - **易错提醒**：定理仅对极形式的标准结构 $\cos\theta + i\sin\theta$（中间为加号、余弦在前、正弦在后、角相同）直接成立！若遇到 $\cos\theta - i\sin\theta$ 或 $\sin\theta + i\cos\theta$，必须先转化为标准极形式再套用。
- **1 的 $n$ 次方根（1 の $n$ 乗根）**（$n$ 为自然数）：
  1. 方程 $z^n = 1$ 的全部 $n$ 个复数解为：
     $$z_k = \cos\frac{2k\pi}{n} + i\sin\frac{2k\pi}{n} \qquad (k = 0, 1, 2, \dots, n-1)$$
  2. **几何意义**：当 $n \ge 3$ 时，点 $z_0, z_1, \dots, z_{n-1}$ 在复数平面上是以点 $1$ 为一个顶点、**内接于单位圆的正 $n$ 边形**的各顶点。
  3. 一般复数方程 $z^n = \alpha\ (\alpha \neq 0)$ 的解法：将 $\alpha$ 化为极形式 $R(\cos\varphi + i\sin\varphi)$，设 $z = r(\cos\theta + i\sin\theta)$，由 $r^n = R$ 与 $n\theta = \varphi + 2k\pi\ (k = 0, 1, \dots, n-1)$ 即可一次性求出全部 $n$ 个根（它们均匀分布在以原点为圆心、半径为 $\sqrt[n]{R}$ 的圆上，构成正 $n$ 边形）。

### 1.2 数列的基本概念、等差数列与调和数列（等差数列・調和数列）

- **数列的基本术语**：
  - 将数排成一列称为**数列（数列）**，记作 $\{a_n\}$；第 1 项 $a_1$ 称**初项（初項）**，第 $n$ 项 $a_n$ 用 $n$ 的式子表示时称**通项（一般項）**。
- **等差数列（等差数列）**（初项 $a$、公差 $d$）：
  - **定义**：对一切自然数 $n$，$a_{n+1} - a_n = d$（常数）。
  - **通项公式**：$a_n = a + (n-1)d$（当 $d \neq 0$ 时，是关于 $n$ 的一次式）。
  - **等差中项（等差中項）**：$a, b, c$ 成等差数列 $\iff 2b = a + c$（$b$ 即 $a, c$ 的算术平均数 相加平均）。
  - **前 $n$ 项和公式（等差数列の和）**：
    $$S_n = \frac{1}{2}n(a + l) = \frac{1}{2}n\{2a + (n-1)d\}$$
    （其中 $l = a_n$ 为末项，$n$ 为项数；当 $d \neq 0$ 时，$S_n$ 是不含常数项的关于 $n$ 的二次式）。
- **调和数列（調和数列）**：
  - 定义：对各项非零的数列 $\{a_n\}$，若其**倒数数列** $\left\{\dfrac{1}{a_n}\right\}$ 构成等差数列，则称 $\{a_n\}$ 为**调和数列**。
  - 解题铁律：**取倒数 $\to$ 按等差数列求通项 $\to$ 再取倒数还原**。

### 1.3 国内高中 vs. 日本 EJU 考纲差异对比

| 对比维度 | 国内高中习惯 | 日本 EJU 习惯 | 备课/应试提醒 |
| :--- | :--- | :--- | :--- |
| **棣莫弗定理与单位根** | 新高考已删去或仅作阅读材料 | **数学Ⅲ/C 必考核心**，常与多项式因式分解、正多边形面积/周长综合 | 必须熟练掌握 $z^n = \alpha$ 的极形式求解，以及 $\cos\theta = \dfrac{z+z^{-1}}{2}$ 技巧 |
| **自然数定义** | 国内教材含 $0$（$0, 1, 2, \dots$） | **日本严格指正整数 $1, 2, 3, \dots$** | 如演習問題 4-(2) 求「最小の自然数 $n$」，答案是 $12$ 而非 $0$！ |
| **调和数列** | 高中课纲很少单独命名 | 日本参考书与 EJU 教材常作为等差数列的直接延伸考查 | 牢记日文名 **調和数列（ちょうわすうれつ）**，见词立刻取倒数 |
| **等差数列证明格式** | 直接观察一次式即可 | 日本記述式要求严格计算 **$a_{n+1} - a_n = \text{定数}$（与 $n$ 无关）** | 如第十章 演習問題 1-(1)，不可只说「因为是一次式所以是等差数列」 |

---

## 二、日文核心词汇与公式假名注音

### 2.1 本分册日文核心词汇

- ド・モアブルの定理（どもあぶるのていり / do moaburu no teiri） — 棣莫弗定理
- 1 の $n$ 乗根（いちのエヌじょうこん / ichi no enu joukon） — 1 的 $n$ 次单位根
- 正 $n$ 角形（せいエヌかっけい / sei enu kakkei） — 正 $n$ 边形
- 数列（すうれつ / suuretsu） — 数列
- 初項（しょこう / shokou） — 首项（第一项）
- 末項（まっこう / makkou） — 末项
- 項数（こうすう / kousuu） — 项数
- 一般項（いっぱんこう / ippankou） — 通项（旧词复现）
- 等差数列（とうさすうれつ / tousa suuretsu） — 等差数列
- 公差（こうさ / kousa） — 公差
- 等差中項（とうさちゅうこう / tousa chuukou） — 等差中项
- 調和数列（ちょうわすうれつ / chouwa suuretsu） — 调和数列
- 逆数（ぎゃくすう / gyakusuu） — 倒数

### 2.2 核心公式的日本课堂口语读法

1. **棣莫弗定理** $(\cos\theta + i\sin\theta)^n = \cos n\theta + i\sin n\theta$
   - 课堂读法：**かっこ コサイン シータ たす アイ サイン シータ かっことじ の エヌじょう イコール コサイン エヌシータ たす アイ サイン エヌシータ**
2. **等差数列通项** $a_n = a + (n-1)d$
   - 课堂读法：**エー エヌ イコール エー たす かっこ エヌ ひく いち かっことじ ディー**
   - 备注：下标 $a_n$ 直接读作「エー エヌ」，$a_{n+1}$ 读作「エー エヌ たす いち」。
3. **等差数列求和公式** $S_n = \dfrac{1}{2}n(a + l)$
   - 课堂读法：**エス エヌ イコール にぶんのいち エヌ かっこ エー たす エル かっことじ**
   - 记忆口诀：**にぶんのいち、こうすう、かっこ しょこう たす まっこう**（二分之一 × 项数 × (初项 + 末项)）。

---

## 三、逐题深度解析（不可跳步）

---

### 第九章 演習問題 4（ド・モアブルの定理・1 の $n$ 乗根・P251–P252）

#### 演習問題 4-(1)
- **【原题重现与翻译】**
  - 原题：次の式を計算せよ。
    - [1] $\left(\cos\dfrac{\pi}{12} + i\sin\dfrac{\pi}{12}\right)^9$
    - [2] $(1 + \sqrt{3}i)^6$
    - [3] $\dfrac{1}{(1 - i)^{10}}$
  - 中文：计算下列各式。
    - [1] $\left(\cos\dfrac{\pi}{12} + i\sin\dfrac{\pi}{12}\right)^9$
    - [2] $(1 + \sqrt{3}i)^6$
    - [3] $\dfrac{1}{(1 - i)^{10}}$
- **【考点定位】**
  - 棣莫弗定理（含负整数指数）求复数高次幂。
- **【分步标准解答】**
  - **[1]** ド・モアブルの定理より、
    $$\left(\cos\frac{\pi}{12} + i\sin\frac{\pi}{12}\right)^9 = \cos\left(9 \cdot \frac{\pi}{12}\right) + i\sin\left(9 \cdot \frac{\pi}{12}\right)$$
    $$= \cos\frac{3}{4}\pi + i\sin\frac{3}{4}\pi = -\frac{\sqrt{2}}{2} + \frac{\sqrt{2}}{2}i$$
    > 💡 讲师批注：计算题最后必须算出具体的 $a + bi$ 数值，不要停留在 $\cos\dfrac{3}{4}\pi + i\sin\dfrac{3}{4}\pi$！

  - **[2]** $1 + \sqrt{3}i$ を極形式で表すと、
    $$1 + \sqrt{3}i = 2\left(\frac{1}{2} + \frac{\sqrt{3}}{2}i\right) = 2\left(\cos\frac{\pi}{3} + i\sin\frac{\pi}{3}\right)$$
    ド・モアブルの定理より、
    $$(1 + \sqrt{3}i)^6 = \left\{2\left(\cos\frac{\pi}{3} + i\sin\frac{\pi}{3}\right)\right\}^6 = 2^6\left(\cos 2\pi + i\sin 2\pi\right) = 64(1 + 0) = 64$$
    > 💡 讲师批注：千万别忘记对模长 $r = 2$ 也做 $6$ 次方（$2^6 = 64$）！这是初学者使用棣莫弗定理时最常漏掉的一步。

  - **[3]** $1 - i$ を極形式で表すと、
    $$1 - i = \sqrt{2}\left(\frac{1}{\sqrt{2}} - \frac{1}{\sqrt{2}}i\right) = \sqrt{2}\left\{\cos\left(-\frac{\pi}{4}\right) + i\sin\left(-\frac{\pi}{4}\right)\right\}$$
    よって、ド・モアブルの定理（負の整数乗）より、
    $$\frac{1}{(1 - i)^{10}} = (1 - i)^{-10} = (\sqrt{2})^{-10}\left\{\cos\left(-10 \cdot \left(-\frac{\pi}{4}\right)\right) + i\sin\left(-10 \cdot \left(-\frac{\pi}{4}\right)\right)\right\}$$
    $$= \frac{1}{2^5}\left(\cos\frac{5}{2}\pi + i\sin\frac{5}{2}\pi\right) = \frac{1}{32}\left(\cos\frac{\pi}{2} + i\sin\frac{\pi}{2}\right) = \frac{1}{32}i$$
    > 💡 讲师批注：快速验算技巧：$(1-i)^2 = 1 - 2i + i^2 = -2i$，所以 $(1-i)^{10} = (-2i)^5 = -32i^5 = -32i$，取倒数 $\dfrac{1}{-32i} = \dfrac{i}{-32i^2} = \dfrac{1}{32}i$，100% 吻合！

- **【最终答案】**
  - **[1] $-\dfrac{\sqrt{2}}{2} + \dfrac{\sqrt{2}}{2}i$**
  - **[2] $64$**
  - **[3] $\dfrac{1}{32}i$**

---

#### 演習問題 4-(2)
- **【原题重现与翻译】**
  - 原题：$\left(\dfrac{1 + i}{\sqrt{3} + i}\right)^n$ が実数となる最小の自然数 $n$ の値を求めよ。
  - 中文：求使 $\left(\dfrac{1 + i}{\sqrt{3} + i}\right)^n$ 为实数的最小自然数 $n$ 的值。
- **【考点定位】**
  - 极形式除法 + 棣莫弗定理 + 复数为实数的充要条件（虚部 $\sin(n\theta) = 0$）。
- **【分步标准解答】**
  分子と分母をそれぞれ極形式で表すと、
  $$1 + i = \sqrt{2}\left(\cos\frac{\pi}{4} + i\sin\frac{\pi}{4}\right),\qquad \sqrt{3} + i = 2\left(\cos\frac{\pi}{6} + i\sin\frac{\pi}{6}\right)$$
  よって、
  $$\frac{1 + i}{\sqrt{3} + i} = \frac{\sqrt{2}}{2}\left\{\cos\left(\frac{\pi}{4} - \frac{\pi}{6}\right) + i\sin\left(\frac{\pi}{4} - \frac{\pi}{6}\right)\right\} = \frac{\sqrt{2}}{2}\left(\cos\frac{\pi}{12} + i\sin\frac{\pi}{12}\right)$$
  ド・モアブルの定理より、
  $$\left(\frac{1 + i}{\sqrt{3} + i}\right)^n = \left(\frac{\sqrt{2}}{2}\right)^n\left(\cos\frac{n\pi}{12} + i\sin\frac{n\pi}{12}\right)$$
  これが実数となるための条件は、虚部が $0$ であること、すなわち
  $$\sin\frac{n\pi}{12} = 0$$
  > 💡 讲师批注：模长 $\left(\dfrac{\sqrt{2}}{2}\right)^n > 0$ 恒不为 $0$，因此复数为实数 $\iff \sin\dfrac{n\pi}{12} = 0 \iff$ 辐角为 $\pi$ 的整数倍。若题干问「正の実数（正实数）」，则还需 $\cos\dfrac{n\pi}{12} = 1$（即 $2\pi$ 的整数倍，$n = 24$）；本题只要求「実数」，故 $\pi$ 的整数倍即可！

  よって、$\dfrac{n\pi}{12} = k\pi$（$k$ は整数）より $n = 12k$。
  $n$ は自然数（$n \ge 1$）であるから、最小の自然数は $k = 1$ のとき $n = 12$ である。
  > 💡 讲师批注：当 $n = 12$ 时，$\cos\pi = -1$，原式 $= \left(\dfrac{\sqrt{2}}{2}\right)^{12}(-1) = -\dfrac{1}{64}$，确实是实数！

- **【最终答案】**
  **$n = 12$**

---

#### 演習問題 4-(3)
- **【原题重现与翻译】**
  - 原题：複素数 $z$ が $z + \dfrac{1}{z} = \sqrt{2}$ を満たすとき、$z^{20} + \dfrac{1}{z^{20}}$ の値を求めよ。
  - 中文：当复数 $z$ 满足 $z + \dfrac{1}{z} = \sqrt{2}$ 时，求 $z^{20} + \dfrac{1}{z^{20}}$ 的值。
- **【考点定位】**
  - 由 $z + z^{-1} = 2\cos\theta$ 识别单位圆上的复数，并用棣莫弗定理秒杀高次对称式 $z^n + z^{-n} = 2\cos n\theta$。
- **【分步标准解答】**
  $z \neq 0$ であるから、与えられた等式の両辺に $z$ を掛けると、
  $$z^2 - \sqrt{2}z + 1 = 0$$
  2 次方程式の解の公式より、
  $$z = \frac{\sqrt{2} \pm \sqrt{(\sqrt{2})^2 - 4}}{2} = \frac{\sqrt{2} \pm \sqrt{-2}}{2} = \frac{\sqrt{2}}{2} \pm \frac{\sqrt{2}}{2}i$$
  これを極形式で表すと、
  $$z = \cos\left(\pm\frac{\pi}{4}\right) + i\sin\left(\pm\frac{\pi}{4}\right) \quad (\text{複号同順})$$
  > 💡 讲师批注：**EJU 高频二级结论**：若 $z + \dfrac{1}{z} = 2\cos\theta$，则 $z = \cos\theta \pm i\sin\theta$，从而直接有 $z^n + \dfrac{1}{z^n} = 2\cos n\theta$！本题中 $2\cos\theta = \sqrt{2} \implies \theta = \dfrac{\pi}{4}$，立刻知 $z^{20} + z^{-20} = 2\cos\left(20 \cdot \dfrac{\pi}{4}\right) = 2\cos 5\pi = -2$！

  ド・モアブルの定理より、
  $$z^{20} = \cos\left(\pm 20 \cdot \frac{\pi}{4}\right) + i\sin\left(\pm 20 \cdot \frac{\pi}{4}\right) = \cos(\pm 5\pi) + i\sin(\pm 5\pi) = -1$$
  $$\frac{1}{z^{20}} = z^{-20} = \cos(\mp 5\pi) + i\sin(\mp 5\pi) = -1$$
  したがって、
  $$z^{20} + \frac{1}{z^{20}} = (-1) + (-1) = -2$$
  > 💡 讲师批注：代数递推验算：$z + z^{-1} = \sqrt{2} \implies z^2 + z^{-2} = (z+z^{-1})^2 - 2 = 0 \implies z^4 = -1 \implies z^{20} = (z^4)^5 = -1 \implies z^{20} + z^{-20} = -2$，完全一致！

- **【最终答案】**
  **$-2$**

---

#### 演習問題 4-(4)
- **【原题重现与翻译】**
  - 原题：極形式を用いて、方程式 $z^6 = 1$ を解け。
  - 中文：用极形式解方程 $z^6 = 1$。
- **【考点定位】**
  - 1 的 6 次单位根（单位圆内接正六边形的 6 个顶点）。
- **【图解辅助（SVG 矢量图）】**

<svg viewBox="0 0 320 260" width="320" height="260" xmlns="http://www.w3.org/2000/svg" style="background:#fafafa;border:1px solid #e0e0e0;border-radius:6px;">
  <defs>
    <marker id="arr5" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto">
      <path d="M0,0 L0,6 L7,3 z" fill="#333"/>
    </marker>
  </defs>
  <!-- 圆心 O(160, 130), 半径 R=85 -->
  <line x1="35" y1="130" x2="290" y2="130" stroke="#333" stroke-width="1.3" marker-end="url(#arr5)"/>
  <line x1="160" y1="245" x2="160" y2="15" stroke="#333" stroke-width="1.3" marker-end="url(#arr5)"/>
  <text x="293" y="134" font-size="12" fill="#333">実軸</text>
  <text x="166" y="22" font-size="12" fill="#333">虚軸</text>
  <text x="146" y="144" font-size="12" fill="#333">O</text>
  <!-- 单位圆 -->
  <circle cx="160" cy="130" r="85" fill="none" stroke="#90caf9" stroke-width="1.5" stroke-dasharray="4,3"/>
  <!-- 正六边形顶点: k=0:(245,130), k=1:(202.5,56.4), k=2:(117.5,56.4), k=3:(75,130), k=4:(117.5,203.6), k=5:(202.5,203.6) -->
  <polygon points="245,130 202.5,56.4 117.5,56.4 75,130 117.5,203.6 202.5,203.6" fill="#e3f2fd" fill-opacity="0.45" stroke="#1e88e5" stroke-width="2"/>
  <circle cx="245" cy="130" r="4" fill="#e53935"/>
  <text x="251" y="124" font-size="12" fill="#e53935" font-weight="bold">z₀ = 1</text>
  <circle cx="202.5" cy="56.4" r="4" fill="#e53935"/>
  <text x="208" y="52" font-size="12" fill="#e53935" font-weight="bold">z₁ (π/3)</text>
  <circle cx="117.5" cy="56.4" r="4" fill="#e53935"/>
  <text x="58" y="52" font-size="12" fill="#e53935" font-weight="bold">z₂ (2π/3)</text>
  <circle cx="75" cy="130" r="4" fill="#e53935"/>
  <text x="36" y="124" font-size="12" fill="#e53935" font-weight="bold">z₃ = -1</text>
  <circle cx="117.5" cy="203.6" r="4" fill="#e53935"/>
  <text x="58" y="218" font-size="12" fill="#e53935" font-weight="bold">z₄ (4π/3)</text>
  <circle cx="202.5" cy="203.6" r="4" fill="#e53935"/>
  <text x="208" y="218" font-size="12" fill="#e53935" font-weight="bold">z₅ (5π/3)</text>
</svg>

- **【分步标准解答】**
  $z = 0$ は解ではないから、$z = r(\cos\theta + i\sin\theta)$（$r > 0,\ 0 \le \theta < 2\pi$）とおく。
  ド・モアブルの定理より、
  $$z^6 = r^6(\cos 6\theta + i\sin 6\theta)$$
  また、$1 = 1 \cdot (\cos 0 + i\sin 0)$ であるから、$z^6 = 1$ は
  $$r^6(\cos 6\theta + i\sin 6\theta) = 1 \cdot (\cos 0 + i\sin 0)$$
  両辺の絶対値と偏角を比較すると、
  $$r^6 = 1,\qquad 6\theta = 0 + 2k\pi \quad (k \text{ は整数})$$
  $r > 0$ より $r = 1$。また、$\theta = \dfrac{k\pi}{3}$ である。
  $0 \le \theta < 2\pi$ より $0 \le \dfrac{k\pi}{3} < 2\pi \implies 0 \le k < 6$ となるから、$k = 0, 1, 2, 3, 4, 5$。
  > 💡 讲师批注：解复数方程 $z^n = \alpha$ 时，**千万不要漏写 $+ 2k\pi$（$k$ 为整数）**！如果直接写 $6\theta = 0 \implies \theta = 0$，就会漏掉其余 5 个复数根！

  それぞれの $k$ に対して $z = \cos\dfrac{k\pi}{3} + i\sin\dfrac{k\pi}{3}$ を計算すると、
  - $k = 0$ のとき：$z = \cos 0 + i\sin 0 = 1$
  - $k = 1$ のとき：$z = \cos\dfrac{\pi}{3} + i\sin\dfrac{\pi}{3} = \dfrac{1 + \sqrt{3}i}{2}$
  - $k = 2$ のとき：$z = \cos\dfrac{2\pi}{3} + i\sin\dfrac{2\pi}{3} = \dfrac{-1 + \sqrt{3}i}{2}$
  - $k = 3$ のとき：$z = \cos\pi + i\sin\pi = -1$
  - $k = 4$ のとき：$z = \cos\dfrac{4\pi}{3} + i\sin\dfrac{4\pi}{3} = \dfrac{-1 - \sqrt{3}i}{2}$
  - $k = 5$ のとき：$z = \cos\dfrac{5\pi}{3} + i\sin\dfrac{5\pi}{3} = \dfrac{1 - \sqrt{3}i}{2}$
- **【最终答案】**
  **$z = \pm 1,\quad \dfrac{1 \pm \sqrt{3}i}{2},\quad \dfrac{-1 \pm \sqrt{3}i}{2}$**

---

#### 演習問題 4-(5)
- **【原题重现与翻译】**
  - 原题：方程式 $z^4 = -8 + 8\sqrt{3}i$ を解け。
  - 中文：解方程 $z^4 = -8 + 8\sqrt{3}i$。
- **【考点定位】**
  - 一般复数方程 $z^n = \alpha$ 的极形式求解（4 个根构成圆心在原点、半径为 $2$ 的内接正方形）。
- **【图解辅助（SVG 矢量图）】**

<svg viewBox="0 0 320 260" width="320" height="260" xmlns="http://www.w3.org/2000/svg" style="background:#fafafa;border:1px solid #e0e0e0;border-radius:6px;">
  <defs>
    <marker id="arr6" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto">
      <path d="M0,0 L0,6 L7,3 z" fill="#333"/>
    </marker>
  </defs>
  <!-- 圆心 O(160, 130), 半径 R=80 (代表r=2) -->
  <line x1="35" y1="130" x2="290" y2="130" stroke="#333" stroke-width="1.3" marker-end="url(#arr6)"/>
  <line x1="160" y1="245" x2="160" y2="15" stroke="#333" stroke-width="1.3" marker-end="url(#arr6)"/>
  <text x="293" y="134" font-size="12" fill="#333">実軸</text>
  <text x="166" y="22" font-size="12" fill="#333">虚軸</text>
  <text x="146" y="144" font-size="12" fill="#333">O</text>
  <!-- 半径 r=2 的圆 -->
  <circle cx="160" cy="130" r="80" fill="none" stroke="#ce93d8" stroke-width="1.5" stroke-dasharray="4,3"/>
  <!-- 4个根: 30°(229.3, 90), 120°(120, 60.7), 210°(90.7, 170), 300°(200, 199.3) -->
  <polygon points="229.3,90 120,60.7 90.7,170 200,199.3" fill="#f3e5f5" fill-opacity="0.55" stroke="#7b1fa2" stroke-width="2"/>
  <line x1="160" y1="130" x2="229.3" y2="90" stroke="#7b1fa2" stroke-width="1.2" stroke-dasharray="3,2"/>
  <text x="182" y="124" font-size="11" fill="#7b1fa2">π/6</text>
  <circle cx="229.3" cy="90" r="4" fill="#e53935"/>
  <text x="236" y="88" font-size="12" fill="#e53935" font-weight="bold">√3 + i</text>
  <circle cx="120" cy="60.7" r="4" fill="#e53935"/>
  <text x="48" y="56" font-size="12" fill="#e53935" font-weight="bold">-1 + √3i</text>
  <circle cx="90.7" cy="170" r="4" fill="#e53935"/>
  <text x="24" y="176" font-size="12" fill="#e53935" font-weight="bold">-√3 - i</text>
  <circle cx="200" cy="199.3" r="4" fill="#e53935"/>
  <text x="206" y="210" font-size="12" fill="#e53935" font-weight="bold">1 - √3i</text>
</svg>

- **【分步标准解答】**
  $z = r(\cos\theta + i\sin\theta)$（$r > 0,\ 0 \le \theta < 2\pi$）とおく。
  右辺を極形式で表すと、$|-8 + 8\sqrt{3}i| = 8\sqrt{(-1)^2 + (\sqrt{3})^2} = 16$ より、
  $$-8 + 8\sqrt{3}i = 16\left(-\frac{1}{2} + \frac{\sqrt{3}}{2}i\right) = 16\left(\cos\frac{2}{3}\pi + i\sin\frac{2}{3}\pi\right)$$
  ド・モアブルの定理より、方程式は
  $$r^4(\cos 4\theta + i\sin 4\theta) = 16\left(\cos\frac{2}{3}\pi + i\sin\frac{2}{3}\pi\right)$$
  両辺の絶対値と偏角を比較すると、
  $$r^4 = 16,\qquad 4\theta = \frac{2}{3}\pi + 2k\pi \quad (k \text{ は整数})$$
  $r > 0$ より $r = 2$。また、$\theta = \dfrac{\pi}{6} + \dfrac{k\pi}{2}$ である。
  $0 \le \theta < 2\pi$ より、$k = 0, 1, 2, 3$ である。
  - $k = 0$ のとき：$\theta = \dfrac{\pi}{6} \implies z = 2\left(\cos\dfrac{\pi}{6} + i\sin\dfrac{\pi}{6}\right) = 2\left(\dfrac{\sqrt{3}}{2} + \dfrac{1}{2}i\right) = \sqrt{3} + i$
  - $k = 1$ のとき：$\theta = \dfrac{2}{3}\pi \implies z = 2\left(\cos\dfrac{2}{3}\pi + i\sin\dfrac{2}{3}\pi\right) = 2\left(-\dfrac{1}{2} + \dfrac{\sqrt{3}}{2}i\right) = -1 + \sqrt{3}i$
  - $k = 2$ のとき：$\theta = \dfrac{7}{6}\pi \implies z = 2\left(\cos\dfrac{7}{6}\pi + i\sin\dfrac{7}{6}\pi\right) = 2\left(-\dfrac{\sqrt{3}}{2} - \dfrac{1}{2}i\right) = -\sqrt{3} - i$
  - $k = 3$ のとき：$\theta = \dfrac{5}{3}\pi \implies z = 2\left(\cos\dfrac{5}{3}\pi + i\sin\dfrac{5}{3}\pi\right) = 2\left(\dfrac{1}{2} - \dfrac{\sqrt{3}}{2}i\right) = 1 - \sqrt{3}i$
  > 💡 讲师批注：求得 $k=0$ 的特解 $z_0 = \sqrt{3} + i$ 后，其余 3 个根只需依次乘以 $i$（绕原点逆时针旋转 $\dfrac{\pi}{2}$）：$(\sqrt{3}+i) \xrightarrow{\times i} (-1+\sqrt{3}i) \xrightarrow{\times i} (-\sqrt{3}-i) \xrightarrow{\times i} (1-\sqrt{3}i)$，既快又零失误！

- **【最终答案】**
  **$z = \sqrt{3} + i,\quad -1 + \sqrt{3}i,\quad -\sqrt{3} - i,\quad 1 - \sqrt{3}i$**

---

### 第十章 演習問題 1（等差数列・調和数列・P255）

#### 演習問題 1-(1)
- **【原题重现与翻译】**
  - 原题：一般項が $a_n = -3n + 7$ である数列 $\{a_n\}$ について
    - [1] 数列 $\{a_n\}$ は等差数列であることを証明し、その初項と公差を求めよ。
    - [2] 一般項が $c_n = a_{3n}$ である数列 $\{c_n\}$ は等差数列であることを証明し、その初項と公差を求めよ。
  - 中文：对于通项为 $a_n = -3n + 7$ 的数列 $\{a_n\}$：
    - [1] 证明数列 $\{a_n\}$ 是等差数列，并求其初项与公差。
    - [2] 证明通项为 $c_n = a_{3n}$ 的数列 $\{c_n\}$ 是等差数列，并求其初项与公差。
- **【考点定位】**
  - 等差数列的定义证明（$a_{n+1} - a_n = \text{定数}$）；等差数列的等距抽取子列性质。
- **【分步标准解答】**
  - **[1]** すべての自然数 $n$ に対して、
    $$a_{n+1} - a_n = \{-3(n + 1) + 7\} - (-3n + 7) = (-3n + 4) - (-3n + 7) = -3$$
    これは $n$ によらない一定の値であるから、数列 $\{a_n\}$ は公差 $-3$ の等差数列である。
    > 💡 讲师批注：证明等差数列的**唯一标准写法**：计算 $a_{n+1} - a_n$ 并指出结果是「与 $n$ 无关的常数（$n$ によらない一定値）」。

    また、初項は $a_1 = -3 \cdot 1 + 7 = 4$ である。

  - **[2]** $c_n = a_{3n} = -3(3n) + 7 = -9n + 7$ であるから、すべての自然数 $n$ に対して、
    $$c_{n+1} - c_n = \{-9(n + 1) + 7\} - (-9n + 7) = (-9n - 2) - (-9n + 7) = -9$$
    これは $n$ によらない一定の値であるから、数列 $\{c_n\}$ は公差 $-9$ の等差数列である。
    また、初項は $c_1 = a_3 = -9 \cdot 1 + 7 = -2$ である。
    > 💡 讲师批注：直观理解：$\{c_n\}$ 抽取的是原数列的第 $3, 6, 9, \dots$ 项，每步跨度为原公差的 $3$ 倍，即 $3 \times (-3) = -9$，首项为 $a_3 = -2$！

- **【最终答案】**
  - **[1] 証明完了。初項 $4$，公差 $-3$**
  - **[2] 証明完了。初項 $-2$，公差 $-9$**

---

#### 演習問題 1-(2)
- **【原题重现与翻译】**
  - 原题：等差数列をなす 3 数があって、その和は $27$、積は $693$ である。この 3 数を求めよ。
  - 中文：有成等差数列的 3 个数，它们的和是 $27$，积是 $693$。求这 3 个数。
- **【考点定位】**
  - 三个数成等差数列的对称设法（$a - d,\ a,\ a + d$）简化方程计算。
- **【分步标准解答】**
  求める 3 数を $a - d,\ a,\ a + d$ とおく。
  > 💡 讲师批注：若设成 $a,\ a+d,\ a+2d$ 也能解，但对称设成 $a-d,\ a,\ a+d$ 时，求和会直接消去 $d$，求积会出现平方差 $(a-d)(a+d) = a^2 - d^2$，计算量减半！

  和が $27$ であるから、
  $$(a - d) + a + (a + d) = 27 \implies 3a = 27 \implies a = 9$$
  積が $693$ であるから、$a = 9$ を代入して、
  $$(9 - d) \cdot 9 \cdot (9 + d) = 693$$
  両辺を $9$ で割ると、
  $$(9 - d)(9 + d) = 77 \implies 81 - d^2 = 77 \implies d^2 = 4 \implies d = \pm 2$$
  - $d = 2$ のとき、3 数は $7,\ 9,\ 11$。
  - $d = -2$ のとき、3 数は $11,\ 9,\ 7$。
  いずれの場合も求める 3 数は $7,\ 9,\ 11$ である。
  > 💡 讲师批注：验算：$7 + 9 + 11 = 27$，$7 \times 9 \times 11 = 63 \times 11 = 693$，完全正确！

- **【最终答案】**
  **$7,\ 9,\ 11$**

---

#### 演習問題 1-(3)
- **【原题重现与翻译】**
  - 原题（教材原文）：調和数列 $20, 15, 10, \dots$ の一般項 $a_n$ を求めよ。
  - 中文（教材原文）：求调和数列 $20, 15, 10, \dots$ 的通项 $a_n$。
  > ⚠️ **教材勘误提示**：经核对原书第 254 页（`page_0255.jpg`），原教材此处存在**明显印刷错误**！检验各项倒数：
  > $$\frac{1}{20} = \frac{3}{60}, \qquad \frac{1}{15} = \frac{4}{60}, \qquad \frac{1}{10} = \frac{6}{60}$$
  > 可见 $\dfrac{1}{15} - \dfrac{1}{20} = \dfrac{1}{60}$，而 $\dfrac{1}{10} - \dfrac{1}{15} = \dfrac{2}{60} \neq \dfrac{1}{60}$，因此 $20, 15, 10$ 实际上是**等差数列**（公差 $-5$），绝非调和数列！
  > 正确原题应为经典调和数列：**$20,\ 15,\ 12,\ \dots$**（其倒数为 $\dfrac{3}{60},\ \dfrac{4}{60},\ \dfrac{5}{60},\ \dots$）。以下按勘误后的正确题目 $20,\ 15,\ 12,\ \dots$ 给出标准解答。
- **【考点定位】**
  - 调和数列的定义与通项求法（取倒数转化为等差数列）。
- **【图解辅助（SVG 矢量图）】**

<svg viewBox="0 0 420 135" width="420" height="135" xmlns="http://www.w3.org/2000/svg" style="background:#fafafa;border:1px solid #e0e0e0;border-radius:6px;">
  <!-- 上排: 调和数列 a_n -->
  <text x="14" y="34" font-size="13" fill="#1e88e5" font-weight="bold">調和数列 {aₙ}：</text>
  <rect x="115" y="16" width="46" height="26" rx="4" fill="#e3f2fd" stroke="#1e88e5"/>
  <text x="131" y="34" font-size="13" fill="#1565c0" font-weight="bold">20</text>
  <rect x="180" y="16" width="46" height="26" rx="4" fill="#e3f2fd" stroke="#1e88e5"/>
  <text x="196" y="34" font-size="13" fill="#1565c0" font-weight="bold">15</text>
  <rect x="245" y="16" width="46" height="26" rx="4" fill="#e3f2fd" stroke="#1e88e5"/>
  <text x="261" y="34" font-size="13" fill="#1565c0" font-weight="bold">12</text>
  <text x="303" y="34" font-size="14" fill="#555">…</text>
  <rect x="328" y="16" width="76" height="26" rx="4" fill="#bbdefb" stroke="#1565c0" stroke-width="1.5"/>
  <text x="339" y="34" font-size="12.5" fill="#0d47a1" font-weight="bold">60 / (n+2)</text>
  <!-- 双向取倒数箭头 -->
  <text x="128" y="67" font-size="12" fill="#e53935">↕ 逆数</text>
  <text x="193" y="67" font-size="12" fill="#e53935">↕</text>
  <text x="258" y="67" font-size="12" fill="#e53935">↕</text>
  <text x="348" y="67" font-size="12" fill="#e53935">↑ 逆数还原</text>
  <!-- 下排: 等差数列 1/a_n -->
  <text x="14" y="102" font-size="13" fill="#2e7d32" font-weight="bold">等差数列 {1/aₙ}：</text>
  <rect x="115" y="84" width="46" height="26" rx="4" fill="#e8f5e9" stroke="#2e7d32"/>
  <text x="125" y="102" font-size="12.5" fill="#1b5e20" font-weight="bold">3/60</text>
  <rect x="180" y="84" width="46" height="26" rx="4" fill="#e8f5e9" stroke="#2e7d32"/>
  <text x="190" y="102" font-size="12.5" fill="#1b5e20" font-weight="bold">4/60</text>
  <rect x="245" y="84" width="46" height="26" rx="4" fill="#e8f5e9" stroke="#2e7d32"/>
  <text x="255" y="102" font-size="12.5" fill="#1b5e20" font-weight="bold">5/60</text>
  <text x="303" y="102" font-size="14" fill="#555">…</text>
  <rect x="328" y="84" width="76" height="26" rx="4" fill="#c8e6c9" stroke="#2e7d32" stroke-width="1.5"/>
  <text x="339" y="102" font-size="12.5" fill="#1b5e20" font-weight="bold">(n+2) / 60</text>
  <!-- 公差标注 -->
  <text x="158" y="126" font-size="11.5" fill="#2e7d32">+1/60</text>
  <text x="223" y="126" font-size="11.5" fill="#2e7d32">+1/60</text>
</svg>

- **【分步标准解答】**（按勘误后的正确数列 $20,\ 15,\ 12,\ \dots$）
  数列 $\{a_n\}$ は調和数列であるから、各項の逆数をとった数列 $\left\{\dfrac{1}{a_n}\right\}$ は等差数列である。
  $$b_n = \frac{1}{a_n}$$
  とおくと、数列 $\{b_n\}$ は
  $$\frac{1}{20},\quad \frac{1}{15},\quad \frac{1}{12},\quad \dots$$
  すなわち、初項 $b_1 = \dfrac{1}{20} = \dfrac{3}{60}$、公差 $d = \dfrac{1}{15} - \dfrac{1}{20} = \dfrac{4 - 3}{60} = \dfrac{1}{60}$ の等差数列である。
  よって、
  $$b_n = \frac{3}{60} + (n - 1)\cdot\frac{1}{60} = \frac{n + 2}{60}$$
  したがって、求める一般項 $a_n$ は
  $$a_n = \frac{1}{b_n} = \frac{60}{n + 2}$$
  > 💡 讲师批注：代入验算：$n=1 \implies \dfrac{60}{3} = 20$，$n=2 \implies \dfrac{60}{4} = 15$，$n=3 \implies \dfrac{60}{5} = 12$，完全吻合！

- **【最终答案】**
  **$a_n = \dfrac{60}{n + 2}$**（原题第 3 项勘误为 $12$ 后）

---

#### 演習問題 1-(4)
- **【原题重现与翻译】**
  - 原题：初項が $a$、第 2 項が $b$ である調和数列がある。この数列の第 $n$ 項 $a_n$ を $a, b$ で表せ。
  - 中文：有一个初项为 $a$、第 2 项为 $b$ 的调和数列。用 $a, b$ 表示该数列的第 $n$ 项 $a_n$。
- **【考点定位】**
  - 含参数调和数列的通项公式推导。
- **【分步标准解答】**
  調和数列の定義より、すべての項は $0$ でないから $a \neq 0,\ b \neq 0$ である。
  $c_n = \dfrac{1}{a_n}$ とおくと、数列 $\{c_n\}$ は初項 $c_1 = \dfrac{1}{a}$、第 2 項 $c_2 = \dfrac{1}{b}$ の等差数列である。
  その公差 $d$ は、
  $$d = c_2 - c_1 = \frac{1}{b} - \frac{1}{a} = \frac{a - b}{ab}$$
  よって、等差数列 $\{c_n\}$ の一般項は、
  $$c_n = \frac{1}{a} + (n - 1)\left(\frac{a - b}{ab}\right) = \frac{b + (n - 1)(a - b)}{ab}$$
  $$= \frac{b + (n - 1)a - (n - 1)b}{ab} = \frac{(n - 1)a - (n - 2)b}{ab}$$
  > 💡 讲师批注：通分整理后，务必用 $n=1$ 和 $n=2$ 做特值验算！
  > - $n = 1$：分子 $= 0 \cdot a - (-1)b = b \implies c_1 = \dfrac{b}{ab} = \dfrac{1}{a} \implies a_1 = a$；
  > - $n = 2$：分子 $= 1 \cdot a - 0 \cdot b = a \implies c_2 = \dfrac{a}{ab} = \dfrac{1}{b} \implies a_2 = b$；
  > - 再代入上题 $a=20, b=15$：$a_n = \dfrac{300}{20(n-1) - 15(n-2)} = \dfrac{300}{5n + 10} = \dfrac{60}{n+2}$，完美验证！

  調和数列であるから $c_n \neq 0$ すなわち $(n - 1)a - (n - 2)b \neq 0$ であり、逆数をとると、
  $$a_n = \frac{1}{c_n} = \frac{ab}{(n - 1)a - (n - 2)b}$$
- **【最终答案】**
  **$a_n = \dfrac{ab}{(n - 1)a - (n - 2)b}$**（亦写作 $\dfrac{ab}{(a - b)n + (2b - a)}$）
