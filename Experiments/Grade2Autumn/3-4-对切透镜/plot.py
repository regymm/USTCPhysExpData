#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os
sys.path.append(os.path.abspath('/home/username/PhysicsExp/Core'))

from Core.mainfunc import *
from Core.gendocx import *

font()

#read data
fin = open('./data.txt', 'r')
d1 = readoneline(fin)
l1 = readonenumber(fin)
d2 = readoneline(fin)
l2 = readonenumber(fin)
fin.close()

#focus of small convex lens
fx = 3.5e-2
#wl
lambdaa = 632.8e-9

docu = Document()
docuaddtitle(docu)
# docuappend(docu, './picfull.png', './figure_1.png', './pic.png', result['string'], './picx.png')
#data process
#findout starts by hand
starts = [1, 0]
for i in range(0, 2):
    if i == 0:
        d = d1
        l = l1
    else:
        d = d2
        l = l2
    d = d / (l / fx - 1)
    print(d)
    dots = len(d) - 1
    deltas = []
    for j in range(dots):
        deltas.append(- d[j + 1] + d[j])
    print(deltas)
    start = starts[i]
    ks = np.array([math.sqrt(k + 1) - math.sqrt(k) for k in range(start, start + dots)])
    print(ks)
    simple_linear_plot(ks, deltas, xlab='$\sqrt{k+1}-\sqrt{k}$', ylab='条纹间距', title='条纹间距和条纹级数$\sqrt{k+1}-\sqrt{k}$图像', save=str(i)+'.png', show=1, issetrange=1)
    result = linear_regression(ks, deltas, quiet=0, simple=0)
    print('a=', result['slope'] ** 2 / lambdaa)
    docuappend(docu, './'+str(i)+'.png')
    docuappend(docu, result['string'])

    print('k\t\tdelta_k\t\tLk\t\tLk+1\t\tdelta_p')
    for j in range(dots):
        print(start + j, '\t\t', end='')
        print('%.3f' % (math.sqrt(start+j+1)-math.sqrt(start+j)), '\t\t', end='')
        print('%.3e' % d[j], '\t\t', end='')
        print('%.3e' % d[j + 1], '\t\t', end='')
        print('%.3e' % deltas[j], '\t\t', end='')
        print('')
    print('--------')
#I don't know I suffer from unexpected end of file error when adding these pictures, are they too big?
# docuappend(docu, '比利对切透镜', './IMG_20181011_202103.jpg', './IMG_20181011_204433.jpg')
# docuappend(docu, '梅斯林对切透镜', './IMG_20181018_201328.jpg', './IMG_20181018_203439.jpg')
docu.save('gen.docx')
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
# gendocx('gen.docx', 'pic.png', result['string'])

#generate docx #2
# docu = Document()
# docuaddtitle(docu)
# docuappend(docu, './picfull.png', './figure_1.png', './pic.png', result['string'], './picx.png')
# docu.save('gen.docx')


