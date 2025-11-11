"""
p175

f(0) = 0, f(1) = 1, f(2) = 2
f(n) = f(n//2) if n odd
f(n) = f(n//2) + f(n//2-1) if n even

f(n)/f(n-1) = 123456789/987654321
f(n)/f(n-1) = 13717421/109739369

f(n) = 13717421
f(n-1) = 109739369

hypothesis: n is odd

f(n) == f(n//2)
f(n-1) == f((n-1)//2) + f((n-1)//2-1)

f(x) + f(x+1) = 109739369       x = (n-1)//2

f_m(45) = 1836311903  =>   n ~= 2**45


f(n) == f(n//2)
f(n-1) == f((n-1)//2) + f((n-1)//2-1)

f(n) = 13717421
f(n-1) = 109739369

f(n//2) = f(n)
f(n-1) = f(n) + f(n//2-1)

f(n//2-1) = f(n-1) -f(n)
f(n//2) = f(n)

"""
import sys
"""
ex: n, n-1 13, 5
n = 52 ; n even
a = n//2 = 26
f(a-1) = 5 (f(25) = 5)
f(a) = 13-5 = 8  (f(26) = 8)

a, a-1 = 8, 5 => a even
b = a//2 = 13
f(b-1) = 5   f(12)
f(b) = 8-5 = 3   f(13)

b, b-1 = 3, 5 => odd
c = b//2 = 6
f(c) = f(b) = 3    f(6)
f(c-1) = 5 - 3 = 2    f(5)

c, c-1 = 3, 2 => even
d = c//2 = 3
f(d-1) = 2
f(d) = 3-2 = 1

d, d-1 = 1, 2 =>
d = 3 : 11
c       110
b       1101
a       11010
n       110100
"""

"""
f(n) = f(n//2) + f(n//2-1) even

f(n) = f(n//2) odd
f(n-1) = f(n//2) + f(n//2-1) : n odd
f(n-1) - f(n) = f(n//2-1)

f(n) = f(n//2) + f(n//2-1) even
f(n-1) = f(n//2-1)
f(n//2) = f(n) - f(n-1)

"""

lim = int(sys.argv[1])
n, n_1 = 13717421, 109739369
bits = []

for i in range(lim):
    #print("{}\t{}".format(n, n_1))
    if n_1 == 1: #n = 2**(n-1)
        print("quit")
        #bits.append(bin(2**(n-1))[2:][::-1])
        bits.append(bin(2**(n-1))[2:])
        print((n-1))
        break
    if n_1 > n: #n is odd
        n, n_1 = n, n_1 - n
        bits.append(1)
    else: # n is even
        n_1, n = n_1, n-n_1
        bits.append(0)
    #print("\t\t{}\t{}".format(n, n_1))
    if n == 1 and n_1 == 2:
        bits.append(1)
        bits.append(1)
        break
    if n == 2 and n_1 == 1:
        bits.append(0)
        bits.append(1)
        break
txt = ""

for b in reversed(bits):
    txt += str(b)

#print("{}\t{}".format(txt, int("0b"+txt, 2)))
print("{}\t{}".format(txt,""))
#ans: 1, n-1 zeros, end of txt
