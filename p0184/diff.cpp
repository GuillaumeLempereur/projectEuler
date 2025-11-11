#include <iostream>
#include <fstream>
#include <cmath>
#include <set>
#include <iterator>
#include <vector>
#include <algorithm>

std::ostream& operator<<(std::ostream &out, const std::pair<int, int> &p) {
    out << "(" << p.first << ";" << p.second << ")";
    return out;
}
template<typename POD>
void deserialize(std::string& fileName, std::vector<POD>& v)
{
	static_assert(std::is_trivial<POD>::value && std::is_standard_layout<POD>::value,
		"Can only deserialize POD types with this function");
	std::ifstream infile{fileName, std::ios::binary};

	decltype(v.size()) size;
	infile.read(reinterpret_cast<char*>(&size), sizeof(size));
	v.resize(size);
	infile.read(reinterpret_cast<char*>(v.data()), v.size() * sizeof(POD));
}

#define _USE_MATH_DEFINES
// is the define usefull ?

using namespace std;

int main(int args, char **argv){
	std::set<std::vector<int>> set1, set2, setDiff;
	std::string pointList;
	int ax = 0, ay = 0, bx = 0, by = 0, cx = 0, cy = 0;
	std::string fileName1("");
	std::string fileName2("");

	if(args != 3)
		return -1;
	fileName1 = std::string(argv[1]);
	fileName2 = std::string(argv[2]);

	std::vector<int> l1, l2;

	deserialize(fileName1, l1);

	/*
	for(auto i: l1)
		std::cout << i << " " ;
	std::cout << std::endl;
	*/
	std::cout << l1.size()/6 << std::endl;
	for(int i=0;i<l1.size()/6;++i){
		//std::pair<int, int> A(l1[6*i], l1[6*i+1]), B(l1[6*i+2], l1[6*i+3]), C(l1[6*i+4], l1[6*i+5]);
		//std::vector<std::pair<int, int>> ptsLst = {A, B, C};
		//set1.insert(ptsLst);
		set1.insert(std::vector<int>({l1[6*i], l1[6*i+1], l1[6*i+2], l1[6*i+3], l1[6*i+4], l1[6*i+5]}));
	}

	deserialize(fileName2, l2);
	int cnt = 0;
	
	std::cout << l2.size()/6 << std::endl;
	for(int i=0;i<l2.size()/6;++i){
		//std::pair<int, int> A(l2[6*i], l2[6*i+1]), B(l2[6*i+2], l2[6*i+3]), C(l2[6*i+4], l2[6*i+5]);
		//std::vector<std::pair<int, int>> ptsLst = {A, B, C};
		//set2.insert(ptsLst);
		set2.insert(std::vector<int>({l2[6*i], l2[6*i+1], l2[6*i+2], l2[6*i+3], l2[6*i+4], l2[6*i+5]}));
	}
	/*
		std::vector<std::pair<int, int>> r90 = {
			std::pair<int, int>(-ay, ax),
			std::pair<int, int>(-by, bx),
			std::pair<int, int>(-cy, cx)};
		std::sort(r90.begin(), r90.end());

		std::vector<std::pair<int, int>> r270 = {
			std::pair<int, int>(ay, -ax),
			std::pair<int, int>(by, -bx),
			std::pair<int, int>(cy, -cx)};
		std::sort(r270.begin(), r270.end());

		std::vector<std::pair<int, int>> r180 = {
			std::pair<int, int>(-ax, -ay),
			std::pair<int, int>(-bx, -by),
			std::pair<int, int>(-cx, -cy)};
		std::sort(r180.begin(), r180.end());

		if(set360.contains(r90))
			cnt++;
		if(set360.contains(r180))
			cnt++;
		if(set360.contains(r270))
			cnt++;
		if(set360.contains(ptsLst))
			cnt++;
		// Making difference 360-U x 4rotations
		set2.insert(r90);
		set2.insert(r180);
		set2.insert(r270);
	}
*/
/*
	std::cout << "List of points that are rotation:" << std::endl;
	int c2 = 0;
	for(std::set<std::vector<std::pair<int,int>>>::const_iterator it=setU.begin(); it!=setU.end();++it){
		int ax = (*it)[0].first, ay = (*it)[0].second, bx = (*it)[1].first, by = (*it)[1].second, cx = (*it)[2].first, cy = (*it)[2].second;
		std::pair<int, int> A(ax, ay), B(bx, by), C(cx, cy);
		std::vector<std::pair<int, int>> ptsLst = {A, B, C};

		std::vector<std::pair<int, int>> r90 = {
			std::pair<int, int>(-ay, ax),
			std::pair<int, int>(-by, bx),
			std::pair<int, int>(-cy, cx)};
		std::sort(r90.begin(), r90.end());

		std::vector<std::pair<int, int>> r270 = {
			std::pair<int, int>(ay, -ax),
			std::pair<int, int>(by, -bx),
			std::pair<int, int>(cy, -cx)};
		std::sort(r270.begin(), r270.end());

		std::vector<std::pair<int, int>> r180 = {
			std::pair<int, int>(-ax, -ay),
			std::pair<int, int>(-bx, -by),
			std::pair<int, int>(-cx, -cy)};
		std::sort(r180.begin(), r180.end());
		
		if(setU.contains(r90)){
			if(ptsLst[0]==r90[0] && ptsLst[1] == r90[1] && ptsLst[2] == r90[2])
				continue;
			std::cout << ptsLst[0] << ptsLst[1] << ptsLst[2] << " < 90> " << r90[0] << r90[1] << r90[2] << std::endl;
		}
		if(setU.contains(r270)){
			if(ptsLst[0]==r270[0] && ptsLst[1] == r270[1] && ptsLst[2] == r270[2])
				continue;
			std::cout << ptsLst[0] << ptsLst[1] << ptsLst[2] << " <270> " << r270[0] << r270[1] << r270[2] << std::endl;
		}
		if(setU.contains(r180)){
			if(ptsLst[0]==r180[0] && ptsLst[1] == r180[1] && ptsLst[2] == r180[2])
				continue;
			std::cout << ptsLst[0] << ptsLst[1] << ptsLst[2] << " <180> " << r180[0] << r180[1] << r180[2] << std::endl;
		}
		
		//if(setU.contains(r90) || setU.contains(r270) || setU.contains(r180))
		//	std::cout << ptsLst[0] << ptsLst[1] << ptsLst[2] << std::endl;
	}
*/
	std::cout << "End list" << std::endl;

	std::cout << set1.size() << std::endl;
	std::cout << set2.size() << std::endl;
	//std::cout << std::endl;
	//std::cout << cnt << std::endl;
	std::cout << std::endl;

	//std::cout << c2 << std::endl;
	//std::cout << std::endl;

	std::cout << "Difference between 1 and 2:" << std::endl;
	std::set_difference(set1.begin(), set1.end(), set2.begin(), set2.end(),std::inserter(setDiff, setDiff.begin()));
	
	for(std::set<std::vector<int>>::const_iterator it=setDiff.begin(); it!=setDiff.end();++it)
		std::cout << "("<< (*it)[0] <<";"<< (*it)[1] <<")("<< (*it)[2]<<";" << (*it)[3] <<")("<< (*it)[4] <<";"<< (*it)[5] <<")"<< std::endl;

	std::cout << "Diff size: " << setDiff.size()/6 << std::endl;

	return 0;
}
