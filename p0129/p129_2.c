/*Problem 129

Repunit divisibility

answer is not 1000171, 1000491
*/

#include <stdio.h>

/*
n not multiple of 10
There exist k such that R(k) is divisible by n

A(n) the least value of k

A(7) = 6 => 111111 divisible by 7
A(41) = 5 => 11111 divisible by 41


1%41 + 10 %41 + 10^2 %41 + 10^3 %41
For ech 1,10,100,... there is a recurrence in the modulo, sum the recurrence until having %n = 0

lim 2000: 245 s => 4.69 s
lim 10000: 107 s r ~= 100000
*/

/*
def R(n):
    s = "1"*n
    return int(s)
*/

int main(int args,char **argv){
	int imax = 0;

	int lim = 100000; // 10000
	int n = 999861;
	for(int i=0;i<lim;++i){
		n++;
		if(n%5==0  || n%2==0)
			continue;
		int a_r = 0;
		int s = 0;
		int rlst[2000000], nr = 0;
		int r = 1;
		rlst[nr++] = r;

		for(int i=1;i<2000000;++i){ // # 10**6 # need to speed up the finding of the recurrence !!!!
			//imax = max(imax,i)
			r = ((10%n)*r) % n;

			s = (s+r)%n;
			//print("\t", r, s)

			if(s == 0){
				//if r not in rl:
				//rl.add(r)
				//rlst.append(r)
				break; // # not interesting cause R(i < 5000) is divisible by n
			}
			if(r == 1){ // # && i > 1){
				//print(n,sum(rlst)%n)
				break; //# found a reccurence
			}
			if(nr>2000000-2)
				return -2;

			rlst[nr++] = r;
		}
		if(s == 0)
			continue;

		//if len(rlst) < n//8: # not really an improvement
		//   continue

		//print(n,rlst)

		// 10xn % p = (10%p * n%p)%p
		s = 0;
		for(int r=0;r<2000000;++r){
			s = (s+rlst[r%nr])%n;
			if(s == 0){
				if(r > 900000)// # 10**6)
					printf("%d %d %d\n",n,r,nr); // # print(R(r+1)%n)
				break;
			}
		}
	}
    //print(n, s, rl)
	return 0;
}
/*
r = 0
rec = [10,18,16,37,1]
for i in range(lim):
    r = (r+rec[i%5])%21
    print(i,r)

*/

/*
def gcd(a,b):
    if a < b:
        return gcd(b,a)
    while(b>0):
        a, b = b, a%b
    return a

lim = 1000
r = 11

fac = 1
for i in range(lim):
    fac *= i*10+1


for i in range(lim):
    print(i,Euler.primefactors(gcd(fac,r)))

    r = r*10 + 1
*/

