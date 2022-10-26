#
# FILENAME: main.py | APCSP Wheel of Fortune Project
# DESCRIPTION: The main game loop
# CREATED: 2022-10-25 @ 12:14 PM
# COPYRIGHT: Copyright (c) 2022 by Ryan Smith
#

import pygame

from window import Window
from sprites.wheel import Wheel
import colors

def gameloop(running: bool) -> None:
	if not running:
		return

def main():
	window = Window(1000, 1000)
	window.set_background(255, 255, 255)

	wheel = Wheel(250, 250, color=colors.WHITE, width=820, height=860)

	all_sprites = pygame.sprite.Group()
	all_sprites.add(wheel)

	window.update()

	running = True
	while running:
		#gameloop(running)

		all_sprites.draw(window.surface())
		pygame.display.flip()

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False

	window.close()

if __name__ == "__main__":
	import sys

	try:
		sys.exit(main())
	except KeyboardInterrupt:
		print("\nQuit.")
