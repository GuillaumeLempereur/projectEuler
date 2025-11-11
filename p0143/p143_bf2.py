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

lim = 150
import math
import time

def isSquare(n):
    if n < 0:
        return False
    s = math.sqrt(n)
    if int(s)**2 == n:
        return int(s)
    return False


a = 399*2
b = 455*2
c = 511*2


count = 0
"""
notmul3 = 0
tot = 0
"""
#2*a*a*b*b + 2*a*a*c*c+2*b*b*c*c-a**4-b**4-c**4

def mayBeTorricelli(a,b,c):
    global count #, notmul3, tot
    #tot += 1
    uglySqrt = (a+b+c)*(a+b-c)*(a-b+c)*(b+c-a)
    if uglySqrt%3 != 0:
        #notmul3 += 1
        #print("Not mul of 3")
        return False
    sqrt = isSquare(uglySqrt//3)
    if not sqrt:
        #print("Not sqrt 1")
        return
    sq2 = (a*a-b*b)**2+3*(sqrt+c*c)**2 # sqC

    sq_A = (c*c-b*b)**2 + 3*(sqrt+a*a)**2
    sq_B = (c*c-a*a)**2+3*(sqrt +b*b)**2
    #print("sq2",sq2)
    sq2 = isSquare(sq2)

    sq_A = isSquare(sq_A) # redondant !!!!
    sq_B = isSquare(sq_B)


    #print("sq2:",sq2)
    if not sq2 or sq2%(2*c) != 0: # or not sq_A or sq_A%(2*a) or not sq_B or sq_B%(2*b)
        #print("Not sqrt 2")
        return
	
    sum = sq2//(2*c)
    #print("Ok: ",sum)
    print(sum,(a+b+c),(a+b-c),(a-b+c),(b+c-a))
    count += 1

start_time = time.time()

for a in range(3,lim):
    for b in range(2,a):
        for c in range(1,b):
            mayBeTorricelli(a,b,c)

elapsed_time = time.time() - start_time

print("elapsed time:",elapsed_time)
print(count)
"""

print(notmul3,tot)
"""

"""

lim = 10

for c in range(1,lim):
    for b in range(1,c+1):
        for a in range(1,b+1):
            if isSquare(12*a**2*c**2-3*(c**2+a**2-b**2)**2) and (c**2+a**2-b**2+int(math.sqrt((12*a**2*c**2-3*(c**2+a**2-b**2)**2))))%2==0:
                print(a,b,c)

"""