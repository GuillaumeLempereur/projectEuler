import Euler
import math

lim2 = 5000
lim = 5000
sq = {}
for i in range(lim2*lim2):
    sq[i*i] = i

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

print("r,d,a,Euler.factorization(r),Euler.factorization(a*a)")
for r in range(1,lim):
    c = False
    f = Euler.factorization(r)
    for i in f:
        if f[i] == 1:
            c = True
            break
    if c:
        continue
    for d in range(r+1,lim):
        aasq = r*d**3
        if aasq in sq:
            asq = sq[aasq]+r
            if asq in sq:
                a = sq[asq]
                #print(r,d,a**4/r,math.sqrt(r*d),a,Euler.factorization(r),Euler.factorization(a*a),Euler.factorization(d**3-r),Euler.factorization(a*a-2*r))
                print(r,d,a,Euler.factorization(r),Euler.factorization(a),Euler.factorization(d))

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
