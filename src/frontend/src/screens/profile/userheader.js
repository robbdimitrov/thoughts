import React from 'react';
import {FontAwesomeIcon} from '@fortawesome/react-fontawesome';

import './userheader.scss';

function UserHeader(props) {
  return (
    <div className='user-header container'>
      <div className='cover'></div>

      <div className='content main-content'>
        <button className='follow-button outline-button'>
          Follow
        </button>

        <div className='texts'>
          <span className='name bold'>{props.user.name}</span>
          <span className='username'>@{props.user.username}</span>
          <p className='bio'>{props.user.bio}</p>

          <div className='join-date'>
            <FontAwesomeIcon icon='calendar-alt' className='join-date-icon' />
            <span className='join-date-text'>Joined March 2011</span>
          </div>
        </div>
      </div>
    </div>
  );
}

export default UserHeader;
