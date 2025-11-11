# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 13:02:24 2022

@author: lempereu
"""

lim = 1000000

for i in range(1,lim):
    n = int(''.join(reversed(list(str(i)))))
    
    s = int(i**(1/2))
    # int
    sr = int(n**(1/2))
    
    if s*s == i and sr*sr == n:
        
        
        l = str(i)
        lr = reversed(list(str(i)))
        
        if len(l) == len(lr):
            s= True
            for k in range(len(l)//2+1):
                if l[k] != lr[len(l)-k-1]:
                    s = False
                    break
            if s:
                print(i, n)
        else:
            print(i, n)