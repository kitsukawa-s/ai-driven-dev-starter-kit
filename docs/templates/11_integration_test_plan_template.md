# <command_or_app_name> 結合試験計画

## 対象コマンド/アプリ

- コマンド/アプリ名: `<command_or_app_name>`
- short_name: `<short_name>`
- 入口ファイル: `src/<command_or_app_name>/entrypoint.py`
- 対象ドキュメント: `docs/<command_or_app_name>/10_overview.md`

`<short_name>` は、単一 feature の command/app では feature 名を使います。
複数 feature を束ねる command/app では、command/app を短く表す名前を使います。

## 結合試験の目的

この結合試験では、`entrypoint.py` から複数の feature を束ねて呼び出したときに、コマンド/アプリとして期待どおり動くことを確認します。

feature 単体の詳細なロジックは、各 feature の単体試験で確認します。

ここでは、以下を中心に確認します。

- entrypoint から feature を正しく呼び出せること
- CLI引数や入力が、適切な feature に渡ること
- feature の結果が、期待する出力形式で返ること
- エラー時に、コマンド/アプリとして期待する扱いになること
- `10_overview.md` に記載された担当範囲から外れていないこと

## 対象範囲

### 確認すること

- 

### 確認しないこと

- feature 内部の詳細ロジック
- 外部API連携
- CI/CD
- デプロイ
- 性能試験
- 負荷試験
- 運用監視

## 参照するドキュメント

- `docs/<command_or_app_name>/10_overview.md`

対象 feature:

| feature | 参照ドキュメント |
|---|---|
| `<feature_name>` | `docs/<command_or_app_name>/features/<feature_name>/20_spec.md` |

## 対象 feature 一覧

| feature | 役割 | 結合試験で確認する観点 |
|---|---|---|
| `<feature_name>` |  |  |

## entrypoint の確認観点

- CLI引数または入力を受け取れること
- 必要な feature を呼び出せること
- feature の結果を受け取れること
- 標準出力、終了コード、レスポンスなどに変換できること
- entrypoint に feature 固有ロジックを持ちすぎていないこと

## 正常系

| No | 観点 | 入力 / 実行例 | 期待結果 | 関連 feature |
|---|---|---|---|---|
| 1 |  |  |  |  |

## 異常系

| No | 観点 | 入力 / 実行例 | 期待結果 | 関連 feature |
|---|---|---|---|---|
| 1 |  |  |  |  |

## Boundary確認

### 10_overview.md との整合

- `10_overview.md` の「担当すること」に含まれる範囲であること
- `10_overview.md` の「担当しないこと」に含まれる処理を試験対象にしていないこと
- feature 分割方針と矛盾していないこと

### entrypoint と features の責務分担

- entrypoint が厚くなりすぎていないこと
- feature 固有処理が features 配下に閉じていること
- common へ勝手に共通化されていないこと

## テスト実行方針

- pytest を使って確認する
- 必要に応じて subprocess で entrypoint を実行する
- 外部APIや外部システムには接続しない
- 実ファイル操作が必要な場合は、一時ディレクトリを使う
- テスト対象は、コマンド/アプリ単位の結合確認に限定する

## 作成するテストファイル候補

- `tests/<command_or_app_name>/test_entrypoint_<short_name>.py`
- `tests/<command_or_app_name>/test_integration_<short_name>.py`

## 今回やらないこと

- 

## 未決事項

| 項目 | 内容 | 判断が必要な理由 |
|---|---|---|
|  |  |  |

## レビュー観点

- `10_overview.md` と矛盾していないこと
- entrypoint から feature を呼び出す流れを確認できること
- feature 単体試験と重複しすぎていないこと
- 結合試験の範囲が広がりすぎていないこと
- 外部依存を勝手に増やしていないこと
- CI/CDやデプロイ資産を追加していないこと

## 補足

該当なし
