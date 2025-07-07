package solution

import (
	"errors"
)

// nonCriticalError represents a non-critical validation error.
type nonCriticalError struct{}

func (e nonCriticalError) Error() string {
	return "validation error"
}

// Critical errors
var (
	errBadConnection = errors.New("bad connection")
	errBadRequest    = errors.New("bad request")
)

const unknownErrorMsg = "unknown error"

// GetErrorMsg checks the type of error and returns the appropriate message.
func GetErrorMsg(err error) string {
	// Check for non-critical errors
	var nonCritErr nonCriticalError
	if errors.As(err, &nonCritErr) {
		return "" // non-critical errors should return an empty string
	}

	// Check for specific critical errors
	if errors.Is(err, errBadConnection) {
		return errBadConnection.Error()
	}
	if errors.Is(err, errBadRequest) {
		return errBadRequest.Error()
	}

	// If the error is unknown, return the unknown error message
	return unknownErrorMsg
}
