# 実装済み feature に追加修正するチュートリアル

このチュートリアルでは、実装済み feature `cli_text_counter` を題材に、変更要求を受けたときの安全な進め方を体験します。

---

## このチュートリアルの目的

既存コードをこっそり直接修正することではありません。

変更要求を受けたときに、**既存の docs / 実装 / テスト / tasks.md / レビュー結果を確認し、影響範囲を整理してから、AIに別作業として修正を依頼する流れ**を体験することです。

変更対象・変更理由・確認結果・未対応事項を作業報告として残すことで、AIと人間が同じ現在地を共有できます。

---

## 010 / 020 との違い

| | チュートリアル | 目的 | 開始状態 |
|---|---|---|---|
| [010](010_simple_calculator.md) | simple_calculator | 初期状態から単一 feature を設計・実装・テスト・レビューする | 仕様書と tasks.md のみ用意済み |
| [020](020_create_new_sample_from_scratch.md) | cli_text_tools（新規作成） | 新しい command/app と複数 feature の初期 docs 構造を作る | 完全にゼロから作る |
| **030（このチュートリアル）** | **cli_text_counter** | **実装済み feature に対して仕様変更・軽微な機能追加・バグ修正・レビュー指摘反映を行う** | **docs / src / tests がすべて揃った完成済みサンプル** |

---

## 題材

### command/app

`cli_text_counter`

入力文字列の文字数を数えて返すシンプルな CLI です。

実行例:

```bash
python src/cli_text_counter/entrypoint.py --text "hello"
```

出力例:

```text
5
```

### 対象 feature

`text_counter` — 入力文字列の文字数を整数として返す feature です。

| ファイル | 役割 |
|---|---|
| `docs/cli_text_counter/10_overview.md` | command/app 全体の目的・責務分担 |
| `docs/cli_text_counter/tasks.md` | command/app 全体の現在地メモ |
| `docs/cli_text_counter/features/text_counter/tasks.md` | feature の現在地メモ |
| `docs/cli_text_counter/features/text_counter/20_spec.md` | feature の仕様 |
| `docs/cli_text_counter/features/text_counter/21_design.md` | 関数設計 |
| `docs/cli_text_counter/features/text_counter/22_flow.md` | 関数呼び出し定義 |
| `docs/cli_text_counter/features/text_counter/23_test_plan.md` | 単体テスト計画 |
| `docs/cli_text_counter/features/text_counter/24_review_checklist.md` | レビュー観点 |
| `docs/cli_text_counter/features/text_counter/25_review_result.md` | feature 単体レビュー結果 |
| `src/cli_text_counter/features/text_counter.py` | feature 実装 |
| `tests/cli_text_counter/features/test_text_counter.py` | feature 単体テスト |
| `src/cli_text_counter/entrypoint.py` | CLI入口 |
| `tests/cli_text_counter/test_entrypoint_text_counter.py` | entrypoint テスト |
| `tests/cli_text_counter/test_integration_text_counter.py` | 結合試験 |

---

## 変更作業の基本方針

### こっそり修正しない

設計・仕様・実装・テスト・`tasks.md` に影響する修正は、人間が直接ファイルを編集するのではなく、AIに別作業として依頼することを基本とします。

AIに直させること自体が目的ではありません。変更対象、変更理由、確認結果、未対応事項を作業報告として残し、AIと人間が同じ現在地を共有するためです。

AIも人間も、調査中・レビュー中・説明中に、ついで修正やこっそり修正を行いません。

### 人間が反映対象を判断する

AIが出した修正候補や指摘をすべて反映するのではなく、人間が内容を確認したうえで反映する指摘と保留する指摘を判断します。

### AIに別作業として修正を依頼する

修正を依頼するときは、変更してよいファイルと変更してはいけないファイルを明示します。変更理由や確認結果も合わせて伝えると、AIが作業報告に残しやすくなります。

### 作業報告を残す

AIの作業後に、変更対象、変更理由、確認結果、未対応事項が作業報告に記録されていることを確認します。

### tasks.md は現在地メモとして必要最小限更新する

修正後に `tasks.md` を確認し、現在の状態と次にやることを短く更新します。仕様・設計・テスト計画・レビュー結果の詳細は `tasks.md` には書きません。

---

## 変更前に確認するファイル

変更要求を受けたとき、まず以下のファイルを確認します。

| ファイル | 確認のポイント |
|---|---|
| `10_overview.md` | 変更要求が command/app の責務範囲に収まるか |
| command/app `tasks.md` | command/app 全体の現在地・保留事項 |
| feature `tasks.md` | feature の現在地・次の作業 |
| `20_spec.md` | 現在の仕様・前提条件 |
| `21_design.md` | 変更対象の関数・責務 |
| `22_flow.md` | 呼び出し関係への影響 |
| `23_test_plan.md` | 既存のテスト観点との整合 |
| `24_review_checklist.md` | レビュー観点への影響 |
| `25_review_result.md` | 過去のレビュー指摘・改善候補 |
| feature 実装ファイル | 現在の実装内容 |
| feature 単体テストファイル | 現在のテスト内容 |
| `entrypoint.py` | 出力形式・引数への影響がないか |
| entrypoint テスト | entrypoint 側のテストへの影響 |
| 結合試験 | 結合試験への影響 |

