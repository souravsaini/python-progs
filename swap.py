a=10
b=20
c=30
if a>b and a>c:
	print(a)
elif b>c:
	print(b)
else:
	print(c)


list=[a,2,b,4,5,6]
if a in list:
	print("a in list", end="")

print()	

for i in list:
	print(i, end=",")

print()

for i in range(0,10,2):
	print(i)

""" Program to find sum of first 100 natural nos 
"""
sum=0
for i in range(1,101):
	sum+=i
print(sum)	

# Pattern 
"""
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
"""


for i in range(1,6):
	for j in range(1,i+1):
		print(j, end=" ")
	print()	

"""
54321
5432
543
54
5
"""

for i in range(1,6):
	for j in range(5,i-1,-1):
		print(j, end=" ")
	print()	
else:
	print("Hello")	


for i in range(1,6):
	pass
	print(i)	

str="sourav"
str="honeypreet"
print(str)	


""" Return multiple items """

def func(a,b):
	a,b = b,a
	return a,b

a=10
b=20
x,y = func(a,b)
print(x,y)	


"""packing"""
a,*b,c = 1,2,3,4,5,6
print(a,b,c)


def packing(*a):
	print(a,b,c)

packing(1,2,3)	