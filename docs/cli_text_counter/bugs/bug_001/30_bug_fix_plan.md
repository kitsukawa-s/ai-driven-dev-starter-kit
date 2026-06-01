<!--
このファイルはバグ修正計画書です。
この段階では、まだ実装コードやドキュメントを変更しません。
人間が承認欄に確認を入れた後、prompts/implement_bug_fix.md を使って修正します。
-->

# バグ修正計画書

## バグID

bug_001

## 修正方針

今回の bug_001 は、feature 実装や entrypoint 通常処理のバグではなく、ドキュメント不整合 / 実行例の環境差として扱う。

PowerShell の `--text ""` を必ず成功させるための実装変更は行わない。
空文字列を CLI から渡す場合の推奨表記は `--text=` とし、`--text ""` は shell によって空文字列の扱いが異なる可能性があることをドキュメント上の注意書きとして扱う。

修正対象はドキュメントのみとする。
`src/` と `tests/` は修正対象に含めない。

## 修正対象ファイル

| ファイル | 変更内容 |
|---|---|
| `docs/cli_text_counter/10_overview.md` | 空文字列を CLI から渡す場合の推奨表記を `--text=` として記載する。`--text ""` は shell によって扱いが異なる可能性がある注意書きを追加する。 |
| `docs/cli_text_counter/11_integration_test_plan.md` | 空文字列の CLI 実行例を `--text=` に修正する。既存の argv 直接渡しテストは有効であること、`--text ""` は shell 差異があるため注意書きとして扱うことを記載する。 |

## 変更してはいけないファイル

- `src/`
- `tests/`
- `docs/cli_text_counter/features/`
- `docs/cli_text_counter/bugs/bug_001/10_bug_report.md`
- `docs/cli_text_counter/bugs/bug_001/20_bug_investigation.md`
- `docs/cli_text_counter/bugs/bug_001/30_bug_fix_plan.md`（実装段階では計画内容の変更対象にしない）
- `prompts/`
- `docs/templates/`
- `AGENTS.md`
- `README.md`
- `requirements.txt`
- CI/CD、デプロイ関連ファイル

## 追加・更新するテスト

- なし。

今回の修正対象はドキュメントのみであり、仕様変更、設計変更、テスト計画変更、実装変更は行わない。
既存テストは、空文字列が argv として渡された場合の動作確認として有効であるため、テストコードの追加・更新は行わない。

## 実行する確認コマンド

文書修正のため、テスト実行は不要。

任意確認として実行する場合:

```bash
python -m pytest
```

ドキュメント修正後の内容確認:

```bash
git diff -- docs/cli_text_counter/10_overview.md docs/cli_text_counter/11_integration_test_plan.md
```

## 仕様・設計・テスト計画への反映要否

| 対象 | 反映が必要か | 内容 |
|---|---|---|
| 仕様（20_spec.md） | 不要 | 空文字列を有効入力として扱う現行仕様は維持する。 |
| 設計（21_design.md） | 不要 | `--text` 単独を空文字列として扱う設計変更は行わない。 |
| フロー（22_flow.md） | 不要 | 空文字列が argv として渡された場合に `0` を返す流れは現行どおり。 |
| テスト計画（23_test_plan.md） | 不要 | feature 単体テスト計画は現行どおり。CLI 実行例の環境差は command/app 側ドキュメントで扱う。 |

## 別作業が必要な事項

- なし。

この修正計画の承認後、`prompts/implement_bug_fix.md` を使って、上記の修正対象ファイルのみを更新する。

## リスク

- `--text ""` を期待している利用者がいる場合、推奨表記が `--text=` であることをドキュメントから読み取れるようにする必要がある。
- shell ごとの空文字列の扱いを詳細に説明しすぎると、スターターキットとしてのドキュメントが複雑になる可能性がある。
- 実装変更を行わないため、PowerShell で `--text ""` を実行した場合の挙動は変わらない。

## ロールバック・戻し方

- ドキュメント修正後に問題があった場合は、`docs/cli_text_counter/10_overview.md` と `docs/cli_text_counter/11_integration_test_plan.md` の該当追記・変更箇所を修正前の記述に戻す。
- `src/` と `tests/` は変更しない計画のため、実装コードやテストコードのロールバックは不要。

## 人間承認欄

- [x] 修正方針を確認した
- [x] 修正対象ファイルを確認した
- [x] 変更してはいけないファイルを確認した
- [x] 追加・更新するテストを確認した
- [x] 仕様・設計・テスト計画への反映要否を確認した
- [x] 別作業事項を確認した
- [x] 上記をすべて確認し、実装に進むことを承認する

## 実装に進んでよいか

人間が承認欄にすべてチェックを入れた後、`prompts/implement_bug_fix.md` を使って実装に進んでください。
承認なしに実装を開始しないでください。

## 実装時の注意点

- この修正計画に書かれていない変更をしない
- ついで修正やリファクタリングをしない
- `src/` を変更しない
- `tests/` を変更しない
- `docs/cli_text_counter/features/` を変更しない
- `docs/cli_text_counter/bugs/bug_001/10_bug_report.md` を変更しない
- `docs/cli_text_counter/bugs/bug_001/20_bug_investigation.md` を変更しない
- `docs/cli_text_counter/bugs/bug_001/30_bug_fix_plan.md` を実装段階で変更しない
- 仕様・設計・テスト計画の更新が必要と判明した場合は、実装を中断して STOP し、報告する
