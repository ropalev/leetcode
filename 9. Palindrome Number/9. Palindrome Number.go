package main

import (
	"fmt"
	"strconv"
	"strings"
)

func reverseString(str string) string {
	output := ""
	for _, s := range str {
		output = string(s) + output
	}
	return output
}
func isPalindrome(x int) bool {
	s := strconv.FormatInt(int64(x), 10)
	s_rev := reverseString(s)
	if strings.Compare(s, s_rev) == 0 {
		return true
	}
	return false
}

func main() {
	fmt.Println(isPalindrome(121))
	fmt.Println(isPalindrome(1))
	fmt.Println(isPalindrome(1211))
}
