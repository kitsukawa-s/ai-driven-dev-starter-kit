# AI駆動開発スターターキット

このリポジトリは、GitHub Copilot Agent Mode を使って、AI駆動開発の流れを小さく体験するためのスターターキットです。

目的は、完成度の高いアプリを作ることではありません。

小さな機能を題材にして、以下の流れを体験することを目的とします。

1. 機能要望を読む
2. 機能要望をレビューする
3. 関数設計を作る
4. 関数設計をレビューする
5. 関数呼び出し定義を作る
6. 関数呼び出し定義をレビューする
7. テスト設計を作る
8. テスト設計をレビューする
9. 実装する
10. 実装をレビューする
11. テストを作る
12. テストをレビューする
13. テストを実行する
14. 最終レビューを行う

重要なのは、AIにコードを丸投げすることではありません。

人間が理解できる仕様と設計を用意し、それをもとにAIと一緒に開発することを目指します。

このリポジトリはスターターキットですが、単なるHello World教材ではありません。

最初は小さく体験できるようにしつつ、実際のプロジェクトにも応用しやすいように、機能単位のドキュメント構成、設計ひな形、レビュー観点を用意しています。

---

## このリポジトリで体験できること

このリポジトリでは、以下を体験できます。

- AIに作業してもらうための `AGENTS.md` の使い方
- 機能単位で設計書を管理する方法
- 仕様から関数設計を作る流れ
- 関数の呼び出し関係を整理する流れ
- テスト設計を先に整理する流れ
- AIに実装とテストを作ってもらう流れ
- AIの出力を各工程でレビューする流れ

---

## 対象者

このリポジトリは、以下のような人を想定しています。

- AI駆動開発を試してみたい人
- GitHub Copilot Agent Mode を使ってみたい人
- AIにコードを書かせる前に、仕様や設計をどう渡すか知りたい人
- AIに丸投げするのではなく、人間がレビューできる形で開発したい人
- チームでAI駆動開発を導入する前に、小さく体験したい人

---

## 前提

このスターターキットでは、以下を前提にしています。

- GitHub のリポジトリを clone またはダウンロードできること
- Python を実行できること
- GitHub Copilot Agent Mode を使えること
- エディタとして Visual Studio Code を使うことを想定

実装コードでは、Python の標準ライブラリのみを使います。

単体テストには `pytest` を使います。
テスト実行用の最小依存として、`requirements.txt` に `pytest` のみを記載しています。

---

## セットアップ

テストを実行する場合は、必要に応じて以下を実行してください。

    python -m pip install -r requirements.txt

このリポジトリでは、実装コードには Python 標準ライブラリのみを使います。

`requirements.txt` は、単体テスト用の `pytest` をインストールするために用意しています。

仮想環境を使う場合は、先に仮想環境を作成してからインストールしてください。

---

## 今回の対象範囲

このスターターキットでは、AI駆動開発の基本的な流れを体験するため、単体試験までを対象にします。

対象にするもの:

- 機能要望の整理
- 関数設計
- 関数呼び出し定義
- テスト設計
- 実装
- 単体テスト
- レビュー

今回は対象外とするもの:

- 結合試験
- 外部システム連携
- 結合試験用スタブ
- CI/CD
- デプロイ
- 本番運用設計

これらは実際のプロジェクトでは重要ですが、今回のスターターキットでは扱いません。

まずは、AIに小さな機能を安全に作ってもらう流れを体験することを優先します。

---

## リポジトリ構成

基本構成は以下です。

    ai-driven-dev-starter-kit/
    ├─ README.md
    ├─ AGENTS.md
    ├─ docs/
    │  ├─ overview.md
    │  ├─ common/
    │  │  └─ README.md
    │  ├─ templates/
    │  │  ├─ 01_feature_template.md
    │  │  ├─ 02_function_design_template.md
    │  │  ├─ 03_function_call_flow_template.md
    │  │  ├─ 04_test_design_template.md
    │  │  └─ 05_review_checklist_template.md
    │  └─ features/
    │     ├─ 010_hello-greeting/
    │     │  ├─ 01_feature.md
    │     │  ├─ 02_function_design.md
    │     │  ├─ 03_function_call_flow.md
    │     │  ├─ 04_test_design.md
    │     │  └─ 05_review_checklist.md
    │     └─ 020_simple-calculator/
    │        └─ 01_feature.md
    ├─ prompts/
    │  ├─ create_feature_spec.md
    │  ├─ create_function_design.md
    │  ├─ create_function_call_flow.md
    │  ├─ create_test_design.md
    │  ├─ create_review_checklist.md
    │  ├─ implement_feature.md
    │  ├─ review_feature.md
    │  └─ tutorial/
    │     ├─ 01_read_sample.md
    │     ├─ 02_create_function_design.md
    │     ├─ 03_create_function_call_flow.md
    │     ├─ 04_create_test_design.md
    │     ├─ 05_create_review_checklist.md
    │     └─ 06_implement_feature.md
    ├─ src/
    │  ├─ common/
    │  │  └─ __init__.py
    │  └─ hello_greeting.py
    └─ tests/
       ├─ common/
       └─ test_hello_greeting.py

