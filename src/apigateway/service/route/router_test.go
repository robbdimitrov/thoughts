package route

import (
	"net/http"
	"testing"

	"github.com/robbdimitrov/thoughts/src/apigateway/service/route"
	"github.com/stretchr/testify/assert"
)

func TestRouter_Find(t *testing.T) {
	router := route.NewRouter()

	handlerFunc := func(w http.ResponseWriter, r *http.Request) {}

	router.AddRoute("/api/users", http.MethodGet, handlerFunc)
	router.AddRoute("/api/users", http.MethodPost, handlerFunc)
	router.AddRoute("/api/users/:id", http.MethodDelete, handlerFunc)

	res, err := router.Find("/api/some", http.MethodGet)
	assert.Nil(t, res.HandlerFunc)
	assert.ErrorIs(t, err, route.ErrPathNotFound)

	res, err = router.find("/api/users", http.MethodDelete)
	assert.Nil(t, res.HandlerFunc)
	assert.ErrorIs(t, err, route.ErrMethodNotAllowed)

	res, err = router.find("/api/users/20", http.MethodDelete)
	assert.NoError(t, err)
	assert.NotNil(t, res.HandlerFunc)
	assert.Equal(t, "20", res.Params["id"])
}
