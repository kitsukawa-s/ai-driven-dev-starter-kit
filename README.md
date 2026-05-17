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
- feature 単体レビューと command/app 全体レビューを分ける流れ
- `overview.md` を起点に、コマンド/アプリ全体と feature 分割を整理する流れ
- 必要に応じて、entrypoint から feature を束ねる結合試験計画を作る流れ

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
│  │  ├─ 00_overview_template.md
│  │  ├─ tasks_template.md
│  │  ├─ 01_spec_template.md
│  │  ├─ 02_design_template.md
│  │  ├─ 03_flow_template.md
│  │  ├─ 04_test_plan_template.md
│  │  ├─ 05_review_checklist_template.md
│  │  ├─ 10_integration_test_plan_template.md
│  │  └─ 11_command_review_result_template.md
│  ├─ tutorials/
│  │  └─ 010_simple_calculator.md
│  ├─ cli_hello_greeting/
│  │  ├─ overview.md
│  │  ├─ 10_integration_test_plan.md
│  │  ├─ 11_command_review_result.md
│  │  └─ features/
│  │     └─ greeting/
│  │        ├─ 01_spec.md
│  │        ├─ 02_design.md
│  │        ├─ 03_flow.md
│  │        ├─ 04_test_plan.md
│  │        └─ 05_review_checklist.md
│  └─ cli_simple_calculator/
│     ├─ overview.md
│     ├─ tasks.md
│     ├─ 10_integration_test_plan.md
│     ├─ 11_command_review_result.md
│     └─ features/
│        └─ calculator/
│           ├─ tasks.md
│           └─ 01_spec.md
├─ prompts/
│  ├─ create_overview.md
│  ├─ create_feature_spec.md
│  ├─ create_function_design.md
│  ├─ create_function_call_flow.md
│  ├─ create_test_design.md
│  ├─ create_review_checklist.md
│  ├─ create_integration_test_plan.md
│  ├─ implement_feature.md
│  ├─ implement_entrypoint.md
│  ├─ implement_integration_test.md
│  ├─ review_feature.md
│  └─ review_command.md
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
      ├─ test_entrypoint_greeting.py
      ├─ test_integration_greeting.py
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

`tasks.md` は作業状態を引き継ぐための現在地メモです。
command/app 単位の `docs/<command_or_app_name>/tasks.md` には全体の作業状態を、feature 単位の `docs/<command_or_app_name>/features/<feature_name>/tasks.md` には個別機能の作業状態を短く記録します。
仕様、設計、テスト計画、レビュー結果の代わりにはしません。
新しく作成する場合は、`docs/templates/tasks_template.md` を参考にします。

---

## overview.md の位置づけ

`docs/<command_or_app_name>/overview.md` は、コマンド/アプリ全体の設計入口です。

ここでは、コマンド/アプリの目的、Boundary、`entrypoint.py`、feature 分割方針、機能一覧を整理します。
新しい機能を追加する場合は、まず overview.md でコマンド/アプリ全体の責務と feature 分割を確認し、そのうえで `features/<feature_name>/` 配下のドキュメントを作成します。

---

## entrypoint と features の責務

`entrypoint.py` はCLI入口として薄く保ちます。

- CLI引数を受け取る
- `features/` 配下の機能を呼び出す
- 結果を標準出力に出す
- 終了コードを返す

`features/` 配下には、機能固有のロジックを置きます。
標準出力やCLI引数解析は原則として持たせません。

実装時は、feature 本体と entrypoint を分けて扱います。
`prompts/implement_feature.md` は feature 本体と feature 単体テストを作成し、`prompts/implement_entrypoint.md` は `entrypoint.py` と `test_entrypoint_<short_name>.py` を作成します。
entrypoint 実装中に feature が呼び出しにくい場合も、勝手に feature 実装を変更せず、見直し候補として報告します。

entrypoint テストと結合試験の標準命名は以下です。

```text
tests/<command_or_app_name>/test_entrypoint_<short_name>.py
tests/<command_or_app_name>/test_integration_<short_name>.py
```

`<short_name>` は、単一 feature の command/app では feature 名を使います。
複数 feature を束ねる command/app では、command/app を短く表す名前を使います。

---

## 結合試験の位置づけ

このスターターキットにおける結合試験は、`entrypoint.py` から複数 feature を束ねて呼び出し、コマンド/アプリとして期待どおり動くことを確認するものです。

feature 単体の詳細ロジックは、各 feature の単体試験で確認します。
結合試験では、`entrypoint.py`、feature 呼び出し、入出力、終了コード、エラー時の扱いを確認します。

結合試験計画は、必要に応じて `docs/<command_or_app_name>/10_integration_test_plan.md` に作成します。
常に必須ではなく、entrypoint から feature を束ねて確認する必要がある場合に扱います。

---

## レビューの位置づけ

レビューは2段階で扱います。

- feature 単体レビュー: `prompts/review_feature.md` を使い、結果を `<対象機能フォルダ>/06_review_result.md` に記録します
- command/app 全体レビュー: `prompts/review_command.md` を使い、結果を `docs/<command_or_app_name>/11_command_review_result.md` に記録します

`review_feature.md` は feature の仕様、設計、実装、単体テストに集中します。
entrypoint と結合試験まで含めた最終確認は `review_command.md` で扱います。

既存のレビュー結果がある場合でも、古い判定をそのまま採用せず、現在のファイル群を読み直して再レビューします。

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

## はじめて使う場合

はじめて使う場合は、以下の順番で確認してください。

1. `README.md` で全体像を確認する
2. `docs/how_to_use_prompts.md` で汎用プロンプトの使い方を確認する
3. `docs/tutorials/010_simple_calculator.md` でチュートリアルを進める
4. 必要に応じて `docs/overview.md` でドキュメント構成を確認する

実際の作業では、`prompts/*.md` を直接編集せず、チャットで「参照するプロンプトのパス」と「対象機能情報」を渡して使います。

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
- CI/CD、デプロイ資産は追加しないでください
- 結合試験は、計画があり必要な場合だけ扱ってください
- feature 単体レビューと command/app 全体レビューを混ぜないでください
- `entrypoint.py` を厚くしないでください
- feature 固有ロジックを `entrypoint.py` に入れないでください
- `src/common/` に勝手に共通処理を追加しないでください
- 結合試験中にテストしにくい点があっても、勝手に実装コードを変更しないでください
- チュートリアル専用プロンプト置き場は作成しないでください
