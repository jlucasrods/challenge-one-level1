from datetime import timedelta, datetime

from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, APIKeyCookie
import jwt
from jwt import InvalidTokenError
from sqlalchemy.orm import Session

from app.config.db import get_db
from app.config.env import AUTH_SECRET
from app.crud.user import get_by_login, get
from app.models.user import UserModel

ALGORITHM = 'HS256'
TOKEN_EXPIRE_MINUTES = 15
AUTH_COOKIE_NAME = 'session'

cookie_sec = APIKeyCookie(name=AUTH_COOKIE_NAME)


def create_token(user_id: int) -> str:
    expire = datetime.utcnow() + timedelta(minutes=TOKEN_EXPIRE_MINUTES)
    return jwt.encode({'sub': user_id, 'exp': expire}, AUTH_SECRET, algorithm=ALGORITHM)


def verify_auth(db: Session = Depends(get_db), auth: str = Depends(cookie_sec)) -> UserModel:
    unauthorized_exception = HTTPException(detail='Invalid token', status_code=401)
    try:
        payload = jwt.decode(auth, AUTH_SECRET, algorithms=[ALGORITHM])
        user_id = payload.get('sub')
    except InvalidTokenError:
        raise unauthorized_exception

    if not user_id:
        raise unauthorized_exception

    user = get(db, user_id)
    if not user:
        raise unauthorized_exception

    return user
