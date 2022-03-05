#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from physicsexp.mainfunc import *
from physicsexp.gendocx import *

# read data
# # 1
# data, data_orig, name = readdata('./data.txt', need=0b111)
# # 2
fin = open('./data.txt', 'r', encoding='utf-8')
volt1 = readoneline(fin)
cnt1 = readoneline(fin)
Al_num = readoneline(fin)
Time = readoneline(fin)
Cnt = readoneline(fin)
fin.close()

# data process

simple_plot(volt1, cnt1, dot='o', save='1.png', xlab='电压/V', ylab='计数', title='G-M管坪曲线', lab='计数')

# 强度，除去本底计数
Strength = Cnt / Time - 98. / (5 * 60)
StrRela = Strength / Strength[0]
# 质量厚度
Al_m = Al_num * 49
simple_plot(Al_m, Strength, dot='o', save='2.png',
            xlab='铝片质量厚度/ $mg/cm^{-2}$', ylab='单位时间计数', title='$\\beta$射线吸收曲线', lab='单位时间计数')
LnStr = np.log(StrRela)
simple_plot([Al_m[0], Al_m[-1]], [-4, -4], lab='下限', show=0, issetrange=0, clr='red', dot='+')
simple_plot(Al_m, LnStr, dot='o', show=0,
            xlab='铝片质量厚度/ $mg/cm^{-2}$', ylab='单位时间计数-相对值，对数', lab='单位时间计数-对数')
k1, b1 = linear_regression(Al_m[1:6], LnStr[1:6])
simple_plot([Al_m[0], Al_m[10]], [k1 * Al_m[0] + b1, k1 * Al_m[10] + b1], lab='拟合段1', clr='red', show=0, issetrange=0)
k2, b2 = linear_regression(Al_m[9:16], LnStr[9:16])
simple_plot([Al_m[5], Al_m[-1]], [k2 * Al_m[5] + b2, k2 * Al_m[-1] + b2], lab='拟合段2', title='$\\beta$射线吸收曲线'
            , clr='green', issetrange=0, save='3.png')
print(k1, k2)
h = 0 - (k1 * Al_m[0] + b1)
print(h)
Rx = ((-4 - h) - b2) / k2
print(Rx)
R = Rx / 49
print(R)
Emax = 1.85e-3 * Rx + 0.245
print(Emax)

gendocx('gen.docx', '1.png', '2.png', '3.png',
        'slope1, intercept1: %f %f' % (k1, b1), 'slope2, intercept2: %f %f' % (k2, b2))
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


