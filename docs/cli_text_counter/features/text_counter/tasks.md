# text_counter tasks

## 目的

`text_counter` 機能の作業状態を、人間とAIが引き継ぎやすくするためのメモです。

このファイルは作業中の現在地を示すために使います。
仕様、設計、テスト計画、レビュー結果の代わりにはしません。

## 現在の状態

- command/app: `cli_text_counter`
- feature: `text_counter`
- 関数名候補: `count_characters`
- 状態: feature 単体レビューを完了済み
- 最終更新: 2026-05-17

## 作業メモ

- [x] feature 用の `tasks.md` を `text_counter` 配下に配置する
- [x] `20_spec.md` を作成する
- [x] `count_characters` は feature 名ではなく、実装時の関数名候補として扱う
- [x] 空文字列と文字数の数え方を `20_spec.md` に反映する
- [x] `21_design.md` を作成する
- [x] `22_flow.md` を作成する
- [x] `23_test_plan.md` を作成する
- [x] `24_review_checklist.md` を作成する
- [x] feature 本体を作成する
- [x] feature 単体テストを作成する
- [x] feature 単体テストの結果を確認する
- [x] feature 単体レビューを行う

## 次に確認すること

- command/app 全体レビューを行う

## 注意点

- `tasks.md` には現在の作業状態と次の一手だけを短く書きます。
- 仕様の詳細は `20_spec.md` に書きます。
- レビュー結果は `25_review_result.md` に記録します。
