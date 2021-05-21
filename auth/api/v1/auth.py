from flask_restx import Namespace

from core.api import Resource
from models.auth import refresh_token_model, signup_model, tokens_model

ns = Namespace("Auth Namespace")
signup = ns.add_model(name="signup", definition=signup_model)
tokens = ns.add_model(name="tokens", definition=tokens_model)
refresh_token = ns.add_model(name="refresh_token", definition=refresh_token_model)


@ns.route("/signup/")
class Signup(Resource):
    @ns.expect(signup)
    @ns.response(201, "Successfully signup in")
    @ns.response(409, "The email you entered is already in use")
    def post(self):
        """Signup new user"""
        return "Successfully signup in"


@ns.route("/login/")
class Login(Resource):
    @ns.expect(signup)
    @ns.response(200, "Successfully logged in", tokens)
    @ns.response(404, "User not found")
    def post(self):
        """Login in user"""
        return self.services.token_service.get()


@ns.route("/logout/")
class Logout(Resource):
    @ns.response(200, "Successfully logout")
    def get(self):
        """Logout user"""
        return "Successfully logout"


@ns.route("/refresh/")
class Refresh(Resource):
    @ns.expect(refresh_token)
    @ns.response(200, "Successfully getting new access and refresh tokens", tokens)
    @ns.response(404, "refresh token not found")
    def get(self):
        """Getting refresh token"""
        return self.services.token_service.get()
