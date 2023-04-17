from random import *
from math import *

N = 1000000 
K = 100
n_i = [0] * (N)
x_i = [0] * (N)
seed()

for i in range(0, N):
    x = randint(0, 100)
    x_i[i] = x / K
    n_i[x] += 1

def x2(n_i):
    x2_result = 0
    p_i = 0
    p_i = 1.0/(K + 1)
    for i in range(0, 101):
        x2_result += (pow(n_i[i], 2)/p_i)
    x2_result = (x2_result / N) - N 
    return x2_result

print(f'Xu: {x2(n_i)}')
    
def auto_cor():
    sum_x, Krelation, s_2, sum_pow2, mat_oj = 0, 0, 0, 0, 0
    
    for i in range(0, N):
        sum_x += x_i[i]
        sum_pow2 += x_i[i] * x_i[i]

    _x = sum_x / N    
    sum_pow2 /= N
    s_2 = (sum_pow2 - (_x * _x))

    for offset in range (1, 30):
        for i in range(0, N - offset):
            Krelation += (x_i[i] - _x)*(x_i[i+offset] - _x)
        Krelation /= (N - offset) * s_2
        prt = "%.7f" % Krelation
        print(f'Смещение {offset} Автокорреляция {prt}')

    return Krelation

auto_cor() 

for i in range(0, 101):
    print(f'{i/100.0} - {n_i[i]}')
