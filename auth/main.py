from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restx import Api

from api.v1.users import ns as profile_ns
from services.user import UserService


class Services:
    def __init__(self, db):
        self.user = UserService(db)


def create_app():
    app = Flask(__name__)
    db = SQLAlchemy(app)

    api = Api(app, title="Auth")
    api.add_namespace(profile_ns, "/api/v1/profile")

    api.services = Services(db)

    return app


app = create_app()
