#!/usr/bin/python3

def pattern1(type='*', limit=10):
	for i in range(1, limit+1):
		for j in range(1, i+1):
			print(type, end=" ")
	
		print(end="\n")


# function call
pattern1()

pattern1(type='+')

pattern1(type='+', limit=50)