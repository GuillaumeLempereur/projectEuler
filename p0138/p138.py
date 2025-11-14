"""
P138

Pell's equation:

x^2-n*y^2 = -1

"""

def isqrt(n):
    x = n
    y = (x + 1) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x

L_lst = []

D = 5
x_0, y_0 = 2, 1
x_n, y_n = 38, 17
print(16,15,17)
L_lst = [17]
for i in range(15):
    x_n1 = x_n*x_0**2+x_n*y_0**2*D+2*x_0*y_0*y_n*D

    y_n1 = 2*x_0*x_n*y_0+y_n*x_0**2+y_0**2*y_n*D

    x_n, y_n = x_n1, y_n1

    dd = -4+2*x_n
    if dd %5 == 0:
        b = dd//5
        h = b+1
        print(b,h,isqrt(b*b//4+h*h))
        L_lst.append(isqrt(b*b//4+h*h))
    dd = 4+2*x_n
    if dd %5 == 0:
        b = dd//5
        h = b-1
        print(b,h,isqrt(b*b//4+h*h))
        L_lst.append(isqrt(b*b//4+h*h))

ll = sorted(L_lst)
print("Ans:", sum(ll[:12]))
