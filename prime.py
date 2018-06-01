#!/usr/bin/python3
import math

def prime(n):
	if n%2==0 and n>2:
		return False
	for x in range(3,(int)(math.sqrt(n))+1,2):
		if n%x==0:
			return False
	return True

n=int(input("Enter a number"))
if prime(n):
	print("%d is prime"%n)
else:	 
	#print("{} is composite".format(n))
	print(n,"is composite")			