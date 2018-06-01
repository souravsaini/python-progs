#!/usr/bin/python3

class Point(object):
	''' Constructor '''
	def __init__(self, x=0, y=0):
		self.x = x
		self.y = y

	''' Calculate distance from origin '''	
	def distance_from_origin(self):
		return (self.x**2 + self.y**2)**0.5		

	def __str__(self):
		return "({0}, {1})".format(self.x, self.y)


class Line(Point):
	def __init__(self, x1, y1, x2, y2):
		self.p1 = Point(x1, y1)
		self.p2 = Point(x2, y2)

	def length(self):
		return ((self.p2.x - self.p1.x)**2 + (self.p2.y - self.p1.y)**2)**0.5		

	def __str__(self):
		return "Line from ({}, {}) to ({}, {})".format(self.p1.x, self.p1.y, self.p2.x, self.p2.y)


line = Line(1, 10, 20, 100)
print("{:.3f}".format(line.length()))