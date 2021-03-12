from fastapi.encoders import jsonable_encoder
from sqlalchemy import or_
from sqlalchemy.orm import Session

from app.config.pass_hashing import hash_password
from app.models.address import AddressModel
from app.models.user import UserModel
from app.schemas.user import UserCreate, UserUpdate


def get(db: Session, user_id: int):
    return db.query(UserModel).get(user_id)


def create(db: Session, user_create: UserCreate) -> UserModel:
    user_model = UserModel(
        name=user_create.name,
        email=user_create.email,
        cpf=user_create.cpf,
        pis=user_create.pis,
        password=hash_password(user_create.password),
        address=AddressModel(
            country=user_create.address.country,
            state=user_create.address.state,
            city=user_create.address.city,
            zip_code=user_create.address.zip_code,
            number=user_create.address.number,
            street=user_create.address.street,
            complement=user_create.address.complement
        )
    )
    db.add(user_model)
    db.commit()
    db.refresh(user_model)
    return user_model


def update(db: Session, user_model: UserModel, user_update: UserUpdate) -> UserModel:
    user_model.name = user_update.name
    user_model.email = user_update.email
    user_model.cpf = user_update.cpf
    user_model.pis = user_update.pis
    user_model.password = hash_password(user_update.newPassword if user_update.newPassword else user_update.oldPassword)
    user_model.address.country = user_update.address.country,
    user_model.address.state = user_update.address.state,
    user_model.address.city = user_update.address.city,
    user_model.address.zip_code = user_update.address.zip_code,
    user_model.address.number = user_update.address.number,
    user_model.address.street = user_update.address.street,
    user_model.address.complement = user_update.address.complement
    db.add(user_model)
    db.commit()
    db.refresh(user_model)
    return user_model


def delete(db: Session, db_obj: UserModel):
    db.delete(db_obj)
    db.commit()


def get_by_login(db: Session, login: str) -> UserModel:
    return db.query(UserModel).filter(
        or_(UserModel.cpf == login, UserModel.pis == login, UserModel.email == login)
    ).first()


def get_by_cpf(db: Session, cpf: str) -> UserModel:
    return db.query(UserModel).filter(UserModel.cpf == cpf).first()


def get_by_pis(db: Session, pis: str) -> UserModel:
    return db.query(UserModel).filter(UserModel.pis == pis).first()


def get_by_email(db: Session, email: str) -> UserModel:
    return db.query(UserModel).filter(UserModel.email == email).first()