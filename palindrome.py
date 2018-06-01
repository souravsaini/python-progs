#!/usr/bin/python3

def palindrome(n):
	sum=0
	temp=n
	while temp>0:
		r=temp%10
		sum=sum*10+r
		temp//=10
	if sum==n:
		return True
	else:
		return False	
	
n=(int(input("Enter a number")))	
if palindrome(n):
	print("{} is palindrome".format(n))
else:
	print("{} is not palindrome".format(n))	
