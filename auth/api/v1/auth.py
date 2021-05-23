from flask import g
from flask_restx import Namespace

from api.v1.models.auth import (
    LoginResponseModel,
    RefreshTokenModel,
    RefreshTokensResponseModel,
    SignupResponseModel,
)
from core.api import Resource, login_required

ns = Namespace("Auth Namespace")
# signup = ns.add_model(name="signup", definition=signup_model)
# tokens = ns.add_model(name="tokens", definition=tokens_model)
# refresh_token = ns.add_model(name="refresh_token", definition=refresh_token_model)


@ns.route("/signup/")
class SignupView(Resource):
    # @ns.expect(signup)
    @ns.response(409, "The email you entered is already in use")
    @ns.marshal_with(SignupResponseModel, "Successfully signup in", code=201)
    def post(self):
        """Signup new user"""
        user_id = "569c6eb9-d49c-483f-89ee-4c6c5354daf3"
        access_token, refresh_token = self.services.token_service.create_tokens(user_id)

        return {
            "access_token": access_token,
            "refresh_token": refresh_token,
        }


@ns.route("/login/")
class LoginView(Resource):
    # @ns.expect(signup)
    @ns.response(404, "User not found")
    @ns.marshal_with(LoginResponseModel, "Successfully logged in")
    def post(self):
        """Login in user"""
        user_id = "569c6eb9-d49c-483f-89ee-4c6c5354daf3"
        access_token, refresh_token = self.services.token_service.create_tokens(user_id)

        return {
            "access_token": access_token,
            "refresh_token": refresh_token,
        }


@ns.route("/logout/")
class LogoutView(Resource):
    @login_required
    @ns.response(200, "Successfully logout")
    def post(self):
        """Logout user"""
        self.services.token_service.remove_tokens(g.access_token)

        return "Successfully logout"


@ns.route("/refresh/")
class RefreshTokensView(Resource):
    @ns.expect(RefreshTokenModel, validate=True)
    @ns.response(404, "Refresh token not found")
    @ns.marshal_with(
        RefreshTokensResponseModel, "Successfully getting new access and refresh tokens"
    )
    def post(self):
        """Getting refresh token"""
        access_token, refresh_token = self.services.token_service.refresh_tokens(
            self.api.payload["refresh_token"]
        )

        return {
            "access_token": access_token,
            "refresh_token": refresh_token,
        }
