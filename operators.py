#!/usr/bin/python

import numpy

arr=numpy.array([[1,2,3],[4,5,6]])
print(arr+1)
print(arr)
print(arr*2)
print(arr//2)
print(arr**3)
arr*=2  #multiplying each element by 2
print(arr)
print(arr.T)  #Transpose array

ar=numpy.array([[1,3,4],[4,5,6],[8,7,9]])
print(ar.max())
print(ar.min())
print(ar.max(axis=0))  #from each column
print(ar.min(axis=1))  #from each row
print(ar.sum())
print(ar.cumsum(axis=0)) #cumulative sum column wise
ar1=numpy.array([[1,4,2],[4,7,6],[9,8,7]])
print(ar+ar1)
print(ar-ar1)
print(ar*ar1)
print(ar/ar1)
print(ar.dot(ar1))  #matrix multiplication