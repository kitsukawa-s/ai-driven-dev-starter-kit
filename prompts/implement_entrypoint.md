# entrypoint を実装してテストを作成してください

あなたは、このリポジトリのAI駆動開発ルールに従う開発補助者です。

このプロンプトは、コマンド/アプリ単位の `entrypoint.py` と、そのテストを作成または更新するためのものです。

`entrypoint.py` は、外部から呼ばれる入口です。  
feature 固有のロジックは `features/` 配下に置き、`entrypoint.py` は薄く保ってください。

このプロンプトファイルは直接書き換えず、チャットでこのファイルのパスと「利用者が指定する項目」を指定して使います。

## 利用者が指定する項目

利用者は、チャットで以下を指定します。

- コマンド/アプリ名: `<command_or_app_name>`
- 対象 overview: `docs/<command_or_app_name>/overview.md`
- 対象 entrypoint: `src/<command_or_app_name>/entrypoint.py`
- 作成または更新するテストファイル: `tests/<command_or_app_name>/test_entrypoint.py`
- 対象 feature: `必要に応じて feature 名を書く。全体対象の場合は「overview.md の機能一覧に従う」`
- 補足条件: `必要に応じて書く。なければ「なし」`

## 参照するファイル

- `AGENTS.md`
- `docs/<command_or_app_name>/overview.md`

必要に応じて、以下も参照してください。

- `docs/<command_or_app_name>/features/<feature_name>/01_spec.md`
- `docs/<command_or_app_name>/features/<feature_name>/02_design.md`
- `docs/<command_or_app_name>/features/<feature_name>/03_flow.md`
- `docs/<command_or_app_name>/features/<feature_name>/04_test_plan.md`
- `docs/<command_or_app_name>/features/<feature_name>/05_review_checklist.md`
- `src/<command_or_app_name>/features/<feature_name>.py`
- `tests/<command_or_app_name>/features/test_<feature_name>.py`

## 作成または更新するファイル

- `src/<command_or_app_name>/entrypoint.py`
- `tests/<command_or_app_name>/test_entrypoint.py`

## 変更してよいファイル

- `src/<command_or_app_name>/entrypoint.py`
- `tests/<command_or_app_name>/test_entrypoint.py`

## 変更してはいけないファイル

明示指示がない限り、以下は変更しないでください。

- このプロンプトファイル
- `AGENTS.md`
- `README.md`
- `docs/overview.md`
- `docs/how_to_use_prompts.md`
- `docs/templates/`
- `docs/<command_or_app_name>/overview.md`
- `docs/<command_or_app_name>/10_integration_test_plan.md`
- `docs/<command_or_app_name>/features/`
- `src/<command_or_app_name>/features/`
- `src/common/`
- `tests/<command_or_app_name>/features/`
- `prompts/`
- 他のコマンド/アプリ配下
- CI/CD、デプロイ関連のファイル

## 作業範囲

1. `AGENTS.md` を確認してください
2. `docs/<command_or_app_name>/overview.md` を確認してください
3. 必要に応じて対象 feature の仕様、設計、呼び出し定義、テスト計画を確認してください
4. `entrypoint.py` が担当すべき責務を整理してください
5. feature 固有のロジックが `entrypoint.py` に入らないようにしてください
6. `src/<command_or_app_name>/entrypoint.py` を作成または更新してください
7. `tests/<command_or_app_name>/test_entrypoint.py` を作成または更新してください
8. 実装後、可能であれば `python -m pytest` を実行してください
9. `python -m pytest` が環境理由で失敗する場合は、利用可能な Python 実体で代替実行してください
10. 実行したコマンドと結果を正確に報告してください

## entrypoint の実装方針

`entrypoint.py` は、CLI入口として薄くしてください。

entrypoint が担当すること:

- CLI引数を受け取る
- 必要な feature を呼び出す
- feature の結果を受け取る
- 結果を標準出力に出す
- 終了コードを返す

entrypoint に入れてはいけないこと:

- feature 固有の業務ロジック
- 複雑な変換処理
- feature 内部で判断すべき条件分岐
- 共通化候補の実装
- 仕様にない便利機能
- 外部API連携
- CI/CD やデプロイに関する処理

