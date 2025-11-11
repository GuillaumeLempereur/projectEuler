"""
p195

it works but it should be otpimized
optimize the search for divisors u of 48*a*a

if a odd => u must be multiple of 4 => l48 = [4, 12]
if a is even => at least u multiple of 8 => but can't say more
Hypothesis: also l48 in case of a pair

u > 4*a*(3**0.5) and u multiple of 4

prime solution:
    u = 3**(odd) * p ** pair
    u = p ** pair
otherwise => combination

check the inner radius below lim:
    the higher u and a, the higher r

prime solution: u is 4 * p**(2*x), 12 * p**(2*x)

u = 4 * div(a²) or 12 * div(a²)
case u = 4 * div_a:
    div_a > a*3**.5 => >= a/2
case u = 12 * div_a
    div_a > a/3**.5 => > a/2

gcd = 1 -> div a must have pair prime
if a%3 == 0: prime solution are u without 3 or with at least 3**3

the list of div is the combination of the square of its f**fs[f]

c*c = a*a + b*b - a*b
1*a*a -1*a*b + 1*b*b - c*c = 0
A = 1, C = 1, B = -1, F = -c*c
ex:
7*7 = 3*3 + 8*8 - 3*8
a, b, c = 3, 8, 7

try to solve: 4c²-3a² - n² = 0
ex: 4*7²-3*3² = 13²
ex: 4*7²- 1*13² - 3*3² = 0

100	1234 => ok
1000 22767 => ok
10000 359912 => ok (prim sol 60398)

A, B, C, D, E, F = 4, 0, -1, 0, 0, -27
case : F ≠ 0 and B2 - 4AC = k² => k = 4
u list : divisors of -4*A*F

try every u to find (c, n)

c*c = a*a + b*b - a*b <=> b*b - a*b + a*a - c*c = 0
delta = a*a - 4*(a*a-c*c) = 4*c*c - 3*a*a
b = (-a +/- detla**0.5)/2
"""
import sys
sys.path.insert(1, '..')
import Euler

#combine all prime factors
def combNoR(v, out):
    lst = []
    #s start item
    #t nb of item to take
    def combNoR_(ix, n):
        for i in range(ix, len(v)):
            n *= v[i]
            out.append(n)
            combNoR_(i+1, n)
            n //= v[i]
    combNoR_(0, 1)

lim=1053779
#lim = int(sys.argv[1])

primes = Euler.primesbelow(5*lim)
lstF = {}

def factorize(n):
    if n in lstF:
        return lstF[n].copy()
    for p in primes:
        if n%p == 0:
            lf = factorize(n//p)
            if p in lf:
                lf[p] += 1
            else:
                lf[p] = 1
            return lf.copy()

for p in primes:
    lstF[p] = {p: 1}

se = set()
cnt = 0
for a in range(2, 5*lim):
    F = -3*a*a
    fs = factorize(a)
    l = []

    if 2 in fs:
        f2 = fs[2]*2
        del fs[2]
        div_a = [f**(2*fs[f]) for f in fs]
        combNoR(div_a, l)
        l = [16 * d for d in l] + [48 * d for d in l] + [2**f2 * d for d in l] + [3*2**f2 * d for d in l]

        l += [2**f2, 3*2**f2]
    else:
        div_a = [f**(2*fs[f]) for f in fs]
        combNoR(div_a, l)
        l = [4 * d for d in l] + [12 * d for d in l]

    for u in l:
        if (u + 16*F//u) % 8 != 0:
            continue
        y = (u + 16*F//u)//8
        if y <= 0:
            continue

        if (u - 4*y) % 8 != 0:
            continue
        x = (u - 4*y) // 8
        if x <= 0:
            continue
        c, n = x, y
        if c == a:
            continue
        b = (a + n)//2
        s = (a+b+c)/2
        r = ((s-a)*(s-b)*(s-c)/s)**0.5
        gcd = Euler.gcd(a,Euler.gcd(b,c))
        abc = sorted([a,b,c])
        if r < lim and gcd == 1:
            cnt += 1
            se.add((abc[0], abc[1], abc[2]))

cnt = 0
for l in sorted(list(se)):
    (a, b, c) = l
    s = (a+b+c)/2
    r = ((s-a)*(s-b)*(s-c)/s)**0.5
    cnt += int(lim/r)
print("prime sol: {} sol: {}".format(len(se), cnt))

