# 《EJU 教材全解与备课讲义》数学 009-A（P121–P129）

> **对应源文件**：`work_math/ocr_md/ocr_009_p121-135.md`（本切片内容丰富，拆分为 `note_009_a.md` 与 `note_009_b.md` 两册完整输出；本册覆盖 P121–P129「三角関数のグラフと性質」「三角関数の応用」及演習問題 2・3）
> **视觉核对参考图**：`work_math/ref_imgs/page_0121.jpg` – `page_0129.jpg`

---

## 一、国内高中基础知识点唤醒与 EJU 考纲差异对比

本切片（P121–P135）对应日本高中 **数学Ⅱ《三角関数》** 的核心主干内容，涵盖 **诱导公式与图像变换、奇偶性与周期性、三角方程与三角不等式、三角函数最值与含参解的个数讨论、加法定理、二倍角/半角/三倍角公式、两直线夹角公式** 七大高频考点。

### 1.1 三角函数的诱导公式（三角関数の性質）

借助**单位圆（単位円）**上动径（終辺）的对称与旋转关系，记住以下 4 组基本性质（$n$ 为整数）：

1. **周期性（$\theta + 2n\pi$）**：
   $$\sin(\theta + 2n\pi) = \sin\theta, \qquad \cos(\theta + 2n\pi) = \cos\theta, \qquad \tan(\theta + 2n\pi) = \tan\theta$$
2. **负角（$-\theta$，关于 $x$ 轴对称）**：
   $$\sin(-\theta) = -\sin\theta, \qquad \cos(-\theta) = \cos\theta, \qquad \tan(-\theta) = -\tan\theta$$
3. **半周旋转（$\theta + \pi$，关于原点对称）与补角（$\pi - \theta$）**：
   $$\sin(\theta + \pi) = -\sin\theta, \qquad \cos(\theta + \pi) = -\cos\theta, \qquad \tan(\theta + \pi) = \tan\theta$$
   $$\sin(\pi - \theta) = \sin\theta, \qquad \cos(\pi - \theta) = -\cos\theta, \qquad \tan(\pi - \theta) = -\tan\theta$$
4. **直角旋转（$\theta + \frac{\pi}{2}$）与余角（$\frac{\pi}{2} - \theta$）**：
   $$\sin\left(\theta + \frac{\pi}{2}\right) = \cos\theta, \qquad \cos\left(\theta + \frac{\pi}{2}\right) = -\sin\theta, \qquad \tan\left(\theta + \frac{\pi}{2}\right) = -\frac{1}{\tan\theta}$$
   $$\sin\left(\frac{\pi}{2} - \theta\right) = \cos\theta, \qquad \cos\left(\frac{\pi}{2} - \theta\right) = \sin\theta, \qquad \tan\left(\frac{\pi}{2} - \theta\right) = \frac{1}{\tan\theta}$$

### 1.2 三角函数的图像、奇偶性、周期与图像变换

- **三大基本图像**：
  - $y = \sin\theta$（正弦曲線）：定义域 $\mathbb{R}$，值域 $[-1, 1]$，奇函数（原点对称），周期 $2\pi$。
  - $y = \cos\theta$（正弦曲線）：定义域 $\mathbb{R}$，值域 $[-1, 1]$，偶函数（$y$ 轴对称），周期 $2\pi$。
  - $y = \tan\theta$（正接曲線）：定义域 $\theta \neq \frac{\pi}{2} + n\pi$（$n \in \mathbb{Z}$），值域 $\mathbb{R}$，奇函数（原点对称），周期 $\pi$，渐近线 $\theta = \frac{\pi}{2} + n\pi$。
- **一般图像变换规则**（以 $y = f(x)$ 为基准）：
  - $y = f(x - p) + q$：沿 $x$ 轴方向平移 $p$，沿 $y$ 轴方向平移 $q$。
  - $y = a f(x)$：沿 $y$ 轴方向扩大（或缩小）为 $|a|$ 倍（若 $a < 0$，还需关于 $x$ 轴对称翻转）。
  - $y = f(kx)$：沿 **$x$ 轴方向**扩大（或缩小）为 $\dfrac{1}{|k|}$ 倍。
  > ⚠️ **教材勘误提示**：原教材第 121 页（`page_0122.jpg`）`[3.7]` 中将 $y = f(kx)$ 的变换误印为「$y$ 軸方向に $\frac{1}{|k|}$ 倍に拡大または縮小」，正确应为 **$x$ 軸方向（横轴方向）に $\dfrac{1}{|k|}$ 倍に拡大または縮小**！
- **周期公式**：
  - $y = \sin(k\theta + \alpha),\; y = \cos(k\theta + \alpha)$ 的周期为 $\dfrac{2\pi}{|k|}$；
  - $y = \tan(k\theta + \alpha)$ 的周期为 $\dfrac{\pi}{|k|}$。

### 1.3 三角方程、三角不等式与一般解

借助单位圆（$0 \le \theta < 2\pi$）确定基本解，再叠加周期得**一般解（一般解）**（$n$ 为整数）：
- $\sin\theta = a$（$-1 \le a \le 1$）：若特解为 $\alpha$，则一般解为 $\theta = \alpha + 2n\pi,\; (\pi - \alpha) + 2n\pi$。
- $\cos\theta = a$（$-1 \le a \le 1$）：若特解为 $\alpha$，则一般解为 $\theta = \pm\alpha + 2n\pi$。
- $\tan\theta = a$：若特解为 $\alpha$，则一般解为 $\theta = \alpha + n\pi$。
- **解三角不等式两步法**：① 先解对应三角方程定出边界动径；② 在单位圆上标出满足条件的弧段，按逆时针（角增大方向）写出 $\theta$ 区间。

### 1.4 加法定理、倍角/半角/三倍角公式与两直线夹角（详题见 `note_009_b.md`）

1. **加法定理（加法定理）**：
   $$\sin(\alpha \pm \beta) = \sin\alpha\cos\beta \pm \cos\alpha\sin\beta$$
   $$\cos(\alpha \pm \beta) = \cos\alpha\cos\beta \mp \sin\alpha\sin\beta$$
   $$\tan(\alpha \pm \beta) = \frac{\tan\alpha \pm \tan\beta}{1 \mp \tan\alpha\tan\beta}$$
2. **2 倍角公式**：
   $$\sin 2\alpha = 2\sin\alpha\cos\alpha, \qquad \cos 2\alpha = \cos^2\alpha - \sin^2\alpha = 1 - 2\sin^2\alpha = 2\cos^2\alpha - 1, \qquad \tan 2\alpha = \frac{2\tan\alpha}{1 - \tan^2\alpha}$$
3. **半角公式**：
   $$\sin^2\frac{\alpha}{2} = \frac{1 - \cos\alpha}{2}, \qquad \cos^2\frac{\alpha}{2} = \frac{1 + \cos\alpha}{2}, \qquad \tan^2\frac{\alpha}{2} = \frac{1 - \cos\alpha}{1 + \cos\alpha}$$
4. **3 倍角公式**：
   $$\sin 3\alpha = 3\sin\alpha - 4\sin^3\alpha, \qquad \cos 3\alpha = 4\cos^3\alpha - 3\cos\alpha$$
5. **两直线的夹锐角公式（2 直線のなす角）**：
   两直线 $y = m_1 x + n_1$ 与 $y = m_2 x + n_2$ 不垂直（$m_1 m_2 \neq -1$）时，其所成锐角 $\theta$ 满足：
   $$\tan\theta = \left|\frac{m_1 - m_2}{1 + m_1 m_2}\right|$$

### 1.5 国内高中 vs. 日本 EJU 考纲差异与符号习惯

