from flask import (
    Blueprint, request, make_response, jsonify
)
from werkzeug.security import generate_password_hash
import re

from userservice import db, status


bp = Blueprint('user', __name__)

@bp.route('/users', methods=['POST'])
def create_user():
    content = request.get_json()

    username = content.get('username')
    email = content.get('email')
    name = content.get('name') or ''
    password = content.get('password')

    if username == None or username == '':
        error = 'Username is missing.'
    elif email == None or email == '':
        error = 'Email is missing.'
    elif re.match(r'[^@]+@[^@]+\.[^@]+', email) == None:
        error = 'Invalid email address.'
    elif password == None:
        error = 'Password is missing'
    else:
        error = None

    if error != None:
        return make_response(jsonify({'error': error}), status.BAD_REQUEST)

    password = generate_password_hash(password)

    cur = db.get_db().cursor()
    cur.execute('''
        INSERT INTO thoughts.user(username, email, name, password)
        VALUES(%s, %s, %s, %s);
        ''',
        (username, email, name, password))
    cur.close()

    return make_response(jsonify({'response': f'Created user {email}.'}),
        status.CREATED)


@bp.route('/users/<username>', methods=['GET'])
def get_user(username):
    return make_response(jsonify({'response': 'Get user'}), 200)


@bp.route('/users/<username>', methods=['UPDATE'])
def update_user(username):
    return make_response(jsonify({'response': 'Update user'}), 200)


@bp.route('/users/<username>', methods=['PUT'])
def update_user_field(username):
    return make_response(jsonify({'response': 'Update user field'}), 200)


@bp.route('/users/<username>', methods=['DELETE'])
def delete_user(username):
    return make_response(jsonify({'response': 'Delete user'}), 200)
