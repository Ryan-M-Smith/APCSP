#
# FILENAME: main.py | APCSP Menu Project
# DESCRIPTION: The main application
# CREATED: 2022-10-19 @ 12:26 PM
# COPYRIGHT: Copyright (c) 2022 by Ryan Smith
#

import locale
from tkinter import (
	CENTER, N, S, E, W, Y,
	StringVar, ttk
)

from ui import *
from commands import update_order, reset_order, place_order, warn_quit

def main():
	window = Window(title="Menu")
	height, width = window.dimensions()

	frame = ttk.Frame(window, height=height, width=width)
	window.add_widget(frame)

	MENU_ITEMS = {
		"Sandwich": 5.50,
		"Salmon": 7.50,
		"Hotdog": 7.99,
		"Hamburger": 10.45
	}

	#
	# Set mutable values the need the change throughout the program. These values can be changed elsewhere
	# in the program and update in real time. By default, these are assigned $0 currency values.
	#

	subtotal_var = StringVar()
	tax_var = StringVar()
	total_var = StringVar()
	current_value = StringVar()
	
	subtotal_var.set("$0.00")
	tax_var.set("$0.00")
	total_var.set("$0.00")

	# Allow prompting the user to place an order
	window.protocol("WM_DELETE_WINDOW", lambda: warn_quit(window, subtotal_var))

	# The default cost layout (for creating the table)
	DEFAULT_COSTS = {
		"Subtotal": subtotal_var,
		"Tax (6%)": tax_var,
		"Total": total_var
	}

	menu_grid = GridFrame(frame, height=height, width=width, borderwidth=1, relief="groove")
	window.add_widget(menu_grid, fillType=Y, expand=False)

	# Display the menu
	for index, pair in enumerate(MENU_ITEMS.items()):
		locale.setlocale(locale.LC_ALL, "")

		# Create a label for each item and its price
		item = ttk.Label(menu_grid, text=pair[0], justify=CENTER)
		price = ttk.Label(menu_grid, text=locale.currency(pair[1]), justify=CENTER)
		
		menu_grid.add_widget(item, row=index, column=0, padx=10, pady=10, sticky=N+S+E+W)
		menu_grid.add_widget(price, row=index, column=1, padx=10, pady=10, sticky=N+S+E+W)

	# Add some informational text
	label = ttk.Label(
		frame,
		text="Choose an item to add to your order from the dropdown box below.\nThen, use the buttons to add to or restart your order.",
		justify=CENTER, wraplength=475
	)
	window.add_widget(label, fillType=Y)

	# Create a grid of menu selection widgets
	selection_grid = GridFrame(frame, height=height, width=width)
	window.add_widget(selection_grid, fillType=Y)
	
	# Create a dropdown box of menu options
	current_value = StringVar()
	menu_options = ttk.OptionMenu(selection_grid, current_value, list(MENU_ITEMS.keys())[0], *MENU_ITEMS)
	selection_grid.add_widget(menu_options, row=0, column=0, padx=5, sticky=N+S+E+W)

	# Create a button to add menu items to the order
	add_button = ttk.Button(
		selection_grid, text="Add to Order",
		command=lambda: update_order(subtotal_var, tax_var, total_var, MENU_ITEMS[current_value.get()])
	)
	selection_grid.add_widget(add_button, row=0, column=1, padx=5)

	# Create a buton to submit the order
	submit_button = ttk.Button(
		selection_grid, text="Place Order",
		command=lambda: place_order(subtotal_var, tax_var, total_var)
	)
	selection_grid.add_widget(submit_button, row=0, column=2, padx=5)

	# Create a button to reset the order
	reset_button = ttk.Button(
		selection_grid, text="Reset Order",
		command=lambda: reset_order(subtotal_var, tax_var, total_var)
	)
	selection_grid.add_widget(reset_button, row=0, column=3)

	# Create a table of price information
	for index, pair in enumerate(DEFAULT_COSTS.items()):
		locale.setlocale(locale.LC_ALL, "")

		# Create a label for each cost and a label for the amount owed per category
		title = ttk.Label(selection_grid, text=pair[0], justify=CENTER)
		amount = ttk.Label(selection_grid, textvariable=pair[1], justify=CENTER)
		
		selection_grid.add_widget(title, row=index + 2, column=0, padx=10, pady=10, sticky=E+W)
		selection_grid.add_widget(amount, row=index + 2, column=1, padx=10, pady=10, sticky=E+W)

	window.update() # Display all the widgets in the window

if __name__ == "__main__":
	import sys

	try:
		sys.exit(main())
	except KeyboardInterrupt:
		sys.exit(0)