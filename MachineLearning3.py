# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 07:27:27 2021

@author: pjw20
"""

from sklearn.datasets import load_iris
iris = load_iris()
X = iris.data
Y = iris.target

from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.4, random_state =42)

from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, Y_train)
Y_predict = knn.predict(X_test)
scores = metrics.accuracy_score(Y_test, Y_predict)
print(scores)