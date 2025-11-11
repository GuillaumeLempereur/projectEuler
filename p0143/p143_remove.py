"""
answer not 22781
"""

#import numpy as np
import math
import Euler

cc= 0
lim = 100
#lim should be 120000**2

ss = [0]*lim

for n in range(1,lim):
    if ss[n]:
        continue # composed solution
    rside = 2*n**2






for a in range(1,lim):
    for b in range(1, a):
        if a*a+b*b+1 > lim:
            break
        for c in range(a-b+1, a+b):

            S = (a + b - c) * (a + c - b) * (b + c - a) * (a + b + c)

            if S//3 < 3 or S%3 != 0:
                continue

            sq = round(math.sqrt(S // 3))

            if a * a + b * b + c*c + 3*sq > 2*lim:
                break

            if sq * sq != S // 3:
                continue
            #print(S//3)
            AN_sq = (a * a + b * b + c*c + 3*sq)//2
            if sq*sq == S//3:
                AN = round(math.sqrt(AN_sq))
                if AN*AN != AN_sq:
                    continue
                cc += 1
                #tt = tuple(sorted([a,b,c,AN]))
                ss.add(AN)
                #print(a,b,c,AN)

print(cc)
print(len(ss))
sumy = 0
for s in ss:
    #AN = tt[3]
    #print(s)
    sumy += s
print(sumy)
print(sorted(list(ss)))

primS = []
for s in ss:
    f = True
    for p in primS:
        if s%p == 0:
            f = False
            break
    if f:
        primS.append(s)

for p in primS:
    print(p,Euler.factorization(p))


"""
sq = [i*i for i in range(1,100000)]

s = 0
lim = 100
ss = 0
for c in range(1,lim):
    for b in range(1,c+1):
        for a in range(c-b+1,b+1):
            #print(a,b,c,(a ** 2 + c ** 2 - b ** 2) / 2 / a / c)
            ss += 1

            s += 1
            S = (a + b - c) * (a + c - b) * (b + c - a) * (a + b + c)
            if S%3==0 and S//3 in sq:
                print(a,b,c,c**2-a**2+b**2,4*a**2*c**2-(a**2+c**2-b**2)**2,b**2-(a-c)**2,(a+c)**2-b**2,a+b-c,a+c-b,b+c-a,a+b+c)



print(s,ss)
"""