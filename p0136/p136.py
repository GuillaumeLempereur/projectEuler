# problem 136
"""
x, y, z = x, x-r, x-2*r
x**2 - y**2-z**2 = x**2-
"""
import sys
sys.path.insert(1, '..')
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
        cc += 1

    else:
        if a%4==0 and isprime(a//4) and n != 32:
            # One solution execpted n==32
            r = (a//4 + 1)
            d = (a//4 - 1)
            x1 = 4 * a//4
            cc += 1
            continue

for a in range(1,(lim+1)//4+1): # n = 4*i -1
    n = 4*a-1

    if not isprime(n):
        continue

    # Only one solution
    r = a
    d = 2*a-1
    x = 4*a-1

    cc += 1

print(cc)
