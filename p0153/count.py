#p153
"""
count the nb of solution
"""
import Euler

d = {}
lim = 10
for n in range(10000):
    d[n] = 0

#Gaussian divider:
for a in range(1, lim):
    for b in range(1, a):
        n = a*a+b*b
        #consider multiple of n
        for i in range(1, 5):
            d[i*n] += 4 # a +/- b i or b +/- c i

    #if a and b not coprime => n/k also good

    n = 2*a*a
    #d[n] += 2
    for i in range(1, 5):
        d[i*n] += 2 # a +/- b i or b +/- c i
        #consider multiple of n
    if a == 1:
        continue
    n = 2*a
    #d[n] += 2
    for i in range(1, 5):
        d[i*n] += 2 # a +/- b i or b +/- c i
        #consider multiple of n

#Real divider:
#list of divider:
for n in range(1,10):
    fs = Euler.factorization(n)
    comb = 1
    for i in fs:
        comb *= (fs[i]+1)
    d[n] += comb

for n in range(1,10):
    print("{}\t{}".format(n, d[n]))
