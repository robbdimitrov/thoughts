package api

import pb "github.com/robbdimitrov/thoughts/src/apigateway/genproto"

func mapUser(u *pb.User) user {
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

func mapPost(p *pb.Post) post {
	return post{
		ID:       p.Id,
		UserID:   p.UserId,
		Content:  p.Content,
		Likes:    p.Likes,
		Liked:    p.Liked,
		Reposts:  p.Reposts,
		Reposted: p.Reposted,
		Created:  p.Created,
	}
}
