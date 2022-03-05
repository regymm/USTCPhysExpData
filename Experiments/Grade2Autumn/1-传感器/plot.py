#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
sys.path.append('/home/username/PhysicsExp/Core')

from Core.mainfunc import *
from Core.gendocx import *

font()

#read data
# #1
# data, data_orig, name = readdata('./data.txt', need=0b111)
# #2
fin = open('./data.txt', 'r')
mass = readoneline(fin)
u1 = readoneline(fin)
u2 = readoneline(fin)
u3 = readoneline(fin)
uknown = readonenumber(fin)

pressure = readoneline(fin)
vout1 = readoneline(fin)


volume = readoneline(fin)
vout2 = readoneline(fin)
fin.close()

#data process


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
simple_linear_plot(mass, u1 - u1[0], xlab='质量m/g', ylab='电压U/mV', dot='o', dotlab='单臂', save=0, show=0)
simple_linear_plot(mass, u2 - u2[0], xlab='质量m/g', ylab='电压U/mV', dot='+', dotlab='半桥', save=0, show=0)
simple_linear_plot(mass, u3 - u3[0], xlab='质量m/g', ylab='电压U/mV', dot='*', dotlab='全桥', title='质量-输出电压图像（已减去零点）', save='pic.png', show=1)
linear_regression(mass, u1, quiet=0, simple=1)
linear_regression(mass, u2, quiet=0, simple=1)
linear_regression(mass, u3, quiet=0, simple=1)
print('---')

simple_linear_plot(pressure, vout1, xlab='压强P/MPa', ylab='输出电压U/V', dot='o', title='压强-输出电压图像', save='pic1.png', show=1)
linear_regression(pressure, vout1, quiet=0, simple=1)

simple_plot(volume, vout2, xlab='乙醇体积（mL）', ylab='输出电压U/V', dot='o', title='乙醇体积-输出电压图像', save='pic2.png', show=1)


#generate docx #1
gendocx('gen.docx', 'pic.png', 'pic1.png', 'pic2.png')

#generate docx #2
# docu = Document()
# docuaddtitle(docu)
# docuappend(docu, './picfull.png', './figure_1.png', './pic.png', result['string'], './picx.png')
# docu.save('gen.docx')


