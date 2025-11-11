"""
p186
bugged
S(n) using pascal triangle
"""
import sys
sys.path.insert(1, '..')
import Euler


#Pascal's method
Sp = [0]
for k in range(1,56):
    Sp.append((100003 - 200003*k + 300007 *k**3) % 1000000)

def S(n):
    r = 0
    nbSteps = (n-56)//24+1
    pascalTri = []
    Euler.pascalTriangle(pascalTri, 15)

    if n < 56:
        return Sp[n]

    for i in range(nbSteps+1):
        k = (n-(24*(nbSteps-i) + 55*i)) % 56
        if k == 0:
            k += 55
        print("{}\t{}".format(n, k))
        r += (pascalTri[nbSteps][i] * Sp[k])%1000000
    return r

#method 1
lim = int(sys.argv[1])

S1 = [0]
for k in range(1,56):
    S1.append((100003 - 200003*k + 300007 *k**3) % 1000000)

for k in range(56, lim+1):
    S1.append((S1[k-24] + S1[k-55]) % 1000000)

#check
for n in range(lim):
    if S(n) != S1[n]:
        print("{}\t{}\t{}".format(n, S(n), S1[n]))
