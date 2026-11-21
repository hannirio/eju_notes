# 《EJU 教材全解与备课讲义》数学 023（上：P331–P337）

> **对应源文件**：`work_math/ocr_md/ocr_023_p331-345.md`（上册：微分法的应用之「関数の増減と値の変化」「関数のグラフ（凹凸・変曲点・漸近線）」全切片知识综述与核心词汇，以及 **演習問題 10 (1)–(11)**；下册 `note_023_b.md` 承接 **演習問題 10 (12)–(21)** 与 **演習問題 11 (1)**）
> **视觉核对参考图**：`work_math/ref_imgs/page_0331.jpg` – `page_0345.jpg`（全 15 页逐页核对）

---

## 一、国内高中基础知识点唤醒与 EJU 考纲差异对比

本切片对应日本高中数学 **数学Ⅱ（微分法の応用）** 与 **数学Ⅲ（微分法の応用：関数の値の変化・グラフの概形）** 的核心内容，涵盖 **函数单调性与极值、闭区间最值、三次函数极值分类、曲线凹凸性与拐点、二阶导数判别极值、渐近线的求法** 六大板块。

### 1.1 函数的增减（单调性）与极值（関数の増減と極値）

- **单调递增与单调递减（単調に増加・減少）**：
  对于区间内任意两数 $u, v$：
  - $u < v \implies f(u) < f(v)$，称 $f(x)$ 在该区间**单调递增（単調に増加）**；
  - $u < v \implies f(u) > f(v)$，称 $f(x)$ 在该区间**单调递减（単調に減少）**。
- **导数符号与单调性**：
  - 在某区间内 $f'(x) > 0 \implies f(x)$ 单调递增（图像右上がり）；
  - 在某区间内 $f'(x) < 0 \implies f(x)$ 单调递减（图像右下がり）；
  - 若 $f'(x) \ge 0$ 且 $f'(x) = 0$ 仅在孤立点成立（如 $y = x^3$ 在 $x=0$ 处），函数依然在整个区间单调递增。
- **极值的定义（極大値・極小値）**：
  在 $x = a$ 的附近（$x \neq a$）：
  - 若恒有 $f(x) < f(a)$，则称 $f(x)$ 在 $x = a$ 处取**极大（極大）**，$f(a)$ 为**极大值（極大値）**；
  - 若恒有 $f(x) > f(a)$，则称 $f(x)$ 在 $x = a$ 处取**极小（極小）**，$f(a)$ 为**极小值（極小値）**。
  - **注意**：不可微点（如尖点 $|x|$ 在 $x=0$ 处）只要连续且左右单调性相反，依然可以取得极值！
- **极值 vs. 最值（最大・最小と極大・極小）**：
  - 极值是**局部概念**（ごく近くでの最大・最小），最值是**全局概念**（区間全体での最大・最小）。
  - 在**闭区间（閉区間）** $a \le x \le b$ 上，连续函数必有最大值与最小值，求法为：**列出增减表 $\to$ 比较所有极值与区间两端点的值**。

### 1.2 三次函数与极值（3次関数と極値）

对于三次函数 $f(x) = ax^3 + bx^2 + cx + d$（$a \neq 0$），其导函数为 $f'(x) = 3ax^2 + 2bx + c$。设方程 $f'(x) = 0$ 的判别式为 $D$，则：
$$\frac{D}{4} = b^2 - 3ac$$

| 判别式 $D$ | $f'(x) = 0$ 的解 | 极值有无 | $a > 0$ 图像特征 | $a < 0$ 图像特征 |
| :---: | :---: | :---: | :--- | :--- |
| **$D > 0$** | 两个不同实数解 $\alpha, \beta$（$\alpha < \beta$） | **有极值** | $x=\alpha$ 极大，$x=\beta$ 极小 | $x=\alpha$ 极小，$x=\beta$ 极大 |
| **$D = 0$** | 重根 $\alpha = -\dfrac{b}{3a}$ | **无极值** | $f'(x) \ge 0$，单调递增（在 $\alpha$ 处切线水平） | $f'(x) \le 0$，单调递减（在 $\alpha$ 处切线水平） |
| **$D < 0$** | 无实数解（虚数解） | **无极值** | $f'(x) > 0$，严格单调递增 | $f'(x) < 0$，严格单调递减 |

> ⚠️ **教材勘误提示**：原教材第 331 页（`page_0332.jpg`）存在 4 处印刷错误，备课与授课时务必修正：
> 1. 正文 ② 将 `$D=0$ ならば、$f'(x)=0$ は重解をもつ` 误印为 `異なる2つの実数解をもつ`；
> 2. 正文 ③ 将 `$D<0$ ならば` 误印为 `$D>0$ ならば`；
> 3. 底部汇总表 `$D>0$` 列将 `$\alpha < \beta$` 误印为 `$\alpha > \beta$`；
> 4. 汇总表 `$D=0, D<0$` 列将 `極値がない` 误印为 `極値かない`（漏浊点）。

### 1.3 曲线的凹凸性、拐点与二阶导数（曲線の凹凸・変曲点・第2次導関数）

- **曲线的凹凸性（曲線の凹凸）**：
  设 $f(x)$ 存在二阶导函数 $f''(x)$：
  - $f''(x) > 0$ 的区间 $\implies f'(x)$ 递增 $\implies$ 曲线 $y = f(x)$ **向下凸（下に凸）**（形如 $\cup$，切线在曲线下方，弦在曲线上方）；
  - $f''(x) < 0$ 的区间 $\implies f'(x)$ 递减 $\implies$ 曲线 $y = f(x)$ **向上凸（上に凸）**（形如 $\cap$，切线在曲线上方，弦在曲线下方）。
  > ⚠️ **教材勘误提示**：原教材第 341 页（`page_0342.jpg`）`[12.1]` ① 正文将两行误印为 `$f''(x)>0$ ... 下に凹` 与 `$f''(x)<0$ ... 下に凸`，**完全颠倒/错字**！正确应为：$f''(x) > 0$ 为**下に凸**，$f''(x) < 0$ 为**上に凸**（与同页右侧插图及第 342 页解説(1)一致）。
- **拐点 / 变曲点（変曲点）**：
  - 凹凸性发生改变的点。若 $f''(a) = 0$ 且在 $x=a$ 两侧 $f''(x)$ **变号**，则 $(a, f(a))$ 是拐点。
  - **逆命题不成立**：$f''(a) = 0$ 未必是拐点（反例：$f(x) = x^4$ 在 $x=0$ 处 $f''(0)=0$，但两侧 $f''(x)=12x^2 > 0$ 不变号，故 $(0,0)$ 不是拐点）。
- **二阶导数判别极值（第2次導関数と極値）**：
  设 $f''(x)$ 在 $x=a$ 附近连续：
  - $f'(a) = 0$ 且 $f''(a) < 0 \implies f(a)$ 为**极大值**；
  - $f'(a) = 0$ 且 $f''(a) > 0 \implies f(a)$ 为**极小值**；
  - 若 $f'(a) = 0$ 且 $f''(a) = 0$，则**无法仅由此判定**，需回归一阶导数符号变化（增减表）。

### 1.4 函数草图绘制六步法与渐近线（グラフの概形と漸近線）

绘制复杂函数草图（数学Ⅲ重点）的 6 个检查维度：① **定義域**（定义域）$\to$ ② **対称性**（偶/奇函数等）$\to$ ③ **増減と極値**（$y'$ 符号）$\to$ ④ **凹凸と変曲点**（$y''$ 符号）$\to$ ⑤ **座標軸との共有点**（截距）$\to$ ⑥ **漸近線**（渐近线）。

- **渐近线的三类求法**：
  1. **平行于 $x$ 轴（水平渐近线）**：$\lim_{x\to\infty} f(x) = a$ 或 $\lim_{x\to -\infty} f(x) = a \implies$ 直线 $y = a$。
  2. **垂直于 $x$ 轴（铅直渐近线）**：$\lim_{x\to b \pm 0} f(x) = \pm\infty \implies$ 直线 $x = b$。
  3. **斜渐近线**：$\lim_{x\to \pm\infty} \{f(x) - (ax+b)\} = 0 \implies$ 直线 $y = ax + b$，其中：
     $$a = \lim_{x\to\pm\infty} \frac{f(x)}{x}, \qquad b = \lim_{x\to\pm\infty} \{f(x) - ax\}$$

### 1.5 国内高中 vs. 日本 EJU 考纲差异与符号习惯

| 对比维度 | 国内高中习惯 | 日本 EJU 习惯 | 备课/应试提醒 |
| :--- | :--- | :--- | :--- |
| **自然对数记号** | $\ln x$（$\lg x$ 表示常用对数） | **$\log x$** 直接表示自然对数 $\log_e x$ | **最高频坑点！** 见演習問題 10 (21) 中的 $\log x$，在微积分章节一律默认底数为 $e$ |
| **单调性表格** | 列表写「增」「减」文字 | 严格画 **増減表（ぞうげんひょう）**，用箭头 $\nearrow$、$\searrow$ 表示 | 数学Ⅲ画含凹凸的增减表时，多加一行 $y''$，箭头可用弯曲箭头 |
| **凹凸性术语** | 国内教材多称「下凸 / 上凸」或「凹 / 凸」（不同教材定义甚至相反！） | 日本绝对统一：**下に凸（$\cup$，向下鼓）** 与 **上に凸（$\cap$，向上鼓）** | 日本的「下に凸 / 上に凸」极其直观，牢记 $f''>0 \Leftrightarrow$ 下に凸 |
| **拐点术语** | 称「拐点」（高中考纲几乎不考） | 称 **変曲点（へんきょくてん）**，**数学Ⅲ必考** | 必考 $y''=0$ 且变号，注意检验是否变号 |
| **斜渐近线** | 高中不要求 | **数学Ⅲ常规考点** | 分式函数先做多项式除法（如 $\frac{x^2+3x+9}{x+3} = x + \frac{9}{x+3}$），直接读出斜渐近线 $y=x$ |
| **三次函数对称性** | 选修拓展性质 | 日本考题高频直接设问（如演習問題 10 (8)） | 牢记三次函数关于拐点 $\left(-\frac{b}{3a}, f\left(-\frac{b}{3a}\right)\right)$ 中心对称 |

