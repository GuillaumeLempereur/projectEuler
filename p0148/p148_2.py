# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 08:41:17 2017

@author: lempereu

P148 Explorig Pascal's triangle

until power of 7 
"""


import scipy
import math

# smart
p = []


"""
i=0:
    0->48
i=1:
    0->342
i=2:
    0->2400
"""


def tri_blank(base,height=-1):
    # height = [0; 7**base[
    print("#",base,height)
    if height == -1 or height == 7**base-1:
        if base <= 1:
            return 0
        return 21*tri_fill(base-1)+28*tri_blank(base-2)
    if height >= 7**base:
        print("error")
        exit(-1)
    
    b_m1 = (7**(base-1)) # base_-1
    n_row_comp = (height+2)//b_m1 -1 # number of tri fill complete
    h_inc = height - n_c*b_m1+1 # number of ligne 'incomplete'
    
    fill_comp = n_row_comp*(n_row_comp+1)//2*tri_fill(base-1)
    blank_comp = n_c*(n_c+1)*tri_blank(base-1)
    
    fill_inc = (n_c+1)*tri_fill(base-1,h_inc)
    blank_inc = (n_c+2)*tri_blank(base-1,h_inc)
    
    print("-"*20)
    print(base,height)
    print(fill_comp)
    print(blank_comp)
    print(fill_inc)
    print(blank_inc)
    print("-"*20)
    return fill_comp+blank_comp+fill_inc+blank_inc

    
    
    """
    base: 0 => 1 => 0
    1 => 7 => 6*7/2=21
    """

def tri_fill(base,height=0):
    if height == 0:
        w = 7**base
        return (w*(w-1))//2
    w = 7**base
    return (w-height)*height+height*(height-1)//2


#tri_blank(11,10**9)

for i in range(5):
    print(i,tri_blank(i))

    
print(1,tri_blank(2,2))
print(1,tri_blank(2,48))


"""
# complete
tri_b_0 = 1
tri_prev = 0
for b in range(1,11):
    tri_b = 7**b
    tri = (tri_b*(tri_b-1))//2
    s = 28*tri_prev+21*tri
    print(b,tri_b,tri_prev,tri,s)
    tri_prev = s


#fill
p7 = []
for i in range(11):
    p7.append(7**i)
    print(i,7**i)
"""





"""    
print(p7)
n = 10**9
for s in reversed(p7):
    sub = n//s
    n -= sub*s
    print(sub)
""" 


"""
for e in range(8):
    #l = []
    c = 0
    n = 7**e-1
    for i in range((n+1)//2):
        if scipy.misc.comb(n,i,exact=True)%7 == 0:
            c += 1
    print(n,c)
    
#print(p)
"""
