package solution

// BEGIN (write your solution here) (write your solution here)
func MostPopularWord(words []string) string {
	wordCount := make(map[string]int)
	for _, word := range words {
		wordCount[word]++
	}

	mostPopular := ""
	maxCount := 0
	for _, word := range words {
		if wordCount[word] > maxCount {
			maxCount = wordCount[word]
			mostPopular = word
		}
	}

	return mostPopular
}

// END
