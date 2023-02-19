package service

import (
	"context"
	"net/http"

	"github.com/robbdimitrov/thoughts/src/apigateway/service/auth"
	"github.com/robbdimitrov/thoughts/src/apigateway/service/post"
	"github.com/robbdimitrov/thoughts/src/apigateway/service/route"
	"github.com/robbdimitrov/thoughts/src/apigateway/service/user"
)

// Server handle
type Server struct {
	addr   string
	auth   *auth.Controller
	post   *post.Controller
	user   *user.Controller
	router *route.Router
	server *http.Server
}

// NewServer creates and setups new http server
func NewServer(addr, authAddr, postAddr, userAddr string) *Server {
	router := route.NewRouter()
	server := &Server{
		addr:   addr,
		auth:   auth.NewController(authAddr),
		post:   post.NewController(postAddr),
		user:   user.NewController(userAddr),
		router: router,
		server: &http.Server{
			Addr:    addr,
			Handler: router,
		},
	}
	server.configureRouter()

	return server
}

func (s *Server) Start() error {
	return s.server.ListenAndServe()
}

func (s *Server) Shutdown(ctx context.Context) error {
	return s.server.Shutdown(ctx)
}

func (s *Server) configureRouter() {
	// Users
	s.router.AddRoute("/users", http.MethodPost, s.user.CreateUser)
	s.router.AddRoute("/users/:userId", http.MethodGet, s.user.GetUser)
	s.router.AddRoute("/users/:userId", http.MethodPut, s.user.UpdateUser)
	s.router.AddRoute("/users/:userId/following", http.MethodGet, s.user.GetFollowing)
	s.router.AddRoute("/users/:userId/followers", http.MethodGet, s.user.GetFollowers)
	s.router.AddRoute("/users/:userId/followers", http.MethodPost, s.user.FollowUser)
	s.router.AddRoute("/users/:userId/followers", http.MethodDelete, s.user.UnfollowUser)

	// Sessions
	s.router.AddRoute("/sessions", http.MethodPost, s.auth.CreateSession)
	s.router.AddRoute("/sessions", http.MethodDelete, s.auth.DeleteSession)

	// Posts
	s.router.AddRoute("/posts", http.MethodPost, s.post.CreatePost)
	s.router.AddRoute("/posts", http.MethodGet, s.post.GetFeed)
	s.router.AddRoute("/users/:userId/posts", http.MethodGet, s.post.GetPosts)
	s.router.AddRoute("/users/:userId/likes", http.MethodGet, s.post.GetLikedPosts)
	s.router.AddRoute("/posts/:postId", http.MethodGet, s.post.GetPost)
	s.router.AddRoute("/posts/:postId", http.MethodDelete, s.post.DeletePost)
	s.router.AddRoute("/posts/:postId/likes", http.MethodPost, s.post.LikePost)
	s.router.AddRoute("/posts/:postId/likes", http.MethodDelete, s.post.UnlikePost)
	s.router.AddRoute("/posts/:postId/reposts", http.MethodPost, s.post.RepostPost)
	s.router.AddRoute("/posts/:postId/reposts", http.MethodDelete, s.post.RemoveRepost)
}
