from typing import List
from fastapi import HTTPException, APIRouter, Response

from app.repositories import userRepository
from app.models import userModel
from app.schemas import userSchema

router = APIRouter()


@router.get("/{user_id}", response_model=userSchema.UserResponse)
def get_user(user_id: int) -> userModel.User:
    db_user = userRepository.get(user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User doesn't exist")

    return db_user


@router.post("", response_model=userSchema.UserResponse)
def create_user(user: userSchema.UserRequest) -> userModel.User:
    db_user = userRepository.get_by_cpf(cpf=user.cpf)
    if db_user:
        raise HTTPException(status_code=400, detail="CPF already registered")

    db_user = userRepository.get_by_pis(pis=user.pis)
    if db_user:
        raise HTTPException(status_code=400, detail="PIS already registered")

    db_user = userRepository.get_by_email(email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    return userRepository.create(user=user)


@router.put("/{user_id}", response_model=userSchema.UserResponse)
def update_user(user_id: int, user: userSchema.UserRequest) -> userModel.User:
    db_user = userRepository.get(user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User doesn't exist")

    db_user = userRepository.update(user_id, user)
    return db_user


@router.delete("/{user_id}")
def delete_user(user_id: int):
    db_user = userRepository.get(user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User doesn't exist")

    userRepository.delete(user_id)
    return Response(status_code=200)

