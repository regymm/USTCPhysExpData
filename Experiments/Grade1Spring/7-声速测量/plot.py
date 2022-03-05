#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
sys.path.append('..')

from template import *
from gendocx import *

font()

#read
data, data_orig, name = readdata('./data.txt', need=0b111)
fin = open('./data.txt', 'r')
t = readoneavg(fin)
water = readoneavg(fin)
freq = readoneavg(fin)

x1 = readoneline(fin)
xair = readoneline(fin)
xwater = readoneline(fin)

lmetal = readoneline(fin)
tmetal = readoneline(fin)
lglass = readoneline(fin)
tglass = readoneline(fin)
fin.close()

#data process


#linear regression and plot
#1
x = np.array([i for i in range(1, len(x1) + 1)])
result1 = linear_regression(x, x1)
setrange(x, x1)
plt.scatter(x, x1, marker='o', color='black', label='原始数据')
plt.plot(x, result1['intercept'] + result1['slope'] * x, 'r', label='拟合直线')
plt.xlabel('第n个极大值')
plt.ylabel('距离$x_i$')
plt.legend(loc=4)
plt.title('空气 -- 驻波法')
plt.savefig('pic1.png')
plt.show()
print('speed:', result1['slope'] * 2 * freq)
print('delta:', sqrtsum(result1['s_slope'], calc_delta_b_graph(x, x1, 0, .02e-3, P=95, C=math.sqrt(3))))
print('deltab:', calc_delta_b_graph(x, x1, 0, .02e-3, P=95, C=math.sqrt(3)))
print('theory:', 331.45 * math.sqrt((1 + t / 273.15) * (1 + .3192 * water / 1.013e5)))
#2
x = np.array([i for i in range(1, len(xair) + 1)])
result2 = linear_regression(x, xair)
setrange(x, xair)
plt.scatter(x, xair, marker='o', color='black', label='原始数据')
plt.plot(x, result2['intercept'] + result2['slope'] * x, 'r', label='拟合直线')
plt.xlabel('第n个极大值')
plt.ylabel('距离$x_i$')
plt.legend(loc=4)
plt.title('空气 --  相位法')
plt.savefig('pic2.png')
plt.show()
print('speed:', result2['slope'] * 2 * freq)

#3
x = np.array([i for i in range(1, len(xwater) + 1)])
result3 = linear_regression(x, xwater)
setrange(x, xwater)
plt.scatter(x, xwater, marker='o', color='black', label='原始数据')
plt.plot(x, result3['intercept'] + result3['slope'] * x, 'r', label='拟合直线')
plt.xlabel('第n个极大值')
plt.ylabel('距离$x_i$')
plt.legend(loc=4)
plt.title('水 --  相位法')
plt.savefig('pic3.png')
plt.show()
print('speed:', result3['slope'] * 2 * freq)

datanum = 3
for i in range(datanum):
    print('metal %d : %f' % (i, lmetal[i] / tmetal[i]))
    print('glass %d : %f' % (i, lglass[i] / tglass[i]))

#generate docx #1
gendocx('gen.docx', 'pic1.png', result1['string'], 'pic2.png', result2['string'], 'pic3.png', result3['string'])

#generate docx #2
# docu = Document()
# docuaddtitle(docu)
# docuappend(docu, './picfull.png', './figure_1.png', './pic.png', result['string'], './picx.png')
# docu.save('gen.docx')


