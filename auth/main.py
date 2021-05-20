from api.v1.auth import ns as auth_ns
from api.v1.users import ns as profile_ns
from core.db import db
from flask import Flask
from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy
from services.auth import TokenService
from services.user import (ChangePasswordService, UserHistoryService,
                           UserService)


class Services:
    def __init__(self, db):
        self.user = UserService(db)
        self.user_history = UserHistoryService(db)
        self.change_password = ChangePasswordService(db)
        self.token_service = TokenService(db)


def create_app():
    app = Flask(__name__)
    # db = SQLAlchemy(app)

    api = Api(app, title="Auth")

    api.add_namespace(profile_ns, "/api/v1/profile")
    api.add_namespace(auth_ns, "/api/v1/auth")

    api.services = Services(db)

    return app


app = create_app()
