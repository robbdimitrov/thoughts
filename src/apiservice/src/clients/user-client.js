import * as grpc from 'grpc';

import * as services from '../genproto/thoughts_grpc_pb';
import * as messages from '../genproto/thoughts_pb';
import { APIClient } from './api-client';

export class UserClient extends APIClient {
  constructor(serviceURI) {
    super(serviceURI);

    this.userClient = new services.UserServiceClient(this.serviceURI,
      grpc.credentials.createInsecure());
    this.followClient = new services.FollowServiceClient(this.serviceURI,
      grpc.credentials.createInsecure());
  }

  // Users

  createUser(username, email, name, password) {
    const request = new messages.UserUpdates();
    request.setUsername(username);
    request.setEmail(email);
    request.setName(name);
    request.setPassword(password);

    return new Promise((res, rej) => {
      this.userClient.createUser(request, (err, response) => {
        if (err) {
          return rej(err);
        }
        const error = response.getError();
        if (error !== undefined) {
          return this.handleError(error, rej);
        }
        res({message: response.getMessage()});
      });
    });
  }

  getUser(userId, token) {
    const request = new messages.UserRequest();
    request.setUserId(userId);
    request.setToken(token);

    return new Promise((res, rej) => {
      this.userClient.getUser(request, (err, response) => {
        if (err) {
          return rej(err);
        }
        const error = response.getError();
        if (error !== undefined) {
          return this.handleError(error, rej);
        }

        const item = response.getUser();
        const user = {
          id: item.getId(),
          username: item.getUsername(),
          email: item.getEmail(),
          name: item.getName(),
          bio: item.getBio(),
          avatar: item.getAvatar(),
          date_created: item.getDateCreated()
        };
        res({user});
      });
    });
  }

  updateUser(username, email, name, password, bio, oldPassword, token) {
    const request = new messages.UserUpdates();
    request.setUsername(username);
    request.setEmail(email);
    request.setName(name);
    request.setPassword(password);
    request.setBio(bio);
    request.setOldPassword(oldPassword);
    request.setToken(token);

    return new Promise((res, rej) => {
      this.userClient.updateUser(request, (err, response) => {
        if (err) {
          return rej(err);
        }
        const error = response.getError();
        if (error !== undefined) {
          return this.handleError(error, rej);
        }
        res({message: response.getMessage()});
      });
    });
  }

  deleteUser(userId, token) {
    const request = new messages.UserRequest();
    request.setUserId(userId);
    request.setToken(token);

    return new Promise((res, rej) => {
      this.userClient.deleteUser(request, (err, response) => {
        if (err) {
          return rej(err);
        }
        const error = response.getError();
        if (error !== undefined) {
          return this.handleError(error, rej);
        }
        res({message: response.getMessage()});
      });
    });
  }

  // Follows

  getFollowing(userId, token, page, limit) {
    const request = new messages.DataRequest();
    request.setUserId(userId);
    request.setToken(token);
    request.setPage(page);
    request.setLimit(limit);

    return new Promise((res, rej) => {
      this.userClient.getFollowing(request, (err, response) => {
        if (err) {
          return rej(err);
        }
        const users = [];
        for (const item of response.getUsers()) {
          const user = {
            id: item.getId(),
            username: item.getUsername(),
            email: item.getEmail(),
            name: item.getName(),
            bio: item.getBio(),
            avatar: item.getAvatar(),
            date_created: item.getDateCreated()
          };
          users.push(user);
        }
        res({users});
      });
    });
  }

  getFollowers(userId, token, page, limit) {
    const request = new messages.DataRequest();
    request.setUserId(userId);
    request.setToken(token);
    request.setPage(page);
    request.setLimit(limit);

    return new Promise((res, rej) => {
      this.userClient.getFollowers(request, (err, response) => {
        if (err) {
          return rej(err);
        }
        const users = [];
        for (const item of response.getUsers()) {
          const user = {
            id: item.getId(),
            username: item.getUsername(),
            email: item.getEmail(),
            name: item.getName(),
            bio: item.getBio(),
            avatar: item.getAvatar(),
            date_created: item.getDateCreated()
          };
          users.push(user);
        }
        res({users});
      });
    });
  }

  followUser(userId, token) {
    const request = new messages.UserRequest();
    request.setUserId(userId);
    request.setToken(token);

    return new Promise((res, rej) => {
      this.userClient.follow(request, (err, response) => {
        if (err) {
          return rej(err);
        }
        const error = response.getError();
        if (error !== undefined) {
          return this.handleError(error, rej);
        }
        res({message: response.getMessage()});
      });
    });
  }

  unfollowUser(userId, token) {
    const request = new messages.UserRequest();
    request.setUserId(userId);
    request.setToken(token);

    return new Promise((res, rej) => {
      this.userClient.unfollow(request, (err, response) => {
        if (err) {
          return rej(err);
        }
        const error = response.getError();
        if (error !== undefined) {
          return this.handleError(error, rej);
        }
        res({message: response.getMessage()});
      });
    });
  }
}
