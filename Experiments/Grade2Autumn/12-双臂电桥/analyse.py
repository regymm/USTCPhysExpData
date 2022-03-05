#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
sys.path.append('/home/username/PhysicsExp/Core')

from Core.mainfunc import *

fin = open('./data.txt', 'r')
zerovalue = .005e-3
cu_d = readoneline(fin)
cu_d = cu_d - zerovalue
al_d = readoneline(fin)
al_d = al_d - zerovalue
R11 = readoneline(fin)
R12 = readoneline(fin)
R1 = (R11 + R12) / 2
R21 = readoneline(fin)
R22 = readoneline(fin)
R2 = (R21 + R22) / 2
R31 = readoneline(fin)
R32 = readoneline(fin)
R3 = (R31 + R32) / 2
fin.close()

R_delta_a = calc_delta_a(R3, P=95)
R_delta_b = calc_delta_b(R3, np.average(R3)*.02e-2, P=95)
R_delta = sqrtsum(R_delta_a, R_delta_b)

d_delta_a = calc_delta_a(al_d, P=95)
d_delta_b = calc_delta_b(al_d, .004e-3, P=95)
d_delta = sqrtsum(d_delta_a, d_delta_b)

print(np.average(R3), R_delta_a, R_delta_b, R_delta)
print(np.average(al_d), d_delta_a, d_delta_b, d_delta)
cu_rou_40 = math.pi * np.average(cu_d)**2 / (4 * 40e-2) * np.average(R1) / 1e3 * .001
cu_rou_30 = math.pi * np.average(cu_d)**2 / (4 * 30e-2) * np.average(R2) / 1e3 * .001
al_rou = math.pi * np.average(al_d)**2 / (4 * 30e-2) * np.average(R3) / 1e3 * .001
u_al_rou = math.sqrt((2*d_delta / np.average(al_d))**2 + (1e-3 / .3)**2 + (R_delta / np.average(R3))**2
                     + (.2 / 1e3)**2 + (1e-7 / 1e-3)**2) * al_rou
print(cu_rou_40)
print(cu_rou_30)
print(al_rou, u_al_rou)

# 551.5 3.284179248051686 0.07206266666666668 3.2849697656539316
# 0.00546066666667 4.179269207781598e-06 2.613333333333333e-06 4.929077218123341e-06
# 9.41328180931e-08
# 9.41751630405e-08
# 4.30532040183e-08 3.04125274247e-10
