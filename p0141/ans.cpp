#include <iostream>
#include <math.h>
#include <stdint.h>
#include "euler.h"

int primes[80000];

int main(){
	int64_t lim = 1000, cc = 0;
	int p = 0;
	std::pair<int,int> dividers[10];

	for(int i=1;i<lim;++i)
		if(is_prime_mr(i)){
			primes[p++] = i;
		}

	for(int r=1;r<lim;++r){
		int nbDiv = 0;

		std::cout << r << std::endl;
		nbDiv = factorize(r,primes, dividers);

		std::cout << r << " : "<< std::endl;
		for(int i=0;i<nbDiv;++i){
			std::cout << "\t"<< dividers[i].first << " " << dividers[i].second;
		}
		std::cout << std::endl;
		/*
		p = 1;
		for(int i=0;i<div.nbDiv;++i){
			if(div.dividers[i].second%3!=0)
				p*= div.dividers[i].first;
		}

		std::cout << r << "  " << p << std::endl;

		// a > r
		int i = r/p+1, a;
		for(a=p*i;a+p<lim;++i){
			a = p*i;
			int64_t cb = r*(a*a-r);
			int64_t q = (int64_t)(round(cbrt(cb))), d = (a*a-r)/q;
			if(q*q*q==cb)
				std::cout << a << " " << q << " " << d << " " << r << std::endl;
			//cc++;
		}
		*/
	}
	//std::cout << cc << std::endl;
	return 0;
}