| 对比维度 | 国内高中习惯 | 日本 EJU 习惯 | 备课/应试提醒 |
| :--- | :--- | :--- | :--- |
| **$\cos\theta$ 图像名称** | 称「余弦曲线」 | 与 $\sin\theta$ 统称 **正弦曲線（せいげんきょくせん）** | 因为 $\cos\theta$ 只是 $\sin\theta$ 平移 $\frac{\pi}{2}$ 所得，日本教材统称正弦曲线 |
| **三角方程解的表示** | 常用 $2k\pi$（$k \in \mathbb{Z}$） | 统一用 **$2n\pi$（$n$ は整数）** | 规范作答时务必注明「$n$ は整数」 |
| **半角公式写法** | 常带 $\pm\sqrt{\cdots}$ 开方形式 | 教科书标准为**平方形式** $\sin^2\frac{\alpha}{2} = \frac{1-\cos\alpha}{2}$ | 避免盲目写正负号，先算平方再由 $\frac{\alpha}{2}$ 所在象限定符号 |
| **三倍角公式** | 高考不作硬性记忆要求 | **EJU / 日本国公立二次考高频工具** | 记忆口诀：$\sin 3\alpha$「三心四立方」，$\cos 3\alpha$「四立方减三余」 |
| **两直线夹角公式** | 新课标多用向量点积 $\cos\theta$ | 数学Ⅱ标准考法为 **$\tan\theta = \left\|\frac{m_1-m_2}{1+m_1m_2}\right\|$** | 用斜率求夹角更快，可用法向量点积作交叉验算 |
| **诱导公式记忆** | 「奇变偶不变，符号看象限」 | 多借助**单位圆对称性**直接推导 | 两种方法相辅相成，考试时用口诀速算、用单位圆复核 |

---

## 二、日文核心词汇与公式假名注音

### 2.1 本切片日文核心词汇

- 三角関数（さんかくかんすう / sankaku kansuu） — 三角函数
- 正弦曲線（せいげんきょくせん / seigen kyokusen） — 正弦曲线
- 正接曲線（せいせつきょくせん / seisetsu kyokusen） — 正切曲线
- 単位円（たんいえん / tan'ien） — 单位圆
- 動径（どうけい / doukei） — 动径（角的终边射线）
- 奇関数（きかんすう / kikansuu） — 奇函数
- 偶関数（ぐうかんすう / guukansuu） — 偶函数
- 拡大（かくだい / kakudai） — 扩大、拉伸
- 縮小（しゅくしょう / shukushou） — 缩小、压缩
- 周期（しゅうき / shuuki） — 周期
- 周期関数（しゅうきかんすう / shuuki kansuu） — 周期函数
- 三角方程式（さんかくほうていしき / sankaku houteishiki） — 三角方程
- 三角不等式（さんかくふとうしき / sankaku futoushiki） — 三角不等式
- 一般角（いっぱんかく / ippankaku） — 一般角（任意角）
- 一般解（いっぱんかい / ippankai） — 通解、一般解
- 加法定理（かほうていり / kahou teiri） — 加法定理（两角和与差公式）
- 2倍角の公式（にばいかくのこうしき / nibaikaku no koushiki） — 二倍角公式
- 半角の公式（はんかくのこうしき / hankaku no koushiki） — 半角公式
- 3倍角の公式（さんばいかくのこうしき / sanbaikaku no koushiki） — 三倍角公式
- なす角（なすかく / nasu kaku） — 夹角
- 鋭角（えいかく / eikaku） — 锐角
- 鈍角（どんかく / donkaku） — 钝角
- 垂直（すいちょく / suichoku） — 垂直
- 平行（へいこう / heikou） — 平行
- 余弦定理（よげんていり / yogen teiri） — 余弦定理
- 距離の公式（きょりのこうしき / kyori no koushiki） — 两点间距离公式

### 2.2 核心公式的日本课堂口语读法

1. **三角函数名与角 $\theta$**
   - $\sin\theta$：**サイン シータ**
   - $\cos\theta$：**コサイン シータ**
   - $\tan\theta$：**タンジェント シータ**
2. **加法定理** $\sin(\alpha + \beta) = \sin\alpha\cos\beta + \cos\alpha\sin\beta$
   - 课堂口诀读法：**咲いた コスモス、コスモス 咲いた（さいた こすもす、こすもす さいた）**
   - $\cos(\alpha + \beta) = \cos\alpha\cos\beta - \sin\alpha\sin\beta$ 口诀：**コスモス コスモス、咲いた 咲いた（符号逆転）**
3. **二倍角公式** $\sin 2\alpha = 2\sin\alpha\cos\alpha$
   - 课堂读法：**サイン にアルファ イコール に サイン アルファ コサイン アルファ**
4. **半角公式** $\sin^2\dfrac{\alpha}{2} = \dfrac{1 - \cos\alpha}{2}$
   - 课堂读法：**サイン にじょう にぶんのアルファ イコール にぶんの いち ひく コサイン アルファ**
5. **两直线夹锐角公式** $\tan\theta = \left|\dfrac{m_1 - m_2}{1 + m_1 m_2}\right|$
   - 课堂读法：**タンジェント シータ イコール ぜったいち、いち たす エムワン エムツー ぶんの エムワン ひく エムツー**

---

## 三、逐题深度解析（上：演習問題 2・演習問題 3）

### 演習問題 2（P124）

#### 演習問題 2 (1)

**【原题重现与翻译】**
> **日文原题**：関数 $y = \sin\theta$ のグラフをもとに、次の関数のグラフを描け、周期を求めよ。
> `[1]` $y = \sin\left(\theta - \dfrac{\pi}{2}\right)$
> `[2]` $y = \dfrac{1}{2}\sin\theta$
> `[3]` $y = \sin\dfrac{\theta}{2}$
> `[4]` $y = 2\cos\left(\dfrac{\theta}{2} - \dfrac{\pi}{6}\right)$
>
> **中文翻译**：以函数 $y = \sin\theta$ 的图像为基础，画出下列函数的图像，并求其周期。

**【考点定位】**
三角函数图像变换（平移变换、纵横伸缩变换）与周期公式 $T = \dfrac{2\pi}{|k|}$。

**【图解辅助（SVG 矢量图）】**

