#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
sys.path.append('..')

from template import *

datanum = 3

U = []
tf = []

fin = open('./data.txt', 'r')
d = readpart(fin, 1, need=0b100)[0][0]
s = readpart(fin, 1, need=0b100)[0][0]
for i in range(datanum):
    U.append(readpart(fin, 1, need=0b100)[0][0])
    tf.append(readpart(fin, 1, need=0b100)[0])
fin.close()

print(d, s, U, tf)

rou1 = 981
rou2 = 1.293
p = 1.013e5
b = .00823
eita = 1.83e-5
g = 9.79
e = 1.6021e-19

const = 9 * math.sqrt(2) * math.pi * d * \
        ((eita * s)**3 / ((rou1 - rou2) * g))**.5 * \
        1 / U[i]

q = []
for i in range(datanum):
    tfmean = np.mean(tf[i])
    print('时间平均值:', tfmean)
    u_t = calc_delta_a(tf[i], P=95, quiet=0)
    print('时间不确定度:', u_t)
    r0 = (9 * eita * (s / tfmean) / (2 * g * (rou1 - rou2)))**.5
    print('油滴半径:', r0)
    u_r0 = .5 * u_t * r0 / tfmean
    print('油滴半径不确定度:', u_r0)
    q.append(
             const * (1 / (1 + b / (p * r0)))**1.5 * \
                    (1 / tfmean)**1.5
            )
    u_q = q[i] * sqrtsum(1.5 * 1 / (1 + p * r0 / b) * u_r0 / r0, 1.5 * u_t / tfmean)
    print('油滴带电量:', q[i])
    print('油滴带电荷数:', q[i] / e)
    print('电量不确定度:', u_q)
    print('---')
r = .5e-6
print(4/3 * math.pi * r**3 * (rou1 - rou2) * g / (6*math.pi*eita*r/(1 + b / (p * r))))
print((6*math.pi*eita*r/(1 + b / (p * r))) / (4/3 * math.pi * r**3 * rou1))
print(-math.log(.01)/2.89e5)
t=1.59e-5
print(3.38e-5*(t+1/2.89e5 * math.exp(-1.59e-5*2.89e5)))
