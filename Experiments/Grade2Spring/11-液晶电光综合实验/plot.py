#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from physicsexp.mainfunc import *
from physicsexp.gendocx import *

# read data
# # 1
# data, data_orig, name = readdata('./data.txt', need=0b111)
# # 2
fin = open('./data.txt', 'r', encoding='utf-8')
volt = readoneline(fin)
perct1 = readoneline(fin)
perct2 = readoneline(fin)
perct3 = readoneline(fin)
vPosAng = readoneline(fin)
vPosTmax = readoneline(fin)
vPosTmin = readoneline(fin)
vNegAng = readoneline(fin)
vNegTmax = readoneline(fin)
vNegTmin = readoneline(fin)
hPosAng = readoneline(fin)
hPosTmax = readoneline(fin)
hPosTmin = readoneline(fin)
hNegAng = readoneline(fin)
hNegTmax = readoneline(fin)
hNegTmin = readoneline(fin)
fin.close()

# data process

perct = (perct1 + perct2 + perct3) / 3
simple_plot(volt, perct, xlab='电压/V', ylab='透过率/%', title='液晶光开关电光特性', save='1.png')
vAng = np.concatenate((-vNegAng[::-1], vPosAng))
vTmax = np.concatenate((vNegTmax[::-1], vPosTmax))
vTmin = np.concatenate((vNegTmin[::-1], vPosTmin))
simple_plot(vAng, vTmin, xlab='角度/度', lab='关透过率', show=0, issetrange=0)
simple_plot(vAng, vTmax, xlab='角度/度', ylab='透过率', lab='开透过率', dot='+', title='液晶光开关特性--水平方向透过率', save='2.png', issetrange=0)
simple_plot(vAng, vTmax/vTmin, xlab='角度/度', ylab='对比度', lab='对比度', title='液晶光开关特性--水平方向对比度', save='3.png')
print(vTmax/vTmin)

hAng = np.concatenate((-hNegAng[::-1], hPosAng))
hTmax = np.concatenate((hNegTmax[::-1], hPosTmax))
hTmin = np.concatenate((hNegTmin[::-1], hPosTmin))
simple_plot(hAng, hTmin, xlab='角度/度', lab='关透过率', show=0, issetrange=0)
simple_plot(hAng, hTmax, xlab='角度/度', ylab='透过率', lab='开透过率', dot='+', title='液晶光开关特性--竖直方向透过率', save='4.png', issetrange=0)
simple_plot([hAng[0], hAng[-1]], [5, 5], show=0, issetrange=0, clr='red', lab='阈值')
simple_plot(hAng, hTmax/hTmin, xlab='角度/度', ylab='对比度', lab='对比度', title='液晶光开关特性--水平方向对比度', save='5.png')
print(hTmax/hTmin)
gendocx('gen.docx', '1.png', '2.png', '3.png', '4.png', '5.png')
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


