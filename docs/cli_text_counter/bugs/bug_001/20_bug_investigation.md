# バグ調査書

## バグID

bug_001

## 調査対象

- command/app: `cli_text_counter`
- feature: `text_counter`
- バグ報告書: `docs/cli_text_counter/bugs/bug_001/10_bug_report.md`
- 実装ファイル: `src/cli_text_counter/features/text_counter.py`
- entrypoint: `src/cli_text_counter/entrypoint.py`
- テストファイル:
  - `tests/cli_text_counter/features/test_text_counter.py`
  - `tests/cli_text_counter/test_entrypoint_text_counter.py`
  - `tests/cli_text_counter/test_integration_text_counter.py`

## 参照したファイル

- `AGENTS.md`
- `docs/concept/ai_driven_development.md`
- `prompts/investigate_bug.md`
- `docs/templates/20_bug_investigation_template.md`
- `docs/cli_text_counter/bugs/bug_001/10_bug_report.md`
- `docs/cli_text_counter/10_overview.md`
- `docs/cli_text_counter/features/text_counter/20_spec.md`
- `docs/cli_text_counter/features/text_counter/21_design.md`
- `docs/cli_text_counter/features/text_counter/22_flow.md`
- `docs/cli_text_counter/features/text_counter/23_test_plan.md`
- `docs/cli_text_counter/11_integration_test_plan.md`
- `docs/cli_text_counter/12_command_review_result.md`
- `src/cli_text_counter/features/text_counter.py`
- `src/cli_text_counter/entrypoint.py`
- `tests/cli_text_counter/features/test_text_counter.py`
- `tests/cli_text_counter/test_entrypoint_text_counter.py`
- `tests/cli_text_counter/test_integration_text_counter.py`

## 関連仕様

- `20_spec.md` では、空文字列は有効な入力として扱い、文字数 `0` を返すと定義されている。
- `20_spec.md` では、入力文字列が指定されていない場合は entrypoint 側で `argparse` の引数エラーにすると定義されている。
- `10_overview.md` では、`cli_text_counter` は CLI 引数で入力文字列を受け取り、文字数を標準出力へ表示すると定義されている。

## 関連設計

- `21_design.md` では、`count_characters(text: str) -> int` が文字数算出だけを担当すると定義されている。
- `21_design.md` では、空文字列は正常系として扱い、`0` を返すと定義されている。
- `entrypoint.py` は CLI 引数の受け取り、feature 呼び出し、標準出力、終了コード返却を担当する設計である。

## 関連フロー

- `22_flow.md` では、CLI 引数で入力文字列を受け取り、`count_characters(text)` に渡し、戻り値を標準出力へ表示する流れが定義されている。
- `22_flow.md` では、空文字列が指定された場合はエラーにせず、`count_characters(text)` が `0` を返すと定義されている。

## 関連テスト

- `23_test_plan.md` では、feature 単体テストとして `count_characters("")` が `0` を返すことを確認する計画になっている。
- `tests/cli_text_counter/features/test_text_counter.py` では、`count_characters("") == 0` を確認している。
- `11_integration_test_plan.md` では、`python src/cli_text_counter/entrypoint.py --text ""` により標準出力に `0` が表示され、終了コード `0` になることを確認する計画になっている。
- `tests/cli_text_counter/test_integration_text_counter.py` では、`subprocess.run([... , "--text", ""])` により空文字列を直接 argv として渡し、標準出力 `0\n` と終了コード `0` を確認している。

## 実装確認結果

- `src/cli_text_counter/features/text_counter.py` の `count_characters` は `return len(text)` のみであり、空文字列を渡すと `0` を返す。
- `src/cli_text_counter/entrypoint.py` の `parse_args` は `parser.add_argument("--text", required=True, help="Input text.")` を定義している。
- `main` は `args.text` を `count_characters` に渡し、結果を `print(result)` して `0` を返す。
- `python src/cli_text_counter/entrypoint.py --text ""` を Windows PowerShell から実行した場合、`argparse` が `argument --text: expected one argument` を出して終了コード `1` になった。
- `python src/cli_text_counter/entrypoint.py --text=` を実行した場合、標準出力に `0` が表示され、終了コード `0` になった。
- `python -m pytest tests/cli_text_counter/ -v` の結果は `11 passed` であった。

## 原因仮説

### 原因として有力なもの

