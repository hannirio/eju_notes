# 《EJU 教材全解与备课讲义》数学 006-B（P82–P90）

> **对应源文件**：`work_math/ocr_md/ocr_006_p76-90.md`（第五章《幾何基礎》之「平面図形と三角比」「三角比の拡張」「演習問題 1・2」）
> **视觉核对参考图**：`work_math/ref_imgs/page_0082.jpg` – `page_0090.jpg`

---

## 一、国内高中基础知识点唤醒与 EJU 考纲差异对比

本册对应日本中学几何核心复习及 **数学Ⅰ（図形と計量）** 的开篇内容，涵盖 **平面几何基础定理（角・全等・相似・中位线・勾股定理・平行四边形）、锐角三角比、$0^\circ \le \theta \le 180^\circ$ 的三角比扩展（单位半圆定义）、诱导公式、直线的斜率与正切、三角方程与三角不等式**。

### 1.1 平面几何核心基础（平面図形）

- **角与平行线**：对顶角（対頂角）相等；两直线平行 $\iff$ 同位角相等 $\iff$ 内错角（錯角）相等。
- **三角形全等条件（合同条件）**：SSS（三辺）、SAS（2辺とその間の角）、ASA（1辺とその両端の角）；直角三角形特有：HL（斜辺と他の1辺）、HA（斜辺と1つの鋭角）。
- **三角形相似条件（相似条件）**：SSS（3組の辺の比）、SAS（2組の辺の比とその間の角）、AA（2組の角）。
- **中位线定理（中点連結定理）**：$M, N$ 为 $AB, AC$ 中点 $\implies MN \parallel BC,\; MN = \dfrac{1}{2}BC$。
- **勾股定理（三平方の定理 / ピタゴラスの定理）**：$\angle C = 90^\circ \iff a^2 + b^2 = c^2$。
- **平行四边形判定（5条）与特殊平行四边形**：长方形（長方形：四角直角・对角线等长）、菱形（菱形：四边等长・对角线垂直）、正方形（兼备以上全部）。

### 1.2 锐角三角比与三角比扩展（$0^\circ \le \theta \le 180^\circ$）

- **单位半圆（半径 $r$ 的半圆）定义**：设点 $P(x, y)$ 在以原点 $O$ 为圆心、半径为 $r$ 的上半圆周上，$\angle AOP = \theta$（$0^\circ \le \theta \le 180^\circ$）：
  $$\sin\theta = \frac{y}{r},\qquad \cos\theta = \frac{x}{r},\qquad \tan\theta = \frac{y}{x} \quad (\theta \neq 90^\circ)$$
- **取值范围（$0^\circ \le \theta \le 180^\circ$）**：$0 \le \sin\theta \le 1$，$-1 \le \cos\theta \le 1$，$\tan\theta$（$\theta \neq 90^\circ$）可取任意实数。
- **相互关系（$0^\circ \le \theta \le 180^\circ$，①③需 $\theta \neq 90^\circ$）**：
  $$\tan\theta = \frac{\sin\theta}{\cos\theta},\qquad \sin^2\theta + \cos^2\theta = 1,\qquad 1 + \tan^2\theta = \frac{1}{\cos^2\theta}$$
- **重要诱导公式（余角・补角・$90^\circ+\theta$）**：
  - **$90^\circ - \theta$**：$\sin(90^\circ - \theta) = \cos\theta$，$\cos(90^\circ - \theta) = \sin\theta$，$\tan(90^\circ - \theta) = \dfrac{1}{\tan\theta}$
  - **$180^\circ - \theta$**：$\sin(180^\circ - \theta) = \sin\theta$，$\cos(180^\circ - \theta) = -\cos\theta$，$\tan(180^\circ - \theta) = -\tan\theta$
  - **$90^\circ + \theta$**：$\sin(90^\circ + \theta) = \cos\theta$，$\cos(90^\circ + \theta) = -\sin\theta$，$\tan(90^\circ + \theta) = -\dfrac{1}{\tan\theta}$
  > ⚠️ **教材勘误提示**：
  > 1. 原教材第 84 页（`page_0085.jpg`）[1.7] 第二行将 $\cos(90^\circ - \theta) = \sin\theta$ 重复误印为 $\sin(90^\circ - \theta) = \cos\theta$；
  > 2. 同页 [1.8] 第三行将 $\tan 45^\circ = 1,\; \tan 60^\circ = \sqrt{3}$ 误印为 $\sin 45^\circ = 1,\; \sin 60^\circ = \sqrt{3}$；
  > 3. 原教材第 86 页（`page_0087.jpg`）[2.3] ② 末行将 $\tan(90^\circ + \theta) = -\dfrac{1}{\tan\theta}$ 误印为 $\tan(180^\circ - \theta) = -\dfrac{1}{\tan\theta}$。
- **直线斜率与正切**：直线 $y = mx + n$ 与 $x$ 轴正方向的夹角（倾斜角）为 $\theta$（$0^\circ \le \theta < 180^\circ,\; \theta \neq 90^\circ$），则 $m = \tan\theta$。

### 1.3 国内高中 vs. 日本 EJU 考纲差异与符号习惯

