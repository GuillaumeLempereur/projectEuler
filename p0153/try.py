#p153
"""
    real part computed but cannot overlap 1000 because of recursion limit
    >10000 takes too much time
    need scale up
"""

import Euler
import sys
import math

"""
useless
#sum for the real parts
def f_r():
    1
    #prime: 1 + n
    # co-prime: ...

#sum for the real parts
def s_r():
    1
    #prime: 1 + n
    # co-prime: ...


def s_r_bf(n):
    c = 1
    while n > 1:
        for i in range(1,n+1):
            if n%i == 0:
                c += i
        n -= 1
    return c
"""

d_a = {} # real part of dividers
lim = int(sys.argv[1])
lp = Euler.primesbelow(lim)
print("list primes done")
for i in range(lim+1):
    d_a[i] = 0

n = lim
#List of coprimes:
iMax = len(lp)
su = 0 # count 1
def cop(d, i):
    global su
    if i == iMax:
        #print("\t{}".format(d))
        #if d in lp: # case d is prime
        #    su += d+1
        if d != 1:
            su += (n//d-1)*d
            #print("\t\t{}".format((n//d-1)*d))
        return
    cop(d, i+1)# leave it
    k = 1
    while d*lp[i]**k <= n/2:
        cop(d*lp[i]**k, i+1)# take it
        k += 1
print("Start Gaussian")
#Gaussian divider:
for a in range(1, lim):
    for b in range(1, a):
        g = Euler.gcd(a, b)
        nn = a*a+b*b
        nn //= g #case2: coprime
        if nn > lim:
            continue # can be improved

        for i in range(1, lim//nn+1):
            d_a[i*nn] += 2*a + 2*b

    #case a == b:
    nn = a*2
    if nn > lim:
        continue # can be improved
    for i in range(1, lim//nn+1):
        d_a[i*nn] += 2*a

print("Finish Gaussian")
"""
for n in range(1,10):
    print("{}\t{}".format(n, d_a[n]))
"""
print()

#Real divider:
"""
Max number of dividers = log2(n)
"""
"""
old method
def lstDiv(lst, d, fs):
    if len(fs)==0:
        #print("\t"*(2-len(fs)) + "append {}".format(d))
        lst.append(d)
        return
    f = 1
    nbMul = 1
    for ff in fs:
        f = ff
        nbMul = fs[f]
        del fs[f]
        break
    for i in range(nbMul+1):
        #print("\t"*(2-len(fs))+"{}\t{}".format(d, fs))
        lstDiv(lst, d*f**i, fs.copy())


tot = 0
#list of divider:
for n in range(1,lim+1):
    fs = Euler.factorization(n) # list of factors with repetition ex: [2, 2, 2, 3, 3]

    lst = []
    lstDiv(lst, 1, fs.copy())
    #print(lst)

    sm = 0
    for d in lst:
        sm += d
    #print("{}\t{}\t{}\t{}".format(n, d_a[n] + sm, d_a[n], sm))
    tot += d_a[n] + sm
"""

if(n<10000):
    cop(1, 0)
    su += (n+1)*n//2+n-1
    #print(su)

gauss_tot = 0
for n in range(1,lim+1):
    gauss_tot += d_a[n]

tot = gauss_tot + su
print("lim\ttot\treal\tgaus".format(lim, tot, su, gauss_tot))
print("{}\t{}\t{}\t{}".format(lim, tot, su, gauss_tot))
