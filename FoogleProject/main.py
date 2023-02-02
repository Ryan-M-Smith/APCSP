from ui import Window, GridFrame
from tkinter import ttk
import webbrowser

def search(query: str) -> None:
	webbrowser.open(f"https://google.com/search?q={'+'.join(query.split())}")

def main():
	window = Window(title="Foogle", theme="black", width=400, height=50)
	width, height = window.dimensions()

	frame = ttk.Frame(window, height=height, width=width)
	window.add_widget(frame)

	title1 = ttk.Label(frame, text="Enter something to search on Google")
	title1.pack(expand=False)

	search_field = GridFrame(frame, borderwidth=1, relief="flat")
	search_field.pack(expand=False)

	search_box = ttk.Entry(search_field, justify="center")
	search_field.add_widget(search_box, row=0, column=0)

	search_button = ttk.Button(search_field, text="Search", command=lambda: search(search_box.get()))
	search_field.add_widget(search_button, row=0, column=1)

	window.update()

if __name__ == "__main__":
	import sys

	try:
		sys.exit(main())
	except KeyboardInterrupt:
		print("\nQuit.")