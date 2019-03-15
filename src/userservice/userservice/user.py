from flask import (
    Blueprint, flash, g, redirect, request, session, url_for, make_response, jsonify
)
from werkzeug.security import check_password_hash, generate_password_hash


bp = Blueprint('user', __name__)

@bp.route('/users', methods=['POST'])
def create_user():
    return make_response(jsonify({'response': 'Create user'}), 200)

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
