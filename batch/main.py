import datetime
import json
import os
import sys

BATCH = os.environ.get("BATCH_NAME", "nightly-etl")


def log_error(error_type, message, source, *, severity="P2", category="app", is_retryable=False):
    rec = {
        "timestamp": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "level": "ERROR",
        "app": BATCH,
        "commit": os.environ.get("GIT_SHA", "unknown"),  # ← 実行中イメージに埋め込んだコミットSHA（耐久的に残す）
        "error_type": error_type,
        "severity": severity,
        "category": category,
        "is_retryable": is_retryable,
        "message": message,
        "source": source,  # ← デプロイ済みコミットの該当箇所を特定する手がかり
    }
    print(json.dumps(rec, ensure_ascii=False), flush=True)


def main():
    if os.environ.get("FORCE_ERROR") == "KeyError":
        try:
            row = {"id": 1}
            _ = row["amount"]  # 必須カラム欠損を再現
        except KeyError as e:
            log_error("KeyError", f"required column missing: {e}", "batch/main.py:main")
            sys.exit(1)
    print(json.dumps({"level": "INFO", "app": BATCH, "message": "completed"}, ensure_ascii=False), flush=True)


if __name__ == "__main__":
    main()