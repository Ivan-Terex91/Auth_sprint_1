from datetime import datetime

from flask_restx import SchemaModel
from pydantic import UUID4, BaseModel, EmailStr, Field
from pydantic.schema import Enum


class Action(Enum):
    login = "login"
    logout = "logout"


class DeviceType(Enum):
    desktop = "desktop"
    smartphone = "smartphone"


class User(BaseModel):
    id: UUID4
    first_name: str = ""
    last_name: str = ""
    email: EmailStr
    password: str = Field(min_length=6, max_length=20)


class UserHistory(BaseModel):
    # action: Action #TODO если оставить так, то ругается swagger, не нашёл пока решения
    action: str
    datetime: datetime
    user_agent: str
    # user_device_type: DeviceType #TODO если оставить так, то ругается swagger, не нашёл пока решения
    user_device_type: str


class ChangePassword(BaseModel):
    old_password: str
    new_password: str


user_model = SchemaModel("user", schema=User.schema())
change_password_model = SchemaModel("change_password", schema=ChangePassword.schema())
user_history_model = SchemaModel("user_history", schema=UserHistory.schema())
