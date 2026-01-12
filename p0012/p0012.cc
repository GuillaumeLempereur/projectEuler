/*
 * p12
*/
#include <iostream>
#include <vector>

int main(){
	int LIM = 20;
	int divisors[LIM] = {0, 1, 2, 3, 2};

	std::vector<int> primes = {2, 3, 5};

	for(int p=5;p<LIM;p++){
		std::vector<int>::const_iterator it = primes.begin();
		bool isPrime = true;
		while(*it * *it < p){
			if(p%*it == 0){
				isPrime = false;
				divisors[p] = p / *it;
				break;
			}
			it++;
		}
		if(isPrime){
			primes.push_back(p);
			divisors[p] = p;
		}
	}
	for(int i=1;i<LIM;++i){
		std::cout << i << "\t" << divisors[i] << std::endl;
	}
	std::vector<int>::const_iterator it = primes.begin();
	std::cout << primes.size() << std::endl;
/*
n*(n-1)/2 

int div[100] = {0, 1};

for(int n=2;n<LIM;++n){
	
}
*/
	//std::cout << "Ans: " << max << std::endl;

	return 0;
}
