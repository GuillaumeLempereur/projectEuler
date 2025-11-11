"""
Problem 139

a,b,c the length of the triangle

a+b+c is less than 10**8
b > a
c is the hypotenuse => a and b < c
a**2 + b**2 = c**2

we want n*(b-a) = c (b-a multiple of c)
"""

import Euler
import time

# Euclide's formula: list all unit pythagorian triples

# a = (m**2-n**2), b = 2*m*n, c = (m**2+n**2)
# m>n , m , n are coprime


start = time.time()
p = 0
for m in range(1,5000,2):
    for n in range(2,m):
        if Euler.gcd(m,n) != 1:
            continue

        c = m*m+n*n
        b = m*m-n*n
        a = 2*m*n
        if b < a:
            a, b = b, a

        #print(a,b,c)
        p += 1
        #print(m,n)

end = time.time()
print(end-start)

print(p)