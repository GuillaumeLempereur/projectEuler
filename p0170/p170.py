"""
p170

case 2 numbers:

p1 = n * a
p2 = n * b

p1 & p2 = panda_1
n & a & b = panda_2

find max panda_1
panda_x is 10 digits with every digits.

p1 = n * a
p2 = n * b
p1&p2 = 9xxx
p1 = 9xxx

start from panda_2 split in 3 (n, a and b) then pick the one having the max p1&p2
"""

mmax = 0

def rec(l, n):
    global c, d, cc, mmax
    if len(l) == 0:
        #print(n)
        #check
        for b_s in range(1,9):
            b = n % (10**b_s)
            if b == 0:
                continue

            nn = n // (10**b_s)
            if b // (10**(b_s-1)) == 0:
                continue
            for a_s in range(1,10-b_s):
                a = nn % (10**a_s)
                if a == 0:
                    continue
                if a // (10**(a_s-1)) == 0:
                    continue
                nnn = nn //(10**a_s)

                p1 = nnn*a
                p2 = nnn*b

                n2c = str(p1)+str(p2)
                if len(n2c) != 10:
                    continue
                nbD = {"0":0, "1":0, "2":0, "3":0, "4":0, "5":0, "6":0, "7":0, "8":0, "9":0}
                skp = False
                for dig in n2c:
                    nbD[dig] += 1
                    if nbD[dig] > 1:
                        skp = True
                        break
                if skp:
                    continue
                cc +=1
                if int(n2c) > mmax:
                    mmax = int(n2c)
                    print("{} = {} & {}\t{}\t{}\t{}".format(n2c, p1, p2, nnn, a, b))
        c += 1
        return
    n *= 10
    for i in range(len(l)):
        n += l[i]
        rec(l[:i] + l[i+1:], n)
        n -= l[i]

for d in range(1,10):
    c = 0
    cc = 0
    l = list(range(d)) + list(range(d+1,10))
    rec(l, d)
    print("{}/9".format(d))
print("ans: {}".format(mmax))
