# バグ修正を実装してください

このプロンプトは、人間が承認した `30_bug_fix_plan.md` に従って、バグ修正を実装するためのものです。

このプロンプトファイルは直接書き換えず、チャットでこのファイルのパスと下の「利用者が指定する項目」を指定して使います。
それ以外の作業ルールは変更せず、`AGENTS.md` と `docs/templates/` に従ってください。

---

## 利用者が指定する項目

- 対象 command/app: `<command_or_app_name>`
- 対象 feature: `<feature_name>`
- バグID: `<bug_id>`
- バグ修正計画書: `docs/<command_or_app_name>/bugs/<bug_id>/30_bug_fix_plan.md`（人間承認済みのもの）
- 補足条件: `必要に応じて書く。なければ「なし」`

## 参照するファイル

必ず現在の以下を読んでください。

- `AGENTS.md`
- `docs/<command_or_app_name>/bugs/<bug_id>/30_bug_fix_plan.md`（承認済みのもの）
- `docs/<command_or_app_name>/bugs/<bug_id>/10_bug_report.md`
- `docs/<command_or_app_name>/bugs/<bug_id>/20_bug_investigation.md`
- `docs/<command_or_app_name>/features/<feature_name>/20_spec.md`
- `docs/<command_or_app_name>/features/<feature_name>/21_design.md`
- `docs/<command_or_app_name>/features/<feature_name>/23_test_plan.md`
- 修正計画書の「修正対象ファイル」に記載されたファイル

## 変更してよいファイル

`30_bug_fix_plan.md` の「修正対象ファイル」に記載されたファイルのみ変更できます。

- 修正計画書に記載された実装ファイル
- 修正計画書に記載されたテストファイル

## 変更してはいけないファイル

- このプロンプトファイル
- `AGENTS.md`
- `README.md`
- `docs/templates/`
- `prompts/`
- `src/common/`
- `docs/<command_or_app_name>/features/` 配下の既存ドキュメント（仕様・設計・テスト計画は変更しない）
- `docs/<command_or_app_name>/bugs/<bug_id>/10_bug_report.md`
- `docs/<command_or_app_name>/bugs/<bug_id>/20_bug_investigation.md`
- `docs/<command_or_app_name>/bugs/<bug_id>/30_bug_fix_plan.md`（承認後は変更しない）
- `30_bug_fix_plan.md` の「修正対象ファイル」に記載されていないファイル
- `docs/<command_or_app_name>/tasks.md`（更新が必要な場合は作業報告に記載し、別作業で対応する）
- CI/CD、デプロイ関連のファイル

---

## 実装前の確認

1. `30_bug_fix_plan.md` の人間承認欄にすべてのチェックが入っていることを確認してください
2. 承認欄に未確認の項目がある場合は、実装を開始せずに STOP し、承認を求めてください
3. 修正計画書に記載された修正対象ファイルと変更してはいけないファイルを確認してください

## 作業範囲

1. 承認済みの `30_bug_fix_plan.md` を確認してください
2. 修正計画に記載された内容のみを実装してください
3. 修正計画に書かれていないついで修正やリファクタリングを行わないでください
4. 実装後に `python -m pytest` を実行し、テスト結果を確認してください
5. テストが通らない場合は修正計画の範囲内で対応し、範囲外の変更が必要な場合は STOP して報告してください
6. 既存の feature 仕様・設計・テスト計画とのズレがある場合は報告してください

## STOP すべき場合

以下のいずれかに該当する場合は、実装を中断して STOP し、報告してください。

- `30_bug_fix_plan.md` の人間承認欄に未確認の項目がある
- 修正を進めると仕様・設計・テスト計画の変更が必要だと判明した
- 修正計画の内容と実際の実装に想定外の矛盾がある
- テストが通らず、修正計画の範囲内では解決できない

## 禁止事項

- 承認なしに実装を開始しないでください
- 修正計画に書かれていない変更を行わないでください
- ついで修正やリファクタリングを行わないでください
- 仕様・設計・テスト計画（`docs/<command_or_app_name>/features/`）を勝手に変更しないでください
- `src/common/` を勝手に作成・更新しないでください
- 修正計画に記載されていない他のバグを「ついでに」修正しないでください
- バグ修正を仕様変更や機能追加と混同しないでください

## 作業後の報告

作業後に、以下を簡潔に報告してください。

- 変更したファイルと変更内容の要約
- テスト実行コマンド（`python -m pytest`）と結果
- 既存の feature 仕様・設計・テスト計画とのズレの有無
- 仕様・設計・テスト計画への反映が必要な別作業の有無
- 修正計画に書かれていない変更を行っていないことの確認

## レビュー補助メモ

作業後の報告に、レビュー補助メモを含めてください。
記載項目とルールは `AGENTS.md` の「レビュー補助メモ」に従います（このプロンプトには定義を複製しません）。

レビュー補助メモは作業完了報告（チャット）に出力します。`tasks.md` には書きません。

## 作業後の tasks.md 更新

このプロンプトでは `tasks.md` を変更しません。

`tasks.md` の更新が必要と判断した場合は、作業報告に「tasks.md 更新候補」として記載してください。
`tasks.md` の実際の更新は、人間が確認したうえで別作業として行います。
