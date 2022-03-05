#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from scipy import stats
from scipy.interpolate import spline
import math
import sys
import re
def font():
    #avoid font problem
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False 

def linear_regression(x, y, quiet=1, simple=0):
    slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
    r_squared = r_value ** 2
    s_slope = slope * math.sqrt((r_value ** -2 - 1) / (len(x) - 2))
    s_intercept = s_slope * math.sqrt(np.mean(x ** 2))
    if quiet == 0:
        print('linear regression:' )
        print('slope:', slope)
        print('intercept:', intercept)
        print('r-value:', r_value)
        print('p-value:', p_value)
        print('std-err:', std_err)
        print('r-squared:', r_squared)
        print('斜率标准差:', s_slope)
        print('截距标准差:', s_intercept)
    string = '''
linear regression: \n \
slope: %g \n \
intercept: %g \n \
r-value: %g \n \
p-value: %g \n \
std-err: %g \n \
r-squared: %g \n \
斜率标准差: %g \n \
截距标准差: %g
''' % (slope, intercept, r_value, p_value, std_err, r_squared, s_slope, s_intercept)
    if simple == 1:
        return slope, intercept
    if simple == 0:
        return {'string':string, 'slope':slope, 'intercept':intercept, \
            'r_value':r_value, 'p_value':p_value, 'std_err':std_err,\
            'r_squared':r_squared, 's_slope':s_slope, 's_intercept':s_intercept}

def curve_smooth(x, y, insnum=300):
    xnew = np.linspace(min(x), max(x), insnum)
    ysmooth = spline(x, y, xnew)
    return (xnew, ysmooth)
def readdata(filename, need=0b111):
    data = []; data_orig = []; name = []
    #order of magnitude
    oom = 0
    fin = open(filename, 'r')
    for i in fin.readlines():
        if len(i) == 0:
            continue
        if i[0] == '#':
            #line start with # is comment
            pass
        elif i[0] == 'e':
            oom = int(i.split()[1])
        elif i[0] == 'n':
            name.append(i.split()[1])
        else:
            data.append(np.array([float(x) * pow(10, oom) for x in i.split()]))
            data_orig.append(np.array([float(x) for x in i.split()]))
            oom = 0
            if len(data) > len(name):
                name.append('i_have_no_name')
    if need == 0b111:
        return (data, data_orig, name)
    if need == 0b110:
        return (data, data_orig)
    if need == 0b101:
        return (data, name)
    if need == 0b011:
        return (data_orig, name)
    if need == 0b010:
        return data_orig
    if need == 0b001:
        return name
    if need == 0b100:
        return data
    # return (data, data_orig, name)

def readpart(fid, number, need=0b111):
    #read number line of real data from file descriptor fid
    data = []; data_orig = []; name = []
    cnt = 0
    oom = 0
    while cnt < number:
        i = fid.readline()
        if re.match('^ *\t*\n*$', i):
            #TODO: improve RE
            #if an empty line with no number but blank
            continue
        # print('-->', i)
        if i[0] == '#':
            pass
        elif i[0] == 'e':
            oom = int(i.split()[1])
        elif i[0] == 'n':
            name.append(i.split()[1])
        else:
            data.append(np.array([float(x) * pow(10, oom) for x in i.split()]))
            data_orig.append(np.array([float(x) for x in i.split()]))
            if len(data) > len(name):
                name.append('i_have_no_name')
            oom = 0
            cnt += 1
    if need == 0b111:
        return (data, data_orig, name)
    if need == 0b110:
        return (data, data_orig)
    if need == 0b101:
        return (data, name)
    if need == 0b011:
        return (data_orig, name)
    if need == 0b010:
        return data_orig
    if need == 0b001:
        return name
    if need == 0b100:
        return data
def readoneline(fid):
    return np.array(readpart(fid, 1, need=0b100)[0])
def readoneavg(fid):
    return np.mean(readpart(fid, 1, need=0b100)[0])



