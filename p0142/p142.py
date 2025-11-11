# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 13:57:51 2017

@author: lempereu
p142
"""

# Find the smallest x + y + z with integers x > y > z > 0 such that x + y, x − y, x + z, x − z, y + z, y − z are all perfect squares.
# x + y, x − y, x + z, x − z, y + z, y − z all perfect square 

import math

"""

# Pythagorian triplet
for m in range(2,5):
    for n in range(1,m):
        for k in range(1,m):
            print(m,n,":",m*m-n*n,2*m*n,m*m+n*n)
"""

#Solution the smallest

x,y,z = 434657, 420968, 150568
a = [math.sqrt(x-y),
math.sqrt(x+y),
math.sqrt(x-z),
math.sqrt(x+z),
math.sqrt(y+z),
math.sqrt(y-z)]
print(a)

#434657, 420968, 150568

sq = set()
for i in range(1,10000):
    sq.add(i*i)
# Pythagorian quadruplet

for n in range(1,35):
    for m in range(0,n+1):
        for q in range(1,n+1):
            if m**2+n**2-q**2 <= 0:
                break
            start = 0
            if m == 0:
                start = 1
            for p in range(start,n+1):
                if m**2+n**2-q**2-p**2 <= 0 or n*q-m*p <= 0:
                    break
                #for k in range(1,m):
                #print(n,m,q,p,":",m**2+n**2-p**2-q**2,2*(m*q+n*p),2*(n*q-m*p),m**2+n**2+p**2+q**2)
                a = m**2+n**2-p**2-q**2
                b = 2*(m*q+n*p)
                c = 2*(n*q-m*p)
                d = m**2+n**2+p**2+q**2
                for k in range(1,20):
                    a,b,c,d = k*a,k*b,k*c,k*d
                    
                    if a*a+b*b in sq and c*c+b*b in sq:
                        #if b%2 == d%2:
                        print(a,c,b,d,math.sqrt(a*a+b*b),math.sqrt(b*b+c*c))
                    
                    if a*a+b*b in sq and c*c+a*a in sq:
                        print(a,c,b,d,math.sqrt(a*a+b*b),math.sqrt(a*a+c*c))
                    
                    if a*a+c*c in sq and c*c+b*b in sq:
                        print(a,c,b,d,math.sqrt(a*a+b*b),math.sqrt(b*b+c*c))
        
"""
couple_a = []
couple_b = []
couple = []
lim = 350

for x in range(1,lim+1,2):
    for y in range(1,x,2):
        #print(x,y)
        a = (x**2+y**2)//2
        b = (x**2-y**2)//2
        couple_a.append(a)
        couple_b.append(b)
        couple.append((a,b))
        #print(x,y,a,b,x**2,y**2)

        
for x in range(2,lim+1,2):
    for y in range(2,x,2):
        #print(x,y)
        a = (x**2+y**2)//2
        b = (x**2-y**2)//2
        couple_a.append(a)
        couple_b.append(b)        
        couple.append((a,b))
        #print(x,y,a,b,x**2,y**2)
        

for i in range(len(couple_a)):
    if couple_a[i] in couple_b:
        idx = couple_b.index(couple_a[i])
        if (couple_a[idx],couple_b[i]) in couple:
            print(couple_a[i],couple_b[i])
"""