from pydantic.schema import Enum


class Action(Enum):
    login = "login"
    logout = "logout"


class DeviceType(Enum):
    desktop = "desktop"
    smartphone = "smartphone"
