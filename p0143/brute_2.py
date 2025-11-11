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



#(t*t-r*r)**2-12*x*x = k*k



print("t,r,c,rt,rt2")
lim = 200
ll= []
cc = 0
c2 = 0
for t in range(1,2*lim):
    for r in range(1,min(t,lim)):
        a = (t + r) // 2
        b = (t - r) // 2

        if (t+r)%2 == 1:
            continue
        for c in range(a,t):

            #if a==455 and b == 399:
            #    print(a,b,c,t)
            cc += 1
            s= (t-c)*(t+c)*(c-r)*(r+c)
            rt = math.floor(math.sqrt(s / 3))
            nsq = (t * t + r * r + 2 * c * c + rt * 6) // 4
            if nsq > lim * lim:
                break
            if nsq%4 != 0 or s%3 != 0 or rt*rt != s/3:
                continue

            n = math.floor(math.sqrt(nsq))
            if n*n == nsq:
                #and Euler.gcd(Euler.gcd(t,r),c) == 1:
                x = (2*n*n+t*t+r*r-4*c*c)//6
                delta = -nsq*nsq+(t*t+r*r)*nsq-r*r*t*t
                print(t,r,c,x,delta,math.sqrt((t*t-n*n)*(n*n-r*r)//3),math.sqrt((t*t-c*c)*(c*c-r*r)//3),n,t)

                """
                v = (t*t-r*r)**2
                i = 1
                v2 = v
                while v2 > 0:
                    rtt = math.floor(math.sqrt(v2))
                    found = False
                    if rtt*rtt == v2:
                        found = True
                        break
                    if not found:
                        print(t,r,c,(t*t-r*r)**2)
                    i += 1
                    v2 = v - i * i * 12
                    """


        """    
        sq = (t * t - r * r) ** 2 - 12*4 # x = 1
        if sq > 0:
            rt = math.floor(math.sqrt(sq))
            if sq == rt*rt:
                print(t,r,rt)

        """





        """
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


            if s%3==0 and rt*rt == s//3 and Euler.gcd(Euler.gcd(t,r),c) == 1:
                #print(c,t,r,c,a,b)
                #print(16*c**4-8*c*c*(r*r+t*t+2*nsq)+(4*nsq-r*r-t*t)**2+12*r*r*t*t)
                #print(math.sqrt((r*r+t*t+2*nsq)**2-(4*nsq-r*r-t*t)**2-12*r*r*t*t), math.sqrt(3*(nsq*r*r+nsq*t*t-nsq**2-r*r*t*t)))
                #print(math.sqrt(3*(nsq*r*r+nsq*t*t-nsq**2-r*r*t*t)))

                #print(math.sqrt(nsq),r,t,math.sqrt((-nsq**2+nsq*(r*r+t*t)-r*r*t*t)*3), c, (r*r+3*t*t)//4)
                print(r*r,nsq)

                #print(math.sqrt(t*t-r*r))
                #ll.append((c,r,t))
            c2 += 1
            """


#for l in sorted(ll):
#    print(l)
print(cc)
print(c2)