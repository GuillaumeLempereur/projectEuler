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

def norm(v):
    return math.sqrt(v[0]**2+v[1]**2)

a = 399
b = 455
c = 511
# p + q + r = 784

beta = math.acos((a**2+c**2-b**2)/2/a/c)

A = np.array([0,0])
B = np.array([c,0])
C = np.array([c-a*math.cos(beta),a*math.sin(beta)])
O = np.array([c/2,-math.sqrt(3)/2*c])
N = np.array([c-a*math.cos(beta+math.pi/3),a*math.sin(beta+math.pi/3)])



#Tx = a*c*math.cos(beta)-c**2/2+a**2*cos
AN = N-A
CO = O-C

x = AN[0]*(C[1]*CO[0]-CO[1]*C[0])/(AN[1]*CO[0]-AN[0]*CO[1])

y = CO[1]*(AN[0]*C[1]-AN[1]*C[0])/(AN[1]*CO[0]-CO[1]*AN[0]) + C[1]

y = AN[1]*(CO[0]*C[1]-CO[1]*C[0])/(AN[1]*CO[0]-CO[1]*AN[0])
#print(x,y)

T = np.array([x,y])

AT = T-A
CT = T-C
BT = T-B
print(norm(AT))

print(C[1]*CO[0]-CO[1]*C[0])
print(a*c/2*(math.sin(beta)-math.sqrt(3)*math.cos(beta))+math.sqrt(3)/2*c*c)

print(CO)
print(C)

print(a*math.cos(beta))
print(a*math.sin(beta))

print(AN[1]*CO[0]-AN[0]*CO[1])
print(math.sqrt(3)/2*(a**2+c**2+a*c*(math.sqrt(3)*math.sin(beta)-math.cos(beta))))

print(x/AN[0])
print(y/AN[1])

print((AN[0]**2+AN[1]**2)*(a*c/2*(math.sin(beta)-math.sqrt(3)*math.cos(beta))+math.sqrt(3)/2*c*c)**2/3/(b*b/2+a*c*(math.sqrt(3)/2*math.sin(beta)+math.cos(beta)/2))**2)
print((AN[0]**2+AN[1]**2)*(a*c/2*(math.sin(beta)-math.sqrt(3)*math.cos(beta))+math.sqrt(3)/2*c*c)**2/3/(b*b/2+a*c*(math.sqrt(3)/2*math.sin(beta)+math.cos(beta)/2))**2)
print(x**2+y**2)

print((c**2+a**2-2*a*c*math.cos(beta+math.pi/3))*(a*c/2*(math.sin(beta)-math.sqrt(3)*math.cos(beta))+math.sqrt(3)/2*c*c)**2/3/(b*b/2+a*c*(math.sqrt(3)/2*math.sin(beta)+math.cos(beta)/2))**2)

print(((b**2+2*a*c*math.cos(beta-math.pi/3))*(math.sqrt(3)/2*c**2-a*c/2*math.cos(beta+math.pi/6))**2)/(math.sqrt(3)/2*(a**2+b**2-a*c*math.cos(beta+math.pi/3)))**2)

print("Num")
print((c**2+a**2-2*a*c*math.cos(beta+math.pi/3))*(a*c/2*(math.sin(beta)-math.sqrt(3)*math.cos(beta))+math.sqrt(3)/2*c*c)**2)

print(((b**2+2*a*c*math.cos(beta-math.pi/3))*(math.sqrt(3)/2*c**2-a*c/2*math.cos(beta+math.pi/6))**2))

#print(((c**2+a**2-2*a*c*math.cos(beta+math.pi/3))*c**2*(-a/2*math.sin(math.pi/3-beta)+math.sqrt(3)/2*c)**2)/(3*(b**2/2+a*c/2*(math.sqrt(3)*math.sin(beta)+math.cos(beta)))))


# DEBUG
print("DEBUG")
print(c**2+a**2-2*a*c*math.cos(beta+math.pi/3))
print(b**2+2*a*c*math.cos(beta-math.pi/3))

