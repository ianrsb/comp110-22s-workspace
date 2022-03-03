"""Some examples of tender, loving function definitions."""


def Love(name: str) -> str:
    """Given a name as a parameter, returns a loving string."""
    return f"I love you {name}!"


def spread_Love(to: str, n: int) -> str:
    """Generates a string that repeats message n times."""
    love_note: str = ""
    i: int = 0
    while i < n:
        love_note += Love(to) + "\n"
        i += 1
    return love_note