from sklearn.svm import SVC
from sklearn.datasets import load_digits
from sys import argv
from random import randint, shuffle
import numpy as np

import matplotlib.pyplot as plt


digits = load_digits()

X = digits.data
y = digits.target

#print(digits.images[0])

cls = SVC()
cls.fit(X, y)

#FIND = int(argv[1])

#print(cls.predict(X[FIND:FIND+1]))
#print(y[FIND:FIND+1])  #verifying the prediction

#plt.imshow(digits.images[FIND])
#plt.show()


digit = []
for i in range(8):
	list=[]
	for j in range(3):
		list+=[randint(0,16)]
	list+=[0]*5

	shuffle(list)	
	digit.append(list)
print(digit)

digi = np.array(digit).reshape(8,8)
print(digi)

out = cls.predict(digi)
print(out)

plt.matshow(digi)
plt.show()

