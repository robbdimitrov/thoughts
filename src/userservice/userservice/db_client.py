import psycopg2
from userservice import db


class DBException(Exception):
    pass


def create_user(username, email, name, password):
    conn = db.get_db()
    cur = conn.cursor()

    cur.execute('''
        SELECT username, email FROM thoughts.users
        WHERE username = %s OR email = %s
        ''',
        (username, email))
    existing_user = cur.fetchone()

    if existing_user is not None:
        if existing_user[0] == username:
            raise DBException('User with this username already exists.')
        else:
            raise DBException('User with this email already exists.')

    try:
        cur.execute('''
            INSERT INTO thoughts.users(username, email, name, password)
            VALUES(%s, %s, %s, %s);
            ''',
            (username, email, name, password))
        conn.commit()
    except psycopg2.Error as e:
        print(f'Error creating user: {str(e)}')
    finally:
        cur.close()


def get_user(username):
    conn = db.get_db()
    cur = conn.cursor()

    cur.execute('''
        SELECT id, username, email, name, bio,
        to_char(reg_date, 'DD-MM-YYYY"T"HH24:MI:SS') FROM thoughts.users
        WHERE username = %s
        ''',
        (username,))
    result = cur.fetchone()
    cur.close()

    if result is None:
        return None

    user = {
        'id': result[0],
        'username': result[1],
        'email': result[2],
        'name': result[3],
        'bio': result[4],
        'reg_date': result[5]
    }
    return user


def get_user_password_hash(username):
    conn = db.get_db()
    cur = conn.cursor()

    cur.execute('''
        SELECT id, password,
        FROM thoughts.users
        WHERE username = %s
        ''',
        (username,))
    result = cur.fetchone()
    cur.close()

    if result is None:
        return None

    user = {
        'id': result[0],
        'password': result[1]
    }
    return user


def update_user(username, updates):
    conn = db.get_db()
    cur = conn.cursor()

    values = []
    for key, value in updates.items():
        values.append(f"{key} = '{value}'")

    command = f"UPDATE thoughts.users SET {', '.join(values)} \
        WHERE username = %s;"

    try:
        cur.execute(command, (username,))
        conn.commit()
    except psycopg2.Error as e:
        print(f'Error updating user: {str(e)}')
        raise DBException('Updating user failed.')
    finally:
        cur.close()


def delete_user(username):
    conn = db.get_db()
    cur = conn.cursor()

    cur.execute('''
        DELETE FROM thoughts.users
        WHERE username = %s
        ''',
        (username,))
    conn.commit()
    cur.close()


def get_followers(username):
    # select name, username from demo.followers, demo.users where user_id = 4;
    pass


def get_following(username):
    # select name, username from demo.followers, demo.users where follower_id = 4;
    pass


def follow_user(username, follower_id):
    conn = db.get_db()
    cur = conn.cursor()

    cur.execute('''
        SELECT id FROM thoughts.users
        WHERE username = %s
        ''',
        (username,))
    user = cur.fetchone()

    if user is None:
        raise DBException('Wrong username.')

    if user['id'] == follower_id:
        raise DBException('You can\'t follow yourself.')

    try:
        cur.execute('''
            INSERT INTO thoughts.followers
            VALUES(%s, %s);
            ''',
            (user['id'], follower_id))
        conn.commit()
    except psycopg2.Error as e:
        print(f'Error following user: {str(e)}')
    finally:
        cur.close()


def unfollow_user(username):
    # delete from demo.followers where user_id = 3, follower_id = 2;
    pass
