# 汎用プロンプトの使い方

このドキュメントでは、`prompts/` 直下にある汎用プロンプトの使い方を説明します。

汎用プロンプトは、直接書き換えて使う作業メモではありません。固定の作業ルールとして置き、チャットで「参照するプロンプトのパス」と「対象機能情報」を渡して使います。

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
作りたいもの: 2つの整数を足し算するシンプルな計算機
補足条件: なし
```

ポイントは、`prompts/create_function_design.md` の中身を書き換えないことです。必要な情報は、チャット側で渡します。

---

## 汎用プロンプト一覧

| プロンプト | 用途 | 主な出力先 |
|---|---|---|
| `prompts/create_overview.md` | コマンド/アプリ全体の overview を作成する | `docs/<command_or_app_name>/overview.md` |
| `prompts/create_feature_spec.md` | feature 仕様を作成する | `<対象機能フォルダ>/01_spec.md` |
| `prompts/create_function_design.md` | 関数設計を作成する | `<対象機能フォルダ>/02_design.md` |
| `prompts/create_function_call_flow.md` | 関数呼び出し定義を作成する | `<対象機能フォルダ>/03_flow.md` |
| `prompts/create_test_design.md` | feature 単体のテスト計画を作成する | `<対象機能フォルダ>/04_test_plan.md` |
| `prompts/create_review_checklist.md` | feature 単体レビュー観点を作成する | `<対象機能フォルダ>/05_review_checklist.md` |
| `prompts/create_integration_test_plan.md` | command/app 単位の結合試験計画を作成する | `docs/<command_or_app_name>/10_integration_test_plan.md` |
| `prompts/implement_feature.md` | feature 本体と feature 単体テストを作成する | 指定された feature 実装ファイル、feature 単体テストファイル |
| `prompts/implement_entrypoint.md` | `entrypoint.py` と entrypoint のテストを作成する | `src/<command_or_app_name>/entrypoint.py`、`tests/<command_or_app_name>/test_entrypoint_<short_name>.py` |
| `prompts/implement_integration_test.md` | 結合試験を実装する | `tests/<command_or_app_name>/test_integration_<short_name>.py` |
| `prompts/review_feature.md` | feature 単体レビューを行う | `<対象機能フォルダ>/06_review_result.md` |
| `prompts/review_command.md` | command/app 全体レビューを行う | `docs/<command_or_app_name>/11_command_review_result.md` |

---

## review_feature と review_command の役割分担

`prompts/review_feature.md` は feature 単体レビュー用です。主に feature 配下の `01_spec.md` から `05_review_checklist.md`、feature 実装、feature 単体テストを確認し、結果を `<対象機能フォルダ>/06_review_result.md` に記録します。

`prompts/review_command.md` は command/app 全体レビュー用です。`overview.md`、`entrypoint.py`、`test_entrypoint_<short_name>.py`、`10_integration_test_plan.md`、`test_integration_<short_name>.py`、feature 単体レビュー結果を確認し、結果を `docs/<command_or_app_name>/11_command_review_result.md` に記録します。

entrypoint と結合試験まで含めた最終確認は、`review_command.md` で扱います。`review_feature.md` で entrypoint や結合試験に触れる場合は、feature との責務分担に関係する範囲にとどめます。

---

## テスト計画と結合試験計画の役割分担

`04_test_plan.md` は feature 単体のテスト計画です。feature の詳細ロジック、正常系、異常系、境界値などを確認します。

`10_integration_test_plan.md` は command/app 単位の結合試験計画です。`entrypoint.py` と feature の接続、入出力、終了コード、エラー時の扱いを確認します。

---

## レビュー結果の役割分担

| ファイル | 役割 |
|---|---|
| `05_review_checklist.md` | feature 単体レビューで確認する観点を定義する |
| `06_review_result.md` | feature 単体レビューの結果、指摘事項、判定を記録する |
| `11_command_review_result.md` | command/app 全体レビューの結果、指摘事項、判定を記録する |

既存の `06_review_result.md` や `11_command_review_result.md` がある場合でも、古い判定をそのまま採用しません。現在のファイル群を読み直して再レビューし、レビュー結果ファイルを上書き更新します。

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

entrypoint テストと結合試験は、複数 command/app 間で同名ファイルが衝突しないように以下の標準命名にします。

```text
tests/<command_or_app_name>/test_entrypoint_<short_name>.py
tests/<command_or_app_name>/test_integration_<short_name>.py
```

`<short_name>` は、単一 feature の command/app では feature 名を使います。
複数 feature を束ねる command/app では、command/app を短く表す名前を使います。

---

## 変更してはいけないもの

汎用プロンプトを使う作業では、原則として以下を変更しません。

- `prompts/*.md`
- `AGENTS.md`
- `docs/templates/`
- 指定された出力先以外の feature ドキュメント
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

```text
prompts/review_command.md を参照してください。

コマンド/アプリ名: cli_simple_calculator
対象 overview: docs/cli_simple_calculator/overview.md
対象 entrypoint: src/cli_simple_calculator/entrypoint.py
entrypoint テスト: tests/cli_simple_calculator/test_entrypoint_calculator.py
結合試験計画: docs/cli_simple_calculator/10_integration_test_plan.md
結合試験ファイル: tests/cli_simple_calculator/test_integration_calculator.py
command/app 全体レビュー結果ファイル: docs/cli_simple_calculator/11_command_review_result.md
補足条件: レビューだけ行い、レビュー結果ファイル以外は変更しないでください。
```
