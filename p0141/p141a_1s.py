import Euler
import math

lim = 10000
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

#print("r,d,a,Euler.factorization(r),Euler.factorization(a*a)")
print("Euler.factorization(d),Euler.factorization(a),Euler.factorization(r),r+round(math.sqrt(r*d**3)),a*a,Euler.factorization(r),Euler.factorization(a*a)")
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
        if round(math.sqrt(aasq))**2 == aasq:
        #if aasq in sq:
            #asq = sq[aasq]+r
            asq = round(math.sqrt(aasq))+r
            #if asq in sq:
            if round(math.sqrt(asq))**2 == asq:
                #a = sq[asq]
                a = round(math.sqrt(asq))
                q = (a*a-r)//d
                #print(r,d,a,Euler.factorization(r),Euler.factorization(a*a))
                print(d,q,math.sqrt(a**4-4*q**3),Euler.factorization(d),Euler.factorization(a),Euler.factorization(r),r+round(math.sqrt(r*d**3)),a*a,Euler.factorization(r),Euler.factorization(a*a))

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
