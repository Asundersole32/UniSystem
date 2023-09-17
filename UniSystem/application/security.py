from datetime import datetime, timedelta
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from typing import Annotated
from os import getenv

from UniSystem.util.env_conection import env_connection_values


SECRET_KEY = env_connection_values('SECRET_KEY')
ALGORITH = env_connection_values('ALGORITH')

pwd_context = CryptContext(schemes=['bcrypt'], deprecated="auto")


def get_hash_password(password):
    return pwd_context.hash(password)


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_user(db, user):
    return


def authenticate_user(db_user, login_user, login_password):
    return
