import json
import os
import re

import boto3

region = os.environ["AWS_REGION"]
cluster = os.environ["CLUSTER_NAME"]
task_arn = os.environ["TASK_ARN"]
repo = os.environ["ECR_REPO"]
log_group = os.environ["LOG_GROUP"]
log_stream = os.environ["LOG_STREAM"]

ecr = boto3.client("ecr", region_name=region)
logs = boto3.client("logs", region_name=region)

# 1) まず CloudWatch Logs（耐久ストレージ）から ログ・source・commit(SHA) を取得する
#    ログは保持期間（既定1週間）残るので、翌日以降のトリアージでもSHAが取れる。
events = logs.get_log_events(logGroupName=log_group, logStreamName=log_stream,
                             limit=50, startFromHead=False).get("events", [])
log_text = "\n".join(e["message"] for e in events)

source, sha = None, None
for e in reversed(events):
    try:
        rec = json.loads(e["message"])
    except ValueError:
        continue
    if rec.get("level") == "ERROR":
        source = source or rec.get("source")
        c = rec.get("commit")
        if c and c != "unknown" and re.fullmatch(r"[0-9a-f]{40}", c):
            sha = sha or c
        if source and sha:
            break

# 2) フォールバック: ログにSHAが無い古いイメージ向け。ECSタスク→imageDigest→ECRタグ逆引き。
#    停止タスクは約1時間で describe-tasks から消えるためベストエフォート（失敗してもログ由来SHAがあれば問題なし）。
image_digest = None
if not sha:
    try:
        ecs = boto3.client("ecs", region_name=region)
        _tasks = ecs.describe_tasks(cluster=cluster, tasks=[task_arn]).get("tasks", [])
        if _tasks:
            image_digest = _tasks[0]["containers"][0].get("imageDigest")
            if image_digest:
                detail = ecr.describe_images(repositoryName=repo,
                    imageIds=[{"imageDigest": image_digest}])["imageDetails"][0]
                for tag in detail.get("imageTags", []):
                    if re.fullmatch(r"[0-9a-f]{40}", tag):
                        sha = tag
                        break
    except Exception as ex:
        print("WARN: ECS fallback skipped: " + str(ex))

# ctx.json は必ず書き出す（SHAが取れなくても analyze は走る）
out = {"sha": sha, "image_digest": image_digest,
       "log_text": log_text, "source": source}
with open(os.path.join(os.environ["RUNNER_TEMP"], "ctx.json"), "w", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False)
print("sha=" + (sha or "NOT_FOUND"))