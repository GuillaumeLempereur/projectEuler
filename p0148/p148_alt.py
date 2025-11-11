# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 08:43:31 2017

@author: lempereu
p148 alternative
"""
import math
import scipy


p = []

for n in range(400):
    l = []
    for i in range(n+1):
        l.append(scipy.misc.comb(n,i,exact=True))

    print(l)
    p.append(l)

print(p)
f = open('small_pascal.html', 'w')

"""
plen = len(p)
maxx = p[-1][plen//2]
nbDigit = math.floor(math.log10(maxx))+1

lstr = plen*nbDigit+(plen-1)
print("n",nbDigit)

sp_l = nbDigit
for l in p:
    print(" "*((lstr-sp_l+1)//2),end=' ')
    for i in l:
        print(str(i).rjust(nbDigit, ' '),end=' ')
    print()
    sp_l += nbDigit+1
"""

f.write("<html>\n")
f.write("<style>p{text-align:center;white-space: nowrap;width:80000px;}</style>\n")
f.write("<p>\n")
for l in p:
    for i in l:
        if i%7==0:
            f.write("<font color=\"red\">1</font> ")
        else:
            f.write("0 ")
    f.write("<br/>\n")
f.write("</p>\n")
f.write("</html>\n")
f.close()