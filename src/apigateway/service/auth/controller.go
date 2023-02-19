package auth

import (
	"context"
	"log"
	"net/http"
	"time"

	"github.com/labstack/echo/v4"
	"google.golang.org/grpc"

	pb "github.com/robbdimitrov/thoughts/src/apigateway/genproto"
	"github.com/robbdimitrov/thoughts/src/apigateway/service/utils"
)

type Controller struct {
	addr string
}

func NewController(addr string) *Controller {
	return &Controller{addr}
}

func (ac *Controller) CreateSession(w http.ResponseWriter, r *http.Request) error {
	conn, err := grpc.Dial(ac.addr, utils.InsecureCredentials(), grpc.WithBlock())
	if err != nil {
		log.Printf("Connecting to service failed: %v", err)
		return utils.NewHTTPError(http.StatusInternalServerError)
	}
	defer conn.Close()
	client := pb.NewAuthServiceClient(conn)

	ctx, cancel := context.WithTimeout(context.Background(), time.Second)
	defer cancel()

	req := pb.Credentials{
		// Email:    c.FormValue("email"),
		// Password: c.FormValue("password"),
	}

	res, err := client.CreateSession(ctx, &req)
	if err != nil {
		log.Printf("Creating session failed: %v", err)
		return utils.ToHTTPError(err)
	}

	// createCookie(c, res.Id)
	// return c.JSON(http.StatusOK, map[string]int32{"id": res.UserId})
	return nil
}

func (ac *Controller) validateSession(r *http.Request) error {
	cookie, err := r.Cookie("session")
	if err != nil {
		return utils.NewHTTPError(http.StatusUnauthorized)
	}

	conn, err := grpc.Dial(ac.addr, utils.InsecureCredentials(), grpc.WithBlock())
	if err != nil {
		log.Printf("Connecting to service failed: %v", err)
		return echo.NewHTTPError(500)
	}
	defer conn.Close()
	client := pb.NewAuthServiceClient(conn)

	ctx, cancel := context.WithTimeout(context.Background(), time.Second)
	defer cancel()

	req := pb.SessionRequest{SessionId: cookie.Value}

	_, err = client.GetSession(ctx, &req)
	if err != nil {
		log.Printf("Validating session failed: %v", err)
		// clearCookie(c)
		return utils.ToHTTPError(err)
	}

	// createCookie(c, res.Id)
	// setUserID(c, strconv.Itoa(int(res.UserId)))
	return nil
}

// DeleteSession deletes
func (ac *Controller) DeleteSession(w http.ResponseWriter, r *http.Request) {
	cookie, err := c.Cookie("session")
	if err != nil {
		return utils.NewHTTPError(http.StatusUnauthorized)
	}

	conn, err := grpc.Dial(ac.addr, utils.InsecureCredentials(), grpc.WithBlock())
	if err != nil {
		log.Printf("Connecting to service failed: %v", err)
		return utils.NewHTTPError(http.StatusInternalServerError)
	}
	defer conn.Close()
	client := pb.NewAuthServiceClient(conn)

	ctx, cancel := context.WithTimeout(context.Background(), time.Second)
	defer cancel()

	req := pb.SessionRequest{SessionId: cookie.Value}

	_, err = client.DeleteSession(ctx, &req)
	if err != nil {
		log.Printf("Deleting session failed: %v", err)
		return utils.ToHTTPError(err)
	}

	// clearCookie(c)
	// return c.NoContent(http.StatusNoContent)
	return nil
}