---

## 二、日文核心词汇与公式假名注音

### 2.1 本切片日文核心词汇

- 単調に増加（たんちょうにぞうか / tanchou ni zouka） — 单调递增（亦作 単調増加 / たんちょうぞうか）
- 単調に減少（たんちょうにげんしょう / tanchou ni genshou） — 单调递减（亦作 単調減少 / たんちょうげんしょう）
- 関数の増減（かんすうのぞうげん / kansuu no zougen） — 函数的增减性（单调性）
- 増減表（ぞうげんひょう / zougenhyou） — 增减表（单调性与极值表）
- 極値（きょくち / kyokuchi） — 极值（极大值与极小值的统称）
- 極大（きょくだい / kyokudai） — 极大
- 極大値（きょくだいち / kyokudaichi） — 极大值
- 極小（きょくしょう / kyokushou） — 极小
- 極小値（きょくしょうち / kyokushouchi） — 极小值
- 3次関数（さんじかんすう / sanji kansuu） — 三次函数
- 4次関数（よじかんすう / yoji kansuu） — 四次函数
- 同符号（どうふごう / doufugou） — 同号（符号相同）
- 凹凸（おうとつ / outotsu） — 凹凸性（曲线的弯曲方向）
- 変曲点（へんきょくてん / henkyokuten） — 拐点（变曲点）
- 第2次導関数（だいにじどうかんすう / dainiji doukansuu） — 二阶导函数（亦作 第二次導関数）
- 対称性（たいしょうせい / taishousei） — 对称性
- 原点対称（げんてんたいしょう / genten taishou） — 关于原点对称
- 微分不可能（びぶんふかのう / bibun fukanou） — 不可微（不可导）

### 2.2 核心公式的日本课堂口语读法

1. **一阶导数与二阶导数** $f'(x),\; f''(x)$
   - 课堂读法：**エフ ダッシュ エックス**（$f'(x)$）、**エフ ツーダッシュ エックス**（$f''(x)$，也读作 **エフ ダブルダッシュ エックス**）。
   - 备注：日本高中课堂习惯将撇号 `'` 读作 **ダッシュ（dash）**，而非英语的 prime。
2. **凹凸性判定** $f''(x) > 0 \implies$ 曲線 $y=f(x)$ は下に凸
   - 课堂读法：**エフ ツーダッシュ エックス だいなり ゼロ ならば、きょくせん ワイ イコール エフ エックス は した に とつ**。
3. **斜渐近线极限式** $\lim_{x\to\infty} \{f(x) - (ax+b)\} = 0$
   - 课堂读法：**リミット エックス やじるし むげんだい、ちゅうかっこ エフ エックス ひく かっこ エーエックス たす ビー かっことじ ちゅうかっことじ イコール ゼロ**。
4. **三次函数判别式** $\dfrac{D}{4} = b^2 - 3ac$
   - 课堂读法：**よん ぶんの ディー イコール ビーのにじょう ひく さんエーシー**。

---

## 三、逐题深度解析（上：演習問題 10 (1)–(11)）

---

### 演習問題 10 (1)

- **【原题重现与翻译】**
  - 原题：次の関数の増減を調べよ。また、その極値を求め、グラフの概形も描け。
    $[1]\; y = x^3 + 3x^2 - 9x \qquad [2]\; y = -\dfrac{1}{3}x^3 + x^2 - x + 2$
  - 中文：讨论下列函数的增减性，求其极值，并画出函数草图。
- **【考点定位】**
  - 三次函数的求导、増減表（增减表）、判别式 $D>0$（有极值）与 $D=0$（无极值）的典型对比。

#### $[1]\; y = x^3 + 3x^2 - 9x$
- **【图解辅助（SVG 矢量图）】**

<svg viewBox="0 0 420 260" xmlns="http://www.w3.org/2000/svg" style="max-width:420px;display:block;margin:10px auto;background:#fafafa;border:1px solid #e0e0e0;border-radius:6px;">
  <defs>
    <marker id="arr1a" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0,0 L0,6 L6,3 z" fill="#333"/></marker>
  </defs>
  <!-- Axes -->
  <line x1="30" y1="180" x2="390" y2="180" stroke="#333" stroke-width="1.5" marker-end="url(#arr1a)"/>
  <line x1="250" y1="245" x2="250" y2="18" stroke="#333" stroke-width="1.5" marker-end="url(#arr1a)"/>
  <text x="392" y="184" font-size="13" font-style="italic" fill="#333">x</text>
  <text x="256" y="24" font-size="13" font-style="italic" fill="#333">y</text>
  <text x="236" y="196" font-size="12" fill="#333">O</text>
  <!-- Cubic curve: O=(250,180), x=-3 -> (130, 45) max 27, x=1 -> (290, 205) min -5 -->
  <path d="M 65,245 C 88,120 105,45 130,45 C 165,45 210,120 250,180 C 268,205 278,205 290,205 C 315,205 335,140 355,35" fill="none" stroke="#1565c0" stroke-width="2.5"/>
  <!-- Dashed guides -->
  <line x1="130" y1="45" x2="130" y2="180" stroke="#888" stroke-dasharray="4,3"/>
  <line x1="130" y1="45" x2="250" y2="45" stroke="#888" stroke-dasharray="4,3"/>
  <line x1="290" y1="205" x2="290" y2="180" stroke="#888" stroke-dasharray="4,3"/>
  <line x1="290" y1="205" x2="250" y2="205" stroke="#888" stroke-dasharray="4,3"/>
  <!-- Points -->
  <circle cx="130" cy="45" r="4" fill="#d32f2f"/>
  <circle cx="290" cy="205" r="4" fill="#d32f2f"/>
  <circle cx="250" cy="180" r="3.5" fill="#1565c0"/>
  <!-- Labels -->
  <text x="122" y="196" font-size="12" fill="#333">-3</text>
  <text x="256" y="49" font-size="12" fill="#333">27</text>
  <text x="286" y="173" font-size="12" fill="#333">1</text>
  <text x="230" y="210" font-size="12" fill="#333">-5</text>
  <text x="72" y="36" font-size="12" fill="#d32f2f" font-weight="bold">極大 (-3, 27)</text>
  <text x="298" y="220" font-size="12" fill="#d32f2f" font-weight="bold">極小 (1, -5)</text>
</svg>

- **【分步标准解答】**
  1. 微分して導関数を求める：
     $$y' = 3x^2 + 6x - 9 = 3(x^2 + 2x - 3) = 3(x + 3)(x - 1)$$
     > 💡 讲师批注：先提公因数 $3$ 再十字相乘，避免直接分解 $3x^2+6x-9$ 时算错。
  2. $y' = 0$ とすると $x = -3,\; 1$。極値を計算する：
     - $x = -3$ のとき：$y = (-3)^3 + 3(-3)^2 - 9(-3) = -27 + 27 + 27 = 27$
     - $x = 1$ のとき：$y = 1^3 + 3(1)^2 - 9(1) = 1 + 3 - 9 = -5$
     - また $x = 0$ のとき $y = 0$（原点を通る）。
     > 💡 讲师批注：画草图时务必顺手算出 $y$ 截距（$x=0$ 的值），确保曲线穿过坐标轴的位置准确。
  3. 増減表をかく：

     | $x$ | $\cdots$ | $-3$ | $\cdots$ | $1$ | $\cdots$ |
     | :---: | :---: | :---: | :---: | :---: | :---: |
     | $y'$ | $+$ | $0$ | $-$ | $0$ | $+$ |
     | $y$ | $\nearrow$ | $27$（極大） | $\searrow$ | $-5$（極小） | $\nearrow$ |

     > 💡 讲师批注：$y'$ 是开口向上的二次函数，两根之外为 $+$，两根之间为 $-$。
- **【最终答案】**
  - **増減**：$x \le -3,\; x \ge 1$ で増加、$-3 \le x \le 1$ で減少。
  - **極値**：**$x = -3$ で極大値 $27$、$x = 1$ で極小値 $-5$**（草图见上）。

#### $[2]\; y = -\dfrac{1}{3}x^3 + x^2 - x + 2$
- **【图解辅助（SVG 矢量图）】**

<svg viewBox="0 0 380 240" xmlns="http://www.w3.org/2000/svg" style="max-width:380px;display:block;margin:10px auto;background:#fafafa;border:1px solid #e0e0e0;border-radius:6px;">
  <defs>
    <marker id="arr1b" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0,0 L0,6 L6,3 z" fill="#333"/></marker>
  </defs>
  <line x1="40" y1="185" x2="350" y2="185" stroke="#333" stroke-width="1.5" marker-end="url(#arr1b)"/>
  <line x1="140" y1="225" x2="140" y2="18" stroke="#333" stroke-width="1.5" marker-end="url(#arr1b)"/>
  <text x="354" y="189" font-size="13" font-style="italic" fill="#333">x</text>
  <text x="146" y="24" font-size="13" font-style="italic" fill="#333">y</text>
  <text x="125" y="200" font-size="12" fill="#333">O</text>
  <!-- y = -1/3(x-1)^3 + 5/3; (0,2) -> (140, 105), (1, 5/3) -> (200, 118) -->
  <path d="M 85,25 C 110,85 155,118 200,118 C 245,118 285,155 315,220" fill="none" stroke="#1565c0" stroke-width="2.5"/>
  <!-- Horizontal tangent at x=1 -->
  <line x1="165" y1="118" x2="235" y2="118" stroke="#d32f2f" stroke-width="1.2" stroke-dasharray="4,3"/>
  <line x1="200" y1="118" x2="200" y2="185" stroke="#888" stroke-dasharray="4,3"/>
  <line x1="140" y1="118" x2="200" y2="118" stroke="#888" stroke-dasharray="4,3"/>
  <circle cx="200" cy="118" r="4" fill="#d32f2f"/>
  <circle cx="140" cy="105" r="3.5" fill="#1565c0"/>
  <text x="196" y="200" font-size="12" fill="#333">1</text>
  <text x="115" y="122" font-size="12" fill="#333">5/3</text>
  <text x="126" y="102" font-size="12" fill="#333">2</text>
  <text x="215" y="108" font-size="12" fill="#d32f2f">y'=0（単調減少・極値なし）</text>
