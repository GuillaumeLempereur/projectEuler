import Euler
"""
Answer: not 18613426663617130
"""

lim = 1000000

#lim = 2500
primes = []

primes = Euler.primesbelow(lim)

primes = primes[2:]

for i in range(lim,lim*4):
    if Euler.isprime(i):
        primes.append(i)
        break

print(len(primes))

#p1 = 2
summ = 0
mask = 10
for i1 in range(len(primes)-1):
    p1 = primes[i1]
    p2 = primes[i1+1]

    s = 0
    if mask < p1:
        mask *= 10

    #print("-"*25)

    #print("p1,p2")
    #print(p1,p2,mask)
    a,b,n = mask%p2, p2, p2-p1
    #print("p1,p2,a,b,n,Euler.equationMod(a,b,n)")
    #print(p1,p2,a,b,n,Euler.equationMod(a,b,n))
    (x_0, y_0) = Euler.equationMod(a,b,n)
    #print(x_0,y_0)
    #print(n//Euler.gcd(a,b),a,x_0)
    x_0 %= b
    s = mask*x_0+p1
    #print("s,p1,p2")
    #print(s,p1,p2, (mask*x_0+p1)/p2)
    """
    for a in range(1,p2):
        n  = mask*a+p1
        if n%p2 ==0:
            s = n
            #print(n,p1,p2)
            break
    """

    if s == 0:
        exit(-2)


    summ += s

print(summ)
