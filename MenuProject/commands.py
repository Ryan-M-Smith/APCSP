#
# FILENAME: commands.py | APCSP Menu Project
# DESCRIPTION: GUI Button actions 
# CREATED: 2022-10-20 @ 11:46 PM
# COPYRIGHT: Copyright (c) 2022 by Ryan Smith
#

import locale
from typing import Tuple

from tkinter import StringVar, messagebox
from ui import Window

def __calculate_prices(subtotal: float, itemPrice: float) -> Tuple[float, float, float]:
	""" Calculate the subtotal, tax, and total price based on a new item added to the order. """

	new_subtotal = subtotal + itemPrice
	tax = new_subtotal * 0.06 # In Maryland, 6% sales tax is charged
	total = new_subtotal + tax

	return new_subtotal, tax, total

def update_order(subtotal: StringVar, tax: StringVar, total: StringVar, itemPrice: float) -> None:
	""" Update the user's order on the screen. """

	# Convert the currency into a floating point number
	locale.setlocale(locale.LC_ALL, "en_US")
	subtotal_val = locale.atof(subtotal.get().strip("$"))

	# Calculate the new prices
	new_subtotal, new_tax, new_total = __calculate_prices(subtotal_val, itemPrice)

	# Convert the floating point numbers into currencies
	subtotal.set(locale.currency(new_subtotal))
	tax.set(locale.currency(new_tax))
	total.set(locale.currency(new_total))

def reset_order(subtotal: StringVar, tax: StringVar, total: StringVar) -> None:
	""" Reset the user's order. """

	# Resetting everything to zero effectively deletes the order
	subtotal.set(locale.currency(0.0))
	tax.set(locale.currency(0.0))
	total.set(locale.currency(0.0))

def place_order(subtotal: StringVar, tax: StringVar, total: StringVar) -> None:
	""" Prompt the user to place their order. """

	answer = messagebox.askokcancel(title="Order confirmation", message=f"Would you like to place an order for {subtotal.get()}?")
	if answer:
		reset_order(subtotal, tax, total)
		messagebox.showinfo(title="Information", message="Order placed successfully.")

def warn_quit(window: Window, subtotal: StringVar) -> None:
	"""
		If the user tries to quit after adding food to their order, prompt them to place the
		order before quitting the app.
	"""

	locale.setlocale(locale.LC_ALL, "en_US")

	if locale.atof(subtotal.get().strip("$")) == 0:
		window.destroy()
	else:
		answer = messagebox.askyesno(title="Confirm quit",  message="Are you sure you want to quit without placing your current order?")
		
		if answer:
			window.destroy()

