#include <iostream>
//#include <pair>
#include <map>
#include <cstdlib>

int main(int args, char **argv){
	int lim = 100;
	lim = atoi(argv[1]);
	std::map<long long,int> sq;

	for(long long i=0;i<25000000;++i)
		sq.insert(std::pair<long long,int>(i*i,i));
	
	std::cout << "Square loaded" << std::endl;


	int c = 0;
	for(long long r=1;r<lim;++r){
		for(long long d=r+1;d<lim;++d){
			long long rdcub = r*d*d*d;
			std::map<long long,int>::iterator it = sq.find(rdcub);
			if(it != sq.end()){
				long long asq = it->second + r;
				//std::cout << r << " " << d << " " << it->second << " " << asq << " " << std::endl;
				std::map<long long,int>::iterator it2 = sq.find(asq);
				if(it2 != sq.end()){
					long long a = it2->second;
					std::cout << r << " " << d << " " << a << " " << std::endl;
				}
				//c++;
			}
		}
	}
	std::cout << c << std::endl;

	return 0;
}
