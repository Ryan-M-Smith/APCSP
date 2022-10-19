#
# FILENAME: surveyproject.py | APCSP Gradebook Calculator Project
# DESCRIPTION: Survey the user
# CREATED: 2022-09-28 @ 12:32 PM
# COPYRIGHT: Copyright (c) 2022 by Ryan Smith
#

def main() -> None:
	""" The main function. """

	# Name

	answer = input("What is your name? ").capitalize()
	MY_NAME = "Ryan"

	if answer == MY_NAME:
		print("We have the same name!")
	else:
		print(f"Nice to meet you, {answer}. My name is Ryan.")
	
	# Age

	age = -1
	MY_AGE = 17

	while age < 0:
		try:
			age = int(input("\nHow old are you? "))
		except ValueError:
			print("\nThat's not a real age", end="")
		else:
			if age >= 0 and age == MY_AGE:
				print("We're the same age.")
			elif age >= 0 and age != MY_AGE:
				print(f"That's cool. I'm {MY_AGE}.")
			else:
				print("\nThat's not a real age", end="")
	
	# Favorite color

	MY_FAVORITE_COLOR = "orange"
	favorite_color = input("\nWhat is your favorite color? ").lower()

	if favorite_color == MY_FAVORITE_COLOR:
		print("That's my favorite color too.")
	else:
		print(f"{favorite_color.capitalize()} is a good color. My favorite color is {MY_FAVORITE_COLOR}.")
	
	# Favorite ice cream flavor

	MY_FAVORITE_FLAVOR = "mint chocolate chip"
	favorite_flavor = input("\nWhat is your favorite ice cream flavor? ")

	if favorite_flavor == MY_FAVORITE_FLAVOR:
		print("That's my favorite flavor too.")
	else:
		print(f"Mmm, that sounds good! My favorite flavor is {MY_FAVORITE_FLAVOR}.")
	
	# Favorite day of the week

	MY_FAVORITE_DAY = "Tuesday"
	DAYS_OF_WEEK = [
		"Monday", "Tuesday", "Wednesday",
		"Thursday", "Friday", "Saturday",
		"Sunday"
	]
	favorite_day = str()

	while len(favorite_day) == 0 or favorite_day not in DAYS_OF_WEEK:
		favorite_day = input("\nWhat is your favorite day of the week? ").capitalize()

		if len(favorite_day) > 0 and favorite_day in DAYS_OF_WEEK:
			break
		else:
			print("That's not a day of the week.")
	
	if favorite_day == MY_FAVORITE_DAY:
		print(f"I like {MY_FAVORITE_DAY}s too!")
	else:
		print(f"That's cool. My favorite day of the week is {MY_FAVORITE_DAY}")
	
	print("\nThanks for taking the survey. Goodbye!")
		

if __name__ == "__main__":
	import sys
	
	try:
		sys.exit(main())
	except (KeyboardInterrupt, EOFError):
		print("\nQuitting...")