import json
import os

import boto3

region = os.environ["AWS_REGION"]
model_id = os.environ["BEDROCK_MODEL_ID"]
max_tokens = int(os.environ.get("MAX_TOKENS", "1200"))

with open(os.path.join(os.environ["RUNNER_TEMP"], "ctx.json"), encoding="utf-8") as f:
    ctx = json.load(f)
sha = ctx.get("sha")
log_text = ctx.get("log_text", "")
source = ctx.get("source")

# ★ HEADではなく『動いていたコミット』のコードを読む（./deployed に checkout済み）
code = "(該当ファイル特定できず)"
if source:
    path = os.path.join("deployed", source.split(":")[0])
    if os.path.exists(path):
        with open(path, encoding="utf-8") as f:
            code = f.read()

prompt = (
    "あなたは障害対応の補助AIです。以下は『エラー発生時に実際にデプロイされていたコミットの"
    "コード』とランタイムのログです。最新コードではなくこの実物を前提に、原因を特定し修正案を作成してください。"
    "断定せず推測は『仮説』と明記すること。次の見出しで日本語のISSUE本文を出力:\n"
    "## 現象\n## エラー原文（ログ）\n## 原因仮説（確信度つき）\n## 修正方針\n## 差分案（擬似diff可）\n"
    "## 影響範囲・テスト観点\n## リスク\n\n"
    f"=== デプロイ済みコミット: {sha} ===\n=== 該当コード ({source}) ===\n{code}\n\n=== ログ ===\n{log_text}\n"
)

client = boto3.client("bedrock-runtime", region_name=region)
resp = client.converse(
    modelId=model_id,
    messages=[{"role": "user", "content": [{"text": prompt}]}],
    inferenceConfig={"maxTokens": max_tokens, "temperature": 0.2})
text = resp["output"]["message"]["content"][0]["text"]

header = (f"> 本ISSUEはAIが自動起票しました。原因特定は **デプロイ済みコミット `{sha}`** の"
          f"コードとランタイムログに基づきます（最新HEADではありません）。内容は仮説を含みます。\n\n")
with open("issue.md", "w", encoding="utf-8") as f:
    f.write(header + text)
print("wrote issue.md")