#!/usr/bin/python3

from sys import argv

str=argv[1]

#split the string basis of whitespaces
str=str.split()
# sort the string
str.sort()

for word in str:
	print(word,end=" ")