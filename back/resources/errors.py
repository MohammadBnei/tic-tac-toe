class InternalServerError(Exception):
    pass

class SchemaValidationError(Exception):
    pass

class ValidationError(Exception):
    pass

class ExpiredTokenError(Exception):
    pass

class MovieAlreadyExistsError(Exception):
    pass

class UpdatingMovieError(Exception):
    pass

class DeletingMovieError(Exception):
    pass

class MovieNotExistsError(Exception):
    pass

class EmailOrNameAlreadyExistsError(Exception):
    pass

class UnauthorizedError(Exception):
    pass

class EmailDoesnotExistsError(Exception):
    pass

class BadTokenError(Exception):
    pass

errors = {
    "InternalServerError": {
        "message": "Something went wrong",
        "status": 500
    },
     "SchemaValidationError": {
         "message": "Request is missing required fields",
         "status": 400
     },
     "ExpiredTokenError": {
         "message": "The reset token has expired",
         "status": 400
     },
     "EmailDoesnotExistsError": {
         "message": "The provided Email does not exist",
         "status": 400
     },
     "BadTokenError": {
         "message": "Incorrect token",
         "status": 403
     },
     "MovieAlreadyExistsError": {
         "message": "Movie with given name already exists",
         "status": 400
     },
     "UpdatingMovieError": {
         "message": "Updating movie added by other is forbidden",
         "status": 403
     },
     "DeletingMovieError": {
         "message": "Deleting movie added by other is forbidden",
         "status": 403
     },
     "MovieNotExistsError": {
         "message": "Movie with given id doesn't exists",
         "status": 400
     },
     "EmailOrNameAlreadyExistsError": {
         "message": "User with given email or name already exists",
         "status": 400
     },
     "UnauthorizedError": {
         "message": "Invalid username or password",
         "status": 401
     }
}