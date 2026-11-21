# 《EJU 教材全解与备课讲义》数学 002-B（P24–P30）

> **对应源文件**：`work_math/ocr_md/ocr_002_p16-30.md`（后半部分：第一章《数と式、集合と命題》之「集合（演習問題7）」「命題と証明（演習問題8）」；第二章《整数性質》之「約数と倍数・素因数分解・約数の個数と総和（基本概念）」）
> **视觉核对参考图**：`work_math/ref_imgs/page_0024.jpg` – `page_0030.jpg`
> **拆卷说明**：本文件承接 `note_002_a.md`（P16–P23），完整覆盖 P24–P30 的全部概念、勘误与 11 道独立小题。

---

## 一、国内高中基础知识点唤醒与 EJU 考纲差异对比

本部分涵盖日本 **数学Ⅰ（集合と命題）** 的全部逻辑基础，以及 **数学A（整数の性質）** 的开篇核心概念。

### 1.1 集合的基本概念与运算（集合）

- **元素与归属（要素・元）**：$a \in A$（$a$ 属于 $A$），$b \notin A$（$b$ 不属于 $A$）。元素有限称**有限集合**，无限称**无限集合**。
- **包含关系（包含関係）**：$A \subset B$ 表示 $A$ 是 $B$ 的**子集（部分集合）**（日本高中教材直接用 $\subset$ 表示包含于，**允许 $A = B$**，亦可用 $\subseteq$）。空集 $\varnothing$ 是任意集合的子集（$\varnothing \subset A$）。
- **集合表示法**：① **列举法（要素の列挙）** $A = \{1, 3, 5, 7, 9\}$；② **描述法（条件を示す）** $A = \{x \mid 1 \leqq x \leqq 9,\; x \text{ は奇数}\}$。
- **交集、并集与补集（共通部分・和集合・補集合）**：
  - 交集：$A \cap B = \{x \mid x \in A \text{ かつ } x \in B\}$
  - 并集：$A \cup B = \{x \mid x \in A \text{ または } x \in B\}$
  - 补集：在全集（全体集合）$U$ 中，不属于 $A$ 的元素构成 $A$ 的补集，日本记作 **$\overline{A}$**（国内多记作 $\complement_U A$）。
  - 基本性质：$\overline{\varnothing} = U,\; \overline{U} = \varnothing,\; \overline{\overline{A}} = A,\; A \cap \overline{A} = \varnothing,\; A \cup \overline{A} = U,\; A \subset B \iff \overline{A} \supset \overline{B}$。
- **德摩根定律（ド・モルガンの法則）**：
  $$\overline{A \cup B} = \overline{A} \cap \overline{B}, \qquad \overline{A \cap B} = \overline{A} \cup \overline{B}$$
  > ⚠️ **教材勘误提示**：原教材第 24 页（`page_0025.jpg`）存在三处小印刷瑕疵：① `[6]` 和集合的文字描述误写为「$A, B, C$ の少なくとも**一方**」（至少一方），三集合应为「少なくとも**一つ**」（至少一个）；② 三圆韦恩图下方的字母 `B`、`C` 印反倒置；③ `[7] 補集合` 第一行「補集合 $A$」漏印了上划线，应为「補集合 $\overline{A}$」。

### 1.2 命题、条件与逻辑推理（命題と証明）

- **命题（命題）**：能明确判定**真（真）**或**伪（偽）**的语句或数学式。
- **命题与集合的对应**：设满足条件 $p, q$ 的元素集合分别为 $P, Q$：
  - 「$p \Rightarrow q$ 为真」$\iff P \subset Q$
  - 「$q \Rightarrow p$ 为真」$\iff P \supset Q$
  - 「$p \Leftrightarrow q$ 为真」$\iff P = Q$
  > ⚠️ **教材勘误提示**：原教材第 26 页（`page_0027.jpg`）`[2] 命題と条件` 第二行误将双箭头印为单箭头（`$p \Rightarrow q$ は「$p \Rightarrow q$」かつ「$q \Rightarrow p$」を表す`），应修正为 **`$p \Leftrightarrow q$ は「$p \Rightarrow q$」かつ「$q \Rightarrow p$」を表す`**；且下方 `[2] 条件と集合` 编号重复。
- **条件否定与量词否定**：
  - $\overline{p \text{ かつ } q} \iff \overline{p} \text{ または } \overline{q}$；$\overline{p \text{ または } q} \iff \overline{p} \text{ かつ } \overline{q}$。
  - 「すべての $x$ について $p$」（$\forall x,\; p$）的否定是「ある $x$ について $\overline{p}$」（$\exists x,\; \overline{p}$）。
  - 「ある $x$ について $p$」（$\exists x,\; p$）的否定是「すべての $x$ について $\overline{p}$」（$\forall x,\; \overline{p}$）。
