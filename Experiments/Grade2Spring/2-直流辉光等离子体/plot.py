#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from physicsexp.mainfunc import *
from physicsexp.gendocx import *

font()

# read data
# # 1
# data, data_orig, name = readdata('./data.txt', need=0b111)
# # 2
fin = open('./data.txt', 'r', encoding='utf-8')
U0 = readoneline(fin)
I0 = readoneline(fin)
U1 = readoneline(fin)
I1 = readoneline(fin)
P0 = readoneline(fin)
Up = readoneline(fin)
Ul11 = readoneline(fin)
Ul12 = readoneline(fin)[::-1]
Il11 = readoneline(fin)
Il12 = readoneline(fin)[::-1]
Ul21 = readoneline(fin)
Ul22 = readoneline(fin)[::-1]
Il21 = readoneline(fin)
Il22 = readoneline(fin)[::-1]
fin.close()

# data process

simple_plot(I0, U0, xlab='I/A', ylab='U/V', title='辉光放电伏安特性曲线 - 20Pa', save='11.png')
simple_plot(I1, U1, xlab='I/A', ylab='U/V', title='辉光放电伏安特性曲线 - 40Pa', save='12.png')
simple_plot(P0, Up, xlab='P/Pa', ylab='U/V', title='击穿电压随压强变化曲线', save='2.png')
simple_linear_plot(np.log(P0), P0/Up, xlab='$lnP$', ylab='$\\frac{P}{U}$', title='验证帕邢定律线性回归曲线', save='3.png')
# --- 1st
simple_plot(Ul11, Il11, show=0, issetrange=0)
simple_plot(Ul12, Il12, show=0, issetrange=0, xlab='U/V', ylab='I/uA', title='双探针伏安特性-P=20Pa, P=8.67W')
offset1 = -8
s1, i1 = linear_regression(Ul11[offset1:], Il11[offset1:], simple=1)
s2, i2 = linear_regression(Ul12[offset1:], Il12[offset1:], simple=1)
rg = np.array([0, max(Ul11[offset1:])])
plt.plot(rg, rg * s1 + i1)
rg = np.array([min(Ul12[offset1:]), 0])
plt.plot(rg, rg * s2 + i2)
offset2 = 9
s3, i3 = linear_regression(Ul12[:offset2][::-1] + Ul11[:offset2],
                           Il12[:offset2][::-1] + Il11[:offset2], simple=1)
offset3 = 14
rg = np.array([min(Ul12[:offset3]), max(Ul11[:offset3])])
plt.plot(rg, rg * s3 + i3)
Ii01 = i1
Ii02 = -i2
dVodI = - 1 / s3
Te = - 1 / kb * electron * (Ii01 * Ii02) / (Ii01 + Ii02) * dVodI
Ie0 = .05
dia = 1.e-3
Se = .25 * math.pi * dia**2
Ne = 4 * Ie0 / (electron * Se) * math.sqrt(math.pi * me / (8 * kb * Te))
print('Ii01, Ii02, dV/dI, Te, Ne:')
print(Ii01)
print(Ii02)
print(dVodI)
print(Te)
print(Ne)
plt.savefig('41.png')
plt.show()
# --- 2nd
Ul11 = Ul21
Ul12 = Ul22
Il11 = Il21
Il12 = Il22
simple_plot(Ul11, Il11, show=0, issetrange=0)
simple_plot(Ul12, Il12, show=0, issetrange=0, xlab='U/V', ylab='I/uA', title='双探针伏安特性-P=20Pa, P=3.82W')
offset1 = -8
s1, i1 = linear_regression(Ul11[offset1:], Il11[offset1:], simple=1)
s2, i2 = linear_regression(Ul12[offset1:], Il12[offset1:], simple=1)
rg = np.array([0, max(Ul11[offset1:])])
plt.plot(rg, rg * s1 + i1)
rg = np.array([min(Ul12[offset1:]), 0])
plt.plot(rg, rg * s2 + i2)
offset2 = 9
s3, i3 = linear_regression(Ul12[:offset2][::-1] + Ul11[:offset2],
                           Il12[:offset2][::-1] + Il11[:offset2], simple=1)
offset3 = 14
rg = np.array([min(Ul12[:offset3]), max(Ul11[:offset3])])
plt.plot(rg, rg * s3 + i3)
Ii01 = i1
Ii02 = -i2
dVodI = - 1 / s3
Te = - 1 / kb * electron * (Ii01 * Ii02) / (Ii01 + Ii02) * dVodI
Ie0 = .05
dia = 1.e-3
Se = .25 * math.pi * dia**2
Ne = 4 * Ie0 / (electron * Se) * math.sqrt(math.pi * me / (8 * kb * Te))
print('Ii01, Ii02, dV/dI, Te, Ne:')
print(Ii01)
print(Ii02)
print(dVodI)
print(Te)
print(Ne)
plt.savefig('42.png')
plt.show()
# simple_plot(Ul21, Il21, show=0, issetrange=0)
# simple_plot(Ul22, Il22, show=0, issetrange=0, xlab='U/V', ylab='I/uA', title='双探针伏安特性-P=40Pa, P=3.82W')
# plt.show()
# plt.savefig('42.png')
# simple_plot(Ul2, Il2, show=0)
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
gendocx('gen.docx', '11.png', '12.png', '2.png', '3.png', '41.png', '42.png')

# generate docx #2
# docu = Document()
# docuaddtitle(docu)
# docuappend(docu, './picfull.png', './figure_1.png', './pic.png', result['string'], './picx.png')
# docu.save('gen.docx')


