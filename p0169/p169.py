"""
p169

f(0) = 0, f(1) = 1, f(2) = 2

"""
import sys

cache = {}
from functools import lru_cache

@lru_cache(maxsize=None)
def rec2(n):
    if n <= 2:
        return n # 1: 1, 2, 2
    if n%2 == 1: # n odd
        return rec2(n//2)
    else: # n even
        return rec2(n//2) + rec2(n//2-1)

"""
lim = 10
for n in range(1,2**lim+1):
    print("{}\t{}".format(n, rec2(n)))
def f_m(n):
    if n == 4:
        return 5
    if n == 5:
        return 8
    return f_m(n-1) + f_m(n-2)
"""
n = int(sys.argv[1])
n = 10**n
print(rec2(n))
