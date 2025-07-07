package solution

import "sort"

// BEGIN (write your solution here)
func UniqueSortedUserIDs(userIDs []int64) []int64 {
	sort.Slice(userIDs, func(i, j int) bool {
		return userIDs[i] < userIDs[j]
	})

	if len(userIDs) == 0 {
		return userIDs
	}

	uniqueUserIDs := make([]int64, 0, len(userIDs))
	uniqueUserIDs = append(uniqueUserIDs, userIDs[0])

	for i := 1; i < len(userIDs); i++ {
		if userIDs[i] != userIDs[i-1] {
			uniqueUserIDs = append(uniqueUserIDs, userIDs[i])
		}
	}
	return uniqueUserIDs
}

// END
