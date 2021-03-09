from fastapi import HTTPException, APIRouter, Response, Depends

from app.config.auth_security import verify_auth
from app.repositories import user_repository
from app.models import user_model
from app.schemas import user_schema
from app.schemas.auth_schema import AuthData

router = APIRouter()


@router.get('/me', response_model=user_schema.UserResponse)
def get_user(auth_data: AuthData = Depends(verify_auth)) -> user_model.User:
    return auth_data.user


@router.post('', response_model=user_schema.UserResponse)
def create_user(user: user_schema.UserRequest) -> user_model.User:
    db_user = user_repository.get_by_cpf(cpf=user.cpf)
    if db_user:
        raise HTTPException(status_code=400, detail="CPF already registered")

    db_user = user_repository.get_by_pis(pis=user.pis)
    if db_user:
        raise HTTPException(status_code=400, detail="PIS already registered")

    db_user = user_repository.get_by_email(email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    return user_repository.create(user=user)


@router.put('/me', response_model=user_schema.UserResponse)
def update_user(user: user_schema.UserRequest, auth_data: AuthData = Depends(verify_auth)) -> user_model.User:
    return user_repository.update(auth_data.user.id, user)


@router.delete('/me', status_code=200)
def delete_user(auth_data: AuthData = Depends(verify_auth)):
    user_repository.delete(auth_data.user.id)
