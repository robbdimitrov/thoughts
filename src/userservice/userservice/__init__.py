import os

from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config['DATABASE_URI'] = os.getenv('DATABASE_URI')

    # Register the database client
    from userservice import db
    db.init_app(app)

    # Register the api routes
    from userservice import user, follow
    app.register_blueprint(user.bp)
    app.register_blueprint(follow.bp)

    return app
