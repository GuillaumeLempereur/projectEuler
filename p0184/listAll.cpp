#include <iostream>
#include <fstream>
#include <string>
#include <chrono>
#include <ctime>
#include <ratio>
#include <set>
#include <iterator>
#include <vector>
#include <utility>
#include <algorithm>

std::ostream& operator<<(std::ostream &out, const std::pair<int, int> &p) {
    out << "(" << p.first << ";" << p.second << ")";
    return out;
}
template<typename POD>
void serialize(std::string& fileName, std::vector<POD> const& v){
	// this only works on built in data types (PODs)
	static_assert(std::is_trivial<POD>::value && std::is_standard_layout<POD>::value,
		"Can only serialize POD types with this function");

	std::ofstream outfile{fileName, std::ios::binary};
	auto size = v.size();
	outfile.write(reinterpret_cast<char const*>(&size), sizeof(size));
	outfile.write(reinterpret_cast<char const*>(v.data()), v.size() * sizeof(POD));
	outfile.close();
}

inline int dst(int x, int y, int d){
	return x*x+y*y >= d*d;
}

int main(int args, char **argv){
	/*
	 * p184 Brute Force vector
	 *
	 * test to list unique shape
	 * list all possible triangles : ex: 3 -> 360
	 *
	 * size: 2 : 8
	 * size: 3 : 360
	 * size: 4 :
	 * size: 5 : 10600
	 *
	 * size: 10: 1101232 TBC
	 * size: 15: 13638120 TBC
	 * size: 25: 300344032 TBC (1.36604s)
	 * size: 30: 913888744 TBC 
	 * size: 105: 
	 *
	*/

	std::set<std::string> s;
	std::vector<int> listIsoBig;
	std::vector<int> listEquiLat;
	std::vector<int> listIsoSmall;
	std::vector<int> listAny;
	std::vector<int> listAll;
	int lim = 2, cnt = 0;
	if(args==2)
		lim = std::atoi(argv[1]);

	std::chrono::high_resolution_clock::time_point start = std::chrono::high_resolution_clock::now();

// ax <= bx <= cx
for(int ax=1-lim;ax<lim;ax++){
	for(int ay=1-lim;ay<lim;ay++){
		if(dst(ax, ay, lim))
			continue; // ax*ax+ay*ay < lim*lim : maybe split in 2 ; 0 lim, -lim 0
		for(int bx=ax;bx<lim;++bx){
			int byMax = lim;
			if(bx==ax)
				byMax = ay;
			for(int by=1-lim;by<byMax;++by){
				if(dst(bx, by, lim))
					continue;
				int ABxAO = (bx-ax)*-ay+ax*(by-ay); // AB x AO
				if(ABxAO==0)
					continue;
				for(int cx=std::max(bx,1);cx<lim;++cx){
						int cyMax = lim;
						if(bx==cx)
							cyMax = by;
					for(int cy=1-lim;cy<cyMax;++cy){
						if(dst(cx, cy, lim))
							continue;
						if(((cx-ax)*-ay+ax*(cy-ay)) * ABxAO  >= 0) // AC x AO &&  AB x AO opposite sign != 0
							continue;
						if(((ax-cx)*-cy+cx*(ay-cy)) * ((bx-cx)*-cy+cx*(by-cy)) >= 0) // CA x CO &&  CB x CO opposite sign != 0
							continue;
						cnt++;
						int dA = ax*ax+ay*ay;
						int dB = bx*bx+by*by;
						int dC = cx*cx+cy*cy;
						//if(dA==dB && dB==dC)
						//std::cout << "\t("<< ax << ";" << ay << ")" << "("<< bx << ";" << by << ")" << "("<< cx << ";" << cy << ")" << std::endl;

						std::pair<int, int> A(ax, ay), B(bx, by), C(cx, cy);
						std::vector<std::pair<int, int>> ptsLst = {A, B, C};
						//std::sort(ptsLst.begin(), ptsLst.end());
						//std::cout << ptsLst[0] << ptsLst[1] << ptsLst[2] << std::endl;

						std::vector<int> tri = {ax, ay, bx, by, cx, cy};

						if(dA==dB && dB==dC){
							listEquiLat.insert(listEquiLat.end(), tri.begin(), tri.end());
						//std::cout << ptsLst[0] << ptsLst[1] << ptsLst[2] << std::endl;
	//for(auto i: listEquiLat)
	//	std::cout << i << " ";
	//std::cout << std::endl;
						}
						else if((dA==dB && dA > dC) || (dA==dC && dA>dB) || (dB==dC && dC>dA))
							listIsoBig.insert(listIsoBig.end(), tri.begin(), tri.end());
						else if((dA==dB && dA < dC) || (dA==dC && dA<dB) || (dB==dC && dC<dA))
							listIsoSmall.insert(listIsoSmall.end(), tri.begin(), tri.end());
						else{
							listAny.insert(listAny.end(), tri.begin(), tri.end());
						//std::cout << ptsLst[0] << ptsLst[1] << ptsLst[2] << std::endl;
						}
						listAll.insert(listAll.end(), tri.begin(), tri.end());
					}
				}
			}
		}
	}
}

	std::chrono::high_resolution_clock::time_point end = std::chrono::high_resolution_clock::now();
	std::chrono::duration<double> time_span = std::chrono::duration_cast<std::chrono::duration<double>>(end - start);
	//std::cout << "Duration: " << time_span.count() << "s" << std::endl;
	std::cout << "size EquiLat "<< listEquiLat.size()/6 << std::endl;
	std::cout << "size Iso big "<< listIsoBig.size()/6 << std::endl;
	std::cout << "size Iso small "<< listIsoSmall.size()/6 << std::endl;
	std::cout << "size Any "<< listAny.size()/6 << std::endl;
	std::cout << "size All "<< listAll.size()/6 << std::endl;

	std::cout << "size "<<  lim << " : " << cnt << std::endl;

	std::string fileName1 = std::string("equiLat_")+std::to_string(lim);
	std::string fileName2 = std::string("isoBig_")+std::to_string(lim);
	std::string fileName3 = std::string("isoSmall_")+std::to_string(lim);
	std::string fileName4 = std::string("any_")+std::to_string(lim);
	std::string fileName5 = std::string("all_")+std::to_string(lim);
	serialize(fileName1, listEquiLat);
	serialize(fileName2, listIsoBig);
	serialize(fileName3, listIsoSmall);
	serialize(fileName4, listAny);
	serialize(fileName5, listAny);

	/*
	for(auto i: listEquiLat)
		std::cout << i << " ";
	std::cout << std::endl;
*/
return 0;
}
