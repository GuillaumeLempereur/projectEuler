import Euler
import math

lim = 5000
sq = {}
for i in range(lim*lim):
    sq[i*i] = i

print("Square loaded")

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
        ss = round(math.sqrt(ssq))
        if ss+r in sq:
            print(r,Euler.factorization(r),(ss-r)**2/r,r*(d**3),ss,d,i,r0)


exit(0)
for r in range(1,lim):
    for d in range(r+1,lim):
        aasq = r*d**3
        if aasq in sq:
            asq = sq[aasq]+r
            if asq in sq:
                a = sq[asq]
                print(r,d,a,Euler.factorization(r),Euler.factorization(d))
