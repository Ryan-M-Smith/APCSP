from ui import Window
from tkinter import Listbox, Frame, Button, simpledialog

def add_item(list_box: Listbox) -> None:
	""" Add an item to the list. """

	if result := simpledialog.askstring(title="Dialog", prompt="Enter a new list item"):
		list_box.insert(list_box.size(), result)

def delete_item(list_box: Listbox) -> None:
	""" Remove an item from the list. """

	# Only one item can be selewcted at a time, so it's safe to get the first index
	# in the tuple.	
	if len(selection := list_box.curselection()) > 0:
		list_box.delete(selection[0])

def clear_list(list_box: Listbox) -> None:
	""" Clear the list. """
	list_box.delete(0, list_box.size() - 1)

def main() -> None:
	window = Window(title="To-Do List", theme="black", width=500, height=215)
	width, height = window.dimensions()

	frame = Frame(window, height=height, width=width)
	window.add_widget(frame)

	todo_list = Listbox(frame)
	window.add_widget(todo_list)

	button_frame = Frame(frame, height=height, width=width)
	window.add_widget(button_frame)
	
	add_button = Button(button_frame, text="Add Item", command=lambda: add_item(todo_list))
	add_button.grid(row=0, column=0)

	delete_button = Button(button_frame, text="Delete Item", command=lambda: delete_item(todo_list))
	delete_button.grid(row=0, column=1)

	clear_button = Button(button_frame, text="Clear List", command=lambda: clear_list(todo_list))
	clear_button.grid(row=0, column=2)

	window.update()

if __name__ == "__main__":
	import sys

	try:
		sys.exit(main())
	except KeyboardInterrupt:
		print("\nQuit.")