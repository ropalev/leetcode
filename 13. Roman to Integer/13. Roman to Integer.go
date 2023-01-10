package main

import "fmt"

func romanToInt(s string) int {
	romanDict := map[string]int{
		"I": 1,
		"V": 5,
		"X": 10,
		"L": 50,
		"C": 100,
		"D": 500,
		"M": 1000,
	}
	var result int = 0
	for i, _ := range s {
		if i == len([]rune(s))-1 {
			break
		}
		if romanDict[string(s[i])] < romanDict[string(s[i+1])] {
			result -= romanDict[string(s[i])]
		} else {
			result += romanDict[string(s[i])]
		}
	}
	result += romanDict[string(s[len(s)-1])]
	return result
}

func main() {
	fmt.Println(romanToInt("III"))
	fmt.Println(romanToInt("LVIII"))
	fmt.Println(romanToInt("MCMXCIV"))
	fmt.Println(romanToInt("IX"))
}
