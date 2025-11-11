# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 09:59:59 2024

@author: lempereu
"""


"""
primes5e7 = [2, 3, …

def howmany(n):
a, b = 0, min(n,len(primes5e7)
while a != b:
c = (a+b)//2
if primes5e7[c] > n:
a = c
else:
b = c
return c+1

cc = 0
for p in primes5e7:
n = 10**8//p
if n < p:
break
cc += Bowman(n)

print(cc)


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
print(13*(perm(4)-perm(3))) # all permut startign by 0

#001A
2*perm(3)//perm(2)

#011A
perm(4)//perm(2) - perm(3)//perm(2) # all - permut starting by 0

#01AA
perm(4)//perm(2) - perm(3)//perm(2) 

print(perm(4)//perm(2) - perm(3)//perm(2) + perm(4)//perm(2) - perm(3)//perm(2) + 2*perm(3)//perm(2))
"""
#01A0, 01A1, 01AA
print(3*perm(4)/2)
"""

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
					
					if len(n.replace("1","").replace("0","").replace("a","")) > 0 and  n[0] == "0":
						cc += 1
					

					#if len(n.replace("1","").replace("0","").replace("a","")) == 0:
					#if n[0] != "0":
					#	cc += 1

print("chex:", chex)
print(cc)


"""
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
"""
	