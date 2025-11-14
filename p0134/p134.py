import sys
sys.path.insert(1, '..')
import Euler
"""
Problem 134
"""

lim = 1000000

primes = []

primes = Euler.primesbelow(lim)

primes = primes[2:]

for i in range(lim,lim*4):
    if Euler.isprime(i):
        primes.append(i)
        break

#p1 = 2
summ = 0
mask = 10
for i1 in range(len(primes)-1):
    p1 = primes[i1]
    p2 = primes[i1+1]

    s = 0
    if mask < p1:
        mask *= 10

    a,b,n = mask%p2, p2, p2-p1
    (x_0, y_0) = Euler.BezoutCoeff(a,b,n)
    x_0 %= b
    s = mask*x_0+p1

    if s == 0:
        exit(-2)


    summ += s

print("Ans:", summ)
