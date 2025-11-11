// P178
#include <iostream>

int arr[40] = {0};
int i = 0, LIM = 30, cc = 0;

void f(){
	if(i<LIM){
		if(arr[i-1] == 0){
			arr[i++] = 1;
			f();
			i--;
		}else if(arr[i-1] == 9){
			arr[i++] = 8;
			f();
			i--;
		}else{
			arr[i] = arr[i-1] - 1;
			i++;
			f();
			i--;
			arr[i] = arr[i-1] + 1;
			i++;
			f();
			i--;
		}
	}else{
		cc++;
	}
}

int main(){
	
	for(int k=0;k<10;k++){
		i = 1;
		arr[0] = k;
		f();
	}

	std::cout << LIM << " " << cc << std::endl;
	return 0;
}
