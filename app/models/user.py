from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.config.db import ModelBase, engine


class UserModel(ModelBase):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    email = Column(String(50), unique=True)
    cpf = Column(String(11), unique=True)
    pis = Column(String(11), unique=True)
    password = Column(String(255))

    address = relationship('AddressModel', back_populates='user', uselist=False, cascade='all, delete-orphan')