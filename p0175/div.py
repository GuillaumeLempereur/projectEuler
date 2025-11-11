lim = 10
l = {}
def rec(n, d):
    if d == lim:
        if n in l:
            l[n] += 1
        else:
            l[n] = 1
        return
    rec(n,d+1)
    rec(n+2**d, d+1)
    rec(n+2*(2**d), d+1)

rec(0, 0)

#print(l)
"""
for n in range(1,2**lim+1):
    print("{}\t{}".format(n, l[n]))
"""
for n in range(1,2**lim):
    print("{}\t{}".format(n, l[n+1]/l[n]))
