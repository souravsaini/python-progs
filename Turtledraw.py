#!/usr/bin/python3

import turtle
from random import randint 

window=turtle.Screen()

tt=turtle.Turtle('turtle')

tt.color('red')
tt.speed(4)
tt.forward(100)
tt.right(90)
tt.forward(200)
tt.backward(400)
tt.right(90)
print(tt.heading())  #?????
tt.setpos(100,100)
tt.begin_fill()   # Turtle begin_fill
tt.circle(50)
tt.dot(20,'blue')
print(tt.stamp()) #????
tt.shape('turtle')  #????
tt.reset()  #reset yhe screen

while(True):
	n=randint(0,3)
	if n==0:
		tt.color("red","green")
		tt.pensize(randint(1,11))
		tt.forward(randint(1,101))
	elif n==1:
		tt.left(randint(1,361))
	else:
		tt.right(randint(1,361))	



window.mainloop()
