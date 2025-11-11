#Problem 143
"""
Investigating the Torricelli point of a triangle

a, b, c, p, q, r are integers

find sum of p+q+r when p+q+r <= 120000

AN = BM = CO = p + q + r
=> AN, BM, CO are integers


Seems that Beta is angle in pythagorean triangle cos(B) = p/q

Idea: compute ||CO|| and others should be integer ! 1st way to discredit some a,b,c values

limits: a,b or c can not be greater or equal to the sum of the 2 others
modulo 3 for a,b and c : allow 3 %3==0, 2 %3==1 and %3==0, 2 %3==2 and %3==0, 2 %3==1 and %3==2, 2 %3==2 and %3==1 ???

lim: 200 > 2.71s
ex: a = 399, b = 455, c = 511
"""

import math
#import numpy as np


a = 399
b = 455
c = 511
# p + q + r = 784

print("t,r,c,a,b")
lim = 500
cc = 0
c2 = 0
for t in range(1,2*lim):
    for r in range(1,min(t,lim)):
        if (t+r)%2 == 1:
            continue

        a = (t+r)//2
        b = (t-r)//2

        c = a
        s= (t-c)*(t+c)*(c-r)*(r+c)
        rt = math.floor(math.sqrt(s/3))
        nsq = (t*t+r*r+2*c*c+rt*6)//4
        if nsq > lim*lim:
            break

        for c in range(a,t):
            cc += 1
            s= (t-c)*(t+c)*(c-r)*(r+c)
            rt = math.floor(math.sqrt(s/3))
            nsq = (t*t+r*r+2*c*c+rt*6)//4
            if nsq > lim*lim:
                break

            if s%3==0 and rt*rt == s//3:
                #print(t,r,c,a,b)
                c2 += 1

print(cc)
print(c2)