</svg>

- **【分步标准解答】**
  1. 微分する：
     $$y' = -x^2 + 2x - 1 = -(x - 1)^2 \le 0$$
     > 💡 讲师批注：$y'$ 配方后恒非正，仅在 $x=1$ 一点处等于 $0$。
  2. $y' = 0$ となるのは $x = 1$ のみであり、$x = 1$ の前後で $y'$ の符号は変化しない（負のまま）。
     - $x = 1$ のとき $y = -\dfrac{1}{3} + 1 - 1 + 2 = \dfrac{5}{3}$、$x = 0$ のとき $y = 2$。
  3. 増減表：

     | $x$ | $\cdots$ | $1$ | $\cdots$ |
     | :---: | :---: | :---: | :---: |
     | $y'$ | $-$ | $0$ | $-$ |
     | $y$ | $\searrow$ | $\dfrac{5}{3}$ | $\searrow$ |

     > 💡 讲师批注：亦可配方验证 $y = -\dfrac{1}{3}(x-1)^3 + \dfrac{5}{3}$，可见在 $(1, \frac{5}{3})$ 处切线水平且严格单调递减，无极值。
- **【最终答案】**
  - **増減**：**常に単調に減少する**（全体实数上单调递减）。
  - **極値**：**極値はない**（无极值，草图见上）。

---

### 演習問題 10 (2)

- **【原题重现与翻译】**
  - 原题：次の関数の増減を調べよ。また、極値を求め、グラフも概形も描け。
    $[1]\; y = \dfrac{x^2 + 3x + 9}{x + 3} \qquad [2]\; y = 3x^4 - 16x^3 + 18x^2 + 5$
  - 中文：讨论下列函数的增减性，求其极值，并画出函数草图。
- **【考点定位】**
  - $[1]$ 分式函数的求导、定义域断点（铅直渐近线）与斜渐近线；$[2]$ 四次函数的增减表与 W 型图像。

#### $[1]\; y = \dfrac{x^2 + 3x + 9}{x + 3}$
- **【图解辅助（SVG 矢量图）】**

<svg viewBox="0 0 420 280" xmlns="http://www.w3.org/2000/svg" style="max-width:420px;display:block;margin:10px auto;background:#fafafa;border:1px solid #e0e0e0;border-radius:6px;">
  <defs>
    <marker id="arr2a" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0,0 L0,6 L6,3 z" fill="#333"/></marker>
  </defs>
  <!-- Origin at (240, 140), scale: 1 unit x = 18px, 1 unit y = 10px -->
  <line x1="25" y1="140" x2="395" y2="140" stroke="#333" stroke-width="1.5" marker-end="url(#arr2a)"/>
  <line x1="240" y1="265" x2="240" y2="15" stroke="#333" stroke-width="1.5" marker-end="url(#arr2a)"/>
  <text x="398" y="144" font-size="13" font-style="italic" fill="#333">x</text>
  <text x="246" y="22" font-size="13" font-style="italic" fill="#333">y</text>
  <text x="245" y="154" font-size="12" fill="#333">O</text>
  <!-- Asymptotes: x=-3 -> X=186; y=x -> through (240,140), slope in screen coords = -10/18 -->
  <line x1="186" y1="20" x2="186" y2="260" stroke="#2e7d32" stroke-width="1.3" stroke-dasharray="5,4"/>
  <line x1="40" y1="251" x2="390" y2="57" stroke="#2e7d32" stroke-width="1.3" stroke-dasharray="5,4"/>
  <text x="150" y="34" font-size="11" fill="#2e7d32">x = -3</text>
  <text x="348" y="54" font-size="11" fill="#2e7d32">y = x</text>
  <!-- Right branch (x > -3): min at (0,3) -> (240,110) -->
  <path d="M 196,20 C 202,82 216,110 240,110 C 275,110 320,90 385,55" fill="none" stroke="#1565c0" stroke-width="2.5"/>
  <!-- Left branch (x < -3): max at (-6,-9) -> (132,230) -->
  <path d="M 45,256 C 85,238 112,230 132,230 C 155,230 172,240 178,265" fill="none" stroke="#1565c0" stroke-width="2.5"/>
  <!-- Extrema -->
  <circle cx="240" cy="110" r="4" fill="#d32f2f"/>
  <circle cx="132" cy="230" r="4" fill="#d32f2f"/>
  <line x1="132" y1="140" x2="132" y2="230" stroke="#888" stroke-dasharray="3,3"/>
  <line x1="132" y1="230" x2="240" y2="230" stroke="#888" stroke-dasharray="3,3"/>
  <text x="122" y="134" font-size="12" fill="#333">-6</text>
  <text x="190" y="154" font-size="12" fill="#333">-3</text>
  <text x="246" y="234" font-size="12" fill="#333">-9</text>
  <text x="247" y="114" font-size="12" fill="#d32f2f" font-weight="bold">極小 (0, 3)</text>
  <text x="52" y="220" font-size="12" fill="#d32f2f" font-weight="bold">極大 (-6, -9)</text>
</svg>

- **【分步标准解答】**
  1. 定義域は $x \neq -3$。分子を分母で割って変形すると：
     $$y = \frac{x(x + 3) + 9}{x + 3} = x + \frac{9}{x + 3}$$
     > 💡 讲师批注：先做带余除法分离整式部分，不仅让求导瞬间变简单，还能一眼看出斜渐近线 $y = x$ 与铅直渐近线 $x = -3$！
  2. 微分する：
     $$y' = 1 - \frac{9}{(x + 3)^2} = \frac{(x + 3)^2 - 9}{(x + 3)^2} = \frac{x(x + 6)}{(x + 3)^2}$$
     > 💡 讲师批注：分母 $(x+3)^2 > 0$（$x \neq -3$），因此 $y'$ 的符号完全由分子 $x(x+6)$ 决定。
  3. $y' = 0$ とすると $x = -6,\; 0$。
     - $x = -6$ のとき $y = -6 + \dfrac{9}{-3} = -9$
     - $x = 0$ のとき $y = 0 + \dfrac{9}{3} = 3$
  4. 増減表（$x = -3$ は定義域外なので斜線または空白で区切る）：

     | $x$ | $\cdots$ | $-6$ | $\cdots$ | $-3$ | $\cdots$ | $0$ | $\cdots$ |
     | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
     | $y'$ | $+$ | $0$ | $-$ | ／ | $-$ | $0$ | $+$ |
     | $y$ | $\nearrow$ | $-9$（極大） | $\searrow$ | ／ | $\searrow$ | $3$（極小） | $\nearrow$ |

  5. 漸近線の確認：
     - $\lim_{x\to -3 \pm 0} y = \pm\infty$ より、直線 $x = -3$ は漸近線。
     - $\lim_{x\to \pm\infty} (y - x) = \lim_{x\to\pm\infty} \dfrac{9}{x+3} = 0$ より、直線 $y = x$ は漸近線。
     > 💡 讲师批注：注意本题出现了「极大值 $-9$ 小于极小值 $3$」的有趣现象！这正是因为 $x=-3$ 处不连续，左右两支各自独立。
- **【最终答案】**
  - **増減**：$x \le -6,\; x \ge 0$ で増加、$-6 \le x < -3,\; -3 < x \le 0$ で減少。
  - **極値**：**$x = -6$ で極大値 $-9$、$x = 0$ で極小値 $3$**（渐近线 $x=-3,\; y=x$，草图见上）。

#### $[2]\; y = 3x^4 - 16x^3 + 18x^2 + 5$
- **【图解辅助（SVG 矢量图）】**

<svg viewBox="0 0 420 260" xmlns="http://www.w3.org/2000/svg" style="max-width:420px;display:block;margin:10px auto;background:#fafafa;border:1px solid #e0e0e0;border-radius:6px;">
  <defs>
    <marker id="arr2b" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0,0 L0,6 L6,3 z" fill="#333"/></marker>
  </defs>
  <!-- Origin at (120, 125), x scale 60px/unit, y scale 4px/unit -->
  <line x1="30" y1="125" x2="395" y2="125" stroke="#333" stroke-width="1.5" marker-end="url(#arr2b)"/>
  <line x1="120" y1="245" x2="120" y2="18" stroke="#333" stroke-width="1.5" marker-end="url(#arr2b)"/>
  <text x="398" y="129" font-size="13" font-style="italic" fill="#333">x</text>
  <text x="126" y="24" font-size="13" font-style="italic" fill="#333">y</text>
  <text x="106" y="140" font-size="12" fill="#333">O</text>
  <!-- Points: (0,5)->(120,105), (1,10)->(180,85), (3,-22)->(300,213) -->
  <path d="M 75,28 C 92,80 105,105 120,105 C 142,105 158,85 180,85 C 225,85 255,213 300,213 C 330,213 352,140 370,25" fill="none" stroke="#1565c0" stroke-width="2.5"/>
  <line x1="180" y1="85" x2="180" y2="125" stroke="#888" stroke-dasharray="3,3"/>
  <line x1="120" y1="85" x2="180" y2="85" stroke="#888" stroke-dasharray="3,3"/>
  <line x1="300" y1="213" x2="300" y2="125" stroke="#888" stroke-dasharray="3,3"/>
  <line x1="120" y1="213" x2="300" y2="213" stroke="#888" stroke-dasharray="3,3"/>
  <circle cx="120" cy="105" r="4" fill="#d32f2f"/>
  <circle cx="180" cy="85" r="4" fill="#d32f2f"/>
  <circle cx="300" cy="213" r="4" fill="#d32f2f"/>
  <text x="176" y="140" font-size="12" fill="#333">1</text>
  <text x="296" y="118" font-size="12" fill="#333">3</text>
  <text x="102" y="109" font-size="12" fill="#333">5</text>
  <text x="98" y="88" font-size="12" fill="#333">10</text>
  <text x="92" y="217" font-size="12" fill="#333">-22</text>
  <text x="184" y="75" font-size="12" fill="#d32f2f" font-weight="bold">極大 (1, 10)</text>
  <text x="266" y="233" font-size="12" fill="#d32f2f" font-weight="bold">極小 (3, -22)</text>
  <text x="45" y="116" font-size="11" fill="#d32f2f" font-weight="bold">極小 (0,5)</text>
