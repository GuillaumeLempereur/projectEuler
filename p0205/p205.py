#Problem 194

tots_4s = [0]*37

nbDice = 9 # 9
valLim = 3
dices = [0]*nbDice

quit = False

tots_4s[nbDice] = 1
while(1):
    dices[0] += 1
    it = 0
    while(dices[it]>valLim):
        dices[it] = 0
        it += 1
        if it == nbDice: # and dices[it-1] == valLim
            quit = True
            break
        dices[it] += 1

    if quit:
        break

    tots_4s[sum(dices)+nbDice] += 1

print(tots_4s)

tots_6s = [0]*37

nbDice = 6 # 9
valLim = 5
dices = [0]*nbDice

quit = False

tots_6s[nbDice] = 1
while(1):
    dices[0] += 1
    it = 0
    while(dices[it]>valLim):
        dices[it] = 0
        it += 1
        if it == nbDice: # and dices[it-1] == valLim
            quit = True
            break
        dices[it] += 1

    if quit:
        break

    tots_6s[sum(dices)+nbDice] += 1

print(tots_6s)

totPos_4s = 4**9
totPos_6s = 6**6

prob = 0

for i in range(9,37): # score of 4-side dices
    for j in range(6,i): # score that 6-side dices can do to loose
        prob += tots_4s[i]/totPos_4s * tots_6s[j]/totPos_6s


print(prob)



"""
def foursidedice(s,dice):
    if dice == 9:
        tots[s] += 1
    for i in range(4):
        foursidedice(s+i+1,dice+1)

foursidedice(0,0)

print(tots)
"""

"""
Nice ideas but brute force win :)

Arrangement:

A(ABBO) = n_tot!/n(A)!/n(B)!/n(O)!


 9 or 36: 1
10 or 35: 9
11 or 34: 9 + 9*8/2 = 45
12 or 33: 9 + 9*8 + 9*8*7/3! = 165
13 or 32: 9*8 + 9*8/2 + 9*8*7/2 = 360
14 or 31: 9*8 + 9*8*7/2 + 9*8*7*6/3! + 9*8*7*6*5/5! = 954
15 or 30:


...
need a recursive function for computing the possibility to make a certain sum like 4 decomposed in 3,1 or 2,2

4 => 3,1 & 2, 2
3 => 2, 1

"""

"""
9 4-faced dices


print(10%6,10%-6)

# prob of having 9 or 36
print(1)

# prob of having 9 or 36
print(9)

# prob of having 9 or 36
print(9+9*8)

# prob of having 9 or 36
print()

# prob of having 9 or 36
print(1)
"""
"""
Way of doing such a particular score:
Score from 9 to 36, compute from 9 to 22: the opposite gives 36 to 23

9 => only 1's
10 => 2 and 1's
12 => 4 and 1's
13 => 4 2 and 1's
"""


"""
basisl = {}
basisl[9] = [1]*9
shift = 0
for i in range(10,23):
    basisl[i] = basisl[i-1][:]

    if basisl[i][shift] < 4:
        basisl[i][shift] += 1
    else:
        shift += 1
        basisl[i][shift] += 1


def comb(dices):

    nbDice = 9
    maxVal = 4
    for d in dices:
        if d == 4: # can decompose in 3,2
            for i in range(nbDice):
                if dices[i] < maxVal:
                    if i== nbDice-1:
                        return
                    dices.insert(i,3)
            print("r")

"""


"""
print("-"*10)
for i in range(9,23):
    #print(basisl[i])
    print(sum(basisl[i]))
"""


"""
d = list(range(1,10))

adjlstA = [[3,1,6],[0,2,6],[1,3,4],[0,2,4],[2,3,5],[4,6],[0,1,5]]
adjlstB = [[3,1,6],[0,2,6],[1,4],[0,4],[2,3,5],[4,6],[0,1,5]]

cnt = 0

def comb(conf, v):
    global cnt
    #print(v, conf)
    if v == 7:
        #finished
        print(conf)
        cnt += 1
        return

    colours = ['R', 'G', 'B']
    for n in adjlstB[v]:
        if n < v:
            # colour already took
            if conf[n] in colours:
                colours.remove(conf[n])

    for c in colours:
        comb(conf[:]+[c],v+1)

conf = []
comb(conf,0)

print(cnt)




for a in range(1,10):
    d.pop(a)
    print(d)

"""