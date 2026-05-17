# simple-calculator チュートリアル

このチュートリアルでは、`cli_simple_calculator` の `calculator` 機能を題材に、AI駆動開発の流れを小さく体験します。

チュートリアル専用プロンプトは使いません。
`prompts/` 直下の汎用プロンプトを参照し、チャットで「参照するプロンプトのパス」と「対象機能情報」を渡して進めます。

---

## 前提

最初の状態では、以下の仕様書と現在地メモが用意されています。

```text
docs/cli_simple_calculator/overview.md
docs/cli_simple_calculator/tasks.md
docs/cli_simple_calculator/features/calculator/01_spec.md
docs/cli_simple_calculator/features/calculator/tasks.md
```

このチュートリアルで作成する主なファイルは以下です。

- `docs/cli_simple_calculator/features/calculator/02_design.md`
- `docs/cli_simple_calculator/features/calculator/03_flow.md`
- `docs/cli_simple_calculator/features/calculator/04_test_plan.md`
- `docs/cli_simple_calculator/features/calculator/05_review_checklist.md`
- `docs/cli_simple_calculator/features/calculator/06_review_result.md`
- `docs/cli_simple_calculator/10_integration_test_plan.md`
- `docs/cli_simple_calculator/11_command_review_result.md`
- `src/cli_simple_calculator/entrypoint.py`
- `src/cli_simple_calculator/features/calculator.py`
- `tests/cli_simple_calculator/test_entrypoint_calculator.py`
- `tests/cli_simple_calculator/test_integration_calculator.py`
- `tests/cli_simple_calculator/features/test_calculator.py`

`prompts/*.md` は直接編集しません。
必要な情報は、各ステップのチャット例としてAIに渡します。

---

## tasks.md の使い方

チュートリアル開始時は、`docs/cli_simple_calculator/tasks.md` を確認して、command/app 全体の現在地を把握します。
feature 作業に入る前は、`docs/cli_simple_calculator/features/calculator/tasks.md` を確認して、個別機能の現在地を把握します。

作業後は、必要に応じて `tasks.md` の「現在の状態」や「次に確認すること」だけを短く更新します。
仕様、設計、レビュー結果の詳細は `tasks.md` には書かず、それぞれの専用ファイルに記録します。

---

## 1. サンプル機能を確認する

まず、完成済みサンプル `cli_hello_greeting` を読み、仕様、設計、実装、テストの対応関係を確認します。

チャット例:

```text
AGENTS.md を確認したうえで、完成済みサンプルを読んでください。

確認対象:
- docs/cli_hello_greeting/overview.md
- docs/cli_hello_greeting/features/greeting/
- src/cli_hello_greeting/
- tests/cli_hello_greeting/

確認してほしいこと:
- 01_spec.md の仕様が実装にどう反映されているか
- 02_design.md の関数設計が実装にどう反映されているか
- 03_flow.md の呼び出し定義が実装にどう反映されているか
- 04_test_plan.md の観点がテストにどう反映されているか
- entrypoint.py と features/greeting.py の責務がどう分かれているか

このステップではファイルを変更しないでください。
```

---

## 2. 関数設計を作成する

`prompts/create_function_design.md` を参照して、関数設計を作成します。
作業前に `docs/cli_simple_calculator/features/calculator/tasks.md` を確認し、feature の現在地を把握します。

チャット例:

```text
prompts/create_function_design.md を参照してください。

対象機能フォルダ: docs/cli_simple_calculator/features/calculator/
コマンド/アプリ名: cli_simple_calculator
対象機能名: calculator
作りたいもの: 2つの整数を足し算するシンプルな計算機
補足条件: entrypoint.py は薄くし、機能ロジックは features/calculator.py に置いてください。
```

作成または更新されるファイル:

```text
docs/cli_simple_calculator/features/calculator/02_design.md
```

---

## 3. 関数呼び出し定義を作成する

`prompts/create_function_call_flow.md` を参照して、関数同士の呼び出し順と責務分担を整理します。

チャット例:

