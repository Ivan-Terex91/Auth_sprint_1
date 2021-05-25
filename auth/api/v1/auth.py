from flask import g
from flask_restx import Namespace

from api.v1.models.auth import (
    LoginResponseModel,
    RefreshTokenModel,
    RefreshTokensResponseModel,
    SignupResponseModel,
)
from api.v1.models.users import LoginRequestModel, UserModel
from core.api import Resource, login_required

ns = Namespace("Auth Namespace")


# signup = ns.add_model(name="signup", definition=signup_model)
# tokens = ns.add_model(name="tokens", definition=tokens_model)
# refresh_token = ns.add_model(name="refresh_token", definition=refresh_token_model)


@ns.route("/signup/")
class SignupView(Resource):
    @ns.expect(LoginRequestModel, validate=True)
    @ns.response(409, description="This email address is already in use")
    @ns.response(400, description="Bad request")
    @ns.response(201, description="Successfully signup in", model=SignupResponseModel)
    def post(self):
        """Signup new user"""
        self.services.user.create(**self.api.payload)
        return {"message": "Successfully signup in"}, 201


@ns.route("/login/")
class LoginView(Resource):
    @ns.expect(LoginRequestModel, validate=True)
    @ns.response(404, description="User not found")
    @ns.response(400, description="Bad request")
    @ns.response(401, description="Unauthorized")
    @ns.response(200, description="Successfully logged in", model=LoginResponseModel)
    def post(self):
        """Login in user"""
        user = self.services.user.get_by_email_password(
            email=self.api.payload.get("email"), password=self.api.payload.get("password")
        )
        if not user:
            return {"message": "User not found"}, 404
        user_id = user.id
        access_token, refresh_token = self.services.token_service.create_tokens(user_id)

        return {"access_token": access_token, "refresh_token": refresh_token}, 200


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
