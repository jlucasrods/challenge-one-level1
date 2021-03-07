from pydantic import BaseModel


class Address(BaseModel):
    country: str
    state: str
    city: str
    zip_code: str
    street: str
    number: int
    complement: str

    class Config:
        orm_mode = True
