#
# FILENAME: ui.py | APCSP Menu Project
# DESCRIPTION: Load the TKinter GUI
# CREATED: 2022-10-19 @ 12:18 PM
# COPYRIGHT: Copyright (c) 2022 by Ryan Smith
#

from collections import namedtuple
from typing import (
	Literal, Optional, Type,
	Any, Callable, List
)

from tkinter import (
	ttk, BOTH, StringVar, Misc,
	font, Button, Frame, messagebox
)
from ttkthemes import ThemedTk

class Window(ThemedTk):
	""" The main window of the application. """

	# Create named tuple to represent the window dimensions
	__dimensions = namedtuple("WinSize", ["height", "width"])

	def __init__(self, title: str = "Window", height: int = 500, width: int = 500, theme: str = None) -> None:
		super().__init__(theme=theme)

		self.title(title)
		self.geometry(f"{height}x{width}")

	def dimensions(self) -> __dimensions:
		return self.__dimensions(self.winfo_height(), self.winfo_width())

	@staticmethod
	def add_widget(widget: ttk.Widget, *, fillType: Literal = BOTH, expand: bool = True) -> None:
		""" Add a widget to the application. """
		widget.pack(fill=fillType, expand=expand)
	
	def update(self) -> None:
		""" Update the screen with widgets. """
		self.mainloop()

class GridFrame(Frame):
	""" A frame that holds a grid of objects. """

	# Create named tuple to represent the window dimensions
	__dimensions = namedtuple("FrameSize", ["height", "width"])

	def __init__(
		self, parent: ttk.Widget, height: int = 500, width: int = 500,
		borderwidth: int = None, relief: str = None
	) -> None:
		super().__init__(parent, height=height, width=width, borderwidth=borderwidth, relief=relief)
	
	def dimensions(self) -> __dimensions:
		return self.__dimensions(self.winfo_height(), self.winfo_width())

	@staticmethod
	def add_widget(
		widget: ttk.Widget, *, row: int = None, column: int = None,
		padx: int = None, pady: int = None, ipadx: int = None, ipady: int = None,
		sticky: Literal = None
	) -> None:
		""" Add a widget to the application. """
		widget.grid(row=row, column=column, padx=padx, pady=pady, ipadx=ipadx, ipady=ipady, sticky=sticky)

class Piece:
	X, O, BLANK = "X", "O", "  "

class BoardSpot(Button):
	""" A spot on the game board. """

	__piece: Optional[str] = None
	__text: StringVar
	__current_val: StringVar

	def __init__(
		self, master: Misc | None, *, command: Type[str] | Callable[..., Any],
		default: Literal["normal", "active", "disabled"] = "normal", image: Any = None,
		state: str = "active", text: float | str | None = None, textvariable: StringVar = None,
		current_val: StringVar = None,
		board_pieces: List[List[StringVar]] = None
	) -> None:
		self.__text = textvariable
		self.__current_val = current_val

		btn_font = font.Font(family='Helvetica', size=24)

		super().__init__(
			master, command=lambda: self.set_piece(current_val.get(), board_pieces), default=default,
			padx=85, pady=75, image=image, state=state,
			text=text, textvariable=self.__text,
			font=btn_font
		)
	
	def disable(self) -> None:
		self["state"] = "disabled"

	def set_piece(self, piece: str, board: List[List[StringVar]]) -> None:
		self.__piece = piece
		self.__text.set(self.__piece)

		win = self.__check_win(board, self.__current_val.get())

		if win:
			messagebox.askokcancel(title="Results", message=f"{self.__current_val.get()} Won")
		elif not win and (Piece.BLANK not in [piece.get() for row in board for piece in row]):
			messagebox.askokcancel(title="Results", message="Tie")

		self.__current_val.set("O" if self.__current_val.get() == "X" else "X")
		self.disable()

	
	def get_piece(self) -> str:
		return self.__piece
	
	@staticmethod
	def __check_win(board: List[List[StringVar]], piece: str) -> bool:
		# Convert the 2D array into a 1D array
		linear_board = [piece.get() for row in board for piece in row]

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
	
