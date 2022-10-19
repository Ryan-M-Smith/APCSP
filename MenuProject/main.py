#
# FILENAME: main.py | APCSP Menu Project
# DESCRIPTION: The main application
# CREATED: 2022-10-19 @ 12:26 PM
# COPYRIGHT: Copyright (c) 2022 by Ryan Smith
#

from tkinter import ttk
from ui import Window

def main():
	window = Window(title="Menu")
	width, height = window.get_dimensions()

	menu = ttk.Frame(window, height=height, width=width)
	window.add_widget(menu)

	MENU_ITEMS = {
		"Sandwich": 5.50,
		"Salmon": 7.50,
		"Fried Chicken": 7.99,
		"Hamburger": 10.45
	}

	for food, price in MENU_ITEMS.items():
		item = ttk.Label(menu, text=f"{food}\t${price}")
		window.add_widget(item)

	window.update()
	

if __name__ == "__main__":
	import sys

	try:
		sys.exit(main())
	except KeyboardInterrupt:
		sys.exit(0)