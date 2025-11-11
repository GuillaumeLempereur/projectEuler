#include <iostream>
#include <math.h>
//#include <boost/multiprecision/cpp_int.hpp>

//using namespace boost::multiprecision;


int main(){
	unsigned long long int lim = 10000, cc = 0;

	std::cout << "a" << " " << "d" << " " << "q" << " " << " " << "r" << " " << "cb" <<std::endl;
	for(unsigned long long int a=1;a<lim;++a){
		for(unsigned long long int r=1;r<a;++r){
			unsigned long long int cb = (a*a-r)*r;
			double ad = a, rd = r;
			unsigned long long int q = (unsigned long long int)(round(cbrt((ad*ad-rd)*rd)));

			unsigned long long int d = (a*a-r)/q;
			if(q*q*q==cb)
				std::cout << a << " " << d << " " << q << " " << r << " " << cb <<std::endl;
			//cc++;
		}
	}
	std::cout << cc << std::endl;
	return 0;
}