- **必要条件・十分条件・同値**：
  - 当 $p \Rightarrow q$ 为真（即 $P \subset Q$）时：**$p$ 是 $q$ 的充分条件（十分条件）**，**$q$ 是 $p$ 的必要条件（必要条件）**。
  - 速记口诀：**「箭尾充分，箭头必要」**（$p \xrightarrow{\text{充分}} q$，$p \xleftarrow{\text{必要}} q$）或**「小推大，小是大的充分，大是小的必要」**。
- **逆・裏・対偶（逆命题・否命题・逆否命题）**：
  - 原命题 $p \Rightarrow q$ 与其**逆否命题（対偶）$\overline{q} \Rightarrow \overline{p}$ 真假完全一致**！
  - 原命题与**逆命题（逆）$q \Rightarrow p$**、**否命题（裏）$\overline{p} \Rightarrow \overline{q}$** 真假不一定一致（但「逆」与「裏」互为対偶，真假一致）。

### 1.3 整数的性质开篇（第二章：約数と倍数・素因数分解）

- **约数与倍数**：若存在整数 $k$ 使 $a = bk$，称 $b$ 是 $a$ 的**约数（約数）**，$a$ 是 $b$ 的**倍数（倍数）**。
- **倍数判定法（倍数の判定法）**：
  - $2$ 的倍数：个位（一の位）为偶数 $0, 2, 4, 6, 8$。
  - $5$ 的倍数：个位为 $0$ 或 $5$。
  - $4$ 的倍数：末两位（下 2 桁）为 $4$ 的倍数。
  - $3$ 的倍数（$9$ 的倍数）：各位数字之**和**为 $3$ 的倍数（$9$ 的倍数）。
  > ⚠️ **教材勘误提示**：原教材第 29 页（`page_0030.jpg`）`[1.2] 倍数の判定法` 有两处明显笔误：①「2 の倍数」括号中竟写着 `(0, 2, 4, 6, 8, 10 のいずれか)`——个位数不可能为 `10`，应删去 `10`；②「9 の倍数」漏印「の和」，应为「各位の数の**和**が 9 の倍数」。
- **素数、合数与素因数分解**：$2$ 以上的自然数，除 $1$ 和自身外无其他正约数的叫**素数（素数）**，否则叫**合成数（合成数）**。**$1$ 既不是素数也不是合数**。
- **正约数的个数与总和（約数の個数・総和）**：
  若自然数 $N$ 的素因数分解为 $N = p^a q^b r^c \cdots$（$p, q, r$ 为互异素数），则：
  - **正约数个数**：$(a + 1)(b + 1)(c + 1)\cdots$
  - **正约数总和**：$(1 + p + p^2 + \cdots + p^a)(1 + q + \cdots + q^b)(1 + r + \cdots + r^c)\cdots$

### 1.4 知识结构图解（SVG 矢量图：德摩根定律 & 逆・裏・対偶四角关系）

