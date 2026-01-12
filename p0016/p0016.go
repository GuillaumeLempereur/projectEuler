/*
p16
*/

package main
import (
	"fmt"
	"math/big"
)

func main() {
	lim := 1000

	//n = 2**1000
	n := big.NewInt(0)
	n.Exp(big.NewInt(2), big.NewInt(int64(lim)), nil)

	r := new(big.Int)
	ans := 0

	for n.Cmp(big.NewInt(0)) == 1{
		n.DivMod(n, big.NewInt(10), r)
		ans += int(r.Int64())
	}

	fmt.Printf("Ans: %v\n", ans)
}
