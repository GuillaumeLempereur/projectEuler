#include <iostream>
#include <cmath>
#include "euler.h"

int primes[80000];

int main(int args, char **argv){
	int lim = 1000;//1000000;
	long long int cc = 0;
	int p=0;

	for(int i=0;i<lim;++i){
		if(is_prime_mr(i)){
			primes[p++] = i;
		}
	}
	std::cout << p << std::endl;

	for(long long int d=1;d<lim;++d){
		double d6 = d,limD = lim ;
		d6 = d6*d6*d6*d6*d6*d6;

		int boundLow = 1 + sqrt(d6+1.0);
		int boundHigh = 1 + sqrt(4*limD*limD+d6);
		for(long long int g = boundLow;g<boundHigh;++g){
			cc++;
			Divider div;

			factorize(g-d*d*d,primes, div);
		}
	}
	printf("%ld\n", cc);

	return 0;
}

/*
# enumerate every g ,d below lim

lim = 200

lim = int(sys.argv[1])

cc = 0
c2 = 0

al = [False]*lim


print("math.sqrt(rs/4), p, g, d")
for d in range(1,lim):
    boundLow = math.floor(math.sqrt(1+d**6))+1
    boundHigh = math.floor(math.sqrt(4*(lim**2)+d**6))+1
    for g in range(boundLow,boundHigh):

        cc += 1
        n = (g-d**3)*(g+d**3)

        if d == 407:
            print("facorizing",g-d**3,g+d**3)
        f1 = Euler.factorization(g-d**3)
        f2 = Euler.factorization(g+d**3)
        if d == 407:
            print("end facorizing")

        #print("-"*15)
        #print(g,d)
        #print(f1)
        #print(f2)
        p = 1
        ff = f1
        for f in f2:
            if f in f1:
                ff[f] += f2[f]
            else:
                ff[f] = f2[f]
        for f in ff:
            if ff[f] %2 == 1:
                p*=f

        #print(ff)
        rs = p**3*(g-d**3)*(g+d**3)
        if rs%4 != 0 or rs >= 4*lim*lim:
            continue
        else:
            #print(math.sqrt(rs/4), p, g, d)
            al[round(math.sqrt(rs//4))] = True
c2 = 0
for i in range(len(al)):
    if al[i]:
        c2 += 1
        print(i)
print(cc)
print(c2)
exit(0)


for g in range(1,2*lim):
    for d in range(1,lim):
        if d**3 >= g:
            break
        n = (g-d**3)*(g+d**3)

# case p = 1


# case p > 1


for a in range(1,lim):
    facs = Euler.factorization(a)

    sq = False
    for f in facs:
        if facs[f]%4==0:
            sq = True

    if sq:
        cc += 1


a = 6072
d = 6400

nsq = d*(4*a*a+d**3)

x = 4*a*a
y = d**3
z = (4*a*a+d**3)

cf = Euler.gcd(x,Euler.gcd(y,z))
x, y, z = x//cf, y//cf, z//cf

x,y,z = root(x), root(y), root(z)

print("cf",cf)
print("x", x)
print("y", y)
print("z", z)


print(x+y,z)

print(math.sqrt(x+z))
print(math.sqrt(z+y))

exit(0)

lim = 500000

cc = {}
for i in range(1,lim):
    cc[3*i**3] = i

print("cc ready")

for a in range(1,lim):
    if (a**2-3)**2 in cc:
        print(a)

exit(0)
for r in range(1,a*a):
    s = (a*a-r)**2

    f_a = Euler.factorization(a)
    f_r = Euler.factorization(r)

    if s % r == 0: #and a%r != 0:
        for f in f_a:
            if f not in f_r:
                print(a,r,f)
        #    print(a,r,s)
*/
