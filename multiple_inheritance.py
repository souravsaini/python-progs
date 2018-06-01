#!/usr/bin/python3


class A(object):
	def __init__(self):
		self.name = "A"

	def get_name(self):
		print(self.name)


class B(object):
	def __init__(self):
		self.name = "B"

	def get_name(self):
		print(self.name)
		

class C(A, B):
	def __init__(self):
		self.name = "C"
		super().get_name()	

	def get_name(self):
		print(self.name)
		

if __name__ == '__main__':
	c = C()