<svg viewBox="0 0 680 215" width="100%" xmlns="http://www.w3.org/2000/svg" style="max-width:680px;display:block;margin:12px auto;font-family:-apple-system,BlinkMacSystemFont,'Hiragino Sans','Noto Sans CJK SC',sans-serif;">
  <rect x="0" y="0" width="680" height="215" rx="8" fill="#f8fafc" stroke="#cbd5e1"/>
  <!-- 左侧：德摩根定律示意 -->
  <text x="160" y="24" font-size="13" font-weight="bold" fill="#0f172a" text-anchor="middle">ド・モルガンの法則（韦恩图）</text>
  <!-- 图1: overline(A U B) = overline(A) n overline(B) -->
  <rect x="20" y="38" width="130" height="92" rx="4" fill="#bfdbfe" stroke="#1e40af" stroke-width="1.5"/>
  <circle cx="67" cy="84" r="30" fill="#ffffff" stroke="#1e293b" stroke-width="1.4"/>
  <circle cx="103" cy="84" r="30" fill="#ffffff" stroke="#1e293b" stroke-width="1.4"/>
  <circle cx="67" cy="84" r="30" fill="none" stroke="#1e293b" stroke-width="1.4"/>
  <text x="27" y="53" font-size="11" font-weight="bold" fill="#1e3a8a">U</text>
  <text x="53" y="88" font-size="12" fill="#0f172a">A</text>
  <text x="112" y="88" font-size="12" fill="#0f172a">B</text>
  <text x="85" y="150" font-size="12" fill="#1e40af" font-weight="bold" text-anchor="middle">A∪B の補 = A補 ∩ B補</text>
  <text x="85" y="168" font-size="11" fill="#475569" text-anchor="middle">（两圆外部阴影）</text>
  <!-- 图2: overline(A n B) = overline(A) U overline(B) -->
  <rect x="170" y="38" width="130" height="92" rx="4" fill="#fecaca" stroke="#b91c1c" stroke-width="1.5"/>
  <defs>
    <clipPath id="clipA"><circle cx="217" cy="84" r="30"/></clipPath>
  </defs>
  <circle cx="253" cy="84" r="30" fill="#ffffff" clip-path="url(#clipA)"/>
  <circle cx="217" cy="84" r="30" fill="none" stroke="#1e293b" stroke-width="1.4"/>
  <circle cx="253" cy="84" r="30" fill="none" stroke="#1e293b" stroke-width="1.4"/>
  <text x="177" y="53" font-size="11" font-weight="bold" fill="#991b1b">U</text>
  <text x="202" y="88" font-size="12" fill="#0f172a">A</text>
  <text x="262" y="88" font-size="12" fill="#0f172a">B</text>
  <text x="235" y="150" font-size="12" fill="#b91c1c" font-weight="bold" text-anchor="middle">A∩B の補 = A補 ∪ B補</text>
  <text x="235" y="168" font-size="11" fill="#475569" text-anchor="middle">（仅挖去中间交集）</text>
  <!-- 分隔线 -->
  <line x1="325" y1="18" x2="325" y2="198" stroke="#cbd5e1" stroke-dasharray="4,4"/>
  <!-- 右侧：逆・裏・対偶四角关系图 -->
  <text x="502" y="24" font-size="13" font-weight="bold" fill="#0f172a" text-anchor="middle">逆・裏・対偶の四角関係</text>
  <!-- 四个命题框 -->
  <rect x="355" y="42" width="106" height="34" rx="5" fill="#dbeafe" stroke="#2563eb" stroke-width="1.6"/>
  <text x="408" y="64" font-size="13" font-weight="bold" fill="#1e3a8a" text-anchor="middle">p ⇒ q（原）</text>
  <rect x="545" y="42" width="106" height="34" rx="5" fill="#f1f5f9" stroke="#64748b" stroke-width="1.5"/>
  <text x="598" y="64" font-size="13" font-weight="bold" fill="#334155" text-anchor="middle">q ⇒ p（逆）</text>
  <rect x="355" y="148" width="106" height="34" rx="5" fill="#f1f5f9" stroke="#64748b" stroke-width="1.5"/>
  <text x="408" y="170" font-size="13" font-weight="bold" fill="#334155" text-anchor="middle">p̄ ⇒ q̄（裏）</text>
  <rect x="545" y="148" width="106" height="34" rx="5" fill="#dbeafe" stroke="#2563eb" stroke-width="1.6"/>
  <text x="598" y="170" font-size="13" font-weight="bold" fill="#1e3a8a" text-anchor="middle">q̄ ⇒ p̄（対偶）</text>
  <!-- 连线与标签 -->
  <line x1="461" y1="59" x2="545" y2="59" stroke="#475569" stroke-width="1.5"/>
  <rect x="490" y="49" width="26" height="19" fill="#f8fafc"/>
  <text x="503" y="63" font-size="12" fill="#475569" text-anchor="middle">逆</text>
  <line x1="461" y1="165" x2="545" y2="165" stroke="#475569" stroke-width="1.5"/>
  <rect x="490" y="155" width="26" height="19" fill="#f8fafc"/>
  <text x="503" y="169" font-size="12" fill="#475569" text-anchor="middle">逆</text>
  <line x1="408" y1="76" x2="408" y2="148" stroke="#475569" stroke-width="1.5"/>
  <rect x="395" y="102" width="26" height="19" fill="#f8fafc"/>
  <text x="408" y="116" font-size="12" fill="#475569" text-anchor="middle">裏</text>
  <line x1="598" y1="76" x2="598" y2="148" stroke="#475569" stroke-width="1.5"/>
  <rect x="585" y="102" width="26" height="19" fill="#f8fafc"/>
  <text x="598" y="116" font-size="12" fill="#475569" text-anchor="middle">裏</text>
  <!-- 对角线：対偶（真偽一致） -->
  <line x1="455" y1="76" x2="551" y2="148" stroke="#2563eb" stroke-width="2"/>
  <line x1="551" y1="76" x2="455" y2="148" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="4,3"/>
  <rect x="466" y="100" width="74" height="22" rx="4" fill="#eff6ff" stroke="#2563eb"/>
  <text x="503" y="115" font-size="11.5" fill="#1d4ed8" font-weight="bold" text-anchor="middle">対偶(真偽一致)</text>
</svg>

### 1.5 国内高中 vs. 日本 EJU 考纲差异与符号习惯

