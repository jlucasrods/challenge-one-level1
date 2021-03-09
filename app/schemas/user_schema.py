import re

from pydantic import BaseModel, EmailStr, validator
from validate_docbr import CPF, PIS

from app.schemas.address_schema import Address

cpf_validator = CPF()
pis_validator = PIS()


class UserBase(BaseModel):
    name: str
    email: EmailStr
    cpf: str
    pis: str
    addresses: Address

    @validator("cpf")
    def cpf_should_be_valid(cls, cpf):
        if not cpf_validator.validate(cpf):
            raise ValueError("CPF must be valid")
        return cpf

    @validator("cpf")
    def cpf_should_contain_11_numbers(cls, cpf):
        if not re.match(r"^[0-9]{11}$", cpf):
            raise ValueError("CPF must contain 11 numbers")
        return cpf

    @validator("pis")
    def pis_should_be_valid(cls, pis):
        if not pis_validator.validate(pis):
            raise ValueError("PIS must be valid")
        return pis

    @validator("pis")
    def pis_should_contain_11_numbers(cls, pis):
        if not re.match(r"^[0-9]{11}$", pis):
            raise ValueError("PIS must contain 11 numbers")
        return pis

    class Config:
        orm_mode = True


class UserRequest(UserBase):
    password: str


class UserResponse(UserBase):
    id: int
