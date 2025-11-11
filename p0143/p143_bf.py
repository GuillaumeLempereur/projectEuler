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

lim = 100

sq = [i*i for i in range(1,1000)]

"""
for a in range(1,lim):
    for b in range(1,lim):
        for c in range(1,lim):
            if S = (a + b - c) * (a + c - b) * (b + c - a) * (a + b + c)



for a in range(1,lim):
    for b in range(1,lim):
        for c in range(1,lim):
            S = (a + b - c) * (a + c - b) * (b + c - a) * (a + b + c)

            print(a,b,c,S)

            #if S%3 == 0 and S//3 in sq and (a**2+b**2+c**2+round(math.sqrt(3*S)))//2 in sq:
            #    print(a,b,c,round(math.sqrt((a**2+b**2+c**2+round(math.sqrt(3*S)))//2)),(a**2+b**2+c**2+round(math.sqrt(3*S)))//2)
"""

for c in range(1,lim):
    for b in range(1,c+1):
        for a in range(c-b+1,b+1):

            S = (a + b - c) * (a + c - b) * (b + c - a) * (a + b + c)

            if 3*S in sq:
                print(a,b,c,S,round(math.sqrt(4*a**2*c**2)),a**2+c**2-b**2)

"""


c = 0

lim = 1000

for a in range(1,lim-2):
    for b in range(a,lim-a-1):
        for c in range(b,a+b):
            S = (a + b - c) * (a + c - b) * (b + c - a) * (a + b + c)
            #print(a,b,c,S)
            if a**2+b**2+c**2+math.sqrt(3*S) >= 2*lim**2:
                break
            c += 1

print(c)
"""