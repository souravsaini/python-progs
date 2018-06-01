#!/usr/bin/python3

def is_prime(n=2):
	for i in range(2, int(n**0.5)+1):
		if n % i == 0:
			return False

	return True 


def primes(n):
	print("Generator Started")
	for i in range(2, n+1):
		if is_prime(i):
			yield i


list = primes(100)
for prime in list:
	print(prime)