

import math
import Euler

lim = 1000000

for delta in range(1,lim):
    for rho_s in range(1,32): #delta):
        rho = rho_s**2
        d = delta**6
        r = rho**2
        if rho*delta**3+rho**2 >= lim:
            break

        alpha = rho + delta**3

        asq = rho*alpha
        a = 0

        rr = round(math.sqrt(asq))
        if rr**2 == asq:
            print(Euler.gcd(rho,delta), rho, delta , d, r, asq)
