from sklearn.neural_network import MLPClassifier
from bs4 

inputs = [
	[2, 4],
	[4, 2],
	[1, 6],
	[2, 7],
	[3, 6],
	[2, 8]
]

outputs = [0, 0, 1, 1, 0, 1]

classifier = MLPClassifier() 
classifier.fit(inputs, outputs) # Train

predict = classifier.predict([3, 10])
print(predict)

