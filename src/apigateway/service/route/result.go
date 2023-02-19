package route

import (
	"github.com/robbdimitrov/thoughts/src/apigateway/service/middleware"
)

// Result contains http handler function and path params
type Result struct {
	HandlerFunc middleware.HandlerFunc
	Params      map[string]string
}

func newResult(handlerFunc middleware.HandlerFunc, params map[string]string) Result {
	return Result{HandlerFunc: handlerFunc, Params: params}
}
