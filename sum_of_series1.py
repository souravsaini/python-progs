#!/usr/bin/python3

# 1 + 2/2! + 3/3! + 4/4! + ... + n/n!

from sys import argv, exit

def fact(n=0):
	if n == 0:
		return 1
	else:
		return n * fact(n-1)


def sum(n=0):
	if n < 0:
		return n
	elif n == 0:
		return 0;
	else: 
		return sum(n-1) + n/fact(n)

def pow(n=0):
	if n < 0:
		return 0
	elif n == 0:
		return 0
	else:
		return pow(n-1) + n/(n**n)


if __name__ == '__main__':
	if (len(argv) == 1):
		print('syntax: {} [sum, pow] number'.format(__file__))
		exit()

	if argv[1] == 'sum':
		try:
			print(sum(int(argv[2])))
		except IndexError:
			print('You forget to give number')
	elif argv[1] == 'pow':
		try:
			print(pow(int(argv[2])))
		except IndexError:
			print('You forget to give number')
	