| 对比维度 | 国内高中习惯 | 日本 EJU 习惯 | 备课/应试提醒 |
| :--- | :--- | :--- | :--- |
| **勾股定理名称** | 称「勾股定理」 | 称 **三平方の定理（さんへいほうのていり）** 或 **ピタゴラスの定理** | 读题时看到「三平方の定理」立刻反应为 $a^2+b^2=c^2$ |
| **内错角 / 中位线** | 称「内错角」「中位线定理」 | 称 **錯角（さっかく）**、**中点連結定理（ちゅうてんれんけつていり）** | 术语差异大，必须专门背诵 |
| **三角比 vs. 三角函数** | 统称「三角函数」，高一直接学任意角与弧度制 | **数学Ⅰ叫「三角比」**（仅限 $0^\circ \le \theta \le 180^\circ$，用角度制）；**数学Ⅱ才叫「三角関数」**（任意角+弧度制） | 本章所有解均限定在 $0^\circ \le \theta \le 180^\circ$，且用角度制（°）作答 |
| **特殊角分母有理化** | 常写 $\frac{\sqrt{2}}{2}$、$\frac{\sqrt{3}}{3}$ | 日本教科书习惯保留 $\dfrac{1}{\sqrt{2}}$、$\dfrac{1}{\sqrt{3}}$（EJU 填空题会按框型决定是否化简） | 两种形式均需熟练互认 |

---

## 二、日文核心词汇与公式假名注音

### 2.1 本切片日文核心词汇

- 平面図形（へいめんずけい / heimen zukei） — 平面图形
- 対頂角（たいちょうかく / taichoukaku） — 对顶角
- 同位角（どういかく / douikaku） — 同位角
- 錯角（さっかく / sakkaku） — 内错角
- 内角（ないかく / naikaku） — 内角
- 外角（がいかく / gaikaku） — 外角
- 二等辺三角形（にとうへんさんかっけい / nitouhen sankakkei） — 等腰三角形
- 頂角（ちょうかく / choukaku） — 顶角
- 底角（ていかく / teikaku） — 底角
- 底辺（ていへん / teihen） — 底边
- 二等分線（にとうぶんせん / nitoubunsen） — 平分线（如 頂角の二等分線 = 顶角平分线）
- 垂直（すいちょく / suichoku） — 垂直
- 垂線（すいせん / suisen） — 垂线
- 合同（ごうどう / goudou） — 全等（合同条件 = 全等判定条件）
- 相似（そうじ / souji） — 相似（相似条件 = 相似判定条件）
- 直角三角形（ちょっかくさんかっけい / chokkaku sankakkei） — 直角三角形
- 斜辺（しゃへん / shahen） — 斜边
- 鋭角（えいかく / eikaku） — 锐角
- 鈍角（どんかく / donkaku） — 钝角
- 中点連結定理（ちゅうてんれんけつていり / chuuten renketsu teiri） — 三角形中位线定理
- 線分（せんぶん / senbun） — 线段
- 三平方の定理（さんへいほうのていり / sanheihou no teiri） — 勾股定理（亦称 ピタゴラスの定理）
- 平行四辺形（へいこうしへんけい / heikou shihenkei） — 平行四边形
- 対辺（たいへん / taihen） — 对边
- 対角（たいかく / taikaku） — 对角
- 対角線（たいかくせん / taikakusen） — 对角线
- 長方形（ちょうほうけい / chouhoukei） — 长方形、矩形
- 菱形（ひしがた / hishigata） — 菱形
- 正方形（せいほうけい / seihoukei） — 正方形
- 三角比（さんかくひ / sankakuhi） — 三角比
- 正弦（せいげん / seigen） — 正弦（$\sin$）
- 余弦（よげん / yogen） — 余弦（$\cos$）
- 正接（せいせつ / seisetsu） — 正接、正切（$\tan$）
- 相互関係（そうごかんけい / sougo kankei） — 相互关系
- 拡張（かくちょう / kakuchou） — 扩展、推广
- 座標（ざひょう / zahyou） — 坐标
- 半円（はんえん / han'en） — 半圆
- 半径（はんけい / hankei） — 半径
- なす角（なすかく / nasukaku） — 夹角

### 2.2 核心公式的日本课堂口语读法

1. **三角比基本符号** $\sin\theta,\; \cos\theta,\; \tan\theta$
   - 课堂读法：**サイン シータ**、**コサイン シータ**、**タンジェント シータ**
2. **平方关系** $\sin^2\theta + \cos^2\theta = 1$
   - 课堂读法：**サイン にじょう シータ たす コサイン にじょう シータ イコール いち**
3. **正切与余弦关系** $1 + \tan^2\theta = \dfrac{1}{\cos^2\theta}$
   - 课堂读法：**いち たす タンジェント にじょう シータ イコール コサイン にじょう シータ ぶんの いち**
4. **勾股定理** $a^2 + b^2 = c^2$
   - 课堂读法：**エーのにじょう たす ビーのにじょう イコール シーのにじょう**

---

## 三、逐题深度解析（不可跳步）

---

### 演習問題 1（鋭角の三角比と相互関係）

