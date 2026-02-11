# Phase 0: Advanceテンプレを標準採用する

### 2) 対象 Mission
- Mission: Phase 0: Advanceテンプレを標準化する
- 背景: Phase 0では「端から端まで回る」ことが最優先であり、Advanceの品質を安定させるためにテンプレを固定したい。

### 3) 判断したいこと（Judgement Point）
- [docs/advances/templates/phase0.md](docs/advances/templates/phase0.md) を、Phase 0の標準Advanceテンプレとして採用してよいか？

### 4) 何が変わったか（Diff）
- 追加
  - Phase 0向けAdvanceテンプレ: [docs/advances/templates/phase0.md](docs/advances/templates/phase0.md)
  - Phase 0向け最小ガバナンス: [docs/governance/PHASE0.md](docs/governance/PHASE0.md)
  - Phase 0のDoD/最小成果物/イテレーション案: [ROADMAP.md](ROADMAP.md)
  - 本Advance（例）: [docs/advances/examples/phase0/001-adopt-advance-template.md](docs/advances/examples/phase0/001-adopt-advance-template.md)
- 影響を受ける範囲
  - Phase 0のAdvanceは、このテンプレの構造に従うことを前提にできる
- 影響を受けない範囲
  - Phase 1以降のテンプレやUI要件は、この判断では決めない

### 5) どう確かめるか（How to Verify）
以下の観点で「判断できるテンプレ」になっているか確認する。

1. 判断点が1つに絞れるか
2. 触って確かめる入口が書けるか
3. Rejectしても次が書けるか（理由/制約/方向性が残るか）

最小の動作確認（ローカル）

```sh
python -m venv .venv
source .venv/bin/activate
pip install -e .

# 初期化
.venv/bin/cobito-crew init

# Missionを作る（タイトル/本文は例）
.venv/bin/cobito-crew mission-create --workspace crew --title "Phase0: advance template" --body "Advanceテンプレを運用で固める"

# テンプレを本文としてAdvanceを作る（まずはreadyで提示できる形を想定）
BODY=$(.venv/bin/cobito-crew advance-template)
.venv/bin/cobito-crew advance-create --workspace crew --mission 1 --title "Adopt template" --body "$BODY" --status ready

# 判断開始（Workspace Lock取得）
.venv/bin/cobito-crew advance-review 1

# 判断（Approve/Rejectのどちらでもよい）
.venv/bin/cobito-crew advance-approve 1 --reason "テンプレだけで判断点・検証手順・引き継ぎが書ける"
```

期待結果
- テンプレをそのまま貼っても、Advance本文として読める
- `advance-review` で `in_review` に遷移できる（Lockが取れる）
- `advance-approve` または `advance-reject` でロックが解放され、状態が確定する

### 6) リスクとロールバック
- リスク
  - テンプレが冗長で、Phase 0の判断速度を落とす可能性
  - 「手順が書けないAdvance」が量産されると、テンプレが形骸化する可能性
- ロールバック/回避策
  - Rejectしてテンプレを短縮・再構成する（Mission Constraintとして「Phase 0のテンプレは最小である」を明文化）

### 7) スコープ外（Out of Scope）
- テンプレを満たす自動チェック（lint）
- 複数テンプレの運用
- Phase 1以降のIssue/PR取り込み

### 8) Reject の場合に次へ引き継ぐもの
- Reject理由の候補
  - 判断点が複数になりがちで、テンプレが判断単位を作れていない
  - 検証手順が書きづらく、「読むだけ」になりやすい
  - 情報量が多く、Phase 0の判断速度を落とす
- Mission Constraint の提案（例）
  - Phase 0のテンプレは「判断点1つ」「検証手順が必須」を満たす最小形に限定する
- 次の Advance の方向性
  - テンプレを短縮し、必須項目を3〜5個に絞った版を提示する
  - 「検証手順」の書き方を、CLI前提の最小例に固定する
