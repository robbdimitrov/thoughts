package response

import "net/http"

// HTTPError is an error containing status code and status text
type HTTPError struct {
	Code   int
	Status string
}

// NewHTTPError creates a new HTTPError instance
func NewHTTPError(code int) HTTPError {
	return HTTPError{Code: code, Status: http.StatusText(code)}
}

func (e HTTPError) Error() string {
	return e.Status
}
