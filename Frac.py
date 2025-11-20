#Frac

import Euler

class Frac:
    n = 0
    d = 1

    def __init__(self, num, den):
        self.n = num
        self.d = den

    def __sub__(self, other):
        new_n = self.n * other.d - self.d * other.n
        new_d = self.d * other.d

        cd = Euler.gcd(new_n,new_d)

        return Frac(new_n//cd,new_d//cd)

    def __add__(self, other):
        new_n = self.n * other.d + self.d * other.n
        new_d = self.d * other.d

        cd = Euler.gcd(new_n,new_d)

        return Frac(new_n//cd,new_d//cd)

    def __float__(self):
        return self.n/self.d

    def __str__(self):
        return str(self.n) + '/' + str(self.d)
