#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from physicsexp.mainfunc import *
from physicsexp.gendocx import *

# read data
# # 1
# data, data_orig, name = readdata('./data.txt', need=0b111)
# # 2
fin = open('./data.txt', 'r', encoding='utf-8')
tI = readoneline(fin)
tB = [readoneline(fin), readoneline(fin)]
IBup = readoneline(fin)
IIup = readoneline(fin)
IBdown = readoneline(fin)
IIdown = readoneline(fin)
fin.close()

# data process


def I2B(I, isdown):
    for i in range(len(tI) - 1):
        if tI[i] < I < tI[i + 1]:
            return (tB[isdown][i + 1] - tB[isdown][i]) / (tI[i + 1] - tI[i]) * (I - tI[i]) + tB[isdown][i]
        elif tI[i] == I:
            return tB[isdown][i]
        elif tI[i + 1] == I:
            return tB[isdown][i + 1]
        else:
            pass
    return -1


def finddeltaB(I, B, Ihalf):
    cnt = 0
    B1 = 0
    for i in range(len(I) - 1):
        if I[i] < Ihalf < I[i + 1] or I[i + 1] < Ihalf < I[i]:
            if cnt == 0:
                B1 = (B[i + 1] - B[i]) / (I[i + 1] - I[i]) * (Ihalf - I[i]) + B[i]
                cnt = cnt + 1
            else:
                B2 = (B[i + 1] - B[i]) / (I[i + 1] - I[i]) * (Ihalf - I[i]) + B[i]
                return math.fabs(B2 - B1)


Bup = np.array([I2B(i, 0) for i in IBup])
simple_plot(Bup, IIup, lab='上升', dot='x', show=0)
Br = Bup[np.argmin(IIup)]
Ir = IIup[np.argmin(IIup)]
I0 = 50
Ihalf = 2 * I0 * Ir / (I0 + Ir)
dB = finddeltaB(IIup, Bup, Ihalf)
print(Br, Ir, Ihalf, dB)

Bdown = np.array([I2B(i, 1) for i in IBdown])
simple_plot(Bdown, IIdown, lab='下降', xlab='B/mT', ylab='I/$\\mu A$', dot='o', title='磁场上升及下降时的谐振腔输出电流', save='1.png')
Br = Bdown[np.argmin(IIdown)]
Ir = IIdown[np.argmin(IIdown)]
I0 = 51
Ihalf = 2 * I0 * Ir / (I0 + Ir)
dB = finddeltaB(IIdown, Bdown, Ihalf)
print(Br, Ir, Ihalf, dB)
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
gendocx('gen.docx', '1.png')

# generate docx #2
# docu = Document()
# docuaddtitle(docu)
# docuappend(docu, './picfull.png', './figure_1.png', './pic.png', result['string'], './picx.png')
# docu.save('gen.docx')


