#p178

arr = [0]*40
i = 0
LIM = 20 # 20
cc = 0
start = [] #start n, min, max
end = [] #end n, min, max
nbStep = 0

startl = [] #start n, min, max
endl = [] #end n, min, max
for k in range(10):
	startl.append([])
	endl.append([])
	for l in range(10):
		startl[k].append([])
		endl[k].append([])
		for m in range(10):
			startl[k][l].append([])
			endl[k][l].append([])
			for n in range(10):
				startl[k][l][m] = []
				endl[k][l][m] = []
		
for k in range(10):
	start.append([])
	end.append([])
	for l in range(10):
		start[k].append([0]*10)
		end[k].append([0]*10)

#lst = []
		
def f():
	global arr, i, LIM, cc, start, end, nbStep
	#print(arr[:i])
	#lst.append(arr[:i])
	m = min(arr[:i])
	M = max(arr[:i])
	if m == 0 and M == 9 and arr[0] != 0:
		nbStep += 1
	start[arr[0]][m][M] += 1
	if i == LIM and arr[0] != 0:
		end[arr[i-1]][m][M] += 1
	
	"""
	st = ""
	for h in arr[:i]:
		st += str(h)
	startl[arr[0]][m][M].append(st)
	if i== 10:
		endl[arr[i-1]][m][M].append(st)
	"""
	cc += 1
	if i < LIM:
		if arr[i-1] == 0:
			arr[i] = 1
			i += 1
			f()
			i -= 1
		elif arr[i-1] == 9:
			arr[i] = 8
			i += 1
			f()
			i -= 1
		else:
			arr[i] = arr[i-1] - 1
			i += 1
			f()
			i -= 1
			arr[i] = arr[i-1] + 1
			i += 1
			f()
			i -= 1
	"""
	else:
		arr[i] = arr[i-1]
	"""
	
for k in range(10):
	i = 1
	arr[0] = k
	f()

print()
print(cc)
print(arr)
print()
print(start)
print()
print(end)

cc = 0

for k in range(10):
	for l in range(10):
		for m in range(10):
			cc += start[k][l][m]

print(cc)

cc = 0

for k in range(10):
	for l in range(10):
		for m in range(10):
			cc += end[k][l][m]

print(cc)

#print(len(lst))

print()
cc = 0

print("#"*20)
for k in range(10):
	for l in range(10):
		for m in range(10):
			if k<9:
				m_f = 1 if l>0 else 10
				for x in range(0,m_f):
					M_s = 0 if m==9 else 9
					for y in range(M_s, 10):
						cc += end[k][l][m]*start[k+1][x][y]
						"""
						for h in endl[k][l][m]:
							for j in startl[k+1][x][y]:
								print(h+j)
						"""
				
			if k>0:
				m_f = 1 if l>0 else 10
				for x in range(0,m_f):
					M_s = 0 if m==9 else 9
					for y in range(M_s, 10):
						cc += end[k][l][m]*start[k-1][x][y]
						"""
						for h in endl[k][l][m]:
							for j in startl[k-1][x][y]:
								print(h+j)
						"""

print("nb step up to {} {}".format(LIM, nbStep))
print("nb step up to {} {}".format(2*LIM, cc+nbStep))

#wrong answer: 111752382


"""
3	34
4	64
5	122
6	232
15	80832
20	2101752
25	
30	1423365002 (15s in c++)
"""