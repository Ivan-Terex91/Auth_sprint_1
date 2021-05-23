from flask_restx import Api

from core.exceptions import AuthError, NotFound

api = Api(title="Auth")


@api.errorhandler(NotFound)
def handle_not_found_error(error):
    return {"message": f"{error!s}"}, 404


@api.errorhandler(AuthError)
def handle_permission_error(error):
    return {"message": f"{error!s}"}, 401
