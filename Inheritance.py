#!/usr/bin/python

class Animal(object):
	def bark():
		print("Animal Bark")

class Dog(Animal):
	def bark():
		print("Dog Bark")		

if __name__ == '__main__':
	dog = Dog  #creation of object
	dog.bark()  # Dog bark
