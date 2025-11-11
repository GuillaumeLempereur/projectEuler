"""
p168

n = a*10+b
b*10**i + a = (a*10+b)*x
i from 1 to 99
b from 1 to 9
a*(10*x-1) = b*10**i-b*x
a = (b*10**i-b*x)/(10*x-1)

10*a*x - a + b*x -b*10**i = 0
-a + 10*a*x + b - b*10**i = 0 => diophantine eq
D = -1, B = 10, E = b, F = -b*10**i
Simple Hyperbolic case A = C = 0; B ≠ 0
DE - BF != 0
-b+10*(b*10**i) = -b+b*10**(i+1) = b*(10**(i+1)-1)
all divisors of DE-BF: Let d1, d2, ..., dn 
x = (d-E)/B
y = (DE-BF)/d-D)/B

10**i > a >= 10**(i-1)
10**i > (d-b)//10 > 10**(i-1)
10**(i+1) > d-b > 10**i (first always true)
d-b > 10**i <=> d > 10**i+b ; d is [div of 10**(i+1)-1]*[div of b]
"""
import sys
import math
import time
sys.path.insert(1, '..')
import Euler
lim = 6

l9 = {} # list of divisors of the 10**i-1 not smaller than 10**(i-2)
for i in range(1,101):
    n = 10**i-1

    l9[i] = [1]
    for d in range(3,100):
        if (n//d)*d == n:
            l9[i].append(n//d)

c = 0
#iMax = int(sys.argv[1]) #100 #24 n  < 10**iMax
iMax = 100

t1 = time.time()

b_div = {1: [1],
         2: [1, 2],
         3: [1,3],
         4: [1,2,4],
         5: [1,5],
         6: [1,2,3,6],
         7: [1,7],
         8: [1,2,4,8],
         9: [1,3,9]}
setN = set()
for b in range(1,10):
    for db in b_div[b]:
        for i in range(1, iMax):
            for d9 in l9[i+1]:
                d = d9*db
                if (b*(10**(i+1)-1)//d+1) % 10 != 0:
                    continue
                a, y = (d-b)//10, (b*(10**(i+1)-1)//d+1)//10
                if a < 10**(i-1):
                    continue
                if 10**(i+1) <= d-b or d-b < 10**i:
                    print("{}\t{}\t{}".format(10**(i+1), d-b, 10**i))
                    exit(-5)
                #print("{}\t{}\t{}\t{}\t{}\t{}".format(b,a,y,b*10**i+a,10*a+b,d))
                setN.add(10*a+b)

t2 = time.time()
s = 0
for i in setN:
    s += i
    #print(i)
print(s%100000)
print(s)
