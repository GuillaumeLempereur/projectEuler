/*
p160

decompose in:
mul of 2, mul of 5, mul of not 2 and not 5
n_2_5, n5, n2

f(10*x) = n_2_5(10**x) * n5(10**x) * n2(10**x) * n_2_5(10**(x-1)) * n5(10**(x-1)) * n2(10**(x-1) ...
*/

#include <map>
#include <vector>
#include <iterator>
#include <iostream>
#include <gmpxx.h>

typedef unsigned long long int uint64_t;
std::map<mpz_class, std::vector<mpz_class>> dec5, dec2;
std::map<mpz_class, mpz_class> power5, power2, cache;
std::map<mpz_class, std::vector<mpz_class>>::const_iterator itd = dec2.begin();
std::vector<mpz_class>::const_iterator itv;
std::map<mpz_class, mpz_class>::const_iterator itp = power2.begin(), itcache;

void n_2_5o(mpz_class &m, mpz_class &r){
	r = mpz_class(1);
	for(mpz_class i=3;i<m+1;i+=2){
		if(i%5==0)
			continue;
		r *= i;
	}
}

//try an optimization
void n_2_5(mpz_class &m, mpz_class &r){
	r = mpz_class(1);
	if(m%100000==0)
		return;
	if(m>100000){
		mpz_class mm(m%100000);
		n_2_5(mm, r);
		return;
	}
	itcache = cache.find(m);
	if(itcache != cache.end()){
		r = itcache->second;
		return;
	}
	for(mpz_class i=3;i<m+1;i+=2){
		if(i%5==0)
			continue;
		r *= i;
	}
	cache[m] = r;
}

void n5(mpz_class &m, mpz_class &r){
	r = mpz_class(1);
	for(mpz_class i=5;i<m+1;i+=10){
		r *= i;
	}
}

void n2(mpz_class &m, mpz_class &r){
	r = mpz_class(1);
	for(mpz_class i=2;i<m+1;i+=2){
		if(i%5==0)
			continue;
		r *= i;
	}
}

void n5f(mpz_class &m, mpz_class &r, mpz_class &p){
	r = mpz_class(1);
	mpz_class v;
	for(itv=dec5[m].begin();itv!=dec5[m].end();++itv){
		if(*itv <= 1)
			break;
		mpz_class rr(1);
		v = *itv;
		n_2_5(v, rr);
		r *= rr%100000;// TODO TBC
	}
	p = power5[m];
}

void n2f(mpz_class &m, mpz_class &r, mpz_class &p){
	r = mpz_class(1);
	mpz_class v;
	for(itv=dec2[m].begin();itv!=dec2[m].end();++itv){
		if(*itv <= 1)
			break;
		mpz_class rr(1);
		v = *itv;
		n_2_5(v, rr);
		r *= rr%1000000;
	}
	p = power2[m];
}

int main(int args, char *argv[]){
	// dec5 power 5
	for(int i=1;i<13;++i){
		mpz_class su(0);
		mpz_class m(1);
		mpz_ui_pow_ui(m.get_mpz_t(), 10, i);
		for(int p=1;p<19;++p){
			mpz_class p5(1);
			mpz_ui_pow_ui(p5.get_mpz_t(), 5, p);
			mpz_class r(0);
			r = m%(2*p5);
			su += (m-r)/(2*p5);
			if(r>=p5)
				su += 1;
			dec5[m].push_back(m/p5);
		}
		power5[m] = su;
	}

	// dec2 power 2
	for(int i=1;i<13;++i){
		mpz_class su(0);
		mpz_class m(1);
		mpz_ui_pow_ui(m.get_mpz_t(), 10, i);
		for(int p=1;p<41;++p){
			mpz_class p2(1);
			mpz_ui_pow_ui(p2.get_mpz_t(), 2, p);
			su += m/p2 - m/p2/5;
			dec2[m].push_back(m/p2);
		}
		power2[m] = su;
	}

	mpz_class m(1);

	mpz_class r(1);
	for(int i = 0;i<12;++i){
		m *= 10;
		mpz_class r2(1), r5(1), r25;
		mpz_class p2(1), p5(1), pp(1);

		n_2_5(m, r25);
		r25 %= 100000;

		n5f(m, r5, p5);
		r5 %= 100000;

		n2f(m, r2, p2);
		r2 %= 100000;

		mpz_class ddd = p2-p5;
		uint64_t dif;

		if(ddd>10000){
			ddd %= 10000;
			dif = mpz_get_ui(ddd.get_mpz_t());
			mpz_ui_pow_ui(pp.get_mpz_t(), 2, dif);
			r *= (r25 * r5 * r2 * pp * 9376)%100000;
		}else{
			dif = mpz_get_ui(ddd.get_mpz_t());
			mpz_ui_pow_ui(pp.get_mpz_t(), 2, dif);
			r *= (r25 * r5 * r2 * pp)%100000;
		}

		std::cout << i << "\t" << r%100000 << std::endl;
	}

	return 0;
}
