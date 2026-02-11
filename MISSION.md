# MISSION

## Mission の設計と扱い（Cobito Crew）

本ドキュメントは、Cobito Crew における  
**Mission がどのようなものであるべきか、  
どのように扱われ、どのように進化するか**を定義する。

Mission は Cobito Crew の出発点であり、  
同時に「判断を学習する組織」の最上流に位置する。

---

## Mission 定義の扱い

Mission の定義（語義）は GLOSSARY.md を正とする。  
本ドキュメントは、Mission を **どう設計し、どう進化させるか**にのみ焦点を当てる。  
以降は「良い Mission にするための設計指針」と「運用中の進化」を扱う。

---

## Mission の抽象度について

Mission の抽象度に上限はない。

以下のような抽象的な願望も、Mission として許容される。

- 「一兆円規模の価値を創出したい」
- 「長期的に意味のある事業を作りたい」
- 「持続可能な組織を構築したい」

重要なのは、  
Mission が **判断可能な Advance に変換できるかどうか**である。

Cobito Crew は、  
Mission をそのまま実行するのではなく、  
判断可能な単位へと変換し続ける。

---

## Mission が満たすべき最小条件

Mission は、次の条件を満たしていればよい。

- 人間の意図が含まれている
- 「前進したかどうか」を問える
- 判断を必要としている

以下は必須ではない。

- 成功条件の完全な定義
- 制約の網羅
- 実行計画の明示

Mission は **不完全であってよい**。  
不完全さは、Advance を通じて補完される。

---

## Mission が不適切な場合（Mission Rework）

次のような場合、Mission は判断可能な形になっていない。

- 抽象的すぎて判断点が存在しない
- 目的が矛盾している
- 何を前進とみなすかが不明確
- 願望はあるが、判断を伴わない

この場合、Cobito Crew は Advance を生成しない。  
代わりに **Mission Rework** を要求する。

Mission Rework は Reject ではなく、  
**判断以前の前提整理**である。

---

## Mission と Advance の関係

Mission は固定される。  
Advance は変化し続ける。

- Mission は意図の軸であり、継続する
- Advance は仮説的な前進であり、更新される

原則として、  
**1 Mission に対して 1 Advance** が提示される。

Advance が Reject された場合でも、  
Mission は維持され、次の Advance が生成される。

---

## Mission Constraint（Mission の進化）

Advance を確認する過程で、  
Mission に書かれていなかった前提や制約が  
新たに発見されることがある。

この場合、Mission は否定されない。  
代わりに **Mission Constraint** が追加される。

Mission Constraint は、

- Mission の解釈空間を狭め
- 次の Advance の前提条件となり
- 判断の学習結果として蓄積される

Mission は、Mission Constraint の追加によって  
**より人間の判断軸に適合した形へと進化する**。

---

## Mission の自動生成と外部入力

Mission は、人間が直接提示するだけでなく、  
外部システムを入力として生成されることがある。

例：
- Issue 管理システム
- 要望一覧
- 課題ログ

この場合でも、Cobito Crew 内部では  
Mission を正として扱い、  
外部の管理単位は補助情報とする。

---

## Mission は評価されない

Cobito Crew において、評価の対象は Advance である。  
Mission 自体は、Approve / Reject の対象ではない。

Mission は、

- 修正される（Rework）
- 制約が追加される（Mission Constraint）
- 継続される

が、  
**採否を問われることはない**。

---

## 本ドキュメントの位置づけ

MISSION.md は、  
Cobito Crew における **「意図の設計書」**である。

- 概念の正は CONCEPTS.md
- 判断の正は DECISIONS.md
- 運用の正は OPERATIONS.md

Mission の扱いに迷った場合、  
必ず本ドキュメントに立ち戻ること。
