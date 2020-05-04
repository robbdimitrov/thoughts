package api

import (
	"context"
	"strconv"
	"time"

	"github.com/labstack/echo/v4"
	"google.golang.org/grpc"
	"google.golang.org/grpc/status"

	pb "github.com/robbdimitrov/thoughts/src/apiservice/genproto"
)

type userService struct {
	addr string
}

func newUserService(addr string) *userService {
	return &userService{addr}
}

// Handlers

func (s *userService) createUser(c echo.Context) error {
	conn, err := grpc.Dial(s.addr, grpc.WithInsecure(), grpc.WithBlock())
	if err != nil {
		return echo.NewHTTPError(500, err.Error())
	}
	defer conn.Close()
	client := pb.NewUserServiceClient(conn)

	ctx, cancel := context.WithTimeout(context.Background(), time.Second)
	defer cancel()

	req := pb.CreateUserRequest{
		Name:     c.FormValue("name"),
		Username: c.FormValue("username"),
		Email:    c.FormValue("email"),
		Password: c.FormValue("password"),
	}

	res, err := client.CreateUser(ctx, &req)
	if err != nil {
		s := status.Convert(err)
		return echo.NewHTTPError(getStatusCode(s), s.Proto().GetMessage())
	}

	return c.JSON(201, map[string]int32{"id": res.UserId})
}

func (s *userService) updateUser(c echo.Context) error {
	conn, err := grpc.Dial(s.addr, grpc.WithInsecure(), grpc.WithBlock())
	if err != nil {
		return echo.NewHTTPError(500, err.Error())
	}
	defer conn.Close()
	client := pb.NewUserServiceClient(conn)

	currentUserID := getUserID(c)
	if currentUserID != c.Param("userId") {
		return echo.NewHTTPError(403)
	}

	ctx, cancel := context.WithTimeout(context.Background(), time.Second)
	ctx = appendUserIDHeader(ctx, c)
	defer cancel()

	req := pb.UpdateUserRequest{
		Name:        c.FormValue("name"),
		Username:    c.FormValue("username"),
		Email:       c.FormValue("email"),
		Password:    c.FormValue("password"),
		OldPassword: c.FormValue("oldPassword"),
	}

	_, err = client.UpdateUser(ctx, &req)
	if err != nil {
		s := status.Convert(err)
		return echo.NewHTTPError(getStatusCode(s), s.Proto().GetMessage())
	}

	return c.NoContent(204)
}

func (s *userService) getUser(c echo.Context) error {
	conn, err := grpc.Dial(s.addr, grpc.WithInsecure(), grpc.WithBlock())
	if err != nil {
		return echo.NewHTTPError(500, err.Error())
	}
	defer conn.Close()
	client := pb.NewUserServiceClient(conn)

	userID, err := strconv.Atoi(c.Param("userId"))
	if err != nil {
		return echo.NewHTTPError(500, err.Error())
	}

	ctx, cancel := context.WithTimeout(context.Background(), time.Second)
	ctx = appendUserIDHeader(ctx, c)
	defer cancel()

	req := pb.UserRequest{UserId: int32(userID)}

	res, err := client.GetUser(ctx, &req)
	if err != nil {
		s := status.Convert(err)
		return echo.NewHTTPError(getStatusCode(s), s.Proto().GetMessage())
	}

	return c.JSON(200, mapUser(res))
}

