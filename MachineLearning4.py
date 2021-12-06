# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import scipy.stats as spst

# K-Means

dfLoad = pd.read_csv("https://raw.githubusercontent.com/hanwoolJeong/lectureUniv/main/ClassificationSample.txt",
                     sep='\s+')
'''
x = np.array(dfLoad["X"]) # column indexing
y = np.array(dfLoad["Y"])
# print(dfLoad.iloc[4]) # row indexing
# print(dfLoad.iloc[4]["X"]) # 해당 값 출력
# dfLoad.groupby("K") # K값 기준으로 분류
N = len(x)
np.random.seed(3)
k = np.round(np.random.rand(N))
npCluster = np.c_[x, y, k]
dfCluster = pd.DataFrame(npCluster)
dfCluster.columns = ["X", "Y", "K"]
dfGroup = dfCluster.groupby("K")
for (cluster, dataInCluster) in dfGroup:
    print(dataInCluster)
'''    
samples = np.array(dfLoad)
N = len(samples)
numberK = 2
x = samples[:, 0]
y = samples[:, 1]
f = plt.figure()
ax1 = f.add_subplot(231)
ax1.plot(x, y, 'b.')

[mx, sx] = [np.mean(x), np.std(x)]
[my, sy] = [np.mean(y), np.std(y)]
z0 = np.array([mx+sx, my+sy]).reshape(1, 2)
z1 = np.array([mx-sx, my-sy]).reshape(1, 2)
Z = np.r_[z0, z1]
ax1.plot(Z[:, 0], Z[:, 1], 'r*', markersize=20)
ax1.set_title("Initial")

k = np.zeros([N, 1])
while(True):
    kOld = np.copy(k)
    for i in range(N):
        k[i] = np.linalg.norm(samples[i, :]-Z[0, :]) > np.linalg.norm(samples[i, :]-Z[1, :])
    if np.alltrue(kOld == k):
        break
    dfCluster = pd.DataFrame(np.c_[x, y, k])
    dfCluster.columns = ["X", "Y", "K"]
    dfGroup = dfCluster.groupby("K")
    for cluster in range(numberK):
        Z[cluster, :] = dfGroup.mean().iloc[cluster]

ax2 = f.add_subplot(232)
for (cluster, dataInCluster) in dfGroup:
    ax2.plot(dataInCluster.X, dataInCluster.Y, '.', label=cluster)
ax2.plot(Z[:, 0], Z[:, 1], 'g*', markersize=20)
ax2.set_title("By k-Means")
ax2.legend()


dfload = pd.read_csv("https://raw.githubusercontent.com/hanwoolJeong/lectureUniv/main/ClassificationSample2.txt",
                     sep='\s+')
npdata = np.array(dfload)
Ndata = len(npdata)
Kdata = 2
X = npdata[:, 0]
Y = npdata[:, 1]

ax3 = f.add_subplot(234)
ax3.plot(X, Y, 'b.')

mx2 = np.mean(X)
my2 = np.mean(Y)
sx2 = np.std(X)
sy2 = np.std(Y)

z20 = np.array([mx2+sx2, my2+sy2]).reshape(1, 2)
z21 = np.array([mx2-sx2, my2-sy2]).reshape(1, 2)
Z2 = np.r_[z20, z21]

ax3.plot(Z2[:, 0], Z2[:, 1], 'r*', markersize=20)
ax3.set_title('Initial')
k = np.zeros([Ndata, 1])
while(True):
    kOld = np.copy(k)
    for i in range(Ndata):
        k[i] = np.linalg.norm(npdata[i, :]-Z2[0, :]) > np.linalg.norm(npdata[i, :]-Z2[1, :])
    if np.alltrue(kOld == k):
        break
    dfCluster2 = pd.DataFrame(np.c_[X, Y, k])
    dfCluster2.columns = ["X", "Y", "K"]
    dfGroup2 = dfCluster2.groupby("K")
    for cluster in range(Kdata):
        Z2[cluster, :] = dfGroup2.mean().iloc[cluster]

ax4 = f.add_subplot(235)
for (cluster, dataInCluster) in dfGroup2:
    ax4.plot(dataInCluster.X, dataInCluster.Y, '.', label=cluster)
ax4.plot(Z2[:, 0], Z2[:, 1], 'g*', markersize=20)
ax4.set_title('By k-Means')
ax4.legend()



# GMM

pi = np.ones(Kdata)*(1/Kdata)
u0 = np.array([mx2+0.5*sx2, my2+sy2])
u1 = np.array([mx2-0.5*sx2, my2-sy2])
sigma0 = np.array([[sx2*sx2/4, 0], [0, sy2*sy2/4]])
sigma1 = np.array([[sx2*sx2/4, 0], [0, sy2*sy2/4]])
R = np.ones([Ndata, Kdata])*(1/Kdata)
N0 = spst.multivariate_normal.pdf(npdata, u0, sigma0)
N1 = spst.multivariate_normal.pdf(npdata, u1, sigma1)
while(True):
    piOld = np.copy(pi)
    R = np.array([pi[0]*N0/(pi[0]*N0+pi[1]*N1), pi[1]*N1/(pi[0]*N0+pi[1]*N1)]).T
    pi = np.ones(N).reshape(1, N).dot(R)/N
    pi = pi.reshape(2, )
    if np.alltrue(piOld == pi):
        break
    weightedSum = npdata.T.dot(R)
    u0 = weightedSum[:, 0]/sum(R[:, 0])
    u1 = weightedSum[:, 1]/sum(R[:, 1])
    sigma0 = npdata.T.dot(np.multiply(R[:, 0].reshape(N, 1), npdata))/sum(R[:, 0]) - u0.reshape(2, 1)*u0.reshape(2, 1).T
    sigma1 = npdata.T.dot(np.multiply(R[:, 1].reshape(N, 1), npdata))/sum(R[:, 1]) - u1.reshape(2, 1)*u1.reshape(2, 1).T

ax5 = f.add_subplot(236)
kGmm = np.zeros(Ndata).reshape(Ndata, 1)
for i in range(Ndata):
    if R[i, 0] > R[i, 1]:
        kGmm[i] = 0
    else:
        kGmm[i] = 1
        
u0 = u0.reshape(1, 2)
u1 = u1.reshape(1, 2)
U = np.r_[u0, u1]
ClusterGmm = np.c_[X, Y, kGmm]
dfClusterGmm = pd.DataFrame(ClusterGmm)
dfClusterGmm.columns = ["X", "Y", "kGmm"]
dfGroupGmm = dfClusterGmm.groupby('kGmm')
for (cluster, data) in dfGroupGmm:
    ax5.plot(data.X, data.Y, '.', label=cluster)
ax5.set_title("By GMM")
ax5.plot(U[:, 0], U[:, 1], 'g*', markersize=20)
