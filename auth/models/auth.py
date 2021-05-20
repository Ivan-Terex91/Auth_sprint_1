from flask_restx import SchemaModel
from pydantic import BaseModel, EmailStr, Field


class Signup(BaseModel):
    email: EmailStr
    password: str = Field(min_length=6, max_length=20)


class Tokens(BaseModel):
    access_token: str
    refresh_token: str


class RefreshToken(BaseModel):
    refresh_token: str


signup_model = SchemaModel("signup", schema=Signup.schema())
tokens_model = SchemaModel("tokens", schema=Tokens.schema())
refresh_token_model = SchemaModel("refresh_token", schema=RefreshToken.schema())
