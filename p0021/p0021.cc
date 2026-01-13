/*
 * p21
*/
#include <iostream>
#include <vector>
#include "../euler.h"
#include "../primesBelow1M.h"

int main(){
	int LIM = 10000;

	int d[10000];

	for(int i=1;i<LIM;++i){
		std::vector<int> lst;
		lstDiv(i, primesBelow1M, lst);
		
		d[i] = -i;//remove the number which is also a divider
		for(const auto &f : lst){
			d[i] += f; // add all divisors
		}
	}

	int s = 0;
	for(int i=1;i<LIM;++i){
		int n = d[i];
		if(n < LIM && i == d[n] && n != i)
			s += i;
	}

	std::cout << "Ans: " << s << std::endl;

	return 0;
}