<svg viewBox="0 0 760 440" width="100%" xmlns="http://www.w3.org/2000/svg" style="background:#fafafa;border:1px solid #e0e0e0;border-radius:8px;margin:8px 0;">
  <!-- Top-left: [1] y = sin(θ - π/2) -->
  <g transform="translate(10,10)">
    <rect x="0" y="0" width="365" height="205" fill="#ffffff" stroke="#e5e7eb" rx="6"/>
    <text x="12" y="22" font-size="13" font-weight="bold" fill="#1f2937">[1] y = sin(θ - π/2)（周期 2π）</text>
    <!-- axes -->
    <line x1="25" y1="115" x2="345" y2="115" stroke="#6b7280" stroke-width="1.2"/>
    <line x1="90" y1="35" x2="90" y2="190" stroke="#6b7280" stroke-width="1.2"/>
    <text x="348" y="119" font-size="11" fill="#374151">θ</text>
    <text x="94" y="42" font-size="11" fill="#374151">y</text>
    <text x="77" y="128" font-size="10" fill="#374151">O</text>
    <text x="74" y="69" font-size="10" fill="#374151">1</text>
    <text x="69" y="169" font-size="10" fill="#374151">-1</text>
    <line x1="87" y1="65" x2="93" y2="65" stroke="#6b7280"/>
    <line x1="87" y1="165" x2="93" y2="165" stroke="#6b7280"/>
    <!-- ticks: π/2 = 45px -->
    <text x="130" y="130" font-size="10" fill="#374151">π/2</text>
    <text x="177" y="130" font-size="10" fill="#374151">π</text>
    <text x="218" y="130" font-size="10" fill="#374151">3π/2</text>
    <text x="266" y="130" font-size="10" fill="#374151">2π</text>
    <!-- reference y=sinθ (dashed) -->
    <path d="M 45,165 C 60,165 75,115 90,115 C 105,115 120,65 135,65 C 150,65 165,115 180,115 C 195,115 210,165 225,165 C 240,165 255,115 270,115 C 285,115 300,65 315,65" fill="none" stroke="#9ca3af" stroke-width="1.3" stroke-dasharray="4,3"/>
    <!-- target y=sin(θ-π/2) = -cosθ -->
    <path d="M 45,115 C 60,115 75,165 90,165 C 105,165 120,115 135,115 C 150,115 165,65 180,65 C 195,65 210,115 225,115 C 240,115 255,165 270,165 C 285,165 300,115 315,115" fill="none" stroke="#2563eb" stroke-width="2.2"/>
    <circle cx="90" cy="165" r="3" fill="#2563eb"/>
    <circle cx="135" cy="115" r="3" fill="#2563eb"/>
    <circle cx="180" cy="65" r="3" fill="#2563eb"/>
    <circle cx="270" cy="165" r="3" fill="#2563eb"/>
    <text x="268" y="55" font-size="10" fill="#9ca3af">--- y=sinθ</text>
  </g>

  <!-- Top-right: [2] y = (1/2)sinθ -->
  <g transform="translate(385,10)">
    <rect x="0" y="0" width="365" height="205" fill="#ffffff" stroke="#e5e7eb" rx="6"/>
    <text x="12" y="22" font-size="13" font-weight="bold" fill="#1f2937">[2] y = (1/2)sinθ（周期 2π）</text>
    <line x1="25" y1="115" x2="345" y2="115" stroke="#6b7280" stroke-width="1.2"/>
    <line x1="90" y1="35" x2="90" y2="190" stroke="#6b7280" stroke-width="1.2"/>
    <text x="348" y="119" font-size="11" fill="#374151">θ</text>
    <text x="94" y="42" font-size="11" fill="#374151">y</text>
    <text x="77" y="128" font-size="10" fill="#374151">O</text>
    <text x="74" y="69" font-size="10" fill="#9ca3af">1</text>
    <text x="64" y="94" font-size="10" fill="#dc2626">1/2</text>
    <text x="58" y="144" font-size="10" fill="#dc2626">-1/2</text>
    <text x="69" y="169" font-size="10" fill="#9ca3af">-1</text>
    <text x="130" y="130" font-size="10" fill="#374151">π/2</text>
    <text x="177" y="130" font-size="10" fill="#374151">π</text>
    <text x="218" y="130" font-size="10" fill="#374151">3π/2</text>
    <text x="266" y="130" font-size="10" fill="#374151">2π</text>
    <!-- y=sinθ dashed -->
    <path d="M 45,165 C 60,165 75,115 90,115 C 105,115 120,65 135,65 C 150,65 165,115 180,115 C 195,115 210,165 225,165 C 240,165 255,115 270,115 C 285,115 300,65 315,65" fill="none" stroke="#9ca3af" stroke-width="1.3" stroke-dasharray="4,3"/>
    <!-- y=(1/2)sinθ -->
    <path d="M 45,140 C 60,140 75,115 90,115 C 105,115 120,90 135,90 C 150,90 165,115 180,115 C 195,115 210,140 225,140 C 240,140 255,115 270,115 C 285,115 300,90 315,90" fill="none" stroke="#dc2626" stroke-width="2.2"/>
    <circle cx="135" cy="90" r="3" fill="#dc2626"/>
    <circle cx="225" cy="140" r="3" fill="#dc2626"/>
  </g>

  <!-- Bottom-left: [3] y = sin(θ/2) -->
  <g transform="translate(10,225)">
    <rect x="0" y="0" width="365" height="205" fill="#ffffff" stroke="#e5e7eb" rx="6"/>
    <text x="12" y="22" font-size="13" font-weight="bold" fill="#1f2937">[3] y = sin(θ/2)（周期 4π）</text>
    <line x1="25" y1="115" x2="345" y2="115" stroke="#6b7280" stroke-width="1.2"/>
    <line x1="75" y1="35" x2="75" y2="190" stroke="#6b7280" stroke-width="1.2"/>
    <text x="348" y="119" font-size="11" fill="#374151">θ</text>
    <text x="79" y="42" font-size="11" fill="#374151">y</text>
    <text x="62" y="128" font-size="10" fill="#374151">O</text>
    <text x="60" y="69" font-size="10" fill="#374151">1</text>
    <text x="55" y="169" font-size="10" fill="#374151">-1</text>
    <!-- π = 60px -->
    <text x="131" y="130" font-size="10" fill="#374151">π</text>
    <text x="190" y="130" font-size="10" fill="#374151">2π</text>
    <text x="250" y="130" font-size="10" fill="#374151">3π</text>
    <text x="310" y="130" font-size="10" fill="#374151">4π</text>
    <!-- y=sinθ dashed (period 2π = 120px) -->
    <path d="M 75,115 C 85,115 95,65 105,65 C 115,65 125,115 135,115 C 145,115 155,165 165,165 C 175,165 185,115 195,115" fill="none" stroke="#9ca3af" stroke-width="1.2" stroke-dasharray="4,3"/>
    <!-- y=sin(θ/2) (period 4π = 240px) -->
    <path d="M 35,158 C 48,145 62,115 75,115 C 95,115 115,65 135,65 C 155,65 175,115 195,115 C 215,115 235,165 255,165 C 275,165 295,115 315,115" fill="none" stroke="#059669" stroke-width="2.2"/>
    <circle cx="135" cy="65" r="3" fill="#059669"/>
    <circle cx="195" cy="115" r="3" fill="#059669"/>
    <circle cx="255" cy="165" r="3" fill="#059669"/>
    <circle cx="315" cy="115" r="3" fill="#059669"/>
  </g>

  <!-- Bottom-right: [4] y = 2cos(θ/2 - π/6) -->
  <g transform="translate(385,225)">
    <rect x="0" y="0" width="365" height="205" fill="#ffffff" stroke="#e5e7eb" rx="6"/>
    <text x="12" y="22" font-size="13" font-weight="bold" fill="#1f2937">[4] y = 2cos(θ/2 - π/6)（周期 4π）</text>
    <line x1="25" y1="115" x2="345" y2="115" stroke="#6b7280" stroke-width="1.2"/>
    <line x1="65" y1="35" x2="65" y2="190" stroke="#6b7280" stroke-width="1.2"/>
    <text x="348" y="119" font-size="11" fill="#374151">θ</text>
    <text x="69" y="42" font-size="11" fill="#374151">y</text>
    <text x="52" y="128" font-size="10" fill="#374151">O</text>
    <text x="50" y="59" font-size="10" fill="#7c3aed">2</text>
    <text x="45" y="179" font-size="10" fill="#7c3aed">-2</text>
    <line x1="62" y1="55" x2="68" y2="55" stroke="#6b7280"/>
    <line x1="62" y1="175" x2="68" y2="175" stroke="#6b7280"/>
    <!-- π = 54px, so π/3 = 18px; key θ: π/3(83), 4π/3(137), 7π/3(191), 10π/3(245), 13π/3(299) -->
    <text x="76" y="130" font-size="9" fill="#374151">π/3</text>
    <text x="127" y="130" font-size="9" fill="#374151">4π/3</text>
    <text x="181" y="130" font-size="9" fill="#374151">7π/3</text>
    <text x="234" y="130" font-size="9" fill="#374151">10π/3</text>
    <text x="288" y="130" font-size="9" fill="#374151">13π/3</text>
    <!-- curve: max at x=83(y=55), 0 at x=137, min at x=191(y=175), 0 at x=245, max at x=299(y=55) -->
    <path d="M 35,98 C 52,70 68,55 83,55 C 101,55 119,115 137,115 C 155,115 173,175 191,175 C 209,175 227,115 245,115 C 263,115 281,55 299,55 C 312,55 322,72 332,90" fill="none" stroke="#7c3aed" stroke-width="2.2"/>
    <circle cx="83" cy="55" r="3" fill="#7c3aed"/>
    <circle cx="137" cy="115" r="3" fill="#7c3aed"/>
    <circle cx="191" cy="175" r="3" fill="#7c3aed"/>
    <circle cx="245" cy="115" r="3" fill="#7c3aed"/>
    <circle cx="299" cy="55" r="3" fill="#7c3aed"/>
    <text x="18" y="68" font-size="9" fill="#6b7280">(0, √3)</text>
  </g>
</svg>

**【分步标准解答】**

- **`[1]`** $y = \sin\left(\theta - \dfrac{\pi}{2}\right)$
  $y = \sin\theta$ のグラフを $\theta$ 軸方向に $\dfrac{\pi}{2}$ だけ平行移動したものである。
  周期は $2\pi$ である。
  > 💡 讲师批注：画图时找准 5 个关键点（五点法）：$(\frac{\pi}{2}, 0),\; (\pi, 1),\; (\frac{3\pi}{2}, 0),\; (2\pi, -1),\; (\frac{5\pi}{2}, 0)$，且当 $\theta = 0$ 时 $y = -1$。实际上该函数等价于 $y = -\cos\theta$。

- **`[2]`** $y = \dfrac{1}{2}\sin\theta$
  $y = \sin\theta$ のグラフを $y$ 軸方向に $\dfrac{1}{2}$ 倍に縮小したものである。
  周期は $2\pi$ である。
  > 💡 讲师批注：纵向伸缩只改变振幅（最大值为 $\frac{1}{2}$，最小值为 $-\frac{1}{2}$），**不改变**零点位置与周期。

