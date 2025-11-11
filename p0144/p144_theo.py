#"""
from matplotlib.patches import Ellipse
import matplotlib as mpl
#matplotlib inline
from matplotlib import pyplot as plt

mean = [ 0 ,  0]
width = 10
height = 20
angle = 0
ell = mpl.patches.Ellipse(xy=mean, width=width, height=height, angle = 180+angle, edgecolor='r', fc='None')
fig, ax = plt.subplots()

ax.add_patch(ell)
ax.set_aspect('equal')
ax.autoscale()

plt.plot([0.0, 1.4],[10.1, -9.6])


#"""
def scalar(a,b):
    print("scalar:", (a[0]*b[0]+a[1]*b[1])/(a[0]**2+a[1]**2)**(1/2)/(b[0]**2+b[1]**2)**(1/2))


x_0, y_0 = 1.4, -9.6
x_a, y_a = 0, 10.1

a_x, a_y = x_0-x_a, y_0-y_a
#b_x, b_y = x_0-x_b, y_0-y_b

n_x, n_y = 1, y_0/(4*x_0)

b_y = (n_y*(a_x+n_y*a_y) + (a_x**2*n_y**2+a_y**2-2*a_x*a_y*n_y)**(1/2))/(1+n_y**2)
print(b_y)

b_x = a_x + n_y*(a_y-b_y)
print(b_x)

print(b_x**2+b_y**2, a_x**2+a_y**2)
print("b_x, b_y",b_x, b_y)

plt.plot([1.4, 1.4-b_x],[-9.6, -9.6-b_y])

scalar([a_x, a_y],[n_x, n_y])
scalar([b_x,b_y],[n_x, n_y])
"""
b_y = (n_y*(a_x+n_y*a_y) - (a_x**2*n_y**2+a_y**2-2*a_x*a_y*n_y)**(1/2))/(1+n_y**2)
print(b_y)
b_x = a_x + n_y*(a_y-b_y)
print(b_x)

print(b_x**2+b_y**2, a_x**2+a_y**2)

scalar([a_x, a_y],[b_x,b_y])
plt.plot([1.4, b_x],[-9.6, b_y])
"""

n = (-8*x_0*(a_x+n_y*a_y)+2*b_y*(4*x_0*n_y-y_0))/(4*(a_x**2+a_y**2)-3*b_y**2)

B_y = y_0+n*b_y
B_x = -((100 - B_y**2)**(1/2))/2

print(n)
print(B_y,B_x)

plt.plot([1.4, B_x],[-9.6, B_y])

plt.show()

