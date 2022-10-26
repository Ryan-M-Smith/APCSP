#
# FILENAME: window.py | APCSP Wheel of Fortune Project
# DESCRIPTION: Create the game window
# CREATED: 2022-10-25 @ 12:16 PM
# COPYRIGHT: Copyright (c) 2022 by Ryan Smith
#

import pygame

class Window():
	__window: pygame.Surface

	def __init__(self, width: int = 500, height: int = 500) -> None:
		pygame.init()
		self.__window = pygame.display.set_mode((width, height))
	
	def surface(self) -> pygame.Surface:
		return self.__window
	
	def set_background(self, r: int, g: int, b: int) -> None:
		self.__window.fill(pygame.Color(255, 255, 255))

	def close(self):
		pygame.quit()
	
	@staticmethod
	def update() -> None:
		pygame.display.update()