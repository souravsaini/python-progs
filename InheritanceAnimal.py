class Animal(object):
	def __init__(self):
		print("Animal constructor")

	def bark(self):
		print("Eating...")

class Dog(Animal):
	def __init__(self):
		print("Dog constructor")

	def eat(self):
		print("Dog eat")

dog = Dog()  #create object	
dog.eat()
dog.bark()		