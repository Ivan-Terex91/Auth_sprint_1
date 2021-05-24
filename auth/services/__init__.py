from flask import current_app
from werkzeug.local import LocalProxy

from services.auth import TokenService
from services.user import ChangePasswordService, UserHistoryService, UserService

services = LocalProxy(lambda: current_app.extensions["services"])


class Services:
    def __init__(self, session, redis, secret_key):
        self.session = session
        self.redis = redis
        self.user = UserService(session)
        self.user_history = UserHistoryService(session)
        self.change_password = ChangePasswordService(session)
        self.token_service = TokenService(session, redis, secret_key)
