import json
from uuid import UUID

from core.api import Resource
from flask import request
from flask_restx import Namespace
from models.users import change_password_model, user_history_model, user_model

ns = Namespace("Profile Namespace")
user = ns.add_model(name="user", definition=user_model)
change_password = ns.add_model(name="change_password", definition=change_password_model)
user_history = ns.add_model(name="user_history", definition=user_history_model)


@ns.route("/<user_id>/")
@ns.response(404, "User not found")
class UserProfile(Resource):
    @ns.response(200, "Successful getting profile", user)
    def get(self, user_id: UUID):
        """Getting profile user by id"""
        return self.services.user.get(user_id)

    @ns.response(200, "Successfully updated user profile")
    @ns.expect(user)
    def put(self, user_id: UUID):
        """Change profile user by id"""
        # data = json.loads(request.data.decode())
        return self.services.user.put(user_id)

    @ns.response(204, "Successfully deleted user profile")
    def delete(self, user_id: UUID):
        """Delete profile user"""
        return self.services.user.delete(user_id)


@ns.response(404, "User not found")
@ns.route("/<user_id>/history/")
class UserHistory(Resource):
    @ns.response(200, "Successful getting history", user_history)
    def get(self, user_id):
        """Getting the user's login history"""
        return self.services.user_history.get(user_id)


@ns.response(404, "User not found")
@ns.route("/<user_id>/change_password/")
class ChangePassword(Resource):
    @ns.response(200, "Successful change password")
    @ns.expect(change_password)
    def patch(self, user_id):
        """Change user password"""
        data = json.loads(request.data.decode())
        old_password = data.get("old_password")
        new_password = data.get("old_password")
        return self.services.change_password.patch(user_id, old_password, new_password)