```text
prompts/create_function_call_flow.md を参照してください。

対象機能フォルダ: docs/cli_simple_calculator/features/calculator/
コマンド/アプリ名: cli_simple_calculator
対象機能名: calculator
作りたいもの: 2つの整数を足し算するシンプルな計算機
補足条件: entrypoint.py から features/calculator.py を呼び出す流れにしてください。
```

作成または更新されるファイル:

```text
docs/cli_simple_calculator/features/calculator/03_flow.md
```

---

## 4. テスト計画を作成する

`prompts/create_test_design.md` を参照して、単体テストの観点を整理します。

チャット例:

```text
prompts/create_test_design.md を参照してください。

対象機能フォルダ: docs/cli_simple_calculator/features/calculator/
コマンド/アプリ名: cli_simple_calculator
対象機能名: calculator
作りたいもの: 2つの整数を足し算するシンプルな計算機
補足条件: tests/cli_simple_calculator/ 配下に置く前提で整理してください。
```

作成または更新されるファイル:

```text
docs/cli_simple_calculator/features/calculator/04_test_plan.md
```

---

## 5. レビュー観点を作成する

`prompts/create_review_checklist.md` を参照して、レビューで確認する観点を作成します。

`05_review_checklist.md` はレビュー観点の定義です。
レビュー結果や指摘事項は書き込みません。

チャット例:

```text
prompts/create_review_checklist.md を参照してください。

対象機能フォルダ: docs/cli_simple_calculator/features/calculator/
コマンド/アプリ名: cli_simple_calculator
対象機能名: calculator
作りたいもの: 2つの整数を足し算するシンプルな計算機
補足条件: common は保護対象として扱い、共通化候補は提案にとどめてください。
```

作成または更新されるファイル:

```text
docs/cli_simple_calculator/features/calculator/05_review_checklist.md
```

---

## 6. feature 実装と feature 単体テストを作成する

`prompts/implement_feature.md` を参照して、feature 本体と feature 単体テストを作成します。

チャット例:

```text
prompts/implement_feature.md を参照してください。

対象機能フォルダ: docs/cli_simple_calculator/features/calculator/
コマンド/アプリ名: cli_simple_calculator
対象機能名: calculator
実装ファイル: src/cli_simple_calculator/features/calculator.py
テストファイル: tests/cli_simple_calculator/features/test_calculator.py
作りたいもの: 2つの整数を足し算するシンプルな計算機
補足条件: Python標準ライブラリのみを使ってください。entrypoint.py と test_entrypoint_calculator.py は作成しないでください。
```

作成または更新されるファイル:

```text
src/cli_simple_calculator/features/calculator.py
tests/cli_simple_calculator/features/test_calculator.py
```

---

## 7. entrypoint.py と entrypoint テストを作成する

`prompts/implement_entrypoint.md` を参照して、CLI入口と entrypoint のテストを作成します。

チャット例:

```text
prompts/implement_entrypoint.md を参照してください。

コマンド/アプリ名: cli_simple_calculator
対象 overview: docs/cli_simple_calculator/overview.md
対象 entrypoint: src/cli_simple_calculator/entrypoint.py
作成または更新するテストファイル: tests/cli_simple_calculator/test_entrypoint_calculator.py
対象 feature: calculator
short_name: calculator
補足条件: entrypoint.py は薄くし、features/calculator.py の機能を呼び出すだけにしてください。
```

作成または更新されるファイル:

```text
src/cli_simple_calculator/entrypoint.py
tests/cli_simple_calculator/test_entrypoint_calculator.py
```

---

## 8. 結合試験計画を作成する

`prompts/create_integration_test_plan.md` を参照して、command/app 単位の結合試験計画を作成します。

feature 単体の詳細ロジックは feature 単体テストに任せ、結合試験計画では entrypoint と feature の接続、入出力、終了コード、エラー時の扱いを整理します。

チャット例:

```text
prompts/create_integration_test_plan.md を参照してください。

コマンド/アプリ名: cli_simple_calculator
対象 overview: docs/cli_simple_calculator/overview.md
作成または更新する結合試験計画: docs/cli_simple_calculator/10_integration_test_plan.md
対象 entrypoint: src/cli_simple_calculator/entrypoint.py
対象 feature: calculator
補足条件:
- entrypoint.py から calculator feature を呼び出し、command/app として期待どおり動くことを確認する計画にしてください。
- feature 単体の詳細ロジックは feature 単体テストに任せてください。
- まだテストコードは作成しないでください。
```