def varinfo(data, name='noname', quiet=0):
    data = np.array(data)
    l = len(data)
    avg = np.mean(data)
    std1 = math.sqrt(sum((data - avg) ** 2) / (l - 1))
    if quiet == 0:
        print('varable name', name, ':')
        print('\tnumber:', l)
        print('\taverage:', avg)
        print('\tstd:', std1)
    return avg, std1

def sqrtsum(*vars):
    return math.sqrt(sum([x ** 2 for x in vars]))

table_t_P_n = {
        68:{3:1.32, 4:1.20, 5:1.14, 6:1.11, 7:1.09, 8:1.08, 9:1.07, 10:1.06, 15:1.04, 20:1.03},
        90:{3:2.92, 4:2.35, 5:2.13, 6:2.02, 7:1.94, 8:1.86, 9:1.83, 10:1.76, 15:1.73, 20:1.71},
        95:{3:4.30, 4:3.18, 5:2.78, 6:2.57, 7:2.46, 8:2.37, 9:2.31, 10:2.26, 15:2.15, 20:2.09},
        99:{3:9.93, 4:5.84, 5:4.60, 6:4.03, 7:3.71, 8:3.50, 9:3.36, 10:3.25, 15:2.98, 20:2.86}
        }
table_kp_P = {
        68:1, 90:1.65, 95:1.96
        }

def calc_delta_a(arr, P=68, quiet=1):
    #delta_a = t_p * u_a
    l = len(arr)
    avg, std = varinfo(arr, quiet=1)
    # print('in calc_delta_a:', l, avg, std)
    if quiet == 0:
        print('calc_delta_a:')
        print('std:', std)
        print('P:', P)
        print('tp:', table_t_P_n[P][l])
    return table_t_P_n[P][l] * std / math.sqrt(l)

def calc_delta_b(arr, delta, delta_human=0, P=68, C=3):
    #delta_b = kp * sqrt(delta_human**2 + delta**2) / C
    return table_kp_P[P] * sqrtsum(delta, delta_human) / C
def calc_delta_b_graph(arrx, arry, deltax, deltay, P=95, C=3):
    result = linear_regression(arrx, arry, quiet=1)
    deltay = result['slope'] * math.sqrt(2 * deltax ** 2 / (arrx[-1] - arrx[0]) ** 2 + 2 * deltay ** 2 / (arry[-1] - arrx[0]) ** 2)
    deltax = deltay / result['slope'] * math.sqrt((arrx[-1] ** 2 + arrx[0] ** 2) / 2)
    return table_kp_P[P] * deltay / C

#set x and y limit to make graph better
def setrange(datax, datay, xy=0b01):
    if xy & 0b01:
        mini = min(datay)
        # print('in setrange:')
        # print(mini)
        maxi = max(datay)
        # print(maxi)
        plt.ylim(mini - .2 * (maxi - mini), maxi + .2 * (maxi - mini))
    if xy & 0b10:
        mini = min(datax)
        maxi = max(datax)
        plt.xlim(mini - .2 * (maxi - mini), maxi + .2 * (maxi - mini))

def my_sort_by(maj, *sub):
    for i in range(len(maj) - 1):
        for j in range(i, len(maj)):
            if maj[i] > maj[j]:
               maj[i], maj[j] = (maj[j], maj[i]) 
               for k in sub:
                   k[i], k[j] = (k[j], k[i]) 
    return (maj, sub)
if __name__ == '__main__':
    #plot
    plt.scatter(x, y, marker='*', color='black', label='原始数据')
    # plt.plot(x, y, '--', color='green', label='光滑曲线')
    #plt.plot(x, intercept + slope * x, 'r', label='拟合直线')



    plt.xlabel('')
    plt.ylabel('')
    plt.legend(loc=4)
    plt.title('')

    plt.savefig('pic.png')
    plt.show()

    from gendocx import gendocx
    gendocx('gen.docx', 'pic.png', string)


