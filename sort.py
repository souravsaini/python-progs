#!/usr/bin/python

import numpy

arr=numpy.array([[7,8,-5],[5,3,7],[9,0,-7]])
print(numpy.sort(arr,axis=0))
print(numpy.sort(arr,axis=None))