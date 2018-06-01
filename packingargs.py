#!/usr/bin/python3

def func(*args):
	sum=0
	for i in range(0,len(args)):
		sum+=args[i]
	return sum

print(func(1,2,3,4,5))
print(func(4,6,3))
print(func(1,2))