#### 演習問題 1-(1)
- **【原题重现与翻译】**
  - 原题（修正后）：右の図の $\triangle ABC$ で、$\angle B = 75^\circ$ とする。頂点 $A$ から辺 $BC$ に垂線 $AD$ を引き、頂点 $B$ から辺 $AC$ に垂線 $BE$ を引くと、$AD = DC,\; AE = 2$ である。
    - [1] 線分 $AD,\; BD$ の長さを求めよ。
    - [2] $\sin 75^\circ,\; \cos 75^\circ$ の値を求めよ。
  - 中文：在右图 $\triangle ABC$ 中，$\angle B = 75^\circ$。自顶点 $A$ 向边 $BC$ 作垂线 $AD$，自顶点 $B$ 向边 $AC$ 作垂线 $BE$，已知 $AD = DC,\; AE = 2$。
    - [1] 求线段 $AD,\; BD$ 的长度。
    - [2] 求 $\sin 75^\circ,\; \cos 75^\circ$ 的值。
  > ⚠️ **教材勘误提示**：原教材第 85 页（`page_0086.jpg`）题干有两处明显印刷错漏：①「頂点 $A$ から辺 $BC$ に垂線 $BE$ を引く」漏印了垂线 $AD$ 及「頂点 $B$ から辺 $AC$ に」；②「$AD = BC$」与右图中标在 $AD$ 与 $DC$ 上的等长双横线不符，正确条件为 **$AD = DC$**。按图示条件方可完美求出 $\sin 75^\circ, \cos 75^\circ$ 的精确值。
- **【考点定位】**
  - 特殊直角三角形（$30^\circ$-$60^\circ$-$90^\circ$ 与 $45^\circ$-$45^\circ$-$90^\circ$）拼图求 $75^\circ$ 三角比 + 双重根号化简。
- **【图解辅助（SVG 矢量图）】**
  <svg viewBox="0 0 340 230" width="340" height="230" xmlns="http://www.w3.org/2000/svg" style="background:#fff;border:1px solid #e2e8f0;border-radius:6px;">
    <!-- 顶点坐标按真实几何比例: D=(95,190), C=(275,190) (DC=180), A=(95,10) (AD=180), B=(47,190) (BD≈48.2) -->
    <!-- AC: (95,10)到(275,190), 垂足E为B向AC作垂线: E=(137,52) -->
    <polygon points="95,22 49,192 265,192" fill="#f8fafc" stroke="#1e293b" stroke-width="2"/>
    <!-- 垂线 AD -->
    <line x1="95" y1="22" x2="95" y2="192" stroke="#2563eb" stroke-width="1.6"/>
    <!-- 垂线 BE: 直线AC斜率1, 从B(49,192)向AC作垂线, E=(134,61)近似按几何计算: AC过(95,22)-(265,192), y-x=-73; 垂线过(49,192), x+y=241 => x=157, y=84? 检算: (95,22)到(265,192) dx=170, dy=170, y = x - 73; 过B(49,192)斜率-1: y = -x + 241; 联立 2x = 314 => x=157, y=84! -->
    <line x1="49" y1="192" x2="157" y2="84" stroke="#dc2626" stroke-width="1.6"/>
    <!-- 直角符号 D -->
    <polyline points="95,180 107,180 107,192" fill="none" stroke="#2563eb" stroke-width="1.3"/>
    <!-- 直角符号 E -->
    <polyline points="148,93 140,85 148,77" fill="none" stroke="#dc2626" stroke-width="1.3"/>
    <!-- 等长双横线 AD=DC -->
    <line x1="89" y1="103" x2="101" y2="103" stroke="#2563eb" stroke-width="1.5"/>
    <line x1="89" y1="109" x2="101" y2="109" stroke="#2563eb" stroke-width="1.5"/>
    <line x1="177" y1="186" x2="177" y2="198" stroke="#2563eb" stroke-width="1.5"/>
    <line x1="183" y1="186" x2="183" y2="198" stroke="#2563eb" stroke-width="1.5"/>
    <!-- 顶点标签 -->
    <text x="90" y="16" font-size="13" fill="#1e293b" font-weight="bold">A</text>
    <text x="35" y="206" font-size="13" fill="#1e293b" font-weight="bold">B</text>
    <text x="90" y="209" font-size="13" fill="#2563eb" font-weight="bold">D</text>
    <text x="270" y="206" font-size="13" fill="#1e293b" font-weight="bold">C</text>
    <text x="163" y="82" font-size="13" fill="#dc2626" font-weight="bold">E</text>
    <!-- 角度与长度标注 -->
    <text x="131" y="48" font-size="12" fill="#dc2626" font-weight="bold">2</text>
    <text x="64" y="183" font-size="11" fill="#1e293b">75°</text>
    <text x="230" y="185" font-size="11" fill="#2563eb">45°</text>
    <text x="98" y="46" font-size="11" fill="#16a34a">60°</text>
  </svg>
