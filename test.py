import numpy as np
from scipy.misc import derivative

def f(x):
    f = np.array([2, 4, 6, 5, 4, 4, 5, 6, 7, 8])
    return f[int(x)]

x = 4
dx = 1
#dfx = (f[x+dx] - f[x])/dx
#d2fx = (f[int(dfx+dx)] - f[int(dfx)])/dx
#print(dfx, d2fx)

der = derivative(f, 5)
der2 = derivative(f, 2, n=2)

print(der, der2)