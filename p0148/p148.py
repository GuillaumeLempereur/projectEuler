"""
P148 Explorig Pascal's triangle

"""
import scipy
import math

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

    if height == -1 or height == 7**base-1:
        if base <= 1:
            return 0
        return 21*tri_fill(base-1)+28*tri_blank(base-1)
    if height >= 7**base:
        print("error")
        exit(-1)

    b_m1 = (7**(base-1)) # base_-1
    n_row_comp = (height+1)//b_m1 # number of tri -1 complete -> 1 == 1 tri_blank
    h_inc = height%b_m1 # height 'incomplete'


    fill_comp = n_row_comp*(n_row_comp-1)//2*tri_fill(base-1)
    blank_comp = n_row_comp*(n_row_comp+1)//2*tri_blank(base-1)

    fill_inc,blank_inc = 0,0
    if h_inc != b_m1-1:
        fill_inc = (n_row_comp)*tri_fill(base-1,h_inc+1)
        blank_inc = (n_row_comp+1)*tri_blank(base-1,h_inc)
    return fill_comp+blank_comp+fill_inc+blank_inc

def tri_fill(base,height=-1):
    if height == -1:
        w = 7**base
        return (w*(w-1))//2
    w = 7**base
    return (w-height)*height+height*(height-1)//2

i = 10**9-1 #10**9
b = math.floor(math.log(i,7))+1
print(b,i,tri_blank(b,i))
print("Ans:", ((i+2)*(i+1))//2-tri_blank(b,i))
