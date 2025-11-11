"""
Problem 139

a,b,c the length of the triangle

a+b+c is less than 10**8
b > a
c is the hypotenuse => a and b < c
a**2 + b**2 = c**2

we want n*(b-a) = c (b-a multiple of c)

For lim = 5000 => 16s
For lim = 7080 every unit pythagorian triples are enumerated

Not 15086639 !!!!
10057761 ?
"""

import time
import sys

# Euclide's formula: list all unit pythagorian triples

# a = (m**2-n**2), b = 2*m*n, c = (m**2+n**2)
# m>n , m , n are coprime


def gcd(a,b):
    while b > 0:
        a, b = b, a%b
    return a

start = time.time()
count = 0
lim = int(sys.argv[1])
print(lim)
for m in range(2,lim): # m impair & pair
    for n in range(1,m):
        if gcd(m,n) == 1 and (m+n)%2==1:

            c = m*m+n*n
            b = m*m-n*n
            a = 2*m*n

            #if b < a:
            #    a, b = b, a
            p = a + b + c
            if p >= 10**8:
                break

            if c%(b-a) == 0:
                count += 1 #(10**8-1)//p

end = time.time()
print(end-start)

print(count)