</svg>

- **【分步标准解答】**
  1. 微分する：
     $$y' = 12x^3 - 48x^2 + 36x = 12x(x^2 - 4x + 3) = 12x(x - 1)(x - 3)$$
     > 💡 讲师批注：先提取公因式 $12x$，再对二次式因式分解。
  2. $y' = 0$ とすると $x = 0,\; 1,\; 3$。各点の値を求める：
     - $x = 0$ のとき：$y = 5$
     - $x = 1$ のとき：$y = 3 - 16 + 18 + 5 = 10$
     - $x = 3$ のとき：$y = 3(81) - 16(27) + 18(9) + 5 = 243 - 432 + 162 + 5 = -22$
     > 💡 讲师批注：算 $x=3$ 时可先提公因式 $3^2=9$ 简化心算：$9(27 - 48 + 18) + 5 = 9(-3) + 5 = -22$，既快又不易错！
  3. 増減表：

     | $x$ | $\cdots$ | $0$ | $\cdots$ | $1$ | $\cdots$ | $3$ | $\cdots$ |
     | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
     | $y'$ | $-$ | $0$ | $+$ | $0$ | $-$ | $0$ | $+$ |
     | $y$ | $\searrow$ | $5$（極小） | $\nearrow$ | $10$（極大） | $\searrow$ | $-22$（極小） | $\nearrow$ |

- **【最终答案】**
  - **増減**：$x \le 0,\; 1 \le x \le 3$ で減少、$0 \le x \le 1,\; x \ge 3$ で増加。
  - **極値**：**$x = 1$ で極大値 $10$、$x = 0$ で極小値 $5$、$x = 3$ で極小値 $-22$**（草图见上）。

---

### 演習問題 10 (3)

- **【原题重现与翻译】**
  - 原题：次の関数の増減を調べよ。また、極値を求め、グラフも概形も描け。
    $[1]\; y = (x^2 - 3)e^{-x} \qquad [2]\; y = |x|\sqrt{x + 3}$
  - 中文：讨论下列函数的增减性，求其极值，并画出函数草图。
- **【考点定位】**
  - $[1]$ 指数与多项式乘积求导、水平渐近线 $\lim_{x\to\infty} x^n e^{-x} = 0$；$[2]$ 含绝对值与根式函数的定义域、分段求导与**不可微点处的极值**。

#### $[1]\; y = (x^2 - 3)e^{-x}$
- **【图解辅助（SVG 矢量图）】**

<svg viewBox="0 0 420 250" xmlns="http://www.w3.org/2000/svg" style="max-width:420px;display:block;margin:10px auto;background:#fafafa;border:1px solid #e0e0e0;border-radius:6px;">
  <defs>
    <marker id="arr3a" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0,0 L0,6 L6,3 z" fill="#333"/></marker>
  </defs>
  <!-- Origin at (160, 100) -->
  <line x1="25" y1="100" x2="395" y2="100" stroke="#333" stroke-width="1.5" marker-end="url(#arr3a)"/>
  <line x1="160" y1="235" x2="160" y2="18" stroke="#333" stroke-width="1.5" marker-end="url(#arr3a)"/>
  <text x="398" y="104" font-size="13" font-style="italic" fill="#333">x</text>
  <text x="166" y="24" font-size="13" font-style="italic" fill="#333">y</text>
  <text x="145" y="114" font-size="12" fill="#333">O</text>
  <!-- Curve: x=-sqrt3 -> (91,100), x=-1 -> (120,208) min -2e, x=0 -> (160,160) y=-3, x=sqrt3 -> (229,100), x=3 -> (280,82) max 6/e^3, then -> 0+ -->
  <path d="M 62,22 C 74,65 82,82 91,100 C 102,155 108,208 120,208 C 136,208 148,180 160,160 C 185,125 210,110 229,100 C 248,90 264,82 280,82 C 310,82 340,94 390,98" fill="none" stroke="#1565c0" stroke-width="2.5"/>
  <line x1="120" y1="100" x2="120" y2="208" stroke="#888" stroke-dasharray="3,3"/>
  <line x1="120" y1="208" x2="160" y2="208" stroke="#888" stroke-dasharray="3,3"/>
  <line x1="280" y1="82" x2="280" y2="100" stroke="#888" stroke-dasharray="3,3"/>
  <line x1="160" y1="82" x2="280" y2="82" stroke="#888" stroke-dasharray="3,3"/>
  <circle cx="120" cy="208" r="4" fill="#d32f2f"/>
  <circle cx="280" cy="82" r="4" fill="#d32f2f"/>
  <circle cx="160" cy="160" r="3" fill="#1565c0"/>
  <text x="112" y="92" font-size="12" fill="#333">-1</text>
  <text x="276" y="114" font-size="12" fill="#333">3</text>
  <text x="166" y="164" font-size="12" fill="#333">-3</text>
  <text x="166" y="212" font-size="12" fill="#333">-2e</text>
  <text x="128" y="80" font-size="11" fill="#333">6/e³</text>
  <text x="64" y="226" font-size="12" fill="#d32f2f" font-weight="bold">極小 (-1, -2e)</text>
  <text x="275" y="68" font-size="12" fill="#d32f2f" font-weight="bold">極大 (3, 6/e³)</text>
  <text x="315" y="116" font-size="11" fill="#2e7d32">x→∞ で y→+0</text>
</svg>

- **【分步标准解答】**
  1. 積の微分法より：
     $$y' = 2x \cdot e^{-x} + (x^2 - 3)(-e^{-x}) = -(x^2 - 2x - 3)e^{-x} = -(x + 1)(x - 3)e^{-x}$$
     > 💡 讲师批注：切记 $(e^{-x})' = -e^{-x}$ 的负号！把 $e^{-x}$ 提到最后，由于 $e^{-x} > 0$ 恒正，$y'$ 符号完全由 $-(x+1)(x-3)$ 决定。
  2. $y' = 0$ とすると $x = -1,\; 3$。
     - $x = -1$ のとき：$y = ((-1)^2 - 3)e^{1} = -2e$
     - $x = 3$ のとき：$y = (3^2 - 3)e^{-3} = \dfrac{6}{e^3}$
     - $x = 0$ のとき $y = -3$；$y = 0$ のとき $x = \pm\sqrt{3}$。
  3. 極限の確認：
     $$\lim_{x\to\infty} (x^2 - 3)e^{-x} = \lim_{x\to\infty} \frac{x^2 - 3}{e^x} = 0, \qquad \lim_{x\to -\infty} (x^2 - 3)e^{-x} = +\infty$$
     よって $x$ 軸（$y=0$）は $x \to \infty$ における漸近線である。
     > 💡 讲师批注：EJU 数学Ⅲ中 $\lim_{x\to\infty} \frac{x^n}{e^x} = 0$ 是核心默认结论，画含 $e^{-x}$ 的草图必须交代 $x \to +\infty$ 趋近 $x$ 轴。
  4. 増減表：

     | $x$ | $\cdots$ | $-1$ | $\cdots$ | $3$ | $\cdots$ |
     | :---: | :---: | :---: | :---: | :---: | :---: |
     | $y'$ | $-$ | $0$ | $+$ | $0$ | $-$ |
     | $y$ | $\searrow$ | $-2e$（極小） | $\nearrow$ | $\dfrac{6}{e^3}$（極大） | $\searrow$ |

- **【最终答案】**
  - **増減**：$x \le -1,\; x \ge 3$ で減少、$-1 \le x \le 3$ で増加。
  - **極値**：**$x = 3$ で極大値 $\dfrac{6}{e^3}$、$x = -1$ で極小値 $-2e$**（草图见上）。

#### $[2]\; y = |x|\sqrt{x + 3}$
- **【图解辅助（SVG 矢量图）】**

<svg viewBox="0 0 400 240" xmlns="http://www.w3.org/2000/svg" style="max-width:400px;display:block;margin:10px auto;background:#fafafa;border:1px solid #e0e0e0;border-radius:6px;">
  <defs>
    <marker id="arr3b" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0,0 L0,6 L6,3 z" fill="#333"/></marker>
  </defs>
  <!-- Origin at (240, 195), x scale 55px/unit, y scale 55px/unit -->
  <line x1="35" y1="195" x2="375" y2="195" stroke="#333" stroke-width="1.5" marker-end="url(#arr3b)"/>
  <line x1="240" y1="225" x2="240" y2="18" stroke="#333" stroke-width="1.5" marker-end="url(#arr3b)"/>
  <text x="378" y="199" font-size="13" font-style="italic" fill="#333">x</text>
  <text x="246" y="24" font-size="13" font-style="italic" fill="#333">y</text>
  <text x="244" y="210" font-size="12" fill="#333">O</text>
  <!-- x=-3 -> (75,195), x=-2 -> (130,85) max 2, x=0 -> (240,195) min 0 (cusp), x=1 -> (295,85), x=1.5 -> (322,30) -->
  <path d="M 75,195 C 75,135 98,85 130,85 C 168,85 208,145 240,195" fill="none" stroke="#1565c0" stroke-width="2.5"/>
  <path d="M 240,195 C 266,150 295,95 328,25" fill="none" stroke="#1565c0" stroke-width="2.5"/>
  <line x1="130" y1="85" x2="130" y2="195" stroke="#888" stroke-dasharray="3,3"/>
  <line x1="130" y1="85" x2="240" y2="85" stroke="#888" stroke-dasharray="3,3"/>
  <circle cx="75" cy="195" r="3.5" fill="#1565c0"/>
  <circle cx="130" cy="85" r="4" fill="#d32f2f"/>
  <circle cx="240" cy="195" r="4" fill="#d32f2f"/>
  <text x="66" y="212" font-size="12" fill="#333">-3</text>
  <text x="122" y="212" font-size="12" fill="#333">-2</text>
  <text x="247" y="89" font-size="12" fill="#333">2</text>
  <text x="108" y="72" font-size="12" fill="#d32f2f" font-weight="bold">極大 (-2, 2)</text>
  <text x="255" y="212" font-size="12" fill="#d32f2f" font-weight="bold">極小 (0, 0)（微分不可）</text>
