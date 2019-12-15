import numpy as np
import scipy as sp
from scipy import interpolate
from matplotlib import pyplot as plt
from utils import local_min, Dihot, parabol, Polinomial_min_square, Polinom_kord
from Function import Function

# Set start values
accuracy = 0.1
x = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60]
y = [7.11, 6.89, 7.84, 7.67, 6.61, 7.06, 7.09, 6.85, 6.58, 6.71, 8.56, 8.49, 9.88]

# Interpolation cubic splain
new_x = np.linspace(min(x), max(x), max(x)*(1/accuracy))
new_y = interpolate.interp1d(x, y, kind="cubic")(new_x)

# Create function for calculate
f = Function(new_x, new_y, (1/accuracy))

plt.figure(1)
plt.plot(x, y, 'yo', label="Исходные точки")
plt.plot(new_x, new_y, 'b-', label="Интерполяция спалайном")
plt.legend()
plt.show()

# Find local minimum
(h, xy_min) = local_min(f.f, 0, f.limits()[1]-1, 5*accuracy)
print(h, xy_min)

# Find minimum via Dihotomia
minimum_x_dihot = np.zeros((h+1, 1))
minimum_y_dihot = np.zeros((h+1, 1))
x_line = np.array([0, 0])
y_line = np.array([0, 60])
result_table = list()

plt.figure(2)
plt.plot(new_x, new_y, 'b-')
#Print line local minimum
for i in range(0, (h+1)*2, 2):
    x_line = [new_x[int(xy_min[i]/accuracy)], new_x[int(xy_min[i]/accuracy)]]
    plt.plot(x_line, y_line, 'y*-')
    x_line = [new_x[int(xy_min[i+1]/accuracy)], new_x[int(xy_min[i+1]/accuracy)]]
    plt.plot(x_line, y_line, 'y*-')
    #Find minimum in area
    (min_index, res_tab) = Dihot(f.f, xy_min[i], xy_min[i+1], accuracy)
    result_table.append(res_tab)
    minimum_x_dihot[int(i/2)] = new_x[int(min_index/accuracy)]
    minimum_y_dihot[int(i/2)] = new_y[int(min_index/accuracy)]
    #Plot local minimum in area
    plt.plot(new_x[int(min_index/accuracy)], new_y[int(min_index/accuracy)], 'ro')

plt.show()
print(result_table)

#print global minimum
print(minimum_x_dihot)
print(min(minimum_y_dihot))

# Parabole method
parabol_min = list()
min_y_parab = np.zeros((10, 1))
min_x_parab = np.zeros((10, 1))
plt.figure(2)
plt.plot(new_x, new_y, 'b-')
for i in range(0, 10):
    point = np.random.uniform(0, 59, 1) # равномерное распр испр
    if point > 60:
        point -= 60 - 1*accuracy
    (min_idx, iterix) = parabol(f.f, point, accuracy)
    min_x_parab[i] = min_idx
    min_y_parab[i] = f.f(min_idx)
    print(point, min_idx, f.f(min_idx), iterix)
    plt.plot(min_idx, f.f(min_idx), "yo")

plt.show()
print(min(min_y_parab))

(C, poly_y) = Polinomial_min_square(x, y)
C *= .9
poly_y2 = Polinom_kord(x, y, C)
plt.figure(2)
plt.plot(x, y, 'yo', label="Исходные точки")
plt.plot(x, poly_y, 'b-', label="Аналитический метод")
plt.plot(x, poly_y2, 'g-', label="Цифровой метод")
plt.legend()
plt.title("Интерполированая функция")
plt.show()

