#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from physicsexp.mainfunc import *
from physicsexp.gendocx import *

# read data
# # 1
# data, data_orig, name = readdata('./data.txt', need=0b111)
# 2
fin = open('./data.txt', 'r', encoding='utf-8')
P1 = readoneline(fin)
t1 = readoneline(fin)
P2 = readoneline(fin)
t2 = readoneline(fin)
fin.close()

# data process

simple_plot(t1, P1, xlab='时间/s', ylab='压强/Pa', title='粗真空P-t图', save='1.png')
k1, b1 = simple_linear_plot(t1, np.log(P1), xlab='t/s', ylab='ln(P)', title='粗真空lnP-t图', save='11.png')
# the volume of bottle
V = 2
print(k1, b1)
print('Speed: ', - V * k1, ' L')


simple_plot(t2, P2, xlab='时间/s', ylab='压强/Pa', title='低真空P-t图', save='2.png')
simple_plot(t2, np.log(P2), xlab='t/s', ylab='ln(P)', title='低真空lnP-t图', show=0)
k2, b2 = simple_linear_plot(t2[:4], np.log(P2[:4]), xlab='t/s', ylab='ln(P)', title='低真空lnP-t图', dotlab='使用的数据', save='21.png')
# the volume of bottle
V = 2
print(k2, b2)
print('Speed(may be bad): ', - V * k2, ' L')

gendocx('gen.docx', '1.png', '11.png', 'k: %f, b: %f' % (k1, b1), '2.png', '21.png', 'k: %f, b: %f' % (k2, b2))

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
# gendocx('gen.docx', 'pic.png', result['string'])

# generate docx #2
# docu = Document()
# docuaddtitle(docu)
# docuappend(docu, './picfull.png', './figure_1.png', './pic.png', result['string'], './picx.png')
# docu.save('gen.docx')

