#
# FILENAME: wheel.py | APCSP Wheel of Fortune Project
# DESCRIPTION: The wheel sprite
# CREATED: 2022-10-25 @ 12:32 PM
# COPYRIGHT: Copyright (c) 2022 by Ryan Smith
#

import os, pygame, random, time
from typing import Tuple

class Wheel(pygame.sprite.Sprite):
	__ASSET_PATH = os.path.join("assets", "wheel.png")
	__x: int
	__y: int

	def __init__(self, x: int, y: int, *, color: Tuple[int], width: int, height: int) -> None:
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
		return rotated_image, new_rect
	
	def spin(self) -> int:
		""" Spin the wheel and return the reward. """

		#random.seed(time.time())
		img, rect = self.rotate(90, 500, 500)
		self.image.fill((255, 255, 255, 0))
		self.image, self.rect = img, rect
