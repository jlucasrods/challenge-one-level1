from app.config.database import db
from app.config.password_security import hash_password
from app.models import user_model
from app.models.address_model import Address
from app.schemas import user_schema


def get(user_id: int):
    return db.query(user_model.User).get(user_id)


def create(user: user_schema.UserRequest) -> user_model.User:
    db_user = user_model.User(
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


def update(user_id: int, user: user_schema.UserRequest) -> user_model.User:
    db_user = db.query(user_model.User).get(user_id)
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
    db_user = db.query(user_model.User).get(user_id)
    db.delete(db_user)
    db.commit()


def get_by_login(login: str) -> user_model.User:
    return db.query(user_model.User).filter(
        user_model.User.cpf == login or
        user_model.User.pis == login or
        user_model.User.email == login
    ).first()


def get_by_cpf(cpf: str) -> user_model.User:
    return db.query(user_model.User).filter(user_model.User.cpf == cpf).first()


def get_by_pis(pis: str) -> user_model.User:
    return db.query(user_model.User).filter(user_model.User.pis == pis).first()


def get_by_email(email: str) -> user_model.User:
    return db.query(user_model.User).filter(user_model.User.email == email).first()
