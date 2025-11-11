
import Euler
import math


def root(x):
    return round(math.sqrt(x))

s = set()
cc = 0
c2 = 0
lim = 1000000 # 250000
lim = 1000 # 250000
for d in range(1,lim):
    boundLow = math.floor(math.sqrt(1+d**6))+1
    boundHigh = math.floor(math.sqrt(4*(lim**2)+d**6))+1
    for g in range(boundLow,boundHigh):
        c2 += 1
        n = (g-d**3)*(g+d**3)
        s.add(g-d**3)
        s.add(g+d**3)
        #t = round(math.sqrt(n2))
        #if t*t == n2:
        #    #print(g,d,n2,g-d**3,g+d**3,Euler.factorization(g-d**3),Euler.factorization(g+d**3))
        #    cc += 1

print(cc)
print(c2)
print(len(s))

exit(0)

cc = 0
c2 = 0
lim = 250000 # 250000
for d in range(1,lim):
    boundLow = math.floor(math.sqrt(1+d**6))+1
    boundHigh = math.floor(math.sqrt(8*(lim**2)+d**6))+1
    for g in range(boundLow,boundHigh):
        c2 += 1
        n2 = 8*(g-d**3)*(g+d**3)

        t = round(math.sqrt(n2))
        if t*t == n2:
            #print(g,d,n2,g-d**3,g+d**3,Euler.factorization(g-d**3),Euler.factorization(g+d**3))
            cc += 1

print(cc)
print(c2)

exit(0)

lim = 1000
for d in range(1,lim):
    boundLow = math.floor(math.sqrt(1+d**6))+1
    boundHigh = math.floor(math.sqrt(4*(lim**2)+d**6))+1
    for g in range(boundLow,boundHigh):

        n2 = 2*(g-d**3)*(g+d**3)

        t = round(math.sqrt(n2))
        if t*t == n2:
            print(g,d,n2,g-d**3,g+d**3,Euler.factorization(g-d**3),Euler.factorization(g+d**3))
exit(0)

a = 6072
d = 6400

nsq = d*(4*a*a+d**3)

x = 4*a*a
y = d**3
z = (4*a*a+d**3)

cf = Euler.gcd(x,Euler.gcd(y,z))
x, y, z = x//cf, y//cf, z//cf

x,y,z = root(x), root(y), root(z)

print("cf",cf)
print("x", x)
print("y", y)
print("z", z)


print(x+y,z)

print(math.sqrt(x+z))
print(math.sqrt(z+y))

exit(0)

lim = 500000

cc = {}
for i in range(1,lim):
    cc[3*i**3] = i

print("cc ready")

for a in range(1,lim):
    if (a**2-3)**2 in cc:
        print(a)

exit(0)
for r in range(1,a*a):
    s = (a*a-r)**2

    f_a = Euler.factorization(a)
    f_r = Euler.factorization(r)

    if s % r == 0: #and a%r != 0:
        for f in f_a:
            if f not in f_r:
                print(a,r,f)
        #    print(a,r,s)
