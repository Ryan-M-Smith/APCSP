#
# FILENAME: main.py | APCSP Tic-Tac-Toe Project
# DESCRIPTION: The main game loop
# CREATED: 2022-10-31 @ 2:17 PM
# COPYRIGHT: Copyright (c) 2022 by Ryan Smith
#

from ui import *
from tkinter import BOTH, Frame
from typing import List

def main():
	window = Window(title="Tic-Tac-Toe", height=620, width=600, theme="black")
	height, width = window.dimensions()

	window.protocol("WM_DELETE_WINDOW", lambda: sys.exit(0))

	frame = Frame(window, height=height, width=width)
	window.add_widget(frame)

	board = GridFrame(frame, height=height, width=width, borderwidth=1, relief="groove")
	window.add_widget(board, fillType=BOTH, expand=True)

	ROWS = COLUMNS = 3
	board_pieces = [
		[StringVar(value=Piece.BLANK) for _ in range(3)],
		[StringVar(value=Piece.BLANK) for _ in range(3)],
		[StringVar(value=Piece.BLANK) for _ in range(3)]
	]

	#last_clicked: Tuple[int, int]
	current_turn = StringVar(value=Piece.BLANK)

	# Add the board spaces
	for row in range(ROWS):
		for column in range(COLUMNS):
			button = BoardSpot(
				board, textvariable=board_pieces[row][column], command=None,
				current_val=current_turn, board_pieces=board_pieces
			)
			board.add_widget(button, row=row, column=column)

	current_turn.set(Piece.X)

	window.mainloop()
		

if __name__ == "__main__":
	import sys

	try:
		sys.exit(main())
	except KeyboardInterrupt:
		print("\nQuit")