"""
p193
it works but higly inefficient !
ans:
1000	608
10000	6083
100000	60794
10**9   607927124
"""
import sys

sys.path.insert(1, '..')
import Euler

lim = int(sys.argv[1])
primes = Euler.primesbelow(int(lim**0.5)+1)
cnt = lim

print("primes list ready!")
m = 1
def comb(s, d):
    global m, cnt
    for i in range(s, len(primes)):
        m *= primes[i]*primes[i]
        if m > lim: # no need to continue
            m //= primes[i]*primes[i]
            return

        if d%2==0:
            cnt -= (lim // m)
        else:
            cnt += (lim // m)

        comb(i+1, d+1)
        m //= primes[i]*primes[i]

comb(0, 0)
print(cnt)
