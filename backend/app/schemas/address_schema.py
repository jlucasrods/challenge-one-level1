from fastapi import Form
from pydantic import BaseModel


class Address(BaseModel):
    country: str = Form(...)
    state: str = Form(...)
    city: str = Form(...)
    zip_code: str = Form(...)
    street: str = Form(...)
    number: int = Form(...)
    complement: str = Form(...)

    class Config:
        orm_mode = True
