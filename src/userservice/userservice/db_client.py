import psycopg2
from userservice import db


class DBException(Exception):
    pass


def create_user(username, email, name, password):
    conn = db.get_db()
    cur = conn.cursor()

    cur.execute('''
        SELECT username, email FROM thoughts.user
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
            INSERT INTO thoughts.user(username, email, name, password)
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
        to_char(reg_date, 'DD-MM-YYYY"T"HH24:MI:SS') FROM thoughts.user
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


def update_user(username, updates):
    conn = db.get_db()
    cur = conn.cursor()

    values = list(map(lambda key: f'{key} = \'{updates[key]}\'',
        list(updates.keys())))

    command = f'''UPDATE thoughts.user SET {', '.join(values)}
    WHERE username = %s;'''
    print(command)
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
        DELETE FROM thoughts.user
        WHERE username = %s
        ''',
        (username,))
    conn.commit()
    cur.close()
