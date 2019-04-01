from flask import (
    Blueprint, request, make_response, jsonify
)
from werkzeug.security import generate_password_hash
import re

from userservice import status, db_client
from userservice.db_client import DBException


bp = Blueprint('user', __name__)

@bp.route('/users', methods=['POST'])
def create_user():
    """Validates input and creates new user account."""

    content = request.get_json()

    username = content.get('username')
    email = content.get('email')
    name = content.get('name') or ''
    password = content.get('password')

    if username is None or username == '':
        error = 'Username is missing.'
    elif email is None or email == '':
        error = 'Email is missing.'
    elif re.match(r'[^@]+@[^@]+\.[^@]+', email) is None:
        error = 'Invalid email address.'
    elif password is None:
        error = 'Password is missing'
    else:
        error = None

    if error is not None:
        return make_response(jsonify({'error': error}), status.BAD_REQUEST)

    password = generate_password_hash(password)

    try:
        db_client.create_user(username, email, name, password)
    except DBException as e:
        return make_response(jsonify({'error': str(e)}), status.BAD_REQUEST)
    else:
        return make_response(jsonify({'response': f'Created user {email}.'}),
            status.CREATED)


@bp.route('/users/<username>', methods=['GET'])
def get_user(username):
    """Gets user with username from the database."""

    user = db_client.get_user(username)

    if user is None:
        return make_response(jsonify({'error': 'Not found.'}), status.NOT_FOUND)

    return make_response(jsonify({'user': user}), status.OK)


@bp.route('/users/<username>', methods=['PUT', 'UPDATE'])
def update_user(username):
    """Updated user with passed updated information"""
    # TODO: Check for valid auth token with decorator
    # TODO: Validate passed information
    # TODO: Return correct response
    # TODO: Handle password change

    content = request.get_json()

    db_client.update_user(username, content)
    return make_response(jsonify({'response': 'Update user'}), 200)


@bp.route('/users/<username>', methods=['DELETE'])
def delete_user(username):
    """Deleted a user if it matches the logged in user."""
    # TODO: Check for valid auth token with decorator
    db_client.delete_user(username)

    return make_response(jsonify({'response': f'Deleted user {username}'}),
        status.OK)
