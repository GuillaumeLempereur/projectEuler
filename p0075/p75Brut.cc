#include <iostream>
#include <cstdlib>
#include <cmath>

int main(int args, char **argv){
	int lMax = std::atoi(argv[1]);
int cnt = 0;
	for(int a=1;a<lMax;++a){
		for(int b=a+1;b<lMax;++b){
			int sq = a*a+b*b;
			int c = std::sqrt(sq);
			if(sq == c*c){
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
