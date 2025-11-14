#Problem 130
"""
Repunit divisibility
"""
import sys
sys.path.insert(1, '..')
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

        if s == 0:
            if((n-1)%i==0):
                imax += 1
                #print("\t",n,i)
                ss += n
            break # not interesting cause R(i < 5000) is divisible by n
        if r == 1: # and i > 1:
            break # found a reccurence
        rlst.append(r)

    if s == 0:
        continue

    # 10xn % p = (10%p * n%p)%p
    s = 0
    for r in range(2*10**6):
        s = (s+rlst[r%len(rlst)])%n
        if s == 0:
            if r > 1: # 10**6:
                if((n-1)%(r+1)==0):
                    imax += 1
                    #print("\t",n,i)
                    ss += n
            break

    if imax == 25:
        print("Ans:", ss)
        break

elapsed_time = time.time() - start_time

print("elapsed time:",elapsed_time)
