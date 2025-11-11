# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 08:41:17 2017

@author: lempereu

P148 Exploring Pascal's triangle: Brute force objectif 2401
"""


import scipy
import math

# smart
l = [1,1]
nl = []
c = 0
for i in range(1,101):
    nl = []
    nl.append(1)
    #print(1,end=' ')
    for i in range(len(l)-1):
        n = l[i]+l[i+1]
        nl.append(n)
        if n%7 == 0:
            c += 1
        #print(l[i]+l[i+1],end=' ')
    nl.append(1)
    #print(1)
    print(l)
    l = nl
print(c)