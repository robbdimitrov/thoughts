import re

from userservice import thoughts_pb2


def validate_email(email):
    return re.match(r'[^@]+@[^@]+\.[^@]+', email) is not None


def row_to_user(row):
    user = thoughts_pb2.User(
        id=row[0],
        username=row[1],
        email=row[2],
        name=row[3],
        bio=row[4],
        avatar=row[5],
        posts=row[6],
        likes=row[7],
        following=[8],
        followers=[9],
        date_created=row[10])
    return user


def rows_to_users(rows):
    users = []
    for row in rows:
        user = row_to_user(row)
        users.append(user)
    return users


def rows_to_ids(rows):
    ids = []
    for row in rows:
        ids.append(row[0])
    return ids