print((math.sqrt(3)/2*c**2-a*c*math.cos(beta+math.pi/6))**2)
print((a*c/2*(math.sin(beta)-math.sqrt(3)*math.cos(beta))+math.sqrt(3)/2*c*c)**2)

print(3*(b*b/2+a*c*(math.sqrt(3)/2*math.sin(beta)-math.cos(beta)/2))**2)
print((math.sqrt(3)*((a**2+b**2)/2-a*c*math.cos(beta+math.pi/3)))**2)

print((b**2+2*a*c*math.cos(beta-math.pi/3))*(math.sqrt(3)/2*c**2-a*c*math.cos(beta+math.pi/6))**2/3/(b*b/2+a*c*(math.sqrt(3)/2*math.sin(beta)+math.cos(beta)/2))**2)

print(4/3*(math.sqrt(3)/2*c**2-a*c*math.cos(beta+math.pi/6))**2/(b*b+2*a*c*math.cos(beta-math.pi/3)))
print((math.sqrt(3)*c**2-2*a*c*math.cos(beta+math.pi/6))**2/3/(b*b+2*a*c*math.cos(beta-math.pi/3)))

m = (math.sqrt(3)*c**2-2*a*c*math.cos(beta+math.pi/6))
n = (b*b+2*a*c*math.cos(beta-math.pi/3))

print((math.sqrt(3)*c**2-a*c*(math.sqrt(3)*math.cos(beta)-math.sin(beta)))**2/3/(b*b+a*c*(math.cos(beta)+math.sqrt(3)*math.sin(beta))))

S = (a+b-c)*(a+c-b)*(b+c-a)*(a+b+c)
print((math.sqrt(3)*(c**2-a**2+b**2)+math.sqrt(S))**2/6/(b**2+a**2+c**2+math.sqrt(3)*math.sqrt(S)))
# DEBUG

# Solving:
print("Solving")

sq = [i*i for i in range(1,100000)]

s = 0
lim = 100
ss = 0
for c in range(1,lim):
    for b in range(1,c+1):
        for a in range(c-b+1,b+1):
            #print(a,b,c,(a ** 2 + c ** 2 - b ** 2) / 2 / a / c)
            ss += 1
            beta = math.acos((a ** 2 + c ** 2 - b ** 2) / 2 / a / c)
            pqr = math.sqrt(c**2+a**2-2*a*c*math.cos(beta+math.pi/3))
            if pqr > 120000:
                break

            s += 1
            S = (a + b - c) * (a + c - b) * (b + c - a) * (a + b + c) # PB with 7 13 15
            if S%3==0 and S//3 in sq and ((round(math.sqrt(S//3))+(c**2-a**2+b**2))**2*3)%(6*(b**2+a**2+c**2+round(math.sqrt(3*S)))) == 0:
                #print(a,b,c,c**2-a**2+b**2/3,4*a**2*c**2-(a**2+c**2-b**2)**2,b**2-(a-c)**2,(a+c)**2-b**2,a+b-c,a+c-b,b+c-a,a+b+c)
                print(a, b, c,(a**2+b**2+c**2+round(math.sqrt(S*3)))/2,(math.sqrt(3)*(c**2-a**2+b**2)+math.sqrt(S))**2, math.sqrt(3*S), math.sqrt(6*(a**2+b**2+c**2+math.sqrt(3*S))),6*(a**2+b**2+c**2+math.sqrt(3*S)), c ** 2 - a ** 2 + b ** 2 / 3, 4 * a ** 2 * c ** 2 - (a ** 2 + c ** 2 - b ** 2) ** 2,
                      b ** 2 - (a - c) ** 2, (a + c) ** 2 - b ** 2, a + b - c, a + c - b, b + c - a, a + b + c)
                #print(9*(c**2-a**2+b**2)**2+3*(4*a**2*c**2-(a**2+c**2-b**2)**2),6*(a**2+b**2+c**2)*(c**2-a**2+b**2))
                #print((3*()))
                #if 9*(c**2-a**2+b**2)**2+3*(4*a**2*c**2-(a**2+c**2-b**2)**2) != 6*(a**2+b**2+c**2)*(c**2-a**2+b**2):



print(s,ss)

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