| 对比维度 | 国内高中习惯 | 日本 EJU 习惯 | 备课/应试提醒 |
| :--- | :--- | :--- | :--- |
| **子集符号** | $\subseteq$（子集），$\subsetneqq$（真子集） | **$\subset$ 表示子集（允许相等）**，真子集写作「$A \subset B$ かつ $A \neq B$」 | **极易混淆！** 看到日本题里的 $A \subset B$，千万不要默认 $A \neq B$ |
| **补集与否定符号** | 补集 $\complement_U A$；否定 $\neg p$ | 补集 **$\overline{A}$**；条件否定 **$\overline{p}$**（均用上划线） | 读作「エー・バー（$A$ bar）」「ピー・バー（$p$ bar）」 |
| **逻辑联结词** | 且（$\land$）、或（$\lor$） | 日文假名 **「かつ」**（且）、**「または」**（或） | 否定变换时「かつ」与「または」互换 |
| **逆否命题与否命题** | 逆命题、否命题、逆否命题 | **逆（ぎゃく）**、**裏（うら）**、**対偶（たいぐう）** | 切勿把「裏（否命题）」与「対偶（逆否命题）」弄混！ |
| **质数 / 合数** | 质数、合数、分解质因数 | **素数（そすう）**、**合成数（ごうせいすう）**、**素因数分解** | EJU 整数题高频词汇，务必熟记 |

---

## 二、日文核心词汇与公式假名注音

### 2.1 本切片（后半）日文核心词汇

- 集合（しゅうごう / shuugou） — 集合
- 要素（ようそ / youso） — 元素（亦称 元 / げん）
- 属する（ぞくする / zokusuru） — 属于（$a \in A$）
- 有限集合（ゆうげんしゅうごう / yuugen shuugou） — 有限集
- 無限集合（むげんしゅうごう / mugen shuugou） — 无限集
- 部分集合（ぶぶんしゅうごう / bubun shuugou） — 子集
- 包含関係（ほうがんかんけい / hougan kankei） — 包含关系
- 空集合（くうしゅうごう / kuushuugou） — 空集（$\varnothing$）
- 共通部分（きょうつうぶぶん / kyoutsuu bubun） — 交集（$A \cap B$）
- 和集合（わしゅうごう / washuugou） — 并集（$A \cup B$）
- ベン図（べんず / benzu） — 韦恩图（Venn diagram）
- 全体集合（ぜんたいしゅうごう / zentai shuugou） — 全集（$U$）
- 補集合（ほしゅうごう / hoshuugou） — 补集（$\overline{A}$）
- ド・モルガンの法則（どもるがんのほうそく / do morugan no housoku） — 德摩根定律
- 命題（めいだい / meidai） — 命题
- 真（しん / shin） — 真（命题成立）
- 偽（ぎ / gi） — 伪、假（命题不成立）
- 反例（はんれい / hanrei） — 反例
- 条件（じょうけん / jouken） — 条件
- 仮定（かてい / katei） — 题设、假设
- 結論（けつろん / ketsuron） — 结论
- 否定（ひてい / hitei） — 否定
- 必要条件（ひつようじょうけん / hitsuyou jouken） — 必要条件
- 十分条件（じゅうぶんじょうけん / juubun jouken） — 十分条件
- 必要十分条件（ひつようじゅうぶんじょうけん / hitsuyou juubun jouken） — 充要条件
- 同値（どうち / douchi） — 等价（$p \Leftrightarrow q$）
- 逆（ぎゃく / gyaku） — 逆命题（$q \Rightarrow p$）
- 裏（うら / ura） — 否命题（$\overline{p} \Rightarrow \overline{q}$）
- 対偶（たいぐう / taiguu） — 逆否命题（$\overline{q} \Rightarrow \overline{p}$）
- 約数（やくすう / yakusuu） — 约数、因数
- 倍数（ばいすう / baisuu） — 倍数
- 最大公約数（さいだいこうやくすう / saidai kouyakusuu） — 最大公约数
- 最小公倍数（さいしょうこうばいすう / saishou koubaisuu） — 最小公倍数
- 素数（そすう / sosuu） — 素数（质数）
- 合成数（ごうせいすう / gouseisuu） — 合数
- 素因数（そいんすう / soinsuu） — 素因数（质因数）
- 素因数分解（そいんすうぶんかい / soinsuu bunkai） — 素因数分解（分解质因数）
- 総和（そうわ / souwa） — 总和

### 2.2 核心公式与符号的日本课堂口语读法

1. **集合交、并、补** $A \cap B,\; A \cup B,\; \overline{A}$
   - $A \cap B$：**エー かつ ビー**（或 **エー キャップ ビー**）
   - $A \cup B$：**エー または ビー**（或 **エー カップ ビー**）
   - $\overline{A}$：**エー バー**（$A$ bar）
   - $\varnothing$：**ファイ**（phi）或 **くうしゅうごう**
2. **命题箭头** $p \Rightarrow q,\; p \Leftrightarrow q$
   - $p \Rightarrow q$：**ピー ならば キュー**
   - $p \Leftrightarrow q$：**ピー と キュー は どうち**（或 **ピー どうち キュー**）
3. **正约数个数公式** $(a+1)(b+1)(c+1)$
   - 课堂读法：**しすうに いちを たして かける**（把各素因数的指数加 1 再相乘）

