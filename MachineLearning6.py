# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 06:54:14 2021

@author: pjw20
"""

from sklearn import datasets, model_selection, svm, metrics
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


# Circle
[X, Y] = datasets.make_circles(n_samples = 500, shuffle = True,
                                noise = 0.2, random_state = 15, factor = 0.3) # noise: 더 넓게 분포함, factor: 중심에서 값이 사라짐
f = plt.figure()
ax1 = f.add_subplot(441)
ax1.plot(X[:, 0], X[:, 1], 'g.')
plt.title("SVM from Shape of Circles")

# 데이터 분리
Xtrain, Xtest, Ytrain, Ytest = model_selection.train_test_split(X, Y,
                                                                test_size = 0.3,
                                                                random_state = 15)

# 데이터 STANDARDIZATION
scaler = StandardScaler()
scaler.fit(Xtrain)
Xtrain_std = scaler.transform(Xtrain)
scaler.fit(Xtest)
Xtest = scaler.transform(Xtest)

# SVM Fitting
svm_clf1 = svm.SVC(C = 15, gamma = 20, kernel = 'rbf')
svm_clf1.fit(Xtrain_std, Ytrain)
ax2 = f.add_subplot(442)
ax2.plot(Xtrain_std[:, 0], Xtrain_std[:, 1], 'r.')
plt.title("STD ver.")

df_clf1 = pd.DataFrame(np.c_[Xtrain_std, Ytrain])
df_clf1.columns = ["X0", "X1", "Y"]
group_clf1 = df_clf1.groupby("Y")
ax3 = f.add_subplot(443)
for Y, data in group_clf1:
    ax3.plot(data.X0, data.X1, '.')
    
[x0min, x0max] = [min(Xtrain_std[:, 0])-0.1, max(Xtrain_std[:, 1])+0.1]
[x1min, x1max] = [min(Xtrain_std[:, 1])-0.1, max(Xtrain_std[:, 1])+0.1]
delta = 0.01
[x0plt, x1plt] = np.meshgrid(np.arange(x0min, x0max, delta), np.arange(x1min, x1max, delta))
h1 = svm_clf1.decision_function(np.c_[x0plt.ravel(), x1plt.ravel()]) # (304836, )
h1 = h1.reshape(x0plt.shape) # (532, 573)
CS1 = ax3.contour(x0plt, x1plt, h1, cmap=plt.cm.twilight)
ax3.clabel(CS1)
plt.title("Training Set by RBF")

ax4 = f.add_subplot(444)
y_pred = svm_clf1.predict(Xtest)
acc_score1 = metrics.accuracy_score(Ytest, y_pred)
print(acc_score1)
Xtest0 = Xtest[:, 0]
Xtest1 = Xtest[:, 1]
df_clf2 = pd.DataFrame(np.c_[Xtest0,Xtest1, y_pred])
df_clf2.columns = ("Xtest0", "Xtest1", "y_pred")
group_clf2 = df_clf2.groupby("y_pred")
for y_pred, testdata in group_clf2:
    ax4.plot(testdata.Xtest0, testdata.Xtest1, '.')
plt.title("Test set(accuracy: {})".format(round(acc_score1, 2)))


svm_clf2 = svm.SVC(C = 25, degree = 3, gamma = 0.15, coef0 = 0.01, kernel = 'poly')
svm_clf2.fit(Xtrain_std, Ytrain)

df_clf3 = pd.DataFrame(np.c_[Xtrain_std, Ytrain])
df_clf3.columns = ["Xtrain0", "Xtrain1", "y"]
group_clf3 = df_clf3.groupby("y")
ax5 = f.add_subplot(447)
for y, traindata in group_clf3:
    ax5.plot(traindata.Xtrain0, traindata.Xtrain1, ".")

h2 = svm_clf2.decision_function(np.c_[x0plt.ravel(), x1plt.ravel()])
h2 = h2.reshape(x0plt.shape)
CS2 = ax5.contour(x0plt, x1plt, h2, cmap = plt.cm.twilight)
ax5.clabel(CS2)
plt.title("Training Set by poly")

ax6 = f.add_subplot(448)
y_label = svm_clf2.predict(Xtest)
acc_score2 = metrics.accuracy_score(Ytest, y_label)
print(acc_score2)
df_clf4 = pd.DataFrame(np.c_[Xtest, y_label])
df_clf4.columns = ["X0test", "X1test", "y_label"]
group_clf4 = df_clf4.groupby('y_label')
for y_label, data in group_clf4:
    ax6.plot(data.X0test, data.X1test, '.')
plt.title("Test set(accuracy: {})".format(round(acc_score2, 2)))


# Moons
[x, y] = datasets.make_moons(n_samples=500, shuffle=True,
                              noise=0.1, random_state = 15)
a1 = f.add_subplot(4, 4, 9)
a1.plot(x[:, 0], x[:, 1], 'g.')
plt.title("SVM from Shape of Moons")

x_train, x_test, y_train, y_test = model_selection.train_test_split(x, y,
                                                                    test_size=0.3, random_state=15)
scaler.fit(x_train)
Stdx_train = scaler.transform(x_train)
scaler.fit(x_test)
x_test = scaler.transform(x_test)
a2 = f.add_subplot(4, 4, 10)
a2.plot(Stdx_train[:, 0], Stdx_train[:, 1], 'r.')
plt.title("STD ver.")

# RBF
svm_clf3 = svm.SVC(C = 5, gamma = 0.2, kernel = 'rbf')
svm_clf3.fit(Stdx_train, y_train)
a3 = f.add_subplot(4, 4, 11)
df_clf5 = pd.DataFrame(np.c_[Stdx_train, y_train])
df_clf5.columns = ["Stdx0", "Stdx1", 'yTrain']
group_clf5 = df_clf5.groupby("yTrain")
for yTrain, StdxData in group_clf5:
    a3.plot(StdxData.Stdx0, StdxData.Stdx1, '.')

[Stdx0min, Stdx0max] = [min(Stdx_train[:, 0])-0.1, max(Stdx_train[:, 0])+0.1]
[Stdx1min, Stdx1max] = [min(Stdx_train[:, 1])-0.1, max(Stdx_train[:, 1])+0.1]
[Stdx0plt, Stdx1plt] = np.meshgrid(np.arange(Stdx0min, Stdx0max, delta),
                                    np.arange(Stdx1min, Stdx1max, delta))
h3 = svm_clf3.decision_function(np.c_[Stdx0plt.ravel(), Stdx1plt.ravel()])
h3 = h3.reshape(Stdx0plt.shape)
CS3 = a3.contour(Stdx0plt, Stdx1plt, h3, cmap = plt.cm.twilight)
a3.clabel(CS3)
plt.title("Training Set by RBF")

a4 = f.add_subplot(4, 4, 12)
Y_pred = svm_clf3.predict(x_test)
acc_score3 = metrics.accuracy_score(y_test, Y_pred)
print(acc_score3)
df_clf6 = pd.DataFrame(np.c_[x_test, Y_pred])
df_clf6.columns = ["x0test", "x1test", "Y_pred"]
group_clf6 = df_clf6.groupby("Y_pred")
for Y_pred, xtest in group_clf6:
    a4.plot(xtest.x0test, xtest.x1test, '.')
plt.title("Test set(accuracy: {})".format(round(acc_score3, 2)))

# poly
a5 = f.add_subplot(4, 4, 15)
svm_clf4 = svm.SVC(C = 0.5, degree = 3, gamma = 2, coef0 = 0.1 , kernel = 'poly')
svm_clf4.fit(Stdx_train, y_train)
df_clf7 = pd.DataFrame(np.c_[Stdx_train, y_train])
df_clf7.columns = ["xStd0", "xStd1", "trainY"]
group_clf7 = df_clf7.groupby('trainY')
for trainY, xStd in group_clf7:
    a5.plot(xStd.xStd0, xStd.xStd1, '.')
plt.title("Training Set by poly")    
h4 = svm_clf4.decision_function(np.c_[Stdx0plt.ravel(), Stdx1plt.ravel()])
h4 = h4.reshape(Stdx0plt.shape)
CS4 = a5.contour(Stdx0plt, Stdx1plt, h4, cmap = plt.cm.twilight)
a5.clabel(CS4)

a6 = f.add_subplot(4, 4, 16)
pred_y = svm_clf4.predict(x_test)
acc_score4 = metrics.accuracy_score(y_test, pred_y)
print(acc_score4)
df_clf8 = pd.DataFrame(np.c_[x_test, pred_y])
df_clf8.columns = ['xtest0', 'xtest1', 'pred_y']
group_clf8 = df_clf8.groupby('pred_y')
for pred_y, testX in group_clf8:
    a6.plot(testX.xtest0, testX.xtest1, '.')
plt.title("Test set(accuracy: {})".format(round(acc_score4,2)))