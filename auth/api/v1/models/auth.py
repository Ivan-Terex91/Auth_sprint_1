from flask_restx import Model, fields

UserModel = Model("UserModel", {"id": fields.String(), "email": fields.String()})
