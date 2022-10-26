#
# FILENAME: wheel.py | APCSP Wheel of Fortune Project
# DESCRIPTION: The wheel sprite
# CREATED: 2022-10-25 @ 12:32 PM
# COPYRIGHT: Copyright (c) 2022 by Ryan Smith
#

import os, pygame, random, time
from typing import Tuple

class Wheel(pygame.sprite.Sprite):
	def __init__(self, x: int, y: int, *, color: Tuple[int], width: int, height: int) -> None:
		""" Create the wheel sprite. """
		super().__init__()

		# Load the wheel image from the assets folder
		self.image = pygame.image.load(os.path.join("assets", "wheel.png")).convert_alpha()
		self.rect = self.image.get_rect()
		
		# Center the wheel on the screen
		self.image = pygame.transform.scale(self.image, (width, height))
		self.rect.x, self.rect.y = 90, 70
	
	def spin(self) -> int:
		""" Spin the wheel and return the reward. """

		random.seed(time.time())
		

		DEGREES = 15.0

	
	def rotate(self, angle: float) -> None:
		""" Rotate the wheel a certain number of degrees. """

		self.image = pygame.transform.rotate(self.image, angle)
		self.rect
