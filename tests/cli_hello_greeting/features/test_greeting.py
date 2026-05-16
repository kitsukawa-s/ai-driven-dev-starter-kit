from pathlib import Path
import sys

import pytest


ROOT_DIR = Path(__file__).resolve().parents[3]
SRC_DIR = ROOT_DIR / "src"
sys.path.insert(0, str(SRC_DIR))

from cli_hello_greeting.features.greeting import create_greeting


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
