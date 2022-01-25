"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730239487"
word_guess1: str = input("Enter a five character word: ")
if len(word_guess1) != 5:
    print("Error: Word must contain 5 characters")
    exit()
character_guess1: str = input("Enter a single character: ")
if len(character_guess1) != 1:
    print("Error: Character must be a single character")
    exit()
matching_characters: int = 0
print("Searching for " + character_guess1 + " in " + word_guess1)
if word_guess1[0] == character_guess1:
    print(character_guess1 + " found at index 0")
if word_guess1[1] == character_guess1:
    print(character_guess1 + " found at index 1")
if word_guess1[2] == character_guess1:
    print(character_guess1 + " found at index 2")
if word_guess1[3] == character_guess1:
    print(character_guess1 + " found at index 3")
if word_guess1[4] == character_guess1:
    print(character_guess1 + " found at index 4")
if word_guess1[0] == character_guess1:
    matching_characters = matching_characters + 1
if word_guess1[1] == character_guess1:
    matching_characters = matching_characters + 1
if word_guess1[2] == character_guess1:
    matching_characters = matching_characters + 1
if word_guess1[3] == character_guess1:
    matching_characters = matching_characters + 1
if word_guess1[4] == character_guess1:
    matching_characters = matching_characters + 1
if matching_characters == 0:
    print("No instances of " + character_guess1 + " found in " + word_guess1)
if matching_characters == 1:
    print("1 instances of " + character_guess1 + " found in " + word_guess1)
if matching_characters == 2:
    print("2 instances of " + character_guess1 + " found in " + word_guess1)
if matching_characters == 3:
    print("3 instances of " + character_guess1 + " found in " + word_guess1)
if matching_characters == 4:
    print("4 instances of " + character_guess1 + " found in " + word_guess1)
if matching_characters == 5:
    print("5 instances of " + character_guess1 + " found in " + word_guess1)