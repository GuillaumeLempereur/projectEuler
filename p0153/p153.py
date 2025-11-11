#p153
"""
    works for lim <= 10
    probably bugged and need scale up

    takes too much time
"""

import Euler
import sys
import math

#d = {}
d_a = {} # real part of dividers
lim = int(sys.argv[1])

for n in range(lim+1):
    #d[n] = 0
    d_a[n] = 0

#Gaussian divider:
for a in range(1, lim):
    for b in range(1, a):
        g = Euler.gcd(a, b)
        n = a*a+b*b
        n //= g #case2: coprime
        if n > lim:
            continue # can be improved

        for i in range(1, lim//n+1):
            #d[i*n] += 4 # a +/- b i or b +/- a i
            d_a[i*n] += 2*a + 2*b

    #case a == b:
    n = a*2
    if n > lim:
        continue # can be improved
    for i in range(1, lim//n+1):
        #d[i*n] += 4 # a +/- a i
        d_a[i*n] += 2*a

"""
for n in range(1,10):
    print("{}\t{}".format(n, d_a[n]))
"""
print()

#Real divider:
"""
Max number of dividers = log2(n)
"""
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

print("ans: {}\t{}".format(lim, tot))

