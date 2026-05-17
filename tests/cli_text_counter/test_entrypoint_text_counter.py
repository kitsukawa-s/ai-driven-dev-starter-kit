from pathlib import Path
import sys

import pytest


ROOT_DIR = Path(__file__).resolve().parents[2]
SRC_DIR = ROOT_DIR / "src"
sys.path.insert(0, str(SRC_DIR))

from cli_text_counter.entrypoint import main, parse_args  # noqa: E402


def test_parse_args_accepts_text():
    args = parse_args(["--text", "hello"])

    assert args.text == "hello"


def test_main_prints_character_count_and_returns_zero(capsys):
    result = main(["--text", "hello"])

    captured = capsys.readouterr()
    assert result == 0
    assert captured.out == "5\n"


def test_main_raises_system_exit_when_text_argument_is_missing():
    with pytest.raises(SystemExit):
        main([])
