# バグ修正計画書を作成または更新してください

このプロンプトは、`10_bug_report.md` と `20_bug_investigation.md` を読み、`docs/<command_or_app_name>/bugs/<bug_id>/30_bug_fix_plan.md` を作成または更新するためのものです。

このプロンプトファイルは直接書き換えず、チャットでこのファイルのパスと下の「利用者が指定する項目」を指定して使います。
それ以外の作業ルールは変更せず、`AGENTS.md` と `docs/templates/` に従ってください。

---

## 利用者が指定する項目

- 対象 command/app: `<command_or_app_name>`
- 対象 feature: `<feature_name>`
- バグID: `<bug_id>`
- バグ報告書: `docs/<command_or_app_name>/bugs/<bug_id>/10_bug_report.md`
- バグ調査書: `docs/<command_or_app_name>/bugs/<bug_id>/20_bug_investigation.md`
- バグ修正計画書の出力先: `docs/<command_or_app_name>/bugs/<bug_id>/30_bug_fix_plan.md`
- 対象機能フォルダ: `docs/<command_or_app_name>/features/<feature_name>/`
- 補足条件: `必要に応じて書く。なければ「なし」`

## 参照するファイル

必ず現在の以下を読んでください。

- `AGENTS.md`
- `docs/templates/30_bug_fix_plan_template.md`
- `docs/<command_or_app_name>/bugs/<bug_id>/10_bug_report.md`
- `docs/<command_or_app_name>/bugs/<bug_id>/20_bug_investigation.md`
- `docs/<command_or_app_name>/features/<feature_name>/20_spec.md`
- `docs/<command_or_app_name>/features/<feature_name>/21_design.md`
- `docs/<command_or_app_name>/features/<feature_name>/23_test_plan.md`

必要に応じて以下も参照してください。

- `docs/context/`（補助資料。確定仕様ではない。確認トリガーとしてのみ参照する）

## 変更してよいファイル

- `docs/<command_or_app_name>/bugs/<bug_id>/30_bug_fix_plan.md`（新規作成または更新）

## 変更してはいけないファイル

- このプロンプトファイル
- `AGENTS.md`
- `README.md`
- `docs/templates/`
- `prompts/`
- `src/`（実装コードは一切変更しない）
- `tests/`（テストコードは一切変更しない）
- `docs/<command_or_app_name>/features/` 配下の既存ドキュメント（仕様・設計・テスト計画は変更しない）
- `docs/<command_or_app_name>/bugs/<bug_id>/10_bug_report.md`
- `docs/<command_or_app_name>/bugs/<bug_id>/20_bug_investigation.md`
- `docs/context/`（補助資料として参照するだけにとどめ、変更しない）

---

## 作業前の確認

`20_bug_investigation.md` の「調査段階の判定」を確認してください。

- `調査完了` の場合のみ、修正計画の作成に進んでください
- `追加調査が必要` または `仕様確認待ち` の場合は、修正計画を作成せずに STOP し、理由を報告してください

また、修正計画が `docs/context/` の未決事項・却下案・保留事項・未反映の会議メモを前提にしていないかを、軽い確認トリガーとして確認してください。
`docs/context/` は確定仕様ではありません。`docs/context/` の横断探索を主責務にせず、context 量が増えても修正計画作成を完遂できるようにしてください。これらを前提にした修正が必要に見える場合は、修正計画を作成せずに STOP し、仕様変更候補または人間確認事項として報告してください。
`docs/context/` の横断的な深掘りが必要な場合は、このプロンプトでは行わず、`prompts/review_context.md` に委譲してください。

## 作業範囲

1. `10_bug_report.md` と `20_bug_investigation.md` を確認してください
2. 調査段階の判定が「調査完了」であることを確認してください
3. 関連する仕様、設計、テスト計画を確認してください
4. 修正方針を整理してください
5. 修正対象ファイルと変更してはいけないファイルを明記してください
6. 追加・更新するテストを明記してください
7. 実行する確認コマンドを明記してください
8. 仕様・設計・テスト計画への反映が必要な場合は、別作業として明記してください
9. `30_bug_fix_plan.md` を作成または更新してください
10. 人間承認欄のチェックが完了するまで、実装を開始しないでください

## 禁止事項

- この段階で実装コード（`src/`）を変更しないでください
- この段階でテストコード（`tests/`）を変更しないでください
- この段階で仕様・設計・テスト計画（`docs/<command_or_app_name>/features/`）を変更しないでください
- 修正計画にないリファクタリングや共通化の提案を修正計画に含めないでください
- 仕様通りに動いているが期待と違う場合は、バグではなく仕様変更候補として扱ってください（この場合は STOP し、報告してください）
- 調査段階の判定が「調査完了」でない場合に修正計画を作成しないでください

## 作業後の tasks.md 更新候補

このプロンプトでは `tasks.md` を直接更新しません。

`tasks.md` の更新が必要と判断した場合は、作業報告に「tasks.md 更新候補」として記載してください。
`tasks.md` の実際の更新は、人間が確認したうえで別作業として行います。

## 作業後の報告

作業後に、以下を簡潔に報告してください。

- 作成または更新したファイル
- 修正方針の要約
- 修正対象ファイルの一覧
- 別作業が必要な事項の有無
- 人間の承認待ちである旨（承認後に `prompts/implement_bug_fix.md` を使って実装する）
