package solution

import (
	"strings"
)

// UserCreateRequest is a request to create a new user.
type UserCreateRequest struct {
	FirstName string // не может быть пустым; не может содержать пробелы
	Age       int    // не может быть 0 или отрицательным; не может быть больше 150
}

// BEGIN (write your solution here)
func Validate(req UserCreateRequest) string {
	if req.FirstName == "" || strings.Contains(req.FirstName, " ") {
		return "invalid request"
	}
	if req.Age == 0 || req.Age < 0 || req.Age > 150 {
		return "invalid request"
	}
	return ""
}

// END
