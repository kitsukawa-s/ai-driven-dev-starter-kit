# 関数設計

## 対象機能

cli_hello_greeting / greeting

## 前提

- Python標準ライブラリのみを使う
- CLI引数解析には `argparse` を使う
- CLI処理とあいさつ文生成ロジックを分ける

## 関数一覧

| 関数名 | 役割 |
|---|---|
| `create_greeting` | 名前からあいさつ文を作る |

## 関数詳細

### `create_greeting(name: str) -> str`

- 役割: 名前から `Hello, <name>!` 形式の文字列を作る
- 入力: `name`
- 出力: あいさつ文の文字列
- エラー扱い: 空文字、空白のみの文字列は `ValueError`
- 実装時の注意点: 標準出力には出さず、文字列を返すだけにする

## エラー処理方針

- 空文字、空白のみは `create_greeting` で `ValueError` にする
- CLI引数のエラーは `entrypoint.py` の `argparse` に任せる
- `entrypoint.py` ではエラーを握りつぶさない

## 共通化候補

現時点では共通化しません。

- 候補となる処理: CLI引数解析や文字列の空チェック
- 想定される共通化先: `src/common/`
- 共通化を検討する理由: 今後、複数機能で同じ処理が必要になる可能性があるため
- 影響を受ける機能: `cli_hello_greeting / greeting`、将来追加されるCLI機能
- 現時点で共通化すべきかどうか: 候補として記録するが、今回は共通化しない

## 実装時の注意点

- 初学者が読めるシンプルな関数構成にする
- 外部ライブラリは使わない
- クラスは使わず、関数中心で実装する
- `src/common/` へ勝手に切り出さない
- CLI引数解析と標準出力は `src/cli_hello_greeting/entrypoint.py` に置く
- 機能ロジックは `src/cli_hello_greeting/features/greeting.py` に置く

## 今回やらないこと

- 多言語対応
- 設定ファイル対応
- GUI対応
- 外部API連携
- 結合試験
- CI/CD

## レビュー観点

- 仕様を満たせる関数構成であること
- CLI処理とロジック処理が分かれていること
- エラー扱いが明確であること
- 共通化候補が提案にとどまっていること

## 補足

該当なし
