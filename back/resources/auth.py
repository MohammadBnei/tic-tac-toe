from flask import request
from flask import Response, request
from flask_jwt_extended import create_access_token
from flask_restful import Resource
import datetime
from mongoengine.errors import FieldDoesNotExist, NotUniqueError, DoesNotExist
from resources.errors import SchemaValidationError, EmailOrNameAlreadyExistsError, UnauthorizedError, InternalServerError, ValidationError

from database.models import User

class SignupApi(Resource):
    def post(self):
        try:
            body = request.get_json()
            user = User(**body)
            user.hash_password()
            user.save()
            return 'Ok', 201
        except ValidationError:
            raise SchemaValidationError
        except FieldDoesNotExist:
            raise SchemaValidationError
        except NotUniqueError:
            raise EmailOrNameAlreadyExistsError
        except Exception:
            raise InternalServerError

class LoginApi(Resource):
    def post(self):
        try:
            body = request.get_json()
            email=body.get('email')
            name=body.get('name')
            if email:
                user = User.objects.get(email=email)
            else :
                user = User.objects.get(name=name)
                
            authorized = user.check_password(body.get('password'))
            if not authorized:
                return {'error': 'Email or password invalid'}, 401
            
            expires = datetime.timedelta(days=7)
            access_token = create_access_token(identity=str(user.id), expires_delta=expires)
            return {
                'token': access_token,
                'name' : user.name
                }, 200
        except (UnauthorizedError, DoesNotExist):
            raise UnauthorizedError
        except Exception:
            raise InternalServerError