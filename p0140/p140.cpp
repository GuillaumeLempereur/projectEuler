#include <iostream>
#include <cmath>
#include <unordered_set>

int gcd(int a, int b){
	while(b>0){
		int tmp = a;
		a = b;
		b = tmp%b;
	}
	return a;
}

int main(int args, char **argv){
	std::unordered_set<unsigned long long int> set_odd, set_even;
	int lim = 20000000;
	unsigned long long int t = 0;
	for(unsigned long long int i=1;t<5*lim;++i){
		t = i*10+2;
		if(t%11==0)
			continue;
		//if(m%5==0)
		set_even.emplace(t*t);
		t = i*10+7;
		if(t%11==0)
			continue;
		set_odd.emplace(t*t);
	}

	std::cout << "p q n t z" << std::endl;
	int c = 1;
	unsigned long long int z = 1;
	for(unsigned long long int i=1;z<lim;++i){
		z = 2*i;
		if(set_even.end() != set_even.find(5*z*z+44)){
			unsigned long long int t = sqrt(5*z*z+44)+0.1, n = t-7,p, q, d;
			if(n==0||n%5!=0)
				continue;
			n /= 5;
			p = z-n-1;
			q = 2*(n+3);
			d = gcd(p,q);
			std::cout << c++ << " " << p/d << " " << q/d << " " << n << " " << t << " " << z << std::endl;
		}
		z = 2*i+1;
		if(set_odd.end() != set_odd.find(5*z*z+44)){
			unsigned long long int t = sqrt(5*z*z+44)+0.1, n = t-7,p, q, d;
			if(n==0||n%5!=0)
				continue;
			n /= 5;
			p = z-n-1;
			q = 2*(n+3);
			d = gcd(p,q);
			std::cout << c++ << " " << p/d << " " << q/d << " " << n << " " << t << " " << z << std::endl;
		}

	}
	return 0;
}
