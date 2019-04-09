from flask import (
    Blueprint, request, make_response, jsonify
)
from werkzeug.security import (
    generate_password_hash, check_password_hash
)

from userservice import db_client
from userservice.helpers import validate_email


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
    elif validate_email(email) == False:
        error = 'Invalid email address.'
    elif password is None:
        error = 'Password is missing'
    else:
        error = None

    if error is not None:
        return make_response(jsonify({'error': error}), 400)

    password = generate_password_hash(password)

    try:
        db_client.create_user(username, email, name, password)
    except db_client.DBException as e:
        return make_response(jsonify({'error': str(e)}), 400)
    else:
        return make_response(jsonify({'response': f'Created user {username}.'}),
            201)


@bp.route('/users/<username>', methods=['GET'])
def get_user(username):
    """Gets user with username from the database."""

    user = db_client.get_user(username)

    if user is None:
        return make_response(jsonify({'error': 'Not found.'}), 404)

    return make_response(jsonify({'user': user}), 200)


@bp.route('/users/<username>', methods=['PUT', 'UPDATE'])
def update_user(username):
    """Updated user with passed updated information"""
    # TODO: Check for valid auth token with decorator

    content = request.get_json()
    changes = {}
    allowed_keys = ['username', 'email', 'name', 'bio', 'password']

    for key, value in content.items():
        if key in allowed_keys:
            changes[key] = value

    error = None

    if 'password' in changes:
        if 'current_password' not in changes:
            error = 'Current password is missing.'
        else:
            password = changes.get('password')
            current_password = changes.get('currentPassword')

            saved_password = db_client.get_user_password_hash(username)
            if check_password_hash(saved_password, current_password) == False:
                error = 'Wrong password.'

            password = generate_password_hash(password)
            changes['password'] = password

    email = content.get('email')

    if email is not None and validate_email(email) == False:
        error = 'Invalid email address.'

    if error is not None:
        return make_response(jsonify({'error': error}), 400)

    try:
        db_client.update_user(username, changes)
    except:
        return make_response(jsonify({'error': 'User update failed.'}), 400)
    else:
        return make_response(jsonify({'response': f'Updated user {username}.'}),
            400)


@bp.route('/users/<username>', methods=['DELETE'])
def delete_user(username):
    """Deleted a user if it matches the logged in user."""
    # TODO: Check for valid auth token with decorator
    db_client.delete_user(username)

    return make_response(jsonify({'response': f'Deleted user {username}.'}), 200)
