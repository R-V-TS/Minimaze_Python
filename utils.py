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
        l += 1
        if fx*fa < 0:
            b = x_mid
        else:
            a = x_mid
    return (x_mid, res_find)


def Polinomial_min_square(x, y):
    A_sum = np.zeros((4, 1))
    A_matrix = np.zeros((3,3))
    s = np.shape(x)
    for i in range(0, s[0]):
        for j in range(1, 5):
            A_sum[j-1] += x[i]**j
    A_matrix[0][0] = s[0]
    A_matrix[0][1] = A_sum[0]
    A_matrix[0][2] = A_sum[1]
    A_matrix[1][0] = A_sum[0]
    A_matrix[1][1] = A_sum[1]
    A_matrix[1][2] = A_sum[2]
    A_matrix[2][0] = A_sum[1]
    A_matrix[2][1] = A_sum[2]
    A_matrix[2][2] = A_sum[3]
    print(A_matrix)
    B_matrix = np.zeros((3, 1))
    for i in range(0, s[0]):
        for j in range(0, 3):
            B_matrix[j] += y[i] * (x[i]**j)
    print(B_matrix)
    A_inv = np.linalg.inv(A_matrix)
    print(A_inv)
    C = A_inv.dot(B_matrix)
    print(C)
    poly_y = np.zeros(s)
    for i in range(0, s[0]):
        poly_y[i] = C[0] + C[1]*x[i] + C[2]*(x[i]**2)
    return (C, poly_y)

def calc_fun_min(a, x, y):
    s = np.shape(x)
    E = np.zeros((s))
    for i in range(0, s[0]):
        E[i] = (a[0] + a[1]*x[i] + a[2]*(x[i]**2) - y[i])**2
    return np.mean(E)

def Polinom_kord(x, y, manual_val, E = 1e-4):
    s = np.shape(x)
    A_val = np.array(manual_val, dtype=float)
    h = np.array([1, 1, 1], dtype=float)
    an = np.array([0, 0, 0], dtype=float)
    
    while np.sqrt(h[0]**2 + h[1]**2 + h[2]**2) > E:
        Func = calc_fun_min(A_val, x, y)
        for i in range(0, 3):
            A_tmp = A_val.copy()
            A_tmp[i] += h[i]
            Func_tmp1 = calc_fun_min(A_tmp, x, y)
            A_tmp[i] -= 2*h[i]
            Func_tmp2 = calc_fun_min(A_tmp, x, y)
            if Func_tmp1 < Func:
                an[i] = A_val[i] + h[i]
            elif Func_tmp2 < Func:
                an[i] = A_val[i] - h[i]
            else:
                an[i] = A_val[i]

        if an[0] == A_val[0]:
            h[0] *= 0.5

        if an[1] == A_val[1]:
            h[1] *= 0.5

        if an[2] == A_val[2]:
            h[2] *= 0.5

        A_val = an.copy()

    print(A_val)
    poly_y = np.zeros(s)
    for i in range(0, s[0]):
        poly_y[i] = A_val[0] + A_val[1] * x[i] + A_val[2] * (x[i] ** 2)
    return poly_y