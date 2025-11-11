# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 08:56:11 2017

@author: lempereu

P131
"""

import Euler
# n^3 + n^2*p = a^3

c =  [x**3 for x in range(1,10000)]

def isCube(x):
    if x in c:
        return True
    return False

print(len(primes))
"""
BF
for p in primes:
    for n in range(1,10000):
        x = n**3+n*n*p
        if isCube(x):
            print(n,p,x)
"""

"""
Smarter
for p in primes:
    for n in range(1,1000):
        v = n**3
        x = v**3+v*v*p
        if isCube(x):
            print(v,p,x)
"""
"""
1 7 8
8 19 1728
27 37 46656
64 61 512000
216 127 16003008
729 271 531441000
1000 331 1331000000
1331 397 3061257408
2197 547 13244763896
2744 631 25412184000
4913 919 140770302408

s = [
(1, 7, 8),
(8, 19, 1728),
(27, 37, 46656),
(64, 61, 512000),
(216, 127, 16003008),
(729, 271, 531441000),
(1000, 331, 1331000000),
(1331, 397, 3061257408),
(2197, 547, 13244763896),
(2744, 631, 25412184000),
(4913, 919, 140770302408)
]
"""

p_l = set()
for a in range(1,2000):
    v = a**3
    b,w = 1,1
    for b in reversed(range(1,a)):
        w = b**3
        p = v-w
        if p >= 1000000: #1e6
            break
        #print(v,w)
        if Euler.isprime(p):
            #print(w,p,v)
            p_l.add(p)
            
print(len(p_l))
