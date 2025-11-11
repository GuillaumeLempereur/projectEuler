N = 10000000
l = []

for i in range(1,N):
	for j in range(int((max(i*i-1000000,1))**(1/2)),i):
		k = i*i-j*j
		if (i+j)%2==0 and k <= 1000000:
			l.append((k,i,j))

#print(l)
print(len(l))
#ans: 1572729