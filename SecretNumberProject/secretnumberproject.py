#
# FILENAME: secretnumberprokect.py | APCSP Secret Number Project
# DESCRIPTION: A secret number-guessing game
# CREATED: 2022-10-22 @ 2:01 PM
# COPYRIGHT: Copyright (c) 2022 by Ryan Smith
#

import random, time

def main():
	random.seed(time.time())
	SECRET_NUMBER = random.randint(1, 5)
	guess = guesses = 0

	while guess != SECRET_NUMBER:
		try:
			guess = int(input("Guess a number between 1 and 5: "))
		except ValueError:
			print("\nInvalid input.")
		else:
			if guess not in range(1, 6):
				print("\nPlease enter a number between 1 and 5.")
				continue
			
			guesses += 1

			if guess > SECRET_NUMBER:
				print("\nYour guess was too high.")
			elif guess < SECRET_NUMBER:
				print("\nYour guess was too low.")
			else:
				break
	
	print(f"\nYou guessed the number! It was {SECRET_NUMBER}.")
	print(f"Guesses made: {guesses}")		

if __name__ == "__main__":
	import sys
	
	try:
		sys.exit(main())
	except (KeyboardInterrupt, EOFError):
		print("\nQuit")