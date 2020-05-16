from grpc import StatusCode

from userservice import thoughts_pb2_grpc, thoughts_pb2
from userservice.crypto import generate_hash, validate_password
from userservice.utils import is_valid_email
from userservice import logger


class Controller(thoughts_pb2_grpc.UserServiceServicer):
    def __init__(self, db_client):
        self.db_client = db_client

    def CreateUser(self, request, context):
        if (len(request.username) == 0
            or len(request.email) == 0
            or len(request.password) == 0):
            context.abort(
                StatusCode.INVALID_ARGUMENT,
                'Name, username, email and password are required.'
            )
        elif is_valid_email(request.email) == False:
            context.abort(
                StatusCode.INVALID_ARGUMENT,
                'Invalid email address.'
            )

        password = generate_hash(request.password)

        try:
            user_id = self.db_client.create_user(
                request.username, request.email,
                request.name, password)
            return thoughts_pb2.Identifier(id=user_id)
        except Exception as e:
            logger.print(f'Creating user failed: {e}')
            context.abort(
                StatusCode.INVALID_ARGUMENT,
                'User with this username or email already exists.'
            )

    def GetUser(self, request, context):
        user_id = dict(context.invocation_metadata())['user-id']

        try:
            user = self.db_client.get_user(
                request.user_id, request.username, user_id)
        except Exception as e:
            logger.print(f'Getting user failed: {e}')
            context.abort(StatusCode.INTERNAL)
        else:
            if user is None:
                context.abort(StatusCode.NOT_FOUND)
            return user

    def UpdateUser(self, request, context):
        user_id = dict(context.invocation_metadata())['user-id']

        if len(request.password) != 0:
            return self.updatePassword(request, context)

        changes = {
            'name': request.name,
            'username': request.username,
            'email': request.email,
            'avatar': request.avatar,
            'bio': request.bio
        }

        if is_valid_email(changes['email']) == False:
            context.abort(
                StatusCode.INVALID_ARGUMENT,
                'Invalid email address.'
            )

        try:
            self.db_client.update_user(user_id, changes)
            return thoughts_pb2.Empty()
        except Exception as e:
            logger.print(f'Updating user failed: {e}')
            context.abort(StatusCode.INTERNAL)

    def updatePassword(self, request, context):
        user_id = dict(context.invocation_metadata())['user-id']

        if len(request.old_password) == 0:
            context.abort(
                StatusCode.INVALID_ARGUMENT,
                'Both password and the current password are required.'
            )

        user = None

        try:
            user = self.db_client.get_user_with_id(user_id)
        except Exception as e:
            logger.print(f'Getting user failed: {e}')
            context.abort(StatusCode.INTERNAL)

        if validate_password(user['email'], request.password) == False:
            context.abort(
                StatusCode.INVALID_ARGUMENT,
                'Wrong password. Enter the correct current password.'
            )

        changes = {'password': generate_hash(request.password)}

        try:
            self.db_client.update_user(user_id, changes)
            return thoughts_pb2.Empty()
        except Exception as e:
            logger.print(f'Updating user failed: {e}')
            context.abort(StatusCode.INTERNAL)

    def GetFollowing(self, request, context):
        user_id = dict(context.invocation_metadata())['user-id']

        try:
            users = self.db_client.get_following(
                request.user_id, request.page,
                request.limit, user_id)
            return thoughts_pb2.Users(users=users)
        except Exception as e:
            logger.print(f'Getting users failed: {e}')
            context.abort(StatusCode.INTERNAL)

    def GetFollowers(self, request, context):
        user_id = dict(context.invocation_metadata())['user-id']

        try:
            users = self.db_client.get_followers(
                request.user_id, request.page,
                request.limit, user_id)
            return thoughts_pb2.Users(users=users)
        except Exception as e:
            logger.print(f'Getting users failed: {e}')
            context.abort(StatusCode.INTERNAL)

    def FollowUser(self, request, context):
        user_id = dict(context.invocation_metadata())['user-id']

        try:
            self.db_client.follow_user(request.user_id, user_id)
            return thoughts_pb2.Empty()
        except Exception as e:
            logger.print(f'Following user failed: {e}')
            context.abort(StatusCode.INTERNAL)

    def UnfollowUser(self, request, context):
        user_id = dict(context.invocation_metadata())['user-id']

        try:
            self.db_client.unfollow_user(request.user_id, user_id)
            return thoughts_pb2.Empty()
        except Exception as e:
            logger.print(f'Unfollowing user failed: {e}')
            context.abort(StatusCode.INTERNAL)
