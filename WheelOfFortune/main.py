#
# FILENAME: main.py | APCSP Wheel of Fortune Project
# DESCRIPTION: The main game loop
# CREATED: 2022-10-25 @ 12:14 PM
# COPYRIGHT: Copyright (c) 2022 by Ryan Smith
#


import pygame, time, math, os, random, locale

from typing import Tuple
from urllib.request import urlopen

from window import Window
from sprites.wheel import Wheel
import colors

def make_text(text: str, font: pygame.font.Font, size: int, use_aa: bool, x: int, y: int, color: Tuple[int, int, int]) -> Tuple[pygame.Surface, pygame.Rect]:
	font = pygame.font.Font(font, size)
	
	text = font.render(text, use_aa, color)
	
	rect = text.get_rect()
	rect.center = (0, 0)
	rect = (x, y)

	return text, rect

def choose_word() -> str:
	word_site = "https://www.mit.edu/~ecprice/wordlist.10000"

	response = urlopen(word_site)
	text = response.read()
	return random.choice(text.splitlines()).decode("utf8")

def instructions() -> None:
	print("Welcome to wheel of fortune.")
	print("Spin the wheel and guess a letter.")
	print("If you guess correctly, the amount you spun will be added to your balance.")
	print("You have 10 tries.")
	print("Good luck!")

def prompt_guess(word: str, current_word: str) -> Tuple[str, bool]:
	print(f"\nHere is the word currently:\n{current_word}")
	guess = str()
	guessed = False

	while not guess.isalpha():
		guess = input("\nGuess a letter: ").lower()

		if not guess.isalpha():
			print("\nInvalid guess.")
	
	if guess in word:
		print("\nYou guessed a letter!")
		indices = [i for i, letter in enumerate(word) if letter == guess]
		
		for i in indices:
			current_word = current_word[:i] + word[i] + current_word[i:]
		
		guessed = True
	else:
		print("\nIncorrect.")
	
	return current_word, guessed

def show_balance(balance: int) -> None:
	""" Print the user's balance. """
	locale.setlocale(locale.LC_ALL, "")
	print(f"\nYour balance: {locale.currency(balance)}")

def main():
	# Instructions and setup
	instructions()
	WORD = choose_word()
	current_word = "_" * len(WORD)
	balance = new_balance = 0
	MAX_GUESSES = 10
	guesses = 0

	# Create the window
	window = Window(1000, 1000)
	window.set_background(255, 255, 255)

	wheel = Wheel(90, 70, width=820, height=860)

	# The screen title and subtitle
	title_text, title_rect = make_text("Wheel of Fortune", "freesansbold.ttf", 32, True, 350, 10, colors.BLACK)
	subtitle_text, subtitle_rect = make_text("Press \"S\" to spin the wheel!", "freesansbold.ttf", 24, True, 320, 40, colors.BLACK)

	all_sprites = pygame.sprite.Group()
	all_sprites.add(wheel)

	# Variables to control the game loop
	running = True
	spinning = False
	prompt = False
	spin_end = 0

	arrow = pygame.image.load(os.path.join("assets", "arrow.png")).convert_alpha()
	arrow_rect = arrow.get_rect()
		
	# Center the wheel on the screen
	arrow = pygame.transform.scale(arrow, (90, 90))
	arrow_rect.x, arrow_rect.y = 45, 500

	show_balance(balance)
	print("\nSpin the wheel to continue.")

	# The game loop
	while running:
		all_sprites.draw(window.surface())
		pygame.display.flip()

		# Draw the text and the arrow
		window.surface().blit(title_text, title_rect)
		window.surface().blit(subtitle_text, subtitle_rect)
		window.surface().blit(arrow, arrow_rect)
		window.update()

		# Spin the wheel
		if spinning and (now := time.time()) <= spin_end:
			pygame.draw.rect(window.surface(), colors.WHITE, (90, 70, 820, 860))
			wheel.spin()
			
			time_left = spin_end - now
			if (seconds := pow(10, -math.floor(time_left))) < 1:
				time.sleep(seconds * time_left)
			else:
				spinning = False
				result =  wheel.get_selected_index()

				# Determine the user's new balance
				if result == "Bankrupt":
					balance = 0

					print("\nYou went bankrupt. Thanks for playing!")
					sys.exit()
				elif result != "Lose a Turn":
					new_balance = balance + result
					prompt = True
		
		if prompt:
			guesses += 1
			current_word, guessed = prompt_guess(WORD, current_word)
			
			print(f"The word is now: {current_word}\n")
			prompt = False

			if guessed:
				balance = new_balance
			elif not guessed and guesses == MAX_GUESSES:
				print("\nYou ran out of guesses!")
				print(f"The word was: {WORD}")
				print("Thanks for playing!")
				sys.exit()
			
			show_balance(balance)
			print("Spin the wheel to continue.")

		# Handle events in the application
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
