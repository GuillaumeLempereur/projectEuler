/*
p22
*/

package main
import (
	"fmt"
	"os"
	"strings"
	"slices"
)

func check(e error) {
    if e != nil {
        panic(e)
    }
}

func main() {
	path := "0022_names.txt"
    dat, err := os.ReadFile(path)
    check(err)

	ans := 0

	namesStr := strings.Replace(string(dat),"\"", "", -1)
	nameLst := strings.Split(namesStr, ",")
	slices.Sort(nameLst)

	for i, name := range nameLst{
		s := 0
		for _, c := range(name){ // compute sum of letters '@' just before 'A'
			s += int(c - '@')
		}
		ans += s*(i+1)
	}

	fmt.Printf("Ans: %v\n", ans)
}
