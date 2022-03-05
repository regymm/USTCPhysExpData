#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
sys.path.append('..')

from template import *

s = []
t = []
#挡光片
d = (15.50 - 5.40) * 1e-3
h = 14.94e-3
L = 86.15e-2
fin = open('./data.txt', 'r')
for i in range(5):
    s.append(readpart(fin, 1, need=0b100)[0][0])
    t.append(np.mean(readpart(fin, 1, need=0b100)))
s = np.array(s)
t = np.array(t)
sdouble = 2 * s
vsquare = (d / t) ** 2
print('vsquare:', vsquare)
print('sdouble:', sdouble)
result = linear_regression(sdouble, vsquare, quiet=0)
print('g:', result['slope'] * L / h, result['s_slope'] * L / h)
for i in range(3):
    print('***collision type %d' % (i + 1))
    m1 = readpart(fin, 1, need=0b100)[0][0]
    m2 = readpart(fin, 1, need=0b100)[0][0]
    # print(m1, m2)
    t11 = readpart(fin, 1, need=0b100)[0]
    t21 = readpart(fin, 1, need=0b100)[0]
    t22 = readpart(fin, 1, need=0b100)[0]
    # print(t11, t21, t22)
    v11 = d / t11
    v21 = d / t21
    v22 = d / t22
    print('v:', v11, v21, v22)
    for j in range(3):
        print('\t*collision %d' % (j + 1))
        print('\tdelta_E / E:', 1 - (.5 * m1 * v22[j] ** 2 + .5 * m2 * v21[j] ** 2) / (.5 * m1 * v11[j] ** 2))
        print('\tdelta_P / P:', 1 - (m1 * v22[j] + m2 * v21[j]) / (m1 * v11[j]))
        print('\te:', (v21[j] - v22[j]) / (v11[j] - 0))
fin.close()

