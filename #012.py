import sys
sys.path.append("C:\\Users\\pjw20\\OneDrive\\바탕 화면\\Download_Data_Sample\\deep-learning-from-scratch-master")
from dataset.mnist import load_mnist
import numpy as np
from PIL import Image


import pickle
def step_function(x):
    return np.array(x>0, dtype=np.int32)
def sigmoid(x):
    return 1 / (1 + np.exp(-x))
def LeRU(x):
    return np.maximum(0, x)
def softmax(x):
    c = np.max(x)
    return np.exp(x-c) / np.sum(np.exp(x-c))


(x_train, t_train), (x_test, t_test) = load_mnist(normalize = False, flatten = True, one_hot_label = False)

print(x_train.shape)
print(t_train.shape)
print(x_test.shape)
print(t_test.shape)


def img_show(img):
    pil_img = Image.fromarray(np.uint8(img))
    pil_img.show()

img = x_train[0]
label = t_train[0]
img = img.reshape(28, 28)
img_show(img)
print(label)


def get_data():
    (x_train, t_train), (x_test, t_test) = load_mnist(normalize = True, flatten = True, one_hot_label = False)
    return x_test, t_test

def init_network():
    with open("C:\\Users\\pjw20\\OneDrive\\바탕 화면\\Download_Data_Sample\\deep-learning-from-scratch-master\\ch03\\sample_weight.pkl", 'rb') as f:
        network = pickle.load(f)
    return network

def predict(network, x):
    W1, W2, W3 = network['W1'], network['W2'], network['W3']
    b1, b2, b3 = network['b1'], network['b2'], network['b3']
    a1 = np.dot(x, W1) + b1
    z1 = sigmoid(a1)
    a2 = np.dot(z1, W2) + b2
    z2 = sigmoid(a2)
    a3 = np.dot(z2, W3) + b3
    y = softmax(a3)
    return y

x, t = get_data()
network = init_network()
accuracy_cnt = 0
for i in range(len(x)):
    y = predict(network, x[i])
    p = np.argmax(y)
    if p == t[i]:
        accuracy_cnt += 1
print("Accuracy: " + str(float(accuracy_cnt) / len(x)))