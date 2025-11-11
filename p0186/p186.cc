#include <iostream>
#include <cstdlib>
#include <string>

/*
 * p186
 * args: number percentage
 * ex: 524287 0.99
 * */

constexpr int RANGE = 1000000;

struct Node{
	int n=0; // number
	struct Node *next = nullptr;
};

struct List{
	int size=0; // list size
	struct Node *head = nullptr;
	struct Node *tail = nullptr;
};

List lN[RANGE]; // for each number => list that contains it
int pl[RANGE]; // list pointer: [c] => index of the list

void print_pl(){
	for(int i=0;i<RANGE;++i)
		std::cout << pl[i] << "\t";
	std::cout << std::endl;
}

void print(){
	for(int i=0;i<RANGE;i++){
		Node *n = lN[pl[i]].head;
		std::cout << i << "\t:\t";
		int c = 0;
		do{
			std::cout << n->n << "\t";
			n = n->next;
			c++;
		}while(n != nullptr && c < 10);
		if(c>=10)
			std::cout << " Fc loop" << std::endl;

	}
}
void merge(List &l1, List &l2){
	if(l2.size > l1.size){ // merge in l1
		merge(l2, l1);
		return;
	}
	int c = 0;
	// merge in l1
	Node *n = l2.head;
	l1.tail->next = l2.head; // append l2 to l1
	l1.tail = l2.tail; // update the new tail of l1
	l1.size = l1.size + l2.size;
	do{ // run through all nodes to update the list pointer
		if(c>10000000){
			std::cout << "loop" << std::endl;
			return;
		}
		pl[n->n] = l1.head->n;
		n = n->next;
		c++;
	}while(n != nullptr);
}

int main(int args, char *argv[]){
	if(args != 3){
		std::cout << "Bad usage: " << argv[0] << " NUMBER PERCENTAGE" << std::endl << "ex: " << argv[0] << " 524287 0.99" << std::endl;
		return -1;
	}
	int pm = std::atoi(argv[1]);
	double percentage = std::atof(argv[2]);
	int lim = 10000000;
	int flSize = percentage*RANGE;
	std::cout << "Find " << pm << " with a fl size: " << flSize << std::endl;


	for(int i=0;i<RANGE;i++){
		lN[i].size = 1;
		lN[i].head = new Node();
		lN[i].tail = lN[i].head;
		lN[i].head->n = i;
		pl[i] = i;
	}

	// if called : caller then they are friends => remove caller : called
	unsigned long long int buff[55];
	
	int caller, called;
	// fill the buffer with the first 55 items
	for(unsigned long long int k=1;k<=55;++k){
		caller = called;
		called = buff[k-1] = (100003-200003*k +300007*k*k*k)%RANGE;
		if(k%2==0){
			if(lN[pl[caller]].head != lN[pl[called]].head){
				merge(lN[pl[called]], lN[pl[caller]]);
			}
		}
	}
	
	caller = buff[54];
	called = buff[0] = (buff[31] + buff[0])%RANGE;
	if(lN[pl[caller]].head != lN[pl[called]].head){
		merge(lN[pl[called]], lN[pl[caller]]);
	}

	int cnt = 29;
	for(int i=29;i<=lim;++i){ // 2*n-1 : 2*n
		int n = 2*i;
		caller = buff[(n-2)%55] = (buff[(n-26)%55] + buff[(n-2)%55])%RANGE;
		called = buff[(n-1)%55] = (buff[(n-25)%55] + buff[(n-1)%55])%RANGE;
		if(caller==called)
			continue;
		
		if(lN[pl[caller]].head != lN[pl[called]].head){
			merge(lN[pl[called]], lN[pl[caller]]);
		}

		if(lN[pl[pm]].size >= flSize){
			std::cout << "ans: " << cnt << std::endl;
			std::cout << "group size: " << lN[pl[pm]].size << std::endl;
			return 0;
		}
		cnt++;
	}
	std::cout << "not found" << std::endl;
	return 0;
}
