from sklearn import datasets
from sklearn import tree

iris_data = datasets.load_iris()

# print(iris_data.feature_names)
# print(iris_data.target_names)
print(iris_data.data)
print(iris_data.target)

# for i in range(len(iris_data.target)):
# 	print("{} - {}".format(iris_data.data[i], iris_data.target[i]))

dtree = tree.DecisionTreeClassifier()
dtree.fit(iris_data.data, iris_data.target)

print(dtree.predict([[5, 3.1, 4, 1.2],[4.7,3.5,4.1,1.4]]))

with open("iris_classifier.dot", "w") as f:
    f = tree.export_graphviz(dtree, out_file=f)