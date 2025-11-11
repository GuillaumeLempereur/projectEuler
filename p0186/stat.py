"""
p186
enumerate all the Sn
find misdial first: n = 442959

lim = 10000000
caller: 8
called: 10
most popular number: 43 times either caller or called

try to make a list of groups of friends => gives up
try to reverse engineer the generator:
try to find recurrence
lim: 10**6  average occurence caller: 1
lim: 5*10**6  average occurence caller: 5
generator seems good random, sweeping all values with same probability


#	caller	called
1	200007	100053
2	600183	500439
3	600683	701497

Caller(n) = S2n-1
Called(n) = S2n

Lagged Fibonacci Generator:

1 <= k <= 55: S_k = [100003 - 200003*k + 300007 *k**3]
56 <= k, S_k = [S_k-24 + S_k-55] mod 1000000

X and Z friend if
X friend with ... friend with ... friend with Z
friend = a : b and b : a

524287

n such that 99% friends of 524287

S(2*n-1) = S(2*n-25) + S(2*n-56) = S(2*n-49) + S(2*n-80) + S(2*n-80) + S(2*n-111)
S(2*n) = S(2*n-24) + S(2*n-55) = S(2*n-48) + S(2*n-79) + S(2*n-79) + S(2*n-110)
"""
import sys
import statistics

ppl = {}
for i in range(1000000):
    ppl[i] = 0

lim = int(sys.argv[1])
S = [0]
for k in range(1,56):
    S.append((100003 - 200003*k + 300007 *k**3) % 1000000)

for k in range(56, 2*lim+1):
    S.append((S[k-24] + S[k-55]) % 1000000)

pCaller = 0
pCalled = 0
callerLst = []
for n in range(1, lim+1):
    #callerLst.append(S[2*n])
    ppl[S[2*n]] += 1
    #ppl[S[2*n-1]] += 1
    if S[2*n-1] == S[2*n]:
        print("misdial n: {}".format(n))

    if S[2*n-1] == 524287:
        pCaller += 1
    if S[2*n] == 524287:
        pCalled += 1
    #print("{}\t{}\t{}".format(n, S[2*n-1], S[2*n]))

print("1er caller: {}".format(pCaller))
print("1er called: {}".format(pCalled))
m = 0
for p in ppl:
    m = max(m, ppl[p])
occ = list(ppl.values())
print(m)
print(max(occ))
print(statistics.mean(occ))
print(sum(occ)/len(occ))
print(statistics.median(occ))
