# Hello World program in Python
    
import sys
cumsum = []
pyramid = []

n = 10
l = 1
for t in range(n):
    pyramid.append([])
    cumsum.append([0])
    cs = 0
    for i in range(t+1):
        elem = (l*615949+797807)%(2**20)-2**19
        pyramid[t].append(elem)
        l += 1
        cs += elem
        cumsum[t].append(cs)

print(pyramid)
print(cumsum)

t = 0
minS = 11000
for r in range(n):
	#
	for c in range(r+1):
		s = pyramid[r][c]
		if s < minS:
			minS = s

		for i in range(n-r-1):
			s += cumsum[r][c+i+2]-cumsum[r][c]
			if s < minS:
				minS = s

		t += 1

print(minS)
