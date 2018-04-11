# Type your code for insertion sort (Exercise 5) here
def insertion_sort(noList):
	for i in range(1, len(numbers)):
		key = numbers[i]
		k = i - 1
		while k >= 0 and key < numbers[k]:
			(numbers[i], numbers[k]) = (numbers[k], numbers[i])
			i -= 1;
			k -= 1;

	print(numbers)

while True:
		try:
			rawInput = input("Enter a list of numbers, or X to exit:")
			if rawInput == "X":
				break
			else:
				numbers = list(map(int, rawInput.split(" ")))
				insertion_sort(numbers)
		except:
			print("Please enter a valid list of space-separated integers!")