class Config(object):
    DEBUG = False
    CSRF_ENABLED = True
    SECRET_KEY = 'this-really-needs-to-be-changed'

class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
