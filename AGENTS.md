# AGENTS.md

このリポジトリは、AI駆動開発を小さく体験するためのスターターキットです。

AIは、いきなり実装するのではなく、仕様・設計・テスト観点を確認しながら、段階的に作業してください。

---

## 基本方針

- いきなり実装しない
- まず対象機能の仕様書を読む
- 仕様に書かれていない機能を勝手に追加しない
- 不明点がある場合は、勝手に決めずに「仮定」として明記する
- 小さく設計し、小さく実装し、小さくテストする
- 初学者が読んでも理解しやすいコードにする
- 実装コードでは、Python標準ライブラリのみを使用する
- 単体テストでは `pytest` を使用してよい
- `requirements.txt` には、単体テスト用の `pytest` 以外の依存を勝手に追加しない
- 変更したファイルと理由を簡潔に説明する
- 実装後は、テスト結果を確認して報告する
- 共通化候補があっても、勝手に共通モジュールへ切り出さない

---

## 対象範囲

このリポジトリでは、feature 単位の単体試験を基本とします。
必要に応じて、command/app 単位の結合試験も扱います。

AIは、以下を勝手に追加しないでください。

- CI/CD設定
- GitHub Actions
- デプロイ設定
- 外部システム連携
- 環境別設定ファイル
- 複雑なテスト基盤

必要だと感じた場合は、実装せずに「今後の拡張候補」として記載してください。

---

## ディレクトリ構成

docs、src、tests は `<command_or_app_name>` 単位で対応させます。

```text
docs/
  <command_or_app_name>/
    10_overview.md
    tasks.md
    11_integration_test_plan.md
    12_command_review_result.md
    features/
      <feature_name>/
        tasks.md
        20_spec.md
        21_design.md
        22_flow.md
        23_test_plan.md
        24_review_checklist.md
        25_review_result.md

src/
  common/
    __init__.py
  <command_or_app_name>/
    __init__.py
    entrypoint.py
    features/
      __init__.py
      <feature_name>.py

tests/
  <command_or_app_name>/
    test_entrypoint_<short_name>.py
    test_integration_<short_name>.py
    features/
      test_<feature_name>.py
```

`<short_name>` は、単一 feature の command/app では feature 名を使います。
複数 feature を束ねる command/app では、command/app を短く表す名前を使います。

`25_review_result.md` は feature 単体レビュー結果を記録するファイルです。
`12_command_review_result.md` は command/app 全体レビュー結果を記録するファイルです。
まだレビューしていない場合は、無理に作成しなくて構いません。

`tasks.md` は作業状態を記録するファイルです。
command/app 単位では `docs/<command_or_app_name>/tasks.md`、feature 単位では `docs/<command_or_app_name>/features/<feature_name>/tasks.md` に配置します。
まだ作業状態を記録する必要がない場合は、無理に作成しなくて構いません。

---

## ドキュメント管理ルール

- コマンド/アプリごとのドキュメントは `docs/<command_or_app_name>/` に配置する
- コマンド/アプリ全体の説明は `docs/<command_or_app_name>/10_overview.md` に書く
- 個別機能の仕様・設計・呼び出し定義・テスト計画・レビュー観点は `docs/<command_or_app_name>/features/<feature_name>/` にまとめる
- 新しい機能を追加する場合は、対象コマンド/アプリの `features/<feature_name>/` 配下に追加する
- feature 名は機能単位の名前にし、関数名や実装上の処理名だけを理由に feature フォルダを分けない
- 処理順・呼び出し順・パイプライン順が重要な場合は、feature フォルダ名に `010_`、`020_`、`030_` のような番号プレフィックスを付けてよい。ただし、Python の実装ファイル名やモジュール名まで番号付きにしない
- 番号付き feature フォルダを使う場合も、フォルダ内のドキュメント番号体系（`20_spec.md`、`21_design.md` など）は変えない
- 作業を中断・再開・引き継ぎしやすくしたい場合は、対象範囲の `tasks.md` に現在の状態、次にやること、保留事項を短く記録する
- `tasks.md` は作業管理用のメモとし、仕様・設計・テスト計画・レビュー結果の代わりにしない
- 実装前に、対象機能フォルダ内の設計書を確認する
- 実装後に、設計書と実装内容にズレがないか確認する

---

## ドキュメントひな形

新しい機能ドキュメントを作成または更新する場合は、`docs/templates/` 配下のひな形を参照してください。

| 作成するファイル | 参照するひな形 |
|---|---|
| `10_overview.md` | `docs/templates/10_overview_template.md` |
| `tasks.md` | `docs/templates/tasks_template.md` |
| `20_spec.md` | `docs/templates/20_spec_template.md` |
| `21_design.md` | `docs/templates/21_design_template.md` |
| `22_flow.md` | `docs/templates/22_flow_template.md` |
| `23_test_plan.md` | `docs/templates/23_test_plan_template.md` |
| `24_review_checklist.md` | `docs/templates/24_review_checklist_template.md` |
| `11_integration_test_plan.md` | `docs/templates/11_integration_test_plan_template.md` |
| `12_command_review_result.md` | `docs/templates/12_command_review_result_template.md` |
| `30_common_proposal.md` | `docs/templates/30_common_proposal_template.md` |

AIは、ひな形の見出し構成を勝手に変更しないでください。
必要な情報がない場合は、見出しを削除せず、`未定`、`該当なし`、`今回は対象外` のように記載してください。

---

## 開発の進め方

原則として、以下の順番で作業してください。

