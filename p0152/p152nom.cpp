/*
Problem 152
Writing 1/2 as a sum of inverse squares

idea: recursive function, take it or pass to the next with check if still possible

Need to remove the cases where it's almost 1/2: should compute cs perfectly
No memory!
*/

#include <iostream>
#include <ctime>
#include <vector>

/*
# Python stat
# before Frac
# 30 => 4.5s, 31: 8.73s, 32: 16.22s,... 35: 107.4s no answer
# after Frac
# 30 => 18s
*/

#define LIM 35

double revcumsum[LIM+1];

class Frac{
    int n, d;
	int gcd(int a, int b){
	    return b == 0 ? a : gcd(b, a % b);
    }

public:
    Frac(int num, int den) : n(num),d(den){}

	int num() const{
		return n;
	}
	int den() const{
		return d;
	}

	Frac& operator+=(const Frac& rhs){
		n = n * rhs.d + d * rhs.n;
        d =  n * rhs.d;
		if(n==0)
			this->d = 1;
		n /= gcd(n,d);
		d /= gcd(n,d);
		return *this;
	}

	operator double(){
		if(d==0)
			std::cerr << "Fuck /0" << std::endl; // not the PB
		else
			return n/d;

	}
};

std::ostream& operator<< (std::ostream& out, const Frac& f){
    return out << f.num() << '/' << f.den();
}

std::ostream& operator<< (std::ostream& out, std::vector<bool>& vec){
    for(std::vector<bool>::const_iterator it=vec.begin();it!=vec.end();++it)
        out << *it << ' ';
    return out;
}

Frac operator+(Frac lhs, const Frac& rhs){
    return lhs += rhs;
}

/*
	lf: list of frac for generating 1/2
	cs: current sum, sum of the lf
	n: the new frac (1/n) to append to the list or not
*/
void genHalf(Frac cs, int n){
    //std::cout << n << std::endl;
    if(n > LIM || 1/2 - (double)(cs) > revcumsum[n])
        return; // impossible to achieve 1/2

    if(cs.num() == 1 && cs.den() == 2){// may be should put a tol
        std::cout << cs << std::endl;
        return;
	}

    genHalf(cs, n + 1);
    if((double)(cs) <= 1/2-1/(n*n)){
        genHalf(cs + Frac(1,n*n), n + 1);
	}
}

int main(int argc, char *argv[]){
	std::clock_t begin = clock();

	revcumsum[LIM] = 1/(LIM*LIM);
    for(int i=LIM;i>=2;--i)
        revcumsum[i] = revcumsum[i+1]+1/(i*i);

	genHalf(Frac(0,1),2);

	std::clock_t end = clock();
	double elapsed_secs = double(end - begin) / CLOCKS_PER_SEC;
	std::cout << elapsed_secs << " elapsed time" << std::endl;
	return 0;
}
