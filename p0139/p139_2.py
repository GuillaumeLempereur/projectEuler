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
"""

import Euler
import time

# Euclide's formula: list all unit pythagorian triples

# a = (m**2-n**2), b = 2*m*n, c = (m**2+n**2)
# m>n , m , n are coprime


start = time.time()
count = 0
lim = 7071
print(10**8-1)
for m in range(1,lim+1,2): # m impair
    for n in range(2,m,2):
        if Euler.gcd(m,n) != 1 or (m+n)%2==0:
            continue

        c = m*m+n*n
        b = m*m-n*n
        a = 2*m*n
        if b < a:
            a, b = b, a
        p = a + b + c
        if p >= 10**8:
            break

        if c%(b-a) == 0:
            count += (10**8-1)//p

        #print(a,b,c)

        #print(m,n)
#print("-"*10)


for m in range(2,lim,2): # m pair
    for n in range(1,m,2):
        if Euler.gcd(m,n) != 1:
            continue

        c = m*m+n*n
        b = m*m-n*n
        a = 2*m*n
        if b < a:
            a, b = b, a

        p = a + b + c
        if p >= 10 ** 8:
            break

        #print(a,b,c)
        if c%(b-a) == 0:
            count += (10**8-1)//p
        #print(m,n)



end = time.time()
print(end-start)

print(count)