---

## 各ファイルの役割

### README.md

このファイルです。

学習者向けに、このリポジトリの目的、構成、進め方を説明します。

### AGENTS.md

AI向けの作業ルールです。

GitHub Copilot Agent Mode に作業してもらうときは、このファイルの方針に従ってもらいます。

主に以下を定義しています。

- いきなり実装しない
- 仕様を読んでから作業する
- 設計、テスト設計、レビューを挟む
- 仕様にない機能を勝手に追加しない
- 初学者が読めるシンプルな実装にする

### docs/overview.md

ドキュメント構成と開発フローの説明です。

このリポジトリでは、機能単位でドキュメントを管理します。

### docs/templates/

機能ドキュメントを作成するときのひな形を配置します。

AIに新しい設計書を作成させる場合は、このひな形を参照させます。

### docs/features/

機能ごとの仕様、設計、テスト設計、レビュー観点を配置します。

各機能は、以下のようにフォルダを分けて管理します。

    docs/features/<number>_<feature-name>/
    ├─ 01_feature.md
    ├─ 02_function_design.md
    ├─ 03_function_call_flow.md
    ├─ 04_test_design.md
    └─ 05_review_checklist.md

先頭の番号は、読む順番や機能追加の順番を分かりやすくするためのものです。

### docs/common/

複数機能で利用する共通モジュールの設計メモを配置します。

ただし、最初から共通化を前提にしすぎないでください。

共通化は、関数設計時に候補として記録し、人間レビューで判断します。

### prompts/

`prompts/` 直下には、実際の開発で繰り返し使う汎用プロンプトを配置します。
利用者は対象機能フォルダを指定して、仕様作成、関数設計、呼び出し定義、テスト設計、レビュー観点作成、実装、レビューに使えます。
汎用プロンプトは、冒頭の「利用者が指定する項目」だけを埋めれば使える形にしています。
主に書き換えるのは、対象機能フォルダ、対象機能名、作りたいもの、必要に応じた補足条件です。
プロンプトによっては、実行イメージ、今回やらないこと、実装ファイル、テストファイルも指定します。

`prompts/tutorial/` には、このスターターキット体験用のプロンプトを配置します。
学習者は、ここにあるプロンプトを順番に使うことで、`020_simple-calculator` を題材にAI駆動開発の流れを体験できます。

GitHub Copilot Agent Mode に貼り付けるためのプロンプト例を配置します。

学習者は、`prompts/tutorial/` にあるプロンプトを順番に使うことで、AI駆動開発の流れを体験できます。

### src/

Python の実装コードを配置します。

### tests/

テストコードを配置します。

---

## 完成済みサンプル

このリポジトリには、完成済みサンプルとして以下の機能を配置します。

    010_hello-greeting

関連ファイルは以下です。

    docs/features/010_hello-greeting/
    src/hello_greeting.py
    tests/test_hello_greeting.py

この機能は、以下の対応関係を確認するためのお手本です。

- 仕様
- 関数設計
- 関数呼び出し定義
- テスト設計
- レビュー観点
- 実装
- テスト

まずは、このサンプルを読んでください。

---

## 体験用機能

学習者は、以下の機能をAIと一緒に追加します。

    020_simple-calculator

最初の状態では、以下だけを用意します。

    docs/features/020_simple-calculator/01_feature.md

学習者は、`prompts/tutorial/` 配下のプロンプトを使って、AIに以下を作成してもらいます。

- `docs/features/020_simple-calculator/02_function_design.md`
- `docs/features/020_simple-calculator/03_function_call_flow.md`
- `docs/features/020_simple-calculator/04_test_design.md`
- `docs/features/020_simple-calculator/05_review_checklist.md`
- `src/simple_calculator.py`
- `tests/test_simple_calculator.py`

---

## 進め方

### 1. サンプルを読む

まず、完成済みサンプルを確認します。

    docs/features/010_hello-greeting/
    src/hello_greeting.py
    tests/test_hello_greeting.py

確認するポイント:

- `01_feature.md` の仕様が、実装にどう反映されているか
- `02_function_design.md` の関数設計が、コードにどう反映されているか
- `03_function_call_flow.md` の呼び出し定義が、実装にどう反映されているか
- `04_test_design.md` の観点が、テストにどう反映されているか
- `05_review_checklist.md` で、何を確認する想定になっているか

### 2. AIにサンプルを読ませる

