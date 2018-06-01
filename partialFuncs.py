#!/usr/bin/python3

from functools import partial

def func(a,b,c,x):
	return 1000*a+100*b+10*c+x

g=partial(func,3,1,4)

#Calling partial function
print(g(5))



def func1(a,b,c):
	return 100*a+10*b+c

g1=partial(func1,c=2,b=5)

print(g1(8))
