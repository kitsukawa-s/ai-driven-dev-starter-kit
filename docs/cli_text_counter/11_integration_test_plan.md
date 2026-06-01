# cli_text_counter 結合試験計画

## 対象コマンド/アプリ

- コマンド/アプリ名: `cli_text_counter`
- short_name: `text_counter`
- 入口ファイル: `src/cli_text_counter/entrypoint.py`
- 対象ドキュメント: `docs/cli_text_counter/10_overview.md`

`text_counter` は単一 feature の command/app であるため、short_name は feature 名を使います。

## 結合試験の目的

この結合試験では、`entrypoint.py` から `text_counter` feature を呼び出したときに、コマンド/アプリとして期待どおり動くことを確認します。

feature 単体の詳細なロジックは、`text_counter` feature の単体試験で確認します。

ここでは、以下を中心に確認します。

- entrypoint から feature を正しく呼び出せること
- CLI引数で受け取った文字列が feature に渡ること
- feature の結果が標準出力へ反映されること
- 正常時に終了コード `0` になること
- エラー時に、コマンド/アプリとして期待する扱いになること
- `10_overview.md` に記載された担当範囲から外れていないこと

## 対象範囲

### 確認すること

- `entrypoint.py` が `--text` で入力文字列を受け取れること
- `entrypoint.py` が `count_characters(text)` を呼び出せること
- 文字数が標準出力に表示されること
- 正常時に終了コード `0` になること
- `--text` が不足した場合に `argparse` のエラーとして正常終了しないこと

### 確認しないこと

- feature 内部の詳細ロジック
- 単語数のカウント
- 行数のカウント
- ファイル入力
- 対話式入力
- 外部API連携
- CI/CD
- デプロイ
- 性能試験
- 負荷試験
- 運用監視

## 参照するドキュメント

- `docs/cli_text_counter/10_overview.md`

対象 feature:

| feature | 参照ドキュメント |
|---|---|
| `text_counter` | `docs/cli_text_counter/features/text_counter/20_spec.md` |

## 対象 feature 一覧

| feature | 役割 | 結合試験で確認する観点 |
|---|---|---|
| `text_counter` | 入力文字列の文字数を数え、整数として返す | CLI引数で受け取った文字列が feature に渡り、結果が標準出力へ表示されること |

## entrypoint の確認観点

- CLI引数 `--text` を受け取れること
- `count_characters(text)` を呼び出せること
- feature の戻り値を受け取れること
- 戻り値を標準出力へ表示できること
- 正常時に終了コード `0` を返せること
- entrypoint に feature 固有ロジックを持ちすぎていないこと

## 正常系

| No | 観点 | 入力 / 実行例 | 期待結果 | 関連 feature |
|---|---|---|---|---|
| 1 | 英数字の文字列をCLIから処理できる | `python src/cli_text_counter/entrypoint.py --text hello` | 標準出力に `5` が表示され、終了コード `0` になる | `text_counter` |
| 2 | 空文字列をCLIから処理できる | `python src/cli_text_counter/entrypoint.py --text=` | 標準出力に `0` が表示され、終了コード `0` になる | `text_counter` |
| 3 | 日本語文字列をCLIから処理できる | `python src/cli_text_counter/entrypoint.py --text こんにちは` | 標準出力に Python の `len("こんにちは")` 相当の文字数が表示され、終了コード `0` になる | `text_counter` |

> **注意（No.2）:** 空文字列の CLI 実行例は `--text=` を推奨します。`--text ""` は shell によって空文字列の扱いが異なる可能性があります。argv を直接渡す既存のテストコードは引き続き有効です。

## 異常系

| No | 観点 | 入力 / 実行例 | 期待結果 | 関連 feature |
|---|---|---|---|---|
| 1 | 必須引数が不足している | `python src/cli_text_counter/entrypoint.py` | `argparse` のエラーとして正常終了しない | `text_counter` |

## Boundary確認

### 10_overview.md との整合

- `10_overview.md` の「CLI引数で入力文字列を受け取る」に含まれる範囲であること
- `10_overview.md` の「文字数を標準出力へ表示する」に含まれる範囲であること
- `10_overview.md` の「担当しないこと」に含まれる単語数、行数、ファイル入力、対話式入力を試験対象にしていないこと
- feature 分割方針と矛盾していないこと

### entrypoint と features の責務分担

- entrypoint がCLI引数、feature 呼び出し、標準出力、終了コードだけを担当していること
- 文字数算出処理が `text_counter` feature に閉じていること
- `src/common/` へ勝手に共通化されていないこと

## テスト実行方針

- pytest を使って確認する
- 必要に応じて標準ライブラリの `subprocess` で entrypoint を実行する
- 外部APIや外部システムには接続しない
- 実ファイル操作は行わない
- テスト対象は、コマンド/アプリ単位の結合確認に限定する

## 作成するテストファイル候補

- `tests/cli_text_counter/test_integration_text_counter.py`

## 今回やらないこと

- 結合試験コードの作成
- feature 単体の詳細ロジックの再確認
- entrypoint テストと同じ観点の過剰な重複
- 単語数のカウント
- 行数のカウント
- ファイル入力
- 対話式入力
- 外部API連携
- CI/CD
- デプロイ

## 未決事項

| 項目 | 内容 | 判断が必要な理由 |
|---|---|---|
| 該当なし | 現時点では結合試験計画作成に必要な情報は揃っている | 該当なし |

## レビュー観点

- `10_overview.md` と矛盾していないこと
- entrypoint から feature を呼び出す流れを確認できること
- feature 単体試験と重複しすぎていないこと
- entrypoint テストと重複しすぎていないこと
- 結合試験の範囲が広がりすぎていないこと
- 外部依存を勝手に増やしていないこと
- CI/CDやデプロイ資産を追加していないこと

## 補足

今回は結合試験計画のみを作成します。