</svg>

- **【分步标准解答】**
  1. 定義域は $x + 3 \ge 0$ すなわち $x \ge -3$。絶対値を外して場合分けする：
     $$y = \begin{cases} x\sqrt{x+3} & (x \ge 0) \\ -x\sqrt{x+3} & (-3 \le x < 0) \end{cases}$$
  2. 各区間の内部で微分する：
     - $x > 0$ のとき：
       $$y' = \sqrt{x+3} + x \cdot \frac{1}{2\sqrt{x+3}} = \frac{2(x+3) + x}{2\sqrt{x+3}} = \frac{3(x+2)}{2\sqrt{x+3}} > 0$$
     - $-3 < x < 0$ のとき：
       $$y' = -\frac{3(x+2)}{2\sqrt{x+3}}$$
       よって $-3 < x < 0$ において $y' = 0 \iff x = -2$。
     > 💡 讲师批注：在 $x=0$ 处，左导数 $\lim_{x\to -0} y' = -\sqrt{3}$，右导数 $\lim_{x\to +0} y' = +\sqrt{3}$，两者不等，故 **$x=0$ 处不可微**！但函数在 $x=0$ 连续且由减变增，因此 $x=0$ 依然是极小值点！这是日本考题最爱的陷阱之一。
  3. 端点と極値の計算：
     - $x = -3$ で $y = 0$（$\lim_{x\to -3+0} y' = +\infty$ より接線は $y$ 軸に平行）；
     - $x = -2$ で $y = |-2|\sqrt{-2+3} = 2$；
     - $x = 0$ で $y = 0$。
  4. 増減表（$x = -3,\; 0$ では $y'$ は存在しないため斜線）：

     | $x$ | $-3$ | $\cdots$ | $-2$ | $\cdots$ | $0$ | $\cdots$ |
     | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
     | $y'$ | ／ | $+$ | $0$ | $-$ | ／ | $+$ |
     | $y$ | $0$ | $\nearrow$ | $2$（極大） | $\searrow$ | $0$（極小） | $\nearrow$ |

- **【最终答案】**
  - **増減**：$-3 \le x \le -2,\; x \ge 0$ で増加、$-2 \le x \le 0$ で減少。
  - **極値**：**$x = -2$ で極大値 $2$、$x = 0$ で極小値 $0$**（草图见上）。

---

### 演習問題 10 (4)

- **【原题重现与翻译】**
  - 原题：次の関数の増減を調べよ。また、極値を求め、グラフも概形も描け。
    $[1]\; y = |x^3 - x^2| \qquad [2]\; y = 2\cos x - \cos 2x \quad (0 \le x \le 2\pi)$
  - 中文：讨论下列函数的增减性，求其极值，并画出函数草图。
- **【考点定位】**
  - $[1]$ 绝对值翻折函数（含可微极小值与不可微尖点极小值）；$[2]$ 三角函数求导与二倍角因式分解。

#### $[1]\; y = |x^3 - x^2|$
- **【图解辅助（SVG 矢量图）】**

<svg viewBox="0 0 400 230" xmlns="http://www.w3.org/2000/svg" style="max-width:400px;display:block;margin:10px auto;background:#fafafa;border:1px solid #e0e0e0;border-radius:6px;">
  <defs>
    <marker id="arr4a" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0,0 L0,6 L6,3 z" fill="#333"/></marker>
  </defs>
  <!-- Origin at (140, 180), x scale 120px/unit, y scale 500px/unit (4/27 ≈ 0.148 -> 74px) -->
  <line x1="30" y1="180" x2="375" y2="180" stroke="#333" stroke-width="1.5" marker-end="url(#arr4a)"/>
  <line x1="140" y1="215" x2="140" y2="18" stroke="#333" stroke-width="1.5" marker-end="url(#arr4a)"/>
  <text x="378" y="184" font-size="13" font-style="italic" fill="#333">x</text>
  <text x="146" y="24" font-size="13" font-style="italic" fill="#333">y</text>
  <text x="126" y="196" font-size="12" fill="#333">O</text>
  <!-- x<1: y = -x^3 + x^2; (0,0)->(140,180), (2/3, 4/27)->(220,106), (1,0)->(260,180) -->
  <path d="M 68,25 C 95,120 116,180 140,180 C 166,180 192,106 220,106 C 242,106 252,145 260,180" fill="none" stroke="#1565c0" stroke-width="2.5"/>
  <!-- x>=1: y = x^3 - x^2 -->
  <path d="M 260,180 C 276,125 296,70 318,22" fill="none" stroke="#1565c0" stroke-width="2.5"/>
  <line x1="220" y1="106" x2="220" y2="180" stroke="#888" stroke-dasharray="3,3"/>
  <line x1="140" y1="106" x2="220" y2="106" stroke="#888" stroke-dasharray="3,3"/>
  <circle cx="140" cy="180" r="4" fill="#d32f2f"/>
  <circle cx="220" cy="106" r="4" fill="#d32f2f"/>
  <circle cx="260" cy="180" r="4" fill="#d32f2f"/>
  <text x="212" y="196" font-size="12" fill="#333">2/3</text>
  <text x="256" y="196" font-size="12" fill="#333">1</text>
  <text x="108" y="110" font-size="12" fill="#333">4/27</text>
  <text x="172" y="92" font-size="12" fill="#d32f2f" font-weight="bold">極大 (2/3, 4/27)</text>
  <text x="268" y="198" font-size="11" fill="#d32f2f" font-weight="bold">極小 (1,0)</text>
  <text x="80" y="198" font-size="11" fill="#d32f2f" font-weight="bold">極小 (0,0)</text>
</svg>

- **【分步标准解答】**
  1. $x^3 - x^2 = x^2(x - 1)$ の符号で場合分けする（$x^2 \ge 0$ より $x=1$ が境目）：
     $$y = \begin{cases} x^3 - x^2 & (x \ge 1) \\ -x^3 + x^2 & (x < 1) \end{cases}$$
     > 💡 讲师批注：不要把 $x=0$ 也当成符号分界点！$x^2 \ge 0$ 恒非负，只有 $x=1$ 两侧 $x^3-x^2$ 才变号。
  2. 各区間で微分する：
     - $x > 1$ のとき：$y' = 3x^2 - 2x = x(3x - 2) > 0$
     - $x < 1$ のとき：$y' = -3x^2 + 2x = -x(3x - 2)$
       よって $x < 1$ で $y' = 0 \iff x = 0,\; \dfrac{2}{3}$。
  3. $x = 1$ での微分可能性の確認：
     左微分係数は $-1$、右微分係数は $+1$ で一致しないため $x = 1$ で微分不可能だが、連続かつ減少から増加に転じるため極小値 $0$ をとる。
     - $x = 0$ で $y = 0$；$x = \dfrac{2}{3}$ で $y = -\dfrac{8}{27} + \dfrac{4}{9} = \dfrac{4}{27}$；$x = 1$ で $y = 0$。
  4. 増減表：

     | $x$ | $\cdots$ | $0$ | $\cdots$ | $\dfrac{2}{3}$ | $\cdots$ | $1$ | $\cdots$ |
     | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
     | $y'$ | $-$ | $0$ | $+$ | $0$ | $-$ | ／ | $+$ |
     | $y$ | $\searrow$ | $0$（極小） | $\nearrow$ | $\dfrac{4}{27}$（極大） | $\searrow$ | $0$（極小） | $\nearrow$ |

     > 💡 讲师批注：几何直观验算——先画 $g(x)=x^3-x^2$，再将 $x$ 轴下方部分（$x<1$）沿 $x$ 轴翻折上去，一目了然！
- **【最终答案】**
  - **増減**：$x \le 0,\; \dfrac{2}{3} \le x \le 1$ で減少、$0 \le x \le \dfrac{2}{3},\; x \ge 1$ で増加。
  - **極値**：**$x = \dfrac{2}{3}$ で極大値 $\dfrac{4}{27}$、$x = 0,\; 1$ で極小値 $0$**（草图见上）。

#### $[2]\; y = 2\cos x - \cos 2x \quad (0 \le x \le 2\pi)$
- **【图解辅助（SVG 矢量图）】**

<svg viewBox="0 0 430 240" xmlns="http://www.w3.org/2000/svg" style="max-width:430px;display:block;margin:10px auto;background:#fafafa;border:1px solid #e0e0e0;border-radius:6px;">
  <defs>
    <marker id="arr4b" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0,0 L0,6 L6,3 z" fill="#333"/></marker>
  </defs>
  <!-- Origin at (55, 110), 2pi = 330px (pi/3 = 55px), y scale 32px/unit -->
  <line x1="30" y1="110" x2="405" y2="110" stroke="#333" stroke-width="1.5" marker-end="url(#arr4b)"/>
  <line x1="55" y1="225" x2="55" y2="18" stroke="#333" stroke-width="1.5" marker-end="url(#arr4b)"/>
  <text x="408" y="114" font-size="13" font-style="italic" fill="#333">x</text>
  <text x="61" y="24" font-size="13" font-style="italic" fill="#333">y</text>
  <text x="42" y="124" font-size="12" fill="#333">O</text>
  <!-- Key points: (0,1)->(55,78), (pi/3, 1.5)->(110,62), (pi,-3)->(220,206), (5pi/3,1.5)->(330,62), (2pi,1)->(385,78) -->
  <path d="M 55,78 C 75,78 90,62 110,62 C 155,62 180,206 220,206 C 260,206 285,62 330,62 C 350,62 365,78 385,78" fill="none" stroke="#1565c0" stroke-width="2.5"/>
  <line x1="110" y1="62" x2="110" y2="110" stroke="#888" stroke-dasharray="3,3"/>
  <line x1="220" y1="110" x2="220" y2="206" stroke="#888" stroke-dasharray="3,3"/>
  <line x1="330" y1="62" x2="330" y2="110" stroke="#888" stroke-dasharray="3,3"/>
  <line x1="385" y1="78" x2="385" y2="110" stroke="#888" stroke-dasharray="3,3"/>
  <line x1="55" y1="62" x2="330" y2="62" stroke="#888" stroke-dasharray="3,3"/>
  <line x1="55" y1="206" x2="220" y2="206" stroke="#888" stroke-dasharray="3,3"/>
  <circle cx="55" cy="78" r="3.5" fill="#1565c0"/>
  <circle cx="110" cy="62" r="4" fill="#d32f2f"/>
  <circle cx="220" cy="206" r="4" fill="#d32f2f"/>
  <circle cx="330" cy="62" r="4" fill="#d32f2f"/>
  <circle cx="385" cy="78" r="3.5" fill="#1565c0"/>
  <text x="100" y="125" font-size="12" fill="#333">π/3</text>
  <text x="216" y="104" font-size="12" fill="#333">π</text>
  <text x="318" y="125" font-size="12" fill="#333">5π/3</text>
  <text x="378" y="125" font-size="12" fill="#333">2π</text>
  <text x="32" y="66" font-size="12" fill="#333">3/2</text>
  <text x="41" y="83" font-size="12" fill="#333">1</text>
  <text x="36" y="210" font-size="12" fill="#333">-3</text>
  <text x="90" y="50" font-size="11" fill="#d32f2f" font-weight="bold">極大 3/2</text>
  <text x="310" y="50" font-size="11" fill="#d32f2f" font-weight="bold">極大 3/2</text>
  <text x="230" y="212" font-size="11" fill="#d32f2f" font-weight="bold">極小 (π, -3)</text>