- **`[3]`** $y = \sin\dfrac{\theta}{2}$
  $y = \sin\theta$ のグラフを $\theta$ 軸方向に $2$ 倍に拡大したものである。
  周期は $\dfrac{2\pi}{\frac{1}{2}} = 4\pi$ である。
  > 💡 讲师批注：横向伸缩口诀「系数变小，图像拉长；系数变大，图像压扁」。此处 $k = \frac{1}{2}$，故沿 $\theta$ 轴拉伸为 $2$ 倍，周期由 $2\pi$ 变为 $4\pi$。

- **`[4]`** $y = 2\cos\left(\dfrac{\theta}{2} - \dfrac{\pi}{6}\right)$
  式を変形すると、
  $$y = 2\cos\left\{\frac{1}{2}\left(\theta - \frac{\pi}{3}\right)\right\}$$
  これは、$y = \cos\theta$ のグラフを $\theta$ 軸方向に $2$ 倍、$y$ 軸方向に $2$ 倍に拡大し、さらに $\theta$ 軸方向に $\dfrac{\pi}{3}$ だけ平行移動したものである。
  （$y = \sin\theta$ を基準にする場合は、$\cos X = \sin\left(X + \dfrac{\pi}{2}\right)$ より $y = 2\sin\left(\dfrac{\theta}{2} + \dfrac{\pi}{3}\right) = 2\sin\left\{\dfrac{1}{2}\left(\theta + \dfrac{2}{3}\pi\right)\right\}$ と表せる。）
  周期は $\dfrac{2\pi}{\frac{1}{2}} = 4\pi$ である。
  > 💡 讲师批注：**最高频易错点！** 计算平移量前，必须先把 $\theta$ 的系数 $\frac{1}{2}$ 提取到括号外：$\frac{\theta}{2} - \frac{\pi}{6} = \frac{1}{2}\left(\theta - \frac{\pi}{3}\right)$，所以平移量是 $\frac{\pi}{3}$ 而**不是** $\frac{\pi}{6}$！验算：代入 $\theta = \frac{\pi}{3}$，括号内恰好为 $0$，$y = 2\cos 0 = 2$（达到最大值）。

**【最终答案】**
- **`[1]` 周期：$2\pi$（图像见上图）**
- **`[2]` 周期：$2\pi$（图像见上图）**
- **`[3]` 周期：$4\pi$（图像见上图）**
- **`[4]` 周期：$4\pi$（图像见上图）**

---

### 演習問題 3（P126–P129）

#### 演習問題 3 (1)（P126）

**【原题重现与翻译】**
> **日文原题**：$0 \le \theta < 2\pi$ のとき、次の方程式と不等式を解け。また、その一般解を求めよ。
> `[1]` $\cos\theta = -\dfrac{1}{2}$
> `[2]` $\tan\theta = -\dfrac{\sqrt{3}}{2}$
> `[3]` $\sin\theta < -\dfrac{\sqrt{3}}{2}$
> `[4]` $\dfrac{1}{2} \le \cos\theta \le -\dfrac{1}{\sqrt{2}}$
>
> **中文翻译**：当 $0 \le \theta < 2\pi$ 时，解下列方程与不等式，并求其一般解（通解）。

> ⚠️ **教材勘误提示**：核对原书 `page_0126.jpg`，本题 `[2]` 与 `[4]` 存在明显印刷错误：
> - **`[2]`** 原印 $\tan\theta = -\dfrac{\sqrt{3}}{2}$ 并非特殊角，极大概率是将 $\tan\theta = -\dfrac{\sqrt{3}}{3}\left(= -\dfrac{1}{\sqrt{3}}\right)$ 的分母 `3` 误印为 `2`；
> - **`[4]`** 原印 $\dfrac{1}{2} \le \cos\theta \le -\dfrac{1}{\sqrt{2}}$ 中左端 $\dfrac{1}{2} > -\dfrac{1}{\sqrt{2}}$，按字面意思无解，显然是将左右端点写反，原意应为 $-\dfrac{1}{\sqrt{2}} \le \cos\theta \le \dfrac{1}{2}$。
> 下文同时给出**原题字面结论**与**勘误修正后的完整解答**。

**【考点定位】**
单位圆法解基本三角方程与三角不等式、一般解（通解）的规范书写。

**【图解辅助（SVG 矢量图）】**

<svg viewBox="0 0 760 220" width="100%" xmlns="http://www.w3.org/2000/svg" style="background:#fafafa;border:1px solid #e0e0e0;border-radius:8px;margin:8px 0;">
  <!-- [1] cosθ = -1/2 -->
  <g transform="translate(10,10)">
    <rect x="0" y="0" width="178" height="200" fill="#fff" stroke="#e5e7eb" rx="6"/>
    <text x="10" y="20" font-size="11.5" font-weight="bold" fill="#1f2937">[1] cosθ = -1/2</text>
    <circle cx="89" cy="112" r="56" fill="none" stroke="#9ca3af" stroke-width="1.3"/>
    <line x1="20" y1="112" x2="158" y2="112" stroke="#6b7280" stroke-width="1"/>
    <line x1="89" y1="42" x2="89" y2="182" stroke="#6b7280" stroke-width="1"/>
    <!-- x = -1/2 -> x = 89 - 28 = 61 -->
    <line x1="61" y1="48" x2="61" y2="176" stroke="#2563eb" stroke-width="1.4" stroke-dasharray="3,2"/>
    <line x1="89" y1="112" x2="61" y2="63.5" stroke="#2563eb" stroke-width="2"/>
    <line x1="89" y1="112" x2="61" y2="160.5" stroke="#2563eb" stroke-width="2"/>
    <circle cx="61" cy="63.5" r="3.5" fill="#2563eb"/>
    <circle cx="61" cy="160.5" r="3.5" fill="#2563eb"/>
    <text x="26" y="58" font-size="10" fill="#2563eb">2π/3</text>
    <text x="26" y="172" font-size="10" fill="#2563eb">4π/3</text>
    <text x="64" y="124" font-size="9" fill="#374151">-1/2</text>
  </g>

  <!-- [2] tanθ = -1/√3 (勘误版) -->
  <g transform="translate(197,10)">
    <rect x="0" y="0" width="178" height="200" fill="#fff" stroke="#e5e7eb" rx="6"/>
    <text x="8" y="20" font-size="11" font-weight="bold" fill="#1f2937">[2] tanθ = -1/√3 (勘误)</text>
    <circle cx="89" cy="112" r="56" fill="none" stroke="#9ca3af" stroke-width="1.3"/>
    <line x1="20" y1="112" x2="158" y2="112" stroke="#6b7280" stroke-width="1"/>
    <line x1="89" y1="42" x2="89" y2="182" stroke="#6b7280" stroke-width="1"/>
    <!-- tangent line x=1 (145) -->
    <line x1="145" y1="45" x2="145" y2="178" stroke="#9ca3af" stroke-width="1" stroke-dasharray="3,2"/>
    <!-- ray for 5π/6 and 11π/6: slope -1/√3 -->
    <line x1="40.5" y1="84" x2="145" y2="144.3" stroke="#059669" stroke-width="2"/>
    <circle cx="40.5" cy="84" r="3.5" fill="#059669"/>
    <circle cx="137.5" cy="140" r="3.5" fill="#059669"/>
    <text x="15" y="79" font-size="10" fill="#059669">5π/6</text>
    <text x="132" y="160" font-size="10" fill="#059669">11π/6</text>
  </g>

  <!-- [3] sinθ < -√3/2 -->
  <g transform="translate(384,10)">
    <rect x="0" y="0" width="178" height="200" fill="#fff" stroke="#e5e7eb" rx="6"/>
    <text x="10" y="20" font-size="11.5" font-weight="bold" fill="#1f2937">[3] sinθ &lt; -√3/2</text>
    <circle cx="89" cy="112" r="56" fill="none" stroke="#9ca3af" stroke-width="1.3"/>
    <line x1="20" y1="112" x2="158" y2="112" stroke="#6b7280" stroke-width="1"/>
    <line x1="89" y1="42" x2="89" y2="182" stroke="#6b7280" stroke-width="1"/>
    <!-- y = -√3/2 -> y = 112 + 48.5 = 160.5 -->
    <line x1="25" y1="160.5" x2="153" y2="160.5" stroke="#dc2626" stroke-width="1.3" stroke-dasharray="3,2"/>
    <!-- arc from 4π/3 (61, 160.5) to 5π/3 (117, 160.5) -->
    <path d="M 61,160.5 A 56,56 0 0 0 117,160.5" fill="none" stroke="#dc2626" stroke-width="3.2"/>
    <circle cx="61" cy="160.5" r="3.5" fill="#fff" stroke="#dc2626" stroke-width="1.8"/>
    <circle cx="117" cy="160.5" r="3.5" fill="#fff" stroke="#dc2626" stroke-width="1.8"/>
    <text x="26" y="174" font-size="10" fill="#dc2626">4π/3</text>
    <text x="122" y="174" font-size="10" fill="#dc2626">5π/3</text>
  </g>

  <!-- [4] -1/√2 <= cosθ <= 1/2 (勘误版) -->
  <g transform="translate(571,10)">
    <rect x="0" y="0" width="179" height="200" fill="#fff" stroke="#e5e7eb" rx="6"/>
    <text x="6" y="20" font-size="10.5" font-weight="bold" fill="#1f2937">[4] -1/√2≤cosθ≤1/2 (勘误)</text>
    <circle cx="89" cy="112" r="56" fill="none" stroke="#9ca3af" stroke-width="1.3"/>
    <line x1="20" y1="112" x2="158" y2="112" stroke="#6b7280" stroke-width="1"/>
    <line x1="89" y1="42" x2="89" y2="182" stroke="#6b7280" stroke-width="1"/>
    <!-- x = 1/2 -> 89+28=117; x = -1/√2 -> 89-39.6=49.4 -->
    <line x1="117" y1="48" x2="117" y2="176" stroke="#7c3aed" stroke-width="1.2" stroke-dasharray="3,2"/>
    <line x1="49.4" y1="48" x2="49.4" y2="176" stroke="#7c3aed" stroke-width="1.2" stroke-dasharray="3,2"/>
    <!-- upper arc: π/3 (117, 63.5) to 3π/4 (49.4, 72.4) -->
    <path d="M 117,63.5 A 56,56 0 0 0 49.4,72.4" fill="none" stroke="#7c3aed" stroke-width="3.2"/>
    <!-- lower arc: 5π/4 (49.4, 151.6) to 5π/3 (117, 160.5) -->
    <path d="M 49.4,151.6 A 56,56 0 0 0 117,160.5" fill="none" stroke="#7c3aed" stroke-width="3.2"/>
    <circle cx="117" cy="63.5" r="3.2" fill="#7c3aed"/>
    <circle cx="49.4" cy="72.4" r="3.2" fill="#7c3aed"/>
    <circle cx="49.4" cy="151.6" r="3.2" fill="#7c3aed"/>
    <circle cx="117" cy="160.5" r="3.2" fill="#7c3aed"/>
    <text x="122" y="61" font-size="9.5" fill="#7c3aed">π/3</text>
    <text x="19" y="68" font-size="9.5" fill="#7c3aed">3π/4</text>
    <text x="18" y="164" font-size="9.5" fill="#7c3aed">5π/4</text>
    <text x="122" y="172" font-size="9.5" fill="#7c3aed">5π/3</text>
  </g>
