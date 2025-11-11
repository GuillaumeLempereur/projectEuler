import Euler
import math

lim = 5000
sq = {}
for i in range(lim*lim):
    sq[i*i] = i

print("Square loaded")

print("r,a,d,i,r0,Euler.factorization(r),(a*a-r)**2,r*(d**3)")
for d in range(2,lim):
    f = Euler.factorization(d)
    r0 = 1
    sqprt = 1
    for i in f:
        e = f[i]
        if e%2 == 1:
            r0 *= i

    for i in range(1,lim):
        r = r0*i*i
        if r >= d:
            break
        ssq = r*(d**3)
        asq = sq[ssq]+r
        if asq in sq:
            a = sq[asq]
            print(r,a,d,i,r0,Euler.factorization(r),(a*a-r)**2,r*(d**3))

exit(0)

for r in range(1,lim):
    for d in range(r+1,lim):
        aasq = r*d**3
        if aasq in sq:
            asq = sq[aasq]+r
            if asq in sq:
                a = sq[asq]
                print(r,d,a,Euler.factorization(r),Euler.factorization(d))
