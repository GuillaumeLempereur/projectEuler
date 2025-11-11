#include <iostream>


int LEN = 20, i = 0, nbL = 0, cc = 0;
char arr[31] = "000000000000000000000000000000";

void f(){
    if(i < LEN){
        if(nbL<1){
            arr[i++] = 'L';
            nbL += 1;
            f();
            i--;
            nbL--;
        }
        if (i < 2 || arr[i-2] != 'A' or arr[i-1] != 'A'){
            arr[i++] = 'A';
            f();
            i--;
        }
        arr[i++] = 'O';
        f();
        i--;
    }else{
        cc++;
	//std::cout << arr << std::endl;
    }
}

int main(int args, char **argv){

	LEN = std::atoi(argv[1]);
    f();
    std::cout << LEN << " " << cc << std::endl;

    return 0;
}
