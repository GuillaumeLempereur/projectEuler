import Euler
import time

"""
n2+1, n2+3, n2+7, n2+9, n2+13, and n2+27

for n below 10**6 => count = 1242490
Takes 52s

if n is multiple of 5 => should be OK
taking multiple of 10 => 17.5s 

1*10**7 => 20s


"""


start = time.time()
count = 0
lim = 150000000
for n in range(10,lim,10): # (2,lim,2)
    ok = True
    if n%3==0 or n%7==0 or n%13==0: #  or (n*n+1) % 5 == 0 or (n*n+3) % 5 == 0
        continue

    for a in [1,3,7,9,13,27]:
        if not Euler.isprime(n*n+a):
            ok = False
            break

    if not ok:
        continue

    for a in [5,11,15,17,19,21,23,25]:
        if Euler.isprime(n*n+a):
            ok = False
            break

    if ok:
        count += n
        print(n)

end = time.time()
print(end-start)

print(count)