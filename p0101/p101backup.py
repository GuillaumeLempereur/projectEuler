def polMul(p1,p2):
	prod = [0]*(len(p1)+len(p2)-1)
	#print(prod,len(p1),len(p2))
	for i in range(len(p1)):
		for j in range(len(p2)):
			#print("\t",i," ",j)
			prod[i+j] += p1[i]*p2[j]
	return prod

def c_n(i):
	return 1

def xpol(i):
	if i == 0:
		return [1 -1]
	else:
		return polMul(xpol(i-1),[1, -i-1])

def p(i):
	if i==0:
		p = [u(1)]
	else:
		return p(i-1) + mulPol(c(i),
	

def u(x):
	return x**3

print("test")

p = polMul([1, 2, 3],[1,2,3])
print(p)

"""
p = [f(1)]
print(p)
for d in range(1,10):
	print(d)
"""

