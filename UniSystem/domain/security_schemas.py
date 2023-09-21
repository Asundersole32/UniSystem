from pydantic import BaseModel


class User(BaseModel):
    username: str
    email: str
    disabled: bool | None = None
    type: int


class Token(BaseModel):
    access_token: str
    type_token:str


class TokenData(BaseModel):
    email: str | None = None
