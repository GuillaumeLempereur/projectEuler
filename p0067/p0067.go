/*
p67
*/

package main
import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	fileName := "0067_triangle.txt"
	data, err := os.ReadFile(fileName)
	if err != nil {
		panic(err)
	}

	// Parse the file to populate the numbs 2D slice
	var numbs = [][]int{}
	for r, row := range strings.Split(string(data), "\n"){
		if len(row) == 0 {
			break
		}
		numbs = append(numbs, []int{})
		for _, n := range strings.Split(row, " "){
			i, err := strconv.Atoi(n)
			if err != nil {
				panic(err)
			}
			numbs[r] = append(numbs[r], i)
		}
	}

	depth := len(numbs)

	/*
		Start from penultimate row to the 1st row and choose the highest of the 2 bottom neighbour for each element
	*/
	for i:=depth-2;i>=0;i--{
		for j:=0;j<len(numbs[i]);j++{
			numbs[i][j] += max(numbs[i+1][j], numbs[i+1][j+1])
		}
	}

	fmt.Printf("Ans: %v\n", numbs[0][0])
}
