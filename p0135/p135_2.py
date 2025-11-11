# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 17:15:02 2017

@author: lempereu
P135
"""
# not th answer: 23907
# 23867

import Euler
import pickle


divList = pickle.load( open( "divList.p", "rb" ))

c = 0
rc = 0
for div in divList:
    if len(div) >= 5:
        c += 1
        cd = 0
        s = set()
        for i in range((len(div)+1)//2):
            x,y = div[i],div[-i-1]
            """
                        if div[-1] == 1155:
                            print(x,y,x+y,y-x)
            """
            if (x+y)%4 != 0 or (y-x)%2 !=0:
                continue

            r = (x+y)//4
            a = (y-x)//2
            if div[-1] == 120:
                print(x,y,r,a,r+a,r-a)
            if r-a > 0:
                cd += 1
                s.add((3*r-a,2*r-a,r-a))
            if r+a > 0:
                cd += 1
                s.add((3*r+a,2*r+a,r+a))
        
        if len(s) == 10:
            #print(s)
            rc += 1
            #print(div[-1])
            #print(div)
        
            #if div[-1] < 1200:
            #    print(div[-1])
print(rc)