---

## 三、逐题深度解析（不可跳步）

---

### 演習問題 7（集合）

#### 演習問題 7-(1)
- **【原题重现与翻译】**
  - 原题：実数 $a$ に対して、$2$ つの集合を
    $$A = \{a - 1,\; 4,\; a^2 - 5a + 6\},\qquad B = \{1,\; a^2 - 4,\; a^2 - 7a + 12,\; 4\}$$
    とする。$A \cap B = \{0, 4\}$ であるとき、$a$ の値を求めよ。
  - 中文：对于实数 $a$，设两个集合 $A = \{a - 1,\; 4,\; a^2 - 5a + 6\}$，$B = \{1,\; a^2 - 4,\; a^2 - 7a + 12,\; 4\}$。当 $A \cap B = \{0, 4\}$ 时，求 $a$ 的值。
- **【考点定位】**
  - 含参集合的交集运算 + **回代检验（逆のチェック：互异性与交集元素不多不少）**。
- **【分步标准解答】**
  $$A \cap B = \{0, 4\} \text{ であるから、} 0 \in A \text{ である。}$$
  $$\text{よって、} a - 1 = 0 \;\text{ または }\; a^2 - 5a + 6 = 0$$
  > 💡 讲师批注：先挑元素个数较少、结构更简单的集合 $A$ 下手！已知 $4$ 已在 $A$ 中，因此 $0$ 必然等于 $a - 1$ 或 $a^2 - 5a + 6$。

  - **$a - 1 = 0$ のとき**：$a = 1$
    $$A = \{0,\; 4,\; 2\},\qquad B = \{1,\; -3,\; 6,\; 4\}$$
    $$\text{このとき、} A \cap B = \{4\} \neq \{0, 4\} \quad (\text{不適})$$

  - **$a^2 - 5a + 6 = 0$ のとき**：$(a - 2)(a - 3) = 0$ より、$a = 2$ または $a = 3$。
    - **[i] $a = 2$ のとき**：
      $$A = \{1,\; 4,\; 0\},\qquad B = \{1,\; 0,\; 2,\; 4\}$$
      $$\text{このとき、} A \cap B = \{0,\; 1,\; 4\} \neq \{0, 4\} \quad (\text{不適})$$
      > 💡 讲师批注：**全题最大陷阱就在 $a = 2$！** 此时虽然 $0 \in A$ 且 $0 \in B$，但 $1$ 也同时出现在 $A$ 和 $B$ 中，导致交集多了一个元素 $1$！含参集合题**必须将每个候选值回代写出完整集合 $A, B$**，检查交集是否「不多也不少」。

    - **[ii] $a = 3$ のとき**：
      $$A = \{2,\; 4,\; 0\},\qquad B = \{1,\; 5,\; 0,\; 4\}$$
      $$\text{このとき、} A \cap B = \{0,\; 4\} \text{ となり、条件を満たす。}$$
- **【最终答案】**
  **$a = 3$**

---

#### 演習問題 7-(2)-[1]
- **【原题重现与翻译】**
  > ⚠️ **教材勘误提示**：原教材第 26 页（`page_0027.jpg`）将本题印为 `$A = \{4n + 1 \mid n \in \mathbb{Z}\},\; B = \{4n + 1 \mid n \in \mathbb{Z}\}$ であるとき、$A \subset B$ かつ $A \neq B$`。两个集合完全相同，不可能证明 $A \neq B$，属于明显排版印刷错误！
  > 参照日本标准教材经典原题，集合 $B$ 应修正为 **$B = \{2n + 1 \mid n \in \mathbb{Z}\}$**（全体奇数集）。下面按修正后的原题给出标准证明。
  - 修正原题：$\mathbb{Z}$ を整数全体の集合とするとき、次のことを証明せよ。
    $[1]\; A = \{4n + 1 \mid n \in \mathbb{Z}\},\; B = \{2n + 1 \mid n \in \mathbb{Z}\}$ であるとき、$A \subset B$ かつ $A \neq B$。
  - 中文：设 $\mathbb{Z}$ 为全体整数的集合。当 $A = \{4n + 1 \mid n \in \mathbb{Z}\},\; B = \{2n + 1 \mid n \in \mathbb{Z}\}$ 时，证明 $A \subset B$ 且 $A \neq B$。
- **【考点定位】**
  - 无限整数集合的**真包含关系（真部分集合）证明**：先证任取 $x \in A \Rightarrow x \in B$，再举反例证存在 $y \in B$ 但 $y \notin A$。
