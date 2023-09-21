from fastapi import APIRouter, Depends
from typing import Annotated
from fastapi.security import OAuth2PasswordRequestForm
from UniSystem.application.security import *
from UniSystem.application.exceptions.http_exceptions import *
from UniSystem.domain.security_schemas import Token


security_router = APIRouter(tags=['Security'])


@security_router.post('/token')
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    user = await authenticate_user(form_data.username, form_data.password)
    if not user:
        credentials_exeption()
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user['institutional_email']}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@security_router.get("/users/me/")
async def read_users_me(
    current_user: Annotated[User, Depends(get_current_user)]
):
    del current_user['password']
    return current_user
