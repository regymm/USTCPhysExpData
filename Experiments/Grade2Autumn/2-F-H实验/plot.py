#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os
sys.path.append(os.path.abspath('/home/username/PhysicsExp/Core'))

from Core.mainfunc import *
from Core.gendocx import *

font()

#read data
# #1
# data, data_orig, name = readdata('./data.txt', need=0b111)
# #2
fin = open('./data.txt', 'r')
u_g2k = readoneline(fin)
i_p = readoneline(fin)
i_p = i_p * 1e7
fin.close()

#data process

simple_plot(u_g2k, i_p, xlab='$U_{G_2K}$ / V', ylab='$I_P$ / $0.1\mu A$', title='氩原子激发曲线', save='curv.png')

u_g2k_min = []
i_p_min_points = []
min_points_idx = []
for i in range(1, len(u_g2k) - 1):
    if i_p[i] < i_p[i - 1] and i_p[i] < i_p[i + 1]:
        i_p_min_points.append(i_p[i])
        u_g2k_min.append(u_g2k[i])
        min_points_idx.append(i)
#对7个谷进行平滑处理，得到包络线
uminnew, iminsmooth = curve_smooth(u_g2k_min, i_p_min_points)
def getval(u):
    for i in range(len(uminnew) - 1):
        #get the point and return the value
        if u == uminnew[i]:
            return iminsmooth[i]
        if u > uminnew[i] and u < uminnew[i + 1]:
            return iminsmooth[i] + (u - uminnew[i]) * (iminsmooth[i + 1] - iminsmooth[i]) / (uminnew[i + 1] - uminnew[i])
    return 0
i_p_min = []
for i in u_g2k:
    i_p_min.append(getval(i))
#得到相差数据
i_p_diff = i_p - i_p_min
#求出6个半峰宽的点
fwhm_points = []
for i in range(6):
    fwhm_points.append(get_intersection_points(u_g2k[min_points_idx[i]:min_points_idx[i + 1]], i_p_diff[min_points_idx[i]:min_points_idx[i + 1]], max(i_p_diff[min_points_idx[i]:min_points_idx[i + 1]]) / 2))
    # print(max(i_p[min_points_idx[i]:min_points_idx[i + 1]]))
    # print(get_intersection_points(u_g2k[min_points_idx[i]:min_points_idx[i + 1]], i_p[min_points_idx[i]:min_points_idx[i + 1]], max(i_p[min_points_idx[i]:min_points_idx[i + 1]]) / 2))
print(fwhm_points)
peak_points_u = [np.mean(x) for x in fwhm_points]
print(peak_points_u)
#最小二乘法
result = linear_regression(np.array([i for i in range(1, 7)]), peak_points_u, quiet=0, simple=0)
# setrange(u_g2k, i_p, xy=0b11)
simple_plot(u_g2k, i_p, xlab='$U_{G_2K}$ / V', ylab='$I_P$ / $0.1\mu A$', title='氩原子激发曲线及相差曲线', show=0)
simple_plot(u_g2k, i_p_min, dot='+', clr='green', label='包络线', show=0)
simple_plot(u_g2k, i_p_diff, dot='*', clr='blue', label='相差曲线', save='curv2.png')
setrange(u_g2k, i_p, xy=0b11)

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
# simple_linear_plot(x, y, xlab='x axis', ylab='y axis', title='my pic', save='pic.png')


#generate docx #1
gendocx('gen.docx', 'curv.png', 'curv2.png')

#generate docx #2
# docu = Document()
# docuaddtitle(docu)
# docuappend(docu, './picfull.png', './figure_1.png', './pic.png', result['string'], './picx.png')
# docu.save('gen.docx')


