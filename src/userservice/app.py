from flask import Flask
import os


app = Flask(__name__)

if os.getenv('FLASK_ENV') == 'development':
    app.config.from_object('config.DevelopmentConfig')
else:
    app.config.from_object('config.Config')


@app.route('/')
def hello():
    return 'Hello, World!'


@app.route('/<name>')
def hello_name(name):
    return 'Hello {}!'.format(name)


if __name__ == '__main__':
    app.run()
