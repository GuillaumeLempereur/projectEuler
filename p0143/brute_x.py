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
import Euler
#import numpy as np


a = 399
b = 455
c = 511
# p + q + r = 784

lim = 1000
nl = [False]*120000
primes = Euler.primesbelow(lim)

print("t,r,c,a,b")
cc = 0
c2 = 0
for t in range(1,lim): # n=t
    if nl[t]:
        continue

    exit = False
    if Euler.isprime(t):
        for p in primes:
            if p >= t:
                break
            b = 1
            if t%2==0:
                b = 2
            for r in range(b,p,2):
                s = (t*t-p*p)*(p*p-r*r)
                rt = round(math.sqrt(s//3))

                if s%3 != 0 or rt*rt != s//3:
                    continue

                print(t,r,c,a,b,"Founded !")

                n = t
                i = 1
                while n < lim:
                    nl[n] = True
                    i += 1
                    n = i*i*t

                exit = True
                break
            if exit:
                break
        if exit:
            continue

    if Euler.isprime(t):
        print("Failed :'(")

    for r in range(1,lim):
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

            nsq = (t*t+r*r+2*c*c+rt*6)//4

            if nsq > lim*lim:
                break

            print(t,r,c,a,b)
            n = t
            i = 1
            while n < lim:
                nl[n] = True
                i += 1
                n = i*i*t
            exit = True
            break

        if exit:
            break


#print(cc)
#print(c2)
