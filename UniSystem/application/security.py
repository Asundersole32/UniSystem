from datetime import datetime, timedelta
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from typing import Annotated
from os import getenv

from UniSystem.util.env_conection import env_connection_values
from UniSystem.infra.querys.consult import *
from UniSystem.application.exceptions.http_exceptions import *
from UniSystem.domain.security_schemas import *


SECRET_KEY = env_connection_values('SECRET_KEY')
ALGORITH = env_connection_values('ALGORITH')
ACCESS_TOKEN_EXPIRE_MINUTES = int(env_connection_values('ACCESS_TOKEN_EXPIRE_MINUTES'))

oauth2_context = OAuth2PasswordBearer(tokenUrl='token')

pwd_context = CryptContext(schemes=['bcrypt'], deprecated="auto")


def get_hash_password(password):
    return pwd_context.hash(password)


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


async def get_user(user_email):
    try:
        user = await find_academic(user_email)
        return user
    except Exception as e:
        bad_request(e)


async def authenticate_user(login_user, login_password):
    user = await get_user(login_user)
    if not verify_password(login_password, user['password']):
        return False
    return user


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({'exp': expire})
    encode_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITH)
    return encode_jwt


async def get_current_user(token: Annotated[str, Depends(oauth2_context)]):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITH])
        user_email: str = payload.get('sub')
        print(user_email)
        if user_email is None:
            credentials_exeption()
        token_data = TokenData(email=user_email)
    except JWTError:
        credentials_exeption()
    user = await get_user(user_email=token_data.email)
    if user is None:
        credentials_exeption()
    return user
