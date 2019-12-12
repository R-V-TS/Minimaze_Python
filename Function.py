import numpy as np

class Function:
    x = np.array([0])
    y = np.array([0])
    mn = 1
    def __init__(self, arr_x, arr_y, mn):
        self.y = arr_y
        self.x = arr_x
        self.mn = mn

    def f(self, idx):
        return self.y[int(idx*self.mn)]

    def x(self, idx):
        return self.x[int(idx * self.mn)]

    def limits(self):
        return [0, max(self.y.shape)/self.mn]
