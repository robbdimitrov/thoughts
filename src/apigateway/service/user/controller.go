package user

import (
	"context"
	"log"
	"net/http"
	"strconv"
	"time"

	"google.golang.org/grpc"

	"github.com/labstack/echo/v4"
	pb "github.com/robbdimitrov/thoughts/src/apigateway/genproto"
	"github.com/robbdimitrov/thoughts/src/apigateway/service/utils"
)

type Controller struct {
	addr string
}

func NewController(addr string) *Controller {
	return &Controller{addr: addr}
}

func (s *Controller) createUser(w http.ResponseWriter, r *http.Request) {
	conn, err := grpc.Dial(s.addr, utils.InsecureCredentials(), grpc.WithBlock())
	if err != nil {
		log.Printf("Connecting to service failed: %v", err)
		// utils.ToHTTPError(http.StatusInternalServerError)
		return
	}
	defer conn.Close()
	client := pb.NewUserServiceClient(conn)

	ctx, cancel := context.WithTimeout(context.Background(), time.Second)
	defer cancel()

	req := pb.CreateUserRequest{
		// Name:     c.FormValue("name"),
		// Username: c.FormValue("username"),
		// Email:    c.FormValue("email"),
		// Password: c.FormValue("password"),
	}

	_, err = client.CreateUser(ctx, &req)
	if err != nil {
		log.Printf("Creating user failed: %v", err)
		utils.ToHTTPError(err)
		return
	}

	// return c.JSON(201, map[string]int32{"id": res.Id})
}

func (s *Controller) getUser(w http.ResponseWriter, r *http.Request) {
	conn, err := grpc.Dial(s.addr, utils.InsecureCredentials(), grpc.WithBlock())
	if err != nil {
		log.Printf("Connecting to service failed: %v", err)
		return echo.NewHTTPError(500)
	}
	defer conn.Close()
	client := pb.NewUserServiceClient(conn)

	userID, err := strconv.Atoi(c.Param("userId"))
	if err != nil {
		return echo.NewHTTPError(400)
	}

	ctx, cancel := context.WithTimeout(context.Background(), time.Second)
	ctx = appendUserIDHeader(ctx, c)
	defer cancel()

	req := pb.UserRequest{UserId: int32(userID)}

	res, err := client.GetUser(ctx, &req)
	if err != nil {
		log.Printf("Getting user failed: %v", err)
		return utils.ToHTTPError(err)
	}

	return c.JSON(200, mapUser(res))
}

func (s *Controller) updateUser(w http.ResponseWriter, r *http.Request) {
	conn, err := grpc.Dial(s.addr, utils.InsecureCredentials(), grpc.WithBlock())
	if err != nil {
		log.Printf("Connecting to service failed: %v", err)
		return echo.NewHTTPError(500)
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
		log.Printf("Updating user failed: %v", err)
		return newHTTPError(err)
	}

	return c.NoContent(http.StatusNoContent)
}

func (s *Controller) getFollowing(w http.ResponseWriter, r *http.Request) {
	conn, err := grpc.Dial(s.addr, insecureCredentials(), grpc.WithBlock())
	if err != nil {
		log.Printf("Connecting to service failed: %v", err)
		return echo.NewHTTPError(500)
	}
	defer conn.Close()
	client := pb.NewUserServiceClient(conn)

	ctx, cancel := context.WithTimeout(context.Background(), time.Second)
	ctx = appendUserIDHeader(ctx, c)
	defer cancel()

	userID, err := strconv.Atoi(c.Param("userId"))
	if err != nil {
		return echo.NewHTTPError(400)
	}
	page, err := strconv.Atoi(c.QueryParam("page"))
	if err != nil {
		return echo.NewHTTPError(400)
	}
	limit, err := strconv.Atoi(c.QueryParam("limit"))
	if err != nil {
		return echo.NewHTTPError(400)
	}

	req := pb.GetUsersRequest{
		UserId: int32(userID),
		Page:   int32(page),
		Limit:  int32(limit),
	}

	res, err := client.GetFollowing(ctx, &req)
	if err != nil {
		log.Printf("Getting following failed: %v", err)
		return newHTTPError(err)
	}

	users := make([]user, len(res.Users))
	for i, v := range res.Users {
		users[i] = mapUser(v)
	}

	return c.JSON(200, map[string][]user{"items": users})
}

