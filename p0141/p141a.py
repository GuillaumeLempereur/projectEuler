import Euler
import math

"""
200000 : 11s
"""

lim = 1000000
"""
sq = {}
for i in range(lim2*lim2):
    sq[i*i] = i
"""
print("Square loaded")


"""
print("p,r,d,a,Euler.factorization(r),Euler.factorization(a*a)")
for p in [2,3,5,7,11,13,17,19,23,29,31,37,43]:
    for rr in range(1,lim):
        r = rr*p
        for d in range(r+1,lim):
            aasq = r*d**3
            if aasq in sq:
                asq = sq[aasq]+r
                if asq in sq:
                    a = sq[asq]
                    print(p,r,d,a,Euler.factorization(r),Euler.factorization(a*a))
"""

sumy = 0

print("a*a,r,d,a,Euler.factorization(r),Euler.factorization(a*a)")
for r in range(1,lim):
    c = False
    f = Euler.factorization(r)
    d0 = 1
    for i in f:
        if f[i] == 1:
            c = True
            break
        d0 *= i
    if c:
        continue
    for j in range(round((r+1)/d0),round(lim/d0)):
        d = d0*j
        aasq = r*d**3
        if round(math.sqrt(aasq))**2 == aasq:
        #if aasq in sq:
            #asq = sq[aasq]+r
            asq = round(math.sqrt(aasq))+r
            #if asq in sq:
            if round(math.sqrt(asq))**2 == asq:
                #a = sq[asq]
                a = round(math.sqrt(asq))
                q = asq//d
                if Euler.gcd(d,q) == 1:
                    print(a*a,q*(d*d+q)//d,r,d,a,Euler.factorization(r),Euler.factorization(a*a))
                    sumy += a*a

print(sumy)

"""
print("r,d,a,Euler.factorization(r),Euler.factorization(a*a)")
for r in range(1,lim):
    for d in range(r+1,lim):
        aasq = r*d**3
        if aasq in sq:
            asq = sq[aasq]+r
            if asq in sq:
                a = sq[asq]
                print(r,d,a,Euler.factorization(r),Euler.factorization(a*a))
"""
