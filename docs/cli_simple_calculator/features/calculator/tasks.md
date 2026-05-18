# calculator tasks

## 目的

`cli_simple_calculator` / `calculator` feature の作業状態を、人間とAIが引き継ぎやすくするためのメモです。

このファイルは作業中の現在地を示すために使います。
仕様、設計、テスト計画、レビュー結果の代わりにはしません。

## 現在の状態

- command/app: `cli_simple_calculator`
- feature: `calculator`
- 関数名候補: `add_numbers`
- 状態: 01_spec.md 作成済み。次は 02_design.md を作成する
- 最終更新: 2026-05-18

## 作業メモ

- [x] feature 用の `tasks.md` を `calculator` 配下に配置済み
- [x] `docs/cli_simple_calculator/features/calculator/01_spec.md` を配置済み
- [x] `add_numbers` は feature 名ではなく、実装時の関数名候補として扱う
- [ ] `docs/cli_simple_calculator/features/calculator/02_design.md` を作成する

## 次に確認すること

- `docs/cli_simple_calculator/features/calculator/02_design.md` を作成する

## 注意点

- `tasks.md` には現在の作業状態と次の一手だけを短く書きます。
- 仕様の詳細は `01_spec.md` に記録します。
- 設計、テスト計画、レビュー結果の詳細は、それぞれの専用ファイルに記録します。
- command/app 全体の現在地は `docs/cli_simple_calculator/tasks.md` 側で扱います。
