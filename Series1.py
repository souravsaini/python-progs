#!/usr/bin/python3


def pow(n=0):
	if n < 0:
		return "Error in input"
	elif n == 0:
		return 0
	else:
		power=n
		for x in range(0,n):
			power**=n
		return power

print(pow(2))