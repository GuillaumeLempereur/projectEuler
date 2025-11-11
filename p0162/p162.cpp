#include <iostream>
#include <set>
#include <string>
#include <algorithm>
#include <sstream>

long long int pwr(long long int n, int pow){
	long long int r = n;
	while(--pow > 0)
		r *= n;
	return r;
}

long long int nbA10x(int size){
	long long int r = 0;

	r = pwr(16, size) - 3*pwr(15, size) + 3*pwr(14, size) - pwr(13, size);
	while(--size >= 2){ 
		r -= pwr(15, size) - 2*pwr(14, size) + pwr(13, size);
		std::cout << "\t"<< pwr(15, size) - 2*pwr(14, size) + pwr(13, size) << std::endl;
	}

	return r;
}

int main(int args, char **argv){
	/*
	 * Optimized solution
	 *
	*/
	
	std::cout << nbA10x(16) << std::endl;

	std::stringstream stream;
	stream << std::hex << nbA10x(16);
	std::string result(stream.str());
	std::transform(result.begin(), result.end(), result.begin(), ::toupper);
	std::cout << result << std::endl;
	return 0;
}
