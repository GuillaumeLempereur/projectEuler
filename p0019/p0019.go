/*
p19
*/

package main
import (
	"fmt"
)

func main() {
	ans := 0

	lim := 2000
	s := 2 // 01/01/1901 was Tuesday -> 2
	for y:=1901;y<=lim;y++{
		if s%7==0 {ans += 1} // if s%7==0 then it's sunday
		s += 31
		if s%7==0 {ans += 1}
		if y%4 == 0{
			s += 29 //leap year
		}else{
			s += 28
		}
		if s%7==0 {ans += 1}
		s += 31
		if s%7==0 {ans += 1}
		s += 30
		if s%7==0 {ans += 1}
		s += 31
		if s%7==0 {ans += 1}
		s += 30
		if s%7==0 {ans += 1}
		s += 31
		if s%7==0 {ans += 1}
		s += 31
		if s%7==0 {ans += 1}
		s += 30
		if s%7==0 {ans += 1}
		s += 31
		if s%7==0 {ans += 1}
		s += 30
		if s%7==0 {ans += 1}
		s += 31
	}
	fmt.Printf("Ans: %v\n", ans)
}
