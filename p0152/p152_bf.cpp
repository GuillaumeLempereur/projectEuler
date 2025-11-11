/*
Problem 152
Writing 1/2 as a sum of inverse squares

idea: recursive function, take it or pass to the next with check if still possible

Need to remove the cases where it's almost 1/2: should compute cs perfectly

*/

#include <iostream>
#include <ctime>

/*
# Python stat
# before Frac
# 30 => 4.5s, 31: 8.73s, 32: 16.22s,... 35: 107.4s no answer
# after Frac
# 30 => 18s
*/

#DEFINE LIM 30
double revcumsum[LIM+1];
revcumsum[LIM] = 1/(LIM*LIM);

for(int i=lim;i>=2;--i)
    revcumsum[i] = revcumsum[i+1]+1/(i**2)

class Frac{
    int n, d;
	int gcd(int a, int b){ return b == 0 ? a : gcd(b, a % b);}
	
public:
    Frac(num, den):n(num),d(den){}
	
	int num() const{
		return n;
	}
	int den() const{
		return d;
	}
	
	Frac& operator+=(const Frac& rhs){
		n = n * rhs.d + d * rhs.n;
        d =  n * rhs.d;
		n /= gcd(n,d);
		d /= gcd(n,d);
		return *this;
	}
	
    Frac operator+(Frac lhs, const Frac& rhs){
		return lhs *= rhs;
	}

    std::ostream& operator<<(std::ostream& out, const Fraction& f){
		return out << f.num() << '/' << f.den();
	}

	operator double(){
		return n/d;
	}
};

/*
	lf: list of frac for generating 1/2
	cs: current sum, sum of the lf
	n: the new frac (1/n) to append to the list or not
*/
void genHalf(std::vector<bool> lf, Frac cs, int n){
    //print(lf)
    if(n > lim || 1/2 - (double)(cs) > revcumsum[n])
        return; // impossible to achieve 1/2

    if(cs.num() == 1 && cs.den() == 2){// may be should put a tol
        std::cout << cs << " " << lf << std::endl;
        return;
	}

    genHalf(lf, cs, n + 1);
    if((double)(cs) <= 1/2-1/(n**2)){
		lf[n] = 1;
        genHalf(lf,cs + Frac(1,n**2), n + 1);
	}
}

int main(int argc, char *argv[]){
	std::clock_t begin = clock();
	std::vector<bool> lf(47,0);
    
	genHalf(lf,Frac(0,1),2);
	
	std::clock_t end = clock();
	double elapsed_secs = double(end - begin) / CLOCKS_PER_SEC;
	std::cout << elapsed_secs << " elapsed time" << std::endl;
	return 0;
}

//----------------------------------------
/*
 
class Fraction
{
    int gcd(int a, int b) { return b == 0 ? a : gcd(b, a % b); }
    int n, d;
public:
    Fraction(int n, int d = 1) : n(n/gcd(n, d)), d(d/gcd(n, d)) { }
    int num() const { return n; }
    int den() const { return d; }
    Fraction& operator*=(const Fraction& rhs)
    {
        int new_n = n * rhs.n/gcd(n * rhs.n, d * rhs.d);
        d = d * rhs.d/gcd(n * rhs.n, d * rhs.d);
        n = new_n;
        return *this;
    }
};
std::ostream& operator<<(std::ostream& out, const Fraction& f)
{
   return out << f.num() << '/' << f.den() ;
}
bool operator==(const Fraction& lhs, const Fraction& rhs)
{
    return lhs.num() == rhs.num() && lhs.den() == rhs.den();
}
bool operator!=(const Fraction& lhs, const Fraction& rhs)
{
    return !(lhs == rhs);
}
Fraction operator*(Fraction lhs, const Fraction& rhs)
{
    return lhs *= rhs;
}
 
int main()
{
   Fraction f1(3, 8), f2(1, 2), f3(10, 2);
   std::cout << f1 << " * " << f2 << " = " << f1 * f2 << '\n'
             << f2 << " * " << f3 << " = " << f2 * f3 << '\n'
             <<  2 << " * " << f1 << " = " <<  2 * f1 << '\n';
}
*/