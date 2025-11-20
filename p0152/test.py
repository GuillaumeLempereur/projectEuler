#p152
#test

"""
#1/kx² = 1/2
LIM = 1 + 80
s = 0
#for i in reversed(range(2,LIM)):
for i in reversed(range(2,LIM)):
    s += 1/i/i
    print(1/i/i, s)

#1/kx² = 1/4

print()
s = 0
for i in reversed(range(3,LIM)):
    s += 1/i/i
    print(1/i/i, s)


# pick k = 2 and k = 4
#1/kx² = 3/16

print()
s = 0
for i in reversed(range(5,LIM)):
    s += 1/i/i
    print(1/i/i, s)

# pick k = 2 and k = 3
#1/kx² = 2/9

print()
s = 0
for i in reversed(range(4,LIM)):
    s += 1/i/i
    print(1/i/i, s)
print(5/36)
"""


"""
#number of k%n required to cancel the denominator n
# 3
n = 5
LIM = 10

for i in range(1,LIM):
    if i%n == 0:
        continue
    a = i*i*n*n
    for j in range(i+1,LIM):
        if j%n == 0:
            continue
        b = j*j*n*n
        if (a+b)%(n*n*n*n) == 0:
            print(2,a,b,i,j)
        for k in range(j+1,LIM):
            if k%n == 0:
                continue
            c = k*k*n*n
            if (a*b+b*c+a*c)%(n*n*n*n*n*n) == 0:
                print(3, a,b,c,i,j,k)
            for l in range(k+1,LIM):
                if l%n == 0:
                    continue
                d = l*l*n*n
                if (a*b*c+b*c*d+a*b*d+a*c*d)%(n*n*n*n*n*n*n*n) == 0:
                    print(4,a,b,c,d,i,j,k,l)
"""

import Frac as F
f1 = F.Frac(1, 5*5)
f2 = F.Frac(1, 35*35)
f3 = F.Frac(1, 25*25)
f4 = F.Frac(1, 35*35)
f5 = F.Frac(1, 40*40)
f6 = F.Frac(1, 36*36)
s = f1+f2
print(s)
print(s.d%5)

""" sum 1/k² => denominator % k != 0
5	15	20	35
7	28	35
3	12	15
2	4	12	20	28

2	4	6	10	20	28	36
3	6	9	36	45
10	20	35	45
7	28	35

2	4	6	12	28	30	36
3	6	9	12	15	30	36	45
15	30	35	45
7	28	35
"""
