from grpc import StatusCode

from userservice import thoughts_pb2_grpc, thoughts_pb2
from userservice.crypto import generate_hash, validate_password
from userservice.utils import is_valid_email
from userservice import logger


class Controller(thoughts_pb2_grpc.UserServiceServicer):
    def __init__(self, db_client):
        self.db_client = db_client

    def CreateUser(self, request, context):
        username = request.username
        email = request.email
        name = request.name or ''
        password = request.password

        error_message = None
        error_type = None

        if len(username) == 0:
            error_message = 'Username is missing.'
            error_type = 'MISSING_USERNAME'
        elif len(email) == 0:
            error_message = 'Email is missing.'
            error_type = 'MISSING_EMAIL'
        elif is_valid_email(email) == False:
            error_message = 'Invalid email address.'
            error_type = 'INVALID_EMAIL'
        elif len(password) == 0:
            error_message = 'Password is missing'
            error_type = 'MISSING_PASSWORD'

        if error_message is not None:
            error = thoughts_pb2.Error(code=400,
                error=error_type,
                message=error_message)
            return thoughts_pb2.Status(error=error)

        password = make_password_hash(password)

        try:
            self.db_client.create_user(username, email, name, password)
        except exceptions.ExistingUserException as e:
            error = thoughts_pb2.Error(code=400,
                error='USER_EXISTS',
                message=str(e))
            return thoughts_pb2.Status(error=error)
        except exceptions.DbException as e:
            error = thoughts_pb2.Error(code=400,
                error='BAD_REQUEST',
                message=str(e))
            return thoughts_pb2.Status(error=error)

        return thoughts_pb2.Status(message='User created.')

    def GetUser(self, request, context):
        """Gets user with username or user_id from the database."""

        user = self.db_client.get_user(request.user_id, request.username)

        if user is None:
            error = thoughts_pb2.Error(code=404
                error='NOT_FOUND',
                message='User not found.')
            return thoughts_pb2.UserStatus(error=error)

        return thoughts_pb2.UserStatus(user=user)

    def UpdateUser(self, request, context):
        response = self.auth_client.validate(request.token)

        if response.error.code != 0:
            return thoughts_pb2.Status(error=response.error)

        user_id = response.user_id

        changes = {}

        changes['username'] = request.username
        changes['name'] = request.name
        changes['bio'] = request.bio
        changes['avatar'] = request.avatar

        email = request.email

        error_message = None
        error_type = None

        if validate_email(email) == False:
            error_message = 'Invalid email address.'
            error_type = 'INVALID_EMAIL'
        else:
            changes['email'] = email

        if error_type is not None:
            error = thoughts_pb2.Error(code=400,
                message=error_message)
            return thoughts_pb2.Status(error=error)

        try:
            self.db_client.update_user(user_id, changes)
        except:
            error = thoughts_pb2.Error(code=400,
                message='User update failed.')
            return thoughts_pb2.Status(error=error)
        else:
            return thoughts_pb2.Status(message=f'User updated.')

    def UpdatePassword(self, request, context):
        response = self.auth_client.validate(request.token)

        if response.error.code != 0:
            return thoughts_pb2.Status(error=response.error)

        user_id = response.user_id

        changes = {}

        password = request.password
        old_password = request.old_password

        error_message = None
        error_type = None

        if len(password) == 0:
            error_message = 'Password is missing.'
            error_type = 'MISSING_PASSWORD'
        else:
            if len(old_password) == 0:
                error_message = 'Current password is missing.'
                error_type = 'MISSING_PASSWORD'
            else:
                user = self.db_client.get_user(user_id)

                result = self.auth_client.validate_password(user['email'], password)

                if result.error.code != 0:
                    error_message = 'Wrong password.'
                    error_type = 'WRONG_PASSWORD'
                else:
                    password = make_password_hash(password)
                    changes['password'] = password

        if error_type is not None:
            error = thoughts_pb2.Error(code=400,
                error=error_type,
                message=error_message)
            return thoughts_pb2.Status(error=error)

        try:
            self.db_client.update_user(user_id, changes)
        except:
            error = thoughts_pb2.Error(code=400,
                error='BAD_REQUEST',
                message='User update failed.')
            return thoughts_pb2.Status(error=error)
        else:
            return thoughts_pb2.Status(message=f'User updated.')

    def GetFollowing(self, request, context):
        user_id = request.user_id
        page = request.page
        limit = request.limit

        users = self.db_client.get_following(user_id, page, limit)

        return thoughts_pb2.Users(users=users)

    def GetFollowers(self, request, context):
        user_id = request.user_id
        page = request.page
        limit = request.limit

        users = self.db_client.get_followers(user_id, page, limit)

        return thoughts_pb2.Users(users=users)

    def FollowUser(self, request, context):
        response = self.auth_client.validate(request.token)

        if response.error.code != 0:
            return thoughts_pb2.Status(error=response.error)

        current_id = response.user_id
        user_id = request.user_id

        try:
            self.db_client.follow_user(user_id, current_id)
        except UserNotFoundException as e:
            error = thoughts_pb2.Error(code=404,
                error='NOT_FOUND',
                message=str(e))
            return thoughts_pb2.Status(error=error)
        except DbException as e:
            error = thoughts_pb2.Error(code=400,
                error='BAD_REQUEST',
                message=str(e))
            return thoughts_pb2.Status(error=error)
        else:
            return thoughts_pb2.Status(message='User followed.')

    def UnfollowUser(self, request, context):
        response = self.auth_client.validate(request.token)

        if response.error.code != 0:
            return thoughts_pb2.Status(error=response.error)

        follower_id = response.user_id
        user_id = request.user_id

        self.db_client.unfollow_user(user_id, follower_id)

        return thoughts_pb2.Status(message='User unfollowed.')
