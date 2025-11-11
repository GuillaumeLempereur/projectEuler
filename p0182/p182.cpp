//P182
//
#include <iostream>
#include <vector>
#include <iomanip>
#include <numeric>
#include <cstdlib>
#include <ctime>

// not the answer but quite close
// check middle
/*
 * quite Brute force : try every e expecting those 5 m are removing the non optimal e
*/

long long expMod(unsigned long long base, unsigned long long exp, unsigned long long mod) {
	unsigned long long res = 1;
	while(exp > 0){
		if(exp % 2 == 1)
			res= (res * base) % mod;
		exp = exp >> 1;
		base = (base * base) % mod;
	}
	return res;
}

int main(int args, char **argv){
	//std::cout << std::fixed << std::setprecision(6);

	unsigned long long p = 1009, q = 3643;
	int BL_NB = 5;
	unsigned long long blackList[5] = {3642, 33210, 73282, 116575, 1225936};

	int lim = 10;
	if(args == 3){
		p = atoi(argv[1]);
		q = atoi(argv[2]);
	}
	unsigned long long n = p*q, phi = (p-1)*(q-1), m = 0, c = 0, e = 7;
	unsigned long long e_tt = 0;
	std::cout << p << " " << q << " " << n << " " << phi << std::endl;
	
	std::vector<int> es, e_cc(phi);
	std::vector<std::vector<int>>  e_unc(phi);
	int es_length = 0;

	if(args==2)
		lim = atoi(argv[1]);
	else
		lim = phi;
	int ccc = 0;
	std::cout << "Start " << std::endl;
	for(e=3;e<lim;e+=2){
		if(std::gcd(e,phi)!=1)
			continue;

		// Black List
		int skip = 0;
		for(int i=0;i<BL_NB;++i)
			if(blackList[i] == expMod(blackList[i], e, n)){
				skip = 1;
				break;
			}
		if(skip)
			continue;

		int cc = 0;
		//es[es_length++] = e;
		//e_cc[e] = 0;
		
		/*
		//for(m=0;m<n/2;m++){
		for(m=n/3;m<n/2;m++){
			c = expMod(m, e, n);
			if(c==m){
				std::cout << m << " ";
				//e_unc[i+1].push_back(m);
				cc++;
			}
		}

		std::cout << std::endl;
		std::cout << e << " " << cc << std::endl;
		*/
		e_tt += e;
		ccc++;
	}
	std::cout << e_tt << std::endl;
	std::cout << ccc << std::endl;

  return 0;
}
