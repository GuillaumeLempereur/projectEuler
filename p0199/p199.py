"""
p199
"""

def rec(k1, k2, k3, depth):
    k4 = k1+k2+k3+2*(k1*k2+k2*k3+k1*k3)**.5
    #print("{}{}\t{}\t{}\t{}".format("\t"*depth,1/k1, 1/k2, 1/k3, 1/k4))
    r = 1/k4/k4 #pi*r² = pi/k² aire of circle
    if depth == 11:
        return r
    return r + rec(k1, k2, k4, depth+1) + rec(k2, k3, k4, depth+1) + rec(k1, k3, k4, depth+1)


k0 = -1
k1 = 1/(2*3**.5-3)
r = 3/k1/k1 + 3*rec(k0, k1, k1, 2) + rec(k1, k1, k1, 2)
print(round(1-r, 8))
