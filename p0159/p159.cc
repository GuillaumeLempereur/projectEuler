#include <iostream>
#include <set>
#include <algorithm>
#include <map>
#include <list>
#include <tuple>
#include <vector>
#include "primesBelow1M.h"

/*
 * p159
 * */

std::vector<std::vector<int>> facto;

int drs(int n){
	int r = 0;
	while(n>0){
		r += n%10;
		n /= 10;
	}
	if(r >= 10)
		return drs(r);
	return r;
}

// v the vector of factors, n the number to factorize
void factorize(std::vector<int> &v, int n){
	if(facto[n].size()>0){
		v.insert(v.end(), facto[n].begin(), facto[n].end());
		return;
	}
	for(int i=0;i<nbPrim1M;++i){
		int p = primesBelow1M[i];
		if(n%p==0){//found a prime factor
			v.push_back(p);
			factorize(v, n/p);
			return;
		}
	}
}

int main(int args, char *argv[]){
	int LIM = 1000000;
	bool nb[1000000];
	char DRS[1000000];
	short sdrs[1000000];
	std::map<int, std::map<int, bool>> pairs;
	std::map<int, std::map<int, std::map<int, bool>>> triplets;
	for(int i=0;i<LIM;++i){
		nb[i] = false;
		sdrs[i] = 0;
		DRS[i] = drs(i);
		facto.push_back(std::vector<int>());
	}
	int cc = 0, ccc = 0, cnt = 0;
	std::vector<int> fs;
	for(int i=0;i<nbPrim1M;++i){
		int p1 = primesBelow1M[i];
		fs.push_back(p1);
		facto[p1] = std::vector<int>(fs);
		unsigned long long int n = p1;
		nb[n] = true;
		sdrs[n] = DRS[n];
		for(int j=i;j<nbPrim1M;++j){
			int p2 = primesBelow1M[j];
			unsigned long long int n2 = n * p2;
			if(n2 >= LIM)
				break;
			fs.push_back(p2);
			facto[n2] = std::vector<int>(fs);
			nb[n2] = true;
			sdrs[n2] = DRS[p1] + DRS[p2];
			if(DRS[n2] > sdrs[n2]){
				sdrs[n2] = DRS[n2];
				cc++;
				pairs[p1][p2] = true;
			}
			for(int k=j;k<nbPrim1M;++k){
				int p3 = primesBelow1M[k];
				unsigned long long int n3 = n2 * p3;
				if(n3 >= LIM)
					break;
				fs.push_back(p3);
				facto[n3] = std::vector<int>(fs);
				nb[n3] = true;
				sdrs[n3] = std::max(DRS[p1]+DRS[p2]+DRS[p3],
						std::max(DRS[p1*p2]+DRS[p3],
						std::max(DRS[p2*p3]+DRS[p1], DRS[p1*p3]+DRS[p2])));
				if(DRS[n3] > sdrs[n3]){
					sdrs[n3] = DRS[p1*p2*p3];
					//std::cout << p1 << "\t" << p2 << "\t" << p3 << std::endl;
					ccc++;
					triplets[p1][p2][p3] = true;
				}
				
				for(int l=k;l<nbPrim1M;++l){
					int p4 = primesBelow1M[l];
					unsigned long long int n4 = n3 * p4;
					if(n4>=LIM)
						break;
					fs.push_back(p4);
					facto[n4] = std::vector<int>(fs);
					for(int m=l;m<nbPrim1M;++m){
						int p5 = primesBelow1M[m];
						unsigned long long int n5 = n4 * p5;
						if(n5>=LIM)
							break;
						fs.push_back(p5);
						facto[n5] = std::vector<int>(fs);
						for(int n=m;n<nbPrim1M;++n){
							int p6 = primesBelow1M[n];
							unsigned long long int n6 = n5 * p6;
							if(n6>=LIM)
								break;
							fs.push_back(p6);
							facto[n6] = std::vector<int>(fs);
							fs.pop_back();
						}
						fs.pop_back();
					}
					fs.pop_back();
				}
				fs.pop_back();
			}
			fs.pop_back();
		}
		fs.pop_back();
	}
	int c = 0;
	for(int i=1;i<LIM;++i){
		if(facto[i].size()>0){
			//c++;
		}else{
			std::vector<int> v;
			factorize(v, i);
			if(i==9570){
				std::cout << "Before sort: ";
				for(int j=0;j<v.size();++j)
					std::cout << v[j] << ", ";
				std::cout << std::endl;
			}
			std::sort(v.begin(), v.end());
			if(i==9570){
				std::cout << "After sort: ";
				for(int j=0;j<v.size();++j)
					std::cout << v[j] << ", ";
				std::cout << std::endl;
			}
			facto[i] = v;
			//c++;
		}
	}

	
	for(int i=2;i<LIM;++i){
		if(nb[i]){
			if(sdrs[i] == 0){
				std::cout <<"p\t"<< i << std::endl;
				return -4;
			}
			continue;
		}
		// try combine pairs
		int sum = 0;
		for(int j=0;j<facto[i].size();++j){
			int p1 = facto[i][j];
			if(pairs.find(p1) == pairs.end())
				continue;

			for(int k=j+1;k<facto[i].size();++k){
				int p2 = facto[i][k];
				if(pairs[p1].find(p2) == pairs[p1].end())
					continue;
				// combine
				sum = std::max(sum, sdrs[p1*p2] + sdrs[i/p1/p2]);
			}
		}
		
		// try combine triplets
		for(int j=0;j<facto[i].size();++j){
			int p1 = facto[i][j];
			if(triplets.find(p1) == triplets.end())
				continue;
			for(int k=j+1;k<facto[i].size();++k){
				int p2 = facto[i][k];
				if(triplets[p1].find(p2) == triplets[p1].end())
					continue;
				for(int l=k+1;l<facto[i].size();++l){
					int p3 = facto[i][l];
					if(triplets[p1][p2].find(p3) == triplets[p1][p2].end())
						continue;

					// combine
					sum = std::max(sum, sdrs[p1*p2*p3] + sdrs[i/p1/p2/p3]);
				}
			}
		}
		if(sum == 0) // no combination useful
			for(int j=0;j<facto[i].size();++j)
				sum += DRS[facto[i][j]];
		sdrs[i] = sum;
	}

	for(int i=2;i<LIM;++i){
		c += sdrs[i];
		//std::cout << i << "\t" << (int)(sdrs[i]) << std::endl;
	}
	std::cout << c << std::endl;

	return 0;
}
