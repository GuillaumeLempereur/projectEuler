#include <stdio.h>
#include <stdlib.h>
#include <math.h>

// not 2252687732
// not 3235417255
int main(int args,char **argv){
	int n[120000] = {0};

	printf("a,b,c,z,y\n");
	int lim = atoi(argv[1]), cc = 0;
	for(long long int a=1;a<lim;++a){
		for(long long int b=1;b<a && a+b<lim;++b){
			long long int csq = (a+b)*(a+b)-a*b;
			long long int c = (long long int)(round(sqrt(csq)));
			if(c*c==csq){

				double ad = a, bd = b, cd = c, s = (ad+bd+cd)*(ad+bd-cd)*(ad+cd-bd)*(bd+cd-ad);
				//long long int s = (a+b+c)*(a+b-c)*(b+c-a)*(a+c-b);
				long long int z = c*c + 3ll*(long long int)(round(sqrt(s/3.0)));
				long long int y = a*a+b*b+4*a*b;
				
				if(z!=y || a+b>lim){
					printf("%lld %lld %lld %lld %lld %lf\n",a,b,c,z,y,s);
					return -5;
				}

				n[a+b] = 1;
				cc++;
			}
		}
	}

	printf("%d\n",cc);
	long long int count = 0;
	cc = 0;
	for(int i=0;i<lim;++i)
		if(n[i]){
			count += i;
			cc++;
		}
	printf("Answer: %lld\n",count);
	printf("%d\n",cc);

	return 0;
}