- **【分步标准解答】**
  - **[1] 線分 $AD,\; BD$ の長さ**：
    1. $\triangle ADC$ において、$\angle ADC = 90^\circ$ かつ $AD = DC$ であるから、$\triangle ADC$ は直角二等辺三角形である。
       よって、$\angle C = 45^\circ$。
    2. $\triangle ABC$ の内角の和より、
       $$\angle BAC = 180^\circ - \angle B - \angle C = 180^\circ - 75^\circ - 45^\circ = 60^\circ$$
    3. 直角三角形 $\triangle ABE$（$\angle AEB = 90^\circ$）において、$\angle BAE = 60^\circ,\; AE = 2$ であるから（辺の比 $1 : 2 : \sqrt{3}$ より）、
       $$AB = 2AE = 4,\qquad BE = \sqrt{3}\,AE = 2\sqrt{3}$$
    4. 直角三角形 $\triangle BEC$ において、$\angle C = 45^\circ$ であるから直角二等辺三角形となり、
       $$EC = BE = 2\sqrt{3}$$
       よって、
       $$AC = AE + EC = 2 + 2\sqrt{3}$$
    5. 直角二等辺三角形 $\triangle ADC$ において $AD : AC = 1 : \sqrt{2}$ であるから、
       $$AD = \frac{AC}{\sqrt{2}} = \frac{2 + 2\sqrt{3}}{\sqrt{2}} = \sqrt{2} + \sqrt{6}$$
    6. 直角三角形 $\triangle ABD$ に三平方の定理を用いると、
       $$BD^2 = AB^2 - AD^2 = 4^2 - (\sqrt{6} + \sqrt{2})^2 = 16 - (6 + 4\sqrt{3} + 2) = 8 - 4\sqrt{3}$$
       $BD > 0$ より、二重根号を外して、
       $$BD = \sqrt{8 - 4\sqrt{3}} = \sqrt{8 - 2\sqrt{12}} = \sqrt{6} - \sqrt{2}$$
       > 💡 讲师批注：也可以不用勾股定理，直接由 $BC = \frac{BE}{\sin 45^\circ} = 2\sqrt{3} \cdot \sqrt{2} = 2\sqrt{6}$，再相减得 $BD = BC - DC = 2\sqrt{6} - (\sqrt{6} + \sqrt{2}) = \sqrt{6} - \sqrt{2}$！**避开了双重根号，快一倍！**

  - **[2] $\sin 75^\circ,\; \cos 75^\circ$ の値**：
    直角三角形 $\triangle ABD$（$\angle ADB = 90^\circ,\; \angle ABD = 75^\circ$）より、
    $$\sin 75^\circ = \frac{AD}{AB} = \frac{\sqrt{6} + \sqrt{2}}{4},\qquad \cos 75^\circ = \frac{BD}{AB} = \frac{\sqrt{6} - \sqrt{2}}{4}$$
- **【最终答案】**
  **[1] $AD = \sqrt{6} + \sqrt{2},\; BD = \sqrt{6} - \sqrt{2}$　　[2] $\sin 75^\circ = \dfrac{\sqrt{6} + \sqrt{2}}{4},\; \cos 75^\circ = \dfrac{\sqrt{6} - \sqrt{2}}{4}$**

---

#### 演習問題 1-(2)
- **【原题重现与翻译】**
  - 原题：$\theta$ は鋭角とする。
    - [1] $\sin\theta = \dfrac{3}{4}$ のとき、$\cos\theta$ と $\tan\theta$ の値を求めよ。
    - [2] $\tan\theta = 3$ のとき、$\sin\theta$ と $\cos\theta$ の値を求めよ。
  - 中文：设 $\theta$ 为锐角。
    - [1] 当 $\sin\theta = \dfrac{3}{4}$ 时，求 $\cos\theta$ 与 $\tan\theta$ 的值。
    - [2] 当 $\tan\theta = 3$ 时，求 $\sin\theta$ 与 $\cos\theta$ 的值。
- **【考点定位】**
  - 锐角三角比相互关系（$\sin^2\theta + \cos^2\theta = 1$、$1 + \tan^2\theta = \dfrac{1}{\cos^2\theta}$）。
- **【分步标准解答】**
  - **[1]** $\theta$ は鋭角であるから $\cos\theta > 0$。
    $$\cos^2\theta = 1 - \sin^2\theta = 1 - \left(\frac{3}{4}\right)^2 = 1 - \frac{9}{16} = \frac{7}{16}$$
    $\cos\theta > 0$ より、$\cos\theta = \dfrac{\sqrt{7}}{4}$。
    $$\tan\theta = \frac{\sin\theta}{\cos\theta} = \frac{\frac{3}{4}}{\frac{\sqrt{7}}{4}} = \frac{3}{\sqrt{7}} = \frac{3\sqrt{7}}{7}$$
  - **[2]** $\theta$ は鋭角であるから $\cos\theta > 0,\; \sin\theta > 0$。
    $$\frac{1}{\cos^2\theta} = 1 + \tan^2\theta = 1 + 3^2 = 10 \implies \cos^2\theta = \frac{1}{10}$$
    $\cos\theta > 0$ より、$\cos\theta = \dfrac{1}{\sqrt{10}} = \dfrac{\sqrt{10}}{10}$。
    $$\sin\theta = \tan\theta \cdot \cos\theta = 3 \cdot \frac{\sqrt{10}}{10} = \frac{3\sqrt{10}}{10}$$
    > 💡 讲师批注：画一个直角边为 $1, 3$、斜边为 $\sqrt{10}$ 的辅助直角三角形，可瞬间口算验算 [2]：$\cos\theta = \frac{1}{\sqrt{10}},\; \sin\theta = \frac{3}{\sqrt{10}}$。
- **【最终答案】**
  **[1] $\cos\theta = \dfrac{\sqrt{7}}{4},\; \tan\theta = \dfrac{3\sqrt{7}}{7}$　　[2] $\sin\theta = \dfrac{3\sqrt{10}}{10},\; \cos\theta = \dfrac{\sqrt{10}}{10}$**