</svg>

- **【分步标准解答】**
  1. 微分し、2倍角の公式 $\sin 2x = 2\sin x \cos x$ を用いて因数分解する：
     $$y' = -2\sin x + 2\sin 2x = -2\sin x + 4\sin x \cos x = 2\sin x (2\cos x - 1)$$
     > 💡 讲师批注：切记 $(\cos 2x)' = -2\sin 2x$，前面的负号抵消后变为 $+2\sin 2x$。
  2. $0 < x < 2\pi$ において $y' = 0$ とすると：
     $$\sin x = 0 \quad \text{または} \quad \cos x = \frac{1}{2} \implies x = \frac{\pi}{3},\; \pi,\; \frac{5\pi}{3}$$
  3. 端点と極値の計算：
     - $x = 0,\; 2\pi$：$y = 2(1) - 1 = 1$
     - $x = \dfrac{\pi}{3},\; \dfrac{5\pi}{3}$：$y = 2\left(\dfrac{1}{2}\right) - \left(-\dfrac{1}{2}\right) = \dfrac{3}{2}$
     - $x = \pi$：$y = 2(-1) - 1 = -3$
  4. 増減表（$0 \le x \le 2\pi$）：

     | $x$ | $0$ | $\cdots$ | $\dfrac{\pi}{3}$ | $\cdots$ | $\pi$ | $\cdots$ | $\dfrac{5\pi}{3}$ | $\cdots$ | $2\pi$ |
     | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
     | $y'$ | $0$ | $+$ | $0$ | $-$ | $0$ | $+$ | $0$ | $-$ | $0$ |
     | $y$ | $1$ | $\nearrow$ | $\dfrac{3}{2}$（極大） | $\searrow$ | $-3$（極小） | $\nearrow$ | $\dfrac{3}{2}$（極大） | $\searrow$ | $1$ |

     > 💡 讲师批注：验算技巧——令 $t = \cos x$，原式 $= -2t^2 + 2t + 1 = -2\left(t-\frac{1}{2}\right)^2 + \frac{3}{2}$，在 $t=\frac{1}{2}$ 取最大 $\frac{3}{2}$，在 $t=-1$ 取最小 $-3$，完美一致！
- **【最终答案】**
  - **増減**：$0 \le x \le \dfrac{\pi}{3},\; \pi \le x \le \dfrac{5\pi}{3}$ で増加、$\dfrac{\pi}{3} \le x \le \pi,\; \dfrac{5\pi}{3} \le x \le 2\pi$ で減少。
  - **極値**：**$x = \dfrac{\pi}{3},\; \dfrac{5\pi}{3}$ で極大値 $\dfrac{3}{2}$、$x = \pi$ で極小値 $-3$**（草图见上）。

---

### 演習問題 10 (5)

- **【原题重现与翻译】**
  - 原题：$a$ は定数とする。関数 $f(x) = \dfrac{x + 1}{x^2 + 2x + a}$ について、次の条件を満たす $a$ の値または範囲をそれぞれ求めよ。
    $[1]\; f(x)$ が $x = 1$ で極値をとる。 $\qquad [2]\; f(x)$ が極値をもつ。
  - 中文：设 $a$ 为常数。对于函数 $f(x) = \dfrac{x + 1}{x^2 + 2x + a}$，分别求满足下列条件的 $a$ 的值或范围：$[1]$ $f(x)$ 在 $x=1$ 处取极值；$[2]$ $f(x)$ 有极值。
- **【考点定位】**
  - 分式函数极值的必要条件与**充分性检验（符号变化与分母非零）**。
- **【分步标准解答】**
  まず商の微分法により $f'(x)$ を求める：
  $$f'(x) = \frac{1\cdot(x^2 + 2x + a) - (x + 1)(2x + 2)}{(x^2 + 2x + a)^2} = \frac{-x^2 - 2x + a - 2}{(x^2 + 2x + a)^2} = \frac{-(x + 1)^2 + (a - 1)}{(x^2 + 2x + a)^2}$$
  > 💡 讲师批注：把分子配成 $-(x+1)^2 + (a-1)$，立刻与分母 $x^2+2x+a = (x+1)^2 + (a-1)$ 形成完美呼应！

  #### $[1]\; f(x)$ が $x = 1$ で極値をとる
  1. **必要条件**：$f(x)$ が $x = 1$ で定義され（分母 $1 + 2 + a \neq 0 \iff a \neq -3$）、かつ $f'(1) = 0$ である必要がある。
     $$-(1 + 1)^2 + (a - 1) = 0 \implies a - 5 = 0 \implies a = 5$$
  2. **十分性の確認**：$a = 5$ のとき、分母は $(x + 1)^2 + 4 > 0$（すべての実数で定義される）。また、
     $$f'(x) = \frac{-(x + 1)^2 + 4}{\{(x+1)^2 + 4\}^2} = \frac{-(x + 3)(x - 1)}{\{(x+1)^2 + 4\}^2}$$
     $x = 1$ の前後で $f'(x)$ の符号は $+$ から $-$ に変化するため、$f(x)$ は $x = 1$ で確かに極大値をとる。
     > 💡 讲师批注：日本描述题中，由 $f'(1)=0$ 求出参数后**必须写「逆に $a=5$ のとき…」检验符号变化**，否则必扣分！

  #### $[2]\; f(x)$ が極値をもつ
  - 分母は $(x+1)^2 + (a - 1)$ であり、$f'(x)$ の符号は分子 $g(x) = -(x + 1)^2 + (a - 1)$ の符号と一致する（分母 $\neq 0$ の範囲で）。
  - $a \le 1$ のとき：$a - 1 \le 0$ より $g(x) = -(x+1)^2 + (a-1) \le 0$ となり、$f'(x)$ は符号を変えない（極値をもたない）。
  - $a > 1$ のとき：分母 $(x+1)^2 + (a-1) > 0$ はすべての実数 $x$ で正（連続かつ微分可能）。さらに $g(x) = 0$ は異なる 2 つの実数解 $x = -1 \pm \sqrt{a-1}$ をもち、その前後で $f'(x)$ の符号が変化するため、極大値・極小値をもつ。
  > 💡 讲师批注：特值检验 $a=1$ 时 $f(x)=\frac{x+1}{(x+1)^2}=\frac{1}{x+1}$（$x \neq -1$），单调递减无极值，故严格大于 $1$。
- **【最终答案】**
  - **$[1]\; a = 5$**
  - **$[2]\; a > 1$**

---

### 演習問題 10 (6)

- **【原题重现与翻译】**
  - 原题：関数 $f(x) = \dfrac{ax^2 + bx + c}{x - 6}$ は $x = 5$ で極大値 $3$、$x = 7$ で極小値 $7$ をとる。このとき、定数 $a, b, c$ の値を求めよ。
  - 中文：函数 $f(x) = \dfrac{ax^2 + bx + c}{x - 6}$ 在 $x=5$ 处取极大值 $3$，在 $x=7$ 处取极小值 $7$，求常数 $a, b, c$ 的值。
- **【考点定位】**
  - 分式函数由极值条件反求参数（联立方程 + 充分性验证）。
- **【分步标准解答】**
  1. 微分する（$x \neq 6$）：
     $$f'(x) = \frac{(2ax + b)(x - 6) - (ax^2 + bx + c)}{(x - 6)^2} = \frac{ax^2 - 12ax - 6b - c}{(x - 6)^2}$$
     > 💡 讲师批注：分子的 $bx$ 项恰好消去！且分子对称轴为 $x=6$，因此 $f'(5)=0$ 与 $f'(7)=0$ 给出的方程是完全等价的。
  2. 極値をもつための必要条件より、$f(5) = 3,\; f(7) = 7,\; f'(5) = 0$（および $f'(7)=0$）が成り立つ：
     - $f(5) = \dfrac{25a + 5b + c}{-1} = 3 \implies 25a + 5b + c = -3 \quad \cdots\text{①}$
     - $f(7) = \dfrac{49a + 7b + c}{1} = 7 \implies 49a + 7b + c = 7 \quad \cdots\text{②}$
     - $f'(5) = 0 \implies 25a - 60a - 6b - c = 0 \implies -35a - 6b - c = 0 \quad \cdots\text{③}$
  3. ①②③を連立して解く：
     - ② $-$ ①：$24a + 2b = 10 \implies b = 5 - 12a \quad \cdots\text{④}$
     - ① $+$ ③：$-10a - b = -3 \implies b = 3 - 10a \quad \cdots\text{⑤}$
     - ④⑤より $5 - 12a = 3 - 10a \implies 2a = 2 \implies a = 1$。
     - ⑤より $b = 3 - 10(1) = -7$。
     - ③より $c = -35(1) - 6(-7) = -35 + 42 = 7$。
  4. **十分性の確認**：$a = 1,\; b = -7,\; c = 7$ のとき、
     $$f(x) = \frac{x^2 - 7x + 7}{x - 6} = x - 1 + \frac{1}{x - 6}, \qquad f'(x) = 1 - \frac{1}{(x-6)^2} = \frac{(x - 5)(x - 7)}{(x - 6)^2}$$
     - $x < 5$ で $f' > 0$、$5 < x < 6$ で $f' < 0 \implies x = 5$ で極大値 $f(5) = 4 - 1 = 3$。
     - $6 < x < 7$ で $f' < 0$、$x > 7$ で $f' > 0 \implies x = 7$ で極小値 $f(7) = 6 + 1 = 7$。
     よって条件をすべて満たす。
     > 💡 讲师批注：把分式写回 $x - 1 + \frac{1}{x-6}$ 后，极值与单调性一目了然，验算极快！
