package user

import pb "github.com/robbdimitrov/thoughts/src/apigateway/genproto"

type user struct {
	ID        int32  `json:"id"`
	Name      string `json:"name"`
	Username  string `json:"username"`
	Email     string `json:"email"`
	Bio       string `json:"bio"`
	Posts     int32  `json:"posts"`
	Likes     int32  `json:"likes"`
	Following int32  `json:"following"`
	Followers int32  `json:"followers"`
	Followed  bool   `json:"followed"`
	Created   string `json:"created"`
}

func newUser(u *pb.User) user {
	return user{
		ID:        u.Id,
		Name:      u.Name,
		Username:  u.Username,
		Email:     u.Email,
		Bio:       u.Bio,
		Posts:     u.Posts,
		Likes:     u.Likes,
		Following: u.Following,
		Followers: u.Followers,
		Followed:  u.Followed,
		Created:   u.Created,
	}
}
