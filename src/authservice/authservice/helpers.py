import bcrypt
import jwt

from authservice.auth import AuthException


def validate_token(auth_header, secret):
    """Helper method for token validation"""

    if auth_header is None:
        raise AuthException(400, 'INVALID_TOKEN', 'Authentication token not provided.')

    auth_token = auth_header.split(' ')[1]

    try:
        payload = jwt.decode(auth_token, secret, algorithms='HS256')
    except jwt.ExpiredSignatureError:
        raise AuthException(401, 'EXPIRED_TOKEN', 'Authorization token is expired.')

    return payload
