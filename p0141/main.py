import math

cc = 0

lim = 1000000 #1000000
for a in range(1,lim):
    q = 1
    while q*q<lim:
        cc += 1
        #sq = math.sqrt(ad**4-4*qd**3)

        q += 1

print(cc)
