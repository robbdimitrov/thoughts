import React from 'react';
import { connect } from 'react-redux';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import PropTypes from 'prop-types';

import { updateUser } from '../store/actions/users';
import session from '../common/services/Session';

class EditProfile extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      name: '',
      username: '',
      email: ''
    };

    this.handleSubmit = this.handleSubmit.bind(this);
    this.handleInputChange = this.handleInputChange.bind(this);
  }

  componentWillMount() {
    const { name, username, email } = this.props.user;

    this.setState({
      name,
      username,
      email
    });
  }

  handleSubmit(event) {
    event.preventDefault();

    const { name, username, email } = this.state;
    this.props.updateUser(name, username, email);
  }

  handleInputChange(event) {
    const target = event.target;
    const value = target.value;
    const name = target.name;

    this.setState({
      [name]: value
    });
  }

  render() {
    return (
      <div className="form-content">
        <h1 className="form-title">Edit Profile</h1>

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
              required
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
              required
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
  updateUser: PropTypes.func.isRequired
};

const mapStateToProps = (state) => {
  return {
    user: state.users.byId[session.getUserId()]
  };
};

export default connect(
  mapStateToProps,
  { updateUser }
)(EditProfile);
