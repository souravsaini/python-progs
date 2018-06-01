#!/usr/bin/python

from urllib import request
from bs4 import BeautifulSoup
from sklearn.neural_network import MLPClassifier

URL="https://en.wikipedia.org/wiki/Iris_flower_data_set"

doc=request.urlopen(URL).read()
soup=BeautifulSoup(doc,'lxml')

#print(soup.prettify())

list_inputs=[]  #List of all inputs

#Add listof all inputs
var=soup.select('table tr td')
k=0
for i in range(0,150):
	list=[]
	for j in range(0,4):
		list.append(float(var[k].text))
		k+=1
	k+=1
	list_inputs.append(list)

#print(list_inputs)		

list_targets=[]  #List of all targets
for i in range(1,151):
	if i<=50:
		list_targets.append(0)
	elif i>50 and i<=100:
		list_targets.append(1)
	else:
		list_targets.append(2)

#print(list_targets)

classifier =MLPClassifier()
classifier.fit(list_inputs,list_targets)
predict = classifier.predict([5.5, 1.5, 0.1, 1.3])
print(predict)

