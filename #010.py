import numpy as np
import matplotlib.pyplot as plt
x = np.arange(0, 6, 0.1)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.tanh(x)
plt.plot(x, y1, label="sin")
plt.plot(x, y2, linestyle="--", label="cos") # cos 함수의 경우 점선으로 그리기
plt.plot(x, y3, linestyle=":", label="tanh") # Supported values are '-', '--', '-.', ':'..
plt.xlabel("x") # x축 이름
plt.ylabel("y") # y축 이름
plt.title("sin & cos & tanh") # 제목
plt.legend() # label 보이도록
plt.show()


import matplotlib.pyplot as plt
from matplotlib.image import imread
img = imread('C:\\Users\\pjw20\\OneDrive\\사진\\증명사진_박주원.jpg')
plt.imshow(img)
plt.show()


# 퍼셉트론 구현
def AND1(x1, x2):
    w1, w2, theta = 0.5, 0.5, 0.7
    tmp = x1*w1 + x2*w2
    if tmp <= theta:
        return 0
    elif tmp > theta:
        return 1
import numpy as np
def AND2(x1, x2):
    x= np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.7
    if np.sum(x*w) + b <= 0:
        return 0
    else:
        return 1
print(AND1(0, 0), AND1(0, 1), AND1(1, 0), AND1(1, 1))
print(AND2(0, 0), AND2(0, 1), AND2(1, 0), AND2(1, 1))

def NAND1(x1, x2):
    w1, w2, theta = -0.5, -0.5, -0.7
    tmp = x1*w1 + x2*w2
    if tmp <= theta:
        return 0
    else:
        return 1
def NAND2(x1, x2):
    x = np.array([x1, x2])
    w = np.array([-0.5, -0.5])
    b = 0.7
    if np.sum(x*w) + b <= 0:
        return 0
    else:
        return 1
print(NAND1(0, 0), NAND1(0, 1), NAND1(1, 0), NAND1(1, 1))
print(NAND2(0, 0), NAND2(0, 1), NAND2(1, 0), NAND2(1, 1))

def OR1(x1, x2):
    w1, w2, theta = 0.5, 0.5, 0.3
    tmp = x1*w1 + x2*w2
    if tmp <= theta:
        return 0
    else:
        return 1
def OR2(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.3
    if np.sum(x*w) + b <= 0:
        return 0
    else:
        return 1
print(OR1(0, 0), OR1(0, 1), OR1(1, 0), OR1(1, 1))
print(OR2(0, 0), OR2(0, 1), OR2(1, 0), OR2(1, 1))


def XOR1(x1, x2):
    nand_w1, nand_wa2, nand_theta = -0.5, -0.5, -0.7
    nand_tmp = x1*nand_w1 + x2*nand_wa2
    if nand_tmp <= nand_theta:
        nand_result = 0
    else:
        nand_result = 1
    or_w1, or_w2, or_theta = 0.5, 0.5, 0.3
    or_tmp = x1*or_w1 + x2*or_w2
    if or_tmp <= or_theta:
        or_result = 0
    else:
        or_result = 1
    and_w1, and_w2, and_theta = 0.5, 0.5, 0.8
    and_tmp = nand_result*and_w1 + or_result*and_w2
    if and_tmp <= and_theta:
        return 0
    else:
        return 1
def XOR2(x1, x2):
    x = np.array([x1, x2])
    nand_w = np.array([-0.5, -0.5])
    w = np.array([0.5, 0.5])
    nand_b = 0.7
    or_b = -0.3
    if np.sum(x*nand_w) + nand_b <= 0:
        nand_x = 0
    else:
        nand_x = 1
    if np.sum(x*w) + or_b <= 0:
        or_x = 0
    else:
        or_x = 1
    and_x = np.array([nand_x, or_x])
    and_b = -0.8
    if np.sum(and_x*w) + and_b <= 0:
        return 0
    else:
        return 1
print(XOR1(0, 0), XOR1(0, 1), XOR1(1, 0), XOR1(1, 1))
print(XOR2(0, 0), XOR2(0, 1), XOR2(1, 0), XOR2(1, 1))

def XOR(x1, x2):
    s1 = NAND1(x1, x2)
    s2 = OR1(x1, x2)
    y = AND1(s1, s2)
    return y
print(XOR(0, 0), XOR(0, 1), XOR(1, 0), XOR(1, 1))