#p152

import sys
sys.path.insert(1, '..')

import Euler
import Frac as F
LIM = 45

if len(sys.argv)==2:
    LIM = int(sys.argv[1])

# remove prime > LIM/2

primes = Euler.primesbelow(LIM+1)
kl = list(range(3, LIM+1))

for p in primes:
    if p > LIM/2:
        kl.remove(p)

#print(kl)
#print(len(kl))

#dictionary of the ks sorted by prime factor {5: [5,10,], 7: [7,14]} except 2 and 3
kl_by_p = {}
for k in kl:
    # we skip 2 and 3 otherwise it takes too much time
    if k in primes and k != 3:
        kl_by_p[k] = []
for p in kl_by_p:
    for k in kl:
        if k%p == 0:
            kl_by_p[p].append(k)

#for each prime, list of the combination of k such sum 1/k² deno %prime != 0
kComb_by_p = {}
for p in kl_by_p:
    kComb_by_p[p] = []


c = 0

# n/d : numerator/denominator of the sum in the list
# k is the prime factor to be combined in such way that sum 1/k denominator %k != 0
# lst : list of the ks taken
# i : index of the next k to take
def rec(n, d, k, lstK, lst, i):
    #global c
    #print(c, i, len(lst))
    #if c > 10:
    #    return
    for ii in range(i, len(lstK)):
        #pick k from the list
        kk = lstK[ii]
        lst.append(kk)
        # n/d = n/d + 1/k/k
        new_n, new_d = kk*kk*n + d, d*kk*kk
        gcd = Euler.gcd(new_n, new_d)
        new_n, new_d = new_n//gcd, new_d//gcd
        if new_d%k != 0:
            #print(lst, " <> ", new_n, new_d)
            kComb_by_p[k].append(lst[:])
            #c += 1
        #print(lst)
        rec(new_n, new_d, k, lstK, lst, ii+1)
        lst.pop()

for p in kComb_by_p:
    lst = []
    rec(0, 1, p, kl_by_p[p], lst, 0)
    #print(p, len(kComb_by_p[p]))
    #print(kComb_by_p[p])

    #remove from kl the k that are not part of a combination (except 2 and 3)
    kl_p = {} # dic of the k present in at least one combination of k for the prime p
    for lst in kComb_by_p[p]:
        for k in lst:
            kl_p[k] = True

    for k in kl_by_p[p]:
        if k not in kl_p:
            kl.remove(k)

#clean kComb_by_p : remove the combination that includes primes not  possible like 11 => 55
pToDel = []
for p in kComb_by_p:
    if len(kComb_by_p[p]) == 0: #the prime has no combination possible
        pToDel.append(p)
        for pp in kComb_by_p:
            toDel = {}
            for i in range(len(kComb_by_p[pp])):
                for el in kComb_by_p[pp][i]:
                    if el % p == 0:
                        toDel[i] = True
            for i in reversed(list(toDel.keys())):
                del kComb_by_p[pp][i]

for p in pToDel:
    del kComb_by_p[p]

for p in kComb_by_p:
    print(p, len(kComb_by_p[p]))
    print(kComb_by_p[p])

#print(kl)
#print(len(kl))
#list of k with no other prime factor than 2 and 3
kl_2_3 = []
for k in kl:
    toDel = False
    for p in kComb_by_p:
        if k%p == 0:
            toDel = True
            break
    if not toDel:
        kl_2_3.append(k)

#print(kl_2_3)
#print(len(kl_2_3))

#all possible sum of k with only 2/3 as prime factor

sum_2_3 = []
sum_2_3_cmb = []
kl_2_3_cmb_by_sum = {}

#combination with only 2 and 3
#n/d so far
#i next k to take
def comb(n, d, i, lst):
    for ii in range(i,len(kl_2_3)):
        k = kl_2_3[ii]
        lst.append(k)
        n_, d_ = k*k*n + d, d*k*k
        gcd = Euler.gcd(n_, d_)
        n_, d_ = n_//gcd, d_//gcd

        if (n_, d_) in kl_2_3_cmb_by_sum:
            kl_2_3_cmb_by_sum[(n_, d_)].append(lst[:])
        else:
            kl_2_3_cmb_by_sum[(n_, d_)] = [lst[:]]

        sum_2_3.append((n_,d_))
        sum_2_3_cmb.append(lst[:])
        comb(n_, d_, ii+1, lst)
        lst.pop()