</svg>

**【分步标准解答】**

- **`[1]`** $\cos\theta = -\dfrac{1}{2}$
  単位円上で $x = -\dfrac{1}{2}$ となる点に対応する角を $0 \le \theta < 2\pi$ の範囲で求めると、
  $$\theta = \frac{2}{3}\pi,\; \frac{4}{3}\pi$$
  一般解は（$n$ を整数として）、
  $$\theta = \pm\frac{2}{3}\pi + 2n\pi \quad \left(\text{または } \theta = \frac{2}{3}\pi + 2n\pi,\; \frac{4}{3}\pi + 2n\pi\right)$$
  > 💡 讲师批注：$\cos\theta = a$ 的两解关于 $x$ 轴对称，因此一般解可以紧凑地写为 $\pm\alpha + 2n\pi$。

- **`[2]`** $\tan\theta = -\dfrac{\sqrt{3}}{2}$（勘误版：$\tan\theta = -\dfrac{\sqrt{3}}{3} = -\dfrac{1}{\sqrt{3}}$）
  - **勘误版解答**：単位円上で傾きが $-\dfrac{1}{\sqrt{3}}$ となる直線と単位円の交点に対応する角を $0 \le \theta < 2\pi$ の範囲で求めると、
    $$\theta = \frac{5}{6}\pi,\; \frac{11}{6}\pi$$
    $\tan\theta$ の周期は $\pi$ であるから、一般解は（$n$ を整数として）、
    $$\theta = \frac{5}{6}\pi + n\pi \quad \left(\text{または } -\frac{\pi}{6} + n\pi\right)$$
  - **原题字面参考**：$\alpha = \arctan\dfrac{\sqrt{3}}{2}\;\left(0 < \alpha < \dfrac{\pi}{2}\right)$ とおくと、$0 \le \theta < 2\pi$ で $\theta = \pi - \alpha,\; 2\pi - \alpha$；一般解は $\theta = -\alpha + n\pi$（$n$ は整数）。

- **`[3]`** $\sin\theta < -\dfrac{\sqrt{3}}{2}$
  まず $\sin\theta = -\dfrac{\sqrt{3}}{2}$ を $0 \le \theta < 2\pi$ で解くと $\theta = \dfrac{4}{3}\pi,\; \dfrac{5}{3}\pi$。
  単位円上で $y < -\dfrac{\sqrt{3}}{2}$ を満たす動径の範囲は、
  $$\frac{4}{3}\pi < \theta < \frac{5}{3}\pi$$
  一般解は（$n$ を整数として）、
  $$\frac{4}{3}\pi + 2n\pi < \theta < \frac{5}{3}\pi + 2n\pi$$
  > 💡 讲师批注：严格不等号 `$<$` 对应单位圆上的**空心圆点**，端点 $\frac{4}{3}\pi, \frac{5}{3}\pi$ 不可取等。

- **`[4]`** $\dfrac{1}{2} \le \cos\theta \le -\dfrac{1}{\sqrt{2}}$（勘误版：$-\dfrac{1}{\sqrt{2}} \le \cos\theta \le \dfrac{1}{2}$）
  - **原题字面**：$\dfrac{1}{2} > -\dfrac{1}{\sqrt{2}}$ より、条件を満たす $\theta$ は存在しない（**解なし**）。
  - **勘误版解答**：境界方程式 $\cos\theta = \dfrac{1}{2}$ より $\theta = \dfrac{\pi}{3}, \dfrac{5}{3}\pi$；$\cos\theta = -\dfrac{1}{\sqrt{2}}$ より $\theta = \dfrac{3}{4}\pi, \dfrac{5}{4}\pi$。
    単位円上で $-\dfrac{1}{\sqrt{2}} \le x \le \dfrac{1}{2}$ を満たす動径の範囲は、
    $$\frac{\pi}{3} \le \theta \le \frac{3}{4}\pi,\quad \frac{5}{4}\pi \le \theta \le \frac{5}{3}\pi$$
    一般解は（$n$ を整数として）、
    $$\frac{\pi}{3} + 2n\pi \le \theta \le \frac{3}{4}\pi + 2n\pi,\quad \frac{5}{4}\pi + 2n\pi \le \theta \le \frac{5}{3}\pi + 2n\pi$$

**【最终答案】（$n$ は整数）**
- **`[1]` $0 \le \theta < 2\pi$：$\theta = \dfrac{2}{3}\pi,\; \dfrac{4}{3}\pi$；一般解：$\theta = \pm\dfrac{2}{3}\pi + 2n\pi$**
- **`[2]`（勘误为 $-\dfrac{\sqrt{3}}{3}$）$0 \le \theta < 2\pi$：$\theta = \dfrac{5}{6}\pi,\; \dfrac{11}{6}\pi$；一般解：$\theta = \dfrac{5}{6}\pi + n\pi$**
- **`[3]` $0 \le \theta < 2\pi$：$\dfrac{4}{3}\pi < \theta < \dfrac{5}{3}\pi$；一般解：$\dfrac{4}{3}\pi + 2n\pi < \theta < \dfrac{5}{3}\pi + 2n\pi$**
- **`[4]` 原题字面无解；（勘误为 $-\dfrac{1}{\sqrt{2}} \le \cos\theta \le \dfrac{1}{2}$）$0 \le \theta < 2\pi$：$\dfrac{\pi}{3} \le \theta \le \dfrac{3}{4}\pi,\; \dfrac{5}{4}\pi \le \theta \le \dfrac{5}{3}\pi$；一般解为各端点分别 $+ 2n\pi$**

---

#### 演習問題 3 (2)（P127）

