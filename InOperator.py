#!/usr/bin/python3

list=['kat','bat','fat','none','stone','mat','At']

for i in list:
	if 'at' in i:
		print(" 'at' is present in {}".format(i))

print(list[3:])
print(list[::-1])
print(list[-4::-1])

for i in list:
	print(i.capitalize())

list1=[1]*10
print(list1)
list1=[2]*10
print(list1)
list1.append(1)
#list1.append(list)
print (min(list1))
print(max(list1))
print(list1.count(2))
list1.reverse()
print(list1)