import uuid

from core.db import db
from models.users import Action, DeviceType
from sqlalchemy.dialects.postgresql import ENUM as pgEnum
from sqlalchemy.dialects.postgresql import UUID


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        unique=True,
        nullable=False,
    )
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f"<User {self.first_name} - {self.last_name}>"


class History(db.Model):
    __tablename__ = "history"

    user_id = db.Column(UUID(as_uuid=True), db.ForeignKey("users.id"))
    action = db.Column(pgEnum(Action), nullable=False)
    datetime: db.Column(db.DateTime, nullable=False)
    user_agent: db.Column(db.String, nullable=False)
    user_device_type: db.Column(pgEnum(DeviceType), nullable=False)

    def __repr__(self):
        return f"{self.user_id} - {self.action} - {self.datetime}"
