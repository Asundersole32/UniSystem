from pydantic import BaseModel


class User(BaseModel):
    registration: str
    name: str
    institutional_email: str
    academic_type_id: str


class Token(BaseModel):
    access_token: str
    type_token:str


class TokenData(BaseModel):
    email: str | None = None
