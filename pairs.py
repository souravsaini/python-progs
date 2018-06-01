#!/usr/bin/python3

from random import randint

MAX = 10000

def find_pairs(arr, arr_len, sum):
	binmap = [0]*MAX
	count = 0

	for i in range(0, arr_len):
		diff = sum - arr[i]
		if diff >= 0 and binmap[diff] == 1:
			print("({}, {})".format(arr[i], diff))
			count += 1

		binmap[arr[i]] = 1

	print("Found {} pairs with sum {}".format(count, sum))


if __name__ == '__main__':
	numbers = []
	for i in range(1, 101):
		numbers.append(randint(1, 101))

	sum = randint(1, 101)
	
	print("List is ", numbers)
	print("We want to find all pairs whose sum is {}".format(sum))

	find_pairs(numbers, len(numbers), sum)