comb(0, 1, 0, [])

#Find in all the combination of k mul of 2 and 3 the sum required
def findCmb23(n,d, kl_primes_cmb):
    c = 0
    # look if in comb_2_3 got the sum to make 1/4: look for (1/4 - n/d)
    r = F.Frac(1,4) - F.Frac(n, d)
    if (r.n, r.d) in kl_2_3_cmb_by_sum:
        for cmb in kl_2_3_cmb_by_sum[(r.n, r.d)]:
            kl_sol = list(set(kl_primes_cmb).union(cmb + [2]))
            print("Found:", sorted(kl_sol))
            c+=1
    return c

"""
Combination
5
7
13
5   7
7   13
5   13
"""

# combine all the combination and check if their sum = 1/4
# 7 only
for kl_p in kComb_by_p[7]:
    n, d = 0, 1
    for k in kl_p:
        n, d = n*k*k + d, d*k*k
    c += findCmb23(n, d, kl_p)

# 5 only
for kl_p in kComb_by_p[5]:
    n, d = 0, 1
    for k in kl_p:
        n, d = n*k*k + d, d*k*k

    c += findCmb23(n, d, kl_p)

# 13 only
for kl_p in kComb_by_p[13]:
    n, d = 0, 1
    for k in kl_p:
        n, d = n*k*k + d, d*k*k

    c += findCmb23(n, d, kl_p)

# 5 & 7
for kl_5 in kComb_by_p[5]:
    for kl_7 in kComb_by_p[7]:
        toSkip = False
        #check that k that are both divisible by 5 and 7 are in both combination
        for k in kl_5 + kl_7:
            if k%7 ==0 and k%5 ==0:
                if not(k in kl_5 and k in kl_7):
                    toSkip = True
                    break
        if toSkip:
            continue
        kl_5_7 = list(set(kl_5).union(set(kl_7)))
        n, d = 0, 1
        for k in kl_5_7:
            n, d = n*k*k + d, d*k*k

        c += findCmb23(n, d, kl_5_7)

# 5 & 13
for kl_5 in kComb_by_p[5]:
    for kl_13 in kComb_by_p[13]:
        toSkip = False
        #check that k that are both divisible by 5 and 13 are in both combination
        for k in kl_5 + kl_13:
            if k%13 ==0 and k%5 ==0:
                if not(k in kl_5 and k in kl_13):
                    toSkip = True
                    break
        if toSkip:
            continue
        kl_primes = list(set(kl_5).union(set(kl_13)))
        n, d = 0, 1
        for k in kl_primes:
            n, d = n*k*k + d, d*k*k

        c += findCmb23(n, d, kl_primes)

# 7 & 13
for kl_7 in kComb_by_p[7]:
    for kl_13 in kComb_by_p[13]:
        toSkip = False
        #check that k that are both divisible by 7 and 13 are in both combination
        for k in kl_7 + kl_13:
            if k%13 ==0 and k%7 ==0:
                if not(k in kl_7 and k in kl_13):
                    toSkip = True
                    break
        if toSkip:
            continue
        kl_primes = list(set(kl_7).union(set(kl_13)))
        n, d = 0, 1
        for k in kl_primes:
            n, d = n*k*k + d, d*k*k

        c += findCmb23(n, d, kl_primes)

        #check 5 & 7 & 13
        for kl_5 in kComb_by_p[5]:
            toSkip = False
            #check that k that are both divisible by 5 and 7 are in both combination
            for k in kl_5 + kl_7:
                if k%5 ==0 and k%7 ==0:
                    if not(k in kl_7 and k in kl_5):
                        toSkip = True
                        break
            if toSkip:
                continue
            toSkip = False
            #check that k that are both divisible by 5 and 7 are in both combination
            for k in kl_5 + kl_13:
                if k%5 ==0 and k%13 ==0:
                    if not(k in kl_13 and k in kl_5):
                        toSkip = True
                        break
            if toSkip:
                continue

            kl_primes = list(set(kl_7+kl_5).union(set(kl_13)))
            n, d = 0, 1
            for k in kl_primes:
                n, d = n*k*k + d, d*k*k

            c += findCmb23(n, d, kl_primes)
print("Answer:",c)
