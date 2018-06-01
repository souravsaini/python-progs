#!/usr/bin/python3

from sys import argv

class PatternMaker(object):
	def __init__(self ,pattern="*",size=1):
		self.pattern=pattern
		self.size=size


	def draw(self,iteration):
		for j in range(1, self.size+1):
			if j != self.size:
				print("{:^40}".format(self.pattern*iteration), end='')
			else:	
				print("{:^40}".format(self.pattern*iteration))

	def _pattern(self):
		self.pattern = self.pattern + ' '
		for i in range(1, 21):
			self.draw(i)

		for i in range(19, 0, -1):
			self.draw(i)


if __name__ == '__main__':
	no_of_obj=int(argv[1])
	for i in range(0,no_of_obj):
		print("Pattern for object {}".format(i+1))
		pat=input()
		size=int(input("No.of blocks ?"))
		p=PatternMaker(pattern=pat,size=size)  #create object 
		p._pattern()

