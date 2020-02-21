from flask import Flask, request, Response
from flask_bcrypt import Bcrypt
from flask_restful import Api
from flask_jwt_extended import JWTManager
from flask_mail import Mail
from dotenv import load_dotenv
import os

from resources.errors import errors
from database.db import initialize_db


app = Flask(__name__)
load_dotenv()
env_config = {
    'JWT_SECRET_KEY': os.getenv('JWT_SECRET_KEY'),
    'MAIL_SERVER': os.getenv('MAIL_SERVER'),
    'MAIL_PORT': os.getenv('MAIL_PORT'),
    'MAIL_USERNAME': os.getenv('MAIL_USERNAME'),
    'MAIL_PASSWORD': os.getenv('MAIL_PASSWORD'),
    'MONGODB_SETTINGS': {
        'host': os.getenv('MONGODB_HOST')
    },
}

for (key, value) in env_config.items():
    app.config[key] = value

mail = Mail(app)

from resources.routes import initialize_routes

api = Api(app, errors=errors)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

initialize_db(app)

initialize_routes(api)
