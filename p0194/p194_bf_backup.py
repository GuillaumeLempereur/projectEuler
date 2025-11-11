#Problem 194
"""
Colour configuration

For each vertex, enumerate the possible colour, then recursively find the others
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



"""
for a in range(1,10):
    d.pop(a)
    print(d)

"""