#!/usr/bin/python3

def sum_of_digits(n):
	sum=0
	while n>0:
		r=n%10
		sum+=r
		n//=10
	return sum
	
n=(int(input("Enter a number")))	
print(sum_of_digits(n))		