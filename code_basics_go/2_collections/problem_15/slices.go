package solution

// BEGIN (write your solution here)
func Remove(nums []int, i int) []int {
	if i >= 0 && i <= len(nums)-1 {
		return append(nums[:i], nums[i+1:]...)
	}
	return nums
}

// END
