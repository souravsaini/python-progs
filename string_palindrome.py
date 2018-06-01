#!/usr/bin/python3

str=input("enter a string\n")


# for caseless operations
str=str.casefold()
# reverse the string
rev_str=reversed(str)
# check both strings
# we cannot write as str==rev_str
if list(str)==list(rev_str):
	print("string is palindrome")
else:
	print("string is not palindrome")	