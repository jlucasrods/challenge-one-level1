from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.config.database import Base, engine


class Address(Base):
    __tablename__ = "addresses"

    id = Column(Integer, primary_key=True, index=True)
    country = Column(String(30))
    state = Column(String(30))
    city = Column(String(30))
    zip_code = Column(String(10))
    street = Column(String(50))
    number = Column(Integer)
    complement = Column(String(20))
    user_id = Column(Integer, ForeignKey("users.id"))

    user = relationship("User", back_populates="addresses")


Address.metadata.create_all(bind=engine)
