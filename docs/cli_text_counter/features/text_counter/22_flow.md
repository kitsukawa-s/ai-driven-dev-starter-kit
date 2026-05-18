# 関数呼び出し定義

## 対象機能

- command/app: `cli_text_counter`
- feature: `text_counter`
- 関数名候補: `count_characters`

入力文字列の文字数を数え、整数として返す feature を対象とします。

## 処理の入口

- CLI実行時の入口: `src/cli_text_counter/entrypoint.py`
- feature 関数: `src/cli_text_counter/features/text_counter.py` の `count_characters(text)`

今回は呼び出し定義ドキュメントのみを作成し、`src/` 配下の実装ファイルは作成しません。

## CLI実行時の呼び出し流れ

1. `entrypoint.py` が CLI引数で入力文字列を受け取る
2. `entrypoint.py` が `features/text_counter.py` の `count_characters(text)` を呼び出す
3. `count_characters(text)` が Python の `len()` 相当で文字数を数える
4. `count_characters(text)` が文字数を整数として返す
5. `entrypoint.py` が返された整数を標準出力へ表示する
6. `entrypoint.py` が終了コードを返す

## 呼び出し関係

```text
CLI引数
  -> src/cli_text_counter/entrypoint.py
      -> src/cli_text_counter/features/text_counter.py
          -> count_characters(text)
              -> int
      -> 標準出力へ表示
      -> 終了コードを返す
```

## 責務の分担

| 関数名 | 責務 |
|---|---|
| `entrypoint.py` | CLI引数を受け取り、feature を呼び出し、結果を標準出力へ表示し、終了コードを返す |
| `count_characters` | 入力文字列の文字数を数え、整数として返す |

## エラー時の流れ

- CLI引数が不足している場合は、`entrypoint.py` 側で `argparse` の引数エラーとして扱う
- 空文字列が指定された場合はエラーにせず、`count_characters(text)` が `0` を返す
- feature には標準出力やCLI引数解析を持たせない
- feature 内では、仕様にない入力補正や追加チェックを勝手に行わない

## 実装時の注意点

- 関数設計と矛盾しないようにする
- CLI処理とロジック処理の責務を混ぜない
- 仕様にない処理を追加しない
- 文字数は Python の `len()` 相当で数える
- `count_characters` は整数を返し、標準出力には直接書き込まない
- entrypoint 実装中に feature が呼び出しにくい場合でも、勝手に feature 設計を変更しない

## レビュー観点

- 関数設計と呼び出し定義に矛盾がないこと
- 処理の流れが追いやすいこと
- エラー時の流れが明確であること
- 不要に複雑な呼び出し構成になっていないこと
- feature に標準出力やCLI引数解析の責務が混ざっていないこと
- 空文字列を正常系として扱う流れになっていること

## 補足

今回は関数呼び出し定義ドキュメントのみを作成します。
