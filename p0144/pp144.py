# -*- coding: utf-8 -*-
"""
Created on Wed May 17 13:23:05 2017

@author: lempereu

p144
"""

import math


r = -0.475309
r = 14.0714
print(r,-1547*math.sqrt(1+r**2)-120*math.sqrt(390.05)*(7/12*r+1))




a_x, a_y = 0, 10.1
o_x, o_y = 1.4, -9.6

xa, ya = o_x-a_x, o_y-a_y


A = (xa**2+ya**2)/(xa-4*o_x/o_y*ya)**2
r = (8*o_x/o_y*A + 2*math.sqrt(16*A*o_x**2/o_y**2+A-1))/(32*A*o_x**2/o_y**2)
#r = (8*o_x/o_y*A - 2*math.sqrt(16*A*o_x**2/o_y**2+A-1))/(32*A*o_x**2/o_y**2)

A = 2
o_x = 1
o_y = 4

r = (8*o_x/o_y*A + 2*math.sqrt(16*A*o_x**2/o_y**2+A-1))/(32*A*o_x**2/o_y**2-2)


""" Debug
print(r)
a = 16*A*o_x**2/o_y**2-1
b = -8*o_x/o_y*A
c = A-1
print(a,b,c)
"""

# y = r*x+o_y-r*o_x
# search for an intersection

b_m, b_M = 0, 0
y_r_0 = o_y-r*o_x

if r < 0 and o_y > 0:
    if y_r_0 > 10:
        b_m, b_M = 0, 5
    else:
        b_m, b_M = -5, 0
elif r < 0 and o_y < 0:
    if y_r_0 < -10:
        b_m, b_M = 0, 5
    else:
        b_m, b_M = -5, 0
elif r > 0 and o_y < 0:
    if y_r_0 < -10:
        b_m, b_M = 0, 5
    else:
        b_m, b_M = -5, 0
elif r > 0 and o_y > 0:
    if y_r_0 < 10:
        b_m, b_M = -5, 0
    else:
        b_m, b_M = 0, 5
else:
    print("What the Fock !")
    exit(-5)

print(b_m, b_M)

"""
n = math.sqrt(xa**2+ya**2)/(xa-4*o_x/o_y*ya)
m = math.sqrt(1+r**2)/(4*o_x/o_y*r-1)

print(m,n)
"""