**【原题重现与翻译】**
> **日文原题**：$0 \le \theta < 2\pi$ のとき、次の方程式と不等式を解け。
> `[1]` $\sqrt{2}\sin\left(\theta + \dfrac{\pi}{6}\right) = 1$
> `[2]` $2\cos\left(2\theta - \dfrac{\pi}{3}\right) \le -1$
> `[3]` $2\cos^2\theta + \sin\theta - 1 = 0$
> `[4]` $2\sin^2\theta + 5\cos\theta - 4 > 0$
>
> **中文翻译**：当 $0 \le \theta < 2\pi$ 时，解下列方程与不等式。

**【考点定位】**
整体换元法（先定新角范围！）、利用 $\sin^2\theta + \cos^2\theta = 1$ 统一函数名化为二次方程/不等式。

**【分步标准解答】**

- **`[1]`** $\sqrt{2}\sin\left(\theta + \dfrac{\pi}{6}\right) = 1$
  両辺を $\sqrt{2}$ で割ると、
  $$\sin\left(\theta + \frac{\pi}{6}\right) = \frac{1}{\sqrt{2}}$$
  $t = \theta + \dfrac{\pi}{6}$ とおくと、$0 \le \theta < 2\pi$ より、
  $$\frac{\pi}{6} \le t < \frac{13}{6}\pi$$
  > 💡 讲师批注：**换元必先写新范围！** 这里 $t$ 的起点是 $\frac{\pi}{6}$、终点是 $\frac{13}{6}\pi$（正好一整圈）。

  この範囲で $\sin t = \dfrac{1}{\sqrt{2}}$ を解くと、
  $$t = \frac{\pi}{4},\; \frac{3}{4}\pi$$
  よって $\theta = t - \dfrac{\pi}{6}$ より、
  $$\theta = \frac{\pi}{4} - \frac{\pi}{6} = \frac{\pi}{12}, \qquad \theta = \frac{3}{4}\pi - \frac{\pi}{6} = \frac{7}{12}\pi$$

- **`[2]`** $2\cos\left(2\theta - \dfrac{\pi}{3}\right) \le -1$
  両辺を $2$ で割ると、
  $$\cos\left(2\theta - \frac{\pi}{3}\right) \le -\frac{1}{2}$$
  $t = 2\theta - \dfrac{\pi}{3}$ とおくと、$0 \le \theta < 2\pi$ より $0 \le 2\theta < 4\pi$ であるから、
  $$-\frac{\pi}{3} \le t < \frac{11}{3}\pi$$
  > 💡 讲师批注：**超级高频陷阱！** 因为角前面系数是 $2$，$t$ 的范围横跨了 **2 个完整周期（$4\pi$）**，所以解集必然有**两段**！千万不要只写第一圈！

  この範囲で $\cos t \le -\dfrac{1}{2}$ を解くと（1 周目と 2 周目）：
  $$\frac{2}{3}\pi \le t \le \frac{4}{3}\pi, \qquad \frac{8}{3}\pi \le t \le \frac{10}{3}\pi$$
  $t = 2\theta - \dfrac{\pi}{3}$ を戻し、各辺に $\dfrac{\pi}{3}$ を加えて $2$ で割ると、
  $$\pi \le 2\theta \le \frac{5}{3}\pi \iff \frac{\pi}{2} \le \theta \le \frac{5}{6}\pi$$
  $$3\pi \le 2\theta \le \frac{11}{3}\pi \iff \frac{3}{2}\pi \le \theta \le \frac{11}{6}\pi$$

- **`[3]`** $2\cos^2\theta + \sin\theta - 1 = 0$
  $\cos^2\theta = 1 - \sin^2\theta$ を代入して $\sin\theta$ に統一すると、
  $$2(1 - \sin^2\theta) + \sin\theta - 1 = 0$$
  $$2\sin^2\theta - \sin\theta - 1 = 0$$
  $$(2\sin\theta + 1)(\sin\theta - 1) = 0$$
  ゆえに $\sin\theta = -\dfrac{1}{2}$ または $\sin\theta = 1$。
  $0 \le \theta < 2\pi$ の範囲で解くと、
  - $\sin\theta = 1$ より $\theta = \dfrac{\pi}{2}$
  - $\sin\theta = -\dfrac{1}{2}$ より $\theta = \dfrac{7}{6}\pi,\; \dfrac{11}{6}\pi$
  > 💡 讲师批注：统一函数名原则——「保留一次项，替换二次项」。此处一次项是 $\sin\theta$，故用 $1-\sin^2\theta$ 替换 $\cos^2\theta$。

- **`[4]`** $2\sin^2\theta + 5\cos\theta - 4 > 0$
  $\sin^2\theta = 1 - \cos^2\theta$ を代入して $\cos\theta$ に統一すると、
  $$2(1 - \cos^2\theta) + 5\cos\theta - 4 > 0$$
  $$-2\cos^2\theta + 5\cos\theta - 2 > 0$$
  両辺に $-1$ を掛けて（不等号の向きが変わる）、
  $$2\cos^2\theta - 5\cos\theta + 2 < 0$$
  $$(2\cos\theta - 1)(\cos\theta - 2) < 0$$
  ここで、すべての実数 $\theta$ に対して $-1 \le \cos\theta \le 1$ であるから、常に $\cos\theta - 2 < 0$ である。
  よって、不等式は次と同値である：
  $$2\cos\theta - 1 > 0 \iff \cos\theta > \frac{1}{2}$$
  $0 \le \theta < 2\pi$ の範囲で解くと、
  $$0 \le \theta < \frac{\pi}{3}, \qquad \frac{5}{3}\pi < \theta < 2\pi$$
  > 💡 讲师批注：注意左端点 $\theta = 0$ 处 $\cos 0 = 1 > \frac{1}{2}$ 满足不等式，故应写 **$0 \le \theta < \frac{\pi}{3}$**（含等号）；右端点 $2\pi$ 本身不在定义域内，故写 **$\frac{5}{3}\pi < \theta < 2\pi$**（不含等号）。

**【最终答案】**
- **`[1]` $\theta = \dfrac{\pi}{12},\; \dfrac{7}{12}\pi$**
- **`[2]` $\dfrac{\pi}{2} \le \theta \le \dfrac{5}{6}\pi,\; \dfrac{3}{2}\pi \le \theta \le \dfrac{11}{6}\pi$**
- **`[3]` $\theta = \dfrac{\pi}{2},\; \dfrac{7}{6}\pi,\; \dfrac{11}{6}\pi$**
- **`[4]` $0 \le \theta < \dfrac{\pi}{3},\; \dfrac{5}{3}\pi < \theta < 2\pi$**

---

#### 演習問題 3 (3)（P128）

**【原题重现与翻译】**
> **日文原题**：関数 $y = 4\sin^2\theta - 4\cos\theta + 1$（$0 \le \theta < 2\pi$）の最大値と最小値を求めよ。また、そのときの $\theta$ の値を求めよ。
>
> **中文翻译**：求函数 $y = 4\sin^2\theta - 4\cos\theta + 1$（$0 \le \theta < 2\pi$）的最大值与最小值，并求出取得最值时的 $\theta$ 值。

**【考点定位】**
换元化为闭区间上的二次函数最值问题。

**【分步标准解答】**
$\sin^2\theta = 1 - \cos^2\theta$ を代入すると、
$$y = 4(1 - \cos^2\theta) - 4\cos\theta + 1 = -4\cos^2\theta - 4\cos\theta + 5$$
$t = \cos\theta$ とおくと、$0 \le \theta < 2\pi$ より $t$ の取り得る値の範囲は $-1 \le t \le 1$ である。
$y$ を $t$ について平方完成すると、
$$y = -4\left(t^2 + t\right) + 5 = -4\left(t + \frac{1}{2}\right)^2 + 6$$
> 💡 讲师批注：二次项系数为 $-4 < 0$（开口向下），对称轴 $t = -\frac{1}{2}$ 落在区间 $[-1, 1]$ 内部，因此顶点处取得最大值，距离对称轴更远的端点 $t = 1$（距离 $\frac{3}{2} > \frac{1}{2}$）处取得最小值。

よって、$-1 \le t \le 1$ の範囲で：
- $t = -\dfrac{1}{2}$ のとき、最大値 $6$ をとる。
  このとき $\cos\theta = -\dfrac{1}{2}$（$0 \le \theta < 2\pi$）より、$\theta = \dfrac{2}{3}\pi,\; \dfrac{4}{3}\pi$。
- $t = 1$ のとき、最小値 $-4(1 + \frac{1}{2})^2 + 6 = -3$ をとる。
  このとき $\cos\theta = 1$（$0 \le \theta < 2\pi$）より、$\theta = 0$。

