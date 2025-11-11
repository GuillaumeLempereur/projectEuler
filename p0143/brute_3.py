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

print("n,c,r")
lim = 300
cc = 0
c2 = 0
for t in range(1,2*lim):
    for r in range(1,min(t,lim)):
        if (t+r)%2 == 1:
            continue

        a = (t+r)//2
        b = (t-r)//2


        for c in range(a,t):
            cc += 1
            s = (t*t-c*c)*(c*c-r*r)
            rt = round(math.sqrt(s//3))

            if s%3 != 0 or rt*rt != s//3:
                continue

            nsq = (t*t+r*r+2*c*c+6*rt)
            if nsq%4!=0:
                continue
            n = round(math.sqrt(nsq//4))

            if n*n != nsq//4:
                continue
            xsq = (n*n-r*r)*(t*t-n*n)
            if xsq%3 != 0:
                continue
            if xsq > 0:
                x = round(math.sqrt(xsq//3))
                csq = ((2*n*n+t*t+r*r)-6*x)//4

                print(t,c,r,n)
            else:
                print(t,c,r,n)
                vv=0

            #print(16*c*c*c*c-8*(2*n*n+t*t+r*r)*c*c+(4*n*n-t*t-r*r)**2+12*r*r*t*t)
            #print(64*(2*n*n+t*t+r*r)**2-4*16*((4*n*n-t*t-r*r)**2+12*r*r*t*t),256*3*xsq)
            #print((2*n*n+t*t+r*r)%4)
            """
            nsq = (t*t+r*r+2*c*c+rt*6)//4
            if nsq%4 != 0:
                continue

            if nsq > lim*lim:
                break
            n = round(math.sqrt(nsq))
            if n*n == nsq:
                delta = 8*(2*n*n+t*t+r*r)-32*c*c # may be or not the other sol
                print(t,r,c,a,b,n,delta)
                #print(16*c**4-8*(2*n*n+t*t+r*r)*c*c+(4*n*n-t*t-r*r)**2+12*r*r*t*t)
                #print((8*(2*n*n+t*t+r*r))**2-4*16*((4*n*n-t*t-r*r)**2+12*r*r*t*t))
                print((2*n*n+t*t+r*r-4*c*c)/16/3, (2*n*n+t*t+r*r-4*c*c)/6, n*n-r*r, t*t-n*n)

                if t*t+r*r+2*c*c+6*rt != 4*nsq:
                    print("Wutt!")
            """

#print(cc)
#print(c2)
