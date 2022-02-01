"""EX02 One Shot Wordle- One Step at a time."""

__author__ = "730239487"
secret: str = "python"
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
indstring: str = ""
word_guess1: str = input(f"What is your {len(secret)}-letter guess? ")
while len(word_guess1) != len(secret):
    word_guess1: str = input(f"That was not {len(secret)}-letters! Try again: ")  
if len(word_guess1) == len(secret):
    i: int = 0
    while len(secret) > len(indstring):
        if word_guess1[i] == secret[i]:
            indstring = indstring + GREEN_BOX
        if word_guess1[i] != secret[i]:
            indstring = indstring + WHITE_BOX
        i = i + 1 
    print(indstring)
    if word_guess1 == secret:
        print("Woo! You got it!")
        exit()
    if (word_guess1) != secret:
        print("Not quite. Play again soon!")
        exit()