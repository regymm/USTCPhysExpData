#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from physicsexp.mainfunc import *
from physicsexp.gendocx import *

# read data
# # 1
# data, data_orig, name = readdata('./data.txt', need=0b111)
# # 2
fin = open('./data.txt', 'r', encoding='utf-8')
f = readoneline(fin)
max1 = readoneline(fin)
max2 = readoneline(fin)
max3 = readoneline(fin)
fin.close()

# data process
print(max1, max2, max3)
simple_plot(f, max1, show=0, issetrange=0, lab='第1个信号', dot='+')
simple_plot(f, max2, show=0, issetrange=0, lab='第2个信号', dot='*')
simple_plot(f, max3, show=1, issetrange=0, lab='第3个信号', xlab='f/MHz', ylab='示波器格子数', dot='o',
            title='三个信号最高点位置随频率变化', save='1.png')

simple_plot(f, max2 - max1, show=0, issetrange=0, lab='max2-max1', dot='+',
            xlab='f/Mhz', ylab='最高点间距', title='第1,2个信号间距随频率变化')
simple_plot(f, max3 - max2, show=1, issetrange=0, lab='max3-max2', dot='*',
            xlab='f/Mhz', ylab='最高点间距', title='第2,3个信号间距随频率变化', save='2.png')
# simple_plot(f, [math.cos(max2[i] - max1[i]) for i in range(len(f))], show=0, issetrange=0, lab='max2-max1', dot='+',
#             xlab='f/Mhz', ylab='最高点间距', title='第1,2个信号间距随频率变化')
# simple_plot(f, [math.cos(max3[i] - max2[i]) for i in range(len(f))], show=1, issetrange=0, lab='max3-max2', dot='*',
#             xlab='f/Mhz', ylab='最高点间距', title='第2,3个信号间距随频率变化', save='2.png')
# linear regression and plot
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
# use automate tool
# simple_linear_plot(x, y, xlab='x axis', ylab='y axis', title='my pic', save='pic.png')


# generate docx #1
gendocx('gen.docx', '1.png', '2.png')

# generate docx #2
# docu = Document()
# docuaddtitle(docu)
# docuappend(docu, './picfull.png', './figure_1.png', './pic.png', result['string'], './picx.png')
# docu.save('gen.docx')


