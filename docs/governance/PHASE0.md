# PHASE0（Governance）

本ドキュメントは、Phase 0（`crew` Workspace）における
最小ガバナンス（責任境界、ロック、介入、失敗時の扱い）を定義する。

ここでの目的は「統制を強くする」ことではない。
判断と責任が混線せず、前進が止まらないための最小ルールを固定する。

---

## 対象範囲

- Workspace: `crew`
- 外部プロジェクト取り込み: しない（Phase 1以降）
- Issue Ingestion: しない（Phase 1以降）

---

## 責任境界（Workspace）

- Phase 0 では、責任境界は `crew` に閉じる
- `crew` 以外の資産・権限に影響する変更は、原則として扱わない

---

## Workspace Lock（判断の直列化）

### 目的
同一Workspaceで人間が同時に複数のAdvanceを判断すると、
責任の衝突・判断の混線が起きるため、判断は常に直列化する。

### ルール
- `in_review` は同一Workspaceで同時に1つのみ
- ロック取得は「人間がそのAdvanceを判断する」と決めた時点
- Approve / Reject によりロックは解放される
- ロック中も、AI（Crew）は次のAdvance準備（draft）を進めてよい

### 例外（Phase 0）
- 例外は原則作らない
- どうしても必要になった場合、Phase 0 の完了条件が満たされていないサインとして扱う

---

## 人間の介入（最小指針）

人間が見る対象は原則として Advance のみ。
介入は「Advanceを得るための必須条件」にしない。

介入が許容される目的は以下に限る。

1. Mission Rework（前提の再設計）
2. Mission Constraint（制約の明文化・確定）
3. Crew 自体の改善（ガードレール、手順、テンプレ）

---

## Mission Constraint の扱い

- AI（Crew）は Mission Constraint を提案してよい
- 確定（採用して前提化する）は必ず人間が行う
- 確定された Mission Constraint は以降のすべての前進を拘束する

---

## 失敗・中断・期限切れ

- Reject は失敗ではなく、学習として履歴に残す
- 中断は正常状態（優先順位変更・前提変更を含む）
- Expired は正常状態（必要なら再生成/再前進する）

---

## Phase 0 の観測（最低限）

Phase 0 は「回っているか」を判断できる必要がある。
最低限、以下が観測できる状態を目指す。

- 判断回数（Approve/Reject/Rework/Constraint）
- Reject理由の分布（Mission Alignment / Advance / Workspace）
- 1判断あたりの所要時間（目安でよい）
