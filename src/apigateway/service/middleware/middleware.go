package middleware

import (
	"log"
	"net/http"
)

type HandlerFunc func(http.ResponseWriter, *http.Request) error
type MiddlewareFunc func(HandlerFunc) HandlerFunc

// WithLogging adds a logging middleware for the http requests
func WithLogging(next HandlerFunc) HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) error {
		log.Printf("Request %s %s", r.Method, r.RequestURI)
		return next(w, r)
	}
}
