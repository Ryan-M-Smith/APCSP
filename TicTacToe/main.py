#
# FILENAME: main.py | APCSP Tic-Tac-Toe Project
# DESCRIPTION: The main game loop
# CREATED: 2022-10-31 @ 2:17 PM
# COPYRIGHT: Copyright (c) 2022 by Ryan Smith
#

from ui import *
from tkinter import ttk, BOTH

def main():
	window = Window(title="Tic-Tac-Toe", height=620, width=600, theme="black")
	height, width = window.dimensions()

	frame = ttk.Frame(window, height=height, width=width)
	window.add_widget(frame)

	board = GridFrame(frame, height=height, width=width, borderwidth=1, relief="groove")
	window.add_widget(board, fillType=BOTH, expand=True)

	ROWS = COLUMNS = 3

	# Add the board spaces
	for row in range(ROWS):
		for column in range(COLUMNS):
			button = BoardSpot(board, textvariable=StringVar(), width=10, height=5)
			board.add_widget(button, row=row, column=column, ipadx=67, ipady=87)

	window.update()

if __name__ == "__main__":
	import sys

	try:
		sys.exit(main())
	except KeyboardInterrupt:
		print("\nQuit")