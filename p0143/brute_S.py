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

700 => 27.48 6769

1200 => 10.15 1184
"""

import math
import Euler
#import numpy as np
import time

a = 399
b = 455
c = 511
# p + q + r = 784

print("t, c, r, rt")
lim = 100
ll= set()
cc = 0
c2 = 0

nl = [False]*120000

# case t = n

miny = 100
start_time = time.time()


for t in range(1,lim):
    if nl[t]:
        cc += 1
        continue
    exit = False
    for r in range(1,t):


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

        for c in range(r+1,t):

            s= (t-c)*(t+c)*(c-r)*(r+c)
            rt = math.floor(math.sqrt(s/3))
            nsq = (t*t+r*r+2*c*c+rt*6)//4
            if nsq > lim*lim:
                break


            if s%3==0 and rt*rt == s//3:
                cc += 1
                #"""
                #exit = True

                i= 1
                n = t
                while n<lim:
                    nl[n] = True

                    i += 1
                    n = t * i * i

                miny = min(miny, c/r)
                #ll.add(rt//3)
                print(t, c, r, rt//3, Euler.factorization(t*t-c*c), Euler.factorization(c*c-r*r))
                #break
                #"""

        if exit:
            break


#for l in sorted(ll):
#    print(l)

elapsed_time = time.time() - start_time
print(elapsed_time)
print(cc)
print(miny)
#print(sorted(list(ll)))
#print(c2)