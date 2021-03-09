from datetime import timedelta, datetime

from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
import jwt
from jwt import DecodeError

from app.config.env import AUTH_JWT_SECRET
from app.repositories import user_repository
from app.schemas.auth_schema import AuthData, AuthToken

ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 30
AUTH_COOKIE_NAME = 'session'

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def create_auth_token(login: str) -> AuthToken:
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    token = jwt.encode({'sub': login, 'exp': expire}, AUTH_JWT_SECRET, algorithm=ALGORITHM)
    return AuthToken(token=token)


def verify_auth(token: str = Depends(oauth2_scheme)) -> AuthData:
    credentials_exception = HTTPException(
        status_code=401,
        detail="Invalid credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, AUTH_JWT_SECRET, algorithms=[ALGORITHM])
        login: str = payload.get('sub')
        if not login:
            raise credentials_exception
    except DecodeError:
        raise credentials_exception

    user = user_repository.get_by_login(login)
    if not user:
        raise credentials_exception

    return AuthData(user=user, claims={'login': login})
