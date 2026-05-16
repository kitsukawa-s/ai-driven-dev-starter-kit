# cli_simple_calculator overview

## コマンド/アプリの目的

`cli_simple_calculator` は、2つの整数を受け取り、足し算の結果を標準出力へ表示するCLIとして設計する体験用コマンドです。

## 入口ファイル

- `src/cli_simple_calculator/entrypoint.py`

現時点では仕様書のみを用意しており、実装ファイルはまだ作成していません。

## 機能一覧

| 機能 | 概要 | ドキュメント |
|---|---|---|
| `calculator` | 2つの整数を足し算する | `docs/cli_simple_calculator/features/calculator/` |

## このコマンド/アプリが担当すること

- CLI引数 `--a` と `--b` を受け取る
- `calculator` 機能を呼び出す
- 足し算の結果を標準出力へ表示する

## 担当しないこと

- 引き算、掛け算、割り算
- 小数対応
- 複雑な入力チェック
- GUI対応
- 外部API連携
- 結合試験、CI/CD、デプロイ

## entrypoint の責務

- CLI引数を受け取る
- `features/calculator.py` の機能を呼び出す
- 結果を標準出力に出す
- 正常終了時に終了コードを返す

## features 配下の責務

- 足し算の機能固有ロジックを実装する
- 標準出力やCLI引数解析を持たない
- 仕様にない演算を追加しない

## common の扱い

`src/common/` は共通処理置き場ですが、人間の明示指示なしに作成・更新しません。
共通化候補がある場合は、設計書やレビュー結果、作業報告に提案として記録します。

## 変更時の注意点

- `entrypoint.py` を厚くしない
- 業務ロジックは `features/` 配下に置く
- 仕様にない便利機能を追加しない
- `src/common/` へ勝手に共通処理を切り出さない
- 対応するテストは `tests/cli_simple_calculator/` 配下に置く
