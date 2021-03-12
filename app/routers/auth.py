from fastapi import APIRouter, HTTPException, Depends
from starlette.responses import Response

from app.config.auth import create_token, AUTH_COOKIE_NAME
from app.config.db import get_db
from app.config.pass_hashing import verify_password
from app.crud.user import get_by_login
from app.schemas.auth import AuthRequest, AuthResponse

router = APIRouter()


@router.post('/login')
def login(credentials: AuthRequest, response: Response, db=Depends(get_db)):
    user = get_by_login(db, credentials.login)

    if not user or not verify_password(credentials.password, user.password):
        raise HTTPException(status_code=401, detail='Invalid credentials')

    token = create_token(user.id)
    response.set_cookie(AUTH_COOKIE_NAME, token)
    response.status_code = 200
    return response


@router.get('/logout')
def logout(response: Response):
    response.delete_cookie(AUTH_COOKIE_NAME)
    response.status_code = 200
    return response
