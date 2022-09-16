#
# FILENAME: main.py | APCSP Interview Project
# DESCRIPTION: Interview the user
# CREATED: 2022-09-09 @ 11:22 AM
# COPYRIGHT: Copyright (c) 2022 by Ryan Smith
#

import os, time

def clear(timeout: int = 0) -> None:
	""" Clear the console. """

	time.sleep(timeout)
	os.system("clear")

def main():
	""" The main function. """

	start = str()
	while start not in ("y", "n"):
		start = input("Welcome to the interview. Would you like to continue (y/n)? ").lower()

	if start == "n":
		print("Goodbye.")
		return
	
	clear()

	print("We have seven questions for you.")
	clear(2)

	# Name
	name = input("What is your name?\n>>> ").capitalize()
	print(f"\nHello, {name}! Nice to meet you!")
	clear(2)

	# Favorite food
	fav_food = input("What is your favorite food?\n>>> ")
	print(f"\nThey serve {fav_food} at the restaurant down the street.")
	clear(2)
	
	# Age
	age = int(input("How old are you?\n>>> "))
	MY_AGE = 17

	if age > MY_AGE:
		print("\nYou're older than me.")
	elif age < MY_AGE:
		print("\nYou're younger than me.")
	else:
		print("\nWe're the same age!")

	clear(2)

	# If you could live anywhere
	new_home = input("If you could live anywhere, where would it be?\n>>> ").capitalize()
	print(f"\n{new_home} sounds like a great place to live.")
	clear(2)

	# Favorite zoo animal
	new_home = input("What's your favorite zoo animal?\n>>> ").capitalize()
	print("\nI wish I could have one as a pet.")
	clear(2)

	# Introvert/extrovert
	personality = input("Are you an introvert or an extrovert?\n>>> ").lower()
	MY_PERSONALITY = "extrovert"

	if personality == MY_PERSONALITY:
		print("\nI'm an extrovert too!")
	else:
		print("\nI'm an extrovert, but introverts are just as cool.")
	
	clear(2)

	# Favorite number
	fav_number = int(input("What is your favorite number?\n>>> "))
	MY_FAV_NUM = 144
	
	if fav_number == MY_FAV_NUM:
		print("\nWe have the same favorite number!")
	else:
		print(f"\n{fav_number} is a good number. My favorite number is 144.")

	clear(2)
	
	print("Thanks for letting us interview you. Goodbye!")

if __name__ == "__main__":
	import sys
	
	try:
		sys.exit(main())
	except (EOFError, KeyboardInterrupt):
		print("\nGoodbye!")