#Problem 130
"""
Repunit divisibility
"""

import Euler
import time

"""
n not multiple of 10
There exist k such that R(k) is divisible by n

A(n) the least value of k

A(7) = 6 => 111111 divisible by 7
A(41) = 5 => 11111 divisible by 41


1%41 + 10 %41 + 10^2 %41 + 10^3 %41
For ech 1,10,100,... there is a recurrence in the modulo, sum the recurrence until having %n = 0


The 5 first: 91, 259, 541, 481, 703

lim 10000: 1:40 r ~= 100000
"""

def R(n):
    s = "1"*n
    return int(s)

#print(R(10847+1)%10851)
start_time = time.time()

imax = 0

ss = 0

lim = 25000 #10000
n = 11
for i in range(lim):
    n += 1
    if n%5==0 or n%2==0 or Euler.isprime(n):
        continue

    a_r = 0
    s = 0
    rlst = []
    r = 1
    rlst.append(r)
    for i in range(1,10**6): # 10**6 # need to speed up the finding of the recurrence !!!!
        r = ((10%n)*r) % n

        s = (s+r)%n
        #print("\t", r, s)

        if s == 0:
            #print(n,i)
            if((n-1)%i==0):
                imax += 1
                print("yep: ",n,i)
                ss += n
            #if r not in rl:
            #    rl.add(r)
            #    rlst.append(r)
            break # not interesting cause R(i < 5000) is divisible by n
        if r == 1: # and i > 1:
            #print(n,sum(rlst)%n)
            break # found a reccurence
        rlst.append(r)

    if s == 0:
        continue

    #if len(rlst) < n//8: # not really an improvement
    #   continue

    #print(n,rlst)

    # 10xn % p = (10%p * n%p)%p
    s = 0
    for r in range(2*10**6):
        s = (s+rlst[r%len(rlst)])%n
        if s == 0:
            if r > 1: # 10**6:
                #print(n,r+1,len(rlst)) # print(R(r+1)%n)
                if((n-1)%(r+1)==0):
                    imax += 1
                    print("\t yep:",n,i)
                    ss += n
            break

    if imax == 25:
        print(ss)
        break

print(imax)

elapsed_time = time.time() - start_time

print("elapsed time:",elapsed_time)

    #print(n, s, rl)

    #print()


"""
r = 0
rec = [10,18,16,37,1]
for i in range(lim):
    r = (r+rec[i%5])%21
    print(i,r)

"""

"""
def gcd(a,b):
    if a < b:
        return gcd(b,a)
    while(b>0):
        a, b = b, a%b
    return a

lim = 1000
r = 11

fac = 1
for i in range(lim):
    fac *= i*10+1


for i in range(lim):
    print(i,Euler.primefactors(gcd(fac,r)))

    r = r*10 + 1
"""

"""

print(R(11))

print((R(10**6))%19)
"""
