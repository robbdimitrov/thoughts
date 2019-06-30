package post

import (
	"context"
	"errors"
	"net/http"

	pb "postservice/genproto"
)

// Service is handling post-related grpc calls
type Service struct {
	dbClient   *DbClient
	authClient *AuthClient
}

// NewService creates a new server instance
func NewService(dbClient *DbClient, authClient *AuthClient) *Service {
	return &Service{dbClient, authClient}
}

// CreatePost creates a new Post object
func (s *Service) CreatePost(ctx context.Context, req *pb.PostUpdates) (*pb.PostStatus, error) {
	status, err := s.authClient.Validate(req.Token)
	if err != nil {
		return nil, err
	} else if status.Error.Code != 0 {
		return &pb.PostStatus{Error: status.Error}, nil
	}

	post, err := s.dbClient.CreatePost(req.Content, status.UserId)
	if err != nil {
		retErr := pb.Error{Code: http.StatusBadRequest, Error: "BAD_REQUEST", Message: "Like post failed."}
		return &pb.PostStatus{Error: &retErr}, err
	}
	return &pb.PostStatus{Post: &post}, nil
}

// GetPost returns a Post object with the id passed from the request
func (s *Service) GetPost(ctx context.Context, req *pb.PostRequest) (*pb.PostStatus, error) {
	status, err := s.authClient.Validate(req.Token)
	if err != nil {
		return nil, err
	} else if status.Error.Code != 0 {
		return &pb.PostStatus{}, errors.New(status.Error.Message)
	}

	post, err := s.dbClient.GetPost(req.PostId, status.UserId)
	if err != nil {
		retErr := pb.Error{Code: http.StatusNotFound, Error: "NOT_FOUND", Message: "Post not found."}
		return &pb.PostStatus{Error: &retErr}, err
	}
	return &pb.PostStatus{Post: &post}, nil
}

// GetFeed returns posts and retweets of users followed by the user
func (s *Service) GetFeed(ctx context.Context, req *pb.DataRequest) (*pb.Posts, error) {
	status, err := s.authClient.Validate(req.Token)
	if err != nil {
		return nil, err
	} else if status.Error.Code != 0 {
		return &pb.Posts{}, errors.New(status.Error.Message)
	}

	posts, err := s.dbClient.GetFeed(status.UserId, req.Page, req.Limit)
	if err != nil {
		return &posts, err
	}
	return &posts, nil
}

// GetPosts returns posts and retweets of user
func (s *Service) GetPosts(ctx context.Context, req *pb.DataRequest) (*pb.Posts, error) {
	status, err := s.authClient.Validate(req.Token)
	if err != nil {
		return nil, err
	} else if status.Error.Code != 0 {
		return &pb.Posts{}, nil
	}

	posts, err := s.dbClient.GetPosts(req.UserId, req.Page, req.Limit, status.UserId)
	if err != nil {
		return &posts, err
	}
	return &posts, nil
}

// GetLikedPosts returns posts liked by the user
func (s *Service) GetLikedPosts(ctx context.Context, req *pb.DataRequest) (*pb.Posts, error) {
	status, err := s.authClient.Validate(req.Token)
	if err != nil {
		return nil, err
	} else if status.Error.Code != 0 {
		return &pb.Posts{}, nil
	}

	posts, err := s.dbClient.GetLikedPosts(req.UserId, req.Page, req.Limit, status.UserId)
	if err != nil {
		return &posts, err
	}
	return &posts, nil
}

// DeletePost deletes a post owned by the user
func (s *Service) DeletePost(ctx context.Context, req *pb.PostRequest) (*pb.Status, error) {
	status, err := s.authClient.Validate(req.Token)
	if err != nil {
		return nil, err
	} else if status.Error.Code != 0 {
		return &pb.Status{Error: status.Error}, nil
	}

	post, _ := s.dbClient.GetPost(req.PostId, status.UserId)
	if post.UserId != status.UserId {
		retErr := pb.Error{Code: http.StatusForbidden, Error: "FORBIDDEN", Message: "This action is forbidden."}
		return &pb.Status{Error: &retErr}, err
	}

	err = s.dbClient.DeletePost(req.PostId)
	if err != nil {
		retErr := pb.Error{Code: http.StatusBadRequest, Error: "BAD_REQUEST", Message: "Deleting post failed."}
		return &pb.Status{Error: &retErr}, err
	}
	return &pb.Status{Message: "Post deleted."}, nil
}
