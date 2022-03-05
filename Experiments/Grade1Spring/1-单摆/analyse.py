#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
from scipy import stats
import math
import sys
sys.path.append('..')

from template import linear_regression,font,readdata,varinfo

data, data_orig, name = readdata('./data.txt')

### main processing ###
for i in range(len(data)):
    varinfo(data[i], name[i])
    varinfo(data_orig[i], name[i] + ' orig')
varinfo(data[1] + .02219, 'real l')
print(data[1] + .02219)
