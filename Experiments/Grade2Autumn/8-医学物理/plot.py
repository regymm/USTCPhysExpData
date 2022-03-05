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
x = readoneline(fin)
y = readoneline(fin)

freq = readoneline(fin)
li = readoneline(fin)
ld = readoneline(fin)
ri = readoneline(fin)
rd = readoneline(fin)
fin.close()

# data process


# exp 1
setrange(x, y)
# plt.scatter(x, y, marker='o', color='black', label='原始数据')
plt.scatter(x, y, marker='o', color='black')
# plt.plot(x, result['intercept'] + result['slope'] * x, 'r', label='拟合直线')
# plt.xlabel('外加压强P/KPa')
# plt.ylabel('输出电压U/mV')
# plt.legend(loc=4)
# plt.title('压力传感器特性曲线')
# plt.savefig('pic.png')
# plt.show()

# #2
# simple_plot(x, y, show=0, save=0)
simple_linear_plot(x[1:], y[1:], xlab='外加压强P/KPa', ylab='输出电压U/mV', title='压力传感器特性曲线', save='pic.png')

result = linear_regression(x[1:], y[1:], quiet=0, simple=0)

# exp 2
left = (li + ld) / 2
right = (ri + rd) / 2
left = left - left[4]
right = right - right[4]
freqlog = np.log(freq)

plt.scatter(freq, left, marker='o', label='左耳听阀')
freq2, left2 = curve_smooth(freqlog, left, insnum=1000)
plt.semilogx(np.exp(freq2), left2, color='g', label='左耳听阀')

plt.scatter(freq, right, marker='*', label='右耳听阀')
freq2, right2 = curve_smooth(freqlog, right, insnum=1000)
plt.semilogx(np.exp(freq2), right2, color='r', label='右耳听阀')

plt.xlabel('声音频率/Hz')
plt.ylabel('相对声压/dB')
plt.title('左右耳听阀曲线')
plt.legend()
plt.savefig('sound.png')
plt.show()

# generate docx #1
gendocx('gen.docx', 'pic.png', result['string'], 'sound.png')

# generate docx #2
# docu = Document()
# docuaddtitle(docu)
# docuappend(docu, './picfull.png', './figure_1.png', './pic.png', result['string'], './picx.png')
# docu.save('gen.docx')
