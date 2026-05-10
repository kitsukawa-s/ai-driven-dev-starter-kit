import argparse


def create_greeting(name: str) -> str:
    """Create a greeting message for the given name."""
    if name.strip() == "":
        raise ValueError("name must not be empty")

    return f"Hello, {name}!"


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Print a greeting message.")
    parser.add_argument("--name", required=True, help="Name to greet.")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    greeting = create_greeting(args.name)
    print(greeting)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
