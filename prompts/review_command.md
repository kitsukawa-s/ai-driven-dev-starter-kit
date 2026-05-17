# command/app 全体レビューを行ってください

このプロンプトは、command/app 全体のレビューを行い、結果を `docs/<command_or_app_name>/11_command_review_result.md` に記録するためのものです。

feature 単体レビューは `prompts/review_feature.md` の範囲です。このプロンプトでは、overview、entrypoint、結合試験、全体テスト、feature 単体レビュー結果を踏まえて、command/app としての整合を確認します。

---

## 利用者が指定する項目

- コマンド/アプリ名: `<command_or_app_name>`
- 対象 overview: `docs/<command_or_app_name>/overview.md`
- 対象 entrypoint: `src/<command_or_app_name>/entrypoint.py`
- entrypoint テスト: `tests/<command_or_app_name>/test_entrypoint_<short_name>.py`
- 結合試験計画: `docs/<command_or_app_name>/10_integration_test_plan.md`
- 結合試験ファイル: `tests/<command_or_app_name>/test_integration_<short_name>.py`
- command/app 全体レビュー結果ファイル: `docs/<command_or_app_name>/11_command_review_result.md`
- short_name: `単一 feature の command/app では feature 名。複数 feature を束ねる command/app では command/app を短く表す名前`
- 補足条件: `必要に応じて書く。なければ「なし」`

## 参照するファイル

必ず現在の以下を読み直してください。

- `AGENTS.md`
- `docs/<command_or_app_name>/overview.md`
- `docs/<command_or_app_name>/10_integration_test_plan.md`
- `src/<command_or_app_name>/entrypoint.py`
- `tests/<command_or_app_name>/test_entrypoint_<short_name>.py`
- `tests/<command_or_app_name>/test_integration_<short_name>.py`
- `docs/<command_or_app_name>/features/*/06_review_result.md`

必要に応じて、以下も参照してください。

- `docs/<command_or_app_name>/features/*/01_spec.md`
- `docs/<command_or_app_name>/features/*/02_design.md`
- `docs/<command_or_app_name>/features/*/03_flow.md`
- `docs/<command_or_app_name>/features/*/04_test_plan.md`
- `docs/<command_or_app_name>/features/*/05_review_checklist.md`
- `src/<command_or_app_name>/features/*.py`
- `tests/<command_or_app_name>/features/test_*.py`

## 作成または更新するファイル

- `docs/<command_or_app_name>/11_command_review_result.md`

## 変更してはいけないファイル

レビュー結果ファイル以外を変更しないでください。

- `src/`
- `tests/`
- `docs/<command_or_app_name>/overview.md`
- `docs/<command_or_app_name>/10_integration_test_plan.md`
- `docs/<command_or_app_name>/features/`
- `prompts/`
- `AGENTS.md`
- `README.md`
- `docs/templates/`

レビュー中に問題を見つけても、勝手に修正しないでください。修正候補として `11_command_review_result.md` に記録してください。

---

## 再レビュー時のルール

既存の `11_command_review_result.md` が存在する場合でも、古い判定をそのまま採用しないでください。

必ず現在の overview、entrypoint、entrypoint テスト、結合試験計画、結合試験、feature 単体レビュー結果を読み直してください。

既存の `11_command_review_result.md` は参考情報として扱っても構いませんが、最終判定は現在のファイル群に基づいて判断し、新しいレビュー結果として上書き更新してください。

## 作業手順

1. `AGENTS.md` を確認してください
2. `docs/<command_or_app_name>/overview.md` を確認してください
3. feature 分割と feature 単体レビュー結果を確認してください
4. `src/<command_or_app_name>/entrypoint.py` を確認してください
5. `tests/<command_or_app_name>/test_entrypoint_<short_name>.py` を確認してください
6. `docs/<command_or_app_name>/10_integration_test_plan.md` を確認してください
7. `tests/<command_or_app_name>/test_integration_<short_name>.py` を確認してください
8. 必要に応じて feature の 01〜05 ドキュメント、実装、単体テストを確認してください
9. `python -m pytest` または利用者が指定したテストコマンドを実行し、全体テスト結果を確認してください
10. レビュー結果を `docs/<command_or_app_name>/11_command_review_result.md` に作成または上書き更新してください

