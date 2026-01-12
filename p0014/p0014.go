/*
p14
*/

package main
import (
	"fmt"
)

var cache [1000000]int

func collatz(n int) int {
	if n < 1000000 && cache[n] != -1 {
		return cache[n];
	}else if n%2 == 0 {
		return collatz(n/2)+1
	}else{
		return collatz(3*n+1)+1
	}
}

func main(){
	for i:=1;i<1000000;i++{
		cache[i] = -1
	}
	cache[1] = 1
	maxx, ans := 0, 1

	for i:=1;i<1000000;i++{
		c := collatz(i)
		if c > maxx {
			ans = i
			maxx = c
		}
	}

	fmt.Printf("Ans: %v\n", ans)
}
