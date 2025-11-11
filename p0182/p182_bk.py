# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 07:59:41 2024

@author: lempereu
"""
# P 182

"""
p, q = 19, 37 => 4 
p, q = 17, 19 => 11
p, q = 11, 23 => 3


best case always 9 unconcealed

23, 41 : 0, 1, 206, 368, 369, 574, 575, 737, 942
19, 37 : 0, 1, 37, 38, 75, 628, 665, 666, 702
11, 59 : 0, 1, 176, 177, 296, 353, 472, 473, 648
3, 53 : 0, 1, 52, 53, 54, 105, 106, 107, 158


ratio ?

0, 1, n-1
"""


import math

p = 1009
q = 3643
n = p*q

phi = (p-1)*(q-1)

print(phi)
print(n)


"""
cc = 0
for e in range(3, phi):
	if math.gcd(e,phi) == 1:
		cc += 1
	#print(e)
print(cc)


"""

print()

primes = [2, 3, 5]#, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43]

for p in primes:
	for q in primes:
		if p == q:
			continue

p = 19
q = 37
n = p*q

phi = (p-1)*(q-1)

blackList = []
es = []


cc = 0
for e in range(3, phi):
	if math.gcd(e,phi) == 1:
		if (3**e)%n == 3:
			#print("\t{}".format(e))
			blackList.append(e)
		else:
			es.append(e)
		#cc += 1
	#print(e)


"""
print(cc)
print("blackList")
print(blackList)
print("es")
print(es)
"""

"""
e= 977
cc = 0
for m in range(2, n):
	if (m**e)%n == m:
		#print("\t{}".format(e))
		cc += 1
	#print(e)
print(n)
print(cc)
"""

"""
r = {}
for e in es:
	cc = 0
	#w = []
	for m in range(1, n):
		if (m**e)%n == m:
			#print("\t{}".format(e))
			cc += 1
			#w.append(m)
		#print(e)
	if cc in r:
		r[cc] += 1
	else:
		r[cc] = 1

for i in r:
	print("{}\t{}".format(i, r[i]))
"""

"""
r = {}
for e in [5, 7, 11, 13, 17, 23, 25, 29]: #es
	cc = 0
	w = []
	for m in range(2, n):
		if (m**e)%n == m:
			#print("\t{}".format(e))
			cc += 1
			w.append(m)
		#print(e)
	r[e] = cc
	print("{}:".format(e))
	print(w)
for i in r:
	print("{}\t{}".format(i, r[i]))
"""

"""
r = {}
for e in es:
	cc = 0
	w = []
	for m in range(2, n):
		if (m**e)%n == m:
			#print("\t{}".format(e))
			cc += 1
			w.append(m)
		#print(e)
	r[e] = w[:]
	#print("{}:".format(e))
	#print(w)

for i in r:
	print("{}\t{}".format(i, r[i]))
"""

r = {}
for e in es:
	cc = 0
	for m in range(2, n):
		if (m**e)%n == m:
			#print("\t{}".format(e))
			cc += 1
		#print(e)
	if cc in r:
		r[cc] += 1
	else:
		r[cc] = 1
	#print("{}:".format(e))
	#print(w)

for i in r:
	print("{}\t{}".format(i, r[i]))


"""
e = 181

m = 55
print(phi)
print(n)

print((m**e)%n)

#print(math.gcd(181,phi))

"""
"""

print("#"*50)

for i in range(2,50):
	print("{}:\t{}\t{}".format(i, (i**60-1)%37, (i**120+i**60+1)%37))
	#print("{}:\t{}\t{}\t{}".format(i, (i**45-1)%37, (i**45+1)%37, (i**90+1)%37))
	
"""