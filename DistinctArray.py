#!/usr/bin/python3

def distinctList(list):
	for i in range(0,len(list)):
		j=0
		for j in range(0,i+1):
			if list[i]==list[j]:
				break
		if i==j:
			print(list[i])

if __name__ == '__main__':
	list=[1,4,3,2,5,4,6,3,8,9]
	distinctList(list)