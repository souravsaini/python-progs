#!/usr/bin/python3

import math

# Integer format specifiers
integer = 10
'''
Reserves 10 units on screen and right alight the number
by default
'''
print("{:10d}".format(integer))

# Float format specifiers
pie = math.pi
# Decimel number of places
print("{:.2f}".format(pie))
# Right align with specific number of places
print("{:>10.2f}".format(pie))

# String format specifiers
str = "Python is nuts"
# Right Align
print("{:>100}".format(str))
# Center Align
print("{:^100}".format(str))