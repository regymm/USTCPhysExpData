#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os
sys.path.append(os.path.abspath('/home/username/PhysicsExp/Core'))

from Core.mainfunc import *
from Core.gendocx import *

font()

# read data
# # 1
# data, data_orig, name = readdata('./data.txt', need=0b111)
# # 2
fin = open('./data.txt', 'r')
Ro1 = readoneline(fin)
Rs = Ro1 / 2
Us1 = readoneline(fin)
Uo1 = readoneline(fin)
Us2 = readoneline(fin)
Uo2 = readoneline(fin)
fin.close()

# data process
delta = Us1 - Uo1
reladelta = delta / Us1
print(delta)
print(reladelta)
# inner resistance Rg
Rg = 100e3

# linear regression and plot
# #1
x = Rg / Rs
y = reladelta
x2 = np.linspace(min(x), max(x), 10000)
y2 = 1 / (1 + x2)
# result = linear_regression(x, y, simple=0)
setrange(x, y)
plt.plot(x, y, marker='o', color='black', label='原始数据')
plt.plot(x2, y2, color='red', label='理论结果')
plt.plot([min(x), max(x)], [.01, .01], color='green', label='误差1%线')
plt.xlabel('$\\frac{R_g}{R_s}$')
plt.ylabel('$\\frac{U_{s1}-U_{o1}}{U_{s1}}$')
plt.legend(loc=4)
plt.title('电压表内阻对结果的影响')
plt.savefig('pic.png')
plt.show()

x = Uo2
y = Us2 - Uo2
print(y)
print(100 * y / Us2)
plt.plot(x, y, marker='o', color='black', label='校准曲线')
plt.plot([min(x), max(x)], [0, 0], color='red')
plt.xlabel('$U_{o1}$')
plt.ylabel('$U_{s1}-U_{o1}$')
plt.legend(loc=4)
plt.title('电压表2V量程校准曲线')
plt.savefig('pic2.png')
plt.show()

# #2
# use automate tool
# simple_linear_plot(x, y, xlab='x axis', ylab='y axis', title='my pic', save='pic.png')


# generate docx #1
gendocx('gen.docx', 'pic.png', 'pic2.png')

# generate docx #2
# docu = Document()
# docuaddtitle(docu)
# docuappend(docu, './picfull.png', './figure_1.png', './pic.png', result['string'], './picx.png')
# docu.save('gen.docx')


