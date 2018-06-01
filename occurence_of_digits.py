#!/usr/bin/python

def count_digit(limit,digit):
	count=0
	for var in range(0,limit+1):
		if var>9:
			list=chop_digit(var)
			print(list)
			for i in list:
				if list[i]==digit:
					count+=1
		else:
			count+=1

	return count

def chop_digit(digit):
	list=[]
	while(digit>0):
		list.append(digit%10)
		digit//=10

	return list

if __name__ == '__main__':
	limit=25
	digit=2
	print(count_digit(limit,digit))
