"""EX02 - One Shot Wordle- One Step at a time."""

__author__ = "730239487"

secret: str = "python"  # secret variable is defined
word_guess1: str = input(f"What is your {len(secret)}-letter guess? ")  # asks user for input to guess the variable
while len(word_guess1) != len(secret):  # this creates a loop where the user will be asked for a proper lengthed guess until the proper length is given
    word_guess1: str = input(f"That was not {len(secret)}-letters! Try again: ")
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
indstring: str = ""
if len(word_guess1) == len(secret):  # this makes it such that the typical wordle boxes print before the final text
    i: int = 0
    while len(secret) > len(indstring):
        if word_guess1[i] == secret[i]:
            indstring = indstring + GREEN_BOX
        if word_guess1[i] != secret[i]:
            indstring = indstring + WHITE_BOX
        i = i + 1  # this makes the loop close and work towards changing what the status of the while satement from true to false
    print(indstring)
    if word_guess1 == secret:
        print("Woo! You got it!")
    if (word_guess1) != secret:
        print("Not quite. Play again soon!")