import Euler

print(Euler.factorization(72))
print(Euler.primefactors(72))

lim = 100
for n in range(1, lim):
    c = 0
    for d in range(1, n+1):
        if n % d == 0:
            c += 1
    fs = Euler.factorization(n)
    k = 1
    for f in fs:
        k *= (fs[f]+1)
    if k != c:
        print(n)

i = 0
c = 1
for j in range(16):
    i += c
    c*=2
    if c>16:
        c = 1
    print(bin(i))