- **【最终答案】**
  **$a = 1,\quad b = -7,\quad c = 7$**

---

### 演習問題 10 (7)

- **【原题重现与翻译】**
  - 原题：関数 $y = e^x \{2x^2 - (p + 4)x + p + 4\} \quad (-1 \le x \le 1)$ の最大値が $7$ であるとき、正の定数 $p$ の値を求めよ。
  - 中文：当函数 $y = e^x \{2x^2 - (p + 4)x + p + 4\} \quad (-1 \le x \le 1)$ 的最大值为 $7$ 时，求正常数 $p$ 的值。
- **【考点定位】**
  - 含参指数乘积函数的闭区间最大值分类讨论 + 关键数值估计（$2e < 7$）。
- **【图解辅助（SVG 矢量图）】**

<svg viewBox="0 0 420 210" xmlns="http://www.w3.org/2000/svg" style="max-width:420px;display:block;margin:10px auto;background:#fafafa;border:1px solid #e0e0e0;border-radius:6px;">
  <!-- Left case: 0 < p/2 < 1 -->
  <text x="40" y="22" font-size="12" font-weight="bold" fill="#1565c0">Case 1: 0 &lt; p &lt; 2 (p/2 &lt; 1)</text>
  <line x1="25" y1="165" x2="195" y2="165" stroke="#333" stroke-width="1.2"/>
  <path d="M 45,140 C 65,90 80,68 95,68 C 115,68 128,125 145,125 C 158,125 168,105 178,92" fill="none" stroke="#1565c0" stroke-width="2.2"/>
  <line x1="45" y1="140" x2="45" y2="165" stroke="#888" stroke-dasharray="3,3"/>
  <line x1="95" y1="68" x2="95" y2="165" stroke="#888" stroke-dasharray="3,3"/>
  <line x1="145" y1="125" x2="145" y2="165" stroke="#888" stroke-dasharray="3,3"/>
  <line x1="178" y1="92" x2="178" y2="165" stroke="#888" stroke-dasharray="3,3"/>
  <circle cx="95" cy="68" r="3.5" fill="#d32f2f"/>
  <circle cx="178" cy="92" r="3.5" fill="#2e7d32"/>
  <text x="38" y="180" font-size="11" fill="#333">-1</text>
  <text x="91" y="180" font-size="11" fill="#333">0</text>
  <text x="137" y="180" font-size="11" fill="#333">p/2</text>
  <text x="174" y="180" font-size="11" fill="#333">1</text>
  <text x="68" y="58" font-size="11" fill="#d32f2f">f(0)=p+4</text>
  <text x="150" y="84" font-size="11" fill="#2e7d32">f(1)=2e&lt;6</text>

  <!-- Divider -->
  <line x1="210" y1="15" x2="210" y2="195" stroke="#ccc" stroke-dasharray="4,4"/>

  <!-- Right case: p/2 >= 1 -->
  <text x="245" y="22" font-size="12" font-weight="bold" fill="#1565c0">Case 2: p ≥ 2 (p/2 ≥ 1)</text>
  <line x1="225" y1="165" x2="400" y2="165" stroke="#333" stroke-width="1.2"/>
  <path d="M 245,140 C 265,90 280,62 300,62 C 325,62 348,95 365,120" fill="none" stroke="#1565c0" stroke-width="2.2"/>
  <path d="M 365,120 C 375,134 382,138 390,138" fill="none" stroke="#999" stroke-width="1.5" stroke-dasharray="3,3"/>
  <line x1="245" y1="140" x2="245" y2="165" stroke="#888" stroke-dasharray="3,3"/>
  <line x1="300" y1="62" x2="300" y2="165" stroke="#888" stroke-dasharray="3,3"/>
  <line x1="365" y1="120" x2="365" y2="165" stroke="#888" stroke-dasharray="3,3"/>
  <circle cx="300" cy="62" r="4" fill="#d32f2f"/>
  <text x="238" y="180" font-size="11" fill="#333">-1</text>
  <text x="296" y="180" font-size="11" fill="#333">0</text>
  <text x="361" y="180" font-size="11" fill="#333">1</text>
  <text x="270" y="52" font-size="11" fill="#d32f2f" font-weight="bold">最大 f(0)=p+4=7</text>
  <text x="275" y="198" font-size="11" fill="#d32f2f">→ p = 3（適合！）</text>
</svg>

- **【分步标准解答】**
  1. $f(x) = e^x \{2x^2 - (p + 4)x + p + 4\}$ とおき、微分する：
     $$f'(x) = e^x \{2x^2 - (p + 4)x + p + 4\} + e^x \{4x - (p + 4)\} = e^x (2x^2 - px) = x(2x - p)e^x$$
     > 💡 讲师批注：求导后常数项 $p+4$ 和一次项 $-4x+4x$ 全部抵消，只剩 $x(2x-p)e^x$！这是典型的出题人精巧设计。
  2. $p > 0$ より $0 < \dfrac{p}{2}$。$f'(x) = 0$ の解は $x = 0,\; \dfrac{p}{2}$。
     全体の増減は $x \le 0$ で増加、$0 \le x \le \dfrac{p}{2}$ で減少、$x \ge \dfrac{p}{2}$ で増加となる。
  3. したがって、閉区間 $-1 \le x \le 1$ における最大値の候補は、$x = 0$（極大）または右端点 $x = 1$ のみである：
     - $f(0) = e^0 (p + 4) = p + 4$
     - $f(1) = e^1 \{2 - (p + 4) + p + 4\} = 2e$
     > 💡 讲师批注：惊喜发现 $f(1) = 2e$ 与 $p$ 无关！
  4. $e < 3$ より $f(1) = 2e < 6 < 7$ である。したがって最大値が $7$ となるためには、最大値は $x = 0$ でとらなければならず：
     $$f(0) = p + 4 = 7 \implies p = 3$$
  5. **確認**：$p = 3$ のとき、$\dfrac{p}{2} = \dfrac{3}{2} > 1$ であるから、区間 $-1 \le x \le 1$ で $f(x)$ は $-1 \le x \le 0$ で増加、$0 \le x \le 1$ で減少し、確かに $x = 0$ で最大値 $7$ をとる（また $p = 3 > 0$ も満たす）。
- **【最终答案】**
  **$p = 3$**

---

### 演習問題 10 (8)

- **【原题重现与翻译】**
  - 原题：$f(x) = x^3 - 9x^2 + 15x + 7$
    $[1]$ 関数 $y = f(x)$ は $x = \alpha$ で極大値、$x = \beta$ で極小値をとる。2 点 $(\alpha, f(\alpha)),\; (\beta, f(\beta))$ を結ぶ線分の中点 $M$ は曲線 $y = f(x)$ 上にあることを示せ。
    $[2]$ 曲線 $y = f(x)$ は、点 $M$ に関して対称であることを示せ。
  - 中文：设 $f(x) = x^3 - 9x^2 + 15x + 7$。$[1]$ 函数在 $x=\alpha$ 处取极大值、$x=\beta$ 处取极小值，证明连接两极值点的线段中点 $M$ 在曲线上；$[2]$ 证明曲线关于点 $M$ 中心对称。
  > ⚠️ **教材勘误提示**：原教材第 335 页（`page_0336.jpg`）$[1]$ 题干将「上にあることを示せ」误印为「上にある**に**ことを示せ」（多了一个助词「に」）。
- **【考点定位】**
  - 三次函数的中心对称性（极值点中点即为拐点与对称中心）。
- **【图解辅助（SVG 矢量图）】**

<svg viewBox="0 0 380 230" xmlns="http://www.w3.org/2000/svg" style="max-width:380px;display:block;margin:10px auto;background:#fafafa;border:1px solid #e0e0e0;border-radius:6px;">
  <defs>
    <marker id="arr8" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0,0 L0,6 L6,3 z" fill="#333"/></marker>
  </defs>
  <line x1="30" y1="115" x2="355" y2="115" stroke="#333" stroke-width="1.3" marker-end="url(#arr8)"/>
  <line x1="70" y1="215" x2="70" y2="18" stroke="#333" stroke-width="1.3" marker-end="url(#arr8)"/>
  <text x="358" y="119" font-size="12" font-style="italic" fill="#333">x</text>
  <text x="76" y="24" font-size="12" font-style="italic" fill="#333">y</text>
  <!-- A(1,14)->(110,45), M(3,-2)->(190,125), B(5,-18)->(270,205) -->
  <path d="M 65,140 C 82,70 95,45 110,45 C 145,45 168,98 190,125 C 212,152 235,205 270,205 C 292,205 312,150 330,45" fill="none" stroke="#1565c0" stroke-width="2.4"/>
  <!-- Line connecting A and B through M -->
  <line x1="110" y1="45" x2="270" y2="205" stroke="#d32f2f" stroke-width="1.4" stroke-dasharray="5,3"/>
  <circle cx="110" cy="45" r="4" fill="#1565c0"/>
  <circle cx="190" cy="125" r="4.5" fill="#d32f2f"/>
  <circle cx="270" cy="205" r="4" fill="#1565c0"/>
  <text x="118" y="42" font-size="12" fill="#1565c0" font-weight="bold">極大 A(1, 14)</text>
  <text x="200" y="128" font-size="12" fill="#d32f2f" font-weight="bold">中点 M(3, -2)</text>
  <text x="276" y="210" font-size="12" fill="#1565c0" font-weight="bold">極小 B(5, -18)</text>