**【最终答案】**
- **最大値：$6$（$\theta = \dfrac{2}{3}\pi,\; \dfrac{4}{3}\pi$ のとき）**
- **最小値：$-3$（$\theta = 0$ のとき）**

---

#### 演習問題 3 (4)（P128）

**【原题重现与翻译】**
> **日文原题**：$y = 2a\cos\theta + 2 - \sin^2\theta$（$-\dfrac{\pi}{2} \le \theta \le \dfrac{\pi}{2}$）の最大値を $a$ の不等式で表せ。
>
> **中文翻译**：用 $a$ 的表达式（按 $a$ 的范围分类）表示函数 $y = 2a\cos\theta + 2 - \sin^2\theta$（$-\dfrac{\pi}{2} \le \theta \le \dfrac{\pi}{2}$）的最大值。

> ⚠️ **教材勘误提示**：原题「$a$ の不等式で表せ」属于表达瑕疵，应理解为「$a$ の式で表せ（用含 $a$ 的式子表示）」。

**【考点定位】**
含参二次函数（动轴定区间）的最大值分类讨论；注意限定角区间下 $\cos\theta$ 的值域收缩！

**【分步标准解答】**
$\sin^2\theta = 1 - \cos^2\theta$ を代入すると、
$$y = 2a\cos\theta + 2 - (1 - \cos^2\theta) = \cos^2\theta + 2a\cos\theta + 1$$
$t = \cos\theta$ とおく。$-\dfrac{\pi}{2} \le \theta \le \dfrac{\pi}{2}$ のとき、$\cos\theta$ の取り得る値の範囲は
$$0 \le t \le 1$$
である。
> 💡 讲师批注：**本题头号陷阱！** 题目给的是 $-\frac{\pi}{2} \le \theta \le \frac{\pi}{2}$（第一、四象限），所以 $t = \cos\theta$ 的范围是 **$0 \le t \le 1$**，而不是 $[-1, 1]$！

$f(t) = t^2 + 2at + 1 = (t + a)^2 - a^2 + 1$ とおく。
これは下に凸の放物線で、軸は $t = -a$ である。定義域 $0 \le t \le 1$ の中点は $t = \dfrac{1}{2}$ であるから、軸 $t = -a$ と中点 $\dfrac{1}{2}$ の位置関係で場合分けする。

1. **$-a < \dfrac{1}{2}$ すなわち $a > -\dfrac{1}{2}$ のとき**：
   軸より遠い右端 $t = 1$ で最大となる。
   $$\text{最大値} = f(1) = 1 + 2a + 1 = 2a + 2$$
2. **$-a = \dfrac{1}{2}$ すなわち $a = -\dfrac{1}{2}$ のとき**：
   両端 $t = 0,\; 1$ でともに最大となる。
   $$\text{最大値} = f(0) = f(1) = 1$$
3. **$-a > \dfrac{1}{2}$ すなわち $a < -\dfrac{1}{2}$ のとき**：
   軸より遠い左端 $t = 0$ で最大となる。
   $$\text{最大値} = f(0) = 1$$

以上（2 は 1 または 3 に統合可能）をまとめると次のようになる。

**【最终答案】**
- **$a \ge -\dfrac{1}{2}$ のとき、最大値は $2a + 2$**
- **$a < -\dfrac{1}{2}$ のとき、最大値は $1$**

---

#### 演習問題 3 (5)（P129）

**【原题重现与翻译】**
> **日文原题**：$\theta$ の方程式 $\sin^2\theta + a\cos\theta - 2a - 1 = 0$ を満たす $\theta$ があるような定数 $a$ の値の範囲を求めよ。
>
> **中文翻译**：求使关于 $\theta$ 的方程 $\sin^2\theta + a\cos\theta - 2a - 1 = 0$ 存在实数解 $\theta$ 的常数 $a$ 的取值范围。

**【考点定位】**
含参三角方程的有解条件 $\iff$ 二次方程在闭区间 $[-1, 1]$ 上有实根（解法一：分离参数 + 均值不等式；解法二：二次函数根的分布）。

**【分步标准解答】**
$\sin^2\theta = 1 - \cos^2\theta$ を代入して整理すると、
$$(1 - \cos^2\theta) + a\cos\theta - 2a - 1 = 0 \iff \cos^2\theta - a\cos\theta + 2a = 0$$
$t = \cos\theta$ とおくと、$\theta$ が実数全体を動くとき $-1 \le t \le 1$ である。
よって、求める条件は「$t$ の方程式 $t^2 - at + 2a = 0$ が $-1 \le t \le 1$ の範囲に少なくとも $1$ つの実数解をもつこと」である。

**【解法一：定数分離法（最速・推奨）】**
方程式を $a$ について変形すると、
$$a(t - 2) = t^2$$
$-1 \le t \le 1$ において $t - 2 \neq 0$（$-3 \le t - 2 \le -1$）であるから、両辺を $t - 2$ で割って、
$$a = \frac{t^2}{t - 2}$$
$v = 2 - t$ とおくと、$-1 \le t \le 1$ より $1 \le v \le 3$、かつ $t = 2 - v$ であるから、
$$a = \frac{(2 - v)^2}{-v} = -\frac{v^2 - 4v + 4}{v} = 4 - \left(v + \frac{4}{v}\right)$$
> 💡 讲师批注：换元 $v = 2 - t > 0$ 后，括号内 $v + \frac{4}{v}$ 是典型的「对勾函数」，在 $v = 2$ 处取最小值 $4$！

$g(v) = v + \dfrac{4}{v}$（$1 \le v \le 3$）の値域を調べる：
- 相加・相乗平均の関係より $g(v) \ge 2\sqrt{v \cdot \dfrac{4}{v}} = 4$（等号は $v = 2 \in [1, 3]$ で成立）。
- 端点値は $g(1) = 1 + 4 = 5$、$g(3) = 3 + \dfrac{4}{3} = \dfrac{13}{3} < 5$。
よって $4 \le g(v) \le 5$ であるから、
$$4 - 5 \le a \le 4 - 4 \iff -1 \le a \le 0$$

**【解法二：二次関数の解の配置による検算】**
$f(t) = t^2 - at + 2a$ とおくと、$f(-1) = 1 + 3a$、$f(1) = 1 + a$、軸は $t = \dfrac{a}{2}$、判別式は $D = a^2 - 8a = a(a - 8)$。
- **［ア］$-1 \le t \le 1$ にただ $1$ つの解をもつ（重解除く）**：$f(-1)f(1) \le 0 \iff (1+3a)(1+a) \le 0 \iff -1 \le a \le -\dfrac{1}{3}$。
- **［イ］$-1 \le t \le 1$ に $2$ つの解（重解含む）をもつ**：
  $$D \ge 0 \;\land\; -1 \le \frac{a}{2} \le 1 \;\land\; f(-1) \ge 0 \;\land\; f(1) \ge 0$$
  これを解くと $-\dfrac{1}{3} \le a \le 0$。
［ア］と［イ］を合わせて、$-1 \le a \le 0$。（解法一と完全一致！）

**【最终答案】**
- **$-1 \le a \le 0$**

---

#### 演習問題 3 (6)（P129）

**【原题重现与翻译】**
> **日文原题**：$a$ は定数とする。$\theta$ に関する方程式 $\sin^2\theta - \cos\theta + a = 0$ について、次の問いに答えよ。ただし、$0 \le \theta < 2\pi$ とする。
> `[1]` この方程式が解を持つための $a$ の条件を求めよ。
> `[2]` この方程式の解の個数を $a$ の値の範囲によって調べよ。
>
> **中文翻译**：设 $a$ 为常数。关于 $\theta$ 的方程 $\sin^2\theta - \cos\theta + a = 0$（其中 $0 \le \theta < 2\pi$），回答下列问题：
> `[1]` 求该方程有解时 $a$ 满足的条件。
> `[2]` 按 $a$ 的取值范围讨论该方程解的个数。

**【考点定位】**
分离参数法结合二次函数图像，$t = \cos\theta$ 与 $\theta$ 的「一对二 / 一对一」对应关系（**EJU 理系数学绝对王牌压轴题型**）。

**【图解辅助（SVG 矢量图）】**

