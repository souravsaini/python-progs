#!/usr/bin/python3

from Shapes.shapes import ( 
	Circle, Cylinder,
	Cone 
)


if __name__ == '__main__':
	circle = Circle(10)
	print("Area of circle is      {:>10.2f}".format(circle.area()))
	print("Perimeter of circle is {:>10.2f}".format(circle.perimeter()))	

	cyl = Cylinder(10, 5)
	print("Area of cylinder is    {:>10.2f}".format(cyl.area()))
	print("Volume of cylinder is  {:>10.2f}".format(cyl.volume()))


	cone = Cone(20, 10)
	print("Area of cone is        {:>10.2f}".format(cone.area()))
	print("Volume of cone is      {:>10.2f}".format(cone.volume()))	