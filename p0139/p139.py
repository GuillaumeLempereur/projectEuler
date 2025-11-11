import time
import sys

def gcd(a,b):
    while b > 0:
        a, b = b, a%b
    return a

start = time.time()
count = 0
lim = 100 #nt(sys.argv[1])

print(lim)

for m in range(2,lim): # m impair & pair
    for n in range(1,m):
        if gcd(m,n) == 1 and (m+n)%2==1:

            c = m*m+n*n
            b = m*m-n*n
            a = 2*m*n

            p = a + b + c
            if p >= 10**8:
                break

            if b<a:
                t = a
                a =b
                b =  t

            if c%(b-a) == 0:
                count += (10**8-1)//p

end = time.time()
print(end-start)

print(count)
