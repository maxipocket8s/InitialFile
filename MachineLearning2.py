# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 08:20:53 2021

@author: pjw20
"""

import numpy as np
import matplotlib.pylab as plt

Ndata = 1000
A = np.random.randn(Ndata)
f1 = plt.figure()
ax1 = plt.axes()
ax1.hist(A, bins=100)

f2 = plt.figure()
ax2 = plt.axes()
d1 = np.random.multivariate_normal(mean=[0, 2], cov=[[2, -5], [-5, 3]], size=Ndata)
d2 = np.random.multivariate_normal(mean=[8, 6], cov=[[5, -3], [-3, 8]], size=Ndata)
plt.scatter(d1[:, 0], d1[:, 1], c="b") # (x값, y값)
plt.scatter(d2[:, 0], d2[:, 1], c="r") # (x값, y값)

f3 = plt.figure()
ax3 = plt.axes(projection = '3d')
ax3.plot(d1[:, 0], d1[:, 1], 0, 'go')
ax3.plot(d2[:, 0], d2[:, 1], 1, 'ro')

X1 = np.c_[np.ones([Ndata, 1]), d1]
X2 = np.c_[np.ones([Ndata, 1]), d2]
X = np.r_[X1, X2] # (2000, 2)
Y1 = np.zeros([Ndata, 1])
Y2 = np.ones([Ndata, 1])
Y = np.r_[Y1, Y2] # (2000, 1)

def sigmoid(x):
    return 1/(1+np.exp(-x))
    
eta = 0.1
n_iteration = 1000
wGD = np.zeros([3, 1])
wGDbuffer = np.zeros([3, n_iteration+1])
for iteration in range(n_iteration):
    mu = sigmoid(wGD.T.dot(X.T)).T # (2000, 1)
    gradients = X.T.dot(mu-Y) # (3, 1)
    wGD = wGD - eta*gradients
    wGDbuffer[:, iteration+1] = [wGD[0], wGD[1], wGD[2]]

x1sig = np.linspace(-5, 10, 100)
x2sig = np.linspace(-5, 10, 100)
[x1sig, x2sig] = np.meshgrid(x1sig, x2sig)
ysig = sigmoid(wGD[0] + wGD[1]*x1sig + wGD[2]*x2sig)

# f4 = plt.figure()
# ax4 = plt.axes(projection = '3d')
# ax4.contour3D(x1sig, x2sig, ysig, 50)

# f5 = plt.figure()
# ax5 = plt.axes(projection = '3d')
# ax5.plot_surface(x1sig, x2sig, ysig, cmap='viridis')

ax3.plot_surface(x1sig, x2sig, ysig, cmap='viridis')