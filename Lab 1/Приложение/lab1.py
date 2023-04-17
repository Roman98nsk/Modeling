import matplotlib.pyplot as plt
import numpy as np
from math import sqrt

def normalize(arr, t_min, t_max):
    norm_arr = []
    diff = t_max - t_min
    diff_arr = max(arr) - min(arr)
    for i in arr:
        temp = (((i - min(arr))*diff)/diff_arr) + t_min
        norm_arr.append(temp)
    return norm_arr
 
def f1(t):
    return 4 - 5 * (t - 1)**2
 
def f2(t):
    return (t - 2)**2 / 2

t = np.arange(0.0, 2.0, 0.01)
fig, ax = plt.subplots()
plt.plot(t, f1(t), 'b', alpha=0.6, label="y = 4 - 5 * (x - 1)^2")
plt.plot(t, f2(t), 'g', alpha=0.6, label="y = (x - 2)^2 / 2")
 
a = 12 / 11 - sqrt(78) / 11
b = 12 / 11 + sqrt(78) / 11
plt.plot(a, f1(a), marker='.', ls='none', ms=10, c="r")
plt.plot(b, f1(b), marker='.', ls='none', ms=10, c="r")
 
n = 300
 
f1_len = 6.85
x = np.random.rand(n) * f1_len
x = normalize(x, 0, b - a)
x = list(map(lambda i: i + a, x))
y = list(map(lambda i: f1(i), x))
plt.plot(x, y, marker='.', ls='none', ms=2, c="r", label="point on y = 4 - 5 * (x - 1)^2")
 
f2_len = 2.24
x = np.random.rand(n) * f2_len
x = normalize(x, 0, b - a)
x = list(map(lambda i: i + a, x))
y = list(map(lambda i: f2(i), x))
plt.plot(x, y, marker='.', ls='none', ms=2, c="purple", label="point on y = (x - 2)^2 / 2")

points = 0
while points < 5000:
    x = np.random.rand() * (b - a) + a
    y = np.random.rand() * 4
    if y <= f1(x) and y >= f2(x):
        plt.plot(x, y, marker='.', ls='none', ms=1, c="black")
    points+=1

ax.legend(loc='lower left')

plt.show()