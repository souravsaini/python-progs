#!/usr/bin/python3

from sys import argv

def pattern(n):
	k=1
	for i in range(1,n+1):
		for j in range(1,i+1):
			print(k,end=" ")
			k+=1
		print()

pattern(int(argv[1]))			