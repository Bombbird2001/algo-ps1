# Type your code for binary search (Exercise 6) here
from random import randint
magicNo = randint(1, 99)
low = 0
high = 100
guesses = 0
while True:
	guess = (low + high) // 2
	guesses += 1
	if guesses > 1000:
		#Just in case something goes wrong
		print("Something went wrong!")
		break
	print("Guess " + str(guesses) + ":", guess)
	if guess < magicNo:
		low = guess
		print("Too low!")
	elif guess > magicNo:
		high = guess
		print("Too high!")
	else:
		print("magicNo is", magicNo)
		break