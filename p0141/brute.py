import Euler
import math
import sys


def root(x):
    return round(math.sqrt(x))



# enumerate every g ,d below lim

lim = 200

lim = int(sys.argv[1])

cc = 0
c2 = 0

print("math.sqrt(rs/4), p, g, d")
for d in range(1,lim):
    boundLow = math.floor(math.sqrt(1+d**6))+1
    boundHigh = math.floor(math.sqrt(4*(lim**2)+d**6))+1
    for g in range(boundLow,boundHigh):

        cc += 1
        n = (g-d**3)*(g+d**3)

        if d == 407:
            print("facorizing",g-d**3,g+d**3)
        f1 = Euler.factorization(g-d**3)
        f2 = Euler.factorization(g+d**3)
        if d == 407:
            print("end facorizing")

        #print("-"*15)
        #print(g,d)
        #print(f1)
        #print(f2)
        p = 1
        ff = f1
        for f in f2:
            if f in f1:
                ff[f] += f2[f]
            else:
                ff[f] = f2[f]
        for f in ff:
            if ff[f] %2 == 1:
                p*=f

        #print(ff)
        rs = p**3*(g-d**3)*(g+d**3)
        if rs%4 != 0 or rs >= 4*lim*lim:
            continue
        else:
            #print(math.sqrt(rs/4), p, g, d)
            al[round(math.sqrt(rs//4))] = True
c2 = 0
for i in range(len(al)):
    if al[i]:
        c2 += 1
        print(i)
print(cc)
print(c2)
exit(0)