<svg viewBox="0 0 680 260" width="100%" xmlns="http://www.w3.org/2000/svg" style="background:#fafafa;border:1px solid #e0e0e0;border-radius:8px;margin:8px 0;">
  <!-- Left: y = g(t) = t^2 + t - 1 on [-1, 1] -->
  <g transform="translate(15,10)">
    <rect x="0" y="0" width="380" height="240" fill="#fff" stroke="#e5e7eb" rx="6"/>
    <text x="12" y="22" font-size="12.5" font-weight="bold" fill="#1f2937">y = g(t) = (t + 1/2)² - 5/4 (-1 ≤ t ≤ 1) 与 y = a</text>
    <!-- coordinate system: origin at (190, 115), scale x: 100px per 1, y: 65px per 1 -->
    <line x1="40" y1="115" x2="350" y2="115" stroke="#6b7280" stroke-width="1.2"/>
    <line x1="190" y1="35" x2="190" y2="225" stroke="#6b7280" stroke-width="1.2"/>
    <text x="353" y="119" font-size="11" fill="#374151">t</text>
    <text x="195" y="42" font-size="11" fill="#374151">y</text>
    <text x="178" y="128" font-size="10" fill="#374151">O</text>
    <!-- vertical lines t=-1 (90) and t=1 (290) -->
    <line x1="90" y1="45" x2="90" y2="215" stroke="#d1d5db" stroke-dasharray="3,3"/>
    <line x1="290" y1="45" x2="290" y2="215" stroke="#d1d5db" stroke-dasharray="3,3"/>
    <text x="82" y="128" font-size="10" fill="#374151">-1</text>
    <text x="287" y="128" font-size="10" fill="#374151">1</text>
    <text x="128" y="128" font-size="9.5" fill="#6b7280">-1/2</text>
    <!-- horizontal reference lines: a=1(y=50), a=-1(y=180), a=-5/4(y=196.25) -->
    <line x1="45" y1="50" x2="340" y2="50" stroke="#7c3aed" stroke-width="1.2" stroke-dasharray="4,3"/>
    <text x="300" y="46" font-size="10" fill="#7c3aed">a = 1 (1个)</text>
    <line x1="45" y1="180" x2="340" y2="180" stroke="#059669" stroke-width="1.2" stroke-dasharray="4,3"/>
    <text x="295" y="176" font-size="10" fill="#059669">a = -1 (3个)</text>
    <line x1="45" y1="196.25" x2="340" y2="196.25" stroke="#dc2626" stroke-width="1.2" stroke-dasharray="4,3"/>
    <text x="280" y="210" font-size="10" fill="#dc2626">a = -5/4 (2个)</text>
    <!-- parabola: t=-1 -> (90,180); t=-0.5 -> (140,196.25); t=0 -> (190,180); t=0.5 -> (240,131.25); t=1 -> (290,50) -->
    <path d="M 90,180 Q 140,212.5 190,180 T 290,50" fill="none" stroke="#2563eb" stroke-width="2.6"/>
    <!-- key points -->
    <circle cx="90" cy="180" r="4" fill="#dc2626"/>
    <circle cx="140" cy="196.25" r="4" fill="#2563eb"/>
    <circle cx="190" cy="180" r="3.5" fill="#2563eb"/>
    <circle cx="290" cy="50" r="4" fill="#dc2626"/>
    <text x="52" y="174" font-size="9.5" fill="#dc2626">(-1,-1)</text>
    <text x="255" y="64" font-size="9.5" fill="#dc2626">(1,1)</text>
  </g>

  <!-- Right: t -> θ correspondence -->
  <g transform="translate(410,10)">
    <rect x="0" y="0" width="255" height="240" fill="#fff" stroke="#e5e7eb" rx="6"/>
    <text x="12" y="22" font-size="12.5" font-weight="bold" fill="#1f2937">t = cosθ 与 θ 解的个数对应</text>
    <circle cx="127" cy="125" r="62" fill="none" stroke="#9ca3af" stroke-width="1.4"/>
    <line x1="45" y1="125" x2="210" y2="125" stroke="#6b7280" stroke-width="1"/>
    <line x1="127" y1="45" x2="127" y2="205" stroke="#6b7280" stroke-width="1"/>
    <!-- t=1 (189,125) and t=-1 (65,125) -->
    <circle cx="189" cy="125" r="4.5" fill="#dc2626"/>
    <circle cx="65" cy="125" r="4.5" fill="#dc2626"/>
    <text x="195" y="121" font-size="10" fill="#dc2626">t=1 → 1个(0)</text>
    <text x="8" y="121" font-size="10" fill="#dc2626">t=-1 → 1个(π)</text>
    <!-- intermediate vertical line -->
    <line x1="100" y1="60" x2="100" y2="190" stroke="#2563eb" stroke-width="1.4" stroke-dasharray="3,2"/>
    <circle cx="100" cy="69" r="3.8" fill="#2563eb"/>
    <circle cx="100" cy="181" r="3.8" fill="#2563eb"/>
    <text x="48" y="218" font-size="11" fill="#2563eb" font-weight="bold">-1 &lt; t &lt; 1 时，每个 t 对应 2 个 θ！</text>
  </g>
</svg>

**【分步标准解答】**

$\sin^2\theta = 1 - \cos^2\theta$ を代入して $a$ を分離すると、
$$1 - \cos^2\theta - \cos\theta + a = 0 \iff a = \cos^2\theta + \cos\theta - 1$$
$t = \cos\theta$ とおくと、$0 \le \theta < 2\pi$ のとき $-1 \le t \le 1$ であり、方程式は
$$a = t^2 + t - 1$$
となる。ここで $g(t) = t^2 + t - 1 = \left(t + \dfrac{1}{2}\right)^2 - \dfrac{5}{4}$（$-1 \le t \le 1$）とおくと、
- 頂点は $\left(-\dfrac{1}{2},\; -\dfrac{5}{4}\right)$
- 端点値は $g(-1) = -1$、$g(1) = 1$（また $g(0) = -1$）

**`[1]` 方程式が解を持つための $a$ の条件**
放物線 $y = g(t)$（$-1 \le t \le 1$）と直線 $y = a$ が共有点をもつことが条件であるから、$g(t)$ の最小値と最大値より、
$$-\frac{5}{4} \le a \le 1$$

**`[2]` 方程式の解の個数**
$0 \le \theta < 2\pi$ の範囲で、$t = \cos\theta$ の値に対する $\theta$ の個数は次の通りである：
- $t = 1$ のとき $\theta = 0$ の **$1$ 個**
- $t = -1$ のとき $\theta = \pi$ の **$1$ 個**
- $-1 < t < 1$ のとき $\theta$ は **$2$ 個**

> 💡 讲师批注：解的个数由「直线 $y = a$ 与抛物线交点的 $t$ 坐标」决定：落在开区间 $(-1, 1)$ 内的交点每个贡献 **2 个** $\theta$，落在端点 $t = \pm 1$ 上的交点每个只贡献 **1 个** $\theta$！

グラフより、$a$ の値に応じて以下のように分類される：
- $a < -\dfrac{5}{4},\; 1 < a$ のとき：共有点なし $\implies$ **$0$ 個**
- $a = -\dfrac{5}{4}$ のとき：$t = -\dfrac{1}{2} \in (-1, 1)$ が $1$ つ $\implies$ **$2$ 個**
- $-\dfrac{5}{4} < a < -1$ のとき：$-1 < t < 1$ に $2$ つ $\implies 2 + 2 =$ **$4$ 個**
- $a = -1$ のとき：$t = -1$（$1$ 個）と $t = 0 \in (-1, 1)$（$2$ 個）$\implies 1 + 2 =$ **$3$ 個**
- $-1 < a < 1$ のとき：$0 < t < 1$ に $1$ つ $\implies$ **$2$ 個**
- $a = 1$ のとき：$t = 1$ が $1$ つ $\implies$ **$1$ 個**

**【最终答案】**
- **`[1]` $-\dfrac{5}{4} \le a \le 1$**
- **`[2]`**
  - **$a < -\dfrac{5}{4},\; 1 < a$ のとき：$0$ 個**
  - **$a = 1$ のとき：$1$ 個**
  - **$a = -\dfrac{5}{4},\; -1 < a < 1$ のとき：$2$ 個**
  - **$a = -1$ のとき：$3$ 個**
  - **$-\dfrac{5}{4} < a < -1$ のとき：$4$ 個**

---

> 👉 **下接**：演習問題 4（加法定理、二倍角・半角公式与两直线夹角，P130–P135）请见 [note_009_b.md](file:///Users/baohan/Desktop/EJU/notes_math/note_009_b.md)。
