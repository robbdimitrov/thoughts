from flask import (
    Blueprint, request, make_response, jsonify
)

from userservice import db_client, status
from userservice.db_client import DBException


bp = Blueprint('follow', __name__)

@bp.route('/users/<username>/followers', methods=['GET'])
def get_followers(username):
    """Returns users followed by the user."""
    return make_response(jsonify({'response': 'Get followers'}), status.OK)


@bp.route('/users/<username>/following', methods=['GET'])
def get_following(username):
    """Returns users following the user."""
    return make_response(jsonify({'response': 'Get following'}), status.OK)


@bp.route('/users/<username>/following', methods=['POST'])
def follow_user(username):
    """Follows a user with the current user."""
    # TODO: Get id of current user
    user_id = '2'

    try:
        db_client.follow_user(username, user_id)
    except DBException as e:
        return make_response(jsonify({'error': str(e)}), status.BAD_REQUEST)
    else:
        return make_response(jsonify({'response': 'Followed user.'}),
            status.OK)


@bp.route('/users/<username>/following', methods=['DELETE'])
def unfollow_user(username):
    """Unfollows a user with the current user."""
    return make_response(jsonify({'response': 'Unfollow user'}), status.OK)
