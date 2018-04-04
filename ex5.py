# Type your code for insertion sort (Exercise 5) here
numbers = list(map(int, input("Enter a list of numbers:").split(" ")))
for i in range(1, len(numbers)):
	key = numbers[i]
	k = i - 1
	while k >= 0 and key < numbers[k]:
		(numbers[i], numbers[k]) = (numbers[k], numbers[i])
		i -= 1;
		k -= 1;

print(numbers)