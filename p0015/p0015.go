/*
p15
*/

package main
import (
	"fmt"
	"math/big"
)

/*
	Factorial
	return n!
*/
func fac(n int64) *big.Int {
	f := big.NewInt(1)
	for i := int64(1);i<=n;i++ {
		f.Mul(f, big.NewInt(i))
	}
	return f
}

func main() {
	f40 := fac(40)
	f20 := fac(20)

	var ans = big.NewInt(0)
	ans.Div(f40, f20)
	ans.Div(ans, f20)
	
	//compute the permutation of 40 movements 20 down, 20 right
	fmt.Printf("Ans: %v\n", ans)
}
