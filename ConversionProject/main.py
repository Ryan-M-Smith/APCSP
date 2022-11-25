#
# FILENAME: main.py | APCSP Conversion Project
# DESCRIPTION: The main application
# CREATED: 2022-11-15 @ 10:02 PM
# COPYRIGHT: Copyright (c) 2022 by Ryan Smith
#

from typing import Optional
from tkinter import StringVar, ttk, X

from ui import GridFrame, Window

def dec_to_bin(dec: int) -> Optional[str]:
	""" Convert decimal to binary. """

	try:
		return bin(dec).replace("0b", "")
	except TypeError:
		return None

def bin_to_dec(bits: str) -> int:
	""" Convert binary to decimal. """

	try:
		return int(bits, base=2)
	except ValueError:
		return None
	

def convert(value: str, display_var: StringVar) -> None:
	result = display_var.get()

	try:
		if all(int(digit) in range(10) for digit in value) and "Decimal" not in display_var.get():
			result = f"Binary: {dec_to_bin(int(value)).zfill(8)}"
		elif all(int(digit) in (0, 1) for digit in value):
			result = f"Decimal: {bin_to_dec(value)}"
	except ValueError:
		pass
	else:
		display_var.set(result)

def main():
	window = Window(title="Convert between Decimal and Binary", theme="black", width=300, height=200)
	width, height = window.dimensions()

	frame = ttk.Frame(window, height=height, width=width)
	window.add_widget(frame)

	#
	# Decimal to binary conversion section
	#

	title1 = ttk.Label(frame, text="Convert Decimal to Binary")
	title1.pack(expand=False)

	subtitle1 = ttk.Label(frame, text="Enter a decimal number below")
	subtitle1.pack(expand=False)

	binary_result = StringVar(frame, value="Binary: 0")
	result1 = ttk.Label(frame, textvariable=binary_result)

	dtob_frame = GridFrame(frame, borderwidth=1, relief="flat")
	dtob_frame.pack(expand=False)

	decimal_num = ttk.Entry(dtob_frame)
	button1 = ttk.Button(dtob_frame, text="Convert", command=lambda: convert(decimal_num.get(), binary_result))

	dtob_frame.add_widget(decimal_num, row=0, column=0)
	dtob_frame.add_widget(button1, row=0, column=2)

	result1.pack(expand=False)

	# Add a separator between the sections
	separator = ttk.Separator(frame, orient='horizontal')
	separator.pack(fill=X)

	#
	# Binary to decimal conversion section
	#

	title2 = ttk.Label(frame, text="Convert Binary to Decimal")
	title2.pack(expand=False)

	subtitle2 = ttk.Label(frame, text="Enter a binary number below")
	subtitle2.pack(expand=False)

	decimal_result = StringVar(frame, value="Decimal: 0")
	result2 = ttk.Label(frame, textvariable=decimal_result)

	btod_frame = GridFrame(frame, borderwidth=1, relief="flat")
	btod_frame.pack(expand=False)

	binary_num = ttk.Entry(btod_frame)
	button2 = ttk.Button(btod_frame, text="Convert", command=lambda: convert(binary_num.get(), decimal_result))

	btod_frame.add_widget(binary_num, row=0, column=0)
	btod_frame.add_widget(button2, row=0, column=2)

	result2.pack(expand=False)

	window.update()

if __name__ == "__main__":
	import sys

	try:
		sys.exit(main())
	except KeyboardInterrupt:
		print("\nQuit.")