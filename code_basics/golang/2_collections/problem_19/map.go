package solution

// BEGIN (write your solution here)
func UniqueUserIDs(userIDs []int64) []int64 {
	uniqueMap := make(map[int64]bool)
	uniqueUserIDs := make([]int64, 0, len(userIDs))

	for _, id := range userIDs {
		if !uniqueMap[id] {
			uniqueMap[id] = true
			uniqueUserIDs = append(uniqueUserIDs, id)
		}
	}

	return uniqueUserIDs
}

// END
