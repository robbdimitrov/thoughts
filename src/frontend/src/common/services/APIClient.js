import session from './Session';
import { apiRoot } from '../../config';

class APIClient {
  // Internal

  headers() {
    const headers = new Headers({
      'Content-Type': 'application/json'
    });

    const token = session.getToken();
    if (token) {
      headers.set('Authorization', `Bearer ${token}`);
    }

    return headers;
  }

  request(urlPath, method = 'GET', body, otherHeaders) {
    const headers = otherHeaders || this.headers();

    const url = apiRoot + urlPath;

    const options = { method, headers };

    if (body) {
      if (headers.get('Content-Type') === 'application/json') {
        options.body = JSON.stringify(body);
      } else {
        options.body = body;
      }
    }

    return fetch(url, options)
      .then((response) => response.json());
  }

  // Session

  createSession(email, password) {
    const url = '/sessions';
    const body = { email, password };
    return this.request(url, 'POST', body);
  }

  refreshToken() {
    const url = '/sessions';
    const headers = this.headers();
    const token = session.getRefreshToken();
    headers.set('Authorization', `Bearer ${token}`);
    return this.request(url, 'POST', undefined, headers);
  }

  getSessions() {
    const url = '/sessions';
    return this.request(url);
  }

  deleteSession(sessionId) {
    const url = `/sessions/${sessionId}`;
    return this.request(url, 'DELETE');
  }

  // User

  createUser(name, username, email, password) {
    const url = '/users';
    const body = { name, username, email, password };
    return this.request(url, 'POST', body);
  }

  updateUser(name, username, email, bio, avatar) {
    const url = `/users/${session.getUserId()}`;

    const body = {
      name,
      username,
      email,
      bio,
      avatar
    };

    return this.request(url, 'PUT', body);
  }

  updatePassword(password, oldPassword) {
    const url = `/users/${session.getUserId()}`;

    const body = {
      password,
      old_password: oldPassword
    };

    return this.request(url, 'PUT', body);
  }

  getUser(userId, username) {
    let url = `/users/${userId}`;

    if (username) {
      url = `/users?username=${username}`;
    }

    return this.request(url);
  }

  getFollowingIds(userId) {
    const url = `/users/${userId}/following?ids=1`;
    return this.request(url);
  }

  getFollowing(userId, page, limit = 20) {
    const url = `/users/${userId}/following?page=${page}&limit=${limit}`;
    return this.request(url);
  }

  getFollowersIds(userId) {
    const url = `/users/${userId}/following?ids=1`;
    return this.request(url);
  }

  getFollowers(userId, page, limit = 20) {
    const url = `/users/${userId}/followers?page=${page}&limit=${limit}`;
    return this.request(url);
  }

  // User actions

  followUser(userId) {
    const url = `/users/${userId}/following`;
    return this.request(url, 'POST');
  }

  unfollowUser(userId) {
    const url = `/users/${userId}/following`;
    return this.request(url, 'DELETE');
  }

  // Post

  createPost(content) {
    const url = '/posts';
    const body = { content };
    return this.request(url, 'POST', body);
  }

  getPost(postId) {
    const url = `/posts/${postId}`;
    return this.request(url);
  }

  deletePost(postId) {
    const url = `/posts/${postId}`;
    return this.request(url, 'DELETE');
  }

  getFeed(page, limit = 20) {
    const url = `/posts/feed?page=${page}&limit=${limit}`;
    return this.request(url);
  }

  getPosts(userId, page, limit = 20) {
    const url = `/users/${userId}/posts?page=${page}&limit=${limit}`;
    return this.request(url);
  }

  getLikes(userId, page, limit = 20) {
    const url = `/users/${userId}/likes?page=${page}&limit=${limit}`;
    return this.request(url);
  }

  // Post actions

  likePost(postId) {
    const url = `/posts/${postId}/likes`;
    return this.request(url, 'POST');
  }

  unlikePost(postId) {
    const url = `/posts/${postId}/likes`;
    return this.request(url, 'DELETE');
  }

  retweetPost(postId) {
    const url = `/posts/${postId}/retweets`;
    return this.request(url, 'POST');
  }

  deleteRetweet(postId) {
    const url = `/posts/${postId}/retweets`;
    return this.request(url, 'DELETE');
  }

  // Image

  postImage(file) {
    const url = `/images`;

    const headers = this.headers();
    headers.delete('Content-Type');

    const formData = new FormData()
    formData.append('image', file);

    return this.request(url, 'POST', formData, headers);
  }
}

const apiClient = new APIClient();

export default apiClient;