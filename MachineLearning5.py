# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 09:13:04 2021

@author: pjw20
"""

from sklearn.preprocessing import StandardScaler
import numpy as np
from sklearn import datasets
import matplotlib.pyplot as plt
import pandas as pd
from sklearn import svm

# X = np.array([[2, -3], [4, 1], [0, -2], [10, 3]])
# scaler = StandardScaler()
# scaler.fit(X)
# X_std = scaler.transform(X)

iris = datasets.load_iris()
X = iris["data"][0:100]
Y = iris['target'][0:100]

f = plt.figure()
ax1 = f.add_subplot(231)
plt.scatter(X[:, 0], X[:, 1], alpha=0.2, s=30*X[:, 2], c=X[:, 3], cmap='viridis') # alpha: 투명도
plt.title('Scatter Plot with Size(Petal Width) & Color(Petal Length)', fontsize=9)
plt.xlabel("Sepal Length", fontsize=7)
plt.ylabel("Sepal Width", fontsize=7)
plt.colorbar()

ax3 = f.add_subplot(233)
plt.scatter(X[:, 2], X[:, 3])
plt.title('Scatter Plot with Petal Width & Petal Length', fontsize=9)
plt.xlabel("Petal Length", fontsize=7)
plt.ylabel("Petal Width", fontsize=7)

ax5 = f.add_subplot(232)
plt.scatter(X[:, 0], X[:, 1])
plt.title('Scatter Plot with Sepal Width & Sepal Length', fontsize=9)
plt.xlabel('Sepal Length', fontsize=7)
plt.ylabel('Sepal Width', fontsize=7)

scaler = StandardScaler()
scaler.fit(X)
X_std = scaler.transform(X)

ax2 = f.add_subplot(234)
plt.scatter(X_std[:, 0], X_std[:, 1], alpha = 0.2, s=50*(X_std[:, 2]+2), c=X_std[:, 3], cmap='viridis')
plt.title('STD ver.', fontsize=9)
plt.xlabel("STD Sepal Length", fontsize=7)
plt.ylabel("STD Sepal Width", fontsize=7)
plt.colorbar()

ax4 = f.add_subplot(236)
plt.scatter(X_std[:, 2], X_std[:, 3])
plt.title('STD ver.', fontsize=9)
plt.xlabel("STD Petal Length", fontsize=7)
plt.ylabel("STD Petal Width", fontsize=7)

ax6 = f.add_subplot(235)
plt.scatter(X_std[:, 0], X_std[:, 1])
plt.title('STD ver.', fontsize=9)
plt.xlabel('STD Sepal Length', fontsize=7)
plt.ylabel('STD Sepal Width', fontsize=7)

x = iris['data'][0:100, (2, 3)]
y = iris['target'][0:100]

# fig1, a1 = plt.subplots()
fig = plt.figure()
a1 = fig.add_subplot(121)
a1.plot(x[:, 0], x[:, 1], "g*")

scaler.fit(x)
x_std = scaler.transform(x)

# fig2, a2 = plt.subplots()
# a2.plot(x_std[:, 0], x_std[:, 1], "*")

df_clf = pd.DataFrame(np.c_[x_std, y])
df_clf.columns = ["petalLength", 'petalWidth', 'target']
df_clf_group = df_clf.groupby('target')

# fig3, a3 = plt.subplots()
a3 = fig.add_subplot(122)
for target, group in df_clf_group:
    a3.plot(group.petalLength, group.petalWidth, "*", label='target')
a3.legend()
    
svm_clf = svm.SVC(C=0.01, kernel='linear')
svm_clf.fit(x_std, y)

[x0Min, x0Max] = [min(x_std[:, 0])-0.1, max(x_std[:, 1])+0.1]
[x1Min, x1Max] = [min(x_std[:, 1])-0.1, max(x_std[:, 1])+0.1]
delta = 0.01
[x0plt, x1plt] = np.meshgrid(np.arange(x0Min, x0Max, delta), np.arange(x1Min, x1Max, delta))
h = svm_clf.decision_function(np.c_[x0plt.ravel(), x1plt.ravel()])
h = h.reshape(x0plt.shape)
CS = a3.contour(x0plt, x1plt, h, cmap=plt.cm.twilight)
a3.clabel(CS) # 각 등고선에 레이블 지정