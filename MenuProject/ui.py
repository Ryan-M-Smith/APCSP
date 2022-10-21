#
# FILENAME: ui.py | APCSP Menu Project
# DESCRIPTION: Load the TKinter GUI
# CREATED: 2022-10-19 @ 12:18 PM
# COPYRIGHT: Copyright (c) 2022 by Ryan Smith
#

from collections import namedtuple
from tkinter import ttk, BOTH
from typing import Literal
from ttkthemes import ThemedTk

class Window(ThemedTk):
	""" The main window of the application. """

	# Create named tuple to represent the window dimensions
	__dimensions = namedtuple("WinSize", ["height", "width"])

	def __init__(self, title: str = "Window", height: int = 500, width: int = 500) -> None:
		super().__init__(theme="black")

		self.title(title)
		self.geometry(f"{height}x{width}")

	def dimensions(self) -> __dimensions:
		return self.__dimensions(self.winfo_height(), self.winfo_width())

	@staticmethod
	def add_widget(widget: ttk.Widget, /, fillType: Literal = BOTH, expand: bool = True) -> None:
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
		widget: ttk.Widget, /, row: int = None, column: int = None,
		padx: int = None, pady: int = None, sticky: Literal = None
	) -> None:
		""" Add a widget to the application. """
		widget.grid(row=row, column=column, padx=padx, pady=pady, sticky=sticky)