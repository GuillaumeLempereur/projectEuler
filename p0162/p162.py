# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 08:41:06 2024

@author: lempereu
"""

#p162



"""
Pop = 16**lim - 15**lim

N0 = 15**lim
N1 = 15**lim

N10 = 14**lim

N1a0 = 13**lim
"""

#162

def fac(n):
    r = 1
    for i in range(n):
        r*= (i+1)
    return r

lim = 3


limm = 16**lim
cc = 0
ccc = 0
c21 = 0
for i in range(1, limm):
    n = hex(i)[2:]
    if "1" in n and "a" in n and ("0" in n or len(n)==3 or len(n)==4 or len(n)==5):
        cc += 1
        n = n.replace("0", "").replace("1", "").replace("a", "")
        if len(n) == 2:
            ccc += 1
        nnn = hex(i)[2:].replace("a", "").replace("0", "")
        if nnn == "11":
            c21 += 1
            #print("\t{}".format(hex(i)[2:]))
        #print(n)
print("tot")
print(cc)


"""
print()
print("1 diff 2 diff")
print(ccc)
print("ana 2 diff")
print(fac(lim)*13*12)
print("c21")
print(c21)


w=0
w = fac(lim)*13**(lim-3)
#1 1, 0 0, 
dd = fac(lim)/6
#1 a ... aa => 
ss = fac(lim)/4
#1 x
oo = fac(lim)*13/2
x = fac(lim)/2
y = fac(lim)/2
z = fac(lim)/2
print("analyze")
#print(w+x+y+z-2)
print(w+3*dd+9*ss+3*oo)
print(3*14**4-3*13**4+12**4-2)
"""

ans = 16**lim-3*15**lim+3*14**lim-13**lim-2
print(ans)
print(hex(ans))


#4609962410815813306
#0x3ff9e063549476ba
# 3FF9E063549476BA