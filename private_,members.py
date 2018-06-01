#!/usr/bin/python3


class Tile(object):
	def __init__(self, privateVar):
		self.__privateVar = privateVar


if __name__ == '__main__':
	tile = Tile(10)
	print(tile.__privateVar)