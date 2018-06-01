#!/usr/bin/python

def merge_array(list1, list2):
	list3=[]
	a=len(list1)
	b=len(list2)
	na,nb,nc=0,0,0

	while na<a and nb<b:
		if list1[na]<list2[nb]:
			list3.append(list1[na])
			na+=1

		else:
			list3.append(list2[nb])
			nb+=1 
        
		nc+=1

	if na<a:
		while na<a:
			list3.append(list1[na])
			na+=1
			nc+=1

	else:
		while nb<b:
			list3.append(list2[nb])
			nb+=1
			nc+=1	

	return list3


if __name__ == '__main__':
	list1=[1,3,5,6,7,8]
	list2=[2,4,5,6,9]
	print(merge_array(list1,list2))



