from pathlib import Path
import sys


ROOT_DIR = Path(__file__).resolve().parents[3]
SRC_DIR = ROOT_DIR / "src"
sys.path.insert(0, str(SRC_DIR))

from cli_text_counter.features.text_counter import count_characters


def test_count_characters_returns_length_for_ascii_text():
    assert count_characters("hello") == 5


def test_count_characters_returns_zero_for_empty_text():
    assert count_characters("") == 0


def test_count_characters_returns_length_for_japanese_text():
    text = "こんにちは"

    assert count_characters(text) == len(text)


def test_count_characters_counts_spaces():
    text = "hello world"

    assert count_characters(text) == len(text)
