from flask import (
    Blueprint, redirect, request, session, url_for, make_response, jsonify
)
from werkzeug.security import check_password_hash, generate_password_hash


bp = Blueprint('follow', __name__)

@bp.route('/users/<username>/followers', methods=['GET'])
def get_followers(username):
    return make_response(jsonify({'response': 'Get followers'}), 200)

@bp.route('/users/<username>/following', methods=['GET'])
def get_following(username):
    return make_response(jsonify({'response': 'Get following'}), 200)

@bp.route('/users/<username>/following', methods=['POST'])
def follow_user(username):
    return make_response(jsonify({'response': 'Follow user'}), 200)

@bp.route('/users/<username>/following', methods=['DELETE'])
def unfollow_user(username):
    return make_response(jsonify({'response': 'Unfollow user'}), 200)
