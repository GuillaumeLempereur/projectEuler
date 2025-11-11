"""
p177

"""
import math
import sys

s = set()

for c_2 in range(1,178): #1 to 180-3 c_2 bigger or equal than others
    for c_1 in range(1 , min(c_2+1, 180-c_2-1)): #1 to c_2
        for b_1 in range(1, min(c_2+1, 180-c_2-c_1)): #1 to c_2
            d_2 = 180-c_1-c_2-b_1
            if d_2 < 1 or d_2 > c_2:
                continue
            if c_1==c_2 and d_2 > b_1:
                continue # if c_2 == c_1 => b1 >= d2
            for b_2 in range(1, min(d_2+c_1, c_2+1)): # 1 to 180-c2-b1-1 or >=d2 if b1=c1
                a_1 = d_2+c_1-b_2
                if a_1 < 1 or a_1 > c_2:
                    continue
                a1 = a_1/180*math.pi
                b1 = b_1/180*math.pi
                b2 = b_2/180*math.pi
                c1 = c_1/180*math.pi
                c2 = c_2/180*math.pi
                d2 = d_2/180*math.pi
                nn = math.sin(a1)*math.sin(b1)*math.sin(c1) # numerator
                dd = math.sin(d2)*math.sin(b1+b2) - math.cos(c1)*math.sin(b1)*math.sin(a1) # denominator
                if abs(dd) < 1e-14: # divide by 0
                    a_2 = 90 # tan(+inf)
                else:
                    a2 = math.atan(nn/dd)
                    a_2 = a2*180/math.pi
                    if abs(round(a_2)-a_2) > 1e-9:
                        continue
                    a_2 = round(a2*180/math.pi)
                if a_2 < 0:
                    a_2 = 180+ a_2
                if a_2 < 1 or a_2 > c_2:
                    continue
                d_1 = 180-a_1-a_2-b_2
                if c_2 == c_1 and b_1 == d_2 and d_1 > b_2:
                    continue

                if d_1 < 1 or d_1 > c_2:
                    continue

                if c_2 == c_1 and b_1 == d_2 and d_1 == b_2 and a_2 > a_1:
                    continue

                A = (a_1+a_2)
                B = b_1+b_2
                C = c_1+c_2
                D = d_1+d_2
                if A >= 180 or B >=180 or C >= 180 or D >= 180:
                    continue

                l = [c_2, c_1, d_2, d_1, a_2, a_1, b_2, b_1]
                cont = False
                #check that it's not already considered starting from another angle = to max (c_2)
                for i in range(len(l)):
                    if i%2==1:
                        continue
                    if l[i] == max(l):
                        ntup = tuple(l[i:]+l[:i])
                        if ntup in s:
                            cont = True
                            break

                #check that it's not already considered in reverse direction
                l = list(reversed([c_2, c_1, d_2, d_1, a_2, a_1, b_2, b_1]))
                for i in range(len(l)):
                    if i%2==1:
                        continue
                    if l[i] == max(l):
                        ntup = tuple(l[i:]+l[:i])
                        if ntup in s:
                            cont = True
                            break
                if cont:
                    continue
                tup = (c_2, c_1, d_2, d_1, a_2, a_1, b_2, b_1)
                s.add(tup)
                #print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}".format(a_1, b_2, b_1, c_2, c_1, d_2, d_1, a_2))
print(len(s))
