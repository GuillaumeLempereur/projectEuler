class Node:
	def __init__(self,v,neigh = [None]*6):
		self.neighbour = neigh
		self.value = v


	def addNeighbour(self,neigh)
		self.neighbour.append(neigh)

	def nbNeigh(self):
		return len(self.neighbour)
	
	def goUp(self):
		return self.neighbour[0]

	def goUpLeft(self):
		return self.neighbour[1]

	def goDownLeft(self):
		return self.neighbour[2]

	def goDown(self):
		return self.neighbour[3]

	def goDownRight(self):
		return self.neighbour[4]

	def goUpRight(self):
		return self.neighbour[5]

nodCur = Node(1)
n = 2
for i in range(1,10):
	
	neigh = [None]*3 + [nodCur] + [None]*2
	node = Node(n,neigh)
	nodCur.neighbour[0] = node
	n += 1
	
	nodCur = node
	
	# Go Left Down
	for _ in range(i):
		neigh = [None]*5 + [nodCur]
		node = Node(n,neigh)
		nodCur.neighbour[2] = node
		n += 1
		nodCur = node

	# Go Down
	for _ in range(i):
		neigh = [nodCur] + [None]*5
		node = Node(n,neigh)
		nodCur.neighbour[3] = node
		n += 1
		nodCur = node


if nodeCur


