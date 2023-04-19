#
# FILENAME: pwcrack.py | APCSP Password Cracker Project
# DESCRIPTION: A brute force password-cracking algorithm
# CREATED: 2022-12-13 @ 8:52 AM
# COPYRIGHT: Copyright (c) 2022 by Ryan Smith
#

import string
from typing import Tuple

def crack_password(password: str) -> Tuple[str, int]:
	tries = 0

	for first in string.ascii_lowercase:
		for second in string.ascii_lowercase:
			for third in string.ascii_lowercase:
				tries += 1

				if (p := f"{first}{second}{third}") == password:
					return p, tries

def main():
	password = ""

	while not 0 < len(password) <= 3:
		password = input(">>> Enter a three-character password to crack: ").lower()
	
	result, tries = crack_password(password)
	print(f"Guessed {result} in {tries} tries")

if __name__ == "__main__":
	import sys

	try:
		sys.exit(main())
	except KeyboardInterrupt:
		print("\nQuit.")