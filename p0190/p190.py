#p190

#import Numpy as np

N = 0

"""
2 : 1.185185185... => 32/27  (4²/3²)*2/3
x = 2/3, y = 4/3 => 32/27

3 : 1.68749995950432
0.5001 0.9999600000000001 1.49994
x = 1/2, y = 1, z = 3/2 => 27/8

4 : 2.8986439188513344
0.4 0.792 1.20744 1.6005599999999998

x = 0.4, y = 0.8, z = 1.2, o = 1.6

x, 2x, 3x, 4x

"""

tot = 0
cumsum = 1
for m in range(2,16):
	cumsum += m
	
	x = m*1.0/cumsum
	#print(m, x)
	
	p = 1
	for i in range(1,m+1):
		p *= (x*i)**i
	tot += p//1
	print(m, x, p//1)
print(tot)
"""
pmax = 0
xmax, ymax, zmax, omax = 0, 0, 0, 0
for i in range(N):
	x = 4.0*i/N
	for j in range(N):
		y = (4.0-x)*j/N
		for k in range(N):
			z = (4.0-x-y)*k/N
			o = 4.0-x-y-z
			if y < 0 or z < 0 or o < 0:
				continue
			
			p = x*y*y*z*z*z*o*o*o*o
			if p > pmax:
				xmax = x
				ymax = y
				zmax = z
				omax = o
			pmax = max(p, pmax)
	
	#print(x, y)
print(pmax)
print(xmax, ymax, zmax, omax)

x = 0.4
y = 0.8
z = 1.2
o = 1.6

print(x*y*y*z*z*z*o*o*o*o)
"""
"""
pmax = 0
xmax, ymax, zmax = 0, 0, 0
for i in range(N):
	for j in range(N):
		x = 3.0*i/N
		y = (3.0-x)*j/N
		z = 3.0-x-y
		if y < 0 or z < 0:
			continue
		
		p = x*y*y*z*z*z
		if p > pmax:
			xmax = x
			ymax = y
			zmax = z
		pmax = max(p, pmax)
	
	#print(x, y)
print(pmax)
print(xmax, ymax, zmax)
"""

"""
pmax = 0
xmax, ymax = 0, 0
for i in range(N):
	x = 2.0*i/N
	y = 2.0-x
	
	p = x*y*y
	if p > pmax:
		xmax = x
		ymax = y
	pmax = max(p, pmax)
	
	#print(x, y)
print(pmax)
print(xmax, ymax)
"""
