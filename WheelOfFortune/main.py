#
# FILENAME: main.py | APCSP Wheel of Fortune Project
# DESCRIPTION: The main game loop
# CREATED: 2022-10-25 @ 12:14 PM
# COPYRIGHT: Copyright (c) 2022 by Ryan Smith
#

import pygame, time, math
from typing import Tuple

from window import Window
from sprites.wheel import Wheel
import colors

def make_text(text: str, font: pygame.font.Font, use_aa: bool, x: int, y: int) -> Tuple[pygame.Surface, pygame.Rect]:
	pass

def main():
	window = Window(1000, 1000)
	window.set_background(255, 255, 255)

	wheel = Wheel(90, 70, color=colors.WHITE, width=820, height=860)

	font = pygame.font.Font('freesansbold.ttf', 32)
	
	title_text = font.render('Wheel of Fortune', True, colors.BLACK)
	
	title_rect = title_text.get_rect()
	title_rect.center = (0, 0)
	title_rect = (350, 10)

	all_sprites = pygame.sprite.Group()
	all_sprites.add(wheel)

	running = True
	spinning = False
	spin_end = 0

	while running:
		all_sprites.draw(window.surface())
		pygame.display.flip()

		window.surface().blit(title_text, title_rect)
		window.update()

		if spinning and (now := time.time()) <= spin_end:
			pygame.draw.rect(window.surface(), colors.WHITE, (90, 70, 820, 860))
			wheel.spin()
			
			if (seconds := pow(10, -math.floor(spin_end - now))) < 1:
				time.sleep(seconds)
			else:
				spinning = False

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
			elif event.type == pygame.KEYDOWN and event.key == pygame.K_s:
				spinning = True
				spin_end = time.time() + 5
				

	window.close()

if __name__ == "__main__":
	import sys

	try:
		sys.exit(main())
	except KeyboardInterrupt:
		print("\nQuit.")
