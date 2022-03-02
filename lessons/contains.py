"""Example of writing a function to search a list."""


def main() -> None:
    guess: str = input("what is the code word?")
    possible_answers: list[str] = ["pokemon", "wordle"]
    



def contains(needle: str, haystack: list[str]) -> bool:
    for item in haystack:
        if item == needle:
            return True
    return False