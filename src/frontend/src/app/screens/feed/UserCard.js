import React from 'react';
import { Link } from 'react-router-dom';

import './UserCard.scss';

function UserCard({ user }) {
  return (
    <div className="user-card container">
      <div className="cover"></div>

      <div className="content">
        <Link to={`/${user.username}`}>
          <img
            className="avatar"
            src={user.avatar}
            alt={user.name}
          />
        </Link>

        <Link to={`/${user.username}`} className="texts">
          <p className="title semibold">{user.name}</p>
          <p className="subtitle light">@{user.username}</p>
        </Link>
      </div>

      <div className="counters">
        <div className="counter">
          <span className="counter-label light">Thoughts</span>
          <span className="counter-value">{user.thoughts}</span>
        </div>

        <div className="counter">
          <span className="counter-label light">Following</span>
          <span className="counter-value">{user.following}</span>
        </div>

        <div className="counter">
          <span className="counter-label light">Followers</span>
          <span className="counter-value">{user.followers}</span>
        </div>
      </div>
    </div>
  );
}

export default UserCard;