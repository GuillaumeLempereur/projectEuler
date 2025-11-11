#Problem 143
"""
Investigating the Torricelli point of a triangle

a, b, c, p, q, r are integers

find sum of p+q+r when p+q+r <= 120000

AN = BM = CO = p + q + r
=> AN, BM, CO are integers


Seems that Beta is angle in pythagorean triangle cos(B) = p/q

Idea: compute ||CO|| and others should be integer ! 1st way to discredit some a,b,c values

limits: a,b or c can not be greater or equal to the sum of the 2 others
modulo 3 for a,b and c : allow 3 %3==0, 2 %3==1 and %3==0, 2 %3==2 and %3==0, 2 %3==1 and %3==2, 2 %3==2 and %3==1 ???

lim: 200 > 2.71s
ex: a = 399, b = 455, c = 511
"""

import math
import numpy as np
import Euler

def norm(v):
    return math.sqrt(v[0]**2+v[1]**2)

a = 399
b = 455
c = 511
# p + q + r = 784

lim = 100

sq = {}
for i in range(1,10000):
    sq[i*i] = i

############### TEST #######

Slst = []

cc = 0
for c in range(1,lim):
    for b in range(1,c+1):
        if Euler.gcd(c,b) > 1:
            continue
        for a in range(c-b+1,b+1):
            cc += 1

            S = (a + b - c) * (a + c - b) * (b + c - a) * (a + b + c)
            S_root = round(math.sqrt(3*S))
            if S % 3 == 0 and S // 3 and S_root*S_root == 3*S:


                t = a+b
                r = b-a

                if Euler.gcd(c,Euler.gcd(t,r)) == 1:
                    Slst.append(tuple(sorted([t, r, c,S])))
                print(math.sqrt(4*a*a*b*b-S),a, b, c, t*t-c*c, c*c-r*r, "|",t,r,c,S//3, S , (t-c)*(t+c)*(c-r)*(c+r), a + b - c, a + c - b, b + c - a, a + b + c)


exit(0)
print(cc)

for s in sorted(Slst):
    print(s)

exit(0)
############### TEST #######

# Solving:
print("Solving")

lim = 500
ss = 0

"""
nb_p = [0 for i in range(20)]
for n in range(1,100000):
    nbp = len(Euler.factorization(n))

    nb_p[nbp] += 1

for i in range(len(nb_p)):
    print(i,nb_p[i])

exit(0)
"""
print("a,b,c,S,S//3,sq[S//3]")
for c in range(1,lim):
    for b in range(1,c+1):
        if Euler.gcd(c,b) > 1:
            continue
        for a in range(c-b+1,b+1):
            #print(a,b,c,(a ** 2 + c ** 2 - b ** 2) / 2 / a / c)
            #"""
            beta = math.acos((a ** 2 + c ** 2 - b ** 2) / 2 / a / c)
            pqr = math.sqrt(c**2+a**2-2*a*c*math.cos(beta+math.pi/3))
            if pqr > 120000:
                break

            #"""
            # s += 1
    
            S = (a + b - c) * (a + c - b) * (b + c - a) * (a + b + c) # PB with 7 13 15
            ansqd = (a*a+b*b+c*c + round(math.sqrt(3*S)))
            if S%3==0 and S//3 in sq and ansqd%2 == 0 and ansqd//2 in sq: #and ((round(math.sqrt(S//3))+(c**2-a**2+b**2))**2*3)%(6*(b**2+a**2+c**2+round(math.sqrt(3*S)))) == 0:
                #print(a,b,c,c**2-a**2+b**2/3,4*a**2*c**2-(a**2+c**2-b**2)**2,b**2-(a-c)**2,(a+c)**2-b**2,a+b-c,a+c-b,b+c-a,a+b+c)
                #print(a, b, c,(a**2+b**2+c**2+round(math.sqrt(S*3)))/2,(math.sqrt(3)*(c**2-a**2+b**2)+math.sqrt(S))**2, math.sqrt(3*S), math.sqrt(6*(a**2+b**2+c**2+math.sqrt(3*S))),6*(a**2+b**2+c**2+math.sqrt(3*S)), c ** 2 - a ** 2 + b ** 2 / 3, 4 * a ** 2 * c ** 2 - (a ** 2 + c ** 2 - b ** 2) ** 2,
                #      b ** 2 - (a - c) ** 2, (a + c) ** 2 - b ** 2, a + b - c, a + c - b, b + c - a, a + b + c)
                #print(9*(c**2-a**2+b**2)**2+3*(4*a**2*c**2-(a**2+c**2-b**2)**2),6*(a**2+b**2+c**2)*(c**2-a**2+b**2))
                #print((3*()))
                #if 9*(c**2-a**2+b**2)**2+3*(4*a**2*c**2-(a**2+c**2-b**2)**2) != 6*(a**2+b**2+c**2)*(c**2-a**2+b**2):

                print(a,b,c,S,S//3,sq[S//3], len(Euler.factorization(S//3)))
                ss += 1


print(ss)

"""
print(norm(BT))
print(norm(CT))
print(norm(AN))
print(norm(CO))

print(CO[0]*(AN[1]*A[0]-A[1]*AN[0]))

print(np.dot(AN,AN))

print((CO[0]*C[1]-C[0]*CO[1]))
print((AN[1]*CO[0]-AN[0]*CO[1]))

print(3*a*c/2*(math.sqrt(3)*math.cos(beta)/2-math.sin(beta))-math.sqrt(3)*(a**2+c**2)/2)
"""