`prompts/tutorial/01_read_sample.md` を GitHub Copilot Agent Mode に貼り付けます。

AIに、完成済みサンプルの構成を確認してもらいます。

### 3. 関数設計を作る

`prompts/tutorial/02_create_function_design.md` を使って、AIに `020_simple-calculator` の関数設計を作成してもらいます。

作成対象:

    docs/features/020_simple-calculator/02_function_design.md

このとき、AIには共通モジュール化できそうな処理がないかも確認してもらいます。

ただし、共通化候補を見つけても、勝手に `src/common/` へ切り出さないでください。

共通化するかどうかは、人間レビューで判断します。

### 4. 関数呼び出し定義を作る

`prompts/tutorial/03_create_function_call_flow.md` を使って、AIに関数呼び出し定義を作成してもらいます。

作成対象:

    docs/features/020_simple-calculator/03_function_call_flow.md

### 5. テスト設計を作る

`prompts/tutorial/04_create_test_design.md` を使って、AIにテスト設計を作成してもらいます。

作成対象:

    docs/features/020_simple-calculator/04_test_design.md

### 6. レビュー観点を作る

`prompts/tutorial/05_create_review_checklist.md` を使って、AIにレビュー観点を作成してもらいます。

作成対象:

    docs/features/020_simple-calculator/05_review_checklist.md

### 7. 実装とテストを作る

`prompts/tutorial/06_implement_feature.md` を使って、AIに実装とテストを作成してもらいます。

作成対象:

    src/simple_calculator.py
    tests/test_simple_calculator.py

### 8. テストを実行する

実装後、テストを実行します。

    python -m pytest

### 9. 最終レビューを行う

以下を確認します。

- 仕様どおりに動いているか
- 設計書と実装がズレていないか
- 関数呼び出し定義と実装がズレていないか
- テスト設計とテストコードが対応しているか
- AIが仕様にない機能を勝手に追加していないか
- AIが勝手に共通モジュールへ切り出していないか
- 初学者が読めるシンプルな実装になっているか

---

## 重要な考え方

このスターターキットで大事にするのは、以下です。

### AIに丸投げしない

AIにいきなり「作って」と依頼すると、もっともらしいコードは出てきます。

しかし、仕様や前提があいまいなままだと、人間がレビューしづらいコードになりがちです。

そのため、このリポジトリでは、先に仕様、設計、テスト観点を整理します。

### 機能単位で閉じる

このリポジトリでは、機能ごとに `docs/features/<number>_<feature-name>/` を作成し、その中に仕様・設計・テスト設計・レビュー観点をまとめます。

これは、ファイルが増えたときにドキュメントが混在することを防ぐためです。

また、AIに作業を依頼するときに、対象機能のフォルダだけを読ませやすくする目的もあります。

AIに依頼するときは、原則として以下のように対象範囲を明示します。

    docs/features/020_simple-calculator/ 配下のドキュメントを確認して、この機能だけ対応してください。

### 各工程でレビューする

AIの出力は、便利ですが、常に正しいとは限りません。

そのため、以下の各工程でレビューを入れます。

- 機能要望レビュー
- 関数設計レビュー
- 関数呼び出し定義レビュー
- テスト設計レビュー
- 実装レビュー
- テストレビュー
- 最終レビュー

### 小さく作る

このスターターキットでは、あえて小さな機能だけを扱います。

理由は、AI駆動開発の型を体験することが目的だからです。

大きなアプリを作る前に、小さな機能で流れを確認します。

### 共通化は提案にとどめる

複数機能で使えそうな処理がある場合、AIには共通化候補として提案してもらいます。

ただし、AIが勝手に共通モジュールへ切り出すことはしません。

共通化するかどうかは、人間レビューで判断します。

---

## 実行例

完成済みサンプルの実行例です。

    python src/hello_greeting.py --name Alice

期待する出力:

    Hello, Alice!

体験用機能の実行例です。

    python src/simple_calculator.py --a 2 --b 3

期待する出力:

    5

---

## テスト実行

テストは以下のコマンドで実行します。

    python -m pytest

---

## 注意事項

- 仕様にない機能を勝手に追加しないでください
- 外部ライブラリは原則使わないでください
- ディレクトリ構成を大きく変えないでください
- AIの出力をそのまま信じず、必ずレビューしてください
- 共通化候補があっても、勝手に共通モジュールへ切り出さないでください
- 実装内容を説明できない場合は、そのまま採用しないでください

---

## このスターターキットのゴール

このスターターキットのゴールは、以下を体験することです。

    AIに任せる前に、AIに渡す情報を整える。
    AIに作らせたあと、人間がレビューできる形にする。

AI駆動開発とは、AIに全部任せることではありません。

人間が仕様を整理し、AIに作業を依頼し、人間が確認できる形で成果物を受け取る開発スタイルです。
