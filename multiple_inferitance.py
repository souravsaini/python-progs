#!/usr/bin/python3

class A(object):
	def __init__(self):
		print("A")
		super(A, self).__init__()


class B(object):
	def __init__(self):
		print("B")
		super(B, self).__init__()


class C(A):
	def __init__(self):
		print("C")
		super(C, self).__init__()


class D(C, B):
	def __init__(self):
		print("D")
		super(D, self).__init__()


# MRO ___

if __name__ == '__main__':
	d = D()		