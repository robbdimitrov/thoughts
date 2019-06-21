import React from 'react';
import { connect } from 'react-redux';
import { Link } from 'react-router-dom';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import PropType from 'prop-types';

import { registerUser } from '../store/actions/users';

class Signup extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      name: '',
      username: '',
      email: '',
      password: ''
    };

    this.handleSubmit = this.handleSubmit.bind(this);
    this.handleInputChange = this.handleInputChange.bind(this);
  }

  handleSubmit(event) {
    event.preventDefault();

    const { name, username, email, password } = this.state;
    this.props.registerUser(name, username, email, password);
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
      <div className="container">
        <div className="form-content main-content">
          <h1 className="form-title">Register</h1>
          <p className="form-message">Create an account and join in!</p>

          <form className="action-form" onSubmit={this.handleSubmit}>
            <div className="fieldset">
              <FontAwesomeIcon icon="passport" className="input-icon" />
              <input
                className="form-input"
                type="text"
                name="name"
                placeholder="Name"
                onChange={this.handleInputChange}
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
                required
              />
            </div>

            <div className="fieldset">
              <FontAwesomeIcon icon="lock" className="input-icon" />
              <input
                className="form-input"
                type="password"
                name="password"
                placeholder="Password"
                minLength="4"
                maxLength="30"
                onChange={this.handleInputChange}
                required
              />
              <button className="visibility-button">
                <FontAwesomeIcon icon="eye" />
              </button>
            </div>

            <input
              className="button form-button"
              type="submit"
              value="Register"
            />
          </form>

          <div className="reference">
            <span className="reference-label">Already have an accout?</span>

            <Link to="/login" className="reference-button">
              <span>Login</span>
            </Link>
          </div>
        </div>
      </div>
    );
  }
}

Signup.propTypes = {
  registerUser: PropType.func.isRequired
};

export default connect(
  null,
  { registerUser }
)(Signup);
