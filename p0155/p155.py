"""
P155 Capacitor combination
"""
import fractions

# The idea is to combine 2 and 3
n = 18
val = [set() for i in range(n+1)]
val[1] = set([fractions.Fraction(1)])
for i in range(2,n+1):
    for k in range(i//2):
        for c1 in val[k+1]:
            for c2 in val[i-k-1]:
                val[i].add(c1+c2)
                val[i].add(c1*c2/(c1+c2))

s = set()
for i in range(n+1):
    s = s | val[i]
    print(i,len(s))
