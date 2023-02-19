package post

import pb "github.com/robbdimitrov/thoughts/src/apigateway/genproto"

type post struct {
	ID       int32  `json:"id"`
	UserID   int32  `json:"userId"`
	Content  string `json:"content"`
	Likes    int32  `json:"likes"`
	Liked    bool   `json:"liked"`
	Reposts  int32  `json:"reposts"`
	Reposted bool   `json:"reposted"`
	Created  string `json:"created"`
}

func newPost(p *pb.Post) post {
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
