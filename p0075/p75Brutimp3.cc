#include <iostream>
#include <cstdlib>

typedef signed long long int int64;
int64 squares[320000000] = {0};

int main(int args, char **argv){
	int64 lMax = std::atoi(argv[1]);
	int cnt = 0;
	
	int64 sq, un = 1, mod = 63, div = 64;
	for(int64 i=1;i<100000;++i){
		sq = i*i;
		squares[sq/div] |= un << (sq&mod);
	}
	
	std::cout << "array ok" << std::endl;
//	std::cout << squares[0] << std::endl;

	for(int64 a=1;a<lMax;++a){
		for(int64 b=a+1;b<lMax;++b){
			int64 sq = a*a+b*b;
//			int c = std::sqrt(sq);
			if(squares[sq/div] & (un << (sq&mod))){
				cnt++;
//				std::cout << a << " " << b << " " << c << std::endl;
				}
//			std::cout << a << " " << b << ", ";
		}
//		std::cout << std::endl;
	}

	std::cout << cnt << std::endl;
	return 0;
}
