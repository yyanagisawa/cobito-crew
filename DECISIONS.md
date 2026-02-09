# DECISIONS

## 判断の構造と学習（Cobito Crew）

本ドキュメントは、Cobito Crew において  
**判断（Approve / Reject）がどのように行われ、  
どのように学習として蓄積され、  
次の前進に引き継がれるか**を定義する。

Cobito Crew は「正解を出す組織」ではない。  
**判断を学習する組織**である。

---

## 0. 判断の前提

Cobito Crew における判断は、主観や雰囲気ではなく、  
明確な構造に基づいて行われる。

- 判断の対象は **Advance** である
- 判断の主体は **常に人間**である
- 判断は **Advance のみ**に対して行われる
- Mission は **Advance の整合性を測る参照軸**であり、評価対象ではない
- 判断は **Mission / Advance / Workspace** の参照軸に照らして行われる
- 判断の履歴は **次の前進を拘束する情報**として保存される

---

## 1. 判断の三層モデル（Advance 評価軸）

Cobito Crew における判断は、以下の三層で構造化される。  
上位層の否定は、下位層を問わず Reject を導く。

---

### 1.1 第1層：Mission Alignment による判断

#### 判断の問い
- この Advance は、Mission を前進させているか？
- Mission の意図・時間軸・方向性と整合しているか？

#### Mission Alignment Reject
以下の場合、**Advance** が Mission Alignment の観点で Reject される。

- Mission の方向性と合っていない
- Mission を満たした「気分」だけを与えている
- Mission を実質的に前進させていない

Mission Alignment Reject は、  
**Advance の質ではなく、前進の方向性の問題**を示す。

---

### 1.2 第2層：Advance 固有の判断

#### 判断の問い
- この Advance は、何を判断させたいのかが明確か？
- 判断に必要な情報・体験が揃っているか？
- 人間が実際に「良い / 悪い」を判断できる形か？

#### Advance Reject
以下の場合、Advance の品質として Reject される。

- 判断点が曖昧である
- 情報や検証手段が不足している
- 途中経過や断片に留まっている

Advance Reject は、  
**前進の質に対するフィードバック**である。

---

### 1.3 第3層：Workspace 文脈による判断

#### 判断の問い
- この判断を、この Workspace の責任範囲で引き受けられるか？
- リスク・コスト・影響を許容できるか？
- 今この Workspace で判断すべき優先度か？

#### Workspace Reject
以下の場合、Advance が Workspace 文脈の制約により Reject される。

- 責任や影響範囲が Workspace を超えている
- リスクやコストが現実的でない
- 優先度やタイミングが不適切である

Workspace Reject は、  
**内容の正しさとは独立した現実制約の判断**である。

---

## 2. Mission Rework（判断以前の前提整理）

Advance を評価できない場合がある。  
それは Advance の問題ではなく、  
**Mission 自体が判断可能な形になっていない場合**である。

この場合、Approve / Reject は行われない。  
代わりに **Mission Rework** が要求される（Mission の再設計要求）。

### Mission Rework が必要な例
- Mission が抽象的すぎる
- 判断軸が含まれていない
- スコープが広すぎる、または矛盾している
- 願望はあるが、判断単位に落とせない

Mission Rework は、判断の失敗ではない。  
**前提条件を整えるための工程**である。

---

## 3. Mission Constraint（暗黙前提の明文化）

Advance を確認する過程で、  
Mission に明示されていなかった前提や制約が  
新たに発見されることがある。

この場合、Mission は否定されない。  
代わりに **Mission Constraint** として制約を追加する。

### Mission Constraint の性質
- Mission を否定しない
- Mission の解釈空間を狭める
- 以降のすべての Advance に適用される

Mission Constraint は、  
**人間の判断と内省から生まれる学習成果**である。

---

## 4. 例外の2軸分類（判断容易性 / リスク制御）

分割・Rework・Constraint は、**理由**で分類する。

- **タイプA：判断容易性**  
  判断可能性を高めるための分割・Rework
- **タイプB：リスク制御**  
  リスクや影響を制御するための分割・Constraint

例外が発生した場合、A/B の種別を判断履歴に付与し、  
次の Advance 生成に反映する。

---

## 5. Mission Constraint の自動提案と確定の線引き

Cobito Crew は、Mission Constraint を  
**自動で抽出・提案してよい**。

ただし、**自動で確定してよい制約は限定される**。

---

### 4.1 自動提案してよい（広く許容）

Advance や Reject 理由から、  
以下のような暗黙前提を提案してよい。

- 時間軸に関する前提
- 実行スピードや規模に関する前提
- 市場・領域の限定
- 既存強み・前提条件に関する示唆

これは判断ではなく、  
**問いの提示**である。

---

### 4.2 条件付きで半自動確定してよい

以下の条件を満たす制約は、  
人間の明示的な同意（Yes）をもって確定してよい。

- 操作的・オペレーション的である
- 価値判断を含まない
- 取り消し可能である

例：
- 初期検証は国内市場に限定する
- 初期予算は月◯◯以内とする

---

### 4.3 自動確定してはならない（人間専用）

以下は、提案は可能だが、  
確定は必ず人間が行う。

- 倫理的判断
- 人生方針・価値観
- 評判・社会的リスク
- 「やりたい / やりたくない」という選好

---

## 6. Reject と Constraint は前進である

Cobito Crew において、

- Reject
- Mission Rework
- Mission Constraint

はいずれも失敗ではない。

これらはすべて、

- 判断軸を明確にし
- 制約条件を追加し
- 次の Advance を鋭くする

ための **構造化された前進**である。

---

## 7. 判断履歴の継承と学習

各判断には、次の情報が紐づけられる。

- 判断の種別  
  （Mission Alignment Reject / Advance Reject / Workspace Reject / Mission Rework / Constraint）
- 判断理由
- 次の Advance に引き継ぐ制約
- 例外タイプ（A: 判断容易性 / B: リスク制御）

Cobito Crew は、  
これらの判断履歴を Mission に紐づけて保持し、  
次の Advance 生成時の前提条件とする。

Cobito Crew が学習するのは、  
正解や成功パターンではない。

**人間の判断軸と制約の地形**である。

---

## 8. 本ドキュメントの位置づけ

本ドキュメントは、Cobito Crew における  
**「判断と学習の憲章」**である。

- 概念の正は CONCEPTS.md
- 運用の正は OPERATIONS.md
- 判断の正は本ドキュメント

判断が曖昧になった場合、  
必ず本ドキュメントに立ち戻ること。