---

## 変更パターン別の進め方

| 変更パターン | まず確認するもの | 更新候補 | 注意点 |
|---|---|---|---|
| **仕様変更** | `20_spec.md`、`10_overview.md` | `20_spec.md`、`21_design.md`、`22_flow.md`、`23_test_plan.md`、実装、テスト | 仕様変更は feature 全体に波及しやすい。ドキュメントから先に更新する |
| **軽微な機能追加** | `20_spec.md`、`21_design.md`、`23_test_plan.md` | `20_spec.md`、`21_design.md`、`23_test_plan.md`、実装、テスト | feature 責務の範囲内か確認する。範囲を超える場合は仕様変更として扱う |
| **判定条件の変更** | `20_spec.md`、`23_test_plan.md` | `20_spec.md`、`23_test_plan.md`、実装、テスト | 境界値が変わる場合はテスト計画を先に整理する |
| **出力項目の追加** | `20_spec.md`、`22_flow.md`、`entrypoint.py`、結合試験 | `20_spec.md`、`21_design.md`、`22_flow.md`、実装、テスト、entrypoint、entrypoint テスト、結合試験 | feature の戻り値変更は entrypoint と結合試験に影響する可能性が高い |
| **バグ修正** | `20_spec.md`、実装ファイル、テストファイル | 実装、テスト（再現テスト追加） | 先に再現テストまたはテスト観点を追加してから修正する |
| **レビュー指摘の反映** | `25_review_result.md`、`12_command_review_result.md` | 指摘内容による | 人間がどの指摘を反映するかを判断してからAIに依頼する |

---

## 例: 軽微な機能追加を行う

`cli_text_counter` を題材に、軽微な機能追加の例を示します。

### 変更要求

文字数カウントで、**空白を除外して数えるオプション**を追加したい。

### まず確認すること

1. `20_spec.md` を確認し、空白除外カウントが既存の責務内に収まるか判断する
2. `21_design.md` を確認し、既存の `count_characters` 関数に引数を追加するか、別関数にするかを考える
3. `23_test_plan.md` を確認し、空白除外に関するテスト観点を追加する必要があるか確認する
4. `entrypoint.py` を確認し、新しいCLI引数（例: `--exclude-spaces`）が必要になるか確認する
5. 結合試験への影響を確認する

### 進める順番の例

以下の順番で進めます。

```text
1. AIに影響範囲を整理させる（ファイルを変更しない）
2. 人間が影響範囲を確認し、修正対象を決める
3. 20_spec.md の更新をAIに依頼する
4. 21_design.md の更新をAIに依頼する
5. 23_test_plan.md の更新をAIに依頼する
6. feature 実装と feature 単体テストの更新をAIに依頼する（implement_feature.md を参照）
7. feature ソースレビューを行う（review_feature_source.md を参照）
8. entrypoint と entrypoint テストの更新をAIに依頼する（影響がある場合）
9. 結合試験の更新をAIに依頼する（影響がある場合）
10. python -m pytest を実行する
11. 必要に応じて review_feature.md / review_command.md で再レビューする
```

---

## 変更要求の影響範囲を整理するプロンプト例

変更作業の最初のステップです。AIに影響範囲を整理させます。**このステップではファイルを変更しません。**

チャット例:

```text
AGENTS.md を確認したうえで、実装済み feature に対する追加修正の影響範囲を整理してください。

対象:
- command/app: cli_text_counter
- feature: text_counter
- 変更要求: 文字数カウントで、空白を除外して数えるオプションを追加したい

確認対象:
- docs/cli_text_counter/10_overview.md
- docs/cli_text_counter/tasks.md
- docs/cli_text_counter/features/text_counter/tasks.md
- docs/cli_text_counter/features/text_counter/20_spec.md
- docs/cli_text_counter/features/text_counter/21_design.md
- docs/cli_text_counter/features/text_counter/22_flow.md
- docs/cli_text_counter/features/text_counter/23_test_plan.md
- docs/cli_text_counter/features/text_counter/24_review_checklist.md
- src/cli_text_counter/features/text_counter.py
- tests/cli_text_counter/features/test_text_counter.py
- src/cli_text_counter/entrypoint.py
- tests/cli_text_counter/test_entrypoint_text_counter.py
- tests/cli_text_counter/test_integration_text_counter.py

確認してほしいこと:
- 変更要求が既存 feature の責務内に収まるか
- 更新が必要になりそうな docs
- 更新が必要になりそうな src / tests
- entrypoint や結合試験に影響するか
- 先に仕様変更すべきか、実装変更に進めるか
- 人間が判断すべき点

このステップではファイルを変更しないでください。
```

AIから影響範囲の整理が報告されたら、人間が内容を確認して次のステップに進みます。

