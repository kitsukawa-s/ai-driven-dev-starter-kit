# cli_text_counter tasks

## 目的

`cli_text_counter` の作業状態を、人間とAIが引き継ぎやすくするためのメモです。

このファイルは作業中の現在地を示すために使います。
仕様、設計、テスト計画、レビュー結果の代わりにはしません。

## 現在の状態

- command/app: `cli_text_counter`
- feature: `text_counter`
- 状態: 10_overview.md の記述を現在の実装状態に合わせて更新済み
- 最終更新: 2026-05-17

## 作業メモ

- [x] `docs/cli_text_counter/10_overview.md` を作成する
- [x] `docs/cli_text_counter/tasks.md` を作成する
- [x] `docs/cli_text_counter/features/text_counter/` を作成する
- [x] `docs/cli_text_counter/features/text_counter/tasks.md` を作成する
- [x] `docs/cli_text_counter/features/text_counter/20_spec.md` を作成する
- [x] 今回は `src/` と `tests/` を作成しない
- [x] 空文字列と文字数の数え方を `20_spec.md` に反映する
- [x] `src/cli_text_counter/entrypoint.py` を作成する
- [x] `tests/cli_text_counter/test_entrypoint_text_counter.py` を作成する
- [x] `cli_text_counter` 関連テストの結果を確認する
- [x] `11_integration_test_plan.md` を作成する
- [x] `tests/cli_text_counter/test_integration_text_counter.py` を作成する
- [x] 結合試験を含む `cli_text_counter` 関連テストの結果を確認する
- [x] command/app 全体レビューを行う（12_command_review_result.md 作成済み）
- [x] 10_overview.md の記述を現在の実装状態に合わせて更新する（軽微な指摘対応）

## 次に確認すること

- fallback import の方針明文化（別作業として保留中）

## 注意点

- `tasks.md` には現在の作業状態と次の一手だけを短く書きます。
- 仕様の詳細は `20_spec.md` に書きます。
- レビュー結果はこのファイルには書きません。
- 結合試験（subprocess）は前回の Codex 環境では WinError 6 で 4 件 skip されていた。Claude Sonnet 環境では 11 passed, 0 skipped で通過済み。WinError 6 が再現する環境では再確認が必要。
