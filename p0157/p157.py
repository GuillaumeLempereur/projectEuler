"""
p157
seems to work for n = 1 & 2
ans:
2	102
3	356
4	958

1/a + 1/b = p/10 => 20 solutions
10**n * (a+b)/(a*b) = p <=> 10**n * (a+b) = p * a*b <=> 10**n = p * a*b/(a+b)
10**n * a + 10**n * b - p*(a*b) = 0
ax² + bxy + cy² + dx + ey + f = 0
a = c = 0 and D = E = 10**n and B = -p
Bxy + Dx + Ey + F = 0
------
https://www.alpertron.com.ar/METHODS.HTM#SHyperb
Simple Hyperbolic case A = C = 0; B ≠ 0 , a hyperbola whose asymptotes are parallel to x and y axes
DE-BF = 10**(2*n) - 0 > 0

Let d1, d2, ..., dn be the set of divisors of DE - BF = 10**(2*n)

x = (d_i - E)/B = (d_i - 10**n)/(-p)
y = ((DE-BF)/d_i - D)/B = (10**(2*n) / d_i - 10**n)/(-p)

x = (10**n - d_i)/p
y = 10**n *(1- 10**n / d_i) / p
Issue ?

ex: p = 7, d_i = {1, 2, 5, 10, 20, 50, 100} 10**(2*n) = 100
------
d < 10**n and (d - 10**n)/d > 0
d < 0
x < y (a < b)
(10**n - d)//p < (10**n) * (d - 10**n)//d//p
10**n - d < (10**n) * (d - 10**n)//d
p <= 2*10**n
"""

import sys
sys.path.insert(1, '..')
import Euler


lim = int(sys.argv[1])

#dl: list of divisors of 10**2n from -10**2n to 0; divisors: 10**n: 2**n * 5**n
tot = 0
for n in range(1,lim+1):
    dl = []
    for i in range(2*n+1):
        for j in range(2*n+1):
            dl.append(-(2**i) * 5**j)
    cnt = 0
    for d in dl:
        pLst = []
        Euler.lstDiv(pLst, 10**n-d)
        #for p in range(1,2*10**n+1):
        for p in pLst:
            if (10**n - d) % p == 0 and ((10**n)*(d - 10**n))%(d*p) == 0:
                x = (10**n - d)//p
                y = (10**n) * (d - 10**n)//d//p
                if x <= y:
                    #print("{}\t{}\t{}\t{}".format(x, y, p, d))
                    cnt += 1
    print("{}\t{}".format(n, cnt))
    tot += cnt
print("ans: {}".format(tot))
