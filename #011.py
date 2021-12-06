import numpy as np
import matplotlib.pyplot as plt

x = np.array([-1.0, 1.0, 2.0])
y = x > 0
print(y)
y = y.astype(np.int32)
print(y)


def step_function(x):
    return np.array(x>0, dtype=np.int32)

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def LeRU(x):
    return np.maximum(0, x)

def softmax(x):
    c = np.max(x)
    return np.exp(x-c) / np.sum(np.exp(x-c))

x = np.linspace(-5, 5, 101)
y1 = step_function(x)
y2 = sigmoid(x)
y3 = LeRU(x)
y4 = softmax(x)
plt.plot(x, y1, label="step_function")
plt.plot(x, y2, linestyle="--", label="sigmoid")
plt.plot(x, y3, linestyle="-.", label="LeRU")
plt.plot(x, y4, linestyle=":", label="softmax")
plt.title('Activation h(x)')
plt.legend()
plt.ylim(-0.5, 1.5)
plt.show()


def init_network():
    network = {}
    network['W1'] = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])
    network['b1'] = np.array([0.1, 0.2, 0.3])
    network['W2'] = np.array([[0.1, 0.4], [0.2, 0.5], [0.3, 0.6]])
    network['b2'] = np.array([0.1, 0.2])
    return network

def forward(network, x):
    W1, W2 = network['W1'], network['W2']
    b1, b2 = network['b1'], network['b2']
    a1 = np.dot(x, W1)+b1
    z1 = sigmoid(a1)
    a2 = np.dot(z1, W2)+b2
    y = a2
    return y

A = init_network()
x = np.array([0.1, 0.5])
y = forward(A, x)
print(y)


B = {}
B['W1'] = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])
B['b1'] = np.array([0.1, 0.2, 0.3])
B['W2'] = np.array([[0.1, 0.4], [0.2, 0.5], [0.3, 0.6]])
B['b2'] = np.array([0.1, 0.2])

x = np.array([0.1, 0.5])
y = forward(B, x)
print(y)