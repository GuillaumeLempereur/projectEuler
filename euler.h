#include <utility>
#include <cstring>
#include <vector>
#include <map>

// calcul a^n%mod
size_t power(size_t a, size_t n, size_t mod);

// n−1 = 2^s * d with d odd by factoring powers of 2 from n−1
bool witness(size_t n, size_t s, size_t d, size_t a);

bool is_prime_mr(size_t n);

/*
 * Populate the map factors of n
 * n: number to factorize
 * primes: int array containing the primes below n at min
 * factors: map reference of the factors = {factors: nb of time present in n, ...}
 * */
void factorize(int n, int primes[], std::map<int, int> &factors);

/*
 * Compute the greatest common divisor
 * return gcd(a, b)
 * */
size_t gcd(size_t a, size_t b);

/*
 *  List all the divisors of n
 *  n: the number we want to list the divisors
 *  primes: array containing all the primes at least <= n
 *  lst: reference vector containing the divisors
 * */
void lstDiv(int n, int primes[], std::vector<int> &lst);

/*
 *  Explore recursively the factors of n and populate the divisors of n in lst
 *  d: the divisor to be combined with of factors
 *  lst: reference vector containing the divisors
 *  fs: reference map of the unexplored factors and how many times present in n
 * */
void lstDiv(int d, std::vector<int> &lst, std::map<int,int> &fs);
