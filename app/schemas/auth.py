from pydantic import BaseModel


class AuthRequest(BaseModel):
    login: str
    password: str


class AuthResponse(BaseModel):
    token: str