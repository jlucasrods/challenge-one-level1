from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, backref

from app.config.database import Base, engine


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    email = Column(String(50), unique=True)
    cpf = Column(String(11), unique=True)
    pis = Column(String(11), unique=True)
    password = Column(String(255))

    addresses = relationship("Address", back_populates="user", uselist=False, cascade="all, delete")


User.metadata.create_all(bind=engine)
