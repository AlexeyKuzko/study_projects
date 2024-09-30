package solution

// BEGIN (write your solution here)
func ErrorMessageToCode(msg string) int {
	const (
		OK        = 0
		CANCELLED = 1
		UNKNOWN   = 2
	)
	if msg == "OK" {
		return OK
	} else if msg == "CANCELLED" {
		return CANCELLED
	} else {
		return UNKNOWN
	}
}

// END
