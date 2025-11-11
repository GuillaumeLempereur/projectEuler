#include <iostream>
#include <math.h>
#include <boost/multiprecision/cpp_int.hpp>

using namespace boost::multiprecision;


int main(){
	int128_t lim = 2000, cc = 0;

	for(int ai=1;ai<lim;++ai){
		for(int qi=1;qi<ai;++qi){
			int128_t a = ai, q = qi; 
			int128_t sq = a*a*a*a-4*q*q*q;
			double ad = ai, qd = qi; 
			int128_t rt = (int128_t)(round(sqrt(ad*ad*ad*ad-4*qd*qd*qd)));

			if(rt*rt==sq)
				std::cout << a << " " << q << " " << rt << std::endl;
			//cc++;
		}
	}
	std::cout << cc << std::endl;
	return 0;
}
