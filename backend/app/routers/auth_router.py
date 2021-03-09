from fastapi import APIRouter, HTTPException

from app.config.auth_security import create_auth_token
from app.config.password_security import verify_password
from app.repositories import user_repository
from app.schemas.auth_schema import AuthCredentials

router = APIRouter()


@router.post('')
def login(auth_credentials: AuthCredentials):
    db_user = user_repository.get_by_login(auth_credentials.login)
    if not db_user or not verify_password(auth_credentials.password, db_user.password):
        raise HTTPException(status_code=401, detail='Invalid credentials')

    return create_auth_token(auth_credentials.login)
