package api

import (
	"github.com/labstack/echo/v4"
	"google.golang.org/grpc/codes"
	"google.golang.org/grpc/status"
)

// getStatusCode converts grpc code to http status code
func getStatusCode(s *status.Status) int {
	c := s.Proto().GetCode()

	switch codes.Code(c) {
	case codes.InvalidArgument:
		return 400
	case codes.Unauthenticated:
		return 401
	case codes.PermissionDenied:
		return 403
	case codes.NotFound:
		return 404
	default:
		return 500
	}
}

// newHTTPError converts grpc error to http error
func newHTTPError(err error) *echo.HTTPError {
	s := status.Convert(err)
	return echo.NewHTTPError(getStatusCode(s), s.Proto().GetMessage())
}
