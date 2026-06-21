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

ecs = boto3.client("ecs", region_name=region)
ecr = boto3.client("ecr", region_name=region)
logs = boto3.client("logs", region_name=region)

task = ecs.describe_tasks(cluster=cluster, tasks=[task_arn])["tasks"][0]
container = task["containers"][0]
image_digest = container.get("imageDigest")
stopped_reason = task.get("stoppedReason", "")

# digest -> commit SHA タグ
sha = None
if image_digest:
    detail = ecr.describe_images(repositoryName=repo,
                                 imageIds=[{"imageDigest": image_digest}])["imageDetails"][0]
    for tag in detail.get("imageTags", []):
        if re.fullmatch(r"[0-9a-f]{40}", tag):
            sha = tag
            break

# 該当タスクのログ取得（直近）
events = logs.get_log_events(logGroupName=log_group, logStreamName=log_stream,
                             limit=50, startFromHead=False).get("events", [])
log_text = "\n".join(e["message"] for e in events)

# ログから source（例 batch/main.py:main）を拾う
source = None
for e in reversed(events):
    try:
        rec = json.loads(e["message"])
    except ValueError:
        continue
    if rec.get("level") == "ERROR" and rec.get("source"):
        source = rec["source"]
        break

out = {"sha": sha, "image_digest": image_digest, "stopped_reason": stopped_reason,
       "log_text": log_text, "source": source}
with open(os.path.join(os.environ["RUNNER_TEMP"], "ctx.json"), "w", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False)
print("sha=" + (sha or "NOT_FOUND"))