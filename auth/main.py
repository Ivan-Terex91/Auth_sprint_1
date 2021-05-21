from flask import Flask
from pydantic import BaseSettings, PostgresDsn, RedisDsn
from redis import Redis

from api import api
from api.v1.auth import ns as auth_ns
from api.v1.users import ns as profile_ns
from core.db import init_session
from services.auth import TokenService
from services.user import ChangePasswordService, UserHistoryService, UserService


class Settings(BaseSettings):
    redis_dsn: RedisDsn
    postgres_dsn: PostgresDsn
    secret_key: str


class Services:
    def __init__(self, session, redis):
        self.session = session
        self.redis = redis
        self.user = UserService(session)
        self.user_history = UserHistoryService(session)
        self.change_password = ChangePasswordService(session)
        self.token_service = TokenService(session)


def create_app():
    settings = Settings()

    app = Flask(__name__)

    session = init_session(f"{str(settings.postgres_dsn)}/auth")
    redis = Redis(host=settings.redis_dsn.host, port=settings.redis_dsn.port, db=1)

    api.init_app(app)
    api.add_namespace(profile_ns, "/api/v1/profile")
    api.add_namespace(auth_ns, "/api/v1/auth")

    api.services = Services(session, redis)

    return app


app = create_app()
