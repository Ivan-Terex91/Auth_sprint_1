import uuid
from datetime import timezone

from sqlalchemy import Column, DateTime, ForeignKey, String, create_engine
from sqlalchemy.dialects.postgresql import ENUM, UUID
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

from core.enums import Action, DeviceType

session = scoped_session(sessionmaker(autocommit=False, autoflush=False))

Base = declarative_base()


class User(Base):
    __tablename__ = "user"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        unique=True,
        nullable=False,
    )
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)

    def __repr__(self):
        return f"<User {self.first_name} - {self.last_name}>"


class RefreshToken(Base):
    __tablename__ = "refresh_token"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        unique=True,
        nullable=False,
    )
    user_id = Column(UUID(as_uuid=True), ForeignKey("user.id", ondelete="CASCADE"))
    token = Column(String, index=True, nullable=False)
    access_token = Column(String, index=True, nullable=False)
    exp = Column(DateTime, nullable=False)


class History(Base):
    __tablename__ = "history"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        unique=True,
        nullable=False,
    )
    user_id = Column(UUID(as_uuid=True), ForeignKey("user.id"))
    action = Column(ENUM(Action), nullable=False)
    datetime = Column(DateTime, nullable=False)
    user_agent = Column(String, nullable=False)
    user_device_type = Column(ENUM(DeviceType), nullable=False)

    def __repr__(self):
        return f"{self.user_id} - {self.action} - {self.datetime}"


def init_session(dsn):
    engine = create_engine(dsn)
    session.configure(bind=engine)
    Base.metadata.create_all(engine)
    return session
