# 汎用プロンプトの使い方

このドキュメントでは、`prompts/` 直下にある汎用プロンプトの使い方を説明します。

汎用プロンプトは、直接書き換えて使う作業メモではありません。
固定の作業ルールとして置き、チャットで「参照するプロンプトのパス」と「対象機能情報」を渡して使います。

---

## どこから始めるか

チュートリアルを進めたい場合は、まず `docs/tutorials/010_simple_calculator.md` を開いてください。

汎用プロンプトの使い方だけを確認したい場合は、このドキュメントを上から読んでください。

---

## 基本方針

- `prompts/*.md` は固定の作業ルールとして参照します
- 利用時に `prompts/*.md` を直接編集しません
- チュートリアルでも `prompts/` 直下の汎用プロンプトを使います
- チュートリアル専用プロンプト置き場は作成しません
- AIは、指定されたプロンプト、`AGENTS.md`、`docs/templates/` に従って作業します
- AIは、プロンプトに書かれた作業範囲を超えて実装、テスト作成、レビューへ勝手に進みません

---

## 使い方

チャットでは、次のように依頼します。

```text
prompts/create_function_design.md を参照してください。

対象機能フォルダ: docs/cli_simple_calculator/features/calculator/
コマンド/アプリ名: cli_simple_calculator
対象機能名: calculator
作りたいもの: 2つの数値を足し算するシンプルな計算機
補足条件: なし
```

ポイントは、`prompts/create_function_design.md` の中身を書き換えないことです。
必要な情報は、チャット側で渡します。

---

## 汎用プロンプト一覧

| プロンプト | 用途 | 主な出力先 |
|---|---|---|
| `prompts/create_overview.md` | コマンド/アプリ全体の overview を作成する | `docs/<command_or_app_name>/overview.md` |
| `prompts/create_feature_spec.md` | 機能仕様を作成する | `<対象機能フォルダ>/01_spec.md` |
| `prompts/create_function_design.md` | 関数設計を作成する | `<対象機能フォルダ>/02_design.md` |
| `prompts/create_function_call_flow.md` | 関数呼び出し定義を作成する | `<対象機能フォルダ>/03_flow.md` |
| `prompts/create_test_design.md` | テスト計画を作成する | `<対象機能フォルダ>/04_test_plan.md` |
| `prompts/create_review_checklist.md` | レビュー観点を作成する | `<対象機能フォルダ>/05_review_checklist.md` |
| `prompts/create_integration_test_plan.md` | 結合試験計画を作成する | `docs/<command_or_app_name>/10_integration_test_plan.md` |
| `prompts/implement_feature.md` | feature 本体と feature 単体テストを作成する | 指定した feature 実装ファイル、feature 単体テストファイル |
| `prompts/implement_entrypoint.md` | `entrypoint.py` と entrypoint のテストを作成する | `src/<command_or_app_name>/entrypoint.py`、`tests/<command_or_app_name>/test_entrypoint.py` |
| `prompts/implement_integration_test.md` | 結合試験を実装する | `tests/<command_or_app_name>/test_integration.py` |
| `prompts/review_feature.md` | 実装後の機能レビューを行う | `<対象機能フォルダ>/06_review_result.md` |

---

## overview と feature 分割

`overview.md` は、feature 作成前に確認する command/app 全体の設計入口です。
コマンド/アプリの目的、Boundary、entrypoint、feature 分割方針、機能一覧を整理してから、個別 feature のドキュメントを作成します。

---

## 対象情報として渡すもの

- 参照するプロンプトのパス
- 対象 overview
- 対象 entrypoint
- entrypoint テストファイル
- 対象機能フォルダ
- コマンド/アプリ名
- 対象機能名
- 作りたいもの
- 実行イメージまたは利用イメージ
- 今回やらないこと
- 実装ファイル
- テストファイル
- レビュー結果ファイル
- 結合試験計画ファイル
- 補足条件

実装ファイルとテストファイルは、原則として以下の形にします。

```text
src/<command_or_app_name>/features/<feature_name>.py
tests/<command_or_app_name>/features/test_<feature_name>.py
```

---

## 結合試験の扱い

結合試験は常に必須ではありません。
`entrypoint.py` から feature を束ねて確認する必要がある場合に、`docs/<command_or_app_name>/10_integration_test_plan.md` を作成し、必要に応じて `tests/<command_or_app_name>/test_integration.py` を実装します。

---

## feature 実装と entrypoint 実装の分担

`prompts/implement_feature.md` は、feature 本体と feature 単体テストを作成するために使います。
`prompts/implement_entrypoint.md` は、`entrypoint.py` と `test_entrypoint.py` を作成するために使います。

`entrypoint.py` には feature 固有ロジックを入れず、CLI引数を受け取り、feature を呼び出し、結果を出力し、終了コードを返す役割に絞ります。

---

## レビュー観点とレビュー結果の分離

`05_review_checklist.md` と `06_review_result.md` は役割が違います。

| ファイル | 役割 |
|---|---|
| `05_review_checklist.md` | レビューで確認する観点を定義する |
| `06_review_result.md` | 実際にレビューした結果、指摘事項、判定を記録する |

`05_review_checklist.md` には、レビュー結果や指摘事項を書き込みません。
`prompts/review_feature.md` を使う場合、レビュー結果は `<対象機能フォルダ>/06_review_result.md` に出力します。

---

## 変更してはいけないもの

汎用プロンプトを使う作業では、原則として以下を変更しません。

- `prompts/*.md`
- `AGENTS.md`
- `docs/templates/`
- 指定された出力先以外の機能ドキュメント
- 指定された実装ファイル以外の実装コード
- 指定されたテストファイル以外のテストコード
- `src/common/`
- CI/CD、デプロイ関連のファイル

必要だと感じた場合も、勝手に変更せず、今後の改善候補として記録します。

---

## 依頼例

```text
prompts/review_feature.md を参照してください。

対象機能フォルダ: docs/cli_simple_calculator/features/calculator/
コマンド/アプリ名: cli_simple_calculator
対象機能名: calculator
実装ファイル: src/cli_simple_calculator/features/calculator.py
テストファイル: tests/cli_simple_calculator/features/test_calculator.py
レビュー結果ファイル: docs/cli_simple_calculator/features/calculator/06_review_result.md
補足条件: レビューだけ行い、実装ファイルとテストファイルは変更しないでください。
```
