#
# FILENAME: stats.py | APCSP Stat Tracker Project
# DESCRIPTION: Store and update the user's stats
# CREATED: 2023-01-31 @ 12:10 PM
# COPYRIGHT: Copyright (c) 2023 by Ryan Smith
#

from dataclasses import dataclass
from tkinter import StringVar

@dataclass
class Stats:
	kills: int = 0
	deaths: int = 0
	assists: int = 0
	wins: int = 0
	losses: int = 0

	kd_ratio: float = 0.0
	kda_ratio: float = 0.0

	def add_kill(self, kills_disp: StringVar, kdr_disp: StringVar, kdar_disp: StringVar) -> None:
		self.kills += 1
		self.kd_ratio = self.__calc_kd_ratio()
		self.kda_ratio = self.__calc_kda_ratio()

		kills_disp.set(str(self.kills))
		kdr_disp.set(str(self.kd_ratio))
		kdar_disp.set(str(self.kda_ratio))
	
	def add_death(self, deaths_disp: StringVar, kdr_disp: StringVar, kdar_disp: StringVar) -> None:
		self.deaths += 1
		self.kd_ratio = self.__calc_kd_ratio()
		self.kda_ratio = self.__calc_kda_ratio()

		deaths_disp.set(str(self.deaths))
		kdr_disp.set(str(self.kd_ratio))
		kdar_disp.set(str(self.kda_ratio))
	
	def add_assist(self, assists_disp: StringVar, kdr_disp: StringVar, kdar_disp: StringVar) -> None:
		self.assists += 1
		self.kd_ratio = self.__calc_kd_ratio()
		self.kda_ratio = self.__calc_kda_ratio()

		assists_disp.set(str(self.assists))
		kdr_disp.set(str(self.kd_ratio))
		kdar_disp.set(str(self.kda_ratio))
	
	def add_win(self, wins_disp: StringVar) -> None:
		self.wins += 1
		wins_disp.set(str(self.wins))
	
	def add_loss(self, losses_disp: StringVar) -> None:
		self.losses += 1
		losses_disp.set(str(self.losses))
	
	def __calc_kd_ratio(self) -> float:
		try:
			return self.kills / self.deaths
		except ZeroDivisionError:
			# KDR doesn't formally exist until deaths are non-zero, so
			# just return zero for simplicity
			return 0.0

	def __calc_kda_ratio(self) -> float:
		try:
			return (self.kills + self.assists) / self.deaths
		except ZeroDivisionError:
			# KDAR doesn't formally exist until deaths are non-zero, so
			# just return zero for simplicity
			return 0.0