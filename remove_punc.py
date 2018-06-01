#!/usr/bin/python3

str_punc='''!()-[]{};:'"\,<>./?@#$%^&*_~'''

str=input("enter a string")

no_punc=""
for char in str:
	if char not in str_punc:
		no_punc=no_punc+char

print(no_punc)		