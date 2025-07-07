package solution

import (
	"encoding/json"
	"errors"
)

// CreateUserRequest is a request to create a new user.
type CreateUserRequest struct {
	Email                string `json:"email"`
	Password             string `json:"password"`
	PasswordConfirmation string `json:"password_confirmation"`
}

// validation errors
var (
	errEmailRequired                = errors.New("email is required")
	errPasswordRequired             = errors.New("password is required")
	errPasswordConfirmationRequired = errors.New("password confirmation is required")
	errPasswordDoesNotMatch         = errors.New("password does not match with the confirmation")
)

// DecodeAndValidateRequest decodes the JSON request body into a CreateUserRequest structure
// and validates the required fields.
func DecodeAndValidateRequest(requestBody []byte) (CreateUserRequest, error) {
	var req CreateUserRequest

	// Attempt to unmarshal the JSON request
	err := json.Unmarshal(requestBody, &req)
	if err != nil {
		return CreateUserRequest{}, err // Return error if JSON is invalid
	}

	// Validate the fields
	if req.Email == "" {
		return CreateUserRequest{}, errEmailRequired
	}
	if req.Password == "" {
		return CreateUserRequest{}, errPasswordRequired
	}
	if req.PasswordConfirmation == "" {
		return CreateUserRequest{}, errPasswordConfirmationRequired
	}
	if req.Password != req.PasswordConfirmation {
		return CreateUserRequest{}, errPasswordDoesNotMatch
	}

	return req, nil
}
