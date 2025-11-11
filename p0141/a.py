
import math
import Euler

lim = 1000000

c = 0
cc = 0
"""
# GCD(r,d) = 1
for d1 in range(1,lim):
    d = d1*d1
    for r1 in range(1,lim//d1):
        r = r1*r1

        cc += 1

        asq = r+r1*d1**3
        a = round(math.sqrt(asq))
        if asq == a*a:
            #print(r,d,a)
            c += 1
"""


for c in range(1,lim):
    fs = Euler.factorization(c)

    c_p = 1
    for f in fs:
        if (fs[f])%2 == 1:
            c_p *= f

    if c_p == 1: # c square
        cc += 1

    else:

        for d1 in range(1,lim):
            d = d1*d1
            for r1 in range(1,lim//d1):
                r = r1*r1

                cc += 1

                asq = r+r1*d1**3
                a = round(math.sqrt(asq))
                if asq == a*a:
                    #print(r,d,a)
                    c += 1

print(c,cc)
