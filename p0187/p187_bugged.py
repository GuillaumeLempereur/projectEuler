# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 09:59:59 2024

@author: lempereu
"""


def perm(n):
	if n == 1:
		return 1
	return n*perm(n-1)

"""
0A1x

x _rest:
13*perm(4)


"""

tot = "0123456789abcdef"
rst = "23456789bcdef"

#01Ar
print(13*perm(4))

#01A0, 01A1, 01AA
print(3*perm(4)/2)

tot4 = 13*perm(4) + 3*perm(4)//2

print(tot4)

cc = 0
chex = 0
for a in tot:
	for b in tot:
		for c in tot:
			for d in tot:
				chex += 1
				n = a+b+c+d
				if "1" in n and "0" in n and "a" in n:
					"""
					if len(n.replace("1","").replace("0","").replace("a","")) > 0:
						cc += 1
					"""

					#if len(n.replace("1","").replace("0","").replace("a","")) == 0:
					cc += 1

print("chex:", chex)
print(cc)

cc = 0
lim = 16**4
chex = 0
for i in range(lim):
	chex += 1
	n = hex(i)[2:]
	if "1" in n and "0" in n and "a" in n:
		cc += 1
print(cc)
print("chex:", chex)
	