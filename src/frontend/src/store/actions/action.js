import apiClient from '../../common/APIClient';
import session from '../../common/Session';

export const LIKE_POST = 'LIKE_POST';
export function likePost(postId) {
  return function(dispatch) {
    apiClient.likePost(postId).then((response) => {
      if (!response.ok) {
        return;
      }
      dispatch({
        type: LIKE_POST,
        userId: session.getUserId(),
        postId
      });
    });
  };
}

export const UNLIKE_POST = 'UNLIKE_POST';
export function unlikePost(postId) {
  return function(dispatch) {
    apiClient.unlikePost(postId).then((response) => {
      if (!response.ok) {
        return;
      }
      dispatch({
        type: UNLIKE_POST,
        userId: session.getUserId(),
        postId
      });
    });
  };
}

export const RETWEET_POST = 'RETWEET_POST';
export function retweetPost(postId) {
  return function(dispatch) {
    apiClient.retweetPost(postId).then((response) => {
      if (!response.ok) {
        return;
      }
      dispatch({
        type: RETWEET_POST,
        userId: session.getUserId(),
        postId
      });
    });
  };
}

export const DELETE_RETWEET = 'DELETE_RETWEET';
export function deleteRetweet(postId) {
  return function(dispatch) {
    apiClient.deleteRetweet(postId).then((response) => {
      if (!response.ok) {
        return;
      }
      dispatch({
        type: DELETE_RETWEET,
        userId: session.getUserId(),
        postId
      });
    });
  };
}