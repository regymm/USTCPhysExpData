#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
sys.path.append('..')

from template import *
from gendocx import *

font()

fin = open('./data.txt', 'r')
R = readpart(fin, 1, need=0b100)[0]
# print(R)
#total 5 main data group
datanum = 5
data = [[] for i in range(datanum)]
for i in range(datanum):
    #freq, volt, volt(mv)
    data[i] = readpart(fin, 3, need = 0b100)
# print(data)
percent, volt = readpart(fin, 2, need=0b100)
# print(readpart(fin, 2, need=0b100))
fin.close()

wavelen = np.array([data[i][0][0] for i in range(datanum)])
freq = 3e8 / wavelen
u_s = []
# print(freq)
#the first task, five plot and get u_s
for i in range(datanum):
    #electric current
    data[i].append(data[i][2] / R)
    U = data[i][1]
    I = data[i][3]
    X = my_sort_by(U, I)
    U = X[0]; I = X[1][0]
    # print(U, I)
    #使用二次线性拟合求出遏止电压
    rangemin = -3
    rangemax = -.1
    Upart, Ipart = [], []
    for j in range(len(U)):
        if U[j] >= rangemin and U[j] <= rangemax:
            Upart.append(U[j]), Ipart.append(I[j])
    # print(Upart, Ipart)
    k, b = linear_regression(np.array(Upart), np.array(Ipart), quiet=1, simple=1)
    # print(k ,b)
    maxid = 0
    maxdist = 0
    for j in range(len(Upart)):
        dist = ( - Ipart[j] + k * Upart[j] + b) / math.sqrt(1 + k ** 2)
        if dist > maxdist:
            maxdist = dist
            maxid = j
    k1, b1 = linear_regression(np.array(Upart[:maxid]), np.array(Ipart[:maxid]), simple=1, quiet=1)
    k2, b2 = linear_regression(np.array(Upart[maxid:]), np.array(Ipart[maxid:]), simple=1, quiet=1)
    #两直线交点横坐标为遏止电压
    xx = - (b2 - b1) / (k2 - k1)
    yy = k1 * xx + b1
    u_s.append(math.fabs(xx))

    setrange(U, I)
    plt.scatter(U, I, marker='o', label='原始数据')
    plt.scatter([xx], [yy], marker='*', color='red', lw=4, label='遏止电压拟合点')
    # plt.plot(U, b + k * U, 'r', label='拟合直线')
    # plt.plot(U, b1 + k1 * U, 'r', label='拟合直线')
    # plt.plot(U, b2 + k2 * U, 'r', label='拟合直线')
    plt.plot(U, I, label='光滑曲线')
    plt.xlabel('电压 / V')
    plt.ylabel('电流 / A')
    plt.title('电流-电压曲线 -- %g nm' % (1e9 * wavelen[i]))
    plt.legend()
    plt.grid()
    plt.savefig('pic' + str(i) + '.png')
    plt.show()
#plot and analyse u_s and freq
# plt.savefig('picfull.png')
# plt.show()
result = linear_regression(freq, u_s)
print(freq, u_s)
setrange(freq, u_s)
plt.scatter(freq, u_s, marker='o', color='black', label='原始数据')
plt.plot(freq, result['intercept'] + result['slope'] * freq, 'r', label='拟合直线')
plt.xlabel('频率 / Hz')
plt.ylabel('遏止电压 / V')
plt.legend(loc=4)
plt.title('遏止电压与频率')

# plt.savefig('pic.png')
plt.show()

#the second task
I = volt / R
slope, intercept = linear_regression(percent, I, quiet=1, simple=1)
p = plt.subplot(111)
#set lim and format to make plot better
# plt.ylim(-.2*max(I), 1.25 * max(I))
setrange(percent, I)
p.yaxis.set_major_formatter(ticker.FormatStrFormatter('%g'))
plt.scatter(percent, I, marker='o', color='black', label='原始数据')
plt.plot(percent, intercept + slope * percent, 'r', label='拟合直线')
plt.xlabel('透过率 / %')
plt.ylabel('饱和光电流 / A')
plt.legend(loc=4)
plt.title('饱和光电流强度与透过率关系图')

answer = result['slope'] * 1.602e-19
print('Planck constant:', answer)

# plt.savefig('picx.png')
plt.show()

# gendocx('gen.docx', 'pic.png', result['string'])
docu = Document()
docuaddtitle(docu)
for i in range(datanum):
    docuappend(docu, 'pic' + str(i) + '.png')
docuappend(docu, './picfull.png', './figure_1.png', './pic.png', result['string'], './picx.png')
docu.save('gen.docx')


