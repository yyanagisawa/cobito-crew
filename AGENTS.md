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
  Mission / Advance / Workspace の存在理由と不変核を定義する。

### 用語の定義（語義の凍結）
- **GLOSSARY.md**  
  Cobito Crew における主要な用語の定義集。  
  用語の正は本ドキュメントのみである。

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

### Mission の設計と扱いを理解したい場合
- **MISSION.md**
  - Mission の設計指針（どう書き、どう進化させるか）
  - Mission Rework / Mission Constraint の扱い

---

## 運用や振る舞いを理解したい場合

### Mission と Advance の運用モデル
- **OPERATIONS.md**
  - Mission → Advance のライフサイクルと手順
  - 1 Mission : 1 Advance 原則と例外運用
  - Workspace ロックと人間介入の最小指針

### 判断の構造と学習
- **DECISIONS.md**
  - 判断の構造（Advance のみを対象とする評価軸）
  - Mission Rework / Mission Constraint の位置づけ
  - 判断履歴の継承と学習

### Advance の粒度と判断基準
- **docs/advances/**
  - Phase 0（単独運用）のテンプレ：docs/advances/templates/phase0.md

---

## 技術構成を理解したい場合

### 高レベルアーキテクチャ
- **ARCHITECTURE.md**
  - Cobito Crew の全体構成と責務分離
  - 外部入力（Issue / PR）の正規化
  - 永続データと一時環境の扱い

### セキュリティとガバナンス
- **docs/governance/**
  - Phase 0（単独運用）の最小ガバナンス：docs/governance/PHASE0.md

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

---

## ドキュメント編集・削除の判断基準（索引の保守ルール）

Cobito Crew のドキュメントを編集・簡潔化する際は、
内容の正しさや重要性ではなく、
**その文章が属する責務**を基準に判断する。

以下の問いに YES と答えられない文章は、
原則として削除または別文書へ移動する。

- この文章は、このドキュメントの「唯一の責務」に属しているか？
- 同じ内容が、他のドキュメントの責務としてより適切に置けないか？
- 概念の定義、運用手順、判断ロジックが混在していないか？

判断に迷った場合は、
文章を削るか、参照に置き換えることを優先する。

思想や背景説明は CONCEPTS.md に集約し、
定義は GLOSSARY.md、
判断構造は DECISIONS.md、
運用手順は OPERATIONS.md に寄せる。

AGENTS.md は、
これらの責務を横断する説明を持たない。
