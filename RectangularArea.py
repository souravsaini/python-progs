#!/usr/bin/python3

class Room(object):
	def __init__(self, length=0, breadth=0):
		self.length=length
		self.breadth=breadth

	def area(self):
		return self.length*self.breadth

	def __str__(self):
		return "Area of room is : {:>10.2f}".format(self.area())


class Tile(object):
	def __init__(self, length=0, breadth=0):
		self.length = length
		self.breadth = breadth

	def area(self):
		return self.length*self.breadth

	def __str__(self):
		return "Area of tile is : {:>10.2f}".format(self.area())

	def no_of_tiles(self, room):
		return "No.of tiles required to fill the room is : {}".format(room.area()//self.area())

if __name__ == '__main__':

	room=Room(400,200)  #Create object of class Room
	tile=Tile(20,10)    #Create object of class Tile
	print(room)
	print(tile)
	print(tile.no_of_tiles(room))



