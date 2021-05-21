from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID

db = SQLAlchemy()


class User(db.Model):
    id = Column(UUID, primary_key=True)
    email = Column(String(120), unique=True, nullable=False)

    def __repr__(self):
        return "<User %r>" % self.username
