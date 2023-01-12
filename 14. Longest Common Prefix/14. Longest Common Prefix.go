package main

import (
	"fmt"
	"strings"
)

func longestCommonPrefix(strs []string) string {
	prefix := strs[0]
	for _, str := range strs {
		for !strings.HasPrefix(str, prefix) {
			prefix = prefix[0 : len(prefix)-1]
		}
	}
	return prefix
}

func main() {
	fmt.Println(longestCommonPrefix([]string{"abcda", "ab", "DDa"}))
	fmt.Println(longestCommonPrefix([]string{"abcda", "ab", "abc"}))
}
