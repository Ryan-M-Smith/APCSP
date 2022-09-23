#
# FILENAME: gradebookcalc.py | APCSP Gradebook Calculator Project
# DESCRIPTION: Calculate a student's average score from five grades
# CREATED: 2022-09-20 @ 11:50 AM
# COPYRIGHT: Copyright (c) 2022 by Ryan Smith
#

from typing import List

def get_grades() -> List[int]:
	""" Prompt the user to enter grades. """

	grades = list()
	for i in range(5):
		grade = -1 # An arbitary starting value not in the range [0, 10]
		
		#
		# When the user enters a grade, if they don't enter a number within the range,
		# or enter an invalid character (blank character, letter, etc.), they are prompted
		# to re-enter that number.
		#
		while grade not in range(11):
			try:
				print("\nPlease enter a grade between 0 and 10.")
				grade = int(input(f"Enter a grade ({i + 1} of 5): " ))
			except ValueError:
				print("\nInvalid input.", end="")
			else:
				if grade in range(11):
					grades.append(grade)
	
	return grades

def main() -> None:
	""" The main function. """

	print("Welcome to the Gradebook Calulator.")
	print("When prompted, you will enter five grades from 0 to 10 points.\n")
	
	# Prompt the user to enter grades
	grades = get_grades()

	# Calculate the overall percentage from those grades
	MAX_POINTS = 50
	total = sum(grades)
	percentage = total / MAX_POINTS * 100

	print(f"Overall percentage: {percentage}%")


if __name__ == "__main__":
	import sys

	try:
		sys.exit(main())
	except (EOFError, KeyboardInterrupt):
		print("\Quit.")
