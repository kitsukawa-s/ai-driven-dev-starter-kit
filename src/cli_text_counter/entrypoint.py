import argparse

try:
    from cli_text_counter.features.text_counter import count_characters
except ModuleNotFoundError:
    from features.text_counter import count_characters


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Count characters in text.")
    parser.add_argument("--text", required=True, help="Input text.")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    result = count_characters(args.text)
    print(result)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
