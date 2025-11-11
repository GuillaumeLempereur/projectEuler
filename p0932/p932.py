import sympy
from sympy.solvers.diophantine.diophantine import base_solution_linear
from sympy.abc import t

"""
9801 bug !!!
"""

ss = set()

#4 9 11
f_l = [[9],
       [9, 11],
       [27, 37],
       [9, 11, 101],
       [9, 41, 271],
       [27, 7, 11, 13, 37],
       [9, 239, 4649],
       [9, 11, 73, 101, 137],
       [81, 37, 333667],
       [9, 11, 41, 271, 9091],
       [9, 21649, 513239],
       [27, 7, 11, 13, 37, 101, 9901],
       [9, 53, 79, 265371653],
       [9, 11, 239, 4649, 909091],
       [27, 31, 37, 41, 271, 2906161]]

c = 0
for fl in f_l:
	print(c)
	#combination
	ab = []
	for f1 in [1, 2, 4]:
		#f = 4*9*11
		f = 4*(10**(c+1)-1)
		factors = fl
		for n in range(2**len(factors)):
			nn = n
			a = f1
			for i in reversed(range(len(factors))):
				if nn%2:
					a *= factors[i]
					nn= nn>>1
					b = f//a
					ab.append((a,b))

