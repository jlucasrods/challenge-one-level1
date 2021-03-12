import re
from typing import Optional

from pydantic import BaseModel, EmailStr, validator
from validate_docbr import CPF, PIS

from app.schemas.address import Address

cpf_validator = CPF()
pis_validator = PIS()


class UserBase(BaseModel):
    name: str
    email: EmailStr
    cpf: str
    pis: str
    address: Address

    @validator("cpf")
    def cpf_should_be_valid(cls, cpf):
        if not cpf_validator.validate(cpf):
            raise ValueError("CPF must be valid")
        return cpf

    @validator("cpf")
    def cpf_should_contain_11_numbers(cls, cpf):
        clean_cpf = re.sub("[^0-9]", "", cpf)
        if len(clean_cpf) != 11:
            raise ValueError("CPF must contain 11 numbers")
        return clean_cpf

    @validator("pis")
    def pis_should_be_valid(cls, pis):
        if not pis_validator.validate(pis):
            raise ValueError("PIS must be valid")
        return pis

    @validator("pis")
    def pis_should_contain_11_numbers(cls, pis):
        clean_pis = re.sub("[^0-9]", "", pis)
        if len(clean_pis) != 11:
            raise ValueError("PIS must contain 11 numbers")
        return clean_pis

    class Config:
        orm_mode = True


class UserCreate(UserBase):
    password: str


class UserUpdate(UserBase):
    oldPassword: str
    newPassword: Optional[str] = None


class UserResponse(UserBase):
    id: int