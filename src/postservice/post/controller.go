package post

import (
	"context"
	"log"

	"google.golang.org/grpc/codes"

	pb "github.com/robbdimitrov/thoughts/src/postservice/genproto"
)

type controller struct {
	pb.UnsafePostServiceServer

	dbClient *DbClient
}

func newController(dbClient *DbClient) *controller {
	return &controller{dbClient: dbClient}
}

func (c *controller) CreatePost(ctx context.Context, req *pb.CreatePostRequest) (*pb.Identifier, error) {
	userID, err := getUserID(ctx)
	if err != nil {
		return nil, err
	}

	res, err := c.dbClient.createPost(req.Content, userID)
	if err != nil {
		log.Printf("Creating post failed: %v", err)
		return nil, newError(codes.Internal)
	}

	return &pb.Identifier{Id: res}, nil
}

func (c *controller) GetFeed(ctx context.Context, req *pb.GetFeedRequest) (*pb.Posts, error) {
	userID, err := getUserID(ctx)
	if err != nil {
		return nil, err
	}

	res, err := c.dbClient.getFeed(userID, req.Page, req.Limit)
	if err != nil {
		log.Printf("Getting posts failed: %v", err)
		return nil, newError(codes.Internal)
	}

	return &pb.Posts{Posts: res}, nil
}

func (c *controller) GetPosts(ctx context.Context, req *pb.GetPostsRequest) (*pb.Posts, error) {
	userID, err := getUserID(ctx)
	if err != nil {
		return nil, err
	}

	res, err := c.dbClient.getPosts(req.UserId, req.Page, req.Limit, userID)
	if err != nil {
		log.Printf("Getting posts failed: %v", err)
		return nil, newError(codes.Internal)
	}

	return &pb.Posts{Posts: res}, nil
}

func (c *controller) GetLikedPosts(ctx context.Context, req *pb.GetPostsRequest) (*pb.Posts, error) {
	userID, err := getUserID(ctx)
	if err != nil {
		return nil, err
	}

	res, err := c.dbClient.getLikedPosts(req.UserId, req.Page, req.Limit, userID)
	if err != nil {
		log.Printf("Getting posts failed: %v", err)
		return nil, newError(codes.Internal)
	}

	return &pb.Posts{Posts: res}, nil
}

func (c *controller) GetPost(ctx context.Context, req *pb.PostRequest) (*pb.Post, error) {
	userID, err := getUserID(ctx)
	if err != nil {
		return nil, err
	}

	res, err := c.dbClient.getPost(req.PostId, userID)
	if err != nil {
		log.Printf("Getting post failed: %v", err)
		return nil, newError(codes.NotFound)
	}

	return res, nil
}

func (c *controller) DeletePost(ctx context.Context, req *pb.PostRequest) (*pb.Empty, error) {
	userID, err := getUserID(ctx)
	if err != nil {
		return nil, err
	}

	if err := c.dbClient.deletePost(req.PostId, userID); err != nil {
		log.Printf("Deleting post failed: %v", err)
		return nil, newError(codes.Internal)
	}

	return &pb.Empty{}, nil
}

func (c *controller) LikePost(ctx context.Context, req *pb.PostRequest) (*pb.Empty, error) {
	userID, err := getUserID(ctx)
	if err != nil {
		return nil, err
	}

	if err = c.dbClient.likePost(req.PostId, userID); err != nil {
		log.Printf("Liking post failed: %v", err)
		return nil, newError(codes.Internal)
	}

	return &pb.Empty{}, nil
}

func (c *controller) UnlikePost(ctx context.Context, req *pb.PostRequest) (*pb.Empty, error) {
	userID, err := getUserID(ctx)
	if err != nil {
		return nil, err
	}

	if err = c.dbClient.unlikePost(req.PostId, userID); err != nil {
		log.Printf("Unliking post failed: %v", err)
		return nil, newError(codes.Internal)
	}

	return &pb.Empty{}, nil
}

func (c *controller) RepostPost(ctx context.Context, req *pb.PostRequest) (*pb.Empty, error) {
	userID, err := getUserID(ctx)
	if err != nil {
		return nil, err
	}

	if err = c.dbClient.repostPost(req.PostId, userID); err != nil {
		log.Printf("Reposting post failed: %v", err)
		return nil, newError(codes.Internal)
	}

	return &pb.Empty{}, nil
}

func (c *controller) RemoveRepost(ctx context.Context, req *pb.PostRequest) (*pb.Empty, error) {
	userID, err := getUserID(ctx)
	if err != nil {
		return nil, err
	}

	if err = c.dbClient.removeRepost(req.PostId, userID); err != nil {
		log.Printf("Removing repost failed: %v", err)
		return nil, newError(codes.Internal)
	}

	return &pb.Empty{}, nil
}
