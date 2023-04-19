#
# FILENAME: caesarcipher.py | APCSP Caesar Cipher Project
# DESCRIPTION: Encrypt and decrypt data using a caesar cipher
# CREATED: 2022-12-05 @ 1:59 PM
# COPYRIGHT: Copyright (c) 2022 by Ryan Smith
#

def cc_encode(plaintext: str, n: int) -> str:
	result = ""

	LOWERCASE_A = ord("a")
	UPPERCASE_A = ord("A")
	NUMBER_ZERO = ord("0")

	for char in plaintext:
		if char.isupper():
			ascii_result = (ord(char) - UPPERCASE_A + n) % 26 + UPPERCASE_A
		elif char.islower():
			ascii_result = (ord(char) - LOWERCASE_A + n) % 26 + LOWERCASE_A
		elif char.isnumeric():
			ascii_result = (ord(char) - NUMBER_ZERO + n) % 10 + NUMBER_ZERO
		else:
			ascii_result = ord(char)
		
		result += chr(ascii_result)

	return result

def cc_decode(ciphertext: str, n: int) -> str:
	result = ""

	LOWERCASE_A = 97
	UPPERCASE_A = 65
	NUMBER_ZERO = 48

	for char in ciphertext:
		if char.isupper():
			ascii_result = (ord(char) - UPPERCASE_A - n) % 26 + UPPERCASE_A
		elif char.islower():
			ascii_result = (ord(char) - LOWERCASE_A - n) % 26 + LOWERCASE_A
		elif char.isnumeric():
			ascii_result = (ord(char) - NUMBER_ZERO - n) % 10 + NUMBER_ZERO
		else:
			ascii_result = ord(char)
		
		result += chr(ascii_result)

	return result

def main():
	message = input("Enter text: ")

	choice = 0
	while choice == 0 and choice not in range(1, 3):
		print("\nWhat would you like to do?")
		print("1. Encrypt message")
		print("2. Decrypt message")
		
		try:
			choice = int(input(">>> "))
		except ValueError:
			print("\nInvalid entry.")
		else:
			if choice not in range(1, 6):
				print("\nInvalid entry.")
	
	if choice == 1:
		key = 0
		while key < 1:
			try:
				key = int(input("\nEnter an encryption key: "))
			except ValueError:
				print("\nInvalid entry.")
			else:
				if choice < 1:
					print("\nPlease enter a value that is at least 1.")
		
		print(f"\nPlaintext: {message}")
		print(f"Ciphertext: {cc_encode(message, key)}")
		print(f"Decryption key: {key}")
	elif choice == 2:
		key = 0
		while key < 1:
			try:
				key = int(input("\nEnter an encryption key: "))
			except ValueError:
				print("\nInvalid entry.")
			else:
				if choice < 1:
					print("\nPlease enter a value that is at least 1.")
		
		print(f"\nCiphertext: {message}")
		print(f"Plaintext: {cc_decode(message, key)}")
		print(f"Encryption key: {key}")

if __name__ == "__main__":
	import sys

	try:
		sys.exit(main())
	except KeyboardInterrupt:
		print("\nQuit.")