- **【分步标准解答】**
  1. **$A \subset B$ の証明**：
     $$x \in A \text{ とすると、ある整数 } n \text{ を用いて } x = 4n + 1 \text{ と表せる。}$$
     $$x = 4n + 1 = 2(2n) + 1$$
     $$n \in \mathbb{Z} \text{ より } 2n \in \mathbb{Z} \text{ であるから、} x \in B\text{。}$$
     $$\text{よって、} A \subset B \text{ が成り立つ。}$$
     > 💡 讲师批注：证明 $A \subset B$ 的黄金模板：任取 $x \in A$，把 $x$ 改写成集合 $B$ 的代表元形式 $2(\text{整数}) + 1$，并明确声明括号内仍是整数（$2n \in \mathbb{Z}$）。

  2. **$A \neq B$ の証明**：
     $$3 = 2 \cdot 1 + 1 \text{ より } 3 \in B \text{ である。}$$
     $$\text{一方、} 4n + 1 = 3 \text{ とすると } 4n = 2 \iff n = \frac{1}{2} \notin \mathbb{Z} \text{ となるため、} 3 \notin A\text{。}$$
     $$\text{したがって、} A \neq B \text{ である。}$$
     > 💡 讲师批注：证明两个集合不相等，只需构造一个具体的反例元素（如 $3$ 或 $-1$），说明它属于 $B$ 但不属于 $A$ 即可。
- **【最终答案】**
  **証明済（修正版 $B = \{2n+1 \mid n \in \mathbb{Z}\}$ のもとで $A \subset B$ かつ $A \neq B$）**

---

#### 演習問題 7-(2)-[2]
- **【原题重现与翻译】**
  - 原题：$\mathbb{Z}$ を整数全体の集合とするとき、次のことを証明せよ。
    $[2]\; A = \{5n + 2 \mid n \in \mathbb{Z}\},\; B = \{5n - 3 \mid n \in \mathbb{Z}\}$ であるとき、$A = B$。
  - 中文：设 $\mathbb{Z}$ 为全体整数的集合。当 $A = \{5n + 2 \mid n \in \mathbb{Z}\},\; B = \{5n - 3 \mid n \in \mathbb{Z}\}$ 时，证明 $A = B$。
- **【考点定位】**
  - 集合相等的标准证明法：**双向包含（$A \subset B$ かつ $B \subset A \iff A = B$）**。
- **【分步标准解答】**
  1. **$A \subset B$ の証明**：
     $$x \in A \text{ とすると、ある整数 } n \text{ を用いて } x = 5n + 2 \text{ と表せる。}$$
     $$x = 5n + 2 = 5(n + 1) - 3$$
     $$n \in \mathbb{Z} \text{ より } n + 1 \in \mathbb{Z} \text{ であるから、} x \in B\text{。よって } A \subset B\text{。}$$
     > 💡 讲师批注：配凑恒等式 $+2 = +5 - 3$，将 $5n+2$ 改写成 $5(n+1) - 3$。

  2. **$B \subset A$ の証明**：
     $$y \in B \text{ とすると、ある整数 } m \text{ を用いて } y = 5m - 3 \text{ と表せる。}$$
     $$y = 5m - 3 = 5(m - 1) + 2$$
     $$m \in \mathbb{Z} \text{ より } m - 1 \in \mathbb{Z} \text{ であるから、} y \in A\text{。よって } B \subset A\text{。}$$

  $$\text{以上より、} A \subset B \text{ かつ } B \subset A \text{ であるから、} A = B \text{ である。}$$
- **【最终答案】**
  **証明済（$A \subset B$ かつ $B \subset A$ より $A = B$）**

---

### 演習問題 8（必要条件・十分条件）

> **共通题干**：次の $\square$ に最も適する語句を（ア）～（エ）からえらべ。$a,\; b,\; m,\; x,\; y$ は実数とする。
> - （ア）必要十分条件である（充要条件）
> - （イ）必要であるが十分条件ではない（必要不充分条件）
> - （ウ）十分条件であるが必要条件ではない（充分不必要条件）
> - （エ）必要条件でも十分条件でもない（既不充分也不必要条件）

- **【通法图解（SVG 矢量图：主语 $p$ 与客语 $q$ 判定框架）】**

