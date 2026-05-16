# ドキュメント構成

このリポジトリでは、コマンド/アプリ単位で docs、src、tests を対応させます。

```text
docs/<command_or_app_name>/
src/<command_or_app_name>/
tests/<command_or_app_name>/
```

個別機能は `features/<feature_name>/` 配下で管理します。

---

## 基本構成

```text
docs/
  <command_or_app_name>/
    overview.md
    features/
      <feature_name>/
        01_spec.md
        02_design.md
        03_flow.md
        04_test_plan.md
        05_review_checklist.md
        06_review_result.md
```

`06_review_result.md` は、実装後レビューを行った場合に作成します。
まだレビューしていない機能では、無理に作成しません。

---

## 各ファイルの役割

| ファイル | 役割 |
|---|---|
| `overview.md` | コマンド/アプリ全体の目的、入口、機能一覧、責務分担を書く |
| `01_spec.md` | 機能要望・仕様を書く |
| `02_design.md` | 関数単位の責務・入力・出力・エラー方針を書く |
| `03_flow.md` | 関数同士の呼び出し順・依存関係・全体フローを書く |
| `04_test_plan.md` | 単体テストの観点を書く |
| `05_review_checklist.md` | レビュー観点を書く。レビュー結果は書き込まない |
| `06_review_result.md` | 実際のレビュー結果、指摘事項、最終判定を書く |

---

## テンプレート

機能ドキュメントを作成する場合は、以下のテンプレートを参照します。

| 作成するファイル | 参照するテンプレート |
|---|---|
| `01_spec.md` | `docs/templates/01_spec_template.md` |
| `02_design.md` | `docs/templates/02_design_template.md` |
| `03_flow.md` | `docs/templates/03_flow_template.md` |
| `04_test_plan.md` | `docs/templates/04_test_plan_template.md` |
| `05_review_checklist.md` | `docs/templates/05_review_checklist_template.md` |

---

## entrypoint と features

`src/<command_or_app_name>/entrypoint.py` はCLI入口です。

- CLI引数を受け取る
- `features/` 配下の機能を呼び出す
- 結果を標準出力に出す
- 終了コードを返す

機能固有のロジックは `src/<command_or_app_name>/features/<feature_name>.py` に置きます。
`entrypoint.py` に業務ロジック本体や複雑な変換処理を置かないでください。

---

## common の扱い

`src/common/` は共通処理置き場です。

ただし、AIは人間の明示指示なしに `src/common/` を作成・更新しません。
共通化候補は、設計書、レビュー結果、作業報告に提案として記録します。

---

## prompts

`prompts/` 直下には、実プロジェクトでも使う汎用プロンプトだけを配置します。
チュートリアル専用プロンプトは置きません。

汎用プロンプトは直接書き換えず、チャットで参照するプロンプトのパスと対象機能情報を渡して使います。

詳しくは `docs/how_to_use_prompts.md` を参照してください。

---

## チュートリアル

チュートリアル手順書は `docs/tutorials/` 配下に配置します。
チュートリアルでも `prompts/` 直下の汎用プロンプトを参照して使います。

---

## 今回の対象範囲

このスターターキットでは、単体試験までを対象にします。

対象にするもの:

- 機能要望の整理
- 関数設計
- 関数呼び出し定義
- テスト計画
- 実装
- 単体テスト
- レビュー

対象外:

- 結合試験
- 外部システム連携
- 結合試験用スタブ
- CI/CD
- デプロイ
- 本番運用設計
