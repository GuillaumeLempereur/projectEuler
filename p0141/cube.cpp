#include <iostream>
#include <math.h>
#include <boost/multiprecision/cpp_int.hpp>

using namespace boost::multiprecision;


int main(){
	int128_t lim = 100000, cc = 0;

	std::cout << "a" << " " << "d" << " " << "q" << " " << "cb" <<std::endl;
	for(int ai=1;ai<lim;++ai){
		for(int ri=1;ri<ai;++ri){
			int128_t a = ai, r = ri;
			int128_t cb = (a*a-r)*r;
			double ad = ai, rd = ri;
			int128_t q = (int128_t)(round(cbrt((ad*ad-rd)*rd)));

			int128_t d = (a*a-r)/q;
			if(q*q*q==cb)
				std::cout << a << " " << d << " " << q << " " << cb <<std::endl;
			//cc++;
		}
	}
	std::cout << cc << std::endl;
	return 0;
}
