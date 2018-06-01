#!/usr/bin/python3

from sys import argv

def draw(pattern, size, iteration):
	for j in range(1, size+1):
		if j != size:
			print("{:^40}".format(pattern*iteration), end='')
		else:	
			print("{:^40}".format(pattern*iteration))

 # DRY - Don't Repear Yourelf
def pattern(pattern='*', size=1):
	pattern = pattern + ' '
	for i in range(1, 21):
		draw(pattern, size, i)

	for i in range(19, 0, -1):
		draw(pattern, size, i)


if __name__ == '__main__':
	pattern(size=int(argv[1]))