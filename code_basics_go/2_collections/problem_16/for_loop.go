package solution

// BEGIN (write your solution here)
func Map(strs []string, mapFunc func(s string) string) []string {
	result := make([]string, len(strs))
	for i, str := range strs {
		result[i] = mapFunc(str)
	}
	return result
}

// END
