# feature 単体レビューを行ってください

このプロンプトは、実装後の feature 単体レビューを行い、結果を `<対象機能フォルダ>/06_review_result.md` に記録するためのものです。

`05_review_checklist.md` はレビュー観点の定義です。レビュー結果や指摘事項は `05_review_checklist.md` には追記せず、`06_review_result.md` に記録してください。

このプロンプトは feature 単体レビュー専用です。`entrypoint.py`、entrypoint テスト、`10_integration_test_plan.md`、結合試験は原則として主対象にしません。feature との責務分担に関係する場合だけ関連ファイルとして参照して構いませんが、command/app 全体の判定は `prompts/review_command.md` に委ねてください。

---

## 利用者が指定する項目

以下を対象 feature に合わせて指定してください。

- 対象機能フォルダ: `docs/<command_or_app_name>/features/<feature_name>/`
- コマンド/アプリ名: `<command_or_app_name>`
- 対象機能名: `<feature_name>`
- 実装ファイル: `src/<command_or_app_name>/features/<feature_name>.py`
- テストファイル: `tests/<command_or_app_name>/features/test_<feature_name>.py`
- レビュー結果ファイル: `<対象機能フォルダ>/06_review_result.md`
- 補足条件: `必要に応じて書く。なければ「なし」`

## 参照するファイル

必ず現在の以下を読み直してください。

- `AGENTS.md`
- `<対象機能フォルダ>/01_spec.md`
- `<対象機能フォルダ>/02_design.md`
- `<対象機能フォルダ>/03_flow.md`
- `<対象機能フォルダ>/04_test_plan.md`
- `<対象機能フォルダ>/05_review_checklist.md`
- 利用者が指定した feature 実装ファイル
- 利用者が指定した feature 単体テストファイル

必要に応じて、feature との責務分担を確認するためだけに以下を参照して構いません。

- `docs/<command_or_app_name>/overview.md`
- `src/<command_or_app_name>/entrypoint.py`
- `tests/<command_or_app_name>/test_entrypoint_<short_name>.py`
- `docs/<command_or_app_name>/10_integration_test_plan.md`
- `tests/<command_or_app_name>/test_integration_<short_name>.py`

ただし、これらの command/app 全体に関する最終判定は `prompts/review_command.md` の範囲です。

## 作成または更新するファイル

- `<対象機能フォルダ>/06_review_result.md`

## 変更してはいけないファイル

レビュー依頼だけの場合、以下は変更しないでください。

- `<対象機能フォルダ>/01_spec.md`
- `<対象機能フォルダ>/02_design.md`
- `<対象機能フォルダ>/03_flow.md`
- `<対象機能フォルダ>/04_test_plan.md`
- `<対象機能フォルダ>/05_review_checklist.md`
- feature 実装ファイル
- feature 単体テストファイル
- `src/<command_or_app_name>/entrypoint.py`
- `tests/<command_or_app_name>/test_entrypoint_<short_name>.py`
- `docs/<command_or_app_name>/10_integration_test_plan.md`
- `tests/<command_or_app_name>/test_integration_<short_name>.py`
- `prompts/`
- `AGENTS.md`
- `README.md`
- `docs/templates/`

レビュー中に仕様、設計、実装、テストの修正が必要だと判断した場合でも、勝手に修正しないでください。修正候補として `06_review_result.md` に記録してください。

---

## 再レビュー時のルール

既存の `06_review_result.md` が存在する場合でも、古い判定をそのまま採用しないでください。

必ず現在の `01_spec.md`、`02_design.md`、`03_flow.md`、`04_test_plan.md`、`05_review_checklist.md`、feature 実装ファイル、feature 単体テストファイルを読み直してください。

既存の `06_review_result.md` は参考情報として扱っても構いませんが、最終判定は現在のファイル群に基づいて判断し、新しいレビュー結果として `06_review_result.md` を上書き更新してください。

---

## 作業手順

1. `AGENTS.md` を確認してください
2. 対象 feature の `01_spec.md` から `05_review_checklist.md` を確認してください
3. feature 実装ファイルを確認してください
4. feature 単体テストファイルを確認してください
5. `05_review_checklist.md` の観点に沿って feature 単体レビューを行ってください
6. 実装が `01_spec.md`、`02_design.md`、`03_flow.md` とズレていないか確認してください
7. 単体テストが `04_test_plan.md` とズレていないか確認してください
8. 必要に応じて `python -m pytest` または利用者が指定したテストコマンドを実行してください
9. レビュー結果を `<対象機能フォルダ>/06_review_result.md` に作成または上書き更新してください

## レビューで確認すること

- feature の仕様が明確で、実装に反映されていること
- feature の関数設計が実装と対応していること
- feature の呼び出し定義が実装と対応していること
- feature 単体テストが `04_test_plan.md` の観点を確認していること
- feature 単体テストが CLI、entrypoint、結合試験の詳細確認に広がりすぎていないこと
- feature 固有ロジックが `entrypoint.py` 側へ流出していないこと
- `src/common/` に勝手に共通化していないこと
- 仕様にない便利機能や余計な抽象化を追加していないこと
- 指定された出力先を AI 判断で変更していないこと
- `pytest` の import mismatch やテストファイル名衝突がある場合、勝手に別名ファイルを作成していないこと
- fallback import などのテスト都合の実装が feature の責務を曖昧にしていないこと

## レビュー結果に記録する内容

`06_review_result.md` には、以下を記録してください。

- レビュー対象
- 参照したファイル
- 実行した確認内容
- テスト実行結果
- 仕様との整合
- 関数設計との整合
- 呼び出し定義との整合
- テスト計画との整合
- feature 実装と feature 単体テストの確認結果
- entrypoint や結合試験との責務分担に関する気づき
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
- `要修正`: 実装または単体テストの修正が必要
- `要仕様確認`: 仕様に戻って確認が必要

command/app 全体の判定が必要な場合は、ここでは判定せず、`prompts/review_command.md` で確認する必要があることを記録してください。

## 仕様変更が必要そうな場合

レビュー中に、現在の仕様では判断できない点や、仕様変更が必要そうな点を見つけた場合は、実装やテストを勝手に修正しないでください。

`06_review_result.md` に、以下を記録してください。

- 仕様確認が必要だと判断した理由
- 影響を受ける要件
- 修正が必要そうなドキュメント
- 実装への影響
- テストへの影響

そのうえで、最終判定を `要仕様確認` としてください。

## 禁止事項

- レビュー依頼だけの場合、勝手に実装を変更しないでください
- レビュー依頼だけの場合、勝手にテストを変更しないでください
- `05_review_checklist.md` にレビュー結果を追記しないでください
- `06_review_result.md` 以外を出力先にしないでください
- 指定された出力先を AI 判断で変更しないでください
- `pytest` の import mismatch やテストファイル名衝突を理由に、勝手に別名のテストファイルを作成しないでください
- 共通モジュールを作成しないでください
- 仕様にない便利機能を追加しないでください
- 結合試験、外部API、CI/CD、デプロイ資産を追加しないでください
- command/app 全体レビューの最終判定を `06_review_result.md` だけで完結させないでください

## 作業後の報告

作業後に、以下を簡潔に報告してください。

- 作成または更新したファイル
- 参照したファイル
- テストを実行した場合、そのコマンドと結果
- 最終判定
- 主な指摘事項
- command/app 全体レビューに委ねる事項の有無
- 仕様確認が必要な点の有無
