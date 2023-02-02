#
# FILENAME: main.py | APCSP Stat Tracker Project
# DESCRIPTION: A video game stat tracker
# CREATED: 2023-01-31 @ 11:23 AM
# COPYRIGHT: Copyright (c) 2023 by Ryan Smith
#

from tkinter import ttk, StringVar

from ui import Window, GridFrame
from stats import Stats

def main():
	window = Window(title="Video Game Stat Tracker", theme="black", width=360, height=215)
	width, height = window.dimensions()

	frame = GridFrame(window, height=height, width=width)
	window.add_widget(frame)

	kills_disp = StringVar(value="0")
	deaths_disp = StringVar(value="0")
	assists_disp = StringVar(value="0")
	wins_disp = StringVar(value="0")
	losses_disp = StringVar(value="0")
	kdr_disp = StringVar(value="0.0")
	kdar_disp = StringVar(value="0.0")

	stats = Stats()

	# Add buttons to update the stats with
	add_kills = ttk.Button(frame, text="Kills", command=lambda: stats.add_kill(kills_disp, kdr_disp, kdar_disp))
	add_deaths = ttk.Button(frame, text="Deaths", command=lambda: stats.add_death(deaths_disp, kdr_disp, kdar_disp))
	add_assists = ttk.Button(frame, text="Assists", command=lambda: stats.add_assist(assists_disp, kdr_disp, kdar_disp))
	add_wins = ttk.Button(frame, text="Wins", command=lambda: stats.add_win(wins_disp))
	add_losses = ttk.Button(frame, text="Losses", command=lambda: stats.add_loss(losses_disp))

	# Add labels to display the stats
	kills_label = ttk.Label(frame, textvariable=kills_disp)
	deaths_label = ttk.Label(frame, textvariable=deaths_disp)
	assists_label = ttk.Label(frame, textvariable=assists_disp)
	wins_label = ttk.Label(frame, textvariable=wins_disp)
	losses_label = ttk.Label(frame, textvariable=losses_disp)

	kdr_title = ttk.Label(frame, text="KD Ratio", relief="raised")
	kdr_label = ttk.Label(frame, textvariable=kdr_disp)
	
	kdar_title = ttk.Label(frame, text="KDA Ratio", relief="raised")
	kdar_label = ttk.Label(frame, textvariable=kdar_disp)

	# Kills
	frame.add_widget(add_kills, row=0, column=0)
	frame.add_widget(kills_label, row=1, column=0)

	# Deaths
	frame.add_widget(add_deaths, row=0, column=1)
	frame.add_widget(deaths_label, row=1, column=1)

	# Assists
	frame.add_widget(add_assists, row=0, column=2)
	frame.add_widget(assists_label, row=1, column=2)

	# Wins
	frame.add_widget(add_wins, row=0, column=3)
	frame.add_widget(wins_label, row=1, column=3)

	# Losses
	frame.add_widget(add_losses, row=0, column=4)
	frame.add_widget(losses_label, row=1, column=4)

	# Add places to display the Kill-Death ratio (KDR) and the
	# Kill-Death-Assist ratio (KDAR). 
	frame.add_widget(kdr_title, row=4, column=0)
	frame.add_widget(kdr_label, row=5, column=0)

	frame.add_widget(kdar_title, row=4, column=1)
	frame.add_widget(kdar_label, row=5, column=1)

	window.update()

if __name__ == "__main__":
	import sys

	try:
		sys.exit(main())
	except KeyboardInterrupt:
		print("\nQuit.")
