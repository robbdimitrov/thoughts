package auth

import (
	"fmt"
	"net/http"

	"github.com/robbdimitrov/thoughts/src/apigateway/service/middleware"
)

var allowed = map[string]struct{}{
	"POST:/sessions":   struct{}{},
	"DELETE:/sessions": struct{}{},
	"POST:/users":      struct{}{},
}

// AuthGuard determines whether a request should be allowed
func AuthGuard(c *Controller) func(middleware.HandlerFunc) middleware.HandlerFunc {
	return func(next middleware.HandlerFunc) middleware.HandlerFunc {
		return func(w http.ResponseWriter, r *http.Request) error {
			key := fmt.Sprintf("%s:%s", r.Method, r.URL.Path)
			if _, ok := allowed[key]; ok {
				return next(w, r)
			}
			err := c.validateSession(r)
			if err != nil {
				return err
			}
			return next(w, r)
		}
	}
}