作成または更新されるファイル:

```text
docs/cli_simple_calculator/10_integration_test_plan.md
```

---

## 9. 結合試験を実装する

`prompts/implement_integration_test.md` を参照して、結合試験を実装します。

結合試験は `10_integration_test_plan.md` に従い、subprocess による `entrypoint.py` の実行確認を中心にします。

チャット例:

```text
prompts/implement_integration_test.md を参照してください。

コマンド/アプリ名: cli_simple_calculator
対象 overview: docs/cli_simple_calculator/overview.md
対象 結合試験計画: docs/cli_simple_calculator/10_integration_test_plan.md
対象 entrypoint: src/cli_simple_calculator/entrypoint.py
作成または更新するテストファイル: tests/cli_simple_calculator/test_integration_calculator.py
対象 feature: calculator
short_name: calculator
補足条件:
- 結合試験は 10_integration_test_plan.md に従い、subprocess による entrypoint.py の実行確認を中心にしてください。
- feature 単体の詳細ロジックは再検証しないでください。
- 指定した出力先パスを変更しないでください。
- pytest の import mismatch やファイル名衝突が発生した場合は、勝手に別名ファイルを作成せず、確認事項として報告してください。
- src、docs、prompts、src/common は変更しないでください。
```

作成または更新されるファイル:

```text
tests/cli_simple_calculator/test_integration_calculator.py
```

---

## 10. テストを実行する

実装後、feature 単体テスト、entrypoint テスト、結合試験をまとめて実行します。

```bash
python -m pytest
```

環境によって `python` が使えない場合は、利用しているPythonの実行コマンドに読み替えてください。

---

## 11. feature 単体レビューを行う

`prompts/review_feature.md` を参照して、feature 単体レビューを行います。

レビュー結果は `05_review_checklist.md` ではなく、`06_review_result.md` に記録します。
既存の `06_review_result.md` がある場合でも、古い判定をそのまま採用せず、現在のファイル群を読み直して上書き再作成します。

`entrypoint.py` や結合試験は、feature との責務分担に関係する範囲でだけ確認します。command/app 全体の最終確認は次の `review_command.md` で扱います。

チャット例:

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

---

## 12. command/app 全体レビューを行う

`prompts/review_command.md` を参照して、command/app 全体レビューを行います。

レビュー結果は `docs/cli_simple_calculator/11_command_review_result.md` に記録します。
既存の `11_command_review_result.md` がある場合でも、古い判定をそのまま採用せず、現在の overview、entrypoint、結合試験計画、結合試験、feature 単体レビュー結果を読み直して上書き再作成します。

チャット例:

```text
prompts/review_command.md を参照してください。

コマンド/アプリ名: cli_simple_calculator
対象 overview: docs/cli_simple_calculator/overview.md
対象 entrypoint: src/cli_simple_calculator/entrypoint.py
entrypoint テスト: tests/cli_simple_calculator/test_entrypoint_calculator.py
結合試験計画: docs/cli_simple_calculator/10_integration_test_plan.md
結合試験ファイル: tests/cli_simple_calculator/test_integration_calculator.py
command/app 全体レビュー結果ファイル: docs/cli_simple_calculator/11_command_review_result.md
short_name: calculator
補足条件: レビューだけ行い、レビュー結果ファイル以外は変更しないでください。
```

---

## 進めるときの注意

- `prompts/*.md` は直接編集しません
- チャットで、参照するプロンプトのパスと対象機能情報を渡します
- 仕様にない便利機能は追加しません
- `entrypoint.py` は薄く保ちます
- feature 実装と entrypoint 実装は別のプロンプトで扱います
- feature 単体レビューと command/app 全体レビューは別のプロンプトで扱います
- 共通化候補があっても、勝手に `src/common/` へ切り出しません
- 結合試験は計画があり必要な場合だけ扱います
- 外部API、CI/CD、デプロイ資産は追加しません
