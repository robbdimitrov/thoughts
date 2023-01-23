import React from 'react';
import {Route, Switch} from 'react-router-dom';

import ThoughtList from '../../shared/components/thoughtlist/ThoughtList';
import UserList from '../../shared/components/userlist/UserList';
import ControlBar from './ControlBar';
import UserHeader from './UserHeader';
import './Profile.scss';

function Profile({match}) {
  return (
    <div className='profile-container'>
      <UserHeader />
      <ControlBar path={match.url} />

      <div className='profile-content main-content'>
        <Switch>
          <Route
            path={`${match.path}/`} exact
            render={() => <ThoughtList items={3} />}
          />
          <Route
            path={`${match.path}/following`} exact
            render={() => <UserList items={5} />}
          />
          <Route
            path={`${match.path}/followers`} exact
            render={() => <UserList items={3} />}
          />
          <Route
            path={`${match.path}/likes`} exact
            render={() => <ThoughtList items={3} />}
          />
        </Switch>
      </div>
    </div>
  );
}

export default Profile;
