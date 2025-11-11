#include <bits/stdc++.h>
#include <array>
#include <cstddef>
#include <cstdlib>
#include "Euler.cc"
#include <chrono>
#include <ctime>

/*
 * useless recursive way to list number from 1 to n by prime combination
 * */

using namespace std;

constexpr std::size_t LP_SIZE = 5761455;
std::array<int, LP_SIZE> lp;
std::vector<int> cops; // list of coprimes

void SieveOfEratosthenes(int n){
    // Create a boolean array "prime[0..n]" and initialize
    // all entries it as true. A value in prime[i] will
    // finally be false if i is Not a prime, else true.
    vector<bool> prime(n + 1, true);

    for(int p = 2; p * p <= n; p++) {

        if (prime[p] == true) {
            // Update all multiples of p greater than or
            // equal to the square of it numbers which are
            // multiple of p and are less than p^2 are
            // already been marked.
            for (int i = p * p; i <= n; i += p)
                prime[i] = false;
        }
    }

	int cc = 0;
    // Print all prime numbers
    for (int p = 2; p <= n; p++)
        if (prime[p]){
            lp[cc++] = p; //cout << p << " ";
		}
	std::cout << cc << std::endl;
}

//List of coprimes
std::size_t iMax = 0;
uint64_t n = 42;
uint64_t su = 0; // check size
void cop(uint64_t d, int i){
	//std::cout << "\t" << d << ", n= "<< n << ", i= " << i<< ", lp[i]: "<< lp[i] << std::endl;
    if(i == iMax){
        cops.push_back(d);
        return;
	}
    uint64_t f = lp[i];
    while(d*f*d*f < n){ // cop² < n because cop² + at least 1 <= n
        cop(d*f, i+1);// take it
        f *= lp[i];
	}
	if(d*lp[i]*d*lp[i]>=n){
		cops.push_back(d);
		return;
	}
    cop(d, i+1);// leave it
}

int main(int agrs, char *argv[]){
    int primeBelowN = 100000000;
	std::chrono::high_resolution_clock::time_point start = std::chrono::high_resolution_clock::now(), end;
	std::chrono::duration<double> time_span;
    n = std::atoi(argv[1]);
    SieveOfEratosthenes(primeBelowN);

	std::cout << " n: " << n << std::endl;

	iMax=0;
	while(iMax<LP_SIZE && lp[iMax]<n){
		iMax++;
	}

	if(iMax == LP_SIZE)
		std::cout << "Maybe error" << std::endl;
	std::cout << " iMax: " << iMax << std::endl;
	start = std::chrono::high_resolution_clock::now();

	cop(1, 0);
	std::cout << "cops:" << std::endl;
	std::cout << cops.size() << std::endl << std::endl;
	
	for(int i=0;i<cops.size();++i){
		std::cout << cops[i] << std::endl;
	}
	end = std::chrono::high_resolution_clock::now();
	time_span = std::chrono::duration_cast<std::chrono::duration<double>>(end - start);
	std::cout << "Duration: " << time_span.count() << "s" << std::endl;
	return 0;
}
