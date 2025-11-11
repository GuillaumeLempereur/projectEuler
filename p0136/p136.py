# problem 136
"""
x, y, z = x, x-r, x-2*r
x**2 - y**2-z**2 = x**2-

Works fine but need improvement
"""

import Euler

lim = 50000000

primesl = Euler.primesbelow(lim)

primes = {}
for p in primesl:
    primes[p] = True

def isprime(n):
    if n in primes:
        return True
    return False


cc = 2
"""
l = [0 for i in range(lim)]

l[4] = (2, 1, 4)
l[16] = (4, 2, 16)
"""
for a in range(1,lim//4): # n = 4*a
    n = 4*a

    if isprime(a) and n != 8:
        r = (a+1)//2
        d = (a-1)//2
        x1 = 2*a
        # x2 = 2 # never solution
        #print("n, x, r: 4*a and a prime")
        #print(n, x1, r, x1 * (4 * r - x1))
        #l[n] = (x1, r, n)
        cc += 1

    else:
        if a%4==0 and isprime(a//4) and n != 32:
            # One solution execpted n==32
            r = (a//4 + 1)
            d = (a//4 - 1)
            x1 = 4 * a//4
            # x2 = 4 # never solution
            #print("n, x, r: 16*a and a prime")
            #print(n, x1, r, x1 * (4 * r - x1))
            #l[n] = (x1, r, n)
            cc += 1
            continue

# Should be OK !!!
for a in range(1,(lim+1)//4+1): # n = 4*i -1
    n = 4*a-1

    if not isprime(n):
        continue

    # Only one solution
    r = a
    d = 2*a-1
    x = 4*a-1

    #print("n, x, r: 4*a-1")
    #print(n,x,r,":",x*(4*r-x))
    #l[n] = (x, r, n)
    cc += 1

"""
for i in l:
    if i != 0:
        print(i)
"""
print(cc)
