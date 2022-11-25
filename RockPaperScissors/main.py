#
# FILENAME: main.py | APCSP Menu Project
# DESCRIPTION: The main game loop
# CREATED: 2022-11-08 @ 12:13 PM
# COPYRIGHT: Copyright (c) 2022 by Ryan Smith
#

import random, time
from typing import Dict
from ui import *
from tkinter import (
	ttk, BOTH, StringVar, messagebox
)

def throw(choice: str, wins: StringVar, losses: StringVar, stats: Dict[str, ttk.Label]) -> None:
	""" Throw rock, paper, or scissors. """

	random.seed(time.time())
	computer_choice = random.choice(("rock", "paper", "scissors"))

	if choice == computer_choice:
		winner = "Tie"
	elif choice == "rock":
		winner = "Computer" if computer_choice == "paper" else "You"
	elif choice == "paper":
		winner = "Computer" if computer_choice == "scissors" else "You"
	elif choice == "scissors":
		winner = "Computer" if computer_choice == "rock" else "You"

	plural = winner == "Computer"
	result = winner if winner == "Tie" else f"{winner} {'wins' if plural else 'win'}"

	if winner == "You":
		wins.set(int(wins.get()) + 1)
	elif winner == "Computer":
		losses.set(int(losses.get()) + 1)
	
	stats["record"].configure(text=f"Record: {wins.get()}-{losses.get()}")
	stats["win_pct"].configure(text=f"| Win Percentage: {get_percentage(int(wins.get()), int(losses.get()))}%")

	messagebox.askokcancel(title="Results", message=f"""You played: {choice}\nThe computer played: {computer_choice}\nResult: {result}""")

def reset_stats(wins: StringVar, losses: StringVar, stats: Dict[str, ttk.Label]) -> None:
	""" Reset the game stats. """

	wins.set(0)
	losses.set(0)
	
	stats["record"].configure(text=f"Record: {wins.get()}-{losses.get()}")
	stats["win_pct"].configure(text=f"| Win Percentage: {get_percentage(int(wins.get()), int(losses.get()))}%")

def get_percentage(wins: int, losses: int) -> float:
	""" Get the player's win percentage. """
	return 0.0 if wins == losses == 0 else wins / (wins + losses) * 100

def main():
	window = Window(title="Rock Paper Scissors", theme="black", width=300, height=100)
	height, width = window.dimensions()

	frame = ttk.Frame(window, width=width, height=height, )
	window.add_widget(frame)

	title = ttk.Label(frame, text="\tChoose Rock, Paper, or Scissors below")
	window.add_widget(title, fillType=BOTH, expand=True)

	choices = GridFrame(frame, width=width, height=height, borderwidth=1, relief="raised")
	window.add_widget(choices, fillType=BOTH, expand=False)

	stats = GridFrame(frame, width=width, height=height, borderwidth=1, relief="flat")
	window.add_widget(stats, fillType=BOTH, expand=True)

	wins = StringVar(window, value=0)
	losses = StringVar(window, value=0)

	stats_list = {
		"record": ttk.Label(stats, text=f"\tRecord: {wins.get()}-{losses.get()}"),
		"win_pct": ttk.Label(stats, text=f"| Win Percentage: {get_percentage(int(wins.get()), int(losses.get()))}%")
	}

	buttons = [
		ttk.Button(choices, text="Rock", command=lambda: throw("rock", wins, losses, stats_list)),
		ttk.Button(choices, text="Paper", command=lambda: throw("paper", wins, losses, stats_list)),
		ttk.Button(choices, text="Scissors", command=lambda: throw("scissors", wins, losses, stats_list)),
		ttk.Button(choices, text="Reset Stats", command=lambda: reset_stats(wins, losses, stats_list))
	]

	for i, button in enumerate(buttons):
		choices.add_widget(button, row=0, column=i)
	
	for i, label in enumerate(stats_list.values()):
		stats.add_widget(label, row=0, column=i)

	window.update()

if __name__ == "__main__":
	import sys

	try:
		sys.exit(main())
	except KeyboardInterrupt:
		print("\nQuit")