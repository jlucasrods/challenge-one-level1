from typing import Optional

from fastapi import Form
from pydantic import BaseModel

from app.models.user_model import User


class AuthCredentials(BaseModel):
    login: str = Form(...)
    password: str = Form(...)


class AuthToken(BaseModel):
    token: str


class AuthData(BaseModel):
    claims: Optional[dict] = None
    user: User

    class Config:
        arbitrary_types_allowed = True
