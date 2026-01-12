/*
p20
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
	n := fac(100)

	r := new(big.Int)
	ans := 0

	for n.Cmp(big.NewInt(0)) == 1{
		n.DivMod(n, big.NewInt(10), r)
		ans += int(r.Int64())
	}

	fmt.Printf("Ans: %v\n", ans)
}
