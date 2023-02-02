#
# FILENAME: main.py | APCSP Car Wash Project
# DESCRIPTION: Clean and print diagnostic information about user-entered data
# CREATED: 2022-11-30 @ 12:04 PM
# COPYRIGHT: Copyright (c) 2022 by Ryan Smith
#

from typing import List

import string

def display_options() -> int:
	""" Display the string cleaning options. """

	choice = 0

	while choice == 0 and choice not in range(1, 5):
		print("\nWhat would you like to do?")
		print("1. Convert text to uppercase")
		print("2. Convert text to lowercase")
		print("3. Split string into words")
		print("4. Split string into characters")
		print("5. Remove whitespace")
		
		try:
			choice = int(input(">>> "))
		except ValueError:
			print("\nInvalid entry.")
		else:
			if choice not in range(1, 6):
				print("\nInvalid entry.")
			else:
				return choice

def print_diagnostics(text: str) -> None:
	""" Print information about the string. """

	# Print a single newline
	print("\n", end="")
	
	if len(text) == 0:
		print("The string is empty")
		return

	if text.isupper():
		print("Case: all uppercase")
	elif text.islower():
		print("Case: all lowercase")
	elif text.istitle():
		print("Case: title case")
	
	if text.isalpha():
		print("Character set: alphabetic")
	elif text.isnumeric():
		print("Character set: numeric")
	elif text.isalnum():
		print("Character set: alphanumeric")
	elif text.isspace():
		print("Character set: whitespace characters")
	else:
		print("Character set: other")
		
	VOWELS = ("a", "e", "i", "o", "u")
	
	# Generate  a list of consonants 
	letters = string.ascii_lowercase
	for vowel in VOWELS:
		letters = letters.replace(vowel, "")
	
	CONSONANTS = tuple([letter for letter in letters])

	if text.startswith(VOWELS):
		print("Your string starts with a vowel")
	elif text.startswith(CONSONANTS):
		print("Your string starts with a consonant")
	
	if text.endswith(VOWELS):
		print("Your string ends with a vowel")
	elif text.endswith(CONSONANTS):
		print("Your string ends with a consonant")
	else:
		print("Your string ends with a number or special character")
	

def parse_choice(choice: int, text: str) -> str | List[str]:
	""" Parse the user's choice. """

	if choice == 1:
		return text.upper()	
	elif choice == 2:
		return text.lower()
	elif choice == 3:
		return text.split()
	elif choice == 4:
		return [c for c in text if c != " "]
	elif choice == 5:
		# Replace spaces and tabs with empty strings
		return text.strip().replace(" ", "").replace("\t", "")

def main() -> None:
	""" The main function. """

	text = input("Enter some text to clean: ")

	print_diagnostics(text)

	choice = display_options()
	print(f"\nResult: {parse_choice(choice, text)}")

if __name__ == "__main__":
	import sys

	try:
		sys.exit(main())
	except (KeyboardInterrupt, IOError):
		print("\nQuit.")