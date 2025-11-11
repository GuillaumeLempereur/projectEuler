#include <stdio.h>
#include <stdlib.h>

// a greater than b
int GCD(int a, int b){
	while(b>0){
		a = b;
		b = a%b;
	}
	return a;
}

int main(int args,char **argv){
	long limit = 100000000;
	long result = 0;
	char *p;
	long mlimit = strtol(argv[1], &p, 10);//7071; //(long)Math.Sqrt(limit / 2);

	mlimit = 10;
	for (long m = 2; m < mlimit; m++) {
		for (long n = 1; n < m; n++) {
			if (((n + m) % 2) == 1 && GCD(m,n) == 1) {
				long a = 2 * m * n;
				long b = m * m - n * n;
				long c = m * m + n * n;
				long p = a + b + c;

				if(b < a){
					long t = a;
					a = b;
					b = t;
				}

				if(c % (b-a) == 0)
					result += limit / p;
			}
		}
	}

	printf("%d %d %d\n",10%6,10%-6,4%1);
	printf("%ld\n",mlimit);
	printf("%ld\n",result);

	return 0;
}
