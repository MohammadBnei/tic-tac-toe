import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'passkey'
    JWT_SECRET_KEY = os.environ('JWT_SECRET_KEY')
    MAIL_SERVER = os.environ('MAIL_SERVER')
    MAIL_PORT = os.environ('MAIL_PORT')
    MAIL_USERNAME = os.environ('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ('MAIL_PASSWORD')
    SQLALCHEMY_DATABASE_URI = os.environ('DATABASE_URL')
    
class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True