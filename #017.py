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


(x_train, t_train), (x_test, t_test) = load_mnist(normalize = True, one_hot_label = True)

train_size = x_train.shape[0]
batch_size = 10
batch_mask = np.random.choice(train_size, batch_size)
x_batch = x_train[batch_mask]
t_batch = t_train[batch_mask]

print(batch_mask)
print(x_train.size) # 60000*784

def cross_entropy_error_1(y, t):
    if y.ndim == 1:
        t = t.reshape(1, t.size)
        y = y.reshape(1, y.size)
    return -np.sum(t * np.log(y+1e-7)) / y.shape[0]


(x_train, t_train), (x_test, t_test) = load_mnist(normalize = True, one_hot_label = True)

print(t_train) # ex. [8 8 0 4 3 7 0 6 2 3]

def cross_entropy_error_2(y, t):
    if y.ndim == 1:
        t = t.reshape(1, t.size)
        y = y.reshape(1, y.size)
    batch_size = y.shape[0]
    return -np.sum(np.log(y[np.arange(batch_size), t] + 1e-7)) / batch_size


def shuffle_dataset(x, t):

    permutation = np.random.permutation(x.shape[0])
    x = x[permutation,:] if x.ndim == 2 else x[permutation,:,:,:]
    t = t[permutation, :]

    return x, t

train_size = x_train.shape[0]
batch_size = 10
x_train, t_train = shuffle_dataset(x_train, t_train)
x_batch = x_train[:10]
t_batch = t_train[:10]
print("x_batch: ", x_batch, "t_batch: ", t_batch)