---

## 反映作業をAIに依頼するプロンプト例

影響範囲を人間が確認した後、具体的な修正をAIに依頼します。以下はチャット例です（このチュートリアルでは実際の修正は行いません）。

### 仕様・設計・テスト計画の更新を依頼する例

```text
AGENTS.md を確認したうえで、以下の変更を行ってください。

変更要求:
- text_counter feature に、空白を除外して文字数を数えるオプションを追加する
- 変更理由: 利用者から「空白なし文字数も知りたい」という要望があった

変更してよいファイル:
- docs/cli_text_counter/features/text_counter/20_spec.md
- docs/cli_text_counter/features/text_counter/21_design.md
- docs/cli_text_counter/features/text_counter/23_test_plan.md
- docs/cli_text_counter/tasks.md
- docs/cli_text_counter/features/text_counter/tasks.md

変更してはいけないファイル:
- src/cli_text_counter/features/text_counter.py（今回は docs のみ更新）
- tests/cli_text_counter/features/test_text_counter.py（今回は docs のみ更新）
- src/cli_text_counter/entrypoint.py
- tests/cli_text_counter/test_entrypoint_text_counter.py
- tests/cli_text_counter/test_integration_text_counter.py
- docs/templates/
- prompts/
- AGENTS.md
- README.md

補足条件: 仕様は 20_spec.md に先に反映してください。entrypoint への影響は後続の作業で扱います。
```

### feature 実装とテストの更新を依頼する例（docs 更新後）

```text
prompts/implement_feature.md を参照してください。

対象機能フォルダ: docs/cli_text_counter/features/text_counter/
コマンド/アプリ名: cli_text_counter
対象機能名: text_counter
実装ファイル: src/cli_text_counter/features/text_counter.py
テストファイル: tests/cli_text_counter/features/test_text_counter.py
作りたいもの: 空白を除外して文字数を数えるオプションを追加する
補足条件:
- 更新済みの 20_spec.md / 21_design.md / 23_test_plan.md に従って実装してください。
- 既存の count_characters 関数の動作は変えないでください。
- 変更対象と変更理由を作業報告に残してください。
```

### ソースレビューを依頼する例（feature 更新後）

```text
prompts/review_feature_source.md を参照してください。

対象機能フォルダ: docs/cli_text_counter/features/text_counter/
コマンド/アプリ名: cli_text_counter
対象機能名: text_counter
実装ファイル: src/cli_text_counter/features/text_counter.py
テストファイル: tests/cli_text_counter/features/test_text_counter.py
補足条件: ソースレビューだけ行い、実装ファイル・テストファイル・docs・tasks.md は変更しないでください。
```

---

## レビュー指摘を反映する場合

`25_review_result.md` または `12_command_review_result.md` に指摘がある場合は、以下の流れで進めます。

1. レビュー結果を人間が確認する
2. 反映する指摘と保留する指摘を人間が判断する
3. 反映する指摘を明示して、AIに別作業として修正を依頼する
4. AIが変更ファイル・変更理由・確認結果・未対応事項を作業報告として残す
5. `python -m pytest` を実行する
6. 必要に応じて `prompts/review_feature.md` または `prompts/review_command.md` で再レビューする

### レビュー指摘の反映を依頼するチャット例

```text
AGENTS.md を確認したうえで、以下のレビュー指摘を反映してください。

反映する指摘:
- docs/cli_text_counter/features/text_counter/25_review_result.md の「改善候補」に記載の内容

変更してよいファイル:
- 指摘内容に応じて判断（AIが提示する）

変更してはいけないファイル:
- docs/cli_text_counter/features/text_counter/25_review_result.md（このファイルは再レビュー時に上書きされる）
- prompts/
- AGENTS.md
- README.md
- docs/templates/

補足条件:
- 変更対象と変更理由を作業報告に残してください。
- 作業後に python -m pytest を実行してください。
```

---

## 作業後に確認すること

- 変更対象と変更理由が作業報告に残っているか
- `tasks.md` が現在地メモとして必要最小限更新されているか（詳細は書かれていないか）
- 仕様・設計・テスト計画・実装・テストのズレがないか
- ついで修正やこっそり修正がないか（変更してよいファイル以外が変更されていないか）
- `python -m pytest` が通っているか
- 必要なレビューを行ったか（`review_feature_source.md`、必要に応じて `review_feature.md` / `review_command.md`）

---

## 進めるときの注意

- 影響範囲の確認ステップではファイルを変更しません
- `prompts/*.md` は直接編集しません
- チャットでは、参照するプロンプトのパス、変更対象、変更理由、今回だけの補足条件を渡します
- feature の変更が entrypoint に影響する場合は、entrypoint の修正も別作業として依頼します
- 変更後は必ず `python -m pytest` を実行します
- `tasks.md` には仕様・設計・テスト計画・レビュー結果の詳細を書きません
- 変更要求が feature の責務を超える場合は、`10_overview.md` に戻って feature 分割から見直します
