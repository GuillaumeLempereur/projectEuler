class Pol:
	p = []
	degree = 0
	it = range(0)

	def __init__(self,pol):
		self.p = pol
		self.degree = len(pol)-1
		self.it = range(self.degree+1)

	def __add__(self,p2):
		if(self.degree>p2.degree):
			pr = self.p[:]
			for i in p2.it:
				pr[i] += p2.p[i]
		else:
			pr = p2.p[:]
			for i in self.it:
				pr[i] += self.p[i]
		return Pol(pr)

	def __mul__(self,p2):
		prod = [0]*(self.degree+p2.degree+1)
		#print(prod,len(p1),len(p2))
		for i in self.it:
			for j in p2.it:
				#print("\t",i," ",j)
				prod[i+j] += self.p[i]*p2.p[j]
		return Pol(prod)

	def __str__(self):
		return str(self.p)
	
	def copy(self):
		return Pol(self.p[:])
"""
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


p = [f(1)]
print(p)
for d in range(1,10):
	print(d)
"""

p1 = Pol([1, 2, 3])
p2 = Pol([-1, 2])
p3 = p2.copy()

print(p1)
print(p2)
print(p3)

p3.p[0] = -5
print(p1)
print(p2)
print(p3)

print("p3 = p1+p2")
p3 = p1+p2
print(p1)
print(p2)
print(p3)

print("p3 = p3*p1")
p3 = p3*p1
print(p1)
print(p2)
print(p3)
