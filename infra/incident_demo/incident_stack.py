from aws_cdk import (
    CfnOutput, Duration, Stack,
    aws_ec2 as ec2, aws_ecr as ecr, aws_ecs as ecs,
    aws_iam as iam, aws_lambda as lambda_, aws_logs as logs,
    aws_logs_destinations as destinations,
    aws_sns as sns, aws_sns_subscriptions as subs,
)
from constructs import Construct


class IncidentDemoStack(Stack):
    def __init__(self, scope, cid, *, github_repo, notify_email, bedrock_profile_arn, bedrock_model_arn, **kw):
        super().__init__(scope, cid, **kw)
        vpc = ec2.Vpc(self, "Vpc", max_azs=2, nat_gateways=0,
                      subnet_configuration=[ec2.SubnetConfiguration(
                          name="public", subnet_type=ec2.SubnetType.PUBLIC)])
        log_group = logs.LogGroup(self, "BatchLogs", retention=logs.RetentionDays.ONE_WEEK)

        # (a) ECRリポジトリ（CIがSHAタグでpushする先）
        repo = ecr.Repository(self, "BatchRepo", repository_name="incident-demo-batch",
                              image_scan_on_push=True)

        # (b) ECSタスク定義：ECRの :latest を参照（digestから後でSHAを逆引き）
        cluster = ecs.Cluster(self, "Cluster", vpc=vpc)
        task_def = ecs.FargateTaskDefinition(self, "BatchTask", cpu=256, memory_limit_mib=512)
        task_def.add_container(
            "batch",
            image=ecs.ContainerImage.from_ecr_repository(repo, "latest"),
            logging=ecs.LogDriver.aws_logs(stream_prefix="batch", log_group=log_group),
            environment={"BATCH_NAME": "nightly-etl"},
        )

        # --- SNS + メール購読 ---
        topic = sns.Topic(self, "IncidentTopic")
        topic.add_subscription(subs.EmailSubscription(notify_email))

        # --- 通知Lambda：ERRORログを受けてメール本文を組み立てSNS publish ---
        notify_fn = lambda_.Function(
            self, "NotifyFn",
            runtime=lambda_.Runtime.PYTHON_3_12,
            handler="index.handler",
            timeout=Duration.seconds(30),
            environment={
                "TOPIC_ARN": topic.topic_arn,
                "CLUSTER_NAME": cluster.cluster_name,
                "LOG_GROUP": log_group.log_group_name,
                "GITHUB_REPO": github_repo,
                "REGION": self.region,
                "ACCOUNT_ID": self.account,
            },
            code=lambda_.Code.from_inline(_NOTIFY_CODE))
        topic.grant_publish(notify_fn)

        # --- CloudWatch Logs サブスクリプション（ERROR を Lambda へ） ---
        logs.SubscriptionFilter(
            self, "ErrorSub",
            log_group=log_group,
            destination=destinations.LambdaDestination(notify_fn),
            filter_pattern=logs.FilterPattern.any_term("ERROR"))

        # OIDC プロバイダ
        provider = iam.OpenIdConnectProvider(
            self, "GitHubOIDC",
            url="https://token.actions.githubusercontent.com",
            client_ids=["sts.amazonaws.com"])

        def gh_principal():
            return iam.WebIdentityPrincipal(
                provider.open_id_connect_provider_arn,
                {"StringEquals": {"token.actions.githubusercontent.com:aud": "sts.amazonaws.com"},
                 "StringLike": {"token.actions.githubusercontent.com:sub": f"repo:{github_repo}:*"}})

        # (c-1) pushロール：ECRへの push のみ
        push_role = iam.Role(self, "GhPushRole", assumed_by=gh_principal())
        repo.grant_pull_push(push_role)

        # (c-2) 調査ロール：読み取り専用 + Bedrock invoke のみ（書き込み・デプロイ権限なし）
        inspect_role = iam.Role(self, "GhInspectRole", assumed_by=gh_principal())
        inspect_role.add_to_policy(iam.PolicyStatement(
            actions=[
                "ecs:DescribeTasks", "ecs:DescribeTaskDefinition", "ecs:ListTasks",
                "ecr:DescribeImages", "ecr:BatchGetImage", "ecr:GetDownloadUrlForLayer",
                "logs:GetLogEvents", "logs:FilterLogEvents", "logs:DescribeLogStreams",
                "rds:DescribeDBInstances",  # ランタイム状態の確認（読み取りのみ）
            ],
            resources=["*"]))
        inspect_role.add_to_policy(iam.PolicyStatement(
            actions=["bedrock:InvokeModel"],
            resources=[bedrock_profile_arn, bedrock_model_arn]))

        CfnOutput(self, "EcrRepoUri", value=repo.repository_uri)
        CfnOutput(self, "GhPushRoleArn", value=push_role.role_arn)
        CfnOutput(self, "GhInspectRoleArn", value=inspect_role.role_arn)
        CfnOutput(self, "LogGroupName", value=log_group.log_group_name)
        CfnOutput(self, "ClusterName", value=cluster.cluster_name)
        CfnOutput(self, "TaskDefArn", value=task_def.task_definition_arn)
        CfnOutput(self, "SubnetIds",
                  value=",".join(s.subnet_id for s in vpc.public_subnets))


_NOTIFY_CODE = r"""
import base64
import gzip
import json
import os

import boto3

sns = boto3.client("sns")


def handler(event, _ctx):
    data = json.loads(gzip.decompress(base64.b64decode(event["awslogs"]["data"])))
    log_group = data["logGroup"]
    log_stream = data["logStream"]
    task_id = log_stream.split("/")[-1]   # awslogs: "batch/batch/<taskId>"
    region = os.environ["REGION"]
    cluster = os.environ["CLUSTER_NAME"]
    repo = os.environ["GITHUB_REPO"]
    account = os.environ["ACCOUNT_ID"]
    task_arn = f"arn:aws:ecs:{region}:{account}:task/{cluster}/{task_id}"
    run_url = "https://github.com/" + repo + "/actions/workflows/triage.yml"  # 旧表記(波括弧表示の都合で壊れていたため連結に修正): "https://github.com/{repo}/actions/workflows/triage.yml"
    msgs = "\n".join(e["message"] for e in data["logEvents"])
    cmd = (f"gh workflow run triage.yml -R {repo} "
           f"-f task_arn='{task_arn}' -f log_stream='{log_stream}'")
    body = (
        "■ バッチ nightly-etl でエラーを検知しました。\n"
        "起票すると判断したら、次の A か B のどちらかで triage を実行してください。\n\n"
        "=== 方法A: GitHub CLI（この1行をそのままコピペ実行）===\n"
        f"{cmd}\n\n"
        "=== 方法B: ブラウザ ===\n"
        f"1) 次のURLを開く: {run_url}\n"
        "2) 右上の「Run workflow」を押す\n"
        "3) 表示される2つの入力欄に、以下をそのまま貼り付けて Run:\n"
        f"   - task_arn   = {task_arn}\n"
        f"   - log_stream = {log_stream}\n\n"
        "※ 必須は log_stream（ログから原因箇所とコミットSHAを特定します）。task_arn は予備（フォールバック用）です。\n\n"
        f"[参考] cluster   = {cluster}\n"
        f"[参考] log_group = {log_group}\n\n"
        "----- 検知ログ -----\n" + msgs
    )
    sns.publish(TopicArn=os.environ["TOPIC_ARN"],
                Subject="[障害][nightly-etl] エラー検知 - 起票評価をお願いします",
                Message=body)
"""