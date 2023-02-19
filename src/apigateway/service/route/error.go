package route

import (
	"net/http"

	"github.com/robbdimitrov/thoughts/src/apigateway/service/utils"
)

var (
	ErrPathNotFound     = utils.NewHTTPError(http.StatusNotFound)
	ErrMethodNotAllowed = utils.NewHTTPError(http.StatusMethodNotAllowed)
)
