import sys
sys.path.append('C:\\Users\\pjw20\\OneDrive\\바탕 화면\\Download_Data_Sample\\deep-learning-from-scratch-master')
import numpy as np
from common.functions import softmax, cross_entropy_error

class simpleNet:
    def __init__(self):
        self.W = np.random.randn(2, 3) # 2 * 3 정규분포
    def predict(self, x):
        return np.dot(x, self.W)
    def loss(self, x, t):
        z = self.predict(x)
        y = softmax(z)
        loss = cross_entropy_error(y, t)
        return loss

net = simpleNet()
print(net.W)
x = np.array([0.6, 0.9])
print(net.W)
p = net.predict(x)
print(p)
t = np.array([0, 0, 1])
print(net.loss(x, t))


def num_gradient_1(f, x):
    h = 1e-4
    grad = np.zeros_like(x)

    for idx in range(x.size):
        tmp_val = x[idx]
        x[idx] = tmp_val + h
        fxh1 = f(x)
        x[idx] = tmp_val - h
        fxh2 = f(x)
        grad[idx] = (fxh1 - fxh2) / (2*h)
        x[idx] = tmp_val

    return grad

def num_gradient_2(f, X):
    if X.ndim == 1:
        return num_gradient_1(f, X)
    else:
        grad = np.zeros_like(X)
        for idx, x in enumerate(X):
            grad[idx] = num_gradient_1(f, x)
        return grad

f = lambda w: net.loss(x, t)
dW = num_gradient_2(f, net.W)
print(num_gradient_2(f, net.W))
