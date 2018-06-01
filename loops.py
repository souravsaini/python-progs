#!/usr/bin/python3

# List
list = [12, 10, 25, 30, 3.14, 25, 'Saurabh', 12.34+34.12j, True]

list.append(100)
list.insert(2, 1000)
print(list.count(25))
list.reverse()



for var in list:
    print(var, end=', ')

# Tuple
t = (12, 10, 25, 30, 3.14, 25, 'Saurabh', 12.34+34.12j, True)

# For
for var in t:
	# print(var)
	# print(var, end='')
   	print(var, end=', ')



