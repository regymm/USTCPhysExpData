#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from physicsexp.mainfunc import *
from physicsexp.gendocx import *

# read data
# # 1
# data, data_orig, name = readdata('./data.txt', need=0b111)
# # 2
fin = open('./data.txt', 'r', encoding='utf-8')
angle1 = readoneline(fin)
pwr1 = readoneline(fin)
angle2 = readoneline(fin)
pwr2 = readoneline(fin)
angle3 = readoneline(fin)
pwr3 = readoneline(fin)
fin.close()

# data process
simple_plot(angle1, pwr1, xlab='角度/度', ylab='功率计读数', title='表面等离激元共振曲线：去离子水', save='1.png')
simple_plot(angle2, pwr2, xlab='角度/度', ylab='功率计读数', title='表面等离激元共振曲线：无水乙醇', save='2.png')
simple_plot(angle3, pwr3, xlab='角度/度', ylab='功率计读数', title='表面等离激元共振曲线：混合液2:1', save='3.png')

theta_sp0 = angle1[np.argmin(pwr1)]
theta_sp2 = angle2[np.argmin(pwr2)]
theta_sp3 = angle3[np.argmin(pwr3)]
print(theta_sp0, theta_sp2, theta_sp3)

# refractive index of the prism, given.
np = 1.5163
# refractive index of water
ns0 = 1.3333
# calculate the Re(Epsilon_m)
re_epsilon_m = np**2 * math.sin(math.radians(theta_sp0))**2 * ns0**2 / \
               (ns0**2 - np**2 * math.sin(math.radians(theta_sp0))**2)
print(re_epsilon_m)
ns2 = np * math.sin(math.radians(theta_sp2)) * \
      math.sqrt(re_epsilon_m / (re_epsilon_m - np**2 * math.sin(math.radians(theta_sp2))**2))
print(ns2)
ns3 = np * math.sin(math.radians(theta_sp3)) * \
      math.sqrt(re_epsilon_m / (re_epsilon_m - np**2 * math.sin(math.radians(theta_sp3))**2))
print(ns3)
# check the calc is correct
ns2 = np * math.sin(math.radians(theta_sp0)) * \
      math.sqrt(re_epsilon_m / (re_epsilon_m - np**2 * math.sin(math.radians(theta_sp0))**2))
print(ns2)

gendocx('gen.docx', '1.png', '2.png', '3.png')
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


