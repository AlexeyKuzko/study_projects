package solution

// BEGIN (write your solution here)
func SafeWrite(nums [5]int, i, val int) [5]int {
	if i >= 0 && i <= len(nums)-1 {
		nums[i] = val
	} else {
		return nums
	}
	return nums
}

// END