---

### 演習問題 2（三角比の拡張・方程式・対称式・不等式）

#### 演習問題 2-(1)
- **【原题重现与翻译】**
  - 原题：次の表において、(ア)(イ)(ウ)(エ)(オ) の値を求めよ。
    | $\theta$ | $120^\circ$ | $135^\circ$ | $150^\circ$ | $180^\circ$ |
    | :---: | :---: | :---: | :---: | :---: |
    | $\sin\theta$ | (ア) | (b) | (オ) | $0$ |
    | $\cos\theta$ | (イ) | (ウ) | (c) | $-1$ |
    | $\tan\theta$ | (a) | (エ) | (d) | $0$ |
  - 中文：求上表中 (ア)(イ)(ウ)(エ)(オ) 的值。
- **【考点定位】**
  - 钝角特殊角（$120^\circ, 135^\circ, 150^\circ$）的三角比值及补角公式 $180^\circ - \theta$。
- **【分步标准解答】**
  - **(ア)** $\sin 120^\circ = \sin(180^\circ - 60^\circ) = \sin 60^\circ = \dfrac{\sqrt{3}}{2}$
  - **(イ)** $\cos 120^\circ = \cos(180^\circ - 60^\circ) = -\cos 60^\circ = -\dfrac{1}{2}$
  - **(ウ)** $\cos 135^\circ = \cos(180^\circ - 45^\circ) = -\cos 45^\circ = -\dfrac{1}{\sqrt{2}} = -\dfrac{\sqrt{2}}{2}$
  - **(エ)** $\tan 135^\circ = \tan(180^\circ - 45^\circ) = -\tan 45^\circ = -1$
  - **(オ)** $\sin 150^\circ = \sin(180^\circ - 30^\circ) = \sin 30^\circ = \dfrac{1}{2}$
  > 💡 讲师批注：顺便补全表中未问的其余空位方便复习：(a) $\tan 120^\circ = -\sqrt{3}$，(b) $\sin 135^\circ = \frac{1}{\sqrt{2}}$，(c) $\cos 150^\circ = -\frac{\sqrt{3}}{2}$，(d) $\tan 150^\circ = -\frac{1}{\sqrt{3}}$。记忆口诀：**钝角中只有 $\sin$ 为正，$\cos$ 与 $\tan$ 均为负！**
- **【最终答案】**
  **(ア) $\dfrac{\sqrt{3}}{2}$，(イ) $-\dfrac{1}{2}$，(ウ) $-\dfrac{1}{\sqrt{2}}$（或 $-\dfrac{\sqrt{2}}{2}$），(エ) $-1$，(オ) $\dfrac{1}{2}$**

---

#### 演習問題 2-(2)
- **【原题重现与翻译】**
  - 原题：次の式の値を求めよ。ただし、$0^\circ \le \theta \le 90^\circ,\; \sin\theta = \dfrac{1}{3}$ とする。
    - [1] $\cos(90^\circ - \theta) + \cos\theta + \cos(90^\circ + \theta) - \sin(90^\circ + \theta)$
    - [2] $\sin(180^\circ - \theta) + \cos\theta + \cos(180^\circ - \theta) - \sin\theta$
  - 中文：求下列各式的值（其中 $0^\circ \le \theta \le 90^\circ,\; \sin\theta = \dfrac{1}{3}$）。
- **【考点定位】**
  - $90^\circ \pm \theta$ 与 $180^\circ - \theta$ 诱导公式的化简。
- **【分步标准解答】**
  - **[1]** 公式 $\cos(90^\circ - \theta) = \sin\theta$、$\cos(90^\circ + \theta) = -\sin\theta$、$\sin(90^\circ + \theta) = \cos\theta$ より、
    $$(\text{与式}) = \sin\theta + \cos\theta + (-\sin\theta) - \cos\theta = 0$$
  - **[2]** 公式 $\sin(180^\circ - \theta) = \sin\theta$、$\cos(180^\circ - \theta) = -\cos\theta$ より、
    $$(\text{与式}) = \sin\theta + \cos\theta + (-\cos\theta) - \sin\theta = 0$$
  > 💡 讲师批注：两小题化简后竟然全部抵消为 $0$，根本用不到条件 $\sin\theta = \frac{1}{3}$！千万不要先急着求 $\cos\theta = \frac{2\sqrt{2}}{3}$ 再代入，先化简再代值是三角恒等变形的铁律。
- **【最终答案】**
  **[1] $0$　　[2] $0$**

---

#### 演習問題 2-(3)
- **【原题重现与翻译】**
  - 原题：$2\cos^2\theta + 3\sin\theta - 3 = 0$ ($0^\circ \le \theta \le 180^\circ$)（方程式を解け）
  - 中文：解方程 $2\cos^2\theta + 3\sin\theta - 3 = 0$（$0^\circ \le \theta \le 180^\circ$）。
- **【考点定位】**
  - 统一三角比名称（$\cos^2\theta = 1 - \sin^2\theta$）+ 解三角二次方程。
