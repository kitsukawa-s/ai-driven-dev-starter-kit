# simple-calculator チュートリアル

このチュートリアルでは、`cli_simple_calculator` の `calculator` 機能を題材に、AI駆動開発の流れを小さく体験します。

チュートリアル専用プロンプトは使いません。
`prompts/` 直下の汎用プロンプトを参照し、チャットで「参照するプロンプトのパス」と「対象機能情報」を渡して進めます。

---

## 前提

最初の状態では、以下の仕様書だけが用意されています。

```text
docs/cli_simple_calculator/features/calculator/01_spec.md
```

このチュートリアルで作成する主なファイルは以下です。

- `docs/cli_simple_calculator/features/calculator/02_design.md`
- `docs/cli_simple_calculator/features/calculator/03_flow.md`
- `docs/cli_simple_calculator/features/calculator/04_test_plan.md`
- `docs/cli_simple_calculator/features/calculator/05_review_checklist.md`
- `src/cli_simple_calculator/entrypoint.py`
- `src/cli_simple_calculator/features/calculator.py`
- `tests/cli_simple_calculator/test_entrypoint.py`
- `tests/cli_simple_calculator/features/test_calculator.py`

`prompts/*.md` は直接編集しません。
必要な情報は、各ステップのチャット例としてAIに渡します。

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
補足条件: Python標準ライブラリのみを使ってください。entrypoint.py と test_entrypoint.py は作成しないでください。
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
作成または更新するテストファイル: tests/cli_simple_calculator/test_entrypoint.py
対象 feature: calculator
補足条件: entrypoint.py は薄くし、features/calculator.py の機能を呼び出すだけにしてください。
```

作成または更新されるファイル:

```text
src/cli_simple_calculator/entrypoint.py
tests/cli_simple_calculator/test_entrypoint.py
```

---

## 8. テストを実行する

実装後、単体テストを実行します。

```bash
python -m pytest
```

環境によって `python` が使えない場合は、利用しているPythonの実行コマンドに読み替えてください。

---

## 9. 機能全体をレビューする

`prompts/review_feature.md` を参照して、実装後の機能レビューを行います。

レビュー結果は `05_review_checklist.md` ではなく、`06_review_result.md` に記録します。

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

## 進めるときの注意

- `prompts/*.md` は直接編集しません
- チャットで、参照するプロンプトのパスと対象機能情報を渡します
- 仕様にない便利機能は追加しません
- `entrypoint.py` は薄く保ちます
- feature 実装と entrypoint 実装は別のプロンプトで扱います
- 共通化候補があっても、勝手に `src/common/` へ切り出しません
- 結合試験、外部API、CI/CD、デプロイ資産は追加しません
