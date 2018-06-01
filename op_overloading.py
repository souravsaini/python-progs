#!/usr/bin/python

import pickle

class Point:
	def __init__(self, x=0.0, y=0.0):
		self.x = x
		self.y = y

	def __str__(self):
		return "({}, {})".format(self.x ,self.y)

	def __lt__(self, other):
		return self.x < other.x or self.y < other.y 	

	def __gt__(self, other):
		return not(self.__lt__(other)) 	

'''
__lt__ <
__gt__ >
__le__ <=
__ge__ >=
__eq__ ==
__ne__ <>
__add__ +
__sub__ -
__mult__ *
__divmod__ /
__mod__ %

'''

if __name__ == '__main__':
	p1 = Point(10, 20)
	p2 = Point(20, 30)

	# file = open("sample.txt", "ab")
	# # file.write(p1)
	# pickle.dump(p1, file)
	file = open("sample.txt", "rb")
	file.read()
	obj = pickle.load(file)
	print(obj)
