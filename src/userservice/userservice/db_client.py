import psycopg2
from psycopg2 import errorcodes
from userservice import db


def create_user(username, email, name, password):
    conn = db.get_db()
    cur = conn.cursor()

    cur.execute('''
        SELECT username, email FROM thoughts.user
        WHERE username = %s OR email = %s
        ''',
        (username, email))
    existing_user = cur.fetchone()

    if existing_user != None:
        if existing_user[0] == username:
            raise Exception('User with this username already exists.')
        else:
            raise Exception('User with this email already exists.')

    try:
        cur.execute('''
            INSERT INTO thoughts.user(username, email, name, password)
            VALUES(%s, %s, %s, %s);
            ''',
            (username, email, name, password))
        conn.commit()
    except psycopg2.Error as e:
        name = errorcodes.lookup(e.pgcode)
        print(f'exception {name} error: {str(e)}')
    finally:
        cur.close()
