import React, { Suspense } from 'react';
import { BrowserRouter, Switch, Redirect } from 'react-router-dom';

import AuthedRoute from './shared/components/AuthedRoute';
import GuardRoute from './shared/components/GuardRoute';
const Feed = React.lazy(() => import('./screens/feed/Feed'));
const Profile = React.lazy(() => import('./screens/profile/Profile'));
const Login = React.lazy(() => import('./screens/user/Login'));
const Signup = React.lazy(() => import('./screens/user/Signup'));
const Settings = React.lazy(() => import('./screens/settings/Settings'));

function AppRouter(props) {
  return (
    <BrowserRouter>
      {props.children}

      <Suspense fallback={<div>Loading...</div>}>
        <Switch>
          <Redirect from="/" exact to="/feed"/>
          <GuardRoute path="/feed" exact component={Feed} />
          <GuardRoute path="/thought" component={Feed} />
          <AuthedRoute path="/login" exact component={Login} />
          <AuthedRoute path="/signup" exact component={Signup} />
          <GuardRoute path="/settings" component={Settings} />
          <GuardRoute path="/:userId" component={Profile} />
        </Switch>
      </Suspense>
    </BrowserRouter>
  );
}

export default AppRouter;