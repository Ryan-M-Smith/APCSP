#
# FILENAME: main.py | APCSP Menu Project
# DESCRIPTION: The main application
# CREATED: 2022-10-19 @ 12:26 PM
# COPYRIGHT: Copyright (c) 2022 by Ryan Smith
#

import locale

from tkinter import StringVar, ttk
from ui import Window

def main():
	window = Window(title="Menu")
	width, height = window.get_dimensions()

	menu = ttk.Frame(window, height=height, width=width)
	window.add_widget(menu)

	MENU_ITEMS = {
		"Sandwich": 5.50,
		"Salmon     ": 7.50, # Add in some extra spaces to make things look nicer
		"Fried Chicken": 7.99,
		"Hamburger": 10.45
	}

	label = ttk.Label(window, text="Choose an item to add to your order.")
	window.add_widget(label)

	# Set a default value for the menu dropdown
	default_val = StringVar(window)
	default_val.set("Sandwich")

	menu_options = ttk.OptionMenu(window, default_val, *MENU_ITEMS)
	window.add_widget(menu_options)

	# Display the menu
	for food, price in MENU_ITEMS.items():
		locale.setlocale(locale.LC_ALL, '')

		item = ttk.Label(menu, text=f"{food}\t{locale.currency(price, grouping=True)}")
		window.add_widget(item)

	window.update()

if __name__ == "__main__":
	import sys

	try:
		sys.exit(main())
	except KeyboardInterrupt:
		sys.exit(0)