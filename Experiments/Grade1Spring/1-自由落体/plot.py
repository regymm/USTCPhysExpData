#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import math
import sys
sys.path.append('..')

from template import linear_regression,font,readdata
from gendocx import gendocx

font()

data, data_orig, name = readdata('./data.txt')

### main processing ###
x = data[1]
y0 = data[0]
data.append(y0 / x)
y1 = data[2]
result = linear_regression(x, y1, quiet=0)
print('算得重力加速度:', 2 * result['slope'])

#plot
plt.scatter(x, y1, marker='*', color='black', label='原始数据')
# plt.plot(x, y1, '--', color='green', label='光滑曲线')
plt.plot(x, result['intercept']+ result['slope']* x, 'r', label='拟合直线')

plt.xlabel('时间 t/s')
plt.ylabel('平均速度 H/t / m/s')
plt.legend(loc=4)
plt.title('小球下落平均速度与时间关系图')

plt.savefig('pic.png')
plt.show()

gendocx('gen.docx', 'pic.png', result['string'])

