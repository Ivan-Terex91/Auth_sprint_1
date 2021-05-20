class TokenService:
    def __init__(self, db):
        self.db = db

    def get(self):
        return {"access_token": "access_token", "refresh_token": "refresh_token"}