func (s *Controller) getFollowers(w http.ResponseWriter, r *http.Request) {
	conn, err := grpc.Dial(s.addr, insecureCredentials(), grpc.WithBlock())
	if err != nil {
		log.Printf("Connecting to service failed: %v", err)
		return echo.NewHTTPError(500)
	}
	defer conn.Close()
	client := pb.NewUserServiceClient(conn)

	ctx, cancel := context.WithTimeout(context.Background(), time.Second)
	ctx = appendUserIDHeader(ctx, c)
	defer cancel()

	userID, err := strconv.Atoi(c.Param("userId"))
	if err != nil {
		return echo.NewHTTPError(400)
	}
	page, err := strconv.Atoi(c.QueryParam("page"))
	if err != nil {
		return echo.NewHTTPError(400)
	}
	limit, err := strconv.Atoi(c.QueryParam("limit"))
	if err != nil {
		return echo.NewHTTPError(400)
	}

	req := pb.GetUsersRequest{
		UserId: int32(userID),
		Page:   int32(page),
		Limit:  int32(limit),
	}

	res, err := client.GetFollowers(ctx, &req)
	if err != nil {
		log.Printf("Getting followers failed: %v", err)
		return newHTTPError(err)
	}

	users := make([]user, len(res.Users))
	for i, v := range res.Users {
		users[i] = mapUser(v)
	}

	return c.JSON(200, map[string][]user{"items": users})
}

func (s *Controller) followUser(w http.ResponseWriter, r *http.Request) {
	conn, err := grpc.Dial(s.addr, utils.InsecureCredentials(), grpc.WithBlock())
	if err != nil {
		log.Printf("Connecting to service failed: %v", err)
		// echo.NewHTTPError(http.StatusInternalServerError)
		return
	}
	defer conn.Close()
	client := pb.NewUserServiceClient(conn)

	ctx, cancel := context.WithTimeout(context.Background(), time.Second)
	// ctx = appendUserIDHeader(ctx, c)
	defer cancel()

	userID, err := strconv.Atoi(c.Param("userId"))
	if err != nil {
		// echo.NewHTTPError(http.StatusBadRequest)
		return
	}
	req := pb.UserRequest{UserId: int32(userID)}

	_, err = client.FollowUser(ctx, &req)
	if err != nil {
		log.Printf("Following user failed: %v", err)
		// newHTTPError(err)
		return
	}

	return c.NoContent(http.StatusNoContent)
}

func (s *Controller) unfollowUser(w http.ResponseWriter, r *http.Request) {
	conn, err := grpc.Dial(s.addr, utils.InsecureCredentials(), grpc.WithBlock())
	if err != nil {
		log.Printf("Connecting to service failed: %v", err)
		// echo.NewHTTPError(http.StatusInternalServerError)
		return
	}
	defer conn.Close()
	client := pb.NewUserServiceClient(conn)

	ctx, cancel := context.WithTimeout(context.Background(), time.Second)
	// ctx = appendUserIDHeader(ctx, c)
	defer cancel()

	userID, err := strconv.Atoi(c.Param("userId"))
	if err != nil {
		echo.NewHTTPError(http.StatusBadRequest)
		return
	}
	req := pb.UserRequest{UserId: int32(userID)}

	_, err = client.UnfollowUser(ctx, &req)
	if err != nil {
		log.Printf("Unfollowing user failed: %v", err)
		utils.ToHTTPError(err)
		return
	}

	// return c.NoContent(http.StatusNoContent)
}
