# ROADMAP

## Cobito Crew の進化計画（最終版）

本ドキュメントは、Cobito Crew が  
**どの順序で、どの能力を獲得し、どこまでスケールするか**を示す。

ここに書かれているのは約束ではない。  
**設計思想と現実制約を踏まえた、優先順位の宣言**である。

---

## 基本方針

Cobito Crew の進化は、次の原則に従う。

- 判断（Approve / Reject）を曖昧にしない
- Mission / Advance / Workspace の核を壊さない
- 人間待ちを前進の条件にしない
- 既存の開発文化（Issue駆動）を否定しない
- スケールより先に「適応」を完成させる

ロードマップは  
「できること」を増やすためではなく、  
**「いまはやらないこと」を明確にするために存在する**。

---

## Phase 0：Crew for itself（単独運用）

### Workspace
- `crew`

### 目的
Cobito Crew 自身を、Cobito Crew の思想どおりに開発できる状態にする。

### 状態
- Mission / Advance / Workspace が確立
- 判断の三層モデルが運用可能
- Mission Rework / Mission Constraint が機能している
- 判断履歴が学習として蓄積される

### やること
- Cobito Crew 自身の開発を Mission / Advance で回す
- Reject / Mission Constraint / Rework の実運用検証
- 人間判断の負荷と質の観測

### やらないこと
- 外部プロジェクトの取り込み
- Issue Ingestion
- 自動化の最適化

---

## Phase 1：Multi Workspace（Crew + Cobito）

### Workspace
- `crew`
- `cobito`

### 前提条件
- Cobito プロジェクトは Issue 駆動である
- Issue を経由せずに Cobito 開発を行うことは現実的でない

### 目的
Cobito Crew を、**既存の Issue 駆動プロジェクトに適用できること**を実証する。

### 状態
- 複数 Workspace が同時に存在
- Workspace ロックにより判断が混線しない
- Cobito Workspace では Issue → Mission → Advance が回る
- 人間は Advance だけを見る

### やること
- 最低限の Issue Ingestion を実装
- 外部入力の正規化レイヤーを整備（Issue / PR → Mission / Advance）
- Issue を Mission に変換し、Advance を生成
- Issue 状態と判断結果の同期

### やらないこと
- Issue 文化の矯正
- 高度な自動分類や優先度推定
- 他プロジェクトへの展開

---

## Phase 2：Issue Ingestion の高度化（適応フェーズ）

### 対象 Workspace
- `cobito`（および準外部プロジェクト）

### 目的
Issue 駆動という既存文化に対して、  
Cobito Crew が **賢く・自然に適応できる能力**を獲得する。

### 状態
- Issue → Mission 変換精度が向上
- Mission Rework / Mission Constraint が自動提案される
- Issue 間の分割・統合が提案される
- 判断履歴が Ingestion に反映される

### やること
- Issue 書式・粒度・文化の揺らぎ吸収
- Mission Rework が必要な Issue の事前検出
- Mission Constraint の自動抽出・提案
- 入力正規化の精度を継続改善

### やらないこと
- Issue テンプレの強制
- 人間の判断の自動化
- 他プロジェクトの大量導入

---

## Phase 3：Multi Workspace（拡張）

### Workspace
- `crew`
- `cobito`
- その他外部プロジェクト

### 前提条件
- Phase 2 が完了していること
- Issue Ingestion が文化差を吸収できていること

### 目的
複数の異なる Issue 文化・プロジェクトを同時に扱っても、  
判断品質を落とさずに運用できることを実証する。

### 状態
- Workspace ごとの判断キューが安定
- Reject / Mission Constraint の学習が横断的に活きる
- 人間の判断負荷が線形に増えない

### やること
- 外部プロジェクトの追加
- Workspace 境界の実証
- 判断優先度制御の洗練

### やらないこと
- 一般公開
- 課金・契約設計
- 高機能UI

---

## Phase 4：外部利用（限定）

### 目的
Cobito Crew を、他者が安全に使える形にする。

### 状態
- Workspace 分離が安全に機能
- 判断と責任の境界が明確
- 誤用しても破綻しない

### やること
- ガバナンス文書の拡充
- 権限・責任モデルの整理
- 失敗時の回復導線整備

### やらないこと
- 判断の自動化
- 人間責任の希薄化

---

## Phase 5：判断OSとしての確立（長期）

### 目的
Cobito Crew を、  
**ソフトウェア開発を超えた「判断と学習のOS」**として確立する。

### 状態
- 非開発 Mission が自然に流入
- 判断履歴が資産として蓄積
- 人間の判断軸が可視化される

### やること
- 判断パターンの分析
- Mission Constraint 進化の可視化
- 運用思想の再言語化

### やらないこと
- 判断の肩代わり
- ブラックボックス化

---

## ロードマップの扱い

本ロードマップは固定ではない。  
ただし **Phase の順序は原則として変更しない**。

Phase を進める条件は、
機能の完成ではなく、  
**判断と運用が破綻なく回っているか**である。

---

## 本ドキュメントの位置づけ

ROADMAP.md は、Cobito Crew における  
**進化の指針**である。

- 概念の正は CONCEPTS.md
- 判断の正は DECISIONS.md
- 運用の正は OPERATIONS.md

スコープや優先順位に迷った場合、  
必ず本ドキュメントに立ち戻ること。