<svg viewBox="0 0 600 105" width="100%" xmlns="http://www.w3.org/2000/svg" style="max-width:600px;display:block;margin:10px auto;font-family:-apple-system,BlinkMacSystemFont,'Hiragino Sans','Noto Sans CJK SC',sans-serif;">
  <rect x="0" y="0" width="600" height="105" rx="6" fill="#f8fafc" stroke="#cbd5e1"/>
  <text x="300" y="22" font-size="12.5" font-weight="bold" fill="#0f172a" text-anchor="middle">「p は q であるための □」判定公式（主语 p 在左！）</text>
  <!-- 4个结果盒 -->
  <rect x="16" y="34" width="134" height="58" rx="5" fill="#dcfce7" stroke="#16a34a"/>
  <text x="83" y="54" font-size="12" font-weight="bold" fill="#166534" text-anchor="middle">p ⇒ q (真) / q ⇒ p (真)</text>
  <text x="83" y="76" font-size="12" fill="#15803d" text-anchor="middle">（ア）必要十分条件</text>

  <rect x="160" y="34" width="134" height="58" rx="5" fill="#fef3c7" stroke="#d97706"/>
  <text x="227" y="54" font-size="12" font-weight="bold" fill="#92400e" text-anchor="middle">p ⇒ q (偽) / q ⇒ p (真)</text>
  <text x="227" y="76" font-size="12" fill="#b45309" text-anchor="middle">（イ）必要のみ</text>

  <rect x="304" y="34" width="134" height="58" rx="5" fill="#dbeafe" stroke="#2563eb"/>
  <text x="371" y="54" font-size="12" font-weight="bold" fill="#1e3a8a" text-anchor="middle">p ⇒ q (真) / q ⇒ p (偽)</text>
  <text x="371" y="76" font-size="12" fill="#1d4ed8" text-anchor="middle">（ウ）十分のみ</text>

  <rect x="448" y="34" width="136" height="58" rx="5" fill="#fee2e2" stroke="#dc2626"/>
  <text x="516" y="54" font-size="12" font-weight="bold" fill="#991b1b" text-anchor="middle">p ⇒ q (偽) / q ⇒ p (偽)</text>
  <text x="516" y="76" font-size="12" fill="#b91c1c" text-anchor="middle">（エ）どちらでもない</text>
</svg>

---

#### 演習問題 8-(1)
- **【原题重现与翻译】**
  - 原题：$x = y$ は $x^2 = y^2$ であるための $\square$
  - 中文：$x = y$ 是 $x^2 = y^2$ 的 $\square$。
- **【考点定位】**
  - 平方等价性与反例构造（$x^2 = y^2 \iff x = \pm y$）。
- **【分步标准解答】**
  - $x = y \Rightarrow x^2 = y^2$：**真**（両辺を 2 乗すれば成り立つ）。
  - $x^2 = y^2 \Rightarrow x = y$：**偽**（反例：$x = 1,\; y = -1$ のとき $1^2 = (-1)^2$ だが $1 \neq -1$）。
  > 💡 讲师批注：主语 $p$ 能推出 $q$，但 $q$ 不能推出 $p$，故为「十分条件であるが必要条件ではない」。
- **【最终答案】**
  **（ウ）十分条件であるが必要条件ではない**

---

#### 演習問題 8-(2)
- **【原题重现与翻译】**
  - 原题：$x = 3$ は $x^2 - 5x + 6 = 0$ であるための $\square$
  - 中文：$x = 3$ 是 $x^2 - 5x + 6 = 0$ 的 $\square$。
- **【考点定位】**
  - 方程解集的包含关系（$P = \{3\} \subset Q = \{2, 3\}$）。
- **【分步标准解答】**
  $$x^2 - 5x + 6 = 0 \iff (x - 2)(x - 3) = 0 \iff x = 2 \text{ または } x = 3$$
  - $x = 3 \Rightarrow x^2 - 5x + 6 = 0$：**真**（$\{3\} \subset \{2, 3\}$）。
  - $x^2 - 5x + 6 = 0 \Rightarrow x = 3$：**偽**（反例：$x = 2$）。
  > 💡 讲师批注：集合角度秒判：小集合 $\{3\}$ 是大集合 $\{2, 3\}$ 的充分不必要条件。
- **【最终答案】**
  **（ウ）十分条件であるが必要条件ではない**

---

#### 演習問題 8-(3)
- **【原题重现与翻译】**
  - 原题：$xy > 0$ は $x > 0$ であるための $\square$
  - 中文：$xy > 0$ 是 $x > 0$ 的 $\square$。
- **【考点定位】**
  - 乘积符号判定（$xy > 0 \iff x, y$ 同号，含「同为负」情况）。
- **【分步标准解答】**
  - $xy > 0 \Rightarrow x > 0$：**偽**（反例：$x = -1,\; y = -1$ のとき $xy = 1 > 0$ だが $x < 0$）。
  - $x > 0 \Rightarrow xy > 0$：**偽**（反例：$x = 1,\; y = -1$ のとき $x > 0$ だが $xy = -1 < 0$；$y = 0$ も反例）。
  > 💡 讲师批注：双向均能举出反例，既不充分也不必要！
- **【最终答案】**
  **（エ）必要条件でも十分条件でもない**

---

#### 演習問題 8-(4)
- **【原题重现与翻译】**
  - 原题：$\angle A = 90^\circ$ は、$\triangle ABC$ が直角三角形であるための $\square$
  - 中文：$\angle A = 90^\circ$ 是 $\triangle ABC$ 为直角三角形的 $\square$。
- **【考点定位】**
  - 几何定义的包含关系（直角三角形的直角可以在 $A, B, C$ 任意一处）。
