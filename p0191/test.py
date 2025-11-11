#p191


"""
A: Absent
L: Late
O: On time
"""

def fact(n,r=0):
    c = 1
    for i in range(r+1,n+1):
        c *= i
    return c

"""

[nbA][nbX] = x

"""

dic = {}

LEN = 30
for le in range(LEN):
    


cc=0
for a in "AX":
    for b in "AX":
        for c in "AX":
            for d in "AX":
                for e in "AX":
                    for f in "AX":
                        w = "{}{}{}{}{}{}".format(a,b,c,d,e,f)
    
                        if w.count("A") == 3:# and w[:3] != "AAA" and w[-3] != "AAA": # and w.count("L") <= 1 w.count("L") <= 1:
                            cc += 1
                            print(w)




"""
le = 8
cc=0
for a in "ALO":
    for b in "ALO":
        for c in "ALO":
            for d in "ALO":
                for e in "ALO":
                    for f in "ALO":
                        for g in "ALO":
                            for h in "ALO":
                                w = "{}{}{}{}{}{}{}{}".format(a,b,c,d,e,f,g,h)
            
                                if w.count("AAA") >= 1 and w[:3] != "AAA" and w[-3] != "AAA": # and w.count("L") <= 1 w.count("L") <= 1:
                                    cc += 1
                                    #print(w)


#start by AAAx... or end by ...xAAA
# case  1: x = L => no more L
#case 2 : x = O => max 1 L
comb = 2*( 2**(le-4) + 2**(le-4) + 2**(le-5)*(le-4))


# ...xAAAx... 
# case  1: x = L => no more L
#case 2 : x = O => max 1 L

comb = 0
for i in range(le-4):
    comb += 2*2*3**i*3**(le-5-i)
    
    
print("{}\t{}".format(cc, comb))
"""
"""
le = 7-2
nbX = le-nbA+2
comb = 2**(nbX)*fact(le)/fact(nbA-2)/fact(nbX) * (nbX+1)/2**nbX
"""

# bugggggggg!


"""
lenn = 6
for nbA in range(3, lenn+1):
    cc=0
    for a in "ALO":
        for b in "ALO":
            for c in "ALO":
                for d in "ALO":
                    for e in "ALO":
                        for f in "ALO":
                            w = "{}{}{}{}{}{}".format(a,b,c,d,e,f)
        
                            if w.count("A") == nbA and w.count("AAA") >= 1: #and w.count("L") <= 1:
                                cc += 1
                                #print(w)
    le = lenn-2
    nbX = le-nbA+2
    comb = 2**(nbX)*fact(le)/fact(nbA-2)/fact(nbX) #* (nbX+1)/2**nbX
    print("{}\t{}\t{}".format(nbA, cc, comb))
"""

"""
for nbA in range(3, 8):
    cc=0
    for a in "ALO":
        for b in "ALO":
            for c in "ALO":
                for d in "ALO":
                    for e in "ALO":
                        for f in "ALO":
                            for g in "ALO":
                                w = "{}{}{}{}{}{}{}".format(a,b,c,d,e,f,g)
            
                                if w.count("A") == nbA and w.count("L") <= 1 and w.count("AAA") >= 1:
                                    cc += 1
                                    #print(w)
    le = 7-2
    nbX = le-nbA+2
    comb = 2**(nbX)*fact(le)/fact(nbA-2)/fact(nbX) * (nbX+1)/2**nbX
    print("{}\t{}\t{}".format(nbA, cc, comb))
# bugggggggg!
"""

"""
for nbA in range(3, 8):
    cc=0
    for a in "ALO":
        for b in "ALO":
            for c in "ALO":
                for d in "ALO":
                    for e in "ALO":
                        for f in "ALO":
                            for g in "ALO":
                                w = "{}{}{}{}{}{}{}".format(a,b,c,d,e,f,g)
            
                                "
                                if w in bl:
                                    continue
                                print(w)
                                #print("{}{}{}{}".format(a,b,c,d))
                                cc += 1
                                "
                                if w.count("A") == nbA and w.count("L") <= 1:
                                    cc += 1
                                    #print(w)
    nbX = 7-nbA
    comb = 2**(nbX)*fact(7)/fact(nbA)/fact(nbX) * (nbX+1)/2**nbX
    print("{}\t{}\t{}".format(nbA, cc, comb))

"""


"""

bl = ["OOOO", "OOOA", "OOOL", "OOAO", "OOAA", "OOAL", "OOLO", "OOLA", "OAOO", "OAOA", "OAOL", "OAAO", "OAAL", "OALO", "OALA", "OLOO", "OLOA", "OLAO", "OLAA", "AOOO", "AOOA", "AOOL", "AOAO", "AOAA", "AOAL", "AOLO", "AOLA", "AAOO", "AAOA", "AAOL", "AALO", "AALA", "ALOO", "ALOA", "ALAO", "ALAA", "LOOO", "LOOA", "LOAO", "LOAA", "LAOO", "LAOA", "LAAO"]

n = 0

# P(AAA in the string)
#len=4 => 4
n += 4

# 1-P(0*O)-P(1*O)
#len=4 => 3**4-2**4-2**3*4
n += 3**4-2**4-2**3*4

# P(2*O and AAA)
#len=4 => 0

#print(3**4-n)



dic = {}
st = "ALO"
cc = 0
for a in st:
    for b in st:
        for c in st:
            for d in st:
                for e in st:
                    w = "{}{}{}{}{}".format(a,b,c,d,e)
                    if w.count("A") == 1:# and w.count("L") <= 1:
                        cc += 1
                        dic[w] = 0
                        print(w)
print(dic)
print("Word XXXAA")
print(cc)

cc = 0
for w in dic:
    if w.count("L") >= 2:
        cc += 1

print("AA max 1L")
print(cc)

# XXXXA 5!/4! => 5

#"
XXX

AAL
ALA
LAA
AAA

LAL
LLA
ALL
LLL

0L  1
1L  3
2L  3
3L  1
"

"
XXXX => 6

AAAL
AALA
ALAA
LAAA
AAA

LAL
LLA
ALL
LLL

0L  1
1L  5
2L  3
3L  1



cc=0
for a in "ALO":
    for b in "ALO":
        for c in "ALO":
            for d in "ALO":
                for e in "ALO":
                    for f in "ALO":
                        for g in "ALO":
                            w = "{}{}{}{}{}{}{}".format(a,b,c,d,e,f,g)
        
                            "
                            if w in bl:
                                continue
                            print(w)
                            #print("{}{}{}{}".format(a,b,c,d))
                            cc += 1
                            ""
                            if w.count("AAA") >= 1:
                                cc += 1
                                print(w)

print(cc)
print()

""
leny = 4
for nL in range(leny):
    #P(nL)
    print(nL)
    print(2**(leny-nL)*(f(leny)//f(nL)))
    print()
""

#print(3**5-cc)
print(cc)
print()


print(2*3*2+2*2)
print(2**5)
print(5*2**4)
print(3**5/8)
print(3*3**2)
print(2**5)
print(5*2**4)
#print(3**4-cc)
"""