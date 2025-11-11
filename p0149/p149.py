#Problem 149
"""
Searching for a maximum-sum subsequence

not the answer: 48519449
answer: 52852124

idea aggregate adjacent number if null restart at the next
"""

import time

s = {}


start = time.time()
sum = 0
def s_k(k):
    if k in s:
        return s[k]
    if k <= 55:
        s[k] = (100003-200003*k + 300007*k**3)%1000000 - 500000
        return s[k]

    s[k] = (s_k(k-24)+s_k(k-55)+1000000) % 1000000 - 500000
    return s[k]

for k in range(1,4000001):
    #print(k,s_k(k))

    sum += s_k(k)

print(sum)

end = time.time()

#--- looking for the max

maxy = 0
size = 2000

# Horizontal

for j in range(size):
    sum = 0
    for i in range(size):
        sum += s[size*j+i+1]
        if sum <=0:
            sum = 0
    if sum > maxy:
        maxy = sum

# Vertical

for j in range(size):
    sum = 0
    for i in range(size):
        sum += s[size * i + j+1]
        if sum <=0:
            sum = 0
    if sum > maxy:
        maxy = sum

# diagonal
# 1st half
"""
* * *
* *
*
"""
for j in range(size):
    sum = 0
    for i in range(j+1):
        sum += s[size * (j-i) + i + 1]
        if sum <=0:
            sum = 0
    if sum > maxy:
        maxy = sum
"""
. . *
. * *
* * *
"""
# 2nd half
for j in range(size):  # j = col
    sum = 0
    for i in range(size - j):  # i = row
        sum += s[size * (size - i - 1) + i + j + 1]
        if sum <=0:
            sum = 0
    if sum > maxy:
        maxy = sum

# anti-diagonal
"""
* * *
. * *
. . *
"""
for j in range(size):
    sum = 0
    for i in range(size-j):
        sum += s[size * i + j + i + 1]
        if sum <=0:
            sum = 0
    if sum > maxy:
        maxy = sum

"""
* . .
* * .
* * *
"""
for j in range(size):
    sum = 0
    for i in range(size - j):
        sum += s[size * (j+i) + i + 1]
        if sum <=0:
            sum = 0
    if sum > maxy:
        maxy = sum

#--- looking for the max

print(end-start)

print(maxy)
