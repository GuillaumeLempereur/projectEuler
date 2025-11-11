
import sys
import Euler


lim = 2500
size = 2500
l = [[] for i in range(size)]

for x in range(1,lim):
    for r in range(1,x):
        n = x*(4*r-x)
        #print(n)
        if n > 0 and n < size:
            l[n].append((x,r,x*(4*r-x)))

for n in l:
    if len(n) == 1:
        print(n[0])

exit(0)

for i in range(16,len(l)):
    #if((i%4==2 or i%4==1) and len(l[i]) > 0):
    """
    if i%4 == 3:
        print(i)
        for h in l[i]:
            (x, r, s) = h
            a = (x*(4*r-x)+1)//4
            print("\t",i,a,h,4*r*r-4*a+1)
    """
    a = (i)//4
    if i%4 == 0 and (a%4 == 1 or a%4 == 3) : # and Euler.isprime(a//4): #and len(Euler.factorization(i)) == 1: # and (i//4)%4==0:
        #fact = Euler.factorization(i)
        #for f,e in fact.items():
            #e = 0
            #print(i,a,e,l[i])

        """
        v = a
        while v%4 == 0:
            v //= 4
        """

        if not Euler.isprime(a):
            print(i,a,a//4,l[i])


        """
        for h in l[i]:
            (x, r, s) = h
            a = (x*(4*r-x))//4
            print("\t",i,a,h,r*r-a)
        """


exit(0)

v = 0
print(v)
for r in range(1,4083):
    for d in range(1,r//2): # max d should be r/2 to avoid impossible solution
        a = r*r-d*d

        if 2*round(math.sqrt(r*r-a)) < r: # 2 solution
            nl[a] += 2 # to reject
        else: # 1 solution
            nl[a] += 1 # OK


    a = r*r #double solution


print(v)


exit(0)

def reject(nl,n,lim):
    i = 2
    while(i*i*n<lim):
        nl[i*i*n] = 0
        i += 1

lim2 = 100

nl = [1]*lim2

for e in range(1,lim2):
    if nl[n] == 0:
        continue # more than 1 solution

    if n%4==3 or n%4 == 2:
        #nl[n] = 0
        #reject(nl,n,lim2)
        continue

    if Euler.isprime(n):
        nl[n] = 0
        #reject(nl,n,lim2)
        continue

    if n%4 == 0:
        a=0#delta = 2*(r*r-a)


    print(n," need to compute its dividers")
