def create_greeting(name: str) -> str:
    """Create a greeting message for the given name."""
    if name.strip() == "":
        raise ValueError("name must not be empty")

    return f"Hello, {name}!"
