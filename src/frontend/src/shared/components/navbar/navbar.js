import React, {useState} from 'react';
import {FontAwesomeIcon} from '@fortawesome/react-fontawesome';

import Link from '../../router/link';
import UserDropdown from './dropdown';
import './navbar.scss';

function Navbar(props) {
  const [state, setState] = useState({
    isDropdownShown: false
  });

  function handleClick() {
    setState((state) => ({
      ...state,
      isDropdownShown: !state.isDropdownShown
    }));
  }

  return (
    <header className='navigation-container bottom-shadow'>
      <div className='navigation-content main-container'>
        {props.isLoggedIn ? (
          <div className='left-items'>
            <Link href='/feed' className='nav-button'>
              <FontAwesomeIcon
                icon='home'
                className='nav-button-icon'
                size='2x'
              />
              <span className='nav-button-label'>Home</span>
            </Link>
          </div>
        ) : (
          <div className='left-items'></div>
        )}

        <FontAwesomeIcon icon='brain' className='icon' size='2x' />

        {props.user ? (
          <div className='right-items'>
            <div className='profile-button' onClick={handleClick}>
              <img
                className='profile-button-image'
                src='https://via.placeholder.com/300.png'
                alt='Profile'
              />

              {state.isDropdownShown &&
                <UserDropdown
                  user={props.user}
                  logoutUser={props.logoutUser}
                />
              }
            </div>
          </div>
        ) : (
          <div className='right-items'>
            <Link href='/login' className='button login-button'>
              Log In
            </Link>
          </div>
        )}
      </div>
    </header>
  );
}

export default Navbar;
