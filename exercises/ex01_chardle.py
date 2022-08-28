"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730559969"

from operator import countOf
from socket import if_indextoname


fivechar_word: str = input("Enter a 5-character word:")
if len(fivechar_word) != 5:
    print("Error: Word must contain 5 characters")
    exit()
single_char: str = input("Enter a single character:")
if len(single_char) != 1:
    print("Error: Character must be a single character")
    exit()
print("Searching for " + single_char + " in " + fivechar_word)
character_match: int = int(0)
if single_char == fivechar_word[0]:
    print("Found at index 0")
    character_match = character_match + 1
if single_char == fivechar_word[1]:
    print("Found at index 1")
    character_match = character_match + 1
if single_char == fivechar_word[2]:
    print("Found at index 2")
    character_match = character_match + 1
if single_char == fivechar_word[3]:
    print("Found at index 3")
    character_match = character_match + 1
if single_char == fivechar_word[4]:
    print("Found at index 4")
    character_match = character_match + 1
if character_match == 0:
    print("No instances of " + single_char + " found in " + fivechar_word)
if character_match == 1:
    print(str(character_match) + " instance of " + single_char + " found in " + fivechar_word)
if character_match >1:
    print(str(character_match) + " instances of " + single_char + " found in " + fivechar_word)