- **【分步标准解答】**
  $\cos^2\theta = 1 - \sin^2\theta$ を代入して $\sin\theta$ に統一する。
  $$2(1 - \sin^2\theta) + 3\sin\theta - 3 = 0$$
  $$-2\sin^2\theta + 3\sin\theta - 1 = 0 \iff 2\sin^2\theta - 3\sin\theta + 1 = 0$$
  $$(2\sin\theta - 1)(\sin\theta - 1) = 0$$
  よって、$\sin\theta = \dfrac{1}{2}$ または $\sin\theta = 1$。
  $0^\circ \le \theta \le 180^\circ$ の範囲で、
  - $\sin\theta = \dfrac{1}{2} \implies \theta = 30^\circ,\; 150^\circ$
  - $\sin\theta = 1 \implies \theta = 90^\circ$
  > 💡 讲师批注：在 $0^\circ \le \theta \le 180^\circ$ 内，看到 $\sin\theta = k$（$0 < k < 1$），**永远有锐角和钝角两个互补解**（如 $30^\circ$ 和 $150^\circ$），切勿漏掉钝角解！
- **【最终答案】**
  **$\theta = 30^\circ,\; 90^\circ,\; 150^\circ$**

---

#### 演習問題 2-(4)
- **【原题重现与翻译】**
  - 原题：$\sin\theta\tan\theta = -\dfrac{3}{2}$ ($90^\circ < \theta \le 180^\circ$)（方程式を解け）
  - 中文：解方程 $\sin\theta\tan\theta = -\dfrac{3}{2}$（$90^\circ < \theta \le 180^\circ$）。
- **【考点定位】**
  - 切化弦（$\tan\theta = \dfrac{\sin\theta}{\cos\theta}$）+ 转化为关于 $\cos\theta$ 的二次方程 + 范围筛选。
- **【分步标准解答】**
  $90^\circ < \theta \le 180^\circ$ より $-1 \le \cos\theta < 0$（特に $\cos\theta \neq 0$）である。
  $\tan\theta = \dfrac{\sin\theta}{\cos\theta}$ を代入すると、
  $$\sin\theta \cdot \frac{\sin\theta}{\cos\theta} = -\frac{3}{2} \iff \frac{\sin^2\theta}{\cos\theta} = -\frac{3}{2}$$
  両辺に $2\cos\theta$ を掛けて、$\sin^2\theta = 1 - \cos^2\theta$ を代入すると、
  $$2(1 - \cos^2\theta) = -3\cos\theta \iff 2\cos^2\theta - 3\cos\theta - 2 = 0$$
  $$(2\cos\theta + 1)(\cos\theta - 2) = 0$$
  よって、$\cos\theta = -\dfrac{1}{2}$ または $\cos\theta = 2$。
  $-1 \le \cos\theta < 0$ より、$\cos\theta = -\dfrac{1}{2}$ のみが適する。
  したがって、$\theta = 120^\circ$。
  > 💡 讲师批注：代回原式验算：$\sin 120^\circ \tan 120^\circ = \frac{\sqrt{3}}{2} \cdot (-\sqrt{3}) = -\frac{3}{2}$，完美吻合！
- **【最终答案】**
  **$\theta = 120^\circ$**

---

#### 演習問題 2-(5)
- **【原题重现与翻译】**
  - 原题：$\sin\theta + \cos\theta = \dfrac{\sqrt{2}}{2}$ ($0^\circ < \theta < 180^\circ$) のとき、次の式の値を求めよ。
    - [1] $\sin\theta\cos\theta,\quad \sin^3\theta + \cos^3\theta$
    - [2] $\sin\theta - \cos\theta,\quad \tan\theta - \dfrac{1}{\tan\theta}$
  - 中文：已知 $\sin\theta + \cos\theta = \dfrac{\sqrt{2}}{2}$（$0^\circ < \theta < 180^\circ$），求下列各式的值：
    - [1] $\sin\theta\cos\theta$ 与 $\sin^3\theta + \cos^3\theta$
    - [2] $\sin\theta - \cos\theta$ 与 $\tan\theta - \dfrac{1}{\tan\theta}$
- **【考点定位】**
  - $\sin\theta \pm \cos\theta$ 与 $\sin\theta\cos\theta$ 的对称式转化 + **利用乘积符号判定 $\sin\theta - \cos\theta$ 的正负**（最高频陷阱！）。
