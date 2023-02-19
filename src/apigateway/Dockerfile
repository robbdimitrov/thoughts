FROM golang:1.19 as builder
WORKDIR /usr/src/app
COPY go.* .
RUN go mod download
COPY . .
RUN go build -v -o apigateway

FROM scratch
COPY --from=builder /usr/src/app/apigateway /apigateway
CMD ["/apigateway"]
