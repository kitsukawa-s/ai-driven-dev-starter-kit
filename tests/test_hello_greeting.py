from pathlib import Path
import sys

import pytest


ROOT_DIR = Path(__file__).resolve().parents[1]
SRC_DIR = ROOT_DIR / "src"
sys.path.insert(0, str(SRC_DIR))

from hello_greeting import create_greeting, main  # noqa: E402


def test_create_greeting_returns_message_for_alice():
    assert create_greeting("Alice") == "Hello, Alice!"


def test_create_greeting_returns_message_for_japanese_name():
    assert create_greeting("太郎") == "Hello, 太郎!"


def test_create_greeting_raises_value_error_for_empty_name():
    with pytest.raises(ValueError):
        create_greeting("")


def test_create_greeting_raises_value_error_for_blank_name():
    with pytest.raises(ValueError):
        create_greeting("   ")


def test_main_prints_greeting_and_returns_zero(capsys):
    result = main(["--name", "Alice"])

    captured = capsys.readouterr()
    assert result == 0
    assert captured.out == "Hello, Alice!\n"


def test_main_raises_system_exit_when_name_is_missing():
    with pytest.raises(SystemExit):
        main([])
