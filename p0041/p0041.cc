/*
 * p0041
 *
 * if the sum of the digit is %3 then divisible by 3
 * so reject 9-digit (45) and 8-digit (36)
 * last digit must be 1 or 3 or 7 otherwise disible by 2 or 5
*/

#include <iostream>
#include <vector>
#include "../euler.h"

int max = 0;

int rec(std::vector<int> &digits, int n){
	if(digits.size()==0){
		if(is_prime_mr(n) && n > max)
			max = n;
	}
	std::vector<int> newDigits;
	for(int i=0;i<digits.size();++i){
		newDigits.assign(digits.begin(), digits.begin()+i);
		newDigits.insert(newDigits.begin(), digits.begin()+i+1, digits.end());
		rec(newDigits, n*10+digits[i]);
	}
	return 0;
}

int main(){
	std::vector<int> digits = {7,6,5,4,3,2,1};
	rec(digits, 0);

	std::cout << "Ans: " << max << std::endl;

	return 0;
}
