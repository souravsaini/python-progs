#!/usr/bin/python

class Student:
	def __init__(self, name, rollno):
		self.name = name
		self.rollno = rollno
	
	def print(self):
		print("Name : {} and rollno : {} ".format(self.name,self.rollno))


if __name__ == '__main__':
	student = Student('sourav saini',1418610)	
	student.print()	