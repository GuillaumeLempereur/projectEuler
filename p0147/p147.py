P147

L, H = 3, 2
n = 0
for l in range(1,L+1):
	for h in range(1,H+1):
		n += (L-l+1)*(H-h+1)

L, H = 3, 2
n = 0
for l in range(1,L+1):
	for h in range(1,H+1):
		n += (L-l+1)*(H-h+1)


"""
Oblic:
1
3
5
7



width: max = 2*h+1-

for w in range(1,2*H): # 2*H-1
	for h in range((w+1)//2+1,L...)
"""
		

		


		
"""
Oblique start from center:


w+h: L = (w+h)//2+1
2: 2
3: 2
4: 3
5: 3
6: 4

5+1 => 4
4+2 => 4
Oblique start from edge:


2: 1
3: 2
4: 2
5: 3
6: 3
7: 4

5+1 => 3
4+2 => 3

width: max = 2*h+1-
"""

#Oblique start from center:	
for w in range(1,2*H): # 2*H-1
	for h in range(1,min(L,(L-1)*2-w)):

#Oblique start from edge:	
for w in range(1,2*H-1): # 2*(H-1)

