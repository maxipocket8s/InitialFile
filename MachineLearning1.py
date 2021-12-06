# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 17:22:54 2021

@author: pjw20
"""
import pandas as pd
import numpy as np
import matplotlib.pylab as plt

A = [[2, 3], [4, 5]]
B = [[2, 3], [4, 5]]
ANP = np.array(A)
BNP = np.array(B)
print("ANP =", ANP)
ANP_transpose = ANP.T
print('ANP_transpose =', ANP_transpose)

C = np.dot(ANP, BNP)
print('C =', C)
D1 = np.dot(ANP_transpose, BNP)
D2 = ANP.T.dot(BNP)
print("D1 =", D1)
print("D2 =", D2)
E = np.diag(ANP)
print('E =', E)
F = np.trace(ANP)
print('F =', F)
G = np.linalg.det(ANP)
print('G =', G)
H = np.linalg.inv(ANP)
print('H =', H)
I = np.linalg.solve(ANP, ANP_transpose)
print('I =', I)
u, s, vh = np.linalg.svd(ANP)
print('u =', u)
print('s =', s)
print('vh =', vh)

dfload = pd.read_csv("https://raw.githubusercontent.com/hanwoolJeong/lectureUniv/main/testData_H_vs_W.txt"
                     , sep = "\s+")
x = dfload["Height"]
y = dfload['Weight']
# plt.plot(x, y, ".r")

dfLoad = pd.read_csv("https://raw.githubusercontent.com/hanwoolJeong/lectureUniv/main/testData_LinearRegression.txt"
                     , sep = "\s+")
xx = dfLoad["xx"]
yy = dfLoad["yy"]
# plt.plot(xx, yy, ".r")
Ndata = len(xx)
X = np.c_[np.ones([Ndata, 1]), xx]
wOLS = np.linalg.inv(X.T.dot(X)).dot(X.T).dot(np.array(yy).reshape(Ndata, 1))
xPredict = np.linspace(0, 2, num=101)
xPredictPadding = np.c_[np.ones([101, 1]), xPredict]
yPredict = wOLS.T.dot(xPredictPadding.T)
# plt.plot(xPredict.reshape(1, 101), yPredict, "b.-")

eta = 0.2
Niteration = 20
wGD = np.array([0, 0]).reshape(2, 1)
for iteration in np.arange(Niteration):
    yGD = wGD.T.dot(xPredictPadding.T)
    # plt.plot(xPredict.reshape(1, 101), yGD, "b.-")
    gradients = -(2/Ndata)*(X.T.dot(np.array(yy).reshape(Ndata, 1)-X.dot(wGD)))
    wGD = wGD - gradients*eta
    print(wGD)
    
DfLoad = pd.read_csv("https://raw.githubusercontent.com/hanwoolJeong/lectureUniv/main/testData_LogisticRegression.txt"
                     , sep = "\s+")
xAxis = np.array(DfLoad.values[:, 0]) 
yAxis = np.array(DfLoad.values[:, 1])
plt.plot(xAxis, yAxis, "r.")
def sigmoid(x):
    return 1/(1+np.exp(-x))
N = len(xAxis)
TestX = np.linspace(0, 10, num=N).reshape(N, 1)
TestXPadding = np.c_[np.ones([N, 1]), TestX] # (N, 2)
# plt.plot(TestX, sigmoid(TestX), "k-")
xAxisPadding = np.c_[np.ones([N, 1]), xAxis].T # (2, N)
PredictX = xAxisPadding.T # (N, 2)
PredictY = yAxis.reshape(N, 1) # (N, 1)

eta = 0.1
n_iteration = 1000
wGD = np.zeros([2, 1])
wGDbuffer = np.zeros([2, n_iteration+1])
for iteration in range(n_iteration):
    mu = sigmoid(wGD.T.dot(xAxisPadding)).T # (N, 1)
    gradients = PredictX.T.dot(mu-PredictY) # (2, 1)
    wGD = wGD - eta*gradients
    # wGDbuffer[:, iteration+1] = [wGD[0], wGD[1]]
    result = sigmoid(wGD.T.dot(TestXPadding.T))
    plt.plot(TestX, sigmoid(wGD.T.dot(TestXPadding.T)).T, 'b-.')