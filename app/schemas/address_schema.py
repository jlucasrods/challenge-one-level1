from fastapi import Form
from pydantic import BaseModel

from app.schemas.form_body_model_util import form_body_model


@form_body_model
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
