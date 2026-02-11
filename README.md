# Cobito Crew

**Advance your Mission.**

Cobito Crew は、人間の判断を中心に据え、  
**Mission を前進させるための判断可能な状態差分（Advance）を自律的に生成するクルー**です。

AIに判断を委ねるのではなく、  
人間が「ここで決める」べき一点だけに集中できる構造を提供します。

## はじめに読むもの
- CONCEPTS.md
- GLOSSARY.md
- AGENTS.md
- MISSION.md
- DECISIONS.md

## Phase 0（ローカル実行・最小CLI）

このリポジトリは Phase 0 として、まず `crew` Workspace をローカルで回すための最小CLIを提供する。

### セットアップ

```sh
python -m venv .venv
source .venv/bin/activate
pip install -e .
```

### 最小ループ（例）

```sh
cobito-crew init

cobito-crew mission-create --workspace crew --title "Phase0: advance template" --body "Advanceテンプレを運用で固める"
cobito-crew mission-list --workspace crew

# mission id を仮に 1 とする
cobito-crew advance-create --workspace crew --mission 1 --title "Draft advance" --body "$(cobito-crew advance-template)" --status ready
cobito-crew advance-list --workspace crew

# Missionに紐づく最新Advance IDを取る（例）
cobito-crew advance-latest 1 --id-only

# advance id を仮に 1 とする
cobito-crew advance-review 1
cobito-crew advance-approve 1 --reason "テンプレで判断できる"
```

ローカル状態（SQLite）は `.cobito_crew/state.db` に保存される。
