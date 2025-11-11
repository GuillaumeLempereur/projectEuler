#include <utility>
#include <cstring>

/*
class Divider{
public:
	std::pair<int,int> dividers[10];
	int nbDiv = 0;

	Divider(){
	}

	void addDiv(int divider, int exp){
		dividers[nbDiv++] = std::make_pair(divider,exp);
	}
};
*/

// calcul a^n%mod
size_t power(size_t a, size_t n, size_t mod);

// n−1 = 2^s * d with d odd by factoring powers of 2 from n−1
bool witness(size_t n, size_t s, size_t d, size_t a);

bool is_prime_mr(size_t n);

int factorize(int i,int *primes, std::pair<int,int> *div);

size_t gcd(size_t a, size_t b);
