# simple-calculator を実装してテストを作成してください

あなたは、このリポジトリのAI駆動開発スターターキットを使う開発補助者です。

`AGENTS.md` に従い、実装前に必ず仕様・設計・呼び出し定義・テスト設計・レビュー観点を確認してください。

## 対象機能

- `docs/features/020_simple-calculator/`

## 参照するファイル

- `docs/features/020_simple-calculator/01_feature.md`
- `docs/features/020_simple-calculator/02_function_design.md`
- `docs/features/020_simple-calculator/03_function_call_flow.md`
- `docs/features/020_simple-calculator/04_test_design.md`
- `docs/features/020_simple-calculator/05_review_checklist.md`

## 作成するファイル

- `src/simple_calculator.py`
- `tests/test_simple_calculator.py`

## 作業内容

1. 仕様・設計・呼び出し定義・テスト設計・レビュー観点を確認してください
2. 実装前レビューとして、設計に矛盾がないか簡潔に確認してください
3. `src/simple_calculator.py` を作成してください
4. 実装をセルフレビューしてください
5. `tests/test_simple_calculator.py` を作成してください
6. テストをレビューしてください
7. 可能であれば、以下を実行してください

```bash
python -m pytest
```

## 注意

- Python標準ライブラリのみを使ってください
- CLI引数解析には `argparse` を使ってください
- テストは `pytest` を前提にしてください
- 初学者が読めるシンプルな実装にしてください
- 複雑なクラス設計は避けてください
- 関数中心で実装してください
- 仕様にない便利機能を追加しないでください
- 共通化候補があっても、人間レビュー前に `src/common/` へ切り出さないでください
- 結合試験、外部API、CI/CD、デプロイ資産は作成しないでください
