package response

import (
	"net/http"

	"google.golang.org/grpc"
	"google.golang.org/grpc/codes"
	"google.golang.org/grpc/credentials/insecure"
	"google.golang.org/grpc/status"
)

// ToHTTPError converts grpc error to http error
func ToHTTPError(err error) HTTPError {
	s := status.Convert(err)
	return HTTPError{Code: getStatusCode(s), Status: s.Proto().GetMessage()}
}

// InsecureCredentials creates insecure option for grpc
func InsecureCredentials() grpc.DialOption {
	return grpc.WithTransportCredentials(insecure.NewCredentials())
}

func getStatusCode(s *status.Status) int {
	c := s.Proto().GetCode()
	switch codes.Code(c) {
	case codes.InvalidArgument:
		return http.StatusBadRequest
	case codes.Unauthenticated:
		return http.StatusUnauthorized
	case codes.PermissionDenied:
		return http.StatusForbidden
	case codes.NotFound:
		return http.StatusNotFound
	default:
		return http.StatusInternalServerError
	}
}
