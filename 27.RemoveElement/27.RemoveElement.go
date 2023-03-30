package main

import "fmt"

func removeElement(nums []int, val int) int {
	i := 0
	for j, v := range nums {
		if nums[j] != val {
			nums[i] = v
			i++
		}
	}
	return i
}

func main() {
	test := []int{3, 2, 2, 3}
	fmt.Println(removeElement(test, 3))
}
