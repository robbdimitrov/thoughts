import os

from flask import Flask


def create_app():
    app = Flask(__name__)

    # register the database commands
    # from flaskr import db
    # db.init_app(app)

    from userservice import user, follow
    app.register_blueprint(user.bp)
    app.register_blueprint(follow.bp)

    return app
