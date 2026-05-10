# 関数呼び出し定義

## 対象機能

010_hello-greeting

## 処理の入口

- CLI実行時の入口は `if __name__ == "__main__":`
- 実際の制御は `main()` が行う

## CLI実行時の呼び出し流れ

1. `raise SystemExit(main())` で `main` を呼び出す
2. `main` が `parse_args` を呼び出す
3. `parse_args` が `--name` を解析する
4. `main` が `create_greeting` を呼び出す
5. `create_greeting` があいさつ文を返す
6. `main` が標準出力に表示する
7. `main` が `0` を返す

## 呼び出し関係

```text
CLI
  -> main
    -> parse_args
    -> create_greeting
```

## 責務の分担

| 関数名 | 責務 |
|---|---|
| `parse_args` | CLI引数の解析 |
| `create_greeting` | あいさつ文の生成 |
| `main` | 全体制御と標準出力 |

## エラー時の流れ

- `--name` 未指定の場合、`parse_args` 内の `argparse` が `SystemExit` を発生させる
- 空文字、空白のみの場合、`create_greeting` が `ValueError` を発生させる
- `main` はこれらのエラーを握りつぶさない

## 実装時の注意点

- `create_greeting` は標準出力を行わない
- `parse_args` はあいさつ文を作らない
- `main` は正常終了時に `0` を返す

## レビュー観点

- 関数設計と呼び出し定義に矛盾がないこと
- CLI処理とロジック処理が混ざっていないこと
- エラー時の流れが明確であること
- 仕様にない処理が追加されていないこと

## 補足

該当なし
