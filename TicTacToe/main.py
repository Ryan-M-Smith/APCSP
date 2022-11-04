#
# FILENAME: main.py | APCSP Tic-Tac-Toe Project
# DESCRIPTION: The main game loop
# CREATED: 2022-10-31 @ 2:17 PM
# COPYRIGHT: Copyright (c) 2022 by Ryan Smith
#

from ui import *
from tkinter import ttk, BOTH
from typing import List

def check_win(board_data: List[List[BoardSpot]], piece: str) -> bool:
	# Convert the 2D array into a 1D array
	linear_board = [piece.get_piece() for row in board_data for piece in row]

	WIN_POSSIBILITIES = [
		# Rows
		[0, 1, 2],
		[3, 4, 5],
		[6, 7, 8],

		# Columns
		[0, 3, 6],
		[1, 4, 7],
		[2, 5, 8],

		# Diagonals
		[0, 4, 8],
		[2, 4, 6]
	]

	for i in range(len(WIN_POSSIBILITIES)):
		win = (
			linear_board[WIN_POSSIBILITIES[i][0]] ==
			linear_board[WIN_POSSIBILITIES[i][1]] ==
			linear_board[WIN_POSSIBILITIES[i][2]] ==
			piece
		)

		if win:
			return True

def move_is_valid(board_data: List[List[str]], row: int, column: int) -> bool:
	return len(board_data[row][column]) == 0

def main():
	window = Window(title="Tic-Tac-Toe", height=620, width=600, theme="black")
	height, width = window.dimensions()

	frame = ttk.Frame(window, height=height, width=width)
	window.add_widget(frame)

	board = GridFrame(frame, height=height, width=width, borderwidth=1, relief="groove")
	window.add_widget(board, fillType=BOTH, expand=True)

	ROWS = COLUMNS = 3

	board_data: List[List[BoardSpot]] = [[], [], []]

	# Add the board spaces
	for row in range(ROWS):
		for column in range(COLUMNS):
			button = BoardSpot(board, textvariable=StringVar(), command=None)
			board.add_widget(button, row=row, column=column, ipadx=67, ipady=87)
			board_data[row].append(button)

	window.update()

	current_turn = StringVar(Piece.X)
	while not (check_win(Piece.X) or check_win(Piece.O)):
		pass

if __name__ == "__main__":
	import sys

	try:
		sys.exit(main())
	except KeyboardInterrupt:
		print("\nQuit")