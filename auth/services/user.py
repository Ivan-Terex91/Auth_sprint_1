from functools import lru_cache


class UserService:
    def __init__(self, db):
        self.db = db

    def get(self, user_id):
        return {
            "id": user_id,
            "first_name": "",
            "last_name": "",
            "email": "user@example.com",
            "password": "string",
        }

    def put(self, user_id):
        return "successfully updated user profile"

    def delete(self, user_id):
        return "successfully deleted user profile"


class UserHistoryService:
    def __init__(self, db):
        self.db = db

    def get(self, user_id):
        return {
            "action": "string",
            "datetime": "2021-05-20T10:57:06.441Z",
            "user_agent": "string",
            "user_device_type": "string",
        }


class ChangePasswordService:
    def __init__(self, db):
        self.db = db

    def patch(self, user_id, old_password, new_password):
        return "successfully change password"
