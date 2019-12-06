import numpy as np
from scipy.misc import derivative
from Function import Function

def parabol(y, x0, E):
    iterix = 0
    xc = x0
    dy = derivative(y, xc)
    d2y = derivative(y, xc, n=2)
    z = 0
    while abs(dy) > E:
        if d2y == 0:
            d2y = 0.001
        if d2y < 0:
            z = -1
        else:
            z = 1
        h = dy/d2y
        xn = xc - z*h
        while y(xn) > y(xc):
            h = h*0.25
            xn = xc - z*h
            iterix += 1
        xc = xn
        dy = derivative(y, xc)
        d2y = derivative(y, xc, n=2)
        iterix += 1
    return (xc, iterix)


def local_min(y, x_min, x_max, step):
    k = -1
    x_now = x_min
    F0 = y(x_min)
    F1 = y(x_min+step)
    min_frame = list()
    isFind = True
    while x_now + step < x_max:
        if F1 < F0:
           while F1 < F0:
               x_now += step
               F0 = y(x_now)
               F1 = y(x_now + step)
           k += 1
           min_frame.append(x_now - step)
           min_frame.append(x_now + step)
        else:
            x_now += step
            F0 = y(x_now)
            F1 = y(x_now+step)

    return (k, min_frame)

def Dihot(y, a, b, E):
    x_mid = 0
    res_find = list()
    l = 0
    while abs(b-a) > E:
        x_mid = (b+a)/2
        fx = y(x_mid)
        fa = y(a)
        res_find.append([a, b, l, x_mid])
        if fx*fa < 0:
            b = x_mid
        else:
            a = x_mid
    return (x_mid, res_find)