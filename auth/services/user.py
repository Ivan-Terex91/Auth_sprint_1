from functools import lru_cache


class UserService:
    def __init__(self, db):
        self.db = db

    def get(self, user_id):
        return {"username": "test", "id": user_id}
