from datetime import timedelta, datetime

from fastapi import Depends, HTTPException
from fastapi.security import APIKeyCookie
from jose import jwt, JWTError

from app.config.env import AUTH_JWT_SECRET
from app.repositories import user_repository
from app.schemas.auth_schema import AuthData

ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 30
AUTH_COOKIE_NAME = 'session'

cookie_sec = APIKeyCookie(name=AUTH_COOKIE_NAME)


def create_auth_token(login: str) -> str:
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    return jwt.encode({"sub": login, 'exp': expire}, AUTH_JWT_SECRET, algorithm=ALGORITHM)


def verify_auth(session: str = Depends(cookie_sec)) -> AuthData:
    unauthorized_exception = HTTPException(detail='Invalid token', status_code=400)
    try:
        payload = jwt.decode(session, AUTH_JWT_SECRET, algorithms=[ALGORITHM])
        login: str = payload.get('sub')
    except JWTError:
        raise unauthorized_exception

    if not login:
        raise unauthorized_exception

    user = user_repository.get_by_login(login)
    if not user:
        raise unauthorized_exception

    return AuthData(user=user, claims={'login': login})
