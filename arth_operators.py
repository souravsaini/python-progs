#!/usr/bin/python3

# variable initializations
var1 = 40
var2 = 3

# Arithmetic Operators

# Additon (+)
var3 = var1 + var2
# print(str(var1) + " + " + str(var2) + " = " + str(var3))
# print("{} + {} = {}".format(var1, var2, var3))
print("{a} + {b} = {c}".format(b=var2, a=var1, c=var3))
print(var3)

# Subtraction (-)
var3 = var1 - var2
print("{a} - {b} = {c}".format(b=var2, a=var1, c=var3))

# Divison (/)
var3 = var1 / var2
print("{a} / {b} = {c}".format(b=var2, a=var1, c=var3))

# Integer Divison (//)
var3 = var1 // var2
print("{a} // {b} = {c}".format(b=var2, a=var1, c=var3))

# Multiplication (*)
var3 = var1 * var2
print("{a} * {b} = {c}".format(b=var2, a=var1, c=var3))

# Raise to power (**)
var3 = var1 ** var2
print("{a} ** {b} = {c}".format(b=var2, a=var1, c=var3))

# Modulus (Remainder) %
var3 = var1 % var2
print("{a} % {b} = {c}".format(b=var2, a=var1, c=var3))
