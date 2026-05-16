# テスト設計

## 対象機能

cli_hello_greeting / greeting

## テスト対象

- `create_greeting`

## テスト方針

- feature 単体テストを対象にする
- ロジック関数 `create_greeting` の正常系と異常系を確認する
- CLI引数解析、標準出力、終了コードはこのテスト計画の対象外にする
- 外部API、結合試験、CI/CD、デプロイは対象外にする

## テスト観点一覧

| 区分 | 観点 |
|---|---|
| 正常系 | 英字名であいさつ文を生成できる |
| 正常系 | 日本語名であいさつ文を生成できる |
| 異常系 | 空文字は `ValueError` |
| 異常系 | 空白のみは `ValueError` |

## 正常系

- `create_greeting("Alice")` が `"Hello, Alice!"` を返す
- `create_greeting("太郎")` が `"Hello, 太郎!"` を返す

## 異常系

- `create_greeting("")` は `ValueError`
- `create_greeting("   ")` は `ValueError`

## CLI実行時の確認観点

今回は対象外です。

entrypoint の確認は `tests/cli_hello_greeting/test_entrypoint_greeting.py` で扱います。
command/app 単位の結合試験は `docs/cli_hello_greeting/10_integration_test_plan.md` と `tests/cli_hello_greeting/test_integration_greeting.py` で扱います。

## 今回テストしないこと

- `entrypoint.parse_args`
- `entrypoint.main`
- CLI引数解析
- 標準出力
- 終了コード
- 結合試験
- 外部API連携
- CI/CD
- デプロイ
- 実際のシェルからの起動確認

## レビュー観点

- 必須要件を feature 単体テストで確認できること
- 正常系と異常系が含まれていること
- 実装の詳細に寄りすぎていないこと
- entrypoint テストや結合試験の観点と混ざっていないこと

## 補足

`argparse` の詳細なメッセージ内容は、今回のテスト対象外とします。
