package route

import (
	"net/http"
	"strings"

	"github.com/robbdimitrov/thoughts/src/apigateway/service/middleware"
)

const (
	pathParamKey    = ":variable"
	pathParamPrefix = ":"
	pathSeparator   = "/"
)

// Router matches routes by path and http method
type Router struct {
	root *route
}

// NewRouter creates a new router instance
func NewRouter() *Router {
	return &Router{root: newRoute()}
}

// AddRoute adds a new route to the router tree
func (r *Router) AddRoute(path, method string, handlerFunc middleware.HandlerFunc) {
	current := r.root

	parts := strings.Split(path, pathSeparator)
	for _, part := range parts {
		name := part
		if strings.HasPrefix(name, pathParamPrefix) {
			name = strings.TrimPrefix(name, pathParamPrefix)
			part = pathParamKey
		}

		subroute, ok := current.subroutes[part]
		if !ok {
			subroute = newRoute()
			subroute.name = name
			current.subroutes[part] = subroute
		}
		current = subroute
	}

	current.methodHandlers[method] = handlerFunc
}

func (r *Router) find(path, method string) (Result, error) {
	current := r.root
	params := make(map[string]string)
	found := true

	parts := strings.Split(path, pathSeparator)
	for _, part := range parts {
		subroute, ok := current.subroutes[part]
		if !ok {
			subroute, ok = current.subroutes[pathParamKey]
			if !ok {
				found = false
				break
			}
			params[subroute.name] = part
		}

		current = subroute
	}

	if !found {
		return Result{}, ErrPathNotFound
	}

	handlerFunc, ok := current.methodHandlers[method]
	if !ok {
		return Result{}, ErrMethodNotAllowed
	}

	return newResult(handlerFunc, params), nil
}

func (r *Router) ServeHTTP(w http.ResponseWriter, req *http.Request) {

}