- **【分步标准解答】**
  - $\angle A = 90^\circ \Rightarrow \triangle ABC$ が直角三角形：**真**。
  - $\triangle ABC$ が直角三角形 $\Rightarrow \angle A = 90^\circ$：**偽**（反例：$\angle B = 90^\circ$ や $\angle C = 90^\circ$ の場合）。
  > 💡 讲师批注：经典几何陷阱，直角三角形不一定非得 $\angle A$ 是直角。
- **【最终答案】**
  **（ウ）十分条件であるが必要条件ではない**

---

#### 演習問題 8-(5)
- **【原题重现与翻译】**
  - 原题：$a \geqq 0$ は $\sqrt{a^2} = a$ であるための $\square$
  - 中文：$a \geqq 0$ 是 $\sqrt{a^2} = a$ 的 $\square$。
- **【考点定位】**
  - 平方根性质 $\sqrt{a^2} = |a|$ 与绝对值性质 $|a| = a \iff a \geqq 0$。
- **【分步标准解答】**
  $$\sqrt{a^2} = |a| \text{ であり、} |a| = a \iff a \geqq 0$$
  - $a \geqq 0 \Rightarrow \sqrt{a^2} = a$：**真**。
  - $\sqrt{a^2} = a \Rightarrow a \geqq 0$：**真**（$\sqrt{a^2} \geqq 0$ であるから、それが $a$ に等しければ必ず $a \geqq 0$）。
  > 💡 讲师批注：注意 $a = 0$ 时 $\sqrt{0^2} = 0$ 也成立！因此是 $a \geqq 0$（含等号）与 $\sqrt{a^2} = a$ 严格等价。如果题目改成 $a > 0$，答案就会变成（ウ）！
- **【最终答案】**
  **（ア）必要十分条件である**

---

#### 演習問題 8-(6)
- **【原题重现与翻译】**
  - 原题：$a = b$ は $ma = mb$ であるための $\square$
  - 中文：$a = b$ 是 $ma = mb$ 的 $\square$。
- **【考点定位】**
  - 等式性质与**零因子 $m = 0$ 陷阱**。
- **【分步标准解答】**
  - $a = b \Rightarrow ma = mb$：**真**（両辺に $m$ を掛けて成り立つ）。
  - $ma = mb \Rightarrow a = b$：**偽**（反例：$m = 0,\; a = 1,\; b = 2$ のとき $0 \cdot 1 = 0 \cdot 2$ だが $a \neq b$）。
  > 💡 讲师批注：EJU 最高频坑点之一！$ma = mb \iff m(a - b) = 0 \iff m = 0 \text{ または } a = b$，两边同除字母 $m$ 之前必须确认 $m \neq 0$！
- **【最终答案】**
  **（ウ）十分条件であるが必要条件ではない**

---

#### 演習問題 8-(7)
- **【原题重现与翻译】**
  - 原题：$x + y > 2$ は $x > 1$ かつ $y > 1$ であるための $\square$
  - 中文：$x + y > 2$ 是「$x > 1$ 且 $y > 1$」的 $\square$。
- **【考点定位】**
  - 同向不等式的可加性（单向成立，不可逆）。
- **【分步标准解答】**
  - $x + y > 2 \Rightarrow (x > 1 \text{ かつ } y > 1)$：**偽**（反例：$x = 3,\; y = 0$ のとき $x + y = 3 > 2$ だが $y \not> 1$）。
  - $(x > 1 \text{ かつ } y > 1) \Rightarrow x + y > 2$：**真**（$x > 1$ と $y > 1$ の両辺を加えて $x + y > 2$）。
  > 💡 讲师批注：左推右为伪、右推左为真，故主语 $p$ 是 $q$ 的「必要であるが十分条件ではない」。
- **【最终答案】**
  **（イ）必要であるが十分条件ではない**

---

#### 演習問題 8-(8)
- **【原题重现与翻译】**
  - 原题：$A,\; B$ を $2$ つの集合とする。$a$ が $A \cup B$ の要素であることは、$a$ が $A$ の要素であるための $\square$
  - 中文：设 $A, B$ 为两个集合。$a$ 是 $A \cup B$ 的元素，是 $a$ 是 $A$ 的元素的 $\square$。
- **【考点定位】**
  - 集合并集包含关系 $A \subset A \cup B$ 与必要条件判定。
- **【分步标准解答】**
  - $a \in A \cup B \Rightarrow a \in A$：**偽**（反例：$a \in B$ かつ $a \notin A$ のとき、$a \in A \cup B$ だが $a \notin A$）。
  - $a \in A \Rightarrow a \in A \cup B$：**真**（常に $A \subset A \cup B$ が成り立つため）。
  > 💡 讲师批注：直接用「大集合是小集合的必要条件」秒杀：$A \cup B \supset A$，主语在大集合 $A \cup B$，故为必要不充分条件！
- **【最终答案】**
  **（イ）必要であるが十分条件ではない**
