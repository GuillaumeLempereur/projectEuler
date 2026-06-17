"""
p278

"""
import sys
sys.path.insert(1, '..')
import Euler

lim = 5000

primes = Euler.primesbelow(lim)
nbPrim = len(primes)
ans = 0
for i in range(nbPrim):
    p = primes[i]
    for j in range(i+1, nbPrim):
        q = primes[j]
        for k in range(j+1, nbPrim):
            r = primes[k]
            f = (p-1)*(q-1) + p*(q-1)*(r-1) + q*(p-1)*(r-1)-1

            #print(p*q, p*r, q*r, f)
            ans += f

print(ans)
