#
# FILENAME: wheel.py | APCSP Wheel of Fortune Project
# DESCRIPTION: The wheel sprite
# CREATED: 2022-10-25 @ 12:32 PM
# COPYRIGHT: Copyright (c) 2022 by Ryan Smith
#

import os, pygame, random, time
from typing import Tuple, Union

class Wheel(pygame.sprite.Sprite):
	__ASSET_PATH = os.path.join("assets", "wheel.png")
	__x: int
	__y: int

	wheel_data = [
		"Bankrupt", 6500, 1000, 3000, "Lose a Turn", 7500, 1250, 3500,
		2000, 5000, "Bankrupt", 20000, 1500, 4000, 1750, 1000, 2000,
		1250, 5000, 2500, 7500, 10000, 4500, 3500
	]
	__reference_index = 0

	__INITIAL_DISTANCE = 17
	__WHEEL_SECTIONS = 24

	def __init__(self, x: int, y: int, *, width: int, height: int) -> None:
		""" Create the wheel sprite. """
		super().__init__()

		self.__x, self.__y = x, y

		# Load the wheel image from the assets folder
		self.image = pygame.image.load(self.__ASSET_PATH).convert_alpha()
		self.rect = self.image.get_rect()
		
		# Center the wheel on the screen
		self.image = pygame.transform.scale(self.image, (width, height))
		self.rect.x, self.rect.y = x, y
	
	def rotate(self, angle: float, x: int, y: int) -> Tuple[pygame.Surface, pygame.Rect]:
		rotated_image = pygame.transform.rotate(self.image, angle)
		new_rect = rotated_image.get_rect(center = self.image.get_rect(center = (x, y)).center)
		
		# Rotate the wheel data with the wheel
		self.wheel_data = self.wheel_data[-6:] + self.wheel_data[:-6]
		self.__reference_index += 6
		
		return rotated_image, new_rect
	
	def spin(self) -> int:
		""" Spin the wheel and return the reward. """

		#random.seed(time.time())
		img, rect = self.rotate(-90, 500, 500)
		self.image.fill((255, 255, 255, 0))
		self.image, self.rect = img, rect
	
	def get_selected_index(self) -> Union[str, int]:
		""" Determine what the wheel landed on. """
		return self.wheel_data[17]
