"""
Try for p 127

c = p**2
"""

import sys
sys.path.append('..')
import Euler
s = 0

lim = int(sys.argv[1])+1
facts = []
for n in range(1,lim):
    #print(n,Euler.factorization(n))
    facts.append(Euler.factorization(n))

for fact in facts:
    ab = 1
    for i in fact:
        #print(i)
        ab *= i**(fact[i]-1)
    #s += ab
    
    #a+b < ab
    if ab < 6:
        continue
    
    #s += 1
    for a in range(1,ab//2+1):
        cnt = True
        for f in fact:
            if f in facts[a-1]:
                cnt = False
                break
        if cnt: # a not multiple of c
            s += 1
            c = 1
            for i in fact:
                c *= i**fact[i]
            b = c - a
            print(a,b,c)
            s += 1



print(s)
