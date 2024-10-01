package solution

import (
	"strings"
	"unicode"
)

// BEGIN (write your solution here)

func latinLetters(s string) string {
	var builder strings.Builder
	for _, r := range s {
		if unicode.Is(unicode.Latin, r) {
			builder.WriteRune(r)
		}
	}
	return builder.String()
}

// END
