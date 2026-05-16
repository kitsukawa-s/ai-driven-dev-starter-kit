# AI駆動開発スターターキット

このリポジトリは、GitHub Copilot Agent Mode を使って、AI駆動開発の流れを小さく体験するためのスターターキットです。

目的は、完成度の高いアプリを作ることではありません。
人間が理解できる仕様と設計を用意し、それをもとにAIと一緒に小さく開発する流れを体験します。

---

## このリポジトリで体験できること

- AIに作業してもらうための `AGENTS.md` の使い方
- コマンド/アプリ単位で docs、src、tests を対応させる方法
- 個別機能を `features/<feature_name>/` で管理する方法
- 仕様、設計、呼び出し定義、テスト計画、レビュー観点を先に整理する流れ
- `entrypoint.py` と `features/` の責務を分ける流れ
- AIの出力を各工程でレビューする流れ

---

## 前提

- Python を実行できること
- GitHub Copilot Agent Mode を使えること
- 実装コードでは Python 標準ライブラリのみを使うこと
- 単体テストには `pytest` を使うこと

テスト実行用の最小依存として、`requirements.txt` に `pytest` のみを記載しています。

```bash
python -m pip install -r requirements.txt
```

---

## リポジトリ構成

```text
ai-driven-dev-starter-kit/
├─ README.md
├─ AGENTS.md
├─ docs/
│  ├─ overview.md
│  ├─ how_to_use_prompts.md
│  ├─ common/
│  │  └─ README.md
│  ├─ templates/
│  │  ├─ 01_spec_template.md
│  │  ├─ 02_design_template.md
│  │  ├─ 03_flow_template.md
│  │  ├─ 04_test_plan_template.md
│  │  └─ 05_review_checklist_template.md
│  ├─ tutorials/
│  │  └─ 010_simple_calculator.md
│  ├─ cli_hello_greeting/
│  │  ├─ overview.md
│  │  └─ features/
│  │     └─ greeting/
│  │        ├─ 01_spec.md
│  │        ├─ 02_design.md
│  │        ├─ 03_flow.md
│  │        ├─ 04_test_plan.md
│  │        └─ 05_review_checklist.md
│  └─ cli_simple_calculator/
│     ├─ overview.md
│     └─ features/
│        └─ calculator/
│           └─ 01_spec.md
├─ prompts/
│  ├─ create_feature_spec.md
│  ├─ create_function_design.md
│  ├─ create_function_call_flow.md
│  ├─ create_test_design.md
│  ├─ create_review_checklist.md
│  ├─ implement_feature.md
│  └─ review_feature.md
├─ src/
│  ├─ common/
│  │  └─ __init__.py
│  └─ cli_hello_greeting/
│     ├─ __init__.py
│     ├─ entrypoint.py
│     └─ features/
│        ├─ __init__.py
│        └─ greeting.py
└─ tests/
   └─ cli_hello_greeting/
      ├─ test_entrypoint.py
      └─ features/
         └─ test_greeting.py
```

---

## docs / src / tests の対応関係

コマンド/アプリ単位で、同じ名前のまとまりを作ります。

```text
docs/<command_or_app_name>/
src/<command_or_app_name>/
tests/<command_or_app_name>/
```

個別機能は、それぞれの `features/` 配下で管理します。

```text
docs/<command_or_app_name>/features/<feature_name>/
src/<command_or_app_name>/features/<feature_name>.py
tests/<command_or_app_name>/features/test_<feature_name>.py
```

---

## entrypoint と features の責務

`entrypoint.py` はCLI入口として薄く保ちます。

- CLI引数を受け取る
- `features/` 配下の機能を呼び出す
- 結果を標準出力に出す
- 終了コードを返す

`features/` 配下には、機能固有のロジックを置きます。
標準出力やCLI引数解析は原則として持たせません。

---

## common の扱い

`src/common/` は共通処理置き場です。

ただし、AIは人間の明示指示なしに `src/common/` を作成・更新しません。
共通化候補がある場合は、設計書、レビュー結果、作業報告に提案として記録します。

---

## prompts の使い方

`prompts/` 直下には、実プロジェクトでも使う汎用プロンプトだけを配置します。
チュートリアル専用プロンプトは置きません。

汎用プロンプトは直接書き換えず、チャットで以下を渡して使います。

- 参照するプロンプトのパス
- 対象機能フォルダ
- コマンド/アプリ名
- 対象機能名
- 実装ファイル
- テストファイル
- 補足条件

詳しくは `docs/how_to_use_prompts.md` を参照してください。

---

## チュートリアル

`docs/tutorials/010_simple_calculator.md` に、`cli_simple_calculator` を題材にした手順書を配置しています。

チュートリアルでも `prompts/` 直下の汎用プロンプトを参照し、チャットで対象機能情報を渡して進めます。

---

## サンプル機能

完成済みサンプルとして、以下を配置しています。

```text
docs/cli_hello_greeting/features/greeting/
src/cli_hello_greeting/
tests/cli_hello_greeting/
```

実行例:

```bash
python src/cli_hello_greeting/entrypoint.py --name Alice
```

期待する出力:

```text
Hello, Alice!
```

---

## テスト実行

```bash
python -m pytest
```

---

## 注意事項

- 仕様にない機能を勝手に追加しないでください
- 外部ライブラリは原則使わないでください
- CI/CD、結合試験、デプロイ資産は追加しないでください
- `entrypoint.py` を厚くしないでください
- `src/common/` に勝手に共通処理を追加しないでください
- チュートリアル専用プロンプト置き場は作成しないでください
