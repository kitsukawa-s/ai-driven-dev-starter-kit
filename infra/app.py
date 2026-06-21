import os

import aws_cdk as cdk

from incident_demo.incident_stack import IncidentDemoStack

app = cdk.App()
region = os.environ.get("CDK_DEFAULT_REGION", "ap-northeast-1")
account = os.environ.get("CDK_DEFAULT_ACCOUNT")
github_repo = os.environ["GITHUB_REPO"]
notify_email = os.environ["NOTIFY_EMAIL"]
# 東京リージョンでは Haiku 4.5 はクロスリージョン推論プロファイル(Japan/jp)経由で使う
model_id = os.environ.get("BEDROCK_MODEL_ID", "jp.anthropic.claude-haiku-4-5-20251001-v1:0")
# プロファイルID（apac./jp./us. など）からベースの基盤モデルIDを取り出す
_prefix = model_id.split(".", 1)[0]
base_model_id = model_id.split(".", 1)[1] if _prefix in ("apac", "jp", "us", "eu", "global") else model_id
# 呼び出しに使う推論プロファイルARN
bedrock_profile_arn = f"arn:aws:bedrock:{region}:{account}:inference-profile/{model_id}"
# プロファイルのルーティング先＝各リージョンの基盤モデルARN（リージョンはワイルドカード）
bedrock_model_arn = f"arn:aws:bedrock:*::foundation-model/{base_model_id}"

IncidentDemoStack(
    app, "IncidentDemoStack",
    github_repo=github_repo,
    notify_email=notify_email,
    bedrock_profile_arn=bedrock_profile_arn,
    bedrock_model_arn=bedrock_model_arn,
    env=cdk.Environment(account=account, region=region))
app.synth()