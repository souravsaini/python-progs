#!/usr/bin/python3

def greet(name='guest', times=1):
	print("Hello, {}\n".format(name) * times)


greet("Ajay Bhatia", 5)
greet(times=10)


# Sum of all items in list
# def sum(numbers):
# 	sum = 0
# 	for number in numbers:
# 		sum += number

# 	return sum

def product(items):
	return reduce(mul, items, 1)