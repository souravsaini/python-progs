from sklearn.linear_model import Perceptron
import numpy as np

# Data
d = np.array([
	[2, 1, 2, 5, 7, 2, 3, 6, 1, 2, 5, 4, 6, 5],
	[2, 3, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 7]
])
 
d90 = np.rot90(d)
d90 = np.rot90(d90)
d90 = np.rot90(d90)

# Labels
t = np.array([0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1])

p = Perceptron(n_iter=1000, verbose=0, random_state=None, fit_intercept=True, eta0=0.001)
f = p.fit(d, t)

predict = p.predict((np.array([3, 3]).reshape(1, -1)))

print(predict)