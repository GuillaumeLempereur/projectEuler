#Problem 194
"""
Colour configuration

For each vertex, enumerate the possible colour, then recursively find the others

*0      *6
    *5
    *2
    *3
*1      *4

*0      *5      *10
    *3      *8
    *2      *7
    *4      *9
*1      *6      *11

"""

d = list(range(1,10))
cnt = 0

def graphAgglomerate(adjlst, conf):
    adjlst.clear()
    if conf[0] == 'A':
        adjlst += [[1,3,5],[0,4,6],[3,4],[0,2,5],[1,2,6],[0,3,6],[1,4,5]]
    elif conf[0] == 'B':
        adjlst += [[1,3,5],[0,4],[3,4],[0,2,5],[1,2,6],[0,3,6],[4,5]]

    for c in conf[1:]:
        l = len(adjlst)
        print(l)
        adjlst[len(adjlst)-2] += [l+3,l+1]

        if c == 'A':
            adjlst[len(adjlst)-1].append([l + 2, l + 4])
            adjlst += [[l + 1, l + 2], [l - 2, l, l + 3], [l - 1, l, l + 4], [l - 2, l + 1, l + 4],
                          [l - 1, l + 2, l + 3]]
        elif c == 'B':
            adjlst[len(adjlst)-1].append([l + 2])
            adjlst += [[l + 1, l + 2], [l - 2, l, l + 3], [l - 1, l, l + 4], [l - 2, l + 1, l + 4],
                          [l + 2, l + 3]]



""" OLD 
def graphAgglomerate(adjlst, conf):
    nn = 5
    for c in conf:
        if len(adjlst) == 0:
            if c == 'A':
                adjlst = adjlstA[:]
            elif c == 'B':
                adjlst = adjlstB[:]

        if c == 'A':
            adjlst[nn].append([nn+3,nn+5])
            adjlst[nn+1].append([nn + 4, nn + 6])
            adjlst.append([[nn+3,nn+4],[nn,nn+2,nn+5],[nn+1,nn+2,nn+6],[nn,nn+3,nn+6],[nn+1,nn+4,nn+5]])
        elif c == 'B':
            adjlst[nn].append(nn + 3)
            adjlst[nn + 1].append([nn + 4, nn + 6])
            adjlst.append([[nn + 3, nn + 4], [nn, nn + 2, nn + 5], [nn + 1, nn + 2, nn + 6], [nn + 3, nn + 6],
                          [nn + 1, nn + 4, nn + 5]])
        nn += 5
"""
z =  [] + [[1,3,5],[0,4,6],[3,4],[0,2,5],[1,2,6],[0,3,6],[1,4,5]]
z.append(z)
print(z)

a = []
conf = 'AABB'
graphAgglomerate(a, conf)
print("adjlst")
print(a)

exit(0)

def comb(conf, v):
    global cnt
    #print(v, conf)
    if v == 7:
        #finished
        print(conf)
        cnt += 1
        return

    colours = ['R', 'G', 'B']
    for n in adjlstA[v]:
        if n < v:
            # colour already took
            if conf[n] in colours:
                colours.remove(conf[n])

    for c in colours:
        comb(conf[:]+[c],v+1)

conf = []
comb(conf,0)

print(cnt)



