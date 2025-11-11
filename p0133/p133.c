/*Problem 133

Repunit divisibility

answer is not 1000171, 1000491
*/

#include <stdio.h>
#include "euler.h"

/*
n not multiple of 10
There exist k such that R(k) is divisible by n

A(n) the least value of k

A(7) = 6 => 111111 divisible by 7
A(41) = 5 => 11111 divisible by 41


1%41 + 10 %41 + 10^2 %41 + 10^3 %41
For ech 1,10,100,... there is a recurrence in the modulo, sum the recurrence until having %n = 0

11,17,41,73 <100 all divider of R(10**n)

answer is not 453747698
may be should sum every primes and substract those that divide 10^n
*/

bool isOnlyMulOf2and5(int n){
	while(n%2==0)
		n /= 2;
	while(n%5==0)
		n /= 5;
	if(n==1)
		return true;
	return false;
}

int main(int args,char **argv){
	int imax = 0;

	int lim = 100000;//200000; // 10000
	int n = 1;
	int ss = 0;
	for(int i=0;i<lim;++i){
		if(imax == 40){
			printf("Answer: %d",ss);
			break;
		}
		n++;
		if(n%5==0 || n%2==0 || !is_prime_mr(n))
			continue;

		int a_r = 0;
		int s = 0;
		int rlst[2000000], nr = 0;
		int r = 1;
		rlst[nr++] = r;

		int i=0;
		for(i=1;i<1000000;++i){ // # 10**6 # need to speed up the finding of the recurrence !!!!
			r = ((10%n)*r) % n;
			s = (s+r)%n;

			if(s == 0){
                //printf("NOP %d %d\n",n,i);
                if(isOnlyMulOf2and5(i)){
                    //printf("%d %d\n",n,imax);
                    ss += n;
                }
				break; // # not interesting cause R(i < 5000) is divisible by n
			}
			if(r == 1){ // # && i > 1){
				break; //# found a reccurence
			}
			if(nr>2000000-2)
				return -2;

			rlst[nr++] = r;
		}
		if(s == 0){
			continue;
		}

		// 10xn % p = (10%p * n%p)%p
		s = 0;
		for(int r=0;r<1000000;++r){
			s = (s+rlst[r%nr])%n;
			if(s == 0){
				if(r > 1) // # 10**6)
					//printf("NOP %d %d\n",n,r+1);
					if(isOnlyMulOf2and5(r+1)){
                        //printf("%d %d\n",n,imax);
                        ss += n;
                    }
				break;
			}
		}

	}
	
	int psum = 0;
	for(int i=2;i<100000;++i){
		if(is_prime_mr(i))
			psum += i;
	}
    printf("ss, psum: %d %d\n",ss,psum);
    printf("Answer: %d\n",psum-ss);
	return 0;
}
