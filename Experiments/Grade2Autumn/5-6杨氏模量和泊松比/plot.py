#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os
sys.path.append(os.path.abspath('/home/username/PhysicsExp/Core'))

from Core.mainfunc import *
from Core.gendocx import *

font()

#read data
# #1
# data, data_orig, name = readdata('./data.txt', need=0b111)
# #2
fin = open('./data.txt', 'r')
m = readoneline(fin)
deltaL = readoneline(fin)
Ug = readoneline(fin)
fin.close()

#data process
for i in range(1, len(m)):
    m[i] = m[i - 1] + m[i]
print(m)
print(deltaL)
print(Ug)
print("deltaL-m")
result1 = linear_regression(m, deltaL, quiet=0, simple=0)
d = .2e-3
L = 94.6e-2
E = 4*L/(math.pi * d**2 * result1['slope'])
print("E: ", E)

print("Ug-deltaL")
result2 = linear_regression(deltaL, Ug, quiet=0, simple=0)
U_AC = .415
R4 =  15.89
Rs = 35.11
print("miu")
miu = .5 * (4 * (R4 / Rs + 1) * result2['slope'] / U_AC - 1)
print(miu)


simple_linear_plot(m, deltaL, xlab='m', ylab='$\\Delta L$', title='加砝码质量$m$和伸长量$\\Delta L$图像', save='1.png', issetrange=1)
simple_linear_plot(deltaL, Ug, xlab='$\\Delta L$', ylab='$U_g$', title='电桥电压$U_g$和伸长量$\\Delta L$图像', save='2.png', issetrange=1)
#linear regression and plot
# #1
# result = linear_regression(x, y)
# setrange(x, y)
# plt.scatter(x, y, marker='o', color='black', label='原始数据')
# plt.plot(x, result['intercept'] + result['slope'] * x, 'r', label='拟合直线')
# plt.xlabel('')
# plt.ylabel('')
# plt.legend(loc=4)
# plt.title('')
# plt.savefig('pic.png')
# plt.show()

# #2
#use automate tool
# simple_linear_plot(x, y, xlab='x axis', ylab='y axis', title='my pic', save='pic.png')


#generate docx #1
gendocx('gen.docx', '1.png', result1['string'], 'E的值：%f' % E, '2.png', result2['string'], 'μ的值：%f' % miu)

#generate docx #2
# docu = Document()
# docuaddtitle(docu)
# docuappend(docu, './picfull.png', './figure_1.png', './pic.png', result['string'], './picx.png')
# docu.save('gen.docx')


