#p151

"""
(1, 0, 0, 0) Prob having A2 in turn 8:
52271 / 864000

3*(52271/864000*7/36*1/2)
+ 2*
"""


import math

class Frac:
    n = 0
    d = 1

    def __init__(self, n, d):
        self.n = n
        self.d = d

    def __add__(self, a):
        dd = self.d * a.d
        nn = self.n*a.d + self.d*a.n

        gcd = math.gcd(nn, dd)
        nn //= gcd
        dd //= gcd
        return Frac(nn, dd)

    def __mul__(self, a):
        dd = self.d*a.d
        nn = self.n*a.n

        if nn ==0:
            return Frac(0,1)
        gcd = math.gcd(nn, dd)
        nn //= gcd
        dd //= gcd
        return Frac(nn, dd)


    def __str__(self):
        return "{} / {}".format(self.n,self.d)

d = {}

nbOStot = Frac(0,1)

def pick(turn, hand, prob, nbOS):
    global nbOStot
    a2, a3, a4, a5 = hand[0], hand[1], hand[2], hand[3]
    ss = a2+a3+a4+a5
    if ss == 1:
        nbOS += 1

    if turn == 14:
        nbOStot += prob * Frac(nbOS, 1)
        if hand in d:
            d[hand] += prob
        else:
            d[hand] = prob
        return

    if a2 > 0:
        pick(turn +1, (a2-1, a3+1, a4+1, a5+1), prob*Frac(a2,ss), nbOS)
    if a3 >0:
        pick(turn +1, (a2, a3-1, a4+1, a5+1), prob*Frac(a3,ss), nbOS)
    if a4 >0:
        pick(turn +1, (a2, a3, a4-1, a5+1), prob*Frac(a4,ss), nbOS)
    if a5 >0:
        pick(turn +1, (a2, a3, a4, a5-1), prob*Frac(a5,ss), nbOS)



#pick(1, (1,1,1,1), Frac(1,1))
#pick(8, (1,0, 0, 0), Frac(1,1))
#pick(12, (0,1, 0, 0), Frac(1,1))
#pick(12, (0,1, 0, 0), Frac(1,1))

pick(1, (1,1,1,1), Frac(1,1), 0)
#print(d)

sss = Frac(0,1)
for h in d:
    print(h)
    print(d[h])
    print()
    sss += d[h]

print("Total")
print(sss)

print()
print(nbOStot)
