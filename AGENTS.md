# AGENTS

## Cobito Crew ドキュメント索引

本ドキュメントは、Cobito Crew における **すべてのドキュメントの入口**である。  
人間およびAI（Crew）は、設計・実装・運用・議論を行う前に、必ず本ドキュメントから参照を開始する。

AGENTS.md 自体は説明を行わない。  
**どこに何が書いてあるかを示す索引のみを提供する。**

---

## まず最初に読むもの（必須）

### 概念と不変核（憲法）
- **CONCEPTS.md**  
  Cobito Crew が何であり、何でないか。  
  Mission / Advance / Workspace を中核とする不変の原則を定義する。

### 用語の定義（語義の凍結）
- **GLOSSARY.md**  
  Cobito Crew における主要な用語の定義集。  
  本ドキュメントに定義された語義が唯一の正である。

---

## Cobito Crew の基本構造を理解したい場合

### 全体像と役割分担
- **CONCEPTS.md**
  - 人間とAI（Crew）の役割分担
  - 判断を外注しないという原則
  - Advance の定義
  - なぜ Agent Teams では足りないのか

### 用語の意味を確認したい場合
- **GLOSSARY.md**
  - Mission / Advance / Workspace
  - 人間 / AI（Crew）
  - 判断 / 前進 / 介入
  - Approve / Reject / Workspace Lock

---

## 運用や振る舞いを理解したい場合

### Mission と Advance の運用モデル
- **OPERATIONS.md**（作成予定）
  - Mission → Advance のライフサイクル
  - 人間の操作（Inbox / Pick / Approve / Reject）
  - 1 Mission : 1 Advance 原則と例外
  - Workspace ロックの扱い

### Advance の粒度と判断基準
- **docs/advances/**（作成予定）
  - 良い Advance / 悪い Advance の例
  - 「人間が判断できる状態差分」とは何か
  - 分割が許容されるケース

---

## 技術構成を理解したい場合

### 高レベルアーキテクチャ
- **ARCHITECTURE.md**（作成予定）
  - Cobito Crew の全体構成
  - GCP 上での責務分離
  - 永続データと一時環境の扱い

### セキュリティとガバナンス
- **docs/governance/**（作成予定）
  - Workspace 分離の原則
  - 権限・責任の境界
  - 失敗時・Reject 時の扱い

---

## 外部プロジェクトへの適用を理解したい場合

### 既存 Issue 運用との関係
- **OPERATIONS.md**
  - Issue と Mission の関係
  - Issue を入力として Mission を生成する考え方

### 外部カスタマー利用
- **ARCHITECTURE.md**
  - Workspace を顧客境界として扱う理由
  - Mission / Advance の可視化単位

---

## 実装・開発に関わる場合

### 開発の前提
- Cobito Crew の実装は、CONCEPTS.md の原則に従うこと
- 用語は GLOSSARY.md の定義を変更しないこと

### 変更時の注意
- CONCEPTS.md を変更する場合、  
  それは Cobito Crew の核を変更する行為である
- 用語の意味を変更する場合、  
  GLOSSARY.md と CONCEPTS.md の整合を必ず取ること

---

## 本ドキュメントの位置づけ

AGENTS.md は、Cobito Crew における **唯一の索引**である。

- 説明を追加しない
- 設計判断を書かない
- 原則や語義を重複して書かない

索引が肥大化した場合は、  
リンク先のドキュメントを整理し、AGENTS.md は常に薄く保つ。