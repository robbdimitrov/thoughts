import {
  CREATE_POST, DELETE_POST, FETCH_POST,
  FETCH_POSTS, FETCH_LIKES
} from '../actions/posts';
import {
  LIKE_POST, UNLIKE_POST, RETWEET_POST, DELETE_RETWEET
} from '../actions/action';
import { FETCH_FEED } from '../actions/feed';
import { LOGOUT_USER } from '../actions/auth';
import {
  addId, addObjectsIds, removeId, addObject,
  addObjects, updateObject, removeObject
} from './helpers';

// State

const initialState = {
  byId: {},
  allIds: []
};

// Post

function addPost(state, action) {
  const { post } = action;

  return {
    byId: addObject(state.byId, post),
    allIds: addId(state.allIds, post.id)
  };
}

function addPosts(state, action) {
  const { posts } = action;

  return {
    byId: addObjects(state.byId, posts),
    allIds: addObjectsIds(state.allIds, posts)
  };
}

function deletePost(state, action) {
  const { postId } = action;

  return {
    byId: removeObject(state.byId, postId),
    allIds: removeId(state.allIds, postId)
  };
}

// Actions

function likePost(state, action) {
  const { postId } = action;

  return {
    ...state,
    byId: updateObject(state.byId, postId, {
      likes: state.byId[postId].likes + 1,
      liked: true
    })
  };
}

function unlikePost(state, action) {
  const { postId } = action;

  return {
    ...state,
    byId: updateObject(state.byId, postId, {
      likes: state.byId[postId].likes - 1,
      liked: false
    })
  };
}

function retweetPost(state, action) {
  const { postId } = action;

  return {
    ...state,
    byId: updateObject(state.byId, postId, {
      retweets: state.byId[postId].retweets + 1,
      retweeted: true
    })
  };
}

function deleteRetweet(state, action) {
  const { postId } = action;

  return {
    ...state,
    byId: updateObject(state.byId, postId, {
      retweets: state.byId[postId].retweets - 1,
      retweeted: false
    })
  };
}

// Main

function posts(state = initialState, action) {
  switch (action.type) {
    case FETCH_POST:
    case CREATE_POST:
      return addPost(state, action);
    case DELETE_POST:
      return deletePost(state, action);
    case LIKE_POST:
      return likePost(state, action);
    case UNLIKE_POST:
      return unlikePost(state, action);
    case RETWEET_POST:
      return retweetPost(state, action);
    case DELETE_RETWEET:
      return deleteRetweet(state, action);
    case FETCH_POSTS:
    case FETCH_LIKES:
    case FETCH_FEED:
      return addPosts(state, action);
    case LOGOUT_USER:
      return initialState;
    default:
      return state;
  }
}

export default posts;