func (s *userService) getFollowing(c echo.Context) error {
	conn, err := grpc.Dial(s.addr, grpc.WithInsecure(), grpc.WithBlock())
	if err != nil {
		return echo.NewHTTPError(500, err.Error())
	}
	defer conn.Close()
	client := pb.NewFollowServiceClient(conn)

	ctx, cancel := context.WithTimeout(context.Background(), time.Second)
	ctx = appendUserIDHeader(ctx, c)
	defer cancel()

	userID, err := strconv.Atoi(c.Param("userId"))
	if err != nil {
		return echo.NewHTTPError(500, err.Error())
	}
	page, err := strconv.Atoi(c.QueryParam("page"))
	if err != nil {
		return echo.NewHTTPError(500, err.Error())
	}
	limit, err := strconv.Atoi(c.QueryParam("limit"))
	if err != nil {
		return echo.NewHTTPError(500, err.Error())
	}

	req := pb.GetUsersRequest{
		UserId: int32(userID),
		Page:   int32(page),
		Limit:  int32(limit),
	}

	res, err := client.GetFollowing(ctx, &req)
	if err != nil {
		s := status.Convert(err)
		return echo.NewHTTPError(getStatusCode(s), s.Proto().GetMessage())
	}

	users := make([]user, len(res.Users))
	for i, v := range res.Users {
		users[i] = mapUser(v)
	}

	return c.JSON(200, map[string][]user{"items": users})
}

func (s *userService) getFollowers(c echo.Context) error {
	conn, err := grpc.Dial(s.addr, grpc.WithInsecure(), grpc.WithBlock())
	if err != nil {
		return echo.NewHTTPError(500, err.Error())
	}
	defer conn.Close()
	client := pb.NewFollowServiceClient(conn)

	ctx, cancel := context.WithTimeout(context.Background(), time.Second)
	ctx = appendUserIDHeader(ctx, c)
	defer cancel()

	userID, err := strconv.Atoi(c.Param("userId"))
	if err != nil {
		return echo.NewHTTPError(500, err.Error())
	}
	page, err := strconv.Atoi(c.QueryParam("page"))
	if err != nil {
		return echo.NewHTTPError(500, err.Error())
	}
	limit, err := strconv.Atoi(c.QueryParam("limit"))
	if err != nil {
		return echo.NewHTTPError(500, err.Error())
	}

	req := pb.GetUsersRequest{
		UserId: int32(userID),
		Page:   int32(page),
		Limit:  int32(limit),
	}

	res, err := client.GetFollowers(ctx, &req)
	if err != nil {
		s := status.Convert(err)
		return echo.NewHTTPError(getStatusCode(s), s.Proto().GetMessage())
	}

	users := make([]user, len(res.Users))
	for i, v := range res.Users {
		users[i] = mapUser(v)
	}

	return c.JSON(200, map[string][]user{"items": users})
}

func (s *userService) followUser(c echo.Context) error {
	conn, err := grpc.Dial(s.addr, grpc.WithInsecure(), grpc.WithBlock())
	if err != nil {
		return echo.NewHTTPError(500, err.Error())
	}
	defer conn.Close()
	client := pb.NewFollowServiceClient(conn)

	ctx, cancel := context.WithTimeout(context.Background(), time.Second)
	ctx = appendUserIDHeader(ctx, c)
	defer cancel()

	userID, err := strconv.Atoi(c.Param("userId"))
	if err != nil {
		return echo.NewHTTPError(500, err.Error())
	}
	req := pb.UserRequest{UserId: int32(userID)}

	_, err = client.FollowUser(ctx, &req)
	if err != nil {
		s := status.Convert(err)
		return echo.NewHTTPError(getStatusCode(s), s.Proto().GetMessage())
	}

	return c.NoContent(204)
}

func (s *userService) unfollowUser(c echo.Context) error {
	conn, err := grpc.Dial(s.addr, grpc.WithInsecure(), grpc.WithBlock())
	if err != nil {
		return echo.NewHTTPError(500, err.Error())
	}
	defer conn.Close()
	client := pb.NewFollowServiceClient(conn)

	ctx, cancel := context.WithTimeout(context.Background(), time.Second)
	ctx = appendUserIDHeader(ctx, c)
	defer cancel()

	userID, err := strconv.Atoi(c.Param("userId"))
	if err != nil {
		return echo.NewHTTPError(500, err.Error())
	}
	req := pb.UserRequest{UserId: int32(userID)}

	_, err = client.UnfollowUser(ctx, &req)
	if err != nil {
		s := status.Convert(err)
		return echo.NewHTTPError(getStatusCode(s), s.Proto().GetMessage())
	}

	return c.NoContent(204)
}
