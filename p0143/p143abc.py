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

lim = 10
cc = 0
for a in range(1,lim):
    for b in range(a,lim):
        for c in range(b,a+b):
            cc += 1
            s= (a+b-c)*(a+c-b)*(b+c-a)*(a+b+c)
            if s %3 == 0:
                print(a,b,c,s)

print(cc)
