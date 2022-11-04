#
# FILENAME: ui.py | APCSP Menu Project
# DESCRIPTION: Load the TKinter GUI
# CREATED: 2022-10-19 @ 12:18 PM
# COPYRIGHT: Copyright (c) 2022 by Ryan Smith
#

from collections import namedtuple
from typing import Literal, Optional, Type, Any, Callable

from tkinter import (
	ttk, BOTH, StringVar, Misc,
	Variable, font, Button
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

class GridFrame(ttk.Frame):
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
	X, O = "X", "O"

class BoardSpot(ttk.Button):
	""" A spot on the game board. """

	__piece: Optional[str] = None
	__text: StringVar

	def __init__(
		self, master: Misc | None, *, command: Type[str] | Callable[..., Any],
		default: Literal["normal", "active", "disabled"] = "normal", image: Any = None,
		state: str = "active", text: float | str | None = None, textvariable: Variable = None
	) -> None:
		self.__text = textvariable
		super().__init__(
			master, command=command, default=default,
			image=image, state=state, text=text, textvariable=self.__text
		)
	
	def disable(self) -> None:
		self["state"] = "disabled"

	def set_piece(self, piece: str) -> None:
		self.__piece = piece
		self.__text.set(self.__piece)
	
	def get_piece(self) -> str:
		return self.__piece
	
