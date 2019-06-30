import React from 'react';
import { connect } from 'react-redux';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import PropTypes from 'prop-types';

import { updateUser, updateAvatar } from '../store/actions/users';
import session from '../common/services/Session';
import { imageURI } from '../common/utils';
import './EditProfile.scss';

class EditProfile extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      avatar: '',
      name: '',
      username: '',
      email: ''
    };

    this.handleSubmit = this.handleSubmit.bind(this);
    this.handleInputChange = this.handleInputChange.bind(this);
    this.handleImageChange = this.handleImageChange.bind(this);
  }

  componentDidMount() {
    const { avatar, name, username, email } = this.props.user;

    this.setState({
      avatar,
      name,
      username,
      email
    });
  }

  componentDidUpdate() {
    const { avatar } = this.props.user;

    if (avatar !== this.state.avatar) {
      this.setState({
        avatar
      });
    }
  }

  handleSubmit(event) {
    event.preventDefault();

    const { name, username, email } = this.state;
    this.props.updateUser(name, username, email);
  }

  handleImageChange(event) {
    this.props.updateAvatar(event.target.files[0]);
  }

  handleInputChange(event) {
    const target = event.target;
    const value = target.value;
    const name = target.name;

    this.setState({
      [name]: value
    });
  }

  profileImage() {
    if (this.props.user.avatar) {
      return imageURI(this.props.user.avatar);
    } else {
      return '';
    }
  }

  render() {
    return (
      <div className="form-content">
        <h1 className="form-title">Edit Profile</h1>

        <div className="avatar-section">
          <img
            className="avatar"
            src={this.profileImage()}
            alt={this.props.user.name}
          />

          <label htmlFor="file" className="icon-button">
            <FontAwesomeIcon icon="image" className="input-icon" />
          </label>
          <input
            id="file"
            type="file"
            accept="image/*"
            onChange={this.handleImageChange}
          />
        </div>

        <form className="action-form" onSubmit={this.handleSubmit}>
          <div className="fieldset">
            <FontAwesomeIcon icon="passport" className="input-icon" />
            <input
              className="form-input"
              type="text"
              name="name"
              placeholder="Name"
              onChange={this.handleInputChange}
              value={this.state.name}
            />
          </div>

          <div className="fieldset">
            <FontAwesomeIcon icon="user" className="input-icon" />
            <input
              className="form-input"
              type="text"
              name="username"
              placeholder="Username"
              onChange={this.handleInputChange}
              value={this.state.username}
              required
            />
          </div>

          <div className="fieldset">
            <FontAwesomeIcon icon="envelope" className="input-icon" />
            <input
              className="form-input"
              type="email"
              name="email"
              placeholder="Email"
              pattern="[^@]+@[^@]+\.[^@]+"
              onChange={this.handleInputChange}
              value={this.state.email}
              required
            />
          </div>

          <div className="fieldset long">
            <FontAwesomeIcon icon="file-alt" className="input-icon" />
            <textarea
              className="form-input"
              type="text"
              name="bio"
              placeholder="Add your bio"
              onChange={this.handleInputChange}
              value={this.state.bio}
            />
          </div>

          <input
            type="submit"
            className="button form-button"
            value="Save changes"
          />
        </form>
      </div>
    );
  }
}

EditProfile.propTypes = {
  user: PropTypes.object.isRequired,
  updateUser: PropTypes.func.isRequired,
  updateAvatar: PropTypes.func.isRequired
};

const mapStateToProps = (state) => {
  return {
    user: state.users.byId[session.getUserId()]
  };
};

export default connect(
  mapStateToProps,
  { updateUser, updateAvatar }
)(EditProfile);
