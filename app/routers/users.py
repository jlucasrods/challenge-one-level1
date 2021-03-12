from fastapi import HTTPException, APIRouter, Response, Depends

from app.config.auth import verify_auth
from app.config.db import get_db
from app.config.pass_hashing import verify_password
from app.crud.user import get_by_cpf, get_by_pis, get_by_email, create, update, delete
from app.models.user import UserModel
from app.schemas.user import UserResponse, UserCreate, UserUpdate

router = APIRouter()


@router.get('/me', response_model=UserResponse)
def get_user(user_auth: UserModel = Depends(verify_auth)):
    """Get the authorized user."""
    return user_auth


@router.post('', response_model=UserResponse)
def create_user(user_create: UserCreate, db=Depends(get_db)):
    """Register a new user. Email, CPF and PIS must be valid and not yet registered."""
    db_user = get_by_cpf(db, user_create.cpf)
    if db_user:
        raise HTTPException(status_code=400, detail="CPF already registered")

    db_user = get_by_pis(db, user_create.pis)
    if db_user:
        raise HTTPException(status_code=400, detail="PIS already registered")

    db_user = get_by_email(db, user_create.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    return create(db, user_create)


@router.put('/me', response_model=UserResponse)
def update_user(user_update: UserUpdate, user_auth: UserModel = Depends(verify_auth), db=Depends(get_db)):
    """Update the authorized user."""
    if not verify_password(user_update.oldPassword, user_auth.password):
        raise HTTPException(status_code=400, detail='Invalid password. Try again.')

    return update(db, user_auth, user_update)


@router.delete('/me', status_code=200)
def delete_user(user_auth: UserModel = Depends(verify_auth), db=Depends(get_db)):
    """Delete the authorized user."""
    delete(db, user_auth)
