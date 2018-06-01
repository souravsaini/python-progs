#!/usr/bin/python

import numpy

#Create a multidimensional array
arr=numpy.array([[1,2,3],[4,5,6]])
print(type(arr))
print(arr.ndim) #number of dimensions
print(arr.shape)
print(arr.size)
print(arr.dtype)

ar=numpy.array([[1,2,4],[5,7,6]] , dtype='float' )
print(ar)

arzeros=numpy.zeros([3,5])
print(arzeros)

arfull=numpy.full([3,5], 6, dtype='complex')
print(arfull)

randarr=numpy.random.random([3,5])
print(randarr)

steparr=numpy.arange(3,15,3)
print(steparr)

linarr=numpy.linspace(0,10,25) #create a array between 0 to 10 with 25 values having equal differences
print(linarr)

reshapearr = numpy.array([[1, 2, 3, 4],
                [5, 2, 4, 2],
                [1, 2, 0, 1]])
newarr = reshapearr.reshape(2, 2, 3)
print(newarr)

print(newarr.flatten())  #Flatten the array