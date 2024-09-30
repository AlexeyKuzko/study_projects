package solution

// BEGIN (write your solution here)
func IntsCopy(src []int, maxLen int) []int {
	{
		if maxLen <= 0 {
			return []int{}
		} else if maxLen > len(src) {
			return src
		}
		return src[:maxLen]
	}
}

// END
