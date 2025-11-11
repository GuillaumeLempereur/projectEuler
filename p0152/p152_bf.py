#Problem 152
"""
Writing 1/2 as a sum of inverse squares

idea: recursive function, take it or pass to the next with check if still possible

Need to remove the cases where it's almost 1/2: should compute cs perfectly

"""


import Euler
import time
start = time.time()

# before Frac
# 30 => 4.5s, 31: 8.73s, 32: 16.22s,... 35: 107.4s no answer
# after Frac
# 30 => 18s


lim = 30
revcumsum = [0]*(lim+1)
revcumsum[lim] = 1/(lim**2)

for i in reversed(range(2,lim)):
    revcumsum[i] = revcumsum[i+1]+1/(i**2)

class Frac:
    n = 0
    d = 1

    def __init__(self, num, den):
        self.n = num
        self.d = den

    def __add__(self, other):
        new_n = self.n * other.d + self.d * other.n
        new_d = self.d * other.d

        cd = Euler.gcd(new_n,new_d)

        return Frac(new_n//cd,new_d//cd)

    def __float__(self):
        return self.n/self.d

    def __str__(self):
        return str(self.n) + '/' + str(self.d)

print(revcumsum)
# lf: list of frac for generating 1/2
# cs: current sum, sum of the lf
# n: the new frac (1/n) to append to the list or not
def genHalf(lf, cs, n):
    #print(lf)
    if n > lim or 1/2 - float(cs) > revcumsum[n]:
        return # impossible to achieve 1/2

    if cs.n==1 and cs.d == 2: # may be should put a tol
        print(cs, lf)
        return

    genHalf(lf[:], cs, n + 1)
    if float(cs) + 1/(n**2) <= 1/2:
        genHalf(lf[:]+ [1/(n**2)],cs + Frac(1,n**2), n + 1)

genHalf([],Frac(0,1),2)

end = time.time()
print(end-start)