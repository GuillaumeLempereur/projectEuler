#include <iostream>
#include <vector>
#include <set>
#include "euler.h"

/*
 c can't be prime ! or a combination of primes but has to be f**n * f2 *f3 with n >1
 below 510510 max 6 primes dividers
 not 17707136 '(
 * */


int primes[12000];
int radl[120000];
Divider divl[120000];

int rad(int a){
	int rad = 1;
	for(int j=0;j<divl[a].nbDiv;++j){
		rad *= divl[a].dividers[j].first;
	}

	return rad;
}
int radd(int a, int b, int c){
	std::set<int> primDiv;

	for(int j=0;j<divl[a].nbDiv;++j){
		primDiv.insert(divl[a].dividers[j].first);
	}
	for(int j=0;j<divl[b].nbDiv;++j){
		primDiv.insert(divl[b].dividers[j].first);
	}
	for(int j=0;j<divl[c].nbDiv;++j){
		primDiv.insert(divl[c].dividers[j].first);
	}

	int rad = 1;
	for (std::set<int>::iterator it = primDiv.begin() ; it != primDiv.end(); ++it){
		rad *= *it;
	}

	return rad;
}

int main(int agrs, char **argv){
	int nbp = 1;
	int lim =120000;
	std::vector<int> c_l;
	primes[0] = 2;

	for(int i=3;i<lim;i+=2){
		if(is_prime_mr(i)){
			primes[nbp++] = i;
		}
	}
	

	// remove each number that doesn't have any factor at least twice
	// seems that there are only 10000 

	for(int i=1;i<lim;++i){
		factorize(i,primes, divl[i]);
		int rad = 1;
		bool added = false;
		for(int d=0;d<divl[i].nbDiv;++d){
			rad *= divl[i].dividers[d].first;
			if(divl[i].dividers[d].second > 1){
				if(added==false){
					c_l.push_back(i);
					added = true;
				}
			}
		}
		radl[i] = rad;
	}

	
	int cc = 0,i;
	for(int i=0;i<c_l.size();++i){
		size_t c = c_l[i];
		size_t rad_c = 1, rad_ab = 0;

		rad_ab = c/radl[c];

		for(int a=1;a<(c+1)/2;++a){
			int b = c-a;
			if(radl[a]*radl[b] < rad_ab){
				if(gcd(a,b)==1 && gcd(a*b,c)==1){
					//std::cout << a << " " << b << " " << c << " abc:" << radd(a,b,c) << " " << rad(a) << " " << rad(b) << " " << rad(c) <<std::endl;
					
					/*
					if(radd(a,b,c) >= c)
						return -9;
					if(gcd(a,b)!=1 || gcd(b,c)!=1 || gcd(a,c)!=1)
						return -4;
					if(a>=b)
						return -7;
					*/
					cc += c;
					//break;
				}
			}
		}
	}

	int s = 0;
	for(int i=1;i<lim;++i){
		int rad = 1;
		for(int d=0;d<divl[i].nbDiv;++d){
			for(int u=0;u<divl[i].dividers[d].second;++u)
				rad *= divl[i].dividers[d].first;
		}
		if(rad != i){
			std::cout << "Nop"<< i << std::endl;
		}
		s += rad;
	}

	std::cout << s << std::endl;
	std::cout << cc << std::endl;

	return 0;
}
