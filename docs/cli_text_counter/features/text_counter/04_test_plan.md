# テスト設計

## 対象機能

- command/app: `cli_text_counter`
- feature: `text_counter`
- 関数名候補: `count_characters`

入力文字列の文字数を数え、整数として返す feature を対象とします。

## テスト対象

- テスト対象関数: `count_characters(text: str) -> int`
- 想定テストファイル: `tests/cli_text_counter/features/test_text_counter.py`

今回はテスト計画ドキュメントのみを作成し、`tests/` 配下のテストファイルは作成しません。

## テスト方針

- feature 単体試験までを対象にする
- `count_characters(text: str) -> int` の関数単位のテストを優先する
- 文字数は Python の `len()` 相当で数える前提にする
- 空文字列は正常系として扱い、`0` を返すことを確認する
- 日本語などのマルチバイト文字も、Python の `len()` 相当の文字数として扱う
- CLI引数解析、標準出力、終了コード、`argparse` のエラーは feature 単体テストでは扱わない
- 外部ライブラリは使わない前提にする

## テスト観点一覧

| 区分 | 観点 |
|---|---|
| 正常系 | 英数字の文字列を渡すと文字数を整数で返す |
| 正常系 | 空文字列を渡すと `0` を返す |
| 正常系 | 日本語などのマルチバイト文字を Python の `len()` 相当で数える |
| 異常系 | feature 単体ではCLI引数不足や `argparse` エラーを扱わない |
| CLI | feature 単体テストではCLI実行時の確認を扱わない |

## 正常系

- `count_characters("hello")` が `5` を返すこと
- `count_characters("")` が `0` を返すこと
- `count_characters("こんにちは")` が Python の `len("こんにちは")` と同じ値を返すこと
- `count_characters("hello world")` が空白を含めた Python の `len("hello world")` と同じ値を返すこと

## 異常系

- CLI引数が不足している場合のエラーは、feature 単体テストでは扱わない
- `argparse` の型変換や引数エラーは、feature 単体テストでは扱わない
- 仕様にない入力補正や追加チェックのテストは行わない

## CLI実行時の確認観点

- 今回は対象外
- CLI引数解析、標準出力、終了コードは、後続の entrypoint テストまたは結合試験で扱う

## 今回テストしないこと

- `src/` 配下の実装
- `tests/` 配下の作成
- CLI引数解析
- 標準出力への表示
- 終了コード
- `argparse` のエラー
- 単語数のカウント
- 行数のカウント
- ファイル入力
- 対話式入力
- 結合試験
- 外部API連携
- CI/CD
- デプロイ

## レビュー観点

- 仕様の必須要件を確認できること
- 正常系だけに偏っていないこと
- 異常系が最低限含まれていること
- 実装の詳細に寄りすぎていないこと
- 単体試験の範囲に収まっていること
- CLI処理と feature 単体のテスト範囲が混ざっていないこと
- 空文字列とマルチバイト文字の観点が含まれていること

## 補足

共通化候補はありません。
共通化が必要になった場合も、`src/common/` へ勝手に切り出さず、提案に留めます。
