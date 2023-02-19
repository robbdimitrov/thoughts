package route

import (
	"github.com/robbdimitrov/thoughts/src/apigateway/service/middleware"
)

type route struct {
	name           string
	subroutes      map[string]*route
	methodHandlers map[string]middleware.HandlerFunc
}

func newRoute() *route {
	return &route{
		subroutes:      make(map[string]*route),
		methodHandlers: make(map[string]middleware.HandlerFunc),
	}
}
