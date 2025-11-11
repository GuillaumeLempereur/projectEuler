# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 09:04:38 2017

@author: lempereu
p144 Ellipse
"""
import math

a_x, a_y = 0.0,10.1

o_x, o_y = 1.4,-9.6


x_a, y_a = o_x-a_x, o_y-a_y

m = -4*o_x/o_y

d_x, dy = 1, m


print("d vector", (d_x,dy))
r_y = math.sqrt(x_a**2+y_a**2)/(x_a+y_a*m)/math.sqrt(1+m**2)
r_x = -m*r_y

# slope reflexion
r_m = (o_y-r_y)/(o_x-r_y)
r_p = ((o_y+r_y)-r_m*(o_x+r_x))/2

y_r_0 = r_y-r_x*r_m
x_y_0 = -r_p/r_m

tol = 10**-8
a, b = -5, 5
if r_x-o_x < 0:
    b = o_x
elif r_x-o_x > 0:
    a = o_x
else:
    print("vertical")
    exit(-42)


if r_y-o_y > 0:
    pos = 1
elif r_y-o_y < 0:
    pos = -1
else:
    print("Flat")
    exit(-58)

if r_y-o_y > 0 and o_y < 0 and abs(x_y_0) > 5:
    pos = -1

if r_y-o_y < 0 and o_y > 0 and abs(x_y_0) > 5:
    pos = 1


xt = (a + b)/2
if r_x-o_x < 0: # <-
    if (pos*math.sqrt(100-4*xt**2)-r_m*xt-r_p)*(pos*math.sqrt(100-4*a**2)-r_m*a-r_p) < 0:
        b = xt
    else:
        a = xt
elif r_x-o_x > 0: # ->
    if (pos*math.sqrt(100-4*xt**2)-r_m*xt-r_p)*(pos*math.sqrt(100-4*b**2)-r_m*b-r_p) < 0:
        a = xt
    else:
        b = xt

while (a + b)/2 > tol:
    xt = (a + b)/2
    if (pos*math.sqrt(100-4*xt**2)-r_m*xt-r_p)*(pos*math.sqrt(100-4*a**2)-r_m*a-r_p)<0:
        b = xt
    else:
        a = xt

print(xt, r_m*xt+r_p)
