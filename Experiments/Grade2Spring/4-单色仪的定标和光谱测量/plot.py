#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from physicsexp.mainfunc import *
from physicsexp.gendocx import *


def load_txt(fname):
    draw = np.loadtxt(fname, delimiter=' ')
    d1 = []
    d2 = []
    for i in draw:
        d1.append(i[0])
        d2.append(i[1])
    return d1, d2

purewl, purestg = load_txt('./My/BrWPure.txt')
redwl, redstg = load_txt('./My/BrWRed.txt')
bluewl, bluestg = load_txt('./My/BrWBlue.txt')
greenwl, greenstg = load_txt('./My/BrWGreen.txt')
simple_plot(purewl, purestg, show=0, issetrange=0, islegend=0)
simple_plot(redwl, redstg, show=0, issetrange=0, clr='red', islegend=0)
simple_plot(bluewl, bluestg, show=0, issetrange=0, clr='blue', islegend=0)
simple_plot(greenwl, greenstg, xlab='波长', ylab='发光相对强度',
        save='1.png', issetrange=0, clr='green', islegend=0, title='溴钨灯光谱以及加红绿蓝滤波片后的光谱')

redabs = [purestg[i] - redstg[i] for i in range(len(purestg))]
blueabs = [purestg[i] - bluestg[i] for i in range(len(purestg))]
greenabs = [purestg[i] - greenstg[i] for i in range(len(purestg))]
simple_plot(redwl, redabs, show=0, issetrange=0, clr='red', islegend=0)
simple_plot(bluewl, blueabs, show=0, issetrange=0, clr='blue', islegend=0)
simple_plot(greenwl, greenabs, xlab='波长', ylab='吸收相对强度',
        save='2.png', issetrange=0, clr='green', islegend=0, title='红绿蓝滤波片的吸收光谱')


redabs = [(purestg[i] - redstg[i]) / purestg[i] for i in range(len(purestg))]
blueabs = [(purestg[i] - bluestg[i]) / purestg[i] for i in range(len(purestg))]
greenabs = [(purestg[i] - greenstg[i]) / purestg[i] for i in range(len(purestg))]
simple_plot(redwl, redabs, show=0, issetrange=0, clr='red', islegend=0)
simple_plot(bluewl, blueabs, show=0, issetrange=0, clr='blue', islegend=0)
simple_plot(greenwl, greenabs, xlab='波长', ylab='吸收相对比例',
        save='3.png', issetrange=0, clr='green', islegend=0, title='红绿蓝滤波片的吸收比例光谱')

gendocx('gen.docx', 
        '滤波片光谱分析', '1.png', '2.png', '3.png', 
        '钠灯各线系光谱', './My/1Na589-300V.bmp', './My/2Na497-798V.bmp', './My/3Na568-633V.bmp', './My/4Na616-766V.bmp', 
        '红宝石发射光谱', './My/Ruby-531V.bmp')

# read data
# # 1
# data, data_orig, name = readdata('./data.txt', need=0b111)
# # 2
# fin = open('./data.txt', 'r', encoding='utf-8')
# x = readoneline(fin)
# y = readoneline(fin)
# z = readonenumber(fin)
# fin.close()

# data process


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


