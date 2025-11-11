import math

a= 399
b= 511
c= 455
n= 784

al= (b*b+c*c-a*a)/2.0/c

print(a,b,c,b*b+c*c-a*a,al)


alpha = (b*b+c*c-a*a)/2.0/c
beta = math.sqrt(b*b-alpha*alpha)
sq3 = math.sqrt(3)
num = c*(-5.0/4.0*beta+(3.0/4.0-3.0*sq3/4.0)*alpha)-2.0*alpha*beta-sq3/2.0*b*b
den = -2.0*c*beta-(a*a+b*b)*sq3/2.0

x = num/den
y = -sq3/2.0*c+(x-c/2.0)*(beta+sq3/2.0*c)/(alpha-c/2.0)

print(x,y)