- **ドキュメント不整合 / 仕様確認待ち**: 仕様・設計・実装は「空文字列を受け取った場合に `0` を返す」方針で一致している。一方、バグ報告書と結合試験計画の再現コマンド `python src/cli_text_counter/entrypoint.py --text ""` は、Windows PowerShell では空文字列が Python プロセスに値として渡らず、`argparse` からは `--text` に値がない状態として見える。このため、ドキュメント上の実行例が利用環境によって期待どおり動かない可能性がある。
- **テスト観点の不足候補**: 結合試験では `subprocess.run` にリスト形式で `""` を渡しており、shell のクォート解釈を経由しない。そのため、Windows PowerShell でドキュメント記載のコマンドをそのまま実行した場合の挙動は検出できていない。ただし、現在のテスト自体は「空文字列が argv として渡った場合に `0` を返す」ことを正しく確認しているため、現時点ではテストコードの誤りとは断定しない。

### 原因として除外したもの

- **仕様バグ**: 現行仕様は空文字列を許可し、`0` を返す方針を明確に記載しているため、仕様自体が空文字列を禁止している不整合はない。ただし、`--text ""` という shell 実行例まで保証対象に含めるかは未確定である。
- **実装バグ（feature）**: `count_characters("")` は `0` を返し、単体テストでも確認済みであるため、feature 実装のバグではない。
- **実装バグ（entrypoint の通常処理）**: `--text=` のように空文字列が argv として渡った場合、entrypoint は `0` を出力して正常終了するため、空文字列受け取り後の処理は仕様通りである。
- **テストバグ**: 既存テストは feature 単体、entrypoint、subprocess 結合の範囲ではすべて成功している。shell 固有の実行例をテスト対象に含めるべきかは、テストバグではなくテスト計画または仕様範囲の確認事項として扱う。

## 影響範囲

- Windows PowerShell など、`--text ""` で空文字列がそのままプロセス引数に渡らない実行環境。
- ドキュメント記載の再現コマンドをそのまま利用する利用者。
- `--text=` を使う場合、またはテストのように argv に空文字列を直接渡す場合は、現行実装で `0` を返せる。

## 人間判断

- PowerShell の `--text ""` を必ず成功させるための実装変更は行わない。
- 空文字列を CLI から渡す場合の推奨表記は `--text=` とする。
- `--text ""` は shell によって空文字列の扱いが異なる可能性があるため、ドキュメント上は注意書きとして扱う。
- 今回の bug_001 は、feature 実装や entrypoint 通常処理のバグではなく、ドキュメント不整合 / 実行例の環境差として扱う。

## 仕様変更が必要か

不要。

空文字列を有効入力として扱う現行仕様は維持する。
PowerShell の `--text ""` を必ず成功させるために、CLI 仕様を変更して `--text` 単独を空文字列扱いにする対応は行わない。
空文字列を CLI から渡す場合は `--text=` を推奨表記とし、`--text ""` は shell によって扱いが異なる可能性がある実行例としてドキュメント上の注意書きで扱う。

## 設計変更が必要か

不要。

現行設計では `--text` に値がない場合は `argparse` の引数エラーとして扱う。
人間判断により、PowerShell の `--text ""` を必ず成功させるための実装変更は行わないため、`--text` 単独を空文字列とみなす設計変更は行わない。
entrypoint 通常処理は、空文字列が argv として渡された場合に `0` を出力できているため、設計変更は不要である。

## テスト計画変更が必要か

不要。

`subprocess.run([... , "--text", ""])` による argv 直接渡しの確認は、空文字列が CLI 引数として渡された場合の entrypoint 動作確認として有効である。
今回の bug_001 はドキュメント不整合 / 実行例の環境差として扱い、PowerShell の `--text ""` を必ず成功させる実装変更は行わないため、テスト計画変更は不要である。
必要な対応は、空文字列の推奨表記を `--text=` とし、`--text ""` の shell 差異をドキュメント上の注意書きとして扱う修正計画で整理する。

## 追加で確認すべきこと

- なし。

人間判断により、PowerShell の `--text ""` 実行は必須保証対象に含めず、空文字列入力の推奨 CLI 表記は `--text=` とする方針で確定した。
`--text` 単独を空文字列として扱う設計変更も行わない。

## 調査段階の判定

`調査完了`

原因の中心は、空文字列が feature または entrypoint の通常処理に渡った後の不具合ではなく、Windows PowerShell で `--text ""` と実行した際に空文字列が `argparse` に値として届かない点である。
人間判断により、今回の bug_001 はドキュメント不整合 / 実行例の環境差として扱うことが確定した。
そのため、次工程では `prompts/create_bug_fix_plan.md` を使い、ドキュメント修正を対象とした修正計画に進める。

## この段階で修正しないこと

- 実装コードを変更しない
- テストコードを変更しない
- 仕様・設計・テスト計画を変更しない（変更候補は上記セクションに記録する）
- 修正計画（30_bug_fix_plan.md）はまだ作成しない
