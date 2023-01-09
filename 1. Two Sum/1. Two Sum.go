package main

import "fmt"

func twoSum(nums []int, target int) []int {
	m := make(map[int]int)
	for i, num := range nums {
		if j, ok := m[target-num]; ok {
			return []int{i, j}
		}
		m[num] = i
	}
	return []int{0, 1}
}

func main() {
	fmt.Println(twoSum([]int{2, 3, 5, 7, 11, 13}, 13))
}