## 主に確認すること

- `overview.md` と実装全体が整合していること
- feature 分割が妥当であること
- `entrypoint.py` が薄く保たれていること
- feature 固有ロジックが `entrypoint.py` に入っていないこと
- `src/common/` に勝手に共通化していないこと
- `10_integration_test_plan.md` と `test_integration_<short_name>.py` が整合していること
- `test_entrypoint_<short_name>.py` と `test_integration_<short_name>.py` の役割が重複しすぎていないこと
- `python -m pytest` の結果が確認されていること
- feature 単体レビュー結果に未解決の重大指摘がないこと
- 指定外ファイル名への変更や AI 判断によるアドリブがないこと
- 指定された出力先を AI 判断で変更していないこと
- entrypoint テストと結合試験が標準命名ルールに従っていること
- `pytest` の import mismatch やテストファイル名衝突がある場合、標準命名ルールと現状の差分を確認せずに別名ファイルを作成していないこと
- fallback import などが必要な場合、その理由と影響が説明できること
- 古いレビュー結果の判定をそのまま再利用していないこと

## レビュー結果に記録する内容

`11_command_review_result.md` には、`docs/templates/11_command_review_result_template.md` の見出し構成に沿って以下を記録してください。

- レビュー対象
- 参照したファイル
- 実行した確認内容
- テスト実行結果
- overview.md との整合
- feature 分割の妥当性
- entrypoint の責務確認
- feature 実装との責務分担
- 結合試験計画との整合
- 結合試験実装との整合
- feature 単体レビュー結果の確認
- 指定外変更・AIアドリブの有無
- 指摘事項
- 改善候補
- 仕様変更が必要そうな点
- 最終判定
- 作業後報告

## 最終判定

レビュー結果の最後に、以下のいずれかを記録してください。

- `OK`: 大きな問題なし
- `軽微な指摘あり`: 軽微な修正または確認事項がある
- `要修正`: 実装、テスト、ドキュメントの修正が必要
- `要仕様確認`: 仕様に戻って確認が必要

## 禁止事項

- `11_command_review_result.md` 以外を変更しないでください
- `src/` を変更しないでください
- `tests/` を変更しないでください
- overview、結合試験計画、feature ドキュメントを変更しないでください
- `prompts/`、`AGENTS.md`、`README.md`、`docs/templates/` を変更しないでください
- 指定された出力先を AI 判断で変更しないでください
- `pytest` の import mismatch やテストファイル名衝突を理由に、標準命名ルールと現状の差分を確認せずに別名のテストファイルを作成しないでください
- fallback import を勝手に追加しないでください
- feature 単体レビュー結果を読み直さず、古い判定をそのまま採用しないでください

## 作業後の報告

作業後に、以下を簡潔に報告してください。

- 作成または更新したファイル
- 参照したファイル
- テスト実行コマンドと結果
- 最終判定
- feature 単体レビュー結果に未解決の重大指摘があったか
- command/app 全体として気になる点

## 作業後の tasks.md 更新

作業後は、対象 command/app または feature の `tasks.md` を必ず確認してください。

必要に応じて、現在の状態、作業メモ、次に確認することだけを短く更新してください。

`tasks.md` には、仕様・設計・テスト計画・レビュー結果の詳細を書かないでください。
詳細は `overview.md`、`10_integration_test_plan.md`、`11_command_review_result.md`、feature 側の専用ファイルなど、それぞれの専用ファイルに記録してください。

`tasks.md` を更新しない場合は、更新しない理由を作業報告に書いてください。
