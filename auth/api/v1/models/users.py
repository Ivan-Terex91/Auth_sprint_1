from flask_restx import fields

from api import api

UserModel = api.model("UserModel", {"id": fields.String(), "email": fields.String()})
