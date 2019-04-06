from flask import (
    Blueprint, request, make_response, jsonify
)

from userservice import db_client, status
from userservice.db_client import DBException


bp = Blueprint('follow', __name__)

@bp.route('/users/<username>/followers', methods=['GET'])
def get_followers(username):
    """Returns users followed by the user."""

    page = request.args.get('page') or 0
    limit = request.args.get('limit') or 20

    users = db_client.get_followers(username, page, limit)

    return make_response(jsonify({'users': users}), status.OK)


@bp.route('/users/<username>/following', methods=['GET'])
def get_following(username):
    """Returns users following the user."""

    page = request.args.get('page') or 0
    limit = request.args.get('limit') or 20

    users = db_client.get_following(username, page, limit)

    return make_response(jsonify({'users': users}), status.OK)


@bp.route('/users/<username>/following', methods=['POST', 'DELETE'])
def follow_user(username):
    """Follows or unfollows a user with the current user."""

    user_id = '2' # TODO: Get id of current user

    try:
        db_client.follow_user(username, user_id)
    except DBException as e:
        return make_response(jsonify({'error': str(e)}), status.BAD_REQUEST)
    else:
        return make_response(jsonify({'response': 'Followed user.'}), status.OK)


@bp.route('/users/<username>/following', methods=['DELETE'])
def unfollow_user(username):
    """Unfollows a user with the current user."""

    user_id = '2' # TODO: Get id of current user

    db_client.unfollow_user(username, user_id)

    return make_response(jsonify({'response': 'Unfollowed user.'}), status.OK)
