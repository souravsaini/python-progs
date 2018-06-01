#!/usr/bin/python

from sklearn import tree
#import matplotlib.pyplot as plt

# 0 - bump, 1 - oval
features = [
	[120, 0],
	[130, 0],
	[140, 1],
	[150, 1]
]

# 0 - Apple, 1 - Orange
targets = [
	0,
	0,
	1,
	1
]

# Make Classifier 
dtree = tree.DecisionTreeClassifier()
dtree.fit(features, targets)

# Predict data
print(dtree.predict([[125, 0],[135,1]]))

with open("fruit_classifier.dot", "w") as f:
    f = tree.export_graphviz(dtree, out_file=f)