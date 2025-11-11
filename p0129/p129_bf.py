#Problem 129
"""
Repunit divisibility
"""

import Euler

"""
n not multiple of 2 and 5
There exist k such that R(k) is divisible by n

ie: n = 7
R(6) = 111111
R(6) = 7 * 15873 => k = 6
A(7) is 6 cause 7 is not divisible for R(1 to 5)

A(n) the least value of k

A(7) = 6 => 111111 divisible by 7
A(41) = 5 => 11111 divisible by 41

n is surely prime
"""

def R(n):
    s = "1"*n
    return int(s)

"""
for n in range(100):
    if n%2 == 0 or n%5 == 0:
        continue

    e = 1
    for i in range(10000):
        e = e *10 +1
        if e%n == 0:
            #if i>9000:
            print(n,i,e)
            break


"""


# List first 37 A(x)
A = {}

def R(n):
    s = "1"*n

    return int(s)

for i in range(1,37):
    ri = R(i)

    for p in Euler.primefactors(ri):
        if p not in A:
            A[p] = i

    #print(i, Euler.primefactors(ri))

for k in A:
    print(A[k],k,Euler.primefactors(R(A[k])))
    
"""

#Idea: enumerate for k and found the n divider

n = list(range(3,20,2))
print(n)

#for i in n:
while n:
    print("-" * 5, "Iteration", "-" * 5)
    i = n.pop(0)
    print(i)
    if i%5==0:
        continue
    print(n)

    ex = False
    for k in range(2,37):
        ri = R(k)

        for f in Euler.primefactors(ri): # may combine the dividers like 3, 3 => 3*3=9
            if f in n:
                n.remove(f)
                print(k,f)
            if f == i:
                ex = True
                print(k, f)
        if ex:
            break
    if not ex:
        print("Problem")

"""