def function_1(x):
    return 0.01*x**2 + 0.1*x

import numpy as np
import matplotlib.pyplot as plt
x = np.arange(0.0, 20.0, 0.1)
y = function_1(x)
plt.xlabel("x")
plt.ylabel('f(x)')
plt.plot(x, y, linestyle="--", label='0.01*x**2 + 0.1*x')
plt.legend()
plt.title("Numerical Differentiation")
plt.show()


def num_diff(f, x): # 수치 미분
    h = 1e-4 # 0.0001
    return (f(x+h) - f(x-h)) / (2*h)

print(num_diff(function_1, 5))
print(num_diff(function_1, 10))


def function_2(x):
    return x[0]**2 + x[1]**2

def num_gradient(f, x): # 기울기
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

print(num_gradient(function_2, np.array([3.0, 4.0])))


def grad_descent(f, init_x, lr=0.01, step_num=100): # 경사하강법
    x = init_x
    for i in range(step_num):
        grad = num_gradient(f, x)
        x -= lr*grad
    return x

init_x = np.array([-3.0, 4.0])
print(grad_descent(function_2, init_x, lr=0.1, step_num=100))