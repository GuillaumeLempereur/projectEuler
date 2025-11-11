"""
p186
try to find rec

"""
import sys

lim = int(sys.argv[1])

def rec(n, d):
    print("{}\t{}".format(d, n))
    if d == 0:
        return
    rec(n+24, d-1)
    rec(n+55, d-1)

rec(0, lim)
