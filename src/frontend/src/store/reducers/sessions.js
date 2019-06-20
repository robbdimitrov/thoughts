import { FETCH_SESSIONS, DELETE_SESSION } from '../actions/sessions';
import { LOGOUT_USER } from '../actions/auth';
import { addObjectsIds, removeId, addObjects, removeObject } from './helpers';

const initialState = {
  byId: {},
  allIds: []
};

function addSessions(state, action) {
  const { sessions } = action;

  return {
    byId: addObjects(state.byId, sessions),
    allIds: addObjectsIds(state.allIds, sessions)
  };
}

function deleteSession(state, action) {
  const { sessionId } = action;

  return {
    byId: removeObject(state.byId, sessionId),
    allIds: removeId(state.allIds, sessionId)
  };
}

function sessions(state = initialState, action) {
  switch (action.type) {
    case FETCH_SESSIONS:
      return addSessions(state, action);
    case DELETE_SESSION:
      return deleteSession(state, action);
    case LOGOUT_USER:
      return initialState;
    default:
      return state;
  }
}

export default sessions;
