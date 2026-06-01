# cli_text_counter 概要

## 目的

`cli_text_counter` は、入力文字列を受け取り、文字数を返すシンプルなCLIです。

## 背景

AI駆動開発スターターキットで、新しい command/app の初期ドキュメント配置を小さく確認するために作成します。

## 想定する利用者

- AI駆動開発スターターキットの学習者
- 小さなCLI機能の仕様作成から段階的に試したい人

## 実行単位

- コマンド/アプリ名: `cli_text_counter`
- 種別: `cli`
- 入口ファイル: `src/cli_text_counter/entrypoint.py`

## 実行イメージ

```bash
python src/cli_text_counter/entrypoint.py --text "hello"
```

空文字列を渡す場合は `--text=` を使用してください。

```bash
python src/cli_text_counter/entrypoint.py --text=
```

> **注意:** `--text ""` は shell によって空文字列の扱いが異なる可能性があります。空文字列を渡す場合は `--text=` を推奨します。

## このコマンド/アプリが担当すること

- CLI引数で入力文字列を受け取る
- `text_counter` 機能を呼び出す
- 文字数を標準出力へ表示する

## このコマンド/アプリが担当しないこと

- 単語数のカウント
- 行数のカウント
- ファイル入力
- 対話式入力
- GUI対応
- 外部API連携

## Boundary

### 入力境界

- CLI引数で受け取る文字列

### 出力境界

- 入力文字列の文字数を表す整数

### 外部依存

- 外部API、DB、環境変数、外部ファイルへの依存はありません。

### 変更してよい範囲

- `docs/cli_text_counter/`
- `src/cli_text_counter/`
- `tests/cli_text_counter/`

### 原則として変更しない範囲

- `AGENTS.md`
- `prompts/`
- `docs/templates/`
- `src/common/`
- 他のコマンド/アプリ配下

## 機能一覧

| feature | 役割 | ドキュメント | 状態 |
|---|---|---|---|
| `text_counter` | 入力文字列の文字数を数える | `docs/cli_text_counter/features/text_counter/` | 実装・テスト・レビュー済み |

## feature 分割方針

入力文字列に対して文字数を返す責務を、1つの feature として `text_counter` にまとめます。

関数名候補の `count_characters` は、feature 名ではなく、実装時の関数名として扱います。

## entrypoint の責務

- CLI引数を受け取る
- `features/text_counter.py` の機能を呼び出す
- 結果を標準出力に出す
- 終了コードを返す

## entrypoint に入れないこと

- 文字数カウントのロジック本体
- 複雑な変換処理
- feature 固有の判断
- 共通化候補の実装
- 仕様にない便利機能

## features 配下の責務

- 入力文字列の文字数を数える feature 固有ロジックを持つ
- 文字数を整数として返す
- CLI引数解析や標準出力を持たない
- 単体試験しやすい小さな関数として実装する

## common の扱い

`src/common/` は共通処理置き場ですが、人間の明示指示なしに作成・更新しません。

今回の範囲では共通化候補はありません。

## 未決事項

| 項目 | 内容 | 判断が必要な理由 |
|---|---|---|
| 該当なし | 空文字列は許可し、文字数は Python の `len()` 相当で数える方針に整理済み | `20_spec.md` に反映済み |

## 仕様変更時の扱い

実装中に仕様変更が必要だと判断した場合は、実装で勝手に吸収せず、対象 feature の `20_spec.md` に戻って見直します。

## 変更時の注意点

- `entrypoint.py` を厚くしない
- feature の責務を曖昧にしない
- `src/common/` へ勝手に共通化しない
- 他のコマンド/アプリ配下を変更しない
- 仕様にない便利機能を追加しない

## 補足

`text_counter` feature の実装・単体テスト・単体レビュー・結合試験・command/app 全体レビューがすべて完了しています。
詳細は各ドキュメントを参照してください。
