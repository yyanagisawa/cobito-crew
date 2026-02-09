# ARCHITECTURE

## Cobito Crew のアーキテクチャ（高レベル）

本ドキュメントは、Cobito Crew の全体構成を高レベルで説明する。  
ここでは「何がどの責務を担うか」を明確にし、  
具体的な技術選定や実装詳細には踏み込まない。

概念・原則・用語は、CONCEPTS.md および GLOSSARY.md を正とする。

---

## 1. 設計方針

Cobito Crew のアーキテクチャは、次の原則に基づいて設計される。

- **Mission / Advance / Workspace が中心であること**
- **人間の判断待ちを前進の条件にしないこと**
- **AI（Crew）が自律的に前進できること**
- **責任と影響範囲が明確に分離されていること**
- **将来、実装やAIモデルが入れ替わっても成立すること**

Cobito Crew は、個々のAIやツールの集合ではなく、  
前進と判断を分離するための構造である。

---

## 2. 全体構成（論理）

Cobito Crew は、論理的に次の3層で構成される。

### 2.1 Control Plane（統制層）
Mission と Advance を管理し、全体の進行を制御する層。

- Mission の受付と状態管理
- Advance の生成・状態遷移の管理
- Workspace ロックの制御
- 人間とのインターフェース（取得・判断・反映）

Cobito Crew の「司令塔」に相当する。

---

### 2.2 Execution Plane（実行層）
AI（Crew）が実際に前進を行う層。

- Mission の理解と分解
- 調査・実装・検証・整理
- 判断可能な Advance の生成

Execution Plane は、複数の実行主体（AI、エージェント、ツール）を含みうるが、  
それらは交換可能であり、アーキテクチャの核ではない。

---

### 2.3 Review Interface（判断接点）
人間が Advance を受け取り、判断を行う接点。

- Advance の一覧取得
- プレビューや確認対象へのアクセス
- Approve / Reject の入力

この層は、人間の判断を最小限の操作で行えることを最優先とする。

---

## 3. データの正（Source of Truth）

Cobito Crew におけるデータの正は明確に分離される。

- **Mission / Advance / Workspace**  
  → Cobito Crew 内部の永続データが正

- **コード・成果物・外部リソース**  
  → 各 Workspace が指す外部システムが正

- **Issue / PR などの外部管理単位**  
  → 入力または補助情報であり、正ではない

これにより、外部プロジェクトや既存運用に依存しない統制が可能となる。

---

## 4. Workspace 分離と安全性

Workspace は、責任と影響範囲を分離するための最小単位である。

- Workspace を跨いで Mission や Advance が干渉することはない
- Workspace ごとに権限・実行環境・リソースが分離される
- 同一 Workspace における人間の判断は、Workspace ロックによって直列化される

この設計により、複数プロジェクトや複数顧客を同時に扱っても、
判断責任と影響範囲が混線しない。

---

## 5. 前進と判断の分離

Cobito Crew のアーキテクチャにおける最重要点は、
**前進（Execution）と判断（Decision）を構造的に分離していること**である。

- 前進は AI（Crew）が担う
- 判断は人間が担う
- 判断は Advance 単位でのみ行われる

Execution Plane は、人間の入力を待たずに前進できる。  
Control Plane は、判断可能な状態になった時点でのみ、人間に接続する。

---

## 6. GCP 前提の考え方（高レベル）

Cobito Crew は、実行環境として GCP を前提に設計される。

ただし、ここで重要なのは特定のサービス名ではなく、  
次の性質が満たされていることである。

- 実行環境が短命・自律的に起動できること
- 永続データと一時環境が明確に分離されていること
- 権限と責任の境界が Workspace 単位で制御できること
- 非同期・イベント駆動で前進を進められること

これらを満たす限り、具体的な実装は将来変更されうる。

---

## 7. 外部エージェント・ツールとの関係

高度な Agent Teams や外部ツールは、
Execution Plane の一部として利用されうる。

それらは Cobito Crew の内部実装であり、
Mission / Advance / Workspace という核を置き換えるものではない。

Cobito Crew は、
「どのAIを使うか」ではなく
「どのように前進と判断を分離するか」を定義する。

---

## 8. 拡張と進化

Cobito Crew のアーキテクチャは、次の拡張を前提とする。

- Workspace の増加（複数プロジェクト・顧客）
- Mission の多様化（ソフトウェア開発以外）
- Execution Plane の高度化（新しいAIやツール）
- Review Interface の洗練（判断体験の改善）

これらの拡張は、CONCEPTS.md に定義された不変核を破壊しない限りにおいて許容される。

---

## 9. 本ドキュメントの位置づけ

ARCHITECTURE.md は、Cobito Crew の構造を理解するための地図である。

- 運用の正は OPERATIONS.md
- 概念の正は CONCEPTS.md
- 用語の正は GLOSSARY.md

実装が本ドキュメントと矛盾する場合、
設計の見直しが必要である。
