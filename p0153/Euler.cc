#include <iostream>
#include <map>
#include <iterator>

// From https://github.com/t3nsor/codebook/blob/master/pollard-rho.cpp

namespace Euler{

typedef long long unsigned int llui;
typedef long long int lli;
typedef long double float64;

llui pow(llui n, int power){
	if(power==0)
		return 1;
	return n*pow(n, power-1);
}

llui mul_mod(llui a, llui b, llui m){
   llui y = (llui)((float64)a*(float64)b/m+(float64)1/2);
   y = y * m;
   llui x = a * b;
   llui r = x - y;
   if ( (lli)r < 0 ){
      r = r + m; y = y - 1;
   }
   return r;
}

llui C,a,b;
llui gcd(llui a, llui b){
   llui c;
   if(a>b){
      c = a; a = b; b = c;
   }
   while(1){
      if(a == 1LL) return 1LL;
      if(a == 0 || a == b) return b;
      c = a; a = b%a;
      b = c;
   }
}

llui f(llui a, llui b){
   llui tmp;
   tmp = mul_mod(a,a,b);
   tmp+=C; tmp%=b;
   return tmp;
}

llui pollard(llui n){
   if(!(n&1)) return 2;
   C=0;
   llui iteracoes = 0;
   while(iteracoes <= 1000){
      llui x,y,d;
      x = y = 2; d = 1;
      while(d == 1){
          x = f(x,n);
          y = f(f(y,n),n);
          llui m = (x>y)?(x-y):(y-x);
          a = m; b = n; d = gcd(a, b);
      }
      if(d != n)
          return d;
      iteracoes++; C = rand();
   }
   return 1;
}

llui pot(llui a, llui b, llui c){
   if(b == 0) return 1;
   if(b == 1) return a%c;
   llui resp = pot(a,b>>1,c);
   resp = mul_mod(resp,resp,c);
   if(b&1)
      resp = mul_mod(resp,a,c);
   return resp;
}

// Rabin-Miller primality testing algorithm
bool isPrime(llui n){
   llui d = n-1;
   llui s = 0;
   if(n <=3 || n == 5) return true;
   if(!(n&1)) return false;
   while(!(d&1)){ s++; d>>=1; }
   for(llui i = 0;i<32;i++){
      llui a = rand();
      a <<=32;
      a+=rand();
      a%=(n-3); a+=2;
      llui x = pot(a,d,n);
      if(x == 1 || x == n-1) continue;
      for(llui j = 1;j<= s-1;j++){
         x = mul_mod(x,x,n);
         if(x == 1) return false;
         if(x == n-1)break;
      }
      if(x != n-1) return false;
   }
   return true;
}
// factors is an empty map reference, n is a positive integer
// factors[p] is the exponent of p in prime factorization of n
void fact(std::map<llui,int> &factors, llui n){
   if(!isPrime(n)){
      llui fac = pollard(n);
      fact(factors, n/fac);
	  fact(factors, fac);
   }else{
	   std::map<llui,int>::iterator it;
      it = factors.find(n);
      if(it != factors.end()){
         (*it).second++;
      }else{
         factors[n] = 1;
      }
   }
}

int main(int agrs, char **argv){
	int n = std::atoi(argv[1]);

	std::map<llui,int> factors;
	fact(factors, n);

	for(std::map<llui, int>::const_iterator it=factors.begin();it!=factors.end();++it){
		std::cout << it->first << " " << it->second << std::endl;
	}

	return 0;
}

} // namespace Euler
