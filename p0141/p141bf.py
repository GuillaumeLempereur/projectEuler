# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 08:52:49 2017

@author: lempereu
P141
"""

# n = d*q+r
# Brute Force
# may be optimized: d start at sqrt(n)
import math

print("n,d,q,r")
c = 0
lim = 3000
for a in range(1,lim):
    n = a*a
    dm = math.floor(math.sqrt(a))+1
    #print(n,dm)
    for j in range(dm,a): # d > q and d > r
        d = j**2
        r = n%d

        if r == 0:
            continue
        q = n//d

        if abs(d/q - q/r)  < 1e-8 or abs(d/r - r/q) < 1e-8:
            c += 1
            print(n,d,q,r)
            print("\t",d*r,((n-r)/d)**2)
            print("\t",d**3*(d**3+4*a*a),d**3)
            break
        if abs(d/r - r/q) < 1e-8:
            print("Miracle")
        """
        if q>d:
            if q/d == d/r:
                print(n,d,q,r)
                c += 1
                break
       """

    #print("-"*10)
print(c)
