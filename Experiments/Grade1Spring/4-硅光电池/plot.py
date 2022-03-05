#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
sys.path.append('..')

from template import *
from gendocx import *

font()

def getlx(d):
    return 40 / (d / .50)
#read
fin = open('./data.txt', 'r')
Udark, Idark = readpart(fin, 2, need=0b100)

#data process
#WARNING: old data may be overwriten by new
#job 1
Udarksmooth, Idarksmooth = curve_smooth(Udark, Idark)
setrange(Udark, Idark)
plt.scatter(Udark, Idark, marker='o', color='black', label='原始数据')
plt.plot(Udarksmooth, Idarksmooth, label='光滑曲线')
plt.xlabel('电压U / V')
plt.ylabel('电流I / A')
plt.legend(loc=4)
plt.title('硅光电池暗伏安特性曲线')
plt.grid('on')
plt.savefig('dark.png')
plt.show()
#job 2
dnum = 4
d = [None for i in range(dnum)]
RL = [None for i in range(dnum)]
U = [None for i in range(dnum)]
I = [None for i in range(dnum)]
P = [None for i in range(dnum)]
L = [None for i in range(dnum)]
#read
for i in range(dnum):
    (d[i], RL[i], U[i]) = readpart(fin, 3, need=0b100)
    d[i] = d[i][0]
    L[i] = getlx(d[i])
    I[i] =  - U[i] / RL[i]
    P[i] =  - U[i] * I[i]
#plot I-U
for i in range(dnum):
    # Usmooth, Ismooth = curve_smooth(U[i], I[i])
    setrange(U[i], I[i])
    plt.scatter(U[i], I[i], marker='o', color='black')
    plt.plot(U[i], I[i], label='光强%.1flx' % L[i])
plt.xlabel('电压U / V')
plt.ylabel('电流I / A')
plt.legend(loc=4)
plt.title('硅光电池输出特性')
plt.grid('on')
plt.savefig('output_UI.png')
plt.show()
#plot R_L - P
for i in range(dnum):
    setrange(RL[i][:-2], P[i][:-2])
    plt.scatter(RL[i][:-2], P[i][:-2], marker='o', color='black')
    plt.plot(RL[i][:-2], P[i][:-2], label='光强%.1flx' % L[i])
    #[:-2] to remove infinity RL
plt.xlabel('负载电阻 / $\Omega$')
plt.ylabel('功率 / P')
plt.legend()
plt.title('硅光电池输出特性')
plt.grid('on')
plt.savefig('output_PR.png')
plt.show()
FF = [None for i in range(dnum)]
for i in range(dnum):
    Isc = I[i][0]
    Uoc = U[i][-1]
    Pm = max(P[i])
    FF[i] = Pm / (-Isc * Uoc)
print('--- L / FF ---')
print(L)
print(FF)
#job 3
(d, Uoc, Usc) = readpart(fin, 3, need=0b100)
L =[]
for i in d:
    L.append(getlx(i))
#a resistance of 50 $\Omega$
Isc = Usc / 50
print('Isc / L slope: %f' % linear_regression(np.array(L), np.array(Isc), simple=1)[0])
setrange(L, Isc)
plt.scatter(L, Isc, marker='o', color='black')
plt.plot(L, Isc, label='短路电流($R=50\Omega$时)')
plt.xlabel('L / lx')
plt.ylabel('$I_{sc}$ / A')
plt.legend(loc=4)
plt.title('短路电流')
plt.grid('on')
plt.savefig('Isc.png')
plt.show()

setrange(L, Uoc)
#only part of Uoc and L is linear.
print('Uoc / L slope: %f' % linear_regression(np.array(L[0:4]), np.array(Uoc[0:4]), simple=1)[0])
plt.scatter(L, Uoc, marker='o', color='black')
plt.plot(L, Uoc, label='开路电压')
plt.xlabel('L / lx')
plt.ylabel('$U_{oc}$ / A')
plt.legend(loc=4)
plt.title('开路电压')
plt.grid('on')
plt.savefig('Uoc.png')
plt.show()
#job 4
dnum = 4
#read
d = readpart(fin, 1, need=0b100)[0]
L = []
for i in d:
    L.append(getlx(i))
for i in range(dnum):
    R = readpart(fin, 1, need=0b100)[0][0]
    U = readpart(fin, 1, need=0b100)[0]
    # print(L, U)
    # setrange(L, U)
    plt.scatter(L, U, marker='o', color='black')
    plt.plot(L, U, label='负载$R=%d\Omega$' % R)
plt.xlabel('L / lx')
plt.ylabel('U / V')
plt.legend(loc=4)
plt.title('不同负载U与L关系')
plt.grid('on')
plt.savefig('UL.png')
plt.show()

fin.close()

gendocx('gen.docx', './dark.png', './output_UI.png', './output_PR.png', './Isc.png', './Uoc.png', './UL.png')



#linear regression and plot
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

#generate docx #1
# gendocx('gen.docx', 'pic.png', result['string'])

#generate docx #2
# docu = Document()
# docuaddtitle(docu)
# docuappend(docu, './picfull.png', './figure_1.png', './pic.png', result['string'], './picx.png')
# docu.save('gen.docx')


