#
# FILENAME: ui.py | APCSP Menu Project
# DESCRIPTION: Load the TKinter GUI
# CREATED: 2022-10-19 @ 12:18 PM
# COPYRIGHT: Copyright (c) 2022 by Ryan Smith
#

from tkinter import ttk
from typing import Tuple
from ttkthemes import ThemedTk

class Window(ThemedTk):
	""" The main window of the application. """

	def __init__(self, title: str = "Window", length: int = 500, width: int = 500) -> None:
		super().__init__(theme="yaru")

		self.title(title)
		self.geometry(f"{length}x{width}")

	def get_dimensions(self) -> Tuple[int, int]:
		return self.winfo_width(), self.winfo_height()

	@staticmethod
	def add_widget(widget: ttk.Widget) -> None:
		""" Add a widget to the application. """
		widget.pack()
	
	def update(self) -> None:
		""" Update the screen with widgets. """
		self.mainloop()