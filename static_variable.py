#!/usr/bin/python3


class Human(object):
	''' Going to be Static variable '''
	count = 0
	''' Constructor '''
	def __init__(self):
		''' Made static '''
		Human.count += 1
	''' To String ''' 
	def __str__(self):
		return str(Human.count)
	''' Destructor '''
	def __del__(self):
		print("Destroyed")


if __name__ == '__main__':
	human1 = Human()
	human2 = Human()
	human3 = Human()
	human4 = Human()

	del human2

	# count will be 4
	print(human2) 