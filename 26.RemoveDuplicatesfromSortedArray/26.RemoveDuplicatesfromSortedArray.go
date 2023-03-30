package main

import "fmt"

func removeDuplicates(nums []int) int {
	i := 0
	for j := range nums {
		if nums[i] != nums[j] {
			i += 1
			nums[i] = nums[j]
		}
	}
	return i + 1
}

func main() {
	test1 := []int{1, 1, 2}
	fmt.Println(removeDuplicates(test1))
}
