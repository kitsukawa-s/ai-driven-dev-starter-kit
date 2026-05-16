from pathlib import Path
import sys

import pytest


ROOT_DIR = Path(__file__).resolve().parents[2]
SRC_DIR = ROOT_DIR / "src"
sys.path.insert(0, str(SRC_DIR))

from cli_hello_greeting.entrypoint import main, parse_args  # noqa: E402


def test_parse_args_accepts_name():
    args = parse_args(["--name", "Alice"])

    assert args.name == "Alice"


def test_main_prints_greeting_and_returns_zero(capsys):
    result = main(["--name", "Alice"])

    captured = capsys.readouterr()
    assert result == 0
    assert captured.out == "Hello, Alice!\n"


def test_main_raises_system_exit_when_name_is_missing():
    with pytest.raises(SystemExit):
        main([])
