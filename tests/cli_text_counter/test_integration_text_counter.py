from pathlib import Path
import subprocess
import sys

import pytest


ROOT_DIR = Path(__file__).resolve().parents[2]
ENTRYPOINT = ROOT_DIR / "src" / "cli_text_counter" / "entrypoint.py"


def run_entrypoint(*args: str) -> subprocess.CompletedProcess[str]:
    try:
        return subprocess.run(
            [sys.executable, str(ENTRYPOINT), *args],
            capture_output=True,
            text=True,
            check=False,
        )
    except OSError as error:
        if getattr(error, "winerror", None) == 6:
            pytest.skip("subprocess is unavailable in this environment: WinError 6")
        raise


def test_entrypoint_prints_character_count_for_ascii_text():
    result = run_entrypoint("--text", "hello")

    assert result.returncode == 0
    assert result.stdout == "5\n"


def test_entrypoint_prints_zero_for_empty_text():
    result = run_entrypoint("--text", "")

    assert result.returncode == 0
    assert result.stdout == "0\n"


def test_entrypoint_prints_character_count_for_japanese_text():
    text = "こんにちは"

    result = run_entrypoint("--text", text)

    assert result.returncode == 0
    assert result.stdout == f"{len(text)}\n"


def test_entrypoint_returns_non_zero_when_text_argument_is_missing():
    result = run_entrypoint()

    assert result.returncode != 0