## feature との分担

feature 固有の処理は、以下に置きます。

- `src/<command_or_app_name>/features/<feature_name>.py`

entrypoint は、その feature を呼び出すだけにしてください。

feature 側が未実装、または設計と矛盾している場合は、勝手に feature 実装を変更しないでください。

その場合は、entrypoint 実装を止め、確認事項として報告してください。

## テスト実装の方針

`test_entrypoint.py` では、entrypoint の責務を確認してください。

確認すること:

- CLI引数または入力を受け取れること
- 対象 feature を呼び出せること
- feature の結果が標準出力に反映されること
- 正常終了時に期待する終了コードを返すこと
- 引数不足や不正入力時に期待する扱いになること

feature 内部の詳細ロジックを、`test_entrypoint.py` で過剰に確認しないでください。

feature 内部の詳細は、以下で確認します。

- `docs/<command_or_app_name>/features/<feature_name>/04_test_plan.md`
- `tests/<command_or_app_name>/features/test_<feature_name>.py`

## テスト実装の注意点

- `pytest` を使ってください
- 標準出力の確認が必要な場合は、`capsys` を使ってください
- サブプロセス実行が必要な場合は、標準ライブラリの `subprocess` を使ってください
- 外部APIや外部システムには接続しないでください
- 実ファイル操作が必要な場合は、`tmp_path` などの一時領域を使ってください
- 実行環境に依存しすぎるテストは避けてください
- テストを通すために feature 実装や `src/common/` を勝手に変更しないでください

## 情報不足時のルール

entrypoint を実装するには情報が不足している場合は、いきなり `entrypoint.py` や `test_entrypoint.py` を作成または更新しないでください。

先に「確認事項」として、不足している情報を箇条書きで提示してください。

特に以下が不明な場合は、確認を優先してください。

- コマンド/アプリとしての入力
- コマンド/アプリとしての出力
- 呼び出す feature
- feature に渡す値
- feature から受け取る値
- 標準出力の形式
- 終了コード
- エラー時の扱い
- `overview.md` の Boundary

ただし、`overview.md`、対象 feature の `01_spec.md`、`03_flow.md`、実装ファイルから明確に読み取れる場合は、それをもとに整理して構いません。

## entrypoint が作りにくい場合

entrypoint 実装中に、feature 実装や設計が entrypoint から呼び出しにくい構造だと判断した場合でも、勝手に `src/<command_or_app_name>/features/` を変更しないでください。

その場合は、以下を作業報告に記載してください。

- entrypoint が作りにくい理由
- 影響する feature
- 影響するファイル
- 見直し候補
- 実装側の変更が必要そうか

実装側の変更が必要かどうかは、人間レビューで判断します。

## 禁止事項

- 情報不足のまま `entrypoint.py` や `test_entrypoint.py` を作成しないでください
- `overview.md` と矛盾する entrypoint を作成しないでください
- feature の仕様や設計と矛盾する entrypoint を作成しないでください
- feature 固有ロジックを `entrypoint.py` に入れないでください
- テストを通すために feature 実装を変更しないでください
- `src/<command_or_app_name>/features/` を変更しないでください
- `src/common/` を作成・更新しないでください
- `docs/` を変更しないでください
- `AGENTS.md` を変更しないでください
- `prompts/` を変更しないでください
- CI/CD、デプロイ資産を追加しないでください
- 外部APIや外部システムへ接続する処理を追加しないでください
- 仕様にない便利機能を追加しないでください

## 作業後の報告

作業後は、以下を簡潔に報告してください。

- 作成または更新したファイル
- 参照したファイル
- 実装した entrypoint の概要
- 対象 feature
- 主な正常系
- 主な異常系
- `overview.md` との整合確認結果
- 対象 feature の `03_flow.md` との整合確認結果
- テストを実行した場合、そのコマンドと結果
- テストを実行できなかった場合、その理由
- 確認事項を提示した場合、その理由
- 仮定を置いた場合、その内容
- entrypoint が作りにくい点があった場合、その内容