- **【分步标准解答】**
  - **[1]** 与えられた式の両辺を 2 乗すると、
    $$(\sin\theta + \cos\theta)^2 = \left(\frac{\sqrt{2}}{2}\right)^2 \iff \sin^2\theta + 2\sin\theta\cos\theta + \cos^2\theta = \frac{1}{2}$$
    $\sin^2\theta + \cos^2\theta = 1$ より、
    $$1 + 2\sin\theta\cos\theta = \frac{1}{2} \iff 2\sin\theta\cos\theta = -\frac{1}{2} \iff \sin\theta\cos\theta = -\frac{1}{4}$$
    次に、$a^3 + b^3 = (a + b)^3 - 3ab(a + b)$ を用いて、
    $$\sin^3\theta + \cos^3\theta = (\sin\theta + \cos\theta)^3 - 3\sin\theta\cos\theta(\sin\theta + \cos\theta)$$
    $$= \left(\frac{\sqrt{2}}{2}\right)^3 - 3\left(-\frac{1}{4}\right)\left(\frac{\sqrt{2}}{2}\right) = \frac{2\sqrt{2}}{8} + \frac{3\sqrt{2}}{8} = \frac{5\sqrt{2}}{8}$$

  - **[2]** まず $(\sin\theta - \cos\theta)^2$ を計算する：
    $$(\sin\theta - \cos\theta)^2 = \sin^2\theta - 2\sin\theta\cos\theta + \cos^2\theta = 1 - 2\left(-\frac{1}{4}\right) = \frac{3}{2}$$
    ここで符号を調べる：$0^\circ < \theta < 180^\circ$ より $\sin\theta > 0$。
    さらに [1] より $\sin\theta\cos\theta = -\dfrac{1}{4} < 0$ であるから、$\cos\theta < 0$ である。
    よって、$\sin\theta - \cos\theta = (\text{正}) - (\text{負}) > 0$ となる。
    > 💡 讲师批注：开方前**必须判定符号**！若直接写成 $\pm\frac{\sqrt{6}}{2}$ 会被扣分。由 $\sin\theta > 0$ 且 $\sin\theta\cos\theta < 0$ 推得 $\cos\theta < 0$，从而锁定 $\sin\theta - \cos\theta > 0$！

    したがって、
    $$\sin\theta - \cos\theta = \sqrt{\frac{3}{2}} = \frac{\sqrt{6}}{2}$$
    最後に、$\tan\theta = \dfrac{\sin\theta}{\cos\theta}$ を用いて通分すると、
    $$\tan\theta - \frac{1}{\tan\theta} = \frac{\sin\theta}{\cos\theta} - \frac{\cos\theta}{\sin\theta} = \frac{\sin^2\theta - \cos^2\theta}{\sin\theta\cos\theta} = \frac{(\sin\theta + \cos\theta)(\sin\theta - \cos\theta)}{\sin\theta\cos\theta}$$
    $$= \frac{\dfrac{\sqrt{2}}{2} \cdot \dfrac{\sqrt{6}}{2}}{-\dfrac{1}{4}} = \frac{\dfrac{2\sqrt{3}}{4}}{-\dfrac{1}{4}} = -2\sqrt{3}$$
- **【最终答案】**
  **[1] $\sin\theta\cos\theta = -\dfrac{1}{4},\; \sin^3\theta + \cos^3\theta = \dfrac{5\sqrt{2}}{8}$　　[2] $\sin\theta - \cos\theta = \dfrac{\sqrt{6}}{2},\; \tan\theta - \dfrac{1}{\tan\theta} = -2\sqrt{3}$**

---

#### 演習問題 2-(6)
- **【原题重现与翻译】**
  - 原题：$0^\circ \le \theta \le 180^\circ$ のとき、次の不等式を解け。
    - [1] $2\sin^2\theta - \cos\theta - 1 \le 0$
    - [2] $2\cos^2\theta + 3\sin\theta < 3$
  - 中文：当 $0^\circ \le \theta \le 180^\circ$ 时，解下列不等式：
    - [1] $2\sin^2\theta - \cos\theta - 1 \le 0$
    - [2] $2\cos^2\theta + 3\sin\theta < 3$
  > ⚠️ **教材勘误提示**：原教材第 89 页（`page_0090.jpg`）将 $0^\circ \le \theta \le 180^\circ$ 中的 $0^\circ$ 漏印了度数符号，写作 $0 \le \theta \le 180^\circ$。
- **【考点定位】**
  - 三角二次不等式 + 单位半圆数形结合 + **端点孤立解检验（$\theta = 180^\circ$）**。
