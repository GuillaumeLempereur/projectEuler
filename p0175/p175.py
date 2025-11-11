"""
p175

f(0) = 0, f(1) = 1, f(2) = 2
f(n) = f(n//2) if n odd
f(n) = f(n//2) + f(n//2-1) if n even

f(n)/f(n-1) = 123456789/987654321
f(n)/f(n-1) = 13717421/109739369

f(n) = 13717421
f(n-1) = 109739369

hypothesis: n is odd

f(n) == f(n//2)
f(n-1) == f((n-1)//2) + f((n-1)//2-1)

f(x) + f(x+1) = 109739369       x = (n-1)//2

f_m(45) = 1836311903  =>   n ~= 2**45


"""
"""
Try:
f(n) = 13717421
f(n-1) = 109739369

hypothesis: n is odd
=> n = 2*a+1 & n-1 = 2*a

f(2*a+1) = 13717421
f(2*a) = 109739369

f(2*a) = f(a) + f(a-1) = 109739369
f(2*a+1) = f(a) = 13717421

f(a-1) = 109739369 - 13717421 = 96021948
f(a) = 13717421

if a odd:
    f(a) = f(a//2) = 13717421
    f(a-1) = f(a//2) + f(a//2-1) = 96021948

    13717421 + f(a//2-1) = 96021948
    f(a//2-1) = 96021948 - 13717421 = 82304527
else: #even
    f(a) = f(a//2) + f(a//2-1) = 13717421
    f(a-1) = f(a//2-1) = 96021948

    f(a//2) + 96021948 = 13717421
    f(a//2) = 13717421 - 96021948 = -82304527 => problem !!!!



f(n) == f(n//2)
f(n-1) == f((n-1)//2) + f((n-1)//2-1)

f(n) = 13717421
f(n-1) = 109739369

f(n//2) = f(n)
f(n-1) = f(n) + f(n//2-1)

f(n//2-1) = f(n-1) -f(n)
f(n//2) = f(n)

rec:

until n is even!!

recurssive algo: a always odd
list f(x) : x range(1,1000)
n?




"""
import sys

def rec2(n):
    if n <= 2:
        return n # 1: 1, 2, 2
    if n%2 == 1: # n odd
        return rec2(n//2)
    else: # n even
        return rec2(n//2) + rec2(n//2-1)

lim = 10
for n in range(1,2**lim+1):
    print("{}\t{}".format(n, rec2(n)))

def f_m(n):
    if n == 4:
        return 5
    if n == 5:
        return 8
    return f_m(n-1) + f_m(n-2)

n = int(sys.argv[1])

#print(rec2(n))

#print(f_m(n))


n_1 = 8
n_2 = 5
for i in range(n-5):
    n_1, n_2 = n_1 + n_2, n_1

print(n_1)

