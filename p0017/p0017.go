/*
p17
*/

package main
import (
	"fmt"
)

var numbs = map[int]string{
	1: "one",
	2: "two",
	3: "three",
4: "four",
5: "five",
6: "six",
7: "seven",
8: "eight",
9: "nine",
10: "ten",
11: "eleven",
12: "twelve",
13: "thirteen",
14: "fourteen",
15: "fifteen",
16: "sixteen",
17: "seventeen",
18: "eighteen",
19: "nineteen",
20: "twenty",
30: "thirty",
40: "forty",
50: "fifty",
60: "sixty",
70: "seventy",
80: "eighty",
90: "ninety",
100: "hundred",
1000: "thousand"}

// int to string
func int2txt(n int) string {
	if n <= 20{
		return numbs[n]
	} else if n == 1000 || n == 100{
		return "one" + numbs[n]
	}else if n < 100 {
		return numbs[n/10*10] + numbs[n%10]
	}else {// > 100
		hund := n/100
		if n%100 == 0{
			return numbs[hund] + "hundred"
		}
			return numbs[hund] + "hundredand" + int2txt(n%100)
	}
}

func main() {
	ans := 0

	lim := 1000
	for i:=1;i<=lim;i++{
		s := int2txt(i)
		ans += len(s)
	}
	fmt.Printf("Ans: %v\n", ans)
}
