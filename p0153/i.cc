#include <bits/stdc++.h>
#include <array>
#include <cstddef>
#include <cstdlib>
#include "Euler.cc"
#include <chrono>
#include <ctime>

/*
 * p153
 * real part looks working <100
 * 1000:	823081
 * 10000:	82256014
 * 100000:	8224740835
 * 1000000:	seg fault
 *
 * tot:
 * 10**5: 17924657155
 * */

using namespace std;

constexpr std::size_t LP_SIZE = 5761455;
std::array<int, LP_SIZE> lp;


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
        //if d in lp: # case d is prime
        //    su += d+1
        if(d != 1){
            su += (n/d-1)*d;
            //print("\t\t{}".format((n//d-1)*d))
		}
        return;
	}
    cop(d, i+1);// leave it
    uint64_t f = lp[i];
	//std::cout << "\t\t" << f << std::endl;
	if(f == 1)
		return;
    while(d*f <= n/2){
        cop(d*f, i+1);// take it
        f *= lp[i];
	}
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

	cop(1, 0);
	su += (n+1)*n/2+n-1;
	end = std::chrono::high_resolution_clock::now();
	time_span = std::chrono::duration_cast<std::chrono::duration<double>>(end - start);
	std::cout << "Duration real: " << time_span.count() << "s" << std::endl;

	start = std::chrono::high_resolution_clock::now();
	uint64_t gauss_tot = 0;
	//Gaussian divider:
	//list all coprimes then multiply the n//nn TODO
	for(uint64_t a=1;a<n;++a){
		uint64_t nn;
		for(uint64_t b=1;b<a;++b){
			int g = Euler::gcd(a, b);
			nn = a*a+b*b;
			nn /= g; // case coprime
			if(nn > n)
				continue; // can be improved
			gauss_tot += (2*a + 2*b)*(n/nn);
		}
		//case a == b
		nn = a*2;
		if(nn > n)
			break;//continue; // can be improved
		gauss_tot += (2*a)*(n/nn);
	}
	std::cout << "Finish Gaussian" << std::endl;
	uint64_t tot = gauss_tot + su;
	std::cout << "tot\tgauss\treal" << std::endl;
	end = std::chrono::high_resolution_clock::now();
	time_span = std::chrono::duration_cast<std::chrono::duration<double>>(end - start);
	std::cout << "Duration gauss : " << time_span.count() << "s" << std::endl;
	std::cout << tot << "\t" << gauss_tot << "\t"<<su << std::endl;
	return 0;
}
