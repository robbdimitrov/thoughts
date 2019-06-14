import apiClient from '../../common/APIClient';

export const INVALIDATE_FEED = 'INVALIDATE_FEED';
export function invalidateFeed() {
  return {
    type: INVALIDATE_FEED
  };
}

export const FETCH_FEED = 'FETCH_FEED';
export function fetchFeed(page) {
  return (dispatch) => {
    apiClient.getFeed(page).then((response) => {
      if (!response.ok) {
        dispatch({
          type: FETCH_FEED,
          error: response.error.message
        });
        return;
      }

      dispatch({
        type: FETCH_FEED,
        posts: response.posts,
        page
      });
    });
  };
}