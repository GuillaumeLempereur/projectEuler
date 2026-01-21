/*
 * p0027
 * */
#include <iostream>
#include "../primesBelow1M.h"
#include <set>

// b must be prime, case n = 0
int main(){
	int ans = 0, maxx = 0;
	std::set<int> primes1k;
	for(int i=0;i<78498;++i){
		int p = primesBelow1M[i];
		primes1k.insert(p);
	}

	// n² + a*n + b = p
	
	for(int a=-999;a<1000;++a){
		int b = 2;
		for(int i=1;b<1000;++i){
			int c = 1;
			for(int n=0;n<b;++n){
				int p = n*n+a*n+b;
				if(!primes1k.contains(p)){
					if(maxx < n){
						maxx = n;
						ans = a*b;
					}
					break;
				}
			}
			b = primesBelow1M[i];
		}
	}

	std::cout << ans << std::endl;
	return 0;
}
