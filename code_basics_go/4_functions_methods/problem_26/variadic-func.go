package solution

import "fmt"

func MergeNumberLists(lists ...[]int) []int {
	// Initialize an empty slice instead of a nil slice
	result := []int{}

	for _, list := range lists {
		result = append(result, list...)
	}

	return result
}

func main() {
	result := MergeNumberLists([]int{1, 2}, []int{3}, []int{4})
	fmt.Println(result) // [1, 2, 3, 4]
}
