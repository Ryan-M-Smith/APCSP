#
# FILENAME: dragonadventureproject.py | APCSP Dragon Adventure Project
# DESCRIPTION: A text-based dragon adventure game
# CREATED: 2022-10-13 @ 3:39 PM
# COPYRIGHT: Copyright (c) 2022 by Ryan Smith
#

import random, sys, time
from typing import NoReturn

def main() -> NoReturn:
	INTRO = [
		"Welcome adventurer.",
		"You have now arrvied on the Island of Many Caves.",
		"Within the caves in front of you, there lie two paths.",
		"Along one of those paths there lives an Exotic Fire Dragon; one of the\ndeadliest dragons ever.",
		"Along the other lies great treasure!"
	]
	
	for sentence in INTRO:
		print(sentence)
		time.sleep(3)
	
	answer = input("Are you up to the task (y/n)? ").lower()

	if answer == "yes" or answer == "y":
		print("Good luck, adventurer!")
	else:
		print("You are not worthy, coward.")
		sys.exit(0)

	while True:
		print("\nYou are now approaching the two caves.")
		direction = input("Do you want to go left or right? ").lower()

		random.seed(time.time())
		DRAGON_POSITION = "left" if random.randint(1, 100) > 50 else "right"

		print("\nTravelling through the cave...")
		time.sleep(random.randint(2, 5))

		if direction == DRAGON_POSITION:
			print("You were eaten by the dragon.")
		else:
			print("You found the treasure! Congratulations!")
		
		answer = input("\nWould you like to play again (y/n)? ")
		if answer == "no" or answer == "n":
			break
	
	sys.exit()


if __name__ == "__main__":
	try:
		sys.exit(main())
	except (EOFError, KeyboardInterrupt):
		print("\nQuit.")