from flask_restx import Namespace

from core.api import Resource

ns = Namespace("Profile Namespace")


@ns.route("/")
class UserProfile(Resource):
    def get(self):
        return self.services.user.get(123)
