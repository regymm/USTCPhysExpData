#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
sys.path.append('..')

from template import *
from gendocx import *

font()

U1 = [0, 0, 0]
I1 = [0, 0, 0]
U2 = [0, 0, 0]
I2 = [0, 0, 0]
name = ['R', 'G', 'B']
color = ['r', 'g', 'b']
#read
fin = open('./data.txt', 'r')
for i in range(3):
    U1[i], I1[i] = readpart(fin, 2, need=0b100)
for i in range(3):
    I2[i], U2[i] = readpart(fin, 2, need=0b100)
fin.close()

#data process
#job 1
for i in range(3):
    # Usmooth, Ismooth = curve_smooth(U1[i], I1[i])
    plt.scatter(U1[i], I1[i], marker='o', color=color[i], label=name[i])
    plt.plot(U1[i], I1[i], color=color[i])
    #计算(估算)发光波长
    slope, intercept = linear_regression(U1[i][9:], I1[i][9:], simple=1, quiet=1)
    #$\Lamba = 1240 / E_g (nm) $ E_g eV
    U0 = math.fabs(intercept) / math.fabs(slope)
    print(name[i], '电压:', U0, '波长估算值(nm):', 1240/U0)

plt.xlabel('电压U / V')
plt.ylabel('电流I / A')
plt.legend(loc=4)
plt.title('LED伏安特性曲线')
plt.grid('on')
plt.savefig('UI.png')
plt.show()
#job 2
#plot I-U
for i in range(3):
    # Usmooth, Ismooth = curve_smooth(U2[i], I2[i])
    plt.scatter(I2[i], U2[i], marker='o', color=color[i], label=name[i])
    plt.plot(I2[i], U2[i], color=color[i])
plt.xlabel('电流 I / A')
plt.ylabel('相对发光强度(光电管电压U / V)')
plt.legend(loc=4)
plt.title('LED发光强度')
plt.grid('on')
plt.savefig('light.png')
plt.show()

gendocx('gen.docx', './UI.png', './light.png')


