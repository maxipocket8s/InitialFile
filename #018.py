class Relu:
    def __init__(self):
        self.mask = None
    def forward(self, x):
        self.mask = (x <= 0)
        out = x.copy()
        out[self.mask] = 0 # True 값을 0으로 변환한다.
        return out
    def backward(self, dout):
        dout[self.mask] = 0
        dx = dout
        return dx

import numpy as np

x = np.random.rand(3, 2)
