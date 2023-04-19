#
# FILENAME: draw.py | APCSP SmileyBugProject
# DESCRIPTION: The main function
# CREATED: 2023-03-20 @ 11:16 AM
# COPYRIGHT: Copyright (c) 2023 by Ryan Smith
#

import sys
from turtle import Turtle, Screen

from drawings import *

def main():
	""" The main function. """

	DRAWINGS = ("face", "spider", "ladybug")

	try:
		drawing = sys.argv[1].lower()
	except IndexError:
		raise SystemExit(f"Usage: {sys.argv[0]} drawing\n\tdrawing: \"face\", \"spider\", or \"ladybug\"")
	else:
		if drawing not in DRAWINGS:
			raise SystemExit(f"\"{drawing}\" cannot be drawn.\n\nUsage: {sys.argv[0]} drawing\n\tdrawing: \"face\", \"spider\", or \"ladybug\"")

	my_turtle = Turtle()
	my_turtle.hideturtle()

	if drawing == "face":
		draw_face(my_turtle)
	elif drawing == "spider":
		draw_spider(my_turtle)
	else:
		raise NotImplementedError(f"{drawing} has not been implemented.")

	window = Screen()

	window.mainloop()

if __name__ == "__main__":
	try:
		sys.exit(main())
	except KeyboardInterrupt:
		print("\nQuit.")