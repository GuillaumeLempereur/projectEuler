# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 13:22:00 2017

@author: lempereu

P138
"""

"""
sq = []
for i in range(1,100000):
    sq.append(i*i)

#case h := b-1
for i in range(1,100000):
    if (i*i+1)%5==0 and (i*i+1)//5 in sq:
        print(i,(i*i+1)//5)
"""
"""
Pell's equation:

x^2-n*y^2 = -1

"""

def isqrt(n):
    x = n
    y = (x + 1) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x

L_lst = []
    
D = 5
x_0, y_0 = 2, 1
x_n, y_n = 38, 17
print(16,15,17)
L_lst = [17]
for i in range(15):
    x_n1 = x_n*x_0**2+x_n*y_0**2*D+2*x_0*y_0*y_n*D
    
    y_n1 = 2*x_0*x_n*y_0+y_n*x_0**2+y_0**2*y_n*D
    
    #print(x_n1,y_n1)
    x_n, y_n = x_n1, y_n1
    
    #case h := b+1
    dd = -4+2*x_n
    if dd %5 == 0:
        b = dd//5
        h = b+1
        print(b,h,isqrt(b*b//4+h*h))
        L_lst.append(isqrt(b*b//4+h*h))
    
    #case h := b+1
    dd = 4+2*x_n
    if dd %5 == 0:
        b = dd//5
        h = b-1
        print(b,h,isqrt(b*b//4+h*h))
        L_lst.append(isqrt(b*b//4+h*h))
#case h := b+1

ll = sorted(L_lst)
print(sum(ll[:12]))

"""
# solution:
    
#Project Euler Problem 138

def f(n):
    if n < 2:
        return n
    return f(n-2) + f(n-1)

#from Euler import fibonacci as f
nt = 12

for n in range(1, nt+1):
    print(f(6*n+3)/2) 
"""