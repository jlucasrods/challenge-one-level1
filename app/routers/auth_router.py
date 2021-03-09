from fastapi import APIRouter, HTTPException
from starlette.responses import Response, RedirectResponse

from app.config.auth_security import create_auth_token, AUTH_COOKIE_NAME
from app.config.password_security import verify_password
from app.repositories import user_repository
from app.schemas.auth_schema import AuthCredentials

router = APIRouter()


@router.post('/login')
def login(auth_credentials: AuthCredentials, response: Response):
    db_user = user_repository.get_by_login(auth_credentials.login)

    if not db_user or not verify_password(auth_credentials.password, db_user.password):
        raise HTTPException(status_code=401, detail='Invalid credentials')

    token = create_auth_token(auth_credentials.login)
    response.set_cookie(AUTH_COOKIE_NAME, token)
    response.status_code = 200
    return response


@router.get('/logout')
def logout(response: Response):
    response.delete_cookie(AUTH_COOKIE_NAME)
    response.status_code = 200
    return response
