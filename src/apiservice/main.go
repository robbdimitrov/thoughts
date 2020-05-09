package main

import (
	"context"
	"fmt"
	"log"
	"os"
	"os/signal"
	"time"

	"github.com/robbdimitrov/thoughts/src/apiservice/api"
)

func main() {
	port := "8080"
	if value := os.Getenv("PORT"); value != "" {
		port = value
	}
	authAddr := os.Getenv("AUTH_SERVICE_ADDR")
	userAddr := os.Getenv("USER_SERVICE_ADDR")
	postAddr := os.Getenv("POST_SERVICE_ADDR")
	imageAddr := os.Getenv("IMAGE_SERVICE_ADDR")

	server := api.CreateServer(authAddr, userAddr, postAddr, imageAddr)

	go func() {
		log.Printf("Server is starting on port %s", port)
		if err := server.Start(fmt.Sprintf(":%s", port)); err != nil {
			log.Fatal(err)
		}
	}()

	quit := make(chan os.Signal)
	signal.Notify(quit, os.Interrupt)
	<-quit

	ctx, cancel := context.WithTimeout(context.Background(), 10*time.Second)
	defer cancel()

	log.Println("Server is shutting down...")
	if err := server.Shutdown(ctx); err != nil {
		log.Fatal(err)
	}
}
