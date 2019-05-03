import datetime
import bcrypt
import jwt

from authservice import auth_service_pb2_grpc, auth_service_pb2, types_pb2
from authservice.utils import validate_email, dict_to_session


class AuthService(auth_service_pb2_grpc.AuthServiceServicer):
    def __init__(self, db_client, secret):
        self.db_client = db_client
        self.secret = secret

    def Login(self, request, context):
        pass

    def Validate(self, request, context):
        pass

    def Refresh(self, request, context):
        pass

    def GetSessions(self, request, context):
        """Get all active sessions of the active user."""

        if request.token is None:
            error = types_pb2.Error(code=400, error='INVALID_TOKEN',
                message='Authentication token not provided.')
            return types_pb2.Status(error=error)

        auth_token = request.token.split(' ')[1]

        try:
            payload = jwt.decode(auth_token, self.secret, algorithms='HS256')
        except jwt.ExpiredSignatureError:
            error = types_pb2.Error(code=401, error='EXPIRED_TOKEN',
                message='Authorization token is expired.')
            return types_pb2.Status(error=error)

        sessions = self.db_client.get_user_sessions(payload['sub'])
        sessions = [dict_to_session(item) for item in sessions]

        return auth_service_pb2.Sessions(sessions=sessions)

    def DeleteSession(self, request, context):
        """Delete a session with a given token."""

        if request.token is None:
            error = types_pb2.Error(code=400, error='INVALID_TOKEN',
                message='Authentication token not provided.')
            return types_pb2.Status(error=error)

        auth_token = request.token.split(' ')[1]

        try:
            payload = jwt.decode(auth_token, self.secret, algorithms='HS256')
        except jwt.ExpiredSignatureError:
            error = types_pb2.Error(code=401, error='EXPIRED_TOKEN',
                message='Authorization token is expired.')
            return types_pb2.Status(error=error)

        session_id = request.session_id

        if self.db_client.get_session(session_id)['user_id'] != payload['sub']:
            error = types_pb2.Error(code=403, error='FORBIDDEN',
                message='This action is forbidden.')
            return types_pb2.Status(error=error)

        self.db_client.delete_session(session_id)

        return types_pb2.Status(message='Deleted session.')


@bp.route('/session', methods=['POST'])
def create_session():
    """Create a new access and refresh tokens."""

    content = request.get_json()

    refresh_token = content.get('refresh_token')
    email = content.get('email')
    password = content.get('password')
    name = content.get('name')

    if email is not None and password is not None:
        if validate_email(email) == False:
            error = {'code': 400, 'error': 'INVALID_EMAIL',
                'message': 'Invalid email address.'}
            return make_response(jsonify({'error': error}), 400)

        # TODO: Move password validation to RPC call
        current_user = db_client.get_user_password_hash(email)
        if check_password_hash(current_user['password'], password) == False:
            error = {'code': 401, 'error': 'INVALID_CREDENTIALS',
                'message': 'Wrong username or password.'}
            return make_response(jsonify({'error': error}), 401)

        session = db_client.create_session(current_user['id'], name)
    elif refresh_token is not None:
        try:
            payload = jwt.decode(refresh_token, secret, algorithms='HS256')
        except jwt.ExpiredSignatureError:
            error = {'code': 401, 'error': 'EXPIRED_TOKEN',
                'message': 'Refresh token is expired.'}
            return make_response(jsonify({'error': error}), 401)

        session = db_client.get_session(payload['sub'])
    else:
        error = {'code': 400, 'error': 'MISSING_CREDENTIALS',
            'message': 'Missing credentials.'}
        return make_response(jsonify({'error': error}), 400)

    if session is None:
        error = {'code': 401, 'error': 'INVALID_SESSION',
            'message': 'Invalid session.'}
        return make_response({'error': error}, 401)

    access_payload = {'sub': session['user_id'],
        'iat': datetime.datetime.utcnow(),
        'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=15)}

    refresh_payload = {'sub': session['session_id'],
        'iat': datetime.datetime.utcnow(),
        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=7)}

    access_token = jwt.encode(access_payload, secret, algorithm='HS256')
    refresh_token = jwt.encode(refresh_payload, secret, algorithm='HS256')

    return make_response(jsonify({'token_type': 'bearer',
        'access_token': access_token,
        'refresh_token': refresh_token}), 200)
