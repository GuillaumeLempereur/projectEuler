
maxy = 0
s = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
size = 3

maxy = 0

# Horizontal

for j in range(size):
    sum = 0
    for i in range(size):
        sum += s[size*j+i+1]
        print(s[size*j+i+1],end=' ')
    if sum > maxy:
        maxy = sum
    print()
print('-'*15)
# Vertical

for j in range(size):
    sum = 0
    for i in range(size):
        sum += s[size * i + j+1]
        print(s[size * i + j+1],end=' ')
    if sum > maxy:
        maxy = sum
    print()
print('-' * 15)
# diagonal
# 1st half
for j in range(size):
    sum = 0
    for i in range(j+1):
        sum += s[size * (j-i) + i + 1]
        print(s[size * (j-i) + i + 1],end= ' ')
    if sum > maxy:
        maxy = sum
    print()
print('-' * 15)
# 2nd half
for j in range(size):  # j = col
    sum = 0
    for i in range(size - j):  # i = row
        sum += s[size * (size - i - 1) + i + j + 1]
        print(s[size * (size - i - 1) + i + j + 1],end=' ')
    if sum > maxy:
        maxy = sum
    print()
print('-' * 15)
# anti-diagonal

for j in range(size):
    sum = 0
    for i in range(size-j):
        sum += s[size * i + j + i + 1]
        print(s[size * i + j + i + 1],end=' ')
    if sum > maxy:
        maxy = sum
    print()
print('-'*15)
for j in range(size):
    sum = 0
    for i in range(size - j):
        sum += s[size * (j+i) + i + 1]
        print(s[size * (j+i) + i + 1],end=' ')
    if sum > maxy:
        maxy = sum
    print()