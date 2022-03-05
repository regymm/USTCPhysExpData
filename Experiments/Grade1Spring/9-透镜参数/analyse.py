#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
sys.path.append('..')

from template import *

fin = open('./data.txt', 'r')
u = readoneavg(fin)
v = readoneline(fin)
print(np.mean(v))
deltav = sqrtsum(calc_delta_a(v, quiet=1), calc_delta_b(v, 1e-3))
print('deltav:', deltav)
f1 = 1 / (1 / u + 1 / v)
deltaf1 = np.mean(f1) * deltav / (np.mean(v)**2 / u + np.mean(v))
print(np.mean(f1))
print('deltaf1:', deltaf1)


L = readoneavg(fin)
x1 = readoneline(fin)
x2 = readoneline(fin)
l = L - x2 - x1
print(np.mean(l))
deltal = sqrtsum(calc_delta_a(l), calc_delta_b(l, 1e-3))
print('deltal:', deltal)
f2 = (L ** 2 - l ** 2) / (4 * L)
deltaf2 = deltal * np.mean(l) / (2 * L)
print('deltaf2:', deltaf2)
print(np.mean(f2))


f3 = readoneline(fin)
deltaf3 = sqrtsum(calc_delta_a(f3), calc_delta_b(f3, 1e-3))
print(np.mean(f3))
print('deltaf3:', deltaf3)





u = readoneline(fin)
v = readoneline(fin)
f1 = 1/(1 / v + 1 / u)
print(f1)
print(np.mean(f1))

f2 = readoneline(fin)
print(np.mean(f2))
fin.close()



