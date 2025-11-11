"""
p180

f1(n) = x**(n+1) + y**(n+1) - z**(n+1)
f2(n) = (x*y+y*z+w*x)*(x**(n-1)+y**(n-1)-z**(n-1))
f3(n) = x*y*z*(x**(n-2) + y**(n-2) - z**(n-2))


fn : (x**n + y**n - z**n)*(x+y+z) = 0
x, y, z = ax/bx, ay/by, az/bz
0 < a < b <= k = 35

look for (x**n + y**n - z**n) = 0
    x**n + y**n = z**n

n = 1: x + y = z
n = 2: Pythagore
n = 3: x**3 + y**3 = z**3 not possible, higher degree too

"""

import sys
sys.path.insert(1, '..')
import Euler

#order n
c = 0
s = set()
for n in [1, 2]: # only order 1 and 2
    for bx in range(1,36):
        for ax in range(1,bx):
            for by in range(1,36):
                for ay in range(1,by):
                    az_n = (ax**n*by**n+ay**n*bx**n)
                    az = round(az_n**(1/n))
                    bz = bx*by
                    if az**n == az_n and az < bz and bz//Euler.gcd(az, bz) <= 35:
                        s_a = ax*by*bz+ay*bx*bz+az*bx*by
                        s_b = bx*by*bz
                        d = Euler.gcd(s_a, s_b)
                        s_a //= d
                        s_b //= d
                        s.add((s_a, s_b))
                        #print("{}\t{}\t{}\t{}\t{}\t{}".format(ax,bx,ay,by,az,bz))
                        c += 1
for n in [1, 2]: # -1 and -2
    for bx in range(1,36):
        for ax in range(1,bx):
            for by in range(1,36):
                for ay in range(1,by):
                    bz_n = (ay**n*bx**n+ax**n*by**n)
                    bz = round(bz_n**(1/n))
                    az = ax*ay
                    if bz**n == bz_n and az < bz and bz//Euler.gcd(az, bz) <= 35:
                        s_a = ax*by*bz+ay*bx*bz+az*bx*by
                        s_b = bx*by*bz
                        d = Euler.gcd(s_a, s_b)
                        s_a //= d
                        s_b //= d
                        s.add((s_a, s_b))
                        #print("{}\t{}\t{}\t{}\t{}\t{}".format(ax,bx,ay,by,az,bz))
                        c += 1
t_a, t_b = 0, 1
for (a,b) in s:
    t_a = t_a*b + a*t_b
    t_b *= b
d = Euler.gcd(t_a, t_b)
t_a //= d
t_b //= d
print(t_a+t_b)