1. `10_overview.md` を確認または作成する
2. 必要に応じて `tasks.md` を確認または作成し、現在の作業状態を短く記録する
3. `10_overview.md` をもとに feature 分割を確認する
4. 対象 feature の `20_spec.md` を作成または確認する
5. 必要に応じて feature 側の `tasks.md` を確認または作成する
6. `21_design.md` を作成または更新する
7. `22_flow.md` を作成または更新する
8. `23_test_plan.md` を作成または更新する
9. `24_review_checklist.md` を作成または更新する
10. feature 本体と feature 単体テストを作成する
11. 必要に応じて `entrypoint.py` と `test_entrypoint_<short_name>.py` を作成する
12. 必要に応じて `11_integration_test_plan.md` を作成する
13. 必要に応じて結合試験を実装する
14. `python -m pytest` を実行する
15. feature 単体レビューを行い、`25_review_result.md` に記録する
16. command/app 全体レビューを行い、`12_command_review_result.md` に記録する

結合試験は常に必須ではありません。
entrypoint から複数 feature を束ねて確認する必要がある場合に扱ってください。

---

## entrypoint と features の責務

`src/<command_or_app_name>/entrypoint.py` は入口として薄くしてください。

entrypoint の責務:

- CLI引数を受け取る
- `features/` 配下の機能を呼び出す
- 結果を標準出力に出す
- 終了コードを返す

entrypoint に入れてはいけないもの:

- 業務ロジック本体
- 複雑な変換処理
- 機能固有の判断
- 共通化候補の実装
- 仕様にない便利機能

機能実装は `src/<command_or_app_name>/features/<feature_name>.py` に置いてください。
entrypoint 実装中に feature が呼び出しにくい場合でも、勝手に feature 実装を変更しないでください。
必要な見直しは作業報告に記載し、人間レビューに回してください。

---

## 結合試験の扱い

`11_integration_test_plan.md` は、command/app 単位の結合試験計画です。

feature 単体の詳細ロジックは、feature 単体試験で確認してください。
結合試験では、`entrypoint.py` と feature の接続、入出力、終了コード、エラー時の扱いを確認します。

結合試験を実装している途中でテストしにくいと判断しても、勝手に `src/` を変更しないでください。
実装側の変更が必要そうな場合は、作業報告に記載し、人間レビューに回してください。

---

## レビュー結果の扱い

feature 単体レビューは `<対象機能フォルダ>/25_review_result.md` に記録します。
command/app 全体レビューは `docs/<command_or_app_name>/12_command_review_result.md` に記録します。

既存のレビュー結果がある場合でも、古い判定をそのまま採用せず、現在の仕様・設計・実装・テストを読み直して再レビューしてください。
レビュー中に問題を見つけても、レビュー結果ファイル以外を勝手に変更しないでください。

レビュー結果に指摘がある場合でも、AIはその場で勝手に修正しないでください。
指摘の反映は、人間がレビュー結果を確認し、反映する指摘を判断したあとに、別作業としてAIに依頼します。
AIは承認された指摘だけを対象に修正を行い、反映後は `python -m pytest` を実行してください。
必要に応じて、再度レビューを行ってください。

`tasks.md` には、レビューの判定や詳細な指摘を記録しません。
未完了作業、次の一手、保留事項だけを短く記録し、レビュー結果は `25_review_result.md` または `12_command_review_result.md` に分けてください。

---

## common の扱い

`src/common/` は共通処理置き場ですが、保護対象です。

AIは、人間の明示指示なしに `src/common/` を作成・更新してはいけません。
共通化候補がある場合は、実装せず、設計書、レビュー結果、または作業報告に提案として記録してください。
提案を整理する場合は、`docs/templates/30_common_proposal_template.md` を使って `docs/common/` 配下にまとめてください。

共通化を検討する場合は、以下を明記してください。

- 候補となる処理
- 想定される共通化先
- 共通化を検討する理由
- 影響を受ける機能
- 現時点で共通化すべきかどうか

判断に迷う場合は、まず機能内に閉じた実装を優先してください。

---

## prompts の扱い

`prompts/` 直下には、実プロジェクトでも使う汎用プロンプトだけを配置します。

- `prompts/*.md` は直接編集しない
- チャットで「参照するプロンプトのパス」と「対象機能情報」を渡す
- チュートリアルでも汎用プロンプトを参照して使う
- チュートリアル専用プロンプトは作成しない

---

## 保護対象

AIは、明示指示なしに以下を変更しないでください。

- `AGENTS.md`
- `prompts/*.md`
- `docs/templates/`
- `src/common/`
- `requirements.txt`
- CI/CD、デプロイ関連ファイル

今回のように利用者が明示的にルール更新を依頼した場合のみ、`AGENTS.md` や `prompts/*.md` を必要最小限で更新してください。

---

## 実装ルール

- Python標準ライブラリのみを使う
- CLI引数の解析には `argparse` を使う
- 単体テストには `pytest` を使う
- ファイル名と関数名はスネークケースにする
- 複雑なクラス設計は避ける
- まずは関数中心で実装する
- 仕様にない便利機能を追加しない

---

## 作業完了時の報告フォーマット

### 作業結果

#### 変更したファイル

- `...`

#### 実装内容

- ...

#### テスト結果

- 実行コマンド: `python -m pytest`
- 結果: ...

#### 確認したこと

- overview とのズレ: なし / あり / 該当なし
- 仕様とのズレ: なし / あり
- 関数設計とのズレ: なし / あり
- 呼び出し定義とのズレ: なし / あり
- テスト計画とのズレ: なし / あり
- 結合試験計画とのズレ: なし / あり / 該当なし
- 共通化候補: なし / あり
- AIが勝手に共通化していないこと: 確認済み / 未確認
- 気になる点: ...

#### 次にやるとよさそうなこと

- ...
