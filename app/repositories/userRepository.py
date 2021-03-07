from typing import List

from app.config.password_hasher import hash_password
from app.models import userModel
from app.models.addressModel import Address
from app.schemas import userSchema
from app.config.database import db


def get(user_id: int):
    return db.query(userModel.User).get(user_id)


def create(user: userSchema.UserRequest) -> userModel.User:
    db_user = userModel.User(
        name=user.name,
        email=user.email,
        cpf=user.cpf,
        pis=user.pis,
        password=hash_password(user.password),
        addresses=Address(
            country=user.addresses.country,
            state=user.addresses.state,
            city=user.addresses.city,
            street=user.addresses.street,
            zip_code=user.addresses.zip_code,
            number=user.addresses.number,
            complement=user.addresses.complement
        )
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def update(user_id: int, user: userSchema.UserRequest) -> userModel.User:
    db_user = db.query(userModel.User).get(user_id)
    db_user.name = user.name
    db_user.email = user.email
    db_user.cpf = user.cpf
    db_user.pis = user.pis
    db_user.password = hash_password(user.password)
    db_user.addresses = Address(
        country=user.addresses.country,
        state=user.addresses.state,
        city=user.addresses.city,
        street=user.addresses.street,
        zip_code=user.addresses.zip_code,
        number=user.addresses.number,
        complement=user.addresses.complement
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def delete(user_id: int):
    db_user = db.query(userModel.User).get(user_id)
    db.delete(db_user)
    db.commit()


def get_by_login(login: str) -> userModel.User:
    return db.query(userModel.User).filter(
        userModel.User.cpf == login or
        userModel.User.pis == login or
        userModel.User.email == login
    ).first()


def get_by_cpf(cpf: str) -> userModel.User:
    return db.query(userModel.User).filter(userModel.User.cpf == cpf).first()


def get_by_pis(pis: str) -> userModel.User:
    return db.query(userModel.User).filter(userModel.User.pis == pis).first()


def get_by_email(email: str) -> userModel.User:
    return db.query(userModel.User).filter(userModel.User.email == email).first()
