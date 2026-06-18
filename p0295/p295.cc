#include <iostream>
#include <map>
#include <set>
#include <tuple>
#include <vector>
#include <chrono>
#include <numeric>
#include <cmath>
#include <algorithm>
#include <format>

/*
 * 14s for 20000
 * use long long int
 * L(10) = 30
 * L(100) = 3442
 * L(1000) = 393451
 * L(10000) = 44336604
 * L(20000) = 182994991 in 11 s
 * L(30000) = 418952079 in 28 s
 * L(50000) = 1188368250 in 84 s
 * L(100000) = ... in 400 s
 *
 * (a+b)%2 == 1 and (c+d)%2 == 1
 * (c-a)%2==1 and (d-b)%2==1 combine only points where a%2 != c%2 and b%2 != d%2 -> 2 ms
 * */

int main(){
	long long int maxR = 100000;
	int cnt = 0;
	int lim = maxR+1;
	constexpr double SQRT2 = std::sqrt(2.0);

	std::set<long long int> sq45;
	long long int mMax;
	for(long long int i=0;i<maxR;++i){
		long long int r = i*i+(i+1LL)*(i+1LL);
		sq45.insert(r);
		if(r > maxR*maxR){
			mMax = i;
			break;
		}
	}

	long long int nb45 = 0;
	for(long long int a=0;a<lim;++a){
		long long int b = a+1LL, r1 = a*a+b*b;
		if(r1 > maxR*maxR)
			break;
		nb45 += mMax-a;
	}
	std::cout << "nb45: " << nb45 << std::endl;

	auto start = std::chrono::high_resolution_clock::now();

	std::multiset<std::tuple<long long int, long long int, long long int>> ms_pair, ms_odd, deltaR; // ms {r², a, b} intersection on cirlce r², deltaR all circles having delta {c-a, d-b, r²}

	// r the radius find (x, y) such  (r-1)² < x²+y² <= r²
	// y min : (r-1)² < y²+y² => (r-1)//2**0.5 < y and y max : y²+0² <= r²
	// x min : (r-1)² < x²+y², x² > (r-1)²-y² and x max : y²+x² <= r², x² <= r²-y²
	for(long long int r=1LL;r<=maxR;++r){
		for(long long int y=(r-1LL)/SQRT2+1LL;y<=r;++y){
			long long int x = 0LL;
			if(y<r){
				x=std::sqrt((r-1LL)*(r-1LL)-y*y)+1LL;
			}
			if(y%2LL==x%2LL)
				x++;
			for(;x<=y;x+=2LL){
				long long int r2 = x*x+y*y;
				if(r2>r*r)
					break;
				cnt++;
				if(x%2LL==0LL)
					ms_pair.insert({r2, x, y});
				else
					ms_odd.insert({r2, x, y});
			}
		}

		// handle the r2 < (y+1)²
		std::multiset<std::tuple<long long int, long long int, long long int>>::iterator i = ms_pair.begin(), j = ms_odd.begin(), jNextStart = ms_odd.begin(); // set of the pairs forming the same sq number
		for(;i!=ms_pair.end();++i){
			long long int r2 = std::get<0>(*i), aa = std::get<1>(*i), bb = std::get<2>(*i);
			// TODO handle pair odd combi
			for(j = jNextStart;j!=ms_odd.end();++j){ // combine all points having same r²
				long long int r2j = std::get<0>(*j), cc = std::get<1>(*j), dd = std::get<2>(*j);
				if(r2j > r2){ // j in advance on i
					break;
				}else if(r2j < r2){
					jNextStart++;
					continue;
				}
				long long int a = aa, b = bb, c = cc, d = dd;
				if(cc < aa){
					a = cc;
					c = aa;
					b = dd;
					d = bb;
				}

				if(std::gcd(d-b, c-a) > 1)
					continue;

				bool isC1Lent = true;

				for(long long int x=(a+c)/2LL;x<c;++x){ // check circle includes at least 1 point of the grid
					long long int y = std::ceil(double((d-b)*(x-a))/double(c-a))+b; //TODO TBC correct formula ?
					if(x*x+y*y < r2){
						isC1Lent = false;
						break;
					}
				}

				if(isC1Lent)
					for(long long int x=(a+c)/2LL-1LL;x>a;--x){ // check circle includes at least 1 point of the grid
						long long int y = std::ceil(double((d-b)*(x-a))/double(c-a))+b; //TODO TBC correct formula ?
						if(x*x+y*y < r2){
							isC1Lent = false;
							break;
						}
					}

				if(!isC1Lent)
					continue;
				deltaR.insert({c-a, d-b, r2});
			}
		}
		ms_pair.clear();
		ms_odd.clear();
	}

	auto stop = std::chrono::high_resolution_clock::now();
	auto duration =  std::chrono::duration_cast<std::chrono::microseconds>(stop - start);
	std::cout << "step 1: " << duration.count()/1000 << " ms" << std::endl;
	start = std::chrono::high_resolution_clock::now();

	std::cout << cnt << std::endl;
	std::cout << "deltaR: " << deltaR.size() << std::endl;
	std::cout << ms_pair.size() << std::endl;
	std::cout << ms_odd.size() << std::endl;
	
	cnt = 0;
	std::multiset<std::tuple<long long int, long long int, long long int>>::iterator i = deltaR.begin(), j;
	std::set<std::pair<long long int, long long int>> s, s3;

	std::set<long long int> dup_r, set_of_r;
	long long int nbW = 0, nbDup=0;// number of non-45 couple; nbr (nb of duplicates)
	
	std::map<std::pair<long long int, long long int>, std::vector<long long int>> mapR;
	std::map<long long int, std::vector<int>> mr2setss; // map r² : [idx of setss]
	std::vector<std::set<long long int>> dupSet; //[[r², r²], [r²]] 

	//Find duplicates
	for(i=deltaR.begin();i!=deltaR.end();++i){
		long long int deltaX = std::get<0>(*i), deltaY = std::get<1>(*i), r2 = std::get<2>(*i);
		if(set_of_r.find(r2) != set_of_r.end()){
			dup_r.insert(r2);
		}else{
			set_of_r.insert(r2);
		}
	}
	for(i=deltaR.begin();i!=deltaR.end();++i){
		long long int deltaX = std::get<0>(*i), deltaY = std::get<1>(*i), r2 = std::get<2>(*i);
		mapR[{deltaX, deltaY}].push_back(r2);
	}

	std::cout << "Nb of dup : " << dup_r.size() << std::endl;
	std::cout << "Nb of r² : " << set_of_r.size() << std::endl;
	std::cout << "mapR size : " << mapR.size() << std::endl;
	long long int ans = 0;

	for(auto p : mapR){
		//std::cout << "(" << p.first.first << ", " << p.first.second <<")\t" << p.second.size() << ": ";
		long long int nbUniq = 0, nb45InSet = 0, nbBoth = 0; // nbUniq = nb of dup :/
		std::set<long long int> setss;
		for(int i=0;i<p.second.size();++i){
			long long int r2 = p.second[i];
			//std::cout << r2 << ", ";
			if(dup_r.find(r2) != dup_r.end()){ // s3 handle the duplicates
				nbUniq++;
				setss.insert(r2);
				mr2setss[r2].push_back(dupSet.size());
			}
			if(sq45.find(r2) != sq45.end()) // s3 handle the duplicates
				nb45InSet++;
			if(dup_r.find(r2) != dup_r.end() && sq45.find(r2) != sq45.end()) // both sq45 and dup
				nbBoth++;
			if(dup_r.find(r2) != dup_r.end() && sq45.find(r2) == sq45.end()){
			}
		}
		dupSet.push_back(setss);
		//std::cout << "setss: " << setss.size() << std::endl;
		long long int si = p.second.size();
		ans += si*(si+1LL)/2LL;
		if(nbUniq != 0){
			ans -= nbUniq*(nbUniq+1LL)/2LL; //remove combination with 2 dup
		}
		if(nb45InSet != 0)
			ans -= nb45InSet*(nb45InSet+1LL)/2LL; //remove combination with 2 45°
		if(nbBoth != 0)
			ans += nbBoth*(nbBoth+1LL)/2LL; //add both

		//std::cout << "nb dup: " << nbUniq << std::endl;
		//std::cout << ": " << nb45InSet << std::endl;
		//std::cout << "pb :" << nb45 << std::endl;
	}
	
	std::set<std::pair<long long int, long long int>> sdTot; // set with all duplicate solutions
	long long int dupc = 0;
	int cnt2 = 0;
	for(auto mr2 : mr2setss){
		long long int r2 = mr2.first;
		std::set<std::pair<long long int, long long int>> sd;
		std::cout << r2 << " " << mr2.second.size() << std::endl;
		//if(sq45.find(r2) == sq45.end()) // s3 handle the duplicates
		//	sdTot.insert({r2, r2});
		for(int i=0;i<mr2.second.size();++i){
			//std::cout << mr2.second[i] << " :";
			std::set<long long int>::iterator it;
			for(it=dupSet[mr2.second[i]].begin();it!=dupSet[mr2.second[i]].end();++it){
				//std::cout << "\t" << dupSet[mr2.second[i]].size() << std::endl;
				if(*it == r2){
					it = dupSet[mr2.second[i]].erase(it);
					if(it == dupSet[mr2.second[i]].end())
						break;
				}
				long long int r = *it;
				if(sq45.find(r2) != sq45.end() && sq45.find(r) != sq45.end()) // s3 handle the duplicates
					continue;
				if(r2<r){
					sd.insert({r2, r});
					//sdTot.insert({r2, r});
				}else{
					sd.insert({r, r2});
				}
				//std::cout << *it <<" ";
			}
			//std::cout << std::endl;
		}
		dupc += (long long int)(sd.size());
		if(sq45.find(r2) == sq45.end()) // {r2, r2} if non-45
			dupc++;
		std::cout << cnt2++ << " /" << mr2setss.size() << std::endl;
	}

	std::cout << "dupSet: " << dupSet.size() << std::endl;
	std::cout << "nb dup: " << mr2setss.size()  << std::endl;
	//std::cout << "Ans : " << nb45 << " + " << ans << " + " << sdTot.size() << " = " << ans + sdTot.size() + nb45 << std::endl;
	std::cout << "Ans : " << nb45 << " + " << ans << " + " << dupc << " = " << ans + dupc + nb45 << std::endl;

	return 0;
}
