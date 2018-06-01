#!/usr/bin/python3

from sys import argv

def factorial(n=0):
	if n < 0:
		return "False value"
	elif n == 0:
		return 1
	else:
		return n * factorial(n-1)

if __name__ == '__main__':
	print(factorial(int(argv[1])))