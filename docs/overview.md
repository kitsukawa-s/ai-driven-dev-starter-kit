# ドキュメント構成

このリポジトリでは、コマンド/アプリ単位で docs、src、tests を対応させます。

```text
docs/<command_or_app_name>/
src/<command_or_app_name>/
tests/<command_or_app_name>/
tests/<command_or_app_name>/test_entrypoint_<short_name>.py
tests/<command_or_app_name>/test_integration_<short_name>.py
tests/<command_or_app_name>/features/test_<feature_name>.py
```

`<short_name>` は、単一 feature の command/app では feature 名を使います。
複数 feature を束ねる command/app では、command/app を短く表す名前を使います。

個別 feature は `features/<feature_name>/` 配下で管理します。

---

## 基本構成

```text
docs/
  <command_or_app_name>/
    10_overview.md
    11_integration_test_plan.md
    12_command_review_result.md
    features/
      <feature_name>/
        20_spec.md
        21_design.md
        22_flow.md
        23_test_plan.md
        24_review_checklist.md
        25_review_result.md
```

`25_review_result.md` は、feature 単体レビューを行った場合に作成します。
`12_command_review_result.md` は、command/app 全体レビューを行った場合に作成します。
まだレビューしていない場合は、無理に作成しません。

---

## 各ファイルの役割

| ファイル | 役割 |
|---|---|
| `10_overview.md` | コマンド/アプリ全体の目的、入口、機能一覧、責務分担を書く |
| `11_integration_test_plan.md` | command/app 単位の結合試験計画を書く |
| `12_command_review_result.md` | command/app 全体レビュー結果を書く |
| `20_spec.md` | feature の要件・仕様を書く |
| `21_design.md` | 関数単位の責務、入力、出力、エラー方針を書く |
| `22_flow.md` | 関数同士の呼び出し順、依存関係、全体フローを書く |
| `23_test_plan.md` | feature 単体テストの観点を書く |
| `24_review_checklist.md` | feature 単体レビュー観点を書く。レビュー結果は書き込まない |
| `25_review_result.md` | feature 単体レビュー結果、指摘事項、最終判定を書く |

`25_review_result.md` は feature 単体の仕様、設計、実装、単体テストを確認するためのレビュー結果です。
`12_command_review_result.md` は overview、entrypoint、結合試験、全体テスト、feature 単体レビュー結果を確認するためのレビュー結果です。

---

## テンプレート

ドキュメントを作成する場合は、以下のテンプレートを参照します。

| 作成するファイル | 参照するテンプレート |
|---|---|
| `10_overview.md` | `docs/templates/10_overview_template.md` |
| `20_spec.md` | `docs/templates/20_spec_template.md` |
| `21_design.md` | `docs/templates/21_design_template.md` |
| `22_flow.md` | `docs/templates/22_flow_template.md` |
| `23_test_plan.md` | `docs/templates/23_test_plan_template.md` |
| `24_review_checklist.md` | `docs/templates/24_review_checklist_template.md` |
| `11_integration_test_plan.md` | `docs/templates/11_integration_test_plan_template.md` |
| `12_command_review_result.md` | `docs/templates/12_command_review_result_template.md` |
| `30_common_proposal.md` | `docs/templates/30_common_proposal_template.md` |

---

## entrypoint と features

`src/<command_or_app_name>/entrypoint.py` はCLI入口です。

- CLI引数を受け取る
- `features/` 配下の機能を呼び出す
- 結果を標準出力に出す
- 終了コードを返す

feature 固有のロジックは `src/<command_or_app_name>/features/<feature_name>.py` に置きます。
`entrypoint.py` に業務ロジック本体や複雑な変換処理を置かないでください。

entrypoint のテストは `tests/<command_or_app_name>/test_entrypoint_<short_name>.py` に置きます。
結合試験は `tests/<command_or_app_name>/test_integration_<short_name>.py` に置きます。
feature の単体テストは `tests/<command_or_app_name>/features/test_<feature_name>.py` に置きます。

---

## feature フォルダ名の番号プレフィックス

単純なアプリでは、feature フォルダ名は `text_counter` のように機能名だけで構いません。

処理順・呼び出し順・パイプライン順が重要な場合は、`010_`、`020_` のような番号プレフィックスを付けてもよいです。

```text
docs/<command_or_app_name>/features/
├─ 010_load_inputs/
├─ 020_normalize_data/
├─ 030_compare_items/
└─ 040_output_result/
```

番号プレフィックスは、人間とAIが処理順を共有しやすくするためのものです。以下の点に注意してください。

- Python の実装ファイル名やモジュール名まで番号付きにする必要はない
- 番号付き feature フォルダを使う場合も、フォルダ内のドキュメント番号体系（`20_spec.md` など）は変わらない
- `tasks.md` は番号なしのまま現在地メモとして扱う

---

## テスト計画と結合試験計画

`23_test_plan.md` は feature 単体テストの計画です。
feature の詳細ロジック、正常系、異常系、境界値などを確認します。

`11_integration_test_plan.md` は command/app 単位の結合試験計画です。
`entrypoint.py` から feature を呼び出したときの接続、入出力、終了コード、エラー時の扱いを確認します。

結合試験は常に必須ではありません。entrypoint から feature を束ねて確認する必要がある場合に扱います。

---

## common の扱い

`src/common/` は共通処理置き場です。

ただし、AIは人間の明示指示なしに `src/common/` を作成・更新しません。
共通化候補がある場合は、設計書、レビュー結果、または作業報告に提案として記録します。
提案をまとめる場合は、`docs/templates/30_common_proposal_template.md` を使います。

---

## prompts

`prompts/` 直下には、実プロジェクトでも使う汎用プロンプトだけを配置します。チュートリアル専用プロンプトは置きません。

汎用プロンプトは直接書き換えず、チャットで参照するプロンプトのパスと対象情報を渡して使います。
詳しくは `docs/how_to_use_prompts.md` を参照してください。

`review_feature_source.md` は `implement_feature.md` 直後の中間チェック用プロンプトです。実装ファイルとテストファイルを仕様・設計・テスト計画と照合し、修正候補をチャットで報告します。ファイルは変更しません。`25_review_result.md` も作成しません。正式なレビュー結果は `review_feature.md` で行います。

---

## 今回の対象範囲

このスターターキットでは、feature 単体の単体試験を基本にします。
必要に応じて、command/app 単位の結合試験計画と結合試験も扱います。

対象にするもの:

- overview による command/app 全体の整理
- feature 分割
- feature 仕様の整理
- 関数設計
- 関数呼び出し定義
- feature 単体テスト計画
- feature 実装
- feature 単体テスト
- 必要に応じた結合試験計画
- 必要に応じた結合試験
- feature ソースレビュー（実装直後の中間チェック）
- feature 単体レビュー
- command/app 全体レビュー

対象外:

- 外部システム連携
- CI/CD
- デプロイ
- 本番運用設定
