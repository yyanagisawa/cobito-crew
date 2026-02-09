# OPERATIONS

## Cobito Crew の運用（Mission → Advance）

本ドキュメントは、Cobito Crew を日常的に運用するための手順とルールを定義する。  
概念・原則・語義は CONCEPTS.md と GLOSSARY.md を正とし、本書は運用（How it works）のみを扱う。

---

## 1. 基本運用ループ（最重要）

Cobito Crew の運用は、常に次のループで進む。

1. 人間が Mission を提示する
2. AI（Crew）が自律的に前進する（調査・実装・検証・整理）
3. AI（Crew）が判断可能な Advance を生成する
4. 人間が Advance を受け取り、触って判断する（Approve / Reject）
5. 判断結果が反映され、Mission が前進または再前進する

このループにおいて、Mission から Advance が生成される過程に
人間の判断待ち・承認待ちを必須化しないことを最優先する。

---

## 2. Mission の運用

### 2.1 Mission の位置づけ
Mission は人間の意図であり、Cobito Crew の入力である。  
Mission は実装方法（How）を含まず、「何を前進させ、何を判断したいか」を表す。

### 2.2 Mission の作成主体
Mission は次のいずれかで作成される。

- 人間が直接提示する
- 外部システム（例：Issue）を入力として、AI（Crew）が Mission を生成する

どちらの場合も、Cobito Crew 内部では Mission を正として扱う。

### 2.3 Mission の完了条件
Mission は、目的が満たされ、Advance が人間により Approve された状態をもって完了とみなす。  
Reject は失敗ではなく、Mission を達成するための正当な判断である。

### 2.4 1 Mission : 1 Advance（原則）
Cobito Crew は原則として、1つの Mission に対して 1つの Advance を生成する。  
人間の判断回数を増やすことは、運用上のコストであり、例外として扱う。

分割（複数 Advance）は、以下のいずれかを満たす場合にのみ許容される。

- 1つの Advance では人間が判断しにくい（判断経路が長い、評価点が多い等）
- リスクが高く、一括での判断が危険である
- 直列依存があり、段階的に判断する方が安全である

分割する場合でも、各 Advance は必ず「人間が判断できる状態差分」でなければならない。

分割は理由で分類し、判断履歴に付与する。  
分類の定義は DECISIONS.md に従う。

---

## 3. Advance のライフサイクル

### 3.1 Advance の前提
Advance は、途中経過や断片ではない。  
人間が触る／確認することで、良いか悪いかを判断できる状態で提示される。

### 3.2 Advance の状態
運用上、Advance は以下の状態で扱う。

- draft：AI（Crew）が生成中（人間の対応は不要）
- ready：判断可能（人間が触って判断できる）
- in_review：人間が選択し、判断中（Workspace ロック取得中）
- approved：採用（Mission の前進が確定）
- rejected：却下（同一 Mission の再前進を要求）
- expired：有効期限切れ（環境等が破棄された）

### 3.3 Ready の条件
Advance が ready として提示されるには、最低限以下が揃っている必要がある。

- 人間が判断できる形である（触る／確認する対象が明確）
- 判断に必要な要点が整理されている（何が変わったか、何を確かめるか）
- 安全に試せる入口が用意されている（必要な場合は Preview など）

※詳細な技術要件は ARCHITECTURE.md に委ねる。

### 3.4 Approve / Reject
人間は Advance に対して次の判断を行う。

- Approve：Advance を採用し、結果を反映する
- Reject：Advance を採用せず、同一 Mission の再前進を求める

Reject は、「より良い前進を引き出すためのフィードバック」であり、
Mission を達成するための正常なループである。

---

## 4. Workspace ロックの運用

### 4.1 ロックの目的
Workspace は責任と影響範囲の境界である。  
同一 Workspace で同時に複数の Advance を人間が判断すると、
責任の衝突や判断負荷の増大が起こるため、Workspace ロックを用いる。

### 4.2 ロックのルール
- 同一 Workspace で人間が同時に判断できる Advance は 1つのみとする
- ロックは Advance が in_review になった時点で取得される
- Approve / Reject によりロックは解放される
- ロック中も、AI（Crew）は次の Advance の準備（draft生成）を進めてよい

### 4.3 優先順位と選択
同一 Workspace に複数の Mission / Advance が存在する場合、
人間は「次にプレビューする Advance」を選択できる。

これにより、重要度の高い Mission の Advance を優先して判断できる。  
人間が判断する順序は、運用上の裁量である。

---

## 5. 人間の介入（最小指針）

Cobito Crew が重視するのは、人間が一切介入しないことではなく、
Mission から Advance が生まれるまでの間に、人間の判断待ちを必須化しない構造を作ることである。

**原則：人間は Advance 以外を見ない。**

通常運用では、人間の進捗確認や実装の精読を必須としない。  
人間が早く Advance を受け取り、判断できる可能性を最大化することを優先する。

一方で、人間は品質や仕組みの改善のためにプロセスへ介入してよい。  
ただし、その介入は Advance を得るための必須条件ではなく、
介入が常態化している場合、それは設計上の改善余地を示す。

介入は、以下の目的に限定する。

1. Mission の再設定（Mission Rework）
2. Constraint の明文化（Mission Constraint）
3. Crew 自体の改善（手順・ガードレールの改善）

---

## 6. 既存 Issue 運用があるプロジェクトへの投入

既存プロジェクトでは Issue が運用されていることが多い。  
Cobito Crew は、既存運用を壊さずに取り込むため、次の原則を採用する。

- Issue は入力（燃料）であり、Cobito Crew の正ではない
- Cobito Crew の正は Mission / Advance である
- Issue は必要に応じて Mission に変換され、状態が同期される

運用上は、Issue の存在を前提にしても、
最終的に人間が判断する単位は常に Advance である。

---

## 7. 失敗・中断・やり直し

### 7.1 Reject 後の扱い
Advance が Reject された場合、同一 Mission の下で再前進が行われる。  
次に提示される Advance は、Reject の意図を反映して改善されることが期待される。

### 7.2 中断
Mission や Advance の実行は、状況に応じて中断されうる。  
中断は異常ではなく、優先順位変更や前提条件の変化によって正当化される。

### 7.3 有効期限（Expired）
Advance に紐づく検証環境等は、有効期限によって破棄されうる。  
期限切れは運用上の正常状態であり、必要なら再生成（再前進）を行う。

---

## 8. 本ドキュメントの位置づけ

OPERATIONS.md は、Cobito Crew の「運転マニュアル」である。

- 原則・概念の正は CONCEPTS.md
- 用語の正は GLOSSARY.md
- 技術構成の正は ARCHITECTURE.md

運用が CONCEPTS.md と矛盾する場合、CONCEPTS.md を優先する。
