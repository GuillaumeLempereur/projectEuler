# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 08:41:17 2017

@author: lempereu

P155 Capacitor combination
"""

"""
Brute force approach

Not 262143
Begin to bug when n >= 5
could be improved only combine n-1 and 1 capacitor
"""

"""
# Recursive function
def d(n):
    if n == 1:
        return set([1])
    #val[n] = val[n-1]
    b = list(d(n-1))
    a = d(n-1)
    
    for c in b:
        a.add(1+c)
        a.add(c/(1+c))
        
    return  a
print(d(5))
"""
"""
for n in range(1,11):    
    print(n,len(d(n)))
"""

"""
# Nearly
# The idea is to combine 2 and 3
# Non recursive function
n = 18
val = [set() for i in range(n+1)]
val[1] = set([1])
for i in range(2,n+1):
    #val[i] = val[i-1].copy()
    for k in range(i//2):
        for c1 in val[k+1]:
            #print("yo",i,k,c1)
            for c2 in val[i-k-1]:
                
                val[i].add(c1+c2)
                val[i].add(round(c1*c2/(c1+c2),13))

s = set()
for i in range(n+1):
    s = s | val[i]
    print(i,len(s))

"""
import fractions
# The idea is to combine 2 and 3
# Non recursive function
n = 18
val = [set() for i in range(n+1)]
val[1] = set([fractions.Fraction(1)])
for i in range(2,n+1):
    #val[i] = val[i-1].copy()
    for k in range(i//2):
        for c1 in val[k+1]:
            #print("yo",i,k,c1)
            for c2 in val[i-k-1]:
                
                val[i].add(c1+c2)
                val[i].add(c1*c2/(c1+c2))

s = set()
for i in range(n+1):
    s = s | val[i]
    print(i,len(s))