</svg>

- **【分步标准解答】**
  #### $[1]$ 中点 $M$ が曲線 $y = f(x)$ 上にあることの証明
  1. 微分する：
     $$f'(x) = 3x^2 - 18x + 15 = 3(x - 1)(x - 5)$$
  2. $f'(x) = 0 \implies x = 1,\; 5$。増減より $x = 1$ で極大、$x = 5$ で極小となるため、$\alpha = 1,\; \beta = 5$。
     - $f(1) = 1 - 9 + 15 + 7 = 14$
     - $f(5) = 125 - 225 + 75 + 7 = -18$
  3. 2 点 $(1, 14),\; (5, -18)$ を結ぶ線分の中点 $M$ の座標は：
     $$M\left(\frac{1 + 5}{2},\; \frac{14 + (-18)}{2}\right) = M(3,\; -2)$$
  4. $x = 3$ を $f(x)$ に代入すると：
     $$f(3) = 3^3 - 9(3^2) + 15(3) + 7 = 27 - 81 + 45 + 7 = -2$$
     よって点 $M(3, -2)$ は曲線 $y = f(x)$ 上にある。（証明終）

  #### $[2]$ 曲線 $y = f(x)$ が点 $M(3, -2)$ に関して対称であることの証明
  - 曲線 $y = f(x)$ 上の任意の点 $P(x, y)$ について、点 $M(3, -2)$ に関して $P$ と対称な点を $Q(x', y')$ とすると：
    $$\frac{x + x'}{2} = 3,\quad \frac{y + y'}{2} = -2 \implies x' = 6 - x,\quad y' = -4 - y$$
  - 点 $Q$ も曲線 $y = f(x)$ 上にあること、すなわち $f(6 - x) = -4 - f(x)$（同値変形：$f(3 + t) + f(3 - t) = -4$）を示せばよい。
  - ここで $x = 3 + t$ とおいて $f(3 + t)$ を展開する：
    $$\begin{aligned}
    f(3 + t) &= (3 + t)^3 - 9(3 + t)^2 + 15(3 + t) + 7 \\
    &= (27 + 27t + 9t^2 + t^3) - 9(9 + 6t + t^2) + (45 + 15t) + 7 \\
    &= t^3 - 12t - 2
    \end{aligned}$$
    > 💡 讲师批注：令 $x = 3+t$ 展开后，$t^2$ 项（偶次项）彻底消失，只剩奇次项 $t^3-12t$ 和常数 $-2$！这等价于把原点平移到 $M(3,-2)$ 后，方程变为奇函数 $Y = X^3 - 12X$。
  - 同様に $f(3 - t) = (-t)^3 - 12(-t) - 2 = -t^3 + 12t - 2$。
  - よって任意の $t$（すなわち任意の $x$）に対して：
    $$f(3 + t) + f(3 - t) = -4 \iff f(6 - x) = -4 - f(x) = -4 - y = y'$$
  - したがって点 $Q(x', y')$ も曲線 $y = f(x)$ 上にあり、曲線は点 $M(3, -2)$ に関して対称である。（証明終）
- **【最终答案】**
  **$[1]$ 中点 $M(3, -2)$ 满足 $f(3) = -2$，故在曲线上；$[2]$ 证明成立（见上）。**

---

### 演習問題 10 (9)

- **【原题重现与翻译】**
  - 原题：関数 $f(x) = x^3 - 6x^2 + 6ax$ が極大値と極小値を持つような定数 $a$ の値の範囲を求めよ。
  - 中文：求使函数 $f(x) = x^3 - 6x^2 + 6ax$ 同时具有极大值和极小值的常数 $a$ 的取值范围。
- **【考点定位】**
  - 三次函数有极值的充要条件：$f'(x) = 0$ 的判别式 $D > 0$。
- **【分步标准解答】**
  1. 微分する：
     $$f'(x) = 3x^2 - 12x + 6a = 3(x^2 - 4x + 2a)$$
  2. 3 次関数 $f(x)$ が極大値と極小値をもつための必要十分条件は、2 次方程式 $x^2 - 4x + 2a = 0$ が異なる 2 つの実数解をもつことである。
  3. 判別式を $D$ とすると：
     $$\frac{D}{4} = (-2)^2 - 1 \cdot 2a = 4 - 2a > 0 \implies a < 2$$
     > 💡 讲师批注：验算 $a=2$ 时 $f'(x) = 3(x-2)^2 \ge 0$ 无极值；$a=0$ 时 $f'(x) = 3x(x-4)$ 有极值，故 $a < 2$ 正确。
- **【最终答案】**
  **$a < 2$**

---

### 演習問題 10 (10)

- **【原题重现与翻译】**
  - 原题：関数 $f(x) = x^3 + ax^2 + x + 1$ が極値を持たないための必要十分条件を求めよ。
  - 中文：求函数 $f(x) = x^3 + ax^2 + x + 1$ 没有极值的充要条件。
- **【考点定位】**
  - 三次函数无极值的充要条件：$f'(x) = 0$ 的判别式 $D \le 0$（注意包含等号 $D = 0$！）。
- **【分步标准解答】**
  1. 微分する：
     $$f'(x) = 3x^2 + 2ax + 1$$
  2. 3 次関数 $f(x)$ が極値をもたないための必要十分条件は、すべての実数 $x$ に対して $f'(x) \ge 0$（すなわち $f'(x) = 0$ が重解または虚数解をもつこと）である。
  3. 判別式を $D$ とすると：
     $$\frac{D}{4} = a^2 - 3 \cdot 1 = a^2 - 3 \le 0 \implies -\sqrt{3} \le a \le \sqrt{3}$$
     > 💡 讲师批注：高频易错点——千万别漏掉等号！当 $D=0$（即 $a=\pm\sqrt{3}$）时，$f'(x)=3\left(x\pm\frac{1}{\sqrt{3}}\right)^2 \ge 0$ 恒不变号，依然没有极值。
- **【最终答案】**
  **$-\sqrt{3} \le a \le \sqrt{3}$**

---

### 演習問題 10 (11)

- **【原题重现与翻译】**
  - 原题：$a$ は定数とする。$f(x) = x^3 + ax^2 + ax + 1$ が $x = \alpha,\; \beta$（$\alpha < \beta$）で極値をとるとき、$f(\alpha) + f(\beta) = 2$ ならば $a = \square$ である。
  - 中文：设 $a$ 为常数。当 $f(x) = x^3 + ax^2 + ax + 1$ 在 $x = \alpha, \beta$（$\alpha < \beta$）处取极值，且 $f(\alpha) + f(\beta) = 2$ 时，$a = \square$。
- **【考点定位】**
  - 极值存在条件（$D > 0$）+ 极值和的计算（降次法 / 三次函数中心对称性秒杀）。
- **【分步标准解答】**
  1. 微分する：
     $$f'(x) = 3x^2 + 2ax + a$$
  2. **極値をもつ条件**（$f'(x) = 0$ が異なる 2 つの実数解 $\alpha, \beta$ をもつ）：
     $$\frac{D}{4} = a^2 - 3a = a(a - 3) > 0 \implies a < 0 \quad \text{または} \quad a > 3 \quad \cdots\text{①}$$
     > 💡 讲师批注：这一步**绝对不能省**！后面解出 $a=0$ 和 $a=\frac{9}{2}$ 时，必须靠 ① 淘汰掉增根 $a=0$！
  3. 解と係数の関係より：
     $$\alpha + \beta = -\frac{2a}{3}, \qquad \alpha\beta = \frac{a}{3}$$
  4. **方法 1（整式除法による次数下げ / 标准解法）**：
     $f(x)$ を $f'(x) = 3x^2 + 2ax + a$ で割ると：
     $$f(x) = \left(\frac{1}{3}x + \frac{a}{9}\right) f'(x) + \left(\frac{2a}{3} - \frac{2a^2}{9}\right)x + \left(1 - \frac{a^2}{9}\right)$$
     $f'(\alpha) = f'(\beta) = 0$ より：
     $$\begin{aligned}
     f(\alpha) + f(\beta) &= \left(\frac{2a}{3} - \frac{2a^2}{9}\right)(\alpha + \beta) + 2\left(1 - \frac{a^2}{9}\right) \\
     &= \frac{2a(3 - a)}{9} \cdot \left(-\frac{2a}{3}\right) + 2 - \frac{2a^2}{9} \\
     &= \frac{-12a^2 + 4a^3 - 6a^2}{27} + 2 = \frac{4a^3 - 18a^2}{27} + 2
     \end{aligned}$$
     > 💡 讲师批注：**方法 2（EJU 考场秒杀法——利用三次函数对称中心！）**：由 (8) 题结论，三次函数关于拐点 $x_0 = \frac{\alpha+\beta}{2} = -\frac{a}{3}$ 中心对称，故直接有 $f(\alpha) + f(\beta) = 2 f\left(-\frac{a}{3}\right) = 2 \implies f\left(-\frac{a}{3}\right) = 1$！代入得 $-\frac{a^3}{27} + \frac{a^3}{9} - \frac{a^2}{3} + 1 = 1 \implies \frac{2a^3 - 9a^2}{27} = 0$，3 秒出答案！
  5. $f(\alpha) + f(\beta) = 2$ より：
     $$\frac{4a^3 - 18a^2}{27} = 0 \implies 2a^2(2a - 9) = 0 \implies a = 0,\; \frac{9}{2}$$
  6. 条件 ①（$a < 0$ または $a > 3$）より $a = 0$ は不適、よって $a = \dfrac{9}{2}$。
- **【最终答案】**
  **$a = \dfrac{9}{2}$**

---

> 👉 **下册继续**：请查阅 [`note_023_b.md`](file:///Users/baohan/Desktop/EJU/notes_math/note_023_b.md)，包含 **演習問題 10 (12)–(21)** 与 **演習問題 11 (1)** 的完整逐题深度解析。
