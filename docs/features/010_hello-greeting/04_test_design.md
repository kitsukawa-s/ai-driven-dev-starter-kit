# テスト設計

## 対象機能

010_hello-greeting

## テスト対象

- `create_greeting`
- `main`

## テスト方針

- 単体試験までを対象にする
- ロジック関数 `create_greeting` の確認を優先する
- CLI相当の確認として `main` に引数リストを渡して確認する
- 外部API、結合試験、CI/CD、デプロイは対象外にする

## テスト観点一覧

| 区分 | 観点 |
|---|---|
| 正常系 | 英字名であいさつ文を生成できる |
| 正常系 | 日本語名であいさつ文を生成できる |
| 異常系 | 空文字は `ValueError` |
| 異常系 | 空白のみは `ValueError` |
| CLI | `main(["--name", "Alice"])` が出力して `0` を返す |
| CLI | `main([])` は `SystemExit` |

## 正常系

- `create_greeting("Alice")` が `"Hello, Alice!"` を返す
- 日本語名でも同じ形式のあいさつ文を返す
- `main(["--name", "Alice"])` が `0` を返し、標準出力に `Hello, Alice!` を出す

## 異常系

- `create_greeting("")` は `ValueError`
- `create_greeting("   ")` は `ValueError`
- `main([])` は `argparse` により `SystemExit`

## CLI実行時の確認観点

- CLI引数 `--name` で名前を指定できること
- 標準出力に期待する文字列が出ること
- 未指定時はCLI引数エラーになること

## 今回テストしないこと

- 結合試験
- 外部API連携
- CI/CD
- デプロイ
- 実際のシェルからの起動確認

## レビュー観点

- 必須要件を確認できるテストになっていること
- 正常系と異常系が含まれていること
- 実装の詳細に寄りすぎていないこと
- 単体試験の範囲に収まっていること

## 補足

`argparse` の詳細なメッセージ内容は、今回のテスト対象外とします。
