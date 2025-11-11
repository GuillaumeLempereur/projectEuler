# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 10:12:54 2024

@author: lempereu
"""

#p158

"""
dic = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(len(dic))

#word = []
cc = 0
for x in range(len(dic)):
	a = dic[x]
	for y in range(len(dic)):
		if y == x:
			continue
		b = dic[y]
		for z in range(len(dic)):
			if z == x or z == y:
				continue
			c = dic[z]
			if a < b and b > c:
				cc += 1
			if a > b and b < c:
				cc += 1
#3 => 10400
print(cc)

dic = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(len(dic))

#word = []
cc = 0
for x in range(len(dic)):
	a = dic[x]
	for y in range(len(dic)):
		if y == x:
			continue
		b = dic[y]
		for z in range(len(dic)):
			if z == x or z == y:
				continue
			c = dic[z]
			for w in range(len(dic)):
				if w == x or w == y or w == z:
					continue
				d = dic[w]
				if a < b and b > c and c > d:
					cc += 1
				if a > b and b < c and c > d:
					cc += 1
				if a > b and b > c and c < d:
					cc += 1

print(cc)
#4 => 164450
"""

"""

dic = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(len(dic))

#word = []
cc = 0
for x in range(len(dic)):
	a = dic[x]
	for y in range(len(dic)):
		if y == x:
			continue
		b = dic[y]
		for z in range(len(dic)):
			if z == x or z == y:
				continue
			c = dic[z]
			for w in range(len(dic)):
				if w == x or w == y or w == z:
					continue
				d = dic[w]
				for v in range(len(dic)):
					if v == x or v == y or v == z or v == w:
						continue
					e = dic[v]
					if a < b and b > c and c > d and d > e:
						cc += 1
					if a > b and b < c and c > d and d > e:
						cc += 1
					if a > b and b > c and c < d and d > e:
						cc += 1
					if a > b and b > c and c < d and d < e:
						cc += 1

#5 => 1841840
print(cc)
"""

"""
1	2	3	4		1	1	1		3
1	2	4	3		1	1	0		2
1	3	2	4		1	0	1		2
1	3	4	2		1	1	0		2
1	4	2	3		1	0	1		2
1	4	3	2		1	0	0		1
2	1	3	4		0	1	1		2
2	1	4	3		0	1	0		1
2	3	1	4		1	0	1		2
2	3	4	1		1	1	0		2
2	4	1	3		1	0	1		2
2	4	3	1		1	0	0		1
3	1	2	4		0	1	1		2
3	1	4	2		0	1	0		1
3	2	1	4		0	0	1		1
3	2	4	1		0	1	0		1
3	4	1	2		1	0	1		2
3	4	2	1		1	0	0		1
4	1	2	3		0	1	1		2
4	1	3	2		0	1	0		1
4	2	1	3		0	0	1		1
4	2	3	1		0	1	0		1
4	3	1	2		0	0	1		1
4	3	2	1		0	0	0		0

"""


"""
def fac(n):
	r = 1
	for i in range(1, n+1):
		r*=i
	return r

base = 3
nn = 1
pp = 0
while nn < base**base:
	dic = set()
	n = nn
	prev = 1000
	ccc = 0
	for i in range(base):
		if n%base > prev:
			ccc += 1
			if ccc >= 2:
				ccc = 0
				break
		if n%base in dic:
			ccc = 0
			break
		dic.add(n%base)
		prev = n%base
		n //= base
		

	if ccc == 1:
		#print(nn)
		ccc = nn
		txt = []
		for i in range(base):
			txt.append(ccc%base)
			ccc//=base
		print(txt) #J[::-1]
		pp +=1
	
	nn += 1
	ff = fac(base)
print("{} / {} = {}".format(pp, ff, pp/ff))
"""