- **【图解辅助（SVG 矢量图）】**
  <svg viewBox="0 0 420 175" width="420" height="175" xmlns="http://www.w3.org/2000/svg" style="background:#fff;border:1px solid #e2e8f0;border-radius:6px;">
    <!-- 左图：[1] cosθ >= 1/2 或 cosθ = -1 -->
    <text x="52" y="18" font-size="11" fill="#1e293b" font-weight="bold">[1] cosθ ≥ 1/2 または cosθ = -1</text>
    <line x1="20" y1="140" x2="195" y2="140" stroke="#334155" stroke-width="1.3"/>
    <line x1="107" y1="155" x2="107" y2="35" stroke="#334155" stroke-width="1.3"/>
    <path d="M 37 140 A 70 70 0 0 1 177 140" fill="none" stroke="#94a3b8" stroke-width="1.8"/>
    <!-- 高亮弧 0° <= θ <= 60°: 从(177,140)到(142,79.4) -->
    <path d="M 177 140 A 70 70 0 0 0 142 79.4" fill="none" stroke="#2563eb" stroke-width="3.5"/>
    <line x1="107" y1="140" x2="142" y2="79.4" stroke="#2563eb" stroke-width="1.3" stroke-dasharray="3,2"/>
    <line x1="142" y1="79.4" x2="142" y2="140" stroke="#2563eb" stroke-width="1.1" stroke-dasharray="3,2"/>
    <circle cx="142" cy="79.4" r="3.8" fill="#2563eb"/>
    <circle cx="177" cy="140" r="3.8" fill="#2563eb"/>
    <!-- 孤立点 θ=180° -->
    <circle cx="37" cy="140" r="4.5" fill="#dc2626"/>
    <text x="15" y="128" font-size="10" fill="#dc2626" font-weight="bold">θ=180°(孤立解!)</text>
    <text x="148" y="75" font-size="10" fill="#2563eb" font-weight="bold">60°</text>
    <text x="135" y="154" font-size="10" fill="#2563eb">1/2</text>
    <text x="178" y="154" font-size="10" fill="#334155">1</text>
    <text x="27" y="154" font-size="10" fill="#334155">-1</text>

    <!-- 右图：[2] 0 <= sinθ < 1/2 -->
    <text x="262" y="18" font-size="11" fill="#1e293b" font-weight="bold">[2] 0 ≤ sinθ &lt; 1/2</text>
    <line x1="225" y1="140" x2="400" y2="140" stroke="#334155" stroke-width="1.3"/>
    <line x1="312" y1="155" x2="312" y2="35" stroke="#334155" stroke-width="1.3"/>
    <path d="M 242 140 A 70 70 0 0 1 382 140" fill="none" stroke="#94a3b8" stroke-width="1.8"/>
    <!-- y = 1/2 水平线: y = 140 - 35 = 105; x = 312 ± 60.6 => 251.4, 372.6 -->
    <line x1="235" y1="105" x2="390" y2="105" stroke="#16a34a" stroke-width="1.2" stroke-dasharray="3,2"/>
    <text x="315" y="101" font-size="10" fill="#16a34a">1/2</text>
    <!-- 高亮弧 0° <= θ < 30° 与 150° < θ <= 180° -->
    <path d="M 382 140 A 70 70 0 0 0 372.6 105" fill="none" stroke="#16a34a" stroke-width="3.5"/>
    <path d="M 251.4 105 A 70 70 0 0 0 242 140" fill="none" stroke="#16a34a" stroke-width="3.5"/>
    <circle cx="382" cy="140" r="3.8" fill="#16a34a"/>
    <circle cx="242" cy="140" r="3.8" fill="#16a34a"/>
    <circle cx="372.6" cy="105" r="3.8" fill="#fff" stroke="#16a34a" stroke-width="2"/>
    <circle cx="251.4" cy="105" r="3.8" fill="#fff" stroke="#16a34a" stroke-width="2"/>
    <text x="378" y="101" font-size="10" fill="#16a34a" font-weight="bold">30°</text>
    <text x="223" y="101" font-size="10" fill="#16a34a" font-weight="bold">150°</text>
  </svg>
- **【分步标准解答】**
  - **[1] $2\sin^2\theta - \cos\theta - 1 \le 0$**：
    $\sin^2\theta = 1 - \cos^2\theta$ を代入して $\cos\theta$ に統一する：
    $$2(1 - \cos^2\theta) - \cos\theta - 1 \le 0 \iff -2\cos^2\theta - \cos\theta + 1 \le 0$$
    両辺に $-1$ を掛けて（不等号の向きが変わる）：
    $$2\cos^2\theta + \cos\theta - 1 \ge 0 \iff (2\cos\theta - 1)(\cos\theta + 1) \ge 0$$
    よって、$\cos\theta \le -1$ または $\cos\theta \ge \dfrac{1}{2}$。
    $0^\circ \le \theta \le 180^\circ$ より $-1 \le \cos\theta \le 1$ であるから、
    $$\cos\theta = -1 \quad \text{または} \quad \frac{1}{2} \le \cos\theta \le 1$$
    - $\cos\theta = -1 \implies \theta = 180^\circ$
    - $\dfrac{1}{2} \le \cos\theta \le 1 \implies 0^\circ \le \theta \le 60^\circ$
    > 💡 讲师批注：**全切片最容易丢分的神坑！** 很多同学看到 $\cos\theta \le -1$ 以为「超范围了直接舍去」，却忘了 **$-1$ 恰好能取到等号**（$\theta = 180^\circ$ 时原不等式左边 $= 0 \le 0$ 成立）！写完二次不等式解集后，务必与 $[-1, 1]$ 逐一取交集！

  - **[2] $2\cos^2\theta + 3\sin\theta < 3$**：
    $\cos^2\theta = 1 - \sin^2\theta$ を代入して $\sin\theta$ に統一する：
    $$2(1 - \sin^2\theta) + 3\sin\theta < 3 \iff -2\sin^2\theta + 3\sin\theta - 1 < 0$$
    両辺に $-1$ を掛けて：
    $$2\sin^2\theta - 3\sin\theta + 1 > 0 \iff (2\sin\theta - 1)(\sin\theta - 1) > 0$$
    よって、$\sin\theta < \dfrac{1}{2}$ または $\sin\theta > 1$。
    $0^\circ \le \theta \le 180^\circ$ より $0 \le \sin\theta \le 1$ であるから、共通範囲は
    $$0 \le \sin\theta < \frac{1}{2}$$
    単位半円より、
    $$0^\circ \le \theta < 30^\circ,\qquad 150^\circ < \theta \le 180^\circ$$
    > 💡 讲师批注：注意端点 $0^\circ$ 与 $180^\circ$ 处 $\sin\theta = 0 < \frac{1}{2}$，均满足严格不等号，故两端为闭区间（$\le$）；而 $30^\circ$ 与 $150^\circ$ 处取等号，故为开区间（$<$）。
- **【最终答案】**
  **[1] $0^\circ \le \theta \le 60^\circ,\; \theta = 180^\circ$　　[2] $0^\circ \le \theta < 30^\circ,\; 150^\circ < \theta \le 180^\circ$**
